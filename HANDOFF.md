# Old Money: Europe's Great Fortunes, 1066 to Today (European Wealth Map)

An interactive, sourced web map of how Europe's largest family fortunes were made, kept and moved from the Norman Conquest (1066) to today, and where that money sits now. It is for general readers (and the project owner) who want to test whether old-money families are worth far more than published rich-list figures suggest, without the site making unsourced or insinuating claims. It is the sister site of "The Triangle Trade" slave-trade map.

## Links

- Live site: https://alxndrhq.github.io/european-wealth-map/
- GitHub repo: https://github.com/AlxndrHQ/european-wealth-map (public, branch `main`, GitHub Pages serves the repo root)
- Sister site: https://alxndrhq.github.io/triangle-trade-mind-map/ (repo `AlxndrHQ/triangle-trade-mind-map`), whose engine this site reuses

## Current state (as of 3 November 2026, the only session)

- Published and live. One commit on `main`: `3ff73cc Old Money: Europe's great fortunes, 1066 to today`. Working tree clean and in sync with `origin/main` as of 10 November 2026.
- `data.json` holds 154 records (86 family/company profiles and 68 entities: estates, banks, trusts, foundations, offshore centres, laws and leak investigations), 80 dated events and 12 money trails. The live data was confirmed to load all 154 records and 12 trails after deploy.
- Every profile has at least 3 sources and all four "Claimed vs Controlled" wealth layers; the build reported no broken links and no isolated records.
- Views (from `tools/template.html`): Web (D3 network, `atlas`), Directory (`grid`), Chronology (`chron`, includes a "Who owns England" chart from Guy Shrubsole's figures), Money trails (`money`), Claimed vs Controlled (`wealth`), Overlaps (`overlaps`), Map (`map`, Leaflet, with a second layer "Where the Money Sits" for estate companies, banks, foundations and offshore centres), dossier drawer, light/dark mode.
- Dossiers show sources-of-fortune tags, a "What They Own Today" holdings list, and a link to the family's dossier on the Triangle Trade site where one exists (`https://alxndrhq.github.io/triangle-trade-mind-map/#/p/<id>`).
- A fact-check and privacy-audit agent ran before publishing: 176 logged changes (96 substantive corrections plus 80 rewritten "searched" fields). Its log is `research/FACTCHECK.md` (local only, see below).
- ICIJ Offshore Leaks checks: 291 lookups through ICIJ's public reconciliation API (the search site blocks bots). Raw hits were mostly name collisions and are kept local; none appear on the site unless ICIJ or a press outlet published the link.

Headline findings shown on the site (as of the session): Grosvenor is £9.7bn on the Sunday Times Rich List 2026 vs £4.2bn family equity in accounts and £9.5bn property managed; Wallenberg has no published family figure but its foundations hold half the votes in Investor AB (about SEK 1.26 trillion); Porsche-Piëch about €12bn (Manager Magazin 2026) but 53% of Volkswagen's votes; Liechtenstein about $9.2bn (Bloomberg 2023) while LGT manages CHF 386bn.

## How it's built

Stack: a single static HTML page (D3 network graph, Leaflet map, vanilla JS) with the data embedded, built by a small Python script. No server, no framework, no package manager. Hosted on GitHub Pages.

Key files:

- `index.html`: the built site (template plus embedded data). Do not hand-edit; rebuild instead.
- `data.json`: merged dataset (records, events, trails), produced by the build.
- `tools/template.html`: the site engine, adapted from the sister repo's template (groups, roles, periods, colors, labels, the Claimed vs Controlled tab).
- `tools/build.py`: merges `research/g*.json` into `data.json`, drops broken links, warns about duplicate IDs, embeds data into `index.html`. Merges trails from each group file.
- `tools/icij_check.py`: runs ICIJ Offshore Leaks reconciliation-API lookups for every family, vehicle and public figure. Its output is unverified and goes to `research/icij/` (git-ignored).
- `research/SCHEMA.md`: record schema, 7 groups, 13 connection types, the strict 1066-descent field (documented or tradition), and the shared ID registry saying which group file owns which ID.
- `research/g1.json`: UK landed aristocracy and gentry, Crown and Church, Norman origins (24 profiles, 17 entities, 20 events, 3 trails, e.g. the Mayfair, Bloomsbury and Crown Estate trails).
- `research/g2.json`: continental princely and noble houses (20 profiles, 16 entities, 20 events, 3 trails).
- `research/g3.json`: banking and merchant dynasties plus colonial companies (21 profiles, 16 entities, 20 events, 3 trails).
- `research/g4.json`: industrial dynasties plus offshore and modern holding structures (21 profiles, 19 entities, 20 events, 3 trails, e.g. Wendel, Agnelli/Exor, Krupp).
- `research/reference/`: copies of the sister site's schema and its old-wealth research (`sister-g24-oldwealth-uk.json`, `sister-g25-oldwealth-continental.json`), used as a starting point. Committed to the public repo.
- Local only (in `.gitignore`, never publish): `research/icij/leads.json` (raw ICIJ name matches that may name private individuals), `research/FACTCHECK.md` (before/after log that quotes removed private details), `European Wealth Handoff.md` (the original planning brief for this project).

Groups (one validated colorblind-safe color plus a node shape each): landed aristocracy and gentry; continental princely and noble houses; banking and merchant dynasties; colonial companies; industrial dynasties; the Crown and the Church; modern holding structures.

Periods: 1066-1300, 1300-1530, 1530-1700, 1700-1850, 1850-1945, 1945-today.

Run, build, deploy:

```
# build (from the project folder)
python3 tools/build.py research .

# preview locally
python3 -m http.server 8000   # then open http://localhost:8000/

# deploy: commit and push to main; GitHub Pages redeploys in 1-3 minutes
git add index.html data.json research/g*.json && git commit -m "..." && git push
```

Testing used headless Chrome screenshots (`--headless=new --screenshot`) on a free port. D3 zoom transitions do not run headless, so test fit logic without the transition. After pushing, poll `https://alxndrhq.github.io/european-wealth-map/data.json` to confirm the deploy.

## Decisions and conventions

- Core question from the user: are old-money families worth far more than claimed? (The user thought Grosvenor was about $90bn; the published figure is about £9.7bn.) The answer is framed through the four-layer Claimed vs Controlled model: (1) published net worth with publisher and year, (2) gross assets in filed accounts, (3) assets controlled or managed beyond the family's share (client money, voting control through holding chains, foundations the family governs), (4) the opaque trusts/offshore layer with a verdict (`documented`, `reported`, `none found`) and a note of what was searched. The layers are never added together and no family total is invented, because they measure different things.
- Starting point is 1066 because the user sees the Norman Conquest as the pivotal point; scope is Europe as a whole.
- Sourcing: every profile has at least 3 real sources found during research; every claim is tagged `documented` or `interpretive`; wealth figures always name the publisher and year.
- "Came over with the Conqueror" descents are marked tradition/interpretive unless a historian (e.g. Complete Peerage, ODNB) documents them.
- "25,000 families with trillions" was corrected to Shrubsole's documented figure: about half of England owned by roughly 25,000 landowners; no research supports "trillions".
- Legal care: offshore is not illegal; leak-based claims are attributed to ICIJ or the publishing outlet with the caveat that being listed is not wrongdoing; a crime is named only where a court or regulator found it; no "hid/hidden/concealed" verbs without a source that uses them (a final sweep confirmed none remain).
- Privacy: living people are named only as public figures (titleholders, monarchs, office holders, directors on public registers, people who spoke publicly about their family). No private relatives, children, addresses. Raw ICIJ leads and the fact-check log stay out of the repo for this reason.
- Workflow the user chose: 4 parallel research agents per round (about 200 web searches each, no sub-agents), one JSON file per group, then a separate fresh fact-check and privacy-audit agent before every publish. Public GitHub repo plus Pages.
- Before each new research round, ask the user which families or industries matter most. They care most about tracing old money to people who hold power today and following the money step by step (money trails).
- Research files live in the repo, not a scratch folder, because scratch folders get wiped between sessions.

## Open items

1. Review `research/reference/` for privacy. It is committed to the public repo, and the fact-checker said it did not check it (it only checked g1-g4).
2. Re-test four Rothschild Archive links (supporting the 1814 gold, Waterloo and Suez claims); the archive was down for maintenance during checks. A BMW PDF link was also kept although it blocks automated checkers.
3. Decide on the definition of `documented` for the opaque layer: five verdicts (Cadogan, Portman, Heineken, Schroders, Albrecht) rest on official registers or filings rather than ICIJ, while the stated definition mentioned ICIJ only.
4. Track live legal matters and update when they resolve: the Lombard Odier Karimova appeal, the Elkann case, Puech v. LVMH, the Mulliez appeal.
5. Refresh wealth figures periodically; Forbes real-time figures are as of 3 November 2026 and will drift. The fact-checker did not go line by line through figures for the less prominent families.
6. Add links from the Triangle Trade site back to this site (proposed, not done).
7. Possible next rounds proposed: a deeper Norman/medieval round (more Domesday lines, Dissolution grantees, enclosure); a modern-structures round on specific family offices and Register of Overseas Entities filings. The user had not yet said which families or industries to prioritise.
8. Question: should this `HANDOFF.md` be committed? The repo is public and `.gitignore` keeps the earlier internal planning brief private; this file contains no private data, but decide before pushing it.

## Session log

- 3 November 2026 (one session, about 7:30-8:45 pm local): read the planning brief, copied and adapted the sister site's engine, wrote `research/SCHEMA.md`, validated the palette, ran four research agents (G1-G4), ran ICIJ reconciliation lookups, built and screenshot-tested every view, fixed the crowded graph labels, ran the fact-check and privacy audit (176 changes), committed, created the public repo `AlxndrHQ/european-wealth-map`, enabled Pages, and confirmed the live deploy.
