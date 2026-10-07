# Canonical metric definitions - the consistency layer

These pin the fuzzy words so the **same question returns the same number**.

## Buckets (always use these)
| Term | Definition |
|------|-----------|
| **M&A** | deal category `MA` (control + minority) |
| **Fundraising / VC funding** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **Most funded companies / top raisers** | VC rounds only - matches Most Funded Companies view (`funding_size_in_period`); excludes M&A/IPO |
| **Funding raised** (a company's total) | early + late rounds + the whole `PUBLIC_OFFERING` category (listings, PIPEs, secondary offerings, fixed income), as the company card counts it. M&A and non-dilutive financing are not funding raised |
| **Raised capital (any event)** | every capital event: `MA`, early, late, `PUBLIC_OFFERING` (deal value, not funding raised). Non-dilutive financing is **not** in it: show it as its own row and say so |
| **Non-dilutive financing** | its own first-class visible category (`NON_DILUTIVE_FINANCING`, label "Non-dilutive Financing"): UA financing, private debt and project financing (publishing advances and minimum guarantees included). Repaid from revenue, so neither fundraising nor M&A and never inside those buckets. Counted in general analytics; the quarterly report holds out UA financing, project financing and secondary offerings, while private debt stays in it, under Private Investments |
| **Always excluded** | `OTHER_MISC`, the whole of the non-visible `OTHER` category, is hidden from the data entirely and is never queryable |

## Time
| Term | Definition |
|------|-----------|
| **recent / latest / new** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **this year / last year** | calendar year of / before today, by effective date (`closed_date` ?? `announcement_date`) |
| **no time word** | no date filter - whole database |
| **the date that matters** | effective date = `closed_date` ?? `announcement_date` - a deal counts in the period it CLOSED (matches the product and quarterly reports); `announcement_date` is the fallback when there's no close date |

## Money & valuation
- **Sizes** are USD millions. **Undisclosed = excluded** from sums/averages, shown as **"n/d"** in lists.
- **Multiples and per-employee figures divide by one valuation per category:** M&A, control and
  minority alike → **Upfront EV** at 100%; early/late-stage rounds → **post-money EV**; a listing or a
  PIPE → **market cap at the offer**. A secondary offering, fixed income, private debt and other
  non-dilutive money carry no multiples. Never the Deal Size or the Max EV.
- Multiples are computed in the target's **reported currency** (valuation over metric), so no FX rate
  enters them; financials stay in reported currency, separate from the deal record.
- When a **sum and a count appear together**, restrict to disclosed sizes so the two reconcile.

## Multiples
- Displayed as **"2.6x"**. **"NM"** = not meaningful: negative, a zero metric, or outside the band.
  EV/Revenue is NM below 0.1x or above 20x; EV/EBITDA, EV/EBIT and EV/Cash EBITDA are NM below 0.25x
  or above 50x. **Blank = no data**, which is a different thing from NM. Neither is ever zero.
- For averaging/sorting, parse to a number and drop NM/blank; for display, show as stored.
- Periods, anchored on the announcement date: **LTM** (trailing twelve months of actuals from the
  last reporting period published before the announcement, the default; the exception is an
  announcement made very close to the publication of the financials, for example within a week
  after the deal, when that period may be used) · **CY0** (the calendar year OF THE ANNOUNCEMENT,
  not the current year; it can coincide with LTM) · **NTM** (the
  calendar year after the announcement year; for a January or February announcement, the same
  calendar year). Single-value fallback order: LTM, then CY0, then NTM. Always write **CY0 with a
  zero**, never with a letter O.

## Counting
- Count distinct deals (`COUNT(DISTINCT deal)`) - a deal with several investors must not be counted
  multiple times.
- For per-investor totals, a deal's full value is attributed to each participating investor (expected);
  for market-wide totals, deduplicate first.

## One-line rule
Every data answer states its scope: **period · geography · what's included/excluded.** No number ships
without it.
