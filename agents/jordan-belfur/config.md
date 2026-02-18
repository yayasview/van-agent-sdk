# Jordan Belfur — Agent Configuration

## OpenClaw Agent Config

```json5
{
  id: "jordan",
  name: "Jordan Belfur",
  workspace: "~/projects/van-agent-sdk/agents/jordan-belfur/workspace",
  model: "anthropic/claude-sonnet-4-6"
}
```

## Slack Binding

```json5
{
  agentId: "jordan",
  match: {
    channel: "slack"
    // Update with actual channel ID after Slack app creation
  }
}
```

## Required Slack Bot Scopes
- `chat:write`
- `channels:read`, `channels:history`
- `groups:read`, `groups:history`
- `im:read`, `im:write`, `im:history`
- `app_mentions:read`
- `files:read`, `files:write`

## Event Subscriptions
- `message.channels`
- `message.groups`
- `message.im`
- `app_mention`

## MCP Connections

MCP servers are configured in `.mcp.json` at the agent root (`agents/jordan-belfur/.mcp.json`).

### HubSpot MCP — read/write contacts, companies, deals

- **Server:** `hubspot-mcp-server` (npm, STDIO transport)
- **Auth:** HubSpot Private App access token via `HUBSPOT_ACCESS_TOKEN` env var
- **Permissions:** Full read/write on contacts, companies, and deals
- **Required HubSpot Private App scopes:**
  - `crm.objects.contacts.read`
  - `crm.objects.contacts.write`
  - `crm.objects.companies.read`
  - `crm.objects.companies.write`
  - `crm.objects.deals.read`
  - `crm.objects.deals.write`
- **Setup:** Create a Private App in HubSpot (Settings > Account Setup > Integrations > Private Apps) with the scopes above. Store the access token in the environment as `HUBSPOT_ACCESS_TOKEN`.

### Google Drive MCP — read/write Drive, Docs, Sheets, Slides

- **Server:** `@piotr-agier/google-drive-mcp` (npm, STDIO transport)
- **Auth:** Google OAuth 2.0 credentials via `GOOGLE_DRIVE_OAUTH_CREDENTIALS` env var (path to `gcp-oauth.keys.json`)
- **Permissions:** Full read/write on Drive files, Docs, Sheets, and Slides
- **Required Google Cloud APIs:**
  - Google Drive API
  - Google Docs API
  - Google Sheets API
  - Google Slides API
- **Required OAuth scopes:**
  - `https://www.googleapis.com/auth/drive`
  - `https://www.googleapis.com/auth/drive.file`
  - `https://www.googleapis.com/auth/documents`
  - `https://www.googleapis.com/auth/spreadsheets`
  - `https://www.googleapis.com/auth/presentations`
- **Setup:**
  1. Create a Google Cloud project at console.cloud.google.com
  2. Enable the four APIs listed above
  3. Configure OAuth consent screen (add users as test users)
  4. Create OAuth 2.0 credentials (Desktop app type), download as `gcp-oauth.keys.json`
  5. Run `npx @piotr-agier/google-drive-mcp auth` once on the EC2 instance to complete OAuth flow
  6. Set `GOOGLE_DRIVE_OAUTH_CREDENTIALS` env var to the path of `gcp-oauth.keys.json`

## Deployment Notes
- Runs as peer agent alongside Gizmo on the same OpenClaw Gateway
- Socket Mode required for Slack
- MCP servers launch as child processes via STDIO transport — no external URLs needed
- The `HUBSPOT_ACCESS_TOKEN` env var must be set in the agent's runtime environment on the EC2 instance
- The `GOOGLE_DRIVE_OAUTH_CREDENTIALS` env var must point to the OAuth credentials JSON file
- OAuth tokens are stored at `~/.config/google-drive-mcp/tokens.json` and auto-refresh
