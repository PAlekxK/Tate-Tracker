# Fernwood, re-founded — scoping what moves from `est-3c9f1a` to `est-e6696a`

`[paul-ruled 2026-09-10]` — *"she knows it's empty and she has to rebuild it. We're keeping Fernwood
legacy as context and nothing gets fully lost."*

⭐ **So this is NOT a data migration.** It is a **re-founding**: Mom rebuilds her record on the new
estate, and the old one is kept as a readable archive. That ruling removes the hardest question
(what to copy) and replaces it with a better one — **what does "kept as context" mean mechanically?**

## 1. What is actually on each side — measured, counts only, no content read

| | `legacy` `est-3c9f1a` | `home` `est-e6696a` |
|---|---|---|
| total keys | **181** | **24** |
| conversations | **35** | 0 |
| metrics batches | **96** | 3 |
| feedback | **11** | 3 |
| zone audio | **3 records + 6 blobs** | 0 |
| observations | **2** | 0 |
| zones | **2** (+ `zones-last-seen`) | 0 |
| cost-log | 22 | 1 |
| canon | **40 plants · 23 zones · property · vehicles · wildlife** (repo root, `instance/fernwood.json → canon: ".."`) | **none** (`canon: "neutral-canon"`) |

⚠️ **176 of legacy's 181 keys are UNPREFIXED** — the pre-C5 era (`conversation:…`, not
`est-3c9f1a:conversation:…`). Anything that reads across the boundary has to handle **two key eras**,
which is the same trap `watch-activity.py` was built to survive: *absence under a prefix is a fact
about the prefix, not about the world.*

## 2. ⛔ THE THING THAT IS NOT A MIGRATION QUESTION AND IS MORE URGENT THAN ONE

**Mom's new estate has no identity, no colour, and no weather station.** `instance/home.json`
declares `name: "My Home"`, no theme `main`, and **`station: "declared-absent"`** — and the live
Worker agrees: `GET /api/ambient` on `fernwood-home` answers **503 `ambient-not-configured`**.

⛔ **There IS a station on that property.** The Ambient Weather unit is real, it is the source of
`weather-history.json`, and CLAUDE.md records that **the weather card is the one card she
demonstrably opens** — both of her card opens in an entire lap.

⭐ **So the single most-used thing in her app is dark on the estate she just joined, and that is
config, not migration.** It needs no data moved. It is the cheapest, highest-value item on this page.

## 3. Disposition by class — what "rebuild" means per kind of thing

| class | what it is | recommendation |
|---|---|---|
| 🎛 **identity + station** | name, colour, station binding | ⭐ **DECLARE on the new estate now.** Not a migration. §2 |
| 🗣 **her authored, irreplaceable** | 6 voice blobs · 3 zone-audio records · 11 answers · 2 observations · 35 Guru turns | ⛔ **cannot be rebuilt** — she cannot re-record July. Reachable as context (§4), never re-authored |
| 🌿 **researched canon** | 40 plants, 23 zones, property, vehicles, wildlife | **she rebuilds**, per the ruling — and the derived property (A0) plus the confirm loop is exactly the machinery for it |
| 📈 **operational telemetry** | 96 metrics · 22 cost-log · door · zones-last-seen | **stays on legacy.** It describes the old deployment's behaviour, not the place |

⭐ **Nothing is deleted from legacy in any of these.** It is already frozen; the ruling makes that
permanent rather than transitional.

## 4. ⭐ WHAT "KEPT AS CONTEXT" HAS TO MEAN — declared lineage

*"Context"* needs a mechanism or it is a hope. The honest one:

    est-e6696a declares est-3c9f1a as its PREDECESSOR

and the canon guard permits reading a **declared predecessor** — never an arbitrary other estate.

⭐ **This is legitimate where `CANON_FOREIGN_OK` was not, and the difference is the whole point.**
`est-3c9f1a` and `est-e6696a` are **the same place and the same person**. That is not a cross-household
read; it is one household re-founded under a new id. The flag was dangerous because it was **global
and undeclared**; a lineage is **specific, one-directional and written down**.

⛔ **Four constraints, and they are what keep it from becoming the flag again:**
1. **Declared in config, never inferred from a request.** No header, no parameter, no body field may
   name a predecessor.
2. **One-directional and read-only.** The successor may read the predecessor. Never the reverse, and
   never a write.
3. **Not transitive.** A predecessor's predecessor is not inherited — one hop, or the chain becomes
   the flag with extra steps.
4. **Visible.** Anything served from the predecessor is labelled as the older record, to her. A
   Journal that silently blends two eras is worse than one that says *"from your Fernwood archive."*

⚠️ **It is a mechanism for one estate to read another's record, so it is Paul's to ratify, not mine
to ship.** I would build it behind that ruling and not before it.

## 5. SEQUENCE

| | | owner | reversible |
|---|---|---|---|
| **M1** | declare identity · theme · **station** on `est-e6696a` | agent, with Paul's read on the name | ✅ config |
| **M2** | derive her property from her address (A0) so the new estate HAS a place | agent | ✅ |
| **M3** | build + publish her Journal record (A1) — small, honest, growing | agent | ✅ |
| **M4** | ratify the **lineage** mechanism | ⛔ **Paul** | — |
| **M5** | implement lineage read + the "from your archive" label | agent | ✅ additive |
| **M6** | confirm-cards seeded from the derived property, so rebuilding is a conversation and not a form | agent | ✅ |
| **M7** | legacy's public GitHub Pages build — the privacy gap | ⛔ **Paul** (`PRIVACY-POSTURE` P2) |

⛔ **M1–M3 need nothing from the migration question at all.** They are why her app is empty *today*,
and none of them is blocked on M4.

## 6. WHAT I WOULD NOT DO

- **Copy her authored content across.** The ruling says legacy is kept and nothing is lost; copying
  makes two originals and no answer to which is true.
- **Copy the canon.** She rebuilds — and a rebuilt record is *hers*, current, and confirmed on the
  ground, which is worth more than 40 inherited rows of which some are now false.
- **Write anything to legacy.** It is the frozen control; adding keys erodes what makes it one.
