---
type: research
project: fernwood / release loop lap 3
research_id: beat7-what-matters-most
last_updated: 2026-09-07
beat: 7 (READ) — first time this beat has ever had an input
seat: user-researcher
evidence_level: mixed — per-claim tags throughout
question: "Across every channel, what matters most to the customer — and who is the customer?"
sources:
  - "feedback-dispositions.json — the four `fold` records, the only records ever routed to this seat"
  - ".plans/2026-09-07-lap3-RESEARCH-BRIEF.md §4 (the 47-row census, A1…J7) and §1–§3"
  - ".private/synthetic-walks/GATE2-paul-findings.md (P10–P32, F1–F15; ⛔ gitignored — cited by id, paraphrased, not reproduced)"
  - ".plans/2026-09-07-lap3-CONSOLIDATION.md (four channels; T1/T2/T3)"
  - ".plans/2026-09-07-lap3-BRIEFING.md §2 (GAP 1 / GAP 2), §7 (rulings J-a, J-b, J-f, J-e, Z-ACK), §8 (the v1 rule)"
  - ".plans/2026-09-07-lap3-paul-feedback-CAPTURE-2.md (F7–F15, verbatim, tracked)"
  - ".user-research/persona-mom.md · .user-research/2026-09-07-what-carries-what-she-redoes.md"
  - "~/.claude/user-research/fernwood.md (audience patterns)"
gate: ⛔ NOTHING HERE EXECUTES AND NOTHING IS RANKED ACROSS LANES. Criticality is stated once,
  inside the customer lane only, with evidence and a falsifier. Paul ranks. `[paul-ruled 2026-09-07, J-b]`
excludes:
  - "⛔ ZONES — off the table for implementation this lap; a separate concurrent session owns concept/design. No zone row is scoped here."
  - "⛔ Z-ACK — CLOSED. Paul discharges it in person. No acknowledgment surface is designed, proposed or implied here."
privacy: >
  Mom's verbatim words are referenced, never reproduced (the 2026-07-26 quarantine clause; this repo
  has a public surface). The P-series findings live in gitignored `.private/` and are cited by id and
  paraphrased in substance rather than re-quoted into a tracked file. F-series quotes are reproduced
  only where they already exist verbatim in tracked `.plans/` files.
---

# Beat 7 · What matters most to the customer

---

## 0 · THE ANSWER, IN ONE PARAGRAPH

**What the customer wants most from this product is to be recognized by it.** Not "recognized" as a
feeling — as a screen state. Paul named it himself on 2026-09-05 (P30): land on a page that is *his*,
empty but **recognisable as his place**. It has two faces, and they are the same failure:

| face | the failure | whose | consequence |
|---|---|---|---|
| **the product does not know WHO you are** | correct server data suppressed under a name that belongs to no account | Mom's face | one shot, unrecoverable, **and invisible to every instrument we have** |
| **the product does not know WHAT you gave it** | address, property type and twelve interests in; *"we're working out your weather"* out | Paul's face | chronic, recoverable, he comes back tomorrow |

⭐ **Inside my lane, the one thing I am calling critical is the first face, for Mom: on her first
open, the only things on the screen that can be hers are her name and her place's name — and that is
exactly the surface that was measured broken today.** Section 3 states it with evidence and a
falsifier. Everything else in this file is consolidation and gaps.

---

## 1 · WHO THE CUSTOMER IS — three populations, not one, and they must not be averaged

| | who | n on the NEW product | what the evidence actually is | strongest tag available |
|---|---|---|---|---|
| **P1** | **Paul — the founding household.** Grant Park Condo, urban, no land, no zones, `est-e6696a` | **1**, and he wrote the code | 10 feedback records (4 substantive) + 15 walk findings + 23 findings from the 09-05 walk | `validated` — a real person, his words, timestamped, in the store |
| **P2** | **Mom — the make-or-break user** | ⛔ **0.** Invite `p-b91e4d` minted 2026-09-07 ~12:05 ET, **unspent** | everything known is from `est-3c9f1a`, **a different product**, frozen | `validated` about the OLD product; ⛔ **nothing** about this one |
| **P3** | **Bob's two houses — the second estate** | ⛔ **0. They do not exist.** | Paul relayed on 08-31 that Bob redirected to his own two houses | `inferred` that the case exists; ⛔ `assumption` on anything Bob wants from a screen — **nobody has asked him** |

### 1.1 The three splits that matter, stated so nothing gets averaged

1. ⭐ **Paul is n=1 AND the builder.** Every `validated` claim about the new product is a claim about
   one user who also wrote the thing. `validated` (stated at every claim in the census §0). This does
   not weaken his findings — one Paul finding outranks any number of agreeing fixtures, by the
   register's own rule — but it means **his wants are not a user base**, and where a want is only his,
   this file says so.
2. ⭐ **Paul-as-customer and Paul-as-builder are two people in one record.** Of his 15 lap-2 findings,
   **five are rulings and directions, not customer wants** — F1 (zones are a priority), F2 (resolve
   strip vs menu), F3 (a staged pipeline), F6 (his synthesis of the seam), F15 (the next question to
   open). Those belong to the process lane, not to me. Ten are customer wants. `validated` (his own
   framing in the register: *"a direction, not a finding"*).
3. ⭐ **Mom is a test subject, not the end user** `[memory: feedback_mom_is_a_test_subject_not_the_end_user]`,
   **and simultaneously the adoption gate** `[~/.claude/user-research/fernwood.md]`. Both are true and
   they pull opposite ways. The resolution this file uses: her *behaviour* is instance evidence and
   does not set engine defaults; her *arrival* is the one measurement the whole project is waiting on.

### 1.2 What each population is the customer FOR

⚠️ This is the table not to collapse. A want with one populated column is a want with one voice.

| want (see §2) | P1 Paul | P2 Mom | P3 Bob |
|---|---|---|---|
| **W1** recognize me | `validated` — measured live, three records disagreed | ⭐ **the consequence case** — `inferred`, unobserved, unrecoverable | — |
| **W2** pay me back for what I gave | ⭐ `validated` — 3 of 4 fold records + F10/F11/F15 + P27/P31/P32 | `inferred` **and stronger than it looks** — see §2.2 | — |
| **W3** show me who else is here | ⭐ `validated` ×2 today, 4× across days | she is the **object** of the ask, not the asker | ⛔ `assumption` — never asked |
| **W4** tell me what matters today | `paul-stated` (a ruling) | ⛔ **`contested`** — do not argue it from her | — |
| **W5** truth about my writing | `validated` — F8, F9, and a measured capture lie | `inferred`, **highest stakes** — the loop's whole premise | — |
| **W6** see and change what I told you | `validated` — F7, F13, P19 | ⭐ `validated` — and the build currently contradicts her | — |
| **W7** the numbers must be checkable | `validated` — he found the class at close | ⭐ `validated` **precedent** — the rainfall event | — |

---

## 2 · CONSOLIDATION — 7 wants, and what collapsed into each

⛔ **W1…W7 is an INDEX, not an order.** No ranking is implied by the numbering. My single criticality
statement is separate, is in §3, and is about one thing.

### 2.0 ⭐ THE FINDING THAT CAME OUT OF DOING THE CONSOLIDATION

**The four `fold` records — the only records Paul has ever routed to this seat — contain ZERO about
W1.** Three land in W2, one lands in W3. That is not an accident of sampling:

> ⭐ **The typed channel is structurally incapable of carrying the identity want.** A note box lives
> *inside* the product. Only a person who is already through the door can write in it. **The failure
> of not getting through the door can never arrive on channel B**, by construction.

`validated` — the mechanism is measured (`.plans/…-CONSOLIDATION.md` §0: four channels; B is *"he
types into the app"*). `inferred` — the consequence for reading the record.

⚠️ **The operative consequence:** a board built from the feedback store will systematically
under-represent the wants of people who cannot get in — which is exactly the population Mom is about
to join. **The store is a good instrument for the wants of people who are already inside it, and a
blind one for everyone else.** This is the general form of the gap `door` telemetry was supposed to
cover, and `door` has a read route and no reader (`CONSOLIDATION` §3, T1).

---

### W1 · "Let me in, and show me this place is mine."

**Collapses 15 ids into one want:**
census **A1 · A2 · A3 · A4 · A5 · A6 · C6** · jobs **J1 · J2 · J3** · lap-2 walk **F4 · F5 · F6 ·
F12** · 09-05 walk **P29 · P30** · backlog **row 20** + `.plans/2026-09-07-sign-in-door-PROPOSAL.md`.

- `validated` (measured live 09-07 on `1e2748d`, with Paul) — three independent records must agree
  before a person sees their own place, and all three disagreed. whoami returned name + address +
  ranked interests while the screen read **"Empty so far."** and **"Signed in as PaulKirsch"**, a
  username belonging to no account.
- `validated` — **all three failures render the identical dead screen.** Nothing visible distinguishes
  *you are not signed in* from *your data is here and we are hiding it*.
- `validated` — F12: logout asked **twice in one evening**. It is not a separate feature want; it is
  the same missing door read from the other side.
- `validated` (09-05, P29) — the last time a person walked the handoff cold, he named an Atlanta place
  and landed on Fernwood. **Recognition failure has already happened to a real person on this product.**
- ⛔ **Zero feedback records.** See §2.0.
- ⛔ **Zero synthetic coverage, and this is measured, not assumed:** 39 of 39 lap-2 walks ran
  `--fresh`; the only returning battery ever run took 12–15 failed actions per seat and all four
  reports went unread. **No seat has ever arrived at this product as a person who already exists.**

**Anti-finding worth carrying:** Paul walked release lap 1 (`c821051`) and reported zero findings.
⚠️ That walk happened immediately after **three out-of-band repairs** cleared his path. It is one datum
about one build and is **not** evidence the seam works. `validated` (the register says so on its face).

---

### W2 · "I gave you my address. Give me something back."

**Collapses 17 ids into one want:**
census **D1 · D2 · D3 · D4 · G2** · jobs **J6 · J7** · lap-2 walk **F10 · F11 · F15** · 09-05 walk
**P27 · P31 · P32** · fold records **`onboard-onboarding-note-1lx0poj`** (→D1) ·
**`fb-53e7l33b-mtre3ll8`** (→D3/C7-R5) · **`onboard-interests-other-atz6kh`** (→D4) · backlog
**C7-R2 · C7-R3 · C7-R5** + `input-to-value-matrix-PROPOSAL`.

⭐ **The largest cluster on the board, and the one the typed channel is almost entirely about** (3 of 4
folds). It is also the only want Paul has stated as a *question about the product itself* rather than
as a defect — P32, paraphrased in substance: *what can we pull together for them at that level of data
provision?*

- `validated` (his own onboarding record) — **"condo" had to be typed into a free-text note because
  there is no property-type field.** The product asked an open question and got a structured answer it
  had no slot for.
- `validated` — the one card that should reflect the answer renders **Pickens-County events at a
  Midtown address**.
- `validated` — **"Houseplants!"** arrived on `onboard-interests-other` — the *"something else"* free
  text **on the interests step**. ⭐ **That settles the briefing's third small question: it is a twelfth
  interest named exactly where the product asked for one, NOT a module request.** (Whether to build
  anything remains Paul's; the *class* question is closed.)
- ⚠️ **Do not read D4 as a correction of Mom.** `validated` (her tap, `questions.json:122`, 2026-08-03):
  she answered *"That's all of them"* on a **five**-item module list. Paul's twelfth interest is an
  addition by a different household, not a revision of her answer.

#### 2.2 Why W2 probably matters MORE to Mom than to Paul, not less

`inferred`, and it is the non-obvious read in this file. Her measured depth on the frozen product is
**depth 2 = 0 and depth 3 = 0** — she reads **card faces** and does not open individuals
(`validated`, one device, lap-8 window). If the face is the whole product for her, then a card face
reading *nothing here yet* is not a minor disappointment on the way to the content. **It is the
content.** Paul can push past an empty card because he knows what is behind it. She has no such model.

⚠️ Held at `inferred` deliberately: one device, one window, a browser bucket is not a person, and it is
a claim about a **different product**.

---

### W3 · "Show me who else can see this place, and let me invite them."

**Collapses 11 ids into one want:**
census **C1 · C2 · C3** (the enabler) **· C4** · job **J5** · lap-2 walk **F14** · fold record
**`homes-second-home`** · backlog **19 · 19b · 19c · C9** · the 09-04 **L-49** view-only role.

- ⭐ `validated` — asked **twice on 2026-09-07 alone**: typed into the production store at 11:17 ET and
  said aloud on the evening walk. Asked **four times across separate days** in total.
- ⚠️ **And the store UNDERSTATES it by construction.** `homes/index.html:243` posts a constant id; the
  Worker de-duplicates per UTC day and returns `200 {duplicate:true}` **while the screen shows the
  success ack**. So the surface that collects *"who else can see this place"* can hold exactly one note
  per day. `validated`.

#### ⭐ 2.3 THE INTERPRETIVE CORRECTION — repetition is a reading about the PIPELINE, not about the customer

This is squarely my lane and it changes how a board should read the repeat counts.

> **Three threads have been asked on separate days unprompted — W3 (4×), W1's journey half (2×), W2's
> card-population half (2×). Each already has a backlog row. None has moved, because each is blocked
> on something that is not a build.** `validated` — the briefing's own diagnosis, §1.

⛔ **So "asked four times" measures how long a row has been stuck. It does not measure how much the
customer needs it.** Reading frequency as importance would put W3 on top of the board, and the honest
reading is that W3's count is high **because the pipeline had only a build-and-ship lane and a
concept blocked on a ruling had nowhere to go.** A want asked once by someone who then walked away is
invisible; a want asked four times by the person who reads the backlog is loud. Those are instrument
properties, not customer properties.

---

### W4 · "Tell me what matters today without making me scan the page."

**Collapses 8 ids:** census **B1 · B2 · B3 · B4 · D5** · job **J4** · lap-2 walk **F2** · backlog
**C7-R1 · C7-R2**.

- `paul-stated` — his resolution: keep the jump strip, collapse the summary intelligence into the
  cards, re-analyse the closed-card state. ⭐ **This answers C7-R1, open since 2026-09-04.**
- ⚠️ **The open half his ruling does not settle**, flagged not decided: the summary menu did **two**
  jobs — it SUMMARISED and it RANKED. Distributing summaries into every collapsed card preserves the
  first and drops the second, so *what matters today* becomes *scan the whole page* — which is the job
  he opened with. `inferred`.
- ⛔ **`contested` — do not quote "she navigates 100% by the jump strip."** `MOM-CYCLE-LOG.md:1115`
  says it; `:1816` says those events fired only from Paul's device; `:1480/:1503/:1525` report no
  post-`8718f46` reading. **This want currently has no Mom evidence at all.**

---

### W5 · "When I write something, tell me the truth about where it went and who sees it."

**Collapses 7 ids:** census **E2** · job **J9** · lap-2 walk **F8 · F9** · 09-05 walk **P26 · P28**.

- `validated` (his words, tracked) — F8: *"Stays on this phone for now. Nobody else sees it."* → *"so
  does that mean it's not syncing, or what exactly does that mean?"* The line is **TRUE and NOT
  LEGIBLE** — it discloses without informing, and it sits against `s0`'s standing promise.
- `validated` — F9: the **ask** path and the **save** path share one error surface. A reader cannot
  tell *my writing was lost* from *the assistant is away*.
- `validated` — E2: the "Add a home" surface returns a **success ack on a record the store threw
  away**. That is *capture must not lie*, inverted, on this repo's own rule.
- `validated` (09-05, P26/P28) — he questioned what a note's destination implies about the operating
  model, and separately did not know what would happen if he saved prematurely, **and did not risk
  finding out.**
- ⛔ **F7, F8 and F9 are the three rows whose third column reads UNANSWERED** in the findings register —
  nobody has checked whether a seat named them before Paul did, and grepping the panel reviews cannot
  answer it because those seats were commissioned after his walk.

⭐ **Why this is Mom-critical and not just a copy problem** — `inferred`: the standing doctrine
**"everything is changeable"** is a promise about reversibility, and *"it must be TRUE: never call a
thing changeable and then make changing it costly."* **A promise of reversibility is unenforceable on
a record whose destination the person cannot read.** W5 is the precondition for that doctrine being
honest, and her documented fear is getting things wrong.

---

### W6 · "Let me see and change what I told you."

**Collapses 7 ids:** census **C5 · H8** · lap-2 walk **F7 · F13** · 09-05 walk **P19** · backlog
**19c** · ruling **J-d**.

- `validated` — F7: settings and *"what you told me"* read bare-bones, **and he questioned whether
  "what you told me" is the right phrase at all.**
- `validated` — F13: let the household rename the almanac. **His own label: low priority.** Recorded
  as given.

#### ⭐ 2.4 TWO THINGS FELL OUT OF THIS COLLAPSE THAT ARE NOT IN ANY CENSUS ROW

**(a) A synthetic seat's preference is standing in the build where a validated user answer is not.**
`validated`, both halves. `engine/viewer.template.html` sets `JOURNAL_NAME = <household> + " Almanac"`,
commented *"(mom seat, round 3)"*. Mom answered `q-almanac-name` **YES — "Journal"** on 2026-07-29
(tap + label + `resolvedAt`, folded). ⛔ **This inverts my own non-negotiable: synthetic input is
`assumption` and may never outrank a `validated` one.** It is one grep to settle. It is not a defect
report and I am not designing the fix — it should be **a decision, not a leftover**, and F13 means
Paul is pushing on the same word from the other direction.

**(b) J-d may already be answered — by Paul, on 2026-09-05.** The census records J-d as an unruled
collision (*"account accent vs estate theme — which wins?"*). ⭐ **P19 states the model:** *"Pick a
colour"* → *"Pick a **profile** colour"*, and it must be **separate from the PLACE colour** — each
place gets its own. `paul-stated 2026-09-05`. That does not say which wins; it says **they are two
different objects in two different scopes and the question as posed may be the wrong question.**
⛔ I am not ruling it. I am reporting that a `paul-stated` datum on this exact question exists in the
09-05 register and appears not to have been read into C5/J-d.

---

### W7 · "The numbers have to be right, because I can check them."

**Collapses 3 ids + one standing precedent:** census **G1 · G6** · the **2026-07-26 rainfall event**.

- `validated` — four arithmetic/unit defects, all estate-independent, all verified at lap-2 close;
  every *"in N days"* is +1, so **yesterday renders as "Tonight."**
- ⭐ `validated` (2026-07-26) — **the precedent, and it is the strongest single piece of user evidence
  this project owns:** the one time a user disbelieved a number on this product, she was right **by
  14×**, because she was standing in the rain the grid cell never saw.

⚠️ **My lane's contribution here is only the precedent, not the fix.** G1 is engineering's. The
research finding is: *the make-or-break user is the one instrument that checks this app against the
actual sky, and trust is the load-bearing emotion.* A wrong number does not cost a wrong number. It
teaches the person the project depends on that the record disagrees with her own eyes.

---

### 2.5 What did NOT collapse into a customer want — and it is about half the board

⭐ **Of the 47 census rows, roughly 24 are not about a customer at all.** They are process (**F1–F5**),
instruments (**I1–I7**), feedback plumbing (**E1 · E3 · E4 · E5**), rulings owed (**J-a…J-g**), and
internal debt (**H1–H12**, several frozen on purpose). Plus five of Paul's fifteen walk findings are
**rulings, not wants** (F1 · F2 · F3 · F6 · F15).

⛔ **This is not a criticism of the census — it is a census and it is correct to hold them.** It is a
warning about how a board reads: **a list that mixes "a person wanted this" with "an instrument will
mislead us" will get sorted by size, not by kind.** The 24 non-customer rows are exactly the rows I
have no standing to speak to.

⛔ **Excluded by instruction and not counted anywhere above:** every zone row (F4 in the census, the
zone hold, `.plans/2026-09-07-zones-*`), and Z-ACK (closed; Paul discharges it in person).

---

## 3 · ⭐ CRITICALITY — one statement, inside my lane, with a falsifier

`[paul-ruled 2026-09-07, J-b: a seat may state criticality within its own lane and must show its
evidence; no seat may rank across lanes, and none decides.]`

> ### The critical customer risk on the board is W1's Mom face: that her first open prints someone else's name over an empty place.

**The five things that make it critical, each tagged:**

1. **The condition is measured, not theorised.** `validated` — 09-07, live on `1e2748d`: correct
   server data fetched, stored, then suppressed by the owner guard, rendering zero rows under
   *"Signed in as PaulKirsch"*, an account that does not exist.
2. ⭐ **The J-f ruling shrinks her recognition surface to exactly the broken part.** `validated`
   (`paul-ruled 2026-09-07`): nothing is pre-filled; she starts blank. That is the right call and it
   protects the answer key. **Its consequence for W1 is that on her first open, the only things on
   screen that can possibly be hers are her name and her place's name.** Every card is legitimately
   empty. The identity strip *is* the product at that moment.
3. **The triggering condition is the likely one.** `inferred` — the device her invite most probably
   opens on is a phone that has held another grant. That is precisely the case A2/A3 describes, and
   `validated` that no seat has ever walked it (39 of 39 lap-2 walks ran `--fresh`).
4. **The user does not report; she stops.** `validated` (frozen instance, one device): **0 taps in 35
   ask-shaped offers**, 5 of 5 on the one affordance that merely moves her, ~0.55 sessions/day, and her
   documented fear is getting things wrong. A screen that names someone else, at the moment she has
   just done what her son asked, is the exact stimulus that reads as *I did it wrong.*
5. ⭐ **And if it happens, no instrument in this loop will show it.** `validated` (beat 1): `door` has
   a `GET /api/door` route and **no tool calls it**; `onboarding-metrics` **has no GET route at all**
   and is write-only. **The failure is both irreversible and invisible.** That combination is what
   makes it critical rather than merely serious.

**What I am NOT saying.** I am not saying W1 outranks G1, or the pipeline, or the build band. Those
are other lanes and other seats. I am saying: **among things that matter to a customer, this is the
only one whose failure cannot be walked back and cannot be seen.**

**⭐ My falsifier, pre-registered:** if Mom opens `p-b91e4d` on a device with no prior grant, sees her
own name over her own place name, and proceeds — then this claim did not fire, and **W2 (the empty
card face, §2.2) becomes the top customer risk on the record.** GAP 1 is that test, exactly.

**The counter-case, stated fairly:** W2 is the largest cluster, carries 3 of 4 folds, and is the only
want Paul has framed as a question about what the product should *be*. It is a stronger claim about
*direction*. It is a weaker claim about *risk*, because a person disappointed by an empty card comes
back tomorrow, and we would know they were disappointed.

---

## 4 · THE GAPS — what changed, what closed, and one that opened

### GAP 1 — Does a real person who is not the builder get through the door at all?
⭐ **Its value went UP, for three independent reasons. Nothing lowered it.**

1. ✅ **It is UNBLOCKED.** `validated` (`paul-ruled 2026-09-07`, J-a): *"Absolutely no freeze on Mom's
   new account in production."* The census listed it as blocked; it is not.
2. ⭐ **It is now the ONLY instrument.** `validated` (beat 1): `door` has a reader-shaped hole and
   `onboarding-metrics` has no read route. T1 and T2 would make part of this deterministic — **but
   neither exists today and her invite is live now.** Until they land, a person in a room is the only
   way this question can be answered at all.
3. **The J-f ruling raised the stakes** — see §3.2. A blank start is correct and it removes every
   fallback that would have made a misidentified header survivable.

**Protocol unchanged** (briefing §2): on **her** phone, before anything else — does the screen ever
print a name that is not hers · `text_size_served` must read `lg` · `door_reached`/`_opened`/`_failed`
· whether any count of outstanding items renders anywhere.

### GAP 2 — Is "add a place" read as FOUNDING or as SWITCHING?
**Value essentially unchanged; one modest increase.** `inferred` — W3's consolidation shows Paul's own
model is explicitly **cross-household** (*"invite mom to have access to my condo and she will invite me
to the house that she sets up"*), so the places list will hold **two kinds of thing** — places you
founded and places you were invited into — before the noun for the list has ever been tested on a
person. That makes the question slightly bigger, not different.

**Still the cheapest high-value question this project can ask**, for the reason already on the record:
naming is the act she demonstrably initiates — 16 names at a kitchen table in one evening against 0
taps in 35 in-app offers. ⚠️ **Ask it before opening anything**, per the briefing's sequence rule.

### ✅ The briefing's "third smaller gap" is CLOSED — by a fold disposition, not by research
`validated` — *"Houseplants!"* arrived on `onboard-interests-other`, the *"something else"* free text
**on the interests step**. It is a twelfth **interest**, named exactly where the product asked for one.
**It is not a module ask.** The one question the briefing wanted put to Paul no longer needs asking as
a *class* question; only *"do we do anything about it"* remains, and that is his call, not research.

### ⭐ A THIRD GAP HAS OPENED — GAP 3

> **Does a person know where their writing went, and who can see it?**

**Why it is a real gap and not a design note.** Four `validated` records point at the same
comprehension failure from four directions, and **none of them is a copy problem**: F8 (a true sync
disclosure he could not interpret) · F9 (two systems sharing one error surface, so *lost* and *away*
are indistinguishable) · E2 (a success ack over a discarded record) · P28 (he did not know what
premature save would do and would not risk finding out).

**Why synthetic walking cannot answer it.** F7, F8 and F9 are the three rows the findings register
records as **UNANSWERED** — no seat raised them, and the panel seats cannot be used as evidence because
they were handed his findings. A seat reads a string and reports the string; it has no expectation
about where its own writing goes, because it has nothing at stake in it.

**Why it is Mom-critical.** `inferred` — the app is the feedback channel by doctrine, text is not, and
*"everything is changeable"* is a promise of reversibility. **Both rest on the person being able to
read where their words went.** Her whole contribution history is words she gave a system she cannot
inspect.

**Cheapest honest version — ~2 minutes, at the same visit, no UI change.** *After* she has written one
thing — a note, anything — ask a past-behaviour question about the act she just performed:
**"where do you think that went, and who can see it?"** Listen for whether she describes a *place*
(a record of hers) or a *recipient* (a message to Paul). ⚠️ Mom-Test-legal because it is about the
thing she just did, not a hypothetical about a feature.

⭐ **The three gaps compose into one visit, in this order:**
**GAP 2** (before any UI is shown) → **GAP 1** (open the invite, four readings) → **GAP 3** (after she
writes one thing). ~5 min + ~20 min + ~2 min. The visit is already ruled to happen.

---

## 5 · WHAT I DECLINED

- ⛔ **To rank across lanes.** §3 is one criticality claim inside the customer lane with a falsifier.
  I have not ordered W1…W7, and I have not compared any of them to an engineering, process or
  instrument row. Paul ranks `[J-b]`.
- ⛔ **To pitch a feature or design a fix.** Every want is stated as what a person wanted and what the
  evidence is. W1 names a falsifier, not an implementation. §2.4(a) names a decision that is owed, not
  a design.
- ⛔ **To scope zones**, or to read/write any `2026-09-07-zones-*` artifact. A separate session owns it.
- ⛔ **To design any acknowledgment for the 23 zones.** Z-ACK is closed; Paul discharges it in person.
- ⛔ **To promote synthetic input.** All four seats stay `assumption`. §2.4(a) exists precisely because
  a synthetic preference reached the build where a validated one did not.
- ⛔ **To claim anything about Mom on the new product.** She has not arrived. Every claim about her is
  cited to the frozen instance and labelled as a claim about a different product.
- ⛔ **To average the three populations.** §1.2 keeps the columns separate, including where a column is
  empty.
- ⛔ **To read repetition as importance.** §2.3 states why, with the briefing's own diagnosis.
- ⛔ **To quote Mom, or to reproduce the gitignored register's verbatim strings into a tracked file.**

---

## Evidence log

- `2026-09-07: [validated] — feedback-dispositions.json, four records with disposition:fold — fb-53e7l33b-mtre3ll8 → D3/C7-R5 (events, neighbourhood) · homes-second-home → rows 19/19b (roles, invitation) · onboard-interests-other-atz6kh → D4 ("Houseplants!" is a twelfth INTEREST, entered on the interests step's free text, not a module ask) · onboard-onboarding-note-1lx0poj → D1 (property type typed into a note because no field exists). THREE of four fold into W2, one into W3, ZERO into W1.`
- `2026-09-07: [validated] — measured live on production 1e2748d with Paul (capture F4) — whoami returned name + address + ranked interests while the card read "Empty so far." and "Signed in as PaulKirsch", a username belonging to no account. All three failure modes render the identical dead screen.`
- `2026-09-07: [validated] — .plans/2026-09-07-lap2-RETRO.md §3.0 via BRIEFING/RESEARCH-BRIEF — 39 of 39 lap-2 walks ran --fresh; the returning mode branches at one stop; the only returning battery ever run produced 12–15 failed actions per seat and four unread reports. No seat has ever arrived as a person who already exists.`
- `2026-09-07: [validated] (paul-ruled, BRIEFING §7 J-a) — the FOCUS FREEZE does not follow Mom to production. GAP 1 is unblocked.`
- `2026-09-07: [validated] (paul-ruled, BRIEFING §7 J-f) — zone work is kept for reference and NOT ported; Mom starts blank. Consequence for W1: on her first open the only things on screen that can be hers are her name and her place's name.`
- `2026-09-07: [validated] — .plans/2026-09-07-lap3-CONSOLIDATION.md §3 — GET /api/door exists and NO tool calls it; /api/onboarding-metrics has NO GET route anywhere and is write-only. If Mom bounces at the door, no instrument in the loop will show it.`
- `2026-09-07: [validated] — CONSOLIDATION §2 / RESEARCH-BRIEF §0 — homes/index.html:243 posts a constant id; worker.js:3082-3085 de-duplicates per UTC day and returns 200 {duplicate:true} while the screen shows a success ack. The roles surface can hold one note per day; the store UNDERSTATES how often W3 was asked.`
- `2026-09-07: [validated] — .plans/2026-09-07-lap3-paul-feedback-CAPTURE-2.md F8 — viewer.html:20723 sync mode household-local; the pill reads "On this phone"; the next line renders no sync button. The copy is TRUE and NOT LEGIBLE, and it sits against s0's "yours on any phone" promise.`
- `2026-09-07: [validated] — CAPTURE-2 F9 — viewer.html:21360 is the catch on the ASK path; the note saved through a separate local path. Two systems, one error surface.`
- `2026-09-07: [validated] — CAPTURE-2 F14 + the production store at 11:17 ET — roles-and-invitation asked TWICE on 2026-09-07, unprompted both times; four times across separate days in total.`
- `2026-09-05: [paul-stated] — .private/synthetic-walks/GATE2-paul-findings.md P19 (cited, not reproduced) — profile colour and PLACE colour are separate things and each place gets its own. Bears directly on the J-d "which wins" framing recorded as unruled.`
- `2026-09-05: [paul-stated] — same register, P29/P30/P31/P32 — he named an Atlanta place and landed on Fernwood; what he asked for instead is a page that is HIS, empty but recognisable as his place, and the question of what an address alone should buy a person.`
- `2026-08-03: [validated] — Mom's own tap, questions.json:122 — q-top-categories answered "That's all of them" on a FIVE-item module list. Paul's twelfth interest does not correct her answer.`
- `2026-07-29: [validated] — Mom's own tap, q-almanac-name = "Yes, Journal", resolvedAt 2026-07-29. ⚠️ engine/viewer.template.html sets JOURNAL_NAME = <household> + " Almanac", commented "(mom seat, round 3)" — a SYNTHETIC seat's preference standing where her validated answer is not.`
- `2026-07-26: [validated] — her free-text note disbelieving the 7-day rainfall figure; she was right by 14× (station 2.01" vs ERA5 grid 0.14"). The precedent under W7: the make-or-break user is the instrument that checks this app against the sky.`
- `lap 8: [validated] (telemetry, ONE device, frozen instance) — every ask-shaped affordance 0 of 10 · 0 of 10 · 0 of 10 · 0 of 5; jump strip 5 of 5; depth 2 and depth 3 both ZERO. ⚠️ A deviceId is a browser bucket, not a person; this is a claim about a different product.`
- `2026-09-07: [validated] — Mom's invite p-b91e4d minted and sent ~12:05 ET, UNSPENT. Nothing about her behaviour on the new product exists.`
- `2026-09-07: [contested] — MOM-CYCLE-LOG.md:1115 vs :1816 vs :1480/:1503/:1525 — the "she navigates 100% by the jump strip" figure. W4 currently has NO usable Mom evidence.`
- `2026-08-31: [inferred] — Paul-relayed (memory project_tate_commons_initiative) — Bob redirected the ask to his own two houses. That the second-estate case exists is inferred; anything Bob wants from a roles screen is [assumption] — he has never been asked.`
- `2026-09-07: [assumption] — every synthetic seat reading, per standing doctrine. None is used as evidence for a user need anywhere in this file.`
- `Open, unobserved: whether a person reads a saved note as a RECORD of theirs or a MESSAGE to Paul (GAP 3) · whether "+" on a places list reads as founding or switching (GAP 2) · whether a real non-builder gets through the door (GAP 1) · whether Bob has any opinion about roles.`
