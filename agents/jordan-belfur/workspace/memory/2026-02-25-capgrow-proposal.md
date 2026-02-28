# 2026-02-25 — CapGrow Partners Proposal (Complete)

## What Happened

Built and delivered the full CapGrow Partners website redesign proposal ($66,700) in a single session. Call is tomorrow Feb 26 at 2pm CT.

## Workflow (End-to-End)

1. **Ingested deal context** — Read deal-brief.md, clay-enrichment.md, deal-context.md (Brand Primer), briefs/brief.json + raw-data.json
2. **Drafted proposal v1** using one-time-project.md template — initially a la carte structure with $38,500 foundation + 5 add-on modules
3. **Yaya feedback round 1** — VAN → Shadow Digital branding, add-ons felt random, CMS/migration/SEO should be core not add-ons
4. **Scoped with project-scope-template.xlsx** — Python (openpyxl) to read 147 line items, YES/NO each with quantities → 381.2 core hrs / $66,719 at $175/hr blended rate. Saved as scope-breakdown.md
5. **Restructured to single package** — $66,700 all-in with 5 workstreams + optional add-ons for training, SEO audit, WAIO, content outlines/writing
6. **Applied scope-definition-matrix.xlsx labels** — Switched from granular deliverables to 30-item client-facing taxonomy
7. **Yaya feedback round 2** — WAIO = $5,000 (not $1,575), content outlines = $150/ea, content writing = $350/ea
8. **Sales self-review** — Identified 11 improvements (training contradiction, Matt name-drop risk, no concrete proof, REIT gap, no urgency, etc.)
9. **Applied all 11 fixes** — Phase 4 softened, Sterling Bank anchor added, REIT gap acknowledged, urgency closer, payment amounts shown, retainer seeded
10. **Fetched case studies** from shadowdigital.cc — Bench (fintech, 1K+ pages, keywords 2K→4.9K), TSIA (200+ pages in 6 weeks, 112% mobile speed), Sterling Bank (financial services, marketing independence)
11. **Generated branded .docx** — Python (python-docx) with Shadow Digital styling: red accent #E8422F, dark table headers, numbered sections, cover page
12. **Uploaded to Google Drive** — CapGrow Partners folder (ID: `1Sx9JgdeFo3CwcXYWVJbBKEB1qqgpgleA`)

## Key Decisions

- **$66,700 not $60,000** — Present at scope-accurate price, let client trim. Don't pre-negotiate against yourself.
- **Single package, not a la carte** — Yaya: "CMS/migration/SEO should already be included." Core services feel random when split out.
- **Shadow Digital, not VAN** — This deal is sold under Shadow Digital brand, not VAN umbrella.
- **WAIO at $5,000** — Standard pricing for WAIO implementation. Previous $1,575 was just the bonus hours.
- **Case studies in proposals** — Bench, TSIA, Sterling Bank selected for relevance (migration scale, speed, financial services, marketing independence).

## Files Created/Modified

| File | Status |
|------|--------|
| `workspace/proposals/capgrow-partners/proposal-draft-v1.md` | Final markdown version |
| `workspace/proposals/capgrow-partners/scope-breakdown.md` | 390.2 hrs detailed breakdown |
| `workspace/proposals/capgrow-partners/generate_proposal_docx.py` | Python script for branded docx |
| `workspace/proposals/capgrow-partners/CapGrow Partners - Website Redesign Proposal.docx` | Final deliverable |
| Google Drive: CapGrow Partners folder | Uploaded docx |

## Lessons Learned

1. **Scope with the xlsx first, then write the proposal.** Starting with the template gave an accurate hour count and forced YES/NO decisions on every line item. Without it, the first draft had random deliverables and soft pricing.
2. **scope-definition-matrix.xlsx > project-scope-template.xlsx for client-facing labels.** The 147-line template is for internal scoping. The 30-item matrix is what goes in the proposal/SOW.
3. **Fold essentials into core, keep add-ons genuinely optional.** CMS, migration, SEO foundation, redirects = core. Training, SEO audit, WAIO, content writing = optional.
4. **Always do a sales self-review before finalizing.** The 11 fixes caught real issues (training contradiction, name-drop risk, missing proof).
5. **Case studies close deals.** Three relevant stories with real metrics > six paragraphs of "why us."
6. **python-docx works well for branded proposals.** Shadow branding (red accent, dark tables, numbered sections) translates cleanly. Script took ~15 min to write, generates professional output.
7. **Google Drive MCP has auth issues** — use `gog drive upload` instead. Works reliably.
8. **The proposal template is solid.** one-time-project.md structure (Opportunity → Outcomes → Approach → Timeline → Investment → Why Us → Next Steps) worked perfectly. Added Case Studies as section 7.
