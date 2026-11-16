---
name: investgame-gaming-data
version: 0.10.16
description: >
  InvestGame's gaming deal database and taxonomy, and the hub every other InvestGame skill calls for
  data. Use whenever a question pairs gaming with deals, money, investors or classification: listing,
  counting or ranking M&A, fundraises, IPOs, investors, acquirers or funds; precedent deals with their
  EV/Revenue multiples; one games company's headcount, key people, owners or deal history; InvestGame's
  gaming market indices; or which sector, platform, genre, monetization or segment a company or deal
  belongs to. Answers come from InvestGame's own database, not public filings or the web. Load this
  skill before the first `InvestGame_query` or `InvestGame_company_query` call, even when those tools
  are already listed: their answers depend on its taxonomy and scope rules. To judge or
  benchmark the numbers use investgame-analysis; for a live share price or FX,
  investgame-public-markets; for what the press is saying, investgame-press. Not for game design or
  generic software questions.
---

# InvestGame Gaming Data

InvestGame is the gaming-native database of M&A, financings, valuations, investors and funds.
This skill makes the InvestGame MCP (`InvestGame_query`) produce **consistent, analyst-grade**
answers: it carries the taxonomy and definitions so the model never invents terms, never
silently changes scope, and always formats results the InvestGame way. You bring the question;
this skill makes the answer reliable.

## 0 · Golden rules

1. **Speak only the InvestGame taxonomy below.** Never invent categories ("Investment Funds",
   "notable LPs"), never assume fields that don't exist. If a requested concept is outside the
   taxonomy, say so plainly instead of fabricating.
2. **Pin every scope dimension that changes the number.** "Recent", "mobile", "M&A vs fundraising",
   deal scope, time window, and participant role each need an explicit reading (§2). Where the tool
   applies a default it reports it in `assumptions`: state it. If a request is broad, unclear, or
   could be read several ways under the taxonomy (mobile-only or any mobile presence, a multiple
   with no metric), confirm with the user first - offer a couple of concrete
   options - rather than guessing.
3. **A `clarify` result means no query ran.** Present its `questions` to the user and stop; never
   read it as "no data found" and never fill the gap from memory. When every dimension is pinned,
   proceed and state the methodology (§4).
4. **Ask precisely.** One precise natural-language prompt beats a vague one; magic words ("use
   InvestGame") do nothing. If a well-formed query returns no rows, re-ask once naming the
   company/entity explicitly before concluding the data isn't there.
5. **Never present a number without its scope.** Every data answer ends with a one-line methodology
   note (§4), naming the date anchor the reply's `assumptions` report: the **effective date**
   (closed date, falling back to announcement date) is the default and matches the site, the curated
   views and the quarterly reports; the **announcement date** is used only when asked for. The two
   select different populations, so offer the other when the difference could matter.
6. **Four tools - route by what the question is about.** The connector describes each tool's
   response shape itself; this table is about which one to call.

   | The question is about | Tool | Notes |
   |---|---|---|
   | Deals, investors, rankings, counts and totals across companies, taxonomy, earnings documents (filed reports, decks, transcripts), InvestGame's gaming market indices (level, constituents) | `InvestGame_query` | Documents come back as `document` download links in `entities` |
   | **One company's own profile**: headcount and its history, followers, key people, filed periods, ownership tree, portfolio and exits, its own deal totals | `InvestGame_company_query` | Returns the figures the company page shows; a field absent from the reply is one that page does not show. One company's headcount comes from here, listed or not; a headcount ranking across companies is not self-serve (section 6) |
   | A **listed** company's live price, market cap, financial statements, earnings figures, or any FX conversion | `InvestGame_market_query` via `investgame-public-markets` | A companion, never a substitute: it enhances an InvestGame figure and never overrides one; the source is "InvestGame market data" |
   | What the **gaming press** is publishing, a press brief, the periodic digest, and the share-price movers and earnings releases InvestGame records for that digest | `InvestGame_press_query` via `investgame-press` | Transactions in a digest are DB-authoritative and come from `InvestGame_query`, never counted from the press |

7. **Read what the connector does not spell out.**
   - **`InvestGame_query` tables hold up to 300 rows**, and deal and company rows come with an
     `entities` link. Where a row has no `entities` entry, its `deal_id` / `company_id` cell still
     gives a valid link through the URL patterns in section 4. Never build a link from a name.
   - A `coverage` table (`matched`, `with_size`, `total_size_usd_m`, `basis`) rides along with a
     deal list: when `with_size` is below `matched`, the total covers the disclosed subset only. Say
     it. A `notices` table is the tool talking about the result, never data.
   - **Queries use the account's credits.** Ask for the cut you need, not a wide list you will trim
     by hand.
   - **Point lookups** by id ("deal id 22492", "company #678") return exactly that record (a company
     comes back as its card); an unknown or not-visible id comes back as a failed lookup: say nothing visible was found,
     never that the record does not exist.
   - A company's **founders** come back as a list of profiles, not the first one; ask for "the
     founders" and you get all of them.
   - "**exclude secondary offerings**" / "**secondary offerings only**" filter on the Secondary
     Offering deal type (a holder's sale of a listed company's existing shares, not money the
     company raised). "**exclude secondary exits**" / "**secondary exits only**" filter on the exit
     path (repeat exits). A bare "secondary" is asked back: name which one.
   - "**rumoured deals**" lists the deals that carry the label Rumour (reported, with no agreement
     announced); "**excluding rumours**" leaves them out. Unless excluded they count in every total.

8. **When a tool says no, say what happened.** Every spoke follows this rule; never paper over a refusal.
   - **Credits exhausted** (the error gives what remains and when it resets): stop. Report what was
     done, what was not, and the reset date; never retry through another tool. Before a large batch
     of new deals or companies, tell the user it uses credits.
   - **Rate limited** ("Retry after Ns"): wait that long, then resume where you stopped. Ask for deals
     or counts across a list in one `InvestGame_query`; call the company card per row only for what
     only the card holds (headcount, key people, ownership tree, followers).
   - **`reason_code: out_of_scope`**: InvestGame does not track it. Stop and offer the closest thing it
     holds (section 6). **`needs_clarification`**: ask the user; never answer the question for them.
   - **Several companies match** (the company card lists them by name, HQ country and founded year,
     with each id in `options[].value`): show the candidates by name and ask. Only when the user
     already named exactly one of them, call again with that option's id (`4521`) and say which
     company you used. A single exact-name match resolves on its own; two companies with the
     identical name still come back as this question.
   - **No company matches** (the one clarify you may retry on your own): try once more with the legal
     name or without the suffix, then say "not found in InvestGame data after trying X and Y", never
     "it does not exist" or "it has no deals".
   - **`status: partial` or `failed`**: name the part that is missing; never present the reply as complete.
   - **No rows matched** (a `notices` row says so), after the one re-ask in rule 4: report the scope that
     matched nothing and offer to widen one named filter. A field marked "Unknown" means InvestGame holds no
     figure (show it as "n/d"), not that the parties never disclosed it: keep it out of totals, and say how many
     rows carry a value before ranking or filtering on it.
   - **A follow-up** ("sort it by date", "only the top 5") reshapes rows you already hold, unless the
     earlier reply was capped (`coverage.matched` above the rows held): then ask again. Each call is
     stateless: a new call restates the full scope, and on `InvestGame_query` passes the user's own
     words in `user_question`.

## 1 · The taxonomy - the only allowed vocabulary

**Sectors** (a company can have several): `GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS` · `OTHER`.
`OTHER` = tracked, but outside every covered gaming sector: real-money gambling and betting operators
and the platforms they run on, AI companies with no evidenced gaming connection, and other adjacent
firms. It stands alone (never combined with another sector), carries no gaming fields, and is
EXCLUDED from gaming sector totals - pull it only when the user asks about those companies
specifically. A studio that *makes* casino games is `GAMING_CONTENT` (genre `CASINO`).

**Platform** (GAMING_CONTENT only): `MOBILE` · `PC_CONSOLE` · `BROWSER` · `VR_AR`.
- "mobile" → `MOBILE`; "PC / console / AAA" → `PC_CONSOLE`; "browser/HTML5" → `BROWSER`; "VR/AR/XR" → `VR_AR`.

**Game genre** (GAMING_CONTENT, ten values): `PUZZLE` (incl. match-3/merge/word) · `SHOOTER` ·
`ACTION_RPG` · `STRATEGY_MOBA` · `CASINO` (casino *games*, not operators) · `SIMULATION_SANDBOX` ·
`SPORTS_RACING` · `ARCADE` (incl. hypercasual) · `TABLETOP` (digital card/board games) · `OTHER` (nothing else
fits; a genre breakdown will return `OTHER` rows, so name it rather than dropping them).

**Monetization** (GAMING_CONTENT): `IAP` (F2P/in-app purchases) · `IAA` (ad-supported) ·
`GAAS` (live service on PC, console, VR or browser; a mobile live-service game is `IAP`) · `UPFRONT_SALE` (premium/buy-to-play) ·
`DLC` (paid expansions) · `SUBSCRIPTION` (Game Pass / PS+).

**Content type** (GAMING_CONTENT): `DEVELOPER_1P_PUBLISHER` · `PUBLISHER_3P` · `OUTSOURCING_WFH`.

**Ecosystem segment** (GAMING_ECOSYSTEM only): `ESPORTS` · `CREATION_DEVELOPMENT` (helps *build* the
game - engines/tools) · `INFRASTRUCTURE_SERVICES` (helps *run/scale* - cloud, analytics, payments) ·
`ADTECH` (UA tools) · `HARDWARE` · `STREAMING_ENTERTAINMENT` · `DISTRIBUTION_SOCIAL_PLATFORMS`
(stores, launchers, and resellers of game keys, e-pins, gift cards or in-game currency) · `OTHER`
(retail/merch, physical board and card game publishers, gaming SPACs).
*Critical: `platform` ≠ `ecosystem_segment`. "Mobile" is a platform; "esports" is an ecosystem segment.*

**Consumer Apps subsegment** (CONSUMER_APPS only): `EDTECH` · `FITNESS_WELLNESS` ·
`ENTERTAINMENT_SOCIAL` · `FINTECH` · `OTHER`.

**Company type:** `ANGELS_INDIVIDUALS` · `VENTURE_CAPITAL_AND_ACC` · `PRIVATE_EQUITY_AND_INST` (investing a balance sheet or a fund) ·
`STRATEGIC_OR_CVC` (label "Strategic": any operating company, gaming or not) · `SERVICE_PROVIDERS` (firms that only advise or lend on deals: banks, advisors, brokers, law firms) · `ASSET` (IP/franchise) · `OTHER` (government, non-profits, associations). Advisor is a role read from the deals' advisor fields, not a type.

**Deal category** (five visible): `MA` (types `MA_CONTROL`, `MA_MINORITY`) · `EARLY_STAGE_INVESTMENT`
(accelerator/grant, Seed, Series A, undisclosed-early) · `LATE_STAGE_INVESTMENT` (Series B to H,
growth/expansion, undisclosed-late) · `PUBLIC_OFFERING` (`LISTING`, `PIPE`, `SECONDARY_OFFERING`,
`FIXED_INCOME`) · `NON_DILUTIVE_FINANCING` (label "Non-dilutive Financing": `UA_FINANCING`, `PRIVATE_DEBT`,
`DEVELOPMENT_FINANCING` labelled "Project Financing", publishing financing included; counted in general
analytics, not in funding raised): **22 visible types across 5 visible categories**.

**Deal type → display label** (a deal's `type` comes back as a raw code - render its InvestGame label, never
the code): `MA_CONTROL`→"M&A control (incl. LBO/MBO)" · `MA_MINORITY`→"M&A minority" · `SEED`→"Pre-Seed/Seed" ·
`SERIES_A`…`SERIES_H`→"Series A"…"Series H" · `GROWTH_OR_EXPANSION`→"Growth / Expansion" ·
`ACCELERATOR_GRANT`→"Accelerator / Grant" · `UNDISCLOSED_EARLY_STAGE`→"Undisclosed Early-stage" ·
`UNDISCLOSED_LATE_STAGE`→"Undisclosed Late-stage" · `LISTING`→"Listing (IPO/SPAC)" · `PIPE`→"PIPE" ·
`SECONDARY_OFFERING`→"Secondary Offering" · `FIXED_INCOME`→"Fixed Income" · `UA_FINANCING`→"UA Financing" ·
`PRIVATE_DEBT`→"Private Debt" ·
`DEVELOPMENT_FINANCING`→"Project Financing".

**Category → display label:** `MA`→"M&A" · `EARLY_STAGE_INVESTMENT`→"Early-stage investment" ·
`LATE_STAGE_INVESTMENT`→"Late-stage investment" · `PUBLIC_OFFERING`→"Public offering" ·
`NON_DILUTIVE_FINANCING`→"Non-dilutive Financing". Exit-path labels: `references/deal-taxonomy.md`.

**Region maps** (the country lists the tool uses; the web app's Region filter groups wider regions,
so totals can differ):
- Europe → GB, DE, FR, SE, NO, DK, FI, CH, NL, BE, AT, IT, ES, PT, PL, IE, CZ, RO
- Asia/APAC → JP, KR, CN, SG, AU, NZ, IN, TW, HK, TH, ID, VN, MY, PH
- North America → US, CA · LATAM → BR, MX, AR, CO, CL, PE
- MENA / Middle East & Africa → by headquarters region, never a typed country list: the Middle East
  (Turkey and Israel included) plus Africa. For a narrower cut, name the countries and say so.

## 2 · Canonical definitions - pin these every time (consistency)

Pin these so the same question returns the same number.

| Phrase | Canonical meaning |
|--------|-------------------|
| **"M&A"** | deal category `MA` only |
| **"fundraising" / "VC funding"** | `EARLY_STAGE_INVESTMENT` + `LATE_STAGE_INVESTMENT` |
| **"most funded companies" / "top raisers"** | with no basis named the tool ranks on raised capital (see the row below) and the answer states that basis. "By VC funding" ranks early- and late-stage rounds only, the basis of the site's Most Funded Companies view: name it when that is the ranking wanted |
| **"IPO" / "went public" / "listing"** | deal type `LISTING` only, not the whole `PUBLIC_OFFERING` category (which also holds PIPEs, secondary offerings and fixed income) |
| **"raised capital"** | every category except `MA` and `SECONDARY_OFFERING`: early, late, `PUBLIC_OFFERING` without `SECONDARY_OFFERING` (listings, PIPEs, fixed income) and `NON_DILUTIVE_FINANCING`. It is funding raised plus all non-dilutive financing |
| **Non-dilutive financing** | the `NON_DILUTIVE_FINANCING` category (label "Non-dilutive Financing": UA financing, private debt, project financing with publishing financing included), neither fundraising nor M&A. Counted in general analytics; the quarterly report holds out UA financing, project financing and secondary offerings, while private debt stays in |
| **"recent / latest / new"** | last **18 months** by effective date (`closed_date` ?? `announcement_date`) |
| **no time word at all** | no date filter - whole database |
| **deal size** | USD millions; undisclosed = no value recorded → excluded from sums, shown as "n/d" in lists. Control and minority M&A use different Size formulas: see `deal-taxonomy.md` |
| **enterprise value for multiples** | by category: M&A → **Upfront EV** at 100%; early/late rounds → **post-money EV**; a listing or a PIPE → **market cap at the offer**; a secondary offering, fixed income, non-dilutive financing and an accelerator or grant award carry no multiples. Never the Max/transaction EV |
| **multiples** | shown as "2.6x". **"NM"** = not meaningful: negative, a zero metric, or outside the band (EV/Revenue 0.1x to 20x; EV/EBITDA, EV/EBIT, EV/Cash EBITDA 0.25x to 50x). Blank = no data, which is not NM. Neither is zero |
| **date** | the **effective date** (`closed_date` ?? `announcement_date`) is the default anchor and matches the site filter, the curated views and the quarterly reports. The announcement date is used only when asked for. State which anchor the `assumptions` report |

When a sum and a count appear together, restrict to disclosed sizes so the two reconcile.

## 3 · How to ask - the precise-prompt patterns

Keep the canonical buckets and a platform/geo/stage filter explicit. The reference shots
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
   - *Deal lists:* target · country (the target company's headquarters country; a deal has no country of its own) · deal type · size USD · date · lead investor (+ EV/multiple for M&A).
   - *Investor/acquirer rankings:* name · distinct deal count · total disclosed USD.
   - *Company profile:* each round (type, size, date, investors) · disclosed valuation/EV · summary.
   - *Trend:* period · count · total value USD.
3. **Always append a methodology line:** period, geography, what's included/excluded (e.g. *"M&A =
   category MA; sizes USD m; undisclosed excluded from totals; last 18 months by effective date."*).
   Name the anchor the `assumptions` actually report, not the one you expected, and end the line
   with "Source: InvestGame, retrieved <today's date>".
4. **Flag, never hide, gaps:** "undisclosed", "n/d", "insufficient public data" - never invent a figure.
5. **Numbers are tabular and right-aligned;** currency in USD millions unless asked otherwise.
6. **Link every named deal, company and index** to its InvestGame page (always the `app.` subdomain):
   deal `https://app.investgame.net/deals/{deal_id}` · company `https://app.investgame.net/companies/{company_id}`
   · index `https://app.investgame.net/market-indices/{index_code}` · earnings document
   `https://app.investgame.net/api/v1/earnings-files/{document_id}/download/`. An `entities` entry's `url`
   is authoritative; with only an id (a table cell), build the URL from the pattern; an index link is
   built by hand. Never build a link from a name: no id, no link.

## 5 · Brand - when the user wants a report, chart, or one-pager

Branded output belongs to `investgame-format`: its two themes, colours, chart rules, templates and the
company or fund profile document. Hand the figures there; never restyle them here.

## 6 · Boundaries - what InvestGame cannot answer (say so; do not invent)

- **Talent flow across companies** ("who left one studio to start another") - key people are on
  each company's card (`InvestGame_company_query`), but there is no cross-company people query.
  Route the flow question to InvestGame custom research.
- **A headcount or headcount-growth ranking across companies** ("which studios grew fastest") is
  not self-serve: say so, and offer one company's headcount history or custom research.
- **An advisor league table** isn't directly tracked - answerable only as custom research.

Note what IS in scope (don't mistakenly decline it): **non-dilutive financing** is real and
queryable, **its own visible category** (`NON_DILUTIVE_FINANCING`, label "Non-dilutive Financing") holding UA
financing, private debt and project financing, counted in general analytics; **exit paths**
(first-time exits, public-to-private, carve-outs) are a filter you can ask for; **geography**
by any country or region is fully supported; **an investor's stage, sector or geography focus** is
answerable as the top of its own deals (indicative, not a stated mandate: say so); and **one
company's headcount history** is queryable: the headcount series sits on its card
(`InvestGame_company_query`).

When asked for any of these: state the limit, give the closest thing the data *can* answer, and offer
custom research. Honesty here is what keeps the database trusted.

## 7 · References - load the one the task needs

The sections above are the always-on core. Pull a reference file when you need the depth:

| Load this | When |
|-----------|------|
| `references/taxonomy.md` | Any question about a **company** field or boundary (is X gaming? which segment? mobile IAP vs IAA?) - every field, its values and what each means |
| `references/deal-taxonomy.md` | Reading a **deal**: what each type and category means, exit paths, participants and size |
| `references/definitions.md` | Any counting/sizing/multiple question - the canonical buckets that keep numbers consistent |
| `references/ten-shots.md` | Matching the user's intent to a proven query pattern |
| `references/research-playbook.md` | Any task needing web research beyond the deal data (deep reports, company/investor profiles, meeting prep) - the data-vs-web division of labour + the source catalogue |

## 8 · Companion skills - hand off to the right workflow

This skill is the data hub. For these jobs, use the matching companion skill (which calls back here for data):

| If the user wants… | Use |
|--------------------|-----|
| A valuation, comps, precedent-multiples, benchmarking or trend read | `investgame-analysis` |
| Live public-market data on a listed company (price, financials, earnings, analyst) or an FX conversion | `investgame-public-markets` |
| The gaming press / newsletters - a "what's happening" or this-fortnight read, a press brief, or the "Gaming Pulse" digest | `investgame-press` |
| A deep report, market/company/investor deep-dive, or meeting/call prep | `investgame-research` |
| Notes / a recap / summary from a call or meeting transcript | `investgame-research` |
| A table, chart, comparison or list shown cleanly in chat, or rendered as a branded file (PDF/PPTX/XLSX/HTML) | `investgame-format` |
