# Com contribuir

Aquest projecte és **obert a tothom**. No cal demanar permís ni formar part de cap equip: si
veus un error, tens una dada millor o vols afinar una classificació, endavant.

Hi ha **dues maneres** de col·laborar:

## A · Demanar o avisar, sense tocar codi

No cal saber programar. Si tens una idea, vols una funcionalitat o has vist una dada que no
quadra, **obre un _Issue_**:

👉 https://github.com/comlaterra/taxa-turistica-catalunya/issues/new/choose

Hi trobaràs formularis senzills en català (suggeriment, error en una dada, pregunta). Omple'ls amb
les teves paraules i ja ens n'encarreguem nosaltres.

## B · Fer el canvi tu mateix/a

Si vols editar dades, classificacions o codi, l'única regla de procés és aquesta:

> **Tots els canvis entren per _Pull Request_ (PR).** La branca `master` està protegida i no
> accepta canvis directes. Qualsevol persona pot obrir un PR.

## El flux, pas a pas

1. **Fes un _fork_** d'aquest repositori al teu compte.
2. **Crea una branca** descriptiva: `git checkout -b corregeix-recaptacio-2020`.
3. Fes els canvis (vegeu més avall on tocar).
4. **Obre un Pull Request** cap a `master`. Explica què canvies i, si toques dades, **enllaça la
   font**.
5. Es revisa i, si tot quadra, s'incorpora. Si cal discutir-ho, ho farem al mateix PR.

No fa falta cap aprovació especial per **obrir** un PR — el pots obrir tu sol. La protecció de
`master` només garanteix que res es publica sense passar per aquí.

## On tocar segons el que vulguis canviar

| Vols… | Edita | Després |
|-------|-------|---------|
| Corregir o afegir una **xifra** | `data/dataset.json` | executa `python3 build.py` |
| Reclassificar una partida (promoció/mitigació/neutre) | `data/dataset.json` (camp `category`) | `python3 build.py` |
| Afegir o revisar una **font** | `data/dataset.json` (bloc `sources`) + `data/fonts.md` + `data/verificacio.md` | `python3 build.py` |
| Canviar **text o disseny** de la pàgina | `index.template.html` | `python3 build.py` |
| Millorar la metodologia | `METODOLOGIA.md` | — |

> ⚠️ **No editis `index.html` ni `data/dataset.csv` directament**: són fitxers **generats**.
> La font de la veritat és `data/dataset.json`, i `python3 build.py` regenera la pàgina i el CSV.
> Així les dades de la pàgina i les descarregables no poden divergir mai.

## La regla d'or de les dades

**Tota dada nova o modificada ha de portar una font pública i verificable.** No s'accepten xifres
sense origen. Si una classificació és discutible (un festival, un esdeveniment…), marca-la com a
tal (`"debatable": true`) i argumenta-ho al PR: és preferible reconèixer l'ambigüitat que
sobre-afirmar.

## Provar-ho localment

```bash
python3 build.py            # regenera index.html i data/dataset.csv
python3 -m http.server 8000 # i obre http://localhost:8000
```

No cal Node, ni npm, ni cap dependència.

## To

Discrepar sobre on classificar un euro és, precisament, de què va aquest projecte. Es debat amb
dades i bona fe. Res de desqualificacions personals.
