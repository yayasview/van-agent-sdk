# VAN Agent SDK — Architecture & Vision

## What Is This

The VAN Agent SDK is the infrastructure layer for VAN's AI agent network. It's a monorepo that houses shared skills, agent definitions, and slash commands that power VAN's AI-assisted operations.

## Core Architecture Decisions

### Monorepo
Everything lives in one repo. Skills are shared at the top level. Agents reference skills — they don't own them. Distribution is a packaging concern solved by GitHub Actions, not repo splitting.

### Peer Agents on OpenClaw
Each agent runs as an independent peer on the OpenClaw Gateway. They have their own workspace, session store, skills, and personality. They can communicate via `sessions_send` but are not hierarchically coupled. Routing happens at the Gateway level via channel bindings.

### Skills as Shared Library
The `skills/` directory is the single source of truth for all agent capabilities. Each skill is a self-contained workflow defined in a `SKILL.md` file. Agents consume skills — they don't duplicate them.

### Commands as Thin Wrappers
Slash commands in `commands/` are intentionally thin. They invoke skills and provide usage context, but contain no business logic themselves.

## Current Agents

### Jordan Belfur
- **Role:** ABM Sales Agent / BDR
- **Model:** Claude Sonnet 4.6
- **Channel:** Slack (`#jordan-belfur`)
- **Skills:** abm-brief, aeo-report, update-deal
- **Integrations:** HubSpot (MCP), Google Workspace (MCP)

## SDK Extension Points

### Adding a New Skill
1. Create `skills/<skill-name>/SKILL.md`
2. Add optional `examples/` subfolder
3. Register in `skill-registry.md`
4. Create a slash command wrapper in `commands/` if needed

### Adding a New Agent
1. Create `agents/<agent-name>/AGENTS.md` (identity + knowledge)
2. Create `agents/<agent-name>/SOUL.md` (personality)
3. Create `agents/<agent-name>/workspace/` with knowledge files
4. Add to OpenClaw config with appropriate bindings
5. Set up channel (Slack, Discord, etc.)

## Infrastructure

- **Runtime:** OpenClaw Gateway on EC2
- **Channels:** Slack (Socket Mode)
- **Tools:** HubSpot MCP, Google Workspace MCP
- **Future:** Clay API, browser automation (queued, not automated)
