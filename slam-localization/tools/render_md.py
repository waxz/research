#!/usr/bin/env python3
"""Render a Markdown file (with $math$ and mermaid) into a single self-contained HTML page.

The Markdown stays the only source; the page embeds it and renders it in the
browser with marked (Markdown), MathJax (equations) and mermaid (diagrams).

    python3 render_md.py SRC.md OUT.html "Page title"              # standalone page
    python3 render_md.py SRC.md OUT.html "Page title" --fragment   # body fragment for hosts that add their own skeleton
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

HEAD = """<title>__TITLE__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,500;75..125,800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: a two-column reference book. A sticky recipe index on wide screens, one 72ch reading column;
   recipe headings carry a mono "R" number tab, worked examples and pitfalls are set apart by colour. */
:root {
  --bg: #f5f5f1; --paper: #ffffff; --ink: #1c1f1d; --muted: #5f6662; --rule: #d9ddd7;
  --accent: #3d4fb0; --accent-soft: #e8ebf8; --warm: #a85d0c; --warm-soft: #f7ecdc; --code-bg: #eef0ec;
  --display: "Archivo", "Helvetica Neue", Arial, sans-serif;
  --body: "Literata", Georgia, "Times New Roman", serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #111412; --paper: #181c1a; --ink: #e3e8e4; --muted: #98a19c; --rule: #2d3430;
    --accent: #95a4f3; --accent-soft: #1f2545; --warm: #efa652; --warm-soft: #3a2a16; --code-bg: #202623;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #111412; --paper: #181c1a; --ink: #e3e8e4; --muted: #98a19c; --rule: #2d3430;
  --accent: #95a4f3; --accent-soft: #1f2545; --warm: #efa652; --warm-soft: #3a2a16; --code-bg: #202623;
  color-scheme: dark;
}
* { box-sizing: border-box; }
body { background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 17px; line-height: 1.62;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 64px; }
.layout { max-width: 1180px; margin: 0 auto; display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 40px; }
nav.toc { position: sticky; top: env(safe-area-inset-top, 0px); align-self: start; max-height: 100vh; overflow-y: auto; padding: 32px 0 24px; font-family: var(--mono); font-size: .74rem; line-height: 1.45; }
nav.toc .p { color: var(--muted); text-transform: uppercase; letter-spacing: .08em; margin: 14px 0 4px; font-size: .68rem; }
nav.toc a { display: block; color: var(--ink); text-decoration: none; padding: 2px 6px; border-radius: 3px; }
nav.toc a:hover, nav.toc a:focus-visible { background: var(--accent-soft); color: var(--accent); outline: none; }
main { min-width: 0; max-width: 74ch; padding-top: 36px; }
@media (max-width: 900px) { .layout { grid-template-columns: 1fr; } nav.toc { display: none; } main { margin: 0 auto; } }
h1, h2, h3 { font-family: var(--display); text-wrap: balance; line-height: 1.15; }
main > h1:first-child { font-size: clamp(2rem, 5vw, 3rem); font-weight: 800; font-stretch: 85%; margin: 0 0 .4rem; }
main h1 { font-size: 1.9rem; font-weight: 800; font-stretch: 88%; margin: 3.4rem 0 .6rem; padding-top: .8rem; border-top: 3px solid var(--ink); }
main h2 { font-size: 1.35rem; font-weight: 800; font-stretch: 92%; margin: 2.6rem 0 .5rem; scroll-margin-top: 12px; }
main h2 .rno { font-family: var(--mono); font-size: .8rem; font-weight: 500; color: var(--paper); background: var(--accent); padding: 2px 7px; border-radius: 3px; margin-right: 10px; vertical-align: 3px; }
main h3 { font-size: 1.05rem; }
p { margin: .7rem 0; }
a { color: var(--accent); text-underline-offset: 2px; }
strong { font-weight: 600; }
main > p:nth-of-type(1) em { color: var(--muted); }
ul, ol { padding-left: 1.4em; } li { margin: .25rem 0; }
li > p { margin: .3rem 0; }
hr { border: 0; border-top: 1px solid var(--rule); margin: 2.4rem 0; }
code { font-family: var(--mono); font-size: .86em; background: var(--code-bg); padding: 1px 4px; border-radius: 3px; }
pre { background: var(--code-bg); padding: 12px 14px; border-radius: 4px; overflow-x: auto; }
pre code { background: none; padding: 0; }
.tbl { overflow-x: auto; margin: 1rem 0; border: 1px solid var(--rule); border-radius: 4px; background: var(--paper); }
table { border-collapse: collapse; width: 100%; font-size: .88rem; line-height: 1.42; }
th, td { text-align: left; padding: 7px 11px; border-bottom: 1px solid var(--rule); vertical-align: top; }
th { font-family: var(--mono); font-size: .7rem; letter-spacing: .05em; text-transform: uppercase; color: var(--muted); font-weight: 500; background: var(--bg); }
tr:last-child td { border-bottom: 0; }
p.we { background: var(--warm-soft); border-left: 3px solid var(--warm); padding: 8px 14px; border-radius: 0 4px 4px 0; }
p.pit { color: var(--muted); font-size: .94rem; }
mjx-container[display="true"] { overflow-x: auto; overflow-y: hidden; max-width: 100%; padding: 4px 0; }
.mermaid { background: var(--paper); border: 1px solid var(--rule); border-radius: 4px; padding: 12px; overflow-x: auto; text-align: center; }
.loading { color: var(--muted); font-family: var(--mono); font-size: .85rem; }
</style>
<script>
  window.MathJax = { tex: { inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }, svg: { fontCache: 'local' }, startup: { typeset: false } };
</script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script>
"""

BODY = """<div class="layout">
  <nav class="toc" id="toc" aria-label="Recipes"></nav>
  <main id="book"><p class="loading">Rendering the cookbook…</p></main>
</div>
<script type="text/markdown" id="src">
__MARKDOWN__
</script>
<script>
(function () {
  var src = document.getElementById('src').textContent;
  var store = [];
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  // protect math from the Markdown parser
  src = src.replace(/\\$\\$([\\s\\S]+?)\\$\\$/g, function (_, m) { store.push('\\\\[' + esc(m) + '\\\\]'); return '@@M' + (store.length - 1) + '@@'; });
  src = src.replace(/\\$([^\\n$]+?)\\$/g, function (_, m) { store.push('\\\\(' + esc(m) + '\\\\)'); return '@@M' + (store.length - 1) + '@@'; });
  var html = marked.parse(src, { gfm: true });
  html = html.replace(/@@M(\\d+)@@/g, function (_, i) { return store[+i]; });
  var book = document.getElementById('book');
  book.innerHTML = html;
  function slug(t) { return t.trim().toLowerCase().replace(/[^\\p{L}\\p{N}\\s_-]/gu, '').replace(/\\s/g, '-'); }
  var toc = document.getElementById('toc');
  book.querySelectorAll('h1, h2').forEach(function (h) {
    h.id = slug(h.textContent);
    if (h.tagName === 'H1' && h !== book.firstElementChild) {
      var p = document.createElement('div'); p.className = 'p'; p.textContent = h.textContent; toc.appendChild(p);
    }
    if (h.tagName === 'H2') {
      var m = h.textContent.match(/^([A-Z]\\d+)\\.\\s*(.*)$/);
      if (m) { h.innerHTML = '<span class="rno">' + m[1] + '</span>' + h.innerHTML.replace(/^[A-Z]\\d+\\.\\s*/, ''); }
      var a = document.createElement('a'); a.href = '#' + h.id; a.textContent = m ? m[1] + ' · ' + m[2] : h.textContent; toc.appendChild(a);
    }
  });
  book.querySelectorAll('table').forEach(function (t) { var w = document.createElement('div'); w.className = 'tbl'; t.parentNode.insertBefore(w, t); w.appendChild(t); });
  book.querySelectorAll('p').forEach(function (p) {
    var s = p.firstElementChild;
    if (s && s.tagName === 'STRONG' && p.firstChild === s) {
      if (/^Worked example/.test(s.textContent)) p.className = 'we';
      if (/^Pitfalls/.test(s.textContent)) p.className = 'pit';
    }
  });
  book.querySelectorAll('pre code.language-mermaid').forEach(function (c) { var d = document.createElement('div'); d.className = 'mermaid'; d.textContent = c.textContent; c.parentNode.replaceWith(d); });
  var dark = document.documentElement.getAttribute('data-theme') === 'dark' || (!document.documentElement.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
  try { mermaid.initialize({ startOnLoad: false, theme: dark ? 'dark' : 'neutral' }); mermaid.run({ querySelector: '.mermaid' }); } catch (e) {}
  if (location.hash) { var t = document.getElementById(decodeURIComponent(location.hash.slice(1))); if (t) t.scrollIntoView(); }
  MathJax.startup.promise.then(function () { return MathJax.typesetPromise([book]); });
})();
</script>
"""


def main():
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    src, out, title = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    md = src.read_text().replace("</script", "<\\/script")
    head = HEAD.replace("__TITLE__", title)
    body = BODY.replace("__MARKDOWN__", md)
    if "--fragment" in sys.argv:
        out.write_text(head + body)
    else:
        out.write_text('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                       + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
    print("wrote", out)


if __name__ == "__main__":
    main()
