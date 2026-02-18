# VAN Agent SDK — Shared Context

## What This Repo Is

This is the **VAN Agent SDK** — a monorepo for all VAN (Veza Agency Network) AI agents, shared skills, and slash commands. Agents reference skills from the top-level `skills/` directory. Distribution is a packaging concern handled by CI/CD, not repo structure.

## Architecture

- **Monorepo.** One repo, shared skills, multiple agents.
- **Peer agents.** Each agent runs independently on the OpenClaw Gateway. They have their own workspace, session store, skills, and personality. They communicate via `sessions_send` but are not hierarchically coupled.
- **Skills are shared.** The `skills/` directory is flat. Each skill has a `SKILL.md` and optional `examples/`. Agents reference skills — they don't own them.
- **Commands are thin wrappers.** The `commands/` directory contains slash command definitions that invoke skills.

## Repo Layout

```
van-agent-sdk/
├── CLAUDE.md              # This file — shared context for all agents
├── skill-registry.md      # Master catalog of all skills
├── skills/                # Shared skill library
├── agents/                # Agent definitions and workspaces
├── commands/              # Slash commands (thin wrappers around skills)
├── plugins/               # Future: packaged bundles for distribution
├── .github/workflows/     # CI/CD
└── docs/                  # Architecture docs, roadmap, guides
```

## About VAN

**Veza Agency Network (VAN)** is a next-generation network of best-in-class digital agencies operating under one umbrella. VAN is a global creative consultancy that combines creative and consulting to orchestrate extraordinary experiences across the full customer journey.

### Key Positioning
VAN is where modern marketing teams go when they've outgrown their agency but aren't ready for (or don't need) a Big 4 consultancy. We bring the specialization of boutique agencies with the scale, reliability, and strategic depth of a network.

### Core Service Pillars
- **Brand** — Identity, positioning, brand strategy, creative direction
- **Digital Experience** — Webflow enterprise development, web design, UX/UI, CMS architecture
- **Performance Marketing** — Paid media, demand gen, conversion optimization
- **Strategy & Consulting** — GTM strategy, digital transformation, marketing ops
- **SEO & Content** — Organic growth, content strategy, thought leadership, AEO
- **Technology** — Integrations, migrations, MarTech stack optimization

## Conventions

- All enterprise pipeline is sold as **VAN**, not individual agencies.
- Never reference individual agencies in outbound messaging unless specifically instructed.
- Content is deal enablement, not general awareness. Educate before we sell.
- When you don't have data, say so. Never fabricate prospect information.
