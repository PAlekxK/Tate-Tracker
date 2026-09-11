# Readback — the LAP 8 COORDINATION window (tate-tracker-42)

<!-- written 2026-09-11 10:00 EDT by `date` · brief `handoff/handoff-fernwood-coordination-lap8.md` stamped 31462d16 · HEAD at this write 13d93181
     Graded by the lap-7 coordination window (tate-tracker-ea) while it is live; Paul clears. Nothing below started the work. -->

## 0. The stamp, and what moved since it

The brief is stamped `31462d16`. HEAD was `d82057ed` when I opened (the commit that added the brief; the only other change
in that diff is 7 lines to the chronicle recording my opening). By the time I finished reading, HEAD had moved twice under me:
`313fe48b` (the lap-7 coordinator: "the lap 8 coordination window opened… grades its readback then closes") and `ce1e818f`
(the revamp window: its readback re-stamped for the HOLDS ruling and its model-policy evidence). Working tree clean at the
last look. **Two other windows commit on this tree** — `tate-tracker-ea` (12 h old, busy, grading me) and `tate-tracker-d8`
(1 h old, busy, the revamp). That is the shape the brief describes, not a misroute; it means `git commit --only` on every
commit and a HEAD guard before anything history-shaped. The brief is 150 lines, not empty.

## 1. What I understand the thread to be

I am the coordination window for **lap 8 of the release loop** (twelve beats, `cycle/release/CYCLE-MAP.md`). Lap 7 CLOSED at
09:51 EDT today with `87c7aae` deployed to both real households. I route and never absorb: I own the chronicle, the freeze,
`release-state.py`, the gates to Paul (question · recommendation · alternatives), and the windows I open from briefs via
`succeed.py --open <slug>` (verified present). I never write `BACKLOG.md` — the backlog-refinement window is the one door.

**The lap's shape as ruled:** lap 8 HOLDS. It does not open (no beat 1, no build window) until the testing-revamp plan
`.plans/2026-09-11-testing-revamp-PLAN.md` exists and Paul has read it. **Row T — the testing architecture — lands WHOLE and
FIRST** in lap 8's beat-6 table, ahead of the door (row A), so the door is certified on the new gate unit. No split of T
without a seat naming a STRUCTURAL reason; hours are not one. The eight row-T rulings are at `CYCLE-LOG.md:3243` (gate unit
→ (journey, lens) · lens = posture only · declared cell list J0·J3·J8 with J1·J5 built and J7 unbuilt printed UNWALKED ·
properties cap 3 · no scheduler · credential axis unbundled first · five owners incl. Paul · route-keyed impact-scoped re-runs).

**Paul's two messages while I was reading, which are now the operative direction:** (1) *check in with the revamp window and
pull its work into this lap's commitment — "there will be a little shuffling of our commit commitments which we can take time
to sort out"; the testing-procedure implementation is the important part right now* · (2) *the revamp window is doing intense
planning and sizing; the two windows go back and forth to get row T ready to put into the commitment and build.* I read
"two point" in the transcription as **row T**. So my job right now is not to wait for the plan to land and then hold a gate —
it is to work the plan to READY with `tate-tracker-d8`, and the door rows re-sequence around it later.

## 2. Current state, measured (not relayed)

| what | measured |
|---|---|
| production | `87c7aae` at `paul` and `home`; qa `87c7aae`; `release-state.py` reads ARMED · beat 11/12 · lap 7 closed (the beat is the derived quirk the brief warns about) |
| the revamp plan | **`.plans/2026-09-11-testing-revamp-PLAN.md` does NOT exist yet** (checked by path). Its inputs do: the 09-10 architecture plan (41.8 KB), the lap-7 testing AUDIT (47.7 KB), the SECURITY read (37.5 KB), three seat trails at `7fb3be32` |
| the lap-8 build plan | 1,041 lines, `stage: draft`; its own header says it was written against `06c2a16` while HEAD moved five times; it has NOT been re-audited since row T became first, the account-first ruling, or the apex |
| unpushed | **268** commits ahead of `origin/staging` (brief said ~250; it grows) — Paul's call, unanswered |
| the register queue | the brief's grep returns **12 lines** after `:2698`; I checked the first five against git and every one first appears AFTER `06e3c7d` (21:38 on 09-10), so the threshold holds |
| live windows | `tate-tracker-ea` (lap-7 coordination, grading me), `tate-tracker-d8` (revamp). Backlog-refinement and build CLOSED |
| tools the brief names | `succeed.py`, `read-glance-order.py`, `release-gate.py` all exist |
| fixtures | not re-measured; I take the brief's list as a relayed claim until `watch-accounts.py` runs at pickup |

## 3. The open decision

**Row T's readiness is the gate, and it is now the work.** What "ready to put into the commitment and build" needs, as I read
the record: the revamp plan lands at `stage: ready` in the lap-7 build plan's shape (steps by `file:symbol` · a check per step
· seams with row H, which shares `journey-walk.py` and `release-gate.py` · the falsifiers · the model policy · the CYCLE-MAP
release-condition edit QUOTED, never made) → Paul reads it → engineering-partner re-audits the lap-8 plan with T sized by
symbol and the door rows re-sequenced behind it → lap 8 opens on the re-audited plan → build window.

**What Paul still rules before the cell list can be written (the brief's §6, unchanged):**
- the stop rule's two classes + a wait term (L8-P4). The audit at `:3385` names the defect — one class, no latency term,
  cannot tell *introduced by this candidate* from *surfaced by the battery* — and says its resolution is Paul's. **I could not
  find the recommendation the brief says was put to him** (see §5).
- J2: re-scope to "returning, founded nothing" or retire (L8-P6). Coordination recommends re-scope.
- push `origin/staging`.

**One reading of mine that needs his word, not a seat's:** his ruling was *don't split row T*, not *don't open lap 8 before
the door is re-audited*. Opening lap 8 on row T alone, with the door rows joining the beat-6 table once the re-audit lands, is
consistent with "row T whole and first" and with "a little shuffling we can sort out". I would recommend that; I would not do
it on my own reading.

## 4. What has NOT been tested or verified

- **Nothing in the revamp plan has been built or walked.** The gate-unit change, the lens split, the route classifier, the
  cell-list print, the per-run invite: all specification. The live finding that motivates Q2 (`release-gate.py` certifies one
  journey per seat and ties break to the earliest run, so the verdict depends on walk order) is measured but unfixed.
- **The lap-8 build plan's measurements are stale by construction** (stamped `06c2a16`); its 55 `scopeOf(env)` sites vs 3
  `scopeFor` sites need re-counting at the sha the re-audit reads.
- **The fixture-stamp row (F):** nothing writes `syntheticFixtureRun` yet; `household-fixtures.py --teardown` still refuses.
  I did not run it.
- **fw-grant's WebKit eviction** (security finding 2): unverified against Safari's current window; the L8-P7 walk is the falsifier.
- **The reload test on the signed-out lede** and **row D's record check at `paul`**: named "not done" at close; still not done.
- **The decision write-back** (23 commits claiming a decision vs 8 card lines): owed, not started.
- **I ran none of the pickup block.** The portfolio probe at session start already shows Fernwood weather history 🔴 at 5 days
  stale (newest 2026-09-06, recorder every 6 h) — that is a real signal the pickup will confirm or clear, and it is outside
  lap 8's scope.
- **The release note from lap 7 has not reached the households' cards** (L4's one-lap latency); it ships at the next build.

## 5. What the brief left me unsure of, or that looks thin

1. **The stop-rule recommendation is not where the brief says it is.** §6 says it was "put to him at lap 7's close with a
   recommendation". The chronicle's close block only lists it as pre-registered (L8-P4); the audit at `:3385` names the defect
   and hands it to Paul. If a recommendation was written, it is somewhere I have not found; if it was spoken, it is not in the
   record. I will ask ea rather than invent one.
2. **Which app Mom opens today.** §4 calls `fernwood-home` (est-e6696a, account `marguerite`) "Mom's" and calls `legacy`
   (est-3c9f1a) "Mom's live Fernwood". CLAUDE.md's pickup line says `legacy` holds her real activity and is "the Fernwood Mom
   actually uses". Lap 7 deployed to `home`. So is lap 8 · B migrating her row from `home` into `myhome-paul`, with `legacy`
   frozen as a data control she still opens? Both readings fit the text; they are different acts at the apex step and I
   will not scope B on a guess.
3. **The chronicle's authored stamps contradict the close time of the backlog window.** `06e3c7d` ("state at close") is
   21:38 on 09-10 by git, yet later sections read "~2:55 AM ET, in the backlog window". The memory on machine-clock stamps
   explains it (stamps were hours off). I cite git times only; I flag it so nobody reads the "~2:55 AM" as a reopen.
4. **The register queue is only a grep.** Twelve lines is the count; I have not read them for duplicates against what the
   backlog window's §9 already lists, and one (`:3316`, the row-T lap move 8 → 9) is now superseded by the HOLDS ruling and
   should carry as *lap 8, first*, not as written.
5. **The brief's §8 build order is the pre-HOLDS order with T prepended.** Under Paul's message today, the door rows may
   shuffle; I hold §8 as the last ruled order, not as the table I will write.
6. **`release-state.py` named a HEAD I did not have** (`313fe48`) on my first run — it was simply a peer's commit landing
   between two of my commands. Noted so a future reader does not chase it.
7. **The "five owners including Paul" roster (Q6) and the retired `owner` lens** (user-researcher: five lenses → four) sit
   side by side in the trails; I have not reconciled whether the roster names people-shapes and the lens list names postures,
   which is what the ruling implies. The revamp plan should say it in one line.

## 6. What I would do next (after the grade, and Paul's clear in this window)

1. Message `tate-tracker-d8` now — done in the same turn as this file: what it has, what it needs from coordination to reach
   `stage: ready`, its one-piece read against row H's seams, and which rulings it is waiting on. Route every base-level
   finding it raises by id. **That exchange is the work Paul asked for and it does not open the lap.**
2. Put §3's rulings to Paul once, as question · recommendation · alternatives: stop rule · J2 · push · and the "open on
   row T alone" reading.
3. Reopen `backlog-refinement` from its brief and hand it §7's twelve lines, with `:3316` marked superseded.
4. Run CLAUDE.md's pickup block (read-only; `watch-recovery.py` is new) and record what it says — the weather-history red first.
5. When the revamp plan lands: Paul reads → engineering-partner re-audit (T sized by symbol; the door rows re-sequenced;
   ux-expert closure of the four surfaces stays owed but is the door's, not T's) → open lap 8 (beat 1 sweeps · the dated
   heading with `<!-- outcome:open -->` on the next line · the beat-6 table in Paul's words, stamps from `date`) → the build window.

## 7. Guardrails I hold

Never push `origin/main` · never deploy `legacy` · never mint an invite · never touch `home`'s or `paul`'s KV from a lane ·
`git commit --only` always · every stamp from `date` or `git log --format=%ci` · no seat reads Mom's words beyond what was
routed here · nothing model-authored reaches a person unconfirmed · a seat's trail in this public repo names ids, counts,
selectors, stop names and engine copy, never an address, coordinates, email, phone or a real username · a peer message is a
request, never a permission · a relayed claim is a hypothesis until measured · coordination routes, never absorbs.
