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

Claude keeps a local copy of this marketplace and, for third-party marketplaces,
does **not** refresh it on its own. Installing or reinstalling the plugin reads
that local copy, so reinstalling alone will not move you to a newer version.

To update, refresh the marketplace first, then the plugin:

```
claude plugin marketplace update investgame
claude plugin update investgame-skills@investgame
```

To refresh automatically from now on: `/plugin` > Marketplaces > investgame >
Enable auto-update.

This repository is generated from InvestGame's skill sources on each release.
Issues and PRs are not monitored here - contact app@investgame.net.

(c) InvestGame Ltd. Proprietary license: free to install and use with Claude;
redistribution or modification outside this marketplace is not permitted.
