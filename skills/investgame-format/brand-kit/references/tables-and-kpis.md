# Tables & KPI tiles

Table and KPI-tile styles and markup for both skins. Pull this file only when you are building or editing a table or a KPI row.

## Contents

Table vs KPI row vs chart · Dark Navy table (table.data) · Warm White table (table.matrix) · Dark Navy KPI tiles · Warm White KPI tiles · Numbers

- [Table vs KPI row vs chart](#table-vs-kpi-row-vs-chart)
- [Dark Navy table - table.data](#dark-navy-table--tabledata)
- [Warm White table - table.matrix](#warm-white-table--tablematrix)
- [Dark Navy KPI tiles - .kpi](#dark-navy-kpi-tiles--kpi)
- [Warm White KPI tiles - .kpi](#warm-white-kpi-tiles--kpi)
- [Numbers](#numbers)

---

## Table vs KPI row vs chart

One-line guide:

- **KPI row** - 2–4 headline figures the reader should remember; no comparison across many rows.
- **Table** - exact values that need to be read, ranked, or looked up row by row.
- **Chart** - the *shape* of the data (trend, share, spread) matters more than the exact figures.

A slide carries **one** primary visual - a KPI row OR a table OR a chart, never several competing for the eye. See **references/layouts.md**.

---

## Dark Navy table - table.data

Navy uppercase header, hairline `#E1E6EC` row borders, one `tr.highlight` row that carries the takeaway (teal-deep left-border + `#E1F4F1` tint), a muted `.rank` column, and right-aligned numbers. Highlight exactly one row - the one the lead-in paragraph flags.

```html
<table class="data">
  <thead>
    <tr>
      <th class="rank">#</th>
      <th>Date</th>
      <th>Company</th>
      <th>Stage</th>
      <th>Raised</th>
      <th>Lead / notable investors</th>
    </tr>
  </thead>
  <tbody>
    <tr class="highlight">
      <td class="rank">1</td>
      <td>MMM 20XX</td>
      <td>Company A</td>
      <td>Stage</td>
      <td class="raised">$XXXm</td>
      <td class="wrap" style="font-size:11px;line-height:1.35;">[Lead investor] · [participant] · [participant]</td>
    </tr>
    <tr><td class="rank">2</td><td>MMM 20XX</td><td>Company B</td><td>Stage</td><td class="raised">$XXXm</td><td>[Lead investor] · [participant]</td></tr>
    <tr><td class="rank">3</td><td>MMM 20XX</td><td>Company C</td><td>Stage</td><td class="raised">$XXm</td><td>[Lead investor] · [participant]</td></tr>
  </tbody>
</table>
```

The `.highlight` styling (tint bg, teal-deep left-border on the first cell, navy bold text) and the muted `.rank` width are defined in `dark-navy.html` - keep the class names and they apply automatically. Put numbers in `td.raised` so they stay right-aligned and bold.

---

## Warm White table - table.matrix

Uppercase muted `th` over a 1.5px bottom border, hairline `#E0DFD9` rows, and `td.num` cells right-aligned in JetBrains Mono with `tabular-nums`. One `tr.hilite` carries the row worth flagging on the teal `accent-soft` (`#E6F4F2`) tint. Add `.dense` to the table for many rows.

```html
<table class="matrix">
  <thead>
    <tr>
      <th>Market</th>
      <th class="num">Value ($bn)</th>
      <th class="num">YoY</th>
      <th class="num">Share</th>
    </tr>
  </thead>
  <tbody>
    <tr class="hilite">
      <td>[Region A]</td>
      <td class="num">12.4</td>
      <td class="num">+8.1%</td>
      <td class="num">34%</td>
    </tr>
    <tr><td>[Region B]</td><td class="num">9.7</td><td class="num">+3.2%</td><td class="num">27%</td></tr>
    <tr><td>[Region C]</td><td class="num">5.1</td><td class="num">-1.4%</td><td class="num">14%</td></tr>
  </tbody>
</table>
```

Every numeric column gets `class="num"` on both the `th` and the `td` so the header label and the figures share the right edge. The mono + tabular figures keep digits in vertical columns down the page.

---

## Dark Navy KPI tiles - .kpi

Tiles in a `.kpi-row` (2–4 columns). Each `.kpi` has a coloured top-border - default teal, with `.alt` (blue), `.alt2` (teal-deep), `.alt3` (blue-deep) to vary across the row in palette order. Inside: an 11px uppercase `.label`, a 40px `.big` value, and a 12px `.small` note.

```html
<div class="kpi-row">
  <div class="kpi">
    <div class="label">[Metric one]</div>
    <div class="big">$XXm</div>
    <div class="small">[supporting note]</div>
  </div>
  <div class="kpi alt">
    <div class="label">[Metric two]</div>
    <div class="big">XX%</div>
    <div class="small">[supporting note]</div>
  </div>
  <div class="kpi alt2">
    <div class="label">[Metric three]</div>
    <div class="big">XX</div>
    <div class="small">[supporting note]</div>
  </div>
  <div class="kpi alt3">
    <div class="label">[Metric four]</div>
    <div class="big">$X.Xbn</div>
    <div class="small">[supporting note]</div>
  </div>
</div>
```

Vary the border colour across the row for rhythm; do not give every tile the same accent unless the row is two tiles.

---

## Warm White KPI tiles - .kpi

Tiles in a `.kpi-row` (add `.cols-4` for four). Default tiles are a hairline-bordered white card. Two semantic variants:

- `.kpi.hero` - teal border + `accent-soft` (`#E6F4F2`) bg for the **headline** metric (one per row).
- `.kpi.warn` - rust border + `warn-soft` (`#F5E6DD`) bg for a **risk / caution** metric.

Inside: `kpi-label` (uppercase, muted), `kpi-value` (large; wrap the unit in `.unit` so it sits small beside the figure), and `kpi-note`.

```html
<div class="kpi-row cols-4">
  <div class="kpi hero">
    <div class="kpi-label">[Headline metric]<sup class="fn">1</sup></div>
    <div class="kpi-value tabular">~XXX<span class="unit">m</span></div>
    <div class="kpi-note">[note - average across N sources; forecast ~YYY m by 20XX]</div>
  </div>
  <div class="kpi">
    <div class="kpi-label">[Metric two]<sup class="fn">2</sup></div>
    <div class="kpi-value tabular">$X.X<span class="unit">bn</span></div>
    <div class="kpi-note">[note - methodology and split]</div>
  </div>
  <div class="kpi">
    <div class="kpi-label">[Metric three]<sup class="fn">2</sup></div>
    <div class="kpi-value tabular">XX<span class="unit">%</span></div>
    <div class="kpi-note">[note]</div>
  </div>
  <div class="kpi warn">
    <div class="kpi-label">[Risk metric]<sup class="fn">3</sup></div>
    <div class="kpi-value tabular">X–Y<span class="unit">m</span></div>
    <div class="kpi-note">[note - InvestGame estimate, basis of calculation]</div>
  </div>
</div>
```

Use `hero` for the one number the slide is about and `warn` for at most one caution metric - both lose their punch if repeated.

---

## Numbers

Right-align numeric columns, set tabular figures, and keep decimal places consistent down a column. In the Warm White skin `td.num` already applies JetBrains Mono + `font-variant-numeric: tabular-nums`; in the Dark Navy skin keep numbers in the right-aligned cells (`td.raised`, `.big`). Put the unit small next to a large value (`<span class="unit">bn</span>`) so the figure leads and the unit does not compete.

Why it matters: right-aligning lines up the ones, tens, and hundreds in a single vertical column, so the reader compares magnitudes by eye without re-reading each cell. Tabular (monospaced) figures give every digit the same width, so `1,111` and `8,888` occupy identical space and rows stay aligned - proportional digits make columns ragged and slow to scan. Consistent decimals stop `1.2` and `1.20` reading as different precision.
