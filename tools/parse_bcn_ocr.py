import csv, re, json, collections

rows=[]
with open('data/_bcn_ocr_raw.tsv') as f:
    for line in f:
        p=line.rstrip('\n').split('\t')
        if len(p)<4: continue
        rows.append((int(p[0]), float(p[1]), float(p[2]), p[3]))

def parse_amount(t):
    t=t.split('€')[0]
    t=re.sub(r'[^0-9,:.]', '', t)
    if not re.search(r'\d', t): return None
    t=t.replace('.','').replace(':','').replace(' ','')
    # keep last comma as decimal
    if ',' in t:
        head,_,dec=t.rpartition(',')
        head=head.replace(',','')
        t=head+'.'+dec
    try: return round(float(t),2)
    except: return None

AMOUNT_RE=re.compile(r'\d')
projects=[]
for page in sorted(set(r[0] for r in rows)):
    pr=[r for r in rows if r[0]==page]
    names=[(y,t) for (_,x,y,t) in pr if x<0.27 and t.strip() and t.strip().lower()!='nom projecte']
    imports=[]
    for (_,x,y,t) in pr:
        if 0.71<=x<0.785 and '€' in t:
            amt=parse_amount(t)
            if amt is not None: imports.append((y,amt,t))
    codes=[(y,t.strip()) for (_,x,y,t) in pr if x>=0.90 and re.fullmatch(r'[A-ET]', t.strip())]
    # assign each name fragment to nearest import by y
    buckets=collections.defaultdict(list)
    for (yn,tn) in names:
        if not imports: continue
        j=min(range(len(imports)), key=lambda k: abs(imports[k][0]-yn))
        buckets[j].append((yn,tn))
    for j,(yi,amt,raw) in enumerate(imports):
        nm=' '.join(t for _,t in sorted(buckets.get(j,[]), key=lambda z:-z[0])).strip()
        code=None
        if codes:
            kk=min(range(len(codes)), key=lambda k: abs(codes[k][0]-yi))
            if abs(codes[kk][0]-yi)<0.03: code=codes[kk][1]
        projects.append({'page':page,'name':nm,'amount':amt,'code':code,'raw':raw.strip()})

# summary
tot=sum(p['amount'] for p in projects)
print(f"Projectes trobats: {len(projects)}")
print(f"Import total: {tot:,.2f} €  ({tot/1e6:.2f} M€)")
print(f"Amb nom buit: {sum(1 for p in projects if not p['name'])}")
print(f"\nDistribució per codi oficial (objectiu finalista):")
for c,n in collections.Counter(p['code'] for p in projects).most_common():
    s=sum(p['amount'] for p in projects if p['code']==c)
    print(f"  {c}: {n} projectes, {s/1e6:.2f} M€")
print(f"\nTop 15 imports:")
for p in sorted(projects,key=lambda z:-z['amount'])[:15]:
    print(f"  {p['amount']:>14,.2f}  [{p['code']}]  {p['name'][:70]}")
print(f"\nPossibles errors de parseig (import > 5M, revisar):")
for p in projects:
    if p['amount']>5_000_000:
        print(f"  p{p['page']}  raw={p['raw']!r}  -> {p['amount']:,.2f}  {p['name'][:50]}")
json.dump(projects, open('data/_bcn_projects_parsed.json','w'), ensure_ascii=False, indent=1)
print("\nsaved data/_bcn_projects_parsed.json")
