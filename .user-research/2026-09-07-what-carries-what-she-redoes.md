---
type: research
project: fernwood / frozen-instance catch-up
research_id: what-carries-what-she-redoes
last_updated: 2026-09-07
evidence_level: mixed — per-claim tags below. ⛔ NOBODY HAS BEEN ASKED ANYTHING ABOUT THIS EVENT.
question: "When Mom arrives in her new production household, what of her frozen Fernwood carries silently, what is re-collected from her, what is presented as an invitation, and what stays in the control only?"
performer: the founding contributor (Fernwood's user since May 2026)
sources:
  - "BACKLOG.md § FOCUS FREEZE + § 2026-09-06 FOUR RULINGS (read :60–:262 in full, 2026-09-07) — rulings 1·3·4·5 and rule 6 (the gate)"
  - ".plans/2026-09-06-maps-and-zones-PROPOSAL.md §7 (ruling B) + §9 Challenge 1 & 2 (the durable forms)"
  - ".user-research/2026-09-06-defining-your-place-research.md (names outlive shapes; the 08-30 session)"
  - ".user-research/2026-09-06-what-a-map-is-for.md (the JOIN table; §6.5 the map is an artifact, not a tool)"
  - "../fernwood-private/.user-research/2026-09-04-onboarding-journey.md (the nine stages; the personalization inventory)"
  - ".content/2026-09-06-empty-card-copy.md (the first-open surface's three-line shape and its {source} slot)"
  - ".private/mom-proxy-packet.md (2026-08-12, gitignored — her routed input rendered plain; READ, NEVER QUOTED HERE)"
  - "questions.json (q-top-categories, q-almanac-name prompts + labels) · viewer.html:12772 (sentiment 'landed' = the YES button)"
  - "engine/viewer.template.html STORAGE_KEYS + JOURNAL_NAME (read at HEAD 2026-09-07)"
  - "MOM-CYCLE-MAP.md (the eight legs, the trigger, leg 6c the proxy's hard line)"
  - "memory: feedback_mom_is_a_test_subject_not_the_end_user · feedback_onboarding_is_lap_one_of_the_cycle · feedback_every_ask_says_use_and_reversibility · feedback_release_cascade_persona_paul_mom · feedback_actioning_feedback_is_the_promotion_gate"
commissioned_by: "Paul, 2026-09-07 ~10:20 ET — 'set up a clear and detailed plan with the experts that can be executed when that gate lifts', via the frozen-instance window"
status: PROPOSAL — nothing built, nothing carried, nothing decided. Ends at Paul's gate.
---

# What carries, what she redoes

**Scope.** Research only. This window owns the **frozen** instance; every requirement on the new
product is a handoff, never a design. No canon touched, no tool run, no file edited but this one.

> ⛔ **PRIVACY.** Her verbatim words were read (the 09-06 hold-lift permits it) and are **referenced,
> never reproduced** — this repo is public and the 2026-07-26 quarantine clause stands. Nothing in
> this file may be shown to her.

---

## 0 · THE ANSWER IN ONE LINE, AND THE RULE UNDER IT

Paul already ruled the default, and it is stronger than "migrate carefully":

> `[validated — BACKLOG.md, paul-stated 2026-09-06]` *"We use everything we've done as grounding
> information, but don't prepopulate."* — **What we know informs the design; it does not pre-fill
> her work.**

So **CARRY is not the default and has to earn each row.** But "carry nothing" is not the ruling
either, and reading it that way would throw away eight months of desk research nobody ever asked her
for. The line the record actually draws:

> ⭐⭐ **WHAT CARRIES IS WHAT SHE NEVER GAVE US.**
> Lidar elevation, ERA5 baselines, species profiles, licensed photos, frost dates, the 178 season
> notes — none of it came from her, none of it sits on the answer key, and re-collecting it teaches
> nothing and costs months. **What does not carry is exactly what the control exists to measure: the
> things she said.**

`inferred` — this is a restatement of ruling 5 in a form that is *computable*: for any record, ask
**is there a provenance trail to her?** Yes → answer key → do not pre-fill. No → infrastructure →
carrying it spends nothing.

⚠️ **And the honest limit on that rule: provenance was mostly not kept.** `zones.json` carries
`namedBy`. A folded confirm leaves `confidence: verified` — a *trace* of her that does not name her.
`feedback-log.json` records where a note went, never who sent it. Guru conversation records carry
`deviceId: null` by construction. **So the rule is only executable where somebody wrote provenance
down, and mostly nobody did.** That is the single cheapest test in this file (§1, row T0).

### The five dispositions used below

| | meaning |
|---|---|
| **CARRY** | present in her production household when she arrives; she is not asked for it |
| **INVITE** | present, **labelled as hers**, with *"have we got this right — and is there more?"* |
| **RE-COLLECT** | asked again, with her, in the visit. The old record does not appear |
| **GROUND** | never appears as content; it decides what gets built, asked first, and in what words |
| **CONTROL** | stays on the frozen instance as the answer key |

⛔ **CONTROL is not a fifth option — it is true of every row.** Nothing is deleted from the frozen
side by any disposition here. The column says what *else* happens.

---

## 1 · DISPOSITION BY DATA FAMILY

Volumes are measured where marked; `[R]` is the main session's 2026-09-07 KV read, quoted not
re-derived.

| # | family | what is actually there | disposition hypothesis | tag | cheapest test that moves it |
|---|---|---|---|---|---|
| **T0** | *(precondition)* **provenance itself** | `namedBy` on zones; nothing equivalent on plants, vehicles, notes or conversations | — | `validated` (read at HEAD) | ⭐ **grep the canon for any her-attributable field.** If the count is ~1 (zones), then §0's rule cannot be executed mechanically and every row below is a **judgement per record**, not a filter. 10 minutes, and it re-prices the whole catch-up |
| **T1** | **her confirm answers** (`feedback:*`, 10 day-buckets `[R]`; the 08-12 packet renders 9 records — 2 self-identify as Paul's verification, 5 are confirm taps, 2 are free-text) | 3 are plant facts (crocosmia cultivar · the white mophead · a bloom window); **2 are structural and much bigger than they look** — see T1a/T1b | **split** | `validated` (her taps, her device, `sentiment: "landed"` = the YES button, `viewer.html:12772`) | for the 3 plant facts: **ask her one of them again in the visit.** If she gives the same answer, re-collection is cheap and the control gains a second reading; if she hesitates, INVITE is the right shape and CARRY is not |
| **T1a** | ⭐⭐ **`q-top-categories`, answered 2026-08-03, YES = "That's all of them"** — the prompt names *vehicles · equipment · house systems · gardening · wildlife* and asks whether the list is complete | **the module manifest is HER ANSWER, confirmed** | ⭐ **CARRY (already carried, invisibly and correctly) + GROUND** | `validated` — her tap on a prompt whose text is in `questions.json:122` | none needed to carry it. ⭐ The test is the *comparison*: her onboarding **ranking** vs this **completeness** answer. Ranking a list she authored is a new question over her own list — **that is the right relationship and it is not a re-ask** |
| **T1b** | ⭐⭐ **`q-almanac-name`, answered 2026-07-29, YES = "Yes, Journal"** — she was asked whether *"Journal"* fit better than *"The Almanac"*, and said yes | her word for the record is **Journal** | **CARRY her word** | `validated` (tap + label + `resolvedAt: 2026-07-29`) | ⛔ **and it is currently contradicted.** `engine/viewer.template.html` sets `JOURNAL_NAME = <household> + " Almanac"`, commented *"(mom seat, round 3)"* — **a synthetic seat's preference is in the production build where her answered one is not.** One grep settles it; it is the other window's line to change (§handoffs) |
| **T2** | **her free-text notes** (2 in the packet, both about the **rainfall** surface — one saying the 7-day figure is not believable, one asking for day-by-day granularity) | these are **app-behaviour corrections**, not facts about the place | ⭐ **GROUND only — build the fix; carry no record** | `validated` (her words, her device; the 14× under-read was independently confirmed) | ⛔ **none — this row is already settled and it is the cleanest case in the file.** The visible form of actioning it is *the rainfall card being right on day one*, never a note reappearing. If it reappears as content, the surveillance read fires for zero benefit |
| **T3** | **Guru conversations** (35 `conversation:*` `[R]`; authorship mixed and asserted by content only) | mostly *questions she asked* (fertilising, moving an azalea, creeping fig, sarracenias, fireplace ash) — **a lookup history, not a record of the place**. A handful produced canon (Spiderwort, Pop Star, Lizard's Tail) | **GROUND + CONTROL.** ⛔ Do **not** carry the transcripts | `inferred` (authorship by content; `deviceId: null` on the records themselves) | ⭐ **count how many of the 35 produced a canon fact vs asked a question.** If the ratio is what it looks like (~3 of 35), Guru's carry value is *the three facts*, which arrive via T7, and the other 32 are a browsing history nobody should ever be shown their own copy of |
| **T3a** | ⭐ **the refused capture** — a long motor-pool log (a bike rebuild, in detail) that Guru declined, telling the author to *"keep a separate log"* | content that was **offered and turned away**; it exists in no canon file | **GROUND — it is the reason motor-pool and equipment are modules at all** | `validated` (the refusal is in the record, verbatim) | none. ⭐ It is the strongest single argument that the new build's module set is right, and it costs nothing to carry as a *design fact* |
| **T4** | **zone recordings** (3 `zone-audio:*` + 6 `zone-audio-blob:*` `[R]`) | her voice, and the only family where **the artifact is her and the text is a model read** | **CONTROL + GROUND.** ⛔ Never carry a transcript as content | `assumption` on content (bodies not opened; transcripts are `[transcript-UNVERIFIED]` by standing rule) | ⭐ **listen to the three, per record, before the gate.** `check-arrival-dispositions.py` says a batch cannot be cleared by one member. If any is hers and unheard, that is an unpaid debt sitting *behind* the Z-ACK debt |
| **T5** | **observations** (`observations` + `est-3c9f1a:observations`) | sightings, dated, place-shaped: a bear with cubs, a skink, spring peepers, a golf-cart drain plug | ⭐ **the one family where CARRY is genuinely arguable** — a dated sighting is a fact about the place that cannot be re-collected (you cannot re-see a bear in May) | `inferred` | **ask Paul one question: is the observation log part of "her work" or part of "the place's history"?** If the latter, it carries; nothing else in the file turns on it |
| **T6** | ⭐⭐ **zones + her 16 spoken names** (23 zones, all `status: draft`, 16 `namedBy` her, 7 Paul's) | the answer key itself | ⛔ **RE-COLLECT (ruled) + CONTROL.** The map arrives empty; the 16 names stay sealed | `validated` (read at HEAD 09-06) — and the disposition is `[validated — paul-stated 2026-09-06 ruling 5]`, not my proposal | ⭐ **the joint session IS the test.** Count the names she produces on a blank map against 16, and count the overlap. That is the whole reason the control is being kept — **and showing her the 16 first destroys the measurement irreversibly** |
| **T7** | **canon built with her** (`plants.json` 36 records · `vehicles.json` · 64 wildlife records) | overwhelmingly desk research + Paul's authoring; her contribution is ~4 confirmations, 2 promotions and one addition | ⭐ **CARRY the records; RE-COLLECT nothing; INVITE only the ~4 she settled — if at all** | `inferred` | ⭐ **the T0 grep is this row's test too.** If her fingerprints on canon are countable on one hand, the "don't prepopulate" ruling barely touches canon, and the cost of treating canon as hers is four re-asks against months of re-derivation |
| **T8** | **browser-local state** (19 `tateTracker.*` keys in `STORAGE_KEYS` at HEAD, + 8 `fw-*` in `onboarding/` and `estate/`) | ⛔ **storage is per ORIGIN. None of it crosses.** `deviceId` cannot migrate (C4 2d) | ⛔ **CARRY IS IMPOSSIBLE — this row is a loss list, not a decision** | `validated` (read at HEAD) | see T8a/T8b — two of these are the highest-value deterministic pre-checks in the whole event |
| **T8a** | ⭐ **her A+ text size** (`tateTracker.textSize`, and `text_size_served` = `lg` in 8 of 8 reports over 60 days, **0 of 37 toggle firings**) | the key does not cross the origin; the new origin serves from instance config | **must be served by config on day one** | `validated` (telemetry, one device) | ⭐⭐ **load the production household at 414×848 on a real device and read `text_size_served`.** If it is not `lg`, she reads a smaller app forever — she has never fired the toggle in 37 opportunities and will not start now. **Config is not evidence; verify by use** |
| **T8b** | ⛔ **the unflushed outbox** (`feedbackOutbox.v1`, `door.outbox.v1`, four `momQueue.*`) | ⭐ **these exist NOWHERE but her phone until they flush** (`viewer.html:11552`, held until a 2xx) | **drain before anything is rotated or disabled** | `validated` (code read; already the ruling-3 sunset order) | ⭐ **one online tap on her device during the visit.** If she wrote a note somewhere with no Wi-Fi — which the site's premise makes likely — **rotating the token first is a silent deletion of her words**, and nothing anywhere would show it |
| **T8c** | **device pairing** (`sync.v1`, `deviceId`) | replaced by the grant, by design | **abandon** | `validated` | ⚠️ **not a defect but a measurement warning:** the new origin starts a **new browser bucket**, so every "since the last lap" engagement figure breaks at the seam. ⛔ **Do not pool pre- and post-migration telemetry** — the same rule already written for 2026-07-30 |

### 1.1 Where the module changes the answer

Most rows above are module-invariant. These six are where it bites:

| module | what changes | disposition | tag |
|---|---|---|---|
| **place** | the whole module *is* the answer key | ⛔ **RE-COLLECT, ruled.** Blank map, built together | `validated` (paul-stated) |
| **garden** | the deepest canon and the thinnest her-fingerprint (~4 records of 36) | **CARRY the canon.** ⚠️ If ruling 5 is read as covering canon, this module is the most expensive place to apply it — say so before applying it | `inferred` |
| **house-systems** | ⭐ **her coinage is the module's name, and there is almost no content behind it** | **CARRY the word** (already the engine's); **RE-COLLECT the content — because there is none.** Nothing to lose, everything to gain | `validated` on the coinage; `validated` on the emptiness (no place field, no cards, `check-domains` prints it every run) |
| **motor-pool** | the one undispositioned arrival is here (`ask-next-motor-pool`, 2026-09-06 10:28 PM `[R]`); Track B work is partially unfrozen | **CARRY the records** (they were never hers); **INVITE the one open item** | `inferred` |
| **equipment** | its existence traces to a capture Guru refused (T3a) | **CARRY records; GROUND the refusal** | `validated` on the refusal |
| **wildlife** | 64 records, no markers, no place field; her share is a photo ID or two | **CARRY.** ⛔ Species do not get a place (a place-tag on a species asserts a territory nobody surveyed) — the sighting is the honest unit, and that is T5 | `inferred`, carried from `what-a-map-is-for` §4 |

⛔ **No module is ranked here.** Ordering is Paul's; the only structural dependency worth naming is
the one already on the record: **place is a join for nine domains**, so a blank map delays every
"where is it" question in every other module. That is a consequence of the ruling, not an argument
against it.

---

## 2 · HER DAY ONE

⛔ **Read every emotion below as `assumption`.** It is my model of her, calibrated on four months of
her behaviour. **Nobody has watched anyone do this, and she has not been asked.**

⚠️ **One thing must be settled before this journey can be drawn properly.** `[validated — BACKLOG]`
Ruling 3 (09-06) makes the transition a **guided visit in person**; the 09-07 gate is worded as
*"her getting her link to set up in prod."* Those are compatible (a link handed over in the room) and
they are also the difference between **an observer present** and **an observer absent** — which the
09-04 journey already measured as the single largest instrumentation loss available. The sketch below
assumes **Paul is in the room**, per the later ruling. §R3.

### 2.1 The shape of the day

| # | moment | what she expects | what she meets | risk |
|---|---|---|---|---|
| 1 | Paul opens it | *"he's showing me something"* | a person, not a product | — |
| 2 | the door | *"do what he asked"* | the first moment in four months where she can be **wrong** | her named fear, exactly |
| 3 | naming herself, naming the place | *"that's easy"* | ⭐ the peak — the one act she has demonstrably initiated | reads as a form → −1; reads as a question → +1 |
| 4 | ranking what matters | *"I already told you this"* | a list **she authored** (T1a), in a new order | ⚠️ see **RE-ASK**, below |
| 5 | **first open** | *"there it is"* | six cards saying *nothing here yet* | ⚠️ see **AMNESIA** |
| 6 | **the map** | *"there's our place"* | ⛔ **blank ground she traced eight days ago** | ⚠️ see **LOSS** |
| 7 | the next morning | *"open it like always"* | the icon question, which nobody can solve for her | invisible if it fails |

### 2.2 The four ways this goes wrong, in the order they are likely

**⚠️ LOSS — "my zones are gone."** `assumption` on the feeling; `validated` that the condition
exists. This one is **structurally guaranteed** by ruling 5: same land, same person, blank map, eight
days after she named sixteen places on it. And the reassurance — *we kept the old one* — is a claim
**she cannot check**, because the sunset revokes her access to the origin that holds it.

> ⭐ **The cheapest thing in this entire file, and it belongs to this window:** produce a **viewable
> rendering of her frozen map** — a static image or PDF of the 23 zones with her 16 names on them —
> that Paul can hold up. It costs an afternoon, it makes *"we kept it"* true in a form she can see,
> and **it is the Z-ACK acknowledgment in the most attributive form the ribbon doctrine could ask
> for.** ⛔ **But it collides head-on with the answer-key measurement** (§T6): showing her the names
> before she re-produces them destroys the comparison. **The two cannot both happen first.** §R2/R4.

**⚠️ SURVEILLANCE — "how does it know what I said in July."** `assumption`. This fires on exactly one
condition: **a fact appears that she did not put there in this session and cannot trace.** Which
gives the operative rule, and it is asymmetric:

> ⭐ **Carrying INFRASTRUCTURE silently reads as competence. Carrying HER MATERIAL silently reads as
> surveillance.** Frost dates, soil series and species profiles may arrive unannounced. **Anything
> with a provenance trail to her arrives labelled, or it does not arrive.**

Two consequences, both already doctrine here wearing a new hat: the *who sees it* half of the
every-ask rule is the half people actually worry about; and `declarePerson`'s guard against
**retro-attributing** records written before her person record existed must not be weakened for this
migration — a new name silently claiming four months of old notes is the purest form of this failure.

**⚠️ DEBT — "you have 60 unanswered items."** `validated` that the material exists: **81 arrivals, 63
batch-cleared by watermark and never individually attested, 17 dispositioned, 1–2 open.** ⛔ **No
count of her outstanding items may render anywhere** — not a badge, not a queue, not a zero. Under
the 09-05 ruling onboarding is lap 1 and personalization is **invitation, never obligation**, and the
ribbon is **attribution, not information.**

> ⭐ **The reframe that makes this safe: the 63 are OUR debt, not hers.** She does not owe answers;
> we owe her things being right. The visible form of the catch-up is **surfaces that are correct on
> day one** — the rainfall card that reads believably (T2) — and never a list of what she still owes.

**⚠️ RE-ASK — "I already told you that."** `inferred`, and it is the risk the record most supports.
The funnel is total: **0 of 35 on every affordance that asks her; 5 of 5 on the one that moves her.**
A day one that is a stack of asks is the same failure at a new origin. ⭐ The mitigation is not
copy — it is **who asks**: the questions happen in the conversation, and the app receives the result
(§4). And where a question genuinely was settled (T1a, T1b), **it must not be asked again at all.**

**⚠️ And a fifth, which is the one the empty-card copy creates.** `inferred` — the shipped shape
traces line 2 to *"You put Gardening first, so this is where we start."* That is **true of the
onboarding ranking and thin against four months.** For a stranger household it is a warm, honest
line. For *her*, on the same land, it credits the last ten minutes and is silent about the year.
**Call it AMNESIA and hand it to the other window as a requirement, not a copy note** (§handoffs).

---

## 3 · WHAT IS HERS vs WHAT IS THE JOB'S

`memory: feedback_mom_is_a_test_subject_not_the_end_user` — over-indexing on her is
instance-leaking-into-engine. Sorted, deliberately, into two lists.

### 3.1 Generalizes — any household moving an old record into a new one

1. ⭐ **The carry line is authorship, not format.** Carry what the person never gave you; re-collect
   what they authored. It is executable only where provenance was written down — **so write it down
   from the first record.** `inferred`
2. ⭐ **Silent carry is asymmetric.** Infrastructure silent = competent. Personal silent =
   surveillance. `assumption`, but it follows directly from the every-ask rule and is cheap to honour.
3. ⛔ **Never render a count of what the person has not answered.** A queue length is a debt display.
   `validated` as doctrine here; `inferred` as a general claim.
4. ⭐ **"We kept your old one" is unfalsifiable to the person unless you can show it.** A migration
   that revokes access to the old record must produce a viewable artifact or stop making the promise.
   `inferred`
5. ⛔ **An old record used to pre-fill is an old record spent.** Its comparison value and its
   convenience value are **mutually exclusive**, and the choice is made silently and irreversibly the
   first time you pre-fill. `inferred` — and this is the general form of ruling 5.
6. ⚠️ **Browser-local state does not cross an origin.** Anything living only there is lost at the
   move, and the person experiences it as *the app forgot me*. Roster it, drain it, or lose it.
   `validated` (mechanism).
7. ⚠️ **Telemetry does not survive the seam.** A new origin is a new bucket. Every before/after
   comparison across a migration is a different instrument, not a trend. `validated`.
8. ⭐ **A structural contribution and a content contribution move differently.** The person's
   *vocabulary* and *categories* should carry invisibly (they are the product's language now); their
   *records* should not. `inferred` — T1a and T1b are the worked examples.

### 3.2 Mom-specific — instance facts, do not promote to engine defaults

- A+ (`lg`) served on 8 of 8 reports; **0 of 37** toggle firings; 414×848 across 51 batches.
- 0-for-35 on ask-shaped affordances, 5-for-5 on the jump strip, **depth 2 and depth 3 both zero**
  (she reads card faces and does not open individuals). ⚠️ *One device; a deviceId is a browser
  bucket, not a person.*
- ~0.55 sessions/day; reading is difficult; her **documented fear is getting things wrong**.
- She coined *"household systems"*, named the record *"Journal"*, and confirmed the module list is
  complete. **Naming is the act she initiates.**
- 16 names at a kitchen table in one evening against 0 taps in 10 in-app offers.
- ⚠️ **Her administrator is her son.** A family arrangement. Elsewhere, an administrator reading a
  household's notes and voice needs **explicit agreement before the first contributor input**.
- Two icons will exist on her home screen; nobody has ever looked at her home screen.
- The Z-ACK debt is a **specific, dated, unacknowledged contribution** — not a general pattern.

> ⛔ **The discipline this list exists to enforce:** *the map arrives empty* is a **ruling for this
> event**, justified by a control and an answer key. **For a household with no prior record there is
> no control, no answer key and no measurement — blank-slate there is just an empty app.** Do not
> promote it to a product principle without saying which half you mean.

---

## 4 · THE APP IS THE RECORD, NOT THE CHANNEL — and what that costs

`[validated — .plans/2026-09-06-maps-and-zones-PROPOSAL.md §7 ruling B + §9 Challenge 2]`
Paul's recommendation on the table: **her words, your transcription.** And the measurement behind it
is not close: **0 for 35 in the app; 16 names in one evening at a table with a photograph and a
second person in the room** — which is also the only arrangement the site's own no-signal premise
permits.

**So for the catch-up: the app is the RECORD. The conversation is the channel.** Three consequences,
and only the third is a build.

1. ⭐ **The catch-up conversation is Paul's, in the room, over the frozen material.** Not a card
   queue, not a ribbon, not an in-app review flow. Every item in §1 marked RE-COLLECT or INVITE is a
   question asked out loud.
2. ⛔ **The AI boundary's INGRESS and QUARANTINE clauses are untouched.** *Paul relays; the model does
   not fetch.* Her account of her own uncertainty stays in `.private/`. A whisper transcript is a
   **model read** — it may support a disposition and may never promote anything to canon on its own.
3. ⭐⭐ **The one build this window asks for: a relayed-capture path that mints an arrival record.**
   Paul-relayed input already *counts* by doctrine — but **`Z-ACK` records that her largest single
   contribution has no arrival record at all: no id, no timestamp, no channel, because it happened on
   paper at a kitchen table.** If the catch-up runs through the same hole, it is invisible to every
   check in the loop, it cannot be dispositioned per record, and in six weeks nobody will be able to
   say what was carried or why. **Deterministic, AI-free, provenance-bearing: who said it, when,
   where, transcribed by whom, `via: relayed`.** §R5.

⚠️ **The cost of ruling B, stated plainly so it is chosen rather than drifted into:** if the app is
the record and not the channel, then **the app's own ask surfaces stop being the thing to fix**, and
the 0-for-35 finding stops being a defect and becomes a design fact. That may be right. It is also
the kind of conclusion that quietly retires a whole workstream, so it should be ruled, not inherited.

---

## 5 · WHAT TO OBSERVE AT GATE-LIFT — falsifiers for week 1

Instruments that exist: `read-onboarding.py` (real · synthetic · unknown), the door events
(`door_reached` / `door_opened` / `door_failed`, `POST /api/door` live), `read-mom-engagement.py`,
per-device metrics, `text_size_served`. **Pre-registered before the gate lifts, so the reading is not
chosen afterwards.**

| # | hypothesis | falsifier | instrument | exists? |
|---|---|---|---|---|
| **H1** | ⭐ Re-collection is experienced as *continuing*, not starting over | she asks why she is doing this again, or produces materially fewer than 16 names on the blank map | the joint session itself; Paul's report | ⛔ human only — **and it is the answer-key measurement, so it must be recorded the day it happens or it is gone** |
| **H2** | The 0-for-35 pattern is about **cards**, not about her | she taps ≥1 in-app ask, unprompted, in week 1 | offered → taken at the new origin | ⚠️ **only if the offer denominator is logged.** An untracked offer makes a zero unreadable — the exact contamination that made the zone launcher's zero uninterpretable |
| **H3** | Nothing that carried reads as surveillance | she asks how it knows something | ⛔ **nothing. Paul's ears.** | 🔴 **name this gap rather than pretending it is covered** |
| **H4** | No debt is displayed | any rendered count of outstanding/unanswered/pending items, anywhere | ⭐ **deterministic — grep the first-open surface before she sees it** | ✅ and it should run **before**, not after |
| **H5** | A+ carries to the new origin | `text_size_served` ≠ `lg` on her first production session | one real load at 414×848 | ✅ **cheapest high-value check in the event** (T8a) |
| **H6** | She returns on day 2 without help | zero sessions at the new origin on day+1, **or any session at the frozen origin after the visit** | both origins read for the same window | 🔴 **no tool reads both.** The most likely failure is invisible at the new origin alone |
| **H7** | Her onboarding ranking agrees with her 08-03 answer | the modules she ranks contradict the list she confirmed complete | `read-onboarding.py` real rows vs `q-top-categories` | ✅ ⭐ **and this is the first chance ever to compare a card answer against a conversation answer from the same person** |
| **H8** | Nothing of hers was silently deleted at the sunset | any `feedbackOutbox` / `door.outbox` / `momQueue.*` content on her phone at lockout time | one online tap during the visit, **before** the token rotates | ✅ mechanism exists; ⛔ **ordering is the whole protection** |

⛔ **What none of these measures: whether she felt heard.** `momack_shown` counts exposure, not
receipt. That gap is real, it is already named in the loop's own clean-lap definition, and it must
not be papered over with a process number.

---

## ⛔ PAUL MUST RULE

Ordered. Everything above is a hypothesis until these land.

```
R1 · Does "don't prepopulate" cover only the MAP, or the whole record?
     Ruling 5 was stated about zones. Read narrowly, canon carries and §1 stands as written.
     Read broadly, plants.json / vehicles.json / 64 wildlife records arrive empty too.
     recommend: NARROW — the ruling's own justification is the answer key, and the answer key
       is the map. Applying it to desk research re-derives months and measures nothing.
     blocks: every row in §1. This is the fork.

R2 · Is the answer-key comparison a measurement you actually intend to take?
     If YES: nothing she authored may be shown to her before she re-produces it — including the
       16 names — and the comparison must be recorded the day the joint session happens.
     If NO: the control's convenience value is available, INVITE becomes usable, and the
       cheapest discharge of Z-ACK (showing her the map) opens up.
     ⛔ These are mutually exclusive and the choice is made irreversibly the first time
       something is shown or pre-filled.

R3 · Day one — GUIDED VISIT (09-06 ruling 3) or LINK (09-07 gate wording)?
     They are compatible in practice and opposite in instrumentation: the visit puts an observer
       at the four stages that otherwise produce ambiguous silence.
     recommend: say which, in the register, before the gate is called.

R4 · Z-ACK — what form does the acknowledgment take, now that she never sees the 23 zones?
     options: a) building the map together in person IS the acknowledgment (state it, and close
                 the debt on the record)
            | b) a viewable rendering of her frozen map, shown to her — cheap, true, attributive,
                 and it spends R2's measurement
            | c) after the joint session: show the old map beside the new one — ⭐ discharges the
                 debt AND preserves the measurement, because the comparison is already taken
     recommend: (c). It is the only option that does not trade one against the other.

R5 · Does the catch-up get a relayed-capture path with an arrival record before the gate lifts?
     Without it the catch-up repeats Z-ACK's own defect: her largest contribution has no id, no
       timestamp and no channel, so no check in the loop can see it and no disposition can be
       attested per record.
     recommend: yes, and it is small — deterministic, AI-free, provenance-bearing.
```

⚠️ **One register discrepancy, flagged not resolved:** the brief that commissioned this file said
Mom's channel is HELD, metadata only. `BACKLOG.md` ruling 4 (09-06) says the hold is **lifted fully**.
The register is newer and Paul's words are in it, so I worked from the register — *a ruling that is
not in the register is not in force* cuts both ways. **If the brief was right and the register is
stale, say so, because I read her material.**

---

## Handoffs to the OTHER window — requirements only

Stated as capabilities the production surface must have. **Nothing here is a design.**

1. ⭐ **Serve A+ on her first real load.** `text_size_served` must read `lg` at 414×848 **verified by
   use**, not by reading config. Her `tateTracker.textSize` does not cross the origin and she has
   never fired the toggle in 37 opportunities.
2. ⛔ **No surface may render a count of her outstanding, unanswered or pending items** — including
   a badge and including zero.
3. ⭐ **Anything arriving in her household with a provenance trail to her must be able to render its
   source** (*"you told us this, in August"*) — **or it must not arrive.** Silent carry is reserved
   for material she never gave us.
4. ⭐ **The first-open surface needs a `{source}` variant that traces to something other than the
   onboarding ranking** — a *carried* provenance — or Paul accepts that day one credits only the last
   ten minutes (§2.2 AMNESIA).
5. ⛔ **`JOURNAL_NAME` currently resolves to `<household> + " Almanac"`, commented *(mom seat, round
   3)*, while her own answered preference (2026-07-29, folded) is **"Journal"**.** A synthetic seat's
   preference is standing where a validated one is not. **Your line, your call — but it should be a
   decision, not a leftover.**
6. **The map's empty state must be first-class** — not an error, not a to-do — and **a named place
   with no geometry must render** (the 2026-07-17 defect where empty-geometry zones did not render at
   all is the failure mode this repeats).
7. ⛔ **`declarePerson`'s retro-attribution guard stays.** A person record must not claim records
   written before it existed.
8. **Onboarding must emit enough to answer "where did she stop"** — or Paul accepts that a stall is
   invisible. `door_reached` and `door_opened` cover 2 of 9 stages today.
9. **Both origins readable for the same window in week 1** (H6). No tool does this today.

---

## What I declined

- **To design anything on the production side** — onboarding screens, the first-open surface, the
  map, the door, tenancy, or any copy. That window owns it; the list above is requirements.
- **To rank the modules.** Method, not content — ordering is Paul's. The only structural note is that
  place is a join for nine domains.
- **To let a synthetic user stand in for her.** No proxy read was run and none is reported. The
  mom-proxy seat's own hard line applies: *it is a proxy, not her.*
- **To quote her.** Her material was read; nothing verbatim appears here or in any tracked file.
- **To state any disposition as decided.** Every row in §1 is a hypothesis with a test.
- **To claim she will feel loss, surveillance or debt.** Those are `assumption`, and the conditions
  that would produce them are what is `validated`, not the feelings.
- **To re-take the archive or touch the frozen instance.** Post-gate by ruling 6; not mine regardless.

---

## Evidence log

- `2026-09-06: [validated] — BACKLOG.md, paul-stated — ruling 5: the map arrives empty; zones do not migrate; "what we know informs the design, it does not pre-fill her work." Ruling 1: the frozen instance is a deliberate DATA CONTROL and the 23 zones are an ANSWER KEY. Ruling 3: the transition is a GUIDED VISIT. Ruling 4: the hold on her feedback is lifted fully; every action lands on the new instance, never the control.`
- `2026-09-06: [validated] — BACKLOG.md census, metadata — 81 arrivals · 17 individually dispositioned · 63 batch-cleared by watermark and never individually attested · 1 undispositioned. The 63 is the real number: most of her feedback was never held or read — it was swept.`
- `2026-08-03: [validated] — her tap, her device — q-top-categories answered YES ("That's all of them") on a prompt naming vehicles · equipment · house systems · gardening · wildlife. THE MODULE MANIFEST IS HER CONFIRMED ANSWER. Prompt text: questions.json:122. sentiment "landed" = the YES button: viewer.html:12772.`
- `2026-07-29: [validated] — same instrument — q-almanac-name answered YES ("Yes, Journal"), resolvedAt 2026-07-29. ⚠️ engine/viewer.template.html sets JOURNAL_NAME = <household> + " Almanac", commented "(mom seat, round 3)" — a SYNTHETIC seat's preference where her validated one is not.`
- `2026-07-26 / 2026-07-29: [validated] — her free-text notes, both about the rainfall surface (disbelief in the 7-day figure; a request for day-by-day granularity). App-behaviour corrections, not facts about the place. The 14× under-read was independently confirmed.`
- `2026-07-03: [validated] — the record's own text — Garden Guru REFUSED a detailed motor-pool log and told the author to keep a separate log. Content offered and turned away; it exists in no canon file. It is the strongest single argument that motor-pool and equipment belong as modules.`
- `2026-08-30 → 2026-09-06: [validated] — 23 zones at HEAD, all status:draft, 16 namedBy her, 7 by Paul; produced at a kitchen table over an aerial photograph, in one evening, with zero geometry.`
- `lap 8: [validated] (telemetry, ONE device) — every ask-shaped affordance 0 of 10 · 0 of 10 · 0 of 10 · 0 of 5; the jump strip 5 of 5; depth 2 and depth 3 both zero. ⚠️ A deviceId is a browser bucket, not a person.`
- `2026-09-01 / 2026-08-24: [validated] — text_size_served reads lg in 8 of 8 reports over 60 days; 0 of 37 toggle firings; 414×848 across 51 metric batches.`
- `2026-09-07: [validated] (read at HEAD) — 19 keys in engine/viewer.template.html's STORAGE_KEYS (against "18 rostered" recorded 2026-09-03; doorOutbox is dated 09-03/C6 2b, so the delta is plausibly a legitimate extension — worth one run of check-storage-keys.py, not a defect claim). Storage is per ORIGIN; deviceId cannot migrate; feedbackOutbox/door.outbox are held until a 2xx and exist nowhere else until they flush.`
- `2026-09-07: [R] — main session's live KV read of est-3c9f1a: 177 keys vs 175 archived · 0 changed · 2 gone (TTL-expired ambient cache) · 4 added. The archive is one feedback arrival behind and nothing re-takes it.`
- `2026-09-07: [assumption] — every emotion, every risk name (LOSS · SURVEILLANCE · DEBT · RE-ASK · AMNESIA), and every claim about how she will experience day one. The CONDITIONS that would produce them are validated; the reactions are a model of her and are not her account.`
- `Open, unobserved: whether an onboarding step reads to her as a card or as a conversation (the seam this whole event turns on, never tested) · whether re-collection reads as continuing or as starting over · what is on her home screen · whether any of the three zone recordings is hers and unheard.`
