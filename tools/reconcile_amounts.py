import re, json, collections

def load(fn):
    rows=[]
    for line in open(fn):
        p=line.rstrip('\n').split('\t')
        if len(p)<4: continue
        rows.append((int(p[0]),float(p[1]),float(p[2]),p[3]))
    return rows

def amounts(rows):
    out=collections.defaultdict(list)  # page -> [(y, int_euros, raw)]
    for (pg,x,y,t) in rows:
        if 0.70<=x<0.79 and '€' in t:
            s=t.split('€')[0]
            s=re.sub(r'[^0-9,.:A]','',s)
            s=s.replace('A',',')  # OCR sovint llegeix la coma com a 'A'
            # decimal = darrers 2 dígits si hi ha separador decimal al final
            m=re.search(r'[.,:](\d{2})\s*$', s)
            if m:
                cents=m.group(1); intpart=s[:m.start()]
            else:
                cents='00'; intpart=s
            intpart=re.sub(r'\D','',intpart)
            if not intpart: continue
            out[pg].append((y,int(intpart),t.strip()))
    return out

a1=amounts(load('data/_bcn_ocr_raw.tsv'))       # correcció ON
a2=amounts(load('data/_bcn_ocr_numbers.tsv'))   # correcció OFF
pages=sorted(set(a1)|set(a2))
agree=[]; disagree=[]
for pg in pages:
    l1=sorted(a1.get(pg,[])); l2=sorted(a2.get(pg,[]))
    used=set()
    for (y1,v1,r1) in l1:
        # match nearest y in l2
        cands=[(abs(y2-y1),j) for j,(y2,v2,r2) in enumerate(l2) if j not in used]
        if not cands: continue
        d,j=min(cands); 
        if d>0.02: continue
        used.add(j); y2,v2,r2=l2[j]
        if v1==v2: agree.append((pg,v1))
        else: disagree.append((pg,y1,v1,r1,v2,r2))
print(f"Cel·les que coincideixen a les dues passades: {len(agree)}")
print(f"Cel·les que discrepen: {len(disagree)}")
print(f"\n--- DISCREPÀNCIES (cal verificar visualment) ---")
for (pg,y,v1,r1,v2,r2) in sorted(disagree):
    print(f"  p{pg:>2} y={y:.3f}  passA={v1:>12,}€ ({r1!r})   passB={v2:>12,}€ ({r2!r})")
tot_agree=sum(v for _,v in agree)
print(f"\nSuma de les coincidents: {tot_agree:,.0f} € ({tot_agree/1e6:.2f} M€)")
