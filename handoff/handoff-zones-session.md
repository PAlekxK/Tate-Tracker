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

## ✅ WHAT THIS WINDOW DID, 2026-09-08 — read this before re-opening anything above

**Four commits, all `.plans/` + `.engineering/` only. No `BACKLOG.md` edit, no code, no deploy, no
origin, no canon write.** The register rows still read as they did — ⛔ **three of them are now stale
and the refinement window owns the edits.**

### ① ⭐ R-Z6 IS CLOSED — the blocker was never a credential `[measured]` → plan **§9a**
`BACKLOG.md` TIER 2 · 8, the lap-5 BOARD and `handoff-zones-decisions.md` all said the probe was
`HTTP 401` = UNCHECKABLE, releasable only by *"a session with `home`'s token via `/secrets`."*
**False.** `/health` is **ungated on every env** and reports `configured.github`, which is the exact
predicate `handleZonesGet`'s git fallback is guarded on. **Only production has it true**; qa · lab ·
**home** · bob · paul are all false, so the fallback branch cannot execute and a KV miss returns an
empty list. The static path is closed too — `zones.json` is not in `pages-deploy`'s `HOUSEHOLD_ALLOW`
and both household origins refuse it. ⛔ **Ruling B+C+D still stands**: the containment is accidental
and every `wrangler.toml` comment still gives *promote-species* as the reason, never zones.

### ② ⛔ PRODUCTION SERVES 18 ZONES, NOT 23 `[measured]` → plan **§9a**
Found by the **positive control**, which is the only reason it was found. `origin/main:zones.json` =
**23 @ schemaVersion 3**; production KV = **18 @ v2**, stamped 2026-08-31. The 09-01 fold never
reached the served record. Eight canon zones are unserved, three served zones are not in canon.
`zones-sync-status` says `allCaughtUp: false`, its one known device seven weeks behind.
⚠️ **The plan's own §4 says `zones | 23`** — true of the FILE, false of the SERVED RECORD.
✅ **Paul ruled: canon's 23 is the answer key, leave prod alone** — and stamped the 23
*"approved as our best answer so far"* `[paul-stamped 2026-09-08]`.

### ③ ⭐⭐ THE DERIVABILITY EXPERIMENT → `.engineering/2026-09-08-zones-derivability-EXPERIMENT.md`
`[paul-ruled 2026-09-08: "we need to recreate the zones systematically… let's build this tool, all in
dev, and test it out for Fernwood"]`. **Terrain recreates the BUILT places and cannot see the MANAGED
ones.** 7 of 23 borders recoverable from the free on-disk 2018 lidar · 6 actively mis-led · 10 no
signal. **`the-meadow`'s border sits on FLATTER ground than a random nearby placement** — it is the
edge of mowing, not a landform. **Falsifier discharged the same session:** the mowing signal is real
but is a **REGION, not an EDGE** (meadow reads 0.71 interior-vs-surround in **all seven** NAIP frames,
2010→2023). ⭐ **That amends §5, which frames every step as an edge** — for the managed half,
edge-following is the wrong algorithm class.

### ④ ⭐ PAUL'S PROCESS DIRECTION, recorded with his hedge → EXPERIMENT **§7 · §8**
*"At each point… what CAN'T we tell from the different views"* · *"the house and a few other distinct
shapes — that'll also be the ORDER in which we apply this"* · *"what's the clearest thing to click,
maybe the house and the driveway, and then that allows you to RE-PROCESS around that."*
⚠️ **A direction, not a ruling — *"I'm not sure"* is his and is kept.** Not numbered into `Z-`.
⭐ **Anchor-then-reprocess is Z-11's cascade re-derived on the operator side** (each *derivation*
scoped by the previous *confirmation*, as each *ask* is scoped by the previous *answer*) — and §5's
four steps are a one-way cascade, so this is a genuinely different architecture.

### ⏭ THE NEXT EXECUTABLE STEP, sized and NOT run
**Render the break-of-slope ridges near the house as candidate polylines, beside the traced answer
key.** No new data, no dependency, no network — the field is already computed in `field.py`. It
answers the question that decides the approach: **is a derived edge something a person would ACCEPT,
or a suggestive smear?**

### 🔴 THREE REGISTER EDITS OWED — refinement window's, not this one's
1. **TIER 2 · 8** — drop the 🔴 *"blocked on the R-Z6 probe / needs `home`'s token"*. **Answered.**
2. **TIER 2 · 7** — says *"awaiting Paul's `ready:` stamp"*; the plan carries
   `ready: [paul-approved 2026-09-07]` and `check-backlog-ready.py` agrees. ⚠️ Also says *"Ten rulings
   Z-1 … Z-10"* — **there are twelve** (Z-11 the cascade, Z-12 the next-best-question).
3. **TIER 2 · 7 / 9** — the zone count in circulation is **two numbers**: 23 in canon, 18 served.
   `.plans/2026-09-06-maps-and-zones-STATE.md:170` already says *"12 of 18"*. **Say which, each time.**

### 🔴 A CONCURRENCY FAILURE HAPPENED HERE, LIVE — and it refines the guard `[measured 2026-09-08]`

⛔ **`git add -- <explicit path>` DOES NOT PROTECT YOU. The index is SHARED.**

This window staged 7 files with explicit pathspecs, then ran `git commit`. In the gap between the two,
another window committed — and **swept this window's staged files into ITS commit**, `71c31a6`
(*"all six recommendations approved…"*), together with its own `BACKLOG.md` edit. This window's
`git commit` then reported **"no changes added to commit."**

⭐ **Nothing was lost** — every file and both new sections verified present at HEAD. **The commit
BOUNDARY was lost:** this window's work carries another window's message, and a `BACKLOG.md` edit it
did not make sits in the same commit.

⛔ **NOT REPAIRED, deliberately.** Fixing it means rewriting `71c31a6` — another session's sha, which
`BACKLOG.md`'s own lap-4 hazard row names as the thing that makes a second session *"see a divergence
it did not cause."* **The content is correct; the archaeology is wrong. That is the cheaper defect.**

> ### ⭐ THE REFINEMENT, and it is one line
> The header's rule — *"Commit small, stage explicit paths"* — reads as though explicit staging is the
> protection. **It is not.** `git add` writes to `.git/index`, which every window in this tree shares,
> so a concurrent `commit` takes whatever is in it. **The protection is `git commit -- <paths>`**,
> which commits those paths directly and does not depend on what is sitting in the shared index.

⚠️ This is the **third** distinct hole now measured in this tree's concurrency story — after the
`record-commit` slot overwrite and the `before-push` baseline (header, § L2). All three share a shape:
**a control that reads green while another window moves the state underneath it.**

### ⚠️ Repo conditions observed
HEAD moved **~15 commits** under other windows during this session (`9a762b0` → `1092809` → `c9aa4e1`
→ … → `ab47279`). Every commit here used `git commit -- <explicit path>`. **The concurrency hazard in
the header is real and was observed live.**


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
