# Readback: ASK DESIGN · the A-ASK design pass

<!-- written 2026-09-10 ~11:05 PM ET by the receiving window (tate-tracker-52) · against Tate-Tracker@ef84c20 on LOCAL main
     brief: handoff/handoff-ask-design.md, source-stamped 7c7e4ae · HEAD is ef84c20 = the commit that wrote the brief itself
     (+ recovery draft §6b). One commit ahead of its own stamp, consistent. Nothing below is started; this is a reading. -->

## 0 · The stamp, and the thing that happened to it

- **Verified.** The brief says source `7c7e4ae`. HEAD is `ef84c20`, whose only changes are the brief (94 lines) and
  `.content/2026-09-11-recovery-copy-DRAFT.md` §6b. So the brief describes the repo at HEAD minus itself. `measured`.
- **The empty-file event is confirmed, not just reported.** `git show --stat 209bf4d` lists `handoff/handoff-ask-design.md | 0`.
  I opened this window on that file, found it empty on disk AND in the commit, and had begun reconstructing the thread from
  the commit message and BACKLOG § A-ASK when coordination's message arrived naming `ef84c20`. This readback is against the
  real brief. ⚠️ Worth one line in whatever records handoff failures: a heredoc that aborts on a backtick commits a
  zero-byte file with a commit message that claims content, and `git status` reads clean afterwards. A receiver that
  trusted the message would have "read" nothing and graded it as thin.
- **Working tree is not mine.** 8 uncommitted files (`worker/worker.js`, `BACKLOG.md`, `tools/watch-door.py`, the recovery
  draft, four untracked plans/reviews) belong to lap 7's build and the backlog window. Three peers are live: `tate-tracker-2a`
  (backlog, the one door), `tate-tracker-94` (unknown to me), `tate-tracker-ea` (coordination, the brief's author).
  `git commit --only <my paths>` is the rule and I will keep to it.

## 1 · What I understand the thread to be

**A design pass, not a build.** Paul ruled *"I say go on both"* at ~1:50 AM ET on coordination's recommendation for
*how we handle asking for their feedback*. "Both" =

1. **this window** — the A-ASK design pass that § A-ASK deferred on 2026-09-01 to *"a conversation of its own, with
   user-researcher as the first seat"*. Its deliverable is **the ask playbook**: `.plans/2026-09-11-ask-design-PLAN.md`,
   `stage: design`, `ready: agent-proposed`. Paul rules it.
2. **the ASK LEDGER reader** — `tools/ask-ledger.py`, a lap-8 RIDER (the third, beside TIER 1 · 36/37, marked RULED on the
   8/9 scope proposal at line 38). Engineering-partner's lap-8 plan builds it; **this window only writes its SPEC.**

The playbook answers, for every household and not only Fernwood: what grammar an ask uses · when the product asks
(card intro · after a signal the person gave · never a standing ask) · the ordering axis and the cap · the elicitation rule
as a check · **the fold** (an answer lands in a personalization field on that household's own record; the card reads it;
the ribbon attributes it) · the decay of the "changeable" scaffolding · where a model may draft and where the human gate
sits · which release beat reads what.

**First worked template: the weather card's card-intro ask** — TIER 2 · 11's `ask` field, lap 9 · A (ruled first row of
lap 9 at ~12:10 AM). Paul's words: *"are you interested in UV, air quality? What do people want from a data point of view
in their dash view? I think that little questionnaire helps us then decide what are the different sub-components of
weather that we present and how we highlight it."*

**Seats:** user-researcher LEADS (research mode; asking is a discovery instrument) · content-steward · ux-expert ·
security-steward (roster: what may be asked/stored per tier) · ai-advisor (where a model may DRAFT behind Paul's gate).
Each writes its own trail in its own directory; I synthesize. **Judgment is Paul's — every ask is approved before it
reaches a person.**

## 2 · Current state, verified against the repo

| claim in the brief | checked | reading |
|---|---|---|
| nothing of this work exists yet | `ls` | ✅ no `.plans/2026-09-11-ask-design-PLAN.md`, no `tools/ask-ledger.py` |
| the legacy-toolchain INVENTORY may not have landed | `ls` | ✅ **absent** at ef84c20. Its §4 THE ASK MODEL is an input I do not have; I will check again on clear and not wait on it |
| fernwood-11 unruled, recommendation written | read the card | ✅ recommends **keep-asking-and-instrument-her-doors**, user-researcher first. fernwood-12 (the non-plant suggest-add fence) coupled and decided after. fernwood-17 (a lens has no inputs of its own) already binds the elicitation lens |
| the ask→fold→attribute loop exists only for Fernwood's plant cards | `questions.json` | ✅ 22 questions, **6 active**, `_foldTarget` shapes: `bloom` ×7 · `confidence` ×2 · `variety` ×1 · `observedGrasses` ×1 — every one a field in Fernwood's instance JSON |
| nothing reads across every ask | `grep` | ✅ readers exist per channel (`read-mom-feedback`, `read-onboarding`, `elicitation-lens`); none joins served → answered → folded → row |
| lap 7 building, laps 8/9/10 scope ruled | CYCLE-LOG 2698–2900 | ✅ weather card = lap 9 first row (9·2); ledger = lap 8 rider; lap 10 theme ruled |
| the elicitation-lens line in the pickup block | read the tool | ✅ **and it already encodes an ask CONTRACT in code** — `CONTRACT = {use, not-use, who-sees, reversible}`: every ask says what the answer is used for, what it is not used for, who sees it, and that it can be changed. The playbook should CITE this, not restate it |
| the recovery ask + receipt as tonight's worked example | read §0–§2 | ✅ a real, Paul-confirmed instance of an ask that names use · who reads it · when · the second door, with a per-sentence falsifier table (§4). This is the closest thing the repo has to a finished ask under the contract, and it is a **security ask, not a personalization ask** — useful for grammar, not for the fold |

## 3 · The open decisions, as I read them

1. **fernwood-11 — which surface serves the ask.** Options on the card: re-scope the confirm queue · keep asking and
   instrument her doors · make the Guru the primary capture surface. The recommendation is the middle one. My plan
   recommends; he rules. ⛔ The third option is a material change to the AI boundary and is his alone.
2. **The weather intro's words.** Content-steward drafts; nothing ships from this window.
3. **Whether a model may draft asks at all.** ⚠️ **I think this is narrower than the brief states, and I want the grader
   to check me.** CLAUDE.md's AI boundary already rules: *"Card phrasing today = the deterministic template bank in
   harvest-questions.py, NOT AI… revisit AI-draft-behind-the-gate only if the loop proves durable — >10 answered across
   reseed cycles."* And § CONTENT · CARDS and CYCLE-LOG both already say the card-intro ask *"is an ask-path surface, so
   AI may draft it behind the administrator's approval."* So there is a standing threshold on one side and a
   PROPOSED-shape sentence on the other. The real question for ai-advisor is not *may a model draft* but **has the
   >10-answered threshold been met, and does it even apply to a card-intro ask** (which is not a confirm card and has no
   canon target). I do not know the current answered count; `_ordering`'s note says `momqueue_tapped` was 3 across 60
   days as of 08-12.

## 4 · What is thin, or where the brief and the record disagree

- **⭐ "ONE ask (not a questionnaire of six)" is the brief's reading, not Paul's words.** §4·3 says the weather template is
  *"the ONE ask (not a questionnaire of six)."* Paul said *"that little questionnaire."* The register row (TIER 2 · 11) and
  § CONTENT · CARDS both say *"one short questionnaire… offering the sub-components the address cannot derive a preference
  for."* The elicitation ruling is *never ask what you could derive* — and a preference for UV over pollen is **not
  derivable from an address**, so the ruling does not by itself collapse the questionnaire to one field. I will treat the
  count as **an open design question the plan must argue with the seats**, not as settled by the brief. If coordination
  meant "one ask-moment, several checkboxes," that reconciles both and I would like it said.
- **The evidence base for "when to ask" is one household, one device, one active day.** The 0-for-35 measurement is Mom.
  The playbook is for every household. Real non-Fernwood ask data is essentially the onboarding interests ranking
  (`read-onboarding.py`, mostly synthetic rows at est-qa0001). The plan has to say this on its face and grade its "when"
  rules `inferred`, or it will read as validated when it is not.
- **"Derived, never typed" vs. where the ask fields live.** The ledger reads *"the rows' ask fields."* Today an item's
  ask field is **prose inside a BACKLOG.md table cell** (see TIER 1 · 27's L2 block). A reader that parses register prose
  is the fragile thing this repo keeps paying for. The SPEC has to name a machine-readable carrier for the ask field, or
  state that it reads prose and what breaks when the prose moves. I do not yet know which the lap-8 build plan expects.
- **"Generalize `_foldTarget`" spans two storage models.** Fernwood's fold writes a field in instance JSON
  (`plants.json` → re-inline). The weather intro's answer is a household preference — by W-8 that is **a per-estate KV row**
  in the Worker, not a canon file. One name over two substrates is where a rule goes quiet. Not verified: what the
  household record actually looks like today for a non-Fernwood estate, and whether any field exists that a preference
  could land in. That is an engineering-partner read I will need before the fold section is honest.
- **"The ribbon attributes it" assumes a ribbon every household has.** `MOM_ACK_DATA` is inlined instance content keyed
  to one person. I have not verified whether any per-household ribbon exists at the estate build. If it does not, the
  playbook's attribution leg is a design for a component that is not there, and the plan must say so rather than draw the
  arrow.
- **TIER 1 · 36 is the same rule as one the playbook needs.** *Stamp every ranking with the wording it was captured
  under* — every ask's answer must ride with its wording, or later answers are incomparable. The playbook should
  generalize 36, not mint a sibling.
- **Five seats plus synthesis is heavy for a design pass.** Security's and ai-advisor's questions are narrow (a roster
  ruling on what an answer may hold per tier; the draft-behind-gate threshold). I would convene user-researcher ·
  content-steward · ux-expert in full and put the two narrow questions to security-steward and ai-advisor as bounded
  asks, unless the grader says the brief meant five full trails.
- **The forward door.** Rows go to `tate-tracker-2a` by message. It is live now; the brief does not say where rows go if
  it closes before this plan is drafted. I assume: hold them in the plan's own § forward-rows and tell coordination.
- **Not fully read yet:** the eleven INTERESTS ids (I confirmed the array exists at `onboarding/index.html:1004`; my grep
  caught three of eleven, my range, not the file) · fernwood-12/17 beyond their heads · the SECURITY doc · the lap-8 build
  plan's rider wording. All on the §2 list; all before any drafting.

## 5 · What has NOT been tested or verified — stated so it does not read as coverage

- No walk has ever seen a card-intro ask. No real household has been asked anything beyond onboarding's ranking.
- No count of Mom's answered cards since lap 8 is in this readback; the >10 threshold's status is unknown to me.
- Whether a non-Fernwood household record has any slot for a preference: unverified.
- Whether a per-household acknowledgment ribbon exists: unverified.
- The INVENTORY's §4 THE ASK MODEL: does not exist yet.
- Any `file:line` I cite above is as of ef84c20 and three windows are writing.

## 6 · What I would do next, on clear

1. Read the §2 list in full (the items named in §4 last bullet first), re-check whether the INVENTORY landed, and read
   the lap-8 build plan's ledger rider so the SPEC matches what engineering-partner expects to build.
2. Convene the seats with one bounded question each, user-researcher first: *for a person who is not Mom, at a card's
   first appearance, what is the one thing worth asking that the address and the ranking cannot tell us — and what does
   answering it cost them?* Each seat writes its own trail; nothing model-authored reaches a person.
3. Draft `.plans/2026-09-11-ask-design-PLAN.md` with: the grammar (cite CLAUDE.md rule 1 and `elicitation-lens.CONTRACT`) ·
   when (cite LATCH ONTO WHAT SHE STARTS, graded `inferred` for other households) · cap and axis (cite `_ordering`) ·
   the fold across BOTH substrates, named · attribution with the ribbon's existence stated honestly · the draft-behind-gate
   threshold as it actually stands · the per-release reading mapped to beats 6 · 1 · 2 · 3 · the weather template ·
   the ledger SPEC (inputs by file, exit 3, falsifier) · forward rows · what v1 defers.
4. Message `tate-tracker-2a` the rows and `tate-tracker-ea` that the plan is drafted. Paul rules in his own time.

## 7 · Questions for the grader

1. "ONE ask" vs. Paul's "little questionnaire" — coordination's compression, or his?
2. Does the CLAUDE.md >10-answered threshold govern a card-intro ask, or only confirm cards?
3. Is there a per-household ribbon anywhere at the estate build, or is attribution a design for a missing component?
4. Where does the lap-8 build plan expect the ledger to read an item's ask field from?

## 8 · The grade — coordination (tate-tracker-ea), ~11:15 PM ET · CLEAN

Answers to §7, carried here so they outlive the message:

1. **"ONE ask" was coordination's compression**, not a ruling. Paul's *"little questionnaire"* is the INTENT; the
   elicitation lens is the CONSTRAINT. The shape (one ask, or a short set) is this pass's finding to make, with its
   falsifier. I recommend; Paul rules.
2. **The >10-answered threshold was written for the confirm cards.** Whether it governs a card-intro ask is ai-advisor's
   read in this pass. Recommend; Paul rules. **The human gate itself is not negotiable either way.**
3. **No per-household ribbon exists.** `MOM_ACK_DATA` is a literal in the template (`engine/viewer.template.html:12022`).
   The seam is **lap 8 row G (TIER 1 · 50, ruled tonight)**. Design the attribution leg AGAINST that seam and state the
   leg is unbuildable until G lands.
4. **The ledger's ask-field source:** today BACKLOG prose; the chain design's **P2** (the four ruled fields get a
   machine-readable carrier on the committed row) is the intended source and is NOT built. Spec the ledger to read the
   P2 carrier when it exists, fall back to row prose with a per-row UNREADABLE (never green by absence), and name P2 as
   its dependency.

Also from the grade: `elicitation-lens.CONTRACT` — cite, never restate. **The INVENTORY has landed since ef84c20** at
`a292af8` (`.plans/2026-09-11-legacy-toolchain-INVENTORY.md`); read its §4 THE ASK MODEL before drafting — `renderAskNext()`
exists and is unreachable; UV and AQI derive from the address, so the weather ask is about **interest, never value**.
Readback stays uncommitted unless told. Paul clears in this window; on clear, proceed per §6.
