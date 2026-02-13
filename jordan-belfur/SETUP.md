# Jordan Belfur — Setup Guide

## Prerequisites

- Node.js installed
- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- HubSpot account with deal/contact/company access

## Quick Start

### 1. Clone the repo

```bash
git clone git@github.com:van-agency-network/van-openclaw-agents.git
cd van-openclaw-agents/jordan-belfur
```

### 2. Add HubSpot MCP (if .mcp.json doesn't auto-connect)

The `.mcp.json` file in this directory should configure HubSpot automatically. If it doesn't, run:

```bash
claude mcp add --transport http hubspot https://mcp.hubspot.com/anthropic
```

### 3. Launch Jordan

```bash
claude
```

The first time you ask Jordan to read or write HubSpot data, a browser window will open for OAuth authentication. Sign in with your HubSpot credentials. This is a one-time step.

### 4. Test the full loop

Paste call notes and say:

> "Hey Jordan, update HubSpot with this."

Jordan should:
1. Parse the notes into a structured deal update
2. Present the formatted update for your review
3. Ask for confirmation before writing to HubSpot
4. On approval, push the update via MCP

### Verify

After the push, check the deal record in HubSpot. Confirm:
- Fields updated correctly
- Activity logged with proper attribution
- No data was fabricated or assumed

## Troubleshooting

**MCP not connecting:**
Run `/mcp` inside Claude Code to check server status. If hubspot shows disconnected, re-run the `claude mcp add` command above.

**OAuth window doesn't open:**
Make sure you're running Claude Code in a terminal that has browser access (not a headless SSH session).

**Wrong HubSpot permissions:**
Jordan inherits your HubSpot user permissions. If you can't edit a deal in the HubSpot UI, Jordan can't either.

## File Structure

```
jordan-belfur/
├── CLAUDE.md          ← Jordan's persona (auto-loaded by Claude Code)
├── .mcp.json          ← HubSpot MCP configuration
├── SETUP.md           ← You are here
├── skills/
│   └── update-deal/
│       ├── SKILL.md
│       └── examples/
│           ├── input-call-transcript.md
│           └── output-deal-update.md
├── tools/
│   └── mcp-config.md  ← Tool access documentation
└── memory/
    └── context.md      ← Accumulated context (starts empty)
```
