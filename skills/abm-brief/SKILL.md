---
name: abm-brief
description: >
  Generate a structured ABM account brief from enriched prospect data.
  Trigger phrases: "create an ABM brief", "generate account brief",
  "build a brief for [company]", "research [company]"
---

# ABM Brief Generator

## Dependencies
- None (standalone skill — Clay data provided as input)

## Inputs
- Company name (required)
- Enriched data from Clay (company info, contacts, signals) — provided as structured data or pasted text
- Tier level (Tier 1 or Tier 2)

## Workflow
1. Parse the enriched company and contact data
2. Identify the primary business pressure (growth, efficiency, transformation, compliance, speed)
3. Select 1-2 strategic triggers from: platform risk, regulatory exposure, speed-to-market pressure, post-event chaos
4. For each contact in the buying committee, generate a pain hypothesis tied to their role, tenure, and activity signals
5. Compile into the standard account brief format (see Output Format)

## Output Format

### [Company Name] — ABM Account Brief

**Company Snapshot** (2 bullets max)
- [Key fact about company size, industry, recent event]
- [Key fact about tech stack, growth trajectory, or market position]

**Trigger Hypothesis** (1 sentence)
[This company is likely under pressure to [X] because [Y].]

**Primary Persona**
[Name] — [Title]

**Their Likely KPI**
[What metric this person is measured on]

**Our POV Angle**
[The specific perspective VAN brings that addresses their pressure]

**Proof We'd Lead With**
[Case study, data point, or teaching event that validates our angle]

**Recommended Entry**
[Teaching-first approach — AI brand report, teaching event invite, or content share]

**Outreach Sequence**
[Step 1 → Step 2 → Step 3 with channel and timing]

## Quality Checks
- Brief must be one page when formatted
- Every claim must cite specific data from the enriched inputs
- Trigger hypothesis must be evidence-based, not speculative
- Outreach sequence must follow the Felix teaching-first methodology
- If data is insufficient for a confident brief, flag the gaps explicitly

## Examples
See `examples/` folder for reference briefs from Tier 1 accounts.
