# InvestGame Deal Taxonomy - deal classification & terms

How a transaction maps to InvestGame's deal **Type** (specific) and **Category** (general, auto-derived
from Type), plus the commercial-terms conventions. Grounded in InvestGame's analyst deal-extraction rules.

## Type → Category

| Category | Type | When |
|----------|------|------|
| `MA` | `MA_CONTROL` | More than 50%, full control, the remaining stake, LBO, MBO, take-private |
| `MA` | `MA_MINORITY` | Existing shares bought from named holders below 50%, whoever the buyer (a fund included) |
| `EARLY_STAGE_INVESTMENT` | `ACCELERATOR_GRANT` · `SEED` · `SERIES_A` · `UNDISCLOSED_EARLY_STAGE` | New shares, capital to the company; unlabelled → early when no round beyond Series A behind it or under $10M with no late signal |
| `LATE_STAGE_INVESTMENT` | `SERIES_B`…`SERIES_H` · `GROWTH_OR_EXPANSION` · `UNDISCLOSED_LATE_STAGE` | Unlabelled late round **with a PE participant** → growth; without → undisclosed-late |
| `PUBLIC_OFFERING` | `LISTING` · `PIPE` · `SECONDARY_OFFERING` · `FIXED_INCOME` | IPO/SPAC/direct, or a secondary listing on a further exchange → listing (a secondary listing is not a secondary offering); a listed company's new shares placed with investors, one or many (private placement, bookbuild, at-the-market, underwritten follow-on) → PIPE; a holder's marketed sale through banks → secondary offering; a listed issuer's notes → fixed income |
| `UA_FINANCING` (label "Non-dilutive Financing"; the value is kept for the API's category filter) | `UA_FINANCING` · `PRIVATE_DEBT` · `DEVELOPMENT_FINANCING` (label "Project Financing") | Repaid from revenue, not bought with shares; a private borrower's loan is private debt whatever the paper; an advance or minimum guarantee is project financing |
| Hidden | `OTHER_MISC` | Never a card; Licensing is retired, a licence is never a deal |

The money-flow rule decides between a round and M&A: new shares to the company is a round; existing
shares from named holders is M&A by the stake. A secondary offering is never M&A; a loan is private
debt or fixed income by the borrower's listing status on the announcement date.

## Selection rules & edge cases
- Majority stake or 100% → `MA_CONTROL`; a minority block from named holders → `MA_MINORITY`, whoever the buyer.
- Explicit "Series X" → that `SERIES_X`; unlabeled → the company's history first (a round beyond Series A behind it → late), and only when the history is unknown, under $10M with no late signal → `UNDISCLOSED_EARLY_STAGE`.
- An unlabelled late round with a **PE participant** → `GROWTH_OR_EXPANSION`; without one → `UNDISCLOSED_LATE_STAGE`.
- Take-private by a consortium → `MA_CONTROL` (consortium lead = Lead Investor; others = Other Investors).
- Convertible notes/bonds issued by a public company → `FIXED_INCOME` (not PIPE).
- Pre-existing stake + acquisition of the rest → `MA_CONTROL` for the new transaction (note prior stake).
- de-SPAC / SPAC merger / direct listing / secondary listing (the same company arriving on a further exchange, never `SECONDARY_OFFERING`) → `LISTING`; an at-the-market programme or an underwritten follow-on on an exchange the company already trades on → `PIPE`.
- MBO → `MA_CONTROL` (note in description).
- **Non-dilutive financing** (`UA_FINANCING`, `PRIVATE_DEBT`, `DEVELOPMENT_FINANCING`) is real,
  queryable and its own visible category. It is neither fundraising nor M&A, never belonged to
  those buckets, and is not counted as "funding raised": report it as its own row. The quarterly
  report holds out UA financing, project financing and secondary offerings, so that those
  comparisons stay consistent with earlier periods; private debt stays in it. Only `OTHER_MISC` is
  hidden from the data entirely and is never queryable.

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
| `MA_MINORITY` | stake % × equity value, where equity = Upfront EV - debt + cash; stake % × Upfront EV with a "bridge missing" flag when debt and cash are unknown |
| Early / Late investment | round size (total raised this round) |
| `LISTING` and `PIPE` | listing gross proceeds (offer price × shares offered) |
| `SECONDARY_OFFERING` | gross proceeds to the selling holder(s) (offer price × shares sold) |
| `FIXED_INCOME` and `PRIVATE_DEBT` | total raised (principal) |
| `UA_FINANCING` and `DEVELOPMENT_FINANCING` | the committed amount (a publisher's advance or minimum guarantee included) |
| `ACCELERATOR_GRANT` | the award |

A fixed deferred payment is part of Upfront EV (the agreed price); the earn-out field holds contingent
amounts only, and only the earn-out is added on top of the stake-weighted upfront.

All monetary values are **millions, reported currency**; `Size, $M` = Size / FX rate. **FX rate =
units of reported currency per 1 USD** (USD deal → 1.0).

## Valuation & multiples conventions
- **The EV basis depends on the deal category**, and it is **never** the transaction/Max EV:
  M&A → **Upfront EV** at 100%; early/late-stage rounds → **post-money EV**; public offerings →
  **listing market cap**. Fixed income, private debt and non-dilutive money carry no EV, so no
  multiples. The bridge to equity value takes the minorities of a consolidated listed subsidiary as
  a debt-like line at market value; a minority deal with unknown debt and cash carries EV = price ÷
  stake and a "bridge missing" flag. Every transaction carries its own valuation.
- A **deferred** payment (fixed, delayed) sits inside Upfront EV; **earn-out** is contingent only.
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
- "M&A" → category `MA`; "fundraising/VC" → early + late stage; "raised capital" (any event) → the
  four equity and public-offering categories (`MA`, early, late, `PUBLIC_OFFERING`). Non-dilutive
  financing (`UA_FINANCING` category) is not funding raised: show it as its own row when asked, and
  say so, since it is repaid from revenue and not comparable with equity.
- "growth round" spans `SERIES_B+`, `GROWTH_OR_EXPANSION`, and `UNDISCLOSED_LATE_STAGE` - confirm scope.
- For valuation questions, default to **EV/Revenue (LTM)** on the EV basis for that deal's category
  (M&A → Upfront EV; rounds → post-money; public offerings → listing market cap) and state it in the
  methodology line. Exclude undisclosed sizes from totals; include all deals in counts/trends.
