# Architectools — Portal Tools Arsitek

Repo publik untuk situs **Architectools**: vitrin tools dan hasil kerja tim arsitek AI.
Agent utama: **Levia** (arsitek — denah via SVG), dengan tim: Grok, hermes, MiniMax, antigravity, GPT, Mistral.

## Struktur repo

- `index.html` — dashboard publik: Tool Directory (status per tools) + AI Workflow + Integrasi
- `docs/` — sitas GitHub Pages (privacy.html, data-deletion.html untuk verifikasi Meta/Google)
- `docs/tools-ui.md` — katalog resmi tools untuk UI (klasifikasi Tier A/B/C)
- `UI-TODO.md` — daftar tugas pengembangan UI berjalan

## Sumber tools

Semua tools, data, dan hasil kerja asli ada di repo privat `imantarsitek-dot/Arsitek`
(sumber kebenaran). Repo ini hanya vitrin — menampilkan hasil, bukan tempat kerja.

## Klasifikasi tools (ringkas)

| Tier | Arti | Contoh |
|---|---|---|
| A | Siap tampil — artefak statis | Galeri denah SVG, symbol library, roadmap |
| B | Data tersedia — render JS ringan | RAB viewer, batch test, audit 1.01, digest |
| C | Butuh backend | RAB engine, digest builder, invoice generator |

Rincian: lihat `docs/tools-ui.md`.

## Deploy

- Frontend: Vercel (auto-deploy dari main)
- Hosting alternatif: GitHub Pages (folder `docs/`)
- Secret/API key tidak disimpan di frontend — hanya di server/secret manager

## Prinsip

1. Situs hanya menampilkan hasil mesin (repo privat); tidak pernah lebih maju dari mesinnya.
2. Compute berat tetap lokal (gratis, deterministik); sitas hanya render.
3. Kebijakan model harian: GLM (Levia rutin), Grok (task banyak beres sekaligus), DeepSeek (spare token, tanpa jeda).

## Terkait

- Repo privat tim: `imantarsitek-dot/Arsitek` (tools, data, workflow)
- Repo privat agent: `imantarsitek-dot/levia` (persona, memori, kurikulum Levia)
- VAH: https://shimone666.github.io/vah-official/
