# Canonical metric definitions - the consistency layer

These pin the fuzzy words so the **same question returns the same number**.

## Buckets (always use these)
| Term | Definition |
|------|-----------|
| **M&A** | deal category `MA` (control + minority) |
| **Fundraising / VC funding** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **Most funded companies / top raisers** | with no basis named, ranked on Raised capital (below); "by VC funding" ranks early- and late-stage rounds only, the basis of the site's Most Funded Companies view |
| **Funding raised** (a company's total) | early + late rounds + the `PUBLIC_OFFERING` category except `SECONDARY_OFFERING` (listings, PIPEs, fixed income), as the company card counts it. M&A and non-dilutive financing are not funding raised |
| **Raised capital** | every category except `MA` and `SECONDARY_OFFERING`: early, late, `PUBLIC_OFFERING` without `SECONDARY_OFFERING` (listings, PIPEs, fixed income) and `NON_DILUTIVE_FINANCING` (UA financing, private debt, project financing). It is funding raised plus all non-dilutive financing |
| **Non-dilutive financing** | its own first-class visible category (`NON_DILUTIVE_FINANCING`, label "Non-dilutive Financing"): UA financing, private debt and project financing (publishing advances and minimum guarantees included). Repaid from revenue, so neither funding raised nor M&A; it is counted in Raised capital. Counted in general analytics; the quarterly report holds out UA financing, project financing and secondary offerings, while private debt stays in it, under Private Investments |

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
  PIPE → **market cap at the offer**. A secondary offering, fixed income, private debt, other
  non-dilutive money and an accelerator or grant award carry no multiples. Never the Deal Size or
  the Max EV.
- A multiple is valuation over metric in one currency, so no FX rate enters it.
- When a **sum and a count appear together**, restrict to disclosed sizes so the two reconcile.

## Multiples
- Displayed as **"2.6x"**. **"NM"** = not meaningful: negative, a zero metric, or outside the band.
  EV/Revenue is NM below 0.1x or above 20x; EV/EBITDA, EV/EBIT and EV/Cash EBITDA are NM below 0.25x
  or above 50x. **Blank = no data**, which is a different thing from NM. Neither is ever zero.
- For averaging/sorting, parse to a number and drop NM/blank; for display, show as stored.
- Periods, anchored on the announcement date: **LTM** (the trailing twelve months of actuals
  reported before the announcement; the default) · **CY0** (the calendar year OF THE ANNOUNCEMENT,
  not the current year; it can coincide with LTM) · **NTM** (the calendar year after the
  announcement year; for a January or February announcement, the same calendar year). Single-value
  fallback order: LTM, then CY0, then NTM. Always write **CY0 with a zero**, never with a letter O.

## Counting
- Count distinct deals - a deal with several investors must not be counted multiple times.
- For per-investor totals, a deal's full value is attributed to each participating investor (expected);
  for market-wide totals, deduplicate first.

## One-line rule
Every data answer states its scope: **period · geography · what's included/excluded.** No number ships
without it.
