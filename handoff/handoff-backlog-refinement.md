# HANDOFF — the backlog refinement thread (Fernwood, lap 5)

- composed: 2026-09-08 · at HEAD `65b38b2` · repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`
- for: a **fresh window running in parallel with the BUILD window**, on Paul's instruction —
  *"commit something that is well defined for the build to start, and launch in a separate window a
  focused backlog refinement session that keeps going during the build."*

## ⛔ READ THIS FIRST — the ownership split, because two windows share one working tree

| | owns |
|---|---|
| **YOU (this window)** | `BACKLOG.md` · `.plans/*` refinement artifacts · `OBJECTIVES.md` |
| **the BUILD window** | `onboarding/index.html` · `viewer.html` · `tools/*` · `cycle/*` |

⛔ **Do NOT edit code, and do NOT edit `cycle/release/*`.** If refinement needs a code fact, read it;
if it needs a cycle-log line, ask. ⚠️ Fernwood's own `CLAUDE.md` carries a **concurrent-session guard**:
if HEAD moves under you or you see edits you did not make, that is expected here — it is the build
window — but **stage explicit paths only** (`git add -- <path>`), never `git add -A`, which a hook
blocks anyway. Commit often and small.

## Where the lap stands

The release loop was **renumbered today** to run in execution order (`cycle/release/CYCLE-MAP.md`
§ The beats): OPEN(1) → DISPOSE(2) → READ(3) → CARRY(4) → **GROOM & BUCKET(5)** → COMMIT(6) →
BUILD(7) → SYNTHETIC(8) → WALK(9) → ↺(10) → CLEAR(11) → DEPLOY & CLOSE(12). **COMMIT now gates BUILD**;
it used to sit at the end arming the next lap, which is what Paul caught today.

**Beats 1–4 are closed. COMMIT has been made** — Paul committed three items (see below) and the build
window is executing them. **You are the continuation of beat 5, GROOM & BUCKET**, which is the beat
that newly owns `groom`.

## What Paul committed — DO NOT re-litigate or re-rank these

- **A · returning recognition** (the lap's STOP) — `onboarding/index.html`, `if (!read(K_USER))`
  returns before the `/api/grant/whoami` fetch; the correct fix exists ~40 lines below
  (*"the record wins over the cache"*) applied to `fw-onboard-step` and not `fw-username`.
  ⚠️ Done = the **two-person falsifier**, not the patch: fixing it alone still lands a `name:null`
  record on the naming screen.
- **B · the station indicator** — the honest string ships inside a `live-dot stale`; a **declaration
  is not a status**. Two sites: the weather panel, and `viewer.html:16736` which gates on runtime
  liveness and ignores the declaration entirely.
- **C · production activity sweep** — `tools/read-mom-engagement.py` has no `--env` and is hardcoded
  to Mom's device on legacy, so nothing can see what real production accounts DO.

## Your job

**① The rationalization that is OWED.** `python3 tools/check-backlog-drift.py` reads OWED: the ranked
list sits **554 lines below its own head** (limit 400), `BACKLOG.md` is **4,100+ lines**, 75 commits
since the 2026-09-03 run. ⛔ **PROPOSE AS A DIFF; DO NOT APPLY UNTIL PAUL SAYS.** CLAUDE.md: *"It FLAGS;
it never reorders."*

⛔ **A concrete collision that already cost something today:** there are **TWO rows numbered 11** —
TIER 1 · 11 (sound pipeline) and TIER 2 · 11 (weather card). A tracked evidence file cited the wrong
one this afternoon. Check for other colliding ordinals.

**② Paul's readiness triage** `[paul-stated 2026-09-08]`: *"we should be able to do some triage on the
backlog and just say, what's ready to build now? And what's very far off from that — the different
iterations or versions of readiness?"*
⭐ **A ladder already exists and grades the WRONG OBJECT.** `tools/check-backlog-ready.py` has
`STAGES = [draft, ready, concept, design, journey, build, qa, shipped, retro]` with WIP bands — and it
grades **typed documents in `.plans/`**, not **rows in `BACKLOG.md`**. The applied proposal says so:
*"Zero rows marked READY — a row earns its file when picked up."* So Paul's question cannot be answered
from the board. **Reuse that vocabulary; do not mint a rival.**

**③ Paul's process-first steer** `[paul-ruled 2026-09-08]`: *"if there were backlog and process related
items in the backlog, let's consolidate those and implement them first, so we don't wind up back in a
situation where we don't enact the fix… because the project can't see the inbox."*
⛔ You may **not** rank them first — ranking is Paul's at COMMIT. You **must** make them legible as a
bucket so he can.

## Two seats were running when this was composed — collect their artifacts before starting

- **product-steward · GROOM & BUCKET** → `.plans/2026-09-08-lap5-BOARD.md` (the proposed diff + the
  two-axis board). **This is your direct predecessor — start from it.**
- **practice-steward · readiness method** → `.plans/2026-09-08-backlog-readiness-METHOD.md`
  (outside best practice, cited, with an honest read on what survives translation to a solo operator).

⚠️ If either file is absent, the seat did not finish; say so rather than proceeding as if it had.

## Context you should not re-derive

- `.plans/2026-09-08-lap5-CARRY.md` — beat 4: 12 citations, **zero rows created**, 6 open questions.
- `.plans/2026-09-07-product-steward-queue.md` — those 6 questions.
- `.plans/2026-09-07-backlog-grooming-SCAN.md` — the 09-07 grooming scan and its slates. **Build on
  it; say what has moved.**
- `.user-research/2026-09-08-lap5-READ.md` — beat 3, including the provenance ruling now in the
  research library: *a fact-of-household report survives the builder-user bias; a preference report
  does not.*
- `BACKLOG.md` § **THE USER'S OWN RECORD** and § **SPLIT THE JOURNEY FROM THE READER** — two themes
  filed today, deliberately unscoped.
- ⭐ **A bucket Paul named that does not exist yet:** a **UX/design theme**. A disposed record was
  routed to it. Minting it is beat 5's. The library it serves already exists —
  `~/.claude/design-principles/` (983 lines) — and `/ux-sweep` pass 2 adjudicates against it
  automatically. That sweep is **OWED** (8 days, 120 viewer commits vs a limit of 20) and now runs
  when due at OPEN, per today's ruling.

## Coordination

The build window can message you and you can message it — use `ListAgents` to find it, then
`SendMessage`. **Tell it before you touch anything it owns, and ask before it touches `BACKLOG.md`.**

## Standing rules that bind you

- **Never rank.** That is Paul's, and the map says no instrument is ever built for it.
- **Prefer citing an existing row to minting one** — this corpus's most-repeated failure is two
  registers each reading current.
- Grade every claim `measured` · `inferred` · `proposed`.
- **An unchecked box is not open work** — verify a row against the world before acting on it. Three
  BACKLOG rows were found wrong this way once; a wrong SSOT row is this repo's most repeated failure.
