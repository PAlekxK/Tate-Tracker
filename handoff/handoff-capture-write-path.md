# HANDOFF — the per-estate capture write path (zones LEG 0)

- **from:** the zones scoping session, 2026-09-07 evening (design lane of release lap 3)
- **sha at handoff:** `a95f4d2`
- **plan of record:** `.plans/2026-09-07-capture-write-path-PLAN.md` — **read it in full before touching anything**
- **parent scope:** `.plans/2026-09-07-zones-PLAN.md` (**read its §0 first** — four things in its own body are superseded and marked)
- **BACKLOG rows:** ▶️ NEXT · TIER 2 · rows **7** (zones epic) and **8** (this)

---

## ⛔ THE GATE — read before doing anything

**`.plans/2026-09-07-capture-write-path-PLAN.md` carries `stage: concept` and NO `ready:` stamp.**
`ready:` is written by **Paul alone**, never by an agent. So:

> ✅ **You MAY:** run the two read-only refutation checks below · read code · verify claims · prepare and
> stage a change · report.
> ⛔ **You MAY NOT:** merge, deploy, push to `origin/main`, or treat the plan as approved. **Stop at the
> stamp and hand back.**

⚠️ **The `build` WIP band is `1/1` with three declared exceptions.** Whether this takes a fourth or waits
for `c4-environments` is **Paul's ruling**, stated on the plan's own face and not pre-empted.

---

## ⭐ START HERE — two checks that could refute this whole plan

The engineering seat pre-registered these **against its own scope**. Both are single read-only requests.
**Run them first. If either fails, the plan is rewritten, not patched.**

1. **POST to each of the five household capture endpoints against `home`** — `/api/feedback`,
   `/api/observations`, `/api/conversations`, `/api/zone-feedback`, `/api/zone-audio`.
   **Expected: all five succeed.** ⛔ *"If more than `zone-save` is broken, my scope correction is wrong
   and the plan should be rewritten, not patched."*
2. **`GET /api/zones` against `home`.**
   **Expected: it returns Fernwood's 23 zones ("The bank", "Eastern Woodlands", …).** ⛔ *"If it returns
   empty, I'm wrong about the fallback — I read the path, I did not exercise it."*
   ⭐ Check 2 is the one that decides whether R-Z6 is real. **The path was read, never exercised.**

---

## What the work is, in one paragraph

**Exactly one thing a household creates cannot be saved: a zone.** `handleZoneSave`'s `503
github-not-configured` sits at the **top** of the handler (`worker/worker.js:~3850`); the **KV write it
blocks** is ~80 lines below (`:~3932`), carrying the handler's own comment *"if git commits fail later, KV
still has the new data"*; the **git commits it should actually guard** are at `:3955` / `:3969`. It is an
early return protecting a later, optional side effect. **Move the gate down.** `home` then works and the
frozen production instance stays byte-identical.

## ⛔ THE CO-REQUISITE — same commit, non-negotiable

Before her first save, `home`'s KV has **no `zones:all` key** — which is exactly the condition that makes
`handleZonesGet` fall through to `ghGetFile(env, "zones.json")` and serve **Fernwood's 23 hand-traced
zones**. **So unblocking the write without gating the read means her FIRST map load shows "The bank."**

That breaks `[paul-ruled 2026-09-07, J-f]` **Mom starts blank** — and it is **irreversible**: she cannot
un-see the answer key, and those 23 zones are the measurement control the whole comparison depends on.

**R-Z6 was ruled by Paul as B + C + D** (*"I go with your recommendation"*):
- **(B)** a **declared per-env switch, default OFF**, gating the git fallback. ⛔ **Never a hardcoded
  `est-3c9f1a`** — this repo has embedded Fernwood literals in engine code three times (`validVertex`'s
  6 km box, both tracer tools).
- **(C)** name **zones** in the `GITHUB_TOKEN` comment in all five `wrangler.toml` env blocks — the guard
  exists today and its stated reason is *promote-species*, so the next person to add a token for a good
  reason will open this without knowing.
- **(D)** a check asserting **every non-frozen env returns an empty zone list**.

⚠️ **It is LATENT, not live.** Only the top-level production env holds a `GITHUB_TOKEN`, so containment
holds today — by accident, and labelled with the wrong reason.

## Also in scope (see the plan for detail)

- **B3** — `build-digest.py`'s unguarded `load()` on `zones.json` raises `FileNotFoundError`. Single-digit
  lines. ⚠️ The old diagnosis was wrong: zones is **489 of 16,614 core tokens**, so the `CORE_INCLUDES`
  floor is never the reason.
- **Geometry shape** — a literal **RFC 7946 Geometry nested at `zone.geometry`**, **not** `{kind,
  coordinates}`. `zone.type` and `zone.geometry.type` do not collide when nested.
- **Identity as a FIELD on this path, not a separate project** — `by: "account:<username>"`.
  ⚠️ **Label it a SESSION, never a person.** Standing rule: *a deviceId is a browser bucket, not a person*
  — and Mom's phone signed in as Mom and handed to Paul is Paul editing as Mom. The record already
  attributes 31 of 42 history entries by hand; this closes the one writer that cannot.
- **Six of the eight `ghPutFile` sites stay 503** — `handlePromoteSpecies` (4) and `handleRemoveSpecies` (2)
  are operator acts on Fernwood's **shipped canon** and are meaningless at a household. **But reword the
  hint**: it currently reads *"set GITHUB_TOKEN and GITHUB_REPO worker secrets"*, which sounds like a
  misconfiguration a household admin ought to fix.
- ⛔ **`images/` on the deploy allow-list is DEFERRED, and the obvious fix is wrong.** Adding `images/` as a
  prefix ships all of `images/property-map/` — Fernwood's NAIP frames and lidar — **to Bob's origin**. That
  is the exact failure the allow-list exists for (measured 09-06: `onboarding/` as a prefix shipped an
  unsent outbound draft). The right shape is a per-instance named path, designed when a household actually
  has an image.

## ⚠️ Repo conditions you will hit

- **Multiple lanes are live in this repo.** Scope **every** commit with explicit paths —
  `git commit -- <path>`. A bare `git add -A` is blocked by `guard-shared-tree` and it blocked this session
  once, correctly. Read `git status --porcelain` first; files you did not touch are the concurrency signal.
- ⛔ **Do not touch `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`** — practice-steward owns it.
- ⚠️ `viewer.html` and `engine/viewer.template.html` were uncommitted under another lane earlier tonight.
- **QA is far behind HEAD** (`fbd5072`, 40+ commits, app surfaces changed). `python3 tools/pages-deploy.py
  --env qa` before anyone walks anything.
- ⚠️ **A green `build-viewer.py --check` is not a working page** — it compares bytes and does not parse JS.
- **Commit messages:** `-F -` with a **quoted** heredoc (`<<'MSG'`).

## How you will know it worked

- Both refutation checks return what the plan predicts (or the plan is rewritten).
- A zone save against `home` succeeds and lands in KV under `est-e6696a`.
- `GET /api/zones` against `home` returns **empty**, not Fernwood's 23.
- The frozen production instance is **byte-identical** in behaviour.
- ⛔ **And nothing merges until Paul stamps `ready:`.**
