# On va la taxa turística?

[![Pàgina en directe](https://img.shields.io/badge/web-en%20directe-f5c451)](https://comlaterra.github.io/taxa-turistica-catalunya/)
[![Llicència: CC0 1.0](https://img.shields.io/badge/llic%C3%A8ncia-CC0%201.0-3aaf6c)](LICENSE)
[![Contribucions: benvingudes](https://img.shields.io/badge/contribucions-benvingudes-e4572e)](CONTRIBUTING.md)

> **Quina part de la taxa turística catalana s'ha destinat, des de 2012, a _mitigar_ l'impacte
> del turisme i quina a _promoure'l_?**

Una pàgina-reportatge, ultra ràpida i sense dependències, que respon aquesta pregunta amb dades
públiques, verificades i reconstruïbles.

👉 **[Veure la pàgina en directe](https://comlaterra.github.io/taxa-turistica-catalunya/)**

## La troballa

A escala de **Catalunya, el percentatge exacte no es pot calcular** — i això _és_ la notícia. La
pròpia **Sindicatura de Comptes** (Informe 34/2023) constata que del 50% del Fons que gestiona la
Generalitat *«no es detalla ni s'especifica la finalitat»* de la despesa.

El que sí diuen les dades que _existeixen_:

- El fons es diu, literalment, **«de Foment del Turisme»** (foment = promoció).
- El 2021, de la part que gestiona la Generalitat, gairebé tot va a dos **ens de promoció**:
  l'Agència Catalana de Turisme (**34,2 M€**) i Circuits de Catalunya (**6,2 M€**).
- A **Barcelona**, on el recàrrec municipal sí es detalla, l'Assemblea de Barris calcula que el
  **90%** (81 M€ de 91) va a foment, amb **39 M€** a Turisme de Barcelona — el consorci dirigit
  pels hotelers — sense justificar-ne la finalitat.

## Com està fet

Un **únic `index.html` estàtic i autocontingut**: dades incrustades, gràfics **SVG fets a mà**,
zero llibreries, zero JavaScript de tercers, zero passos de _build_ per a qui el visita. Carrega
en menys de 100 ms i funciona fins i tot sense JavaScript.

```
index.html              Pàgina final, autocontinguda. GENERADA — no l'editis a mà.
index.template.html     Plantilla amb el marcador __DATASET__.
build.py                Injecta data/dataset.json a la plantilla i genera data/dataset.csv.
METODOLOGIA.md          Rúbrica de classificació, fonts i el límit honest del que no es pot saber.
data/
  dataset.json          Font de la veritat: cada xifra amb la seva procedència.
  dataset.csv           Les mateixes dades, planes, per descarregar. GENERADA.
  fonts.md              Totes les URL, font a font.
  verificacio.md        Registre de verificació d'enllaços (estat HTTP + data + què sosté cadascun).
  *.xlsx / *.pdf        Documents primaris descarregats (Generalitat, Sindicatura, Ajuntament).
```

## Les dades

La sèrie de recaptació prové de l'**Excel oficial de la Generalitat** (Empresa i Treball,
2012–2025), contrastada amb la **Sindicatura de Comptes**. El recàrrec de Barcelona, del **portal
de dades obertes**. El repartiment de Barcelona, de l'**Assemblea de Barris pel Decreixement
Turístic** (petició d'accés a la informació) i de mitjans com **El Crític** i **Públic**.

Totes les fonts estan **verificades** (HTTP 200) i documentades a
[`data/verificacio.md`](data/verificacio.md). Cap xifra de la pàgina surt d'enlloc que no sigui
[`data/dataset.json`](data/dataset.json).

La classificació **promoció / mitigació / neutre** segueix una rúbrica pública, explicada a
[`METODOLOGIA.md`](METODOLOGIA.md). És, inevitablement, editorial — i per això és **oberta a
discussió**: pots reclassificar qualsevol partida amb un PR argumentat.

## Executar localment

```bash
python3 build.py             # regenera index.html i data/dataset.csv
python3 -m http.server 8000  # i obre http://localhost:8000
```

No cal Node, ni npm, ni cap dependència. `index.html` també s'obre directament al navegador.

## Desplegament

El lloc es publica amb **GitHub Pages** servint l'arrel de la branca `master`. Qualsevol canvi a
`index.html` passa abans pel `build.py` i per un Pull Request (vegeu més avall).

## Contribuir

Tothom hi és benvingut, de dues maneres:

- **Sense tocar codi** — obre un [Issue](https://github.com/comlaterra/taxa-turistica-catalunya/issues/new/choose)
  amb un formulari senzill en català (demana una funcionalitat, reporta un error en una dada o
  fes una pregunta). Ens n'encarreguem nosaltres.
- **Fent el canvi tu** — **els canvis entren per Pull Request** (la branca `master` està
  protegida). Tota dada nova ha de portar font verificable.

Tens la guia completa a [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Llicència

**[CC0 1.0 Universal](LICENSE)** — domini públic. Pots copiar, modificar, distribuir i fer servir
aquest treball, fins i tot comercialment, **sense demanar permís ni atribuir res**.

Excepció d'abast: els **documents oficials** inclosos a `data/` (l'Excel de la Generalitat i els
PDF de la Sindicatura i de l'Ajuntament) pertanyen als seus organismes emissors i s'hi inclouen
només per a arxiu i verificació; conserven les seves condicions d'origen. La renúncia CC0 cobreix
**la nostra obra**: el codi, la compilació de dades (`dataset.json`), els gràfics i la
documentació.

---

Fet com a resposta a [una pregunta a X](https://x.com/joeldiazbrah/status/2061476681865384081).
Dades públiques; classificació editorial i oberta a discussió.

No som periodistes. Som gent que sap fer servir la intel·ligència artificial per construir coses
que, de tant en tant, tenen valor. Aquesta n'és una: les dades hi són i es poden verificar.
