#!/usr/bin/env python3
"""Build CATALOG.md and catalog.csv from catalog.json, optionally downloading arXiv PDFs.

Usage (from the robot-learning-control/ folder):
    python3 tools/build_catalog.py             # regenerate CATALOG.md and catalog.csv
    python3 tools/build_catalog.py --download  # also fetch missing PDFs for entries with "pdf": true

catalog.json is the single source of truth: edit it, then rerun this script.
"""
import csv
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"


def links(p):
    out = []
    if p.get("arxiv"):
        out.append(f"[arXiv](https://arxiv.org/abs/{p['arxiv']})")
    if p.get("url"):
        out.append(f"[link]({p['url']})")
    return out


def pdf_path(p):
    return PAPERS / p["cat"] / f"{p['key']}.pdf"


def download(papers):
    for p in papers:
        if not (p.get("pdf") and p.get("arxiv")):
            continue
        dest = pdf_path(p)
        if dest.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://arxiv.org/pdf/{p['arxiv']}"
        print(f"fetch {p['key']} <- {url}")
        data = urllib.request.urlopen(url, timeout=120).read()
        if not data.startswith(b"%PDF"):
            raise SystemExit(f"{p['key']}: response is not a PDF")
        dest.write_bytes(data)
        time.sleep(3)  # be polite to arXiv


def write_catalog(cats, papers):
    by_cat = {c["id"]: [] for c in cats}
    for p in papers:
        by_cat[p["cat"]].append(p)
    n_pdf = sum(1 for p in papers if pdf_path(p).exists())

    lines = [
        "# Paper catalog",
        "",
        f"{len(papers)} papers in {len(cats)} categories; {n_pdf} have a local PDF copy (open-access arXiv versions).",
        "Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.",
        "",
        "| Category | Papers | Local PDFs |",
        "|---|---:|---:|",
    ]
    for c in cats:
        ps = by_cat[c["id"]]
        local = sum(1 for p in ps if pdf_path(p).exists())
        lines.append(f"| [{c['name']}](#{c['id']}) | {len(ps)} | {local} |")
    lines.append("")

    for c in cats:
        lines += [f"<a id=\"{c['id']}\"></a>", f"## {c['name']}", "", c["about"], "",
                  "| Year | Paper | Venue | Links | Why it is here |", "|---:|---|---|---|---|"]
        for p in sorted(by_cat[c["id"]], key=lambda p: (p["year"], p["key"])):
            ref = links(p)
            if pdf_path(p).exists():
                ref.insert(0, f"[PDF](papers/{p['cat']}/{p['key']}.pdf)")
            lines.append(f"| {p['year']} | **{p['title']}**<br>{p['authors']} | {p['venue']} | {' · '.join(ref)} | {p['note']} |")
        lines.append("")
    (ROOT / "CATALOG.md").write_text("\n".join(lines))

    with open(ROOT / "catalog.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "category", "year", "title", "authors", "venue", "arxiv", "url", "local_pdf", "note"])
        for p in papers:
            local = f"papers/{p['cat']}/{p['key']}.pdf" if pdf_path(p).exists() else ""
            w.writerow([p["key"], p["cat"], p["year"], p["title"], p["authors"], p["venue"],
                        p.get("arxiv", ""), p.get("url", ""), local, p["note"]])


def main():
    data = json.loads((ROOT / "catalog.json").read_text())
    cats, papers = data["categories"], data["papers"]
    keys = [p["key"] for p in papers]
    if len(keys) != len(set(keys)):
        raise SystemExit("duplicate keys in catalog.json")
    known = {c["id"] for c in cats}
    for p in papers:
        if p["cat"] not in known:
            raise SystemExit(f"{p['key']}: unknown category {p['cat']}")
    if "--download" in sys.argv:
        download(papers)
    write_catalog(cats, papers)
    print(f"wrote CATALOG.md and catalog.csv ({len(papers)} papers)")


if __name__ == "__main__":
    main()
