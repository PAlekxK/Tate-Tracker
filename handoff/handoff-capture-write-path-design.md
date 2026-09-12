# HANDOFF — the CAPTURE WRITE PATH · ⛔ THE DESIGN PASS IS CLOSED. This is CURRENT STATE.

<!-- rewritten 2026-09-12 evening at the close of the design window.
     ⛔ This file previously briefed a window INTO the design pass. That pass is DONE.
     If you are looking for the pass's own instructions, they are in git history, not here.
     ⚠️ CITE BY SYMBOL, NOT BY LINE. Three `file:line` references went stale in a single
        afternoon here, every one from a concurrent `[env.…]` insertion and not one from a
        change to the thing cited. Re-read before you cite; `grep` the symbol. -->

## 1 · WHERE THIS STANDS — one line

`.plans/2026-09-07-capture-write-path-PLAN.md` is at **`stage: design`**, ladder **✅ READY**, next
rung *"the stage gate to build (a sha on QA)."* **Nothing has shipped, deployed or been pushed.**

## 2 ⛔⛔ DO NOT READ "R3 DISCHARGED" AS "GO" — THERE ARE STILL TWO LIVE GATES

R3 (*the build window opens only after the `design` band clears*) **is discharged**: the band went
3/2 → **2/2** when `.plans/2026-09-10-multi-tenancy-PLAN.md` was retired to `stage: retro`
(`853f76eb`) — **not** by finishing lap-8's P2 body half the way both windows assumed. Paul asked
*"what is the question?"* and there wasn't one: all four of its changes were spent, so its
never-given `ready:` stamp had nothing left to gate.

⛔ **Two gates remain, and they are independent — either alone could be argued away, together they
are not a scheduling opinion:**

| gate | state |
|---|---|
| **the `build` WIP band** | ⛔ **`build 1/1 (+4 excepted)` — FULL.** A fifth exception is Paul's ruling and was deliberately not requested. |
| **the dependency chain's ROOT** | ⛔ **This plan is LAYER 3 on an unbuilt LAYER 1** — the per-estate canon STORE (`BACKLOG.md` TIER 2 · 12, still `concept`). `[paul-ruled 2026-09-12: "let's adopt this chain as our priority"]` |

⭐ **Why layer 1 actually bites:** `handlePromoteSpecies` 503s permanently at every household, so a
confirmed entry has **nowhere to land** until that root exists. Verified: `canonFor(env, scope)` /
`foreignCanon()` guard `handleTodayLine`, `handleClassify`, `handleChat` and `handlePromoteSpecies`
(plus a throw in `canonFor`'s own caller) — **the journal's asking and a module's adding fail at the
same line.** ⛔ This does **not** refute the design; the reshaped step 1 is the shape layer 1 needs.
**It bounds what a build may CLAIM to deliver.**

## 3 · PAUL'S RULINGS — and what is NOT his

| | |
|---|---|
| **R5** `[paul-ruled]` | Zones are **NAMEABLE now, DRAWABLE later.** `validVertex`'s envelope is its own row (TIER 1 · 83), lifted with §5's basemap deferral. ⛔ **This build does NOT make a household's zones drawable and must never be described as if it does.** |
| **R3** `[paul-ruled]` | Build opens after the band clears — **discharged, see §2.** ⛔ His 09-07 `ready:` stamp was written against `concept` and is **NOT spent** by this plan. |
| **R6** `[paul-stated: "edit is fine"]` | The resident-facing noun for a zone edit is **“edit”**. Checked against `VOCABULARY.md` §4 first — not in the rejected register. |
| R1 · R2 · R4 | 🔵 **AGENT-TAKEN on the recommendation, NOT Paul's.** Reversible on his word; never cite them back as his. Recorded as such in the build plan. |

## 4 · THE EXECUTABLE ARTIFACT

**`.engineering/2026-09-12-capture-write-path-build-PLAN.md`** — the build-expert audit, per
`[paul-stated 2026-09-10]`. Sequence **B0** (replay harness + frozen baselines) → **B1**
(`handleZoneSave`) → **B4** (switch + comments) → **B5** (the `/health` check) → **B6** (routing).
Falsifier 3 is proved **without deploying to the frozen Fernwood**: `worker.js` already imports in
node, so two named exports are deploy-neutral; capture baselines **before** B1 touches the handler.
⚠️ Caveat that must ride with it: the frozen deployment returns `build_sha: null` — **unstamped**, so
a green harness is evidence about the FILE, not the deployment.

Copy for step 5: **`.content/2026-09-12-sync-chip-copy-DRAFT.md`** (draft; nothing shipped).
Seat trail: `.ux-reviews/2026-09-12-zone-save-honest-response-and-outbox.json`.

## 5 ⭐⭐ FOUR FINDINGS THAT OUTLIVED THIS THREAD — none is capture-write-path's to fix

1. ⛔ **THE `stale-client` 409 HAS NEVER FIRED, and a durability control was nearly built on it.**
   The client's zone-save payload is `{zones, _deleted, deviceId}` — **`_meta` appears ZERO times**
   in the whole sync region. So `clientSchema` is always `undefined` and the guard is inert. It was
   written to police the v2→v3 schema move and **slept through all of it.** ⭐ *A guard nobody can
   trip is not a guard* — worth sweeping for others of the shape.
2. ⛔ **`validVertex`'s envelope is FERNWOOD'S OWN NEIGHBOURHOOD applied to every estate**
   (`ZONE_LAT_MIN/MAX`, `ZONE_LON_MIN/MAX`). A household outside it fails **every** vertex → the
   whole save 400s with a hint naming an envelope that is not that estate's. Latent through the app
   (no basemap → no drawing); **live via `tools/kml-to-zones.py`.** → TIER 1 · 83.
3. 🔴 **The latent resident-facing wall** — the chip is hidden except in `failed`, where it prints
   `lastError` **raw**, which at a household reads *"set GITHUB_TOKEN and GITHUB_REPO worker
   secrets."* → TIER 1 · 78, **ships in the same commit as the write path.**
4. ⛔ **`/api/pending-species` keys on `scopeOf(env)`, never `scopeFor(request)`** — so the STAGING
   half of promotion already works at a household, and **the day one deployment holds two estates,
   one person's suggestion lands in the other's queue.** Filed by the backlog window.

## 6 · WHAT IS STILL OWED, AND BY WHOM

- ⛔ **PAUL — the local-history scrub.** A neighbourhood for the `est-e6696a` household was committed
  to this **PUBLIC** repo and scrubbed forward in `516f2e15`. **Nothing was pushed** (local `main` is
  ~1150 commits ahead of `origin/main`), so it never left the machine — **but it is in local history
  and wants scrubbing before any push of this branch.** History rewriting is destructive and was
  deliberately not attempted. `.private/condo-location.md` is gitignored precisely so that location
  stays out.
- **PAUL — R6's siblings**: `:13737` says *"online"* where every other sentence says *"Wi-Fi"*
  (pre-existing), and the `✓` convention is ratified as *"we have your words"* while a zone edit is a
  name plus geometry. Both small, both in the copy draft, both **unrecorded decisions** if left.
- **Falsifier 1's remaining half** — the five capture POSTs against `home`. ⭐ Its expensive half is
  **already discharged statically**: all five capture handlers contain **zero** git references at
  HEAD. The live POSTs are a **gate-kit act** — `lab`/`dev` holds no `SHARED_TOKEN` and 401s before
  the handler, and spending five unprovable fixture rows in `est-qa0001` to fake it was refused.

## 7 · HOW TO VERIFY ANY OF THIS CHEAPLY

⭐ **`GET /health` is UNAUTHENTICATED and publishes `configured.github` — the same predicate
`handleZoneSave` gates on.** So the binding question costs one anonymous curl:

```
for h in fernwood fernwood-home fernwood-qa fernwood-lab myhome-paul; do
  curl -s -A ua "https://$h.paul-kirschenbauer.workers.dev/health"; done
```
Measured 2026-09-12: **`github: true` at the frozen Fernwood (`env: production`) ONLY**; false at
`home`, `qa`, `dev`/`lab`, `paul`. Corroborated independently by `wrangler secret list`.
⚠️ `fernwood-home.pages.dev/api/zones` returns **HTTP 200 with the SPA shell** — Pages serves
`index.html` for unknown paths, so a status check against the wrong host reads GREEN for an endpoint
that is not there. **Match the payload, not the container.**

## 8 · GUARDRAILS THAT DID NOT EXPIRE

1. ⛔ **Never edit `BACKLOG.md`** — the standing backlog window is its sole writer. Route rows there.
2. ⛔ **Never write a `ready:` stamp.** Paul alone.
3. ⛔ **`wrangler.toml` ENFORCES NOTHING here.** `GITHUB_TOKEN` is a *secret*: zero assignments in
   that file. The prohibition is doctrine in a comment and **does not survive `wrangler secret put`**
   — and it is **uneven**: outright with a reason at `dev` and `home`, **weaker at `qa`** (it
   describes today's config, it does not forbid tomorrow's), **silent at `paul`**.
4. **An unchecked box is not open work.** Probe the world. This thread found four documents
   over-reporting open work, including the brief that started it.
