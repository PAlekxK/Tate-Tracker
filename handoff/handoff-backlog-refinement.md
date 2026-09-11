# Handoff: fernwood — the STANDING BACKLOG SESSION

<!-- generated 2026-09-10 ~5:45 PM ET · source: Tate-Tracker@cf2a078 + one uncommitted row on LOCAL main
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Every file:line has a half-life of about an hour when several lanes are live. Cite the symbol, stamp the sha. -->

## 1. Mission — what this window IS

`[paul-stated 2026-09-10]`: *"I almost think it's worth having just a standing session that's going
through the backlog and helping me refine it, and also queuing up items for the next couple laps of
build. Our commit phase is the one time we pull from the backlog, so that's the only time it really
needs to be frozen. We can keep having that conversation going in real time in another session."*

**You are that session.** A live, continuing conversation with Paul over `BACKLOG.md`: refine rows,
surface what is stale, and keep a short **queue for the next two build laps** that a build session can
pull from at its commit phase. You are not a build lane and not the coordinator.

## 2. The three windows — and which you are

| window | job | never |
|---|---|---|
| **coordination** (`tate-tracker` main, the one that opened you) | routes, sequences, holds the commit-phase freeze, merges | writes a feature |
| **this one — backlog** | refines the backlog with Paul in real time; queues the next two laps | commits code; pulls rows into a build |
| **build** (opened separately, per item) | pulls from the queue at its commit phase and builds | edits `BACKLOG.md` status prose |

⛔ **The freeze is on the PULL, not the document.** When a build lane declares a commit-phase pull, hold
edits to the rows it names until it releases. Everything else keeps moving.

## 3. Read first (in this order)

1. `.plans/2026-09-10-OPEN-ITEMS.md` — the consolidated board. Section ⓪ is the environment map:
   **"production" and "main" each name two things.** Section ⑥ is the register-and-process findings
   that are *your* material: the register is DUPLICATED not DERIVED; `BACKLOG.md` has at least four
   writers plus six shadow lap-scoped registers; `→ PLAN ·` and the three `row:` states were ruled
   today and not yet applied (2 false pointers, 5 stale-prose rows owed to owners).
2. `BACKLOG.md` lines 1–75 — the vocabulary (`READY`, `→ PLAN ·`, `row:` three states, `wip-exception:`).
3. `handoff/handoff-backlog-registrar.md` — the registrar lane's handover — and
   **`.plans/2026-09-10-link-syntax-and-proposal-intent-RECOMMENDATIONS.md` §2**, which holds the ④
   spec (`row:` three states, ~45 lines + a scripted header pass, falsifiers). *(Corrected after the
   readback: the brief first pointed at the practice-steward AUDIT, which does not contain ④.)*
   `.plans/2026-09-10-backlog-management-AUDIT.md` is the structural read beside it.
4. **`.plans/2026-09-10-rationalization-PROPOSAL.md`** (57 KB, `stage: draft`, agent-proposed) — **still
   unread by Paul.** Do not summarise it to him as if it were current; offer to walk it with him.
   *(Corrected after the readback: the brief first named the 09-02 proposal, which its own header says
   was APPLIED 09-03 `[paul-approved]`. The "§7.2 stale" reference resolves in neither file; treat it as
   the coordinator's unverified relay.)*

## 4. State — measured at close

- **Paul ruled today: the QA synthetic lap is FOUNDING ONLY** — owners setting up their own house.
  No invitations, no joining this round. Bob's invite stays unspent and what it does when spent is
  **UNRULED**.
- **New row, uncommitted at the moment of writing, committed right after:** `## 🤝 INVITE & JOIN`
  (before `## 🧭 SEGMENT HYPOTHESES`) — Paul's described shape for a later lap, with the scope
  questions and a falsifier. It exists because the coordinator measured that founding never reads the
  invite's `conferred*` promise, so there is no join path in code.
- **Open rulings on the board (①):** X-Estate sequencing · interests-label scope (blocking a lane) ·
  product-steward absorption (the deciding edit is `CYCLE-MAP.md`) · the condo's return via `adopt` ·
  Paul's address in `est-qa0001` · `anchors.py` at Bob's address (gated) · security seat after G1.
- **Live defects (②)** and **instrument gaps (⑤)** are on the board; you do not fix them, you keep
  their rows honest.

## 5. ⛔ Guardrails

- **One writer per file.** `BACKLOG.md` is yours to edit **with Paul in the loop**; never edit
  `worker.js`, the HTML surfaces, the walk harness, or any `.plans/*-PLAN.md` a build lane owns.
- **Transcribe, don't author, a lane's status.** A row's status prose belongs to the lane that
  measured it; you may flag it stale and route it, not rewrite it.
- **An unchecked box is not open work.** Before calling a row open, probe reality (grep the symbol,
  run the check). Rows over-report open work, never under.
- **Never `git push origin main`** (Mom's frozen production). Commits to local main are fine.
- **Two hook-generated files are dirty in the tree — `cycle/release/cycle-state.json`,
  `worker/digest.json`. Never commit them.**
- **Rulings are Paul's.** When two readings of a row exist, put both to him with a recommendation.
  `[paul-stated]` in a row means his words; do not paraphrase them into a stronger claim.

## 6. First tasks (ordered)

1. Verify the sha and read §3. Write your readback (the launcher tells you where).
2. Apply the half of ④ that is still open: `row:` three states in `check-backlog-ready.py` plus the
   scripted header pass over the 21 proposals, **as a diff for Paul**. *(Corrected after the readback:
   the two `→ PLAN ·` flips already landed at `e5626b7`, and the instrument sees 2 "Not stamped."
   stale-prose rows, not 5 — route those two by name; the other three need a human read of the
   sentence before anyone can say what is stale.)* Do not rewrite anyone's row.
   ⚠️ **Ownership seam, Paul's to rule (raised by the readback):** the registrar brief names a SOLE
   scribe writer of `BACKLOG.md`; this brief names you a refiner with Paul. Until he rules, write
   nothing to `BACKLOG.md` except forwarded rows transcribed verbatim and attributed.
3. Draft **the queue for the next two build laps** as a short section at the top of `BACKLOG.md`
   (or a file it points to), each entry naming its row, its plan pointer state, and what would make
   it READY. Put it to Paul; he ranks.
4. Then: stay open. Take Paul's refinements as they come.

## 7. What is NOT verified — say so if asked

The 174 qa accounts and 7 lab households (no KV read by the coordinator today). Whether deploying the
new Pages build to qa affects existing accounts under the changed route-row shape (a dry-run was
running at handoff time). Every `file:line` older than an hour.

---

## 8. STATE AT CLOSE — 2026-09-10 ~10:05 PM ET · HEAD `7631c34` (+ this commit)

**Closed on Paul's word** (*"let's close out all the other sessions you've got running to be sure we don't have any
loose ends"*). The standing backlog window reopens from this brief via `succeed.py` when he opens lap 7.

**Uncommitted, for Paul, by design:** `tools/check-backlog-ready.py` (the ④ `row:` three-state parser + the
`--ladder` derived view; selftest 41 pass, 1 pre-existing fail) and `handoff/patches/` (the header-pass diff, already
applied at `326791c`; the patch is the record). Apply or discard is his.

**Rows added tonight, TIER 1:** 23 the build-description chain (into lap 6, act 6 done) · 24 `/api/session` lies to a
founder · 25 the gate kit for Paul's walk (PAK/Homey; username-rule lesson) · 26 the founding-flow design window →
the lap-7 UX bundle (closed `112894c`; both sweep passes, the content read, the plan, six exhibits; **all eleven
rulings given**) · 27 the lap-7 UX bundle (a/b/c ruled: lifecycle in · colour noun only · one candidate) · 28 the
feedback bubble from account creation · 29 the colour noun · 30 Paul's 6:22 PM bubble note · 31 content-steward
reads every walk (① done; ② a gate-① content clause, lap 7's open) · 32 `post-deploy.py` container vs payload ·
33–40 Mom's onboarding answers (user-researcher; 33 = two published places under her estate id at `home`) · 41
cross-device sign-in (single door now a RULING; lap 8) · 42 the lost condo note (in his phone's outbox behind a
"Saved on your phone ✓"; mechanism = no Worker mapping; "fold in") · 43 empty *Your Perspective* card · 44 Settings /
What you told me, second sighting · 45 `myhome-*` origins have no Worker mapping (lap 7, first by class) · 46 the
account model (ruled: one sign-in page routing to every estate; lap 8).
**Also:** § INVITE & JOIN (three roles · second estates · member spill-over; Bob's invite overtaken) · § ADDRESS
VALIDATION (fresh, not this lap; unit number optional) · § THE FIFTH LENS (people found their own; Fernwood-in-
production the one exception; **the teardown ruling**) · § THE STANDING PRINCIPLE (capture what personalizes;
describe-or-infer open) · ⏭ THE NEXT TWO LAPS (derived queue) · ONE DOOR (the registrar folded in) · the
21-proposal header pass · C7 set aside + the Midtown scratch instance retired · C9's founding clause struck · P-26
reworded · TIER 2 · 7 Z-13, the cleaned 23 as leading candidate, labelled and watched, preload on Mom's founding.

**Rulings given, NOT YET ACTED — lap 7's opening queue:**
1. **The teardown** — Bob's deployment first (the nigel/aida procedure), the Midtown scratch instance (keep the
   ownerless neutrality fixture), `pkirsch`@qa (*production only*), PAK/Homey, the seven qa seat houses
   (`rihhdp` · `d7teqw` · `bzr4gb` · `pr9pwl` · `otzfk2` · `ofd6vk` · `gndlvf`), lab's seven — a NAMED list, one
   unprovable row stops the run; `marguerite`@home and `pkirsch`@paul kept. The go is his.
2. **`check-canon-scope.py --deep` at `home`** (row 33) before any digest there.
3. Rows 33–40's items (user-researcher), 43/44/45 (exhibit- and bug-derived), the not-punch-sized list in the
   sweep trail, and the 15-item punch list — all inside lap 7's one candidate.
4. The gate-① content clause (31 ②) and the post-deploy blob check (32) at lap 7's open, per the chronicle's
   pre-registrations.

**Still Paul's, unanswered:** which deployment is his working model (`paul` vs `home`); the three unclassified
proposals (canon-ingestion · interests-as-activities · the 09-10 rationalization draft — my reading: `proposed`);
the surname in two seat trails and the pushed staging history; the tool diff.

**What I would put in front of him at lap 7's open, one line each:** the Worker map first, because a real
household is printing false receipts today · the teardown before the first battery, because every battery adds
houses to it · row 33's collision before `home`'s Guru speaks for anyone · then the bundle, with all eleven
design rulings already in hand.

**Blind spots for the successor:** the coordinator (`paulkirschenbauer-96`) holds the map, the candidate and the
apply — check with it before any write it might be sequencing; `git status BACKLOG.md` before every write, explicit
paths only; the register-trailer convention (`Backlog-Register:` / `Backlog-Forwarded-By:` in the final paragraph
with `Co-Authored-By:`); and two reader traps measured tonight — `wrangler kv key list` without `--remote` returns
`[]` exit 0, and `watch-feedback.py` prints a stale "checked Nh ago" line when it did not read.

---

## 9. STATE AT CLOSE — 2026-09-11 ~3:55 AM ET · HEAD `7450b9d` (+ this commit) · window `tate-tracker-2a`

**Closed on Paul's word** (*"ok let's close out"*). The successor reopens from this brief; ⚠️ **§1–§8 are two earlier
sittings — §6's task list is stale on its face (④ and the queue are done); read §8 then this section, not §6.**

**Who is live at close:** coordination `tate-tracker-ea` (the map, the chronicle, the freeze) · the lap-7 build window
`tate-tracker-94` (row A in progress; rows B, C, P closed) · the ask-design window `tate-tracker-52` (plan tracked at
`927d93c`). This window is the ONE DOOR to `BACKLOG.md` `[paul-ruled "fold it in"]`; the freeze on the lap-7 rows
(TIER 1 · 45 · 42 · 26 · 27 · 28 · 29 · 30 · 31 · 43 · 44 · 32 · 23; TIER 2 · 10 · 13 · 18 · 19 · 20 · 21 · 25) is in force —
those rows take only the build's own forwards and four-field fills until the coordinator lifts it.

**What this window landed (all on `main`, none pushed):** the readback at `5c66e38` graded clean · Paul's rulings carried as
they came: synced · teardown go (PAK/Homey resolved) · row 33 reconciled against the live store · §3i deployment/environment
glosses · the eight build-plan rulings Q1–Q8 · L2's four fields on every lap-7 row · the environment model · `myhome.place` as
the production origin's ADDRESS · the STARTING NAME **My Home Place**, Home emphasized (product-name Q3 ruled; the plan can take
his stamp) · laps 8/9 scope RULED on every question · lap 10 scope (three ruled, one deferred, one lean-to-no) · laps 9 and 10
stay separate · the fourteen open items (1 deferred, 2–5 closed, 6–14 by recommendation, all carried) · the third
rationalization applied as one diff (drift reads rested at 2026-09-11) · the committed-by-ruling rung in
`check-backlog-ready.py --ladder` (48/1 selftest; reads OPEN laps by outcome marker) · sections opened in his words:
HOUSEPLANTS · CONTENT · CARDS · PRODUCTIZE LEGACY FERNWOOD · rows 47–59 · TIER 1 · 51 acted (his address deleted from qa by id).

**Still his, none blocking a lap:** the lap-8 build plan's Q0–Q8 (at lap 8's open) · the ask-design plan's §13 (fifteen rows,
his time) · lap 10 Q-10·2 (the fertilizer question as the acceptance walk — a lean to no) and Q-10·5 (five Fernwood zone
facts, deferred to lap 10's groom) · the product-name plan's `ready:` stamp · the receipt-first reorder of the weather card
(lap 9's open) · the small-lap-9 shape (lap 9's open).

**Owed by this window, not started:** run the distinct-`questionId` count (TIER 1 · 59) when the lap-8 window closes · the four
register edits the closed zones window still owes to TIER 2 · 7 and the derived-first-draft plan (lap-10 proposal's riders) ·
the PRODUCTIZE census (engineering-partner + ux-expert, citing the inventory's §2 as done) · a `#card-told` cut of the
changeable clause is content's, routed.

**Blind spots for the successor — measured tonight:**
1. ⛔ **`git commit --only BACKLOG.md`, always.** The index is SHARED with live lanes; `git add <path>` by name does NOT exclude
   what another lane staged — `dcbc660` swept in the teardown lane's staged deletion of `instance/bob.json` under a register
   message. HEAD moved before a rewrite could run, so it stands, cited by the lane's report. `--only` ignores the rest of the index.
2. **The abort guard worked once and should stay:** `test "$(git rev-parse --short HEAD)" = "<expected>" || exit` before any
   history-touching command — HEAD moves under this window a dozen times an hour.
3. **`registrar-sweep.py`'s matcher** drops a `§` prefix and splits on `·` inside a heading name, and a `TIER n · m` anywhere in
   the claim short-circuits the rest; name a heading by its words. `4766cc3` and `dcbc660` read UNPLACED for that reason and are
   placed in fact.
4. **The rung reads `## Lap N —` headings + `### Beat 6 · COMMIT` tables of laps whose `<!-- outcome:open -->` marker says open** —
   lap 5's heading still says OPEN while its marker says closed; a pre-commitment written as a `###` under lap 7 is not on the
   rung by design.
5. **Every `.plans` `depends-on:` line must be a bare path** — an annotation after the path reads as a path that does not exist.
6. **A Bash heredoc carrying long quoted markdown can be refused by the auto-mode classifier** ("Instruction Poisoning"); the Edit
   tool with anchored strings is the reliable path, and a Python line-range move (no content embedded) for block moves.
7. `MEMORY.md`'s one-door memory lives under `~/.claude/projects/-Users-paulkirschenbauer/memory/`, not this repo's memory dir.

## 10. REOPEN — the register queue held while this window was closed `[written by the lap-8 coordination window, tate-tracker-42]`

Lap 7 CLOSED at `87c7aae` (09:51 EDT 2026-09-11); lap 8 HOLDS for the testing-revamp plan; **row T lands whole and FIRST in
lap 8** (supersedes the lap-9 placement). Every line below is an unfiled carry. Carry with the register-trailer convention,
`git commit --only BACKLOG.md`. HEAD moves under you many times an hour — three windows commit on this tree.

**A. The chronicle's queue** — `grep -n -iE 'queued for the register|register carry|Register:' cycle/release/CYCLE-LOG.md | awk -F: '$1>2698'`
returns twelve lines (2862 · 3020 · 3056 · 3088 · 3141 · 3316 · 3359 · 3469 · 3480 · 3507 · 3545 · 3643); every one first
appears in git AFTER `06e3c7d`. ⚠️ **`:3316` is SUPERSEDED** — it moves row T to lap 9; carry it as **lap 8, first**
(`CYCLE-LOG.md` § "LAP 8 HOLDS", 09:47 EDT). Read `:3498` (the account is always the first layer) and `:3605` before the rest.

**B. Paul's walk PW1–PW11 + two rules** ⚠️ **ID CORRECTED by the readback's finding ①, and it was a real error in this brief** — `BACKLOG.md` already uses `W0`…`W11` for the Track A zones/map series (`W2` = *Zones, Paul draws she reconciles*; `W6` = the instance model). Filing the walk findings as `W*` would have collided with live rows. **They carry as `PW1`…`PW11` (Paul's Walk)**, ruled by coordination `[tate-tracker-42]`; the readback's own recommendation, adopted., from the coordination brief §6: W2 the looping *Create your account ›* link (lap 8 ·
A11) · W1 post-sign-out door · W7 the "early days" landing · W8 masthead spill at laptop width · W9 cards ≠ jump strip · W10
weather card · W11 the Journal's "stays on this phone" · the renderer's bare-id fragility · the seat-trails public-repo rule →
CLAUDE.md's AI-boundary section (a standing line; you file the row, coordination edits CLAUDE.md).

**C. Nine findings by id from the revamp window** (none needs it; route as rows or folds):
SEC-R1-A `mint_invite` env allow-list — FIXED `2010eee5` (cite done; optional: remove `home` from `--origin` choices) ·
SEC-R4-1 `fw-grant` localStorage-only, WebKit-evictable — lap 8 · A roster row · SEC-R3-4 seat artifacts tracked in a public
repo (.content 16 · .practice 3 · .engineering 83 · .user-research 48) — the standing rule above · UR-§5 two record SHAPES
for `ranked` in the store (bare strings vs label objects) and `estate/index.html`'s unguarded `(r && r.label) || r` prints
ids · UR-§7a Mom's protected phrase in two vintages on one account · SIZ-0c recorder bug: `transcript.answers` written from
the loaded fixture regardless of typing → row T · T9 · SIZ-T18 W2's handler registered only inside `showFrontDoor()` — a
product fact for A11 · MP-0 the reading tier is inherited from the global settings file and no Fernwood check reads it ·
UR-§7c an A+ contradiction reported, not resolved (LENSES file). Also: **three of TIER 2 · 22's four items are done** (the J3
fixture, field notes, the bare door) and the row does not say so; only `urlBefore` is open, and it is T7.

**D. Your own §9 owes** stand unless you measure otherwise (the distinct-questionId count · the zones window's four register
edits · the PRODUCTIZE census · the #card-told cut).

Four rulings at the clear (the stop rule's two classes + one-hour wait · J2 re-scoped "returning, founded nothing" · staging
pushed · lap 8 opens on row T alone) are in `CYCLE-LOG.md`'s newest section — cite, never restate. Forward any row that needs
Paul to coordination by message; you never gate him yourself.


## 11. THE GRADE — and three answers `[tate-tracker-42, coordinator of record]`

**CLEAN.** Four findings I did not have, two of them errors in my own §10:

1. ✅ **The `W1–W11` id collision is REAL and was my error** — verified: `BACKLOG.md` carries `W0`…`W8` live in Track A
   (`:1589` · `:1597`–`:1604` · `:1700`–`:1707`). **RULED: carry them as `PW1`…`PW11`.** §10.B is corrected above.
2. ✅ **THE ROW FREEZE IS LIFTED.** Lap 7 CLOSED at 09:51 EDT (`CYCLE-LOG.md:3618`); the freeze was on lap 7's pull and
   nothing has replaced it — lap 8 is not open. Coordination lifts it explicitly rather than leaving you to infer it from a
   closed lap: **TIER 1 · 45 · 42 · 26 · 27 · 28 · 29 · 30 · 31 · 43 · 44 · 32 · 23 and TIER 2 · 10 · 13 · 18 · 19 · 20 ·
   21 · 25 are WRITABLE.** A new freeze arrives by message when lap 8 pulls.
3. ✅ **SEC-R4-1 unfiled — confirmed by measurement**, not taken on your word: `fw-grant|SEC-R4|WebKit` returns **0** hits in
   `BACKLOG.md`. Real work. Your ordering (it first, then UR-§5) is right.
4. ⭐ **Your §6 mom signal is routed, not yours to carry** — 2 undispositioned arrivals (1 Guru, 1 cards, each needing its
   OWN disposition) and her last card answer 22 days ago, past the 21-day `answer-age` threshold. Surfaced to Paul as a
   mom-cycle trigger. Do not file it as a backlog row; a fired loop is not a backlog item.

**The brief §6 you could not resolve** is `handoff/handoff-fernwood-coordination-lap8.md` — your read was right.

**Standing, from here:** carry §10.A's nine unread lines with `:3316` as *lap 8, first* · then §10.C, SEC-R4-1 leading ·
correct TIER 2 · 22 once probed · regenerate the two-lap queue from `--ladder` when lap 8's shape is known, never retyped.
**Paul has now RULED all fifteen of the revamp plan's §13 questions as recommended** (`f51d8530`) — those consequences are
register material once lap 8 opens; wait for my message rather than pre-filing them.


---

## 12. STATE AT CLOSE — 2026-09-11 · the standing backlog window `[closed on Paul's word: "close all the windows out when they're done with their work… do that as work actually concludes, don't force it"]`

**Two commits, `BACKLOG.md` only, `--only` both times, nothing pushed.**

### What I carried

**`31f806c6` — TIER 1 · 60–69, the lap-7 register carries.** §10.A's twelve chronicle lines read in context and filed as
rows rather than restated: `60` `check-telemetry.py` has no `--env` (EMIT side only; `read-glance-order.py --env qa` is the
reader of record at a candidate) · `61` the three named A/H deviations · `62` two lab-fixture facts for `walk-fixtures.py`'s
row · `63` six cross-seat findings, with the box-only founding path flagged as needing a **ruling** · `64` two record shapes
for `ranked` and the renderer's bare-id fragility · `65` the device-noun copy slot + the post-sign-out marker · `66` lap 7's
qa fixture estates named, the KEEP list, and the three things lap 7 left explicitly not done · `67` **Mom's feedback PARKED**
· `68` the UR-§7c legibility row.

**`09661e38` — § PW · PAUL'S WALK (PW1–PW11), TIER 1 · 70, and TIER 1 · 69 struck.**

### ⛔ Three things a successor must NOT assume

1. **`PW3`–`PW6`'s ids are MINE, not the lane's.** The chronicle numbers `W1`, `W2` and `W7`–`W11` and then says *"W1–W6,
   the six base-level findings"* without numbering the middle four. The content is transcribed exactly; **the labels are an
   inference and the section says so on its face.** If the lane meant a different order, move the labels, not the content.
   The `PW*` prefix itself **is** ruled (coordination, on this window's collision finding) — `W0`…`W11` are live Track A ids.
2. ⛔⛔ **TIER 1 · 67 DOES NOT CLEAR MOM'S CHANNEL, and must never be read as though it does.** Parking is a decision about
   **when**, not a disposition. `check-arrival-dispositions.py` keys on **(channel, record id)** and nothing but opening the
   record supplies one; **neither record has been opened by anyone.** The watermark has not moved and **the checker will keep
   flagging both arrivals — that is it working, not a fault to repair.** The cost is on the row's face: she gets no return leg
   while the stability work runs, and Paul chose that knowingly. Her words stay in `.private/`; the row carries counts, ids
   and dates only.
3. **TIER 1 · 69 is CLOSED, and it is kept struck for its lesson, not its content.** I verified a live `CLAUDE.md`
   self-contradiction, wrote the row, and `eea77381` struck the offending paragraph **in the gap between my verification and
   my commit** — so the row shipped at `31f806c6` describing a defect that was already fixed. **The brief's "half-life of
   about an hour" for a `file:line` measured under ten minutes** with three windows committing on one tree. ⭐ **Re-read the
   file you are citing immediately before the commit, not only before the edit.** I applied it to the second commit.

### Queued, deliberately NOT started `[coordination's call; I agree with it]`

- **The rest of §10.C's nine findings** — UR-§5 is folded into TIER 1 · 64 and SEC-R3-4's standing rule is recorded in the PW
  section, but **UR-§7a** (Mom's protected phrase in two vintages on one account), **SIZ-0c** (the recorder writes
  `transcript.answers` from the fixture regardless of typing → row T · T9), **SIZ-T18** (W2's handler registered only inside
  `showFrontDoor()`) and **MP-0** (the reading tier is inherited from the global settings file; no Fernwood check reads it)
  are **unfiled**.
- **TIER 2 · 22's correction** — §10.C says three of its four items are done (the J3 fixture, field notes, the bare door) and
  only `urlBefore` is open, which is T7. ⚠️ **I did not verify the three.** Probe before editing the row.
- **The two-lap queue regeneration** — ⛔ **correctly blocked: lap 8's shape is not known.** Regenerating now would bake in a
  guess, and the section's own rule is *derive it from `--ladder`, never retype it.*
- **My §9 owes, still standing:** the distinct-`questionId` count (TIER 1 · 59, filed — what is owed is *running* it, after
  the lap-8 window closes) · the zones window's four register edits to TIER 2 · 7 · the PRODUCTIZE census · the `#card-told`
  cut, routed to content.

### Measured this session, for whoever picks up

- `check-backlog-ready.py` exits **1**, and **not because of anything in `BACKLOG.md`** — every complaint is a `.plans/`
  header on two files other lanes landed mid-session (`2026-09-11-lap8-build-PLAN.md`, `2026-09-11-testing-revamp-PLAN.md`:
  missing `row:`/`objective:`/`class:`/`stage:`/`seats:` and the four required sections; the revamp plan's `depends-on:` is an
  annotated path, which the checker reads as a path that does not exist — the brief's blind spot 5, live).
- `check-backlog-drift.py`: **rested**, 0 d. The third rationalization is applied; no grooming is owed.
- **Escape `|` inside code spans in table cells** — `(r && r.label) \|\| r` and `stored \|\| DEFAULT_SIZE` silently split
  their rows into seven cells until escaped. Nothing in the repo checks table integrity; I checked by script.
- **HEAD moved at least eight times** during this window (`d0016be` → `670eec3` → `de0bd28` → `ed39af4` → `da7e770` →
  `eea7738` → `31f806c` → `e73d509` → `09661e3`). Both commits used the abort guard and `--only`; neither swept another
  lane's staged work.

