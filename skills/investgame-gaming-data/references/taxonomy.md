# InvestGame taxonomy - the company vocabulary

The closed vocabulary behind every InvestGame company record: each field, its allowed values and what
each value means. Reformulate a question into these terms and **never invent a category**. If a
concept is outside this vocabulary, say "InvestGame doesn't track that" rather than fabricating a field.

## Contents
1. What counts as gaming · 2. What counts as a deal · 3. Company type · 4. Sector and its fields
5. Monetization · 6. Game genre · 7. Ecosystem segment · 8. Consumer Apps · 9. When to ask the user

---

## 1 · What counts as gaming

**Inside the gaming sectors:** game developers and publishers on any platform, makers of digital
casino games included (genre `CASINO`); companies that serve the games industry (tools,
infrastructure, adtech, esports, streaming, hardware, distribution); and consumer apps built on
visible game mechanics (§8).

**Tracked, but outside the gaming sectors** (sector `OTHER`, "Other (non-covered sector)"):
real-money gambling and betting operators and the platforms they run on, AI companies with no
evidenced gaming connection, and other adjacent companies InvestGame follows. They carry no gaming
fields and are EXCLUDED from gaming sector totals. Their deals stay visible, so they are answerable
when the user asks about them specifically; they never inflate a gaming number. A game with
real-money or skill-based mechanics where players compete against each other is Gaming Content
(feature `CASH_OR_SKILL_BASED_OR_RMG`); an operator that takes bets is sector `OTHER`.

An AI company counts as gaming only on evidence: gaming customers, gaming use, or a gaming-specific
product.

## 2 · What counts as a deal

Tracked once completed or announced: equity rounds (early and late), M&A (control and minority,
carve-outs included), public offerings (listings, PIPEs, secondary offerings, fixed income) and
**non-dilutive financing**. A deal reported only as in talks is a rumour
and carries the label Rumour. A VC or PE fund raise is a fund record, not a deal.
Not tracked: buybacks, partnerships and sponsorships with no capital committed, restructurings with
no new capital, internal reorganisations.
*(Types and categories → `deal-taxonomy.md`; the counting buckets → `definitions.md`.)*

## 3 · Company type (exactly one per company)

| Type | Who |
|------|-----|
| `STRATEGIC_OR_CVC` (label "Strategic") | Any operating company, gaming or not, and a corporate venture arm (through its parent) |
| `VENTURE_CAPITAL_AND_ACC` | Venture capital firms and accelerators |
| `PRIVATE_EQUITY_AND_INST` | Firms investing a balance sheet or a fund: private equity, asset managers, sovereign and pension funds, insurers, family offices, private lenders |
| `SERVICE_PROVIDERS` | Firms that only advise or lend on deals: banks, M&A advisors, brokers, law firms |
| `ANGELS_INDIVIDUALS` | Individuals investing personally |
| `ASSET` | A game title, a franchise or an IP, held under a parent company |
| `OTHER` | Government bodies, non-profits, associations. Visible: do not exclude it from company queries. Not the sector `OTHER` (§4) |

**Advisor is a role, not a type.** A company is an advisor when it advised on at least one deal: read
the role from the deals' advisor fields. A firm that also invests carries an investor type, so a
filter on `SERVICE_PROVIDERS` alone misses it.

**What each type carries:**
- `STRATEGIC_OR_CVC` → sector and the sector's fields (§4).
- `VENTURE_CAPITAL_AND_ACC` and `PRIVATE_EQUITY_AND_INST` → investor specialization (`GENERALIST` /
  `GAMING`), AUM and the named funds the firm has raised (each fund's vintage year and size), so
  "largest gaming funds by AUM" is answerable. No sector fields.
- `ASSET` → its parent company and the sector fields.
- `SERVICE_PROVIDERS` and `ANGELS_INDIVIDUALS` → identity only.

## 4 · Sector (a company can carry several) and its fields

`GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS` · `OTHER`. The first sector listed is the
company's predominant business.

- **GAMING_CONTENT** (develops or publishes games) → `content_type` (`DEVELOPER_1P_PUBLISHER` /
  `PUBLISHER_3P` / `OUTSOURCING_WFH`), `platform`, `monetization_type`, `game_genre`, `top_games`.
  A studio doing game work for other studios (co-development, QA, localisation, art) is
  `OUTSOURCING_WFH`.
- **GAMING_ECOSYSTEM** (serves the games industry and makes no games) → `ecosystem_type` (`B2C` for
  gamers, `B2B` for companies) and `ecosystem_segment` (§7).
- **CONSUMER_APPS** → `gamified_subsegment` (§8).
- **OTHER** → stands alone (never combined with another sector), carries no gaming fields and is
  excluded from gaming totals. It is distinct from the `OTHER` value inside `ecosystem_segment`,
  `gamified_subsegment` or `game_genre`, which sits inside a covered sector.

**Platform:** `MOBILE` · `PC_CONSOLE` · `BROWSER` · `VR_AR`.

**Features** (tags, on any sector): `AI_OR_ML` (sells AI technology or an AI-native product, not a
company that merely uses AI) · `BLOCKCHAIN_OR_WEB3` · `UGC_MODDING` (the product centres on
player-made content or modding) · `CASH_OR_SKILL_BASED_OR_RMG` (real-money or skill-based mechanics
inside a game) · `UA_FINANCING` (a tag on some investors; it is not the list of
UA financing providers: for who provides UA financing, read the investors of the `UA_FINANCING`
deals) · `SHORT_DRAMA` (Consumer
Apps only).
*(Use `BLOCKCHAIN_OR_WEB3` to include or exclude crypto gaming: 2021-22 data is Web3-heavy.)*

## 5 · Monetization (GAMING_CONTENT)

`IAP` (in-app purchases) · `IAA` (ad-supported) · `GAAS` (live service) · `UPFRONT_SALE` (premium,
buy-to-play) · `DLC` (paid expansions) · `SUBSCRIPTION`. The predominant model is listed first; a
second model means a real second revenue line.

Which model applies on which platform: `IAP` and `IAA` on `MOBILE` or `BROWSER`; `GAAS` and `DLC` on
`PC_CONSOLE`, `VR_AR` or `BROWSER`; `SUBSCRIPTION` and `UPFRONT_SALE` on any platform. So a mobile
live-service game is `IAP`, not `GAAS`: to find mobile live-ops studios, filter on `MOBILE` and `IAP`.

## 6 · Game genre (one closed set)

`PUZZLE` (match-3, block/tile, word, hidden-object, physics) · `ARCADE` (hyper-casual, endless runner,
tap/reflex) · `SPORTS_RACING` (football, basketball, cricket, golf, tennis, racing/driving) ·
`TABLETOP` (digital card and board games, CCG, chess, solitaire) · `SHOOTER` (FPS, TPS, battle
royale, tactical/hero) · `STRATEGY_MOBA` (4X, RTS, base building, MOBA, auto-battlers, tower
defense) · `ACTION_RPG` (real-time combat RPG, gacha RPG, dungeon crawlers, hack-and-slash) ·
`SIMULATION_SANDBOX` (life/farm/city sims, management, sandbox, idle, tycoon) · `CASINO` (slots,
poker, roulette, bingo, social casino) · `OTHER` (nothing above fits).

## 7 · Gaming Ecosystem segment

| Segment | What it holds |
|---------|---------------|
| `CREATION_DEVELOPMENT` | helps **build** the game: engines, SDKs, dev tools, middleware, rendering, build pipelines |
| `INFRASTRUCTURE_SERVICES` | helps **run and scale** the business: analytics, monetization and payment platforms, server hosting, cloud gaming, live-ops tooling, agencies that promote a game, market-research and market-data firms |
| `ADTECH` | advertising technology: ad networks, DSPs/SSPs, mediation, user-acquisition tools |
| `DISTRIBUTION_SOCIAL_PLATFORMS` | app stores, portals, launchers, community and social platforms, resellers of game keys, gift cards or in-game currency |
| `ESPORTS` | tournament organisers, leagues, teams, competitive platforms |
| `STREAMING_ENTERTAINMENT` | game livestreaming, gaming video and media |
| `HARDWARE` | peripherals, consoles, controllers, VR/AR headsets, gaming PCs |
| `OTHER` | ecosystem companies fitting nothing above: retail and merchandise, publishers of physical board and card games, gaming SPACs |

`platform` is not `ecosystem_segment`: "mobile" is a platform, "esports" is a segment. UA financing
is not a segment: its providers are the investors of the `UA_FINANCING` deals.

## 8 · Consumer Apps (gamified, non-game B2C)

A consumer app that is not a game but whose experience is built on visible game mechanics: streaks,
levels, leaderboards, badges, virtual currency, challenges. B2B products, gambling apps and pure
games are not Consumer Apps.

Subsegment, by primary purpose: `EDTECH` · `FITNESS_WELLNESS` · `ENTERTAINMENT_SOCIAL` (short drama
carries the `SHORT_DRAMA` tag) · `FINTECH` · `OTHER`.

## 9 · When to ask the user

Confirm the reading before querying when the user says "mobile" (mobile-only or any company with a
mobile presence), "the West" or "Europe" (which country set: the hub's region maps), "funds" (VC/PE
firms or the funds they raised), hyper-casual versus casual, or any term outside this vocabulary.
State your reading in one line and offer to widen it; never silently pick a scope.
