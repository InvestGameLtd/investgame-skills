# InvestGame Analyst Skills

Official [InvestGame](https://app.investgame.net) analyst skills for Claude:
gaming deal taxonomy, valuation methodology, public-markets guidance, research
playbooks, press digests and house formatting. Pairs with the InvestGame MCP
connector (`https://app.investgame.net/mcp`).

## Install

- **Claude.ai / Desktop / Cowork:** Customize > Personal plugins > "+" >
  Add marketplace > `InvestGameLtd/investgame-skills`, then install the
  `investgame-skills` plugin.
- **Claude Code:** `claude plugin marketplace add InvestGameLtd/investgame-skills`
  then `claude plugin install investgame-skills@investgame`.

Full per-surface guide: <https://app.investgame.net/setup>

## Updating

Reinstalling does **not** update the plugin, on any surface: `install` does
nothing when the plugin is already there. How you actually update depends on
where you run Claude.

**Claude Code.** Refresh the catalogue, then the plugin. Both are needed: without
the first, the second can report you are already current when you are not.

```
claude plugin marketplace update investgame
claude plugin update investgame-skills@investgame
```

To keep it current automatically: `/plugin` > Marketplaces > investgame > Enable
auto-update. It is off by default for third-party marketplaces.

**Claude.ai, Desktop and Cowork.** These serve plugins from your account rather
than from your machine, and can keep serving an older version than the one
published here. No command forces a refresh. If you need to be certain you are on
the current skills, install them directly from <https://app.investgame.net/setup>,
which are rebuilt from our live deployment on every download.

This repository is generated from InvestGame's skill sources on each release.
Issues and PRs are not monitored here - contact app@investgame.net.

(c) InvestGame Ltd. Proprietary license: free to install and use with Claude;
redistribution or modification outside this marketplace is not permitted.
