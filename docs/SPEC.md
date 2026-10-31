# Architectools — Spec (untuk Mistral/GPT)

## Positioning
Architectools adalah **portal publik** (showcase) yang menampilkan tool-tool RAB/konstruksi dari repo Arsitek. Bukan full tools—hanya **preview/demo terbatas**. Tujuan: portfolio + dokumentasi, bukan eksekusi RAB penuh di browser.

## Tools yang ditampilkan
- RAB Engine — generate RAB dari paket/lantai (demo: screenshot/video + ringkasan)
- Audit Workbook — audit & map workbook Green House (demo)
- Invoice Generator — generate invoice (demo)
- Roadmap Builder — penyusun roadmap (demo)
- Symbol Library — library simbol (demo)

## Aturan untuk Mistral/GPT
- Jangan sentuh folder `tools/` implementasi asli di repo Arsitek (hanya registry + docs di sini).
- Jangan taruh API secret di frontend.
- Stack: HTML/CSS/JS statis (tanpa framework berat). Vercel auto-deploy dari `main`.
- Struktur yang diharapkan:
  - `index.html` (dashboard)
  - `tools/registry.json` (schema tools)
  - `docs/SPEC.md` (ini)
- Konvensi: nama file lowercase-kebab, CSS variables, responsive.
- Status tool: `planned | dev | demo | active`. Jangan klaim `active` kalau belum bisa dipakai.

## Input/Output (konseptual)
- Input: workbook/master harga (tidak diupload publik; demo pakai contoh)
- Output: preview (screenshot/video) + link ke repo/penjelasan, bukan file RAB penuh.

## Batasan
- Tidak ada auth, tidak ada backend publik di fase ini.
- Tidak ada pemrosesan data pengguna.
- Preview terbatas: maksimal 1 contoh per tool.
EOF