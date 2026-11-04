# Old Money: Europe's Great Fortunes, 1066 to Today

An interactive, sourced map of how Europe's largest family fortunes were made, from the Norman Conquest to today. It covers the land grants, banks, colonial companies and industries behind them, where the money sits now, and how a family's published net worth compares with what it controls.

**Live site:** https://alxndrhq.github.io/european-wealth-map/

Sister site: [The Triangle Trade](https://alxndrhq.github.io/triangle-trade-mind-map/). Families covered on both sites link to each other.

## What's in it

- 86 family and company dossiers and 68 estates, banks, trusts, offshore centres, laws and leaks, in seven groups: landed aristocracy and gentry, princely and noble houses, banking and merchant dynasties, colonial companies, industrial dynasties, the Crown and the Church, and modern holding structures.
- **Claimed vs Controlled:** for every family, four layers side by side, never added together:
  1. published net worth (publisher and year);
  2. gross assets in filed accounts;
  3. assets controlled or managed beyond the family's share (client money, voting control through holding chains, foundations the family governs);
  4. the opaque layer of trusts, foundations and offshore vehicles, with a verdict (`documented`, `reported` or `none found`) and a note of what was searched.
- **Money trails:** single fortunes followed step by step, such as the 1677 Davies marriage → Mayfair → Grosvenor Group → trusts.
- Web (network), Directory, Chronology, Overlaps and Map views, plus a light and dark mode.

## Rules the data follows

- Every profile has at least 3 real sources, and every claim is tagged `documented` or `interpretive`.
- Wealth figures always name the publisher and year. No family total is invented.
- Offshore is not illegal. Leak-based claims are attributed to ICIJ or the publishing outlet, and being listed in ICIJ data does not imply wrongdoing. A crime is named only where a court or regulator found it.
- Living people are named only as public figures: titleholders, monarchs, office holders, directors on public registers, and people who have spoken publicly about their family.
- "Came over with the Conqueror" is marked as tradition unless a historian documents the descent.

## Build

```
python3 tools/build.py research .
```

This merges `research/g*.json` into `data.json` and embeds it in `index.html`. The schema and shared ID registry are in `research/SCHEMA.md`. `tools/icij_check.py` runs ICIJ Offshore Leaks reconciliation lookups for every family, vehicle and public figure; its raw output is unverified name matches and is kept out of the repo.

Research was compiled in November 2026, and rich-list figures will drift. Corrections are welcome as issues.
