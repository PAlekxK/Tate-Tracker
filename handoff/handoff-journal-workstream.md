# HANDOFF — THE JOURNAL · can each estate ask its own record and be answered

<!-- generated 2026-09-12 · source: Tate-Tracker@45aae0c9 · main
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Several lanes are live on this tree. A file:line here has a half-life measured in minutes —
        cite the SYMBOL, stamp the sha, re-read immediately before the commit, not only before the edit. -->

## 1. Mission

`[paul-stated 2026-09-12]`: *"consolidate all this journal work into one big package to research… and
design and plan."*

**You are that package.** Three phases, in order: **RESEARCH → DESIGN → PLAN.** ⛔ **You are not a build
lane.** Nothing ships from here.

**Your subject in one line:** *a household asks its journal a question about its own place, and gets an
answer built from its own record.*

**Canonical grouping:** `BACKLOG.md` § **📖 THE JOURNAL** (a THEME, filed 2026-09-12). It names the rows,
the gap and the constraints. ⛔ **Read it there; it is not restated here.**

## 2. Windows — and which you are

| window | job | never |
|---|---|---|
| **coordination** — `tate-tracker` main | routes, sequences, runs laps | writes a feature |
| **backlog** (standing, LIVE) | **SOLE WRITER of `BACKLOG.md`** | commits code |
| **capture-write-path design** (may be live) | zones' write path, `concept → design` | touches the journal |
| **this one — journal** | research · design · plan for the per-estate journal | ⛔ **writes `BACKLOG.md`** · ships code · stamps its own `ready:` |

⛔⛔ **DO NOT EDIT `BACKLOG.md`.** Route row changes to the backlog window — it files the pointer for you,
which is how your plan avoids becoming an orphan the checker flags.

⚠️ **A sibling lane owns the WRITE path** (`.plans/2026-09-07-capture-write-path-PLAN.md` — zones, KV,
`handleZoneSave`). **You own the READ/ANSWER path.** They meet at the per-estate store (TIER 2 · 12).
Coordinate through coordination; do not both design that seam.

## 3. ⛔⛔ START HERE — THE GROUND MOVED ON 2026-09-10 AND MOST ARTIFACTS DO NOT KNOW

**This is the single most important section. Two widely-cited claims are dead.**

### ⭐⭐ Canon is resolved PER REQUEST, not per deployment — `a263ed3c`, 2026-09-10

- ⛔ **`canonIsThisEstate()` NO LONGER EXISTS.** It survives only as a comment at `worker.js:119`.
- ✅ **`canonFor(env, scope)`** reads the caller's estate's published digest from KV
  (`keyFor(scope, "digest")`), **requires the digest's stamp to agree with the caller**, and returns
  `null` otherwise. `foreignCanon()` 503s at **four** sites — `worker.js:2115 · 2188 · 2967 · 3478`.
- The scope is per request: `const canonScope = scopeFor(request, env, grant)` (`worker.js:4877`).
- **The bundled digest is a fallback for EXACTLY ONE case:** the deployment whose `ESTATE_ID` it was
  built for. That keeps legacy working while every other estate reads its own published record.

⭐⭐ **AND THE WORKER'S OWN COMMENT CARRIES THE FINDING THAT REFRAMES EVERYTHING YOU WILL READ:**

> *"a deployment could serve exactly one household's model routes and every other household got a 503.
> **That is why Guru, the daily line and classify have been dark at every real household including
> Mom's.**"*

⛔ **So "the journal is dark at every household" was a KNOWN, NAMED, FIXED defect — not a mystery.** Any
artifact dated before 2026-09-10 that treats darkness as unexplained is reasoning from a dead premise.
⚠️ **It specifically weakens `BACKLOG.md` TIER 1 · 72** (qa's missing `ANTHROPIC_WORKSPACE_ID` as the
cause of qa's dark routes) — that hypothesis is now the *second* candidate, and the sweep it rests on
predates the fix. **Settle it by USE: one `/api/chat` turn at `qa`.**

### ⛔ `CANON_FOREIGN_OK` is DELETED, not defaulted — and the config did not get the message

Code: *"with per-estate canon it has no legitimate use; its only effect would be to feed one household's
record into another's prompt."* ⚠️ **But `wrangler.toml:59` (qa) and `:128` (lab) STILL SET
`CANON_FOREIGN_OK = "true"`** for a var nothing reads. Harmless today, **misleading to the next reader**
— a var that survives its feature teaches the wrong model. Flag it; the fix is not yours alone.

## 4. ⭐ THE GAP — nothing verifies that an estate's journal ANSWERS correctly

`measured 2026-09-12.` Two readers exist and neither closes it:

- **`check-canon-scope.py`** reads the **digest** — the *input* to the prompt. It answers *whose place is
  in this household's model prompt* and says **nothing about what comes back out**.
- **`guru-probe.py`** *does* grade real answers, and grades them well — **inverted**, so a row is red when
  the answer carries a must-NOT even if the right number is also there. ⛔ **But it is QA-WORKER-ONLY by
  construction and has NO `--env`:** it reads `/health` and **refuses unless `env=="qa"`**.

⛔ **So the one instrument that reads a journal's RESPONSE can only ever look at one deployment.** Same
shape `CLAUDE.md` records for `read-mom-engagement.py` — *"the capability existed for one person on one
estate and nobody else."* ⭐ **A `--env` plus a per-estate expectation set is the cheap half and is
unfiled.** It is a strong candidate for your PLAN phase's first deliverable.

## 5. The three phases

### ① RESEARCH
- **Which retrieval shape serves N estates?** Per-estate digest (what ships today) · a per-estate store ·
  or the prose library index. ⚠️ **`build-library-index.py --check` reads `5777 chunks · 19726 terms ·
  731 shards · loaded: qa@2026-09-04` — `CLAUDE.md` says 7,330. The tool wins; the doc is stale.** And
  note *loaded: qa* — a fresh manifest with a stale KV is still possible, and it is loaded at ONE env.
- ⭐ **The sharper question under the "60 literals" number:** row 15 measured **60 hardcoded place
  literals against 43 derived interpolations** on 2026-09-08. ⛔ **RE-MEASURE IT — it is four days old and
  predates `a263ed3c`.** Then split it: **which literals are DERIVABLE from a household's record, and
  which are authored content that is genuinely Fernwood's and must not travel?** *Those are two different
  problems and one count conflates them.* That split is probably this phase's main deliverable.
- **What does a journal do when it does not know?** Today the honest answer is a 503 with a hint. That is
  correct plumbing and a poor answer to a person.

### ② DESIGN
- The seam: how a route gets the right estate's facts — and where that meets the capture lane's store.
- ⭐ **What the journal IS to a household** (TIER 2 · 20): its role, what it may be asked, its voice when
  it lacks a record. ⚠️ **content-steward's, not yours to word alone.**
- A brand-new estate has an **empty** record. The journal's first day is its hardest, and no artifact
  currently describes it.

### ③ PLAN
Sequence, falsifiers, and the per-estate verification from §4. ⛔ **Stop at the plan. Do not build.**

## 6. ⛔ Constraints — cited, never re-argued

- ⭐ **This is the ASK path, and it is where a model legitimately lives.** *AI on the ask path; capture
  stays AI-free.* ⛔ Nothing here licenses a model on a capture path.
- ⛔ **THE AI BOUNDARY** — *the **administrator's** eyes sit between the model and the estate's people,
  both directions* `[paul-ratified 2026-09-02 — the gate is a ROLE, not a person]`.
- ⛔ **Allow-list, never an exclude-list.** A new environment inherits the refusal.
- 🔤 **`Almanac` is REJECTED as a portable noun** (`VOCABULARY.md` §4); **JOURNAL is the engine default for
  every household that is not Fernwood** (`5587b884`). **`estate` never reaches a user-facing surface.**
- 🌐 **THREE environments — `lab` · `qa` · `production` (ONE)**; `legacy` is a DATA CONTROL; `home`/`paul`
  are DEPLOYMENTS. ⚠️ **Enforced since `eef7dd2e` by `check-vocabulary.py` V6** — a live surface claiming
  4+ environments goes red. `.plans/` is never graded; `CLAUDE.md` and `VOCABULARY.md` are. To quote the
  wrong model deliberately, mark the line `3i-cite`.
- ⚠️ **The history that sizes the risk:** before the stamp, `worker.js` imported ONE `digest.json`
  statically, so **every deployment carried Fernwood's whole record into five model routes' prompts** — a
  one-turn probe on `est-qa0001` gave up the street address, the lidar elevation, three plants and a
  vehicle. ⛔ **No page check could see it: the leak was never on a page.**

## 7. Trust status

| claim | status |
|---|---|
| Canon resolved per request; `canonIsThisEstate` gone | 🔵 **model-verified in code** at `eef7dd2e` (4 call sites + the scope line). Not human-cleared |
| Per-deployment guard is why routes were dark at every household | 🟢 **the Worker's own comment says so**, beside the commit that fixed it. Strong; nobody has signed it |
| `CANON_FOREIGN_OK` vestigial in `wrangler.toml` | 🔵 **model-verified** — deleted in code, still set at `:59`/`:128` |
| `guru-probe.py` cannot see any env but qa | 🔵 **model-verified** — no `--env`; refuses unless `/health` says qa |
| 60 literals vs 43 derived | 🟠 **CARRIED FROM 2026-09-08, NOT RE-MEASURED, and it predates `a263ed3c`** |
| library index = 5,777 chunks | 🔵 **tool output today.** ⛔ `CLAUDE.md`'s 7,330 is stale |
| qa's missing workspace id explains dark routes | 🔴 **weakened** — §3 names a better-documented cause |

## 8. Done when

The three phases have produced their artifacts, the plan carries its falsifiers and a per-estate
verification, and **the 60/43 split has been re-measured and separated into derivable vs authored.**

⛔ **Then hand back.** Route row changes to the backlog window; lap decisions and rulings to coordination.
