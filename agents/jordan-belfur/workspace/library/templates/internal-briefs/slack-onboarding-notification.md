# Slack Onboarding Notification

> **Template Type:** New account notification for #van-new-account-onboarding
> **Trigger:** After internal project brief is complete and ready to share
> **Channel:** #van-new-account-onboarding
> **Purpose:** Alert the accounts team to a new closed-won deal, provide all resources, and set the next action.

---

## Message Format

```
🟢 CLOSED WON: {{client_company}} – {{project_summary}} ({{deal_structure}})

{{overview}}

Here's everything you need:
📄 Internal Brief: {{brief_link}}
{{resource_lines}}
📎 Contract: {{contract_link}}

👉 {{next_step}}
```

---

## Field-by-Field Instructions

### Header

`🟢 CLOSED WON: {{client_company}} – {{project_summary}} ({{deal_structure}})`

> **BDR Instructions:**
> - Always start with `🟢 CLOSED WON:`
> - `{{project_summary}}` = short project descriptor (3-6 words). Examples: "Institute Landing Page", "Webflow Migration + WAIO", "Pro+ Growth Retainer"
> - `{{deal_structure}}` = pricing structure in parentheses. Format depends on engagement type:
>   - **Retainer:** `X months @ $X,XXX/mo`
>   - **Fixed project:** `$XX,XXX`
>   - **Hybrid:** `$XX,XXX + $X,XXX/mo ongoing`

### Overview

> **BDR Instructions:** 1-2 sentences max. Cover:
> 1. Relationship context (new vs. returning client)
> 2. What they signed and what it's for
>
> Keep it conversational — this is Slack, not a document. The team will read the full brief for details.
>
> Examples:
> - "They're a returning client (Shadow built their original Webflow site) and they just signed a $10K Growth Plan engagement to build out the Earned Institute — a new learning hub on their existing site."
> - "New client, inbound via Webflow partner referral. $31.8K full migration + WAIO build for their HVAC brand. Big upsell potential — they have two sister brands that need the same treatment."
> - "Returning client upgrading from Base to Growth. Adding SEO/AEO to their existing retainer. $5K/mo, 3-month commitment."

### Resources

> **BDR Instructions:** List all resources the accounts team needs. Always include the Internal Brief and Contract. Add any additional resources that were shared during the sales process.
>
> Standard resources (always include):
> - `📄 Internal Brief:` — link to the brief in Google Drive or attached file
> - `📎 Contract:` — link to signed PandaDoc or attached PDF
>
> Conditional resources (include when available):
> - `🎨 Design Preview:` — Figma, mockup links, or design files the client provided
> - `🌐 Current Site:` — link to client's existing website
> - `📊 Proposal:` — link to the proposal if different from contract
> - `📝 Meeting Notes:` — link to discovery/strategy call notes
> - `🔗 Webflow Project:` — link to existing Webflow project (for returning clients)
>
> Format each as: `[emoji] [Label]: [Link or "Attached"]`

### Next Step

> **BDR Instructions:** One clear, specific action. Always include:
> 1. Who to contact (name + email)
> 2. What to do (schedule kickoff, send welcome, etc.)
>
> Examples:
> - "Please reach out to Dana (dana@earned.com) and Shay (shay@earned.com) to schedule the kickoff."
> - "Andrea (andrea@client.com) is the day-to-day lead — reach out to her to schedule kickoff. CC Jason (jason@client.com) who is the decision maker but won't be in every meeting."
> - "Client is expecting to hear from us within 24 hours. Please reach out to Dan (dan@windowsusa.com) to schedule the kickoff for early next week."

---

## Template Variables Reference

> **For BDR agent use — do not include in final output.**

| Variable | Description | Source |
|----------|-------------|--------|
| `{{client_company}}` | Client name | HubSpot deal |
| `{{project_summary}}` | Short project descriptor | Proposal title |
| `{{deal_structure}}` | Pricing format | Proposal commercials |
| `{{overview}}` | 1-2 sentence context | Sales notes + proposal |
| `{{brief_link}}` | Link to internal brief | Google Drive / file |
| `{{resource_lines}}` | Additional resource links | Varies by deal |
| `{{contract_link}}` | Signed contract link | PandaDoc |
| `{{next_step}}` | Action item with contacts | Deal contacts |

---

## Example: Complete Message

```
🟢 CLOSED WON: Earned – Institute Landing Page (2 months @ $5,000/mo)

They're a returning client (Shadow built their original Webflow site) and they just signed a $10K Growth Plan engagement to build out the Earned Institute — a new learning hub on their existing site.

Here's everything you need:
📄 Internal Brief: Earned – Internal Brief (Earned Institute LP)
🎨 Design Preview: Earned Institute Mockups
📎 Contract: Attached

👉 Please reach out to Dana (dana.del.poso@earned.com) and Shay (shay.wadsworth@earned.com) to schedule the kickoff.
```

---

## Tone Notes

> - This is Slack. Keep it tight. No paragraphs, no formality.
> - The header does the heavy lifting — make it scannable.
> - The overview gives just enough context for the PM to know what they're walking into.
> - Resources should be clickable and complete — no one should have to ask "where's the brief?"
> - Next step should be unambiguous — one person, one action.
