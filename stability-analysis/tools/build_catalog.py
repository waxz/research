#!/usr/bin/env python3
"""Build CATALOG.md and catalog.csv from catalog.json, optionally downloading or checking PDFs.

Usage (from the collection folder, e.g. robot-learning-control/):
    python3 tools/build_catalog.py             # regenerate CATALOG.md and catalog.csv
    python3 tools/build_catalog.py --download  # also fetch missing local copies for entries with "pdf": true
    python3 tools/build_catalog.py --check     # verify that non-arXiv online PDF links return a PDF

catalog.json is the single source of truth: edit it, then rerun this script.

Each entry may have:
    "arxiv":   arXiv ID          -> abstract link, and https://arxiv.org/pdf/<id> as its online PDF
    "url":     landing page/DOI  -> "link"; used as the online PDF if it ends in .pdf
    "pdf_url": open PDF anywhere -> online PDF (overrides the two defaults above)
    "pdf":     true              -> keep a local copy in papers/<category>/<key>.pdf (downloaded from the online PDF)
"""
import csv
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
UA = {"User-Agent": "Mozilla/5.0 (research-catalog builder)"}


def online_pdf(p):
    if p.get("pdf_url"):
        return p["pdf_url"]
    if p.get("arxiv"):
        return f"https://arxiv.org/pdf/{p['arxiv']}"
    if p.get("url", "").lower().endswith(".pdf"):
        return p["url"]
    return None


def pdf_path(p):
    return PAPERS / p["cat"] / f"{p['key']}.pdf"


def links(p):
    out = []
    if pdf_path(p).exists():
        out.append(f"[PDF](papers/{p['cat']}/{p['key']}.pdf)")
    if online_pdf(p):
        out.append(f"[PDF ↗]({online_pdf(p)})")
    if p.get("arxiv"):
        out.append(f"[arXiv](https://arxiv.org/abs/{p['arxiv']})")
    if p.get("url") and p.get("url") != online_pdf(p):
        out.append(f"[link]({p['url']})")
    return out


def fetch(url, nbytes=None):
    headers = dict(UA)
    if nbytes:
        headers["Range"] = f"bytes=0-{nbytes - 1}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120) as r:
        return r.read(nbytes) if nbytes else r.read()


def download(papers):
    for p in papers:
        src = online_pdf(p)
        if not (p.get("pdf") and src):
            continue
        dest = pdf_path(p)
        if dest.exists():
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"fetch {p['key']} <- {src}")
        data = fetch(src)
        if not data.startswith(b"%PDF"):
            raise SystemExit(f"{p['key']}: response is not a PDF")
        dest.write_bytes(data)
        time.sleep(3)  # be polite to servers


def check(papers):
    bad = 0
    for p in papers:
        src = online_pdf(p)
        if not src or p.get("arxiv") and not p.get("pdf_url"):
            continue  # arXiv PDF links follow from IDs already checked against the arXiv API
        try:
            ok = fetch(src, 8).startswith(b"%PDF")
        except Exception as e:  # network errors are reported, not fatal
            ok, src = False, f"{src} ({str(e)[:50]})"
        print(("ok   " if ok else "FAIL ") + f"{p['key']}: {src}")
        bad += not ok
    print(f"{bad} online PDF link(s) failed")


def write_catalog(cats, papers):
    by_cat = {c["id"]: [] for c in cats}
    for p in papers:
        by_cat[p["cat"]].append(p)
    n_local = sum(1 for p in papers if pdf_path(p).exists())
    n_online = sum(1 for p in papers if online_pdf(p))

    lines = [
        "# Paper catalog",
        "",
        f"{len(papers)} entries in {len(cats)} categories. **{n_online}** have a PDF available online (PDF ↗) and "
        f"**{n_local}** also have a local copy in this repository (PDF).",
        "Generated from `catalog.json` by `tools/build_catalog.py`. Do not edit by hand.",
        "",
        "| Category | Entries | PDF online | Local PDF |",
        "|---|---:|---:|---:|",
    ]
    for c in cats:
        ps = by_cat[c["id"]]
        lines.append(f"| [{c['name']}](#{c['id']}) | {len(ps)} | {sum(1 for p in ps if online_pdf(p))} | "
                     f"{sum(1 for p in ps if pdf_path(p).exists())} |")
    lines.append("")

    for c in cats:
        lines += [f"<a id=\"{c['id']}\"></a>", f"## {c['name']}", "", c["about"], "",
                  "| Year | Paper | Venue | Links | Why it is here |", "|---:|---|---|---|---|"]
        for p in sorted(by_cat[c["id"]], key=lambda p: (p["year"], p["key"])):
            lines.append(f"| {p['year']} | **{p['title']}**<br>{p['authors']} | {p['venue']} | {' · '.join(links(p))} | {p['note']} |")
        lines.append("")
    (ROOT / "CATALOG.md").write_text("\n".join(lines))

    with open(ROOT / "catalog.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["key", "category", "year", "title", "authors", "venue", "arxiv", "url", "online_pdf", "local_pdf", "note"])
        for p in papers:
            local = f"papers/{p['cat']}/{p['key']}.pdf" if pdf_path(p).exists() else ""
            w.writerow([p["key"], p["cat"], p["year"], p["title"], p["authors"], p["venue"],
                        p.get("arxiv", ""), p.get("url", ""), online_pdf(p) or "", local, p["note"]])


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
    if "--check" in sys.argv:
        check(papers)
    write_catalog(cats, papers)
    print(f"wrote CATALOG.md and catalog.csv ({len(papers)} entries)")


if __name__ == "__main__":
    main()
