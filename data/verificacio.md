# Registre de verificació de fonts

Última comprovació: **2026-06-03**. Mètode: petició HTTP (seguint redireccions) amb agent de
navegador; es registra el codi de la resposta final. Totes les fonts són públiques.

## Estat dels enllaços

| Estat | Font | Què sosté |
|-------|------|-----------|
| ✅ 200 | [Excel oficial IEET 2012–2025 (Empresa i Treball)](https://empresa.gencat.cat/web/.content/20_-_turisme/coneixement_i_planificacio/estadistiques/IEET/Cataluna/arxius/Informe-IEET-municipis-2012-2025.xlsx) | Sèrie de recaptació IEET 2012–2025 |
| ✅ 200 | [Pàgina d'estadístiques de l'IEET](https://empresa.gencat.cat/ca/treb_ambits_actuacio/turisme/professionals_turisme/emo_impost_establiments_turistics/estadistiques/) | Índex d'on penja l'Excel |
| ✅ 200 | [Sindicatura de Comptes — Informe 34/2023 (PDF)](https://www.sindicatura.cat/documents/36414/85841/2023_34_es.pdf) | Recaptació auditada 2016–2022; despesa 2021 per destinatari; cita sobre no-detall de finalitats |
| ✅ 200 | [Dades obertes — IEET per municipi i tipologia (q4sr-68c3)](https://analisi.transparenciacatalunya.cat/Hisenda/Impost-sobre-les-Estades-en-Establiments-Tur-stics/q4sr-68c3) | Recàrrec de Barcelona 2021–2025; detall per tipologia |
| ✅ 200 | [Dades obertes — IEET per marca turística (rn32-up9n)](https://analisi.transparenciacatalunya.cat/Hisenda/Impost-sobre-les-Estades-en-Establiments-Tur-stics/rn32-up9n) | Contrast per marca turística |
| ✅ 200 | [Assemblea de Barris pel Decreixement Turístic — «Ni solució ni gestió, només promoció»](https://assembleabarris.wordpress.com/2024/03/20/taxa-turistica-ni-solucio-ni-gestio-nomes-promocio-i-financament-de-turisme-de-barcelona/) | Anàlisi 2013–2022 via petició d'accés a la informació: 90% a foment; 39 M€ a Turisme de Barcelona no justificats |
| ✅ 200 | [El Crític — consorci hoteler / 39 milions](https://www.elcritic.cat/investigacio/un-consorci-dirigit-pels-hotelers-ha-rebut-39-milions-publics-de-la-taxa-turistica-195808) | Desglossament del recàrrec de Barcelona 2012–2022 |
| ✅ 200 | [Públic / Diari Públic — 90% a promoció](https://www.diaripublic.cat/90-recaptacio-taxa-turistica-barcelona-els-darrers-10-anys-s-destinat-promocio-turisme.html) | 90% (81 M€ de 91); classificació de l'Assemblea | 
| ✅ 200 | [Verificat — on van els diners](https://www.verificat.cat/on-van-els-diners-de-la-taxa-turistica-de-catalunya-i-el-recarrec-de-barcelona/) | Reforma 2025: 25% habitatge / 75% Fons |
| ✅ 200 | [Ajuntament de Barcelona — recàrrec IEET](https://ajuntament.barcelona.cat/turisme/en/tourism-barcelona/projects/municipal-surcharge-ieet) | Existència i calendari del recàrrec municipal |
| ✅ 200 | [Ajuntament de Barcelona — PDF de projectes (oct. 2025)](https://ajuntament.barcelona.cat/turisme/sites/default/files/2025-10/Projectes%20IEET%20fins%20a%2020251016.pdf) | Llista oficial de projectes finançats |
| ✅ 200 | [Ajuntament de Barcelona — nota de premsa juny 2025](https://ajuntament.barcelona.cat/premsa/2025/06/08/lajuntament-aprova-un-nou-paquet-d1164me-de-limpost-turistic-per-a-27-projectes-diferents/) | 11,64 M€ / 27 projectes |
| ✅ 200 | [Text refós de l'IEET (Economia)](https://economia.gencat.cat/web/.content/70_tributs/Normativa/Refoses/IEET.pdf) | Marc legal de l'impost i del Fons |
| ✅ 200 | [Govern — Reglament del Fons](https://govern.cat/salapremsa/notes-premsa/196648/govern-aprova-reglament-del-fons-al-foment-del-turisme) | Finalitats legals del Fons |

> Nota: `publico.es/public/...` redirigeix (301) a la URL canònica `diaripublic.cat`; per evitar
> el salt, citem directament la destinació final.

## Grounding de les xifres (no només enllaços, sinó extracció)

No ens limitem a enllaçar: les xifres clau s'han **extret directament del document primari**, no
de resums:

- **Sèrie de recaptació 2012–2025** — llegida de la fila *TOTAL CATALUNYA* de l'Excel oficial
  (full «Taules»), agregant semestres a anual. Contrastada amb la taula de recaptació per
  temporada de l'Informe 34/2023 de la Sindicatura (diferències <5%, explicades a la metodologia).
- **Despesa per destinatari 2021** — llegida de la taula de transferències del PDF de la
  Sindicatura: ACT **34.179.188 €**, Circuits de Catalunya **6.230.700 €**, Patrimoni Cultural
  10.500 €, etc.
- **Cita sobre la no-especificació de finalitats** — transcrita literalment del mateix PDF
  (apartat 2.2.3, p. 24–26): *«para el 50% restante del Fondo… el Comité bilateral no detalla ni
  especifica las actuaciones o finalidades concretas…»*.
- **Recàrrec de Barcelona 2021–2025** — agregat de l'API de dades obertes (columna de recàrrec
  municipal).
- **Repartiment de Barcelona 2012–2022** — xifres d'El Crític i de Públic/Assemblea (font
  secundària, atribuïda explícitament i marcada com a tal).

Els documents primaris descarregats es conserven a `data/` per a comprovació independent.
