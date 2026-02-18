# MCP Setup Guide — Jordan Belfur

Step-by-step instructions to finalize HubSpot and Google Drive MCP connections for Jordan's agent. These MCPs are configured in `agents/jordan-belfur/.mcp.json` and are auto-discovered by Claude Code and OpenClaw.

---

## Prerequisites

- **Node.js v18+** installed on the target machine (EC2 instance or local dev)
- **npm/npx** available in PATH
- Admin access to VAN's HubSpot account
- Admin access to VAN's Google Workspace / Google Cloud Console

---

## Part 1: HubSpot MCP

### Step 1 — Create a HubSpot Private App

1. Log into HubSpot at https://app.hubspot.com
2. Navigate to **Settings** (gear icon, top right)
3. In the left sidebar: **Account Setup → Integrations → Private Apps**
4. Click **Create a private app**
5. Fill in:
   - **Name:** `Jordan Belfur Agent`
   - **Description:** `MCP connection for Jordan's AI agent — read/write CRM access`

### Step 2 — Configure Scopes

In the **Scopes** tab of the Private App setup, search for and enable these six scopes:

| Scope | Access |
|-------|--------|
| `crm.objects.contacts.read` | Read contacts |
| `crm.objects.contacts.write` | Write contacts |
| `crm.objects.companies.read` | Read companies |
| `crm.objects.companies.write` | Write companies |
| `crm.objects.deals.read` | Read deals |
| `crm.objects.deals.write` | Write deals |

Click **Create app** when done. HubSpot will show a confirmation dialog — click **Continue creating**.

### Step 3 — Copy the Access Token

After creation, HubSpot displays the access token **once**. Copy it immediately and store it securely.

The token format looks like: `pat-na1-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

> **Warning:** If you lose this token, you'll need to rotate it from the Private App settings page. HubSpot does not show it again after initial creation.

### Step 4 — Set the Environment Variable

On the EC2 instance (or local machine), add to your shell profile (`~/.bashrc`, `~/.zshrc`, or equivalent):

```bash
export HUBSPOT_ACCESS_TOKEN="pat-na1-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```

Then reload:

```bash
source ~/.bashrc
```

For OpenClaw, ensure this env var is available to Jordan's agent process. If OpenClaw uses a `.env` file or systemd service, add it there as well.

### Step 5 — Verify HubSpot MCP

Test that the MCP server starts correctly:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}' | HUBSPOT_ACCESS_TOKEN="$HUBSPOT_ACCESS_TOKEN" npx -y hubspot-mcp-server
```

You should see a JSON response with `serverInfo` and `capabilities`. Press `Ctrl+C` to exit.

If you get an authentication error, double-check the token value and scopes.

---

## Part 2: Google Drive MCP

### Step 1 — Create a Google Cloud Project

1. Go to https://console.cloud.google.com
2. Click the project dropdown (top left) → **New Project**
3. **Project name:** `VAN Agent SDK` (or similar)
4. Click **Create**
5. Make sure the new project is selected in the project dropdown

### Step 2 — Enable Required APIs

1. Navigate to **APIs & Services → Library** (left sidebar)
2. Search for and enable each of these four APIs:
   - **Google Drive API** — click **Enable**
   - **Google Docs API** — click **Enable**
   - **Google Sheets API** — click **Enable**
   - **Google Slides API** — click **Enable**

### Step 3 — Configure OAuth Consent Screen

1. Navigate to **APIs & Services → OAuth consent screen**
2. Click **Get started** (or **Configure consent screen**)
3. Fill in:
   - **App name:** `VAN Agent SDK`
   - **User support email:** your email
   - **Developer contact email:** your email
4. Under **Audience**, select:
   - **Internal** if using Google Workspace (recommended — no app review needed)
   - **External** if using personal Gmail accounts
5. Under **Data Access** (or **Scopes**), click **Add or Remove Scopes** and add:
   - `https://www.googleapis.com/auth/drive`
   - `https://www.googleapis.com/auth/drive.file`
   - `https://www.googleapis.com/auth/documents`
   - `https://www.googleapis.com/auth/spreadsheets`
   - `https://www.googleapis.com/auth/presentations`
6. Click **Save and Continue**
7. If you chose **External**: under **Test users**, click **Add users** and add the Google account email(s) that will authorize the app

### Step 4 — Create OAuth 2.0 Credentials

1. Navigate to **APIs & Services → Credentials**
2. Click **+ CREATE CREDENTIALS → OAuth client ID**
3. **Application type:** `Desktop app`
4. **Name:** `VAN Agent MCP`
5. Click **Create**
6. In the confirmation dialog, click **Download JSON**
7. Rename the downloaded file to `gcp-oauth.keys.json`
8. Move it to a secure location on the EC2 instance, e.g.:
   ```bash
   mkdir -p ~/.config/van-agent-sdk
   mv ~/Downloads/gcp-oauth.keys.json ~/.config/van-agent-sdk/gcp-oauth.keys.json
   chmod 600 ~/.config/van-agent-sdk/gcp-oauth.keys.json
   ```

> **Important:** Never commit this file to git. It contains your client secret.

### Step 5 — Run the OAuth Authorization Flow

On the EC2 instance (or locally), run:

```bash
GOOGLE_DRIVE_OAUTH_CREDENTIALS="$HOME/.config/van-agent-sdk/gcp-oauth.keys.json" \
  npx -y @piotr-agier/google-drive-mcp auth
```

This will:
1. Open a browser window (or print a URL to visit)
2. Ask you to sign in with the Google account that has Drive access
3. Ask you to grant the requested permissions
4. Save the OAuth tokens to `~/.config/google-drive-mcp/tokens.json`

> **Headless EC2 note:** If the EC2 instance has no browser, run the auth step on your local machine first, then copy the tokens file to the EC2 instance:
> ```bash
> # On your local machine after auth completes:
> scp ~/.config/google-drive-mcp/tokens.json ec2-user@your-ec2:~/.config/google-drive-mcp/tokens.json
> ```
> Make sure the `gcp-oauth.keys.json` file is also present on the EC2 instance.

### Step 6 — Set the Environment Variable

Add to your shell profile on the EC2 instance:

```bash
export GOOGLE_DRIVE_OAUTH_CREDENTIALS="$HOME/.config/van-agent-sdk/gcp-oauth.keys.json"
```

Then reload:

```bash
source ~/.bashrc
```

### Step 7 — Verify Google Drive MCP

Test that the MCP server starts correctly:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}' | GOOGLE_DRIVE_OAUTH_CREDENTIALS="$GOOGLE_DRIVE_OAUTH_CREDENTIALS" npx -y @piotr-agier/google-drive-mcp
```

You should see a JSON response with `serverInfo` and `capabilities`. Press `Ctrl+C` to exit.

---

## Part 3: Verify in Claude Code

Once both MCPs are set up, open the repo in Claude Code:

```bash
cd ~/projects/van-agent-sdk/agents/jordan-belfur
claude
```

Claude Code will auto-discover the `.mcp.json` file and start both MCP servers. You should see them listed when Claude starts up. Test with:

- **HubSpot:** "List the most recent deals in our HubSpot pipeline"
- **Google Drive:** "Search Google Drive for files containing 'ABM strategy'"

If either fails, check:
1. The env vars are set in the shell session running Claude Code
2. The HubSpot token hasn't expired or been rotated
3. The Google OAuth tokens are present at `~/.config/google-drive-mcp/tokens.json`

---

## Token Maintenance

### HubSpot
- Private App tokens **do not expire** unless manually rotated
- If you rotate the token in HubSpot, update `HUBSPOT_ACCESS_TOKEN` everywhere

### Google Drive
- OAuth tokens **auto-refresh** using the refresh token
- If the Google Cloud app is in **Testing** mode, refresh tokens expire after **7 days** — you'll need to re-run the auth flow
- To avoid this, publish the app (requires Google's OAuth verification for external apps) or use **Internal** app type with Google Workspace

---

## Environment Variable Summary

| Variable | Value | Used By |
|----------|-------|---------|
| `HUBSPOT_ACCESS_TOKEN` | HubSpot Private App token (`pat-na1-...`) | `hubspot-mcp-server` |
| `GOOGLE_DRIVE_OAUTH_CREDENTIALS` | Path to `gcp-oauth.keys.json` | `@piotr-agier/google-drive-mcp` |

Both must be set in the environment where Jordan's agent runs (EC2 shell, OpenClaw process, or Claude Code session).

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `HUBSPOT_ACCESS_TOKEN is not set` | Ensure the env var is exported in the current shell |
| HubSpot 401 Unauthorized | Token may have been rotated — check Private App settings in HubSpot |
| HubSpot 403 Forbidden | Missing scopes — verify all six scopes are enabled on the Private App |
| Google Drive auth fails on headless EC2 | Run auth locally, then copy `tokens.json` to the EC2 instance |
| Google tokens expired after 7 days | App is in Testing mode — re-run auth or switch to Internal app type |
| `gcp-oauth.keys.json` not found | Check the `GOOGLE_DRIVE_OAUTH_CREDENTIALS` path is correct |
| MCP server doesn't start | Run `npx -y <package-name>` manually to see error output |
| Claude Code doesn't show MCP tools | Make sure you opened Claude Code from the `agents/jordan-belfur/` directory (where `.mcp.json` lives) |
