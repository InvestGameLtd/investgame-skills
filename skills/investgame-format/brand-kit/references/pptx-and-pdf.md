# PPTX & PDF - output paths

InvestGame ships decks two ways. Most work is **HTML → PDF**; PowerPoint is for when the recipient genuinely needs an editable `.pptx`. Pick the path first, because they share almost no mechanics.

## Contents

- [Path 1 - HTML → PDF (default)](#path-1--html--pdf-default)
- [Path 2 - PowerPoint](#path-2--powerpoint)
- [Related references](#related-references)

---

## Path 1 - HTML → PDF (default)

The bundled templates already do the hard part. Both `assets/templates/dark-navy.html` and `assets/templates/warm-white.html` set their `@page` size and a print stylesheet, so rendering is just "honour the CSS page size" - no per-export sizing flags to fiddle with.

| Skin | `@page` size |
|------|--------------|
| Dark Navy | `1456px × 820px` |
| Warm White | `1280px × 720px` |

**Render with the bundled script:**

```bash
python scripts/render_pdf.py input.html [output.pdf]
```

It tries two backends in order and uses whichever is available:

1. **Playwright** - best fidelity. It emulates `print` media (so the print stylesheet applies) and renders with `preferCSSPageSize` so the PDF page equals the slide canvas.
2. **Headless Chrome / Chromium** - fallback via `--print-to-pdf`.

Charts need a moment to paint before the page is captured - the script waits for that, so Chart.js canvases aren't snapshotted blank. If neither backend is present, install one:

```bash
pip install playwright && playwright install chromium
```

…or have Google Chrome / Chromium on the machine. Either satisfies the renderer.

Because Playwright emulates print media, anything you put behind `@media print` in the template (hiding nav chrome, forcing backgrounds) takes effect only in the PDF - preview in a browser will look slightly different from the export, which is expected. Always eyeball the rendered PDF, not just the HTML.

### Multi-page A4 documents (reports, not slides)

`render_pdf.py` is tuned for full-bleed 16:9 **slides**: it sets `@page { margin: 0 }` and `preferCSSPageSize`, so it ignores any CSS `@page { margin }` you set for a flowing multi-page document. The result is that the last block jams against the physical page bottom and a `position: fixed` footer overlaps the content.

For an A4 **report** (notes, methodology write-ups, anything that flows across pages), bypass the slide path:

- Set CSS `@page { size: A4; margin: 0 }` and drop any fixed or repeating footer (use a one-off footer at the end of the flow instead).
- Render with explicit margins and **without** `preferCSSPageSize`:

  ```python
  page.pdf(format="A4", print_background=True,
           margin={"top": "12mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
  ```

- QA every page image: `pdftoppm -jpeg -r 120 out.pdf qa`, then look at each one.

### Font fidelity in the PDF

Web fonts pulled through the template's Google Fonts `<link>` are fine. But if a deliverable uses a **locally installed or proprietary face**, Chromium will not match it by display name, so a bare `font-family: "Some Face"` silently falls back (old-style "bouncing" figures are the tell that it happened).

- Wire each local face through `@font-face { src: local("Full Name"), local("PostScript-Name") }` with a `font-weight` **range**, so Chromium never synthesises a faux-bold.
- Render with real Chrome (`chromium.launch({ channel: 'chrome' })` sees system fonts), `await document.fonts.ready` before `page.pdf()`, and **redraw Chart.js canvases on `document.fonts.ready`** (a canvas cannot use a font that loaded after it painted).
- Verify the embedded faces with `pdffonts out.pdf` before sending.

---

## Path 2 - PowerPoint

The philosophy is the same as the HTML templates: **prefer copying and adapting an existing on-brand `.pptx` and editing it in place over building from a blank deck.** Blank decks drift off-brand - PowerPoint's defaults pull in the wrong fonts, the wrong chart colours, and the wrong slide size, and you spend more time correcting drift than you saved.

**Never edit an existing hand-maintained or client master deck in place.** When asked to add or develop slides for a deck the team owns and assembles by hand, build the new or option slides in a **separate** `.pptx` (e.g. `…/new-slides/<deck>_NEW-SLIDES.pptx`) and leave the master untouched: generated slides are drafts the owner slots in themselves. "Editing in place" above means a **brand template you copied**, not someone's working master.

**Steps:**

1. **Set the slide size to 13.33 × 7.5 in (16:9) first.** Do this before adding any content - placeholder positions and safe-zones assume it, and resizing a populated deck reflows everything.
2. **Use the `example-skills:pptx` skill for the mechanics** - the unpack → edit slide XML → clean → pack workflow. That skill owns the file-surgery details; this file owns the brand decisions layered on top.
3. **Pull colours and fonts from `assets/ig_helpers.py`:**
   - The `IG`, `IG_DARK`, and `IG_WHITE` dicts hold the named hex values - refer to them by name, never retype hex.
   - `hex_to_rgbcolor()` converts a bare 6-char hex into the tuple python-pptx's `RGBColor(*...)` wants.
   - For pptxgenjs, pass the **bare 6-character hex** string directly (no leading `#`).
4. **Set chart series colours manually from `CHART_COLORS`** - apply them 1..n in sequence. Never let PowerPoint auto-assign chart colours; its palette is off-brand and will reorder series on edit.
5. **Apply fonts with the fallbacks from typography.md** - the Warm White fonts (Space Grotesk / Inter / JetBrains Mono) aren't installed everywhere, so the PowerPoint fallbacks listed there keep the deck readable on a stock machine.

The two skins map to two PPTX looks: a **dark master** for the Dark Navy skin and a **light master** for the Warm White skin. Build each on its own master rather than recolouring one into the other.

**To export a PPTX to PDF**, use the `example-skills:pptx` skill's tooling (LibreOffice / `soffice` headless conversion) - don't round-trip through the HTML renderer, which only knows the HTML templates.

---

## Related references

- **charts.md** - chart-type map, Chart.js and PowerPoint chart recipes, palette order.
- **colors.md** - full palette, named tokens, decision trees.
- **typography.md** - font roles, sizes, weights, and the PowerPoint fallbacks referenced above.
