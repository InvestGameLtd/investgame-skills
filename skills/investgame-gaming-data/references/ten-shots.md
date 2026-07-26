# Ten Shots - the proven InvestGame query library

Verified against the live database. Match the user's intent to the closest shot,
then swap the geography / segment / size band. Always include "use InvestGame" and "think hard".

These mirror the curated views on the InvestGame website (Notable Acquisitions, Mega Transactions,
First-Time Exits, Most Active Investors, Most-Funded Companies…). There is no one-click "give me view X"
button - the chat reproduces each view's logic **as a query**, so framing a question the way the data
is organised is what gets you the curated result. Reach for these before building something from scratch.

## Source & monitor
1. **Market pulse:** "Show the year-over-year trend in gaming deal value and count for the last 5 years, split M&A vs fundraising (early + late stage). Table by year + one-line methodology."
2. **Live deal wire:** "List gaming fundraisings and M&A from the last 90 days where the target is a mobile gaming company. Target, country, deal type, size USD, date, lead investor. Sort by date desc."
3. **Geography deep-dive:** "Deal-making in <geo> across all history: top 10 fundraisings, top 10 M&A by size, plus the year-by-year deal-count trend. Note data caveats."

## Screen & source
4. **Early-stage sourcing screen:** "Early-stage (Seed + Series A) mobile gaming fundraisings in companies HQ'd in <country list>, last 24 months. Company, country, round, size USD, date, investors."
5. **Competitive investor landscape:** "Most active venture investors in early-stage mobile gaming deals over the last 3 years. Top 20 by distinct deal count + total disclosed invested."

## Value & diligence
6. **Portfolio mirror:** "Analyze <investor>'s activity: number of deals, typical check size, typical stage, most frequent target profile."
7. **Precedent comps:** "Precedent M&A multiples for mobile gaming targets with EV $<low>M–$<high>M. Target, acquirer, deal value, EV, EV/Revenue + one-line EV-basis note."
8. **Exit / acquirer landscape:** "Most active acquirers of mobile gaming studios over the last 5 years. Top 15 by acquisition count (as lead investor, target = mobile gaming company)."
9. **Company deep-dive:** "Profile of <company>: total funding raised, each round with size and date, investors, any disclosed valuation."
10. **Valuation benchmark:** "Compare average EV/Revenue (LTM) for M&A of mobile vs PC/console gaming companies over the last 5 years. Deal count + average revenue multiple per group."

## Exits & landscape
11. **Exit landscape:** "First-time exits (M&A and IPO/SPAC) of mobile gaming studios over the last 5 years. Company, exit type, acquirer/route, size USD, date."
12. **Notable deals:** "The notable gaming-content acquisitions of the last 12 months." (the curated Notable Gaming Content Acquisitions set)
13. **Fund / LP landscape:** "Largest gaming VC/PE funds by fund size (AUM): fund name, vintage year, size USD, managing firm. Top 15."
14. **Genre landscape:** "Over the last 3 years, gaming deal count and total disclosed value by game genre for mobile gaming content companies. Rank by deal count."

## Out of scope (do not run - route to custom research)
Talent-flow / who-left-X · headcount-growth · clean SEA early-stage mobile equity. (NB: UA-financing,
exits and any country/region geography ARE queryable - don't route those out.)
