# Jordan Belfur — Memory Context

## Team Preferences

- Yaya prefers proposals created as Google Docs (via gogcli `gog docs write --markdown`)
- Project plans are always Google Sheets with visual formatting (colored gantt blocks, dark headers)
- Client-facing proposals use `templates/proposals/one-time-project.md` template
- Internal briefs use the 12-section format modeled on the Kooth brief (see `templates/internal-briefs/`)
- Agency name for client-facing work: **Shadow Digital** (not VAN — VAN is the internal network name)
- Standard payment terms: 50/40/10 split (signing / net-30 / handoff) for proposals; 50/50 for internal briefs
- Always include WAIO as a no-cost bonus ($5,000 value)
- Always include 2 weeks post-launch support as included

## Active Deals — Context Notes

### Sofar Ocean
- **Discovery call:** Feb 12, 2026 (notes in Granola)
- **Key contacts:** Michelle (primary), Rosie (day-to-day review lead) — full names/titles/emails still needed
- **Situation:** 5-year-old ocean tech startup, two product lines (Spotter hardware, Wayfinder SaaS), two distinct audiences. Website is "duct tape and bubble gum" — no one agency has ever owned it. Team has zero Webflow experience.
- **Proposals delivered:** Two options prepared — dev-only ($68,960 / 384 hrs / 12 wks) and full-service with design ($102,360 / 568 hrs / 18 wks)
- **Deliverables created:**
  - Project Plan sheet: `130VwrxmtVLHbnJ5ZYnRe50TeSmkfWvxEM17_-ojTd_Y`
  - Internal Brief doc: `1OZXEttwHfrt9U4nlSAWL8Oe6Xj3GNwDRWzVArYXNUsg`
  - Client Proposal doc: `1NFOPQH1RFzIV19G5_7CG848zlW1WT0l25xzEfn8jsSc`
- **Next steps:** Deliver proposals to Rosie (10am meeting), get preference on Option A vs B, confirm contact details, assign internal team

## Patterns & Learnings

### Proposal Workflow (proven sequence)
1. Pull meeting notes from Granola (`query_granola_meetings`)
2. Fetch client sitemap (`WebFetch` on `/sitemap.xml`)
3. Create project plan sheet (`gog sheets create` → `update` → `format`)
4. Create internal brief Google Doc (12-section format from Kooth template)
5. Create client-facing proposal Google Doc (from `one-time-project.md` template)
6. Update HubSpot deal record with deliverable links

### Google Sheets Formatting
- Always run `gog sheets metadata` before formatting to confirm tab names
- **Never** use a format-fields mask that includes fields not explicitly set in the JSON — this causes fields to reset to defaults (black background)
- Rate limit: ~60 write requests/minute. Batch format calls, and if rate-limited, wait 5-10 seconds and retry
- `gog` cannot create/rename/delete tabs — only the user can do this in the UI
- Export to PDF + pdftoppm to verify formatting visually before delivering

### Reference Sheets
- **Soluna project plan (style reference):** `1tPZ3MgWUcE0QUVdnwxtpjt2-Ek-e6jQqf1EGDpxDVOM`
- **Autura project plan (structure reference):** `1cdF2XPVDdzsP0ygC1PvaqTD0qH83OdJpdd04ser0xGA`

### Standard Rates
| Role | Rate |
|------|------|
| Project Manager | $195/hr |
| Webflow Developer | $175/hr |
| Motion Developer | $195/hr |
| UX Designer | $175/hr |
| UI Designer | $175/hr |
| Creative Director | $225/hr |
| SEO Specialist | $225/hr |
| QA Specialist | $140/hr |
| Data/Content Team | $140/hr |
| Web Designer | $175/hr |
