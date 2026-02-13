---
name: update-deal
description: Takes call notes, email threads, meeting summaries, or Slack recaps
  and produces a structured HubSpot deal record update. Trigger phrases include
  "update the deal", "log these notes", "here's what happened on the call",
  "update HubSpot", "deal update for [company]".
---

# Update Deal

## Purpose

After every sales interaction — call, email exchange, meeting, or async update — the deal record in HubSpot needs to reflect what happened, what changed, and what's next. This skill takes raw, unstructured notes and transforms them into a clean, structured deal update ready for HubSpot.

## Inputs

**Required:**
- Raw interaction notes (call transcript, email thread, meeting notes, or Slack summary)
- Company or deal name (to identify which HubSpot record to update)

**Optional:**
- Current deal stage (if not provided, pull from HubSpot)
- Contact names mentioned (if not provided, infer from notes)
- Date of interaction (if not provided, assume today)

## Workflow

1. **Parse the raw input.** Identify:
   - Who was on the call/in the exchange (names, titles, roles)
   - Key topics discussed
   - Decisions made or commitments given
   - Objections raised
   - Next steps agreed upon
   - Timeline references
   - Budget or pricing discussions
   - Competitive mentions
   - Any red flags or deal risks

2. **Map to HubSpot deal fields.** Structure the parsed information into:

   | Field | Description | Source |
   |-------|-------------|--------|
   | `deal_name` | Company — Engagement Type | Existing or inferred |
   | `deal_stage` | Current stage (do NOT change unless explicitly instructed) | Existing |
   | `amount` | Deal value if discussed | From notes |
   | `close_date` | Expected close if mentioned | From notes |
   | `next_step` | The single most important next action | Parsed from discussion |
   | `next_step_date` | When the next step should happen | From notes or inferred |
   | `last_activity_date` | Date of this interaction | Provided or today |
   | `notes` | Structured summary (see Output Format below) | Parsed |
   | `contacts_involved` | Names and roles from the interaction | Parsed |

3. **Check for gaps.** If critical fields are missing or contradictory:
   - Flag them explicitly: "⚠️ No close date discussed — should I estimate based on the timeline they mentioned?"
   - Do NOT fill in guesses silently. Surface the gap so the team can decide.

4. **Format the update.** Use the Output Format below.

5. **Present for approval.** Post the formatted update in Slack and explicitly ask: "Ready to push this to HubSpot?" Do NOT write to HubSpot until confirmed.

6. **On approval, push to HubSpot** via the HubSpot MCP connection. Confirm success or report any errors.

## Output Format

```
## Deal Update: [Company Name]
**Date:** [interaction date]
**Interaction:** [Call / Email / Meeting / Async]
**Participants:** [names and titles]

### Summary
[2-3 sentence summary of what happened and what matters]

### Key Details
- **Decision(s):** [any decisions made]
- **Objections/Concerns:** [what they pushed back on, or "None raised"]
- **Budget/Pricing:** [any financial discussion, or "Not discussed"]
- **Timeline:** [any dates or urgency signals, or "No timeline established"]
- **Competition:** [any competitive mentions, or "None mentioned"]

### Next Steps
1. [Most important next action] — **Owner:** [who] — **By:** [when]
2. [Second action if applicable]

### Risk Flags
- [Any red flags, stalled signals, or concerns. "None identified" if clean.]

### HubSpot Field Updates
| Field | Current Value | New Value |
|-------|--------------|-----------|
| [field] | [old] | [new] |
```

## Quality Checks

- [ ] Every next step has an owner and a date
- [ ] Deal stage was NOT changed unless the team explicitly said to change it
- [ ] No information was fabricated — everything traces back to the input notes
- [ ] Gaps and uncertainties are flagged, not filled with assumptions
- [ ] The summary is useful in 10 seconds — a busy AE should be able to scan it and know what matters
- [ ] Contact names match existing HubSpot records (flag new contacts that need to be created)

## Edge Cases

- **Vague notes:** If the input is "good call with Hiya, moving forward" — don't guess. Respond: "These notes are too light for a proper update. Can you give me: who was on the call, what you discussed, and what the next step is?"
- **Multiple deals for one company:** Ask which deal to update. Don't assume.
- **Conflicting information:** If notes contradict what's in HubSpot (e.g., notes say $150K but HubSpot shows $200K), flag both values and ask which is correct.
- **Deal stage change implied but not stated:** If the notes strongly imply a stage change (e.g., "they asked us to send a proposal"), flag it as a suggestion: "This sounds like it should move to Proposal stage — confirm?" Do NOT move it automatically.

## Examples

See `examples/` folder:
- `input-call-transcript.md` — Sample call notes input
- `output-deal-update.md` — Expected structured output
