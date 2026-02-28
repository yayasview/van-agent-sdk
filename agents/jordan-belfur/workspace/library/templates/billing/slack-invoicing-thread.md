# Slack Invoicing Thread Reply

> **Template Type:** Billing/invoicing details for accounting team
> **Trigger:** Immediately after posting the onboarding notification in #van-new-account-onboarding
> **Format:** Reply in the thread of the onboarding notification message (not a new channel message)
> **Always tag:** <@U01LN9D998S> (Julia R. Nicoloski, Executive Assistant - Finance)

---

## Message Format

```
<@U01LN9D998S> invoicing should be {{invoicing_cadence}}:
{{invoice_line_items}}
```

---

## Field Instructions

### Invoicing Cadence

> **BDR Instructions:** Determine from the signed proposal/contract. Common formats:
> - `monthly` — for retainer/support plan engagements
> - `milestone-based` — for fixed projects with payment splits (e.g., 50/40/10)
> - `one-time` — for single-payment engagements

### Invoice Line Items

> **BDR Instructions:** List each invoice as a bullet point with: amount, timing, and payment terms.
>
> **For retainer/monthly engagements:**
> ```
> • First invoice to go out immediately: $X,XXX, net-30
> • Next invoice to go out in 30 days: $X,XXX, net-30
> ```
> (Continue pattern for the duration of the commitment)
>
> **For fixed project (milestone-based):**
> ```
> • Invoice 1 (50%) to go out immediately: $XX,XXX, due at signing
> • Invoice 2 (40%) to go out net-30 post kickoff: $XX,XXX, net-30
> • Invoice 3 (10%) to go out at handoff: $X,XXX, due at handoff
> ```
>
> **For hybrid (initial project + retainer):**
> ```
> • Project deposit to go out immediately: $XX,XXX, due at signing
> • Monthly retainer begins [date]: $X,XXX/mo, net-30
> ```

---

## CRITICAL: Verification Rule

> **If the invoicing schedule is NOT specifically defined in the proposal or contract, DO NOT generate this message. Instead, ask Yaya for verification before posting.**
>
> Things that require verification:
> - Payment schedule not explicitly stated in the proposal
> - Discounted or custom payment arrangements mentioned in meeting notes but not in the signed contract
> - Multi-entity billing (e.g., different VAN agencies invoicing different portions)
> - Non-standard payment terms (anything other than net-30 or due-at-signing)

---

## Examples

### Retainer (Monthly)

```
<@U01LN9D998S> invoicing should be monthly:
• First invoice to go out immediately: $5,000, net-30
• Next invoice to go out in 30 days: $5,000, net-30
```

### Fixed Project (50/40/10)

```
<@U01LN9D998S> invoicing should be milestone-based:
• Invoice 1 (50%) to go out immediately: $10,500, due at signing
• Invoice 2 (40%) to go out net-30 post kickoff: $8,400, net-30
• Invoice 3 (10%) to go out at handoff: $2,100, due at handoff
```

### 3-Month Retainer with Higher First Month

```
<@U01LN9D998S> invoicing should be monthly:
• First invoice to go out immediately: $8,000, net-30
• Month 2 invoice to go out in 30 days: $5,000, net-30
• Month 3 invoice to go out in 60 days: $5,000, net-30
```

---

## Template Variables Reference

> **For BDR agent use — do not include in final output.**

| Variable | Description | Source |
|----------|-------------|--------|
| `{{invoicing_cadence}}` | Monthly, milestone-based, or one-time | Proposal payment terms |
| `{{invoice_line_items}}` | Bullet list of invoices with amounts and timing | Proposal payment schedule |
