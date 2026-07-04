# Digest construction playbook

The step-by-step pipeline the host LLM follows to build one **Gaming Pulse** edition: a fortnightly,
C-level gaming-press digest assembled from three proprietary datasets (the stored press corpus, the
InvestGame deal database, and InvestGame live public-market data). Read this end to end before building.
The filter grammar, the source roster and the topic facets live in the sibling references
(`press-sources.md`, `topic-facets.md`); this file owns the **build**.

Work through it as seven ordered stages: **Retrieve -> Cluster -> Synthesize -> Three desks -> Scan ->
Deep-dive review -> Render.** Stage 6 (the deep-dive review) is mandatory and gates the render: nothing
reaches the reader until every claim has passed it.

---

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
| 0 | **Cover** | fixed | - | Edition number, date range, and a one-line **period thesis** stated as a FACT of coverage ("This fortnight the press converged most on X (N newsletters) and Y (M)"), never a prediction |
| 1 | **Executive Brief** | fixed | scan+narrative | 5-7 bullets, each a sourced fact + computed counts (posts, sources, deals, movers) + the clickable TOC |
| 2 | **Big Stories** | fixed (>=1) | narrative | 3-6 convergence-ranked clusters; each = what-happened + DB overlay + attributed source take + source links |
| 3 | **Deals desk** | body | narrative | M&A + fundraising in the window from `InvestGame_query` (DB-authoritative); optional Content / Ecosystem split |
| 4 | **Public-Markets desk** | body | narrative | Movers by segment + AdTech, earnings, and public offerings / IPOs from `InvestGame_market_query` |
| 5 | **Coverage Sweep** | fixed | scan | The 5 by-nature facets, each a short sourced list |
| 6 | **The Wire** | fixed | scan | The long tail, link-only, one line each |
| 7 | **Reading List** | body | scan | Notable long-form / essays / teardowns worth the click |
| 8 | **Methodology & Sources** | fixed | - | Window, source count, post count, convergence method, the factual-only posture, full source roster |

---

## Stage 1 - Retrieve the window

**Goal:** pull every press post in the period, with full bodies, into working context.

- [ ] Call **`InvestGame_press_query`** for the window. **Default 14 days** (the fortnightly cadence); honor
      any window the user names in chat. A longer window yields more convergence signal for ranking.
- [ ] Ask for the **full `body_markdown`**, not the teaser excerpt. The stored body is ~15x richer than the
      feed summary; synthesis quality depends on it. If a post has no stored body yet, treat it as Wire-only
      (link, do not synthesize from a 140-char teaser).
- [ ] Pull each post's `topics` (the multi-label facets), `source`, `published_at`, `url`, and
      `is_paywalled` flag. These drive clustering, the Coverage Sweep, and the click-through links.
- [ ] **Down-weight podcasts.** Sources flagged `is_podcast` carry **show notes only**. They may corroborate
      a story or sit in the Wire, but a podcast **never leads a Big Story on thin show-notes alone**
      (it cannot supply the body text a synthesis needs).
- [ ] Record the **computed counts** now (total posts, distinct active sources, podcasts vs text). These
      feed the Exec Brief and Methodology and must be real, never estimated.

---

## Stage 2 - Cluster by convergence, NOT by entity

**Goal:** group the window's posts into stories, ranked by how many independent newsletters covered each.

This is the core move and the exact thing the old system got wrong (it clustered on the named entity and
produced mechanical, duplicated output). Cluster on the **story**, and let cross-newsletter convergence be
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
- [ ] **A transactions-tagged cluster is a routing signal, not a desk.** Posts tagged `transactions` flag
      a deal the press is discussing; the **deal itself is owned by the Deals or Public-Markets desk**
      (the DB is authoritative, ~95% coverage). The press cluster becomes attributed *commentary* overlaid
      on the DB deal, never the source of the deal figures. See Stage 4.

---

## Stage 3 - Synthesize each Big Story (factually)

**Goal:** turn each top cluster into a short, dense, fully-sourced story. No invented "why it matters".

For each Big Story, assemble exactly these factual layers and nothing else:

1. [ ] **What happened, in four anchors: who / what / how-much / when.** Every anchor is a fact lifted from
       a stored body, and every number, name, and date matches the source exactly.
2. [ ] **The convergence fact:** "Covered independently by N newsletters this fortnight" (the Stage-2 count).
       This is the importance statement, stated as a fact about coverage, not an opinion.
3. [ ] **The proprietary DB overlay (a fact, not a take).** Where the deal/company sits in the InvestGame
       record: the recorded deal value, its rank or precedent context, the multiple, the ownership history.
       Pull it from `InvestGame_query` / `InvestGame_market_query`. Present it as InvestGame data, linked to
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

## Stage 4 - The three desks (transactions are DB-authoritative)

**Goal:** the deal and public-market sections, sourced from the authoritative InvestGame datasets, not the
press. The press only overlays attributed commentary.

### Deals desk (via `InvestGame_query`)
- [ ] Pull **M&A and fundraising deals in the window** from `InvestGame_query` (the deal database is the
      authoritative record, ~95% coverage of gaming M&A / funding / IPO). Date by **effective date**
      (the close date, or the announcement date when not yet closed), matching the InvestGame quarterly
      convention.
- [ ] Default deal-list columns (mirror the app): target, country, deal type, size USD, date, lead investor;
      add EV and EV/Revenue for M&A. Numbers right-aligned, USD millions, undisclosed flagged not invented.
- [ ] **Optional Content / Ecosystem split** via the InvestGame sector tags when the period has enough
      volume to warrant two sub-tables. Otherwise one ranked table.
- [ ] **Press deal-commentary overlays, it does not replace.** If a `transactions`-tagged press cluster
      discusses a desk deal, attach it as attributed commentary on the DB row. The figures are the DB's;
      the colour is the newsletter's, attributed.
- [ ] Link every deal row to its **InvestGame deal page**. Append a one-line methodology note (period basis,
      what is included/excluded).
- [ ] Reach for the `ten-shots` query patterns to frame these pulls (notable acquisitions, most-active
      acquirers, precedent multiples) rather than building a query from scratch.

### Public-Markets desk (via `InvestGame_market_query`)
Three parts, all from `InvestGame_market_query` (live InvestGame market data):
- [ ] **Movers:** the period's top share-price gainers and decliners among tracked public gaming companies,
      **bucketed by the curated content segments plus AdTech.** Use the segments the tool returns from the
      curated MarketIndex buckets (PC/console, mobile, diversified large-cap, ecosystem, casino & toys, and
      AdTech as its own bucket). **Do not invent buckets**: use what the data carries. Positive moves in
      brand teal, never green; caution in rust, used sparingly.
- [ ] **Earnings:** the latest earnings releases in the window, each with **EPS surprise (actual vs
      estimate), revenue, and the market reaction** (the post-print price move). Facts only; a source's
      earnings-call read may be quoted with attribution.
- [ ] **Public offerings / IPOs / listings:** any public offering, IPO, or new listing in the window lives
      **here**, in the Public-Markets desk (not in the editorial sweep).
- [ ] Present every public figure as **InvestGame market data**; never name or speculate about where it
      comes from. It supplements the proprietary deal record, it never overrides it: a live market cap and a
      historical deal EV measure different things, so say which is which when they appear to differ.

---

## Stage 5 - Scan register (breadth)

**Goal:** guarantee nothing is missed, via the by-nature facets and the link-only long tail.

### Coverage Sweep (the 5 editorial facets)
Organize the mid-tail (everything not a Big Story or a desk row) into the **five by-nature facets** the
classifier tags posts with. Each facet is a short, sourced list (one line per item, source-linked):

| Facet (`PressTopic`) | What lands here |
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
the stored sources and strips anything that fails. This is a hard requirement and the reason the old
digest's failures (below) can never recur. Run it as a distinct pass, ideally with a second adversarial
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
- [ ] **(e) No machine artifacts or duplicates.** Scan for and remove the exact failure modes the OLD
      InvestGame digest shipped to real recipients:
      - a **leaked JSON envelope** or raw tool output pasted into prose;
      - a **"corrupted item" / placeholder** (e.g. "the fifth news item was corrupted");
      - a **duplicated story** (the old digest shipped the same Switch 2 story twice);
      - a **headline repeated verbatim as the first bullet**;
      - any **unattributed projection** presented as fact.

**Drop log.** Keep a short list of what was dropped or corrected and why (failed which check). It is not
rendered into the digest, but it is the proof the review actually ran. Never ship a claim that failed any
check; fix it against the source or remove it.

---

## Stage 7 - Render to Warm-White HTML (PDF-portable)

**Goal:** produce the branded, click-through, print-clean digest. The HTML standard is already codified in
the `assets/templates/digest.html` fork of the brand-kit Warm-White template: this stage fills a **content
contract**, it does not write CSS.

- [ ] Use the **Warm-White** theme (bg `#F4F3EE`; Space Grotesk display / Inter body / JetBrains Mono
      numbers). Positive movement in **brand teal `#00928A`, never green**; caution in **rust `#C07B5A`**,
      sparingly. The InvestGame **navy** logo (`ig-logo-navy.png`), never the white-wordmark file that
      vanishes on the warm background.
- [ ] **Clickable TOC** on the cover/brief, wired to the section anchors (the hash engine already supports
      it; this is markup only).
- [ ] **Per-claim click-through:** every fact links to its source, press post or InvestGame entity page.
      Every deal row links to its InvestGame deal page; every public name to its profile.
- [ ] **Embedded charts/images** for chart-heavy stories, served from the mirrored image URLs so they render
      even when the source is paywalled client-side. Keep the brand-kit's resize-before-print chart handler
      so charts do not export blank to PDF.
- [ ] **Computed counts only** in the Cover and Exec Brief (posts, sources, deals, movers): the real Stage-1
      numbers, never padded or rounded for effect.
- [ ] **Methodology & Sources** at the end: window, source count, post count, the convergence method, the
      factual-only posture, and the full source roster with links.
- [ ] Render to PDF via the explicit Playwright path (fixed page size, zero margin) so the on-screen HTML and
      the PDF match. Hand presentation specifics to `investgame-format`; this playbook owns the content, that
      skill owns the brand render.

---

## What this playbook is NOT (guards)

- **Not an opinion column.** No InvestGame predictions, recommendations, or "why it matters" takes. Only
  consolidated facts, convergence, DB overlay, and attributed source analysis.
- **Not an entity tracker.** Cluster by **story and convergence**, never by named entity (the old system's
  failure).
- **Not a press-sourced deal sheet.** Deal and market figures come from the **authoritative InvestGame
  datasets**; the press only overlays attributed commentary.
- **Not a teaser digest.** Synthesize from the **full stored bodies**, never from the 140-char feed excerpts.
- **Not auto-shipped.** Nothing renders until the Stage-6 deep-dive review has passed on every claim and the
  drop log exists.
- **Not a machine dump.** No leaked JSON, no placeholders, no duplicates, no headline-as-first-bullet: the
  exact artifacts the deep-dive review is built to catch.

## Quick build checklist (one pass, top to bottom)

1. [ ] Retrieve the 14-day window, full bodies, with topics/source/date/paywall; down-weight podcasts;
       record computed counts.
2. [ ] Cluster by story; count independent newsletters; rank; do not over-collapse.
3. [ ] Synthesize 3-6 Big Stories: who/what/how-much/when + convergence + DB overlay + attributed analysis;
       source-link every claim; no created "why it matters".
4. [ ] Build the Deals desk (`InvestGame_query`, DB-authoritative) and the Public-Markets desk
       (`InvestGame_market_query`: movers by segment + AdTech, earnings, public offerings).
5. [ ] Fill the Coverage Sweep (5 facets) and the link-only Wire; optional Reading List.
6. [ ] Run the deep-dive review on every claim (a-e); fix or drop failures; keep the drop log.
7. [ ] Render to Warm-White `digest.html`: TOC, per-claim links, embedded charts, navy logo, computed
       counts, methodology; export to PDF.
