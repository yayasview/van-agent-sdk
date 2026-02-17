# Jordan Belfur — Setup Guide

## Prerequisites

- Node.js installed
- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- HubSpot account with deal/contact/company access
- [gogcli](https://github.com/steipete/gogcli) installed (`brew install steipete/tap/gogcli`)

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

### 3. Set up Google Workspace access (gogcli)

Jordan uses `gogcli` to read Google Drive, Docs, and Sheets (proposals, briefs, pipeline spreadsheets).

**a. Create a Google Cloud project:**

1. Go to [console.cloud.google.com](https://console.cloud.google.com) → **New Project** (e.g. `van-jordan-belfur`)
2. Enable **Google Drive API** and **Google Sheets API** (and Docs API if needed)
3. Configure **OAuth consent screen** (External or Internal) with your scopes
4. Create **OAuth client ID** (type: Desktop app) and download the JSON file

**b. Register credentials and authorize:**

```bash
gog auth credentials ~/Downloads/client_secret_*.json
gog auth add you@yourdomain.com
```

A browser window opens for OAuth sign-in. Tokens are stored in your macOS Keychain.

**c. Verify access:**

```bash
export GOG_ACCOUNT=you@yourdomain.com
gog drive ls --limit 5
```

> **Note:** The `uploads/` directory is gitignored. Never commit `client_secret*.json` files.

### 4. Launch Jordan

```bash
claude
```

The first time you ask Jordan to read or write HubSpot data, a browser window will open for OAuth authentication. Sign in with your HubSpot credentials. This is a one-time step.

### 5. Test the full loop

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

**gogcli not working:**
Check `gog auth ls` to verify your account is authorized. If tokens expired, re-run `gog auth add you@yourdomain.com`. Make sure `GOG_ACCOUNT` is set or pass `--account` on each command.

## File Structure

```
jordan-belfur/
├── CLAUDE.md          ← Jordan's persona (auto-loaded by Claude Code)
├── .mcp.json          ← HubSpot + Granola MCP configuration
├── .gitignore         ← Keeps secrets and OS files out of git
├── SETUP.md           ← You are here
├── skills/
│   ├── update-deal/
│   │   ├── SKILL.md
│   │   └── examples/
│   │       ├── input-call-transcript.md
│   │       └── output-deal-update.md
│   └── fetch-doc/
│       └── SKILL.md
├── tools/
│   └── mcp-config.md  ← Tool access documentation
├── uploads/           ← OAuth credentials (gitignored)
└── memory/
    └── context.md      ← Accumulated context (starts empty)
```
