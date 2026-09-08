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

- stage-note: 2026-09-08 — **second real use, same day.** Lap 5's BOARD (beat 5, GROOM & BUCKET) opened
  **Q7–Q13** against **zero** BACKLOG writes — that beat's own exit condition forbids touching the file
  (*"it FLAGS; it never reorders"*), so the §6.7 ratio is **structurally meaningless** at this beat and
  is recorded as a charter finding rather than a result. Full round:
  `.plans/2026-09-08-lap5-BOARD.md`. ⭐ **Q1 CLOSED** (`b998b30` corrected the disposition's `why` to
  TIER 2 · 11 — the *class* is carried instead into the BOARD's B8). ⭐ **Q2 CLOSED** — the UX/design
  theme is minted as **B1 · UX & DESIGN COHERENCE**, with its members, its library
  (`~/.claude/design-principles/`), its supply (`/ux-sweep`, OWED) and its own falsifier. ⭐ **Q5
  ANSWERED for this lap** at beat 3 — Paul: *"Mom hasn't asked for anything lately. She's been very
  busy"*; ⛔ the standing half (which beat OWNS the act) is still open. **Q3 · Q4 · Q6 remain open.**

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

- ✅ **RULED `[paul-approved 2026-09-08]` — it belongs at OPEN (beat 1).** On the precedent set this lap:
  the `/ux-sweep` staleness check *"is checked every lap and RUNS when due at OPEN"* — same shape, a
  standing obligation with a staleness property. ⛔ **A question asked, NEVER a gate.** B10 rules that
  *"Mom has not asked for anything lately"* is **a reason, not silence**, and a beat that demands an
  answer will manufacture one. Spec: §6.

### Q6 · 🔴 `--record` HAS BEEN BROKEN SINCE THE HOUR ROUND 1 WAS RECORDED, so this trial's falsifier ledger cannot be written to. Who repairs it?
- raised-by: 2026-09-08 CARRY (beat 4) · found by running the exact command the CHARTER prints at `§6`
- the finding: `python3 tools/product-steward.py --record …` exits with `NameError: name 'cmd_record' is not defined`. **`tools/product-steward.py:1135` calls it; nothing defines it.** `git log -S` locates the cause exactly: **`890efd5`** (*"the trial reports its STATE, not just its numbers"*, 2026-09-07 12:45) **deleted the six-argument `def cmd_record(...)` and updated the call site to pass a seventh argument (`--confounded`) without ever adding the replacement definition.** Round 1 was recorded at **12:02**; the writer died **43 minutes later**, so **no round has ever been recordable since the first one.**
- ⛔ **AND THE SELFTEST IS GREEN OVER IT.** `--selftest` passes **24 clauses, proven by mutation, and not one of them exercises `--record`** — so the tool that exists to keep a trial honest reports ✅ while the half that writes the trial's evidence is dead. ⭐ **This is the charter's own §6a shape from the inside:** *"a hand-typed count beside a tool that computes the same count"*, inverted — a tool that computes nothing while its documentation says it does.
- ⛔ **The stakes are R7's own, stated in the charter:** *"A trial that is not instrumented is renewed by inertia, which is the one outcome R7 exists to prevent."* At lap close the disposal rule is *"the ledger decides which"*, and the ledger holds **one round** — which reads identically to *only one round ever ran*.
- why it could not be cited: **it is a code defect in this seat's own instrument, and code is not in this seat's write set.** Charter §3 is exhaustive: *"BACKLOG row fields, plan header keys, and one queue file of questions it could not cite. **Nothing else, ever.**"* ⛔ **And hand-writing `.private/product-steward-ledger.json` was DECLINED for the same reason it would be tempting** — a hand-written row would make `--ledger` read as though the writer worked, which is the failure this entry exists to make visible. **Fail loud, not tidy.**
- what would close it: **restore `cmd_record` with its seventh parameter** (the deleted six-argument body is recoverable at `890efd5^`), **add a selftest clause that fails when `--record` cannot write** — otherwise the same silence returns — then record round 2 from `.plans/2026-09-08-lap5-CARRY.md` §4.1, whose numbers are **12 carried · 6 already · 5 questions · 0 unwritten** at `bfa3f23`, with the confound stated. ⚠️ **Until then `--ledger` under-reports the trial by one round and every reading of both falsifiers is drawn from a single data point.**

### Q7 · Nine live ordinal collisions in `BACKLOG.md`. Mandate the qualified form, or mint stable slug ids?
- raised-by: 2026-09-08 BOARD (beat 5) · `.plans/2026-09-08-lap5-BOARD.md` §1.3, measured by parsing the three tier tables at `71119d6`
- the finding: `measured` — TIER 1 ∩ TIER 2 collide on **11, 14, 15, 16, 18, 19, 20**; TIER 1 ∩ TIER 3 on **6**; TIER 2 ∩ TIER 3 on **7**. **Nine live.** One has already produced a wrong citation in a tracked file — `feedback-dispositions.json`'s `why` for `fb-vurlf77f` read *"TIER 1 · 11 (the weather card from an address)"*, a right title on a wrong tier, so a reader landed on a row about bird audio (Q1, fixed `b998b30`).
- why it could not be cited: ⛔ **renumbering is not available.** `measured`: eleven `TIER n · m` or bare `row N` citations live outside `BACKLOG.md`, **six of them inside `worker/worker.js`**, plus `viewer.html`, `engine/viewer.template.html`, `CLAUDE.md`, `tools/grant-mint.py:213` and `tools/guard-concurrent.py:69`. A renumber would silently falsify comments in a running Worker. So the choice is **C1** (mandate `TIER n · m` everywhere; cheap, does not fix the class) against **stable slug ids** (`T2-11-weather-from-address`; fixes it permanently, is a schema change and a rewrite of every external citation). **A seat that picked would be choosing the file's identity scheme.**
- what would close it: **Paul's word** on C1 vs slugs, and on whether the proposed `tools/check-row-citations.py` (BOARD §1.3 · C3) is worth its own maintenance.

- ✅ **RULED `[paul-ruled 2026-09-08]` — DO NOT RENUMBER; mandate the qualified form.** Paul's words:
  *"Two seven is fine. We can ratify — if everyone says don't renumber it, let's not renumber it."*
  ⭐ **Both windows reached this independently, with different parsers**, and the BOARD measured the cost
  (eleven external citations, six in `worker/worker.js`). **Write `TIER 2 · 11`, never *"row 11"*.**
  ⛔ **Slug ids are NOT adopted** — not rejected on merit, simply not needed once the qualified form is
  mandated. Whether `tools/check-row-citations.py` earns its maintenance is still open and is the only
  part of Q7 not closed.

### Q8 · Where does the archive go — a bottom `# 🗄 ARCHIVE` region, or a companion `BACKLOG-ARCHIVE.md`?
- raised-by: 2026-09-08 BOARD (beat 5) · §1.4
- the finding: **178 lines across four sections read finished with no live rider** (`measured`, each grepped for `🔴 🟠 🟡 ⏸ OWED / NOT FIXED / still open`): `✅ M1` (77) · `✅ Z-ACK` (34) · `✅ L1` (48) · `✅ SHIPPED 2026-07-29 — the Tier-1 correctness pass` (19). A fifth, `✅ SHIPPED 2026-07-29 (evening)` (55), is `inferred` clean. ⚠️ **Archiving closes ZERO head-gap** — every candidate sits below TIER 1. It is for the reader, not the metric.
- why it could not be cited: **the precedent cuts both ways inside this same file.** `PICKUP-LOG-ARCHIVE.md` is the companion-file precedent; `## KILLED / SUPERSEDED` at `BACKLOG.md:3735` is the bottom-region precedent. Two right answers is not something a seat resolves.
- what would close it: **Paul's word.** ⛔ Whichever he picks, **three of eight ✅/SHIPPED-headed sections carry live work** — `A1` holds the live R1/R2 monitoring definitions, `FLEET LAP 1 · BEAT 6` holds `⏸ Emissions hardware STAYS OPEN` and two `fleet_probe.py` defects *FILED, NOT FIXED*, and `The shape system` holds `🔬 NEXT LAP` and `🟡 PARTLY FIXED`. **They must not be swept in**, and splitting their riders out is a judgment edit, not a move.

- ✅ **RULED `[paul-ruled 2026-09-08]` — a bottom `# 🗄 ARCHIVE` region in `BACKLOG.md`.** Paul's words:
  *"Let's just put it at the bottom so there's not two separate documents to maintain."* ⛔ The reason is
  the ruling's own scope test: **a companion file is a second document with a second staleness rule**, and
  this corpus's most-repeated failure is two registers each reading current.
  ⚠️ **Unchanged by this ruling: FOUR of eight ✅/SHIPPED-headed sections carry live work** and must not
  move — `A1` (live R1/R2 spec), `FLEET LAP 1 · BEAT 6`, the shape system, and **Z-ACK** (regraded
  2026-09-08, `.plans/2026-09-08-lap5-REFINEMENT.md` §10.3). **Archiving closes ZERO head-gap** — it is
  for the reader, never the metric.

### Q9 · 26 plans and 1 seat trail that no ranked row cites — is a plan REQUIRED to have a row?
- raised-by: 2026-09-08 BOARD (beat 5) · §2 · B8, from `check-backlog-ready.py` and `product-steward --triggers` T2
- the finding: `measured` today — **26 `.plans/` documents flagged `no BACKLOG.md row points at this plan (orphan)`**, inside 141 readiness flags across 38 plans; plus **1 uncited seat trail**, `.user-research/2026-09-08-localized-feed-and-property-type.md`. ⭐ **This is Q3 generalized** — Q3 asks it of `2026-09-08-setup-journey-PLAN.md`; the census says it is a property of the corpus.
- why it could not be cited: ⛔ **the predicate may be wrong, and that changes the answer entirely.** A `-PROPOSAL` that was considered and set down *should* have no row. If "orphan" means *considered and closed*, 26 is healthy and the check over-reports; if it means *unreachable work*, it is the largest single reachability gap on the board. **Nothing in the record distinguishes the two today**, and inventing the distinction would be a seat deciding what a plan is.
- what would close it: **a ruling on what an orphan means** — or a `closed:` header key that lets a plan say it is finished, which makes the count read honestly under either reading.

- ✅ **RECOMMENDATION APPROVED `[paul-approved 2026-09-08]`** — *"I'm good with all your recommendations."*
  ⛔ **This does NOT answer Q9's own question** (*is a plan REQUIRED to have a row?*). It **resizes** it:
  the predicate is one-directional and points the wrong way, so **26 decomposes into 10 `row: process`
  (correct by convention) · 9 with no header · 7 genuinely one-sided** `measured`. Read the link
  bidirectionally, count `row: process` as linked, report the three groups separately. **Then the real
  ruling is a ~3-case question and still Paul's.** Spec: `.plans/2026-09-08-meatier-rulings-RECOMMENDATIONS.md` §2.

### Q10 · `release-state.py` reports `beat 9/12 (Paul walks it)` while lap 5 is running beat 5. Which number is the lap's position?
- raised-by: 2026-09-08 BOARD (beat 5) · §2 · B8
- the finding: `measured` today — `python3 tools/release-state.py` prints *"FIRED · beat 9/12 (Paul walks it) · owner: paul · candidate bfa3f23 · seats pass: True"* while the lap is executing **GROOM & BUCKET (5)** and has not reached COMMIT. `python3 tools/check-release-docs.py` is **✅ green**: the map and the code agree on the beat *list*, so this is not the drift that check is built to see.
- why it could not be cited: `inferred`, and **which of the two readings is the defect is a judgement.** The derived beat may be reading **evidence state** — a gate that passed on an earlier build — where a reader takes it for **lap position**; or the lap's own reckoning may be what is wrong. `check-release-docs`'s own rule is *flags, never edits*, and its note records that this call *"has gone both ways."*
- what would close it: **Paul's word**, or a ruling that `release-state` publishes the two readings separately. ⚠️ It matters because **`beat.owner: paul` is how this loop announces that a human gate is open**, and it is currently announcing one at the wrong gate.

- 🔬 **DIRECTED, not ruled `[paul-directed 2026-09-08]`:** *"You tell me — do some analysis, bring in the
  process steward, and let's fix this so it doesn't happen again."* ⛔ **So the deliverable is not the
  number.** The number is a symptom; the ask is the mechanism that let a derived beat report a position no
  lap was at, and a change that stops it recurring. **practice-steward is to be dispatched.** Open.

### Q11 · Does the pointer-head region get a declared LINE BUDGET — and what happens to § FOCUS FREEZE?
- raised-by: 2026-09-08 BOARD (beat 5) · §1.2, §1.6
- the finding: `measured` across lap 5's own commits — the head-gap went **510 → 554 → 604 → 648 → 672** as beats 1–4 filed into the head region: **+162 lines in one day, every beat of the lap widening the thing beat 5 exists to close.** The proposed move set buys **219 lines of headroom**, i.e. **~1.4 laps at this lap's own rate**, after which beat 5 re-runs the identical move forever. ⭐ Separately, **§ FOCUS FREEZE** — the one head section the proposal keeps — has the same defect one altitude down: **five successive amendments (09-03 → 09-04)**, each partly superseding the last, so its operative state is derivable only by reading all five in order.
- why it could not be cited: a **line budget is a process rule** (and possibly a new clause in `check-backlog-drift`), and **rewriting the freeze block is a judgment edit** — the 09-02 rationalization is explicit that splitting is not a move. Both are outside a seat's verbs.
- what would close it: **a ruling on a head budget** and whether the drift check should measure it; and separately, **whether § FOCUS FREEZE is rewritten to state its current position once.**

- ✅ **RULED `[paul-approved 2026-09-08]`** — the **routing rule is the primary fix** (a new THEME files into
  `# 🗂 THEMES` from the start; a standing CONTRACT into the lens region), and the line budget is a
  **second, ADVISORY line that never exits non-zero** — `check-backlog-drift.py` already owns the 400
  trigger and two controls on one number would disagree. ✅ **`## 🧊 FOCUS FREEZE` STAYS in the head and the
  declared reading order now NAMES it** — applied to `BACKLOG.md:36` this session. Spec: §3.

### Q12 · K12 and TIER 2 · 22 disagree about `transcript.personId`. Which is right?
- raised-by: 2026-09-08 BOARD (beat 5) · §1.5, on the 09-07 kill list's one unapplied entry
- the finding: `.plans/2026-09-07-backlog-grooming-SCAN.md` §4d killed it — *"a finding that was correctly recorded and then filed as a row. It has no v1, no falsifier and nothing to build… that belongs in the walk harness's own documentation, next to the field."* **CARRY then wrote the same finding into TIER 2 · 22** at F13, as a member of *the gate's own camera*, on the strength of **two seats tripping on it and one nearly filing a false alarm**.
- why it could not be cited: ⛔ **both readings are defensible and they imply opposite acts** — write a comment, or treat undocumented harness fields as a defect class that costs seat-hours and manufactures false findings. **Neither is stale**: K12 is one day old, F13 is hours old. A seat choosing between two live judgements would be overturning one of them.
- what would close it: **Paul's word**, or a citation showing the two are about different scopes (the field's own documentation vs. the class of undocumented harness fields) — in which case **both stand** and only the row's wording needs to say so.

- ❓ **MORE INFORMATION REQUESTED `[paul-2026-09-08]`:** *"I don't know what this is. I need more
  information."* ⛔ **Do not read this as a deferral** — the question as posed was unanswerable because it
  assumed context Paul does not hold. **Owed: a restatement that says what `transcript.personId` IS, what
  the two registers each claim, and what breaks under each answer.** Open, and the debt is the asker's.

### ⚠️ Q13 · Which of B6, B7, B8 does Paul's *"process related items"* mean?
- raised-by: 2026-09-08 BOARD (beat 5) · §2 · B8, from `[paul-ruled 2026-09-08]` at lap 5's open
- the finding: the steer is *"if there were backlog and process related items in the backlog, let's consolidate those and implement them first, so we don't wind up back in a situation where we don't enact the fix… because the project can't see the inbox."* The BOARD makes them findable as three distinct kind-shaped buckets: **B8** the loop's record of itself · **B7** the release instrument · **B6** instrumentation of the product. **All three answer to the name.**
- why it could not be cited: ⛔ **answering it IS the ranking.** *"Implement them first"* is a COMMIT-beat act and naming which bucket goes first is precisely the verb this seat does not have — `cycle/release/CYCLE-MAP.md:85`: *"he picks. This is a human gate and no instrument is ever built for it."*
- what would close it: **Paul, at COMMIT.** ⭐ The board's obligation was to make the three findable and distinct so the question costs one sentence instead of a re-read; that half is done.

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
- ✅ **RULED `[paul-ruled 2026-09-08]` — ALL THREE.** *"I think all three of these are important and worth
  prioritizing."* ⭐ **This closes Q13 as posed.** The question was *which bucket did "process related"
  mean*, and the answer is that the phrase was never exclusive: **B6 (instrumentation of the product),
  B7 (the release instrument) and B8 (the loop's own record) are all in scope.**
- ⚠️ **What it does NOT settle, stated plainly so nobody reads it as settled:** *"all three"* is a **SCOPE**
  ruling, not a **SEQUENCE**. The three buckets hold ~30 members between them and the WIP band is
  `build 1/1`. **Nothing here says which member is picked next, and no instrument is proposed for it.**
- ⭐ **The discriminator Paul has ALREADY ratified, and it is a property rather than a preference:** the
  cheaper-now-than-later criterion `[paul-stated 2026-09-08]` — *does the remediation cost GROW with time,
  and is any part of the delay window UNRECOVERABLE?* ⛔ **It cuts ACROSS all three buckets** rather than
  ordering them, so it narrows the next pick without ranking anything. Applied to the now-in-scope set:
  `.plans/2026-09-08-lap5-REFINEMENT.md` §13.

### Q<n> · <the question, in one line>
- raised-by: <beat 8 run date> · from <chronicle file:line, or the seat trail>
- the finding: <what was carried>
- why it could not be cited: <the specific row that should exist and does not, or the ambiguity>
- what would close it: <a citation, or Paul's word — say which>
```

⭐ **`why it could not be cited` is the load-bearing field.** *"No row exists"* and *"two rows both
half-cover it and I cannot tell which"* are different problems with different fixes, and a question
that does not distinguish them is a shrug with a heading.
