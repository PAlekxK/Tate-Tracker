# Handoff: backlog-registrar

<!-- generated 2026-09-10 ~5:45 PM ET · source: Tate-Tracker@889ae75 (verify vs HEAD before trusting status) · supersedes the 27d4f1a brief; the first window (tate-tracker-4c) closed clean -->

## 1. Mission — unchanged

**You are the BACKLOG REGISTRAR — a standing lane, created by Paul 2026-09-10.** His words:

> *"A backlog rationalization and maintenance session, since there are so many work items… a **standing
> expert** that's helping keep track of everything and that they can all **forward their updates to**
> and questions and so on, and help identify **how we can package work together**."*
> — and: *"let's just put that in our backlog so we don't have too many things roaming around."*

⭐ **You are `BACKLOG.md`'s SOLE WRITER, as a SCRIBE — not an author.** Lanes forward rows to you; you
transcribe them **verbatim, attributed to the lane and its sha**, and you read the placement back to the
lane. You flag and propose in your own clearly-marked voice, separately. ⛔ **You never author a status,
never re-tier, never delete, never split a section.**

**Why the boundary matters, measured on day one:** the coordinator relayed a count ("four rows") that
came from the registrar's own earlier report and had hardened into a fact by being relayed; the registrar
grepped before writing and found it was the wrong predicate (§4). A relayed claim is a hypothesis. **The
seat worked on day one because it enforced its boundary against the coordinator** — three refusals, all
right: transcribe from the lane's own artifact not the coordinator's summary; author no discharge you did
not measure; leave your own proposal flagged as an orphan rather than clear it with a false claim.

## 2. You are a WINDOW, and the door is now a door

Session name in this run: `tate-tracker-4c`. Lanes addressed it directly and **four forwards arrived in
one working session** (b8 · b3 · claude-meta · ec), so the falsifier in §8 was answered. ⛔ **The
walk-harness lane is a SUBAGENT of the coordinator (`tate-tracker-af`) and cannot be addressed**; its
forwards come through the coordinator, labelled as relayed. `paulkirschenbauer-3b` is the security-seat
window under `~/.claude`, not a Fernwood lane (it forwarded one Paul ruling anyway, correctly).

## 3. Read first

- `.plans/2026-09-10-backlog-registrar-PROPOSAL.md` — **your charter** (its header's `stage-note:` lines are the log)
- `.plans/2026-09-10-link-syntax-and-proposal-intent-RECOMMENDATIONS.md` — **the ③/④ packet, with Paul** (§5 below)
- `.plans/2026-09-10-backlog-management-AUDIT.md` (`0fe685a`) — practice-steward's structural read; **reached the same remedies independently**. ⛔ Do not reconcile it with the packet; where they differ is Paul's information
- `.plans/2026-09-10-PLAN-OF-RECORD.md` · `.plans/2026-09-10-G1-RULING-PACKET.md` · `BACKLOG.md` (~4,360 lines) · `VOCABULARY.md`

## 4. What landed this session (all committed on `main`, none pushed)

| sha | what |
|---|---|
| `ea63a0e` | TIER 2 · 25 (onboarding-ask-b3 @ 54813e0 — `viewer.html:18481` sentence-case regex, 1 of 5 labels) · Paul's ruling that **the AI boundary is a property of the system, not a promise about a person** (claude-meta, `~/.claude` @ 49a1fb7) under § BUILD vs INTEGRATE › ③ A SECURITY SEAT, with two measured registrar flags |
| `d3f14dd` | TIER 1 · 19 (tate-tracker-ec @ 6414435 + 4f7c04f — the founding path's two missing writes; nigel/aida destroyed, `c1ae9bb` reversed, `est-76012d`/`est-92e588` RETIRED NEVER REUSED) |
| `9271c4c` | `tools/registrar-sweep.py` — three defects fixed (§6) |
| `15b4f9a` | the ③/④ packet |
| `e5626b7` | ⭐ **Paul's ③ ruling at `BACKLOG.md:14`** (*"I'm good with the recommendation there"*) + the two false pointers flipped to `→ PLAN ·` · TIER 1 · 21, 22 (tate-tracker-ec @ d6c2f37 — fold-answer rebuilds the digest only behind `--deploy`; retraction has no path — **findings, not status**, tier is Paul's to confirm) · TIER 2 · 26, 27 (walk-harness lane via the coordinator, no sha given, `b1c5391` — within-estate cross-person isolation is unobservable; a lab-parity denominator) · § ③ A SECURITY SEAT — Paul: *"integrating him into the process"* |
| `889ae75` | `tools/check-backlog-ready.py` — two link keywords, **bidirectional pointer-vs-header check**, stale-"not stamped" flag; ④ recorded as RULED AND UNBUILT in `UNGRADED_BY_DESIGN` |

**Ruled numbers, measured live at `889ae75`:** 0 false readiness claims (2 before the flips) · 0 promote-the-link · **2** stale *"not stamped"* rows (A6 guru-retrieval, C7 condo) — exactly the two the packet named · 31 orphans (④ unbuilt).

Already in the file before this window and **read back, not duplicated**: b8's row-9 buildings falsifier
(`06874b7`) and b3's Houseplants correction (`2488394`, TIER 2 · 16). ⭐ *Two of everything* is the file's
recorded failure; reading back is the discipline.

## 5. Parked — where each stopped

1. ✅ **③ is RULED AND LANDED** (`e5626b7` + `889ae75`) — Paul approved the recommendation *including* the
   bidirectional check. ⭐ **④ is RULED AND PARKED, deliberately.** Paul ruled *intent, three `row:` states*
   (`none` · `proposed` · `<pointer>`), and the coordinator authorised the registrar to build it or park it
   (*"a half-normalised register is worse than an un-normalised one"*). It is ~45 lines in
   `check-backlog-ready.py` (parse `row:` into three states · orphan = a declared pointer that is absent, or a
   BACKLOG pointer to a `row: none` file · `proposed` prints under one AWAITING header · `row: none` files are
   graded as documents, which needs `proposal` added to `KINDS`) **plus a scripted header pass over 21
   proposals (7 headerless → `row: none` + `kind:`; 14 → `row: proposed — …`) as a diff for Paul**, at
   close-out, touching files the registrar did not author. That is the sprawl case. **Where it stopped:**
   the ruling is recorded in `UNGRADED_BY_DESIGN["-PROPOSAL"]` and packet §2 carries the per-file
   classification and the cost table. The next registrar session builds it FIRST; its falsifiers are in
   packet §2f (14 AWAITING / 0 proposal-orphans after landing, or §2a is wrong).
   ⚠️ **One selftest in `check-backlog-ready.py` was already failing at HEAD before the ③ change**
   (*"two in flight with no exception is flagged"* — it predates the ruling that `concept` is uncapped).
   Not touched; it is a test-vs-ruling judgement, not the registrar's.
2. **Five rows with stale prose beside a TRUE stamp** (`:139` onboarding · `:248` zones · `:252` weather ·
   `:1468` guru · `:3324` C7 — *"Not stamped."* is the pre-stamp sentence never deleted). Owed to their
   lanes or Paul; the registrar rewrites no prose it did not transcribe.
3. **`b5a4247` is UNPLACED and is NOT tate-tracker-ec's** (that lane's commits are `6414435` · `4f7c04f` ·
   `d6c2f37` · `4ab6a85`). It is *"the shelf reads the record's own answer"* — the `homes/` shelf, so almost
   certainly the **onboarding-ask lane**; ⚠️ that is inference from the subject, not knowledge. Its trailer
   names `worker.js whoami — hasEstate …`, which is not a row. ec's read, offered as inference only: it
   belongs in TIER 1 · 19's founding path (the empty-shelf state). **Ask onboarding-ask-b3, then place.**
   Adjacent hypothesis from ec, **unverified and not a row:** the `handover` walk's 🔴 *USERNAME renders
   empty* may be `/api/profile`-writes-ACCOUNT vs `whoami`-reads-GRANT — written up with its probe in
   `handoff/handoff-fernwood-credential-path.md` §3.2 (`4ab6a85`).
4. **Six untrailered lane commits since the convention began** (`0fe685a` · `b1c5391` · `a01e66f` ·
   `54813e0` · `83b9fa8` · `9b5be1d`). Not yours to author rows for; the coordinator is carrying the format.
5. **G1 ⑧ (the registrar seat itself)** — your own charter is `row: proposed`, an orphan by today's
   checker, and stays so on principle.
6. **The two Paul-only closures stand:** `BACKLOG.md` is written by the mom + fleet loops too (one door
   or it isn't a door — the audit §3·B challenges the *evidence* for a sole writer, not the ruling), and
   `-PROPOSAL` document-vs-item (now ④ of the packet).

## 6. ⭐ THE EVIDENCE THE SEAT IS WORTH HAVING — the sweep found five defects in itself, all on its author

`tools/registrar-sweep.py` (`5d29b67`, fixed `9271c4c`). Selftest **12 → 17, every defect pinned by a
mutation that fails on the old code**:

| found | defect | class |
|---|---|---|
| first live run | `none` after an em-dash read UNPLACED | instrument measuring its users' precision |
| first live run | autosave commits and pre-convention commits listed as unregistered (2,250 under `--all`) | a control red on day one |
| within an hour, live | `③ A SECURITY SEAT` read UNPLACED because the heading is `### ③ ⭐ A SECURITY SEAT` | same class as `none` |
| within an hour, by reading | `TIER 2 · 99` read **PLACED** on the strength of "TIER 2" alone — a false green, the inverse of the tool's one rule | a matcher that drops short fragments |
| within an hour, live | two forwards from two lanes both printed as the first lane's (`via[0]`) | attribution to the wrong lane, worse than none |

⭐ *"An instrument that only works when its users are precise measures its users, not the world."* Run
`python3 tools/registrar-sweep.py --selftest` and `--since <sha>` at pickup; a `⚠️ N forwarded-by lines
for M claims — pairing not knowable` line is the tool refusing to guess, not a bug.

## 7. ⛔ BLIND SPOTS — what a fresh session does not know

1. **The trailer trap:** `Backlog-Register:` and `Backlog-Forwarded-By:` must sit in the **same final
   paragraph as `Co-Authored-By:`, no blank line** — git parses trailers only from the last paragraph.
   Sweep with `%(trailers:key=…)`, never `--grep`. `Register:` was rejected (double-booked by `eac5648`).
2. **A trailer only sees COMMITTED work.** Uncommitted lane work is structurally invisible to the sweep,
   and the two most valuable register facts of 09-10 (Paul's rulings given in conversation) had no
   Tate-Tracker sha at all. Conversational rulings arrive by message and are transcribed with the lane's
   own repo + sha (`~/.claude @ 49a1fb7` was one).
3. **The sweep proves a forward was PLACED, never that the placement is TRUE.** Only a reader can say that.
4. **The scribe boundary is the whole value.** A status attributable to *the lane that measured it* is
   strictly stronger than one attributable to whichever session last had the file open. The moment the
   registrar authors a status, that property is gone and the seat is just another writer.
5. **Where the packet and the audit differ, unsmoothed** (packet §5): its *"12 pointers, only 3 clean"*
   vs the packet's 5 consistent / 5 stale-prose / 2 false — the split is whether stale prose beside a
   true stamp counts as unclean; the remedy differs (delete a sentence vs flip a token). Its §3·B
   challenges the sole-writer evidence. Paul sees both; nobody reconciles them for him.
6. **The tree is shared with the coordinator**, which commits on `main` under you (HEAD moved a dozen
   times in one session). `git status BACKLOG.md` immediately before every write; stage only your file.
7. `cycle/release/cycle-state.json` and `worker/digest.json` are always modified in the tree — generated
   and another lane's. **Never commit either.**

## 8. Guardrails — unchanged

⛔ Never `git push origin main` · never deploy · nothing outbound · never write another lane's files
(`worker/worker.js`, `viewer.html`, `onboarding/index.html`, `homes/index.html`, `tools/journey-*.py`,
`tools/publish-digest.py`, `zones.json`, `.plans/` files you did not author). Cross-lane through
`tate-tracker-af`. **Grep, then read the line** — a count locates, it does not establish.

## 9. Your own falsifier — answered once, re-armed

*"If no lane has forwarded you anything in a working session, the door is not a door and you should say
so rather than sweeping an empty inbox."* Four lanes forwarded in the first session. If the next one is
empty, say so.
