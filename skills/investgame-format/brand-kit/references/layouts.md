# Layouts

Slide anatomy and copy-pasteable markup for both skins. Pick a skin first (see SKILL.md), copy its template, then edit the structures below in place. The class names here are the **real** ones from the templates and source decks - keep them.

All example copy and figures below are **generic placeholders** - replace `[bracketed text]`, `Company A`, `$XXX`, `NN%` etc. with your own. Never carry placeholder numbers into a finished deck.

## Contents

- [The one-visual rule](#the-one-visual-rule)
- [Where the visual internals live](#where-the-visual-internals-live)
- [Dark Navy skin](#dark-navy-skin)
  - [Canvas, safe-zone, chrome](#feature--canvas-safe-zone-chrome)
  - [Cover](#feature--cover)
  - [Content + KPI row](#feature--content--kpi-row)
  - [Content + bar chart](#feature--content--bar-chart)
  - [Data table](#feature--data-table)
  - [Two-column / timeline](#feature--two-column--timeline)
  - [Closing](#feature--closing)
- [Warm White skin](#warm-white-skin)
  - [Canvas, safe-zone, chrome](#report--canvas-safe-zone-chrome)
  - [Cover](#report--cover)
  - [Content slide anatomy](#report--content-slide-anatomy)
  - [KPI row](#report--kpi-row)
  - [Matrix table](#report--matrix-table)
  - [Chart + side-callout](#report--chart--side-callout)
  - [Glossary](#report--glossary)
  - [Sources](#report--sources)
- [HTML reports read on screen (not slides)](#html-reports-read-on-screen-not-slides)

---

## The one-visual rule

A content slide carries **one** primary visual: a KPI row **OR** a table **OR** a chart - never two or three competing for the eye.

**Why:** the title states the takeaway, and a single visual proves it. Put a KPI row next to a table next to a chart and the reader doesn't know where to look, so the takeaway lands nowhere. Bullets and a conclusion line can sit alongside the one visual because they read as supporting text, not as a second focal point. If you have two visuals worth showing, that's two slides.

---

## Where the visual internals live

This file covers slide skeletons and where each block sits. For the internals of the visuals themselves:

- Chart construction, Chart.js config, palette order, the `resize()` gotcha → `references/charts.md`.
- Table row styling and KPI tile variants in depth → `references/tables-and-kpis.md`.
- Colour tokens by name → `references/colors.md`. Font roles and sizes → `references/typography.md`.

---

## Dark Navy skin

Dark-navy, editorial. Template: `assets/templates/dark-navy.html`.

### Dark Navy - canvas, safe-zone, chrome

- **Canvas:** `1456 × 820 px`, set in `@page { size: 1456px 820px; margin: 0; }`. Each slide is `<section class="page ...">`.
- **Page padding (safe-zone):** `36px 56px`. Body content lives inside this; `.page-light` (white bg) and `.page-dark` (navy bg) both apply it. The cover overrides padding with its own grid columns.
- **Header chrome** - top of every content page, a `.header-row`:

```html
<div class="header-row">
  <span class="feature-chip">02</span>
  <span class="feature-title">[Section label · period]</span>
</div>
```

The `.feature-chip` is a deep-teal page tag (or `.feature-chip.wide` for a kicker on the cover); `.feature-title` is the small uppercase section label. On dark pages use `<div class="header-row dark">`.

- **Footer chrome** - absolutely positioned `left:56px; right:56px; bottom:24px`:

```html
<div class="footer">
  <div>Source: [provenance line - see content-and-qa.md]</div>
  <div class="page-num">02 / 07</div>
</div>
```

The white logo goes here at 18–24px (see `references/logos.md`); on dark pages use `<div class="footer dark">`. Source line left, `.page-num` right.

Below the header, content pages open with `<h2 class="page-title">` (the insight) and `<p class="page-deck">` (the so-what), then the one visual.

### Dark Navy - cover

Two-column grid `1.05fr / 0.95fr`: dark text column left, decorative panel right.

```html
<section class="page cover">
  <div class="cover-left">
    <div>
      <div class="header-row dark">
        <span class="feature-chip wide">[KICKER · CHIP TEXT]</span>
        <span class="feature-title" style="color:#fff;">[Kicker · date]</span>
      </div>
      <h1 class="cover-headline">[Headline with an <span class="accent">accent phrase</span>]</h1>
      <p class="cover-sub">[One-line subtitle.]</p>
    </div>
    <div class="cover-bottom">
      <img src="../logos/ig-logotype-white.png" alt="InvestGame"/>
      <span class="divider"></span>
      <div>
        <div class="cover-prep">Prepared for</div>
        <div style="font-size:18px;font-weight:700;margin-top:4px;color:#fff;">[Recipient]</div>
      </div>
    </div>
  </div>
  <div class="cover-right"><!-- decorative grid via CSS, no content --></div>
</section>
```

The `.cover-right` panel is pure CSS (perspective grid + radial glows) - leave it empty. The white logotype sits ~38px tall, bottom-left.

### Dark Navy - content + KPI row

Four tiles across, each colour-keyed by variant:

```html
<div class="kpi-row">
  <div class="kpi"><div class="label">[LABEL]</div><div class="big">$XXX</div><div class="small">[note]</div></div>
  <div class="kpi alt"><div class="label">[LABEL]</div><div class="big">NN</div><div class="small">[note]</div></div>
  <div class="kpi alt2"><div class="label">[LABEL]</div><div class="big">$X.XB</div><div class="small">[note]</div></div>
  <div class="kpi alt3"><div class="label">[LABEL]</div><div class="big">NN%</div><div class="small">[note]</div></div>
</div>
```

`.kpi` carries a teal top-border; `.alt` blue, `.alt2` deep-teal, `.alt3` deep-blue - the palette order. Use 2–4 tiles. Details in `references/tables-and-kpis.md`.

### Dark Navy - content + bar chart

A bordered card with a navy header bar and CSS bar columns. Each column is a stacked `.bar-stack` of `.bar-seg`s; bar height is set inline in px against a fixed pixel max.

```html
<div class="chart-card">
  <h3>[Chart title - what, unit]</h3>
  <div class="bars-wrap">
    <div class="bars">
      <div class="bar-col">
        <div class="bar-total">$XXXm</div>
        <div class="bar-stack" style="height:162px;">
          <div class="bar-seg c" style="height:126px;"></div>
          <div class="bar-seg d" style="height:28px;"></div>
          <div class="bar-seg o" style="height:8px;"></div>
        </div>
      </div>
      <!-- repeat .bar-col per category -->
    </div>
    <div class="bar-labels"><span>20XX</span><!-- one per column --></div>
  </div>
  <div class="legend">
    <span><span class="sw" style="background:var(--teal);"></span>[Series 1]</span>
    <span><span class="sw" style="background:var(--blue);"></span>[Series 2]</span>
    <span><span class="sw" style="background:var(--slate);"></span>[Series 3]</span>
  </div>
</div>
```

Segment classes map to the palette: `.c` teal (primary series), `.d` blue, `.o` slate. Pick one chart per slide; Chart.js is the alternative - see `references/charts.md`.

### Dark Navy - data table

Full-width `table.data`: navy uppercase `thead`, hairline row borders, one `tr.highlight` row (teal tint + teal-deep left border) for the takeaway line.

```html
<table class="data">
  <thead>
    <tr><th class="rank">#</th><th>Date</th><th>Company</th><th>Stage</th><th>Raised</th><th>Notable investors</th></tr>
  </thead>
  <tbody>
    <tr class="highlight">
      <td class="rank">1</td><td>20XX</td><td>Company A</td><td>Series B</td>
      <td class="raised">$XXXM</td><td class="wrap">[Lead · participants]</td>
    </tr>
    <tr><td class="rank">2</td><td>20XX</td><td>Company B</td><td>Seed</td><td class="raised">$XXM</td><td>[investors]</td></tr>
    <!-- more rows -->
  </tbody>
</table>
```

`.raised` right-emphasises the money column; `.wrap` lets a long cell wrap. Highlight exactly one row. For the investor-ranking variant add `class="data vc"` and use `.pos` instead of `.rank`. Full table styling in `references/tables-and-kpis.md`.

### Dark Navy - two-column / timeline

Two patterns share this slot.

**Timeline** - four steps on a gradient rail; mark the final/peak step with `.peak`:

```html
<div class="timeline">
  <div class="tl-step">
    <div class="tl-dot"></div>
    <div class="date">[Date]</div>
    <div class="stage">[Stage]</div>
    <div class="amount">$XXM</div>
    <div class="val">[valuation / leads]</div>
    <div class="leads">[short note]</div>
  </div>
  <!-- tl-step ×3; last one class="tl-step peak" -->
</div>
<div class="stats-foot">
  <div class="stat-card"><div class="h">[LABEL]</div><div class="v">$XXXM+</div><div class="d">[note]</div></div>
  <div class="stat-card alt">…</div>
  <div class="stat-card alt2">…</div>
</div>
```

`.stat-card` is a teal left-border callout (`.alt` blue, `.alt2` deep-teal).

**Two-column / universe** - a `260px / 1fr` (or `1fr / 1fr` via `.two-col`) split: a summary `.total-block` on the left, segmented `.seg` rows or `.stat-card`s on the right. Use `.two-col` for this-vs-that or chart-plus-callout pairings.

### Dark Navy - closing

Dark page (`.page-dark`): a `1.05fr / 0.95fr` `.close-grid` - takeaway points left in `ul.points`, a branded `.ig-card` right (white logotype + KPI tiles + CTA). End with the dark footer carrying the white logo inline at 18px.

---

## Warm White skin

Warm off-white, scholarly, paginated. Template: `assets/templates/warm-white.html`. Chart-heavy; uses Chart.js throughout.

### Warm White - canvas, safe-zone, chrome

- **Canvas:** `1280 × 720 px`. Each slide is `<section class="slide" data-id="N">`; only `.slide.active` is shown (JS paginates).
- **Scaling wrapper:** `#stage` (fixed full-viewport flex centerer) holds `#stage-inner` (the 1280×720 board). A `fit()` function scales `#stage-inner` to the window; in print/PDF mode this is bypassed and slides stack. Don't remove these - they're how the deck both presents and prints to exact size.
- **Page padding (safe-zone):** `30px 56px 44px` (extra bottom room for footnotes).
- **Header chrome** - `.slide-meta`: page number left, section label right, on a hairline bottom border:

```html
<div class="slide-meta">
  <span>02 / 15</span>
  <span class="section-label">Part 1<span class="sep">·</span>[Section]</span>
</div>
```

- **Footer chrome** - `.footnotes`, absolutely positioned `left:60px; right:60px; bottom:18px`; each footnote is a `<span>` with a teal `.fn-mark`, keyed to a `<sup class="fn">N</sup>` in the body:

```html
<div class="footnotes">
  <span><span class="fn-mark">(1)</span>[Provider, report title, date; scope note]</span>
  <span><span class="fn-mark">(2)</span>[Provider, report title, date]</span>
</div>
```

### Warm White - cover

Typographic and image-led. A header band leads with the navy-wordmark InvestGame logo in its top-left meta slot, date on the right; the big title is Space Grotesk; a thin top-bordered line at the bottom carries an italic source note.

```html
<section class="slide active cover-slide" data-id="cover">
  <div style="display:flex; flex-direction:column; height:100%; justify-content:space-between;">
    <div class="slide-meta-cover"><!-- navy-wordmark logo left, date right -->
      <img src="../logos/ig-logo-navy.png" alt="InvestGame" style="height:28px;"><span>[Month 20XX]</span>
    </div>
    <h1 class="font-display" style="font-size:60px;font-weight:700;">[Report title]</h1>
    <div><!-- top-bordered line --><span style="font-style:italic;">[Source basis note]</span></div>
  </div>
</section>
```

See `references/logos.md` for why the cover uses the full-colour logo image.

### Warm White - content slide anatomy

The canonical content slide stacks these blocks, in order:

```text
.slide-meta      → header chrome (page no. + section)
.kicker          → small uppercase eyebrow (optional)
.slide-title     → the insight, one sentence
.slide-conclusion→ the so-what callout (teal-soft, deep-teal left border)
.visual          → the ONE primary visual: KPI row OR table OR chart
.slide-bullets   → supporting points (square teal bullets)
.footnotes       → footer chrome
```

```html
<section class="slide" data-id="1">
  <div class="slide-meta"><span>01 / 15</span><span class="section-label">Part 1<span class="sep">·</span>[Section]</span></div>
  <div class="kicker">[Eyebrow]</div>
  <h1 class="slide-title">[Insight - one-sentence takeaway]</h1>
  <div class="slide-conclusion">[The single most important statement, with the key figure $X.X bn and the range across sources.]</div>
  <div class="visual"><!-- KPI row, table, or chart - see below --></div>
  <ul class="slide-bullets">
    <li>[Supporting point with a <strong>figure</strong>.<sup class="fn">1</sup></li>
  </ul>
  <div class="footnotes"><span><span class="fn-mark">(1)</span>[Source]</span></div>
</section>
```

Density variants `.slide-medium` / `.slide-dense` on the `<section>` shrink type and spacing when a slide runs long - reach for them before deleting content.

### Warm White - KPI row

Three tiles by default (`.kpi-row`, or `.kpi-row.cols-4` for four). Variants colour-key the tile:

```html
<div class="visual">
  <div class="kpi-row">
    <div class="kpi hero"><div class="kpi-label">[Headline metric]<sup class="fn">1</sup></div>
      <div class="kpi-value tabular">~XXX<span class="unit">m</span></div>
      <div class="kpi-note">[basis - average across N sources]</div></div>
    <div class="kpi"><div class="kpi-label">[Metric]<sup class="fn">2</sup></div>
      <div class="kpi-value tabular">$X.X<span class="unit">bn</span></div>
      <div class="kpi-note">[methodology]</div></div>
    <div class="kpi warn"><div class="kpi-label">[Caution metric]<sup class="fn">3</sup></div>
      <div class="kpi-value tabular">X–Y<span class="unit">m</span></div>
      <div class="kpi-note">[InvestGame estimate, basis]</div></div>
  </div>
</div>
```

`.kpi.hero` = teal-soft tile for the headline figure; `.kpi.warn` = rust-soft tile for a risk/caution figure; plain `.kpi` for the rest. Keep numbers in `.tabular`. Details in `references/tables-and-kpis.md`.

### Warm White - matrix table

`table.matrix`: uppercase muted header on a heavy bottom rule, hairline rows, `.num` cells right-aligned in JetBrains Mono, one `tr.hilite` row in teal-soft for the takeaway.

```html
<div class="visual">
  <table class="matrix">
    <thead><tr><th>[Metric]</th><th style="text-align:right">[Period A]</th><th style="text-align:right">[Period B]</th><th>[Note]</th></tr></thead>
    <tbody>
      <tr class="hilite"><td>[Headline row]</td><td class="num">$X.X bn</td><td class="num">~$X.X bn</td><td>[note]</td></tr>
      <tr><td>[Row]</td><td class="num">$X.X bn</td><td class="num">$0</td><td>[note]</td></tr>
    </tbody>
  </table>
</div>
```

Use `table.matrix.dense` when rows are tight. Highlight exactly one row.

### Warm White - chart + side-callout

Two-column inside the slide: a Chart.js canvas on the left (`flex: 4` or similar), a narrow callout box on the right (`flex: 1`) - often a `warn`-toned aside. The chart fills its column; the callout carries the one or two figures the chart can't label.

```html
<div style="display:flex; gap:24px; flex:1; min-height:0; margin-top:16px;">
  <div style="flex:4; position:relative; min-height:0;"><canvas id="chart-[name]"></canvas></div>
  <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
    <div style="background:var(--ig-warn-soft); border-left:4px solid var(--ig-warn); padding:10px 12px; border-radius:4px;">
      <div style="font-size:10px;font-weight:700;color:var(--ig-warn);text-transform:uppercase;">[Aside label]</div>
      <div style="font-size:12.5px;">[Short prose]</div>
    </div>
  </div>
</div>
```

For a chart filling the full body instead, use `<div class="visual"><div class="chart-wrap"><canvas …></canvas><div class="chart-caption">…</div></div></div>`. Every Chart.js canvas on a paginated slide must call `resize()` when its slide becomes active - see `references/charts.md`.

### Warm White - glossary

Two-column grid of teal-left-border cards:

```html
<div class="glossary">
  <div class="glossary-item">
    <div class="glossary-term">[Term]</div>
    <div class="glossary-def">[One-line definition.]</div>
  </div>
  <!-- repeat -->
</div>
```

### Warm White - sources

A numbered `.source-list`; deep-teal `.src-num` indices in JetBrains Mono, links in `accent-deep`. Use `.source-list.cols-2` to split a long list across two columns.

```html
<div class="source-list">
  <div><span class="src-num">[1]</span> [Provider]. "[Report title]" (date). <a href="https://example.com">example.com</a></div>
  <div><span class="src-num">[2]</span> [Provider]. "[Report title]" (date).</div>
</div>
```

Every figure on a content slide should trace to a numbered source here - see `references/content-and-qa.md`.

---

## HTML reports read on screen (not slides)

Everything above sizes a fixed 16:9 canvas for a deck. A **report read in a browser** is a different artifact and takes these three rules instead.

- **Full width.** Fill a wide screen. Use a container of `min(1520px, 94vw)`, not a narrow centred ~900px column, and then actually use the width: multi-column card grids for list items, full-width tables and charts. Keep prose readable inside the wide frame with columns or a capped measure, but the page must not look cramped on a large monitor.
- **Warm background, not white.** A plain white or near-white page is wrong. Use a warm cream or sand tone, warmer than the deck background `#F4F3EE`, with cards in a lighter warm ivory (never stark white), navy text, and brand-teal accents.
- **Logo.** A navy header band with the white-wordmark logo is the preferred report header. Everywhere else on the page, including the footer, use `ig-logo-navy.png` directly on the warm background. See `references/logos.md`.
