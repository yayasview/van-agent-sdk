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
- HubSpot MCP — read/write contacts, companies, deals
- Google Workspace MCP — Drive access, Docs/Sheets creation

## Deployment Notes
- Runs as peer agent alongside Gizmo on the same OpenClaw Gateway
- Socket Mode required for Slack
- Check existing Gizmo config for MCP connection pattern and replicate for Jordan
