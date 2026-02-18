# TOOLS.md — Jordan's Tool Config

## HubSpot (via MCP)

**Server:** `hubspot-mcp-server` (npm, STDIO transport)
**Config:** `agents/jordan-belfur/.mcp.json`
**Auth:** `HUBSPOT_ACCESS_TOKEN` env var (HubSpot Private App token)

Jordan has full read/write access to HubSpot for pipeline operations.

### Available Operations

**Contacts**
- Create, read, update, search, and list contacts
- Look up contacts by company, role, or email
- Create new contacts with duplicate prevention

**Companies**
- Create, read, update, search, and list companies
- Pull company data, update properties
- Create new companies with duplicate prevention

**Deals**
- Create, read, update, search, and list deals
- Query pipeline stages, update deal stages
- Add notes, modify amounts/close dates

**Associations**
- Query and manage associations between contacts, companies, and deals

**Tasks & Engagements**
- Create follow-up tasks
- Search and filter notes and engagements

### Usage Rules
- Always append notes, never overwrite existing ones
- Confirm with user before changing deal stages
- If a deal can't be found, ask for clarification before creating new records
- Never create duplicate records — use search first

## Google Workspace (via MCP)

Jordan has access to Google Drive, Docs, and Sheets:

- **Google Drive** — Read. Search and access files (meeting transcripts, research docs, account data)
- **Google Docs** — Read/write. Create and edit documents (briefs, reports, proposals)
- **Google Sheets** — Read/write. Create and edit spreadsheets (project plans, account trackers)

## Skills (Shared Library)

Skills live in the shared skill library at the repo root. When you need a skill, read its `SKILL.md`:

| Skill | Path (relative to workspace) | Description |
|-------|------------------------------|-------------|
| `abm-brief` | `../../skills/abm-brief/SKILL.md` | Generate structured ABM account briefs from enriched data |
| `aeo-report` | `../../skills/aeo-report/SKILL.md` | Generate AEO analysis reports for prospect websites |
| `update-deal` | `../../skills/update-deal/SKILL.md` | Update HubSpot deal records from call notes/emails/transcripts |
| `sop-from-transcript` | `../../skills/sop-from-transcript/SKILL.md` | Generate SOPs from video/call transcripts |

**How to use a skill:** Read the SKILL.md, follow its workflow, use its output format. Skills are the playbook — follow them.

## Knowledge Directory

Deep-dive strategy docs and account data live in `knowledge/`:

| File | What's in it |
|------|-------------|
| `knowledge/q1-strategy-full.md` | Full Q1 2026 strategy document |
| `knowledge/abm-strategy.md` | ABM strategy and engagement playbooks |
| `knowledge/icp-framework.md` | ICP criteria and scoring model |
| `knowledge/messaging-framework-v1.md` | Persona messaging, objection handling, outreach templates |
| `knowledge/timeline.md` | Project timeline and milestones |
| `knowledge/accounts/` | Account data — Tier 1 briefs, AEO reports, AI responses, raw data |
