---
name: investgame-press
version: 0.10.16
description: >
  What the gaming press is publishing: InvestGame's curated corpus of industry newsletters and shows,
  its news feed by category or tag, and the periodic "Gaming Pulse" digest built from them with
  InvestGame's deal and market data. Use for "what's happening in gaming this week", "what are the
  newsletters saying about X", "only Naavik, last two weeks", "people news", "news tagged layoffs", a
  press brief or a digest, and for the share-price movers and earnings releases InvestGame records for a
  digest. Owns InvestGame_press_query. A deal or company fact goes to investgame-gaming-data; a live
  quote or FX to investgame-public-markets; a full market report to investgame-research. Not for game
  design or generic software questions.
---

# InvestGame Press & Digest

The gaming-press layer. The hub (`investgame-gaming-data`) answers deal and company facts; the
public-markets spoke answers live prices and FX. This skill reads what the **gaming press** is
publishing - a curated corpus of newsletters and shows (Naavik, The Game Business, Game File,
GameDiscoverCo, Mobile Ad Revenue, MIDiA, Deconstructor of Fun, SuperJoost, InvestGame's own, and more),
and turns a window of it into the C-level **"Gaming Pulse" digest**, overlaid with InvestGame's own
deal and market data. One tool: **`InvestGame_press_query`**.

## When to use it - route the question

Four tools, four jobs. Pick by what the question is *about*:

| The question is about… | Use | Tool |
|------------------------|-----|------|
| What the **press** is saying - a topic, a source, a window, a digest, "what's happening" - and the share-price movers and earnings releases InvestGame records for the digest | **this skill** | `InvestGame_press_query` |
| A **deal / company fact** - how many M&A, what a studio raised, a multiple, a category | `investgame-gaming-data` (hub) | `InvestGame_query` |
| **One company's own profile** - headcount, key people, ownership, its own deal totals | `investgame-gaming-data` (hub) | `InvestGame_company_query` |
| A **live price / market cap / full statement / earnings on one listed company / FX** | `investgame-public-markets` | `InvestGame_market_query` |

**Negative triggers (do NOT answer here):** a deal or company fact → hand to the hub; a live share
price, market cap or currency conversion → hand to public-markets. The press corpus carries *what was
written*, never the authoritative transaction record - for any number on a deal, a raise, or a price,
route to the owning tool. The press only *overlays* those facts as attributed commentary.

## How the user filters - the phrasing grammar

Teach the user (and yourself) the cuts. They compose: "only Naavik + AI, last two weeks".

| Cut by | The user says | How it resolves |
|--------|---------------|-----------------|
| **Source** | "only Naavik", "just Mobile Ad Revenue and Game File", "the InvestGame newsletter" | exact or fuzzy source name; podcasts are flagged **show-notes-only** (down-weighted) |
| **Topic** | "only UA", "AI stories", "people moves / layoffs", "anything on policy or regulation" | one of the **five by-nature facets** below (posts are multi-label) |
| **Window** | "the last two weeks", "this fortnight", "since June 1" | a date window - **default 14 days** when the user gives no time word |
| **Drill** | "go deeper on the Scopely story", "what did each newsletter say about X" | pulls the **full article bodies** for that story + the source links |
| **Feed** | "People news", "earnings news", "news tagged Layoffs" | the InvestGame news feed by its category or tag |

**The five by-nature topic facets** (the only topic vocabulary - geography is *not* a topic, it is a
within-item "X-based" tag):

1. **Product, releases & live-ops** - launches, updates, live-ops, content.
2. **UA, marketing & monetization** - user acquisition, ad-tech, pricing, IAP/IAA.
3. **AI & tech** - AI tooling, engines, infrastructure, platform tech.
4. **People & organizations** - exec moves, layoffs, studio openings/closures, restructurings.
5. **Industry & platform trends** - policy, regulation, platform shifts, market reports & data.

A sixth tag, **Transactions** (M&A / fundraising / IPO), is only a *routing tag*: those facts come from
the **authoritative InvestGame deal & market data**, never from the editorial sweep.
When a press item discusses a deal, overlay it onto the DB deal - don't count it from the press.

## The tool - `InvestGame_press_query` (this skill owns it)

- **Call** `InvestGame_press_query` with a plain-English question that pins the cut(s): the source(s),
  the topic facet, and the window. Prefer one precise prompt over a vague one.
- The corpus holds, per post: title, the teaser summary, the **full article body** (text only, no
  images) where the source allows it (paywalled, very recent and podcast posts carry only the teaser
  or show notes), the topic facets, the published date, the source, and the URL - so it can answer
  richly, not just list headlines.
- **Name the facet in the question** ("UA and monetization", "people moves") so the tool filters on
  the tags rather than on a keyword; a facet catches synonyms; the very newest posts may not
  carry a facet yet, so widen with a keyword if a fresh story is missing.
- **Bodies have a budget.** One article is served whole up to a per-article cap; an answer holds
  several whole articles (more when they are short) before later rows fall back to a preview: a cell shaped
  `{"_truncated": true, "chars": N, "preview": "..."}`. A preview is not the article: to read one
  story, ask for that story alone ("go deeper on the Scopely piece") and the body comes back whole.
- **An empty or refused reply** (no rows, credits, rate limit): follow the hub's rule 8. An empty
  source or topic filter means the corpus holds nothing tagged that way in the window: say so and
  offer a wider window or another facet instead.
- **Podcasts are show-notes-only**: they can corroborate a story or appear in the Wire, but they
  never *lead* a story on thin show-notes alone.

## The two non-negotiables

1. **Transactions are DB-authoritative, never press-counted.** The InvestGame deal database is the
   authoritative record for M&A, fundraising and IPOs. Press deal-commentary is *overlay only* - attributed context on top of
   the DB figure, never the figure itself. For any transaction count, size, or multiple, the number
   comes from `InvestGame_query` (hub), public offerings, IPOs and listings included; movers and
   earnings come from `InvestGame_press_query`. The press never overrides a proprietary figure.
2. **Factual-only - consolidate, never opine.** The press layer *aggregates and synthesizes facts*; it
   does **not** create opinions, predictions, decisions, or subjective statements. Every fact must (a)
   reference a source and (b) be present in that source's **stored** text. A source's *own* analysis may
   appear **only if explicitly attributed** - "Konvoy argues…", "Alinea forecasts…" - never in
   InvestGame's voice, never invented. This is the headline rule; the deep-dive review (below) enforces it.

## Building the digest - the construction contract

The "Gaming Pulse" digest serves gaming **C-level** readers (CEO / CFO / CSO / corp-dev / scaling
founders). It must do **both** jobs at once, in **two registers**:

- **NARRATIVE register (insight)** - the Big Stories: convergence-ranked story clusters, each with
  *what happened* + the proprietary *DB overlay* (a fact, not an opinion) + the *attributed*
  cross-newsletter take + source links.
- **SCAN register (breadth)** - miss nothing: the Coverage Sweep across the five facets, plus a
  link-only Wire for the long tail.

**Fixed spine (always present):** Cover (cadence + window + headline) · Contents (clickable) ·
Executive Brief (counts) · **3-6 Big Stories** · Coverage Sweep · The Wire · Methodology & Sources.

**Flexible body (sized to the period, counts computed never padded):** Deals desk · Public-Markets desk
· Reading list.

**The three desks - each on a different proprietary dataset:**

- **Press desk** (this skill, `InvestGame_press_query`) - the Big Stories + the Coverage Sweep.
- **Deals desk** (`investgame-gaming-data`, `InvestGame_query`) - M&A + fundraising from the DB,
  optionally split Content vs Ecosystem by our sector tags. DB-authoritative.
- **Public-Markets desk** - **movers and earnings come from `InvestGame_press_query`** (this skill), the
  tool that reads InvestGame's recorded share-price movers, earnings releases and index segments. Movers are
  the share-price moves InvestGame recorded in the window, bucketed by index segment, not a
  recomputed weekly change. **Public offerings / IPOs / listings come from the hub** (`InvestGame_query`).
  Use `investgame-public-markets` only for a live quote or a full financial statement on one company.

**Cluster by CONVERGENCE, not entity.** Group posts that describe the *same story*; the count of
independent newsletters covering it is its importance signal. The "so what" for a C-level reader is the **factual DB overlay + the
convergence count + attributed source analysis**, never InvestGame's own opinion. When in doubt whether
two items are one story, keep them separate.

## The deep-dive review gate - mandatory before any render

No digest reaches the reader until a dedicated review pass clears **every** claim.

1. **Factual & sourced** - the claim is present in the stored source text and references it; drop it if not.
2. **No opinion** - no created opinion, prediction, or subjective statement; attributed source-analysis
   is kept **only** with the attribution intact, otherwise strip the editorializing.
3. **Anti-hallucination** - every number, name and date matches the source exactly.
4. **Devil's advocate** - a second pass actively tries to falsify each headline claim.
5. **No machine artifacts** - no leaked JSON, no "corrupted item" placeholders, no duplicate stories,
   no headline repeated as the first bullet.

Fix or drop anything that fails, and log what was dropped.

## Presenting - hand off to investgame-format

This skill decides **what** the digest says; `investgame-format` renders it on-brand. The digest ships
as a **Warm-White** 16:9 slide-format HTML digest (the `assets/templates/digest.html` template:
clickable TOC, story slides, the deal table with per-row links into the InvestGame app, the Public-Markets movers grid +
earnings cards, an embedded-image slot for chart-heavy stories, the Wire, the Reading list, and the
Methodology), portable to PDF. Source line stays neutral ("InvestGame"); never name or hint at how the
market data is obtained.

## Not investgame-research

Both do deep work, but they are different jobs. `investgame-research` builds a **bespoke** deliverable
for one subject - a market landscape, a company/investor profile, meeting prep - on request. This skill
runs the **repeatable, periodic press digest** off the curated corpus with a fixed editorial contract
and the deep-dive review gate. A one-off "research the mobile market for a deck" is research; "what's the
gaming press saying this fortnight / build the digest" is this skill.

## Common mistakes

- Counting a deal, raise, or multiple from the press instead of routing to `InvestGame_query`.
- Letting a press figure override a proprietary DB figure (it only overlays as attributed context).
- Inventing a "why it matters" - the insight is the DB overlay + the convergence count + attributed
  analysis, never InvestGame's own opinion or prediction.
- Clustering by entity instead of by story.
- Leading a Big Story on a podcast's show notes alone.
- Rendering before the deep-dive review gate has cleared every claim.
- Defaulting to a 7-day window - the press default is **14 days** unless the user says otherwise.

## References - load the one the task needs

| Load this | When |
|-----------|------|
| `references/press-sources.md` | Naming or grouping sources - the curated corpus + which are podcasts (show-notes-only) |
| `references/digest-playbook.md` | Building a digest - the seven-stage build (retrieve, cluster, synthesize, deals and markets desks, scan, deep-dive review, render) + the section contract |
| `assets/templates/digest.html` | Rendering - the Warm-White digest template (hand to `investgame-format`) |
