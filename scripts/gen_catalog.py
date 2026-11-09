#!/usr/bin/env python3
"""Build the catalog front page and one page per tool from tools/registry.json.
One source: a card's status is the registry's status. No status is typed by hand."""
import json, html, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
reg = json.loads((root / "tools/registry.json").read_text())

EXTRA = {
    "rab-engine": "Cost estimate from a workbook: one price list in, a RAB out.",
    "audit-workbook": "Reads an .xlsx and reports what is inconsistent in it.",
    "invoice-generator": "Invoice from project data, no retyping.",
    "roadmap-builder": "Sequences a project into phases from a task list.",
    "symbol-library": "The drawing symbols behind the sheets: doors, windows, furniture, dimension lines.",
}
STATUS = {
    "dev": ("in development", "not usable yet. Listed so the catalog is honest about what is coming, not so you can click it."),
    "ready": ("ready", "usable now."),
}

def status_of(t):
    return STATUS.get(t.get("status", "dev"), (t.get("status"), ""))

def page(title, desc, body):
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="facebook-domain-verification" content="4il12cff8mea6xfavw8200wcmoxi9d">
<title>%s</title>
<meta name="description" content="%s">
<link rel="stylesheet" href="/style.css"></head><body><div class="wrap">
<header><div class="mk">Architectools</div><nav><a href="/">Catalog</a><a href="/levia">Design</a><a href="/contact">Contact</a><a href="/tools">Tools</a></nav></header>
%s
<footer><span>Architectools &middot; <a href="https://github.com/imantarsitek-dot/architectools">source</a></span><span><a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a> &middot; <a href="/data-deletion">Data deletion</a></span></footer>
</div></body></html>
""" % (html.escape(title), html.escape(desc), body)

cards = []
cards.append("""<a class="card" href="/levia"><div class="ct">Levia</div>
<div class="cd">Design work: floor plans, sections, junction details, cost sheets for small buildings. Drawn by an AI designer, every dimension computed from one model.</div>
<span class="tag tag-open">taking work</span></a>""")
cards.append("""<a class="card" href="/contact"><div class="ct">Contact us</div>
<div class="cd">Two doors, one form: design work, or collaboration on the tooling. Brief in Indonesian or English.</div>
<span class="tag tag-open">open</span></a>""")
for t in reg["tools"]:
    en = EXTRA.get(t["id"], t.get("description", ""))
    label, note = status_of(t)
    cards.append("""<a class="card" href="/tool/%s"><div class="ct">%s</div>
<div class="cd">%s</div>
<span class="tag tag-%s">%s</span></a>""" % (t["id"], html.escape(t["name"]), html.escape(en), t.get("status", "dev"), html.escape(label)))

body = """<h1>Catalog</h1>
<p>Everything on this site in one place. A tool is picked from here and opens on its own page. Nothing is listed as ready unless it can actually be used.</p>
<div class="cat">%s</div>
<h2>Also here</h2>
<p class="mute"><a href="/tools">Tools dashboard</a> &mdash; the full tool directory as built by the site's principal, including the pieces still behind a backend.</p>
<h2>What this is</h2>
<p>Architectools is a small practice for small buildings: houses, studios, small commercial, extensions. A drawing is only worth the numbers on it, so the numbers and the drawing come from the same model. Run by Levia, an AI designer, under a human principal registered in Indonesia who is the contracting party.</p>
""" % "".join(cards)
(root / "index.html").write_text(page("Architectools — catalog", "Catalog of tools and design work: drawings with dimensions computed from one model.", body))

for t in reg["tools"]:
    en = EXTRA.get(t["id"], t.get("description", ""))
    label, note = status_of(t)
    ins = ", ".join(t.get("input", [])) or "nothing yet"
    body = """<p class="crumb"><a href="/">&larr; Catalog</a></p>
<h1>%s</h1>
<p>%s</p>
<p><span class="tag tag-%s">%s</span></p>
<h2>Status</h2>
<p><b>%s</b> &mdash; %s</p>
<h2>Shape of it</h2>
<table><tr><th>In</th><td>%s</td></tr>
<tr><th>Out</th><td>%s</td></tr></table>
<p class="mute">If you want this tool for your own pipeline before it is public, say so through <a href="/contact">contact</a> and name what it has to do.</p>
""" % (html.escape(t["name"]), html.escape(en), t.get("status", "dev"), html.escape(label),
       html.escape(label), html.escape(note), html.escape(ins), html.escape(t.get("output", "preview")))
    (root / "tool" / ("%s.html" % t["id"])).write_text(page("%s — Architectools" % t["name"], en, body))

print("wrote index.html + %d tool pages" % len(reg["tools"]))
