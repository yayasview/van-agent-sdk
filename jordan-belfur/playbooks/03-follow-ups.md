# Follow-Up Sequences Playbook

## Purpose
Systematically re-engage prospects at the right time with personalized, value-driven follow-ups that move deals forward.

---

## 1. Identifying Deals Needing Follow-Up

### Automated Trigger-Based Identification

**Daily Check** (5 min, 9 AM):
1. Log into HubSpot
2. View Deals filtered by: **Last Activity > [Threshold Days]** (see criteria below by stage)
3. For each deal flagged, check activity date and assess action needed

### Stage-Based Inactivity Thresholds

| Deal Stage | Inactivity Threshold | Action Trigger |
|---|---|---|
| Qualified Prospect | 7 days | Send re-engagement email |
| Discovery | 5 days | Send check-in or meeting reminder |
| Proposal | 3 days | Send "How are we looking?" check-in |
| Negotiation | 2 days | Send urgency check or call directly |
| Contract | 1 day | Call directly (if not signed yet) |

### Additional Trigger Criteria

Beyond inactivity, identify deals needing follow-up if:
- **Proposal sent and expiration date is 2 days away** → Send "Final reminder—expiring soon"
- **Next scheduled action is overdue** → Log "Attempting contact" task immediately
- **Deal is in Qualified Prospect > 30 days** → Escalate or move to Lost
- **Deal is in Discovery > 60 days** → Reassess fit; may need to move to Lost
- **Prospect responded with objection** → Send objection resolution message (don't delay)
- **Budget mentioned as pending** → Follow up after stated approval date
- **Decision timeline is today or tomorrow** → Proactive check-in call

### HubSpot Report Setup (Optional, for automation)
Create saved report:
- **Filter**: Last Activity > [Stage-specific days] AND Deal Stage = [Stage]
- **View**: Deal name, Last Activity Date, Deal Amount, Next Activity Date
- **Run**: Daily at 8 AM or weekly on Monday
- **Review**: Check flagged deals against follow-up playbook

---

## 2. Follow-Up Cadence by Deal Stage

### Stage 1: Qualified Prospect (No Discovery Call Yet)

**Goal**: Schedule first conversation

**Cadence**:
- Day 0: Initial outreach email sent
- Day 2: Check-in via email if no response
- Day 4: Phone call or LinkedIn message
- Day 7: Final email before moving to Lost
- Day 10+: Close as "Lost - No Response"

**Template for Day 2 Check-In**:
```
Subject: Following up on [intro/last email]

Hi [Name],

I wanted to follow up on [my email last Tuesday/our conversation on LinkedIn/etc.].
I know you're busy, but I think there's a real opportunity here for [Company]
around [specific pain point/benefit].

Would you have 15 min this week for a quick call?
I'm available [2-3 specific times].

Best,
[Your Name]
```

**Template for Day 4 Phone Call**:
```
If voicemail: "Hi [Name], it's [Your Name] from VAN. I'm reaching out because
I think we could help [Company] with [specific need]. Give me a call back when
you get a chance—[your phone]. Looking forward to chatting!"

If they answer: "Hi [Name]! I've been trying to reach you because I think VAN
could be a great fit for [Company]'s [need]. Do you have 15 minutes now, or
should I schedule something later this week?"
```

---

### Stage 2: Discovery (Conversation Scheduled or In Progress)

**Goal**: Complete discovery call and move to Proposal (or Lost if poor fit)

**Cadence**:
- Day 0: Discovery call held
- Day 1: Send recap email (see 02-meeting-notes.md)
- Day 3: If no follow-up meeting scheduled, send check-in
- Day 7: Send light follow-up if pending info not received
- Day 14+: No response = Move to Lost or re-engage with fresh approach

**Template for Day 3 Check-In** (if proposal not yet ready):
```
Subject: Quick follow-up from our call

Hi [Name],

Thanks again for the great conversation on [date]!
Just checking in—do you have any questions about what we discussed?

As next steps, we're drafting a proposal and should have something to you by [DATE].
In the meantime, if anything comes to mind about [specific need], let me know.

Talk soon,
[Your Name]
```

**Template for Day 7 Follow-Up** (if awaiting their input):
```
Subject: Checking in—any other questions?

Hi [Name],

I wanted to check in and see if you've had a chance to think more about
[specific area discussed in call].

We're on track to send the proposal by [DATE].
Is there anything else you'd like us to include or clarify?

Quick question: What does the decision timeline look like on your end?

Best,
[Your Name]
```

---

### Stage 3: Proposal (Proposal Sent, Awaiting Response)

**Goal**: Get feedback or buy-in; move to Negotiation

**Cadence**:
- Day 0: Proposal sent (via PandaDoc link)
- Day 2: "Check in" if sent via email (e.g., "Let me know if you have questions")
- Day 5: Send "How are we looking?" follow-up
- Day 7: If expiration date approaching, send urgency message
- Day 10: Send final follow-up ("Still interested?") or close as Lost
- Day 14+: Move to Lost if no engagement

**Template for Day 5 Check-In**:
```
Subject: Checking in on the proposal

Hi [Name],

I wanted to check in and see if you've had a chance to review the proposal
we sent on [date].

Do you have any questions about [specific service/pricing/timeline]?
Or is there anything you'd like to adjust?

Looking forward to hearing from you!

Best,
[Your Name]
```

**Template for Day 7 Urgency (if expiration near)**:
```
Subject: Quick reminder—proposal expires on [DATE]

Hi [Name],

Just a quick reminder: the pricing and terms in the proposal we sent are locked
until [DATE]. After that, we'll need to update some details.

Do you have any feedback or questions? Happy to discuss any adjustments.

Let me know soon if this is still on your radar!

Best,
[Your Name]
```

**Template for Day 10 Final Follow-Up**:
```
Subject: Final check on the proposal

Hi [Name],

I haven't heard back on the proposal yet. I want to make sure this is still
a priority for you.

Are you still interested in moving forward? If so, what's the best way to
address any remaining questions?

If now's not the right time, no problem—let me know and we can reconnect later.

Best,
[Your Name]
```

**If No Response by Day 10**: Move deal to "Lost - No Response" and add note:
"Followed up 3x; prospect not engaged. Revisit Q[Next Quarter]."

---

### Stage 4: Negotiation (Active Discussion, Terms Being Finalized)

**Goal**: Close negotiation and get to Contract stage

**Cadence**:
- Day 0: First negotiation point discussed (email or call)
- Day 1: Log discussion, send recap if complex
- Day 2: If no response, send check-in with specific question
- Day 5: If no movement, escalate or re-clarify terms
- Day 7: Send contract draft if all terms agreed
- Day 10+: No progress = Escalate to manager or close

**Template for Day 2 Check-In** (if negotiating specific point):
```
Subject: Re: [Specific term/issue discussed]

Hi [Name],

Just following up on our discussion about [specific negotiation point].

On our end, we can [offer/concession], which should address your concern about [issue].
Does that work for you?

Let me know your thoughts, and we can move forward with the contract.

Best,
[Your Name]
```

**Template for Day 7** (if all terms agreed):
```
Subject: Contract for [Company] engagement

Hi [Name],

Great news! Based on our discussions, I've prepared the contract for [service/project].

I'm attaching it below for your review. Once you sign, we can get moving on [next step].

Let me know if you have any questions about the terms.

Best,
[Your Name]
```

**If Negotiation Stalls > 7 Days**:
1. Send check-in: "Any concerns about [last proposed terms]?"
2. If still no response: Call directly
3. If still stuck: Escalate to sales manager

---

### Stage 5: Contract (Sent, Awaiting Signature)

**Goal**: Get signature; move to Client stage

**Cadence**:
- Day 0: Contract sent
- Day 1: Brief follow-up email ("Let me know if you have questions")
- Day 3: If unsigned, send "Checking in" email
- Day 7: Send "Ready to move forward?" follow-up
- Day 10: Call directly (urgent)
- Day 14+: Escalate to manager or close as Lost

**Template for Day 1**:
```
Subject: Contract ready for signature

Hi [Name],

I've sent over the contract for [project/service].
Please review and let me know if you have any questions.

Once you sign, we'll schedule the kickoff and get started!

Best,
[Your Name]
```

**Template for Day 7**:
```
Subject: Ready to move forward?

Hi [Name],

Just checking in on the contract status. Are you ready to move forward,
or do you need anything from us?

Let me know what I can do to help move this across the finish line!

Best,
[Your Name]
```

**Template for Day 10** (if urgent or high-value deal):
```
Subject: Let's finalize this

Hi [Name],

I want to reach out directly because I really want to get this started
and locked in for Q[Timeframe].

Do you have 10 minutes to call? I'm available [2-3 times].

Otherwise, are there any concerns with the contract I should address?

[Your phone number]

Best,
[Your Name]
```

---

## 3. How to Draft Personalized Follow-Ups Using Templates + Deal Context

### Framework: Template + 2 Personal Details = Personalized Follow-Up

**Step 1: Select Template** (based on stage and situation)
**Step 2: Insert Deal-Specific Context**:
- Prospect company name
- Specific service discussed (not generic "services")
- Actual timeline they mentioned (not "soon")
- Their stated goal or pain point (in their words if possible)

**Step 3: Add 1 Personal Detail**:
- Reference something they said in a call ("When you mentioned the Q2 timeline...")
- Reference an industry trend relevant to them
- Acknowledge their timeline pressure ("I know you're trying to finalize this by year-end...")
- Ask a specific follow-up question ("Did the technical approach I outlined make sense?")

**Step 4: Check Tone**:
- Genuine and conversational (not salesy)
- Respectful of their time (acknowledge if following up)
- Specific (not generic)

### Example: Turning Template into Personalized Follow-Up

**Template (Generic)**:
```
Hi [Name],

Checking in on the proposal we sent. Do you have any feedback?

Let me know!
```

**Personalized Version**:
```
Hi Sarah,

I wanted to check in on the proposal we sent Friday for TechCorp's web redesign.

When we talked, you mentioned needing the site live by Q2 for the product launch.
I want to make sure we included the right timeline and scope to support that.

Have you had a chance to review? Any questions about the approach or timeline?

Looking forward to getting this started!
```

**What Changed**:
- Added prospect name (Sarah)
- Added company name (TechCorp) and specific service (web redesign)
- Referenced their stated goal (Q2 launch) in their context
- Added specific question (about timeline and scope)
- Tone is conversational and shows you listened

---

## 4. Escalation Rules for Cold Deals

### Cold Deal Definition
A deal is "cold" if:
- No response to 2+ follow-ups within normal timeframe for stage
- More than 14 days of inactivity
- Prospect explicitly expressed low priority ("Maybe next quarter")

### Escalation Path

**Step 1: One More Try** (Day 14-16)
- Send ultra-direct message: "Are you still interested in exploring this with us?"
- Wait 3 business days for response

**Step 2: Escalate to Manager** (if no response by Day 17)
- Notify sales manager: "Deal [Name] is cold. Prospect unresponsive for 14+ days. Recommend moving to Lost unless you want to intervene."
- Manager decides: Attempt final outreach, move to Lost, or add to re-engagement campaign

**Step 3: Move to Lost** (if no manager intervention within 2 days)
- Close deal as "Lost - No Response" with note: "[Number of attempts] follow-up attempts with no engagement; moved to Lost on [date]. Can revisit in Q[future]."
- Add deal to "Lost - Revisit Later" pipeline segment for quarterly re-engagement

### Re-Engagement Campaign for Cold Deals (Optional)
If deal is high-value and strategic:
1. Wait 30 days after closure
2. Send fresh, value-focused email: "Hi [Name], I came across [relevant article/news about company]. Thought you might find it interesting. Hope you're open to reconnecting soon!"
3. If they re-engage: Move deal back to appropriate stage
4. If not: Hold for next re-engagement cycle

---

## 5. Break-Up Email Criteria and Approach

### When to Send Break-Up Email (Closing Deal as Lost)

**Send Break-Up Email If**:
- Prospect explicitly said "No thanks" or "Not right now"
- Prospect said "We're going with [competitor]"
- Prospect became unresponsive for 10+ days and multiple follow-ups sent
- Mutual agreement it's not a fit

**Don't Send Break-Up Email If**:
- Prospect is just slow/busy (keep deal open, keep following up)
- It's natural seasonal downtime for their business (keep deal open, revisit later)
- They said "Not now, maybe next quarter" with promise to reconnect (schedule follow-up, don't close)

### Break-Up Email Templates

#### Template A: Prospect Explicitly Said No
```
Subject: Totally understand

Hi [Name],

Thanks for considering us on [project/need]. I totally understand if VAN isn't
the right fit at this moment.

If circumstances change or you want to explore options down the road,
please don't hesitate to reach out. We're always here to help.

Best of luck with [project/initiative]!

[Your Name]
```

#### Template B: Prospect Going With Competitor
```
Subject: Thanks for considering us

Hi [Name],

Thanks so much for the opportunity to work with you on [project].
I completely understand your decision to move forward with [competitor].

If their scope changes or you want to explore what VAN could do differently,
feel free to reach out anytime. We're rooting for your success!

All the best,
[Your Name]
```

#### Template C: Unresponsive / Moving to Lost
```
Subject: Checking in one more time

Hi [Name],

I've been trying to reach out about [project], but I haven't heard back.
I want to respect your time, so I'm going to assume this isn't a priority right now.

If you'd like to reconnect in the future, just let me know. We're always happy to chat!

Best,
[Your Name]
```

### After Sending Break-Up Email

1. **In HubSpot**: Close deal with reason:
   - "Lost - Prospect said no"
   - "Lost - Went with competitor"
   - "Lost - No response"
   - "Lost - Not a fit"

2. **Add Note**: "[Reason]. Closed on [date]. Revisit [timeframe if applicable]."

3. **Update Close Date**: Set to date deal was closed (not future date)

4. **Keep Contact Record**: Don't delete contact; can re-engage in future

5. **Document Learnings**: Brief note on what you learned (market feedback, requirements, etc.)

---

## 6. Decision Trees

### Decision Tree 1: "Should I Follow Up Today?"
```
→ Check: Was there activity on this deal in the last [X days]?
   [X = stage-specific threshold from Section 2]
├─ YES: No follow-up needed yet. Check tomorrow.
└─ NO: → Is prospect currently scheduled for a meeting/call?
    ├─ YES: Send light check-in email (optional)
    └─ NO: → Send follow-up based on template for deal stage
```

### Decision Tree 2: "What Type of Follow-Up Should I Send?"
```
→ What was the last interaction?
├─ Initial outreach/no response
│  └─ Send check-in ("Hi [Name], just wanted to follow up...")
├─ Proposal sent
│  └─ Send "How are we looking?" check-in
├─ Negotiation in progress
│  └─ Send recap or specific question on stalled point
├─ Contract sent
│  └─ Send "Ready to finalize?" message
└─ No response for 10+ days
   └─ Send final "Still interested?" then close as Lost if no response
```

### Decision Tree 3: "When to Stop Following Up (Move to Lost)?"
```
→ Deal stage?
├─ Qualified Prospect: Stop after 3 attempts over 10 days → LOST
├─ Discovery: Stop after 2 attempts over 14 days (no discovery call) → LOST
├─ Proposal: Stop after 3 attempts over 10 days → LOST
├─ Negotiation: Stop after 2 attempts over 10 days; escalate or LOST
├─ Contract: Stop after 3 attempts over 14 days; escalate before closing
└─ Any stage: If prospect explicitly says "no" → LOST immediately
```

---

## 7. Follow-Up Cadence Summary (Quick Reference)

| Stage | Days to First Follow-Up | Total Attempts | Days to Close as Lost |
|---|---|---|---|
| Qualified Prospect | 2 | 3 | 10 |
| Discovery | 5 | 2 | 14 |
| Proposal | 5 | 3 | 10 |
| Negotiation | 2 | 2 | 10+ (escalate) |
| Contract | 3 | 3 | 14+ (escalate) |

---

## 8. Special Scenarios

### Scenario: Prospect Says "Call Me Back in [Timeframe]"
**Action**:
1. Set task in HubSpot: "Follow up with [Name]" on that exact date
2. Leave deal in current stage
3. No follow-up attempts during waiting period (respect their timeline)
4. Contact them on promised date with: "Hi [Name], you mentioned checking in on [date]. Got a few minutes to chat?"

### Scenario: Prospect Goes Silent During Proposal Review
**Action**:
1. Day 5: Send single check-in ("Any questions?")
2. Day 8: Send another check-in ("Still reviewing?")
3. Day 10: Send final follow-up with direct question
4. Day 12: Close as Lost with note "Unresponsive during proposal review"

### Scenario: High-Value Deal (> $100K)
**Modified Cadence**:
- Follow up more frequently (every 3-5 days instead of 5-7)
- Escalate to sales manager after 7 days of inactivity
- Make direct phone call if email follow-ups don't get response
- Consider sending valuable content (article, case study, industry insight) as "touch" instead of just asking for status

### Scenario: Prospect Responds with Objection
**Action**:
1. Acknowledge objection in same message
2. Provide brief response addressing objection
3. Ask follow-up question to keep conversation moving
4. Don't wait; respond same day
5. Log in HubSpot as activity with objection type and response

---

## 9. Follow-Up Frequency Guardrails

### Minimum Spacing Between Follow-Ups
- Qualified Prospect stage: Minimum 2 days between attempts
- Discovery/Proposal: Minimum 3 days between attempts
- Negotiation/Contract: Minimum 2 days (can be more frequent)

### Maximum Follow-Ups Per Deal (Before Escalation or Closure)
- Never more than 4 follow-ups without sign of life
- If 3 follow-ups attempted: Escalate to manager or move to Lost
- Exception: High-value deals (> $100K) may warrant 5 attempts over 21 days

### Don't Over-Follow-Up
- Avoid multiple emails same day
- Don't follow up via email + phone + LinkedIn on same day (spread out)
- If you've followed up 3x, next attempt should be phone call, not email

---

## 10. Metrics to Track

- **Follow-up response rate**: % of follow-ups that get a response (target: 30-50%)
- **Follow-ups to close**: Average # of follow-ups before deal closes (target: 3-5 for Proposal stage)
- **Cold deal rate**: % of deals moving to "Lost - No Response" (target: < 20%)
- **Average response time**: Days from follow-up to prospect response (track by stage)

---

## Summary

**Follow-ups are the glue that holds deals together.** Use templates as the base, personalize with deal context, stick to stage-based cadences, and know when to escalate or close. Consistency and timing matter more than perfection.

