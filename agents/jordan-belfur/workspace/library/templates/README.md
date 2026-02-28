# VAN Sales BDR — Templates

This folder contains all templates that power the BDR system. The BDR agent uses these templates as the starting point for every output — it never drafts from scratch.

## How to Add Templates

Drop your existing VAN templates into the appropriate subfolder. Supported formats: `.docx`, `.pdf`, `.md`, `.txt`, `.html`

The BDR agent will read and adapt these templates based on deal-specific context (meeting notes, HubSpot data, client requirements).

## Template Categories

### `/proposals/`
Outcome-driven proposal templates. These are the strategic "sell" documents — they answer: Why this project? Why now? Why VAN? What will the business gain? Proposals are framed around business outcomes, not technical deliverables.

**What to add here:**
- VAN proposal templates (one-time project, retainer)
- Service-specific proposal variants
- Pricing frameworks or rate cards

**Current templates:**
- `one-time-project.md` — Fixed-scope project proposals (migrations, builds, redesigns)
- `retainer-support.md` — Ongoing retainer / Pro+ Support proposals (needs split — still combined format)

### `/contracts/`
Statement of Work (SOW) and contract templates. These are the "bind" documents — detailed scope, deliverables, hour breakdowns, payment schedules, signatures, and legal terms. Prepared here, then uploaded to PandaDoc for signature.

**What to add here:**
- Statement of work (SOW) templates
- Master services agreement (MSA)
- NDA template (if used)
- Amendment templates

**Current templates:**
- `one-time-project-sow.md` — Fixed-scope project SOW (companion to proposals/one-time-project.md)

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
