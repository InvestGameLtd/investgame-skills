# InvestGame Gaming-Data Skill - client package

A drop-in skill that makes Claude answer gaming-investment questions at **InvestGame quality**, every
time, from a short prompt. It pairs with the InvestGame MCP connector: the **MCP** fetches the data,
this **skill** carries the taxonomy, the definitions, and the house style so the answer is correctly
scoped and formatted instead of guessed.

## Why it exists

Out of the box, an AI agent invents what it doesn't know - wrong categories ("Investment Funds"),
arbitrary scope ("recent = 6 months"), inconsistent buckets (the same year returning 181 vs 104 M&A
deals). This skill removes the guessing: it is the InvestGame "house brain" running on your side.

## What's inside

| File | Purpose |
|------|---------|
| `SKILL.md` | The orchestrator Claude loads - golden rules + pointers to the references below |
| `references/taxonomy.md` | Company classification - closed vocabulary + InvestGame's analyst decision rules (gaming-gate, every enum, monetization×platform logic) |
| `references/deal-taxonomy.md` | Deal classification - Type→Category derivation, edge cases, size/EV/multiple conventions |
| `references/definitions.md` | Canonical metric buckets - the consistency layer (M&A vs fundraising, "recent", EV basis) |
| `references/output-and-brand.md` | Answer structure, default columns, methodology line, InvestGame brand |
| `references/ten-shots.md` | The proven query library across the VC workflow |

## How it works with the MCP

```
Your question ─► [ InvestGame skill ]            ─► [ InvestGame MCP ] ─► InvestGame DB
                  reformulates into the              fetches data
                  real taxonomy, pins the scope,      (read-only)
                  asks if ambiguous
                       ▲                                   │
                       └────── formats the answer ◄────────┘
                              (columns + methodology + brand)
```

The skill never sees your data and adds no latency to the database - it just shapes the question going
in and the answer coming out. When a question falls outside InvestGame's scope or is ambiguous, the MCP
returns a lean `clarify` result (its `questions`, and sometimes `suggestions`) **instead of any data**,
and the skill puts those questions to the user rather than guessing; a well-formed question returns the
`data` result (tables + linkable entities).

## Install

**All Claude surfaces (recommended):** add the plugin marketplace `InvestGameLtd/investgame-skills`
(`claude plugin marketplace add InvestGameLtd/investgame-skills` in Claude Code, or the claude.ai
"Add marketplace" UI) and install the `investgame-skills` plugin; the skill activates automatically on
any gaming deal / company / investor / valuation question. Connect the InvestGame MCP connector
(2-minute setup) so the data calls resolve.

**Fallback:** per-skill zips for the claude.ai "Upload a skill" flow are served from
<https://app.investgame.net/setup>. The npm package `@investgame/skills`
(`npx @investgame/skills install`) remains as a legacy channel.

## What it deliberately won't do

It declares - rather than fabricates - the things InvestGame can't self-serve: people/talent-flow,
headcount-growth, a few advanced cuts (investor stage/geo focus, advisor league tables), and thin
early-stage Southeast-Asia mobile equity. Those route to InvestGame custom research. Honesty here is
what keeps the data trusted.
