---
name: investgame-gaming-data
version: 0.9.1
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
   e.g. `InvestGame:InvestGame_query`) with a natural-language prompt. What matters is precision, not
   any magic words: a phrase like "use InvestGame" is ignored, and it never acts as a company-name
   filter. Prefer one precise prompt over a vague one - vague prompts are the main cause of weak
   answers. If a well-formed query returns no rows, re-ask once naming the company/entity explicitly
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
   `{"mode":"clarify","reason_code":"out_of_scope"|"needs_clarification","questions":[...],"suggestions"?,"reason"?}`
   - ask the user those `questions` verbatim (offering any `suggestions`), then call again with their
   answer; do not reformulate the question yourself. `reason_code` is always present and tells you what
   to do next: `out_of_scope` means InvestGame does not track this, so stop retrying;
   `needs_clarification` means the question is underspecified, so ask and call again. Or
   `{"mode":"data","tables":[{name,columns,rows}],"entities":[{type,id,url}]}` - read the tables and
   answer, linking each entity via its `url` (always on `https://app.investgame.net`, the `app.`
   subdomain). The tool emits two entity kinds only: company → `/companies/{id}` and deal →
   `/deals/{id}`. A `data` reply may also carry a `status` flag: `"failed"` means
   the lookup could not be completed (tell the user it failed; never present it as "no results found"),
   `"partial"` means answer with what came back but flag it as incomplete, and no `status` key means the
   answer is complete. Presentation detail lives in `investgame-format`.
8. **Always state the `assumptions`.** A `data` reply may carry `"assumptions":[...]`: the scope
   decisions that shaped the result, above all **which date the period filtered on**. Never drop
   these: they change what the numbers mean. There are two anchors and they select different
   populations, not different phrasings of one:
   - **Effective date** (`closed_date` falling back to `announcement_date`) is the **default**, and
     it is what the site filter, the curated views and the quarterly reports all use.
   - **Announcement date** is used when the user asks for it explicitly.

   A closed-date window omits deals announced in the period but not yet closed, and many rounds never
   record a close date at all. So report which anchor the `assumptions` name, and offer the other when
   the difference could matter.

## 1 · The taxonomy - the only allowed vocabulary

**Sectors** (a company can have several): `GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS` · `OTHER`.
`OTHER` = tracked, but outside every covered gaming sector: real-money gambling and betting operators,
generic AI companies with no evidenced gaming market, and other adjacent firms we follow without
counting them as gaming. Exclusive (never combined with another sector), carries no gaming fields, and
is EXCLUDED from gaming sector totals - pull it only when the user asks about those companies
specifically. Note the line: a studio that *makes* casino games is `GAMING_CONTENT` (genre `CASINO`),
even when the games pay out real money; only the operator taking the wagers sits in `OTHER`.

**Platform** (GAMING_CONTENT only): `MOBILE` · `PC_CONSOLE` · `BROWSER` · `VR_AR`.
- "mobile" → `MOBILE`; "PC / console / AAA" → `PC_CONSOLE`; "browser/HTML5" → `BROWSER`; "VR/AR/XR" → `VR_AR`.

**Game genre** (GAMING_CONTENT, ten values): `PUZZLE` (incl. match-3/merge/word) · `SHOOTER` ·
`ACTION_RPG` · `STRATEGY_MOBA` · `CASINO` (casino *games*, not operators) · `SIMULATION_SANDBOX` ·
`SPORTS_RACING` · `ARCADE` (incl. hypercasual) · `TABLETOP` (card/board) · `OTHER` (nothing else
fits; a genre breakdown will return `OTHER` rows, so name it rather than dropping them).

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

**Deal category** (five visible): `MA` (types `MA_CONTROL`, `MA_MINORITY`) · `EARLY_STAGE_INVESTMENT`
(accelerator/grant, Seed, Series A, undisclosed-early) · `LATE_STAGE_INVESTMENT` (Series B to H,
growth/expansion, undisclosed-late) · `PUBLIC_OFFERING` (`LISTING`, `PIPE`, `FIXED_INCOME`) ·
`UA_FINANCING` (its own first-class category, counted in general analytics and held out only of the
quarterly report). A sixth category, `OTHER`, holds only the three hidden types and is never
queryable: **19 visible types across 5 visible categories**.

**Deal type → display label** (a deal's `type` comes back as a raw code - render its InvestGame label, never
the code): `MA_CONTROL`→"M&A control (incl. LBO/MBO)" · `MA_MINORITY`→"M&A minority" · `SEED`→"Pre-Seed/Seed" ·
`SERIES_A`…`SERIES_H`→"Series A"…"Series H" · `GROWTH_OR_EXPANSION`→"Growth / Expansion" ·
`ACCELERATOR_GRANT`→"Accelerator / Grant" · `UNDISCLOSED_EARLY_STAGE`→"Undisclosed Early-stage" ·
`UNDISCLOSED_LATE_STAGE`→"Undisclosed Late-stage" · `LISTING`→"Listing (IPO/SPAC)" · `PIPE`→"PIPE" ·
`FIXED_INCOME`→"Fixed Income" · `UA_FINANCING`→"UA Financing". Development financing, licensing and
`OTHER_MISC` are hidden and never come back from a query.

**Region maps** (use the country lists, not granular sub-regions):
- Europe → GB, DE, FR, SE, NO, DK, FI, CH, NL, BE, AT, IT, ES, PT, PL, IE, CZ, RO
- Asia/APAC → JP, KR, CN, SG, AU, NZ, IN, TW, HK, TH, ID, VN, MY, PH
- North America → US, CA · LATAM → BR, MX, AR, CO, CL, PE
- MENA (gaming-relevant) → SA, AE, JO, EG. Turkey (TR) is **not** in MENA: it is its own hub, often
  reported alongside it.

## 2 · Canonical definitions - pin these every time (consistency)

These are the difference between "181 M&A in 2025" and "104 M&A in 2025" for the *same year*.

| Phrase | Canonical meaning |
|--------|-------------------|
| **"M&A"** | deal category `MA` only |
| **"fundraising" / "VC funding"** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **"most funded companies" / "top raisers"** | VC rounds only (Most Funded Companies view) |
| **"raised capital" (any event)** | all **five visible categories**, `UA_FINANCING` included. Flag it when it is in a total, since it is non-dilutive |
| **UA-financing** | its own first-class visible category, neither fundraising nor M&A. Counted in general analytics; held out only of the quarterly report |
| **never in the data at all** | development financing, licensing and `OTHER_MISC`: hidden types, never queryable |
| **"recent / latest / new"** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **no time word at all** | no date filter - whole database |
| **deal size** | USD millions; undisclosed = no value recorded → excluded from sums, shown as "n/d" in lists. Control and minority M&A use different Size formulas: see `deal-taxonomy.md` |
| **enterprise value for multiples** | by category: M&A → **Upfront EV** at 100%; early/late rounds → **post-money EV**; public offerings → **listing market cap**. Never the Max/transaction EV |
| **multiples** | shown as "2.6x". **"NM"** = negative or outside the band (EV/Revenue 0.1x to 20x; EV/EBITDA, EV/EBIT, EV/Cash EBITDA 0.25x to 50x). Blank = no data, which is not NM. Neither is zero |
| **date** | the **effective date** (`closed_date` ?? `announcement_date`) is the default anchor and matches the site filter, the curated views and the quarterly reports. The announcement date is used only when asked for. State which anchor the `assumptions` report |

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
   category MA; sizes USD m; undisclosed excluded from totals; last 18 months by effective date."*).
   Name the anchor the `assumptions` actually report, not the one you expected.
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
**and its own visible category** (`UA_FINANCING`), counted in general analytics and held out only of
the quarterly report; **exit paths** (first-time exits, public-to-private, carve-outs) are a derived
filter you can ask for; and **geography** by any country or region is fully supported.

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
