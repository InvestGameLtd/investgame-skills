# InvestGame deal taxonomy - types, categories and terms

What each deal **Type** (specific) and **Category** (general, derived from the Type) means, and how to
read a deal's exit path, participants and size.

## Type → Category

| Category | Type | What it is |
|----------|------|-----------|
| `MA` | `MA_CONTROL` | An acquisition of control: a stake of 50% or more, or a change of control; LBO, MBO and take-private included; also the purchase of a business, a game or an IP rather than shares |
| `MA` | `MA_MINORITY` | A purchase of existing shares that leaves the buyer below control |
| `EARLY_STAGE_INVESTMENT` | `ACCELERATOR_GRANT` · `SEED` · `SERIES_A` · `UNDISCLOSED_EARLY_STAGE` | New shares, capital to the company, at an early stage; `ACCELERATOR_GRANT` is accelerator or grant money (the award), not always shares. `SEED` covers pre-seed, angel and pre-Series A rounds |
| `LATE_STAGE_INVESTMENT` | `SERIES_B`…`SERIES_H` · `GROWTH_OR_EXPANSION` · `UNDISCLOSED_LATE_STAGE` | New shares at a later stage. A round labelled with a plus ("Series C+") keeps its series |
| `PUBLIC_OFFERING` | `LISTING` · `PIPE` · `SECONDARY_OFFERING` · `FIXED_INCOME` | `LISTING`: a company arriving on an exchange (IPO, SPAC merger, direct listing, a listing on a further exchange). `PIPE`: new shares of a listed company placed with investors, follow-on offerings included. `SECONDARY_OFFERING`: a holder's sale of a listed company's existing shares. `FIXED_INCOME`: a listed company's bonds, notes or loans |
| `NON_DILUTIVE_FINANCING` (label "Non-dilutive Financing") | `UA_FINANCING` · `PRIVATE_DEBT` · `DEVELOPMENT_FINANCING` (label "Project Financing") | Money repaid from revenue rather than bought with shares: user-acquisition financing, the debt of a company that is not listed, and project financing (a publisher's advance or minimum guarantee included) |

New shares issued by the company make a round; existing shares changing hands make M&A. A secondary
offering is not M&A, and a licence that buys nothing is not a deal.

## Exit path (control M&A and listings)

Control acquisitions and listings carry an **exit path**: how founders or earlier owners cashed out.
It is a filter you can ask for ("exits", "first-time exits"):
- `FIRST_TIME_EXIT_MA` ("First-Time Exit (M&A)") - the first exit, by selling control.
- `FIRST_TIME_EXIT_IPO_SPAC` ("First-Time Exit (IPO/SPAC)") - the first exit, by going public.
- `PUBLIC_TAKEOVER` ("Public Takeover") - a listed company is taken private.
- `CARVE_OUT` ("Carve-out") - a parent sells or spins off a division or an asset, or a joint venture is unwound.
- `SECONDARY_EXIT` ("Secondary Exit") - a repeat exit: the company changes hands again or lists again, a listing on a further exchange included.

The First-Time Exits and Public-to-Private views on the site are built on these.

## Participants
- M&A: the acquirer is the lead investor; the target is the target company.
- Rounds and offerings: check **both** the lead and the other-investor lists. A lead shown as
  "Undisclosed" means no lead was named: it is a placeholder, not an investor, so keep it out of
  investor rankings.
- Debt and non-dilutive financing: the lenders are the leads; the lead may be empty.
- Advisors sit in four separate roles (sell-side and buy-side, financial and legal). IPO underwriters
  are advisors, not investors.

## What "Size" means (by type)

Size is **not one formula**, so never add or compare sizes across types as if it were:

| Type | Size = |
|------|--------|
| `MA_CONTROL` | the value of the transaction: the enterprise value at 100% × the stake acquired, plus the maximum earn-out; with no disclosed enterprise value, the price paid plus the maximum earn-out |
| `MA_MINORITY` | the value of the stake: stake % × equity value (enterprise value less debt plus cash) |
| Early / late investment | the round size (total raised in the round) |
| `LISTING` and `PIPE` | the gross proceeds of the offering |
| `SECONDARY_OFFERING` | the consideration paid for the shares |
| `FIXED_INCOME` and `PRIVATE_DEBT` | the principal; for a credit line, the full facility |
| `UA_FINANCING` and `DEVELOPMENT_FINANCING` | the committed amount |
| `ACCELERATOR_GRANT` | the award |

Sizes come back in USD millions. An earn-out of `0` means the source confirms there is none; an
empty earn-out means unknown.

## Valuation and multiples
The EV basis of every multiple, the NM rule and the periods: `definitions.md`.

## For querying
- "M&A" → category `MA`; "fundraising / VC" → early + late stage; "IPO" / "went public" → type
  `LISTING`; "funding raised", "raised capital" and non-dilutive financing → the buckets in
  `definitions.md`.
- "growth round" spans `SERIES_B` and later, `GROWTH_OR_EXPANSION` and `UNDISCLOSED_LATE_STAGE`:
  confirm the scope.
- For valuation questions, default to **EV/Revenue (LTM)** on the EV basis of the deal's category
  (`definitions.md`) and state it in the methodology line.
- Exclude undisclosed sizes from totals. A count shown on its own includes all deals; when a count
  sits beside a total, restrict both to disclosed sizes and say so.
