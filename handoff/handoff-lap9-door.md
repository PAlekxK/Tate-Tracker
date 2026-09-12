# HANDOFF — LAP 9 · THE DOOR

<!-- generated 2026-09-12 · source: Tate-Tracker@96d46e13 · main · CLEAN TREE · sole live window
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Cite the SYMBOL, stamp the sha, re-read immediately before the commit — three file:line
        citations went stale inside single afternoons on 2026-09-12, every one from a concurrent
        insertion rather than a change to the thing cited. -->

## 1. Mission

`[paul-ruled 2026-09-12]` — **lap 9 is THE DOOR**, recorded in `cycle/release/CYCLE-LOG.md` at
`c34e0c1f` (*"LAP 9 IS THE DOOR, AND THE 8·3 / 9·2 ORDERING IS RELEASED"*).

**Spine:** `.plans/2026-09-11-lap8-build-PLAN.md` § **ROW A · the door**, steps **A0–A15** — written by
the build expert, audited, **never executed**. **Small half:** `BACKLOG.md` TIER 1 · **71 · 72 · 73 · 74**
and **92**, plus ⛔ **89, which is not optional — see §5.**

⭐ **Why the door and not the weather card:** the 8·3 / 9·2 ordering that put the weather card first is
**released by ruling**, and the door stopped being a preference — **it is the structural prerequisite of
the `myhome-prod` cutover.** One deployment holding two estates *is* multi-tenancy; `scopeOf(env)` spans
~69 lines against **one** live consuming call of `scopeFor(request, env, grant)`. **The cutover and this
lap are the same body of work under two names.**

## 2. ⛔⛔ THREE GATES BEFORE ANY STEP — measured, not assumed

| # | gate | state at `96d46e13` |
|---|---|---|
| **G1** | ⛔ **The build plan is UNSTAMPED** — `stage: draft` · `ready: agent-proposed` | **PAUL'S STAMP ONLY.** ⛔ No agent may write `ready:`; that is the one act this gate exists to prevent |
| **G2** | ⚠️ **`build` WIP band is `1/1 (+4 excepted)`** | a **fifth exception**, or something leaves. **Paul's, knowingly** — do not take it by default |
| **G3** | ⚠️ **QA serves `87c7aae`, ~200 behind** | a lap may **OPEN** without it; it may **NOT CERTIFY**. ⭐ **Schedule the QA deploy as an early beat, not at gate ①** |

⛔ **If G1 is not cleared, stop and hand back.** Building against an unstamped plan is the failure the
stage gate exists for, and it has happened in this repo before.

## 3. ⚠️ A NUMBERING TRAP — read this before citing any "A" id

`.plans/2026-09-11-lap8-build-PLAN.md` carries **TWO** A-schemes:
- `## A1` … `## A11` — **AUDIT FINDINGS** (e.g. *A4 · nothing says what `ESTATE_ID` is*)
- `### A0` … `### A15` — **THE BUILD STEPS** (your spine)

⛔ **They collide and a grep for "A4" returns both.** Always say *"step A4"* or *"finding A4"*. *(This is
the third such collision found on 2026-09-12 — "Q8" names four different question series, and "five
seats" names both agent roles and walk fixtures.)*

## 4. The spine — steps A0–A15, as written

**A0** `tools/check-scope-sites.py`, the classifier, **before any conversion** · **A1** declare the
production origin's `ESTATE_ID` *(Paul's ruling, then one var)* · **A2** convert **B-CALLER** (~30 sites,
by key kind, reviewable batches) · **A3** convert **B-CACHE** (4) · **A4** ⛔ **declare** B-DEPLOY (~13) —
**annotate, do not convert** · **A5** `route:` stops naming the estate · **A6** the
`grant:<personId>:<estateId>` edge + `grantsFor()` · **A7** `X-Estate` · **A8** `hostAgrees()`/`FAMILY_HOSTS`
becomes an ordinary CSRF control · **A9** `/api/session` returns the **array** of estates · **A10** the 409
stays, its comment rewritten · **A11** the single sign-in page · **A12** the shelf after sign-in ·
**A13** `/api/account/available` · **A14** ⭐ **the migration rehearsal at `dev` — BEFORE any real row
moves** · **A15** ⭐ **the multi-tenancy falsifier at `dev`, verbatim — the gate before B.**

⚠️ **`lab` was renamed `dev` on 2026-09-12** (`89c47401`) — the env LABEL moved; ⛔ the Worker stays
`fernwood-lab` and the estate stays `est-lab0001` (a **KV key prefix**; renaming it orphans every row).
The plan predates the rename and says `lab`.

## 5. ⛔⛔ ROW 89 SHIPS WITH THIS LAP — it is ARMED BY the thing you are building

**Zone edits live under a BARE, un-scoped browser key**, and a **1500 ms boot timer** reads it, compares
`savedAt` against last-synced, and calls `scheduleZoneSync()` **with no user action**. Symbols:
`ZONE_STORE_KEY` · `ZONE_LAST_SYNCED_KEY` · `STORAGE_KEYS_PER_ESTATE` (which holds **only** the four
`momQueue*` keys) · `scheduleZoneSync` — all `engine/viewer.template.html`. ⛔ **Symbols, not lines.**

✅ **Latent today** — it cannot fire while each deployment serves one household.
⛔⛔ **It arms on EXACTLY what this lap delivers: one origin, every household a row inside it.** Edit at
estate A, open estate B on the same device, 1.5 s later A's overrides are POSTed into B's record.
**Do not ship the single-origin door without it.**

## 6. The small half — five rows, each already measured

**71** zone-save 503s outside `legacy`, and the bindings are **forbidden by design** (⛔ *provisioning the
token is the one remedy ruled out*) · **72** `qa`'s dark model routes — ✅ **cause SETTLED: no digest is
published for `est-qa0001`**, neither of the two earlier hypotheses · **73** G6 never renders at `home`
(⚠️ run `check-telemetry.py --before` first; the negative is not yet proven) · **74** the refutation
checks need a grant token, and `fernwood-home.pages.dev/api/zones` returns **200 with the SPA shell** —
*match the payload, not the container* · **92** 🔴 the **DEV-ONLY error oracle** in the unauthenticated
`POST /api/account` branch — **the code contains its own ruling against itself, unenforced**, and Paul
has ruled **fix it now**.

## 7. ⭐⭐ EVERY ITEM NAMES ITS TEST — AT DECISION TIME, NOT IN THE LAP

`[paul-stated 2026-09-12]`: *"I don't want to guess on testing when we get to the laps we build these in."*

| kind | what it means |
|---|---|
| **WALK** | a seat, a screen, a sha — gate ①'s unit. ⛔ **Unavailable to most of this lap** |
| **CHECK** | deterministic, runnable at any sha, and it **states what it does NOT cover on its own face** |
| **PROOF** | a property argued from code — ⚠️ **a property is not a test; say so when it is all there is** |

⛔⛔ **THE FALSIFIER MUST BE RUNNABLE.** `measured`: **91 falsifiers, 25 name an instrument, 6 cannot be
run**; two name tools that **never existed**. ⛔ **Do not add a seventh.** If a test needs a tool that does
not exist, **say so and size it**.

⭐ **Instruments that already exist for this lap** — prefer them to new ones: `check-household-isolation.py`
(pure key algebra, no network — *"a boundary needs no test to be true; a prefix does"*) ·
`check-storage-keys.py` (the roster row 89 violates) · `falsifier-tenancy.py --setup` at `dev` (**that is
step A14's rehearsal**) · `walk-founding.py` · `release-gate.py` for the walk tier.
⚠️ **Recommended and NOT built: `configured.canon` on `/health`** (XS) — today the only way to learn
whether a household's journal can answer is to ask Claude and watch for a 503, which fails
*deterministic things need a non-AI door* by the literal text of its own falsifier.

## 8. ⛔ Guardrails

1. ⛔ **Never edit `BACKLOG.md`** — the standing backlog window is its sole writer and is LIVE. Route rows to it.
2. ⛔ **Never write your own `ready:` stamp.**
3. ⛔ **Do not deploy to `home`, `paul` or `legacy`.** ⚠️ **`legacy` is a DATA CONTROL** — 55 commits sit
   undeployed and shipping them contaminates it. A separate ruled act covers that, and it is not this lap.
4. **`git commit --only <paths>`.** Never `-a`.
5. ⚠️ **`.engineering/` and `.plans/` are git-tracked and `origin` is PUBLIC.** Sweep with **two**
   predicates before committing a trail — place/identity AND credential/person.
6. **An unchecked box is not open work.** Probe before acting on status prose — 2026-09-12 produced four
   rows that were already discharged when filed.
7. **You flag; Paul clears.**

## 9. Trust status

| claim | status |
|---|---|
| Lap 9 = the door; 8·3 released | ✅ **human-cleared**, in the CYCLE-LOG at `c34e0c1f` |
| The door was never built | 🔵 **model-verified**, four independent probes |
| Row 89's auto-sync | 🔵 **model-verified** — the timer read verbatim, both sides |
| Row 92's error oracle | 🟠 **SOURCE-READ ONLY. Nobody has POSTed it.** One `curl` settles it |
| `qa` dark = no published digest | 🔵 **model-verified** by `check-canon-scope.py`; ⛔ no POST made |
| The plan is ready to build | 🔴 **NO — it is `draft` and UNSTAMPED.** G1 |

## 10. Done when

The lap's beat-6 scope is delivered, **every row ships with its test named in §7's terms**, and the
falsifier for each is one somebody can actually run.

⛔ **Route to the backlog window:** every row change. **Route to Paul:** G1, G2, and any ruling.
