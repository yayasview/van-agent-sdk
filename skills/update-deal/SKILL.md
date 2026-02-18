---
name: update-deal
description: >
  Update a HubSpot deal record from call notes, email threads, or meeting transcripts.
  Trigger phrases: "update the deal", "log this call", "update HubSpot",
  "update [company] deal", "log meeting notes for [company]"
---

# Update Deal

## Dependencies
- HubSpot MCP connection (required)

## Inputs
- Call notes, email thread, or meeting transcript (required)
- Company name or deal name (required — used to find the correct HubSpot record)
- Deal stage change (optional — if the call resulted in stage progression)

## Workflow
1. Parse the call notes/email/transcript for key information:
   - Attendees and their roles
   - Topics discussed
   - Decisions made
   - Next steps and action items
   - Objections raised
   - Budget/timeline signals
   - Deal stage indicators
2. Find the matching deal in HubSpot by company name or deal name
3. Update the following HubSpot properties:
   - Last activity date
   - Notes/description (append, don't overwrite)
   - Deal stage (if progression was indicated)
   - Next step
   - Amount (if budget was discussed)
   - Close date (if timeline was discussed)
4. Confirm the update was successful and summarize what was changed

## Output Format
**Deal Updated: [Company Name]**
- Stage: [Previous] → [New] (or "unchanged")
- Key Notes Added: [2-3 sentence summary]
- Next Steps: [Action items with owners]
- Flags: [Any concerns or blockers noted]

## Quality Checks
- Never overwrite existing notes — always append
- If the deal can't be found in HubSpot, ask for clarification before creating a new record
- If deal stage change is ambiguous, confirm with the user before updating
- Always include a summary of what was changed for audit trail

## Examples
See `examples/` folder.
