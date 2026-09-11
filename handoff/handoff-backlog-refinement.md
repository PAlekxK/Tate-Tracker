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
