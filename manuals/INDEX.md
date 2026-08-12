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

**How YOU search it (no model involved) — added 2026-08-09:**

```
python3 tools/manuals-search.py "spark plug gap"        # whole fleet, ranked
python3 tools/manuals-search.py --machine drz400 "oil"  # one machine
python3 tools/manuals-search.py --list                  # what's in the corpus
```

`grep -rin manuals/text` still works and always will. The tool adds the three things grep
structurally cannot: it names **which machine** a hit belongs to, it **ranks** (a 1,341-page
owner's manual and a 7-page quick-ref no longer arrive in alphabetical order), and it matches
**document names** as well as contents. It prints each document's confidence marker from the
table below, so a 🟡/⚠️ hit arrives already flagged as maybe-not-your-unit.
⛔ **This is not Guru retrieval** — that is the separate, still-parked §A6 build.

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
| `g22a-2005-wiring` | Yamaha G22A **CHASSIS SPECIFICATIONS** (p. 10-3) + a duplicate of the wiring diagram (p. 11-1, `Y-509`) — service-manual scan | 1 | 🟡 dealer-hosted scan, file says 2003-2007 | yamahagolfcarsofca.com (a Yamaha *dealer*). Ingested 2026-08-12. ⛔ **NOT a re-sourced wiring diagram — the diagram was never missing.** `g22a-2005.pdf` **p. 43** is the same document (same `Y-509`, same page 11-1, same 16 callouts) and has been held since 2026-07-08, in better quality and WITH a text layer. `LINKS.md` spent 8 days chasing a gap the corpus did not have. **Kept only for the chassis spec table**, which neither `g22a-2005` nor `g22a-2005-ax2` contains. ⚠️ Image-only PDF — `pdftotext` returns 1 byte, so `text/g22a-2005-wiring.txt` is hand-written; its component legend is ✅ corroborated against `g22a-2005.txt`, its spec values are an explicitly flagged **model read of a scan** |
| `g22a-2005-ax2` | Yamaha Golf Car **G22-AX2** Owner/Operator Manual, 2006 (`1EJU0-100E1`) | 56 | 🟡 sibling variant, one year later | yamahagolfcars.com.au (3rd-party copy of genuine Yamaha file). Ingested 2026-08-04. **Secondary** — the `g22a-2005` gas manual above stays the card link. Kept because it is 9 pp longer and may cover assemblies the shorter one omits; compare before relying on it |
| `generac-7000exl` | **Generac Portable Products 7000EXL Extended Life Generator** — Owner's Manual | 24 | ✅ names "7000EXL" 23× | archive.org (`manualsbase-id-609002`). Ingested 2026-08-04. ⚠️ **GENERATOR ONLY — it defers all engine service to a separate engine owner's manual we do NOT hold**, so it carries no oil, spark-plug or air-filter spec. Finding that engine manual is the top open item on the card |
| `bronco-1989-lmc-catalog-fd88` | **LMC Truck parts catalog FD.88** — Ford Truck & Bronco 1980–96, 2026 Edition Vol. 2 | 180 | ✅ covers the '89 Bronco directly (many rows are Bronco-specific) | LMC Truck print/PDF catalog (Paul's copy, ingested 2026-08-03) |
| `bronco-1989-audio-motor2b` | **RetroSound Motor 2B — User Manual** (the installed head unit) | 26 | ✅ exact model, receipt-verified | help.retromanufacturing.com (official). Ingested 2026-08-09 |
| `bronco-1989-audio-din-install` | **RetroSound DIN Solutions — Installation & Assembly Manual** (rev. 3-12-25) | 12 | ✅ the DIN-opening mounting path this truck needs | help.retromanufacturing.com (official). Ingested 2026-08-09 |
| `bronco-1989-audio-speakers` | **Bolores audio — Infinity Kappa 63XF + 86CFX specifications** | — | 🟡 **COMPILED, not a PDF extraction** — see note | vendor + retailer pages (attributed line-by-line in the file). Compiled 2026-08-09 |

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
- **Bolores audio (added 2026-08-09):** the head unit is a **RetroSound Motor 2B**, established
  from the purchase receipt (order #116059, 2026-01-20) — *not* the "Liberty" the record carried
  for six months, which was an unverified inference from a December shopping thread. The Motor 2B
  manual is the authority for the two facts the amp/sub decision rests on: **front / rear /
  subwoofer pre-amp outputs**, a **separate amplifier turn-on lead**, and **25 W RMS × 4 into a
  rated 4-ohm load**. The DIN Solutions manual is here because this truck's dash was cut to a
  7×2" DIN opening by a previous owner (for a Pioneer MVH-P8200BT) and RetroSound publishes **no
  vehicle-specific listing for an '89 Bronco** — so the DIN sleeve + backstrap is the mounting
  path, not the usual shaft-and-bracket one.
- ⚠️ **`bronco-1989-audio-speakers` is the one file in `text/` that is NOT a `pdftotext` output.**
  Infinity/Harman block automated reads (product pages 410, shop + Crutchfield 403, ManualsLib's
  PDF endpoint 403), so their spec sheets could not be downloaded and the figures were compiled
  by hand with per-line attribution. The vendor PDFs are real and are queued as 📥 INGEST rows in
  `.private/service-records/bronco-1989/REFERENCE.md` (**not** `LINKS.md` — the Bronco exception
  in that file sends every Bolores link to its own workspace). A 403 is a bot block, not rot, so
  those PDFs will open in a browser: it's a manual-download job, not a dead end. If they ever land
  in `pdf/`, this file should be re-derived from them. Treat it as 🟡 vendor-published, never as
  first-party capture.

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

## 🚚 THE FLEET SWEEP — open workstream `[paul-stated 2026-08-05]`

**This resolves the sentence that got cut off at close-out on 2026-08-04** ("Bring our fleet
into…"), which was recorded rather than guessed. His words on 08-05:

> *"let's make sure we've looked at all these bookmarks and mined all the data for all the
> vehicles and everything else that could be useful… as well as looked across all my other iCloud
> for other manuals or anything else that we should be properly locating and consolidating like we
> did with the bolores bronco files that we found on my iCloud archives, and being sure that's all
> set up to be ingested and accessible in one place related to the vehicle."*

**Bolores is the worked example, and it is the ONLY one.** Measured 2026-08-05 across the 18
`vehicles.json` entries:

| | Count | |
|---|---:|---|
| Fleet entries | **18** | 7 vehicles · 10 equipment · 1 household system |
| Have a manual in this INDEX | **21 docs** | good coverage — this is the part that IS done |
| Have a `referenceLibrary` | **1** | `bronco-1989` only |
| Have a service-record directory | **5** | bronco · gti · tiguan · dr200s · drz400s |
| Have had their manual text **mined** | **1** | `bronco-1989`, 2026-08-05 |

**The three legs, in dependency order:**

1. **MINE what is already on disk.** `text/` holds **5.66 MB across 21 manuals** and, until
   2026-08-05, exactly none of it had been mined against open work. `tools/mine_parts_catalog.py`
   is the pattern — but note it is *catalogue-shaped* (part rows). A service manual needs a
   different miner (procedures + specs), so this is a build, not a re-run. **Cheapest leg, zero
   network, and it is where Bolores' wins came from.**
2. **SWEEP iCloud for what is not on disk yet.** The Bolores `_assets/` material was found in the
   iCloud archives, not on the web — so the same sweep across the other 17 entries is the obvious
   next seam. ⚠️ **Not yet scoped: nobody has looked.** Do not state a count until one exists.
3. **CONSOLIDATE per vehicle.** "Accessible in one place related to the vehicle" = give the fleet
   what `bronco-1989` has — a `referenceLibrary` entry and, where there is material,
   a `REFERENCE.md` + `SOURCES.md` pair. **The structure is already proven; it just has one
   occupant.**

> ⚠️ **Do NOT invent a fourth store for this.** The existing split holds fleet-wide: model-level →
> `manuals/` (this INDEX for files, `LINKS.md` for links) · machine-level →
> `.private/service-records/<id>/`. The whole reason those two files exist is that a third home was
> considered on 2026-08-04 and deliberately refused.

**The bookmark half is filed but NOT captured** — see `~/.claude/handoff/BOOKMARK-SWEEP.md`:
103 of 135 filed, **0 archived, 0 cleared**, and **11 of 27 Bronco links are already unreachable**.
Filing recorded that we knew about a link; it did not keep the page. That is the leg with a clock on it.

---

_To refresh: run `bash download.sh` (re-downloads any missing PDF), then_
_`for f in pdf/*.pdf; do pdftotext -q "$f" "text/$(basename "$f" .pdf).txt"; done`._
