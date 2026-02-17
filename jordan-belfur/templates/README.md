# VAN Sales BDR — Templates

This folder contains all templates that power the BDR system. The BDR agent uses these templates as the starting point for every output — it never drafts from scratch.

## How to Add Templates

Drop your existing VAN templates into the appropriate subfolder. Supported formats: `.docx`, `.pdf`, `.md`, `.txt`, `.html`

The BDR agent will read and adapt these templates based on deal-specific context (meeting notes, HubSpot data, client requirements).

## Template Categories

### `/proposals/`
Proposal templates for VAN services. Should include sections for: executive summary, scope of work, deliverables, timeline, pricing, team, and terms.

**What to add here:**
- Your standard VAN proposal template(s)
- Any service-specific proposal variants (e.g., Webflow migration vs. performance marketing)
- Pricing frameworks or rate cards

### `/contracts/`
Contract and SOW templates. These get prepared here and then uploaded to PandaDoc for signature.

**What to add here:**
- Master services agreement (MSA)
- Statement of work (SOW) template
- NDA template (if used)
- Any amendment templates

### `/emails/follow-ups/`
Follow-up email templates for unresponsive deals at various stages.

**What to add here:**
- Post-discovery follow-up
- Post-proposal follow-up
- Stale deal re-engagement
- Break-up / final attempt email

### `/emails/meeting-recaps/`
Meeting recap email templates.

**What to add here:**
- Discovery call recap
- Strategy session recap
- Proposal review recap
- General meeting recap

### `/emails/welcome/`
Client welcome and onboarding emails.

**What to add here:**
- Welcome email (sent on contract signature)
- Kickoff scheduling email
- Access/onboarding instructions email

### `/internal-briefs/`
Internal handoff documents for the accounts team.

**What to add here:**
- Client handoff brief template
- Project brief template
- Account setup checklist

### `/billing/`
Billing and invoicing information templates.

**What to add here:**
- New client billing setup form
- Invoice template or format guide
- Payment terms reference

## Naming Convention

Use descriptive, lowercase, hyphenated names:
- `standard-proposal.docx`
- `webflow-migration-sow.docx`
- `post-discovery-follow-up.md`
- `client-handoff-brief.md`
