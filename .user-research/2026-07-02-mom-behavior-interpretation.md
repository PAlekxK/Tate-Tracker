---
type: behavioral-interpretation
project: fernwood
artifact_id: mom-behavior-interpretation-2026-07-02
date: 2026-07-02
evidence_level: "⛔️ device→Mom REFUTED 2026-07-28; re-attributed 2026-08-01 — see the banner"
reattributed: 2026-08-01
sources:
  - .user-research/2026-07-02-garden-guru-conversation-analysis.md (real KV turn content + 40-day metrics window)
  - .user-research/persona-mom.md (2026-05-27 telemetry-grounded persona)
  - .user-research/jtbd-2026-05-27.md (Mom's jobs, first telemetry read)
  - .user-research/jtbd-talk-to-the-property.md (Phase E inner job)
  - .user-research/eval-garden-guru.md (standing eval rubric)
purpose: >
  Read Mom's real Garden Guru behavior (through 2026-07-02) as the discovery
  signal we'd been waiting on the interview to give us. Update the persona with
  validated/refuted tags, reconcile the eval rubric's [inferred] signals against
  behavior, and draft a short set of verification questions for the few things
  behavior genuinely can't settle.
---

# Mom's behavior as the transcript — interpretation, rubric reconciliation, verification questions

> # ⛔️ RE-ATTRIBUTED 2026-08-01 — the device this artifact reads as Mom is PAUL
>
> **The caveat below asked for exactly one thing: a Paul-sights-her-phone confirmation.
> It arrived on 2026-07-28 and went the other way.** `tools/people.json` corrected the map
> against *content*: `d-14nyhnjz` is Paul; Mom is `d-szqlt0h7`.
>
> This artifact has now been re-attributed **per conversation**, not waved off. Method:
> `conversation_started` metrics events carry a `deviceId` (the conversation records
> themselves carry `deviceId: null` — **which is why this was never checkable from the
> conversation data alone, and is the root cause of the whole error**). Each of the 25
> conversation records was joined to its start event by timestamp; nearest match ≤12s, and
> the two closest start events in the entire corpus are **51s** apart, so **zero joins are
> ambiguous.**
>
> ### The corpus, 2026-05-01 → 2026-08-01
>
> | | conversations | multi-turn (a real follow-up) |
> |---|---|---|
> | **Paul** (`d-14nyhnjz` + `d-avslqpyd`) | **12** | 7/03 ×3 (incl. an **8-turn**), 7/14 |
> | **Mom** (`d-szqlt0h7`) | **9**, spanning 05-21 → 07-26 | **5/28 (4-turn) and 7/26 (6-turn)** |
> | unattributed | 4 (all 05-20, 19:38–19:41 — four in four minutes, launch-day testing) | — |
>
> ### What that does to this artifact's four findings
>
> 1. **"Adoption is durable — active 27 of ~40 days" → PAUL.** The headline is void as a
>    statement about Mom. Her real cadence is in `persona-mom.md`.
> 2. **"Her Guru questions are the stewardship-lookup the rubric predicted" → SURVIVES, and
>    this artifact had the evidence in hand.** §"Paul-mobile silent failure" logged
>    `d-szqlt0h7` as *"7 conversations, stewardship-voiced"* and filed it as an unresolved
>    **Paul** device. The stewardship voice was read correctly and attached to the wrong
>    person. **Content-reading was the sound instrument here; device attribution was the
>    broken one.**
> 3. **The 5/28 creeping-fig follow-up → CORRECTLY Mom's** (4 turns, joined at Δ7s). The
>    "she was trying to continue and hit a UI wall" reading stands.
> 4. **The 7/02 lily-pad utterance → PAUL's** (07-02T18:24, 2 turns, Δ8s). ⛔️ **This one
>    proposed a NEW JOB for the persona off a single observation.** It is Paul's own
>    utterance. The candidate job is withdrawn; it was never evidence about Mom.
>
> ### And one thing that is now BETTER than this artifact claimed
>
> The anti-persona says Mom *"is not the power-user conversationalist who chains 8
> follow-ups."* Corrected: **the 8-turn conversation in this corpus is Paul's**, and **Mom
> has two genuine multi-turn conversations, not one** — 5/28 (4 turns) and 7/26 (6 turns,
> her longest). The "single follow-up in the entire corpus" framing was an artifact of
> counting Paul's device as hers. She follows up more than this said.
>
> ⚠️ **`turnCount` is a TURN PAIR, not a user turn** — `turnCount: 2` means *one* user turn.
> Every conversation in the corpus is ≥2. Read ≥4 as "she came back."
>
> *Re-attribution is metadata-only (device, timestamp, turn count) — no turn content was
> re-read, per the ingress/quarantine clauses in CLAUDE.md.*


We stopped waiting on the discovery interview because Mom's 40 days of real use
answer most of what the interview was designed to ask. This artifact reads that
behavior, marks what it settles, and isolates the handful of questions only she can
close.

**Device attribution caveat, stated once and carried throughout:** everything below
treats `d-14nyhnjz` as Mom. That is `[inferred, strong]`, not certain — 27 active
days through today, 1,045 events (most of any device), 22 accessibility-toggle events
(the only device that touches the A/A+ control Paul shipped for her no-glasses use),
and a warm possessive question voice ("**our** garden," "**our** Lily pads"). It is
the best read by a wide margin, but a Paul-sights-her-phone confirmation is still the
thing that would make it `[validated]`. The creeping-fig follow-up (5/28, "**our**
journal") is attributed to Mom on the same possessive-voice basis — flagged wherever it
carries weight.

---

## Part A — What Mom's behavior tells us vs. what the personas assumed

### 1. Adoption is durable, not a novelty spike. `[validated]`
The 2026-05-27 persona could only say "27 sessions in 6 days" and left
*Guru-becomes-pattern* as **NOT YET** and the 4-day Guru silence (5/22→5/26) as an
open worry. Forty days later: she's active **27 of ~40 days through today**, and today
she ran a photo-bearing Guru conversation. The novelty-wears-off reading is retired.
The persona's central adoption question — *does she keep opening it?* — is answered
yes, at a horizon long enough to trust.

### 2. Her Guru questions are exactly the stewardship-lookup the rubric predicted. `[validated]`
Read as a demand curve, her questions are overwhelmingly **property-stewardship**
shaped: fertilize timing (rhododendron/mountain laurel), transplant timing (native
azalea), soil amendment (fireplace ash), ID ("what's this purple flower in our
garden?"), and now seasonal diagnosis (lily-pad dieback). None are idle chat. This is
the eval rubric's Q5 wedge — "specifics for fertilizing a given plant" — showing up in
her actual words. What the persona *assumed* about the shape of her Guru job, behavior
now confirms.

### 3. A new job the personas didn't hold: log a seasonal change on a plant she already knows. `[inferred, single-observation]`
Today's lily-pad utterance is three intents in one breath — *capture/log* + *diagnose*
+ *get care advice* — about an **already-known** plant, with a photo:

> "We're seeing some apparent die back of our Lily pads so I attached a photo wanted to
> go ahead and **log that** and see **what could be driving that**… wanted to **log it.
> See what we can do to help the plant** and… have it **populate our field** [notes]."

This is **distinct from the two Guru jobs already in the library**:
- Not Job 3 (identify something I can't name) — she knows it's the lily pads.
- Not Job 5 (promote a *new species* to canon) — lily pads are already known; she wants
  to record a *seasonal observation on an existing plant*, which the current
  photo→suggest-species→promote pipeline does not serve.

It's a **candidate new job**: *"When something changes on a plant I already know, I want
to record what I'm seeing and get help with it in the same breath, so noticing and
logging and asking aren't three separate chores."* Tagged `[inferred,
single-observation]` — it is one utterance from one (probable-Mom) user. Strong, but N=1.
The verification questions below are built to firm it up. It is the cleanest expression
yet of the parent job in `jtbd-talk-to-the-property.md` (collapse the gap between
noticing and knowing) — and it currently **dead-ends**: the observation she asked to log
became Paul's manual `INQUIRIES.md` entry the same day.

### 4. The "she's a one-shot, not a conversationalist" read needs softening — but not deletion. `[contested]`
`persona-mom.md` added an anti-persona line on 2026-05-27: *"not the power-user
conversationalist who chains 8 follow-ups… designing affordances that assume multi-turn
engagement probably misses her."* Behavior now **contests the causal story behind it**.
The single follow-up in the entire corpus (5/28, probable-Mom, "our journal") was Mom
*trying to continue* — to get a plant added. She wasn't one-and-done by disposition
there; she pushed for a second turn and hit a wall. The persona's own open question
("Why all 2-turn conversations? (1) two turns enough vs (2) all she has patience for /
discoverability") gains a **third candidate the analysis argues hardest for: the view
layer dead-ends her after a reply, so continuing is structurally hard, not chosen.**

Important: this does *not* flip her into a power-conversationalist. She still isn't
chaining eight turns, and the low-attention bed/coffee posture is real. What changes is
that "she doesn't follow up" can no longer be read as "she doesn't want to." Behavior
can't separate *didn't want to* from *couldn't find how* — that separation is exactly
verification Q1. Keep the anti-persona line; strip its confident causal claim.

### 5. What behavior does NOT touch.
- The **star** (0 uses in now-many revisits) — no new signal; the 2026-05-27 read stands
  unchanged, not this artifact's focus.
- The **bed/coffee time-of-day posture** — still `[inferred]`; needs time-of-day data or
  her word.

---

## Part B — Reconciling the eval rubric's `[inferred]` signals

Per the charge: noting these, not rewriting the rubric. Three honest categories —
**REFUTED** (a stated conclusion that was wrong), **RISK RETIRED** (a feared silent
failure that did not materialize over 40 days), **VALIDATED** (an inferred win signal now
confirmed).

| Rubric signal (source) | Was | Now | Basis |
|---|---|---|---|
| "5-turn cap is mechanism without need" / no demand for follow-ups (2026-05-26 rollup conclusion) | inferred conclusion | **REFUTED** | The one follow-up ever recorded was substantive (add-a-plant); 15/16 single-turn reflects a dead-ending UI, not satisfied users. Event counts can't tell "didn't want to" from "couldn't"; content + Paul's lived UX say the latter. |
| Mom silent failure: "she opens it once or twice, then quietly stops" | inferred risk | **RISK RETIRED** | 27 active days across a 40-day window, active today. |
| Mom silent failure: "she uses the dashboard but never tries Guru" | inferred risk | **RISK RETIRED** | She uses Guru, with photos, including today. |
| Mom silent failure: "strictly-worse-than-Claude — keeps using Claude for ID, never Guru" | inferred risk | **RISK RETIRED** | Her ID + log + diagnose intent is landing *in Fernwood*, not defecting to Claude. (The wedge still narrows every time Guru can't actually log what she asks it to.) |
| Mom win: "dashboard gets opened regularly" (the load-bearing metric) | inferred win | **VALIDATED** | Sustained daily-ish use over 40 days. |
| Mom win: "when Guru is engaged, the question is the Q5 stewardship-lookup or a close cousin" | inferred win | **VALIDATED** | Her whole question corpus is stewardship-shaped. |
| Paul-mobile silent failure: "Paul stops opening Guru in the field" | inferred risk | **UNRESOLVED — leans concerning** | Paul's mapped devices show little Guru use; the active 2nd iPhone `d-szqlt0h7` (7 conversations, stewardship-voiced, through 6/27) is still the unresolved Reading-A/B device from jtbd-2026-05-27. Not this artifact's charge; flagged so it isn't lost. |

**Net:** the Mom column of the rubric flips decisively green on adoption and
question-shape. The one thing that does *not* resolve — and that the redesign hangs
on — is *why* conversations stay single-turn, and *what she believes happens when she
asks Guru to "log" something*. That is what the questions below are for.

Two rubric items also worth a light touch when Paul next edits the rubric itself (not
done here): the Mom win-signal list and silent-failure list should carry the
RETIRED/VALIDATED marks above, and the anti-persona multi-turn line should be softened
per Part A.4.

---

## Part C — Verification questions for Mom (the key deliverable)

**What these are for.** Behavior settled adoption, question-shape, and demand. It
**cannot** settle four things, all about what's happening *in her head* at the moment of
use. These four map 1:1 to the "still genuinely needs Mom" list in the analysis doc.

**Design rules applied (The Mom Test):** every question asks about a *specific past
moment*, not a hypothetical or a feature idea; none describe the redesign or lead toward
a "yes"; each offers the deflating branch as openly as the confirming one so she can tell
Paul the un-fun answer. Register: warm, plain, research-transparent (she's
research-literate) — Paul's mom, not a usability subject. They work asked
conversationally in any order, or folded into the pending interview.

**Optional warm opener (sets ease, not a data question):**
> "Can I ask you a few quick things about how Garden Guru's been feeling to use lately?
> There are no right answers — I'm just trying to see it through your eyes instead of
> mine."

**Q1 — Did she have a follow-up in mind, or was she done?** *(the single-turn mechanism)*
> "Think back to the last time you asked Garden Guru something and then set your phone
> down. Was that because you had what you needed — or was there something more you wanted
> to ask, and you just weren't sure how?"

*Reads:* "had what I needed" → single-turn is genuinely enough for her mode.
"wanted to ask more but wasn't sure how" → the dead-ending UI is the blocker (confirms
Part A.4 / the rubric REFUTED row directly, from her mouth).

**Q2 — What did she think "log it" did?** *(today's lily-pad; the capture expectation)*
> "The other day you sent it a photo of the lily pads and said you wanted to log it.
> After it wrote back to you — what did you figure happened to that note? Did you picture
> it landing somewhere in Fernwood?"

*Reads:* "I thought it saved to the journal" → she believes an in-app log happened that
didn't (a real expectation gap the redesign must close). "I didn't really think about
it / just wanted the advice" → the logging intent is softer than the utterance suggested.
Either way it grounds the candidate new job (Part A.3) in her actual expectation.

**Q3 — One action or two: telling vs. asking?** *(the log/ask blur — bears on the
no-AI-on-capture rule)*
> "When you sent that lily-pad photo — in your own head, were you *telling* Fernwood
> something you'd noticed, or *asking* it a question? Or did it not really feel like a
> difference?"

*Reads:* "it's all one thing to me" → she experiences capture and ask as a single act,
which collides with the standing "capture path stays AI-free" separation and is a genuine
design fork worth Paul's judgment. "telling is different from asking" → the two-surface
model matches her mental model. Grounded in the specific past act, so it stays Mom-Test-safe.

**Q4 — Has she ever tried to continue — a second photo, one more thing?** *(discoverability
of follow-ups / photos-in-thread)*
> "Has there ever been a time you got an answer and then wanted to send it a second photo,
> or ask one more thing right in the same spot? What happened when you went to do it — or
> did it just not occur to you to try?"

*Reads:* "I tried and couldn't" → affordance is present-but-broken/hidden (surfacing fix,
high priority). "didn't occur to me to try" → she doesn't know multi-turn/second-photo is
possible (discoverability, different fix). Distinguishes the two failure modes the rubric
couldn't.

**Keep it to these four.** They're the whole "needs Mom" set; a fifth would pad. If the
conversation only has room for two, Q1 and Q2 carry the most redesign weight.

---

## Evidence log
- `2026-07-02: [validated] — 2026-07-02 Garden Guru conversation analysis — d-14nyhnjz active 27/~40 days through today; sustained adoption refutes novelty-decay and retires the "opens once or twice then stops" risk.`
- `2026-07-02: [validated] — same — full question corpus is property-stewardship shaped (fertilize/transplant/amend/ID/seasonal-diagnosis); confirms the rubric's Q5 wedge as her real Guru job.`
- `2026-07-02: [inferred, single-observation] — same — today's lily-pad utterance fuses log+diagnose+advise on an already-known plant; candidate new job distinct from Job 3 (ID) and Job 5 (promote species). N=1, probable-Mom. Dead-ended into Paul's manual INQUIRIES.md entry (commit b0d728f).`
- `2026-07-02: [contested] — same — the only 2-turn conversation in the corpus (5/28 creeping-fig, probable-Mom "our journal") was a user trying to continue and hitting a wall; softens the 2026-05-27 anti-persona "multi-turn probably misses her" causal claim.`
- `2026-07-02: [inferred, strong] — same — device→Mom attribution rests on 22 accessibility-toggle events (sole device), 40-day dominance, possessive voice. Not yet Paul-confirmed; confirmation would promote to validated.`
