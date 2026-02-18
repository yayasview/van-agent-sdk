# VAN Agent SDK

Monorepo for VAN's AI agent network. Skills are shared at the top level. Agents reference skills — they don't own them.

## Agents

- **Jordan Belfur** — VAN's ABM Sales Agent. Handles pipeline ops, account briefs, AEO reports, and deal management via Slack.

## Quick Start

### Prerequisites
- OpenClaw Gateway running on EC2
- Slack App configured (Socket Mode)
- HubSpot MCP server access
- Google Workspace MCP server access

### Deploy Jordan

1. Clone the repo to the EC2 instance:
   ```bash
   cd ~/projects
   git clone git@github.com:van-agency-network/van-agent-sdk.git
   ```

2. Add Jordan to OpenClaw config (`~/.openclaw/openclaw.json`):
   ```json5
   {
     agents: {
       list: [
         {
           id: "jordan",
           name: "Jordan Belfur",
           workspace: "~/projects/van-agent-sdk/agents/jordan-belfur/workspace",
           model: "anthropic/claude-sonnet-4-6"
         }
       ]
     }
   }
   ```

3. Configure Slack bindings and MCP connections (see `docs/BUILD.md` Section 4-6)

4. Restart the gateway:
   ```bash
   openclaw gateway restart
   ```

5. Test in `#jordan-belfur` Slack channel

## Repo Structure

```
van-agent-sdk/
├── CLAUDE.md              # Shared VAN context for all agents
├── skill-registry.md      # Master catalog of all skills
├── skills/                # Shared skill library
│   ├── abm-brief/         # ABM account brief generation
│   ├── aeo-report/        # AEO analysis reports
│   ├── update-deal/       # HubSpot deal updates
│   └── sop-from-transcript/  # SOP generation from transcripts
├── agents/
│   └── jordan-belfur/     # Jordan's agent definition + workspace
├── commands/              # Slash commands (thin wrappers)
├── plugins/               # Future: packaged bundles
├── .github/workflows/     # CI/CD
└── docs/                  # Architecture, roadmap, build guide
```

## Docs

- [BUILD.md](docs/BUILD.md) — Step-by-step build and deployment guide
- [HANDOFF.md](docs/HANDOFF.md) — SDK architecture and vision
- [ROADMAP.md](docs/ROADMAP.md) — 12-month roadmap
- [CONTRIBUTING.md](docs/CONTRIBUTING.md) — How to create new skills
