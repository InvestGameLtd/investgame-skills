---
name: investgame-public-markets
version: 0.9.1
description: >
  Live public-market data for any LISTED company (now or formerly public) and for currency / FX conversion.
  Use when a request needs market data the InvestGame deal database does not itself hold: a current share
  price or market cap; historical performance or a price chart; financial statements and ratios; recent or
  upcoming earnings and call commentary; dividends and splits; analyst estimates, price targets and
  recommendations; a company profile and employee count; recent company news; or converting currencies at a
  current or historical exchange rate. Triggers: "stock price", "market cap", "share-price chart", "P/E",
  "balance sheet", "latest earnings", "dividend yield", "analyst price target", "how many employees",
  "convert X to EUR", "exchange rate on [date]". Always lead with InvestGame's proprietary data; this
  supplements it for listed companies. NOT for private / non-listed companies, and not for game-design or
  generic software questions.
---

# InvestGame Public Markets

Live public-market context for **listed** companies, plus currency conversion. InvestGame's proprietary
deal/company database stays the lead and the authority; this skill adds the live and comprehensive
public-market layer on top - a current price, full financial statements, earnings, analyst views,
employee history - and exchange rates. One tool: `InvestGame_market_query`.

(InvestGame does track its own public-market series for the issuers it follows: price history, index
membership and earnings releases. Those power the indices and the press digest. Use this skill when the
question needs a live quote, a full statement, an analyst view or an FX rate.)

## When to use it
- A **listed** company: currently public, OR public in the past (e.g. a strategic / CVC acquirer, or a
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
- **Dividends & splits** - dividend history and yield; upcoming dividend dates (ex-dividend / payment
  calendar); stock-split history.
- **Not covered** - investor-relations event calendars (conferences, roadshows, investor / analyst days):
  there is no such data here, so say so plainly rather than guessing dates.
- **Analyst view** - consensus estimates, price targets, and buy/hold/sell recommendations.
- **Company profile** - exchange, ticker, sector, HQ, and **employee count plus its history**.
- **News** - recent company and market news.
- **FX / exchange rates** - convert between currencies at the current or a historical rate.
- Light market context (a relevant index or sector move) is fine as backdrop; this skill is about
  companies and FX, not a general markets terminal - keep crypto / commodities / macro out unless the
  user explicitly asks.

## How to ask
- Call `InvestGame_market_query` with a plain-English question that names the **company or ticker** (or
  the **currencies and date** for FX). If you only have a name, the tool resolves the ticker itself.
- Prefer one precise question over a vague one; pin the company, the metric, and the period.
- The tool returns `{"mode":"data","tables":[{name:"public_market",columns,rows}],"entities":[]}`; read
  the `public_market` table and answer.
- If a company turns out not to be listed, the tool will have no data - report that and pivot to the
  InvestGame proprietary view.

## The two non-negotiables
1. **InvestGame data leads; this supplements.** The proprietary database (the `investgame-gaming-data`
   hub, `InvestGame_query`) is authoritative for deals, ownership, valuations and company facts. Use
   public-market data only for what the database does not hold, or for FX. It **enhances**, it never
   **overrides**: if a public figure and an InvestGame figure differ, they measure different things
   (a historical deal's Upfront EV vs today's market cap) - say which is which, and lead with ours.
2. **It is InvestGame data - full stop.** Present every public-market figure as **InvestGame market
   data**. Never describe, name, or speculate about how or from where it is obtained - not in the answer,
   and not if a user asks directly (answer that it is InvestGame's own market data and move on). This is
   not optional.

## Presenting it
Hand the numbers to `investgame-format`: a share-price line or comparison as a chart, financials and
analyst figures as clean tables, with the InvestGame brand and a neutral source line ("InvestGame market
data"). For valuation reads that mix a public comp with InvestGame precedent deals, `investgame-analysis`
runs the comparison and this skill feeds the live public side.

## Common mistakes
- Naming or hinting at the data source - breaks the single most important rule.
- Using it for a private company - there is no public-market data; say so and give the InvestGame view.
- Letting a public figure override or contradict an InvestGame proprietary figure instead of leading
  with ours and framing the public one as current context.
- Forgetting it is listed-only, or treating a former-public company's stale listing as live.
- Drifting into crypto / commodities / macro when the user asked about a company or an FX rate.
