# Katalog Tools untuk UI — Architectools

Dibuat: 31 Okt 2026. Sumber: repo Arsitek (imantarsitek-dot/Arsitek).
Klasifikasi berdasarkan kemampuan hosting statis (Vercel / GitHub Pages) tanpa backend.

---

## TIER A — Siap dilihat sekarang (artefak statis, tinggal di-embed)

| Tools | Artefak | Lokasi sumber |
|---|---|---|
| Symbol Library | `symbols.svg` (pintu, jendela, furnitur, sanitair, dim line, scale bar, title block) | Arsitek/tools/symbol-library |
| Denah latihan Levia | `practice_plan.svg` | Arsitek/tools/symbol-library |
| Roadmap Fase 1-5 | `Fase_1.png`, `Fase_2-5.png`, `Ringkasan.png`, `Riset_Google_AI.png` | Arsitek/tools/roadmap |
| Denah Flint (Grok) | output `denah_flint.py` + `site_map_flint.py` (SVG) | Arsitek/tools/grok-build/denah-flint |
| Office Flint 7x20 | plan + front elevation (SVG) | Arsitek (commit 29 Okt) |

Semua bisa langsung ditampilkan sebagai galeri SVG/PNG. SVG juga bisa jadi input
untuk viewer interaktif (zoom/pan) dengan JS kecil tanpa backend.

## TIER B — Bisa dilihat dengan JS ringan (render data yang sudah ada)

| Tools | Data | Bentuk UI |
|---|---|---|
| Hasil test RAB engine | `hasil_test/LAPORAN-BATCH.csv`, folder cipageran & dt-house | Tabel hasil + rekap, statistik pass/fail |
| RAB projects | `projects/cipageran`, `projects/dt-house` | Tabel RAB per proyek, subtotal/PPN/grand total, rekap zona |
| Digest | `rab_digest.json` per proyek | Tree-view struktur RAB (kunci item, zona, rumus) |
| Audit 1.01 | `Arsitek_Roadmap...inspect.ndjson`, output inspect_structure.py | Laporan temuan audit, badge status per sheet |
| Roadmap builder | `Arsitek_Roadmap_Fase_1-5.xlsx` → ekspor JSON/CSV | Timeline fase interaktif |

Catatan: file hasil Python tidak perlu backend untuk dilihat — cukup hasil ekspor
(CSV/JSON) ikut di-commit, lalu UI merender sebagai tabel/chart client-side.
Compute tetap di lokal (gratis), situs hanya menampilkan.

## TIER C — Butuh backend (serverless function / porting JS)

| Tools | Alasan |
|---|---|
| RAB Engine (rab_engine.py, batch_runner.py) | Perhitungan Python — jalankan di serverless atau port ke JS |
| Digest builder (xl_reader.py + digest_builder.py) | Baca .xlsx — untuk upload-file-di-web perlu backend; versi lokal tetap gratis |
| Invoice generator (arsitek_invoice.py) | Compute Python — atau jadi form JS yang men-generate unduhan |

Rekomendasi: TIER C jangan diburu-buru. Kebutuhan saat ini (vitrin + dokumen
untuk promo/klien) sudah terpenuhi TIER A+B. Backend baru saat ada klien yang
butuh compute langsung di web.

---

## Struktur halaman yang disarankan

1. **Beranda** — kartu tools dengan badge tier (A/B/C) & status (siap / data tersedia / butuh backend)
2. **Galeri Denah** — SVG Levia & Flint (zoom, skala, title block)
3. **RAB Viewer** — tabel proyek (dt-house, cipageran) + LAPORAN-BATCH
4. **Audit** — temuan audit 1.01, badge per sheet
5. **Roadmap** — timeline fase 1-5
6. **Symbol Library** — grid simbol arsitektur

## Pembaruan status tim (31 Okt 2026)

- Bergabung: hermes (manajer/persona tracker), MiniMax (handoff digest), antigravity
- Levia: siap jadi tenaga arsitek — gambar denah via SVG (method terbukti)
- OpenClaw: pensiun
- GPT: membangun HTML untuk Vercel (repo ini)
