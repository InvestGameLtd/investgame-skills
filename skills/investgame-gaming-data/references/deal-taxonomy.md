# InvestGame Deal Taxonomy — deal classification & terms

How a transaction maps to InvestGame's deal **Type** (specific) and **Category** (general, auto-derived
from Type), plus the commercial-terms conventions. Grounded in the analyst ("Fira") deal-extraction rules.

## Type → Category

| Category | Type | When |
|----------|------|------|
| `MA` | `MA_CONTROL` | Full (100%), majority (>50%), LBO, MBO, take-private |
| `MA` | `MA_MINORITY` | Minority stake (<50%) by a **strategic** buyer |
| `EARLY_STAGE_INVESTMENT` | `ACCELERATOR_GRANT` · `SEED` · `SERIES_A` · `UNDISCLOSED_EARLY_STAGE` | Seed/A; unlabeled early (<$10M typical) → undisclosed-early |
| `LATE_STAGE_INVESTMENT` | `SERIES_B`…`SERIES_H` · `GROWTH_OR_EXPANSION` · `UNDISCLOSED_LATE_STAGE` | Growth equity or late round **with PE** (incl. PE+CVC) → growth; **CVC-only** (no PE) → undisclosed-late |
| `PUBLIC_OFFERING` | `LISTING` · `PIPE` · `FIXED_INCOME` | IPO/SPAC/direct/ATM/secondary → listing; private investment in a public co → PIPE; bond/note/loan → fixed income |

## Selection rules & edge cases
- Majority stake or 100% → `MA_CONTROL`; minority by strategic → `MA_MINORITY`.
- Explicit "Series X" → that `SERIES_X`; unlabeled early <$10M → `UNDISCLOSED_EARLY_STAGE`.
- "Growth equity" / late round with **any PE** participation → `GROWTH_OR_EXPANSION`; **CVC-only** → `UNDISCLOSED_LATE_STAGE`.
- Take-private by a consortium → `MA_CONTROL` (consortium lead = Lead Investor; others = Other Investors).
- Convertible notes/bonds issued by a public company → `FIXED_INCOME` (not PIPE).
- Pre-existing stake + acquisition of the rest → `MA_CONTROL` for the new transaction (note prior stake).
- de-SPAC / SPAC merger / direct listing / ATM / secondary listing → `LISTING`.
- MBO → `MA_CONTROL` (note in description).
- **UA-financing** (`UA_FINANCING`) is a real, queryable deal type — ask for it directly when you want
  it — but by InvestGame methodology it is **excluded from headline fundraising/M&A totals** (not
  comparable to equity or M&A). `OTHER`, dev-financing and licensing are excluded from analytics and
  aren't part of the queryable set — never count them.

## Exit path (control M&A and listings)

Control acquisitions and listings carry an **exit path** — how founders or earlier owners cashed out.
It is a derived filter you can query (ask for "exits" or "first-time exits"):
- `FIRST_TIME_EXIT_MA` — founders/early backers cash out for the first time by selling control.
- `FIRST_TIME_EXIT_IPO_SPAC` — the first exit is by going public.
- `PUBLIC_TAKEOVER` — an already-public company is taken private.
- `CARVE_OUT` — a parent sells a division/asset, or a JV is unwound.
- `SECONDARY_EXIT` — a repeat exit (one financial owner sells to another, a re-sale or re-listing).
The First-Time Exits and Public-to-Private question patterns are built on these.

## Participants
- M&A: acquirer = Lead Investor/Acquirer; target = `target_company`.
- Investment: lead investor(s) = lead; co-investors = other. Always check **both** lead + other investor tables.
- Advisors live in four separate roles: sell/buy × financial/legal. IPO underwriters are **advisors**, not investors.
- Service-provider firms (banks/law) participate as advisors, not targets/investors.

## What "Size" means (by category)
| Category | Size = |
|----------|--------|
| M&A (control/minority) | total consideration (upfront + deferred + max earn-out) |
| Early/Late investment | round size (total raised this round) |
| Listing | gross proceeds (offer price × shares offered) |
| PIPE | investment amount · Fixed income | principal |

All monetary values are **millions, reported currency**; `Size, $M` = Size / FX rate. **FX rate =
units of reported currency per 1 USD** (USD deal → 1.0).

## Valuation & multiples conventions
- **Upfront Enterprise Value** (100%-basis) is the anchor for all EV/Revenue & EV/EBITDA multiples —
  **never** the transaction/Max EV.
- Distinguish **deferred** (fixed, delayed payment) from **earn-out** (contingent, performance-based).
- **Earn-out 0 vs "-":** `0` = source confirms no earn-out; `"-"` = unknown/undisclosed. Never use "-"
  when the source confirms there is none.
- Multiples shown as "2.6x"; **"NM"** = not meaningful (negative or out of range); blank = no data.
  Periods: LTM (trailing, default) · NTM (forward) · CYO (current calendar year).
- Financials (revenue/EBITDA) are in **reported currency**, separate from the deal record.

## For querying (what this means for the agent)
- "M&A" → category `MA`; "fundraising/VC" → early + late stage; "raised capital" → all except `OTHER`.
- "growth round" spans `SERIES_B+`, `GROWTH_OR_EXPANSION`, and `UNDISCLOSED_LATE_STAGE` — confirm scope.
- For valuation questions, default to **EV/Revenue (LTM)** on the Upfront EV basis and state it in the
  methodology line. Exclude undisclosed sizes from totals; include all deals in counts/trends.
