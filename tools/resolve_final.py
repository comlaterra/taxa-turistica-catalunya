import re, json, collections

def load(fn):
    rows=[]
    for line in open(fn):
        p=line.rstrip('\n').split('\t')
        if len(p)>=4: rows.append((int(p[0]),float(p[1]),float(p[2]),p[3]))
    return rows
r1=load('data/_bcn_ocr_raw.tsv'); r2=load('data/_bcn_ocr_numbers.tsv')

CANON=re.compile(r'^\d{1,3}(\.\d{3})*,\d{2}$')
def clean(t):
    s=t.split('€')[0].strip().rstrip('|/').strip()
    return s
def canon_val(t):
    s=clean(t)
    if CANON.match(s):
        return int(s.replace('.','').replace(',',''))/100.0
    return None

def imports(rows):
    d=collections.defaultdict(list)
    for (pg,x,y,t) in rows:
        if 0.70<=x<0.79 and '€' in t: d[pg].append((y,t))
    for pg in d: d[pg].sort()
    return d
i1=imports(r1); i2=imports(r2)

def names(rows):
    d=collections.defaultdict(list)
    for (pg,x,y,t) in rows:
        if x<0.27 and t.strip() and t.strip().lower()!='nom projecte': d[pg].append((y,t.strip()))
    return d
nm=names(r1)
def codes(rows):
    d=collections.defaultdict(list)
    for (pg,x,y,t) in rows:
        if x>=0.90 and re.fullmatch(r'[A-ET]',t.strip()): d[pg].append((y,t.strip()))
    return d
cd=codes(r1)

projects=[]; flags=[]
for pg in sorted(i1):
    l2=i2.get(pg,[])
    # name buckets by nearest import y (pass1 imports as anchors)
    anchors=[y for (y,_) in i1[pg]]
    buck=collections.defaultdict(list)
    for (yn,tn) in nm.get(pg,[]):
        if not anchors: continue
        k=min(range(len(anchors)),key=lambda i:abs(anchors[i]-yn)); buck[k].append((yn,tn))
    for k,(y1,t1) in enumerate(i1[pg]):
        v1=canon_val(t1)
        # matched pass2
        t2=None; v2=None
        if l2:
            j=min(range(len(l2)),key=lambda i:abs(l2[i][0]-y1))
            if abs(l2[j][0]-y1)<0.02: t2=l2[j][1]; v2=canon_val(t2)
        if v1 is not None and v2 is not None and v1!=v2:
            final=None; status='flag-both-canon'
        elif v1 is not None:
            final=v1; status='ok'
        elif v2 is not None:
            final=v2; status='ok'
        else:
            final=None; status='flag-none'
        name=' '.join(t for _,t in sorted(buck.get(k,[]),key=lambda z:-z[0])).strip()
        code=None
        if cd.get(pg):
            cc=min(cd[pg],key=lambda z:abs(z[0]-y1))
            if abs(cc[0]-y1)<0.03: code=cc[1]
        rec={'page':pg,'y':round(y1,3),'name':name,'code':code,'amount':final,
             'raw1':clean(t1),'raw2':clean(t2) if t2 else None,'status':status}
        projects.append(rec)
        if final is None: flags.append(rec)

ok=[p for p in projects if p['amount'] is not None]
tot=sum(p['amount'] for p in ok)
print(f"Total files: {len(projects)} | resoltes: {len(ok)} | a verificar visualment: {len(flags)}")
print(f"Suma resolta: {tot:,.2f} € ({tot/1e6:.2f} M€)")
print(f"\n--- A VERIFICAR (cap passada canònica) ---")
for f in flags:
    print(f"  p{f['page']:>2} y={f['y']}  raw1={f['raw1']!r} raw2={f['raw2']!r}  | {f['name'][:55]}")
json.dump(projects, open('data/_bcn_projects_resolved.json','w'), ensure_ascii=False, indent=1)
print("\nsaved data/_bcn_projects_resolved.json")
