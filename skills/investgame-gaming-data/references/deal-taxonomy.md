# InvestGame Deal Taxonomy - deal classification & terms

How a transaction maps to InvestGame's deal **Type** (specific) and **Category** (general, auto-derived
from Type), plus the commercial-terms conventions. Grounded in InvestGame's analyst deal-extraction rules.

## Type → Category

| Category | Type | When |
|----------|------|------|
| `MA` | `MA_CONTROL` | A stake of 50% or more; a smaller stake that takes the buyer's holding to 50% or more, or that the source describes as a change of control (the buyer becomes the controlling shareholder and takes over the board or management); full control, the remaining stake, LBO, MBO, take-private; a private company buying out its investor's stake (an MBO even when the stake is a minority, never a buyback); the purchase of a business, a game, an IP or rights rather than shares (a carve-out, a business transfer) |
| `MA` | `MA_MINORITY` | Existing shares bought from named holders, below 50% with no change of control, whoever the buyer (a fund included) |
| `EARLY_STAGE_INVESTMENT` | `ACCELERATOR_GRANT` · `SEED` · `SERIES_A` · `UNDISCLOSED_EARLY_STAGE` | New shares, capital to the company; an unlabelled round is typed by the company's history (below) |
| `LATE_STAGE_INVESTMENT` | `SERIES_B`…`SERIES_H` · `GROWTH_OR_EXPANSION` · `UNDISCLOSED_LATE_STAGE` | Unlabelled late round **with a PE participant** (below) → growth; without → undisclosed-late |
| `PUBLIC_OFFERING` | `LISTING` · `PIPE` · `SECONDARY_OFFERING` · `FIXED_INCOME` | IPO/SPAC/direct, a spin-off whose shares are distributed to the parent's shareholders and listed, or a secondary listing on a further exchange → listing (a secondary listing is not a secondary offering); a listed company's new shares placed with investors, one or many (private placement, bookbuild, at-the-market, underwritten follow-on), and new shares of an unlisted subsidiary of a listed group → PIPE; a holder's marketed sale through banks, and a purchase on the exchange by an outside buyer with no named seller → secondary offering; a listed issuer's bonds, notes or convertible loans → fixed income |
| `NON_DILUTIVE_FINANCING` (label "Non-dilutive Financing") | `UA_FINANCING` · `PRIVATE_DEBT` · `DEVELOPMENT_FINANCING` (label "Project Financing") | Repaid from revenue, not bought with shares; debt of a borrower not listed on the deal date is private debt, wherever the paper trades, and a listed borrower's debt is fixed income; an advance or minimum guarantee is project financing |
| Hidden | `OTHER_MISC` | Never a card; Licensing is retired, a licence is never a deal |

The money-flow rule decides between a round and M&A: new shares to the company is a round; existing
shares from named holders is M&A, typed by the control test above. A secondary offering is never M&A;
a loan is private debt or fixed income by the borrower's listing status on the announcement date.

## Selection rules & edge cases
- Explicit "Series X" → that `SERIES_X`. An unlabelled round is read from the company's history first: a round beyond Series A behind it → late, whatever the size; none → early. Only when the history is unknown does the size decide: under $10M with no late-stage signal → early, otherwise late.
- A **PE participant** is an investor of type `PRIVATE_EQUITY_AND_INST` (PE, sovereign, pension or institutional money); taking part is enough, it need not lead.
- A SAFE or convertible note sold to venture investors as a round → typed by stage; a convertible loan from a bank or credit fund → `PRIVATE_DEBT`, or `FIXED_INCOME` for a listed borrower.
- Take-private by a consortium → `MA_CONTROL` (consortium lead = Lead Investor; others = Other Investors).
- A formal tender or takeover offer → M&A by the control test, even when the shares are bought on the market.
- Pre-existing stake + acquisition of the rest → `MA_CONTROL` for the new transaction (note prior stake).
- de-SPAC / SPAC merger / direct listing / secondary listing (the same company arriving on a further exchange, never `SECONDARY_OFFERING`) → `LISTING`; an at-the-market programme or an underwritten follow-on on an exchange the company already trades on → `PIPE`.
- A loan drawn to pay an acquisition's price is no card: its lender, amount and instrument sit in the M&A card's terms. A bond or notes the acquirer issues to the market is its own debt card.
- A division sold with its own name, website or LinkedIn page → its own company card and an M&A deal (equity sale); a game, IP, rights or other assets from a portfolio → an asset card under the acquirer (asset sale).
- Non-dilutive financing and what counts as funding raised: `definitions.md`.

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
- Service-provider firms (banks/law) participate as advisors, never targets; a bank may also lend or invest on the same deal, a law firm never.

## What "Size" means (by category and type)

Size is **not one formula**. Control and minority M&A read different fields, and merging them
misstates every minority deal:

| Type | Size = |
|------|--------|
| `MA_CONTROL` | Upfront EV × stake % + maximum earn-out (the transaction basis: what changed hands); with no disclosed EV, the price paid for the stake + maximum earn-out; a remaining stake bought in the same deal sits in the earn-out, and once it is paid the size is the total actually paid, Upfront EV unchanged; when control comes by paying the company, every amount put in counts, equity and debt alike |
| `MA_MINORITY` | stake % × equity value, where equity = Upfront EV - debt + cash; stake % × Upfront EV with a "bridge missing" flag when debt and cash are unknown |
| Early / Late investment | round size (total raised this round) |
| `LISTING` and `PIPE` | listing gross proceeds (offer price × shares offered; for a PIPE the shares allotted at completion); a spin-off by distribution: the opening price on the first trading day × all shares of every class, listed or not, at that day's central-bank rate; a direct listing with no shares offered: no size (its market cap goes in its own field) |
| `SECONDARY_OFFERING` | the consideration paid for the shares: the seller's gross proceeds when a seller is named, the buyer's disclosed outlay when bought on the exchange |
| `FIXED_INCOME` and `PRIVATE_DEBT` | the principal; for a credit line the full facility amount, drawn or not |
| `UA_FINANCING` and `DEVELOPMENT_FINANCING` | the committed amount (a publisher's advance or minimum guarantee included) |
| `ACCELERATOR_GRANT` | the award |

A fixed deferred payment is part of Upfront EV (the agreed price); the earn-out field holds contingent
amounts only, and only the earn-out is added on top of the stake-weighted upfront.

All monetary values are **millions, reported currency**; `Size, $M` = Size / FX rate. **FX rate =
units of reported currency per 1 USD** (USD deal → 1.0).

## Valuation & multiples conventions
- The EV basis of every multiple, the NM rule and the periods: `definitions.md`.
- The bridge to equity value takes the minorities of a consolidated listed subsidiary as a debt-like
  line at market value; a minority deal with unknown debt and cash carries EV = price ÷ stake and a
  "bridge missing" flag. Every transaction carries its own valuation.
- **Earn-out:** `0` = the source confirms no earn-out; empty = unknown or undisclosed, never a dash.

## For querying (what this means for the agent)
- "M&A" → category `MA`; "fundraising/VC" → early + late stage; "funding raised", "raised capital"
  and non-dilutive financing → the buckets in `definitions.md`.
- "growth round" spans `SERIES_B+`, `GROWTH_OR_EXPANSION`, and `UNDISCLOSED_LATE_STAGE` - confirm scope.
- For valuation questions, default to **EV/Revenue (LTM)** on the EV basis for that deal's category
  (`definitions.md`) and state it in the methodology line. Exclude undisclosed sizes from totals;
  include all deals in counts/trends.
