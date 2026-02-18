# VAN Agent SDK — Roadmap

## Phase 1: Foundation (Feb 18, 2026) — CURRENT
- [x] Scaffold monorepo structure
- [ ] Deploy Jordan Belfur as peer agent on OpenClaw
- [ ] Slack integration (Socket Mode)
- [ ] HubSpot MCP read/write
- [ ] Google Workspace MCP access
- [ ] ABM brief skill (template)
- [ ] AEO report skill (template)
- [ ] Update deal skill

## Phase 2: Skill Maturity (Feb 19-21)
- [ ] Port real Claude Code workflows into ABM brief skill
- [ ] Port real Claude Code workflows into AEO report skill
- [ ] Add real examples to all skill `examples/` folders
- [ ] Load account research data into Jordan's knowledge directory
- [ ] Test each skill with 5+ real inputs, document failures, iterate

## Phase 3: Data Integration (Feb 24-28)
- [ ] Clay API integration for enrichment pulls
- [ ] Outreach message drafting skill (Clay data + messaging framework)
- [ ] Messaging framework as referenceable skill
- [ ] LinkedIn research prep (queuing actions, not executing)

## Phase 4: Team Rollout (March)
- [ ] Full sales ops plugin packaging
- [ ] Collin onboarded as daily Jordan user
- [ ] Feedback loop with Gizmo's skill-updater meta-skill
- [ ] Metrics collection: usage counts, edit rates, time savings

## Phase 5: Multi-Agent Expansion (Q2 2026)
- [ ] Second agent deployment (strategy/ops focused)
- [ ] Inter-agent communication via `sessions_send`
- [ ] Shared context protocol between agents
- [ ] Plugin distribution via GitHub Actions

## Phase 6: Platform (Q3-Q4 2026)
- [ ] SDK packaging for external use
- [ ] Skill marketplace / registry
- [ ] Agent templates for common use cases
- [ ] Self-improving skill loop (agents update their own skills based on feedback)
