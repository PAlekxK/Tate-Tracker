# HANDOFF — the ZONE DEFINITION session (Fernwood, launched during lap 5)

- composed: 2026-09-08 · at HEAD `9a762b0` · repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`
- composed by: the **backlog-refinement** window, on Paul's instruction — *"all the zone definition work,
  which I know is super meaty, so I'd kind of like to launch a session dedicated to that… that would be a
  separate session. I can address all zone questions in that other window."*
- ⭐ **Paul is answering zone questions HERE.** This window holds the zone conversation; the other windows
  must not re-open it.

---

## ⛔ READ FIRST — you are the FOURTH live window on ONE working tree

| window | owns |
|---|---|
| **BUILD** | `onboarding/index.html` · `viewer.html` · `engine/*` · `tools/*` · `cycle/*` |
| **BACKLOG REFINEMENT** | `BACKLOG.md` · `.plans/*` refinement artifacts · `OBJECTIVES.md` |
| **tools & supplies** | its own research artifacts; a theme it will hand to refinement |
| **YOU** | the zones lane — `.plans/2026-09-07-zones-PLAN.md` and the zone conversation |

⛔ **Do NOT edit `BACKLOG.md`.** The refinement window owns it this lap. If a zones ruling changes a row
(TIER 2 · 7, 8 or 9 are all live), **message that window and it will make the edit** — do not touch it,
and do not let two registers each read current. ⛔ **Do not edit code the BUILD window owns** while its
A/B/C scope is in flight. `git add -- <explicit path>` only; `git add -A` is hook-blocked anyway.

🔴 **And a measured hazard, found today, that now applies to you.** `BACKLOG.md` § **L2**: the concurrency
guard `tools/guard-concurrent.py` keeps **one** `start`/`commit` slot in `.private/cycle-guard-state.json`
with `"lap": null` — verified still true at HEAD. With multiple sessions in this tree, each
`record-commit` overwrites the others', and `before-push` has been observed **passing on another
session's baseline**. Commit small, stage explicit paths, and **do not trust a green guard check** as
proof that no one else has moved HEAD.

---

## ⭐ START HERE — two files, in this order. Do not skip the second.

1. **`handoff/handoff-zones-decisions.md`** — the 09-07 design session's full record: the twelve rulings
   **Z-1 … Z-10** and six decisions **R-Z1 … R-Z6**, each with where its consequence lives.
2. **`.plans/2026-09-07-zones-PLAN.md` § 0 FIRST.** ⚠️ **Four things in that file's own body are
   superseded and marked as such, deliberately not edited away. Reading the body without §0 will mislead
   you.** The plan is ~64 KB; §0 is the map to which parts are still true.

Supporting seat trails, already run — do not re-commission them:
`.user-research/2026-09-07-zones-uses-landscape.md` · `.engineering/2026-09-07-zones-v1-path.md` ·
`.ux-reviews/2026-09-07-zones-v1-surfaces.md` · `.ux-reviews/2026-09-07-zones-v1-copy.md` ·
`.plans/2026-09-06-ai-mapping-capability-SCAN.md`

---

## The register — three live rows, and their relationship is Paul's ruling, not a ranking

| row | what it is | state |
|---|---|---|
| **TIER 2 · 7** | ⭐ **ZONES AS A FEATURE — the epic.** *"The primitive is a NAMED PLACE, geometry optional"*, reached four independent ways. **v1 = zones × plants, zones defined FIRST**, and the frozen instance's plant↔place data does **not** travel `[Z-10]` | `stage: design`, `→ READY · .plans/2026-09-07-zones-PLAN.md` |
| **TIER 2 · 8** | ⛔ **LEG 0 — the per-estate capture write path.** ⚠️ **Smaller than first called:** the five capture handlers touch no git and work at `home` today. **Exactly one create is broken** — `handleZoneSave`'s 503 sits at the TOP of the handler, blocking a KV write ~80 lines below whose own comment says *"if git commits fail later, KV still has the new data"*. **Move the gate down.** | live |
| **TIER 2 · 9** | 🔭 **PROCESS B — the derived first draft from an address.** The long-horizon half. v1 = `address → frame, georeferenced to one bbox, plus a coverage report that refuses to be green by absence`; **rendering deliberately cut** | live |

⛔ **`R-Z6(B)` makes LEG 0 a SAME-COMMIT co-requisite** — *before her first save*. That is **Paul's own
ruling recorded in the plan**, not an ordering anyone invented. Every other question of what comes first
is **Paul's**, and no other window may answer it.

Adjacent, not the same thing — decide explicitly whether they are in scope:
- **`BACKLOG.md` § Z2 · ZONE CONSOLIDATION** — *"a consolidation run of all the various zones I've drawn
  over time… I definitely have done some draws recently that are not reflected here."* Three overlapping
  sources have diverged. Surveyed 2026-09-02; **the consolidation itself never ran.**
- **§ INBOUND from photo-organizer, 2026-09-01** — the photo→zone join has a **measured floor** and
  **12 of 18 zones sit under it**; re-tracing will not fix it (three separate limits, only the first is
  fixable by drawing better).

---

## What has MOVED since the 09-07 design session — check these before acting on the plan

1. ⚠️ **A stamp discrepancy, unresolved, and it is the first thing to settle.**
   `.plans/2026-09-07-zones-PLAN.md:16` carries **`ready: [paul-approved 2026-09-07]`** — *"I'm good to
   stamp everything as it is."* But **TIER 2 · 7 still reads *"awaiting Paul's `ready:` stamp."*** The
   plan's own caveat is probably the reconciliation — *"a stamp on a `design`-stage plan authorises the
   **STAGE**, not the build"* — but **the row and the file disagree on their face.** `measured` at HEAD.
   ⭐ **Ask Paul which he meant before building anything.** If the row is stale, the refinement window
   makes that edit, not you.
2. 🚦 **The WIP band is FULL at build.** `python3 tools/check-backlog-ready.py` reports
   **`build 1/1`** (C4 environments) **+3 declared exceptions**; `design 1/2`, and the zones plan is the
   one occupying `design`. **Zones cannot move `design → build` under the band as written** without C4
   clearing or a declared exception. That is a governance fact, not a technical blocker — **Paul's call.**
3. **The release loop was renumbered today** to execution order; **COMMIT now gates BUILD**. The BUILD
   window is executing Paul's committed A/B/C scope (returning recognition · the station indicator ·
   the production activity sweep). **B is already shipped** (`32d6d80`) and turned out to be **six sites,
   not two**.
4. **Beat 5 GROOM & BUCKET produced two artifacts you may need:**
   `.plans/2026-09-08-lap5-BOARD.md` (ten kind-shaped buckets + a proposed rationalization diff) and
   `.plans/2026-09-08-lap5-REFINEMENT.md` (readiness triage; **all 34 open rows graded**).
   ⛔ **Neither is applied. Nothing in `BACKLOG.md` has been reordered.**
5. ⛔ **Addressing: nine live ordinal collisions across the tier tables**, derived independently by two
   windows. **Always write `TIER 2 · 7`, never *"row 7"*** — *"row 11"* alone already caused one real
   mis-citation in a tracked file today. **Do not renumber**: eleven citations outside `BACKLOG.md`, six
   of them in `worker/worker.js`, would be silently falsified.

---

## Standing rules that bind this window

- **Never rank.** Ordering is Paul's. Dependency, evidence and reachability are not ranking; preference is.
- ⛔ **Nothing reaches Mom.** The instance is frozen as a data control; **WORK is lifted, PUSH is frozen**
  `[paul-stated 2026-09-06]`. It may be built and may not ship to her.
- **Prefer citing an existing row to minting one** — two registers each reading current is this corpus's
  most-repeated failure.
- Grade every claim `measured` · `inferred` · `proposed`.
- **An unchecked box is not open work** — probe the world before acting on a row. Three rows the
  refinement window checked today read ✅ in their own text and were **all still legitimately open**;
  one row's stated evidence had gone stale while its defect stood.
