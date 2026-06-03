# Metodologia

Aquest projecte respon, amb dades públiques i verificables, la pregunta: **quina part de la
taxa turística catalana s'ha destinat a mitigar l'impacte del turisme i quina a promoure'l, des
de 2012?**

La conclusió central és tan important com incòmoda: **a escala de Catalunya, el percentatge
exacte NO es pot calcular, perquè la Generalitat no publica la despesa del Fons per finalitat.**
Ho confirma la pròpia Sindicatura de Comptes. Aquesta opacitat no és un detall tècnic: és part
de la resposta.

## 1. Què és l'IEET i el Fons per al Foment del Turisme

- **IEET** — Impost sobre les Estades en Establiments Turístics. Creat per la **Llei 5/2012**
  (vigent des de l'1 de novembre de 2012) i regulat de nou per la **Llei 5/2017**.
- La recaptació està afectada a la **dotació del Fons per al Foment del Turisme**. El nom és
  literal: *foment* = promoció.
- **Recàrrec de Barcelona** — des de juny de 2021 l'Ajuntament de Barcelona aplica un recàrrec
  municipal propi sobre l'IEET, que **gestiona íntegrament al marge del Fons català**.

## 2. Fonts de dades (totes públiques)

| Dada | Font | Format | Cobertura |
|------|------|--------|-----------|
| Recaptació IEET (sèrie principal) | Generalitat, Dept. d'Empresa i Treball — *Informe IEET per municipis 2012-2025* | Excel | 2012 S2 – 2025 S1 |
| Recaptació IEET (auditada, contrast) | Sindicatura de Comptes — *Informe 34/2023* | PDF | 2016 – 2022 |
| Recaptació per període/municipi/tipologia + recàrrec | Portal de dades obertes (Socrata, `q4sr-68c3`) | API/CSV/JSON | 2017 – 2025 |
| Despesa del Fons per destinatari (2021) | Sindicatura de Comptes — *Informe 34/2023* | PDF | 2021 |
| Repartiment de Barcelona (itemitzat) | El Crític (investigació) | Article | 2012 – 2022 |
| Repartiment de Barcelona (% promoció) | Públic / Assemblea de Barris pel Decreixement Turístic | Article | 2013 – 2022 |
| Repartiment de Barcelona (narrativa oficial) | Ajuntament de Barcelona | Web/PDF | actual |
| Reforma 25% habitatge (2025) | Verificat | Article | 2025 |

Les URL concretes són a [`data/fonts.md`](data/fonts.md). Els documents primaris descarregats
(Excel i PDF de la Sindicatura) es conserven a `data/`.

## 3. Quina sèrie de recaptació fem servir i per què

Fem servir com a **sèrie principal l'Excel oficial d'Empresa i Treball** (TOTAL CATALUNYA per
semestre, agregat a anual), perquè és l'única font amb **metodologia homogènia per a tots els
anys 2012–2025**. Mostrem en paral·lel els **totals auditats de la Sindicatura (2016–2022)** com
a contrast.

Les diferències entre totes dues sèries són petites (de l'ordre de l'1–5 %) i s'expliquen per:

- criteri de **meritació vs caixa**,
- el **calendari d'autoliquidacions** (una temporada es liquida en semestres posteriors),
- arrodoniments.

`2012` i `2025` són **anys parcials** (mig any de dades) i es marquen sempre com a tals.

El **recàrrec de Barcelona** es mostra a part (no se suma a l'IEET base), perquè és un tribut
municipal diferent i de gestió separada. Les xifres del recàrrec provenen de Socrata i estan
arrodonides a milers.

## 4. La rúbrica de classificació (mitigació vs promoció)

Classificar despesa pública com a "mitigació" o "promoció" és, inevitablement, un acte
editorial. Per fer-lo **transparent i reproduïble**, fem servir **tres categories** i una regla
pública. Tota partida discutible es marca amb asterisc a la pàgina.

- **🔴 Promoció** — captar o atraure visitants: màrqueting i campanyes, fires, viatges de
  familiarització, ens i consorcis de promoció (ACT, Circuits de Catalunya, Turisme de
  Barcelona) i esdeveniments-aparador pensats per atraure turisme.
- **🟢 Mitigació** — reduir o gestionar l'impacte del turisme: agents cívics, reforç de transport
  públic, inspecció de pisos turístics, neteja i seguretat a zones saturades, habitatge i
  protecció de recursos sota pressió.
- **⚪ Neutre / mixt** — infraestructura genèrica, gestió administrativa i cultura ciutadana
  ambivalent que no encaixa clarament en cap bloc. La categoria existeix **per no sobre-afirmar**.

### Casos discutibles
Els festivals i esdeveniments culturals (Grec, Sónar, biennals) són el cas fronterer típic:
tenen valor ciutadà propi però també funcionen com a reclam turístic. Per defecte els situem a
**Neutre** llevat que el seu propòsit declarat sigui clarament d'aparador internacional (World
Padel Tour, Barcelona Obertura, Llum BCN → Promoció). Qualsevol pot reclassificar-los: el
dataset és obert.

## 5. El límit honest: el que NO es pot saber

La Sindicatura de Comptes (Informe 34/2023), fiscalitzant l'exercici 2021, conclou textualment:

> «para el 50% restante del Fondo, además de la aprobación del importe global, el Comité
> bilateral **no detalla ni especifica las actuaciones o finalidades concretas** a las que debe
> destinarse el importe.»

És a dir: **de la meitat del Fons que gestiona la Generalitat, la finalitat concreta de la
despesa no es fa pública.** Per això:

- **No** publiquem un percentatge mitigació-vs-promoció a escala de Catalunya: seria inventat.
- **Sí** mostrem un *proxy* sòlid: a qui es transfereixen els diners (exercici 2021). El gruix va
  a l'**ACT (34,2 M€)** i a **Circuits de Catalunya (6,2 M€)** — tots dos **ens de promoció**.
- **Sí** reconstruïm el desglossament real **a Barcelona**, on el recàrrec municipal sí es
  detalla.

## 6. Reproductibilitat

Totes les xifres viuen a [`data/dataset.json`](data/dataset.json), amb la font indicada a cada
bloc, i s'exporten també a [`data/dataset.csv`](data/dataset.csv). La pàgina (`index.html`)
incrusta aquestes mateixes dades; no hi ha cap xifra a la pàgina que no surti del dataset.
