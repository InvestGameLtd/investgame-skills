# Canonical metric definitions — the consistency layer

These pin the fuzzy words so the **same question returns the same number**. (Live proof: "gaming
M&A in 2025" returned 181 deals under one phrasing and 104 under another, purely because the buckets
weren't fixed. This file is the fix.)

## Buckets (always use these)
| Term | Definition |
|------|-----------|
| **M&A** | deal category `MA` (control + minority) |
| **Fundraising / VC funding** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **Most funded companies / top raisers** | VC rounds only — matches Most Funded Companies view (`funding_size_in_period`); excludes M&A/IPO |
| **Raised capital (any event)** | every category **except** `OTHER` |
| **UA-financing** | a real, queryable deal type (`UA_FINANCING`) — ask for it directly, but it is kept **out of headline fundraising/M&A totals** by methodology |
| **Always excluded** | `OTHER` from totals; dev-financing + licensing are hidden from the data entirely |

## Time
| Term | Definition |
|------|-----------|
| **recent / latest / new** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **this year / last year** | calendar year of / before today, by effective date (`closed_date` ?? `announcement_date`) |
| **no time word** | no date filter — whole database |
| **the date that matters** | effective date = `closed_date` ?? `announcement_date` — a deal counts in the period it CLOSED (matches the product and quarterly reports); `announcement_date` is the fallback when there's no close date |

## Money & valuation
- **Sizes** are USD millions. **Undisclosed = excluded** from sums/averages, shown as **"n/d"** in lists.
- **Enterprise value for multiples = Upfront EV** (100%-basis). Never use the transaction/Max EV for
  multiples. Private-investment EV = post-money; listings = market cap.
- When a **sum and a count appear together**, restrict to disclosed sizes so the two reconcile.

## Multiples
- Displayed as **"2.6x"**. **"NM"** = not meaningful (negative or out of range). Blank = no data.
- For averaging/sorting, parse to a number and drop NM/blank; for display, show as stored.
- Periods: **LTM** (trailing 12m, default) · **NTM** (forward) · **CYO** (current calendar year).

## Counting
- Count distinct deals (`COUNT(DISTINCT deal)`) — a deal with several investors must not be counted
  multiple times.
- For per-investor totals, a deal's full value is attributed to each participating investor (expected);
  for market-wide totals, deduplicate first.

## One-line rule
Every data answer states its scope: **period · geography · what's included/excluded.** No number ships
without it.
