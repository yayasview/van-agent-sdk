---
name: linkedin-connection-checker
description: >
  Check LinkedIn connection status for ABM contacts marked as "Pending" in
  HubSpot and update records when connections are confirmed. Uses a two-step
  HubSpot query (companies with abm_tier → associated contacts with Pending
  status) and browser navigation (Claude in Chrome) to verify LinkedIn
  connections.
  Trigger phrases: "check connections", "check LinkedIn status",
  "check-connect", "verify LinkedIn connections"
---

# LinkedIn Connection Checker

## Dependencies
- HubSpot MCP connection (required)
- Browser access via Claude in Chrome extension or computer use (required)
- LinkedIn account must be logged in and active in the browser

## Inputs
- No inputs required — the skill uses a two-step HubSpot query with hardcoded filters
- Dry run flag (optional) — if set, report results without updating HubSpot

## Workflow

### Step 1 — Fetch pending ABM contacts from HubSpot

The HubSpot search API can't filter contacts by an associated company's property directly. So this requires a two-step query:

#### Step 1a — Get all ABM company IDs

```
objectType: "companies"
filterGroups: [
  {
    "filters": [
      { "propertyName": "abm_tier", "operator": "HAS_PROPERTY" }
    ]
  }
]
properties: ["name", "abm_tier"]
limit: 200
```

Collect all company IDs from the results. Handle pagination if `total` > page size.

#### Step 1b — Get pending contacts associated with those companies

```
objectType: "contacts"
filterGroups: [
  {
    "filters": [
      { "propertyName": "linkedin_connection_status", "operator": "EQ", "value": "Pending" }
    ],
    "associatedWith": [
      { "objectType": "companies", "operator": "IN", "objectIds": ["<all company IDs from Step 1a>"] }
    ]
  }
]
properties: ["firstname", "lastname", "email", "company", "linkedin_profile_url", "linkedin_connection_status", "jobtitle"]
limit: 200
```

**Important details:**
- The `linkedin_connection_status` enum value is `"Pending"` (capital P) — HubSpot is case-sensitive on enum values
- LinkedIn URLs are stored in `linkedin_profile_url` (NOT `hs_linkedin_url`)
- The `associatedWith` IN operator accepts all company IDs in a single array

After fetching:
1. Handle pagination — if `total` exceeds the page size, fetch subsequent pages using `offset`.
2. Filter out contacts that have no `linkedin_profile_url` — flag these in the final report as "Missing LinkedIn URL".
3. Log the total count: contacts found, contacts to check, contacts with missing URLs.

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

1. Use the HubSpot MCP to update the contact's `linkedin_connection_status` property to `Connected` (capital C — matches HubSpot enum).
2. Log each successful update.
3. If an update fails, record the failure and continue with the remaining contacts.

**Only update contacts that are newly confirmed as `connected`.** Do not overwrite other statuses — the report handles those.

### Step 4 — Generate and deliver the report

Produce a structured report with the following sections:

## Output Format

```
LinkedIn Connection Check Report
================================
Filter: ABM company (abm_tier is known) + LinkedIn Connection Status = "Pending"
Date: [YYYY-MM-DD]
Total contacts matched: [N]
Contacts checked: [N]
Contacts skipped (no LinkedIn URL): [N]

NEWLY CONNECTED (updated in HubSpot)
-------------------------------------
| # | Name            | Company    | Title                      | Updated |
|---|-----------------|------------|----------------------------|---------|
| 1 | Jane Smith      | Acme Corp  | VP Marketing               | Yes     |

PENDING (request sent, not yet accepted)
-----------------------------------------
| # | Name            | Company    | Title                      |
|---|-----------------|------------|----------------------------|
| 1 | Sarah Chen      | FooCo      | Head of Growth             |

NOT CONNECTED (no request sent)
--------------------------------
| # | Name            | Company    | Title                      |
|---|-----------------|------------|----------------------------|
| 1 | Tom Williams    | BarInc     | Director Marketing         |

ISSUES
-------
| # | Name            | Issue                                 |
|---|-----------------|---------------------------------------|
| 1 | Alex Brown      | Missing LinkedIn URL                  |
| 2 | Pat Davis       | URL invalid — profile not found       |
| 3 | Chris Lee       | Check failed — page did not load      |

Summary: [X] connections confirmed and updated. [Y] still pending. [Z] issues flagged.
```

### Step 5 — Post report to Slack

After generating the report, send it directly to `#van-growth` (channel ID: `C0ABDUL07BM`) via the Slack MCP (`slack_send_message`).

**Formatting rules for Slack:**
- Use Slack markdown: `*bold*` (single asterisks), `_italic_`, `` `code` ``
- Tables are supported — keep the same format as the report above
- Slack message limit is 5,000 characters for text. If the report exceeds this, split into two messages: (1) summary + newly connected, (2) pending + issues.
- No need for user review — send directly.

## Quality Checks
- Never update a contact's status to anything other than `Connected` — other statuses are informational only
- Always confirm LinkedIn login status before starting the batch
- If more than 25% of checks fail due to page load errors, stop and alert the user — there may be a LinkedIn rate limit or session issue
- The report must account for every contact returned by the filter — no contact should be silently dropped
- If the `linkedin_connection_status` property doesn't exist in HubSpot, alert the user and provide instructions to create it

## HubSpot Property Reference

This skill depends on these HubSpot properties:

| Object | Property | Internal Name | Type | Values |
|--------|----------|--------------|------|--------|
| Company | ABM Tier | `abm_tier` | String | Tier 1, Tier 2, Tier 3 |
| Contact | LinkedIn Connection Status | `linkedin_connection_status` | Enumeration | `Connected`, `Pending`, `Not Connected`, `Rejected` |
| Contact | LinkedIn Profile URL | `linkedin_profile_url` | String | Full LinkedIn URL |

## Claude Code / Claude Cowork Usage

This skill is designed to run in two environments:

**Claude Code (CLI):**
- Requires Claude in Chrome MCP or computer use to navigate LinkedIn.
- Run with: `/check-connect`
- The agent will query HubSpot for pending ABM contacts, check each via browser, update HubSpot, and deliver a report.

**Claude Cowork (browser-native):**
- The Claude in Chrome extension handles browser navigation directly.
- The agent opens LinkedIn tabs, reads the DOM for connection indicators, and proceeds through the list.
- Particularly well-suited since the browser session is already active with LinkedIn credentials.

## Examples
See `examples/` folder.
