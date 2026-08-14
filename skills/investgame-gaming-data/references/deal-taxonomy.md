# InvestGame Deal Taxonomy - deal classification & terms

How a transaction maps to InvestGame's deal **Type** (specific) and **Category** (general, auto-derived
from Type), plus the commercial-terms conventions. Grounded in InvestGame's analyst deal-extraction rules.

## Type → Category

| Category | Type | When |
|----------|------|------|
| `MA` | `MA_CONTROL` | Full (100%), majority (>50%), LBO, MBO, take-private |
| `MA` | `MA_MINORITY` | Minority stake (<50%) by a **strategic** buyer |
| `EARLY_STAGE_INVESTMENT` | `ACCELERATOR_GRANT` · `SEED` · `SERIES_A` · `UNDISCLOSED_EARLY_STAGE` | Seed/A; unlabeled early (<$10M typical) → undisclosed-early |
| `LATE_STAGE_INVESTMENT` | `SERIES_B`…`SERIES_H` · `GROWTH_OR_EXPANSION` · `UNDISCLOSED_LATE_STAGE` | Growth equity or late round **with PE** (incl. PE+CVC) → growth; **CVC-only** (no PE) → undisclosed-late |
| `PUBLIC_OFFERING` | `LISTING` · `PIPE` · `FIXED_INCOME` | IPO/SPAC/direct/ATM/secondary → listing; private investment in a public co → PIPE; bond/note/loan → fixed income |
| `UA_FINANCING` | `UA_FINANCING` | Non-dilutive user-acquisition capital. Its own first-class category, not a member of M&A or fundraising |

Those are the **five visible categories**. A sixth, `OTHER`, holds only the three hidden types
(development financing, licensing, `OTHER_MISC`) and is not queryable: 19 visible types in 5 visible
categories.

## Selection rules & edge cases
- Majority stake or 100% → `MA_CONTROL`; minority by strategic → `MA_MINORITY`.
- Explicit "Series X" → that `SERIES_X`; unlabeled early <$10M → `UNDISCLOSED_EARLY_STAGE`.
- "Growth equity" / late round with **any PE** participation → `GROWTH_OR_EXPANSION`; **CVC-only** → `UNDISCLOSED_LATE_STAGE`.
- Take-private by a consortium → `MA_CONTROL` (consortium lead = Lead Investor; others = Other Investors).
- Convertible notes/bonds issued by a public company → `FIXED_INCOME` (not PIPE).
- Pre-existing stake + acquisition of the rest → `MA_CONTROL` for the new transaction (note prior stake).
- de-SPAC / SPAC merger / direct listing / ATM / secondary listing → `LISTING`.
- MBO → `MA_CONTROL` (note in description).
- **UA-financing** (`UA_FINANCING`) is a real, queryable deal type **and its own visible category**.
  It is non-dilutive, so it is neither fundraising nor M&A and never belonged to those buckets. It
  **is** counted in general analytics; the one place it is held out is the quarterly report, so that
  those comparisons stay consistent with earlier periods. Development financing, licensing and
  `OTHER_MISC` are hidden from the data entirely and are never queryable.

## Exit path (control M&A and listings)

Control acquisitions and listings carry an **exit path** - how founders or earlier owners cashed out.
It is a derived filter you can query (ask for "exits" or "first-time exits"):
- `FIRST_TIME_EXIT_MA` - founders/early backers cash out for the first time by selling control.
- `FIRST_TIME_EXIT_IPO_SPAC` - the first exit is by going public.
- `PUBLIC_TAKEOVER` - an already-public company is taken private.
- `CARVE_OUT` - a parent sells a division/asset, or a JV is unwound.
- `SECONDARY_EXIT` - a repeat exit (one financial owner sells to another, a re-sale or re-listing).
The First-Time Exits and Public-to-Private question patterns are built on these.

## Participants
- M&A: acquirer = Lead Investor/Acquirer; target = `target_company`.
- Investment: lead investor(s) = lead; co-investors = other. Always check **both** lead + other investor tables.
- Advisors live in four separate roles: sell/buy × financial/legal. IPO underwriters are **advisors**, not investors.
- Service-provider firms (banks/law) participate as advisors, not targets/investors.

## What "Size" means (by category and type)

Size is **not one formula**. Control and minority M&A read different fields, and merging them
misstates every minority deal:

| Type | Size = |
|------|--------|
| `MA_CONTROL` | Upfront EV × stake % + maximum earn-out (the transaction basis: what changed hands) |
| `MA_MINORITY` | stake % × equity value, where equity = Upfront EV - debt + cash |
| Early / Late investment | round size (total raised this round) |
| `LISTING` and `PIPE` | listing gross proceeds (offer price × shares offered) |
| `FIXED_INCOME` | total raised (principal) |

There is **no "deferred" component** in either M&A formula: control adds a maximum earn-out, minority
takes a stake share of equity value. Only the earn-out enters Size.

All monetary values are **millions, reported currency**; `Size, $M` = Size / FX rate. **FX rate =
units of reported currency per 1 USD** (USD deal → 1.0).

## Valuation & multiples conventions
- **The EV basis depends on the deal category**, and it is **never** the transaction/Max EV:
  M&A → **Upfront EV** at 100%; early/late-stage rounds → **post-money EV**; public offerings →
  **listing market cap**. Fixed income carries no meaningful EV, so no multiples.
- Distinguish **deferred** (fixed, delayed payment) from **earn-out** (contingent, performance-based).
- **Earn-out 0 vs "-":** `0` = source confirms no earn-out; `"-"` = unknown/undisclosed. Never use "-"
  when the source confirms there is none.
- Multiples shown as "2.6x". **"NM"** = not meaningful: negative, or outside the band. EV/Revenue is
  NM below 0.1x or above 20x; EV/EBITDA, EV/EBIT and EV/Cash EBITDA are NM below 0.25x or above 50x.
  **Blank means no data, which is not the same as NM.** Neither is ever zero.
- Periods: **LTM** (trailing twelve months, the default) · **CY0** (the calendar year OF THE
  ANNOUNCEMENT, not the current year) · **NTM** (forward). Where one headline multiple is shown, the
  fallback order is LTM, then CY0, then NTM. Always write **CY0 with a zero**, never with a letter O.
- Financials (revenue/EBITDA) are in **reported currency**, separate from the deal record.

## For querying (what this means for the agent)
- "M&A" → category `MA`; "fundraising/VC" → early + late stage; "raised capital" (any event) → all
  five visible categories, which includes `UA_FINANCING`. Say so when UA financing is in a total,
  since it is non-dilutive and not comparable with equity.
- "growth round" spans `SERIES_B+`, `GROWTH_OR_EXPANSION`, and `UNDISCLOSED_LATE_STAGE` - confirm scope.
- For valuation questions, default to **EV/Revenue (LTM)** on the EV basis for that deal's category
  (M&A → Upfront EV; rounds → post-money; public offerings → listing market cap) and state it in the
  methodology line. Exclude undisclosed sizes from totals; include all deals in counts/trends.
