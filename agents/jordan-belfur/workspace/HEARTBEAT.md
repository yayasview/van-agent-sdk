# HEARTBEAT.md — Jordan's Automated Pipeline Maintenance

---

## Every Heartbeat (4-6 hours)

1. **Check for new daily notes** since last extraction
2. **Pipeline pulse** — scan for accounts that haven't been touched in 2+ weeks
3. **Extract durable facts** from recent conversations:
   - Deal stage changes
   - New contacts discovered
   - Strategy decisions made
   - Outreach results (responses, meetings booked)
4. **Write extracted facts** to `memory/YYYY-MM-DD.md`
5. **Update MEMORY.md** pipeline table if any deal moved

## Weekly (Every 7 days)

1. **Pipeline summary** — create weekly pipeline snapshot in `memory/`
2. **Review MEMORY.md** — update pipeline state table, prune stale entries
3. **Check account coverage** — are all Tier 1 accounts getting attention?
4. **Flag stalled accounts** — any T1 account with no activity in 2+ weeks
5. **Notify Yaya** in Slack if any T1 account is going cold

---

## Extraction Heuristics

### Extract:
- Deal stage changes (new meeting, proposal sent, closed-won/lost)
- Contact information (names, roles, email addresses)
- Account intelligence (budget signals, org changes, tech stack details)
- Strategy decisions (messaging changes, targeting shifts)
- Outreach results (reply rates, meeting conversions)
- Teaching event attendance and follow-ups
- Partner conversations and intros

### Skip:
- Casual conversation
- Already-captured facts
- Transient requests ("what time is it", "thanks")
- Hypothetical scenarios not tied to active accounts

### Create daily note entry if:
- A deal moved stages
- New contact or relationship discovered
- Strategy decision was made
- Outreach was sent or received a response
- Account research was completed

---

## Where Things Go

| Type | File |
|------|------|
| Raw session logs | `memory/YYYY-MM-DD.md` |
| Pipeline state | `MEMORY.md` → Pipeline State table |
| Decisions & context | `MEMORY.md` → Key Decisions & Context |
| People changes | `MEMORY.md` → People & Relationships |
| ABM account intel | `abm/tier-1/<account>/` |
| Active deal intel | `deals/<company>/` |
| Lessons learned | `MEMORY.md` → Lessons Learned |

---

## Quiet Hours

- **23:00-08:00 ET**: No proactive outreach. `HEARTBEAT_OK` unless urgent.
- **Nothing new**: If no pipeline movement since last check, reply `HEARTBEAT_OK`.
- **< 30 min since last check**: Always `HEARTBEAT_OK`.
