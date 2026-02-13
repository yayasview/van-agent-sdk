# VAN OpenClaw Agents

AI employees for the Veza Agency Network. Each agent is a named team member with distinct skills, tools, memory, and personality — deployed via OpenClaw into Slack.

## Agents

| Agent | Role | Slack Handle | Status |
|-------|------|-------------|--------|
| **Jordan Belfur** | SDR/AE — Sales Operations | `@jordan` | 🟢 Active |
| *More agents coming* | | | |

## Architecture

Each agent lives in its own directory with:
- `CLAUDE.md` — Persona, role, boundaries, communication style
- `skills/` — Domain-specific SKILL.md files the agent executes
- `tools/` — MCP and API configurations scoped to the agent's needs
- `memory/` — Accumulated context from interactions

`shared-skills/` contains skills that multiple agents can reference.

`_skill-updater/` is the meta-skill Gizmo uses to process feedback and improve skills via PRs.

## Infrastructure

- **Runtime:** Mac Mini M4 (32GB) running OpenClaw instances
- **Source of truth:** This GitHub repo
- **Skill lifecycle:** Team feedback → Gizmo → PR → Review → Merge → Agents pick up changes
- **Surfaces:** Slack (primary), claude.ai (deep work), n8n (automated workflows)

## Naming Convention

All agents are named with Gremlins movie puns. Don't ask why. Just accept it.
