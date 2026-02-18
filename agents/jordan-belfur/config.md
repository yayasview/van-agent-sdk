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

### Google Workspace MCP — Drive access, Docs/Sheets creation
- TBD — not yet configured

## Deployment Notes
- Runs as peer agent alongside Gizmo on the same OpenClaw Gateway
- Socket Mode required for Slack
- MCP servers launch as child processes via STDIO transport — no external URLs needed
- The `HUBSPOT_ACCESS_TOKEN` env var must be set in the agent's runtime environment on the EC2 instance
