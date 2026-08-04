# Fernwood — equipment & vehicle manuals corpus

Reference materials for the fleet on the Vehicles card. Assembled 2026-07-08.

> **Companion file (added 2026-08-04): [`LINKS.md`](LINKS.md)** — fleet references we do **not** hold
> as files (videos, forum threads, vendor pages, and manuals found but not yet downloaded).
> **The discriminator is one question: is there a file on disk?** Yes → this INDEX. No → `LINKS.md`.
> That test is mechanical, so the two files cannot both claim the same document — which is the
> duplicate the FD.88 re-ingest produced on 2026-08-04. `LINKS.md` is also the **ingestion queue**:
> its 📥 rows move *here* once downloaded, and the move is the ingestion.

**Structure**
- `pdf/` — source PDFs. **Local-only / gitignored** (public repo; avoids republishing
  copyrighted manuals and keeps the repo lean). Re-fetch anytime with `download.sh`.
- `text/` — plain-text extraction of each PDF (`pdftotext`). **Committed.** This is the
  searchable substrate a future Garden Guru retrieval layer would read. Filename = the
  vehicles.json `id` (plus `-parts` / `-service` / `-engine` for secondary docs).

**How it reaches Garden Guru (today):** each item carries a `manual: {label, url}` link in
`vehicles.json`; `build-digest.py` copies it into the digest, so Guru can point a reader to
the right manual and the 📖 link shows on the card. Guru does **not** read the manual *text*
yet — that's the deferred retrieval step the `text/` corpus is staged for (kept out of the
digest to protect its ~57K/80K-token budget).

**Confidence convention** mirrors the maintenance blocks: ✅ exact model/year match ·
🟡 close-match (different year or combined-model manual, mechanically applicable) ·
⚠️ model unconfirmed (best-guess doc; verify against the unit).

---

## Vehicles

| id | Document | Pages | Match | Source (authority) |
|---|---|---|---|---|
| `gti-2016` | VW Golf / GTI / Golf R Owner's Manual — MY2016 US ed. (07.2015) | 1341 | ✅ | carworklog.com (3rd-party copy of the genuine VW US file) |
| `tiguan-2018` | VW Tiguan Owner's Manual — 2nd-gen, Ed. 05.2017 (PartNr 5NA…) | 341 | 🟡 exact generation, intl-English printing (1st-gen was 5N) | vwmanuals.org (3rd-party) |
| `f150-2006` | Ford F-150 Owner's Guide — 2006 (Ed. 1) | 336 | ✅ | opinautos.com mirror of the official Ford file (Ford's own CDN is browser-only) |
| `bronco-1989` | Ford Bronco **Quick-Reference** Operating Guide — 1988 | 7 | 🟡 quick-ref only, applies to the 1987–91 body | archive.org (enthusiast scan) |
| `dr200s-2017-service` | Suzuki **DR200SE Service Manual** (99500-…) | 262 | 🟡 service (not owner's) manual; DR200S unchanged across years. OCR text is sparse (scan). | djebel-club.ru (enthusiast archive) |
| `drz400s-2001-service` | Suzuki DR-Z400S/SM **Service Manual** — 2000–2009 | 431 | ✅ covers 2001 | archive.org (enthusiast archive) |
| `g22a-2005` | Yamaha Golf Car G22A (gas) Owner's/Operator Manual — LIT-19626-16 | 47 | ✅ gas variant | mygolfbuggy.com (3rd-party copy of genuine Yamaha file) |
| `bronco-1989-lmc-catalog-fd88` | **LMC Truck parts catalog FD.88** — Ford Truck & Bronco 1980–96, 2026 Edition Vol. 2 | 180 | ✅ covers the '89 Bronco directly (many rows are Bronco-specific) | LMC Truck print/PDF catalog (Paul's copy, ingested 2026-08-03) |

**Notes**
- **DR200S:** no clean owner's-manual PDF exists free; the 262-pg factory *service* manual is
  the richer doc and is what we hold. The card link stays the readable owner's-manual viewer
  at manua.ls (205 pp).
- **DR-Z400S:** the first archive.org hit was a 14-page front-matter excerpt — discarded in favor
  of the full 431-page 2000–2009 factory service manual (high value; bike is under active
  electrical/speedo repair).
- **Bronco:** the full 1989 owner's manual (328 pp) exists only behind ManualsLib's login/captcha
  (`manualslib.com/manual/231684`). The Bolores restoration already has 4 dedicated guides in
  `guides/`, so the owner's manual is the lowest-value doc in the fleet.
- **LMC catalog (FD.88):** the parts book for the Bolores restoration — LMC's *website* blocks
  automated reads (403, see the carpet research), so this local copy is the only queryable view of
  their part numbers and prices we have. ⚠️ **Prices expired 2026-08-03** (cover: "valid May 5 –
  Aug 3, 2026") — treat every price as approximate; part numbers and applications stay good.
  **Both the PDF and its extracted text are LOCAL-ONLY / gitignored** — unlike the manuals, this is
  a current commercial price catalog ("no part may be reproduced"), so its text doesn't go in the
  public repo. Not re-fetchable by `download.sh`; the source copy lives in Paul's Desktop/Claude
  drop (FD88.pdf). No `manual:` link in vehicles.json — it's a catalog, not an operating doc.

## Equipment

| id | Document | Pages | Match | Source (authority) |
|---|---|---|---|---|
| `kobalt-km2040x-06` | Kobalt 20" 40V Dual-Blade Mower — Use & Care Guide (item #0506586) | 22 | ✅ | pdf.lowes.com (official — Kobalt is Lowe's house brand) |
| `echo-pb7910t` | Echo PB-7910 H/T Backpack Blower — Operator's Manual | 52 | ✅ (combined H/T manual) | echo-usa.com (official) |
| `echo-pb250ln` | Echo PB-250LN Blower — Operator's Manual | 36 | ✅ | echo-usa.com (official) |
| `echo-pb250ln-parts` | Echo PB-250LN — Parts Catalog | 16 | ✅ | echo-usa.com (official) |
| `chainsaw-cs352` | Echo CS-352 Chainsaw — Operator's Manual | 60 | ✅ | echo-usa.com (official) |
| `chainsaw-cs352-parts` | Echo CS-352 — Parts Catalog | 23 | ✅ | echo-usa.com (official) |
| `chainsaw-ms290` | Stihl MS 290 / 310 / 390 — Instruction Manual (0458-209-0121-B) | 44 | ✅ (covers MS 290) | ssc.stihl.com (official) |
| `homelite-trimmer` | Homelite UT33600/UT33650 26cc String Trimmer — Operator's Manual | 44 | ✅ one manual covers curved (UT33600A) & straight (UT33650A); **UT33550A is not a real model — sticker ambiguity resolved** | manuals.ttigroupna.com (official) |
| `homelite-blower-vac` | Homelite UT26HBV 26cc Blower/Vac — Operator's Manual | 40 | ⚠️ unit has no sticker; UT26HBV is the best-match 26cc blower/vac (converts to vacuum) | manuals.ttigroupna.com (official) |
| `husqvarna-mower-engine` | Kawasaki **FR691V** Engine (FR651V/FR691V/FR730V) — Owner's Manual | 82 | ✅ engine confirmed — the authoritative maintenance doc | thdstatic.com (Home Depot CDN copy of the OEM Kawasaki manual) |
| `husqvarna-mower-yth24v54` | Husqvarna YTH24V54 54" Lawn Tractor — Operator's Manual | 60 | ⚠️ mower model unconfirmed; YTH24V54 is a best-guess 54"/24HP candidate | husqvarna.com (official) |

**Notes**
- **Husqvarna mower:** the exact Husqvarna model is still unread (sticker under seat / rear
  fender — see CLAUDE.md "Outstanding for Paul" #1). The **Kawasaki FR691V engine manual is the
  reliable maintenance anchor** regardless of the tractor SKU; the YTH24V54 tractor manual is a
  candidate held for reference. Once the model sticker is read, re-confirm and swap if needed.
- **Homelite blower/vac:** model inferred from body shape; specs already come from the shared
  26cc engine family (see the item's `researchNeeded`).
- **Echo PB-7910T:** no static parts-catalog PDF is published (Echo uses an interactive lookup);
  operator's manual only.

---

_To refresh: run `bash download.sh` (re-downloads any missing PDF), then_
_`for f in pdf/*.pdf; do pdftotext -q "$f" "text/$(basename "$f" .pdf).txt"; done`._
