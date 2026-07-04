# Logos

How to place the InvestGame mark on either skin. For where layouts put the cover and footer slots, see `references/layouts.md`. For the colour tokens named below, see `references/colors.md`.

## Contents

- [The real logo files](#the-real-logo-files)
- [Which mark on which background — and why](#which-mark-on-which-background--and-why)
- [Where the logo goes](#where-the-logo-goes)
- [Clear space](#clear-space)
- [Minimum sizes](#minimum-sizes)
- [Don'ts](#donts)

---

## The real logo files

The shipped artwork lives in `assets/logos/`. There are only four files; everything below uses one of them.

| File | What it is | Use on |
|------|------------|--------|
| `ig-logo.png` | Full-colour InvestGame mark | LIGHT backgrounds |
| `ig-logo-336x88.png` | Horizontal full-colour lockup, 336×88 | LIGHT backgrounds where a wide mark fits (covers, wide footers) |
| `ig-logotype-white.png` | White logotype (raster) | DARK backgrounds |
| `ig-logotype-white.webp` | White logotype (smaller `.webp`) | DARK backgrounds — prefer when the renderer supports WebP; smaller file, same artwork |

The templates reference these by relative path — e.g. `assets/templates/dark-navy.html` loads `../logos/ig-logotype-white.png` on its dark cover and footer. Keep that path when you copy a template; don't inline a different logo.

---

## Which mark on which background — and why

The rule is contrast, not preference:

- **Dark page (navy `#0E1F33`, or any dark panel) → white logotype** (`ig-logotype-white.png` / `.webp`). The full-colour mark loses its edges on navy; the white logotype reads cleanly.
- **Light page (white, or warm off-white `#F4F3EE`) → colour mark** (`ig-logo.png`, or the wide `ig-logo-336x88.png` lockup where a horizontal mark fits). The white logotype would vanish on light.

Both skins carry the logo as an image — the difference is which file the background calls for. The **Dark Navy** skin uses the **white logotype** (`ig-logotype-white.png`) on its dark cover and footer. The **Warm White** skin uses the **full-colour logo** (`ig-logo.png`) on its warm cover and as a small colour mark on content slides — the warm/white background needs the colour mark, never the white one, which would vanish on light. See the cover anatomy in `references/layouts.md`.

---

## Where the logo goes

Place the mark in two slots only: the **cover** and the **footer**.

- **Cover (Dark Navy skin):** white logotype, roughly **38px tall**, bottom-left of the cover-left column (the `.cover-bottom img` slot). It sits beside a thin divider and the "Prepared for" line.
- **Footer (Dark Navy):** white logotype, small — about **18–24px tall** (`.footer img` renders at 24px; the closing-page inline footer logo at 18px). Pair it with the page number on the opposite edge.

**Do not stamp the logo on every content slide.** Repeating it on each page adds visual noise and competes with the slide's one takeaway. Cover plus footer is enough to brand the whole deck — the footer already carries it on every page.

---

## Clear space

Keep padding around the mark on **all sides equal to roughly the cap-height of the logo** (the height of its letterforms). This is the minimum breathing room that stops adjacent text, rules, or chart edges from crowding the mark and reading as part of it. When in doubt, give it more — never less.

The cover and footer slots in the templates already bake in this clearance; if you move the logo, re-check the gap by eye against its own height.

---

## Minimum sizes

Below these, the mark turns muddy in print-to-PDF and the wordmark stops being legible:

- **Footer:** keep the logo **≥ 18px tall**. (The templates use 18–24px — don't go under 18.)
- **Cover:** keep the mark **≥ 120px wide** so the wordmark stays readable at presentation distance. The Dark Navy cover's ~38px-tall logotype clears this comfortably.
- Prefer the `.webp` white logotype on dark when the renderer supports it — it stays crisp at small footer sizes.

---

## Don'ts

Each is one rule, no exceptions:

- Never recolour the mark — no tinting, no mono fills, no brand-teal "version."
- Never stretch or distort the aspect ratio — scale width and height together.
- Never rotate the mark.
- Never add a drop-shadow, glow, outline, or any effect.
- Never place it on a busy photo or a low-contrast background — put it on a solid navy, white, or off-white area.
- Never reconstruct or re-typeset the wordmark in another font — use the supplied files.
- Never substitute a logo from outside `assets/logos/`.
