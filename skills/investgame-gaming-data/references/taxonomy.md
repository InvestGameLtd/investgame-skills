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
publishers included (as `GAMING_ECOSYSTEM`, B2C, segment `OTHER`, never `GAMING_CONTENT`); digital casino **games** (genre `CASINO`); skill-based cash-out
games; esports orgs and gaming infrastructure/tools/adtech with a genuine gaming use-case;
sports data and sports media, even when betting brands are among their clients or advertisers;
fan-engagement technology when gaming or esports is a material line of it (a horizontal platform with
games as one vertical among several is out); B2C non-game apps with real game mechanics (Consumer
Apps - §8). A mixed business (a media group with a games arm, an agency with a gaming division) is in
when the gaming part is material: the division decides, not the parent's label.

**Out of the gaming sectors:** real-money gambling / iGaming **operators**, including any company that takes bets whatever it calls the product (real-money fantasy sports, daily, season-long or pick'em, such as Underdog and PrizePicks), betting affiliates and betting media paid for sending players to operators, and the **apparatus** operators run on (casino / sportsbook / iLottery platforms, remote game servers, betting terminals, lottery systems, casino-floor hardware); physical toys other than board and card games, and merchandise
(unless licensed game IP); generic PR / brand / marketing that is **not games-specific** and merely
counts game companies among its clients; adjacent tech with no gaming use-case.

These are still TRACKED companies: they carry the sector `OTHER` ("Other (non-covered sector)") with
no gaming-gated fields, and several are listed companies whose earnings InvestGame follows. They are
EXCLUDED from gaming sector totals; their deals stay tracked and visible, and the quarterly report
leaves them out - so they are answerable, but they never inflate a gaming number.

**Three service categories that fall between those rules**, none of which makes games of its own.
That decides their SECTOR, not whether they are in scope: a company whose customers are game
companies and whose output is game work is an outsourcing gaming business, and it is IN.

- **Infrastructure, backend, tooling and engines** - game-server hosting and orchestration,
  matchmaking, build pipelines, SDKs, engine vendors. The gaming use-case is exclusive and real, but
  the company makes no games: `GAMING_ECOSYSTEM`, never `GAMING_CONTENT`.
- **Creative, marketing, influencer and events agencies working on games** - split by what they
  deliver: work that is part of the game is `GAMING_CONTENT` / `OUTSOURCING_WFH`; work that promotes
  or sells a game (trailers, key art, influencer and events campaigns) is `GAMING_ECOSYSTEM`, B2B or
  B2C by its customer, segment `INFRASTRUCTURE_SERVICES`.
- **Film and TV services vendors** - VFX, animation, virtual production, motion capture. Often
  outsourcing for games too, so they need **confirmation**: named game titles worked on, or games
  named among the services or sectors served. Confirmed, they are IN as `GAMING_CONTENT` /
  `OUTSOURCING_WFH` however large the film business beside them; unconfirmed, empty sector.

The line analysts apply most: **a digital casino game is content; a casino operator, and the
apparatus it runs on, are out of the gaming sectors** - tracked, but under sector `OTHER`. A studio
that *makes* digital casino games is Gaming Content even when those games pay out real money and its
customers are operators, because it produces games rather than taking wagers (Light & Wonder,
Microgaming, and Aristocrat through its digital and social casino publishing). White Hat, a
real-money casino studio, is out by name; the casino-game makers are revisited together. A company
that supplies the machinery of wagering - casino / sportsbook / iLottery platforms, remote game
servers, betting terminals, VLT and retail lottery systems - is `OTHER` alongside the operator, and
that line prevails: a company that sells the platform and also makes casino games for it is `OTHER`,
and so is a maker of casino-floor hardware with no digital titles (slot cabinets, table products,
shufflers: PlayAGS). Whose games the machinery runs decides it: terminals, cabinets or a game server that carry
only the studio's own digital titles are how it delivers its games, and it stays Gaming Content. A
skill-based mobile game that pays cash out to players (Skillz, Papaya, Avia Games, Mobile Premier
League) is Gaming Content with `CASH_OR_SKILL_BASED_OR_RMG`. A gambling-side company never carries
`GAMING_ECOSYSTEM`: those segments describe services sold to the games industry, not to gambling
operators.

**AI and ML companies.** AI is horizontal, so "uses AI" or "could be used for games" is not enough.
An AI lab or generative-media company is **IN** when any one of six signs holds, with evidence; the
signs add up and none replaces another: gaming is a core market on its own site or among its
customers; its product sits in the game-development pipeline (assets, animation, audio, tools studios
use); it is a playable real-time experience; it is an interactive world a user enters; it comes out
of games (spun out of a games company, its models built on and sold into games); or it has a named
gaming product line. Evidence means gaming customers, gaming use, or a gaming-specific product - not a
TAM line, a single logo, a gaming investor on the cap table, or training data. A horizontal video,
image or media generator with none of the signs is generic AI: tracked under sector `OTHER`, outside
every gaming sector. A product-owner ruling overrides the signs in either direction, and a lab that
is in keeps all its rounds.

## 2 · Deal-inclusion gate (is it a tracked deal?)

Tracked, whether completed, announced or reported as in talks: equity rounds (early & late), M&A
(control & minority, carve-outs included), public offerings (IPOs/listings, PIPEs, secondary
offerings, fixed income), and **non-dilutive financing**. A reported or rumoured deal with no
agreement yet is a card whose description opens with [RUMOUR]; it is not shown until an analyst
enables it, then it is visible and counted like any card. A VC/PE fund raise goes to the fund
register, not to a deal. Not tracked: buybacks, partnerships, sponsorships, restructurings with no
new capital, internal reorganisations.
*(Types and categories → `deal-taxonomy.md`; non-dilutive financing → `definitions.md`.)*

## 3 · Company type (pick exactly one)

| Type | When | Key rule |
|------|------|----------|
| `STRATEGIC_OR_CVC` (label "Strategic") | Any operating company, whether or not it has anything to do with games, and a corporate venture arm | A non-gaming operating company (OpenAI, a telecom) keeps this type and carries sector `OTHER`. A corporate venture arm (e.g. "Sony Interactive Ventures") is Strategic through its **parent**; the venture arm of a non-gaming corporate is `VENTURE_CAPITAL_AND_ACC`. A firm doing work for games companies is Strategic, `GAMING_ECOSYSTEM`, B2B: a market-research or market-data firm (Newzoo, AppMagic) is segment `INFRASTRUCTURE_SERVICES`; a monetisation or design consultancy, a consultancy on a studio's publishing or commercial strategy, and a recruiter are segment `OTHER`. A gaming news/press/video media business monetizing an audience is Strategic too, `GAMING_ECOSYSTEM`/`STREAMING_ENTERTAINMENT` (§7), any format |
| `VENTURE_CAPITAL_AND_ACC` | VC firms, accelerators | name has "Ventures/Capital/Partners" + fund structure. A merchant bank or boutique that leads deals with its own money or fund keeps this type (The Raine Group) and also appears as an advisor on deals (the advisor role is read from the deal's advisor fields, not from the type) |
| `PRIVATE_EQUITY_AND_INST` | A firm whose business is investing a balance sheet or a fund: PE firms, asset managers, sovereign and pension funds, insurers, family offices, a credit fund or private lender investing a fund | A bank that leads deals through an asset-management or growth arm carded as the bank keeps this type (J.P. Morgan, Goldman Sachs) and also appears as an advisor on deals (the advisor role is read from the deal's advisor fields, not from the type) |
| `SERVICE_PROVIDERS` | A consultant on deals: a bank (commercial or investment), an M&A or corporate-finance advisor, a broker, a law firm, a financial, tax or legal advisor on transactions, an investment consultancy | The type of a firm that only advises or lends; a bank or advisory firm that leads deals with its own money or fund keeps an investor type. **Advisor** is also a role read from the deals: a company is an advisor when it is typed `SERVICE_PROVIDERS` or was an advisor, financial or legal, on at least one visible deal; the role is read from the deals' advisor fields and is not a second type, and the VC and PE rankings read the type alone. A service provider takes part as advisor, investor or lender, never as target, and a law firm only as advisor. Market-research, market-data and games consultancies are not here: they are Strategic |
| `ANGELS_INDIVIDUALS` | Individuals investing personally (not via a fund) | |
| `ASSET` | A game title / franchise / division sold as an asset | **requires a parent company** |
| `OTHER` | Government bodies, non-profits, an association, guild, federation or alliance whatever it runs, non-operating entities, anything that fits no other type | visible - do **not** exclude from company queries. An investor is never type `OTHER`. Not the sector `OTHER` (§4): a non-gaming operating company is `STRATEGIC_OR_CVC` with sector `OTHER` |

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
filler values INSIDE a covered sector. `CONSUMER_APPS` is not `OTHER`: a gamified consumer app is
inside the gaming universe, `OTHER` is outside it.
**Features** (six values): `AI_OR_ML` · `BLOCKCHAIN_OR_WEB3` · `UGC_MODDING` · `CASH_OR_SKILL_BASED_OR_RMG` · `UA_FINANCING` are sector-agnostic (any sector). `SHORT_DRAMA` is the exception - short drama is a Consumer Apps content vertical, so it applies only to companies whose sectors include `CONSUMER_APPS`.

`UA_FINANCING` as a **feature** marks an investor that provides non-dilutive user-acquisition capital; it is an investor-role tag, not an attribute of a studio's product. It is distinct from the `UA_FINANCING` **deal type** and the `NON_DILUTIVE_FINANCING` **deal category** (`deal-taxonomy.md`). To find UA-financing providers, filter companies on this feature rather than counting deals.
*(Use `BLOCKCHAIN_OR_WEB3` to include/exclude crypto-gaming - 2021–22 data is Web3-heavy.)*

What each feature flag means (a tag marks what is core to the company, never what it merely uses):
- `AI_OR_ML` - only a seller of AI technology or an AI-native product; never a company that merely uses AI internally. To build the "AI in gaming" set, first apply the gaming-inclusion AI gate (§1), then read `AI_OR_ML` inside that set, never as the inclusion filter on its own.
- `UGC_MODDING` - the product centres on user-generated content or modding (creation/sharing by players).
- `CASH_OR_SKILL_BASED_OR_RMG` - real-money or skill-based wagering mechanics *inside a game*; this tags content, it is not the casino-operator exclusion (see §1).

- **GAMING_CONTENT** → `content_type` (`DEVELOPER_1P_PUBLISHER` / `PUBLISHER_3P` / `OUTSOURCING_WFH`),
  plus `platform`, `monetization_type`, `game_genre`, `top_games` (the last three not required for
  pure outsourcing).
- **GAMING_ECOSYSTEM** → `ecosystem_type` (`B2C`/`B2B`) + `ecosystem_segment` (§7). Includes a company
  selling gaming-licensed merchandise, apparel or physical goods, or reselling game keys, e-pins,
  gift cards or in-game currency, that does not develop games itself
  (`ecosystem_segment = OTHER`, "retail/merch") - it is never `GAMING_CONTENT`, which requires the
  company to actually develop or publish a game. A publisher of physical board and card games only is
  here too: `B2C`, `ecosystem_segment = OTHER`.
- **CONSUMER_APPS** → `gamified_subsegment` + visible game mechanics (§8).
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

## 6 · Game genre (one closed set)

`PUZZLE` (match-3, block/tile, word, hidden-object, physics) · `ARCADE` (hyper-casual, endless runner,
tap/reflex, arcade clones) · `SPORTS_RACING` (football/basketball/cricket/golf/tennis, racing/driving) ·
`TABLETOP` (card, board, CCG, chess, solitaire) · `SHOOTER` (FPS, TPS, battle royale,
tactical/hero) · `STRATEGY_MOBA` (4X, RTS, city/base building, MOBA, auto-battlers, tower defense) ·
`ACTION_RPG` (real-time combat RPG, gacha RPG, dungeon crawlers, hack-and-slash) · `SIMULATION_SANDBOX`
(life/farm/city sims, management, sandbox, idle, tycoon) · `CASINO` (slots, poker, roulette, bingo,
social casino) · `OTHER` (only when nothing above fits - never combine `OTHER` with a named genre).

## 7 · Gaming Ecosystem segment (build vs operate)

The deciding test for the top two is **build vs operate.**

| Segment | Core question | Includes / examples |
|---------|---------------|---------------------|
| `CREATION_DEVELOPMENT` | Does it help **build** the game? | engines, SDKs, dev tools, middleware, co-dev, QA, localisation, art outsourcing, backend SDKs, rendering, build pipelines (Unity, Incredibuild, Parsec, Helpshift) |
| `INFRASTRUCTURE_SERVICES` | Does it help **run / scale** the business? | analytics, LTV/monetization tooling, cohort forecasting, server hosting, cloud live-ops, monetization platforms (GameAnalytics, Overwolf, Multiplay, Xsolla) |
| `ADTECH` | Is the core product advertising tech? | ad networks, DSPs/SSPs, mediation, programmatic (AppLovin, ironSource, Adjust) |
| `DISTRIBUTION_SOCIAL_PLATFORMS` | - | app stores, portals, launchers, community/social (Steam, Epic Store, Discord) |
| `ESPORTS` | - | tournament organisers, leagues, team orgs, competitive infra |
| `STREAMING_ENTERTAINMENT` | - | game streaming, cloud gaming, gaming video platforms (Twitch, YouTube Gaming) |
| `HARDWARE` | - | peripherals, consoles, controllers, VR/AR headsets, gaming PCs |
| `OTHER` | - | ecosystem firms fitting nothing above (retail/merch); a gaming SPAC, a listed blank-check company formed to buy a games business (`STRATEGIC_OR_CVC`, B2B, its deals tracked) |

`ecosystem_type` = `B2C` (gamers) or `B2B` (companies). UA financing is not a segment: its providers
carry the company feature `UA_FINANCING` (§4), valid on VC, PE and Strategic companies, so the ecosystem
segment alone undercounts the roster; its deals are non-dilutive financing, counted in general analytics
but not as funding raised.

## 8 · Consumer Apps (gamified, non-game B2C)

**Qualifies only if ALL hold:** B2C (not B2B/enterprise); not a game (no core gameplay loop as the
product); the user-facing experience is built on **visible gamification mechanics** (streaks,
levels/XP, leaderboards, progress bars, badges, IAP progression, virtual currency, challenges).

**Exclusions:** B2B/enterprise (e.g. Wellhub), gambling/betting apps, pure games (→ `GAMING_CONTENT`),
apps whose mechanics the user never sees.

**Subsegment (by primary purpose):** `EDTECH` (Duolingo, Kahoot!) · `FITNESS_WELLNESS` (Strava, Calm,
Zwift) · `ENTERTAINMENT_SOCIAL` (Reddit, Wattpad, short-drama / mini-drama carrying the `SHORT_DRAMA` tag) · `FINTECH` (Ugami, Rule, StockBattle - money or the markets, mechanic visible; Robinhood and Stash are out) · `OTHER` (Habitica).

## 9 · Region maps (use the country lists, not granular sub-regions)
These lists are InvestGame's query configuration, not a classification rule.
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
