# Typography

Exact font roles, sizes, and weights for both InvestGame skins, the web-font load for the Warm White skin, offline fallbacks, and the two type habits that keep a deck looking professional. Names match `assets/ig_brand.css` and `assets/ig_helpers.py`.

## Contents

- [Dark Navy skin](#dark-navy-skin)
- [Warm White skin](#warm-white-skin)
- [Google Fonts load (Warm White skin)](#google-fonts-load-warm-white-skin)
- [PowerPoint / offline fallbacks](#powerpoint--offline-fallbacks)
- [Keep the type scale consistent](#keep-the-type-scale-consistent)
- [Tabular figures for number columns](#tabular-figures-for-number-columns)

---

## Dark Navy skin

Font: **"Helvetica Neue"**, `Arial` fallback. One family throughout - weight and size carry the hierarchy, not a second typeface.

| Role | Size | Weight | Notes |
|------|------|--------|-------|
| Cover headline | 78px | 800 | Letter-spacing −1px; the hero line |
| Page title | 32px | 800 | Slide takeaway title |
| Dark Navy chip | 14px | 800 | Uppercase; section / kicker label |
| Page deck / body | 15px | 400 | Paragraph and bullet body |
| KPI label | 11px | 700 | Uppercase tile label |
| KPI value (big) | 40px | 800 | The headline metric on a tile |
| Table | 11–12px | 400–700 | Header row 700 uppercase; cells 400 |
| Footer | 12px | 400 | In `--gray` |

---

## Warm White skin

Fonts: body **Inter**, display **Space Grotesk**, numbers **JetBrains Mono**. Each family has one job - don't set body in Space Grotesk or headings in Inter.

| Role | Size | Weight | Font | Notes |
|------|------|--------|------|-------|
| Cover h1 | 60px | 700 | Space Grotesk | Report title |
| Slide title | 28px | 700 | Inter | Letter-spacing −0.015em |
| Kicker | 11px | 700 | Inter | Uppercase, letter-spacing 0.22em, colour `--ig-accent-deep #3D9B8F` |
| Slide conclusion | 17px | 500 | Inter | The so-what line under the title |
| Bullets | 16px | 400 | Inter | Line-height 1.48 |
| KPI label | 10px | 600 | Inter | Uppercase tile label |
| KPI value | 30px | 700 | Space Grotesk | The metric on a tile |
| Matrix `th` | 11px | 600–700 | Inter | Uppercase header row |
| Matrix `td.num` | 13px | 400 | JetBrains Mono | Right-aligned numeric cells |
| Footnotes | 9.5px | 400 | Inter | In `--ig-text-muted` |

---

## Google Fonts load (Warm White skin)

Put this in the `<head>` so the three families are available before first paint:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

The Dark Navy skin needs no web font - Helvetica Neue ships with the OS.

---

## PowerPoint / offline fallbacks

When a build can't load web fonts (PowerPoint, headless render without network, an offline reader), map to a system face that holds the same weight feel rather than letting the app substitute silently.

| Brand font | Fallback |
|------------|----------|
| Space Grotesk | Arial Bold / Heavy |
| Inter | Aptos (or Arial) |
| JetBrains Mono | Consolas |
| Helvetica Neue | Arial |

(`FONTS_FEATURE` and `FONTS_REPORT` in `ig_helpers.py` carry these for python-pptx / openpyxl builds.)

---

## Keep the type scale consistent

Reuse the same size for the same role on every slide - a page title is 32px (Dark Navy) or 28px (Warm White) on slide 2 and on slide 20, never nudged to fit. Size-jumping between similar slides is the single most common thing that makes a deck look amateur: the reader reads inconsistent sizes as inconsistent importance, and the deck stops feeling like one document. If a title doesn't fit, cut words or change the layout - don't shrink the type.

---

## Tabular figures for number columns

Set `font-variant-numeric: tabular-nums` on any column of numbers (the `.tabular` class in `ig_brand.css`; JetBrains Mono in the Warm White skin is already monospaced). Proportional digits give each numeral a different width, so a stack of figures jitters left-to-right and the decimal points don't line up - the eye can't scan or compare down the column. Tabular figures fix every digit to the same width, so numbers align cleanly and a quick visual sort actually works. See `references/tables-and-kpis.md` for table styling.
