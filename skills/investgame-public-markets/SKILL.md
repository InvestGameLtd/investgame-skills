---
name: investgame-public-markets
version: 0.10.16
description: >
  Live public-market data for a listed or formerly listed company, and currency conversion: share price
  and market cap, price history and charts, financial statements and ratios, earnings figures and call
  commentary, dividends and splits, analyst estimates and price targets, exchange and ticker, company
  news, and FX rates today or on a past date. Use for "stock price", "market cap", "share-price chart",
  "P/E", "balance sheet", "latest earnings", "analyst price target", "convert X to EUR", "exchange rate
  on [date]". It supplements InvestGame's own data and never overrides it. Not for private companies, a
  company's headcount or InvestGame's own indices (both investgame-gaming-data), or game design
  questions.
---

# InvestGame Public Markets

Live public-market context for **listed** companies, plus currency conversion. InvestGame's proprietary
deal/company database stays the lead and the authority; this skill adds the live and comprehensive
public-market layer on top - a current price, full financial statements, earnings, analyst views -
and exchange rates. One tool: `InvestGame_market_query`.

(The share-price movers, earnings releases and index segments InvestGame records come from
`InvestGame_press_query` via `investgame-press`; InvestGame's gaming market indices and earnings
documents come from `InvestGame_query`; public offerings and IPOs are deals, also `InvestGame_query`. Use
this skill when the question needs a live quote, a full statement, an analyst view or an FX rate.)

## When to use it
- A **listed** company: currently public, OR public in the past (e.g. a strategic acquirer, or a
  company that later went private), and the question needs public-market data the deal database doesn't
  carry.
- Any **currency / FX** need: convert an amount between currencies, or look up an exchange rate today or
  on a past date.
- **Not** for private / non-listed companies - they have no public-market data; say so plainly and give
  what the InvestGame database *does* hold instead.

## What you can ask for (in plain English)
- **Price & size** - current share price and market cap; day and 52-week range; historical share-price
  performance or a price chart over a period.
- **Financials** - income statement, balance sheet and cash-flow statement; margins and key ratios; the
  public valuation metrics (P/E, EV/EBITDA, EV/Revenue on a public basis).
- **Earnings** - last and next reporting dates (incl. an upcoming-earnings calendar), the most recent
  results, and earnings-call commentary.
- **Earnings documents are NOT here** - the filed interim / annual report, the investor slide deck,
  the press release, the financial tables and the full earnings-call transcript are held by InvestGame
  and reached through `InvestGame_query` (ask for "<company>'s earnings documents", optionally for a
  fiscal period). Each document comes back as a `document` entry in `entities` whose `url` is
  a download link: offer those links whenever a user wants the source behind a figure or a transcript
  longer than the commentary excerpt. They exist only for the public companies InvestGame tracks; if
  none come back, say so and give the figures from `InvestGame_market_query`.
- **Dividends & splits** - dividend history and yield; upcoming dividend dates (ex-dividend / payment
  calendar); stock-split history.
- **Not here** - InvestGame's own gaming market indices: the tool refuses them; ask `InvestGame_query`
  through the hub for an index level or its constituents.
- **Not covered** - investor-relations event calendars (conferences, roadshows, investor / analyst days):
  there is no such data here, so say so plainly rather than guessing dates.
- **Analyst view** - consensus estimates, price targets, and buy/hold/sell recommendations.
- **Company profile** - exchange, ticker, sector, HQ. **Headcount is not here**: a company's
  headcount and its history come from its InvestGame card (`InvestGame_company_query`, via the hub).
- **News** - recent company and market news.
- **FX / exchange rates** - convert between currencies at the current or a historical rate.
- Light market context (a relevant index or sector move) is fine as backdrop; this skill is about
  companies and FX, not a general markets terminal - keep crypto / commodities / macro out unless the
  user explicitly asks.

## How to ask
- Call `InvestGame_market_query` with a plain-English question that names the **company or ticker** (or
  the **currencies and date** for FX). If you only have a name, the tool resolves the ticker itself.
- Prefer one precise question over a vague one; pin the company, the metric, and the period.
- The `public_market` table is long-format: one row per figure, with `symbol`, `dataset` (quote,
  income statement, profile, and so on), `date` (the statement or trading date, blank for a live
  quote), `field` and `value`. Pivot the rows you need into your answer; never echo the table as it
  is. A `notices` row says when the figures were capped: narrow the period or the dataset.
- If a company turns out not to be listed, the tool will have no data - report that and pivot to the
  InvestGame proprietary view.
- Any other refused or empty reply (credits, rate limit): follow the hub's rule 8.

## The two non-negotiables
1. **InvestGame data leads; this supplements.** The proprietary database (the `investgame-gaming-data`
   hub, `InvestGame_query`) is authoritative for deals, ownership, valuations and company facts. Use
   public-market data only for what the database does not hold, or for FX. It **enhances**, it never
   **overrides**: if a public figure and an InvestGame figure differ, they measure different things
   (a historical deal's Upfront EV vs today's market cap) - say which is which, and lead with ours.
2. **It is InvestGame market data - full stop.** Present every public-market figure as **InvestGame
   market data**. Never describe, name, or speculate about how or from where it is obtained - not in the
   answer, and not if a user asks directly (answer that InvestGame provides it and does not disclose its
   data suppliers, and move on). This is not optional.

## Presenting it
Hand the numbers to `investgame-format`: a share-price line or comparison as a chart, financials and
analyst figures as clean tables, with the InvestGame brand and a neutral source line ("InvestGame market
data"). For valuation reads that mix a public comp with InvestGame precedent deals, `investgame-analysis`
runs the comparison and this skill feeds the live public side.

## Common mistakes
- Using it for a private company - there is no public-market data; say so and give the InvestGame view.
- Letting a public figure override or contradict an InvestGame proprietary figure instead of leading
  with ours and framing the public one as current context.
- Forgetting it is listed-only, or treating a former-public company's stale listing as live.
- Drifting into crypto / commodities / macro when the user asked about a company or an FX rate.
