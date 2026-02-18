# Deploying a New Agent on OpenClaw

Operational guide for adding a new peer agent alongside existing agents on the VAN OpenClaw gateway. Based on the Jordan Belfur deployment (Feb 2026).

---

## Prerequisites

- OpenClaw **>= 2026.2.17** (earlier versions have a multi-agent session path bug)
- SSH access to the EC2 instance running the gateway
- A Slack app created for the new agent (see Step 1)
- The agent's workspace directory ready in this repo under `agents/<agent-name>/workspace/`

**Check your version before starting:**
```bash
openclaw --version
# If below 2026.2.17:
sudo npm install -g openclaw@latest
```

---

## Step 1: Create the Slack App

1. Go to https://api.slack.com/apps and click **Create New App** > **From scratch**
2. Name it after your agent (e.g., "Jordan Belfur")
3. Select the VAN workspace

### Enable Socket Mode
- Go to **Socket Mode** in the sidebar and toggle it **on**
- Generate an **App-Level Token** with `connections:write` scope
- Save the token (`xapp-1-...`)

### Add Bot Scopes
Go to **OAuth & Permissions** > **Bot Token Scopes** and add:
- `chat:write`
- `channels:read`, `channels:history`
- `groups:read`, `groups:history`
- `im:read`, `im:write`, `im:history`
- `app_mentions:read`
- `files:read`, `files:write`

### Subscribe to Events
Go to **Event Subscriptions** > toggle **on**, then under **Subscribe to bot events** add:
- `message.channels`
- `message.groups`
- `message.im`
- `app_mention`

### Install the App
- Go to **Install App** and click **Install to Workspace**
- Copy the **Bot User OAuth Token** (`xoxb-...`)

### Invite the Bot
- In Slack, create a channel for the agent (e.g., `#jordan-belfur`) or DM the bot directly
- Invite the bot: `/invite @AgentName`

You should now have two tokens:
- **App Token:** `xapp-1-...`
- **Bot Token:** `xoxb-...`

---

## Step 2: Clone or Update the Repo on EC2

```bash
cd ~/projects/van-agent-sdk
git pull origin main
```

Or if first time:
```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/yayasview/van-agent-sdk.git
```

---

## Step 3: Add the Slack Channel Account

Each agent with its own Slack bot needs a **separate channel account**. This is the key to multi-agent Slack — do NOT put tokens in the default `channels.slack` block.

```bash
openclaw channels add \
  --channel slack \
  --account <agent-id> \
  --bot-token "xoxb-YOUR-BOT-TOKEN" \
  --app-token "xapp-YOUR-APP-TOKEN" \
  --name "Agent Display Name"
```

Example for Jordan:
```bash
openclaw channels add \
  --channel slack \
  --account jordan \
  --bot-token "xoxb-636071098567-..." \
  --app-token "xapp-1-A0AFLPFDD4M-..." \
  --name "Jordan Belfur"
```

This creates `channels.slack.accounts.<agent-id>` in `openclaw.json` — separate from the default Slack account used by Gizmo.

**Verify:**
```bash
openclaw channels list
```
You should see both the default Slack account and the new one listed.

---

## Step 4: Register the Agent

```bash
openclaw agents add <agent-id> \
  --workspace ~/projects/van-agent-sdk/agents/<agent-name>/workspace \
  --model "anthropic/claude-sonnet-4-6" \
  --bind "slack:<agent-id>" \
  --non-interactive
```

Example for Jordan:
```bash
openclaw agents add jordan \
  --workspace ~/projects/van-agent-sdk/agents/jordan-belfur/workspace \
  --model "anthropic/claude-sonnet-4-6" \
  --bind "slack:jordan" \
  --non-interactive
```

What this does:
- Adds the agent to `agents.list[]` in `openclaw.json`
- Sets the workspace (where AGENTS.md, SOUL.md, etc. live)
- Creates the agent state directory at `~/.openclaw/agents/<agent-id>/`
- Creates a binding that routes `slack` messages from account `<agent-id>` to this agent

### Set Identity (optional)

```bash
openclaw agents set-identity --agent <agent-id> --name "Display Name" --emoji "🎯"
```

**Verify:**
```bash
openclaw agents list --bindings
```

You should see the new agent with its routing rule: `slack accountId=<agent-id>`.

---

## Step 5: Restart the Gateway

```bash
openclaw gateway restart
```

Then validate:
```bash
openclaw doctor
openclaw channels status --probe
```

Both the existing and new Slack accounts should show `works`.

---

## Step 6: Test

Send a DM to the new bot in Slack:
- "Hey, who are you?"
- Verify personality and knowledge from workspace files

**If it doesn't respond**, check logs:
```bash
openclaw channels logs --channel slack --lines 50
```

---

## Troubleshooting

### "Session file path must be within sessions directory"
This is a known bug in OpenClaw **< 2026.2.17**. The fix:
```bash
sudo npm install -g openclaw@latest
echo '{}' > ~/.openclaw/agents/<agent-id>/sessions/sessions.json
openclaw gateway restart
```

### Bot connects but doesn't respond
1. Check logs: `openclaw channels logs --channel slack --lines 50`
2. Verify the binding: `openclaw agents list --bindings` — the agent must have a routing rule matching the Slack account
3. Verify the workspace has an `AGENTS.md` file — this is the system prompt

### Agent responds as Gizmo / wrong personality
The binding is routing to the wrong agent. Check:
```bash
openclaw agents list --bindings
```
Ensure the new agent has `slack accountId=<agent-id>` and NOT just `channel: "slack"` (which would catch all Slack traffic).

### Gizmo's Slack stopped working after adding a new agent
If Gizmo uses the **default** Slack account, it needs its own binding now. Without one, unmatched Slack messages fall through to the default agent — but only if no explicit bindings match. Add Gizmo a binding if needed:
```bash
# Only if Gizmo's Slack broke after adding the new agent
openclaw agents add main --bind "slack:default"
```

---

## Reference: What Gets Created

After running the steps above, here's what's in `openclaw.json`:

```
agents.list[]:     { id: "<agent-id>", workspace: "...", model: "..." }
bindings[]:        { agentId: "<agent-id>", match: { channel: "slack", accountId: "<agent-id>" } }
channels.slack.accounts.<agent-id>:  { botToken: "...", appToken: "...", name: "..." }
```

And on disk:
```
~/.openclaw/agents/<agent-id>/
  agent/          # Agent state (can copy AGENTS.md, SOUL.md here too)
  sessions/       # Per-agent session store (auto-managed)
    sessions.json
    *.jsonl       # Session transcripts
```

---

## Checklist for New Agents

- [ ] Slack app created with Socket Mode + correct scopes
- [ ] Bot token (`xoxb-`) and app token (`xapp-`) saved
- [ ] Agent workspace exists in repo at `agents/<name>/workspace/`
- [ ] Workspace has at minimum: `AGENTS.md` (system prompt)
- [ ] OpenClaw >= 2026.2.17
- [ ] `openclaw channels add --channel slack --account <id> --bot-token ... --app-token ...`
- [ ] `openclaw agents add <id> --workspace ... --model ... --bind "slack:<id>"`
- [ ] `openclaw gateway restart`
- [ ] `openclaw channels status --probe` shows `works`
- [ ] DM test in Slack gets a response with correct personality
