# Deploying a New Agent on OpenClaw

Operational guide for adding a new peer agent alongside existing agents on the VAN OpenClaw gateway. Covers Slack setup, registration, memory/search configuration, and heartbeat activation. Based on the Jordan Belfur deployment (Feb 2026).

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

## Step 5: Set Up Memory, Search & Heartbeat

Every agent should launch with a working memory system. Without this, the agent can't remember anything across sessions, can't search its own knowledge base, and won't do automated maintenance. These are the improvements that make the difference between a stateless chatbot and a persistent teammate.

### 5a. Create Workspace Memory Files

Your workspace should include these files **before** the first restart:

```
agents/<agent-name>/workspace/
├── AGENTS.md          # System prompt (required)
├── SOUL.md            # Personality and voice
├── IDENTITY.md        # Name, role, emoji
├── USER.md            # Who the agent works with
├── TOOLS.md           # Tool guidance and capabilities
├── BOOTSTRAP.md       # First-run instructions
├── HEARTBEAT.md       # Automated maintenance schedule (see below)
├── MEMORY.md          # Structured long-term memory (see below)
├── memory/            # Daily notes (auto-populated)
└── knowledge/         # Domain-specific reference material (optional)
```

### 5b. Create `MEMORY.md` — Structured Long-Term Memory

Every agent needs a `MEMORY.md` that acts as its persistent brain. **Customize this for the agent's role.** Don't copy-paste Gizmo's personal MEMORY.md — build one that matches what this agent needs to remember.

**Template** (adapt the sections to the agent's domain):
```markdown
# MEMORY.md — <Agent Name>'s Long-Term Memory

**System**: <one-line description of what this agent tracks>
**Last Updated**: <deploy date>

## Quick Links
- **[Daily Notes](./memory/)** — Session logs and conversation notes
- **[Knowledge Base](./knowledge/)** — <domain-specific description>

## <Domain State Section>
(The core thing this agent tracks — pipeline, projects, accounts, etc.)

| Column1 | Column2 | Column3 | Last Touch | Next Action |
|---------|---------|---------|------------|-------------|
| *(populated as agent works)* | | | | |

## Key Decisions & Context
(Important decisions, strategy shifts, lessons learned)

- <deploy date>: <Agent> deployed. <Brief description of initial mission>.

## People & Relationships
| Who | Role | Notes |
|-----|------|-------|
| <key people the agent works with> | | |

## Lessons Learned
*(Populated over time as agent learns from interactions)*

## No-Deletion Rule
Never delete facts. When outdated: strike through the old, add updated below.
```

**Examples by role:**
- **Sales agent** → Pipeline State table with accounts, stages, last touch, next actions
- **Operations agent** → Project tracker with status, owners, deadlines
- **Research agent** → Topic index with sources, findings, confidence levels
- **Support agent** → Issue tracker with patterns, resolutions, escalation contacts

### 5c. Create `HEARTBEAT.md` — Automated Maintenance

The heartbeat is how your agent stays sharp between conversations. **If HEARTBEAT.md is empty or only has comments, the agent will skip heartbeats entirely.** You must put real instructions in here.

**Template** (customize the checks for the agent's role):
```markdown
# HEARTBEAT.md — <Agent Name>'s Automated Maintenance

## Every Heartbeat (4-6 hours)

1. **Check for new daily notes** since last extraction
2. **<Domain-specific pulse>** — scan for <things going stale/needing attention>
3. **Extract durable facts** from recent conversations:
   - <Fact type 1 relevant to this agent's role>
   - <Fact type 2>
   - <Fact type 3>
4. **Write extracted facts** to `memory/YYYY-MM-DD.md`
5. **Update MEMORY.md** <domain state section> if anything changed

## Weekly (Every 7 days)

1. **<Domain summary>** — create weekly snapshot in `memory/`
2. **Review MEMORY.md** — update state tables, prune stale entries
3. **Flag issues** — <what should the agent proactively alert on?>

## Extraction Heuristics

### Extract:
- <list of things worth remembering for this agent>

### Skip:
- Casual conversation
- Already-captured facts
- Transient requests

## Quiet Hours
- **23:00-08:00 ET**: No proactive outreach. `HEARTBEAT_OK` unless urgent.
- **Nothing new**: Reply `HEARTBEAT_OK`.
- **< 30 min since last check**: Always `HEARTBEAT_OK`.
```

**Key principle:** The heartbeat instructions should be specific to the agent's job. A sales agent checks pipeline movement. An ops agent checks project deadlines. A research agent checks for new sources. Don't just copy another agent's heartbeat.

### 5d. Add Memory Search Config to `openclaw.json`

If your agent has a `knowledge/` directory (or any content outside `memory/`), you **must** tell OpenClaw to index it. By default, only `memory/**/*.md` and session transcripts are indexed.

Edit the agent's entry in `openclaw.json` to add `memorySearch.extraPaths` and `heartbeat`:

```json
{
  "id": "<agent-id>",
  "name": "<agent-id>",
  "workspace": "~/projects/van-agent-sdk/agents/<agent-name>/workspace",
  "agentDir": "~/.openclaw/agents/<agent-id>/agent",
  "model": "anthropic/claude-sonnet-4-6",
  "identity": {
    "name": "<Display Name>",
    "emoji": "<emoji>"
  },
  "memorySearch": {
    "extraPaths": ["knowledge"]
  },
  "heartbeat": {
    "every": "4h"
  }
}
```

**What `extraPaths` does:** Tells the memory indexer to also scan files in `<workspace>/knowledge/` (in addition to the default `memory/` directory). All `.md` files in those paths get embedded and become searchable via `memory_search`.

**What `heartbeat.every` does:** Gives this agent its own heartbeat schedule. Without it, only the default agent (`main`) runs heartbeats. The agent reads `HEARTBEAT.md` on each tick and follows the instructions there.

**What's already inherited from global defaults** (no config needed):
- `memorySearch.sources: ["memory", "sessions"]` — searches both memory files and past session transcripts
- `memorySearch.experimental.sessionMemory: true` — cross-session retrieval
- `compaction.mode: "safeguard"` — safe context compaction for long sessions
- `compaction.memoryFlush.enabled: true` — writes memories to disk before compacting context
- `session-memory` hook — automatically writes session summaries to `memory/` on `/new`

---

## Step 6: Restart the Gateway

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

## Step 7: Index the Agent's Memory

After the first restart, force a full reindex so all the agent's content is searchable:

```bash
openclaw memory index --agent <agent-id> --force --verbose
```

**Verify the index:**
```bash
openclaw memory status --agent <agent-id> --json
```

You should see:
- `files` count matching your workspace content (memory files + knowledge files + sessions)
- `extraPaths` showing `["knowledge"]`
- `sourceCounts` breaking down memory vs session chunks

**Test a search:**
```bash
openclaw memory search --agent <agent-id> "a topic from your knowledge base"
```

If you get results, the index is working. If empty, check that:
- `extraPaths` is set correctly in `openclaw.json`
- The files are `.md` format (only markdown is indexed by default)
- You ran `--force` on the reindex

---

## Step 8: Test

Send a DM to the new bot in Slack:
- "Hey, who are you?" — verify personality from SOUL.md
- Ask about something in the agent's knowledge base — verify memory search works
- Ask "What are your current priorities?" — verify MEMORY.md is being read

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

### Memory search returns empty results
1. Check index status: `openclaw memory status --agent <agent-id> --json`
2. If `files: 0` or `chunks: 0`, the index needs rebuilding: `openclaw memory index --agent <agent-id> --force`
3. If `extraPaths` is empty but you have a `knowledge/` dir, add it to the agent config and restart
4. Only `.md` files are indexed — `.json`, `.csv`, `.pdf` files in `knowledge/` won't be searchable
5. After config changes, always restart the gateway before reindexing

### Heartbeat not firing
1. Confirm the agent has `"heartbeat": { "every": "4h" }` in its `agents.list[]` entry
2. Confirm `HEARTBEAT.md` has actual instructions (not just comments)
3. Check `openclaw doctor` — it should show heartbeat status for the agent
4. Check logs: `openclaw channels logs --channel slack --lines 50` for heartbeat entries

---

## Reference: What Gets Created

After running the steps above, here's what's in `openclaw.json`:

```
agents.list[]:
  {
    id: "<agent-id>",
    workspace: "...",
    model: "...",
    identity: { name: "...", emoji: "..." },
    memorySearch: { extraPaths: ["knowledge"] },
    heartbeat: { every: "4h" }
  }

bindings[]:
  { agentId: "<agent-id>", match: { channel: "slack", accountId: "<agent-id>" } }

channels.slack.accounts.<agent-id>:
  { botToken: "...", appToken: "...", name: "..." }
```

On disk:
```
~/.openclaw/agents/<agent-id>/
  agent/              # Agent state
  sessions/           # Per-agent session store (auto-managed)
    sessions.json
    *.jsonl           # Session transcripts

~/.openclaw/memory/<agent-id>.sqlite    # Memory index (auto-created)
```

In the repo:
```
agents/<agent-name>/workspace/
  AGENTS.md           # System prompt (required)
  SOUL.md             # Personality
  IDENTITY.md         # Name, role
  USER.md             # Who agent works with
  TOOLS.md            # Tool guidance
  BOOTSTRAP.md        # First-run instructions
  HEARTBEAT.md        # Automated maintenance schedule
  MEMORY.md           # Structured long-term memory
  memory/             # Daily notes (auto-populated over time)
  knowledge/          # Domain reference material (indexed via extraPaths)
```

### What's inherited from global defaults (no per-agent config needed)

| Setting | Default | Effect |
|---------|---------|--------|
| `memorySearch.sources` | `["memory", "sessions"]` | Searches memory files and past conversations |
| `memorySearch.experimental.sessionMemory` | `true` | Cross-session retrieval enabled |
| `compaction.mode` | `"safeguard"` | Safe context compaction for long sessions |
| `compaction.memoryFlush.enabled` | `true` | Writes memories to disk before compacting |
| `hooks.internal.session-memory` | `enabled` | Auto-writes session summaries to `memory/` |
| `hooks.internal.boot-md` | `enabled` | Loads workspace .md files at session start |
| Hybrid search (BM25 + vector) | On | Both keyword and semantic search |
| Embedding provider | OpenAI `text-embedding-3-small` | Via global `OPENAI_API_KEY` |

---

## Checklist for New Agents

### Slack & Registration
- [ ] Slack app created with Socket Mode + correct scopes
- [ ] Bot token (`xoxb-`) and app token (`xapp-`) saved
- [ ] OpenClaw >= 2026.2.17
- [ ] `openclaw channels add --channel slack --account <id> --bot-token ... --app-token ...`
- [ ] `openclaw agents add <id> --workspace ... --model ... --bind "slack:<id>"`
- [ ] `openclaw agents set-identity --agent <id> --name "..." --emoji "..."`

### Workspace Files
- [ ] `AGENTS.md` — system prompt with role, context, instructions
- [ ] `SOUL.md` — personality, voice, communication style
- [ ] `IDENTITY.md` — name and role definition
- [ ] `USER.md` — who the agent works with
- [ ] `TOOLS.md` — tool capabilities and guidance
- [ ] `BOOTSTRAP.md` — first-run orientation
- [ ] `HEARTBEAT.md` — **actual maintenance instructions** (not empty!)
- [ ] `MEMORY.md` — structured long-term memory, personalized for role
- [ ] `memory/` directory exists
- [ ] `knowledge/` directory with domain reference material (if applicable)

### Memory & Search Config
- [ ] `memorySearch.extraPaths: ["knowledge"]` added to agent config (if using `knowledge/`)
- [ ] `heartbeat.every: "4h"` added to agent config
- [ ] Gateway restarted after config changes
- [ ] `openclaw memory index --agent <id> --force` run after first restart
- [ ] `openclaw memory status --agent <id>` shows files and chunks indexed
- [ ] `openclaw memory search --agent <id> "<test query>"` returns results

### Verification
- [ ] `openclaw channels status --probe` shows `works`
- [ ] DM test gets response with correct personality
- [ ] Knowledge base question gets accurate answer (memory search working)
- [ ] `openclaw doctor` shows no errors
