---
name: investgame-format
version: 0.8.2
description: >
  Presentation layer for every InvestGame answer — decide how to show it and, when asked, render it
  on-brand. Use on ANY answer that benefits from being presented well, not only file requests: whenever
  you show a table, a chart, a comparison, a comp set, or a list of deals/companies, make it clean,
  consistent and readable. Triggers: "make a deck", "build a PDF", "export to PowerPoint", "an Excel of
  this", "a branded report", "a one-pager", "a page", "show this as a chart/table", "present this", "make
  it presentable", "put our brand on it" — and implicitly on every data answer. Two jobs: (1) presentation
  advice — the right form, chart, tags, links and layout; (2) the render engine — on-brand
  HTML/PDF/PowerPoint/Excel from the bundled InvestGame brand kit. Pure InvestGame brand. It decides HOW to
  present; WHAT is analytically worth showing is investgame-analysis's call. Not for game-design or generic
  software questions.
---

# InvestGame Format

The presentation layer for every InvestGame answer — always on, not only when someone asks for a file. Any
time you show data, think about how to present it so the reader gets the insight at a glance. Two jobs:
advise on the right way to present, and render it on-brand when a real deliverable is asked for. Pure
InvestGame brand — never another house brand, never internal authorship.

## Job 1 — match the presentation to the request
First decide how much presentation the request needs. Most answers stay in chat; only some become files.

In chat (the default — no file, no brand kit needed):
- For a normal data answer, present it cleanly with your built-in, in-chat tools — a readable table, or a
  simple chart when the data is visual (a trend, a breakdown, a comp set). You don't need the brand kit or a
  file for this; just make the in-chat output consistent, well-labelled and easy to scan, and apply the
  presentation conventions below (tags, flags, links).
- A quick fact → a sentence. A short comparison → a compact table. A handful of headline metrics → a small
  table or KPI-style lines. A trend or a comp set → an in-chat chart.
- If the surface can't render a chart, degrade to a well-labelled table carrying the same comparison (keep
  the median row, sort by the multiple) — never emit broken chart markup or drop the comparison silently.

A real deliverable (only when the user asks for one — "deck", "report", "PDF", "PowerPoint", "Excel",
"one-pager", "a page", "branded", "on our brand"):
- Build it with the brand kit. Default order: start with an interactive HTML build; produce a PDF from it if
  a fixed document is wanted; produce PowerPoint or Excel only when the client asks for those formats.
- A two-line answer never needs a deck; a board report shouldn't be a wall of text.

If it's genuinely unclear, or both would work, ask once with a concrete suggestion ("just here in chat, or a
branded one-pager?"), then commit. If the user already named a form ("make a deck"), don't re-ask.

## The fence with investgame-analysis (read this)
investgame-analysis decides WHAT is analytically relevant — which metrics and supporting fields answer the
question and help the user decide. Format decides HOW that content is shown — which fields become table
columns, which get demoted to a footnote or small print, their order and grouping, and the best visual
(table / chart / KPI tiles). Format never DROPS an analytically-relevant field to save room: if content
genuinely won't fit, demote or summarise it, or flag that the scope is too wide — cutting a field is
investgame-analysis's call. Quick routing test: if the decision changes WHETHER a field is in the answer,
it's Analysis; if it only changes WHERE or HOW it appears, it's Format.

## Presenting valuations & comp sets (the house pattern)
Multiples and comps have a standard, recognisable look — use it whenever you show a valuation comparison
(the single most common analytical output). Works the same in-chat and as a branded deliverable:
- A column/bar chart, one bar per deal, sorted by the multiple (high to low), each bar labelled with its
  value (e.g. "8.2x").
- A median line across the chart, labelled ("Median 8.2x") — the comp-set reference point.
- Colour the bars by a meaningful category (monetization, platform, or deal type), with a short legend, so
  the pattern is visible at a glance.
- Below the chart, a table of the deals: date · target · acquirer/investor · EV ($M) · the multiple · the
  period (LTM/CYO/NTM) and metric (EV/EBITDA vs EV/EBIT) · the category as a tag.
- A one-line source note ("Source: InvestGame") and any caveat (e.g. which metric/period mix was used, per
  the never-break-silently rule in investgame-analysis).
Analysis chooses the comps and the fields; you make them read like a comp set.

## Presentation conventions (in-chat and on-brand)
- Tags for fixed-choice fields. When a field has a defined set of values — monetization, company type,
  sector, genre, platform — show it as a small tag/chip, not raw text. Faster to scan, and it looks
  considered.
- Flags for countries. Show the country flag alongside (or in place of) the ISO code. In branded HTML use
  flag-icon SVGs, not Unicode flag emoji (emoji flags render as bare letters on some platforms, e.g.
  Windows); in chat, the built-in rendering is fine.
- Links for entities — link every named deal, company and index to its InvestGame page, so the reader can
  click any name and land on the record. Base URL: `https://app.investgame.net` (always the `app.` subdomain).
  - Deal → `https://app.investgame.net/deals/{deal_id}`
  - Company → `https://app.investgame.net/companies/{company_id}`
  - Index → `https://app.investgame.net/market-indices/{slug}`
  The ids come from the response's `entities` array (`{type, id, url}`) — that `url` is authoritative, use it
  directly. When you only have an id (a table cell), build the URL from the pattern above. Never link the bare
  `investgame.net/...` host (it 404s), and never invent a link from a name — if there is no id, leave the name
  unlinked rather than guess.
- Numbers right-aligned, USD millions unless stated, consistent decimals; lead the eye to the takeaway.

## Start from a template — don't rebuild (deliverables)
The complete InvestGame brand system ships in brand-kit/. Highest-leverage habit: copy the matching theme
template and replace content in place, keeping the class names — far faster and more on-brand than a blank
file. Bundled:
- brand-kit/assets/templates/warm-white.html and dark-navy.html — canonical starters (canvas, cover, KPI
  tiles, table/chart styling, logo, print-to-PDF CSS all pre-encoded).
- brand-kit/assets/logos/ — the real InvestGame logos · brand-kit/assets/ig_brand.css — colour/type tokens.
- brand-kit/assets/ig_helpers.py — colour/type constants for PowerPoint & Excel · brand-kit/assets/
  ig_helpers.js — colour tokens + Chart.js defaults for HTML.
- brand-kit/scripts/render_pdf.py — headless HTML→PDF at the exact canvas (cross-platform).

## Pick the theme (never mix them in one file)
| Theme | Use for | Canvas / fonts |
|-------|---------|----------------|
| Warm White (default) | data-dense reports, comps, market reports, briefings | 1280×720 · Space Grotesk + Inter + JetBrains Mono · bg #F4F3EE |
| Dark Navy | bold/editorial decks, recaps | 1456×820 · Helvetica Neue · bg #0E1F33 |
Offer the choice plainly when someone asks for a deck. Both carry the brand teal and the InvestGame logo.

## Brand constants
- Brand teal #61BFB3 is the InvestGame colour. Positive = teal #00928A, never green. Caution = rust #C07B5A,
  sparingly — InvestGame outputs are not red/green dashboards. Secondary series: blue #6189D6 → deep teal →
  deep blue → slate.
- One idea per slide; the title carries the insight, not the topic. Whitespace over clutter. InvestGame logo
  present; every data slide carries a source line.

## Render playbook
- In chat (default). Use your built-in chart/table rendering and apply the conventions above (tags, flags,
  links, the comp-set pattern). No brand kit, no file.
- HTML interactive (the default for a deliverable). Copy brand-kit/assets/templates/<theme>.html, duplicate a
  slide section per page, replace placeholders in place. Render to PDF with brand-kit/scripts/render_pdf.py —
  it finds a headless browser and honours the template's CSS @page size. The script needs ONE headless
  browser: Playwright's bundled Chromium (pip install playwright && playwright install chromium) or a system
  Chrome/Chromium; if it reports no renderer, install one of those. Don't use a generic HTML→PDF helper that
  forces A4 — it squashes the canvas. Verify the PDF page size matches the canvas.
- PowerPoint (.pptx, on request). Set slide size to 13.33 × 7.5 in first; apply brand colours/fonts from
  assets/ig_helpers.py explicitly (never let PowerPoint auto-pick chart colours); one primary visual per
  slide.
- Excel (.xlsx — on request, AND as the data backup for any deliverable with charts). Header row navy #0E1F33
  + white bold; thin #CCCCCC borders; right-aligned tabular numbers (USD millions unless stated); a
  source/notes row; freeze the header; charts in the teal palette. Whenever a deck or PDF ships a chart, also
  provide a clean Excel of the underlying data, so the reader can see how each chart was built and where the
  numbers came from.
- HTML (interactive). Same tokens; charts via Chart.js (interactive on hover). See Charts below for the
  resize-before-print gotcha that otherwise exports a blank chart.

## Charts — overview
Default to bar/column unless the data clearly calls for something else — most legible, most on-brand. Build
with Chart.js so charts are interactive on screen; the PDF export stays clean and static. Apply series in
palette order (teal → blue → deep teal → deep blue → slate); positive deltas teal, caution rust, never green,
never a red/green dashboard. Gotcha: a chart on a slide that is shown/hidden must call chart.resize() when its
slide becomes visible (and on beforeprint) or it paints at 0px / exports blank — the bundled templates already
handle this. Full chart-type-to-data map + Chart.js / PowerPoint recipes in brand-kit/references/charts.md.

## Tables & KPI tiles — overview
Tables: uppercase header row, hairline row separators, right-aligned tabular numbers, one highlighted row with
a teal left-border for the takeaway; fixed-choice fields as tags, entities as links. KPI tiles: small
uppercase label, large value + small unit, one-line note; teal "hero" variant for the headline metric, rust
"warn" for a risk metric. Full styles in brand-kit/references/tables-and-kpis.md.

## Content & QA — overview
A branded output still fails if the words and numbers are sloppy. Titles carry the insight, not the topic.
One source of truth per figure; when sources disagree, show the range, never silently pick one. Label fiscal
vs calendar years and FX next to converted figures. Acknowledge gaps honestly. Ship the data-backup Excel for
any deliverable with charts. Full rules + the pre-export QA checklist in brand-kit/references/content-and-qa.md.

## References (pull the one the task needs — don't read them up front)
- brand-kit/references/colors.md — full palette, decision trees, chart series order.
- brand-kit/references/typography.md — font roles, sizes, weights, PowerPoint fallbacks.
- brand-kit/references/logos.md — placing the logo; clear-space, sizing, on-light/on-dark, don'ts.
- brand-kit/references/layouts.md — building/editing a slide; anatomy + markup per layout, both themes.
- brand-kit/references/charts.md — chart-type map, Chart.js + PowerPoint recipes, palette.
- brand-kit/references/tables-and-kpis.md — table & KPI styles and markup, both themes.
- brand-kit/references/content-and-qa.md — wording, sourcing, data integrity, pre-export QA checklist.
- brand-kit/references/pptx-and-pdf.md — rendering HTML→PDF, or producing a PowerPoint file.

## Companions
Content comes from the investgame-gaming-data hub (the data) and investgame-analysis (the read). For a full
structured report, investgame-research orchestrates and calls this skill for the presentation step.

## Common mistakes
- Treating presentation as optional — every data answer should be shown cleanly, in chat or as a file.
- Building a deck when a sentence or a small in-chat table would do — match the form to the ask.
- Mixing the two themes in one file. · Green for positive (use teal) or a red/green dashboard.
- Showing fixed-choice fields as raw text instead of tags; bare country codes with no flag; entity names that
  aren't linked when a link exists.
- A4-squash from a generic PDF helper — use the bundled render script that honours the CSS @page size.
- Charts exporting blank — resize before print. · A deck/PDF with charts but no backup Excel of the data.
- No source line on a data slide. · A title that states the topic instead of the insight.
- Any non-InvestGame branding slipping in.
- Dropping or re-judging which fields belong in the answer — that's investgame-analysis's call; Format only
  decides how the chosen fields are shown.
