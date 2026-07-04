# Press sources — the curated corpus

The gaming-press corpus `InvestGame_press_query` reads. Filter by source name or slug
("only Naavik", "just Mobile Dev Memo and Game File"). Podcasts are show-notes-only: down-weight
them and never let one lead a Big Story alone.

> The LIVE roster is whatever `live_media_source` has `is_active = true` — query the table for the
> current set. The lists below are orientation, not an exhaustive registry.

## Text newsletters / blogs (lead-worthy)

| Source | Typical focus |
|--------|---------------|
| Naavik | Business breakdowns, M&A, mobile, live-ops |
| Mobile Ad Revenue | Mobile ad revenue, UA economics, ad monetization |
| The Game Business | Industry news, layoffs, M&A, exec moves |
| Game File | Industry journalism, labor, policy |
| GameDiscoverCo | Discovery, storefronts, platform, wishlists |
| Deconstructor of Fun | Game-economy design, live-ops, monetization |
| SuperJoost | Strategy, market structure |
| MIDiA Research | Market data, trends, consumer |
| Griffin Gaming Partners (and other VC weeklies) | VC, funding, market data, AI, web3 |
| GameDev Reports · Game Makers · Alinea Analytics · Niko News · others | Analyst / data + dev |
| InvestGame (own) | Our own deal / market commentary |

## Podcasts (show-notes only — down-weight, never lead)

The Game Business Show · Gamecraft · Two & a Half Gamers · Naavik Gaming Podcast ·
Deconstructor of Fun Podcast · Mobile Dev Memo Podcast.

These carry show notes, not transcripts. Use them to corroborate a story or in the Wire, never as
the sole source of a Big Story. They are flagged `live_media_source.is_podcast = true`.

## How to name a source in a query

- Exact slug: `live_media_source.slug = 'naavik'`.
- Fuzzy name: `live_media_source.name ILIKE '%mobile dev memo%'`.
- Exclude podcasts: add `WHERE s.is_podcast = false`.
