"""Merge research/g*.json into data.json, report problems, and embed the data into index.html.
Usage: python3 build.py <research_dir> <out_dir>"""
import json, sys, glob, os, re, collections

src, out = sys.argv[1], sys.argv[2]
records, events, owner, trails_g = [], [], {}, []
for f in sorted(glob.glob(os.path.join(src, 'g*.json'))):
    d = json.load(open(f))
    g = os.path.basename(f)[:-5]
    for r in d.get('records', []):
        if r['id'] in owner:
            print(f'DUP {r["id"]}: {owner[r["id"]]} & {g} (keeping first, merging connections)')
            first = next(x for x in records if x['id'] == r['id'])
            first.setdefault('connections', []).extend(r.get('connections', []))
            continue
        owner[r['id']] = g
        records.append(r)
    events += d.get('events', [])
    trails_g += d.get('trails', [])

ids = set(owner)
missing = collections.Counter()
for r in records:
    keep = []
    for c in r.get('connections', []):
        c = {'id': c} if isinstance(c, str) else c
        if c['id'] in ids and c['id'] != r['id']:
            keep.append(c)
        else:
            missing[c['id']] += 1
    r['connections'] = keep
for e in events:
    for i in e.get('ids', []):
        if i not in ids:
            missing['(event) ' + i] += 1
    e['ids'] = [i for i in e.get('ids', []) if i in ids]
events.sort(key=lambda e: e['year'])

# dedupe events with the same year and near-identical title
seen, ev2 = set(), []
for e in events:
    k = (e['year'], re.sub(r'\W+', '', e['title'].lower())[:24])
    if k in seen:
        continue
    seen.add(k); ev2.append(e)

prof = [r for r in records if r.get('type') != 'entity']
print(f'{len(prof)} profiles, {len(records)-len(prof)} entities, {len(ev2)} events')
print('by category', collections.Counter(r.get('category') for r in prof))
print('under 3 sources', [r['id'] for r in prof if len(r.get('sources', [])) < 3])
print('no wealth layers', [r['id'] for r in prof if not r.get('wealth')])
print('entities without source', [r['id'] for r in records if r.get('type') == 'entity' and not r.get('sources')])
print('no geo', [r['id'] for r in prof if not r.get('geo')])
deg = collections.Counter()
for r in records:
    for c in r['connections']:
        deg[r['id']] += 1; deg[c['id']] += 1
print('isolated', [r['id'] for r in records if deg[r['id']] == 0])
if missing:
    print('dropped links to unknown ids:', dict(missing.most_common(60)))

trails = list(trails_g)
tp = os.path.join(src, 'trails.json')
if os.path.exists(tp):
    trails += json.load(open(tp)).get('trails', [])
if trails:
    for t in trails:
        for st in t.get('steps', []):
            bad = [i for i in st.get('ids', []) if i not in ids]
            if bad: print('trail', t['id'], 'drops unknown ids', bad)
            st['ids'] = [i for i in st.get('ids', []) if i in ids]
    print(len(trails), 'money trails')
data = {'records': records, 'events': ev2, 'trails': trails}
os.makedirs(out, exist_ok=True)
json.dump(data, open(os.path.join(out, 'data.json'), 'w'), ensure_ascii=False, indent=1)
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html')).read()
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html = re.sub(r'/\*DATA-START\*/.*?/\*DATA-END\*/', lambda m: '/*DATA-START*/' + blob + '/*DATA-END*/', tpl, flags=re.S)
open(os.path.join(out, 'index.html'), 'w').write(html)
print('wrote', out)
