#!/usr/bin/env python3
"""Build index.html from index.template.html + data/dataset.json, and emit data/dataset.csv.

Single source of truth = data/dataset.json. The page embeds the same data, so the
downloadable files and the page can never diverge. No external dependencies.
"""
import json, csv, io, pathlib

ROOT = pathlib.Path(__file__).parent
dataset = json.loads((ROOT / "data" / "dataset.json").read_text(encoding="utf-8"))

# 1) inject dataset into the page
tpl = (ROOT / "index.template.html").read_text(encoding="utf-8")
embedded = json.dumps(dataset, ensure_ascii=False, separators=(",", ":"))
html = tpl.replace("__DATASET__", embedded)

# inline the base64-embedded fonts so the page stays a single self-contained file
fonts_path = ROOT / "assets" / "fonts-embed.css"
if fonts_path.exists():
    html = html.replace("/*__FONTS__*/", fonts_path.read_text(encoding="utf-8"))
(ROOT / "index.html").write_text(html, encoding="utf-8")

# 2) emit a flat CSV (one tidy row per data point, with source)
buf = io.StringIO()
w = csv.writer(buf)
w.writerow(["block", "year_or_period", "concept", "category", "amount_eur", "source"])

rec = dataset["recaptacio"]
for r in rec["rows"]:
    w.writerow(["recaptacio", r["year"], "IEET (Generalitat)", "", f'{r["ieet"]:.2f}', "Excel oficial Empresa i Treball"])
    if r.get("sind_audit"):
        w.writerow(["recaptacio_auditada", r["year"], "IEET auditat", "", r["sind_audit"], "Sindicatura 34/2023"])
    if r.get("recarrec_bcn"):
        w.writerow(["recarrec_barcelona", r["year"], "Recàrrec municipal BCN", "", r["recarrec_bcn"], "Dades obertes (Socrata)"])

dist = dataset["distribucio_generalitat_2021"]
for it in dist["items"]:
    w.writerow(["distribucio_generalitat", 2021, it["dest"], it["category"], it["amount"], "Sindicatura 34/2023"])

bcn = dataset["barcelona"]["itemized"]
for it in bcn["items"]:
    w.writerow(["barcelona_recarrec", bcn["period"], it["concept"], it["category"], it["amount"], bcn["source"]])

(ROOT / "data" / "dataset.csv").write_text(buf.getvalue(), encoding="utf-8")

print("Built index.html ({:,} bytes) and data/dataset.csv".format(len((ROOT/'index.html').read_text())))
