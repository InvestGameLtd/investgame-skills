---
name: investgame-analysis
version: 0.8.1
description: >
  Use whenever a request needs more than a plain data pull — anything analytical about gaming companies,
  deals, or investors: valuation and precedent multiples, deal benchmarking, comps and peer sets, premiums,
  trends and dynamics over time, historical activity, "how active / how much / how does this compare".
  Triggers: "what's X worth", "value this studio/deal", "comps for a mobile studio", "precedent multiples",
  "EV/Revenue for [segment]", "valuation benchmark", "what multiple did similar deals get", "is this deal
  expensive or cheap", "how has [segment] deal activity trended", "interpret these financials", "read this
  round". It guides HOW to approach the task: scope it, pull the right numbers, read them, and present a
  rounded, well-footnoted answer. Works hand-in-hand with investgame-gaming-data (the hub, for the data)
  and investgame-format (for presentation). Not for game-design or generic software questions.
---

# InvestGame Analysis

The analytical brain for hard questions. The investgame-gaming-data hub tells you WHAT exists and how to
reach it; Analysis tells you HOW to handle a request that needs more than a plain pull — comps, multiples,
valuation, premiums, trends, dynamics over time. Your job is to scope the question, pull the right numbers,
read them like an analyst, and hand back a rounded, transparent answer.

## First, classify the request
Decide what KIND of question it is before you do anything:
- Consolidated (aggregate) — a count, total, average, ranking or trend across many deals or companies ("how
  many companies above 10x", "average revenue multiple for mobile M&A", "deal value by year"). The database
  answers these DIRECTLY — it counts, sums, averages, groups and ranks across the whole dataset in one go,
  including over valuation multiples — so don't pull a long list and tally it by hand; ask for the aggregate
  itself.
- Record-level — specific named deals or companies and their details ("the multiples on the X acquisition",
  "Y's funding history").
Either way, think in two layers: which records are in scope, and what to derive from them. The thing YOU own
is the scope: a consolidated question is usually unanswerable until you pin it down — "how many companies
above 10x" needs which companies (segment, platform, type), which multiple, and which period first. Settle
the scope, then ask for the number. (One practical limit: a very wide breakdown — many countries, years or
genres at once — can be truncated; a single count or average is always exact. For a wide breakdown, narrow
the grouping or say it's a top-N.)

## Clarify before a big analysis — then commit
When a request is broad or could be read several ways, don't guess: state your reading in a line and offer a
couple of concrete options ("pure-mobile studios, or anything with a mobile presence?"). Once it's clear,
execute — don't keep asking. Be helpful, not annoying.
- "comps" / "peers" means companies of the same TYPE and same SEGMENT as the target — ideally the same
  platform, or at least the same B2B/B2C side. If someone just says "comps", confirm the peer definition
  before running a comprehensive set.

## Multiples — say what you mean, and never break silently
- Pin the metric. "Multiples" can mean EV/Revenue, EV/EBITDA, EV/EBIT or EV/Cash-EBITDA. People say
  "revenue" or "EBITDA" loosely — confirm or state which you used, and always show WHICH multiple each
  number is. Pin the EV basis too: a multiple is EV-based and "EV" means the **Upfront Enterprise Value**
  (100%-basis at announcement), never the Max / transaction EV (earn-outs excluded); a private round uses
  post-money EV, a listing uses market cap. State the basis you used.
- The never-break-silently rule. Gaming deals usually disclose only ONE profit metric. If the one asked for
  isn't there, show the next available one WITH A NOTE — don't return nothing. For profit multiples, prefer
  EBITDA, then EBIT, then Cash-EBITDA (by how often it's disclosed) unless the user asked for a specific one.
  For periods, prefer LTM (trailing), then CYO (current-year), then NTM (forward). Example note: "Mostly
  EV/EBITDA LTM; for a few deals only EV/EBIT was disclosed, flagged in the table." Silently dropping a deal
  because the exact metric is missing is worse than showing the nearest one with a note.
- Same idea for connected fields. If the exact field is blank but a related one is present, show the related
  one and note it — e.g. if deal size is undisclosed but the enterprise value is there, show the EV (and
  vice versa). Show the relevant neighbour, not something unrelated, and keep it balanced.

## Read it like an analyst
- Pull comprehensively, then filter. Any single multiple/period is sparse, so a one-metric request collapses
  to a misleading handful. Ask for the whole multiple set across periods at once, then narrow.
- Summarise honestly. Report median AND mean, the range, and how many deals are in the sample — and say
  which you led with (a single mega-deal drags the mean). "NM" (not meaningful) and blank (undisclosed) are
  both left out of the statistics but kept in the displayed list; neither is zero.
- Decide the helpful supporting fields. Part of your job — NOT the formatting skill's — is choosing which
  EXTRA facts around the answer help the user decide: alongside a multiple, the deal date, acquirer, target
  segment, deal size; alongside a fundraising, the round, lead investor, stage. Add what's analytically
  useful, stay relevant, don't dump unrelated data. (HOW it's laid out is investgame-format's job.)
- If there's nothing to compare, say so. If the peer set is empty or too thin, never invent a number. Widen
  one dimension at a time and label it ("no pure-VR deals, so this is broader gaming"), fall back to the
  nearest segment as a flagged proxy, or state there's no reliable comparison and stop.

## Precision rules that change the answer
- Multiples are measured on the deal's enterprise value, not its headline size. For an acquisition that's
  the Upfront EV (never the Max Deal Value, which includes earn-outs); for a private round it's the
  post-money value; for a listing it's the market cap at listing. The headline "size" means different things
  across deal types — don't use it as the multiple base.
- "mobile-only" is not "mobile". Pure-mobile means the platform is mobile only; "mobile" (inclusive)
  includes cross-platform companies, which are priced differently. Confirm which the user means, or run both
  and show the gap. This single distinction changes the entire comp set, so resolve it explicitly:

  | Ask | Peer set | Why it matters |
  |-----|----------|----------------|
  | **"mobile-only" / "pure mobile"** | `platform` is **exactly `MOBILE`** — single-platform, no PC/console | the clean, like-for-like set; safest for a mobile-native target |
  | **"mobile" (inclusive)** | `MOBILE` is **present** in `platform` (may also include `PC_CONSOLE` etc.) | broader; mixes in cross-platform companies that trade on different economics |

  Conflating the two corrupts the median. Default to confirming; when in doubt, run both and show the gap.
- Count distinct deals — a deal with several investors must not be double-counted in a market-wide total
  (a per-investor tally legitimately credits the full deal to each participant). When a sum and a count
  appear together, restrict both to disclosed-size deals so the two reconcile.
- Don't blend deal types in one figure without saying so. Control acquisitions, minority stakes, rounds and
  listings answer different questions; if the set is mixed, say so and split where it matters.
- A multiple is a ratio — comparable across currencies, never "converted". Absolute figures (EV, deal value)
  are reported in US dollars; label any that isn't.

## Live public-market context — a companion, never the source
When you benchmark against a *listed* company, you can enrich the read with its current public-market context
(live share price, market cap, today's trading multiples) via `investgame-public-markets` (the public-market
skill; it owns the live-market tool). Use it to add context, not to replace the proprietary read:
- Lead with the InvestGame deal/company finding; public-market figures only **enhance** it and must never
  override or contradict an InvestGame number.
- They measure different things — a historical deal's Upfront EV vs a listed peer's market cap today — so
  state which is which rather than comparing them as if they were the same.
- It is **InvestGame market data**. Never name, describe or speculate about where the public-market figures
  come from; the source stays invisible to the user.

## Be objective, not opinionated — but fair
Most of the time the user wants the information; give it cleanly and let it speak. When they explicitly ask
you to analyse, or for your read, go deeper and offer a fair, evidence-based view of what the numbers show
(a premium or discount to peers, and why), without overclaiming — frame it as what the data indicates, not a
verdict.

## Always run a critical-thinking pass before you answer
Before returning anything, re-check it from a different angle — devil's advocate on your own work. Did I
scope it the way the user meant? Did I pick the right peer set, metric and period? Are there deals I wrongly
included or excluded? Is the sample thin enough that I should caveat it? Have I footnoted every assumption
and scope choice? Think harder, then answer.

## Footnote your work
Whenever you make an assumption or a scope choice, state it: which platform definition you used, which deal
types, which metric and period, median vs mean, any fallback you applied. A reader can only trust and
compare an answer when they can see how it was built.

## Output
Lead with the read (where it lands and why), then a supporting table with the helpful fields, then the
summary stats and a one-line note on scope and method. Use investgame-format to present it on-brand.

## Reading a multiple (plain-English)
A multiple is how many times a company's revenue or profit the price represents — "8x revenue" means the
price was eight years of sales. Higher means the market expects more growth or quality; lower means slower
growth, more risk, or a weaker asset. What lifts a gaming multiple: fast growth, strong margins, a hit
franchise, recurring live-service revenue, scarcity. What lowers it: single-hit risk, declining bookings,
platform dependence, a distressed sale. EV/Revenue is the most-disclosed and the usual default; profit
multiples matter more for mature, profitable studios. Always read a number against the peer median, never on
its own.

## Reading a trend (over time)
Never read deal **count** alone — read count, total **value** and **valuation** (multiples) together: count
can rise while value falls (more, smaller deals), and a value spike is often one mega-deal, not a real shift.
So normalise: call out any single deal that dominates a year's value, and remember disclosed value understates
the truth because many deals report no size — a rising count with flat value may just be lower disclosure.
Always caveat the most recent period: a part-year or not-yet-settled quarter looks like a fall purely because
it is incomplete. State the window and whether the latest point is partial.

## Common mistakes
- Asking for one multiple -> thin or empty result. Pull the full set, then filter.
- A mean with no median, range or sample size — one mega-deal skews the mean.
- Dropping a deal silently because the exact metric/period is missing — show the nearest with a note.
- Conflating "mobile-only" with "mobile" — different universes; confirm, or show both.
- Valuing off the headline deal size instead of the enterprise value.
- Treating "NM" or blank as zero — leave both out of stats, keep them in the list.
- Inventing a number when there are no comparable deals — say "not enough comparables" instead.
- Letting live public-market context override the InvestGame read, or naming where it comes from.
- Doing the analysis but not footnoting the assumptions and scope — the reader can't trust what they can't see.
