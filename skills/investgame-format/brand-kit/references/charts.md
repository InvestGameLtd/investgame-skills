# Charts

How to pick a chart type and render it on-brand in either skin. Pull this file only when you are actually building or editing a chart.

## Contents

Default to bar/column · Chart type → data shape · Palette & the two delta colours · Warm White Chart.js recipe · the chart.resize() rule · Dark Navy CSS/HTML bars · PowerPoint charts

- [Default to bar/column](#default-to-barcolumn)
- [Chart type → data shape](#chart-type--data-shape)
- [Palette and the two delta colours](#palette-and-the-two-delta-colours)
- [Warm White skin - Chart.js recipe](#warm-white-skin--chartjs-recipe)
- [The chart.resize() rule](#the-chartresize-rule)
- [Dark Navy skin - no-JS CSS/HTML bars](#dark-navy-skin--no-js-csshtml-bars)
- [PowerPoint charts](#powerpoint-charts)

---

## Default to bar/column

Reach for a bar or column chart first, and only switch when the data clearly calls for something else. Bars are the most legible encoding for the work InvestGame ships - readers compare lengths along a shared baseline far more reliably than they judge angles, areas, or slopes - and a clean column chart is the most on-brand look in either skin. A slide that paginates well and reads in two seconds beats a clever encoding that needs a caption to decode. When in doubt, bar it.

---

## Chart type → data shape

| The data is… | Use | Notes |
|---|---|---|
| A trend over time | **Column** (one bar per period) | Add a delta or CAGR callout - the chart shows the shape, the callout states the so-what. |
| Share of a single total | **Doughnut** | Preferred over pie: the centre hole carries the total or headline figure, and the thinner ring makes small slices easier to read. Keep to ≤5 slices; beyond that switch to a ranked bar. |
| Comparison across categories | **Horizontal or vertical bar** | Horizontal when labels are long or there are many categories; vertical for a handful of short labels. Sort by value unless a natural order (time, size tier) applies. |
| A range or valuation spread | **Range bars** (floating bars min→max) | One bar per item spanning low to high; mark the midpoint. Reads as "where the number could land", not a single point. |
| Cumulative flow or cohorts | **Stacked area** | Bands sum to the total over time. Order bands largest-at-bottom; cap at ~4 bands before it turns to mud. |
| Two metrics that may correlate | **Scatter** | Teal points (`#61BFB3`); one variable per axis. Add a light trend line only if the relationship is the point. |

---

## Palette and the two delta colours

Apply chart series in this fixed order so two charts never disagree on which segment is which:

| # | Name | Hex |
|---|------|-----|
| 1 | Teal | `#61BFB3` |
| 2 | Blue | `#6189D6` |
| 3 | Teal-deep | `#00928A` |
| 4 | Blue-deep | `#2D5BA8` |
| 5 | Slate | `#8A95A4` |
| 6 | Teal-bright | `#1ECABA` |
| 7 | Gray | `#8FA1B5` |

This is `IG.chartColors` in `assets/ig_helpers.js` and `CHART_COLORS` in `assets/ig_helpers.py`. Take colours from the array in order - do not hand-pick.

Two semantic colours sit outside the series order:

- **Positive delta / "up" → teal-deep `#00928A`.** Never green - green reads as generic finance-dashboard noise and dilutes the brand teal.
- **Negative / caution / "down" / banned → rust `#C07B5A`, used sparingly.** InvestGame charts are not red-and-green dashboards; rust is an occasional flag, not a second primary.

---

## Warm White skin - Chart.js recipe

Copy-pasteable single-series bar. Loads `igChartDefaults()` from `assets/ig_helpers.js` (sets the Inter font, muted axis labels, no tick marks, no axis border), applies the palette, turns datalabels on for the one series, draws gridlines on the value axis only, and hides the legend because a single series needs no key.

```html
<canvas id="chart-share"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.min.js"></script>
<script src="../assets/ig_helpers.js"></script>
<script>
  Chart.register(ChartDataLabels);
  Chart.defaults.set('plugins.datalabels', { display: false }); // default OFF, enable per-dataset
  const { muted, grid } = igChartDefaults(Chart); // Warm White defaults; pass { dark: true } for Dark Navy

  new Chart(document.getElementById('chart-share'), {
    type: 'bar',
    data: {
      labels: ['[Cat A]', '[Cat B]', '[Cat C]', '[Cat D]'],
      datasets: [{
        data: [42, 31, 18, 9],
        backgroundColor: IG.chartColors[0],   // teal - series 1; add more series in array order
        borderWidth: 0,
        barPercentage: 0.7,
        categoryPercentage: 0.7,
        datalabels: {
          display: true, anchor: 'end', align: 'top', offset: 2,
          color: IG.report.text, font: { size: 11, weight: 700 },
          formatter: v => v + '%'
        }
      }]
    },
    options: {
      maintainAspectRatio: false, responsive: true,
      scales: {
        x: { grid: { display: false }, ticks: { color: muted } },          // no gridlines on category axis
        y: { beginAtZero: true, grid: { color: grid }, ticks: { color: muted, callback: v => v + '%' } } // subtle value-axis gridlines only
      },
      plugins: { legend: { display: false } }                              // single series → no legend
    }
  });
</script>
```

To add series, append objects to `datasets` and take their `backgroundColor` from `IG.chartColors[1]`, `[2]`, … in order; with more than one series, set `plugins.legend` to `{ position: 'bottom', align: 'start' }` instead of hiding it. For a positive/negative bar, colour the values with `IG.positive` and `IG.negative`. The Dark Navy skin uses the same recipe with `igChartDefaults(Chart, { dark: true })` for light labels on navy.

---

## The chart.resize() rule

**Any Chart.js chart on a slide that is shown/hidden must call `chart.resize()` the moment its slide becomes visible.** The Warm White template paginates by toggling `.slide.active` (display none → flex), so a chart created while its slide is hidden measures a **0px container** and paints blank or as a one-pixel sliver on first view - and never recovers on its own. Resizing on show forces Chart.js to re-measure the now-visible container and lay the chart out correctly.

The template's pagination already does this - keep it intact when you add slides:

```javascript
function show(i) {
  slides.forEach((s, k) => s.classList.toggle('active', k === i));
  const s = slides[i];
  // CRITICAL: resize every chart on the shown slide so it does not paint at 0px width.
  if (s && typeof Chart !== 'undefined' && Chart.getChart) {
    s.querySelectorAll('canvas').forEach(c => {
      const inst = Chart.getChart(c);
      if (inst) inst.resize();
    });
  }
}
```

If you build pagination from scratch, replicate this - every show handler iterates the slide's canvases and calls `resize()`. Symptom that you forgot: charts on the first slide look fine, charts on every later slide render blank or tiny until you nudge the window.

---

## Dark Navy skin - no-JS CSS/HTML bars

The Dark Navy deck draws bars in pure CSS - no Chart.js, no canvas, nothing to resize, and it prints to PDF identically every time. A `.chart-card` (white panel, hairline border, navy header bar) holds a `.bars` grid; each `.bar-col` stacks a `.bar-total` over a `.bar-stack` whose `.bar-seg` segments are sized in pixels. The three stack classes map to the series palette:

- `.bar-seg.c` → teal `#61BFB3` (series 1)
- `.bar-seg.d` → blue `#6189D6` (series 2)
- `.bar-seg.o` → slate `#8A95A4` (series 3)

To scale: pick the largest total, give its `.bar-stack` ~220px, then size every other stack and its segments proportionally in px.

```html
<div class="chart-card" style="max-width:980px;">
  <h3>[Chart title · units, e.g. annual value by segment ($M)]</h3>
  <div class="bars-wrap">
    <div class="bars">
      <div class="bar-col">
        <div class="bar-total">$XXm</div>
        <div class="bar-stack" style="height:70px;">
          <div class="bar-seg o" style="height:12px;"></div>
          <div class="bar-seg d" style="height:18px;"></div>
          <div class="bar-seg c" style="height:40px;"></div>
        </div>
      </div>
      <div class="bar-col">
        <div class="bar-total" style="color:var(--teal-dark);">$XXXm*</div>
        <div class="bar-stack" style="height:220px;">
          <div class="bar-seg o" style="height:60px;"></div>
          <div class="bar-seg d" style="height:18px;"></div>
          <div class="bar-seg c" style="height:142px;"></div>
        </div>
      </div>
    </div>
    <div class="bar-labels"><span>20XX</span><span>20XX YTD*</span></div>
  </div>
  <div class="legend">
    <span><span class="sw" style="background:var(--teal);"></span>Segment One</span>
    <span><span class="sw" style="background:var(--blue);"></span>Segment Two</span>
    <span><span class="sw" style="background:var(--slate);"></span>Segment Three</span>
  </div>
</div>
```

Use this for the Dark Navy skin; reach for Chart.js there only when you genuinely need an axis, many points, or a doughnut.

---

## PowerPoint charts

PowerPoint will not pick on-brand colours - beyond the first few series it auto-assigns its own off-brand defaults - so set every series colour by hand from `CHART_COLORS` in `assets/ig_helpers.py` (hex stored **without** the leading `#`). Walk the array in order, exactly as in HTML. Prefer a doughnut over a pie for the same legibility reasons as on the web. Use `POSITIVE` (`00928A`) and `NEGATIVE` (`C07B5A`) for delta bars; never green, never a red/green dashboard. Full PowerPoint chart wiring, `hex_to_rgbcolor()` usage, and slide sizing are in **references/pptx-and-pdf.md**.
