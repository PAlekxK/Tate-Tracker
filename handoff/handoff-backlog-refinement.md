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
3. `handoff/handoff-backlog-registrar.md` and `.plans/2026-09-10-backlog-management-AUDIT.md` — the
   registrar lane's handover and the audit. **Its ④ implementation (`row:` three states, ~45 lines + a
   scripted header pass) is ruled, parked, and is the first mechanical task in your lane.**
4. `.plans/2026-09-02-rationalization-PROPOSAL.md` — **still unread by Paul**, its own §7.2 stale. Do
   not summarise it to him as if it were current; offer to walk it with him.

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
2. Apply the ruled-and-parked ④: `row:` three states + `→ PLAN ·` flips (2 false pointers), and
   route the 5 stale-prose rows to their owners — do not rewrite them.
3. Draft **the queue for the next two build laps** as a short section at the top of `BACKLOG.md`
   (or a file it points to), each entry naming its row, its plan pointer state, and what would make
   it READY. Put it to Paul; he ranks.
4. Then: stay open. Take Paul's refinements as they come.

## 7. What is NOT verified — say so if asked

The 174 qa accounts and 7 lab households (no KV read by the coordinator today). Whether deploying the
new Pages build to qa affects existing accounts under the changed route-row shape (a dry-run was
running at handoff time). Every `file:line` older than an hour.
