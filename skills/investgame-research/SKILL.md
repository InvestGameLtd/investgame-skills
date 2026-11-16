---
name: investgame-research
version: 0.10.16
description: >
  Deep, multi-part InvestGame work: a market or regional report, a landscape or deep dive, a company,
  deal or investor write-up, meeting or call prep, or structured notes from a call transcript. Use for
  "report on / state of / landscape of [market]", "deep dive on [topic]", "profile or write up [company
  or investor]", "prepare me for a meeting with [company]", "notes from this call", or a deck or PDF
  about a topic. It plans first, then combines investgame-gaming-data, investgame-analysis and web
  research into a benchmarked deliverable rendered with investgame-format. Not this skill: a single fact
  or one company's card figures (the hub), what the press published this week (investgame-press), a
  one-off chart (investgame-format), game design or generic software questions.
---

# InvestGame Research & Reports

The deep-work layer. The everyday skills (data via the investgame-gaming-data hub, analysis, format) answer
a question; this one handles the bigger ask - a report, a landscape, a deep dive, company or trend research,
an investor profile, prep for a meeting. Whatever the shape, the job is the same: investigate comprehensively,
prepare the material properly, and deliver it on-brand. A "report" is just the most common instance of this.

## When this activates
A request that needs depth, not a single number: "a market report on …", "the state of … gaming", "a deep
dive / deep research on …", "research this company / deal / trend", "profile this investor", "prepare me for
a meeting with …", "make a deck / PDF about …", or any broad, comprehensive task. A quick fact is NOT this -
answer that directly with the investgame-gaming-data hub.

## Plan first - always
Deep work starts with a plan, not with output. Never jump straight to a 15-slide deck.
1. Understand the task - what question, which subject (a market / segment / company / investor / trend), how
   deep, and for what audience.
2. Investigate enough to plan well - a quick first pass over the data and the sources (below) so the plan is
   grounded, not guessed.
3. Propose a short, human-readable plan - a table of contents: the sections/slides with a sub-bullet each
   ("Slide 1 - market at a glance; Slide 2 - deal activity & trend; …"). Aim for ~5 sections for a focused
   ask, up to ~15 for a broad one. Ask which theme (Warm White or Dark Navy). Invite changes.
4. On approval (or if the user already said "just do it"), execute. Don't build the full thing before the
   plan is agreed. Keep the plan concise - a TOC with light sub-bullets, not an essay.

## Gather comprehensively (two streams, run them together)
A deep deliverable needs a rounded picture, so pull from more than one angle.
- InvestGame data - via the investgame-gaming-data hub. Don't pull one cut; assemble several so the story is
  complete. Standard cuts (unless the user narrows them): top ~15 deals; top ~15 buyers / most-active
  investors / most-funded companies by VC funding; and historical dynamics over time across dimensions - value (deal size),
  count (number of deals/events), and valuation (multiples); plus breakdowns by segment, platform,
  geography or deal type. Full recipes in references/playbook.md.
  Many lookups spend credits and meet the rate limit: the hub's rule 8 says how to handle both.
- Research - the narrative and outside perspective a report needs. Prioritise sources in order:
  1) investgame.net first - the digest and features pages already cover the deals and themes; start there.
  2) the curated gaming-industry sources in references/research-sources.md (analysts, newsletters, market
     data) - prefer these over generic search results.
  3) general web - for broader context and narrative.
  (Web research uses your own web tools; InvestGame's data tool doesn't browse.)
If your agent has no web/browsing tool, say so plainly and deliver only the InvestGame data layers rather
than leaving blank sections - never fabricate the outside-context stream from memory.

## Read, benchmark, present
- Read & benchmark via investgame-analysis - never describe a market or company in isolation; put it in
  context (peers, the global total, prior years). The comparison is the value. Analysis's rules carry over
  (multiples, never-break-silently, footnote assumptions, objective-not-opinionated).
- Present via investgame-format - on-brand, in the theme the user picked. Format owns the look and the form:
  a deck/PDF for a full report, a one-pager or a written brief for lighter prep. For market-size figures
  InvestGame doesn't hold, cite third-party sources separately, average and show the range, and never blend
  them into InvestGame deal numbers.

## What you can produce (instances of the same workflow)
- A market / regional / segment report - activity, sizing, leaders, outlook, benchmarked.
- A deep dive / trend research - a theme over time, grounded in the data.
- A company or deal research write-up; an investor / fund profile. For a company or fund profile
  document the layout is fixed: the matching sample from the Reports tab shelf "MCP & Skills build
  examples" (the user downloads it; the MCP cannot fetch it), filled from the company card and the deal
  queries, as investgame-format describes.
- A meeting or call preparation brief - a focused, deep profile to walk in ready.
- Structured notes / a recap from a call or meeting transcript - topic-organised, decision-focused, with
  single-owner action items, enriched with InvestGame context (see the notes mode below).
See references/playbook.md for the section recipes and the standard data cuts per type.

## Notes from a call or meeting transcript (a different mode - no plan step)
When the input is a transcript rather than a research question, don't plan-first - process it:
1. **Clarify only if needed** - unidentified speakers, missing company/context, ambiguous action-item
   ownership, or poor transcript quality (many [inaudible]). Match the output language to the transcript.
2. **Process** - map speakers to names/roles; **group by topic, not chronologically**; extract
   **decisions** (what was decided, not just discussed); extract **action items** (task · single owner ·
   deadline · priority); note open questions.
3. **Enrich via the hub** - for any gaming company or deal mentioned, pull concise InvestGame context
   (recent funding, last deal, valuation, segment) into an "InvestGame context" block; you may add a quick
   web check for very recent news. Keep it factual; flag anything unverified.
4. **Render via investgame-format** - a clean, branded notes document. Structure: participants · subject ·
   summary (≤6 bullets of decisions/outcomes, not topics) · discussion by topic · InvestGame context ·
   action items table · open questions · next steps.
Call notes (short 1:1 / intro / diligence) stay tight; meeting notes (multi-party) are fuller - same
logic, different weight. If unsure, ask "quick call recap or full meeting record?"

## Charter (non-negotiable)
Objective, never sell-side - present what the data and sources show, not how to "win" a pitch. People and
companies described neutrally. Honest sourcing: label every source, flag gaps ("insufficient public data")
instead of inventing, no hype.

## Common mistakes
- Jumping to a full deck before the plan is agreed.
- Pulling one data cut - a deep report needs several angles (top deals, top players, the time trend).
- Skipping investgame.net and the curated sources, going straight to generic web.
- Describing in isolation instead of benchmarking.
- Blending third-party market-size figures into InvestGame deal numbers without labelling.
- Treating a quick lookup as deep work - just answer it with the investgame-gaming-data hub.
- For a transcript: transcribing chronologically instead of synthesising by topic, or listing discussion
  topics as if they were decisions.
