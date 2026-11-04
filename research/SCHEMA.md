# European Wealth Map, 1066 to Today: research data schema

Output ONE JSON file per group: `{"records":[...], "events":[...], "trails":[...]}`. Valid JSON, no comments, UTF-8.

The site answers four questions for each family:
1. **How did they make the money?** (origins, the mechanism, step by step)
2. **Where is the money today?** (the named companies, estates, trusts and vehicles)
3. **What are they invested in now?** (sectors, stakes and holdings, by name)
4. **Are they worth what is claimed?** Kept honest through the `wealth` layers below. We never invent a total. We show the published figure next to what filings show they *control*, and say plainly what is opaque.

## PROFILE record (families, dynasties, houses, and major companies, banks or holding vehicles that deserve a full dossier)
```json
{
  "id": "kebab-case-unique-id",
  "name": "Grosvenor family (Dukes of Westminster)",
  "category": "Landed Aristocracy & Gentry" | "Princely & Noble Houses" | "Banking & Merchant Dynasties" | "Colonial Companies & Investors" | "Industrial Dynasties" | "Crown & Church" | "Holding Structures",
  "role": "Conquest & Royal Grant" | "Church Land & Dissolution" | "Urban Ground Rents" | "Agricultural Land & Enclosure" | "Mining & Mineral Royalties" | "Banking & Sovereign Lending" | "Trade & Chartered Monopoly" | "Colonial Extraction" | "Industry & Manufacturing" | "Arms & Armaments" | "Sovereign & Princely Rule" | "Modern Finance & Holding",   // the PRIMARY engine of the fortune
  "moneySources": ["Norman grant", "Marriage to heiress", "Urban ground rents", "Coal royalties"],  // 2–6 short tags, oldest first: every documented engine of the fortune
  "nation": "England" | "Scotland" | "United Kingdom" | "France" | "Germany" | "Austria" | "Italy" | "Spain" | "Netherlands" | "Belgium" | "Sweden" | "Switzerland" | "Liechtenstein" | "Monaco" | "Luxembourg" | other short label,
  "scale": "Minor" | "Significant" | "Major" | "Dominant",   // relative economic weight TODAY (or at peak if defunct)
  "scaleBasis": "documented" | "estimated",
  "scaleNote": "One sentence justifying scale, with a published number.",
  "start": 1066,          // first documented year of the fortune (integer)
  "end": null,            // year the fortune/line ended, or null if it still exists
  "lifespan": "1066–present (Mayfair from 1677)",
  "base": "Mayfair, London",
  "geo": [51.512, -0.151],   // [lat, lng] of seat or HQ, 3 decimals
  "aliases": ["Grosvenor Group", "Earls Grosvenor"],
  "origins": "2–3 sentences: where the family came from and the first source of money.",
  "role_summary": "2–3 sentences: HOW THE MONEY WAS MADE (the callout). Concrete mechanisms, dates and amounts.",
  "roleDetail": [ {"t":"Short bold claim.", "d":"1–2 sentence detail with specifics.", "basis":"documented"|"interpretive"} ],   // 3–5 items, chronological
  "legacy": "2–3 sentences: WHERE THE MONEY IS TODAY: named holding companies, estates and trusts.",
  "legacyDetail": [ {"t":"...", "d":"...", "basis":"documented"|"interpretive"} ],   // 1–3 items
  "norman": { "claim": "documented" | "interpretive" | "none",
              "text": "1–2 sentences: does the family descend from a 1066 companion or Domesday tenant? 'documented' ONLY if a historian or Complete Peerage/ODNB/Open Domesday supports it; family tradition = 'interpretive'.",
              "source": {"label":"…","url":"https://…"} },        // include for families with ANY claimed medieval/Norman origin; omit otherwise
  "wealth": {
    "published": [ {"figure":"£9.677bn", "usd":"c. $12.9bn", "who":"Duke of Westminster and family", "publisher":"Sunday Times Rich List", "year":2026, "rank":"18th", "url":"https://…"} ],   // ONLY real published estimates. Empty list if none, and say so in publishedNote.
    "publishedNote": "optional: e.g. 'No Rich List or Forbes figure published since 2013.'",
    "grossAssets": {"text":"What filed accounts show: e.g. 'Grosvenor Group: property assets of £X bn, net assets £Y bn, year to Dec 2025 (Companies House accounts).' Gross ≠ net: say what debt or partner capital sits against it.", "source":{"label":"…","url":"https://…"}},
    "controlled": {"text":"Assets the family CONTROLS or MANAGES beyond its net share: funds run for third parties, AUM, joint ventures, foundations it governs, voting control via dual-class shares. e.g. 'LGT manages CHF 386bn of client assets (2025); this is not family wealth, but it is the family's reach.'", "source":{"label":"…","url":"https://…"}},
    "opaque": {"verdict":"documented" | "reported" | "none found",
               "text":"What sits in trusts, foundations or offshore vehicles whose value is NOT public, and what that structure hides (beneficiaries, values, distributions).",
               "searched":"What you searched: e.g. 'ICIJ Offshore Leaks (surname, estate company), Register of Overseas Entities, Companies House PSC'.",
               "source":{"label":"…","url":"https://…"}},
    "gapNote": "1–2 sentences, interpretive and clearly hedged: why the published figure may understate (or overstate) the family's economic reach. e.g. 'The Rich List counts the family's equity; the estate company controls about £X bn of property, and trust assets abroad are not counted.' Leave out if there's nothing documented to say."
  },
  "holdingsToday": [   // 3–10 items: WHAT THEY ARE INVESTED IN NOW, by name
    {"name":"Grosvenor Britain & Ireland", "kind":"Urban property" | "Rural land" | "Bank / wealth manager" | "Listed stake" | "Private company" | "Fund / private equity" | "Foundation" | "Trust" | "Family office" | "Art & collections" | "Agriculture & forestry" | "Energy & minerals" | "Other",
     "sector":"Real estate", "where":"London", "detail":"c. 300 acres of Mayfair and Belgravia", "basis":"documented"|"interpretive",
     "source":{"label":"…","url":"https://…"}}
  ],
  "slaveSiteId": "grosvenor-family-westminster",   // ONLY if this family has a dossier on the sister site (list below)
  "lineage": [ {"name":"…", "relation":"founder" | "father" | "son" | "heir" | "spouse" | "heiress" | "descendant" | "successor firm" | other short word, "years":"1665–1730", "note":"1 sentence: what passed between them (land, title, firm, money).", "id":"existing-record-id-if-any", "basis":"documented"|"interpretive"} ],   // oldest → newest, 3–7 items
  "today": "2–4 sentences: the family, its money and its name today. Only PUBLICLY documented people.",
  "today_people": [ {"name":"Hugh Grosvenor, 7th Duke of Westminster", "relation":"titleholder", "role":"Chair of the Grosvenor Trustees", "sector":"Land & estates" | "Banking & finance" | "Politics & government" | "Business & industry" | "Royalty & titles" | "Culture & media" | "Philanthropy", "year":2026, "basis":"documented", "source":{"label":"…","url":"https://…"}} ],
  "sources": [ {"label":"Publisher — Title", "url":"https://..."} ],   // 3–6 REAL URLs you actually opened or found in search
  "connections": [ {"id":"other-id", "type":"<edge type>", "label":"short label, e.g. 'granted Ebury manor 1677 by marriage'"} ]   // 4–10
}
```

## ENTITY record (estates, estate companies, banks, trusts, foundations, offshore centres, laws, charters, leaks, places)
```json
{ "id":"grosvenor-group", "name":"Grosvenor Group Ltd", "type":"entity",
  "kind":"Estate / district" | "Estate company" | "Bank / wealth manager" | "Holding company" | "Trust / foundation" | "Family office" | "Offshore centre" | "Chartered company" | "Law / charter / tax" | "Leak / investigation" | "Register / dataset" | "Church / monastery" | "Battle / event" | "Listed company" | other short label,
  "description":"2–3 factual sentences, with numbers where documented.", "start":1677, "geo":[51.51,-0.15] (optional),
  "sources":[{"label":"…","url":"…"}] (1–3), "connections":[...] }
```

## Edge types (use exactly these)
- `ownership`: founded, owns, shareholder of, controls
- `trade`: traded with, supplied, merchant partner
- `finance`: loan, credit, banker to, invested in
- `charter`: royal grant, charter, licence, monopoly, appointed by
- `family`: family, descent, cadet branch
- `marriage-settlement`: land or money that came by marriage
- `inheritance`: passed by will or entail
- `enclosure-or-grant`: Norman/feudal grant, enclosure award
- `dissolution-grant`: received monastic or Church land
- `trust`: held in trust for, trustee of
- `offshore`: held via an offshore entity or jurisdiction (cite the source)
- `legacy`: successor firm, merged into, money flowed to, endowment
- `political`: ally, war, office, lobbying, treaty

## Rules
1. **Accuracy over volume.** Use reputable sources: company accounts and annual reports, Companies House, Land Registry, ICIJ, the Sunday Times Rich List / Forbes / Bloomberg (as reported), the History of Parliament, Open Domesday, the National Archives, Britannica, university sites, major press (FT, Guardian, Times, Bloomberg, Reuters, BBC, Der Spiegel, Le Monde, NZZ…). Wikipedia is fine as one source among others, never the only one. Never use conspiracy sites ("Black Nobility", "13 bloodlines", Illuminati content and the like).
2. **Every profile needs ≥3 sources** with real URLs you found while researching. Never invent a URL. Every entity needs ≥1.
3. **Wealth figures name the publisher and year.** If none exists, say so. Never compute or guess a family total. Convert to USD only as "c." using that year's rough rate.
4. **Tag every claim `documented` or `interpretive`.** "Came over with the Conqueror" is interpretive unless a historian documents it.
5. **Offshore ≠ illegal.** For ICIJ-based claims: attribute to ICIJ or the named outlet and add "Being listed in ICIJ data does not imply wrongdoing." Use "held via", "structured through" and the like, not "hid" or "hiding", unless a cited source uses that word, and then quote and attribute it. Name a crime only if there is a court finding or a regulator action.
6. **Living people:** only public figures (titleholders, monarchs, office holders, directors listed on public registers, people who have spoken publicly about their family history). Never children, private relatives, addresses or contact details.
7. **Connections:** 4–10 per profile. Only link to IDs in your own file or in the SHARED REGISTRY below. Never create a record whose ID the registry assigns to another group. If you need a missing shared node, link to the closest registry ID, or create it in your file with your group prefix in the id (e.g. `g3-schroders-plc`).
8. **events:** 12–20 key dated events: `{"year":1086, "title":"Domesday survey completed", "text":"1–2 sentences.", "ids":["record-ids"], "source":{"label":"…","url":"…"}}`.
9. **trails (money trails):** 2–3 per group. Each follows one fortune step by step from origin to today's vehicle:
```json
{"id":"g1-mayfair-trail", "title":"From a Cheshire manor to Mayfair to Grosvenor Group", "region":"London", "summary":"2–3 sentences.",
 "steps":[ {"year":1677, "title":"Marriage to Mary Davies", "text":"2–3 sentences.", "ids":["grosvenor-family-westminster"], "kind":"land" | "money" | "power" | "structure" | "today", "basis":"documented"|"interpretive", "amount":"optional: '£… / … acres'", "source":{"label":"…","url":"…"}} ]}   // 5–9 steps, the last of kind "today"
```
10. Write the file with the Write tool to the exact path given, then validate it: `python3 -c "import json;json.load(open('PATH'))"`. Save partial progress early and often (overwrite the same file), so work survives an interruption.

## Sister site (the Triangle Trade): families with an existing dossier
Set `slaveSiteId` to the exact id when you cover one of these. Their old-wealth facts (Rich List 2026, register checks, slavery links) are in `research/reference/sister-g24-oldwealth-uk.json` and `sister-g25-oldwealth-continental.json`. READ THEM FIRST and build on them. Their URLs are already verified; reuse them and add new ones.
UK: grosvenor-family-westminster, cadogan-family, howard-de-walden-family, portman-family, montagu-douglas-scott-buccleuch, percy-family-northumberland, cavendish-family-devonshire, russell-family-bedford, fitzalan-howard-family-norfolk, stanley-family-derby, manners-family-rutland, spencer-family-althorp, spencer-churchill-family-marlborough, thynne-family-bath, leveson-gower-family-sutherland, brydges-family-chandos, british-crown-estate-duchies, lascelles-family, gladstone-family, drax (the sister site uses `drax-family`), nm-rothschild, fugger-family.
Continental: house-of-liechtenstein, thurn-und-taxis-family, house-of-hesse-kassel, house-of-hohenzollern, house-of-saxe-coburg-gotha, house-of-habsburg, house-of-bourbon, house-of-wittelsbach, house-of-grimaldi-monaco, wallenberg-family, house-of-bernadotte, house-of-orleans-braganza, house-of-orange (Orange-Nassau), congo-free-state.
**Use the same id as the sister site** for these families in this project too (e.g. the Grosvenor profile's id is `grosvenor-family-westminster`).

## SHARED REGISTRY (id — name). Only the owning group creates the record. Everyone may link.

**G1: UK landed, Crown & Church, Norman origins**
- william-the-conqueror: William I and the Norman Conquest (profile, category Crown & Church)
- domesday-book (entity, 1086), battle-of-hastings (entity, 1066), dissolution-of-the-monasteries (entity, 1536–41), enclosure-acts (entity), magna-carta (entity, 1215)
- death-duties-inheritance-tax (entity: 1894 estate duty → inheritance tax, heritage/agricultural reliefs), register-of-overseas-entities (entity, 2022), uk-land-registry-ccod-ocod (entity), who-owns-england (entity)
- british-crown-estate-duchies (profile), church-of-england-commissioners (profile, Church Commissioners)
- grosvenor-family-westminster, grosvenor-group (entity), cadogan-family, cadogan-group (entity), howard-de-walden-family, portman-family, montagu-douglas-scott-buccleuch, percy-family-northumberland, cavendish-family-devonshire, russell-family-bedford, fitzalan-howard-family-norfolk, stanley-family-derby, manners-family-rutland, spencer-churchill-family-marlborough, thynne-family-bath, leveson-gower-family-sutherland, cecil-family-salisbury, berkeley-family, lowther-family-lonsdale, herbert-family-pembroke, cavendish-bentinck-portland
- mayfair-belgravia (entity), chelsea-knightsbridge (entity), marylebone (entity)

**G2: Continental princely and noble houses**
- house-of-liechtenstein, lgt-group (entity), thurn-und-taxis-family, house-of-habsburg, house-of-grimaldi-monaco, house-of-orange, house-of-wittelsbach, house-of-hohenzollern, house-of-hesse-kassel, house-of-saxe-coburg-gotha, house-of-bourbon, house-of-bernadotte, house-of-savoy, house-of-alba, esterhazy-family, schwarzenberg-family, furstenberg-family, lobkowicz-family
- leopold-ii-belgium (profile), congo-free-state (entity), holy-roman-empire (entity), french-revolution-confiscations (entity), weimar-1919-expropriations (entity), communist-expropriations-1945 (entity)

**G3: Banking and merchant dynasties, colonial companies**
- medici-family, bardi-peruzzi (one profile for both), fugger-family, welser-family, nm-rothschild (the Rothschild family; profile), rothschild-and-co (entity), edmond-de-rothschild-group (entity), baring-family, hope-and-co, hoare-family, coutts-family, wallenberg-family, investor-ab (entity), schroder-family, hambro-family, warburg-family, oppenheim-family, lazard-david-weill, pictet-lombard-odier (Geneva partner banks; one profile), hottinguer-mallet (French haute banque; one profile)
- hanseatic-league (entity), east-india-company (profile, Colonial Companies), dutch-east-india-company (profile), dutch-west-india-company (entity), british-south-africa-company (profile), cecil-rhodes (profile), bank-of-england (entity), south-sea-company (entity), city-of-london-corporation (entity)

**G4: Industrial dynasties and modern holding structures**
- krupp-family, thyssen-family (incl. Thyssen-Bornemisza), quandt-family, porsche-piech-family, agnelli-elkann-family, exor (entity), schneider-family, wendel-family, peugeot-family, michelin-family, merck-family-darmstadt, haniel-family, henkel-family, siemens-family, reimann-family, heineken-family, guinness-family-iveagh, bettencourt-meyers-family, hermes-dumas-family, mulliez-family
- offshore centres (entities): jersey, guernsey, isle-of-man, british-virgin-islands, cayman-islands, luxembourg, switzerland-banking-secrecy, liechtenstein-foundations, netherlands-stichting
- leaks (entities): panama-papers, paradise-papers, pandora-papers, icij-offshore-leaks-db
- german-family-foundations (entity: Familienstiftung / doppelstiftung model), family-office (entity: the modern single-family office)
