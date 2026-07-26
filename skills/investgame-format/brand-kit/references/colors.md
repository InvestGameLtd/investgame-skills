# Colours

The full InvestGame palette, the two rules that decide most colour calls, the chart series order, and a short decision guide. Names match `assets/ig_brand.css` and `assets/ig_helpers.py` - refer to colours by name, not by re-typed hex, so artifacts don't drift off-palette.

## Contents

- [Shared brand core](#shared-brand-core)
- [Dark Navy skin](#dark-navy-skin)
- [Warm White skin](#warm-white-skin)
- [The two rules that matter most](#the-two-rules-that-matter-most)
- [Chart series order](#chart-series-order)
- [Decision guide](#decision-guide)
- [Contrast & accessibility](#contrast--accessibility)

---

## Shared brand core

Present in every InvestGame artifact, both skins. The teal is what reads as "InvestGame" - keep it on screen.

| Hex | Token | Role |
|-----|-------|------|
| `#61BFB3` | `--ig-teal` | **PRIMARY** - the InvestGame colour. Accents, highlights, first chart series, positive feeling in both skins |
| `#1ECABA` | `--ig-teal-bright` | Bright teal - big stat numerals on dark backgrounds |
| `#00928A` | `--ig-teal-deep` | Deep teal - chips, emphasis, **positive deltas** |
| `#6189D6` | `--ig-blue` | Secondary accent, second chart series |
| `#2D5BA8` | `--ig-blue-deep` | Deep blue - third accent |

---

## Dark Navy skin

Dark-navy editorial deck (canvas 1456×820). Adds these to the core.

| Hex | Token | Role |
|-----|-------|------|
| `#0E1F33` | `--navy` | Primary dark background **and** body text on light pages |
| `#142A44` | `--navy-2` | Secondary dark / gradient stop |
| `#8A95A4` | `--slate` | Muted slate text |
| `#8FA1B5` | `--gray` | Labels, captions, footer |
| `#F5F7FA` | `--light` | Subtle panel background on light pages |
| `#E1E6EC` | `--rule` | Hairline borders |
| `#45596F` | `--ink-soft` | Secondary body text on light pages |
| `#E1F4F1` | `--tint-teal` | Teal-tinted highlight row / panel |

---

## Warm White skin

Warm off-white scholarly report (canvas 1280×720). Adds these to the core.

| Hex | Token | Role |
|-----|-------|------|
| `#F4F3EE` | `--ig-bg` | Warm off-white page background |
| `#EEEDE6` | `--ig-bg-soft` | Softer panel background |
| `#FFFFFF` | `--ig-card-bg` | White card |
| `#0B1A2A` | `--ig-text` | Primary text (warm navy) |
| `#5F6B7A` | `--ig-text-muted` | Secondary text, captions, footnotes |
| `#8E99A6` | `--ig-text-soft` | Tertiary text, separators |
| `#61BFB3` | `--ig-accent` | Primary brand teal |
| `#3D9B8F` | `--ig-accent-deep` | Deep teal - kickers, footnote marks, accents |
| `#E6F4F2` | `--ig-accent-soft` | Teal-tinted callout / highlighted row |
| `#C07B5A` | `--ig-warn` | Rust - caution / "banned" / negative |
| `#F5E6DD` | `--ig-warn-soft` | Rust-tinted panel |
| `#E0DFD9` | `--ig-border` | Hairline border |
| `#C7C6C0` | `--ig-border-strong` | Stronger divider |

---

## The two rules that matter most

**1. Positive movement is teal `#00928A` - not green.** Green is the default colour every generic finance dashboard uses for "up", so it reads as profit/loss noise rather than a deliberate brand choice. Teal carries the same "good" meaning while staying unmistakably InvestGame. Use `#00928A` for up-deltas, growth bars, and positive callouts in both skins (`POSITIVE` in `ig_helpers.py`).

**2. Negative / caution is rust `#C07B5A` - used sparingly.** InvestGame decks are analysis, not a red/green trading screen, so saturated red is off-brand. The warm rust signals "down", banned, or risk without turning a slide into a dashboard. Reach for it only on the one figure that needs the warning; a slide full of rust defeats the point (`NEGATIVE` in `ig_helpers.py`, `--ig-warn` in the Warm White skin).

---

## Chart series order

Apply colours to series in this exact sequence so any two charts in a deck stay consistent. See `references/charts.md` for the full chart recipes.

| # | Hex | Name |
|---|-----|------|
| 1 | `#61BFB3` | teal (primary) |
| 2 | `#6189D6` | blue |
| 3 | `#00928A` | teal-deep |
| 4 | `#2D5BA8` | blue-deep |
| 5 | `#8A95A4` | slate |
| 6 | `#1ECABA` | teal-bright |
| 7 | `#8FA1B5` | gray |

Positive deltas override the sequence with teal `#00928A`; caution with rust `#C07B5A`. (`CHART_COLORS` in `ig_helpers.py`.)

---

## Decision guide

**Teal vs blue vs slate**

- **Teal `#61BFB3`** - the default accent and first thing the eye should land on. The brand signature, the lead chart series, the takeaway highlight.
- **Blue `#6189D6` / `#2D5BA8`** - the second voice. Use when you need a clear contrast to teal: a second series, a "compare against" bar, a secondary accent. Don't lead with blue where teal would do - that reads as a different brand.
- **Slate `#8A95A4` / gray `#8FA1B5`** - recede. Labels, captions, footer, axis ticks, and the "rest" or "other" series that should sit quietly behind the highlighted ones.

**When the tint / highlight panel applies**

- **Dark Navy skin** - drop `--tint-teal #E1F4F1` behind the one row or panel carrying the slide's takeaway (pairs with a teal left-border). One tinted row per table; more than one and the highlight stops meaning anything.
- **Warm White skin** - `--ig-accent-soft #E6F4F2` does the same job for the highlighted row or a positive callout box. Use `--ig-warn-soft #F5E6DD` only for the rust caution callout, matching rule 2 above.

---

## Contrast & accessibility

- **On navy `#0E1F33`** - use white text and the bright teal `#1ECABA` for big numerals; both clear AA comfortably. Body greys (`--slate`, `--gray`) are for labels on dark, not paragraph text.
- **On warm bg `#F4F3EE`** - use `#0B1A2A` for body text (high contrast, warm navy). `--ig-text-muted #5F6B7A` is fine for captions; `--ig-text-soft #8E99A6` is for separators and tertiary marks only, not body copy.
- **Keep rust `#C07B5A` off large text.** It is a signal colour with modest contrast on warm backgrounds - fine for a small delta, a chip, or a thin caution bar, but it fails as a headline or body fill. If a whole block needs to read "caution", use `--ig-warn-soft` as the panel and keep the words in `#0B1A2A`.
