# Content & QA

The judgement rules that travel with every InvestGame data deck. A slide can sit on perfect colours and typography and still fail if the words and numbers are sloppy — these rules keep the *analysis* on-brand, not just the pixels. Each one states the *why*, so you can apply it to a case this file didn't anticipate.

## Contents

- [Titles carry the insight](#titles-carry-the-insight)
- [One source of truth per figure](#one-source-of-truth-per-figure)
- [Layered uniqueness](#layered-uniqueness)
- [Acknowledge data gaps honestly](#acknowledge-data-gaps-honestly)
- [Cover minimalism](#cover-minimalism)
- [Source-line discipline](#source-line-discipline)
- [Typography hierarchy stays consistent](#typography-hierarchy-stays-consistent)
- [Verify load-bearing figures against the source](#verify-load-bearing-figures-against-the-source)
- [Third-party brand caution](#third-party-brand-caution)
- [Pre-export QA checklist](#pre-export-qa-checklist)

---

## Titles carry the insight

Make the title state the conclusion, not the subject. The reader should learn the finding from the title alone; the body just proves it.

- **Before:** "PC hardware overview"
- **After:** "PC gaming runs on budget laptops, not desktops"

The "before" tells the reader what the slide is *about* and makes them dig for the point. The "after" *is* the point. Under the title, a single conclusion line states the so-what — the one sentence the reader should leave with. Why this matters: a deck is skimmed, not read; if the title is a topic, the insight never lands.

## One source of truth per figure

Every number on a slide should resolve to one defensible value. When public sources disagree, average across them and show the range — never silently pick the one you like. Showing the range is honest and pre-empts the "but Newzoo says X" objection.

Label fiscal vs calendar years (**FY** vs **CY**) and state FX assumptions right next to any converted figure. Mixing FY and CY on one axis without labels is a real and common error: a reader compares a vendor's FY2024 against a market CY2024 and silently draws a wrong conclusion. The same applies to currency — a EUR figure converted to USD needs the rate and date inline, or the chart is unauditable.

## Layered uniqueness

The KPI row, table, bullets, and conclusion should each add something the others don't. None restates another. Why: duplication wastes the one screen you get, and a slide that says the same thing four ways signals thin analysis — there was only one idea, padded out. If the conclusion just re-reads the KPI tile, cut one of them or find a second layer of meaning.

## Acknowledge data gaps honestly

Where the public record is thin, say so. "Insufficient public data" beats an invented number every time. A fabricated figure is a credibility landmine: one reader who knows the real number discredits the whole deck. A stated gap, by contrast, reads as rigour and tells the reader exactly how far the analysis goes.

## Cover minimalism

The cover carries only: the title, the date, and one confidentiality line. No version stamps, no "v1.1", no subtitle clutter, no working-draft notes. Why: a clean cover reads as finished and authoritative; version cruft reads as an internal draft that escaped. Keep iteration metadata in the filename or the commit history, not on the page.

## Source-line discipline

Every data slide carries its sources. The skin decides the mechanism:

- **Warm White skin** — footnotes via `.footnotes` with `<sup class="fn">` reference marks tying each claim to its source.
- **Dark Navy skin** — a single source line at the foot of the slide.

A data slide with no source is unauditable and, in practice, untrusted. The source line is not decoration; it is the difference between an assertion and evidence.

## Typography hierarchy stays consistent

Keep the type scale identical across slides of the same kind — same title size, same KPI numeral size, same body size. Jumping sizes between similar slides is the single most common thing that makes a deck look amateur, because the eye reads inconsistency as a mistake. The role-by-role sizes and weights live in **typography.md** — match them rather than eyeballing per slide.

## Verify load-bearing figures against the source

When a number is load-bearing — a headline KPI, a "largest deal of the quarter", a count the whole argument rests on — check it against the original source (the filing, the provider's report, or the InvestGame database entry) rather than a cached aggregate or a secondary write-up, which drift and misattribute. If the slide's credibility hangs on the figure, confirm it at the source.

## Third-party brand caution

Naming an external platform or company as a "partner" needs explicit sign-off. "Partner" is a legal and commercial claim, not a casual description — calling a company a partner when no agreement exists can be both wrong and actionable. Unless a formal partnership is confirmed, describe the external party as a **user** or **customer** of the platform.

## Pre-export QA checklist

Run this top to bottom before exporting any deck. It is copy-pasteable — paste it into the working notes and tick each line.

1. Canvas size matches the skin (Dark Navy 1456×820, Warm White 1280×720; PowerPoint 13.33×7.5 in).
2. One primary visual per slide — a KPI row OR a table OR a chart, never several competing.
3. Every title is an insight, not a topic; the conclusion line states the so-what.
4. Source lines / footnotes present on every data slide.
5. FY vs CY labelled, and FX rate + date stated next to every converted figure.
6. Only on-palette colours — no off-brand hex, no green-for-positive (positive is teal `#00928A`).
7. Correct logo variant for the background — white logotype on dark, colour mark on light.
8. Every Chart.js chart calls `resize()` when its slide becomes visible (or it paints at 0px).
9. Numbers right-aligned, tabular, with consistent decimal places down a column.
10. Layered uniqueness holds — KPI ≠ table ≠ bullets ≠ conclusion; none restates another.
11. Spellcheck and proofread the full copy.
12. Render to PDF and eyeball every page — what looks fine in HTML can clip or reflow on export.
