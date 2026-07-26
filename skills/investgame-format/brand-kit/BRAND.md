---
name: investgame-brand
description: Use when building, editing, or styling any visual deliverable for InvestGame - pitch decks, market or regional gaming reports, feature and research decks, one-pagers, charts, tables, KPI tiles, cover and section slides, or any branded HTML-to-PDF or PowerPoint artifact about the games industry, gaming M&A, financings, or company and market analysis. Establishes InvestGame colours, typography, logos, slide layouts, and chart and table conventions. Trigger on "InvestGame deck", "InvestGame report", "brand colors", "our palette", "company theme", "dark navy or warm white", "build a deck", "make a chart", "make a table", "market report", "feature deck", "gaming report", "regional report", "one-pager", or any request for InvestGame-branded slides even when the word "deck" is not used. Load this skill before the pptx or xlsx skills so brand settings, templates, and chart conventions are established first, and prefer copying a bundled HTML template over building from a blank file.
license: © InvestGame Ltd. Provided to InvestGame and its clients for producing InvestGame-branded materials.
metadata:
  version: 1.1.0
---

# InvestGame Brand System

This skill is the visual identity for **InvestGame** - the data and research voice for games-industry investment, M&A, and financings. It exists so every deck, report, chart, and one-pager looks like it came from the same house, without re-deciding colours and layout each time.

Read this file once before any visual work. Pull the matching `references/` file only when you actually need that detail - they are split so you load one section, not nine.

**Core principle:** match the artifact to one of the two **themes** below, then start from its bundled template and replace content in place. Building from a blank file is the fallback, not the default - it is how decks drift off-brand.

## Contents
The two themes · Start from a template · Design principles · Colour system · Typography · Logo usage · Slide canvas & layout · Charts · Tables & KPI tiles · Content & QA · References cheat-sheet · Do's and Don'ts

---

## The two themes - Dark Navy or Warm White

InvestGame ships in two looks that share one teal/navy core and both carry the InvestGame logo. When someone asks for a deck, offer the choice plainly: **Dark Navy** (dark, bold) or **Warm White** (light, data-dense). Pick one per artifact by what it is - don't mix them on one deck; that reads as two brands stapled together.

| | **Dark Navy** | **Warm White** |
|---|---|---|
| Pick it for | Bold, editorial - features, pitches, deal/financing recaps, narrative research with a hero cover | Calm, scholarly - data-dense market & regional reports, methodology-heavy analysis, many charts/tables |
| Background | Navy `#0E1F33` (dark pages) / white content pages | Warm off-white `#F4F3EE` |
| Canvas | **1456 × 820 px** (16:9) | **1280 × 720 px** (16:9) |
| Fonts | Helvetica Neue | Space Grotesk (display) · Inter (body) · JetBrains Mono (numbers) |
| Logo | White logotype on cover + footer | Full-colour logo on cover + slide corner |
| Template | `assets/templates/dark-navy.html` | `assets/templates/warm-white.html` |
| Charts | Interactive Chart.js (or static CSS bars) | Interactive Chart.js |

Both carry the **primary brand teal `#61BFB3`** - the single colour that says "InvestGame" in either theme.

---

## Start from a template - don't rebuild

This is the highest-leverage habit in the skill. The bundled templates already encode canvas size, cover, content layouts, KPI tiles, chart/table styling, the logo, footer chrome, and print-to-PDF CSS. Copying one and swapping content is faster and stays on-brand; rebuilding from a blank file reliably drifts.

**HTML → PDF workflow (default for both themes):**
1. Copy the matching template to your working folder.
2. Replace placeholder copy, numbers, and chart data **in place** - keep the class names and structure.
3. Duplicate a slide section to add a page; delete sections you don't need.
4. Render to PDF (see `references/pptx-and-pdf.md`; `scripts/render_pdf.py` does it headless).

**PowerPoint workflow:** see `references/pptx-and-pdf.md`. Set slide size to **13.33 × 7.5 in** first, build with `assets/ig_helpers.py` constants, and never let PowerPoint auto-pick colours.

### Bundled files

| File | What it is |
|------|------------|
| `assets/templates/dark-navy.html` | Canonical Dark Navy starter - copy this for that theme |
| `assets/templates/warm-white.html` | Canonical Warm White starter - copy this for that theme |
| `assets/ig_brand.css` | Token source of truth (both themes) for from-scratch HTML builds |
| `assets/ig_helpers.py` | Colour/type constants for PowerPoint & Excel (python-pptx / pptxgenjs / openpyxl) |
| `assets/ig_helpers.js` | Colour tokens + Chart.js defaults for HTML decks |
| `assets/logos/` | The real InvestGame logos - colour mark + white logotype (see `references/logos.md`) |
| `scripts/render_pdf.py` | Headless HTML → PDF at the exact slide canvas |

---

## Design principles

The templates already embody these; keep them when you edit, and lean on them when you build something new. Each is a habit that separates a polished deck from a generic one.

- **One idea per slide.** A single takeaway, one primary visual (a KPI row OR a table OR a chart). Competing visuals split attention and the point is lost.
- **Lead the eye.** Build a clear hierarchy - the reader should land on the takeaway first. Size, weight, and the teal accent direct attention; everything else recedes.
- **Whitespace is confidence.** Don't fill every pixel. Breathing room around a chart or a stat reads as considered; a crammed slide reads as anxious.
- **Align to the grid.** Everything sits on the template's safe-zone and margins. Ragged, hand-nudged edges are the fastest tell of an amateur deck.
- **Restraint and repetition.** Reuse the same patterns slide to slide; let one accent do the highlighting. Consistency makes a deck feel like one document.
- **Maximise meaning, minimise ink.** No chartjunk, no 3-D, no gradients for their own sake. Every mark should carry information.
- **Charts are interactive on screen.** Build charts with Chart.js so the audience can hover for tooltips and probe the numbers; the exported PDF stays clean and static. Colour carries meaning - teal is brand/positive, rust is caution - never decoration.
- **Legible and accessible.** Text meets contrast on its background; never signal with colour alone (pair it with a label or position).

Claude's general design tooling (such as a frontend-design skill, if present in the environment) complements these, but everything here is self-contained - the skill works on its own.

---

## Colour system - overview

The shared core appears in every artifact; reach past it only with intent.

| Role | Name | Hex | Where |
|------|------|-----|-------|
| Primary | Brand Teal | `#61BFB3` | The InvestGame colour - accents, highlights, positive in both themes |
| Bright | Teal Bright | `#1ECABA` | Big stat numerals on dark |
| Deep | Teal Deep | `#00928A` | Chips, emphasis, **positive deltas** |
| Secondary | Blue | `#6189D6` | Second chart series, secondary accents |
| Secondary deep | Blue Deep | `#2D5BA8` | Third accent |

- **Dark Navy** adds: Navy `#0E1F33` (background + body text on light), Slate `#8A95A4` / Gray `#8FA1B5` (labels), Light `#F5F7FA` (panels), Rule `#E1E6EC` (borders), teal tint `#E1F4F1` (highlight rows).
- **Warm White** adds: warm bg `#F4F3EE`, text `#0B1A2A`, muted `#5F6B7A`, deep-teal accent `#3D9B8F`, teal-soft `#E6F4F2`, and a **rust caution** tone `#C07B5A` / `#F5E6DD` for "down" or risk callouts.

**Two colour rules that matter most:** positive movement is **teal `#00928A`, never green** - green reads as generic profit/loss noise in finance decks. Negative/caution is the **rust `#C07B5A`, used sparingly** - InvestGame decks are not red-and-green dashboards. Full palette, decision trees, and the chart series order live in **`references/colors.md`**.

---

## Typography - overview

| Theme | Display / headings | Body | Numbers |
|------|--------------------|------|---------|
| Dark Navy | Helvetica Neue, 800 weight | Helvetica Neue | Helvetica Neue |
| Warm White | Space Grotesk, 700 | Inter, 400–600 | JetBrains Mono |

The Warm White theme loads its three fonts from Google Fonts (link in `assets/ig_brand.css`). Keep the type scale consistent - jumping sizes between similar slides is the most common thing that makes a deck look amateur. For PowerPoint fallbacks, the exact role table, and sizes, see **`references/typography.md`**.

---

## Logo usage - overview

The real logos live in `assets/logos/`. **The background decides the file, nothing else does:** light or warm takes `ig-logo-navy.png`, dark takes `ig-logotype-white.png` / `.webp` or `ig-logo.png`. The wordmark is **one word, "investgame"**. Which file goes in which slot, clear space, minimum sizes, and the full Don'ts are in **`references/logos.md`**.

---

## Slide canvas & layout

Set the canvas first (Dark Navy 1456×820, Warm White 1280×720) - both are 16:9; the body safe-zone and footer positions in the templates assume these exact sizes.

Pick a layout by what the slide carries:

| If the slide is… | Use |
|---|---|
| Cover / title | Cover layout (hero headline + logo) |
| Major section break | Section divider |
| One insight + a KPI row (2–4 tiles) | Content + KPI tiles |
| One insight + a single chart | Content + chart (one visual per slide) |
| Ranked / comparative data | Data table |
| This-vs-that or chart + side callout | Two-column |
| Glossary / sources | List layouts |
| Closing | Thanks / contact |

A slide carries **one** primary visual (a KPI row OR a table OR a chart), never several competing for attention. Anatomy and worked markup for every layout are in **`references/layouts.md`**.

---

## Charts - overview

**Default to bar/column** unless the data clearly calls for something else - it is the most legible and the most on-brand. Build with **Chart.js so charts are interactive on screen** - hovering a category pops a tooltip with the underlying numbers; the PDF export stays clean and static. Apply series in the palette order (teal → blue → deep teal → deep blue → slate). Positive deltas teal `#00928A`, caution rust `#C07B5A`, never green, never a red/green dashboard.

**Chart.js gotcha:** any chart on a slide that is shown/hidden (the Warm White template paginates this way) must call `chart.resize()` when its slide becomes visible - and resize on `beforeprint` - or it paints at 0px / exports blank. The bundled templates already handle this. The chart-type-to-data map and full Chart.js / PowerPoint recipes are in **`references/charts.md`**.

---

## Tables & KPI tiles - overview

Tables: uppercase header row, hairline row separators, right-aligned tabular numbers (JetBrains Mono in the Warm White theme), one highlighted row with a teal left-border for the takeaway line. KPI tiles: small uppercase label, large value with a small unit, one-line note; use the teal "hero" variant for the headline metric and the rust "warn" variant for a risk metric. Full styles for both themes in **`references/tables-and-kpis.md`**.

---

## Content & QA

A branded deck still fails if the words and numbers are sloppy. The judgement rules that travel with InvestGame decks:

- **Titles carry the insight, not the topic.** "PC gaming runs on budget laptops, not desktops" - not "PC hardware overview." The conclusion line underneath says the *so-what*.
- **One source of truth per figure.** When sources disagree, average across them and show the range; never silently pick one. Label fiscal vs calendar years and state FX assumptions next to converted figures.
- **Layered uniqueness.** KPI row, table, bullets, and conclusion each add something - none restates another.
- **Acknowledge gaps honestly.** "Insufficient public data" beats an invented number.

The full content rules, sourcing discipline, the cover-minimalism guidance, and the pre-export **QA checklist** are in **`references/content-and-qa.md`**.

---

## References cheat-sheet

Don't read these up front - pull the one the task needs.

| File | Read it when |
|------|--------------|
| `references/colors.md` | Choosing any non-obvious colour; full palette, decision trees, chart order |
| `references/typography.md` | Font roles, sizes, weights, PowerPoint fallbacks |
| `references/logos.md` | Placing the logo; clear-space, sizing, on-light/on-dark, don'ts |
| `references/layouts.md` | Building or editing a slide; anatomy + markup per layout, both themes |
| `references/charts.md` | Any chart; chart-type map, Chart.js + PowerPoint recipes, palette |
| `references/tables-and-kpis.md` | Tables and KPI tiles; styles and markup for both themes |
| `references/content-and-qa.md` | Wording, sourcing, data integrity, and the pre-export QA checklist |
| `references/pptx-and-pdf.md` | Rendering HTML to PDF, or producing a PowerPoint file |

---

## Do's and Don'ts

**Do:**
- Offer the choice - Dark Navy or Warm White - then copy that theme's template and edit in place.
- Set the canvas size before adding content (Dark Navy 1456×820, Warm White 1280×720; PowerPoint 13.33×7.5in).
- Refer to colours by name from `ig_brand.css` / `ig_helpers.*`.
- Keep the brand teal `#61BFB3` and the InvestGame logo present; use teal `#00928A` for positive movement.
- Give each slide one primary visual and a takeaway title.
- Build charts with Chart.js so they're interactive on hover.
- Put the source line on every data slide; label FY vs CY and FX.
- Use the white logotype on dark backgrounds, the colour logo on light/warm backgrounds.

**Don't:**
- Don't rebuild from a blank file when a template fits.
- Don't mix the two themes on one artifact.
- Don't use green for positive or build a red/green dashboard - teal is positive, rust is caution, used sparingly.
- Don't recolour, stretch, rotate, or add effects to the logo.
- Don't put more than one primary visual on a slide.
- Don't let a title state a topic instead of the insight.
- Don't ship a data slide with no source, or mix fiscal and calendar years on one axis without labels.
- Don't let PowerPoint auto-assign chart colours - set them from `ig_helpers.py`.
