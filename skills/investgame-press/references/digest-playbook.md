# Digest construction playbook

The step-by-step pipeline the host LLM follows to build one **Gaming Pulse** edition: a fortnightly,
C-level gaming-press digest assembled from three proprietary datasets (the stored press corpus, the
InvestGame deal database, and InvestGame public-market data). Read this end to end before building.
The filter grammar and the topic facets live in the skill's `SKILL.md`, the source roster in
`press-sources.md`; this file owns the **build**.

Work through it as seven ordered stages: **Retrieve -> Cluster -> Synthesize -> Deals and markets desks -> Scan ->
Deep-dive review -> Render.** Stage 6 (the deep-dive review) is mandatory and gates the render: nothing
reaches the reader until every claim has passed it.

---

**Contents:** Prime directive: factual-only, every fact sourced (read first) · Two registers in one document · Section spine (fixed) + body (flexible) · Stage 1 - Retrieve the window · Stage 2 - Cluster by convergence, NOT by entity · Stage 3 - Synthesize each Big Story (factually) · Stage 4 - The Deals and Public-Markets desks (transactions are DB-authoritative) · Stage 5 - Scan register (breadth) · Stage 6 - DEEP-DIVE REVIEW (mandatory, gates the render) · Stage 7 - Render to Warm-White HTML (PDF-portable) · What this playbook is NOT (guards) · Quick build checklist (one pass, top to bottom)

## Prime directive: factual-only, every fact sourced (read first)

The Pulse **consolidates facts; it never creates opinion.** This is the single rule that overrides every
other instinct in this playbook. Concretely:

- **Allowed:** a fact present in a stored source (a newsletter body or the InvestGame database), the
  convergence count ("N independent newsletters covered this"), the proprietary DB overlay (a recorded
  deal value, rank, multiple, ownership fact), and a source's **own** analysis **with the attribution
  intact** ("Konvoy argues...", "Naavik's teardown estimates...", "Alinea forecasts...").
- **Forbidden:** any opinion, prediction, recommendation, "why it matters" editorial, or subjective
  framing written in InvestGame's own voice. No invented numbers, no inferred motives, no "this signals
  that...". If a claim is not in a stored source, it does not ship.
- **Every fact carries its source.** A press fact links to the post it came from; a deal/market fact links
  to the InvestGame entity page. The two layers stay visibly labelled (press vs InvestGame data) so the
  reader always knows which is which, exactly as in the research-playbook division of labour.

The C-level "so what" is delivered **factually**: convergence (how many newsletters independently said it)
plus the DB overlay (where it sits in the recorded deal record) plus attributed source analysis. That triad
is the insight. InvestGame never adds its own take.

---

## Two registers in one document

| Register | Job | Where it lives |
|----------|-----|----------------|
| **NARRATIVE** (insight) | A few stories told in depth: consolidation + convergence + DB overlay + attributed analysis | Big Stories, Deals desk, Public-Markets desk |
| **SCAN** (breadth) | Span everything else so the reader misses nothing | Coverage Sweep, The Wire, Reading List |

The mandate is **both**: genuine executive-grade depth on the handful of stories that matter, and total
breadth across the fortnight so nothing is missed. The two registers are how one document does both.

---

## Section spine (fixed) + body (flexible)

The **spine is always present, in this order.** The **body desks expand or shrink to the period** and may
be dropped when the window genuinely has nothing for them. Counts are **computed from the data, never
padded.**

| # | Section | Spine / body | Register | Contents |
|---|---------|--------------|----------|----------|
| 0 | **Cover** | fixed | - | Cadence label, date range, and a one-line **headline** stated as a FACT of coverage ("This fortnight the press converged most on X (N newsletters) and Y (M)"), never a prediction |
| 1 | **Executive Brief** | fixed | scan+narrative | 5-7 bullets, each a sourced fact + computed counts (posts, sources, deals, movers) |
| 2 | **Big Stories** | fixed | narrative | 3-6 convergence-ranked clusters; each = what-happened + DB overlay + attributed source take + source links |
| 3 | **Deals desk** | body | narrative | M&A + fundraising in the window from `InvestGame_query` (DB-authoritative); optional Content / Ecosystem split |
| 4 | **Public-Markets desk** | body | narrative | Movers by index segment and earnings from `InvestGame_press_query`; public offerings / IPOs from `InvestGame_query` |
| 5 | **Coverage Sweep** | fixed | scan | The 5 by-nature facets, each a short sourced list |
| 6 | **The Wire** | fixed | scan | The long tail, link-only, one line each |
| 7 | **Reading List** | body | scan | Notable long-form / essays / teardowns worth the click |
| 8 | **Methodology & Sources** | fixed | - | Window, source count, post count, convergence method, the factual-only posture, full source roster |

---

## Stage 1 - Retrieve the window

**Goal:** list every press post in the period lean first (title, source, date, topics, URL), then fetch
full bodies only for the top clusters (once Stage 2 has ranked them), a few articles per call. A preview
cell (`"_truncated": true`) is not the article: treat it as Wire-only until it is fetched alone.

- [ ] Call **`InvestGame_press_query`** for the window. **Default 14 days** (the fortnightly cadence); honor
      any window the user names in chat. A longer window yields more convergence signal for ranking.
- [ ] Once Stage 2 has ranked the clusters, fetch the **full article body** for the top ones, a few per
      call; synthesis quality depends on it, never on the teaser excerpt. Fetch a preview cell's story alone.
      A post with no body at all (paywalled, very recent, podcast) is Wire-only (link, do not synthesize
      from the teaser).
- [ ] Pull each post's topics (the multi-label facets), source, published date, URL, and paywalled
      flag. These drive clustering, the Coverage Sweep, and the click-through links.
- [ ] **Down-weight podcasts.** Podcast sources carry **show notes only**. They may corroborate
      a story or sit in the Wire, but a podcast **never leads a Big Story on thin show-notes alone**
      (it cannot supply the body text a synthesis needs).
- [ ] Record the **computed counts** now (total posts, distinct active sources, podcasts vs text). These
      feed the Exec Brief and Methodology and must be real, never estimated.

---

## Stage 2 - Cluster by convergence, NOT by entity

**Goal:** group the window's posts into stories, ranked by how many independent newsletters covered each.

This is the core move: clustering on the named entity produces mechanical, duplicated output. Cluster on
the **story**, and let cross-newsletter convergence be
the importance signal.

- [ ] **Group posts that describe the same underlying story**, even when they use different entities,
      framings, or headlines. One story = one cluster, regardless of how many newsletters touched it.
- [ ] **Count the distinct independent newsletters in each cluster.** That count is the story's **factual
      importance signal.** Five newsletters independently covering one event outranks a single deep essay,
      and the digest says so as a fact ("covered by N of the fortnight's sources").
- [ ] **Rank clusters by convergence count**, then by recency. The top **3-6** become Big Stories
      (Stage 3). The mid-tail flows into the Coverage Sweep (Stage 5); the long tail into the Wire.
- [ ] **Do not over-collapse.** If two events are genuinely distinct, keep them as separate clusters even
      when they share a company. When in doubt, split: a wrongly-merged cluster is a factual error the
      deep-dive review (Stage 6) is told to hunt for.
- [ ] **A Transactions-tagged cluster is a routing signal, not a desk.** Posts with the Transactions tag flag
      a deal the press is discussing; the **deal itself is owned by the Deals or Public-Markets desk**
      (the DB is the authoritative record). The press cluster becomes attributed *commentary* overlaid
      on the DB deal, never the source of the deal figures. See Stage 4.

---

## Stage 3 - Synthesize each Big Story (factually)

**Goal:** turn each top cluster into a short, dense, fully-sourced story. No invented "why it matters".

For each Big Story, assemble exactly these factual layers and nothing else:

1. [ ] **What happened, in four anchors: who / what / how-much / when.** Every anchor is a fact taken from
       a stored body, and every number, name, and date matches the source exactly.
2. [ ] **The convergence fact:** "Covered independently by N newsletters this fortnight" (the Stage-2 count).
       This is the importance statement, stated as a fact about coverage, not an opinion.
3. [ ] **The proprietary DB overlay (a fact, not a take).** Where the deal/company sits in the InvestGame
       record: the recorded deal value, its rank or precedent context, the multiple, the ownership history.
       Pull it from `InvestGame_query` (one company's ownership history from `InvestGame_company_query`,
       a live market cap from `InvestGame_market_query`). Present it as InvestGame data, linked to
       the entity page. This is the layer no newsletter has and is the digest's real edge.
4. [ ] **Attributed source analysis, where a source analyzed it.** If a newsletter offered its own read,
       include it **with the attribution intact** ("Konvoy argues...", "Deconstructor of Fun's teardown
       estimates..."). Never restate a source's opinion as InvestGame's own, and never invent one where the
       source gave none.
5. [ ] **Source links on every claim.** Each fact links to the post (press) or the entity page (DB) it came
       from. A story with an unlinkable claim has a claim that does not belong in it.

**Hard stop:** there is **no created "why it matters" paragraph.** The executive insight is layers 2-4
(convergence + DB overlay + attributed analysis). If you find yourself writing InvestGame's opinion about
the future or the meaning, delete it; it will fail Stage 6.

---

## Stage 4 - The Deals and Public-Markets desks (transactions are DB-authoritative)

**Goal:** the deal and public-market sections, sourced from the authoritative InvestGame datasets, not the
press. The press only overlays attributed commentary.

### Deals desk (via `InvestGame_query`)
- [ ] Pull **M&A and fundraising deals in the window** from `InvestGame_query` (the deal database is the
      authoritative record for gaming M&A, funding and IPOs). Date by **effective date**
      (the close date, or the announcement date when not yet closed), matching the InvestGame quarterly
      convention.
- [ ] Default deal-list columns (mirror the app): target, country, deal type, size USD, date, lead investor;
      add EV and EV/Revenue for M&A. Numbers right-aligned, USD millions, undisclosed flagged not invented.
- [ ] **Optional Content / Ecosystem split** via the InvestGame sector tags when the period has enough
      volume to warrant two sub-tables. Otherwise one ranked table.
- [ ] **Press deal-commentary overlays, it does not replace.** If a Transactions-tagged press cluster
      discusses a desk deal, attach it as attributed commentary on the DB row. The figures are the DB's;
      the colour is the newsletter's, attributed.
- [ ] Link every deal row to its **InvestGame deal page**. Append a one-line methodology note (period basis,
      what is included/excluded).
- [ ] Reach for the `ten-shots` query patterns to frame these pulls (notable acquisitions, most-active
      acquirers, precedent multiples) rather than building a query from scratch.

### Public-Markets desk (movers and earnings via `InvestGame_press_query`; public offerings / IPOs / listings via `InvestGame_query`)
Three parts; use `InvestGame_market_query` only for a live quote or a full statement on one company:
- [ ] **Movers:** the period's top share-price gainers and decliners among tracked public gaming companies,
      bucketed by InvestGame's index segments as the tool returns them. **Do not invent buckets**: use what
      the data carries.
- [ ] **Earnings:** the latest earnings releases in the window, each with **EPS surprise (actual vs
      estimate), revenue, and the market reaction** (the post-print price move). Facts only; a source's
      earnings-call read may be quoted with attribution.
- [ ] **Public offerings / IPOs / listings:** pull every public offering, IPO or new listing in the window
      from `InvestGame_query` (the deal database) and show it here, in the Public-Markets desk (not in the
      editorial sweep).
- [ ] Present every public figure as **InvestGame market data** (the source rule in `SKILL.md`,
      Presenting). It supplements the proprietary deal record, it never overrides it: a live market cap and a
      historical deal EV measure different things, so say which is which when they appear to differ.

---

## Stage 5 - Scan register (breadth)

**Goal:** guarantee nothing is missed, via the by-nature facets and the link-only long tail.

### Coverage Sweep (the 5 editorial facets)
Organize the mid-tail (everything not a Big Story or a desk row) into the **five by-nature facets** posts
are tagged with. Each facet is a short, sourced list (one line per item, source-linked):

| Facet | What lands here |
|----------------------|-----------------|
| **Product, releases & live-ops** | launches, updates, live-ops, content drops |
| **UA, marketing & monetization** | user acquisition, ad monetization, pricing, marketing |
| **AI & tech** | AI tooling, infra, engines, technical shifts |
| **People & organizations** | exec moves, layoffs, studio openings/closures, restructures |
| **Industry & platform trends** | policy, regulation, platform rules, market reports, structural trends |

- [ ] Geography is **not** a facet: it is a within-item attribute (an "X-based studio" tag inside a line),
      never its own section.
- [ ] A post can appear under more than one facet (multi-label), but keep each line tight and sourced.

### The Wire (long tail, link-only)
- [ ] Everything that did not earn a Big Story, a desk row, or a Sweep line, as a **one-line, link-only**
      entry (headline + source + link). No synthesis, no commentary. This is pure breadth insurance.

### Reading List (optional)
- [ ] Notable long-form, essays, and teardowns worth a deliberate click, with a one-line factual descriptor
      and the source. Podcasts may appear here flagged as audio / show-notes.

---

## Stage 6 - DEEP-DIVE REVIEW (mandatory, gates the render)

**Goal:** before a single line reaches the reader, a dedicated review pass checks **every claim** against
the stored sources and strips anything that fails. This is a hard requirement. Run it as a distinct pass, ideally with a second adversarial
agent, **after** drafting and **before** rendering.

For **each claim** in the draft, all five checks must pass:

- [ ] **(a) Factual & sourced.** The claim is present in a stored source body (a press post) or the
      InvestGame database, and it links to that source. If it cannot be traced to stored content, **drop it.**
      No claim survives on memory or inference.
- [ ] **(b) No created opinion.** No opinion, prediction, recommendation, or subjective "why it matters" in
      InvestGame's voice. Attributed source-analysis is allowed **only with the attribution intact**
      ("Konvoy argues..."); strip any editorializing that lost its attribution or never had one.
- [ ] **(c) Anti-hallucination.** Every number, name, ticker, and date **matches the source exactly.**
      Re-check each figure against the stored body or the DB row. A transposed number or a wrong date is a
      drop-or-fix, not a rounding nicety.
- [ ] **(d) Devil's advocate.** Actively try to **falsify each headline claim**: is the convergence count
      right, did two distinct stories get merged into one cluster, is the "largest / first / record" framing
      actually supported by the DB? If a headline claim cannot survive a falsification attempt, weaken it to
      what the source supports or drop it.
- [ ] **(e) No machine artifacts or duplicates.** Scan for and remove these failure modes:
      - a **leaked JSON envelope** or raw tool output pasted into prose;
      - a **"corrupted item" / placeholder** (e.g. "[item unavailable]");
      - a **duplicated story** (the same story twice under two headlines);
      - a **headline repeated verbatim as the first bullet**;
      - any **unattributed projection** presented as fact.

**Drop log.** Keep a short list of what was dropped or corrected and why (failed which check). It is not
rendered into the digest, but it is the proof the review actually ran. Never ship a claim that failed any
check; fix it against the source or remove it.

---

## Stage 7 - Render to Warm-White HTML (PDF-portable)

**Goal:** produce the branded, click-through, print-clean digest. The `assets/templates/digest.html`
template holds the layout: this stage fills a **content contract**, it does not write CSS.

- [ ] Use the **Warm-White** theme, its colours, fonts and the navy logo, as `investgame-format` defines
      them. Positive movement in **deep teal `#00928A`, never green**; caution in **rust**, sparingly.
- [ ] **Clickable TOC** on the Contents slide after the cover, wired to the section anchors.
- [ ] **Per-claim click-through:** every fact links to its source, press post or InvestGame entity page.
      Every deal row links to its InvestGame deal page; every public name to its profile.
- [ ] **Embedded charts/images** for chart-heavy stories only when you already hold an image URL the
      source published, with the source credited in the caption; otherwise link to the article.
- [ ] **Computed counts only** in the Cover and Exec Brief (posts, sources, deals, movers): the real Stage-1
      numbers, never padded or rounded for effect.
- [ ] **Methodology & Sources** at the end: window, source count, post count, the convergence method, the
      factual-only posture, and the full source roster with links.
- [ ] Keep the template's `logos/` folder beside the rendered page: the digest template reads its
      logo from there, not from the brand kit's `../logos/`.
- [ ] Export to PDF through `investgame-format`: this playbook owns the content, that skill owns the brand
      render.

---

## What this playbook is NOT (guards)

- **Not an opinion column.** No InvestGame predictions, recommendations, or "why it matters" takes. Only
  consolidated facts, convergence, DB overlay, and attributed source analysis.
- **Not an entity tracker.** Cluster by **story and convergence**, never by named entity.
- **Not a press-sourced deal sheet.** Deal and market figures come from the **authoritative InvestGame
  datasets**; the press only overlays attributed commentary.
- **Not a teaser digest.** Synthesize from the **full stored bodies**, never from the teaser excerpts.
- **Not auto-shipped.** Nothing renders until the Stage-6 deep-dive review has passed on every claim and the
  drop log exists.
- **Not a machine dump.** No leaked JSON, no placeholders, no duplicates, no headline-as-first-bullet: the
  exact artifacts the deep-dive review is built to catch.

## Quick build checklist (one pass, top to bottom)

1. [ ] Retrieve the 14-day window lean (topics/source/date/paywall), then full bodies for the top clusters;
       down-weight podcasts; record computed counts.
2. [ ] Cluster by story; count independent newsletters; rank; do not over-collapse.
3. [ ] Synthesize 3-6 Big Stories: who/what/how-much/when + convergence + DB overlay + attributed analysis;
       source-link every claim; no created "why it matters".
4. [ ] Build the Deals desk (`InvestGame_query`, DB-authoritative) and the Public-Markets desk
       (movers by segment and earnings from `InvestGame_press_query`; public offerings from `InvestGame_query`).
5. [ ] Fill the Coverage Sweep (5 facets) and the link-only Wire; optional Reading List.
6. [ ] Run the deep-dive review on every claim (a-e); fix or drop failures; keep the drop log.
7. [ ] Render to Warm-White `digest.html`: TOC, per-claim links, charts only from published image URLs, navy logo, computed
       counts, methodology; export to PDF.
