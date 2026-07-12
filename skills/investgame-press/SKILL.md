---
name: investgame-press
version: 0.8.0
description: >
  The gaming-press layer of the InvestGame skills — what the industry's newsletters and shows are
  publishing, and the fortnightly "Gaming Pulse" digest built from them. Use the moment a question is about
  the gaming PRESS itself rather than a deal or a price: "what's happening in gaming", "what are the
  newsletters saying", "this week / this fortnight in gaming", "the gaming press", "a press brief", a
  "digest", or filtering the press by source ("only Naavik / Mobile Ad Revenue"), by topic (product &
  live-ops, UA & monetization, AI & tech, people, platform trends), or by time window. It also builds the
  digest — the period's press overlaid with InvestGame's proprietary deal and market data. Owns the
  InvestGame_press_query tool. Do NOT use for a deal or company FACT (M&A counts, what a studio raised, an
  EV/Revenue multiple) — that is the investgame-gaming-data hub; or for a live share price, market cap or FX
  rate — that is investgame-public-markets. Not for game-design or generic software questions.
---

# InvestGame Press & Digest

The gaming-press layer. The hub (`investgame-gaming-data`) answers deal and company facts; the
public-markets spoke answers live prices and FX. This skill reads what the **gaming press** is
publishing — a curated corpus of newsletters and shows (Naavik, The Game Business, Game File,
GameDiscoverCo, Mobile Ad Revenue, MIDiA, Deconstructor of Fun, SuperJoost, InvestGame's own, and more)
— and turns a window of it into the C-level **"Gaming Pulse" digest**, overlaid with InvestGame's own
deal and market data. One tool: **`InvestGame_press_query`**.

## When to use it — route the question

Three tools, three jobs. Pick by what the question is *about*:

| The question is about… | Use | Tool |
|------------------------|-----|------|
| What the **press** is saying — a topic, a source, a window, a digest, "what's happening" | **this skill** | `InvestGame_press_query` |
| A **deal / company fact** — how many M&A, what a studio raised, a multiple, a category | `investgame-gaming-data` (hub) | `InvestGame_query` |
| A **live price / market cap / earnings / FX** on a listed company | `investgame-public-markets` | `InvestGame_market_query` |

**Negative triggers (do NOT answer here):** a deal or company fact → hand to the hub; a live share
price, market cap or currency conversion → hand to public-markets. The press corpus carries *what was
written*, never the authoritative transaction record — for any number on a deal, a raise, or a price,
route to the owning tool. The press only *overlays* those facts as attributed commentary.

## How the user filters — the phrasing grammar

Teach the user (and yourself) the three cuts. They compose: "only Naavik + AI, last two weeks".

| Cut by | The user says | How it resolves |
|--------|---------------|-----------------|
| **Source** | "only Naavik", "just Mobile Ad Revenue and Game File", "the InvestGame newsletter" | exact or fuzzy source name; podcasts are flagged **show-notes-only** (down-weighted) |
| **Topic** | "only UA", "AI stories", "people moves / layoffs", "anything on policy or regulation" | one of the **five by-nature facets** below (posts are multi-label) |
| **Window** | "the last two weeks", "this fortnight", "since June 1" | a date window — **default 14 days** when the user gives no time word (D7) |
| **Drill** | "go deeper on the Scopely story", "what did each newsletter say about X" | pulls the **full article bodies** for that story + the source links |

**The five by-nature topic facets** (the only topic vocabulary — geography is *not* a topic, it is a
within-item "X-based" tag):

1. **Product, releases & live-ops** — launches, updates, live-ops, content.
2. **UA, marketing & monetization** — user acquisition, ad-tech, pricing, IAP/IAA.
3. **AI & tech** — AI tooling, engines, infrastructure, platform tech.
4. **People & organizations** — exec moves, layoffs, studio openings/closures, restructurings.
5. **Industry & platform trends** — policy, regulation, platform shifts, market reports & data.

A sixth tag, **Transactions** (M&A / fundraising / IPO), is only a *routing tag*: those facts come from
the **authoritative InvestGame deal & market data (~95% coverage)**, never from the editorial sweep.
When a press item discusses a deal, overlay it onto the DB deal — don't count it from the press.

## The tool — `InvestGame_press_query` (this skill owns it)

Mirror how `investgame-public-markets` owns `InvestGame_market_query`: every press question is served
by this one tool, and nothing else routes here.

- **Call** `InvestGame_press_query` with a plain-English question that pins the cut(s): the source(s),
  the topic facet, and the window. Prefer one precise prompt over a vague one.
- The corpus holds, per post: title, the teaser summary, the **full article `body_markdown`** (≈15× the
  teaser), the topic facets, the published date, the source, and the URL — so it can answer richly, not
  just list headlines.
- **Two response modes** (same envelope as the other tools):
  `{"mode":"clarify","questions":[...]}` — the ask is underspecified or out of scope; put those
  `questions` to the user verbatim and stop (no data ran), then call again with the answer — or
  `{"mode":"data","tables":[{name,columns,rows}],"entities":[...]}` — read the tables and answer,
  linking the sources.
- **Podcasts are show-notes-only** (D11): they can corroborate a story or appear in the Wire, but they
  never *lead* a story on thin show-notes alone.

## The two non-negotiables

1. **Transactions are DB-authoritative, never press-counted.** The InvestGame deal database covers ~95%
   of M&A, fundraising and IPOs. Press deal-commentary is *overlay only* — attributed context on top of
   the DB figure, never the figure itself. For any transaction count, size, or multiple, the number
   comes from `InvestGame_query` (hub); public offerings, movers and earnings come from the
   Public-Markets desk. The press never overrides a proprietary figure.
2. **Factual-only — consolidate, never opine.** The press layer *aggregates and synthesizes facts*; it
   does **not** create opinions, predictions, decisions, or subjective statements. Every fact must (a)
   reference a source and (b) be present in that source's **stored** text. A source's *own* analysis may
   appear **only if explicitly attributed** — "Konvoy argues…", "Alinea forecasts…" — never in
   InvestGame's voice, never invented. This is the headline rule; the deep-dive review (below) enforces it.

## Building the digest — the construction contract

The "Gaming Pulse" digest serves gaming **C-level** readers (CEO / CFO / CSO / corp-dev / scaling
founders). It must do **both** jobs at once, in **two registers**:

- **NARRATIVE register (insight)** — the Big Stories: convergence-ranked story clusters, each with
  *what happened* + the proprietary *DB overlay* (a fact, not an opinion) + the *attributed*
  cross-newsletter take + source links.
- **SCAN register (breadth)** — miss nothing: the Coverage Sweep across the five facets, plus a
  link-only Wire for the long tail.

**Fixed spine (always present):** Cover (edition + window + period thesis) · Executive Brief (counts +
clickable TOC) · **≥1 Big Story** · Coverage Sweep · The Wire · Methodology & Sources.

**Flexible body (sized to the period, counts computed never padded):** Deals desk · Public-Markets desk
· Reading list.

**The three desks — each on a different proprietary dataset:**

- **Press desk** (this skill, `InvestGame_press_query`) — the Big Stories + the Coverage Sweep.
- **Deals desk** (`investgame-gaming-data`, `InvestGame_query`) — M&A + fundraising from the DB,
  optionally split Content vs Ecosystem by our sector tags. DB-authoritative.
- **Public-Markets desk** (`investgame-public-markets`, `InvestGame_market_query`; IPOs from the hub) —
  weekly share-price **movers bucketed by the five content segments + AdTech**; latest **earnings**
  (EPS surprise / revenue / market reaction); and **public offerings / IPOs / listings**.

**Cluster by CONVERGENCE, not entity.** Group posts that describe the *same story*; the count of
independent newsletters covering it is its importance signal. (The old system clustered on *entity* and
failed — do not repeat it.) The "so what" for a C-level reader is the **factual DB overlay + the
convergence count + attributed source analysis**, never InvestGame's own opinion. When in doubt whether
two items are one story, keep them separate.

## The deep-dive review gate — mandatory before any render

No digest reaches the reader until a dedicated review pass clears **every** claim. This is the #1
requirement; a prior hand-built edition shipped a leaked JSON envelope, a "this item was corrupted"
placeholder, and a duplicated story to real recipients — exactly what this gate exists to catch.

1. **Factual & sourced** — the claim is present in the stored source text and references it; drop it if not.
2. **No opinion** — no created opinion, prediction, or subjective statement; attributed source-analysis
   is kept **only** with the attribution intact, otherwise strip the editorializing.
3. **Anti-hallucination** — every number, name and date matches the source exactly.
4. **Devil's advocate** — a second pass actively tries to falsify each headline claim.
5. **No machine artifacts** — no leaked JSON, no "corrupted item" placeholders, no duplicate stories,
   no headline repeated as the first bullet.

Fix or drop anything that fails, and log what was dropped.

## Presenting — hand off to investgame-format

This skill decides **what** the digest says; `investgame-format` renders it on-brand. The digest ships
as a **Warm-White** HTML report (the `assets/templates/digest.html` partial set: clickable TOC, story
bodies, the deal table with per-row links into the InvestGame app, the Public-Markets movers grid +
earnings cards, an embedded-image slot for chart-heavy stories, the Wire, the Reading list, and the
Methodology), portable to PDF. Source line stays neutral ("InvestGame"); never name or hint at how the
market data is obtained.

## Not investgame-research

Both do deep work, but they are different jobs. `investgame-research` builds a **bespoke** deliverable
for one subject — a market landscape, a company/investor profile, meeting prep — on request. This skill
runs the **repeatable, periodic press digest** off the curated corpus with a fixed editorial contract
and the deep-dive review gate. A one-off "research the mobile market for a deck" is research; "what's the
gaming press saying this fortnight / build the digest" is this skill.

## Common mistakes

- Counting a deal, raise, or multiple from the press instead of routing to `InvestGame_query`.
- Letting a press figure override a proprietary DB figure (it only overlays as attributed context).
- Inventing a "why it matters" — the insight is the DB overlay + the convergence count + attributed
  analysis, never InvestGame's own opinion or prediction.
- Clustering by entity instead of by story (the old system's core failure).
- Leading a Big Story on a podcast's show notes alone.
- Rendering before the deep-dive review gate has cleared every claim.
- Defaulting to a 7-day window — the press default is **14 days** unless the user says otherwise.

## References — load the one the task needs

| Load this | When |
|-----------|------|
| `references/press-sources.md` | Naming or grouping sources — the curated corpus + which are podcasts (show-notes-only) |
| `references/digest-playbook.md` | Building a digest — the retrieve → cluster → synthesize → overlay → deep-dive review → render steps + the section contract |
| `assets/templates/digest.html` | Rendering — the Warm-White digest partials (hand to `investgame-format`) |
