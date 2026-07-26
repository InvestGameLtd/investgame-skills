# Output format & InvestGame brand

How every answer should look so it reads as InvestGame, not as a raw database dump.

## Answer structure
1. **Lead with the answer** in one sentence, then the supporting table/ranking. One primary object
   per answer - a table OR a ranking OR a profile, not three competing for attention.
2. **Default columns by query type** (mirror the InvestGame web app):

| Query type | Columns |
|------------|---------|
| Deal list | target · country · deal type · size USD · date · lead investor *(+ EV & EV/Revenue for M&A)* |
| Investor / acquirer ranking | name · distinct deal count · total disclosed USD |
| Company profile | each round (type · size · date · investors) · disclosed valuation/EV · 1-line summary |
| Trend | period · count · total value USD *(chart-friendly)* |

3. **Always append a methodology line** - period, geography, included/excluded. Example:
   *"M&A = category MA; mobile = MOBILE platform; sizes USD m, undisclosed excluded from totals;
   last 18 months by announcement date."*
4. **Flag gaps, never fill them:** "undisclosed", "n/d", "insufficient public data". Never invent a figure.
5. **Numbers tabular, right-aligned, USD millions** unless asked otherwise. Link entities to their
   InvestGame pages when the tool returns URLs.

## Brand - when the user wants a report, chart, or one-pager

Two themes, **never mixed in one artifact**:
- **Warm White** - bg `#F4F3EE`, fonts Space Grotesk (display) / Inter (body) / JetBrains Mono
  (numbers). For data-dense market reports, tables, methodology-heavy analysis.
- **Dark Navy** - bg `#0E1F33`, Helvetica Neue. For bold/editorial decks and recaps.

Colour:
- **Brand teal `#61BFB3`** is the InvestGame colour (accents/highlights in both themes).
- **Positive movement = teal `#00928A`, never green.** **Caution = rust `#C07B5A`, used sparingly.**
  InvestGame decks are not red/green dashboards.
- Secondary series: blue `#6189D6`, then deep teal/blue.

Layout discipline:
- One idea per slide; the **title carries the insight**, not the topic ("Mobile M&A multiples
  compressed to ~2.8x", not "Multiples overview").
- Charts: **bar/column by default**, interactive on screen, palette teal → blue → deep teal.
- Whitespace over clutter; align to a grid; the InvestGame logo present; **every data slide cites a source line.**

(When generating HTML/PDF or PowerPoint artifacts, the bundled InvestGame brand templates encode all
of the above - copy a template and replace content in place rather than building from blank.)
