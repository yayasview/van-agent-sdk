# CapGrow Partners — PageSpeed Insights Results

**URL:** https://capgrowpartners.com
**Date:** 2026-02-25
**Source:** PageSpeed Insights (web.dev)

---

## Scores Summary

| Category | Mobile | Desktop |
|----------|--------|---------|
| **Performance** | **80** | **63** |
| **Accessibility** | **90** | **90** |
| **Best Practices** | **58** | **58** |
| **SEO** | **92** | **92** |

---

## Core Web Vitals

| Metric | Mobile | Desktop | Target |
|--------|--------|---------|--------|
| **First Contentful Paint (FCP)** | 0.8s | 0.8s | < 1.8s |
| **Largest Contentful Paint (LCP)** | 2.1s | 2.6s | < 2.5s |
| **Total Blocking Time (TBT)** | 200ms | 410ms | < 200ms |
| **Cumulative Layout Shift (CLS)** | 0.069 | 0.069 | < 0.1 |
| **Speed Index** | 1.8s | 2.0s | < 3.4s |

### Assessment
- **FCP:** Good on both mobile and desktop
- **LCP:** Mobile passes (2.1s), desktop FAILS (2.6s > 2.5s threshold)
- **TBT:** Mobile borderline (200ms exactly at threshold), desktop FAILS badly (410ms)
- **CLS:** Good on both
- **Speed Index:** Good on both

---

## Failed Audits & Opportunities

### Critical Issues (FAIL)

| Issue | Impact | Details |
|-------|--------|---------|
| **Render blocking requests** | 2,550ms savings | JavaScript and CSS blocking initial render. Multiple jQuery plugins, theme scripts, and plugin CSS loading synchronously. |
| **Improve image delivery** | 1,500 KiB savings | Images not in next-gen formats (WebP/AVIF). Unoptimized file sizes. |
| **Use efficient cache lifetimes** | 355 KiB savings | Static assets served without proper cache headers. Browser re-downloads on every visit. |
| **Font display** | 70ms savings | Web fonts blocking text rendering during load. |
| **Forced reflow** | — | JavaScript forcing layout recalculations. Likely from slider/animation plugins. |
| **LCP request discovery** | — | Largest Contentful Paint element not discoverable by the browser early enough. |
| **Network dependency tree** | — | Deep chain of dependent network requests slowing load. |
| **Legacy JavaScript** | 20 KiB savings | Polyfills and legacy code served to modern browsers. |

### Warnings

| Issue | Impact |
|-------|--------|
| **Reduce JavaScript execution time** | 3.1s of JS execution on mobile |
| **Minimize main thread work** | Too much processing on the main thread |
| **DOM size** | Excessive number of DOM elements |
| **Reduce unused JavaScript** | Bundled JS not used on this page |

---

## Best Practices Issues (Score: 58)

The low Best Practices score (58/100) likely stems from:
- Deprecated APIs being used by old jQuery plugins
- Missing HTTPS on some resources
- Issues with third-party cookies
- Console errors from outdated JavaScript

---

## What This Means for the Proposal

### The bad news (for CapGrow):
1. **Desktop performance is poor** — 63/100 is below industry standards. Prospects evaluating CapGrow against competitors will notice slow load times.
2. **Best Practices at 58** — signals technical debt and an unmaintained codebase. This is the WordPress plugin sprawl in action.
3. **2,550ms of render-blocking resources** — the site loads dozens of JavaScript files and CSS stylesheets before showing anything. First impressions matter.
4. **410ms Total Blocking Time on desktop** — the site is unresponsive for almost half a second after loading. For a site that serves as a "billboard" for conference leads, this creates friction at the exact moment of evaluation.

### The good news (for the proposal):
1. **SEO score is 92** — the Yoast plugin is doing its job. Technical SEO foundation is decent.
2. **Accessibility at 90** — reasonable baseline to build from.
3. **CLS is clean** — layout doesn't shift around, which means the visual structure is stable even if slow.
4. **All of these issues are solved by migrating to Webflow** — modern hosting, optimized asset delivery, no plugin bloat, built-in performance optimization.

### Value selling angle:
- "Your site takes 2.6 seconds to show its main content on desktop — that's the device your C-suite prospects are using when they check you out after meeting you at a conference."
- "2,550ms of render-blocking resources means your site is loading 20+ JavaScript files before showing a single pixel. That's the WordPress plugin tax."
- "A Webflow rebuild eliminates the plugin dependency entirely. Our builds consistently hit 90+ Lighthouse performance scores."
