---
type: audit
project: fernwood
artifact_id: feedback-loop-audit-2026-07-26
date: 2026-07-26
last_updated: 2026-07-26
evidence_level: mixed — see per-claim tags
performer: .user-research/persona-mom.md
lens: user-research only (engineering-partner, ux-expert, ai-advisor ran their own lenses in parallel)
sources:
  - BACKLOG.md A1 / A3 / A4 / A6 / B6 (read 2026-07-26)
  - CLAUDE.md "Mama's Perspective" — lifecycle, channel doctrine, AI boundary, lifecycle rule
  - .private/mom-feedback-2026-07-26.md (REFERENCED, never quoted — see privacy note)
  - .private/2026-07-26-mom-feedback-synthesis.md + .private/2026-07-26-mom-feedback-return-leg.md
  - .user-research/persona-mom.md · 2026-07-02-mom-behavior-interpretation.md · 2026-07-13-mom-feedback-queue.md
  - worker/worker.js, tools/momlib.py, tools/*.py, viewer.html MOM_ACK_DATA, feedback-log.json (read directly, 2026-07-26)
privacy: >
  PUBLIC REPO. Mom's words about HERSELF are referenced by pointer only
  (.private/mom-feedback-2026-07-26.md) and never quoted here. Her words about the
  APP are quoted only where BACKLOG.md already publishes them.
purpose: >
  A holistic per-channel read of the Mom feedback loop: recognition, analysis,
  reflection-to-her, corpus incorporation, backlog steering, and question generation —
  re-read in light of the 2026-07-26 rainfall episode.
---

# The feedback loop, channel by channel — a user-research audit

**If Paul reads five lines:**

1. The wrongness-risk hypothesis is **right in direction and not yet separable from a second explanation** — authorship. They predict identical data so far. One card (moss) separates them. `[inferred, strong]`
2. The rainfall note is the best evidence in the project — but **not for the hypothesis as stated.** She *did* adjudicate the app. She just did it in her own words, at her own moment, hedged into a statement about her own belief. **She'll adjudicate; she won't be examined.** `[inferred, strong]`
3. **`/api/zone-feedback` is read by nothing.** Not by a tool, not by `momlib.ARRIVAL_CHANNELS`, not by the R2 unacknowledged-arrivals check. If she has ever used it, we do not know, and the loop-health dashboard would read **green while blind.** `[validated — code read]`
4. **There is no evidence she has ever noticed the ack ribbon — and one live test that leans against it.** The ribbon was up from 7/22 and did not prevent what she told Paul on 7/26. The only return leg ever *observed* working was a human telling her, in a channel where she could reply. `[inferred, strong]`
5. The risk that stops her is **a second unanswered report**, not fatigue from being asked. The evidence against asking is *futility*, not *harm* — don't over-correct into asking nothing.

---

## Part 1 — Testing the wrongness-risk hypothesis against the record

### 1.1 The hypothesis, and what survives

> **Paul's working hypothesis:** the channels sort by wrongness risk. She avoids anything that asks her to be right about *our* guess, and uses anything where she reports *her own* experience.

**The direction holds across every channel we have data on.** `[inferred, strong — multi-source]`

| Channel | Shape of the ask | Her rate |
|---|---|---|
| Confirm card | grade our guess | **1 answered / 35 offered** `[validated]` |
| Guru | she asks, we answer | 2 real questions + a genuine follow-up in one 9-min session `[validated]` |
| General feedback box | her words, her topic | the rainfall report `[validated]` |
| Photo → pending-species | she supplies the object | Spiderwort promoted to canon 5/22 `[validated]` |
| Weeds card (reference only) | asks nothing | the only unprompted praise in project history `[validated]` |
| Zone voice / zone text | her words, our frame | **0 Mom captures in ~9 days live** `[validated]` |

Corroborating detail that matters: the three confirms she *did* answer were the three she'd have been certain of. `[validated — BACKLOG A3]` And on 7/26 she named a card she would answer, then spent nine minutes in the app asking Guru instead and left it unanswered. `[validated]`

### 1.2 What the rainfall note actually proves — and it is not quite what Paul thinks

Her note, 2026-07-26 09:20 ET (quoted because BACKLOG.md already publishes it as app feedback):

> *"It's confusing to read the rainfall over the past seven days because I don't believe it's literally the past seven days. Today it shows as .14 inches over the last seven days, which is certainly not correct in a perfect world. I could look back and see the rainfall by day."*

She was right by **14×**. `[validated — verified in code, fixed in f38c275]`

**Read the grammar, not just the content.** She did not write *"the number is wrong."* She wrote *it's confusing to read*, *I don't believe*, *in a perfect world*. Every one of those is a statement about her own experience or belief — **none of them can be scored false.** She delivered a hard factual contradiction of the app while keeping the epistemic escape hatch open the whole way. `[inferred, strong — from her own text]`

So this episode does **not** show that she'll take on wrongness risk when the stakes are high. It shows the opposite, more precisely: **the wrongness-avoidance is so consistent that it operates even when she is certain and correct.** It shapes her *sentence construction*, not just her channel choice.

That sharpens the axis. It is not "risk of being contradicted." It is:

> **Can this statement be scored false and attributed to her?**
>
> She freely produces: her own perception, her own belief, her own expertise, questions, and hedged proposals.
> She does not produce: a binary, checkable, attributed verdict on a fact we chose.

### 1.3 Is it over-fitted? Yes, partly — and here is exactly where

**n is small and the confound is total.** The confirm-card channel differs from every channel she uses on **six** dimensions at once, not one:

1. It is the only channel where **we initiate** (push). Every channel she uses, she initiated.
2. It is the only channel where **we choose the topic**.
3. It is the only channel whose primary answer is a **binary button**.
4. It was **structurally broken** for most of the window (A-or-B question wired to Yes/No; "Ask me later" as the not-sure label; no photo until 7/20). `[validated — BACKLOG A1]`
5. It is the only channel where **no loop had ever visibly closed** until this week. `[validated]`
6. It **accumulates and persists** — cards return.

Any one of those alone predicts a 1/35 funnel. Wrongness risk is one of six candidates — it is the one **she named**, which is real evidence, but *self-reported cause is the weakest class of validated evidence*. People are unreliable narrators of their own reasons, and she was answering a reassuring son at the time.

**The rival explanation that fits the data equally well is AUTHORSHIP.** Every rich contribution in project history was about a thing she was already thinking about that morning. The confirm card asks about a thing *we* were thinking about. That predicts identical data and involves no fear at all. It also explains the three she answered (plants she actually thinks about) as well as the fear model does.

**The decisive test has never been run.** No observation-shaped or expertise-shaped card has ever been served. Everything to date compares a *broken push channel* against *healthy pull channels* — which is not a test of question type.

**Verdict: `[inferred, strong]`, not `validated`.** Act on it. Don't write it into doctrine as settled, and don't let it stand as the sole justification for retiring a whole card class.

### 1.4 The one card that separates the two hypotheses

The moss card (BACKLOG "👥 Agent drafts → Paul confirms," item 9) is already queued as *the nicest first card*. It is more than that — it is **the discriminating instrument**, and Paul should run it knowing what each outcome means:

- Moss is **expertise-class** (zero wrongness risk — she is the source, the app is the novice).
- Moss is still **ours-initiated, ours-timed, ours-framed** (authorship unchanged).

> **She answers it** → wrongness risk was the binding constraint. Re-shape the card slate to classes 2/3, keep investing in the widget.
> **She doesn't answer it** → authorship is the binding constraint. No card shape will fix it; cap the confirm-card investment permanently and put the budget into making it trivially easy for her to say the thing she was already going to say.

n = 1 either way, and a null is weaker than a hit (she may simply not have opened the app). But it is the cheapest fork in the project, and the two branches have very different budgets attached. `[assumption — this experimental design; the discrimination logic is sound, the n is not]`

### 1.5 The sentence I'd keep

The prior formulation was *"she'll ask; she won't answer."* The rainfall note breaks that — she asserted, hard, unprompted. The formulation that survives all the evidence:

> **She'll adjudicate. She won't be examined.**

The confirm card's defect may not be that it asks for a verdict — she volunteered one. It's that it **conscripts** her into one, on our schedule, on our topic, on a form, with the result visible as a score. `[inferred — this is a refinement, not an established finding; the moss card tests it]`

---

## Part 2 — The nine channels: does the loop actually close?

Legend: ✅ automated · ⚠️ partial / human-triggered · ❌ none.

| # | Channel | Recognized? | Analyzed? | **Reflected to her?** | Into corpus? | Steers backlog? | Generates questions? |
|---|---|---|---|---|---|---|---|
| 1 | Confirm-card **tap** | ✅ `/api/feedback` — pickup, watch, ack-check | ✅ canon-derived punch-list (`momlib.question_state`) | ⚠️ chip flip + ribbon | ✅ `fold-answer.py` | ✅ | ⚠️ reseed, but from *our* doubt |
| 2 | Confirm-card **note** | ✅ rides the same record | ⚠️ human | ❌ no path of its own | ⚠️ hand-applied | ⚠️ | ❌ |
| 3 | **General feedback box** (ribbon + q-open) | ✅ *since 7/26* — `check-mom-ack.py`, 8pm launchd | ⚠️ human (correctly) | ✅ *since 7/26* — ribbon + `feedback-log.json` | ⚠️ disposition only, never her words (public repo) | ✅ shipped a fix same day | ❌ |
| 4 | **Field note / observation** | ✅ `/api/observations` in R2 | ❌ | ⚠️ she sees her own entry; nothing comes back | ❌ no path to canon | ❌ | ❌ |
| 5 | **Garden Guru question** | ✅ `/api/conversations`, metadata only | ❌ (correct — AI boundary) | ✅ the answer, instantly — and nothing after | ❌ | ⚠️ only if Paul reads | ❌ |
| 6 | **Zone voice capture** | ✅ `/api/zone-audio` | ⚠️ transcription built, Paul-side, UNVERIFIED-stamped | ❌ | ❌ manual | ❌ | ❌ |
| 7 | **Zone "describe a place" text** (`/api/zone-feedback`) | ❌ **NOTHING READS IT** | ❌ | ❌ | ❌ | ❌ | ❌ |
| 8 | **Photo → pending-species** | ✅ `review-pending-species.py` | ✅ | ✅ **the species appears** | ✅ `promote-species` | ❌ | ❌ |
| 9 | **Behavioural metrics** | ✅ heavily | ✅ | ❌ *(and correctly — never reflect telemetry to her)* | n/a | ✅ **over-weighted** | ✅ |

### 2.1 ⛔ Channel 7 is the finding — a live channel nothing has ever read

`[validated — code read, 2026-07-26]`

- `worker.js` accepts `POST /api/zone-feedback`, stores records with `status: "pending"`, and exposes a date-range `GET`.
- **No file in `tools/` references it.** `momlib.ARRIVAL_CHANNELS` is `feedback · observations · zone-audio · guru` — zone-feedback is absent.
- Therefore **R2 (unacknowledged arrivals) is structurally blind to it.** The ack check can report 🟢 while her input sits in KV.

Three things follow, in order of severity:

1. **A green dashboard that is blind to a live channel is worse than no dashboard**, because it converts an *unknown* into a *confident false negative*. This is the same class of error as the 7/26 punch-list phantom — a tool reporting from an incomplete model of the world — and it survived the determinism build that fixed the other two.
2. It is the **exact failure mode of the rainfall note, one degree worse.** The rainfall note at least had a watermark path that surfaced it once. This has zero read path — anything here has been silent since ship day.
3. **It fails Paul's own brand-new standing rule** (CLAUDE.md, 7/26: *a new input surface does not ship until a note arriving on it can be surfaced, protected from the watermark, and closed*). This channel is the rule's first back-test and it fails all three legs.

**First action is not a build. It's a read.** `GET /api/zone-feedback?start=<launch>&end=today` and find out whether the count is zero. That is a five-minute deterministic question, and no honest statement about loop health can be made until it's answered. If it's non-zero, an arrival has been sitting unanswered for weeks and it outranks everything else in Track A.

### 2.2 What "reflected back to her" should MEAN, per channel

It is not the same act for a voice recording as for a bug report. Concretely:

**1 · Confirm-card tap** — the chip flip is **evidence about the plant**; what she needed was **evidence about her** (correctly diagnosed in `.private/2026-07-26-mom-feedback-return-leg.md` §1b). The reflection must happen **at the site of the contribution, not the site of the record** — where the card was, on her next open, something that says what changed *because of her*, in that slot. She should never have to navigate to a plant card to learn her answer was good. `[inferred, strong]`

**2 · Confirm-card note** — a note is prose. The dignifying reflection for prose is **quotation, not summary**: her words appearing verbatim in the record, attributed to her. `[assumption — the mechanism is untested; grounded in her documented sensitivity to having her wording changed, CLAUDE.md 7/26]`

**3 · General feedback box** — the thing she flagged **visibly different, plus a sentence conceding she was right.** The live ribbon does this and is the best return-leg artifact the project has produced:

> *"You were right about the rainfall — it wasn't our own gauge it was reading. It is now, and you can look back at it day by day."*

Three properties worth naming as a template: it **concedes** ("you were right"), it **names the specific thing** (rainfall, our gauge), and it **hands her a new capability** (day by day). For a user whose documented hesitation is about being wrong, an explicit *you were right* is the single highest-value sentence the system can emit. `[inferred, strong]`

**4 · Field note / observation** — the reflection with the highest value-per-unit-effort in a *field journal* is **her observation coming back to her, seasonally**: *"you noted the laurel opening April 25 last year — watch for it now."* That is Phase G, currently gated on ~50 observations. Nearer-term and nearly free: her observation should be **visible on the thing it is about** — the lily-pad note showing on the lily-pad card. Right now her notes go into a list and never touch the subject. `[inferred]`

**5 · Garden Guru** — the answer is the reflection, and it works. What is missing is everything after. **Her questions carry facts.** *"How can I best utilize the rich filter water from our pond filter"* asserts that the property has a pond filter producing rich water — ground-truth absent from the record, delivered inside a question. **Guru is a ground-truth channel we treat as a service channel.** `[inferred, strong — one clear instance; the pattern generalizes but n=1 for premise-harvesting specifically]`

The reflection she'd notice: **the app later knowing the premise of her question.** And note that she has *already asked for this return leg herself* — *"Is there a way to look back at these, eg in the 'journal'?"* That is not a findability request. **It is her asking for her contributions to be durable.** Re-file A6 from findability to return-leg; it changes what "done" means (her questions live *in the journal*, in her framing, not in a new Conversations screen).

**6 · Zone voice** — the reflection that lands is **hearing her own words come back as the record's words.** One trap: transcription is a hypothesis, so the instinct is to show her the transcript and ask *"did we hear you right?"* — **that is a verdict ask, the exact class she declines.** The reflection for voice must be **assertive, not interrogative**: show what we wrote down; do not ask her to approve it. If it's wrong she will say so — she just proved she will. `[inferred, strong — the rainfall episode is the proof she volunteers corrections]`
**But: 0 Mom captures in ~9 days.** Do not build a return leg for a channel with no arrivals.

**7 · Zone text** — undefined, because nothing has ever been read. See 2.1.

**8 · Photo → pending-species** — **this is the best-working loop in the app and nobody counts it as a feedback channel.** She submits a photo; a species appears in the record. No acknowledgment mechanism is needed **because the change *is* the acknowledgment.** `[validated — Spiderwort promoted 5/22, persona telemetry]`

**9 · Behavioural metrics** — reflect **nothing**. Telling her *"you opened the app 27 times"* is the productivity-app anti-persona in pure form. This channel's failure mode is not under-reflection; it is **over-weighting**: metrics steer the backlog more than her words do, and they are the least reliable input (deviceId is a browser bucket; Safari ITP evicts it). The A1 episode is the proof — a widget funnel blocked a whole track for two weeks while her words said something different. `[validated]`

### 2.3 The structural pattern underneath all nine

> **Her input lands when it becomes an OBJECT she can see. It dies when it adjusts a PROPERTY of an object.** `[inferred, multi-source]`

- Photo → **a new species record** (object). Works.
- Guru question → **an answer** (object). Works.
- Moss / household systems → **things she proposed** (objects). Highest energy she has ever shown.
- Rainfall note → **a new day-by-day view** (object). She got a real artifact back.
- Confirm tap → `confidence: inferred → verified` (**an invisible property**) plus a small chip. Dead.

This predicts the entire engagement pattern without invoking fear at all, which is why it deserves a place next to the wrongness-risk hypothesis rather than under it. **Design steer: prefer asks whose answer produces a thing she can see, over asks that adjust an attribute of a thing that already exists.** It also explains why the ribbon works better than the chip — the ribbon is an object addressed to her; the chip is an attribute of a plant.

---

## Part 3 — The right next question, and through which channel

Paul asked for the loop to generate new questions where we need clarification. Four named questions, plus the mechanism that should produce them automatically.

### Q-A · The in-app next ask — moss, expertise-class

**Channel:** the confirm-card slot (`MAX_VISIBLE` down to 1 while it's tested).
**Why this one:** she is the authority, the app is the novice, the record has nothing, and it is the discriminating test in §1.4. She cannot lose the exchange.
**Design constraints, from the record:** one thing per card (the compound-question defect killed `q-clematis-variety` *and* `q-weed-stiltgrass`); no verdict; her coinages preserved exactly.

**Draft for Paul's confirmation — card wording reaches Mom, so this is a proposal, not a shipped string:**

> *The record doesn't know about the moss yet. Where are the good mossy spots?*

That is deliberately bare: no buttons, one free-text field, no "confirm." If Paul wants a tap-first version, the honest tap version is a **list of places she can pick from** (by the barn, the pond edge, the north side) — a choice among places she knows, never a yes/no about a place we guessed.

**What it must NOT do:** ask about the buttermilk. She already told us the technique; asking again would read as not having listened, which is the precise injury to avoid this week.

### Q-B · The clarification the record genuinely needs — household systems

Her proposal is a **stated future want** — the weakest evidence class in The Mom Test — but it named a **specific past failure** (not being able to find a receipt), which is the strong kind. B6 is already scoped as one enum value, so the risk isn't build cost; it's building the wrong job.

**Two different builds hide behind the same ask:** *find the receipt when something breaks* (warranty/service job) vs. *know what I have* (inventory job).

**Ask about the past event, never the feature. Draft:**

> *"The last time something in the house needed a repair or a part — what were you trying to find, and where did you end up looking?"*

**Channel: Paul, in conversation, and relayed.** Not a card. This is a story question; a card cannot hold it, and the app has no surface for a multi-sentence answer she'd actually give. Doctrine permits this explicitly — *Paul relays; the model does not fetch.*

### Q-C · The master question — what does she believe happens to things she says?

**This is the highest-value unanswered question in the project**, and everything in Part 2 is downstream of it. It supersedes Q2 from `2026-07-02-mom-behavior-interpretation.md` ("what did you figure happened to that note?") with a better anchor, because we now have an episode where we *know* she contributed and *know* we responded.

**Draft (Mom-Test-clean — past behavior, non-leading, deflating branch offered as openly as the confirming one):**

> *"When you wrote in that the rainfall number looked wrong — what did you figure would happen with that? Did you picture me seeing it, or the app doing something with it, or were you not really sure?"*

**Why this and not "did you see the ribbon?":** that question is leading, yes-prone, and exam-shaped — the exact form she declines, asked about the exact topic where she's most likely to be agreeable. Q-C asks about her expectation *before* our response, which she can't get wrong.

**What each answer changes:**
- *"I figured you'd see it"* → the return leg can stay quiet and personal; the ribbon is optional garnish.
- *"I thought the app would do something"* → the return leg must be **in the app, loud, and specific** — the current design is right and needs to be reliable.
- *"I wasn't sure"* → we are training an expectation from zero, and the first few responses matter more than any of the mechanism work.

**Channel: Paul, in conversation.** Not a card, not the app.

### Q-D · Not a question for Mom — a question for the codebase

**Has anything ever arrived at `/api/zone-feedback`?** Answer this before asking her anything about zones, and before reading any loop-health number as green.

### The mechanism: how the loop should generate questions on its own

Right now, nothing in the system produces a clarification question. The concrete place one *should* have been produced this week:

She wrote *"I could look back and see the rainfall by day."* We built a by-day view — **at her gauge.** She might have meant the regional series she was reading. **We interpreted, shipped, and the interpretation left no trace.**

**Proposal:** `feedback-log.json` gains an `openQuestion` field alongside `disposition`. When Paul addresses a note by *interpreting* what she meant, the interpretation is recorded as a question, and the **next acknowledgment can carry it** — inside her own topic, as the second sentence of the ribbon, exactly the shape §2b of the return-leg companion recommends.

That is the honest answer to "where does the loop generate questions": **not from our uncertainty markers** (`harvest-questions.py` is structurally a verdict-ask factory — it can only ever produce class-1 asks), **but from the gaps in our reading of what she already said.** Those are guaranteed to be inside her topic, guaranteed to be things only she can settle, and guaranteed to be things she already cared enough to raise. `[assumption — proposed mechanism, unbuilt]`

---

## Part 4 — The uncomfortable one: has she ever noticed the ribbon?

### 4.1 The honest answer: no evidence — and one live test that leans against it

`momack_shown` counts exposure, not receipt (BACKLOG A1 · R4 says so explicitly, and correctly). `[validated]`

But the situation is worse than "unmeasured." **The ribbon has had exactly one live trial and it did not visibly work.** `[inferred, strong]`

- Ribbon shipped **2026-07-22**, naming the panicle hydrangea.
- It sat on her surface, unchanged, through **2026-07-26** — the week she was actively contributing through four channels.
- On **2026-07-26** she told Paul what she told him about her own answers (referenced, not quoted: `.private/mom-feedback-2026-07-26.md`).

Three readings, and **the instrument cannot distinguish them:**
1. She never saw it.
2. She saw it and it did not register as being about whether *her answers were good*.
3. She saw it and it wasn't enough.

**All three are bad for the current design**, and there is no version of these facts in which the 7/22 ribbon succeeded. That is the honest read, and I don't think it has been stated yet.

### 4.2 The one return-leg mechanism we have ever *observed* working

Paul told her, in words, in a channel where **she could reply** — and she replied. The reply *was* the receipt. `[validated — .private/mom-feedback-2026-07-26.md, referenced]`

**Structural conclusion:** the ribbon is a **broadcast, not an acknowledgment.** A message you cannot answer generates no evidence that it arrived. Receipt isn't unmeasurable because of ITP or deviceId — **it's unmeasurable because we built a one-way surface and then asked how to measure whether it landed.**

And note the cost Paul has already accepted: **closing text as an official channel removed the only surface where receipt has ever been observed.** CLAUDE.md states the cost once and correctly. The consequence for this audit: the app now has to *reproduce* a reply-capable acknowledgment, or receipt stays permanently unmeasurable by construction.

**Recommendation (for ux-expert to shape, not me):** make the ack ribbon **tappable**, opening the existing general-feedback panel with focus in the field. No CTA text, no badge — just a reply path. It adds no surface to the W8 stack (both elements exist), it inverts the exposure/receipt problem (**replies are receipts**), and it turns the acknowledgment from a broadcast into a conversation, which is the register that demonstrably worked. Risk to weigh: a tappable ack could read as an ask, which would poison the one surface whose job is to ask nothing. `[assumption — proposed, untested]`

### 4.3 So how should Paul read the loop's health? Three tiers, honestly labelled

**Tier 1 — PROCESS (measurable, ours, already built).** R1 ack staleness · R2 unacknowledged arrivals · R3 specificity. Green means **we did our part**. It is never evidence she felt heard. Keep exactly as built — **and add channel 7 to `ARRIVAL_CHANNELS`, or R2's green is a lie.**

**Tier 2 — BEHAVIOURAL CONSEQUENCE (measurable, hers, indirect).** Not *"did she see it"* but **did arrivals hold or rise in the window after a specific, correct, conceding acknowledgment.** No new instrumentation; the arrival timestamps already exist. State the limit out loud: with one user on a bursty weekly cadence this will **never** reach significance. It is a **narrative** instrument, not a statistical one, and it should be read as a story Paul tells over months, not a number.

**The one clean case available right now:** did she open the **day-by-day rainfall view**? It is new, and the ribbon is its primary signpost. **Asymmetric evidence — a hit is the strongest receipt evidence this project will ever get without asking her; a miss proves nothing** (she may have read the ribbon and been satisfied; the release-notes card is a second discovery path). Instrument it, and pre-commit to not over-reading a zero.

**Tier 3 — TRUE RECEIPT: she says something back.** Currently impossible in-app by construction (§4.2). Either give the ribbon a reply path, or accept that receipt is validated only when Paul talks to her — which is legitimate, and should be *stated* rather than papered over with a proxy.

**The one-line honest read of loop health today:**

> The capture leg is now well-instrumented on four of nine channels, blind on one, and partial on the rest. The return leg is **one week old**, has **one shipped delivery** whose receipt is unknown, and its **only historically validated instance happened outside the app in a channel that is now closed by doctrine.**

That is not a failing loop. It is a **loop with a strong new mechanism and no evidence yet that it reaches the person.** Read it that way and the next month's work is obvious: reliability first, receipt evidence second, new asks third.

---

## Part 5 — What is most likely to make her STOP contributing

Ranked by evidence strength, not by theory.

### 1. A second unanswered report `[inferred, strong]` — the top risk, and it is ours

She has now had **exactly one** experience of contradicting the app: she was right, and within a day the app conceded and handed her a new capability. That is a **single reinforced trial**. The next report that goes unanswered — or answered late, or answered generically — teaches the opposite lesson on a base of n=1, and **extinction after one reinforced trial is fast**.

The exposure is live and specific: **`/api/zone-feedback` guarantees silence if she uses it** (§2.1). Field notes and Guru turns have ack coverage but **no per-item lifecycle** — the same gap one layer over, as BACKLOG A3 already notes. Zone-audio has 5 recordings, 3 never listened to.

**This is the risk to spend on.** It is entirely within Paul's control and it does not require knowing anything more about her.

### 2. Garden Guru being wrong about her property `[inferred, strong]`

The 2,800 ft error is on her surface, in the channel she uses **most freely**, and it is the original Fernwood error class returning (lake elevation attributed to the property). Note the asymmetry the backlog under-weights: **the rainfall bug damaged a channel she barely used; a Guru error damages her primary one.** And she is demonstrably the kind of user who catches errors. Trust is the load-bearing emotion, and the channel with her highest usage currently has the least verification. Sitting behind *"check a few more answers first"* is right on rigor and too slow on priority.

### 3. Her words being corrected or improved `[validated as a mechanism; the injury is `assumption` — it hasn't happened to her yet]`

The system already caught itself once: she coined "household systems," hedged that it might be wrong, was right — and the first ribbon draft silently improved it to "the house's own systems." For someone whose documented hesitation is about getting words wrong, **being quietly corrected is the precise injury.** Low frequency, highest severity. The standing rule in CLAUDE.md covers it; the residual risk is anything AI-drafted reaching her, and the existing gate is the right one.

### 4. The un-draining card stack `[assumption — and currently CONTRADICTED by evidence]`

The theory: 33 unanswered cards at the top of her app are a standing visible record of things she hasn't done — a scoreboard of un-taken tests for someone who fears being wrong, violating the tone doctrine *structurally* even while the copy stays calm.

**But the one datapoint we have contradicts it.** During the exact window those 33 cards accumulated, she said the app is getting better every time she opens it. `[validated — BACKLOG A1]` **So this stays a watch item, not a finding.** Worth doing anyway on other grounds (`MAX_VISIBLE` → 1 while the new slate is tested; consider letting unanswered cards age out silently — **an ask that never expires becomes a debt**), but do not justify it with an attrition claim the evidence doesn't support.

### 5. Adding asks as the app gets better `[inferred]`

Her praise was for the section that **asks nothing** (weeds). Every new solicitation surface spends goodwill that the reference surfaces earn. W8 exists precisely for this and is un-run.

### ⚠️ The calibration correction — don't over-correct into asking nothing

The whole team's read this week has swung toward *stop asking her*. Hold the distinction:

> **The evidence is for FUTILITY, not HARM.** `[validated]`

No negative reaction to any card has ever been observed. She has never complained about being asked. She viewed 33 cards and said the app is getting better. The cards aren't hurting her — **they're not working.** Those call for different responses: futility says *change the ask*; harm would say *remove the surface*. Removing the ask surface on futility evidence would be the same over-reading that produced the A1 gate — a widget's health mistaken for a verdict about her.

---

## Evidence log

- `2026-07-26: [validated] — code read (worker/worker.js, tools/momlib.py ARRIVAL_CHANNELS, grep across tools/) — POST/GET /api/zone-feedback exists and stores records with status:"pending"; NO tool references it and it is absent from the R2 arrival-channel list. A live input channel has never been read, and the ack check would report green while blind to it.`
- `2026-07-26: [inferred, strong] — Mom's rainfall note (BACKLOG A1, publicly quoted) — she delivered a 14x factual correction using only unfalsifiable constructions ("it's confusing to read," "I don't believe," "in a perfect world"). Wrongness-avoidance shapes her sentence construction, not just her channel choice. Refines Paul's hypothesis: the axis is "can this be scored false and attributed to me," not "am I contradicting the app."`
- `2026-07-26: [inferred, strong] — the confirm channel differs from every channel she uses on six dimensions simultaneously (push, our topic, binary buttons, structurally broken until 7/20, never visibly closed, accumulates). Wrongness risk is one of six candidate explanations and is the only one resting on self-reported cause. AUTHORSHIP predicts identical data with no fear term. Not separable at current n.`
- `2026-07-26: [assumption — experimental design] — the moss card is the discriminating instrument: expertise-class (zero wrongness risk) but still ours-initiated/ours-topic (authorship unchanged). An answer implicates wrongness risk; a null implicates authorship. n=1; a hit is informative, a miss is weak.`
- `2026-07-26: [inferred, multi-source] — her input lands when it becomes an OBJECT she can see (photo→species record; Guru answer; the day-by-day rainfall view; the domains she proposed) and dies when it adjusts a PROPERTY of an existing object (confidence: inferred→verified + a chip). Predicts the full engagement pattern without invoking fear.`
- `2026-07-26: [inferred, strong] — Guru questions carry ground-truth in their premises ("the rich filter water from our pond filter" asserts a pond filter absent from the record). Guru is a ground-truth channel treated as a service channel; no premise-harvest exists. One clear instance.`
- `2026-07-26: [validated] — Mom, publicly quoted in BACKLOG A1 — "Is there a way to look back at these, eg in the 'journal'?" — asked minutes after two Guru questions. Read as a RETURN-LEG request (make my contributions durable), not a findability request. Re-frames A6's definition of done.`
- `2026-07-26: [inferred, strong] — the MOM_ACK_DATA ribbon shipped 7/22 and stood unchanged through 7/26, the week she told Paul what she told him about her own answers (ref: .private/mom-feedback-2026-07-26.md). The ribbon has had one live trial and there is no reading of these facts in which it succeeded. Three explanations (unseen / registered wrong / insufficient) are indistinguishable with the current instrument.`
- `2026-07-26: [validated] — the only observed instance of the return leg working was a human telling her in a channel where she could reply; the reply was the receipt. The ack ribbon has no reply affordance, so receipt is unmeasurable BY CONSTRUCTION, not because of deviceId/ITP.`
- `2026-07-26: [assumption — proposed] — making the ack ribbon tappable into the existing general-feedback panel would convert broadcast into conversation and make replies serve as receipts, without growing the W8 stack. Risk: a tappable ack may read as an ask, poisoning the one surface whose job is to ask nothing. Needs ux-expert.`
- `2026-07-26: [inferred] — did she open the new day-by-day rainfall view is the one clean receipt proxy currently available (the ribbon is its primary signpost). Evidence is asymmetric: a hit is strong, a miss is null (release-notes card is a second discovery path).`
- `2026-07-26: [validated] — she viewed 33 confirm cards without answering them and, in the same window, said the app is getting better every time she opens it (BACKLOG A1). The evidence against the confirm card is FUTILITY, not HARM. The card-stack-as-attrition-risk theory is currently contradicted; hold it as a watch item, not a finding.`
- `2026-07-26: [validated] — feedback-log.json records the rainfall note as addressed AND acknowledged (f38c275 fix, f2cd8a7 ribbon). The general-feedback channel is the only one of nine with a complete, closed, per-item lifecycle.`
- `2026-07-26: [assumption — proposed mechanism] — the loop's natural source of clarification questions is the gaps in OUR reading of what she already said (e.g. by-day rainfall: her gauge or the regional series?), recorded as an openQuestion field on feedback-log.json and carried as the second sentence of the next acknowledgment. harvest-questions.py cannot serve this role — it seeds from our uncertainty markers and is structurally a verdict-ask factory.`

## Open questions

- **Has anything ever arrived at `/api/zone-feedback`?** Answerable deterministically in five minutes. Blocks any honest loop-health read.
- **Q-C — what does she believe happens to things she says?** The master question. Paul, in conversation. Supersedes Q2 of `2026-07-02-mom-behavior-interpretation.md`.
- **Q-B — household systems: warranty/service job or inventory job?** Ask about the past failure, not the feature. Paul, in conversation.
- **Does an expertise-class card get answered?** The moss card. Separates wrongness risk from authorship.
- **Do a confirm-card *note* and a field-note have any lifecycle at all?** Flagged for engineering-partner — they appear in the ack check but I found no per-item `needs-reply` path for either.
- **Q1 of `2026-07-02-mom-behavior-interpretation.md`** (did she have a follow-up in mind, or was she done?) is now partly answered — she followed up unprompted on 7/26. The remaining half (does the UI dead-end her) is still open.
