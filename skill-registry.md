# Skill Registry — VAN Agent SDK

Master catalog of all available skills. Agents reference skills by name. Skills live in `skills/<skill-name>/SKILL.md`.

## Active Skills

| Skill | Path | Description | Status |
|-------|------|-------------|--------|
| `abm-brief` | `skills/abm-brief/SKILL.md` | Generate structured ABM account briefs from enriched data | Template — needs real workflow |
| `aeo-report` | `skills/aeo-report/SKILL.md` | Generate AEO analysis reports for prospect websites | Template — needs real workflow |
| `update-deal` | `skills/update-deal/SKILL.md` | Update HubSpot deal records from call notes/emails/transcripts | Active |
| `sop-from-transcript` | `skills/sop-from-transcript/SKILL.md` | Generate SOPs from video/call transcripts | Placeholder |

## Planned Skills

| Skill | Description | Target Date |
|-------|-------------|-------------|
| `clay-enrich` | Pull enrichment data from Clay API | Week of Feb 24 |
| `outreach-draft` | Draft outreach messages using Clay data + messaging framework | Week of Feb 24 |
| `linkedin-prep` | Queue LinkedIn actions (research only, no automation) | March |

## Slash Commands

Commands are thin wrappers in `commands/` that invoke skills:

| Command | Invokes Skill | Usage |
|---------|--------------|-------|
| `/abm-brief` | `abm-brief` | `/abm-brief [company name]` |
| `/aeo-report` | `aeo-report` | `/aeo-report [URL or company name]` |
| `/update-deal` | `update-deal` | `/update-deal [company name]` |
