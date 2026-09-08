# LAP 3 · THE OPTIONS BOARD — everything that could advance, and what each would cost

- row: process — no BACKLOG row, same posture as every process document in `.plans/`
- objective: O5 (the loops are the artifact) · bears on O3
- kind: queue
- class: engine · declared
- seats: user-researcher → `.user-research/2026-09-07-beat7-what-matters-most.md` (beat 7, the READ)
         practice-steward → `2026-09-07-lap3-PROCESS-AUDIT.md` + `2026-09-07-review-gate-to-qa-DESIGN.md`
         product-steward → this layout (beat 9, BUCKET) · `2026-09-07-product-steward-CHARTER.md`
         engineering-partner → ⛔ **OWED, NOT WAIVED.** Rows B2, B3, C1 and D2 each need a build it
         has not costed. Their "what it costs" cells are `proposed`, by a session, not by that seat.
         ux-expert · content-steward · ai-advisor → waived: no surface, copy or model is decided here.
- depends-on: .plans/2026-09-07-lap3-BRIEFING.md
- depends-on: .user-research/2026-09-07-beat7-what-matters-most.md
- depends-on: .plans/2026-09-07-lap3-PROCESS-AUDIT.md
- depends-on: .plans/2026-09-07-review-gate-to-qa-DESIGN.md
- depends-on: .plans/2026-09-07-lap3-CONSOLIDATION.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔⛔ **NOTHING HERE IS RANKED AND NOTHING HERE EXECUTES.** Rows are grouped by **what they are
  blocked on** — a kind, not a value. Severity is **CARRIED** from the seat that claimed it, with a
  citation, and is never originated here `[paul-ruled 2026-09-07: product-steward may bucket, on two
  axes; it may not rank]`. **Paul picks.**
- stage-note: 2026-09-07 — beat 10's input, built at the commitment point and not before
  `[paul-stated: "the options list we should build more extensively once we are in lap three and have
  collected all the feedback and input and data that's out there"]`. Every prerequisite is now met:
  the three sweeps ran, beat 6 disposed all 8 gating records, beat 7 read them.

---

## 0 · HOW TO READ THIS

**Two axes, and only one of them is mine.**

| axis | who produced it | what it is |
|---|---|---|
| **bucket** (the sections below) | product-steward | **what a row is BLOCKED ON.** Kind-shaped, unordered, citable from the row itself |
| **severity** (the `claimed` column) | ⛔ **the LANE SEAT that claimed it** | carried verbatim with its citation. No row's severity was decided here |

⛔ **The buckets do not sort best-to-worst.** If they could, they would be a ranking with coarser
grain, which is out of bounds. *"Blocked on your word"* is not better or worse than *"blocked on a
build"* — it is a different **kind** of stuck, and it tells you which of them only you can unstick.

⭐ **`ships?` is the column the staged pipeline exists for.** A row that advances a rung and ships
NOTHING is a successful outcome this lap `[A-5]`, not a failed one. Zones is the named test case.

⚠️ **`v1 defers` is mandatory on anything marked v1-ready** `[the v1 rule, briefing §8]` — *"we'll
refine it later"* is only honest if the refinement has somewhere to live.

---

## 1 · ⛔ BLOCKED ON YOUR WORD — nothing moves until you rule

These are stuck on a decision. **No amount of building unsticks them.**

| # | what it is | claimed | ships? | cost | v1 defers |
|---|---|---|---|---|---|
| **A1** | **Move the review gate to QA** — adopt the design: rename `lab→dev`, `home→prod`, `prod→legacy` *(legacy already done)*, close mirror defects M1–M5, add `post-deploy` *(already built)* | practice-steward: *"the shape is right, and the deviation from standard practice is the CURRENT arrangement"* | ⛔ nothing to a user | the renames touch **9 files** and there is **no drift control** on the release map | keeps `ENV_NAME` as-is — that is a data migration, not a rename |
| **A2** | **Cloudflare Access on QA — keep or drop** | steward: *"a HOLD whose release condition was never written; the privacy seat recommended AGAINST it"* | nothing | a config change either way | — |
| **A3** | **May a synthetic walker touch your household?** The steward declined to rule it | steward: **declined — "that is his"** | nothing | — | — |
| ~~**A4**~~ | ⛔ **WITHDRAWN — the finding was wrong.** The Journal→Almanac rename is **Paul's own ruling, `BACKLOG.md:476`, 2026-07-30**, made knowingly against her answer as a CONSOLIDATION and dropped from tracking on his instruction 08-02. No synthetic seat overrode her. ⭐ **REPLACED BY E1 below**, which is his reframing and is a better question | — | — | — | — |
| **A5** | **`second-viewport`** — retired by declaring the coverage gap. ⭐ **Already ruled; listed only so it is not re-raised** | — | — | done | — |

---

## 1b · ⭐ THE ROW PAUL MINTED WHILE RULING — display name vs internal name

| # | what it is | claimed | ships? | cost | v1 defers |
|---|---|---|---|---|---|
| **E1** | ⭐ **Let a household name its own Almanac.** `paul-stated 2026-09-07`: *"there's a bigger question we've talked about in the backlog — whether everyone can customize the name of their Almanac, because everyone may have a different take on what makes sense or feels the most natural. So that would be a way of systematically replacing the name in the displays, but keeping that module still have an internal name that's consistent."* | `paul-stated` | ✅ **yes** — the noun on a surface every household reads | a DISPLAY-name field + one accessor; ⛔ engineering-partner owed | v1 = the Almanac only, one name, set in settings. **Defers** every other module's display name, and defers whether the name is per-place or per-account |

⭐⭐ **WHY THIS DISSOLVES THE CONFLICT RATHER THAN SPLITTING IT.** The 07-30 consolidation was right
*because scattered names confused her* — that argument is about the **internal** name, and it is
untouched. Her *"Journal"* answer was right *because it was her word for it* — that is about the
**display** name. They were only ever in tension while one string had to serve both. ⭐ **And it is
the multi-tenant form of the same insight**: with N households, "the most natural name" is not one
answer, so a fixed display string is wrong by construction no matter which word wins.

⚠️ **It also makes the 07-30 ruling checkable at last.** `BACKLOG.md:476` says the open question is
*"does Almanac land for her"* and that **if she wants Journal it goes back everywhere.** Under E1 that
stops being a rename and becomes a setting she can change herself — which is exactly *"have her do it
through the application"* `[ruling 3b]`.

---

## 2 · ⭐ BLOCKED ON NOTHING — buildable now, and each SHIPS NOTHING TO A USER

⭐ **This is the bucket ruling 3b just made load-bearing.** *"Let's do things without her where we
can."* Every row here can be done without Mom, without you, and without a deploy to her.

| # | what it is | claimed | ships? | cost | v1 defers |
|---|---|---|---|---|---|
| **B1** | **T1 · a `door` reader** — `GET /api/door` works and **no tool calls it**. It is the channel that shows *"someone opened the invite and stopped"* | ⭐⭐ **user-researcher, CRITICAL, in lane, with a falsifier**: her first open is *"irreversible AND invisible"* — and per **3b there is now no other instrument** | nothing | small — a reader over an existing route | v1 = arrivals per day per estate, flagging any with no matching account. Defers correlating a door arrival to a later account |
| **B2** | **T2 · `GET /api/onboarding-metrics`** — POST-only today, **no GET anywhere**, so every onboarding behaviour signal from both laps is unreadable by the loop | same as B1 — it is the other half of the same blindness | nothing user-facing (a Worker route) | small — mirror `/api/feedback`'s shape | v1 = a read-only range query. Defers any analysis on top of it |
| **B3** | **T3 · give a NULL author a reason** — `personSource: "grant"` exists; a null says nothing, so *"nobody was signed in"*, *"the grant would not resolve"* and *"this path predates attribution"* are one value | `paul-stated 2026-09-07`: *"we need to be sure that for everything we know who wrote it"* | nothing | one field at `PERSON_UNKNOWN` + call sites | ⛔ **defers BACKFILL** — records already written stay null forever; inventing a predicate for them is the misattribution this row prevents |
| **B4** | **M2 · add `"qa"` to `HOUSEHOLD`** — QA and production are built by **different branches of one script**, which is *why* a live production defect was invisible in its own mirror | practice-steward: *"the biggest mirror defect, and one nobody had named"* | ⛔ changes **what QA serves** | ~one line — but verify the `:236` index rewrite first | — |
| **B5** | **Beat 8 · carry the 20 uncarried ruling lines** — each to a row it can cite, or a question in the named queue | product-steward T1 trigger: **20 lines carried by nothing**, +8 UNCHECKABLE | nothing | one pass; the destination file now exists | — |
| **B6** | **C-2 · make the RETURNING journey walkable** — `journey-walk.py` branches on `fresh` at exactly ONE stop, so a returning walker lands past the whole script | ⭐ blocks **P2**, a pre-registration that otherwise discharges as `carried`, never answered | nothing | a real build — engineering-partner owed | — |

---

## 3 · ⛔ BLOCKED ON ANOTHER ITEM — order is forced, not chosen

| # | what it is | blocked by | claimed |
|---|---|---|---|
| **C1** | **The identity seam** (W1 · F4 · F6 · row 20) — *"an account's facts and its credential are two separate records, and exactly one code path reconciles them — the one with no door."* **15 census ids collapsed into this** | ⭐ **B6.** The steward's finding stands: *"until C-2 lands, no amount of design work on this seam can be certified by the loop"* — the harness cannot walk a returning person, and F4 **is** a returning person's defect | user-researcher: **W1, the critical want** · `validated` |
| **C2** | **Deploy the tombstone fix** (committed `9b96e07`, not deployed) | ⭐ **the new `cleared_sha` gate** — production now refuses anything but `1e2748d`. It ships when you clear a build | — |
| **C3** | **`4a3a61b` — two knowingly-shipped defects, on `main`, NEVER WALKED** | a round at that sha; the gate is per-sha so its evidence expires | — |

---

## 4 · THE DESIGN LANE — advances a rung, ships nothing, and that is the point

| # | what it is | rung now → target | ships? |
|---|---|---|---|
| **D1** | ⭐ **Zones** — `paul-ruled 2026-09-07`: **off the table for implementation**; concept/design only. A concurrent session has it at `design` with a journey artifact | concept → **design** *(reached)* → journey | ⛔ **nothing, by ruling.** The named test case for whether a lap can advance and deploy nothing |
| **D2** | **W2 · what fills a card** (D1–D5 · F10 · F11) — the place card is about the **property**, not the weather | concept | nothing yet |

---

## 5 · ⬜ NOT ON THE BOARD, AND WHY — the honest column

⛔ **A board that lists only what can move is a board that hides what cannot.**

| | why it is not a row |
|---|---|
| **GAP 1** (does a real person get through the door?) | ⛔ **its instrument no longer exists** `[3b]`. It is not blocked — it is **unanswerable by observation**. B1 and B2 are what replace it |
| **GAP 2** (is "add a place" founding or switching?) | ⚠️ **probably already spent.** It was only valid before she saw the UI, and the link is in her hands. Ask only if a natural moment arises; treat as gone |
| **GAP 3** (does she know where her writing went?) | opportunistic, per 3b — never scheduled |
| **Bob's two houses** | ⛔ `assumption` throughout — **nobody has asked him**, and he has no household |
| **Z-ACK** | ✅ closed. Paul discharges it as a person, any time |
| **J-d colour precedence** | ✅ **was never open** — ruled 09-06, `VOCABULARY.md §3g`. Re-raised in error this lap |

---

## 6 · ⚠️ WHAT THIS BOARD COULD GET WRONG

- **Severity is carried from ONE seat.** engineering-partner has not run this lap, so **no build-side
  criticality is represented at all** — and Paul's own J-b ruling says a critical build finding must
  be surfaced unprompted. **A whole lane is silent, and that is a gap in this board, not evidence
  there is nothing there.**
- **The costs in §2 are `proposed` by a session**, not costed by the seat that would build them.
- ⭐ **Repetition is deliberately NOT a column.** *"Asked 4×"* measures how long a row has been stuck,
  not how much anyone needs it `[user-researcher, beat 7]`. Sorting by it would rank by our own
  latency and call it customer signal.
- **n=1 and the builder.** Every `validated` here except Mom's folded answers is Paul's own word about
  a product he wrote. The one population that matters most has **n=0 on this product**.
