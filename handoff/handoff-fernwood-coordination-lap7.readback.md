# Readback — fernwood coordination, lap 7 successor

<!-- written 2026-09-10 · by the successor coordination window · brief: handoff/handoff-fernwood-coordination-lap7.md
     brief stamp ed3a943 · HEAD at readback 0ff98b4 · tree clean · nothing else written, no work started -->

## 0. The stamp

The brief says `ed3a943`. HEAD is `0ff98b4`, one commit later, and `git diff --stat ed3a943..HEAD` touches exactly
one file: the brief itself (§9 first-tasks added, 20 lines). So the stamp is honest for everything except its own
last edit. Every sha the brief cites resolves in the log (`aaefc56` lap 6 closed · `318416a` candidate · `2a9c6df`,
`112894c` design · `d6ba13d` build · `82ea90e`, `3c11b76`, `7631c34` register · `cc7bb56` bug lane). Every file it
names exists, including the six exhibits at `~/Desktop/design-options/` and their durable copies. `git status` is
clean; no stash.

## 1. What I understand the thread to be

I am the **coordination window** for the Fernwood release loop, between a closed lap 6 and an unopened lap 7. My job
is to run the loop's beats and route work to lanes (build, design, backlog, teardown), never to do the lane's work in
this window. The standing memory says the same: *coordinator routes, never absorbs.* Paul's model of the work is the
seven-step agile shape (groom → commit → build → test → clear → deploy → close), and lap 7 is meant to be a big build
lap run as ONE candidate.

## 2. Current state — what I verified vs. what I am taking from the brief

**Verified in the repo tonight:**
- Lap 6 is closed in `CYCLE-LOG.md` (line 2317, `outcome:closed at 2026-09-10T22:45Z`). `release-state.py` reads
  ARMED, beat 11/12, candidate `318416a`, seats pass True, six laps closed. It cannot observe beat 12 (deploy) by its
  own note, so "deployed to paul + home" rests on the chronicle and the brief, not on this tool.
- `cycle-state.json` carries L7-P1..P5 pre-registered. Gate ①'s `ux_clause` reads *UNCHECKABLE — no artifact
  convention*, which is exactly L7-P2's subject.
- `check-ux-sweep.py` reads rested (last 2026-09-10, 0 viewer commits, 0 laps), which matches the brief's
  expectation for beat 1.
- `qa-behind.py`: QA serves `318416a`, 97 commits behind HEAD, no app surface changed. So every commit since the
  candidate is register, handoff and tooling. Good.
- The bug lane's headline holds: `viewer.html:7316` `PAGES_WORKERS` maps only `fernwood-qa`, `fernwood-lab`,
  `fernwood-home`. `wrangler.toml` declares envs `qa · lab · home · bob · paul`. So the `paul` and `bob` Workers exist
  and the page served at a `myhome-*` origin cannot reach them. That is the "Worker map first" item.
- The design plan's §4 apply list exists: ten ordered steps (front door B2 · post-signup bubble · account receipt at
  naming · gate card + PO-box + optional unit line · one filled commit on ranking · receipt with live change links ·
  shelf one control · account sign-out/recovery/house-named refusals · D8 punch items · D6/D9 only if ruled in time).
- The backlog window's brief §8 (state at close, HEAD `7631c34`) agrees with this brief on the teardown list, the
  eleven rulings given, and the "Worker map first" ordering.
- The memory the brief names, `feedback_build_expert_audits_the_plan_before_the_build_window`, exists, but under the
  home-directory project's memory dir, not this repo's. This session did not recall it at start. The brief carries
  the rule in §5, so nothing is lost, but the memory is not where a Tate-Tracker session would find it.

**Taken from the brief, not re-verified:** that production (`paul` est-d93508, `home` est-e6696a) serves `318416a`
byte-identical; that gate ① was 5 of 5 in visible Chrome; that Paul cleared it; the environment vocabulary
(legacy ≠ production; never push `origin/main`); that the three lane sessions (`tate-tracker-0d`, `-8d`, `-21`) have
actually exited rather than merely been told to.

## 3. The open decisions

Nothing is mine to decide. Three are Paul's and the brief asks them once at lap open:

1. **"Go teardown"** on the named list: `bob` deployment (nigel/aida procedure) · the Midtown scratch instance (after
   asking what else reads it; keep the ownerless neutrality fixture) · `pkirsch`@qa · the seven qa seat houses
   `rihhdp · d7teqw · bzr4gb · pr9pwl · otzfk2 · ofd6vk · gndlvf` · lab's seven. Keep `pkirsch`@paul, `PAK`/Homey,
   `marguerite`@home, est-qa0001 itself. Irreversible, so it needs his word in the window that runs it.
2. **Which deployment is his working model**, `paul` or `home`.
3. **What "synced" means** beyond one sign-in reaching every house.

And one that is a sequencing fact, not a question: **nothing in the bundle applies until the eleven design rulings
are read as given.** §4c says all eleven are given. §4 (earlier in the same brief) still shows several as "apply
held." I read §4c as superseding §4.

## 4. What has NOT been tested or verified

- **The Worker map fix is designed nowhere yet.** The brief orders it first in the build half and points at the
  bug FINDINGS §3.1 for the finding, but no plan step, no symbol list, no check exists for it. The
  engineering-partner audit is supposed to produce that. Until then "first" is an order, not a task.
- **The full battery needs a journey the harness does not have.** Design plan §4 says the candidate is walked by
  five seats across J0 + J2 + J3 *plus a sign-out/return journey* that `journey-walk` has no stop for (D4). The
  brief's §5 and §9 do not name this. If it is not built in the build window, gate ① will pass on a battery that
  never exercised the account-lifecycle screens.
- **The teardown may be structurally unable to run on the qa seat houses.** CLAUDE.md's own line on
  `household-fixtures.py --teardown`: nothing writes `syntheticFixtureRun`, so every fixture row is unprovable and
  one unprovable row stops the whole run. The brief's rule ("one unprovable row stops the run; refusals reported")
  is the right rule, and it may mean the seven qa houses cannot be torn down by tool today without first landing
  the stamp. Bob's deployment is a different mechanism (Wrangler delete, the nigel/aida procedure) and is not
  subject to this.
- **"Lab's seven" has no ids anywhere I can find.** A named list with an unnamed half is not a named list yet.
- **Paul's lost condo note recovery** via paired-device sync is marked untested in the brief and I found nothing
  since that tests it.
- **`check-canon-scope.py --deep` at `home`** (row 33: two places under Mom's estate id) has not run since her
  signup. Two sections of the brief give it to two different owners (§4 teardown lane, report only; §9.6 this
  window, at open). I would run it here at open because it is read-only, and say so.
- **`post-deploy.py` red at production** is explained (row 32, stamp vs. payload) but the fix (compare the
  `worker.js` blob hash) is L7-P4 and unbuilt. Until it lands, a red post-deploy at lap 7's production deploy will
  need reading by hand, and a green one is not proof either.
- **Worker sha vs. Pages sha.** TIER 1 · 23 records the lap 6 Worker as `d0cec6f` and Pages as `318416a`; the brief
  says "byte-identical." Those can both be true (same `worker.js`, different `BUILD_SHA`), and that gap is exactly
  row 32. I am flagging it so nobody reads the two shas as a contradiction later.
- **Session-start health probe** flagged Fernwood weather history newest entry 2026-09-06, four days old, recorder
  every 6 h. That is legacy-side and outside this brief, but it belongs in beat 1's health sweep and the brief
  does not mention it.
- I have not run the CLAUDE.md pickup block. The instruction was to write this and wait.

## 5. What I would do next, on Paul's "open lap 7"

1. Beat 1 sweeps, read-only: health probe (including the weather-history gap above) · `watch-accounts` ·
   `watch-feedback` · `read-mom-feedback --pickup` · `check-ux-sweep` (expect rested) · `check-canon-scope --deep`
   at `home` (row 33), report only.
2. Write the `## Lap 7 — <date>` heading with `<!-- outcome:open -->`, then the beat-6 commitment table in his
   words: A applied founding-flow design (six exhibit rulings + five sweep rulings) · B account lifecycle · C G6
   telemetry · D Worker map for `myhome-*` origins · E teardown as a process row. Exclusions, each with its ruling:
   single sign-in door = lap 8 · zones preload · INVITE & JOIN · address validation. `release-state.py --write`.
3. Commit-phase rule: spawn engineering-partner (path-evaluation) to audit §4 of the design plan + FINDINGS §3.1 +
   G6 (TIER 2 · 10/13) + account lifecycle (TIER 2 · 18) and write `.plans/<date>-lap7-build-PLAN.md`. Ask it to
   name the missing sign-out/return journey stop and the Worker map's symbol list explicitly. Paul reads the plan.
   **Paul, 2026-09-10 (while this readback was being written):** the build commitment is to be *ratified and
   thought through* by the engineering partner into a detailed plan, and *"call another expert like the UX expert
   to help close any last-minute design decisions."* So before the engineering-partner audit, one ux-expert
   consult on whatever the design plan still leaves open — §4 names D6 and D9 as "only if ruled," and the
   sign-out/return screens have no walk yet. The ux-expert closes the design questions; the engineering-partner
   then plans against a closed design, not an open one. Both are commissioned from this window and run in the
   commit phase, before the build window opens.
4. Reopen the backlog window from `handoff-backlog-refinement.md` via `~/.claude/tools/succeed.py --open
   backlog-refinement`; grade its readback. It is the one door to `BACKLOG.md`; I do not write that file.
5. Ask Paul once, in one message: go teardown (named list, with the `syntheticFixtureRun` caveat stated) ·
   working-model deployment · what "synced" means.
6. Open the build window from a brief pointing at the engineering-partner's plan; declare the freeze on its
   candidate. Then deploy qa → full battery once → Paul's walk (two visible Chrome tabs, door link + `pkirsch`, one
   throwaway he names, the 3–40 username rule stated) → production `paul` + `home` → close.
7. Runs with no ruling needed at open: practice-steward §2 amendment for the content clause (L7-P3) · the security
   report's home (`.security/` not in FINDING_DIRS; I have not located FINDING_DIRS) · post-deploy blob compare (L7-P4).

## 6. Where the brief left me unsure or looks thin

- **§6 says `tools/check-backlog-ready.py` and `handoff/patches/` are uncommitted for Paul.** They are not.
  `ed3a943` is titled "④ applied — the row: three-state parser and the --ladder derived view; the header-pass
  patches kept as the record," and the tree is clean. Someone committed Paul's decision. If that was on his word,
  §6 is stale; if not, it is a write that should not have happened, and he should know which.
- **§4 and §4c disagree on colour.** §4: "colour = one-line noun fix." §4c: "TWO colours (account colour AND a
  colour per estate)." I am reading §4c as the later ruling. The beat-6 table should carry the §4c wording.
- **§4b says the backlog window "stays open"; §4c says every lane closed.** Same resolution: the later line wins,
  and §8 of the backlog brief confirms it closed on his word.
- **G6** is cited only as TIER 2 · 10/13. I do not yet know what G6 is beyond "telemetry" and would read those rows
  before commissioning anything against them.
- **The gate kit's "3–40 username rule"** is cited as a lesson (row 25) without the lesson's content. Readable from
  the register, but the brief does not say what went wrong.
- **The old coordination window (`paulkirschenbauer-96`) is still live** and shares this working tree. Per the
  concurrent-session guard I will not write or commit anything in this repo beyond this file until Paul says the
  seam is complete and that window is closed, or he tells me to drive both.
- **The brief never names the production deploy mechanism** beyond "his `!` commands if the classifier blocks
  you." I assume `pages-deploy.py --env paul` and `--env home` plus `deploy-worker.sh` per env, and that the
  deploy calls `release-gate.py` and `post-deploy.py` itself. Not verified.

Nothing started. Waiting for the grade.
