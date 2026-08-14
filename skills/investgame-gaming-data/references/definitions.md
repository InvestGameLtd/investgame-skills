# Canonical metric definitions - the consistency layer

These pin the fuzzy words so the **same question returns the same number**. (Live proof: "gaming
M&A in 2025" returned 181 deals under one phrasing and 104 under another, purely because the buckets
weren't fixed. This file is the fix.)

## Buckets (always use these)
| Term | Definition |
|------|-----------|
| **M&A** | deal category `MA` (control + minority) |
| **Fundraising / VC funding** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **Most funded companies / top raisers** | VC rounds only - matches Most Funded Companies view (`funding_size_in_period`); excludes M&A/IPO |
| **Raised capital (any event)** | all **five visible categories**, which includes `UA_FINANCING`. Say so when it is in a total |
| **UA-financing** | its own first-class visible category (`UA_FINANCING`). Non-dilutive, so neither fundraising nor M&A and never inside those buckets. Counted in general analytics; held out only of the quarterly report |
| **Always excluded** | development financing, licensing and `OTHER_MISC` are hidden from the data entirely and are never queryable. They are the whole of the non-visible `OTHER` category |

## Time
| Term | Definition |
|------|-----------|
| **recent / latest / new** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **this year / last year** | calendar year of / before today, by effective date (`closed_date` ?? `announcement_date`) |
| **no time word** | no date filter - whole database |
| **the date that matters** | effective date = `closed_date` ?? `announcement_date` - a deal counts in the period it CLOSED (matches the product and quarterly reports); `announcement_date` is the fallback when there's no close date |

## Money & valuation
- **Sizes** are USD millions. **Undisclosed = excluded** from sums/averages, shown as **"n/d"** in lists.
- **The EV basis for multiples depends on the deal category:** M&A → **Upfront EV** at 100%;
  early/late-stage rounds → **post-money EV**; public offerings → **listing market cap**. Fixed income
  carries no meaningful EV. Never use the transaction/Max EV for a multiple in any category.
- When a **sum and a count appear together**, restrict to disclosed sizes so the two reconcile.

## Multiples
- Displayed as **"2.6x"**. **"NM"** = not meaningful: negative, or outside the band. EV/Revenue is NM
  below 0.1x or above 20x; EV/EBITDA, EV/EBIT and EV/Cash EBITDA are NM below 0.25x or above 50x.
  **Blank = no data**, which is a different thing from NM. Neither is ever zero.
- For averaging/sorting, parse to a number and drop NM/blank; for display, show as stored.
- Periods: **LTM** (trailing 12m, the default) · **CY0** (the calendar year OF THE ANNOUNCEMENT, not
  the current year) · **NTM** (forward). Single-value fallback order: LTM, then CY0, then NTM. Always
  write **CY0 with a zero**, never with a letter O.

## Counting
- Count distinct deals (`COUNT(DISTINCT deal)`) - a deal with several investors must not be counted
  multiple times.
- For per-investor totals, a deal's full value is attributed to each participating investor (expected);
  for market-wide totals, deduplicate first.

## One-line rule
Every data answer states its scope: **period · geography · what's included/excluded.** No number ships
without it.
