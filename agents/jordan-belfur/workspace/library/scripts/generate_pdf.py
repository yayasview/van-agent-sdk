#!/usr/bin/env python3
"""Generate styled PDF for Dimer Health preliminary RFP response."""

import base64
from pathlib import Path
from weasyprint import HTML

# Paths
SCRIPT_DIR = Path(__file__).parent
LOGO_PATH = Path("/Users/yaya/Claude/van-agent-sdk/agents/jordan-belfur/workspace/library/assets/logos/van-logo_dark.svg")
OUTPUT_PATH = SCRIPT_DIR / "Dimer-Health_VAN-Preliminary-Response.pdf"

# Read and encode logo
logo_svg = LOGO_PATH.read_text()
logo_b64 = base64.b64encode(logo_svg.encode()).decode()

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

  @page {{
    size: letter;
    margin: 60px 65px 50px 65px;
    @bottom-center {{
      content: counter(page);
      font-family: 'Inter', sans-serif;
      font-size: 9px;
      color: #999;
    }}
  }}

  @page :first {{
    margin-top: 40px;
    @bottom-center {{
      content: none;
    }}
  }}

  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 10.5px;
    line-height: 1.65;
    color: #1a1a1a;
  }}

  /* Cover / Header */
  .cover {{
    padding-bottom: 30px;
    margin-bottom: 30px;
    border-bottom: 2px solid #1a1a1a;
  }}

  .logo {{
    width: 120px;
    margin-bottom: 35px;
  }}

  .cover h1 {{
    font-size: 28px;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #1a1a1a;
    margin-bottom: 8px;
    line-height: 1.15;
  }}

  .cover .subtitle {{
    font-size: 12px;
    font-weight: 400;
    color: #666;
    margin-bottom: 3px;
  }}

  /* Section headers */
  h2 {{
    font-size: 16px;
    font-weight: 700;
    color: #1a1a1a;
    margin-top: 32px;
    margin-bottom: 14px;
    padding-bottom: 6px;
    border-bottom: 1px solid #e0e0e0;
    letter-spacing: -0.3px;
  }}

  /* Body text */
  p {{
    margin-bottom: 12px;
  }}

  .section {{
    margin-bottom: 8px;
  }}

  /* Bold inline labels */
  strong {{
    font-weight: 600;
    color: #1a1a1a;
  }}

  /* Case study blocks */
  .case-study {{
    margin-bottom: 14px;
    padding-left: 12px;
    border-left: 2px solid #d0d0d0;
  }}

  .case-study .cs-header {{
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 2px;
  }}

  .case-study .cs-tag {{
    font-size: 9.5px;
    font-weight: 500;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  /* Phase blocks */
  .phase {{
    margin-bottom: 16px;
    padding: 14px 16px;
    background: #f8f8f8;
    border-radius: 4px;
  }}

  .phase .phase-title {{
    font-size: 12px;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 6px;
  }}

  /* Manifesto section */
  .manifesto {{
    margin-bottom: 12px;
  }}

  .manifesto-close {{
    font-weight: 500;
    font-style: italic;
    color: #333;
  }}

  /* Team table */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    margin-bottom: 16px;
    font-size: 10px;
  }}

  thead th {{
    text-align: left;
    font-weight: 600;
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #666;
    padding: 8px 10px;
    border-bottom: 2px solid #1a1a1a;
  }}

  tbody td {{
    padding: 7px 10px;
    border-bottom: 1px solid #eee;
    vertical-align: top;
  }}

  tbody tr:last-child td {{
    border-bottom: 1px solid #ccc;
  }}

  /* What's next list */
  .next-list {{
    list-style: none;
    padding: 0;
  }}

  .next-list li {{
    margin-bottom: 10px;
    padding-left: 14px;
    position: relative;
  }}

  .next-list li::before {{
    content: "—";
    position: absolute;
    left: 0;
    color: #999;
  }}

  /* Callout box */
  .callout {{
    background: #1a1a1a;
    color: #fff;
    padding: 14px 18px;
    border-radius: 4px;
    margin: 16px 0;
    font-size: 10.5px;
    font-weight: 500;
  }}

  /* Footer */
  .footer {{
    margin-top: 35px;
    padding-top: 16px;
    border-top: 1px solid #e0e0e0;
    font-size: 10px;
    color: #666;
  }}

  /* Closing line */
  .closing {{
    margin-top: 20px;
    font-size: 10.5px;
    color: #666;
  }}

  /* Differentiator blocks in Why VAN */
  .diff {{
    margin-bottom: 12px;
  }}

  .diff-title {{
    font-weight: 600;
    color: #1a1a1a;
  }}
</style>
</head>
<body>

<!-- COVER -->
<div class="cover">
  <img class="logo" src="data:image/svg+xml;base64,{logo_b64}" alt="VAN">
  <h1>Dimer Health</h1>
  <h1 style="color: #666; font-weight: 400;">Marketing &amp; Growth Partnership</h1>
  <p class="subtitle">Preliminary Response to Partner Brief</p>
  <p class="subtitle">Prepared by Veza Agency Network (VAN) &nbsp;|&nbsp; February 27, 2026</p>
</div>

<!-- EXECUTIVE SUMMARY -->
<h2>Executive Summary</h2>
<div class="section">
  <p>Dimer Health is defining a new category — Transitional Care Medicine — with clinical outcomes that speak for themselves: 67% fewer readmissions, 4.9/5 patient ratings, partnerships with leading health systems. With the Series A closed and a new product entering beta, the company is entering a fundamentally different phase — shifting from clinic-forward to product-forward, with a 10x growth ambition and a Series A announcement that will put Dimer in front of every enterprise buyer in the space.</p>
  <p>The digital engine needs to match that ambition. Right now, your website tells a different story than your clinical reality. Enterprise buyers researching Dimer online — including through AI platforms — aren't finding the company you've built. And with the announcement targeting end of March, the window to get this right is measured in weeks, not quarters.</p>
  <p>Your partner brief outlines five pillars of support: positioning, go-to-market strategy, website development, marketing execution, and sales enablement. Most agencies you evaluate will be strong in one or two of these and will subcontract or underdeliver the rest. VAN covers all five under one team, one relationship, and one engagement.</p>
  <p>We've done this in healthcare and across regulated industries — from AI-powered revenue cycle platforms to virtual care providers to global financial institutions. Engagements that start with strategy and a build, then evolve into ongoing growth partnerships. That's the model we'd bring to Dimer.</p>
  <p>We've also run Dimer Health through our proprietary AI brand representation analysis. When enterprise buyers ask AI platforms about your company, the answers are wrong — in ways that directly undermine your category creation goals. We'll present the full findings on Thursday.</p>
  <div class="callout">A full proposal — including AI brand data, a homepage concept, phased engagement framework, and investment structure — is in progress and will be presented on our next call.</div>
</div>

<!-- WHY VAN -->
<h2>Why VAN</h2>
<div class="section">
  <p>VAN is a network of specialized agencies operating as one team. That means Dimer gets the depth of a boutique — dedicated specialists in brand, development, content, SEO — without the limitations of one. No subcontracting to agencies you've never met. No gaps covered by generalists. One team, one relationship, full accountability.</p>
  <div class="diff">
    <p><span class="diff-title">AI discoverability.</span> VAN has a proprietary framework (WAIO) for optimizing how AI platforms represent your brand. In a market where enterprise buyers increasingly use ChatGPT, Perplexity, and Gemini to research vendors, this is a capability most agencies don't offer — because most agencies don't know it exists yet.</p>
  </div>
  <div class="diff">
    <p><span class="diff-title">Enablement, not dependency.</span> We build your team's capability alongside the work. CMS training, content templates, component libraries, documented systems — so your marketing team scales independently, not just through us.</p>
  </div>
</div>

<!-- EXPERIENCE -->
<h2>Experience</h2>
<div class="section">
  <p>VAN works primarily in regulated, high-stakes industries where messaging precision matters and buyer journeys are complex — healthcare, fintech, financial services, biotech, and cybersecurity. The common thread: enterprise buyers who need to trust you before they buy, multi-persona sites that speak to clinical, financial, and operational decision-makers, and marketing teams that need a partner who understands the nuance.</p>

  <div class="case-study">
    <p class="cs-header"><a href="https://adonis.com" style="color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #999;">Adonis</a> <span class="cs-tag">&nbsp;Healthcare</span></p>
    <p>AI-powered revenue cycle management platform ($31M Series B). Full-service engagement: complete rebrand and Webflow enterprise development, followed by over a year of ongoing marketing, content, and SEO partnership. Built a multi-persona site architecture serving health systems, hospitals, physician groups, and digital health organizations — with an active content engine publishing weekly across multiple categories. Adonis sells to the same enterprise healthcare buyers Dimer is targeting.</p>
  </div>

  <div class="case-study">
    <p class="cs-header"><a href="https://galileo.io" style="color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #999;">Galileo</a> <span class="cs-tag">&nbsp;Healthcare</span></p>
    <p>Virtual primary care platform founded by the creator of One Medical. Led the Webflow migration and ongoing support — working closely with their marketing team to consolidate multiple verticals (patients, employers, health plans), realign positioning across audiences, and launch several campaigns. Galileo faced the same dual-audience challenge Dimer faces: speaking to patients and enterprise buyers without diluting either message.</p>
  </div>

  <div class="case-study">
    <p class="cs-header"><a href="https://mizuhogroup.com" style="color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #999;">Mizuho Bank</a> <span class="cs-tag">&nbsp;Financial Services</span></p>
    <p>The largest migration in Webflow history. Migrated 5,000+ pages for a global financial institution, integrated with their existing systems to enable a global marketing team, and now provide ongoing support with continuous updates and enhancements. Complex audience segmentation, regulatory compliance, and multi-market coordination — publishing cycle went from multi-week to same-day.</p>
  </div>

  <div class="case-study">
    <p class="cs-header"><a href="https://beyondidentity.com" style="color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #999;">Beyond Identity</a> <span class="cs-tag">&nbsp;Cybersecurity</span></p>
    <p>Enterprise identity and access security platform. Consulted with their internal team on a full site redesign, then built the new website on Webflow while migrating away from their legacy CMS — preserving and enhancing their SEO presence throughout the transition.</p>
  </div>

  <div class="case-study">
    <p class="cs-header"><a href="https://bench.co" style="color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #999;">Bench</a> <span class="cs-tag">&nbsp;Fintech</span></p>
    <p>Migrated 1,000+ content pieces from WordPress to Webflow. Organic keywords grew from 2,000 to 4,900 (+145%). But the bigger impact was operational: Bench's marketing team went from filing tickets for every website change to publishing independently the same day. Within 6 months they'd created 450 new pages on their own — a 3X increase in content velocity that would have been impossible on their old platform.</p>
  </div>

  <p style="margin-top: 6px; font-style: italic; color: #555;">All engagements started as builds and became ongoing partnerships — working alongside marketing teams, not replacing them.</p>
</div>

<!-- RECOMMENDED ENGAGEMENT APPROACH -->
<h2>Recommended Engagement Approach</h2>
<div class="section">
  <p>Your website gets 425 visits a month. When a health system VP Googles you, they find a site built for patients — not for the enterprise buyer deciding whether to partner. When they ask ChatGPT, they get a different company entirely.</p>
  <p>The clinical product is proven. The digital engine isn't there yet. Here's how we'd change that — in three phases: <strong>Build → Attract → Convert.</strong></p>

  <div class="phase">
    <p class="phase-title">Phase 1 — Build</p>
    <p>Define what Transitional Care Medicine means — not just clinically, but commercially. How does a health system CFO hear the value differently than a clinical director? How does a patient's family member find you at 2am after a discharge? We build the positioning, the messaging frameworks, the website, and the sales materials that let Dimer show up as the enterprise platform it already is. When this phase is done, your site speaks to every buyer in your pipeline — not just patients.</p>
  </div>

  <div class="phase">
    <p class="phase-title">Phase 2 — Attract</p>
    <p>A rebuilt site with no traffic is a billboard in the desert. We drive the right people to it: SEO and AI discoverability strategy so enterprise buyers find you through Google, ChatGPT, and Perplexity — not a competitor or a UV disinfection company with a similar name. Content, backlinks, and PR that position Dimer as the authority defining this category. When this phase is working, your site is generating inbound interest — not just validating outbound pitches.</p>
  </div>

  <div class="phase">
    <p class="phase-title">Phase 3 — Convert</p>
    <p>Traffic without pipeline is a vanity metric. We turn visitors into conversations: A/B testing, account-based personalization for enterprise buyers, conversion experiments across your key actions — partner inquiries, patient bookings, app downloads. When this phase is running, you can measure the direct line from website visit to revenue.</p>
  </div>

  <p>The phases overlap and build on each other. All run on a single, predictable monthly investment — no project cliff, no re-onboarding. The engagement evolves, the budget stays consistent.</p>
  <p>We'll detail the specific deliverables, timeline, and investment structure in our full proposal — built around what we discussed today and timed to support the Series A announcement.</p>
</div>

<!-- HOW WE STRUCTURE ENGAGEMENTS -->
<h2>How We Structure Engagements</h2>
<div class="section manifesto">
  <p>The model is broken. Consultancies sell strategy they don't stick around to execute. Agencies execute without understanding the business well enough to get it right. You end up with a beautiful brand book in a drawer or a website that looks good but doesn't convert — because the people who built it never understood what you were actually selling.</p>
  <p>For a company like Dimer — defining a new category, selling to enterprise healthcare buyers, and scaling a clinical product into a commercial platform — you can't afford that gap. The team that defines the Transitional Care Medicine narrative needs to be the same team building the site, writing the content, and optimizing the conversion paths. Strategy and execution aren't separate phases. They're the same work, done by the same people, at the same time.</p>
  <p>That's how we operate. One team. One monthly investment. The deliverable mix evolves — early months are heavier on positioning, design, and development; later months shift toward content, SEO, and conversion optimization — but the budget stays consistent and the team stays the same. No project cliff where the agency launches a site and disappears. No re-onboarding a new team to execute someone else's strategy.</p>
  <p class="manifesto-close">Predictable spend that finance can plan around. Continuity that compounds. A partner that builds alongside you, not for you.</p>
</div>

<!-- PROPOSED TEAM -->
<h2>Proposed Team</h2>
<div class="section">
  <p>A dedicated team covering all pillars of your brief.</p>
  <table>
    <thead>
      <tr>
        <th style="width: 28%;">Role</th>
        <th style="width: 32%;">Name</th>
        <th style="width: 40%;">Title</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Strategic Lead</td><td>Yannick Lorenz</td><td>CGO</td></tr>
      <tr><td>Project Lead</td><td>David Georgievski</td><td>Group Accounts Director</td></tr>
      <tr><td>Account Manager</td><td>Brian Yun</td><td>Senior Account Manager</td></tr>
      <tr><td>Project Manager</td><td>Dimitrije Janjic</td><td>Projects Operations Manager</td></tr>
      <tr><td>Development Lead</td><td>Muhammad Ukasha</td><td>Head of Development</td></tr>
      <tr><td>Design Lead</td><td>Inna Ramashko</td><td>Web Designer</td></tr>
      <tr><td>SEO &amp; AEO Lead</td><td>Mina Djoric</td><td>SEO Strategist</td></tr>
      <tr><td>Content Strategist</td><td>Ivana Poposka</td><td>Copywriter</td></tr>
      <tr><td>Marketing &amp; Growth</td><td>Alberto Conceicao</td><td>Marketing Specialist</td></tr>
    </tbody>
  </table>
</div>

<!-- WHAT WE'RE PREPARING FOR THURSDAY -->
<h2>What We're Preparing for Thursday</h2>
<div class="section">
  <p>Based on our conversation, here's what we'll walk through on our next call:</p>
  <ul class="next-list">
    <li><strong>Homepage Concept</strong> — An initial design direction based on the content and Figma vision you're sharing with us. Yours to keep and use internally regardless of partner selection.</li>
    <li><strong>AI Brand Representation Analysis</strong> — Proprietary data on how AI platforms currently describe Dimer Health to enterprise buyers researching you. The findings are significant and worth walking through together.</li>
    <li><strong>Full Proposal</strong> — Phased engagement approach (Build → Attract → Convert), deliverables mapped to each phase, proposed timeline aligned to your Series A announcement, and investment structure. One predictable monthly number, evolving deliverables.</li>
    <li><strong>Measurable Outcomes</strong> — Benchmarks and success metrics tied to your growth targets.</li>
  </ul>
  <p>We'll walk through all of this live — the AI data in particular is better presented than read.</p>
</div>

<!-- FOOTER -->
<div class="footer">
  Veza Agency Network &nbsp;|&nbsp; veza.network &nbsp;|&nbsp; y@vezadigital.com
</div>

</body>
</html>
"""

html = HTML(string=html_content)
html.write_pdf(str(OUTPUT_PATH))
print(f"PDF generated: {OUTPUT_PATH}")
