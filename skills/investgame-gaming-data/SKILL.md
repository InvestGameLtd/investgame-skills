---
name: investgame-gaming-data
version: 0.9.0
description: >
  The home for games-industry deal and market intelligence. Use the moment a question pairs gaming with
  money, deals, investors, or classification: listing or counting M&A, fundraises, financing rounds, or
  IPOs; ranking the most active investors, funds, or acquirers; pulling precedent valuations or EV/Revenue
  multiples; or deciding how a games company, deal, or segment fits the InvestGame taxonomy (sector,
  platform, genre, monetization, segment). Answers come from InvestGame's proprietary deal database - not
  public filings or the open web - across studios, publishers, ecosystem and infrastructure, every region
  and period. Trigger on any "who / how many / which deals / what multiple / what category" question about
  gaming transactions, capital flows, or investor activity. Do NOT use for game design or development
  advice, or generic software recommendations. For a listed company's live stock price, market cap,
  financials or FX conversion, see the companion skill investgame-public-markets.
---

# InvestGame Gaming Data

InvestGame is the gaming-native database of M&A, financings, valuations, investors and funds.
This skill makes the InvestGame MCP (`InvestGame_query`) produce **consistent, analyst-grade**
answers: it carries the taxonomy and definitions so the model never invents terms, never
silently changes scope, and always formats results the InvestGame way. You bring the question;
this skill makes the answer reliable.

## 0 · Golden rules (the "taxonomy policeman")

1. **Speak only the InvestGame taxonomy below.** Never invent categories ("Investment Funds",
   "notable LPs"), never assume fields that don't exist. If a requested concept is outside the
   taxonomy, say so plainly instead of fabricating.
2. **Pin every scope dimension before querying.** "Recent", "mobile", "M&A vs fundraising",
   deal scope, time window, and participant role each need an explicit reading (§2). If a request is
   broad, unclear, or could be read several ways under the taxonomy, confirm with the user first -   offer a couple of concrete options - rather than guessing.
3. **A `clarify` result means no query ran.** When `InvestGame_query` returns `mode:"clarify"`, the
   tool answered with `questions` (and sometimes `suggestions`) **instead of running anything** - the
   result carries no data. Present those `questions` to the user and stop. Never read the empty result
   as "no data found", and never fill the gap from memory. When every dimension is pinned in the
   question, proceed and state the methodology (§4).
4. **Call the InvestGame connector's `InvestGame_query` tool** (your host may show it fully-qualified,
   e.g. `InvestGame:InvestGame_query`) with a natural-language prompt, and **always pass `use InvestGame`
   and `think hard`**. Prefer one precise prompt over a vague one - vague prompts are the main cause of
   weak answers. If a well-formed query returns no rows, re-ask once naming the company/entity explicitly
   before concluding the data isn't there.
5. **Never present a number without its scope.** Every data answer ends with a one-line methodology
   note (§4).
6. **Two tools - route the question.** This hub answers proprietary InvestGame questions (deals,
   companies, investors, valuations, taxonomy) via `InvestGame_query`. For a **listed** company's live
   public-market data (price, market cap, financials, earnings, dividends, analyst view, employee count)
   or any **FX / currency conversion**, hand off to `investgame-public-markets` (it owns the
   `InvestGame_market_query` tool). If a question needs both - e.g. benchmark a deal against the peer's
   current public value - use both, but **lead with InvestGame**. Public-market data is a **companion,
   not a substitute**: it only enhances and must never override or contradict an InvestGame figure;
   when they look different they measure different things (a historical deal EV vs today's market cap) -   state what each is. The public-market source is never named - it is "InvestGame market data".
   For the **gaming press itself** - what the newsletters and shows are publishing, a "what's happening
   / this fortnight in gaming" synthesis, a press brief, or the periodic digest - hand off to
   `investgame-press` (it owns the `InvestGame_press_query` tool). It reads the press corpus and never
   answers a deal/company fact (that is this hub) or a live price (that is `investgame-public-markets`);
   conversely, transactions in a digest are DB-authoritative and come back from this hub, never counted
   from the press.
7. **Handle the two response modes.** `InvestGame_query` returns exactly one of two lean shapes:
   `{"mode":"clarify","questions":[...],"suggestions"?,"reason"?}` - ask the user those `questions`
   verbatim (offering any `suggestions`), then call again with their answer; do not reformulate the
   question yourself - or
   `{"mode":"data","tables":[{name,columns,rows}],"entities":[{type,id,url}]}` - read the tables and
   answer, linking each entity via its `url` (always on `https://app.investgame.net` - the `app.`
   subdomain; the bare `investgame.net` host 404s). Deal → `/deals/{id}`, company → `/companies/{id}`,
   index → `/market-indices/{slug}`. A `data` reply may also carry a `status` flag: `"failed"` means
   the lookup could not be completed (tell the user it failed; never present it as "no results found"),
   `"partial"` means answer with what came back but flag it as incomplete, and no `status` key means the
   answer is complete. Presentation detail lives in `investgame-format`.
8. **Always state the `assumptions`.** A `data` reply may carry `"assumptions":[...]`: the scope
   decisions that shaped the result, above all **which date the period filtered on**. Never drop
   these: they change what the numbers mean. "Closed in Q2" and "announced in Q2" are different
   populations, not phrasing. A round is *announced*, and many never record a closed date, so a
   closed-date window omits deals announced in the period but not yet closed. Ranking a quarter on
   the closed anchor can understate the top deal several-fold. If the user wants "the deals of Q2",
   they almost always mean **announced**: say which anchor you used, and offer the other.

## 1 · The taxonomy - the only allowed vocabulary

**Sectors** (a company can have several): `GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS` · `OTHER`.
`OTHER` = tracked, but outside every covered gaming sector (real-money gambling operators such as
DraftKings, MGM Resorts, Entain). Exclusive, carries no gaming fields, and is EXCLUDED from gaming
sector totals - pull it only when the user asks about those companies specifically.

**Platform** (GAMING_CONTENT only): `MOBILE` · `PC_CONSOLE` · `BROWSER` · `VR_AR`.
- "mobile" → `MOBILE`; "PC / console / AAA" → `PC_CONSOLE`; "browser/HTML5" → `BROWSER`; "VR/AR/XR" → `VR_AR`.

**Game genre** (GAMING_CONTENT): `PUZZLE` (incl. match-3/merge/word) · `SHOOTER` · `ACTION_RPG` ·
`STRATEGY_MOBA` · `CASINO` (casino *games*, not operators) · `SIMULATION_SANDBOX` · `SPORTS_RACING` ·
`ARCADE` (incl. hypercasual) · `TABLETOP` (card/board).

**Monetization** (GAMING_CONTENT): `IAP` (F2P/in-app purchases) · `IAA` (ad-supported) ·
`GAAS` (live service - *not* mobile-specific) · `UPFRONT_SALE` (premium/buy-to-play) ·
`DLC` (paid expansions) · `SUBSCRIPTION` (Game Pass / PS+).

**Content type** (GAMING_CONTENT): `DEVELOPER_1P_PUBLISHER` · `PUBLISHER_3P` · `OUTSOURCING_WFH`.

**Ecosystem segment** (GAMING_ECOSYSTEM only): `ESPORTS` · `CREATION_DEVELOPMENT` (helps *build* the
game - engines/tools) · `INFRASTRUCTURE_SERVICES` (helps *run/scale* - cloud, analytics, payments) ·
`ADTECH` (UA tools) · `HARDWARE` · `STREAMING_ENTERTAINMENT` · `DISTRIBUTION_SOCIAL_PLATFORMS`.
*Critical: `platform` ≠ `ecosystem_segment`. "Mobile" is a platform; "esports" is an ecosystem segment.*

**Consumer Apps subsegment** (CONSUMER_APPS only): `EDTECH` · `FITNESS_WELLNESS` ·
`ENTERTAINMENT_SOCIAL` · `OTHER`.

**Company type:** `ANGELS_INDIVIDUALS` · `VENTURE_CAPITAL_AND_ACC` · `PRIVATE_EQUITY_AND_INST` ·
`STRATEGIC_OR_CVC` · `SERVICE_PROVIDERS` (banks/advisors/law firms) · `ASSET` (IP/franchise) · `OTHER`.

**Deal category:** `MA` (types `MA_CONTROL`, `MA_MINORITY`) · `EARLY_STAGE_INVESTMENT`
(Seed, Series A, accelerator, undisclosed-early) · `LATE_STAGE_INVESTMENT` (Series B–H, growth,
undisclosed-late) · `PUBLIC_OFFERING` (IPO/SPAC/listing) · `OTHER` (always excluded).

**Deal type → display label** (a deal's `type` comes back as a raw code - render its InvestGame label, never
the code): `MA_CONTROL`→"M&A control (incl. LBO/MBO)" · `MA_MINORITY`→"M&A minority" · `SEED`→"Pre-Seed/Seed" ·
`SERIES_A`…`SERIES_H`→"Series A"…"Series H" · `GROWTH_OR_EXPANSION`→"Growth / Expansion" ·
`ACCELERATOR_GRANT`→"Accelerator / Grant" · `LISTING`→"Listing (IPO/SPAC)" · `PIPE`→"PIPE" ·
`FIXED_INCOME`→"Fixed Income" · `UA_FINANCING`→"UA Financing" · `OTHER_MISC`→"Other".

**Region maps** (use the country lists, not granular sub-regions):
- Europe → GB, DE, FR, SE, NO, DK, FI, CH, NL, BE, AT, IT, ES, PT, PL, IE, CZ, RO
- Asia/APAC → JP, KR, CN, SG, AU, NZ, IN, TW, HK, TH, ID, VN, MY, PH
- North America → US, CA · LATAM → BR, MX, AR, CO, CL, PE
- MENA (gaming-relevant) → SA, AE, JO, EG, TR is treated as its own hub, often paired with MENA.

## 2 · Canonical definitions - pin these every time (consistency)

These are the difference between "181 M&A in 2025" and "104 M&A in 2025" for the *same year*.

| Phrase | Canonical meaning |
|--------|-------------------|
| **"M&A"** | deal category `MA` only |
| **"fundraising" / "VC funding"** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **"most funded companies" / "top raisers"** | VC rounds only (Most Funded Companies view) |
| **"raised capital" (any event)** | all categories **except** `OTHER` |
| **exclude from headline totals** | `OTHER`; and UA-financing - a real, queryable category (`UA_FINANCING`), but kept out of fundraising/M&A totals by methodology (ask for it explicitly). Dev-financing & licensing aren't in the queryable set at all. |
| **"recent / latest / new"** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **no time word at all** | no date filter - whole database |
| **deal size** | USD millions; undisclosed = NULL → excluded from sums, shown as "n/d" in lists |
| **enterprise value for multiples** | **Upfront EV** (100%-basis). Never use Max/transaction EV for multiples. |
| **multiples** | shown as "2.6x"; **"NM"** = not meaningful (negative or out of range); blank = no data |
| **date** | period analysis uses the effective date `closed_date` ?? `announcement_date` (a deal counts in the period it CLOSED, matching the product and quarterly reports); `announcement_date` is the fallback when there's no close date |

When a sum and a count appear together, restrict to disclosed sizes so the two reconcile.

## 3 · How to ask - the precise-prompt patterns

Keep the canonical buckets and a platform/geo/stage filter explicit. The 10 reference shots
(`references/ten-shots.md`) are the proven library - match the user's intent to the closest one,
then adjust the geography/segment/size band. Examples of well-formed asks:

- *"…gaming fundraisings and M&A in the last 90 days where the target is a **mobile** gaming
  company; show target, country, type, size, date, lead investor."*
- *"…early-stage (Seed + Series A) **mobile** rounds in **Turkey, Saudi Arabia, UAE, Jordan, Egypt**
  over the last 24 months."*
- *"…precedent **M&A** multiples for **mobile** targets, EV **$20M–$700M**, with EV/Revenue and an EV-basis note."*

## 4 · Output - InvestGame-grade every time

1. **Lead with the answer**, then the supporting table or ranking - one primary object per answer.
2. **Default columns by query type** (mirror the web app):
   - *Deal lists:* target · country · deal type · size USD · date · lead investor (+ EV/multiple for M&A).
   - *Investor/acquirer rankings:* name · distinct deal count · total disclosed USD.
   - *Company profile:* each round (type, size, date, investors) · disclosed valuation/EV · summary.
3. **Always append a methodology line:** period, geography, what's included/excluded (e.g. *"M&A =
   category MA; sizes USD m; undisclosed excluded from totals; last 18 months by announcement date."*).
4. **Flag, never hide, gaps:** "undisclosed", "n/d", "insufficient public data" - never invent a figure.
5. **Numbers are tabular and right-aligned;** currency in USD millions unless asked otherwise.

## 5 · Brand - when the user wants a report, chart, or one-pager

Render in the **InvestGame** look (two themes, never mixed):
- **Warm White** (`#F4F3EE` bg, data-dense, Space Grotesk + Inter + JetBrains Mono) for market/data
  reports and tables. **Dark Navy** (`#0E1F33`) for bold/editorial decks.
- Brand teal **`#61BFB3`** is the InvestGame colour; **positive = teal `#00928A`** (never green),
  **caution = rust `#C07B5A`** (sparingly). Logo present; one idea per slide; titles carry the insight.
- Charts: bar/column by default, interactive, palette teal → blue → deep teal. Every data slide cites
  its source line.

## 6 · Boundaries - what InvestGame cannot answer (say so; do not invent)

- **People / talent-flow** ("who left Peak to start a new studio") - no person-level data in the
  queryable set. Route to InvestGame custom research.
- **Headcount / growth signals** ("studios scaling fastest by headcount") - no headcount history.
- **Some advanced cuts** (an investor's stage or geography focus, an advisor league table) aren't
  directly tracked - answerable only as a custom query, if at all.
- **Southeast-Asia early-stage mobile equity** - sparse and dated; widen the lens or flag the gap.

Note what IS in scope (don't mistakenly decline it): **UA-financing** is a real, queryable deal type
(`UA_FINANCING`) - only excluded from headline fundraising/M&A totals; **exit paths** (first-time
exits, public-to-private, carve-outs) are a derived filter you can ask for; and **geography** by any
country or region is fully supported.

When asked for any of these: state the limit, give the closest thing the data *can* answer, and offer
custom research. Honesty here is what keeps the database trusted.

## 7 · References - load the one the task needs

The sections above are the always-on core. Pull a reference file when you need the depth:

| Load this | When |
|-----------|------|
| `references/taxonomy.md` | Classifying a **company** or any boundary call (is X gaming? which segment? mobile IAP vs IAA?) - full enums + InvestGame's analyst decision rules incl. monetization×platform |
| `references/deal-taxonomy.md` | Classifying a **deal** (M&A vs growth vs listing), or interpreting deal terms / multiples / size |
| `references/definitions.md` | Any counting/sizing/multiple question - the canonical buckets that keep numbers consistent |
| `references/output-and-brand.md` | Formatting an answer or producing a report/chart - columns, methodology line, InvestGame brand |
| `references/ten-shots.md` | Matching the user's intent to a proven query pattern |
| `references/research-playbook.md` | Any task needing web research beyond the deal data (deep reports, company/investor profiles, meeting prep) - the data-vs-web division of labour + the source catalogue |

## 8 · Companion skills - hand off to the right workflow

This skill is the data hub. For these jobs, use the matching companion skill (which calls back here for data):

| If the user wants… | Use |
|--------------------|-----|
| A valuation, comps, precedent-multiples, benchmarking or trend read | `investgame-analysis` |
| Live public-market data on a listed company (price, financials, earnings, analyst, employees) or an FX conversion | `investgame-public-markets` |
| The gaming press / newsletters - a "what's happening" or this-fortnight read, a press brief, or the "Gaming Pulse" digest | `investgame-press` |
| A deep report, market/company/investor deep-dive, or meeting/call prep | `investgame-research` |
| Notes / a recap / summary from a call or meeting transcript | `investgame-research` |
| Any answer presented cleanly in chat, or rendered as a branded file (PDF/PPTX/XLSX/HTML) | `investgame-format` |
