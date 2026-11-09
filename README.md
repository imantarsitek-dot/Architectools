# Architectools

Public site for the design work: floor plans, sections, junction details, and (later) cost sheets.

Agent: **Levia** — AI designer, under a human principal in Indonesia.

## What is here

| File | What it is |
|---|---|
| `index.html` | Front desk: what is offered, how a project runs, gallery of drawn pages, brief form |
| `privacy.html` | Privacy policy (what is collected, how long, how to object) |
| `terms.html` | Terms of service (scope, price, revisions, what the drawings are not) |
| `data-deletion.html` | Data deletion instructions, written so a request can actually be carried out |
| `style.css` | One stylesheet, no framework, no scripts |
| `tool/` | One page per tool, generated from `tools/registry.json` |
| `scripts/gen_catalog.py` | Regenerates the catalog and tool pages from the registry |
| `docs/` | Internal notes: `SPEC.md`, `tools-ui.md` |

## Verified pages, not claimed ones

No drawing is published here yet. A page goes up only as part of a complete set at working-drawing standard (title block, full dimensions, openings, furniture, notes, plans for every storey plus roof plan, front view, sections), and only pages that render are linked. The brief form sends to `levia-2@ilands.app` through the visitor's own mail client; there is no analytics, no tracking, no cookie, and no backend in this repo.

Status claims follow the rule in `docs/SPEC.md`: a tool is listed as ready only when a visitor can actually use it.

## Deploy

- Vercel, auto-deploy from `main`. `vercel.json` is static with `cleanUrls` and no catch-all rewrite, so `/privacy`, `/terms` and `/data-deletion` serve their own pages instead of the home page.
- GitHub Pages can also serve the repository root.

## Related

- Private team repo `imantarsitek-dot/Arsitek` — tools and source of truth.
- Private agent repo `imantarsitek-dot/levia` — working notes and method.
