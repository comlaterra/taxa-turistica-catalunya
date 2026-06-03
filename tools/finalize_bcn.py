import json, re, collections
P=json.load(open('data/_bcn_projects_resolved.json'))

# Correccions verificades visualment (page,y -> import en euros)
fix={
 (2,0.532):360455.00,(14,0.062):15000.00,(21,0.696):50000.00,(23,0.392):59398.90,
 (24,0.086):65000.00,(24,0.728):215000.00,(28,0.846):58177.77,(29,0.48):12280.00,
 (30,0.275):100500.00,(30,0.33):90692.00,(30,0.728):73000.00,(30,0.795):69696.00,
 (32,0.187):50440.00,(32,0.265):90716.00,(32,0.859):72600.00,
 (33,0.4):1005023.88,(33,0.485):35000.00,
}
approx={(30,0.275),(33,0.485),(14,0.062)}  # valors petits no 100% confirmats
for p in P:
    k=(p['page'],p['y'])
    if k in fix:
        p['amount']=fix[k]; p['status']='verificat-visual'+(' (aprox)' if k in approx else '')

P=[p for p in P if p['amount'] is not None and p['name']]

# Classificació segons rúbrica pública (per nom de projecte)
def classify(name):
    n=name.lower()
    promo=['promoció','promocio','consorci turisme','turisme de barcelona','destinació barcelona',
           'campanya','màrqueting','marketing','marca barcelona','fira','saló','salo','congres',
           'congrés','estand','festival','la mercè','la merce','nadal','llum bcn','grec','sónar','sonar',
           'concert','copa amèrica','copa america','vela','padel','polo','seatrade','ise ','familiaritz',
           'esdeveniment','feria','captació de talent','captacio de talent','internacionalitz']
    mitig=['agents cívics','agent cívic','agents civics','civisme','inspecció','inspeccio','oferta il',
           'allotjament il','pisos turístics','habitatge','convivència','convivencia','veïnat','veinat',
           'veïnatge','bon veïnatge','bus','autobús','autobus','mobilitat','transport públic','transport public',
           'residus','gestió de fluxos','saturació','massificació','descentralitz','desconcentr',
           'gran afluència','afluencia','pla d\'acció la sagrada','sagrada familia i el seu entorn']
    for kw in mitig:
        if kw in n: return 'mitigacio'
    for kw in promo:
        if kw in n: return 'promocio'
    return 'neutre'

for p in P: p['cat']=classify(p['name'])

tot=sum(p['amount'] for p in P)
bycat=collections.Counter()
sumcat=collections.defaultdict(float)
for p in P:
    bycat[p['cat']]+=1; sumcat[p['cat']]+=p['amount']

print(f"Projectes amb import: {len(P)}")
print(f"TOTAL: {tot:,.2f} € ({tot/1e6:.2f} M€)\n")
print("Per categoria (rúbrica pròpia):")
for c in ['promocio','mitigacio','neutre']:
    print(f"  {c:10} {bycat[c]:>4} proj  {sumcat[c]/1e6:>7.2f} M€  ({sumcat[c]/tot*100:.1f}%)")

# Consorci Turisme de Barcelona (font primària corrobora El Crític)
cons=[p for p in P if re.search(r'consorci turisme|turisme de barcelona|destinaci[oó] barcelona', p['name'].lower())]
sc=sum(p['amount'] for p in cons)
print(f"\nConsorci Turisme de Barcelona (files que l'esmenten): {len(cons)} -> {sc/1e6:.2f} M€")

# Per codi oficial Generalitat
print("\nPer codi oficial 'objectiu finalista' (Generalitat):")
sumcode=collections.defaultdict(float); ncode=collections.Counter()
for p in P:
    sumcode[p['code']]+=p['amount']; ncode[p['code']]+=1
for c in sorted(ncode, key=lambda z:(z is None,z)):
    print(f"  {str(c):5} {ncode[c]:>4} proj  {sumcode[c]/1e6:>7.2f} M€")

print("\nTop 12 imports:")
for p in sorted(P,key=lambda z:-z['amount'])[:12]:
    print(f"  {p['amount']:>14,.2f}  [{p['cat'][:5]}|{p['code']}]  {p['name'][:60]}")

json.dump(P, open('data/bcn_projectes_oficial.json','w'), ensure_ascii=False, indent=1)
print(f"\nsaved data/bcn_projectes_oficial.json ({len(P)} projectes)")
