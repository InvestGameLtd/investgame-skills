# InvestGame Taxonomy - company classification rules

The closed vocabulary and the decision rules behind every InvestGame company record. The agent
reformulates questions into these terms and **never invents categories**. If a concept is outside this
taxonomy, say "InvestGame doesn't track that" rather than fabricating a field.

*Grounded in InvestGame's analyst classification rules: this is the authoritative term set behind
every InvestGame company record.*

## Contents
1. Gaming-inclusion test · 2. Deal-inclusion gate · 3. Company type · 4. Sector & gated fields · 5. Monetization × platform
6. Game genre · 7. Ecosystem segment · 8. Consumer Apps · 9. Region maps · 10. "Ask the user" triggers

---

## 1 · Gaming-inclusion test (is the target even "gaming"?)

**In scope:** game developers & publishers (any platform), physical board and card games and their
publishers included; casino **games** (genre `CASINO`); skill-based cash-out games and real-money
fantasy sports; esports orgs and gaming infrastructure/tools/adtech with a genuine gaming use-case;
sports data, sports media and fan-engagement technology, even when betting brands are among their
clients or advertisers; B2C non-game apps with real game mechanics (Consumer Apps - §7). A mixed
business (a media group with a games arm, an agency with a gaming division) is in when the gaming
part is material: the division decides, not the parent's label.

**Out of the gaming sectors:** real-money gambling / iGaming **operators** and the **apparatus** they run on (casino / sportsbook / iLottery platforms, remote game servers, betting terminals, lottery systems); physical toys other than board and card games, and merchandise
(unless licensed game IP); generic PR / brand / marketing that is **not games-specific** and merely
counts game companies among its clients; adjacent tech with no gaming use-case.

These are still TRACKED companies: they carry the sector `OTHER` ("Other (non-covered sector)") with
no gaming-gated fields, and several are listed companies whose earnings InvestGame follows. They are
EXCLUDED from gaming sector totals, and their own transactions are not tracked as deals - so they are
answerable as companies, but they never inflate a gaming number.

**Three service categories that fall between those rules**, none of which makes games of its own.
That decides their SECTOR, not whether they are in scope: a company whose customers are game
companies and whose output is game work is an outsourcing gaming business, and it is IN.

- **Infrastructure, backend, tooling and engines** - game-server hosting and orchestration,
  matchmaking, build pipelines, SDKs, engine vendors. The gaming use-case is exclusive and real, but
  the company makes no games: `GAMING_ECOSYSTEM`, never `GAMING_CONTENT`.
- **Gaming-specialised creative and marketing studios** - trailer houses, key art, cinematics and
  in-engine production, influencer and events agencies working for publishers. IN as
  `GAMING_CONTENT` / `OUTSOURCING_WFH`: being gaming-only is what puts a studio in scope, not what
  keeps it out.
- **Film and TV services vendors** - VFX, animation, virtual production, motion capture. Often
  outsourcing for games too, so they need **confirmation**: named game titles worked on, or games
  named among the services or sectors served. Confirmed, they are IN as `GAMING_CONTENT` /
  `OUTSOURCING_WFH` however large the film business beside them; unconfirmed, empty sector.

The line analysts apply most: **a casino game is content; a casino operator, and the apparatus it
runs on, are out of the gaming sectors** - tracked, but under sector `OTHER`. A studio that *makes*
casino games is Gaming Content even when those games pay out real money and its customers are
operators, because it produces games rather than taking wagers (Light & Wonder, Microgaming).
Aristocrat is out: it divested its games business and now sells casino machines. A company that
supplies the machinery of wagering - casino / sportsbook / iLottery platforms, remote game servers,
betting terminals, VLT and retail lottery systems - is `OTHER` alongside the operator, and that line
prevails: a company that sells the platform and also makes casino games for it is `OTHER`. Whose
games the machinery runs decides it: terminals, cabinets or a game server that carry only the
studio's own titles are how it delivers its games, and it stays Gaming Content. A skill-based mobile
game that pays cash out to players (Skillz, Papaya, Avia Games, Mobile Premier League) and a
real-money fantasy sports app (Underdog) are Gaming Content with `CASH_OR_SKILL_BASED_OR_RMG`; only
sports betting is out. Sports data, sports media and fan-engagement technology (Genius Sports,
Sportradar) are in even when betting brands are among their clients or advertisers: only the
operator that takes the bets is out. A gambling-side company never carries `GAMING_ECOSYSTEM`: those
segments describe services sold to the games industry, not to gambling operators.

**AI and ML companies.** AI is horizontal, so "uses AI" or "could be used for games" is not enough.
A company is **IN** when gaming or interactive media is a real market it serves **and there is
evidence of that connection**: gaming is a declared market with a real product; the product is sold
into game-making (assets, audio, dev tools, SDKs, engines, distribution); or the output is itself
game or playable content. The served market decides it, not the media type: a generative video or
audio tool marketed to game studios is in, while the same technology sold only to film or advertising
creators is out. Evidence means gaming customers, gaming use, or a gaming-specific product - not a
TAM line, a single logo, a gaming investor on the cap table, or training data. Without it the company
is generic AI: tracked under sector `OTHER`, outside every gaming sector. Borderline cases are
editorial decisions, made case by case.

## 2 · Deal-inclusion gate (is it a tracked deal?)

Tracked: equity rounds (early & late), M&A (control & minority, carve-outs included), public
offerings (IPOs/listings, PIPEs, secondary offerings, fixed income), and **non-dilutive financing**
(the `UA_FINANCING` category, label "Non-dilutive Financing": UA financing, private debt and project
financing - its own first-class visible deal category, counted in general analytics but not as
funding raised; it is neither fundraising nor M&A, so it never sat inside those buckets). A VC/PE
fund raise is recorded on the fund, not as a deal. Not tracked: buybacks, partnerships, sponsorships,
restructurings with no new capital, internal reorganisations. `OTHER_MISC` is hidden from the data entirely and is not
queryable; project financing is a visible non-dilutive type and Licensing no longer exists.
*(Full deal classification → `deal-taxonomy.md`.)*

## 3 · Company type (pick exactly one)

| Type | When | Key rule |
|------|------|----------|
| `STRATEGIC_OR_CVC` | Operating companies, corporates, corporate-VC arms | **Default for a gaming company.** A CVC arm (e.g. "Sony Interactive Ventures") is classified via its **parent** → STRATEGIC. |
| `VENTURE_CAPITAL_AND_ACC` | VC firms, accelerators | name has "Ventures/Capital/Partners" + fund structure |
| `PRIVATE_EQUITY_AND_INST` | PE firms, sovereign wealth, pension, family offices | |
| `SERVICE_PROVIDERS` | Banks, advisory, law, accounting firms, gaming research/consulting/market-analysis firms selling insight AS A SERVICE to industry clients | participate as **advisors**, not targets/investors. Not a gaming news/press/video media business monetizing an audience - that's `STRATEGIC_OR_CVC` + `GAMING_ECOSYSTEM`/`STREAMING_ENTERTAINMENT` (§6), any format |
| `ANGELS_INDIVIDUALS` | Individuals investing personally (not via a fund) | |
| `ASSET` | A game title / franchise / division sold as an asset | **requires a parent company** |
| `OTHER` | Government, non-profit, unclassifiable | visible - do **not** exclude from company queries. Not for a research/consulting/advisory firm either - selling insight for a fee is operating a business, so it is `SERVICE_PROVIDERS` (a gaming news/press/video media business is `STRATEGIC_OR_CVC` instead - see §4) |

**Field applicability (what each type carries):**
- `STRATEGIC_OR_CVC` → sector + sector-gated fields (below); never investor fields.
- `VC`/`PE` → investor specialization (`GENERALIST`/`GAMING`) + AUM, plus the **named funds** the firm
  has raised (each fund's vintage year and size/AUM - so "largest gaming funds by AUM" is answerable);
  **never** sector/content fields.
- `SERVICE_PROVIDERS` → identity only; no sector/investor fields.
- `ASSET` → parent company + sectors + the sector bundle (platform, monetization, genre, top games;
  ecosystem segment), never content type or ecosystem type, which the parent carries; no
  company-identity fields.
- `ANGELS_INDIVIDUALS` → identity only.

## 4 · Sector (a company can carry several) and its gated fields

`GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS` · `OTHER`. Sector gates which fields are populated.
**The list is ordered: the first sector is the predominant business** (the quarterly series reads
it), and each listed sector is a material line of business with its own product or revenue. Up to three.

`OTHER` = "Other (non-covered sector)": a company InvestGame tracks that sits outside every covered
sector (a real-money gambling operator, a large non-gaming AI or hardware firm). It is **exclusive**
(never combined with another sector), carries **no** gaming-gated fields, and is excluded from gaming
sector totals. Distinct from `gamified_subsegment.OTHER` and `ecosystem_segment.OTHER`, which are
filler values INSIDE a covered sector.
**Features** (six values): `AI_OR_ML` · `BLOCKCHAIN_OR_WEB3` · `UGC_MODDING` · `CASH_OR_SKILL_BASED_OR_RMG` · `UA_FINANCING` are sector-agnostic (any sector). `SHORT_DRAMA` is the exception - short drama is a Consumer Apps content vertical, so it applies only to companies whose sectors include `CONSUMER_APPS`.

`UA_FINANCING` as a **feature** marks an investor that provides non-dilutive user-acquisition capital; it is an investor-role tag, not an attribute of a studio's product. It is distinct from the `UA_FINANCING` **deal type and deal category** (`deal-taxonomy.md`). To find UA-financing providers, filter companies on this feature rather than counting deals.
*(Use `BLOCKCHAIN_OR_WEB3` to include/exclude crypto-gaming - 2021–22 data is Web3-heavy.)*

What each feature flag means (it tags a product capability, NOT a company category):
- `AI_OR_ML` - the product uses AI/ML *inside the game or tooling*. **It does NOT mean "an AI-focused company"**: it is a capability flag and also catches large publishers using AI internally. To build the "AI in gaming" set, first apply the gaming-inclusion AI gate (§1: gaming must be a real market the company serves, with evidence of that connection), then read `AI_OR_ML` as the in-set capability flag, not as the inclusion filter on its own.
- `UGC_MODDING` - the product centres on user-generated content or modding (creation/sharing by players).
- `CASH_OR_SKILL_BASED_OR_RMG` - real-money or skill-based wagering mechanics *inside a game*; this tags content, it is not the casino-operator exclusion (see §1).

- **GAMING_CONTENT** → `content_type` (`DEVELOPER_1P_PUBLISHER` / `PUBLISHER_3P` / `OUTSOURCING_WFH`),
  plus `platform`, `monetization_type`, `game_genre`, `top_games` (the last three not required for
  pure outsourcing).
- **GAMING_ECOSYSTEM** → `ecosystem_type` (`B2C`/`B2B`) + `ecosystem_segment` (§6). Includes a company
  selling gaming-licensed merchandise, apparel or physical goods, or reselling game keys, e-pins,
  gift cards or in-game currency, that does not develop games itself
  (`ecosystem_segment = OTHER`, "retail/merch") - it is never `GAMING_CONTENT`, which requires the
  company to actually develop or publish a game.
- **CONSUMER_APPS** → `gamified_subsegment` + visible game mechanics (§7).
- **platform:** `MOBILE` · `PC_CONSOLE` (incl. cloud gaming) · `BROWSER` · `VR_AR`.

## 5 · Monetization × platform - the decision rules (analyst-critical)

**List the predominant model first.** Without a disclosed split, exactly one model, read from the
signals below; a second model only when a disclosed share gives it 30% or more of revenue, or the
source says "hybrid" in so many words. A game monetised mainly through purchases with ads as a small part carries `IAP` alone, and
the reverse carries `IAA` alone.

**Allowed values:** `IAP` · `IAA` · `GAAS` · `UPFRONT_SALE` · `DLC` · `SUBSCRIPTION`.

**The platform matrix decides what is applicable** (every InvestGame record follows it): `IAP` and `IAA` need
`MOBILE` or `BROWSER`; `GAAS` and `DLC` need `PC_CONSOLE`, `VR_AR` or `BROWSER`; `SUBSCRIPTION` and
`UPFRONT_SALE` apply on any platform (a paid mobile download with no purchases and no ads is
`UPFRONT_SALE` on `MOBILE`, rare and verified, never assumed).

| Signal in the source | Model |
|---|---|
| Disclosed revenue split | the largest share first; a second only at 30% or more |
| "hybrid-casual" / "hybrid monetization": ads and purchases roughly equal | `IAA` and `IAP`, the larger first |
| hyper-casual, short sessions, ad-driven, install-led (CPI) scaling | `IAA` alone |
| progression economy: gacha, meta-progression, collection, a mobile battle pass; rewarded ads a small part | `IAP` alone |
| ad-led portfolio with a small purchase store | `IAA` alone |
| mobile, no signal at all | `IAP` |
| paid download, no service economy (Early Access included) | `UPFRONT_SALE` |
| paid expansions or add-ons after launch | add `DLC` |
| battle pass, seasons, a recurring cosmetic store after launch | `GAAS`, with `UPFRONT_SALE` when the base game is paid |
| a monthly fee for access | `SUBSCRIPTION` |
| cross-platform | read by the platform where the revenue is |

Premium, `DLC` and `GAAS` on PC and console are three separate questions, each answered by its own
signal. Mobile live operations, seasonal content and a mobile battle pass are `IAP`, never `GAAS`;
`GAAS` on a mobile entry applies only when the title is a cross-platform live service whose
platform set includes `PC_CONSOLE`.

### Time rule
- Classify monetization **as of the deal announcement date**, not the company's current model.

## 6 · Game genre (one closed set)

`PUZZLE` (match-3, block/tile, word, hidden-object, physics) · `ARCADE` (hyper-casual, endless runner,
tap/reflex, arcade clones) · `SPORTS_RACING` (football/basketball/cricket/golf/tennis, racing/driving) ·
`TABLETOP` (card, board, CCG, poker, chess, solitaire) · `SHOOTER` (FPS, TPS, battle royale,
tactical/hero) · `STRATEGY_MOBA` (4X, RTS, city/base building, MOBA, auto-battlers, tower defense) ·
`ACTION_RPG` (real-time combat RPG, gacha RPG, dungeon crawlers, hack-and-slash) · `SIMULATION_SANDBOX`
(life/farm/city sims, management, sandbox, idle, tycoon) · `CASINO` (slots, poker, roulette, bingo,
social casino) · `OTHER` (only when nothing above fits - never combine `OTHER` with a named genre).

## 7 · Gaming Ecosystem segment (build vs operate)

The deciding test for the top two is **build vs operate.**

| Segment | Core question | Includes / examples |
|---------|---------------|---------------------|
| `CREATION_DEVELOPMENT` | Does it help **build** the game? | engines, SDKs, dev tools, middleware, co-dev, QA, localisation, art outsourcing, backend SDKs, rendering, build pipelines (Unity, Incredibuild, Parsec, Helpshift) |
| `INFRASTRUCTURE_SERVICES` | Does it help **run / scale** the business? | analytics, LTV/monetization tooling, **UA financing**, cohort forecasting, server hosting, cloud live-ops, monetization platforms (GameAnalytics, Overwolf, Multiplay, Xsolla) |
| `ADTECH` | Is the core product advertising tech? | ad networks, DSPs/SSPs, mediation, programmatic (AppLovin, ironSource, Adjust) |
| `DISTRIBUTION_SOCIAL_PLATFORMS` | - | app stores, portals, launchers, community/social (Steam, Epic Store, Discord) |
| `ESPORTS` | - | tournament organisers, leagues, team orgs, competitive infra |
| `STREAMING_ENTERTAINMENT` | - | game streaming, cloud gaming, gaming video platforms (Twitch, YouTube Gaming) |
| `HARDWARE` | - | peripherals, consoles, controllers, VR/AR headsets, gaming PCs |
| `OTHER` | - | ecosystem firms fitting nothing above (retail/merch) |

`ecosystem_type` = `B2C` (gamers) or `B2B` (companies). *(Note: to find UA-financing **providers**,
filter on the company feature `UA_FINANCING` (§4). It is valid on VC, PE and Strategic/CVC companies,
so the ecosystem segment alone undercounts the roster. UA-financing **deals** sit in the visible
Non-dilutive Financing category with private debt and project financing, counted in general analytics
but not as funding raised.)*

## 8 · Consumer Apps (gamified, non-game B2C)

**Qualifies only if ALL hold:** B2C (not B2B/enterprise); not a game (no core gameplay loop as the
product); the user-facing experience is built on **visible gamification mechanics** (streaks,
levels/XP, leaderboards, progress bars, badges, IAP progression, virtual currency, challenges).

**Exclusions:** B2B/enterprise (e.g. Wellhub), gambling/betting apps, pure games (→ `GAMING_CONTENT`),
apps whose mechanics the user never sees.

**Subsegment (by primary purpose):** `EDTECH` (Duolingo, Kahoot!) · `FITNESS_WELLNESS` (Strava, Calm,
Zwift) · `ENTERTAINMENT_SOCIAL` (Reddit, Wattpad, short-drama / mini-drama carrying the `SHORT_DRAMA` tag) · `OTHER` (Habitica).

## 9 · Region maps (use the country lists, not granular sub-regions)
- **Europe:** GB DE FR SE NO DK FI CH NL BE AT IT ES PT PL IE CZ RO
- **Asia/APAC:** JP KR CN SG AU NZ IN TW HK TH ID VN MY PH
- **North America:** US CA · **LATAM:** BR MX AR CO CL PE
- **MENA (gaming hubs):** SA AE JO EG · **Turkey (TR):** its own hub, usually paired with MENA.

## 10 · "Ask the user" triggers (the safe-buffer)
Confirm the reading before querying when the user says: "recent" (→ 18 months), "mobile" (pure vs
mixed portfolio), "the West"/"Europe" (which country set), "funds" (VC/PE firms vs fund-vehicle raises),
hyper-casual vs casual, or any term outside this taxonomy. State your reading in one line and offer to
widen it - never silently pick a scope. Known contradictions needing a human tie-break: AdTech players
that carry a separate non-InvestGame taxonomy.
