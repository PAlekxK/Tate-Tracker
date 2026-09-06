# THE USER FEEDBACK CYCLE — one engine, N instances; the mom-cycle becomes its first · PROPOSAL

- row: process (no BACKLOG row yet — same posture as the 09-05 cascade, registry and state-of-the-work proposals)
- objective: O5
- class: engine · must-not-diverge (a second definition of "we heard a user" is the defect this exists to prevent)
- seats: practice-steward (this file)
        engineering-partner → deferred: §4's note tuple and §5's per-estate token resolution have code consequences; nothing is designed here
        content-steward → **owed, not waived**: §6's return leg is authored words to a person who is not family, and no content seat has read them
        ux-expert → deferred: the bubble's siting is `.plans/2026-09-06-state-and-next-steps-AUDIT.md` R1/R3, not this file
        ai-advisor → waived: capture stays deterministic and AI-free by standing rule; §7 names the one place a model could sit and declines it
        user-researcher → deferred: §6's evidence is measured behaviour, not a study
- depends-on: .plans/2026-09-06-state-and-next-steps-AUDIT.md
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- ready: agent-proposed 2026-09-06 — **Paul rules**
- stage: concept

> **Method only.** This proposes a loop shape. It ranks no feature, writes no copy, and decides no
> cadence Paul has not already set. §8 is what I decline.

---

## 0 · THE RULING ASKED FOR — new cycle, or the mom-cycle generalised?

**Neither, and the third answer is already ratified in this repo for code.**

> **The mom-cycle is not a loop that needs generalising. It is the FERNWOOD INSTANCE of a loop whose
> ENGINE has never been extracted. Extract the engine. `MOM-CYCLE-MAP.md` becomes its first
> instance, unchanged. A second estate gets a second INSTANCE, never a second cycle.**

**Why not a new cycle.** `feedback_cyclical_vs_finite_projects` and `MOM-CYCLE-MAP.md`'s own rule —
*"The loop rests. HER INPUT is what fires it"* — mean loops fire one at a time and rest between.
A fifteenth loop duplicating eight legs is the exact shape this repo has paid for repeatedly, and
`VOCABULARY.md` already carries seven live word-forks. A parallel "user feedback cycle" beside a
"mom feedback cycle" would fork *feedback* itself, which is the one word the whole thing is named
for.

**Why not generalise the mom-cycle in place.** Its calibration is **measured against one person over
eight laps** and is not portable: `offers-passed ≥3` · `sessions-quiet ≥3` · `answer-age ≥21d` ·
her conditions ratified at **414×848 at A+**. `feedback_mom_is_a_test_subject_not_the_end_user` says
those are evidence about **the job**, not constants about **users**. Rewriting them to be generic
destroys eight laps of calibration and replaces it with numbers nobody measured. ⛔ **The
instance-leaking-into-engine failure runs both ways, and generalising in place is the reverse
direction of it.**

**Why the engine/instance seam is the right one — and it is reuse, not invention.** This repo already
splits **code** exactly this way: `ENGINE-MANIFEST.md` classes every tracked file `engine` /
`config` / `instance` with a divergence tier, and `check-engine-manifest.py` enforces it. The loop is
the only major artifact in the project that has **not** been put through that seam. Applying Paul's
own ratified split to his own loop is the cheapest possible move: no new vocabulary, no new state
word, one existing checker's shape reused.

⭐ **The test that settles it:** when Bob's estate produces its first note, does anything about *how
we read a note* have to change? **No** — the trigger, the disposition rule, the ack, the retro are
all identical. What changes is **whose** record, **whose** thresholds, and **who** writes back. That
is precisely the engine/instance line, drawn where it already is in the code.

---

## 1 · WHAT THE ENGINE IS — the parts that are already estate-agnostic

Read off `MOM-CYCLE-MAP.md` and the tools, not designed here.

| engine element | today's implementation | estate-specific? |
|---|---|---|
| **an ARRIVAL fires a lap; the loop rests otherwise** | `mom-cycle-status.py: position()` | ⛔ no — pure |
| **BEHAVIOUR can also fire it** (`offers-passed` · `sessions-quiet` · `answer-age`) | `mom-cycle-status.py`, amended 2026-08-17 | the **signals** are engine; the **thresholds** are instance |
| **a fired-by-behaviour lap publishes its own stated reason** — *"she saw the ask and passed over it"* reads differently from *"read what she sent"* | same | ⛔ no — pure, and load-bearing |
| **disposition is per-ARRIVAL, so a batch cannot be cleared by one member** | `check-arrival-dispositions.py` | ⛔ no — **this is the anti-unread-queue mechanism** |
| **an empty answer record is not a quiet user** | `read-mom-engagement.py` against `/api/metrics` | ⛔ no |
| **a deviceId is a browser bucket, not a person** | `momlib._drop_harness()`, `people.json` | ⛔ no |
| **an event first firing inside the window publishes `"?"`, never `0`** | same | ⛔ no |
| **the two-pass UX sweep is a TRIGGER, not a beat** | `check-ux-sweep.py` | ⛔ no |
| **retro amends before reset; "none — metric unmoved" is a valid outcome** | `MOM-CYCLE-LOG.md` | ⛔ no |
| **verify it live, after the push, at the user's real conditions** | `check-live.py` | the **conditions** are instance |

| instance element | today | why it cannot be engine |
|---|---|---|
| the person, their device, their conditions | Mom · `d-…` · 414×848 A+ | measured per person |
| the thresholds | 3 / 3 / 21d | eight laps of calibration on **one** person |
| the estate's Worker + token | `momlib.WORKER_URL` = the **legacy** Worker | §5 |
| **the return leg** | Paul writes to his mother | §6 — **the one part with no engine form yet** |
| the ack ribbon's copy | Mom's register | content's |

**Nine of the ten engine rows already run as estate-agnostic code.** The extraction is mostly
**declaring** a split that exists, not building one.

---

## 2 · THE SHAPE — one loop object, N resting instances, one board

```
FEEDBACK-CYCLE  (engine)               ← the map, the legs, the trigger rule, the checks
   ├── instance: fernwood   (Mom)      ← = today's MOM-CYCLE-MAP.md, renamed, thresholds intact
   ├── instance: <second estate>       ← its own thresholds, its own return leg, its own log
   └── instance: <…>
                  ↓
        ONE awareness surface — operating-layer render.py, exactly as it already renders 14 loops
```

⭐ **The critical property, and it is the answer to "what stops it degrading into an unread queue":
there is no queue. There are N loops, each resting, each fired by its own estate's arrival.** The
mom-cycle never had a queue — it had a trigger — and that is *why* it has never gone unread. A
cross-estate inbox would create the queue on day one.

⚠️ **This design has a stated ceiling and I will not pretend otherwise.** N resting loops each need
Paul at their gate. Fourteen loops already rest against one person's attention. **Pre-register the
ceiling rather than discovering it:** if two instances are ever `FIRED` simultaneously and both wait
more than one lap-length for Paul, the one-at-a-time property has broken and a real queue — with an
owner and an ordering rule — has to be designed. **That ordering rule is a priority mechanism and
therefore Paul's, which is another reason not to build it before it is needed.**

---

## 3 · SPINE CONFORMANCE (`~/.claude/rituals/CYCLE-SPINE.md`, S1–S6)

| | how this carries it | new work? |
|---|---|---|
| **S1** state schema — `state`, `generated_at`, `generated_by`, `last_lap` as a dict | one state artifact **per instance**; the engine defines the schema once | ⚠️ the engine must forbid a *merged* state artifact — a single file for N instances cannot answer "did **this** estate's lap close?" |
| **S2** ≥1 blocking human gate, machine-visible | unchanged: the return leg is Paul's gate, per instance | none |
| **S3** ≥1 deterministic check seen to fail, sited | `check-arrival-dispositions.py` is the sited one, and its siting sentence already exists | ⚠️ it must key on **(estate, arrival)**, not arrival alone — §5 |
| **S4** machine-checkable closing condition | per-instance chronicle + per-instance state; `cycle-docs-check.py` already reads both | ⚠️ it must not treat "instance B did not lap" as "the loop is stale" |
| **S6** the map PARSES — `\| N · NAME`, 👤 on the gated row | the engine map carries the beats; instance files carry no beat table | none |

⛔ **S3's siting clause is COVERAGE, counted, never graded** — and the exemplar the spine cites is
`MOM-CYCLE-MAP.md:451`. **The loop being generalised is the spine's own worked example of S3.** That
is the strongest single argument for extracting rather than replacing it.

---

## 4 · WHAT MAKES A NOTE ACTIONABLE — the tuple, with `090a42a` as the precedent

`090a42a`'s own commit message states the principle: *"'this is confusing' is worth little; 'this is
confusing, on the address screen' is a punch-list row."* Generalised, **five fields, four of which
already exist**:

| field | today | source of truth |
|---|---|---|
| **WHO** — `personId` | ⚠️ present since `c111417`/`56c5b0d`; **`null` on every onboarding answer before that** | the **grant**, presented as `X-Grant`. Never the client's assertion |
| **WHERE** — `estateId` | ✅ the Worker stamps it | ⛔ **the KV binding, never the payload** — `worker.js`: *"No estate field is READ — one sent is ignored"* |
| **WHICH SURFACE** — screen / route | ✅ `postAnswer("note-" + currentScreen, …)`, `index.html:1184` | the page |
| **WHEN** | ✅ `receivedAt`, stamped server-side | the Worker |
| **WHICH BUILD** — the sha | 🔴 **absent** | ⭐ the page already knows: `qa-build.json` is served beside it (`pages-deploy.py:79`) |

⭐ **The build sha is the one cheap addition and it closes a defect the audit found independently.**
Without it, a note and the code it was written against are joined by a timestamp and a guess — which
is exactly how `PUNCH-LIST §F` ended up carrying *"the plan's stage-note still reads GATE 1 WALKED @
`408ff94`; 14 commits have since touched the journey set."* **A note stamped with its build is a note
that can be retired when the build changes; a note without one is re-litigated forever.**

⚠️ **The prior defect is the warning, not the pattern.** `personId: null` on every onboarding answer
had **two independent causes** and fixing either alone attributed nothing — the page sent no
`X-Grant`, *and* the Worker routed the POST above the grant gate. **Attribution is a two-sided
property and a one-sided check reads green.** Any conformance check on this tuple must assert from a
**stored record**, never from the code path.

⛔ **Capture stays deterministic and AI-free.** The bubble already honours it; nothing here adds a
model to the capture path.

---

## 5 · THE READ SIDE — the blocker, stated plainly

From the audit §4 step 3(b), verified two ways (by tool name and by route):

> **No tool in this repo both knows about the `home` estate and reads `/api/feedback`.** The two sets
> are disjoint. `momlib.py:42` pins the **legacy** Worker; `.private/` holds `fernwood-token` and
> `fernwood-token-qa` and **no `fernwood-token-home`**.

**Every one of the fourteen `read-*` lines in `CLAUDE.md`'s session-start block reads the frozen
estate.** So the engine's first required change is not a new beat — it is that **the readers take an
estate**, resolving Worker URL and token from an estate register rather than from a module constant.

⛔ **And that is the whole reason this proposal exists now rather than when a second household
arrives.** A feedback loop whose readers are hardcoded to one estate is a loop that **silently reads
the wrong estate** when a second appears. It does not error. It returns Mom's notes. **X and not-X
produce the same observation** — the corpus's own dominant failure shape, sitting on the read side of
the very mechanism being generalised.

**Minimum change, named not designed:** one estate register (`estateId → {worker, tokenFile,
pagesOrigin}`), `momlib` resolving from it, every `read-*` taking `--estate` and **failing closed with
no default**. ⛔ **A default estate is how the wrong-estate read becomes silent again.**

---

## 6 · THE RETURN LEG WHEN THE USER IS NOT MOM — ⛔ UNSOLVED, and I will not invent it

This is the part the coordinator asked for and it is the part I have to decline to design, because
the evidence says the obvious answer is already measured as **not working**.

**What exists.** The mom-cycle's return leg is *Paul tells Mom what happened*, carried by the
**acknowledgment ribbon** (`check-mom-ack.py`), with the rule `[paul-stated 2026-08-04]` — *HANDLED,
THEN RETIRED, in that order.*

**What is measured, lap 8** (`CLAUDE.md`, "LATCH ONTO WHAT SHE STARTS"):

| affordance | offered → taken |
|---|---|
| jump strip (**moves** her) | 5 → **5** |
| Mama's Perspective queue (**asks** her) | 10 → 4 viewed → **0** |
| **acknowledgment ribbon** (**asks** her) | 10 → **0** |
| front-door launcher (asks her) | 10 → 4 viewed → **0** |
| look-for prompt (asks her) | 5 → **0** |

> ⭐ **The existing return leg has a measured take-rate of zero on the one person who has a
> relationship with the author.** Generalising it to a person with no relationship would be
> generalising a mechanism that does not work, to a harder case.

**What I can say structurally, and it is three things:**

1. **The return leg must become an ARTIFACT, not a message.** With Mom it can be an iMessage; with
   Bob it cannot, and a loop whose closing beat depends on a personal channel has no engine form.
   **The engine's closing beat is "the change is visible in the product where the note was made"** —
   which is the only return that requires no relationship. That claim is grounded in the same lap-8
   measurement: **the affordance that MOVES her was taken 5 of 5.**
2. **It must not ask for acknowledgment.** Every asking affordance measured zero. A return leg that
   requires a tap to count as delivered will read as undelivered forever — a permanently-red control.
3. ⛔ **Whether a non-family user gets a *personal* reply at all is Paul's, and it is not a copy
   question.** He tied it to the operating model himself — **P26**, `GATE2-paul-findings.md`: *"that
   goes straight to Paul"* should not survive to production maturity, *"closer to 'we'll take that
   into consideration'"*, explicitly *"the update cycle as part of the operating model."* **That
   sentence is the return leg's contract with the reader, and it is currently a promise made by
   `onboarding/index.html:1459` and `:722` that only Paul can keep.**

**So the honest state: the engine has a closing beat with no working implementation, and it is
flagged rather than filled.** `content-steward` is **owed, not waived** here.

---

## 7 · THE THREE CHANNELS — and the one that has no store

The coordinator's (b) — *"a note about onboarding, a note about the estate view, and a note about the
invite email are one person's experience of one product."*

| channel | where a note lands today | in the loop? |
|---|---|---|
| onboarding page (`.fblink`, `090a42a`) | `POST /api/feedback` → **that env's estate** (`est-e6696a` on production) | 🔴 **written, never read** (§5) |
| estate view (`.feedback-ribbon`) | `POST /api/feedback` → **legacy estate** (`est-3c9f1a`) | ✅ read by every `read-*` tool |
| **the invite message** (`onboarding/invite-message.md`) | ⛔ **nowhere.** Paul sends it by hand; a reply arrives in his personal inbox | 🔴 **no store, no channel, no watcher** |

⭐ **The invite is the first surface a new user meets and it is the only one with no capture at
all.** For Mom that is invisible — she replies to her son. For a second household it is the moment
with the highest chance of a question and the lowest chance of it reaching the record.

⛔ **I am not proposing a channel for it.** It is outbound, personal, and Paul's — and
`feedback_leading_indicator_not_safety_net` applies: he covers that inbox today. **What I am
recording is that the loop's coverage has a hole at its own front door**, so the hole is a known one
rather than a discovered one.

**The one place a model could sit** — clustering N notes across M estates into themes — **is declined
for now.** At today's n it would be a model summarising a handful of sentences a person can read, and
the read side does not exist yet (§5). Revisit when a single lap routinely carries more notes than
Paul reads in one sitting; that is a measurable trigger, not a hunch.

---

## 8 · WHAT IS PAUL'S

| # | ruling | why |
|---|---|---|
| **F1** | ⭐ **Is the split engine/instance, or is this a new cycle?** §0 is my ruling with reasoning; it is a governance call and his to accept or reject | everything below depends on it |
| **F2** | **What a non-family user is told happens to a note** (P26). The contract, not the wording | operating-model; he named it as such |
| **F3** | **Whether the return leg may be product-visible-change only**, with no personal reply | trades his time against a reader's expectation |
| **F4** | **Do the mom-cycle's thresholds travel to a second instance as defaults, or does each instance start uncalibrated?** | uncalibrated is honest and slow; travelling is fast and unmeasured. Both defensible |
| **F5** | **When the estate register is built** — before a second estate exists, or when one does | `feedback_build_doors_on_measured_demand` says on measured demand; §5 says the failure is silent. **Genuinely two-sided; not mine** |

**What an agent can drive once F1 lands:** declare the engine/instance split in `ENGINE-MANIFEST.md`
using the existing tier vocabulary · add the build sha to the note tuple · give every `read-*` an
`--estate` that fails closed · key `check-arrival-dispositions.py` on `(estate, arrival)`.

## 9 · FALSIFIERS

1. **§0's ruling is wrong** if a second estate's first lap requires changing *how a note is read* —
   not who reads it, not whose thresholds, but the rule itself. Then the loops are genuinely
   different and two cycles is correct.
2. **§2's "no queue" claim is wrong** the first time two instances sit `FIRED` simultaneously for
   more than one lap-length. Pre-registered.
3. **§6's "return leg must not ask" is wrong** if any asking affordance in this product ever reaches
   a non-zero take-rate. Watch the counter; do not argue it.
4. **§7's decline of a clustering model is wrong** once one lap carries more notes than Paul reads in
   one sitting. That is countable.
5. **§5's disjoint-sets claim** was verified by two greps (tool name, route literal). If a reader
   resolves its estate through a path neither grep sees, it is wrong — check `momlib` consumers
   before relying on it.

## 10 · WHAT THIS PROPOSAL DID NOT DO

- **Did not rename anything.** `MOM-CYCLE-MAP.md` / `MOM-CYCLE-LOG.md` stay put until F1.
- **Did not write a second cycle map, a skill, or a `/feedback-cycle` command.** Nothing is built.
- **Did not touch the mom-cycle's thresholds** or any of its checks.
- **Did not design the estate register**, only its refusal behaviour.
- **Did not research any second household**, and did not open `~/Developer/tate-commons`. §0's
  demand evidence is `VOCABULARY.md:147`, already in this repo, `paul-stated 2026-09-05`.
