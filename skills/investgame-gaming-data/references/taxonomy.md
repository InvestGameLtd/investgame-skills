# InvestGame Taxonomy — company classification rules

The closed vocabulary and the decision rules behind every InvestGame company record. The agent
reformulates questions into these terms and **never invents categories**. If a concept is outside this
taxonomy, say "InvestGame doesn't track that" rather than fabricating a field.

*Grounded in the InvestGame analyst ("Fira") classification rules + the production schema enums — this
is the authoritative term set the database is built on.*

## Contents
1. Gaming-inclusion test · 2. Deal-inclusion gate · 3. Company type · 4. Sector & gated fields · 5. Monetization × platform
6. Game genre · 7. Ecosystem segment · 8. Consumer Apps · 9. Region maps · 10. "Ask the user" triggers

---

## 1 · Gaming-inclusion test (is the target even "gaming"?)

**In scope:** game developers & publishers (any platform); casino **games** (genre `CASINO`); esports
orgs and gaming infrastructure/tools/adtech with a genuine gaming use-case; B2C non-game apps with real
game mechanics (Consumer Apps — §7).

**Out of scope:** real-money gambling / iGaming **operators**; physical toys & merchandise (unless
licensed game IP); generic PR / brand / marketing; adjacent tech with no gaming use-case.

The line analysts apply most: **a casino game is content; a casino operator is out.**

## 2 · Deal-inclusion gate (is it a tracked deal?)

Tracked: equity rounds (early & late), M&A (control & minority), IPOs/listings, VC/PE fund raises,
and **UA-financing** (`UA_FINANCING` — a real, queryable deal type, just kept out of headline
fundraising/M&A totals by methodology). Not tracked: buybacks, partnerships, sponsorships,
restructurings with no new capital, internal reorganisations; dev-financing and licensing are not in
the queryable set at all, and `OTHER` is excluded from analytics totals.
*(Full deal classification → `deal-taxonomy.md`.)*

## 3 · Company type (pick exactly one)

| Type | When | Key rule |
|------|------|----------|
| `STRATEGIC_OR_CVC` | Operating companies, corporates, corporate-VC arms | **Default for a gaming company.** A CVC arm (e.g. "Sony Interactive Ventures") is classified via its **parent** → STRATEGIC. |
| `VENTURE_CAPITAL_AND_ACC` | VC firms, accelerators | name has "Ventures/Capital/Partners" + fund structure |
| `PRIVATE_EQUITY_AND_INST` | PE firms, sovereign wealth, pension, family offices | |
| `SERVICE_PROVIDERS` | Banks, advisory, law, accounting firms | participate as **advisors**, not targets/investors |
| `ANGELS_INDIVIDUALS` | Individuals investing personally (not via a fund) | |
| `ASSET` | A game title / franchise / division sold as an asset | **requires a parent company** |
| `OTHER` | Government, non-profit, unclassifiable | visible — do **not** exclude from company queries |

**Field applicability (what each type carries):**
- `STRATEGIC_OR_CVC` → sector + sector-gated fields (below); never investor fields.
- `VC`/`PE` → investor specialization (`GENERALIST`/`GAMING`) + AUM, plus the **named funds** the firm
  has raised (each fund's vintage year and size/AUM — so "largest gaming funds by AUM" is answerable);
  **never** sector/content fields.
- `SERVICE_PROVIDERS` → identity only; no sector/investor fields.
- `ASSET` → parent company + optional platform/genre/monetization; no sector/company-identity fields.
- `ANGELS_INDIVIDUALS` → identity only.

## 4 · Sector (a company can carry several) and its gated fields

`GAMING_CONTENT` · `GAMING_ECOSYSTEM` · `CONSUMER_APPS`. Sector gates which fields are populated.
**Features**: `AI_OR_ML` · `BLOCKCHAIN_OR_WEB3` · `UGC_MODDING` · `CASH_OR_SKILL_BASED_OR_RMG` are sector-agnostic (any sector). `SHORT_DRAMA` is the exception — short drama is a Consumer Apps content vertical, so it applies only to companies whose sectors include `CONSUMER_APPS`.
*(Use `BLOCKCHAIN_OR_WEB3` to include/exclude crypto-gaming — 2021–22 data is Web3-heavy.)*

What each feature flag means (it tags a product capability, NOT a company category):
- `AI_OR_ML` — the product uses AI/ML *inside the game or tooling*. **It does NOT mean "an AI-focused company"**: it is a capability flag and also catches large publishers using AI internally. To build the "AI in gaming" set, apply the gaming-inclusion AI gate (three triggers: a declared gaming market, building into the game pipeline, or a playable real-time output; general-purpose AI like OpenAI and linear media generation like Suno / Luma are out), then read `AI_OR_ML` as the in-set capability flag, not as the inclusion filter on its own.
- `UGC_MODDING` — the product centres on user-generated content or modding (creation/sharing by players).
- `CASH_OR_SKILL_BASED_OR_RMG` — real-money or skill-based wagering mechanics *inside a game*; this tags content, it is not the casino-operator exclusion (see §1).

- **GAMING_CONTENT** → `content_type` (`DEVELOPER_1P_PUBLISHER` / `PUBLISHER_3P` / `OUTSOURCING_WFH`),
  plus `platform`, `monetization_type`, `game_genre`, `top_games` (the last three not required for
  pure outsourcing).
- **GAMING_ECOSYSTEM** → `ecosystem_type` (`B2C`/`B2B`) + `ecosystem_segment` (§6).
- **CONSUMER_APPS** → `gamified_subsegment` + ≥2 visible mechanics (§7).
- **platform:** `MOBILE` · `PC_CONSOLE` (incl. cloud gaming) · `BROWSER` · `VR_AR`.

## 5 · Monetization × platform — the decision rules (analyst-critical)

Monetization is **not free choice** — it is dictated by platform. These rules are the difference
between a defensible classification and a guess.

**Allowed values:** `IAP` · `IAA` · `GAAS` · `UPFRONT_SALE` · `DLC` · `SUBSCRIPTION`.

### Mobile (`MOBILE` + GAMING_CONTENT)
- Primary monetization is **strictly one of `IAP` or `IAA`** — `GAAS`/HYBRID are **not** valid as
  mobile primary (HYBRID only as a secondary annotation).
- **`IAP` = progression economy** — gacha, loot boxes, character/weapon upgrades, energy/stamina
  gating, meta-progression unlocks (long progression, lower DAU).
- **`IAA` = attention economy** — short loops (<5 min), frequent inter-level ads, hyper-casual or
  level-based puzzle, CPI-driven scale (high DAU).
- **Hyper-casual ⇒ `IAA` primary** (overrides `IAP`, even if IAP exists).
- **Tiebreaker when both present:** short session + high DAU → IAA; long progression + low DAU → IAP;
  intent words "hyper-casual / ad-monetized / CPI scaling" → IAA; "meta-progression / collection /
  gacha" → IAP. If still ambiguous → **flag for senior review, do not guess.**
- **Mobile `GAAS` is banned** except globally recognised cross-platform live-service titles
  (e.g. Fortnite mobile). Battle pass → `IAP`; seasonal content → `IAP`/`IAA`; live-ops updates are
  **not** `GAAS`.

### PC / Console (`PC_CONSOLE`)
- **`IAP`/`IAA` are banned here** (mobile-native). Use only `GAAS` (live-service / battle pass /
  seasonal), `UPFRONT_SALE` (paid purchase), `DLC` (paid expansions), `SUBSCRIPTION` (Game Pass / PS+).

### Cross-platform
- Classify by the **dominant platform by revenue**; IAP/IAA apply only if mobile dominates.

### `GAAS` guardrail
- Assign `GAAS` only when there is a real **service economy** (battle pass / seasonal systems /
  structured live-service loop). Ongoing updates alone ≠ GAAS. Never `GAAS` for hyper-casual,
  ad-driven portfolios, or level-based puzzle games.

### Time rule
- Classify monetization **as of the deal announcement date**, not the company's current model.

## 6 · Game genre (one closed set)

`PUZZLE` (match-3, block/tile, word, hidden-object, physics) · `ARCADE` (hyper-casual, endless runner,
tap/reflex, arcade clones) · `SPORTS_RACING` (football/basketball/cricket/golf/tennis, racing/driving) ·
`TABLETOP` (card, board, CCG, poker, chess, solitaire) · `SHOOTER` (FPS, TPS, battle royale,
tactical/hero) · `STRATEGY_MOBA` (4X, RTS, city/base building, MOBA, auto-battlers, tower defense) ·
`ACTION_RPG` (real-time combat RPG, gacha RPG, dungeon crawlers, hack-and-slash) · `SIMULATION_SANDBOX`
(life/farm/city sims, management, sandbox, idle, tycoon) · `CASINO` (slots, poker, roulette, bingo,
social casino) · `OTHER` (only when nothing above fits — never combine `OTHER` with a named genre).

## 7 · Gaming Ecosystem segment (build vs operate)

The deciding test for the top two is **build vs operate.**

| Segment | Core question | Includes / examples |
|---------|---------------|---------------------|
| `CREATION_DEVELOPMENT` | Does it help **build** the game? | engines, SDKs, dev tools, middleware, co-dev, QA, localisation, art outsourcing, backend SDKs, rendering, build pipelines (Unity, Incredibuild, Parsec, Helpshift) |
| `INFRASTRUCTURE_SERVICES` | Does it help **run / scale** the business? | analytics, LTV/monetization tooling, **UA financing**, cohort forecasting, server hosting, cloud live-ops, monetization platforms (GameAnalytics, Overwolf, Multiplay, Xsolla) |
| `ADTECH` | Is the core product advertising tech? | ad networks, DSPs/SSPs, mediation, programmatic (AppLovin, ironSource, Adjust) |
| `DISTRIBUTION_SOCIAL_PLATFORMS` | — | app stores, portals, launchers, community/social (Steam, Epic Store, Discord) |
| `ESPORTS` | — | tournament organisers, leagues, team orgs, competitive infra |
| `STREAMING_ENTERTAINMENT` | — | game streaming, cloud gaming, gaming video platforms (Twitch, YouTube Gaming) |
| `HARDWARE` | — | peripherals, consoles, controllers, VR/AR headsets, gaming PCs |
| `OTHER` | — | ecosystem firms fitting nothing above (retail/merch) |

`ecosystem_type` = `B2C` (gamers) or `B2B` (companies). *(Note: UA-financing **companies** are
`INFRASTRUCTURE_SERVICES` ecosystem; UA-financing **deals** are queryable but excluded from headline
fundraising/M&A totals.)*

## 8 · Consumer Apps (gamified, non-game B2C)

**Qualifies only if ALL hold:** B2C (not B2B/enterprise); not a game (no core gameplay loop as the
product); **≥2 visible gamification mechanics** in the UI (streaks, levels/XP, leaderboards, progress
bars, badges, IAP progression, virtual currency, challenges); materially worse without them.

**Exclusions:** B2B/enterprise (e.g. Wellhub), gambling/betting apps, pure games (→ `GAMING_CONTENT`),
apps with ≤1 mechanic.

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
widen it — never silently pick a scope. Known contradictions needing a human tie-break: AdTech players
that carry a separate non-InvestGame taxonomy.
