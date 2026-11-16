---
name: investgame-format
version: 0.10.16
description: >
  Present InvestGame answers well: tables, charts, comp sets and ranked lists in chat, and branded files
  (HTML, PDF, PowerPoint, Excel) built from the bundled InvestGame brand kit. Use when an answer is
  shown as a table, chart, comparison or list of deals or companies, or the user asks to "make a deck",
  "build a PDF", "export to PowerPoint", "an Excel of this", "a one-pager", "a branded report", "show
  this as a chart", "make it presentable" or "put our brand on it". It decides how to show a result;
  what is worth showing is investgame-analysis's call, and a full report or deep dive is
  investgame-research, which calls this skill to render. Not for a one-line fact, game design or generic
  software questions.
---

# InvestGame Format

The presentation layer for InvestGame answers shown as a table, chart, comparison or list, not only when
someone asks for a file. Whenever you show data that way, think about how to present it so the reader gets the insight at a glance. Two jobs:
advise on the right way to present, and render it on-brand when a real deliverable is asked for. Pure
InvestGame brand - never another house brand, never internal authorship.

## Job 1 - match the presentation to the request
First decide how much presentation the request needs. Most answers stay in chat; only some become files.

In chat (the default - no file, no brand kit needed):
- For a normal data answer, present it cleanly with your built-in, in-chat tools - a readable table, or a
  simple chart when the data is visual (a trend, a breakdown, a comp set). You don't need the brand kit or a
  file for this; just make the in-chat output consistent, well-labelled and easy to scan, and apply the
  presentation conventions below (tags, flags, links).
- A quick fact → a sentence. A short comparison → a compact table. A handful of headline metrics → a small
  table or KPI-style lines. A trend or a comp set → an in-chat chart.
- If the surface can't render a chart, degrade to a well-labelled table carrying the same comparison (keep
  the median row, sort by the multiple) - never emit broken chart markup or drop the comparison silently.

A real deliverable (only when the user asks for one - "deck", "report", "PDF", "PowerPoint", "Excel",
"one-pager", "a page", "branded", "on our brand"):
- Build it with the brand kit. Default order: start with an interactive HTML build; produce a PDF from it if
  a fixed document is wanted; produce PowerPoint or Excel only when the client asks for those formats.
- A two-line answer never needs a deck; a board report shouldn't be a wall of text.

If it's genuinely unclear, or both would work, ask once with a concrete suggestion ("just here in chat, or a
branded one-pager?"), then commit. If the user already named a form ("make a deck"), don't re-ask.

## The fence with investgame-analysis (read this)
investgame-analysis decides WHAT is analytically relevant - which metrics and supporting fields answer the
question and help the user decide. Format decides HOW that content is shown - which fields become table
columns, which get demoted to a footnote or small print, their order and grouping, and the best visual
(table / chart / KPI tiles). Format never DROPS an analytically-relevant field to save room: if content
genuinely won't fit, demote or summarise it, or flag that the scope is too wide - cutting a field is
investgame-analysis's call. Quick routing test: if the decision changes WHETHER a field is in the answer,
it's Analysis; if it only changes WHERE or HOW it appears, it's Format.

## Presenting valuations & comp sets (the house pattern)
Multiples and comps have a standard, recognisable look - use it whenever you show a valuation comparison
(the single most common analytical output). Works the same in-chat and as a branded deliverable:
- A column/bar chart, one bar per deal, sorted by the multiple (high to low), each bar labelled with its
  value (e.g. "8.2x").
- A median line across the chart, labelled ("Median 8.2x") - the comp-set reference point.
- Colour the bars by a meaningful category (monetization, platform, or deal type), with a short legend, so
  the pattern is visible at a glance.
- Below the chart, a table of the deals: date · target · acquirer/investor · EV ($M) · the multiple · the
  period (LTM / CY0 / NTM, CY0 with a zero) and metric (EV/Revenue, EV/EBITDA, EV/EBIT or
  EV/Cash EBITDA) · the category as a tag. Label the EV column with its basis when the set mixes
  categories: M&A is Upfront EV, a round is post-money, a listing is market cap.
- A one-line source note ("Source: InvestGame, retrieved <date>") and any caveat (e.g. which metric/period mix was used, per
  the never-break-silently rule in investgame-analysis).
Analysis chooses the comps and the fields; you make them read like a comp set.

## Presentation conventions (in-chat and on-brand)
- Tags for fixed-choice fields. When a field has a defined set of values - monetization, company type,
  sector, genre, platform - show it as a small tag/chip, not raw text. Faster to scan, and it looks
  considered.
- Flags for countries. Show the country flag alongside (or in place of) the ISO code. In branded HTML use
  a flag image (an SVG flag), never a Unicode flag emoji (emoji flags render as bare letters on some
  platforms, e.g. Windows); every template styles a flag image through the `flag` class: `<img class="flag" src="[flag svg]" alt="">`.
  In chat, the built-in rendering is fine.
- Links for entities - link every named deal, company and index to its InvestGame page with the URL
  patterns in the hub's output section (`investgame-gaming-data`, section 4, item 6).
- Numbers right-aligned, USD millions unless stated, consistent decimals; lead the eye to the takeaway.

## Start from a template - don't rebuild (deliverables)
The complete InvestGame brand system ships in brand-kit/. Highest-leverage habit: copy the matching theme
template and replace content in place, keeping the class names - far faster and more on-brand than a blank
file. Bundled:
- brand-kit/assets/templates/warm-white.html and dark-navy.html - canonical starters (canvas, cover, KPI
  tiles, table/chart styling, logo, print-to-PDF CSS all pre-encoded).
- brand-kit/assets/logos/ - the real InvestGame logos · brand-kit/assets/ig_brand.css - colour/type tokens.
- brand-kit/assets/ig_helpers.py - colour/type constants for PowerPoint & Excel · brand-kit/assets/
  ig_helpers.js - colour tokens + Chart.js defaults for HTML.
- brand-kit/scripts/render_pdf.py - headless HTML→PDF at the exact canvas (Playwright on any OS; the
  system-Chrome fallback covers macOS and Linux).
- Exception: a company or fund profile document (one to three pages on one company) is not built
  from the deck templates. Four finished examples sit on the Reports tab of app.investgame.net, shelf
  "MCP & Skills build examples": Company Profile Short, Company Profile Extended (two variants, an
  operator that was acquired and an acquirer with a portfolio), Fund Profile. The MCP has no tool that
  reads that shelf, so ask the user to download the closest sample there (the HTML button) and attach
  it. The comment at the top of the file names the connector call for every field: change only the
  data block marked profile-data, and keep the stylesheet and the renderer exactly as they are.

## Pick the theme (never mix them in one file)
| Theme | Use for | Canvas / fonts |
|-------|---------|----------------|
| Warm White (default) | data-dense reports, comps, market reports, briefings | 1280×720 · Space Grotesk + Inter + JetBrains Mono · bg #F4F3EE |
| Dark Navy | bold/editorial decks, recaps | 1456×820 · Helvetica Neue · bg #0E1F33 |
Offer the choice plainly when someone asks for a deck; for any other deliverable use Warm White unless
they name Dark Navy. Both carry the brand teal and the InvestGame logo.

## Brand constants
- Brand teal #61BFB3 is the InvestGame colour. Positive = teal #00928A, never green. Caution = rust #C07B5A,
  sparingly - InvestGame outputs are not red/green dashboards. Secondary series: blue #6189D6 → deep teal →
  deep blue → slate.
- One idea per slide; the title carries the insight, not the topic. Whitespace over clutter. InvestGame logo
  present; every data slide carries a source line.

## Render playbook
- In chat (default). Use your built-in chart/table rendering and apply the conventions above (tags, flags,
  links, the comp-set pattern). No brand kit, no file.
- HTML interactive (the default for a deliverable). Copy brand-kit/assets/templates/<theme>.html and keep
  its ../logos/ paths working: copy brand-kit/assets/logos/ one level above the page (work/logos/ beside
  work/deck/), or point each logo src and CSS url() at an absolute path or a data: URI. Duplicate a slide
  section per page, replace placeholders in place. Render to PDF with brand-kit/scripts/render_pdf.py -
  it finds a headless browser and honours the template's CSS @page size. The script needs ONE headless
  browser: Playwright's bundled Chromium (pip install playwright && playwright install chromium) or a system
  Chrome/Chromium; if it reports no renderer, install one of those. Don't use a generic HTML→PDF helper that
  forces A4 for slide decks - it squashes the canvas; flowing A4 reports follow
  brand-kit/references/pptx-and-pdf.md. Verify the PDF page size matches the canvas. Warm White loads
  its fonts from Google Fonts, and both templates load Chart.js from cdn.jsdelivr.net; for offline or
  restricted recipients, send the PDF or inline the scripts.
- PowerPoint (.pptx, on request). Set slide size to 13.33 × 7.5 in first; apply brand colours/fonts from
  assets/ig_helpers.py explicitly (never let PowerPoint auto-pick chart colours); one primary visual per
  slide.
- Excel (.xlsx, only when the user explicitly asks for one). Do NOT auto-generate a data-backup Excel
  alongside a chart deliverable: produce a spreadsheet solely on request. When asked: header row navy #0E1F33
  + white bold; thin #CCCCCC borders; right-aligned tabular numbers (USD millions unless stated); a
  source/notes row; freeze the header; charts in the teal palette.
- HTML (interactive). Same tokens; charts via Chart.js (interactive on hover) on Warm White; the Dark
  Navy template draws its default bar chart in CSS and also carries a Chart.js canvas page. See Charts below for the
  resize-before-print gotcha that otherwise exports a blank chart.

## Charts - overview
Default to bar/column unless the data clearly calls for something else - most legible, most on-brand. Build
with Chart.js so charts are interactive on screen; the PDF export stays clean and static (Warm White; the
Dark Navy template draws its default bar chart in CSS and also carries a Chart.js canvas page). Apply series in
palette order (teal → blue → deep teal → deep blue → slate); positive deltas teal, caution rust, never green,
never a red/green dashboard. Gotcha: a chart on a slide that is shown/hidden must call chart.resize() when its
slide becomes visible (and on beforeprint) or it paints at 0px / exports blank - the bundled templates already
handle this. Full chart-type-to-data map, the Chart.js recipe and the PowerPoint chart colour rules in
brand-kit/references/charts.md.

## Tables & KPI tiles - overview
Tables: uppercase header row, hairline row separators, right-aligned tabular numbers, one highlighted row for
the takeaway (a teal left-border in Dark Navy, a teal tint in Warm White); fixed-choice fields as tags,
entities as links. KPI tiles: small uppercase label, large value + small unit, one-line note; in Warm White
a teal "hero" variant for the headline metric and a rust "warn" for a risk metric. Full styles in brand-kit/references/tables-and-kpis.md.

## Content & QA - overview
A branded output still fails if the words and numbers are sloppy. Titles carry the insight, not the topic.
One source of truth per figure. When third-party estimates of the same thing disagree (a market size), cite
each, average across them and show the range, never silently pick one; never average or blend them into an
InvestGame deal figure. Label fiscal
vs calendar years and FX next to converted figures. Acknowledge gaps honestly. Full rules + the pre-export QA
checklist in brand-kit/references/content-and-qa.md.

## References (pull the one the task needs - don't read them up front)
- brand-kit/BRAND.md - the brand on one page: the two themes side by side; read it once before visual work.
- brand-kit/references/colors.md - full palette, decision trees, chart series order.
- brand-kit/references/typography.md - font roles, sizes, weights, PowerPoint fallbacks.
- brand-kit/references/logos.md - placing the logo; clear-space, sizing, on-light/on-dark, don'ts.
- brand-kit/references/layouts.md - building/editing a slide; anatomy + markup per layout, both themes.
- brand-kit/references/charts.md - chart-type map, Chart.js recipe, PowerPoint chart colour rules, palette.
- brand-kit/references/tables-and-kpis.md - table & KPI styles and markup, both themes.
- brand-kit/references/content-and-qa.md - wording, sourcing, data integrity, pre-export QA checklist.
- brand-kit/references/pptx-and-pdf.md - rendering HTML→PDF, or producing a PowerPoint file.

## Companions
Content comes from the investgame-gaming-data hub (the data) and investgame-analysis (the read). For a full
structured report, investgame-research orchestrates and calls this skill for the presentation step.

## Common mistakes
- Treating presentation as optional - every data answer should be shown cleanly, in chat or as a file.
- Building a deck when a sentence or a small in-chat table would do - match the form to the ask.
- Mixing the two themes in one file. · Green for positive (use teal) or a red/green dashboard.
- Showing fixed-choice fields as raw text instead of tags; bare country codes with no flag; entity names that
  aren't linked when a link exists.
- A4-squash of a slide deck from a generic PDF helper - use the bundled render script that honours the CSS @page size.
- Charts exporting blank - resize before print.
- No source line on a data slide. · A title that states the topic instead of the insight.
- Any non-InvestGame branding slipping in.
- Dropping or re-judging which fields belong in the answer - that's investgame-analysis's call; Format only
  decides how the chosen fields are shown.
