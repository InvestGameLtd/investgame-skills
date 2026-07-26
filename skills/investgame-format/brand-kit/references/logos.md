# Logos

How to place the InvestGame mark on either skin. For where layouts put the cover and footer slots, see `references/layouts.md`. For the colour tokens named below, see `references/colors.md`.

## Contents

- [The real logo files](#the-real-logo-files)
- [The wordmark is one word: "investgame"](#the-wordmark-is-one-word-investgame)
- [Which mark on which background - and why](#which-mark-on-which-background--and-why)
- [Where the logo goes](#where-the-logo-goes)
- [Clear space](#clear-space)
- [Minimum sizes](#minimum-sizes)
- [Don'ts](#donts)

---

## The real logo files

The shipped artwork lives in `assets/logos/`. There are only four files; everything below uses one of them.

| File | What it is | Use on |
|------|------------|--------|
| `ig-logo-navy.png` | Navy wordmark + teal mark | **LIGHT backgrounds. The default light-background logo.** |
| `ig-logo.png` | White wordmark + teal mark | DARK backgrounds, and inside a navy band |
| `ig-logotype-white.png` | White logotype (raster) | DARK backgrounds |
| `ig-logotype-white.webp` | White logotype (smaller `.webp`) | DARK backgrounds - prefer when the renderer supports WebP; smaller file, same artwork |

The templates reference these by relative path - e.g. `assets/templates/dark-navy.html` loads `../logos/ig-logotype-white.png` on its dark cover and footer, and `warm-white.html` loads `../logos/ig-logo-navy.png`. Keep that path when you copy a template; don't inline a different logo.

## The wordmark is one word: "investgame"

**Never use artwork that renders it as "invest game" with a space, or splits it across two lines.** The one-word lockup is the current mark. Older exports carry a spaced version and are stale, so before using any logo from outside `assets/logos/`, look at it: a gap between "invest" and "game" means it is the old artwork and must not ship.

---

## Which mark on which background - and why

**The background decides the file. Nothing else does.** The rule is contrast, not preference:

| Background | Wordmark | File |
|---|---|---|
| Warm White `#F4F3EE`, white, any light page | **Navy** | `ig-logo-navy.png` |
| Navy `#0E1F33`, any dark page or panel | White | `ig-logotype-white.png` / `.webp`, or `ig-logo.png` |

This single rule covers every slot: cover, footer, and slide corner alike. The **Dark Navy** skin uses the white logotype on its dark cover and footer. The **Warm White** skin uses `ig-logo-navy.png` on its warm cover, in the slide corner and in the footer. See the cover anatomy in `references/layouts.md`.

**Why a navy-wordmark file exists.** Every logo export historically carried a pure white wordmark `#FFFFFF`, including the ones labelled for light backgrounds, so on Warm White the word "investgame" was invisible and only the teal mark showed. `ig-logo-navy.png` is that artwork with the white wordmark pixels swapped to navy `#0B1A2A`, teal mark untouched. It is a legibility repair, not a re-tint. Use the shipped file rather than regenerating it, or copies will drift. If you ever must rebuild it from corrected source artwork, the transform is: any pixel with alpha > 0 and R, G, B all above 175 becomes `(11, 26, 42, alpha)`. Do **not** drop opacity or apply CSS `filter: invert()` instead - invert flips the teal mark too.

**A navy band is a layout choice, not a logo rule.** For a full-width report header you may place the logo on a navy band `#0E1F33` and use the white-wordmark `ig-logo.png` on it. That is a decision about the band: once the background is dark, the table above already tells you which file to use. Do not put a navy rectangle in a slide corner or beside a page number, where it reads as a sticker rather than branding.

---

## Where the logo goes

Place the mark in two slots only: the **cover** and the **footer**.

- **Cover (Dark Navy skin):** white logotype, roughly **38px tall**, bottom-left of the cover-left column (the `.cover-bottom img` slot). It sits beside a thin divider and the "Prepared for" line.
- **Footer (Dark Navy):** white logotype, small - about **18–24px tall** (`.footer img` renders at 24px; the closing-page inline footer logo at 18px). Pair it with the page number on the opposite edge.

**Do not stamp the logo on every content slide.** Repeating it on each page adds visual noise and competes with the slide's one takeaway. Cover plus footer is enough to brand the whole deck - the footer already carries it on every page.

---

## Clear space

Keep padding around the mark on **all sides equal to roughly the cap-height of the logo** (the height of its letterforms). This is the minimum breathing room that stops adjacent text, rules, or chart edges from crowding the mark and reading as part of it. When in doubt, give it more - never less.

The cover and footer slots in the templates already bake in this clearance; if you move the logo, re-check the gap by eye against its own height.

---

## Minimum sizes

Below these, the mark turns muddy in print-to-PDF and the wordmark stops being legible:

- **Footer:** keep the logo **≥ 18px tall**. (The templates use 18–24px - don't go under 18.)
- **Cover:** keep the mark **≥ 120px wide** so the wordmark stays readable at presentation distance. The Dark Navy cover's ~38px-tall logotype clears this comfortably.
- Prefer the `.webp` white logotype on dark when the renderer supports it - it stays crisp at small footer sizes.

---

## Don'ts

Each is one rule, no exceptions:

- Never recolour the **teal mark** - no tinting, no mono fills, no brand-teal "version."
- Never ship artwork that reads "invest game" with a space, or stacks the two halves on separate lines. It is one word.
- Never stretch or distort the aspect ratio - scale width and height together.
- Never rotate the mark.
- Never add a drop-shadow, glow, outline, or any effect.
- Never place it on a busy photo or a low-contrast background - put it on a solid navy, white, or off-white area.
- Never reconstruct or re-typeset the wordmark in another font - use the supplied files.
- Never substitute a logo from outside `assets/logos/`.
