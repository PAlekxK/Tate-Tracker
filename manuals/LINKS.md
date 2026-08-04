# Fernwood — fleet REFERENCES we do not hold as files

Companion to `INDEX.md`. Established 2026-08-04. Fleet-wide, all machines — **not** per-vehicle.

---

## Why this file exists, and the one question that files a thing

A concurrent session flagged links as "a third resource type with no home yet." Having now read the
whole bookmark export, I'd put it differently, and the difference decides where things go:

> **The axis is SUBJECT, not FORMAT.** `manuals/` holds what is about **the model**;
> `.private/service-records/<id>/_assets/` holds what is about **this individual machine**. A URL is
> a format, not a subject. A YouTube teardown of the MK7 water pump is about the model, so it lives
> on the `manuals/` side of the existing line — it does not need a third line drawn.

So this is not a third store. It is the **second shelf of the same store**, and the discriminator
between the two shelves is one mechanical question:

> ### Is there a file on disk?
> **Yes → `INDEX.md`** (page count, match confidence, source).
> **No → here.**

That test can't produce the FD.88 duplicate, because a document cannot simultaneously be on disk and
not on disk. **A LINKS file that also listed manuals we hold would be exactly that mistake in a new
costume** — a second place that says where a manual is.

⚠️ **Check `INDEX.md` before adding a row here** — same standing rule, same reason.

### This file is also the ingestion queue

A manual we have found but not yet downloaded is a row **here**; downloading it moves the row to
`INDEX.md`. That migration *is* the ingestion, and it makes "known but not held" a visible state
rather than an invisible one. Rows marked **📥 INGEST** below are queued for exactly that.

### Tiers

Reused verbatim from `.private/service-records/bronco-1989/SOURCES.md` rather than invented here —
one vocabulary, one place it is defined:

**A** = document in hand (never applies in this file — by definition we hold no file) ·
**B** = corroborated, or Paul observed it first-hand · **C** = forum, video, owner account, single
vendor listing. **A useful seed, never load-bearing alone.** A **C** never silently becomes an **A**.

Almost everything here is **C**. That is the honest reading of a saved video: it records that a
stranger's machine behaved a certain way.

### ⚠️ Privacy — this file is COMMITTED to a PUBLIC repo

Only vehicle and equipment references may appear here. The bookmark export it was seeded from also
contains Finances, CCs, and Health folders; **none of that may ever reach this file.** The export
itself is not in this repo — see "Provenance" at the bottom.

---

## Small engines — Generac 7000EXL generator

Fleet context: the generator was added to `vehicles.json` on 2026-08-04 and is **decommissioned,
fully drained** (Paul). These five are the entire research basis for recommissioning it.

| Ref | Tier | What it is | What it does NOT settle |
|---|---|---|---|
| 📥 **INGEST** — [Generac 7000EXL user manual](https://archive.org/details/manualsbase-id-609002) · PDF: `archive.org/download/manualsbase-id-609002/609002.pdf` | — | The manual. Title verified against the archive.org metadata API 2026-08-04. **Queued for `INDEX.md`** — see BACKLOG B2 | Whether it matches our unit: `7000EXL` currently comes from bookmark titles, **not from the data plate** |
| [Generator won't start after sitting for years — Generac 7000EXL](https://www.youtube.com/watch?v=eJrhMdziZDk) | **C** | Model-specific, and the closest published case to ours | One person's machine. Not a procedure for ours |
| [How to start a generator that's been sitting too long](https://www.youtube.com/watch?v=oGq7ywlU2KY) | **C** | General long-storage restart | Not Generac-specific |
| [What to do when your Generac portable generator won't start](https://www.youtube.com/watch?v=Wmdj4eYM1AY) | **C** | Generac-brand troubleshooting | Not 7000EXL-specific |
| [How to start a portable generator — electric start](https://www.youtube.com/watch?v=6Uncapq6NMw&t=125s) | **C** | Electric-start procedure | — |

> **Where the manual and the videos disagree, the manual wins.** The videos are the informal half.

---

## Golf cart — Yamaha G22A (2005)

| Ref | Tier | What it is | What it does NOT settle |
|---|---|---|---|
| 📥 **INGEST** — [Yamaha G22-AX2 manual, 2006 (`1EJU0-100E1`)](https://www.yamahagolfcars.com.au/uploads/2/0/7/5/20756704/g22-ax2_ju03_2006_1eju0100e1.pdf) | — | Second G22 manual, AX2 variant. Secondary to the G22A gas manual already held | Whether it adds anything over the held manual — compare before ingesting |
| 🔴 **DEAD (404, checked 2026-08-04)** — G22A wiring diagram, cunninghamgolfcar.com | — | Was the only wiring diagram found for this cart. **Needs re-sourcing** | — |
| [Yamaha golf-cart model-year guide](https://hookupmycart.com/tech-center/yamaha-golf-cart-year-guide/) | **C** | Vendor year/model decoder | A vendor's table, not Yamaha's |
| [Oil in air cleaner, G9](https://buggiesgonewild.com/showthread.php?t=154878) | **C** | Forum thread on a **G9**, not a G22 | Different model. A seed only |

✅ The **G22A gas owner's manual** is already held — `INDEX.md`, `g22a-2005`, 47 pp, ✅ match. Do not
re-save it; it is the byte-identical trap.

---

## Motorcycles — Suzuki DR-Z400S (2001) · DR200S (2017)

| Ref | Tier | What it is | What it does NOT settle |
|---|---|---|---|
| 📥 **INGEST** — [Suzuki DR-Z400 2004 (K4) USA parts list + schematics](https://www.cmsnl.com/suzuki-dr-z400-2004-k4-usa-e03-drz400-dr-z400_model33970/partslist/) | — | **Parts fiche** — the complementary document to the service manual we hold. Rule 1 names parts catalogues as `manuals/` material | 2004 fiche vs our 2001 bike — confirm applicability per assembly, don't assume |
| 📥 **INGEST** — [Suzuki DR200SE 2009 (K9) USA parts list + schematics](https://www.cmsnl.com/suzuki-dr200se-2009-k9-usa-e03_model34019/partslist/) | — | Parts fiche for the DR200 | Same year-drift caveat |
| [Fix DRZ400S lean-running — adjustable fuel-mixture screw install](https://www.youtube.com/watch?v=qtvRgvzSdiU) | **C** | A known DRZ400S characteristic and a common fix | Whether **our** bike runs lean — nothing on the card says so |
| [Cleaning a motorcycle gas tank that sat 6 years](https://www.youtube.com/watch?v=LQq6W9PEzw0&t=66s) | **C** | Long-storage tank cleaning. Same failure family as the generator | Not model-specific |
| [DRZ400S rear rack — CycleRacks](https://cycleracks.com/products/suzuki-drz400s-rear-rack) | **C** | A vendor product page — **shopping, not reference** | Nothing. Kept only because it names a fitment |
| [DRZ400SM speedometer cluster, 11,876 mi — eBay](https://www.ebay.com/itm/186425305791) | **C** | A single expired-ish listing. `drz400s-2001` status names a **speedometer rebuild as next** | Whether it is still listed, or the right part. eBay URLs rot fast |

**Why the service manuals are not listed here:** both are held. `drz400s-2001-service` (431 pp, ✅)
and `dr200s-2017-service` (262 pp, 🟡) are `INDEX.md` rows.

---

## VW GTI (2016, MK7)

`gti-2016` currently has `techniques: null` while `dr200s-2017` uses that field for exactly this kind
of hands-on knowledge. These three are the raw material for filling it.

| Ref | Tier | What it is | What it does NOT settle |
|---|---|---|---|
| [MK7 water pump / thermostat housing — DIY](https://www.youtube.com/watch?v=RIVyvfEWztc) | **C** | The MK7's best-known failure item | That ours has failed |
| [MK7 coolant/oil leak behind the AC compressor](https://www.youtube.com/watch?v=ynfhJlnv46Y) | **C** | ⭐ Directly relevant: the card's status is *"Active — coolant leak diagnosis ongoing"* and B1 carries a coolant dye/pressure check. **This is a candidate location, not a diagnosis** | Where **our** leak is. It names a place to look |
| [MK7 engine component locations](https://www.youtube.com/watch?v=JjisPTl_5C8) | **C** | Orientation | — |

---

## Bronco (1989) — deliberately NOT populated here

**Owned by a concurrent session (Bolores/paint/reference thread), and left to it on purpose.** The
export holds **27** Bronco links; none has been triaged into this file, because two windows filing
the same 27 rows is the duplicate-that-diverges problem this file exists to avoid.

Bolores evidence and its tiers live in `.private/service-records/bronco-1989/SOURCES.md`; the FD.88
catalogue is an `INDEX.md` row.

⚠️ **Two things that thread should know:**
1. **One Bronco link is misfiled outside the Bronco folder** — *"Tailgate rewire! Works 100x better!"*
   (`fullsizebronco.com/threads/…361210`) sits under **Finances** in the export.
2. **fullsizebronco.com now redirects to a tollbit paywall** — agents can no longer fetch those
   threads. **Save the page as a file before more of them go**, which converts a **C** link into an
   **A** document and moves the row to `INDEX.md`. That migration is the whole point of this file.

---

## Link rot — measured, not assumed

All 108 non-Bronco bookmarks were liveness-checked 2026-08-04. Across the fleet folders: **one hard
404** (the G22A wiring diagram, noted above). The Home Depot / eBay / iNaturalist 403s in the wider
export are **bot-blocks, not dead pages** — they load fine in a browser, and an automated check must
not be read as link rot.

**The lesson the Bronco forum makes concrete:** a **C** link is not durable. When one matters,
download it. This file lists things we can lose; `INDEX.md` lists things we can't.

---

## Provenance

Seeded 2026-08-04 from an export of Paul's browser bookmarks, analysed in
`~/Desktop/Claude/bookmarks-analysis-2026-08-04.md`.

⚠️ **The export is deliberately NOT in this repo.** A copy had been placed in Bolores' `_assets/`;
it was byte-identical (md5 `5365177d…`) to Paul's own copy at `~/Desktop/Claude/bookmarks_8_4_26.html`
and was removed to the Trash on 2026-08-04. Two reasons, and the second is the real one:

1. By the store rule it was in the wrong place — it spans the whole fleet, not one truck.
2. **It contains Finances, CCs, and Health folders.** Keeping a full copy of that inside a public
   repo — even in a gitignored directory — is a standing exposure one `.gitignore` edit away from
   being real. The vehicle slice is what this repo needs, and it is now *here*, in the open, as text.

Verified at removal: `.private/` is gitignored, **zero** files under it are tracked, and no commit in
the repo's history has ever touched `.private/` or contained a bookmark export.
