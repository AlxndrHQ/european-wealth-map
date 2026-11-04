"""Query the ICIJ Offshore Leaks reconciliation API for every family, holding vehicle and public
titleholder in research/g*.json, and write the raw candidate matches to research/icij/leads.json.

A match here is only a LEAD: names collide (street names, unrelated people). A profile's
opaque verdict may be 'documented' or 'reported' only when ICIJ or a named press partner
published the link. Being listed in ICIJ data does not imply wrongdoing.
Usage: python3 tools/icij_check.py research"""
import json, sys, glob, os, re, time, urllib.request

API = 'https://offshoreleaks.icij.org/api/v1/reconcile'
src = sys.argv[1]
STOP = re.compile(r'\b(family|house|of|the|and|dukes?|earls?|princes?|counts?|marquess(es)?|viscounts?|barons?|lords?|royal|incl\.?|line|lines|branch)\b', re.I)

def key_name(name):
    base = re.sub(r'\(.*?\)', '', name)
    base = STOP.sub(' ', base)
    return re.sub(r'\s+', ' ', base).strip(' ,;&/')

queries = {}   # query text -> {record ids, why}
for f in sorted(glob.glob(os.path.join(src, 'g*.json'))):
    for r in json.load(open(f)).get('records', []):
        if r.get('type') == 'entity':
            continue
        cand = [(key_name(r['name']), 'family name')]
        cand += [(h['name'], 'holding') for h in r.get('holdingsToday', []) if h.get('kind') in
                 ('Private company', 'Family office', 'Trust', 'Foundation', 'Fund / private equity', 'Bank / wealth manager', 'Listed stake')]
        cand += [(p['name'], 'public figure') for p in r.get('today_people', [])]
        for q0, why in cand:
            for q in re.split(r'\s*/\s*', re.sub(r'\(.*?\)', '', q0)):   # the API rejects '/'
                q = q.strip()
                if len(q) < 4:
                    continue
                e = queries.setdefault(q, {'ids': set(), 'why': why})
                e['ids'].add(r['id'])

def post(batch):
    body = json.dumps({'queries': {f'q{i}': {'query': q, 'limit': 8} for i, q in enumerate(batch)}}).encode()
    req = urllib.request.Request(API, data=body, headers={'Content-Type': 'application/json', 'User-Agent': 'old-money-research-check/1.0'})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)

qs = sorted(queries)
leads, failed = [], []
for i in range(0, len(qs), 10):
    batch = qs[i:i + 10]
    try:
        res = post(batch)
    except Exception:
        res = {}
        for j, q in enumerate(batch):   # retry one by one; a single odd query can fail the batch
            for attempt in range(3):
                try:
                    res[f'q{j}'] = post([q])['q0']; break
                except Exception as ex:
                    err = ex; time.sleep(3 + 3 * attempt)
            else:
                print('query failed', q, err)
                failed.append(q)
    for j, q in enumerate(batch):
        toks = [t.lower() for t in re.findall(r'[\w-]{4,}', q)]
        hits = []
        for h in res.get(f'q{j}', {}).get('result', []):
            typ = h['types'][0]['name'] if h.get('types') else ''
            if typ == 'Address':
                continue
            nm = h['name'].lower()
            if toks and not all(t in nm for t in toks[:2]):   # require the main tokens in the hit name
                continue
            hits.append({'icij_id': h['id'], 'name': h['name'], 'type': typ, 'dataset': h.get('description', ''),
                         'score': round(h.get('score', 0), 1), 'url': f"https://offshoreleaks.icij.org/nodes/{h['id']}"})
        leads.append({'query': q, 'why': queries[q]['why'], 'records': sorted(queries[q]['ids']), 'hits': hits})
    time.sleep(1)

os.makedirs(os.path.join(src, 'icij'), exist_ok=True)
out = {'checked': time.strftime('%Y-%m-%d'), 'api': API,
       'caveat': 'Raw name matches from the ICIJ Offshore Leaks database. Leads only: names collide, and being listed does not imply wrongdoing.',
       'failed': failed, 'queries': len(leads), 'with_hits': sum(1 for l in leads if l['hits']), 'leads': leads}
json.dump(out, open(os.path.join(src, 'icij', 'leads.json'), 'w'), ensure_ascii=False, indent=1)
print(f"{len(leads)} queries, {out['with_hits']} with candidate hits")
for l in leads:
    if l['hits']:
        print(f"- {l['query']} [{l['why']}] -> " + '; '.join(f"{h['name']} ({h['type']}, {h['dataset'][:40]})" for h in l['hits'][:4]))
