# Sales BDR AI Integration Setup Guide

**System:** Sales BDR AI Assistant | **Mode:** Claude Cowork | **Network:** VAN (Veza Agency Network)

Last Updated: February 2026

---

## Integration Status Overview

| Integration | Priority | Status | Connected Capabilities | Missing Capabilities |
|---|---|---|---|---|
| **HubSpot CRM** | CRITICAL | Not Connected | — | Deal mgmt, Contact mgmt, Activity logging, Pipeline tracking |
| **Email/Gmail** | CRITICAL | Not Connected | — | Outbound email, Follow-ups, Recaps, Welcome sequences |
| **PandaDoc** | IMPORTANT | Not Connected | — | Proposal generation, Contract creation, eSignature tracking |
| **Google Calendar** | NICE-TO-HAVE | Not Connected | — | Scheduling, Meeting coordination, Availability checks |
| **Google Meet** | OPTIONAL | Not Connected | — | Call notes integration, Meeting transcription |

---

## 1. HubSpot CRM (CRITICAL)

### Purpose in BDR Workflow
HubSpot is the system of record for all sales activity. The AI assistant reads/writes deal data, manages contacts, logs activities, tracks pipeline status, and enriches prospect information. **This is a required integration** — the system cannot function without CRM access.

### Required Capabilities & Permissions
- **Contacts:** Create, read, update contact records with enriched data (company, title, industry)
- **Deals:** Create, read, update, move deals through pipeline stages
- **Activities:** Log calls, emails, meetings (linked to contacts/deals)
- **Pipeline:** Read pipeline configuration, move deals between stages
- **Companies:** Read company info for account-based targeting
- **Custom Objects:** (If using) Read/write custom fields for BDR-specific workflows
- **Lists:** Read/create smart lists for segmentation
- **Timeline:** Log all outbound activities for deal context

### Setup in Claude Cowork

#### Prerequisites
1. Active HubSpot account with Sales Hub tier or higher
2. User must have API access enabled (not restricted by HubSpot workspace)
3. Create private app in HubSpot for dedicated AI access:
   - Go to HubSpot Settings → Integrations → Private Apps
   - Create new app named "Sales BDR AI"
   - Grant scopes:
     - `crm.objects.contacts.read`
     - `crm.objects.contacts.write`
     - `crm.objects.deals.read`
     - `crm.objects.deals.write`
     - `crm.objects.companies.read`
     - `crm.objects.activities.write`
     - `crm.lists.read`
   - Copy private app access token

#### MCP Connector Installation
1. In Claude Cowork, navigate to **Integrations → Available Connectors**
2. Search for and select **HubSpot**
3. Click **Connect**
4. Paste private app access token when prompted
5. Verify connection by testing contact/deal read operations

#### Alternative: Manual API Credentials
If HubSpot connector not available in your Cowork version:
- Provide HubSpot API token to system admin to configure in environment
- Verify with: `curl -H "Authorization: Bearer [TOKEN]" https://api.hubapi.com/crm/v3/objects/contacts`

### Data Flow (HubSpot ↔ AI System)

**Inbound (AI reads):**
- Contact records (name, email, phone, company, title, industry, custom fields)
- Deal records (deal name, stage, value, close date, associated contacts)
- Activity history (previous calls, emails, meetings on contact)
- Pipeline configuration (stages, default values)
- Company enrichment data

**Outbound (AI writes):**
- New contact creation (from prospect lists/web forms)
- Activity logging (calls, emails, research notes)
- Deal updates (move to next stage, update close date, add notes)
- Contact field updates (role confirmation, company info refinement)

### Fallback Workflow (If HubSpot Not Connected)

1. **Manual Contact Management:**
   - Prospect data provided via CSV or Google Sheets
   - AI generates outreach strategy but cannot log to CRM
   - User manually enters activities into HubSpot after AI interaction
   - Track deal progress externally in spreadsheet

2. **Activity Logging:**
   - AI generates activity summary (call notes, email sent, next steps)
   - User copies/pastes summary into HubSpot activity timeline
   - No real-time sync — risk of lost data or duplicates

3. **Pipeline Tracking:**
   - User updates deal stage in HubSpot independently
   - AI cannot advise on stage-specific actions until informed of stage change
   - Decision-making is delayed and error-prone

**Recommendation:** Do not proceed without HubSpot integration. The manual workaround adds hours of overhead per day.

---

## 2. Email/Gmail (CRITICAL)

### Purpose in BDR Workflow
Sends all outbound communication: follow-up emails, meeting recaps, proposal introductions, cold outreach sequences, and welcome emails. Essential for maintaining prospect communication cadence and proving engagement history.

### Required Capabilities & Permissions
- **Send emails:** Compose and send from team email address
- **Email templates:** Store and populate BDR email sequences
- **Read sent folder:** Verify deliverability and track sent email history
- **Label/filter:** Organize prospect conversations and track responses
- **Thread tracking:** Link emails to CRM contacts for context
- **BCC to address:** Allow system to BCC a central monitoring inbox for compliance

### Setup in Claude Cowork

#### For Gmail (Recommended)

1. **Create dedicated Gmail service account** (optional but recommended):
   - Create new Google Workspace account: `bdr-ai@yourcompany.com`
   - Add to company mailing lists if needed
   - Grant appropriate labels/filters by admin

2. **Enable API Access:**
   - Go to Google Cloud Console → APIs & Services
   - Enable **Gmail API**
   - Create OAuth 2.0 credential (type: "Desktop application")
   - Download credentials JSON

3. **Connect in Claude Cowork:**
   - Navigate to **Integrations → Available Connectors**
   - Search for **Gmail** or **Google Mail**
   - Click **Connect**
   - Paste OAuth credentials or authenticate via browser
   - Grant permissions when prompted

#### For Generic Email (SMTP Fallback)

If Gmail connector unavailable:
- Provide SMTP credentials (server, port, username, password)
- Configure in environment: `EMAIL_SMTP_SERVER`, `EMAIL_SMTP_PORT`, `EMAIL_FROM`
- Test with: `sendmail -v recipient@example.com`

### Data Flow (Email ↔ AI System)

**Outbound (AI sends):**
- Follow-up emails (templated, personalized)
- Meeting confirmations and recaps
- Proposal introduction emails
- Welcome/nurture sequences
- Cold outreach (with delay/throttling)

**Inbound (AI reads):**
- Delivery status and bounce notifications
- Reply detection (prospect responded to outreach)
- Email thread history for context on ongoing conversations

**Integration with HubSpot:**
- Email activity logged to HubSpot contact timeline
- Prospect replies trigger CRM activity notifications
- Email send timestamp recorded for pipeline progression

### Fallback Workflow (If Email Not Connected)

1. **Manual Email Composition:**
   - AI generates email draft (subject + body)
   - User copies draft into Gmail/Outlook
   - User manually sends and logs to HubSpot
   - No tracking of delivery or response

2. **Sequence Management:**
   - AI cannot execute multi-step email sequences
   - User must manually send each follow-up email
   - Delays between sends (hours/days instead of minutes)
   - Risk of duplicate sends or missed follow-ups

3. **Response Tracking:**
   - User must manually monitor inbox for replies
   - AI cannot detect incoming prospect responses
   - No real-time engagement signals to inform next action

**Recommendation:** Connect email immediately after HubSpot. Waiting adds 30+ minutes per day of manual work.

---

## 3. PandaDoc (IMPORTANT)

### Purpose in BDR Workflow
Creates and tracks proposals and contracts. AI generates proposal content, PandaDoc formats and delivers, system tracks signature status and sends automated reminders. Used for deal acceleration and quote delivery within hours instead of days.

### Required Capabilities & Permissions
- **Template management:** Access pre-built proposal/contract templates
- **Document creation:** Generate new proposals from templates with data merge
- **Recipient management:** Add signers, send documents, track viewing/signing activity
- **Signature tracking:** Monitor signature progress and completion
- **Data merge:** Auto-populate prospect/deal data into proposals
- **Folder organization:** Store docs by deal or prospect for audit trail
- **API webhooks:** Notify AI system when signatures are received

### Setup in Claude Cowork

#### Prerequisites
1. Active PandaDoc workspace with API access (requires plan upgrade)
2. Pre-built proposal and contract templates in PandaDoc
3. PandaDoc API token

#### MCP Connector Installation
1. In Claude Cowork, navigate to **Integrations → Available Connectors**
2. Search for **PandaDoc**
3. Click **Connect**
4. Paste PandaDoc API token when prompted
5. Authorize API access to templates and documents

#### Manual Setup (If Connector Unavailable)
- Provide API token to system admin
- Configure: `PANDADOC_API_KEY` in environment
- Verify with: `curl -H "Authorization: Bearer [TOKEN]" https://api.pandadoc.com/public/v1/users/me`

### Data Flow (PandaDoc ↔ AI System)

**Outbound (AI initiates):**
- Document creation requests (template ID, data fields to merge)
- Recipient list (signer names, emails, signing order)
- Document sending triggers
- Reminder scheduling for pending signatures

**Inbound (AI reads):**
- Document status (draft, sent, viewed, signed, completed)
- Signer activity (who viewed, who signed, timestamp)
- Signature completion notifications
- Download links for completed documents

**Integration with HubSpot:**
- Document link stored in deal record
- Signature status updates deal "proposal stage"
- Signature completion can auto-trigger next pipeline stage

### Fallback Workflow (If PandaDoc Not Connected)

1. **Manual Proposal Creation:**
   - AI writes proposal content (structure, talking points)
   - User opens PandaDoc template, manually fills fields
   - User manually sends to prospect and tracks status
   - 15-30 minute delay per proposal

2. **Signature Tracking:**
   - User monitors PandaDoc inbox for signature updates
   - AI cannot see signature status until user reports it
   - User must manually update HubSpot deal stage
   - Risk of proposals forgotten/expiring unsigned

3. **Automated Reminders:**
   - System cannot auto-send signature reminders
   - User must manually send reminder emails
   - Follow-up sequence breaks down

**Recommendation:** Nice-to-have for workflow efficiency. Use if you generate 5+ proposals/week. For lower volume, manual process is acceptable.

---

## 4. Google Calendar (NICE-TO-HAVE)

### Purpose in BDR Workflow
Checks team member availability for meeting scheduling, avoids double-booking, suggests optimal meeting times, and auto-books confirmed meetings. Improves meeting close rate by reducing scheduling friction.

### Required Capabilities & Permissions
- **Read calendar:** View availability for team members
- **Create events:** Book confirmed meetings on team member calendar
- **Read busy times:** Identify conflicts and availabile slots
- **Attendee management:** Add prospects as meeting attendees
- **Timezone handling:** Schedule across regions correctly

### Setup in Claude Cowork

#### Prerequisites
1. Team members' Google Workspace calendars must be shared with service account
2. Google Calendar API enabled in Google Cloud Console
3. OAuth credentials for service account

#### MCP Connector Installation
1. In Claude Cowork, navigate to **Integrations → Available Connectors**
2. Search for **Google Calendar**
3. Click **Connect**
4. Authenticate and authorize calendar access
5. Test by checking current week's availability

#### Shared Calendar Setup
- Team lead shares team calendar with `bdr-ai@yourcompany.com`
- Grant "Make changes to events" permission
- Verify bot can create events

### Data Flow (Google Calendar ↔ AI System)

**Inbound (AI reads):**
- Team member availability (busy/free blocks)
- Existing meeting schedule
- Timezone information
- Calendar preferences (do-not-schedule times)

**Outbound (AI writes):**
- Meeting confirmation events for agreed times
- Meeting attendees (prospect + team)
- Meeting description with prep notes

### Fallback Workflow (If Google Calendar Not Connected)

1. **Manual Scheduling:**
   - AI suggests 2-3 time slots to prospect
   - Prospect responds with preference
   - User manually checks calendar and confirms
   - User creates calendar event manually
   - Adds 10-15 minutes overhead per meeting

2. **Availability Checking:**
   - AI cannot verify team availability
   - Double-booking possible if team member accepts another meeting
   - Coordination required between AI and team

**Recommendation:** Defer until HubSpot and Email are working. Low impact on immediate BDR workflow.

---

## Integration Setup Checklist

### Phase 1: Minimum Viable Setup (Day 1)
- [ ] HubSpot CRM — Private app created, token obtained
- [ ] HubSpot connector installed in Claude Cowork
- [ ] HubSpot connection tested (successful contact/deal query)
- [ ] Gmail account created or designated for AI use
- [ ] Gmail API enabled in Google Cloud Console
- [ ] Gmail connector installed in Claude Cowork
- [ ] Gmail connection tested (successful test email sent)
- [ ] BDR team notified that system is live

### Phase 2: Complete Workflow (Week 1)
- [ ] PandaDoc workspace upgraded to API plan (if not already)
- [ ] Proposal templates created/uploaded to PandaDoc
- [ ] PandaDoc API token obtained
- [ ] PandaDoc connector installed in Claude Cowork
- [ ] Test proposal generation and signature request
- [ ] HubSpot-Gmail integration verified (emails logged to contacts)

### Phase 3: Enhancement (Week 2+)
- [ ] Google Calendar shared with AI service account
- [ ] Google Calendar connector installed
- [ ] Test meeting scheduling
- [ ] Monitor system performance and adjust email throttling
- [ ] Gather feedback from BDR team on AI-generated content quality

---

## Troubleshooting

### HubSpot Connection Issues
**Problem:** "Unauthorized" or "Invalid token" error
- **Solution:** Verify private app token hasn't expired. Regenerate in HubSpot Settings if needed.

**Problem:** Cannot read deals or contacts
- **Solution:** Check private app scopes include required permissions. Regenerate app if scopes were modified.

**Problem:** Activities not logging to HubSpot
- **Solution:** Verify contact ID is correctly passed to activity creation API. Check timestamp format (ISO 8601).

### Gmail Connection Issues
**Problem:** "Gmail API not enabled" error
- **Solution:** Go to Google Cloud Console → APIs & Services → Enable Gmail API. Wait 1-2 minutes for propagation.

**Problem:** Emails not sending
- **Solution:** Check OAuth credentials are current. Ensure email account has not hit daily send limit (Gmail limit: 500/day).

**Problem:** Emails not appearing in "Sent" folder
- **Solution:** Confirm OAuth scopes include `https://www.googleapis.com/auth/gmail.send` and `https://www.googleapis.com/auth/gmail.readonly`.

### PandaDoc Connection Issues
**Problem:** Templates not visible in connector
- **Solution:** Verify API token has template read permission. Check PandaDoc workspace plan includes API access.

**Problem:** Documents not creating
- **Solution:** Validate template ID exists. Check data merge fields match template placeholders exactly.

---

## Security & Compliance Notes

1. **API Tokens:** Store all API tokens in environment variables, not in code or config files.
2. **Email Compliance:** Enable BCC to compliance inbox for all outbound emails. Maintain audit trail.
3. **Data Retention:** Set PandaDoc document retention policy (recommend: keep for 1 year minimum).
4. **Access Control:** Limit HubSpot private app permissions to minimum required scopes.
5. **Rate Limiting:** Implement throttling on email sends to avoid spam filters (recommend: max 50 emails/hour per domain).
6. **Backup:** Export CRM contacts and deals weekly to protect against data loss.

---

## Integration Capability Matrix

| Workflow Step | HubSpot | Email | PandaDoc | Calendar |
|---|---|---|---|---|
| Prospect research & enrichment | ✓ Read | — | — | — |
| Personalized cold email send | ✓ Log | ✓ Send | — | — |
| Meeting request + scheduling | ✓ Log | ✓ Send | — | ✓ Check + Book |
| Proposal generation & delivery | ✓ Log | — | ✓ Generate | — |
| Signature tracking | ✓ Update | — | ✓ Track | — |
| Meeting recap + next steps | ✓ Log | ✓ Send | — | ✓ Update |
| Deal stage progression | ✓ Update | ✓ Log | ✓ Trigger | — |

---

## Support & Next Steps

1. **For MCP Connector Issues:** Consult Claude Cowork documentation or contact Anthropic support
2. **For Integration-Specific Questions:**
   - HubSpot: https://developers.hubspot.com
   - Gmail: https://developers.google.com/gmail/api
   - PandaDoc: https://api.pandadoc.com/docs
   - Google Calendar: https://developers.google.com/calendar
3. **For System Issues:** Contact VAN (Veza Agency Network) technical team with error logs

---

**Document Version:** 1.0 | **Last Reviewed:** February 2026
