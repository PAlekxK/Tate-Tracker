# product-steward — QUESTIONS IT COULD NOT CITE

- row: process — no BACKLOG row, same posture as every process document in `.plans/`
- objective: O5
- kind: queue
- class: engine · declared
- seats: product-steward (this file is its only write destination outside a BACKLOG row)
- depends-on: .plans/2026-09-07-product-steward-CHARTER.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ NOTHING HERE EXECUTES. A question is an OPEN question; it is not a finding, a
  recommendation, or a decision. ⛔ **This seat may not CLOSE a question** — that verb is not in its
  table. Paul closes, or a later citation does.
- stage-note: 2026-09-07 — **created to close process-audit G3.** Beat 8's exit condition is *"each
  finding reaches a row it can CITE, or opens a question where it cannot"*, and the charter's verb
  table promises *"one queue file of questions it could not cite"* (`:105`) — **without ever naming
  the file.** `measured`: no such file existed. The three `*-queue.md` files already in `.plans/`
  (`field-capture`, `grooming`, `independent`) belong to other threads and are not this.
  ⭐ **The failure mode that made this worth fixing before beat 8 runs**, not after: with no named
  destination the choice gets made per-finding, at speed, by whoever is writing — which is how the
  same class of item ends up in three places and the register stops being one register.
- stage-note: 2026-09-08 — **first real use.** Lap 5's CARRY (beat 4, renumbered from beat 8 by the
  CYCLE-MAP reorder — flagged below, not edited) opened **Q1–Q5** against **12 writes carried to
  existing rows**. ⭐ Writes exceed questions for the first time; the charter's second falsifier
  (§6.7, *questions-opened > writes*) does not fire on this round. ⚠️ **Read it with round 1's
  confound in mind and not against it**: round 1 drained a backlog no round had consolidated, this
  round read one lap's own three records and one battery, and **neither is a steady-state reading.**
  Full round: `.plans/2026-09-08-lap5-CARRY.md`.

---

## ⭐ THE TWO DESTINATIONS, NAMED — this is the whole point of the file

| beat 8 outcome | destination |
|---|---|
| the finding **can be cited** to an existing row | ⭐ **`BACKLOG.md`** — the row's own fields (stage · pointer · stage-note · seat citation), with a `[paul-ruled <date>] <file:line>` provenance line. **No new row is created** — `CREATE` is not in the seat's verb table |
| the finding **cannot be cited** | ⭐ **THIS FILE**, one entry, with what it could not find |

⛔ **There is no third destination**, and a finding that reaches neither has not been carried.

---

## Open questions

⚠️ **A NAMING DRIFT IN THIS FILE, FLAGGED AND NOT EDITED.** Everything below the header says
*"beat 8"*; `cycle/release/CYCLE-MAP.md:83` now numbers CARRY as **beat 4** of twelve. The file was
written 2026-09-07 against the pre-reorder map. ⛔ **Flagged rather than rewritten** — which of the two
is right is `check-release-docs.py`'s question and a judgement, and that tool's own rule is *flags,
never edits*. Read every *"beat 8"* below as **CARRY**.

### Q1 · The lap-5 disposition for `fb-vurlf77f` cites **TIER 1 · 11**; the row it actually folded into is **TIER 2 · 11**. Which is the record of where it went?
- raised-by: 2026-09-08 CARRY (beat 4) · from `feedback-dispositions.json`, key `home|est-e6696a|feedback|fb-vurlf77f-mtt49x18`, and reproduced in `.user-research/2026-09-08-lap5-READ.md`'s evidence log
- the finding: the disposition's `why` opens *"FOLDS INTO TIER 1 · 11 (the weather card from an address)"*. **TIER 1 · 11 is the sound-pipeline row** — *"the sound pipeline never verifies that a recording IS the species it is filed under"*. The weather card from an address is **TIER 2 · 11**, and the fold **did** land there: that row carries `fb-vurlf77f` by name, with its corrected mechanism.
- why it could not be cited: **the write is right and the reason string is wrong**, so there is nothing to carry — but `feedback-dispositions.json` is **not in this seat's write set** (charter §3: BACKLOG row fields, plan header keys, this queue file — *"nothing else, ever"*). ⭐ It is the charter's own defined failure: *"a miscitation, which is a defect with a location."* A reader following the disposition record lands on a row about bird audio.
- what would close it: **one edit to that record's `why`, by whoever owns the disposition file** — TIER 1 · 11 → TIER 2 · 11. ⚠️ Worth one thought first, because it is cheap and recurs: nothing checks that a disposition's named destination row exists or matches its parenthetical title, and this one was wrong in a way a human re-reading the sentence could not detect — the title was right, only the tier was wrong.

### Q2 · Record 1 was routed to *"a UX/design theme"* that does not exist. Does GROOM & BUCKET mint it, and what else moves into it?
- raised-by: 2026-09-08 CARRY (beat 4) · from `feedback-dispositions.json` `fb-gu2zv3t9-mtt494f1`, and `.user-research/2026-09-08-lap5-READ.md` §1 · 3rd
- the finding: Paul's ruling at DISPOSE is explicit — *"I would wanna build up a bucket or theme of just, like, UX and design work… so we continue to build a UX design library and do things cohesively"* — and the record was disposed `act` **to that theme**. `grep` across `BACKLOG.md` returns exactly one mention of it: the theme evidence row that names it as a destination. **The destination is the only thing that cites it.**
- why it could not be cited: **no row exists, and CARRY may not mint one** (charter §3: no CREATE verb). ⛔ And it should not be minted here even if it could: the disposition's own words site it *"at GROOM & BUCKET"*, which is beat 5.
- what would close it: **beat 5 buckets it, or Paul rules that it lives inside an existing row.** ⚠️ Two candidates already half-cover it and neither is it — **TIER 2 · 17** (colour axes) is one substrate of design consistency, and **TIER 2 · 21** (the masthead bar) is `ux-expert`'s but is one surface. The findings waiting on it from this lap alone: the `.told-row` divider-vs-accent-rail grammar · the first onboarding screen asking seven things before the product says what it is for (`mom`) · the browser-default blue radios in a Stone-and-green product (`wide-eyed`, already partly on 17).

### Q3 · `.plans/2026-09-08-setup-journey-PLAN.md` owns the build steps for four carried findings and is cited by no ranked row. Is TIER 2 · 18 its row, or does it need one?
- raised-by: 2026-09-08 CARRY (beat 4) · from the plan's own header — `row: BACKLOG.md § TIER 2 (row to add)`
- the finding: the plan's ten steps include **B2/B2i** (the returning-recognition routing — the `owner` seat's STOP), **B6** (show the email and phone, *unknown* rather than absent), **B7** (sign out), **B9** (the PO-box sentence moves to the moment of asking — `strict`'s standing finding (b), unrecorded on the board anywhere else) and **B10** (recovery). `measured`: no `BACKLOG.md` or `PRODUCT-ENGINE.md` line cites the file.
- why it could not be cited: **two rows both half-cover it and CARRY cannot tell which is right.** **TIER 2 · 18**'s falsifier *is* this plan's journey almost verbatim, which is why CARRY **linked** it there (a LINK is in the verb table); but 18 is explicitly *"named, deliberately not scoped"* on Paul's instruction, and a ten-step build plan with a `ready:` line is scope. **C6**'s sign-in block owns the mechanism half and is scoping-only.
- what would close it: **beat 5, or Paul's word.** ⛔ The link CARRY made asserts nothing about whether the plan should start — its `ready:` reads *agent-proposed 2026-09-08 — Paul rules*, and its own §3 says **NOTHING IN § Sequence STARTS**.

### Q4 · The READ beat pre-registered a measurement that expires when Mom or Bob first opens the product. Does lap 5 record it as a pre-registration, and where?
- raised-by: 2026-09-08 CARRY (beat 4) · from `.user-research/2026-09-08-lap5-READ.md` §2.2
- the finding: *"Paul is, at this moment, the only person who has ever arrived at this product as a household with nothing to measure with. When Mom or Bob arrives, this exact question — **does a household with no instruments feel served or feel broken?** — will be askable of someone who is not the builder, **once**, and only at first open."* The seat's grade: `inferred`, and *"it costs nothing to pre-register it now. It is unrecoverable after."*
- why it could not be cited: it is **not a backlog item** — nothing is built, nothing is asked, no surface changes. It is an **observation to make at a moment that has not arrived**, and the loop's pre-registration mechanism lives in `cycle/release/CYCLE-LOG.md` at beat 12 (lap close), which is **not in this seat's write set**.
- what would close it: **a `L5-P<n>` pre-registration written at lap 5's close**, or Paul's word that it is not worth one. ⚠️ It has a real expiry: **Mom's invite `p-b91e4d` is minted and, at the last recorded reading, unspent.**

### Q5 · The standing act *"ask Paul what Mom has asked him for lately"* is ruled, is owed, and has no owner at any beat. Whose is it?
- raised-by: 2026-09-08 CARRY (beat 4) · from `.user-research/2026-09-08-lap5-READ.md` §2.3, citing `CLAUDE.md` § *AN EMPTY ENGAGEMENT RECORD IS NOT AN ABSENT DEMAND* `[paul-affirmed 2026-09-07]`
- the finding: the rule is unambiguous — *"before any finding about her BEHAVIOUR becomes an organising claim, ask Paul what she has asked him for lately"* — and it is the move that **falsified two full research passes on 2026-09-07**. The READ seat named it as *"the one act I am asking for at this beat, costing one line, that outranks everything above"*, and recorded it in its own open-questions log as **unasked**.
- why it could not be cited: ⛔ **it is an ACT, not a row**, and no beat in `cycle/release/CYCLE-MAP.md` owns it. CLAUDE.md sites it at *session start* / pickup, but this loop's laps do not each open a session, and lap 5's beat 3 ran without it. **A rule with no owning beat is the exact shape CLAUDE.md's own most-repeated lesson is about** — *a capability the loop cannot reach by running its own procedure is not a capability the loop has.*
- what would close it: **Paul answering it** (which closes it for this lap only), **or** a ruling on which beat owns it standing — beat 1 (OPEN, beside the gate sweep) is the obvious candidate and CARRY does not get to pick.

### Q6 · 🔴 `--record` HAS BEEN BROKEN SINCE THE HOUR ROUND 1 WAS RECORDED, so this trial's falsifier ledger cannot be written to. Who repairs it?
- raised-by: 2026-09-08 CARRY (beat 4) · found by running the exact command the CHARTER prints at `§6`
- the finding: `python3 tools/product-steward.py --record …` exits with `NameError: name 'cmd_record' is not defined`. **`tools/product-steward.py:1135` calls it; nothing defines it.** `git log -S` locates the cause exactly: **`890efd5`** (*"the trial reports its STATE, not just its numbers"*, 2026-09-07 12:45) **deleted the six-argument `def cmd_record(...)` and updated the call site to pass a seventh argument (`--confounded`) without ever adding the replacement definition.** Round 1 was recorded at **12:02**; the writer died **43 minutes later**, so **no round has ever been recordable since the first one.**
- ⛔ **AND THE SELFTEST IS GREEN OVER IT.** `--selftest` passes **24 clauses, proven by mutation, and not one of them exercises `--record`** — so the tool that exists to keep a trial honest reports ✅ while the half that writes the trial's evidence is dead. ⭐ **This is the charter's own §6a shape from the inside:** *"a hand-typed count beside a tool that computes the same count"*, inverted — a tool that computes nothing while its documentation says it does.
- ⛔ **The stakes are R7's own, stated in the charter:** *"A trial that is not instrumented is renewed by inertia, which is the one outcome R7 exists to prevent."* At lap close the disposal rule is *"the ledger decides which"*, and the ledger holds **one round** — which reads identically to *only one round ever ran*.
- why it could not be cited: **it is a code defect in this seat's own instrument, and code is not in this seat's write set.** Charter §3 is exhaustive: *"BACKLOG row fields, plan header keys, and one queue file of questions it could not cite. **Nothing else, ever.**"* ⛔ **And hand-writing `.private/product-steward-ledger.json` was DECLINED for the same reason it would be tempting** — a hand-written row would make `--ledger` read as though the writer worked, which is the failure this entry exists to make visible. **Fail loud, not tidy.**
- what would close it: **restore `cmd_record` with its seventh parameter** (the deleted six-argument body is recoverable at `890efd5^`), **add a selftest clause that fails when `--record` cannot write** — otherwise the same silence returns — then record round 2 from `.plans/2026-09-08-lap5-CARRY.md` §4.1, whose numbers are **12 carried · 6 already · 5 questions · 0 unwritten** at `bfa3f23`, with the confound stated. ⚠️ **Until then `--ledger` under-reports the trial by one round and every reading of both falsifiers is drawn from a single data point.**

⚠️ **The inbox beat 8 will work from**, `measured` by `python3 tools/product-steward.py` at HEAD
`cfd41fb`: **20 ruling lines that nothing in the register carries**, plus **8 more UNCHECKABLE by
that predicate** (no quotable verbatim on the line — *absent*, not *clean*), **3 uncited seat trails**,
and **1 plan whose newest stage-note predates its own last commit**.

⛔ **Those 20 are NOT questions yet and must not be bulk-copied here.** The point of the beat is that
each is *looked at* and either cited to a row or written down as a question with its own reason. A
bulk paste would reproduce exactly the batch-clear failure this repo already records
`[[feedback_gated_is_ruling_or_hunt]]` — a list captioned *needs Paul* where a third of the rows
carried no judgement at all.

---

## Entry format

```
### Q<n> · <the question, in one line>
- raised-by: <beat 8 run date> · from <chronicle file:line, or the seat trail>
- the finding: <what was carried>
- why it could not be cited: <the specific row that should exist and does not, or the ambiguity>
- what would close it: <a citation, or Paul's word — say which>
```

⭐ **`why it could not be cited` is the load-bearing field.** *"No row exists"* and *"two rows both
half-cover it and I cannot tell which"* are different problems with different fixes, and a question
that does not distinguish them is a shrug with a heading.
