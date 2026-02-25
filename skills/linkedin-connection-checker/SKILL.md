---
name: linkedin-connection-checker
description: >
  Check LinkedIn connection status for contacts in a HubSpot list and update
  HubSpot records accordingly. Uses HubSpot MCP for contact data and browser
  navigation (Claude in Chrome / computer use) to verify LinkedIn connections.
  Trigger phrases: "check connections", "check LinkedIn status",
  "check-connect [URL]", "verify LinkedIn connections for [list]"
---

# LinkedIn Connection Checker

## Dependencies
- HubSpot MCP connection (required)
- Browser access via Claude in Chrome extension or computer use (required)
- LinkedIn account must be logged in and active in the browser

## Inputs
- HubSpot list or segment URL (required) — e.g. `https://app.hubspot.com/contacts/<portalId>/lists/<listId>`
- Dry run flag (optional) — if set, report results without updating HubSpot

## Workflow

### Step 1 — Parse the HubSpot URL and extract the list

1. Extract the **list ID** (and portal ID if present) from the provided HubSpot URL.
   - Expected URL patterns:
     - `https://app.hubspot.com/contacts/<portalId>/lists/<listId>`
     - `https://app.hubspot.com/contacts/<portalId>/objects/0-1/views/<viewId>`
   - If the URL doesn't match a recognized pattern, ask the user to confirm the list ID.
2. Use the HubSpot MCP to retrieve all contacts in the list.
   - Fetch the following properties for each contact:
     - `firstname`
     - `lastname`
     - `email`
     - `hs_linkedin_url` (or the custom property storing the LinkedIn profile URL)
     - `linkedin_connection_status` (the custom property to be updated)
   - Handle pagination — fetch all contacts, not just the first page.
3. Filter out contacts that:
   - Have no LinkedIn profile URL (flag these in the final report as "Missing LinkedIn URL")
   - Already have `linkedin_connection_status` set to `connected` (skip these — already confirmed)
4. Log the total count: contacts found, contacts to check, contacts skipped.

### Step 2 — Check LinkedIn connection status via browser

For each contact with a LinkedIn profile URL to check:

1. **Navigate** to the contact's LinkedIn profile URL in the browser.
2. **Wait** for the profile page to fully load (look for the profile header/name to appear).
3. **Identify the connection status** using the JavaScript detection below. This must be run via `mcp__claude-in-chrome__javascript_tool` on each profile page.

#### Detection Script

**IMPORTANT:** LinkedIn Premium / Sales Navigator accounts show an InMail "Message" link on ALL profiles regardless of connection status. Do NOT use the presence of a `messaging/compose` link as a connection indicator — it produces 100% false positives. The "Connect" button is also frequently hidden inside the "More" dropdown rather than shown as a primary action.

```js
(async () => {
  const mainSection = document.querySelector('main');
  if (!mainSection) return JSON.stringify({ status: 'check_failed', reason: 'no main section' });

  const title = document.title;
  const mainText = mainSection.innerText;

  // 1. Profile not found
  const notFound = mainText.includes("page doesn't exist") ||
                   mainText.includes('Profile not found');
  if (notFound) return JSON.stringify({ title, status: 'url_invalid' });

  // 2. Connected — "1st" degree badge in profile header section
  const profileSection = mainSection.querySelector('section');
  const profileHeaderText = profileSection ? profileSection.innerText : '';
  const has1stDegree = profileHeaderText.includes('1st');
  if (has1stDegree) return JSON.stringify({ title, status: 'connected', has1stDegree: true });

  // 3. Pending — check visible elements first
  let hasPending = !!Array.from(mainSection.querySelectorAll('button, span, div'))
    .find(el => el.textContent.trim() === 'Pending');

  // 4. Pending — if not visible, check inside the "More" dropdown
  //    LinkedIn hides "Pending" in the More menu on some profiles (especially with Sales Navigator)
  if (!hasPending && profileSection) {
    const moreBtn = profileSection.querySelector('button[aria-label="More"]');
    if (moreBtn) {
      moreBtn.click();
      await new Promise(r => setTimeout(r, 500));
      const menuItems = document.querySelectorAll('[role="menuitem"]');
      hasPending = !!Array.from(menuItems).find(el => el.textContent.trim() === 'Pending');
      document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    }
  }

  if (hasPending) return JSON.stringify({ title, status: 'pending', pendingInDropdown: true });

  // 5. Not connected — visible "Connect" button
  const hasConnect = !!Array.from(mainSection.querySelectorAll('button'))
    .find(b => b.textContent.trim() === 'Connect');

  // 6. Follow only — profile has connections turned off
  const hasFollow = !!Array.from(mainSection.querySelectorAll('button'))
    .find(b => b.textContent.trim() === 'Follow');

  let status;
  if (hasConnect) status = 'not_connected';
  else if (hasFollow) status = 'follow_only';
  else status = 'check_failed';

  return JSON.stringify({ title, status, hasConnect, hasFollow });
})()
```

#### Detection Priority Order

| Priority | Check | Status | How |
|----------|-------|--------|-----|
| 1 | Profile not found | `url_invalid` | Page text contains "page doesn't exist" or "Profile not found" |
| 2 | 1st degree badge | `connected` | First `<section>` in `<main>` contains text "1st" |
| 3 | Pending (visible) | `pending` | Any `button`, `span`, or `div` in `<main>` with exact text "Pending" |
| 4 | Pending (dropdown) | `pending` | Click `button[aria-label="More"]` in profile section, check `[role="menuitem"]` for "Pending" |
| 5 | Connect button | `not_connected` | Any `button` in `<main>` with exact text "Connect" |
| 6 | Follow button | `follow_only` | Any `button` in `<main>` with exact text "Follow" |
| 7 | None matched | `check_failed` | Fallback — page loaded but no indicators found |

#### Key Rules
- **Scope all queries to `document.querySelector('main')`** — avoids false positives from nav bar elements
- **Never use `a[href*="messaging/compose"]`** — matches InMail on every profile with Premium/Sales Navigator
- **Always check the "More" dropdown** — LinkedIn hides "Pending" there on ~25% of profiles
- **The "Connect" button may also be in the dropdown** — but if "Pending" is also there, "Pending" takes priority

4. **Record the result** for each contact:
   - Contact name
   - LinkedIn URL
   - Detected status
   - Timestamp of check

#### Browser Navigation Rules
- **Rate limiting:** Wait 3-5 seconds between each profile visit to avoid LinkedIn rate limits.
- **Session check:** Before starting the batch, navigate to `linkedin.com` and confirm you are logged in. If not logged in, stop and ask the user to log in.
- **Error handling:** If a profile page fails to load or shows an error, mark as `check_failed` and move on. Do not retry more than once per profile.
- **Batch size:** If the list has more than 50 contacts, process in batches of 50 and provide a progress update between batches.

### Step 3 — Update HubSpot records

For contacts whose status was detected as `connected`:

1. Use the HubSpot MCP to update the contact's `linkedin_connection_status` property to `connected`.
2. Log each successful update.
3. If an update fails, record the failure and continue with the remaining contacts.

**Only update contacts that are newly confirmed as `connected`.** Do not overwrite other statuses — the report handles those.

### Step 4 — Generate and deliver the report

Produce a structured report with the following sections:

## Output Format

```
LinkedIn Connection Check Report
================================
List: [List Name / ID]
Date: [YYYY-MM-DD]
Total contacts in list: [N]
Contacts checked: [N]
Contacts skipped (already connected): [N]
Contacts skipped (no LinkedIn URL): [N]

NEWLY CONNECTED (updated in HubSpot)
-------------------------------------
| # | Name            | LinkedIn URL                          | Updated |
|---|-----------------|---------------------------------------|---------|
| 1 | Jane Smith      | linkedin.com/in/janesmith             | Yes     |
| 2 | Mike Johnson    | linkedin.com/in/mikejohnson           | Yes     |

PENDING (request sent, not yet accepted)
-----------------------------------------
| # | Name            | LinkedIn URL                          |
|---|-----------------|---------------------------------------|
| 1 | Sarah Chen      | linkedin.com/in/sarachen              |

NOT CONNECTED (no request sent)
--------------------------------
| # | Name            | LinkedIn URL                          |
|---|-----------------|---------------------------------------|
| 1 | Tom Williams    | linkedin.com/in/tomwilliams           |

ISSUES
-------
| # | Name            | Issue                                 |
|---|-----------------|---------------------------------------|
| 1 | Alex Brown      | Missing LinkedIn URL                  |
| 2 | Pat Davis       | URL invalid — profile not found       |
| 3 | Chris Lee       | Check failed — page did not load      |

Summary: [X] connections confirmed and updated. [Y] still pending. [Z] issues flagged.
```

## Quality Checks
- Never update a contact's status to anything other than `connected` — other statuses are informational only
- Always confirm LinkedIn login status before starting the batch
- If more than 25% of checks fail due to page load errors, stop and alert the user — there may be a LinkedIn rate limit or session issue
- The report must account for every contact in the list — no contact should be silently dropped
- If the `linkedin_connection_status` property doesn't exist in HubSpot, alert the user and provide instructions to create it as a single-line text property on the Contact object

## HubSpot Property Setup

This skill requires a custom contact property in HubSpot:

| Property | Internal Name | Type | Field Type | Options |
|----------|--------------|------|------------|---------|
| LinkedIn Connection Status | `linkedin_connection_status` | Enumeration | Radio select | `connected`, `pending`, `not_connected`, `follow_only`, `url_invalid` |

Create this under Settings > Properties > Contact Properties if it doesn't already exist.

## Claude Code / Claude Cowork Usage

This skill is designed to run in two environments:

**Claude Code (CLI):**
- Requires computer use or a browser MCP tool to navigate LinkedIn.
- Run with: `/check-connect [HubSpot list URL]`
- The agent will handle browser navigation, status detection, and HubSpot updates in sequence.

**Claude Cowork (browser-native):**
- The Claude in Chrome extension handles browser navigation directly.
- The agent opens LinkedIn tabs, reads the DOM for connection indicators, and proceeds through the list.
- Particularly well-suited since the browser session is already active with LinkedIn credentials.

## Examples
See `examples/` folder.
