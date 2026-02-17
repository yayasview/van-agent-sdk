# {{client_company}} | Project Plan

> **Template Type:** Google Sheets Project Plan (Webflow Build/Migration/Redesign)
> **Based on:** Soluna / Autura / Sofar Ocean examples
> **Usage:** Use this template to create a Google Sheets project plan for any Webflow engagement. Produces two deliverables: a **Pages inventory** and a **Project Plan** with sprint schedule, hourly breakdown, and cost summary.
> **Output:** Google Sheet created via `gog sheets create` + `gog sheets update`

---

## How to Use This Template

### Step 1: Create the Sheet

```bash
GOG_KEYRING_PASSWORD="dummy" gog sheets create "{{client_company}} | Project Plan"
```

Save the returned spreadsheet ID for all subsequent commands.

### Step 2: Pull the Client's Sitemap

Fetch `https://www.{{client_domain}}/sitemap.xml` via WebFetch. Organize the URLs into sections by directory. Identify:
- Core static pages
- Product/service pages (unique builds vs. templates with instances)
- CMS/content (blog posts, resources, videos — note total count)
- Conversion pages (forms, demos, landing pages)
- Legal/utility pages

### Step 3: Build the Pages Inventory

Write to the first tab. Use `gog sheets update` with `--values-json`.

**Column structure:**

| Column | Header | Description |
|--------|--------|-------------|
| A | Address | URL path (e.g., `sofarocean.com/products/spotter`) |
| B | Section | Logical section name |
| C | Type | `Static`, `Template`, or `Collection` |
| D | Instances | Number of pages using this template (1 for static) |
| E | Effort | `Min`, `Low`, `Medium`, `High` |
| F | Hours | Estimated dev hours for this page/template |
| G | Migrate? | `Yes` or `No` |
| H | Notes | Brief description, what content this covers |

**Row structure:**

```
Row 1:  Column headers
Row 2:  (empty separator)
Row 3:  Section header — "CORE PAGES" (or first section name)
Rows:   Page data rows
Row:    (empty separator)
Row:    Section header — next section
...
Row:    (empty separator)
Row:    "TOTAL UNIQUE BUILDS" + hours sum
Row:    "Content Migration (X posts, Y videos)" + migration hours
Row:    "TOTAL PAGE HOURS" + grand total
```

**Effort → Hours mapping (guidelines):**

| Effort | Hours | When to Use |
|--------|-------|-------------|
| Min | 2 | Legal pages, simple text-only pages |
| Low | 4 | Utility pages, simple forms, basic templates |
| Medium | 8-10 | Standard pages, CMS templates, product sub-pages |
| High | 16-20 | Hero pages, complex product pages, homepage |

**Content migration hours (guidelines):**
- Blog posts: ~0.3 hrs/post for automated migration + QA
- Videos: ~1 hr/video for embed + metadata setup
- Add 20% buffer for edge cases

### Step 4: Build the Project Plan

Write below the pages inventory (or to a second tab if manually created).

**Section A: Sprint Gantt Chart**

```
Row:  Sprint       | Sprint 1    | Sprint 2    | Sprint 3    | ...  | Support Sprint
Row:  Date         | M/D   M/D  | M/D   M/D  | M/D   M/D  | ...  | M/D   M/D
Row:  Project Setup| [block]     |             |             |      |
Row:  Development  |             | [block spans across sprints]     |
Row:  Animations   |             |             | [block]     |      |
Row:  Content Migr.|             |             |      [block spans] |
Row:  SEO          | [audit]     |             | [setup]     |      | [setup]
Row:  QA           |             |             | [QA]  | [QA]|      | [QA]
Row:  Design Conslt| [block]     |             |             |      |
Row:  Enablement   |             |             |             |      | [block]
```

Sprints = 2 weeks each. Standard work streams:
- **Project Setup** — Sprint 1 only
- **Development** — Spans most sprints (core deliverable)
- **Animations/Motion** — Starts after initial dev, overlaps
- **Content Migration** — Mid-project, after CMS architecture is built
- **SEO** — Audit in Sprint 1, then setup in later sprints
- **QA** — Starts mid-project, every other sprint
- **Design Consulting** — Sprint 1-2 only (dev-only engagements)
- **Enablement** — Final sprint(s)

For **full-service** engagements, prepend a design phase:
- Discovery & IA (2 sprints)
- UX/Wireframes (2 sprints, overlaps with discovery)
- Visual Design (2 sprints)
- Motion Concepts (1 sprint, overlaps with visual design)
- Design Review checkpoints scattered throughout

**Section B: Hourly Breakdown**

```
Row:  HOURLY BREAKDOWN
Row:  (blank) | Totals
Row:  Role    |        | Wk1 | Wk2 | Wk3 | ... | WkN
Row:  Project Manager  | XX  | 4   | 4   | 4   | ...
Row:  Webflow Developer| XX  | 0   | 8   | 16  | ...
...
Row:  (empty)
Row:  Total   | XXX    | XX  | XX  | XX  | ...
```

**Standard roles and rates:**

| Role | Rate | Typical Weekly Hours | Notes |
|------|------|---------------------|-------|
| Project Manager | $195/hr | 4 hrs/week constant | Always included |
| Webflow Developer | $175/hr | 8-16 hrs/week | Core role, ramps up after setup |
| Motion Developer | $195/hr | 8 hrs/week | Only if motion/animation required |
| Data/Content Team | $140/hr | 4-8 hrs/week | Content migration phase only |
| SEO Specialist | $225/hr | 4 hrs/week | Audit early, setup mid-late |
| QA Specialist | $140/hr | 4 hrs/week | Mid-project onward |
| Design Consultant | $195/hr | 8 hrs/week | Sprint 1-2 only (dev-only) |
| UX Designer | $175/hr | 8-12 hrs/week | Full-service only |
| UI Designer | $175/hr | 4-16 hrs/week | Full-service only |
| Creative Director | $225/hr | 4 hrs/week | Full-service only, light touch |

**Section C: Team Overview + Overview Table + Cost Breakdown**

Three side-by-side blocks:

**Team Overview (left):**
| Role | Rate |
|------|------|
| (each role) | (hourly rate) |
| Blended Rate | $XXX |

**Overview Table (center):**
| Metric | Value |
|--------|-------|
| Start Date | MM/DD/YYYY |
| Handoff Date | MM/DD/YYYY |
| Weeks | X |
| Days | X |
| Rate | $175 |
| Rate (Standard MSA) | $150 |
| Hours Total | XXX |
| Hours Weekly | XX |
| Weekly Run Rate | $X,XXX |
| Budget Per Sprint | $XX,XXX |
| Total | $XX,XXX |

**Cost Breakdown (right):**
| Work Stream | Total Hours | Cost |
|-------------|-------------|------|
| (each work stream) | XX | $X,XXX |
| **Total** | **XXX** | **$XX,XXX** |

### Step 5: Apply Visual Formatting

Use `gog sheets format` with `--format-json` and `--format-fields`.

**CRITICAL:** Always use explicit colors for BOTH background AND text in every format call. Never rely on defaults. The format fields mask should match what you're setting — use `backgroundColor,textFormat` only when the JSON includes both.

**Color palette (Google Sheets API 0-1 RGB):**

| Use | Color | RGB |
|-----|-------|-----|
| Dark header (section titles, sprint row) | Charcoal | `{"red":0.2,"green":0.2,"blue":0.2}` + white text |
| Section headers (pages inventory) | Blue | `{"red":0.26,"green":0.43,"blue":0.71}` + white text |
| Light gray (date row, sub-headers) | Gray | `{"red":0.94,"green":0.94,"blue":0.94}` + black text |
| Gantt: Setup/Design/Enablement | Orange | `{"red":0.89,"green":0.6,"blue":0.2}` + white text |
| Gantt: Development/Motion | Blue | `{"red":0.26,"green":0.43,"blue":0.71}` + white text |
| Gantt: Content Migration | Green | `{"red":0.27,"green":0.55,"blue":0.38}` + white text |
| Gantt: SEO | Purple | `{"red":0.4,"green":0.27,"blue":0.6}` + white text |
| Gantt: QA/Review | Gray | `{"red":0.55,"green":0.55,"blue":0.55}` + white text |
| Totals row | Gold | `{"red":0.84,"green":0.65,"blue":0.16}` + white text |
| Highlight (key metrics) | Yellow | `{"red":1,"green":0.95,"blue":0.6}` + black text |

**Format call pattern — ALWAYS include both bg and text:**

```bash
# Dark header with white text
gog sheets format "$SID" "Tab!A1:P1" \
  --format-json '{"backgroundColor":{"red":0.2,"green":0.2,"blue":0.2},"textFormat":{"bold":true,"foregroundColor":{"red":1,"green":1,"blue":1}}}' \
  --format-fields "backgroundColor,textFormat" -y

# Bold text on white background (for labels)
gog sheets format "$SID" "Tab!A5:A10" \
  --format-json '{"backgroundColor":{"red":1,"green":1,"blue":1},"textFormat":{"bold":true,"foregroundColor":{"red":0,"green":0,"blue":0}}}' \
  --format-fields "backgroundColor,textFormat" -y
```

**Never do this — it causes black-on-black:**
```bash
# BAD: format-fields includes backgroundColor but JSON doesn't set it
gog sheets format "$SID" "Tab!A5:A10" \
  --format-json '{"textFormat":{"bold":true}}' \
  --format-fields "backgroundColor,textFormat" -y
```

### Step 6: Verify

Export as PDF and convert to images for visual check:
```bash
gog sheets export "$SID" --format pdf --out /tmp/verify.pdf
pdftoppm -png -r 200 /tmp/verify.pdf /tmp/verify_page
```

Then use Read tool to inspect each page image.

---

## Sizing Guidelines

| Project Size | Pages | Sprints | Hours | Budget Range |
|--------------|-------|---------|-------|-------------|
| Small (Autura-size) | 10-20 | 4 (8 wks) | 150-200 | $25K-$35K |
| Medium (Sofar-size) | 20-30 | 6 (12 wks) | 300-400 | $55K-$75K |
| Large | 30-50 | 8-10 (16-20 wks) | 400-600 | $75K-$110K |
| Full-service add | +3-4 sprints | +6-8 wks | +150-200 hrs | +$30K-$40K |

## Template Variables Reference

> **For BDR agent use — do not include in final output.**

| Variable | Description | Example |
|----------|-------------|---------|
| `{{client_company}}` | Client company name | Sofar Ocean |
| `{{client_domain}}` | Client website domain | sofarocean.com |
| `{{project_type}}` | Webflow Build, Migration, Redesign | Webflow Rebuild |
| `{{start_date}}` | Project start date | 03/03/2026 |
| `{{total_weeks}}` | Total weeks including support | 14 |
| `{{total_hours}}` | Total billable hours | 384 |
| `{{total_cost}}` | Total project cost | $68,960 |
| `{{blended_rate}}` | Blended hourly rate | $178 |
