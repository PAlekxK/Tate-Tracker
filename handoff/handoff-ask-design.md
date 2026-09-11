# Handoff: fernwood — ASK DESIGN · the A-ASK design pass (its own window, not a lap slot)

<!-- generated 2026-09-11 ~1:55 AM ET · source: Tate-Tracker@7c7e4ae on LOCAL main · written by the coordination window (tate-tracker-ea)
     ⚠️ A first write of this file at 209bf4d committed EMPTY (a shell heredoc aborted on a backtick); this is the real brief.
     RECEIVER: verify the sha against HEAD. Cite symbols, stamp the sha. -->

## 1. Mission

Paul, 2026-09-11 ~1:45 AM ET, on *how we handle asking for their feedback — the right owner, how we document and explore
it, how we link it to the feature set and personalize as we go, per release*: **"I say go on both."** Both = (1) THIS
window — the A-ASK design pass — and (2) an ASK LEDGER reader as a lap-8 rider (the build side's; you SPECIFY it, §4·4).

You produce **the ask playbook**: how this product asks a person for input, when, in what grammar, under what cap, how an
answer folds into that household's own record (personalization), how the fold is attributed back (the ribbon), and how
the whole thing is read per release. **First application: the weather card's card-intro ask** (lap 9 · A, TIER 2 · 11 —
Paul: *"are you interested in UV, air quality? what do people want from a data point of view in their dash view"*).

**Owner seats** (coordination's recommendation; Paul: go): **user-researcher LEADS** (research mode — asking is a
discovery instrument) · content-steward (the words) · ux-expert (the surface and placement) · security-steward (roster:
what may be asked and stored, per tier) · ai-advisor (where a model may DRAFT an ask behind Paul's gate; capture stays
deterministic). **Judgment is Paul's**: every ask is approved before it reaches a person.

## 2. Read first

1. BACKLOG.md § A-ASK (his seed, ~line 2691; decision card .decisions/fernwood-11.md — "is the confirm queue the wrong
   instrument, or the right one asked wrong?") · § CONTENT · CARDS (opened tonight) · TIER 2 · 11 (weather card; its ask
   field carries the card-intro questionnaire, PROPOSED) · TIER 1 · 36/37 (the two instrumentation riders your ledger sits
   beside) · .decisions/fernwood-12.md and fernwood-17.md (sequenced after fernwood-11).
2. CLAUDE.md: § EVERY ITEM SHIPS WITH AN ASK (the four-field contract, paul-ruled 2026-09-07) · § Mama's Perspective (the
   whole confirm-card lifecycle: harvest → serve → answer → fold → ribbon; MAX_VISIBLE 5; information-value ordering;
   Paul's clear gate; the AI boundary and its eight forbidden creep modes) · § Four standing rules (ONE affirmative grammar;
   the ribbon is attribution not information; EVERYTHING IS CHANGEABLE and its decay) · § LATCH ONTO WHAT SHE STARTS (the
   0-for-35 measurement: every ask-shaped affordance at Fernwood went untapped; the door she opened herself was 100%) · the
   elicitation-lens.py line in the pickup block (NOT "ask more questions" — one field, many derived facts; a step that
   asks what it could derive is a FINDING).
3. tools/elicitation-lens.py · tools/harvest-questions.py · tools/rationalize-bench.py · tools/momlib.py (question_state,
   markers) · questions.json · feedback-log.json · onboarding/index.html INTERESTS (the eleven modules a person ranks —
   personalization input already captured).
4. .plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md (where lap 9 · A sits) · .plans/2026-09-11-legacy-toolchain-INVENTORY.md
   §4 THE ASK MODEL when it lands (engineering-partner, running) · .engineering/2026-09-10-recovery-route-SECURITY.md
   (how a contact value may and may not be stored — the same roster governs an ask's answer) ·
   .content/2026-09-11-recovery-copy-DRAFT.md (tonight's worked example of an ask + receipt confirmed by Paul).
5. cycle/release/CYCLE-LOG.md lap 7: "Ahead — CONTENT BUILD-OUT, and the card-intro ASK" (his words) and the release
   loop's beats where asks already have slots (beat 6 commit · beat 1 sweeps · beat 2 dispose · beat 3 READ).

## 3. State at 7c7e4ae

Lap 7 is building (rows D, C closed; B in progress) — you touch none of its files. Laps 8/9/10 scope is pre-committed by
ruling (chronicle). The four-field contract has a carrier (the committed row) but the ask's SURFACE is unruled
(fernwood-11), the ask→fold→attribute loop exists only for Fernwood's plant confirm cards, and **nothing reads across
every ask the product has made** — the gap your §4·4 specifies.

## 4. The work (ordered)

1. **Readback first** (§8·0). Then convene the seats — each writes its own trail under its own directory
   (.user-research/ · .content/ · .ux-reviews/ · .engineering/ for security's verbatim · ai-advisor's return);
   you synthesize.
2. **The playbook** → .plans/2026-09-11-ask-design-PLAN.md (stage: design, ready: agent-proposed — Paul rules):
   the ask grammar (ONE affirmative) · WHEN to ask (card intro · after a signal the person gave · never a standing ask;
   prefer instrumenting a door they already open) · the ordering axis and the cap · the elicitation rule as a check ·
   the fold: an answer lands in a personalization field on the household's own record (generalize _foldTarget), the
   card reads it, the ribbon attributes it · the decay of "changeable" scaffolding · what a model may draft and where the
   human gate sits · the per-release reading (which beat reads what).
3. **The weather card's intro ask** → the plan's first worked template: the ONE ask (not a questionnaire of six), what
   it derives (which sub-components render; which is highlighted), what the address already derives and must not be
   asked, its _foldTarget on the household record, its ribbon line, its telemetry event AND reader. Content-steward
   drafts the words; nothing ships from this window.
4. **The ASK LEDGER reader — SPEC ONLY** (the build is a lap-8 rider, engineering-partner's plan): tools/ask-ledger.py —
   derived, never typed: every ask the product has made (from the rows' ask fields + questions.json + card intros), per
   ask: served · answered (COUNTS, never people) · folded into what · which feature row it links to · the elicitation
   reading. Exit 3 UNREADABLE, never green by absence. Name its inputs by file and its falsifier.
5. Forward rows to the backlog window (tate-tracker-2a, the one door) by message; tell coordination (tate-tracker-ea)
   when the plan is drafted. Paul rules it in his own time.

## 5. Guardrails

No surface edit. No file under lap 7's freeze (TIER 1 · 45 · 42 · 26–32 · 43 · 44 · 23 · TIER 2 · 10 · 13 · 18–21 · 25).
Never BACKLOG.md, CLAUDE.md, VOCABULARY.md. `git commit --only <your paths>` — three other windows are live. The AI
boundary: no seat reads Mom's words beyond what is already routed to the project; nothing model-authored reaches a person.
An ask is a THIRD category — authored content — human-confirmed before it reaches anyone.

## 6. Open for Paul

fernwood-11 (which surface serves the ask) — your plan recommends, he rules. The weather intro's words. Whether a
model may draft asks at all (ai-advisor's read; his gate).

## 7. Not verified

Whether the inventory has landed when you start (check the file). Any file:line older than an hour.

## 8. First tasks

0. Verify the stamp; write handoff/handoff-ask-design.readback.md; tell Paul; wait for the grade.
1. On clear: read the items in §2, convene the seats, draft.
