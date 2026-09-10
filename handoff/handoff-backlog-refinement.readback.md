# READBACK — backlog-refinement (the standing backlog session)

- written: 2026-09-10 ~5:50 PM ET · by the incoming session · at HEAD `737b535`
- brief read: `handoff/handoff-backlog-refinement.md` (stamped `cf2a078` + one uncommitted row)
- for: the outgoing session, to grade against its own context · and Paul

## 0 · The stamp — verified, consistent

The brief says `cf2a078` plus one uncommitted row on local main. HEAD is `737b535`, one commit past
`cf2a078`, and that commit is the row (`BACKLOG.md` +21, `## 🤝 INVITE & JOIN` at `:620`) plus the
rewritten brief. Consistent. Two things the stamp does not say and I measured:

- `737b535` landed **81 seconds before this session opened**, and the reflog shows HEAD moving a dozen
  times in the prior twenty minutes. The coordinator is live and commits on this tree under me. I will
  `git status BACKLOG.md` before every write and stage explicit paths only.
- `737b535` carries no `Backlog-Register:` trailer; `registrar-sweep.py --since cf2a078` lists it as the
  one unregistered commit. That is the outgoing session's own commit, flagged by its own instrument.
- `cycle/release/cycle-state.json` and `worker/digest.json` are dirty in the tree, as the brief says.
  Not mine, never committed.

## 1 · What I understand the thread to be

A standing, live conversation with Paul over `BACKLOG.md`. Three jobs: refine rows with him in the
loop, surface what is stale, and keep a short **queue for the next two build laps** that a build
window pulls from at its commit phase. The commit-phase pull is the only thing that freezes, and the
freeze is on the rows a build lane names, not on the document. I am neither the coordinator (routes,
merges, holds the freeze) nor a build lane (never edits status prose). I never push `origin/main`.

## 2 · Current state, as I measured it — where it differs from the brief

| brief says | I measured | so |
|---|---|---|
| §6·2: apply *"`→ PLAN ·` flips (2 false pointers)"* | The registrar handoff records both flips at `e5626b7`. `check-backlog-ready.py` reads **0 false readiness claims** at HEAD. `→ PLAN ·` sits at `:139` (vocabulary-nicknames) and `:1187` (frozen-fernwood-catchup) | **Already done.** The brief over-reports open work here. Only the `row:` three-states half of ④ is open |
| §6·2: *"route the 5 stale-prose rows"* | The checker sees **2** literal *"Not stamped."* rows: guru-retrieval (`:1499`) and C7 condo (`:3355`). The registrar's five (`:139` onboarding · `:248` zones · `:252` weather · guru · C7) have moved by ~31 lines, and the other three carry stale prose in a form no instrument reads | I can route the two by name today. The other three need a human reading of the sentence beside a true stamp before I can name what is stale. **Not verified which sentence.** |
| §3·3: the ④ implementation is in the **AUDIT** | The ④ spec (three `row:` states, ~45 lines, the scripted header pass, its falsifiers) is **§2 of the RECOMMENDATIONS packet** (`.plans/2026-09-10-link-syntax-and-proposal-intent-RECOMMENDATIONS.md`). The audit is practice-steward's structural read and does not contain ④ | Wrong pointer, right neighbourhood |
| §3·4: `.plans/2026-09-02-rationalization-PROPOSAL.md` is *"still unread by Paul, its own §7.2 stale"* | That file's own header reads **APPLIED 2026-09-03 in `9f17419` `[paul-approved]`**, and it has sections 0–6, no §7. A **third** rationalization exists that the brief never names: `.plans/2026-09-10-rationalization-PROPOSAL.md` (57 KB, `988a682`, `stage: draft`, *"agent-proposed — Paul rules · Nothing here is applied"*). `check-backlog-drift.py` reads **OWED** and names it | I believe the brief means the **09-10** file. The board's ⑦ line 163 has the same slip. **§7.2 does not resolve in either file and I did not chase it further.** |
| §4: INVITE & JOIN *"uncommitted at the moment of writing, committed right after"* | True: `:620`, in `737b535` | consistent |
| §4: Paul ruled the QA synthetic lap is **founding only**; Bob's invite unspent and what it does when spent is **UNRULED** | Read in the row itself, verbatim-marked | consistent |

Instruments at HEAD, for the record: `check-backlog-ready.py` 🔴 **166 flags across 44 plans**, exit 1
(red on every run, so nobody reads it as a signal); its selftest **34 pass / 1 fail**, the pre-existing
*"two in flight with no exception"* case the registrar flagged as a test-vs-ruling judgement, not mine.
`registrar-sweep.py --selftest` 17/17. `check-backlog-drift.py` OWED: 14 commits since the 09-08 head
marker, plus the 09-10 draft unapplied.

## 3 · The open decision — and the one the brief did not name

**On the board (①), Paul's, unchanged by me:** X-Estate sequencing · interests-label scope (blocking a
lane) · product-steward absorption · the condo's return via `adopt` · Paul's address in `est-qa0001` ·
`anchors.py` at Bob's address · the security seat after G1 · Bob's invite joins-or-founds.

**The one I am actually blocked on, which the brief does not state as a decision:** two handoff briefs,
generated at the same minute, claim the same file and the same first task.

- `handoff-backlog-registrar.md`: *"You are `BACKLOG.md`'s SOLE WRITER, as a SCRIBE — not an author…
  The next registrar session builds ④ FIRST."*
- `handoff-backlog-refinement.md`: *"`BACKLOG.md` is yours to edit with Paul in the loop… Apply the
  ruled-and-parked ④."*

Those are not the same seat. The registrar transcribes and never authors a status; this window
*refines rows* with Paul, which is authoring behind his gate. The board's own ⑥ line says *"one door or
it isn't a door — Paul's, unresolved."* So: **is the registrar seat absorbed into this window, or is it a
separate lane that is not open right now?** If both are live, we are two writers on one file the same
hour the audit said that was the disease. My recommendation: this window carries the registrar's scribe
discipline for forwarded rows (verbatim, attributed, read back) *and* refines with Paul in its own
marked voice, and the registrar brief is archived as folded in. But that is a ruling, not mine.

A second, smaller line to draw: ④ edits `tools/check-backlog-ready.py` and 21 `.plans/*-PROPOSAL.md`
headers (the packet offers *"+13 other orphans if desired"*, which reach into `-PLAN.md` files). My
brief says never edit a `.plans/*-PLAN.md` a build lane owns. I will take the 21 proposals only and
leave the 13 unless told otherwise.

## 4 · What has NOT been tested or verified

- Everything the brief's §7 lists: the 174 qa accounts and 7 lab households, the qa Pages dry-run
  under the changed route-row shape, every `file:line` older than an hour.
- The three non-"Not stamped" stale-prose rows: which sentence is stale, and whether it still is.
- §7.2 of any rationalization proposal — the reference does not resolve.
- Whether the 09-08 zones session ever ran. `handoff/handoff-zones-session.md` was composed **by a
  prior backlog-refinement window** on 09-08 at `9a762b0` for exactly the ask Paul just repeated; no
  readback file exists for it. Eight zones commits landed 09-08 → 09-10 (the automation assessment at
  `2395268`/`2acdace`, the candidate render, the mowing falsifier), so *some* zones lane worked, but
  the record does not say it was that session. That brief also says *"you are the FOURTH live window"*
  with a window map that no longer matches today's three.
- I have not read the zones plan §0, the 09-10 assessment body, or the 09-10 rationalization proposal
  in depth. Everything I say about their content is from headers and grep.
- I ran no KV read, no deploy, no browser. Nothing was written except this file.

## 5 · What I would do next — folding in Paul's message of a minute ago

Paul, mid-turn: get a good sense of how developed each feature and backlog item is; a more or less
systematic way of organizing them; line up a couple of things for the next few builds from the backlog
(what we are close on, what questions need answering, what needs exploring); and **zones gets its own
launched session because it is so meaty.** That is task 3 of the brief, sharpened.

1. **Get the ownership ruling (§3) before any `BACKLOG.md` write.** One question, one answer.
2. **④, the half that is open** — `row:` three states in `check-backlog-ready.py` plus the scripted
   header pass over the 21 proposals, as a **diff for Paul**. Falsifier from the packet §2f: 14
   AWAITING, 0 proposal-orphans after landing. Route the two *"Not stamped."* rows to their owners by
   message. Fix nothing else in that tool; the failing selftest is a judgement call I will name, not take.
3. **The queue as a DERIVED view, not typed prose.** The organizing axes Paul asks for already exist —
   tier (what unblocks it) × class (engine/config/instance) × plan stage × pointer state — and the
   audit's §3·D finding is that the register is *duplicated, not derived*. So the "how developed is each
   item" read should be **computed from the 21 plan headers**, not written by hand into a section that
   decays. Measured at HEAD: `build` 3 (c4 environments · c6 door-for-paul · guru-retrieval) · `qa` 1
   (onboarding) · `design` 1 (zones) · `ready` 3 (c7 condo stamped; c3 trace-query and product-name
   *agent-proposed, unstamped*) · `concept` 6 · `draft` 1 (testing-architecture) · `retro`/`executed` 2 ·
   **3 with no header at all** (map-region-smoothing · three-environments · multi-tenancy 09-10). I would
   propose a small reader (a `--ladder` view on the existing checker, or a sibling) that prints stage ·
   stamped? · row pointer · declared seats missing · **what would make it READY**, and put *that* to Paul
   to rank. It is a tool edit, so it waits on a go. ⚠️ I will not invent a new taxonomy; the gap is a
   view, not a vocabulary.
4. **Zones: compose a fresh launch brief at HEAD, not reuse the 09-08 one.** Zones is at `design`,
   stamped 09-07 *for the stage, not the build*; its co-requisite is row 8 (capture write path,
   concept) and its long-horizon half is row 9 (Process B, concept); the 09-10 assessment moved the
   house and driveway from derivation to download. The 09-08 brief is two days and eight commits stale
   and describes a window map that no longer exists. On Paul's go I write `handoff-zones-session.md`
   anew, sha-stamped, with the zone questions still open listed by name — and this window keeps the
   `BACKLOG.md` rows 7/8/9 edits, as the old brief already ruled.
5. **The 09-10 rationalization proposal**: offer to walk it with Paul, section by section, never
   summarize it as current. It is 57 KB and unread; drift says a pass is owed.
6. Then stay open.

## 6 · What looks thin, said plainly

- The brief's first mechanical task is half done and the brief does not know it. That is the exact
  failure the repo's own rule names (*an unchecked box is not open work*), on the brief that tells me
  to apply the rule.
- The brief points at the wrong rationalization file and the wrong section for ④. Both are recoverable
  from the neighbourhood, but a fresh reader without the registrar handoff beside it would have started
  on a document Paul already approved.
- The registrar/refinement seam is the real gap. Two briefs, one file, one first task, opposite
  authorship rules, same timestamp. Nothing in either brief says which one survives.
- "Queue for the next two laps" has no shape yet — the brief says *"a short section at the top of
  `BACKLOG.md` (or a file it points to)"*, and the top of `BACKLOG.md` is the region two rationalizations
  fought to keep as pointers only. I would rather it be a file the head points to, derived.
