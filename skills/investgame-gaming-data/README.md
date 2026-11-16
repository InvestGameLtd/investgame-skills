# InvestGame Gaming-Data Skill - client package

A drop-in skill that makes Claude answer gaming-investment questions at **InvestGame quality**, every
time, from a short prompt. It pairs with the InvestGame MCP connector: the **MCP** fetches the data,
this **skill** carries the taxonomy, the definitions, and the house style so the answer is correctly
scoped and formatted instead of guessed.

## What's inside

| File | Purpose |
|------|---------|
| `SKILL.md` | The orchestrator Claude loads - golden rules + pointers to the references below |
| `references/taxonomy.md` | The company vocabulary - every field, its values and what each means |
| `references/deal-taxonomy.md` | Deal types and categories, exit paths, participants and what Size means |
| `references/definitions.md` | Canonical metric buckets - the consistency layer (M&A vs fundraising, "recent", EV basis) |
| `references/ten-shots.md` | The proven query library |
| `references/research-playbook.md` | Web research beyond the deal data - who researches what, and where to look |

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

The skill is instructions only: it adds no data and no network calls of its own. It shapes the
question going in and the answer coming out. When a question falls outside InvestGame's scope or is ambiguous, the MCP
returns a lean `clarify` result (its `questions`, and sometimes `suggestions`) **instead of any data**,
and the skill puts those questions to the user rather than guessing; a well-formed question returns the
`data` result (tables + linkable entities).

## Install

**All Claude surfaces (recommended):** add the plugin marketplace `InvestGameLtd/investgame-skills`
(`claude plugin marketplace add InvestGameLtd/investgame-skills` in Claude Code, or the claude.ai
"Add marketplace" UI) and install the `investgame-skills` plugin; the skill activates automatically on
any gaming deal / company / investor / valuation question. Connect the InvestGame MCP connector
(2-minute setup) so the data calls resolve.

**Fallback:** a download with every skill, each a ready-to-upload zip for the claude.ai "Upload a
skill" flow, is on <https://app.investgame.net/setup>.

## What it deliberately won't do

It declares - rather than fabricates - the things InvestGame can't self-serve: talent flow across
companies, a headcount ranking across companies and advisor league tables. Those route to InvestGame
custom research. Honesty here is what keeps the data trusted.
