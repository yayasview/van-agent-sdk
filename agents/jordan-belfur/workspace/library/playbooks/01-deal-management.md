# Deal Management Playbook

## Purpose
Manage deals through the sales pipeline with proper structure, tracking, and hygiene.

---

## 1. Creating a New Deal in HubSpot

### Input Requirements
- Company name (existing or new in HubSpot)
- Company contact person (email, name, phone)
- Deal name (format: `[Company] - [Service/Product]`)
- Deal amount (estimated annual contract value or one-time fee)
- Deal stage (typically starts at "Qualified Prospect" or "Discovery")
- Source/origin of lead

### Steps
1. Log into HubSpot CRM
2. Navigate to Deals > Create deal
3. Enter deal name using format: `[Company] - [Service/Product]`
4. Select Company (link to existing or create new)
5. Select Deal Stage: Start with "Qualified Prospect" (unless pre-qualified)
6. Enter Deal Amount (base on consultation or discovery call data)
7. Set Close Date (realistic estimate based on deal stage)
8. Add deal owner (typically "BDR AI" or assigned sales rep)
9. Add custom fields:
   - Service Type (e.g., "Web Design", "Digital Marketing", "App Development")
   - Decision Timeline
   - Budget Confirmed (Yes/No)
   - Competitor (if known)
10. Attach Company contact as Primary Contact
11. Click "Save"

### Quality Checks
- Deal name must be specific (not generic "Client A")
- Deal amount must be > $0
- Close Date must be in future
- Company and contact linked correctly
- All required custom fields populated

### Output
- Deal created with unique HubSpot ID
- Deal appears in pipeline dashboard

---

## 2. Deal Stage Definitions & Progression Criteria

### Stage 1: Qualified Prospect
**Definition**: Initial prospect identified, basic qualification done, first contact attempted.

**Progression Criteria** (Move to Discovery):
- First conversation completed (email, call, or meeting)
- Initial interest expressed (they agree to a discovery call)
- Rough fit confirmed (they have relevant needs)
- Next meeting scheduled

**Activities to Log**:
- Initial outreach attempt
- Response received
- Call/meeting scheduled

---

### Stage 2: Discovery
**Definition**: Engaged prospect, understanding their needs, exploring fit.

**Progression Criteria** (Move to Proposal):
- Discovery call completed
- Needs documented (pain points, goals, timeline, budget range)
- Solution approach identified
- Proposal decision made (will/won't send proposal)

**Progression Criteria** (Move back to Qualified Prospect or lose):
- If prospects become unresponsive after 2 weeks: Move to "Stale" or close as "Lost"

**Activities to Log**:
- Discovery call completed
- Meeting notes attached
- Needs summary documented
- Next steps communicated

---

### Stage 3: Proposal
**Definition**: Proposal sent, awaiting feedback or negotiation.

**Progression Criteria** (Move to Negotiation):
- Proposal reviewed by prospect
- Feedback received (questions, objections, interest in revision)
- Prospect engaged in discussion

**Progression Criteria** (Move back to Discovery or close):
- No response after 5 business days: Send follow-up
- No response after 10 business days: Move to "Stale" or "Lost"
- Prospect explicitly says "Not interested": Close as "Lost - Lack of Fit"

**Activities to Log**:
- Proposal sent (PandaDoc link)
- Prospect feedback recorded
- Revision requests logged

---

### Stage 4: Negotiation
**Definition**: Prospect engaged, actively discussing terms, pricing, or contract details.

**Progression Criteria** (Move to Contract):
- Final terms agreed
- Pricing confirmed
- Contract ready for signature
- Signing date scheduled

**Progression Criteria** (Move back to Proposal or close):
- Prospect goes silent for 7+ days: Send check-in
- Negotiations stall: Clarify next step or close as "Lost"

**Activities to Log**:
- Negotiation points discussed
- Terms changes recorded
- Contract version sent
- Signature timeline confirmed

---

### Stage 5: Contract
**Definition**: Contract signed, pending final activation/kickoff.

**Progression Criteria** (Move to Client or close):
- Signed contract received
- Billing/payment terms confirmed
- Kickoff meeting scheduled or completed
- Onboarding initiated

**Activities to Log**:
- Contract signed (date, version)
- Payment received (if applicable)
- Kickoff meeting scheduled
- Onboarding checklist started

---

### Stage 6: Client
**Definition**: Deal closed won, contract active, handoff to accounts team.

**Next Action**: Run Client Onboarding Playbook (05-client-onboarding.md)

---

## 3. When and How to Log Activities

### Activity Types & When to Log
- **Email sent**: Log same day; include email subject and recipient
- **Phone call**: Log same day; duration, outcome, next steps
- **Meeting/call**: Log immediately after; attach notes or recap email
- **Proposal sent**: Log with PandaDoc link and expiration date
- **Contract sent**: Log with contract version number
- **No response/silence**: Log as "Attempting contact" after 2-3 days of inactivity
- **Objection received**: Log objection type and response plan

### How to Log in HubSpot
1. Open deal record
2. Scroll to Activity section (or click "Log activity")
3. Select activity type: Call, Email, Meeting, Task, Note
4. Fill in relevant details:
   - **Call**: Duration, notes on outcome, action items
   - **Email**: Subject, recipient, key message
   - **Meeting**: Attendees, agenda, discussion summary, decisions
   - **Task**: Due date, description, assignee
   - **Note**: Key information or decision point
5. Set follow-up date if action needed
6. Click "Save"

### Minimum Info Required
- **Activity type** (mandatory)
- **Date** (auto-filled to today, adjust if needed)
- **Description** (at least 1-2 sentences; be specific)
- **Outcome** (if applicable): Success, No answer, Interested, Not interested, etc.

### Quality Checks
- Activity logged within 24 hours of occurrence
- Description is specific enough for teammate to understand context
- Next action/follow-up date set if deal needs progression
- No duplicate activities for same event

---

## 4. Pipeline Hygiene: Stale Deal Cleanup & Data Quality

### Weekly Pipeline Review (Every Monday)

#### Step 1: Identify Stale Deals
1. Open HubSpot Pipeline view
2. Filter for deals with **last activity > 14 days ago**
3. For each stale deal:
   - **Check deal stage**: Is it aligned with actual engagement level?
   - **Check close date**: Is it realistic or outdated?
   - **Assess viability**: Is prospect still engaged?

#### Step 2: Take Action on Stale Deals

**For Qualified Prospect stage** (no discovery call yet):
- If last activity > 21 days: Move to "Lost - No Response"
- If potentially valid: Send fresh outreach, set 5-day follow-up task

**For Discovery/Proposal/Negotiation stages**:
- If last activity > 14 days: Log "Check-in" task
- Send check-in email (see 03-follow-ups.md for template)
- If no response within 7 days of check-in: Close as "Lost - No Response"

**For Contract stage** (signed):
- All Contract deals should have kickoff scheduled within 7 days
- If no kickoff date: Schedule immediately or escalate

#### Step 3: Data Quality Audit
Run these checks monthly (1st of month):

**Missing Data**:
- [ ] All deals have deal amount > $0
- [ ] All deals have realistic close date (within 12 months)
- [ ] All deals have primary contact linked
- [ ] All deals have service type specified

**Incorrect Data**:
- [ ] Deal stages match engagement reality (no Discovery deals older than 60 days)
- [ ] Deal names are descriptive and follow format
- [ ] Company names spelled correctly and linked to correct company record

**Action on Data Issues**:
- Correct or delete incorrect records
- Add missing information from deal notes
- Document any deletions (log as "Deal record cleaned up" in note)

### Stale Deal Resolution Options
1. **Send Re-engagement Email**: "Checking in—still a priority?" (see 03-follow-ups.md)
2. **Move to Lost**: Close with reason "No Response" or "Not a Fit"
3. **Move to Archive Deal Stage**: Create if needed for "On Hold" deals with pending events

### Clean Deal Criteria (Healthy Pipeline)
- Last activity within 7 days (active deals)
- Close dates within 90 days for Proposal/Negotiation stage
- No deals in Discovery > 60 days (move to Lost or restart)
- All required fields populated

---

## 5. Daily Deal Review Process

### Morning Routine (9 AM, 15 min)
1. Log into HubSpot
2. View Pipeline board (sorted by stage)
3. Check for **red flags**:
   - Any deals with close date TODAY or in past → Immediate action
   - Any deals with task overdue → Complete or reschedule
   - Any new activity from prospects → Respond within 2 hours
4. Identify **top 3 priorities** for day:
   - Active negotiations needing follow-up
   - Proposals expiring today/tomorrow
   - Calls scheduled
5. Log these in task list or daily notes

### End-of-Day Routine (4:30 PM, 10 min)
1. Open HubSpot deals with activity today
2. For each deal touched:
   - Verify activity logged
   - Confirm next steps are clear
   - Set follow-up task if needed
3. Log any new deals created today
4. Check for any overdue tasks—reschedule or complete
5. Note any blockers or escalations needed

### Weekly Deal Review (Every Thursday, 30 min)
1. Run stale deal report (filter: last activity > 14 days)
2. Address each stale deal (see Section 4)
3. Review all deals in Proposal stage—assess proposal status
4. Review all deals in Negotiation stage—next step?
5. Review all deals in Contract stage—kickoff scheduled?
6. Document any metrics:
   - Deals created this week
   - Deals advanced to next stage
   - Deals closed (won or lost)
   - Average deal cycle time
7. Adjust close dates if timelines shift

### Metrics to Track Manually or via HubSpot Reports
- **Pipeline Total**: Sum of all active deal amounts
- **Deals by Stage**: Count in each stage
- **Average Deal Size**: By service type
- **Deal Win Rate**: Closed Won / (Closed Won + Closed Lost)
- **Sales Cycle**: Average days from Qualified Prospect to Client

---

## 6. Decision Trees

### "Should I Move This Deal Forward?"
```
→ Has prospect responded to last contact?
  ├─ YES: Is response positive (interest, engagement)?
  │   ├─ YES: Move stage forward OR set follow-up task
  │   └─ NO: (Objection) Log objection, address in next contact
  └─ NO: (Days since contact?)
      ├─ < 7 days: Wait and monitor
      ├─ 7-14 days: Send one follow-up, set 5-day check task
      └─ > 14 days: Close as Lost or re-engage (assess viability)
```

### "Is This Deal Healthy?"
```
→ Does deal meet these criteria?
├─ 1. Prospect has engaged (at least 1 conversation)
├─ 2. Last activity within 14 days
├─ 3. Deal amount > $0
├─ 4. Close date is future + realistic (within 12 months)
├─ 5. Clear next step documented
└─ ALL YES? → Healthy deal. Continue progression.
   ANY NO? → Address gaps immediately (update data, contact prospect, or close deal)
```

---

## Templates & Resources

### Deal Name Format
```
[Company Name] - [Service/Product Type]
Example: "TechStartup Inc - Web App Development"
```

### Activity Log Template
```
Date: [MM/DD/YYYY]
Activity Type: [Call/Email/Meeting/Note]
Duration/Length: [If applicable]
Attendees: [Names and titles]
Outcome: [Positive/Neutral/Negative; be specific]
Key Points: [1-3 bullet points]
Next Step: [Specific action, owner, due date]
```

---

## Escalation Rules

### Escalate to Sales Manager If:
- Deal stalled > 30 days with no clear blocker
- Large deal (> $50K) in Proposal stage without decision
- Prospect threatening to go to competitor
- Contract negotiation in stalemate (> 10 days without progress)
- Special pricing or terms requested (verify with leadership)

---

## Summary

**Deal management is the backbone of the sales process.** Keep deals clean, move them forward systematically, and maintain data quality. Log activities consistently, review stale deals weekly, and escalate when needed.

