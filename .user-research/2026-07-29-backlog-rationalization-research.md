---
type: audit
project: fernwood
artifact_id: backlog-rationalization-user-research-2026-07-29
date: 2026-07-29
last_updated: 2026-07-29
lens: user-research (one seat of the 2026-07-29 rationalization panel)
evidence_level: mixed — every claim carries its own tag
performer: .user-research/persona-mom.md (⚠️ see §3 — that file is partly contaminated)
sources:
  - .plans/2026-07-29-rationalization-brief.md (the shared brief + the orienting principle)
  - BACKLOG.md TOP ITEM / A1 / A2 / A3 / A4 / A6 / B6 / Track C (read 2026-07-29)
  - CLAUDE.md — Mama's Perspective, the channel doctrine, the AI boundary, the taxonomy rule
  - questions.json, feedback-log.json, tools/people.json, tools/momlib.py, tools/check-mom-ack.py,
    plants.json (moss record), viewer.html 9351–9765 (read directly, 2026-07-29)
  - ~/.claude/skills/mom-cycle/SKILL.md (the one-card-per-cycle rule + Refinement log runs 0–1)
  - .user-research/2026-07-26-feedback-loop-audit.md · persona-mom.md ·
    2026-07-02-mom-behavior-interpretation.md · 2026-07-02-garden-guru-conversation-analysis.md ·
    jtbd-2026-05-27.md · .plans/2026-07-16-mental-model-elicitation-brief.md
  - .private/mom-feedback-2026-07-26.md — REFERENCED BY POINTER ONLY, never read into this file
privacy: >
  PUBLIC REPO. Mom's words about herself are referenced by pointer only and never quoted.
  Her words about the APP are quoted only where BACKLOG.md / questions.json already publish them.
---

# Fernwood backlog rationalization — the user-research lens

## If Paul reads six lines

1. **The "1 answered of 35 offered" funnel is the wrong person's denominator and it is still being
   quoted in four live artifacts.** On the corrected attribution the number is **~10 offered → 4
   answered**. `[validated — tools/people.json, BACKLOG A1 corrected read, questions.json resolutions]`
   Almost every downstream conclusion about her was sized against the wrong ratio.
2. **The moss card is no longer a discriminating instrument, and the experiment it was designed to
   run has already been run.** `q-almanac-name` — zero wrongness risk, seeded from her own words —
   was **answered in under a day** (7/29 08:54 ET). Meanwhile `q-strategy-pollinators` — *also* zero
   wrongness risk, but **our** topic — has sat unanswered for **15 days**. `[inferred, strong]`
3. **That pair flips the ranking of the two hypotheses.** On corrected data, **authorship (topic
   origin) fits better than wrongness-risk**, because wrongness-risk predicts pollinators gets
   answered and it didn't. Do not build the next quarter on the fear reading.
4. **Sequencing verdict: the moss card does NOT go out. Not now, not after the cleanup.** Ship the
   moss **record** as a return leg (it already exists in `plants.json` and she has never been shown
   it). The one-card budget goes to a real discriminator — see the ranked queue in §1·A.
5. **`persona-mom.md`'s entire telemetry tier is Paul's device.** Including the claim that behaviour
   validated her reading difficulty: **she has fired the A/A+ text-size toggle zero times.** That
   changes W8·b — optimise the *default* type scale, not `body.text-lg`. `[validated — code read]`
6. **R4 is stale: receipt is no longer unmeasurable.** `momack_followed` and `momack_acknowledged`
   shipped and `momack_followed` **fired from her device on 7/28**. That is the first behavioural
   receipt this project has ever had, and the A1 table still says it can't exist. `[validated]`

---

# 1 · Tiered findings

Tier is defined by **what unblocks it** (brief §THE AXIS). Effort is S/M/L. Every Tier-3 row carries
① the exact question and ② the capture path, or it is on the kill list instead.

## 1·A ⭐ THE ONE-AT-A-TIME ASK QUEUE — the primary deliverable

The binding constraints: **app-only channel** (text is not a channel; Paul may relay) · **card
wording is human-confirmed before it ships** · **at most ONE clarifying card per `/mom-cycle`**.
So this is not a list of twenty questions. It is a **sequence**, and each entry says what it buys and
what it costs to run it now.

Ranked by *what it unblocks*, not by how nice it is.

| # | Ask | Class | Topic origin | The exact question | Capture path | What it unblocks | Tier · effort |
|---|---|---|---|---|---|---|---|
| **0 — IN FLIGHT. Nothing else ships until this clears.** | `q-top-categories` | preference / expertise | **hers** (in-person, relayed 7/29) | *Live text, already Paul-approved:* "You mentioned wanting the big categories across the top — **vehicles**, **equipment**, **house systems**, **gardening**, **wildlife**. Is that the whole list, or is something missing? Once we know, we can lay the app out so each one is easy to reach." | Confirm card → `POST /api/feedback` (yes/no + `correctionPrompt` free text) → `read-mom-feedback.py --pickup`. ⚠️ Reflective/unprobeable — **it will hold the watermark until hand-retired** (`active:false` + `resolvedAt`). Pre-schedule the retire. | **W8·a** (the IA restructure) and **Track C** (*"how should the record be organized, holistically?"*) — both are unanswerable without it. Also gates `harvest-questions.py`'s weed wiring. | 3 · S (shipped) |
| **1** | **The discriminator — a zero-wrongness card on OUR topic** | observation | **ours** | *Draft, needs Paul + content-steward before it ships:* "We've never written down what's actually coming to the feeders this summer — only what the books say should be. **From where you sit, are the hummingbirds still working the feeders, or have they thinned out?**" Labels: *Still coming* · *Thinning out* · *Haven't watched lately*. `correctionPrompt`: "Anything else showing up?" | Confirm card → `/api/feedback`. **Needs a `_foldTarget`** so it can self-clear: fold to a dated `observedHere` line on the Birds card, in her name. | **This is the experiment that actually discriminates.** She answers → topic origin is *not* binding, question quality was, and the whole `harvest-questions.py` supply chain is repairable. She doesn't → **topic origin binds**, our-topic asks are permanently dead, and the entire card budget moves to seeding from her own inputs. Two very different budgets. | 3 · S |
| **2** | Fairway grass seed-heads | observation | ours | *Already staged verbatim in `questions.json` (`q-fairway-grass-seedheads`, `active:false`) — no drafting needed.* | Card exists; `_foldTarget: observedGrasses`. Flip `active:true` **in August** when seed-heads emerge. | The crabgrass ID (A7) + the fairway/meadow record. Also a **second data point in the same cell as #1** — which is what a single-case design needs (§4). | 3 · S |
| **3** | Household systems — which job is it? | story / past behaviour | hers | *Paul asks in conversation, not a card:* "The last time something in the house needed a repair or a part — what were you trying to find, and where did you end up looking?" | **Paul relays.** Doctrine-sanctioned (*Paul relays; the model does not fetch*). Lands as an observation or as a backlog note; **does not consume the one-card budget.** | **B6.** Two different builds hide behind one ask — *find the receipt when it breaks* (warranty job) vs *know what I have* (inventory job). Building the wrong one is the risk, not build cost. | 3 · S |
| **4** | The master question — what does she believe happens to things she says? | story / past behaviour | hers | *Paul asks in conversation:* "When you wrote in that the rainfall number looked wrong — what did you figure would happen with that? Did you picture me seeing it, or the app doing something with it, or were you not really sure?" | **Paul relays.** Does not consume the card budget. | The **whole return-leg design**. *"I figured you'd see it"* → the ribbon is garnish, keep it quiet. *"I thought the app would do something"* → the current design is right and must be reliable. *"I wasn't sure"* → we are training an expectation from zero and the first few responses matter more than any mechanism. | 3 · S |
| **5** | Categories: membership vs **placement** | preference | hers | *Do not draft yet — one cycle after #0 answers.* The gap: `q-top-categories` asks whether the list is complete. It does **not** ask whether those five belong **across the top as tabs** or as an index inside the record. A Yes will be read as "build the tabs" when it only confirms the list. | Card, next cycle. | Stops W8·a being built on an over-read of a Yes. | 3 · S |

**What is deliberately NOT in this queue:** the moss card (→ §2 kill list, converted to a return leg),
the W4b add-a-photo validation (→ §2), the W5 ribbon-signifier Mom-check (→ §2), and any bloom
confirm authored by the current template (→ Tier 1 below, retire them).

**The rule this queue enforces:** at n≈10 offers, **a card is not free — it is the scarcest resource
in the project.** Every ask that could have been settled by telemetry or by Paul spends it for
nothing (`/mom-cycle` Leg 3, and run 1's log where telemetry overturned three of three conclusions).

## 1·B Findings table

| # | Tier | Claim | Touches | Effort | Tier-3: question + capture path |
|---|---|---|---|---|---|
| **U1** | **1 · FIX NOW** | **The live queue is 60% the card class she has never answered, sitting under the one card that matters.** Visible five, in file order: `q-top-categories` · `q-clematis-variety` · `q-butterfly-weed-bloom` · `q-lizards-tail-bloom` · `q-strategy-pollinators`. Three are bloom/verdict cards on the template A3 itself calls broken; two of those carry **no `later` label at all**, so "I haven't looked" is not expressible. `q-weed-stiltgrass` is `active:true` and **renders to nobody** (6th, below `MAX_VISIBLE=5`). `[validated — questions.json file order + viewer.html:9477,9489]` | `questions.json`; A3 | S | — (removal is not authoring, but it changes her surface → one-line Paul confirm) |
| **U2** | **1 · FIX NOW** | **Stop citing "1 of 35."** It appears in `BACKLOG.md` A3, `.plans/2026-07-29-rationalization-brief.md`, `~/.claude/skills/mom-cycle/SKILL.md` Leg 3, and `questions.json` → `q-top-categories._note`. `tools/people.json` explicitly instructs that the pre-07-28 funnel figures "do not reproduce" and must be re-derived. Corrected: **~10 offered → 4 answered.** `[validated]` | 4 files | S | — |
| **U3** | **1 · FIX NOW** | **`persona-mom.md` is the wrong person's telemetry** and is the handoff artifact `ux-expert` reads for its `user_context` block. Every `[validated — 2026-05-27]` and `[validated — 2026-07-02]` claim in it derives from `d-14nyhnjz`, which `tools/people.json` establishes is **Paul's**. Full list in §3. `[validated]` | `.user-research/persona-mom.md` | M | — |
| **U4** | **1 · FIX NOW** | **She has never used the A/A+ text-size toggle. Zero events.** Paul's device fired 22. `[validated — 2026-07-02-garden-guru-conversation-analysis.md:108–109 read against the corrected mapping]` The reading-difficulty constraint still stands on Paul's direct testimony (`validated`, 2026-05-22), but its *behavioural* corroboration is gone — and the design consequence is live: **`body.text-lg` is being tuned for a mode she has never turned on.** | W8·b; `persona-mom.md` | S | — |
| **U5** | **1 · FIX NOW** | **R4 is stale — receipt is measurable now.** The A1 table says delivery is *"explicitly unmeasurable"*; since then `momack_followed`, `momack_tapped` and `momack_acknowledged` shipped (viewer.html:9682, 9725, 9731), "Got it" posts a real `/api/feedback` record excluded from R2 by `momlib.py:445`, and **`momack_followed` fired from her device 7/28 12:28 ET**. `[validated — code read + BACKLOG W8·c]` | A1 · R4 | S | — |
| **U6** | **1 · FIX NOW** | **R1 is clearable by the wrong action.** It reads `today − acknowledgedThrough`, a field **Paul stamps**. `momlib.py` states the project's own rule — *a detection mechanism must be clearable ONLY by the action whose absence it detects.* `--acknowledged-through` clears R1 without anything reaching her. `arrivedAt`/`arrivalRef` now exist in `MOM_ACK_DATA`, so the honest metric is available. `[validated — check-mom-ack.py:26,194; viewer.html:9417–9419]` | A1 · R1 | S | — |
| **U7** | **2 · CONFIRMED** | **Ship the moss RECORD as a return leg — it already exists and she has never been shown it.** `plants.json` carries a full `moss` record: the buttermilk slurry as *her* technique, two zones (Western Garden + Eastern Patio flagstone joints), Saihō-ji sourcing, month-keyed notes. She gave that input 7/26 and the app has never reflected a word of it back. Point the next ribbon at it with `linkPhrase`/`linkCard` (mechanism shipped, viewer.html:9671–9688). **Asks her nothing. Produces an object she can see.** `[inferred, strong]` | A2 moss row; A3 return leg | S | — |
| **U8** | **2 · CONFIRMED** | **`q-almanac-name` is the 4th answered confirm and the first that was neither a plant nor a verdict.** Answered Yes 7/29 08:54 ET, folded (card renamed to Journal), retired same day — and retiring it released the watermark. This is the strongest single piece of evidence in the project about *what kind of ask works*, and it is currently recorded only as a resolution string in `questions.json`. Promote it into the evidence base. `[validated — questions.json:28–30]` | A6; A3 | S | — |
| **U9** | **2 · CONFIRMED** | **A6 "conversation browse" is a return-leg row, not a findability row.** Her ask — *"Is there a way to look back at these, eg in the 'journal'?"* — is a request that **her contributions be durable**. She then confirmed the name herself. "Done" means her questions live *in the Journal, in her framing*, not in a Conversations screen. `[inferred, strong]` | A6 | M | — |
| **U10** | **2 · CONFIRMED** | **The Almanac/Journal is her most-used read behaviour and it sits 8th under a name she didn't recognise** — 41 of 139 card expansions, 113 of 249 entry-revisits over 18 days. Combined with `card_expanded` 4× in 30 days across 15 sessions: **she reads the glance and rarely opens the second layer, but when she does open one, it is disproportionately this one.** Promote the Journal in the card order. `[inferred — behavioural, single-device attribution]` | W8·a; A6 | M | — |
| **U11** | **3 · STEER** | **The discriminator card** (queue #1). See 1·A. | A3 | S | ✅ question + capture path in 1·A |
| **U12** | **3 · STEER** | **Household systems: warranty job or inventory job?** (queue #3) | B6 | S | ✅ question + capture path in 1·A |
| **U13** | **3 · STEER** | **The master question — what does she think happens to what she says?** (queue #4) | A3 return leg | S | ✅ question + capture path in 1·A |
| **U14** | **3 · STEER** | **Categories: membership confirmed ≠ tabs confirmed** (queue #5) | W8·a; Track C | S | ✅ named in 1·A; drafting deferred one cycle by the one-card rule |
| **U15** | **3 · STEER** | **Fairway grass seed-heads, August** (queue #2) | A7; A3 | S | ✅ card already staged verbatim |
| **U16** | **2 · CONFIRMED** | **Add `_askClass` / `_effort` / `_topicOrigin` to every card in `questions.json`.** Three literal fields (`verdict\|observation\|expertise\|preference`; `from-here\|needs-a-walk`; `hers\|ours`). Paul-facing metadata only — never rendered. This is what turns one-off card experiments into an accumulating register, which is the only rigorous move available at n=1 (§4). `[assumption — proposed mechanism]` | A3; Track C | S | — |
| **U17** | **1 · FIX NOW** | **Her real viewport is 414×848, not 393×793.** `[validated — 2026-07-02-garden-guru-conversation-analysis.md:109, read against the corrected mapping]` Reviewing at 390×844 is *conservative* (narrower is harder), so the brief's constraint is safe — but the persona's stated viewport is wrong and the "iPhone Pro" device inference was Paul's phone. | `persona-mom.md`; W8·a | S | — |
| **U18** | **2 · CONFIRMED** | **The general-feedback channel is the only one of nine with a complete, closed, per-item lifecycle** — and it is now **two-for-two**: rainfall (7/26) and the rainfall-range note (7/29) both captured → addressed → acknowledged. `feedback-log.json` proves it. **This is the shape every other channel should be copied to**, and it is the strongest thing the project has built. `[validated — feedback-log.json]` | A3 lifecycle rule | — | — |
| **U19** | **3 · STEER** | **Track C taxonomy — her model is close to the INVERSE of the file layout.** See §1·D. Blocked on queue #0 + #5. | Track C; W8·a | L | ✅ via queue #0 and #5 |

## 1·C The two hypotheses — and why the moss card cannot separate them any more

### The corrected evidence, laid out honestly

Every offer/answer we can attribute to her, on the post-07-28 mapping:

| Card | Class | Topic origin | Effort | Offered | Outcome |
|---|---|---|---|---|---|
| `q-crocosmia-lucifer` | verdict | ours | look (but she was certain) | 7/13 | ✅ answered same day |
| `q-white-mophead-annabelle` | verdict | ours | look (certain) | 7/13 | ✅ answered same day |
| `q-panicle-hydrangea-bloom` | verdict/observation | ours | needs a look | 7/13 | ✅ answered 7/18 |
| `q-clematis-variety` | observation | ours | needs a walk | 7/14 | ❌ 15 days |
| `q-butterfly-weed-bloom` | verdict | ours | needs a walk | 7/14 | ❌ 15 days |
| `q-lizards-tail-bloom` | verdict | ours | needs a walk | 7/14 | ❌ 15 days |
| `q-strategy-pollinators` | **preference — zero wrongness risk** | **ours** | **from a chair** | 7/14 | ❌ **15 days** |
| `q-weed-stiltgrass` | observation | ours | needs a walk | 7/22 | ❌ (below the cap since 7/28) |
| `q-almanac-name` | **preference — zero wrongness risk** | **hers** | **from a chair** | 7/28 | ✅ **answered <24h** |
| `q-top-categories` | preference | hers | from a chair | 7/29 | in flight |

`[validated — questions.json createdAt/resolution fields, BACKLOG A1 corrected funnel]`

### What this does to each hypothesis

**① Wrongness-risk — DEMOTED.** `[inferred → weakened]` It predicts that a zero-wrongness card gets
answered. `q-strategy-pollinators` is exactly that and has sat 15 days. The hypothesis survives only
with an epicycle (the "next spring" hypothetical is its own dead class — which is true, per The Mom
Test, but is a *different* explanation). It also rests on **self-reported cause, n=1, offered to a
reassuring son** — already the weakest class of evidence, and the external literature (§4) says the
base rate of "fear of making errors" in this population is high enough that her saying it is only
weakly diagnostic of *her* behaviour.

**② Authorship / topic origin — PROMOTED to the better-fitting explanation.** `[inferred, strong]`
It predicts the whole table without an epicycle: **every card authored from our uncertainty markers
and offered after 7/14 is unanswered (0 of 4 over 15 days). The one card seeded from her own words
was answered in under a day.** It also matches the structural read from 7/26 — her input lands when
it becomes an object she can see, and dies when it adjusts an invisible property.

**③ OCCASION / effort — a real third candidate that nobody has named.** `[assumption]` She answers
what is settleable in the posture she is actually in (phone, reclined, indoors, low attention). Fits
7 of 9 rows. Fails on `q-strategy-pollinators` (from a chair, unanswered) and `q-panicle-hydrangea-bloom`
(needed a look, answered). Not the best fit — but it is confounded with ② in every row, and it has a
completely different remedy (make asks answerable from where she is, vs. only ever ask about what she
raised). **It has to be on the board or ② will be over-credited.**

### ⛔ The moss card is not a valid discriminating instrument

The 7/26 design said: moss is expertise-class (kills wrongness risk) but ours-initiated (leaves
authorship intact), so an answer implicates ① and a null implicates ②.

**That reasoning no longer holds, for three reasons:**

1. **Moss is HER topic.** She raised the moss and the buttermilk technique unprompted on 7/26.
   Under ② her-topic asks get answered. So moss is predicted answered by ①, ② *and* ③ — it is
   **over-determined and discriminates nothing.**
2. **The experiment has already been run, better.** `q-almanac-name` is the same cell
   (zero-wrongness × her-topic × from-a-chair) and came back **positive in under a day**. Running
   moss adds a redundant observation in a cell we have already sampled.
3. **The moss record already exists in canon.** A card asking "where are the good mossy spots?" is
   now **stale-premised** — `plants.json` already names two plantings and two zones. The one real
   remaining gap is the species, and asking her to name a moss species is an **ID verdict** — the
   worst class. The other gap ("more sources, maybe by the barn") is a walk-the-property task she
   already told us she intends.

**Sequencing verdict, asked for explicitly: the moss card does not wait for the UX cleanup — it does
not go out at all.** Convert it to §1·B U7 (the record as a return leg, pointed at by the ribbon).
The one-card budget goes to queue #1.

### Does the *discriminator* wait for the UX cleanup?

**No — but only because its evidence is asymmetric, and Paul must pre-commit to that.**

The measurement-hygiene problem is real: with five stacked input surfaces at 390px we cannot tell
*declined* from *never understood which thing I was answering*. But that contaminates **nulls, not
hits**. If she answers queue #1, she saw it, parsed it, and chose to answer — the confusing stack
cannot manufacture that. If she doesn't, the result is **uninterpretable until the cleanup lands.**

So the rule to write down before the card ships:

> **A hit on queue #1 is readable immediately. A miss is NOT evidence for authorship until W8·a has
> shipped and the card has been re-offered on a clean surface.** Pre-commit to that now, in writing,
> or a null will be over-read exactly the way the A1 gate was.

And the ordering that follows: **W8·a (input-stack cleanup) still goes first** — it is cheap, it is
Tier 1/2, it unblocks the interpretation of every subsequent ask, and queue #0 is occupying the
card slot anyway until she answers it.

## 1·D The taxonomy / IA question (Track C + W8·a) — does her model match the file layout?

**No. It is close to the exact inverse, in both directions.** `[inferred — mapping her five
relayed categories against the repo's canon files; her list is `validated` as *stated*, the reading
of what it implies is mine]`

| Her category | What backs it in the record |
|---|---|
| gardening | `plants.json` + `weeds.json` + `turf.json` + `candidates.json` — **4 files → 1 category** |
| wildlife | `birds.json` + `mammals.json` + `amphibians.json` (+ `fishing.json`?) — **3–4 files → 1 category** |
| vehicles | `vehicles.json`, `group: "vehicle"` — **1 file → 3 categories** |
| equipment | `vehicles.json`, `group: "equipment"` | |
| house systems | `vehicles.json`, `group: "household-system"` (B6) | |

**The finding:** where the data is one file she wants three doors; where the data is four files she
wants one door. **`group` — a *field* — is doing the work she expects a *category* to do, and
`file` is doing work she expects to be invisible.** That is a decisive argument against the
"one JSON file per card" accretion pattern and against answering Track C by refactoring the files.

**What is absent from her five is as informative as what is in it:** weather, the map/zones, the
Journal, celestial, fishing. Those are exactly the things that are *not things you tend or own*.
Her five are a **stewardship taxonomy** — a repository index — not a content taxonomy. Which means
her "tabs across the top" almost certainly sits **beside** the glance rather than replacing it, and
is fully compatible with the ratified glance-and-repository doctrine. `[inferred]` **Do not read a
Yes on `q-top-categories` as a mandate to tab-ify the whole app** — that is queue #5.

**And the finding about *what kind of ask works*, which is bigger than the IA:** this is the one
class of question that **asks no verdict of her about a plant she might get wrong** — and it is
also **seeded from her own words**, and it is **answerable from a chair**. All three of the live
hypotheses predict she engages with it. That is *why* it is the right card, and it is also why it
**cannot** double as an experiment. Keep the roles separate: `q-top-categories` is a **decision
input**; queue #1 is the **instrument**. Do not let one card try to be both — that is what happened
to moss.

## 1·E R1–R4 — do they measure "did we answer her?"

The failure condition flipped from *is she engaged* to *did we answer her*. Assessment per metric:

| Metric | Does it measure the new failure condition? | Verdict |
|---|---|---|
| **R1 · ack staleness** (`today − acknowledgedThrough`) | **Partly, and it measures the wrong interval.** `acknowledgedThrough` is *when Paul stamped*, not *how long she waited*. Her experience is `arrivedAt → shipped`. `arrivedAt`/`arrivalRef` now exist in `MOM_ACK_DATA`. **It is also clearable by the wrong action** — `--acknowledged-through` turns it green with nothing reaching her, violating the project's own rule in `momlib.py`. | **Rewrite as arrival→acknowledgment latency.** Keep staleness as a separate, secondary number. `[validated — code read]` |
| **R2 · unacknowledged arrivals** | **Yes — this is the good one.** It is arrival-anchored, counts *and* ages, covers five channels, and correctly excludes ack-receipts and bench traffic (`momlib.py:445,460`). `/api/zone-feedback` is no longer a blind spot — it was rerouted onto the general-note path 7/26 and the historical read is **0 entries across 207 days** (viewer.html:9362). | **Keep as built.** My 7/26 open question Q-D is closed. `[validated]` |
| **R3 · specificity** | **Yes, and correctly left un-automated.** A template can only produce "thanks for your feedback," which is worse than silence at the moment she is doubting herself. | Keep. |
| **R4 · delivery** | **Stale — it says "explicitly unmeasurable" and that is no longer true.** `momack_acknowledged` (a "Got it" tap → a real feedback record) and `momack_followed` (the inline link) both ship. `momack_followed` **fired from her device 7/28 12:28 ET**. | **Rewrite.** R4 = *did an action attributable to the ribbon occur?* **Asymmetric: a hit is the strongest receipt evidence this project will ever get without asking her; a miss proves nothing.** Pre-commit to not over-reading a zero. `[validated]` |
| **R5 — missing** | Nothing measures **behavioural consequence**: did arrivals hold or rise in the window after a *specific, correct, conceding* acknowledgment. No new instrumentation needed — the arrival timestamps exist. | **Add it, and label it a NARRATIVE instrument.** At n=1 on a bursty weekly cadence it will never reach significance and must never be reported as if it had. `[assumption — proposed]` |

**Is the process-metric caveat being honoured in practice? Mostly yes — say so honestly.** I looked
for a place where R1/R2 green was read as "she felt heard" and **did not find one**. The `/mom-cycle`
Refinement log run 1 is a model of the right discipline (telemetry overturned three of three
written conclusions before they shipped). The real drift is not caveat-violation; it is **U6** —
R1's greenness is under Paul's own thumb, which is a *mechanism* failure, not a *reading* failure.
`[validated — grep across BACKLOG.md, CLAUDE.md, .user-research/]`

---

# 2 · Kill list

| Row | Why it should not be done |
|---|---|
| **The moss card as an ask** (BACKLOG "👥 Agent drafts → Paul confirms," item 9; A3 "→ THE NEXT MOVE IS THE MOSS CARD") | Three independent reasons, any one sufficient: it is **over-determined** (all three hypotheses predict an answer, so it discriminates nothing); the same cell has **already been sampled positive** (`q-almanac-name`); and it is **stale-premised** — `plants.json` already holds a rich moss record naming her technique and two zones. **Convert to U7** (the record as a return leg). Killing this frees the one-card budget for a real instrument. |
| **W4b — "validate the add-a-photo affordance with Mom before building"** (A2) | It is a **hypothetical future feature preference** — the weakest class in The Mom Test and the exact class already sitting unanswered for 15 days (`q-strategy-pollinators`). A null would be uninterpretable and would burn the one card. **Replace the ask entirely:** either ship the affordance on one card and read the behaviour, or don't build it. No question, no capture path → kill. |
| **W5 — "the 30-second Mom-check on the ribbon signifier (face vs glyph) and placement"** (A4) | Paul has already decided the label and declined the face. The remaining half — that the tab covers ~40% of a reading band and **overlaps the card text at 390px** — is a *defect*, not a preference, and it is squarely inside W8·a. Asking her to adjudicate a layout we already know is broken is the "adjudicate our work" class she declines. **Fix it; don't ask about it.** |
| **"Retire the confirm surface"** (a live temptation across several rows) | Already the calibration correction from 7/26 and it still holds: **the evidence is FUTILITY, not HARM.** No negative reaction has ever been observed; she viewed the stack and volunteered that the app keeps getting better. Futility says *change the ask*; harm would say *remove the surface*. Retiring on futility evidence would repeat the A1-gate over-read exactly. |
| **Any further attempt to settle the hypotheses with ONE decisive card** | At n=4 answers a three-way discrimination is not available and chasing it wastes her attention. The methodologically correct move at n=1 is a **register that accumulates** (U16), not a decisive experiment. This is the single-case-design import in §4. |

---

# 3 · Status corrections

Everything here was verified against code, canon, or `questions.json` — not read off a backlog row.

| # | What a live artifact says | What is actually true | Proof |
|---|---|---|---|
| **S1** | `persona-mom.md` presents ~10 `[validated]` behavioural claims about Mom | **They are Paul's device.** `d-14nyhnjz` was recorded as Mom until 2026-07-28; `tools/people.json` now lists it under `paul` and states that every pre-07-28 engagement number "attributed Paul's own app-opens to Mom." Affected: "27 sessions / 341 events over 6 days" · "~4.5 sessions/day" · "12 (later 22) `text_size_changed` events — the only device that used A/A+" · "0 stars in 55 `entry_revisited`" · the card-popularity table (Plants 60 / Weather 60 / Wildlife 54 / Celestial 47 / Property 45) · "all her Guru conversations are 2-turn" · "active 27 of ~40 days" · "mobile-only, viewport 393×793" | `tools/people.json` `_meta.resetWhy` + `whatThisInvalidates`; `persona-mom.md:11,18` |
| **S2** | Persona: the no-reading-glasses constraint is **behaviourally validated** — "she is actively reaching for the affordance designed for it" | **She has fired the toggle zero times.** Her real device shows `text-size toggle: 0`. The constraint stands on Paul's direct testimony (`validated`, 2026-05-22); the behavioural promotion does not survive. **Design consequence: `body.text-lg` is being tuned for a mode she has never used.** | `2026-07-02-garden-guru-conversation-analysis.md:108–109` read against the corrected mapping |
| **S3** | Persona + A1: "her Guru use is 2 conversations, not yet a pattern" | **Her real device started 7 Guru conversations by 6/27 — the most of any device in the corpus** — and was set aside at the time as "Paul's 2nd device? co-steward?" | Same table, row `d-szqlt0h7`; `2026-07-02-mom-behavior-interpretation.md:122` |
| **S4** | BACKLOG A1: *"Proven live 7/26 … she uses **at least two** [device buckets]"* | **Does not survive.** The observation was: a Guru conversation from a bucket absent from `people.json` while "her" mapped id showed zero. After the 7/28 remap that is **fully explained by the misattribution** — the unmapped bucket *was* her, the mapped one was Paul. Downgrade to `assumption`: she owns a MacBook that has never produced authored content. The **ITP-eviction mechanism** remains `validated` as a risk; the claim that it has *already happened to her* does not. | `people.json`; BACKLOG A1 measurement-integrity row |
| **S5** | Four live artifacts: "offered 35 → viewed 33 → tapped 1 → answered 1" | **Do not cite.** Corrected read (BACKLOG A1, `4878994`): confirm carousel **offered 9 → answered 3**; launcher offered 5 → tapped 0. Plus `q-almanac-name` 7/29 → **4 answered.** ~10 offers, 4 answers. | `people.json` `whatThisInvalidates`; BACKLOG A1; `questions.json:28–30` |
| **S6** | BACKLOG A2 moss row: *"Add the record (agent-draftable, Paul approves)"* — reads as open | **SHIPPED.** `plants.json` holds a complete `moss` record: `confidence` marked unsettled, month-keyed season notes incl. the buttermilk slurry, a `fertilize` entry explaining the slurry is an adhesive not a feed, `zoneId: western-garden` + a `zoneNote` naming the Eastern Patio flagstone joints as the second planting and flagging it as **W6 firing for real**. | `plants.json:4720–4861` |
| **S7** | BACKLOG A1 · R4: delivery is *"explicitly unmeasurable"* | **Superseded.** `momack_followed` / `momack_tapped` / `momack_acknowledged` all ship; "Got it" writes a real feedback record; `momlib.py` excludes ack-receipts from R2 and exposes an `ack_receipts()` reader. `momack_followed` fired from her device 7/28. | viewer.html:9682, 9723–9731; `momlib.py:445,460,710` |
| **S8** | My own 7/26 audit's open question Q-D: *"Has anything ever arrived at `/api/zone-feedback`?"* | **ANSWERED — 0 entries across 207 days**, and the channel was rerouted onto the general-note path the same day. Close the question; the R2-blind-spot finding is resolved. | viewer.html:9352–9365 |
| **S9** | My own 7/26 recommendation: "make the ack ribbon tappable — replies are receipts" | **SHIPPED**, and better than proposed: two doors ("Got it" = one tap, cannot be wrong; "Write back" = the panel), plus an inline `linkPhrase`/`linkCard` so the ribbon carries the path to what it describes. | viewer.html:9609–9735 |
| **S10** | `questions.json` implies `q-weed-stiltgrass` is being served (`active: true`) | **It renders to nobody.** `outstanding()` slices the first `MAX_VISIBLE=5` active confirms in **file order**; stiltgrass is 6th and has been below the cap since `q-almanac-name` was inserted first on 7/28. | `questions.json` order; viewer.html:9477, 9489 |
| **S11** | BACKLOG A3: the ask-reframe residual — "`q-strategy-pollinators` still says *Ask me later*" | **Partly stale.** Its `later` label now reads *"Haven't thought about it"*. The real residuals stand: `q-butterfly-weed-bloom` and `q-lizards-tail-bloom` carry **no `later` label at all**, and the reframe has still not reached `harvest-questions.py`. | `questions.json` |

---

# 4 · External research

Current (2025–26) practice, and **the specific Fernwood row each source changes.** Where the
literature conflicts with ratified Fernwood doctrine I name the conflict rather than applying the
generic advice.

### 4.1 Single-case experimental design (SCED) / N-of-1 — the right methodology import

Sources: [Tate et al., *A proposed regulatory and ethical framework for SCED*, Neuropsych. Rehab. 2025](https://www.tandfonline.com/doi/full/10.1080/09602011.2025.2480443) · [*Evidence and reporting standards in N-of-1 studies: a systematic review*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10354076/) · [*The Family of Single-Case Experimental Designs*, Harvard Data Science Review](https://hdsr.mitpress.mit.edu/pub/nqvadq0w/download/pdf)

The load-bearing points: an **alternating-treatments design** compares two or three conditions by
**repeatedly re-presenting them over time**, never by running each once; WWC standards require
multiple phases and multiple demonstrations of effect before a claim is credible; and
**carryover between conditions** is the design's primary threat when conditions alternate quickly.

**Rows it changes:**
- **A3 "→ THE NEXT MOVE IS THE MOSS CARD, AND IT IS A DISCRIMINATING INSTRUMENT."** This is a
  one-shot A/B on one participant. SCED says that is not a design — a single alternation cannot
  demonstrate an effect. → **kill list**, and the replacement is **U16**: label every card with
  class / effort / topic-origin so the conditions alternate naturally and the answer rate
  accumulates. That is the alternating-treatments design, run at Fernwood's actual cadence.
- **Carryover is a real threat here and nobody has named it.** Cards persist in a stack; an
  unanswered card is still on screen when the next one arrives. So condition *n* is contaminated by
  condition *n−1* in a way a clean SCED forbids. → argues for **U1** (retire the un-reframed bloom
  cards) on *measurement* grounds, not just legibility grounds.
- **⚠️ Conflict with doctrine, named:** SCED wants *rapid* alternation. Paul's **one card per
  `/mom-cycle`** rule makes alternation slow. **Defend the local call.** Her attention is the
  scarcest resource in the project and one card per cycle is what keeps an ask reading as
  conversation rather than a quiz. The correct adaptation is **more cycles**, not more cards per
  cycle — and the register (U16) is what makes a slow design still add up.

### 4.2 Acquiescence bias, satisficing, and age

Sources: [Schanze, *Response Behavior and Quality of Survey Data*, Soc. Meth. & Research 2023](https://journals.sagepub.com/doi/10.1177/0049124121995534) · [*Quality of Survey Responses at Older Ages*, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9155162/) · [*The acquiescence effect in responding to a questionnaire*, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2736523/)

Acquiescence — agreeing regardless of content — is a recognised **indicator of satisficing**, and
satisficing rises when ability or motivation is low **and question difficulty is high**. High
acquiescence correlates with older age.

**Rows it changes:**
- **A3 / U1 — the bloom-card template.** *"The X should be in flower about now… does that match?"* is
  an **agree-shaped** question with a Yes button, aimed at a low-attention reading posture. It is
  close to a textbook acquiescence trap. That the three she answered were all **Yes/"Looks right"**
  is exactly the artifact this literature predicts. → the 7/13 panel's *"Guardrail (health, not
  success)"* note about agreeableness artifacts was **right and is still un-acted-on.** Retire the
  template's Yes/No shape, not just its wording.
- **W2 — "demote the confirm button; ask *which of these is wrong?*"** This literature is the
  strongest external support for that row. Her base rate on confirms was 2-for-2 Yes; a confirm
  cannot surface an omission. Keep the row alive.
- **It also means U8 must be read carefully.** `q-almanac-name` was answered **Yes**. A Yes on a
  card whose Yes label is the pleasing answer is weak evidence *about the content*. It is strong
  evidence *about engagement* (she tapped a card at all, in under a day, on a class she had
  never engaged before) — which is the claim I make and the only one I make.

### 4.3 Attitudinal vs behavioural weighting when self-report is unreliable

Sources: [NN/g, *Attitudinal vs. Behavioral Research in UX*](https://www.nngroup.com/articles/attitudinal-behavioral/) · [Quirk's, *Bridging the say-do gap with behavioral data*](https://www.quirks.com/articles/bridging-the-say-do-gap-with-behavioral-data)

NN/g: attitudinal research **cannot reliably capture past behaviour or future intentions** (recall +
social desirability); behavioural research cannot tell you *why*; **the insight is in the
mismatch**. Explicit guidance favours behavioural data when the two conflict.

**Rows it changes:**
- **A3's headline finding** (she hesitates because she is afraid of being wrong) is a
  **self-reported cause of past behaviour** — the exact combination NN/g says is least reliable.
  Combined with §1·C's `q-strategy-pollinators` datapoint, this is enough to **demote it from the
  project's "highest-confidence user finding" to one of three live candidates.**
- **The brief's orienting principle ① is straightforwardly corroborated** — explicit *and*
  behavioural both count, and where they disagree the behaviour wins. My concrete application: the
  fear self-report and the pollinators non-answer disagree; **the non-answer wins.**
- **U16** is the mismatch instrument: it makes the say/do comparison computable per card class.

### 4.4 Technology self-efficacy and fear of error in older adults

Sources: [*Older adults' self-perception, technology anxiety, and intention to use digital public services*, BMC Public Health 2024](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-024-21088-2) · [*Influencing factors of digital health technology anxiety in the elderly: systematic review & meta-analysis* (searched to Oct 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12528084/)

The finding that matters: **fear of making errors is common even among older adults who consider
themselves confident with technology**, and technology self-efficacy is the strongest negative
correlate of technology anxiety.

**Rows it changes:**
- **Cuts both ways on A3, and both directions are useful.** It **raises the prior** that her
  self-report is describing something real — so do not dismiss it. It also means the mechanism has a
  **high base rate**, so her stating it is only weakly diagnostic of *her specific* funnel. Net:
  keep wrongness-risk on the board, stop treating it as the settled explanation.
- **It supports the self-efficacy remedy over the question-design remedy** for A3's residual
  ("make 'I'm not sure' a first-class answer" · "consider whether a wrong answer costs her nothing
  **and she is told so**"). Self-efficacy is built by **visible success**, which is exactly U7 and
  U9 — showing her the moss record and making her contributions durable in the Journal. **The
  return leg is a self-efficacy intervention, not a politeness gesture.**

### 4.5 Continuous discovery at n=1 — and its critics

Sources: [Torres, *Continuous Discovery* glossary](https://www.producttalk.org/glossary-discovery-continuous-discovery/) · [Torres, *5 Objections to User Research*](https://www.looppanel.com/blog/objections-user-research-teresa-torres) · [Rutter, *Continuous discovery — holy grail or poisoned chalice?*](https://www.uxforthemasses.com/wp-content/uploads/2023/09/Continuous-discovery-Holy-grail-or-poisoned-chalice-notes.pdf)

Torres's frame is **weekly touchpoints by the team building the product**. The critique that lands
here: the opportunity-solution tree can create **a false sense of analytical rigour** — its quality
is entirely a function of the interviews under it, and the framework is more prescriptive about
*cadence* than about what makes a conversation epistemically sound. A second critique: "the 20
customers you know best are not a representative sample."

**Rows it changes:**
- **`/mom-cycle` is Fernwood's continuous-discovery cadence** and it is well-built. The critique
  applies precisely: the cadence exists, and the thing underneath it — the *quality of the asks* — is
  where the failure is (0 of 4 our-topic asks answered in 15 days). → keep the cadence, fix the
  supply. **U16 + queue #1.**
- **"Not a representative sample" is the wrong critique for Fernwood and should be dismissed
  explicitly.** Mom is not a sample of anything; she is the population. Representativeness is not a
  threat here — **regression to the researcher is** (§4.6).
- **⚠️ Conflict with doctrine, named:** Torres wants weekly *interviews*. Fernwood forbids the
  channel that would make that possible (text is not a channel; an agent does not fetch her words).
  **Defend the local call** — the doctrine is a product decision with a stated cost, and closing the
  easy channel is what forces the app to earn the input. But **state the consequence honestly:**
  Fernwood runs continuous discovery **without the interview leg**, which means the *relayed*
  conversations (queue #3 and #4) are not optional garnish — **they are the only interview leg the
  method has**, and they should be treated as first-class, scheduled work rather than as
  opportunistic.

### 4.6 Ethics of researching a family member who is also the only user

Sources: [Råheim et al., *Researcher–researched relationship in qualitative research*, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4910304/) · [UVic, *Guidelines for ethics in dual-role research*](https://www.uvic.ca/research-services/how-do-i/get-ethics-approval/how-to-apply-human-ethics-approval/dual-role-research-guidelines/index.php) · [Fischer et al., *Co-Design with Older Adults*, ACM CSCW](https://dl.acm.org/doi/10.1145/3479506) · [*Designing Meaningful Engagement for Older Adults*, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12793890/)

The consistent finding: in dual-role research a **"warm and friendly atmosphere of trust" does not
neutralise the underlying status asymmetry**, and the researcher must recognise the structure of
the relationship rather than the feel of it. The co-design literature names the specific risk
directly — older adults "attempt to please" researchers in design-related questions — and its
practical countermeasures are **participant-led documentation** (reduce the bias of the researcher
scribing) and **participant autonomy over how much they commit**.

**Rows it changes:**
- **It is the strongest external validation of an already-ratified Fernwood rule** —
  *adopt her words, never improve them*. "Participant-led documentation" is precisely the
  household-systems episode: she coined the term, hedged, was right, and the first ribbon draft
  silently corrected her. Keep that rule as a hard gate.
- **It is a direct caution about `.private/mom-feedback-2026-07-26.md` as an evidence source.** Her
  account of her own uncertainty was offered **to a reassuring son, in a private channel, in a
  moment of reassurance** — the textbook dual-role condition. That is the second independent reason
  (with §4.3) to demote the fear reading. The quarantine clause already protects her; this says the
  same material should also be **weighted down as evidence**, not just protected as content.
- **"Autonomy over how much they commit" argues against the persistent card stack** — an ask that
  never expires becomes a debt. → supports letting unanswered cards **age out silently** (still on
  the A3 watch list). ⚠️ But note the 7/26 calibration: the attrition theory is currently
  *contradicted* by her own "getting better every time I open it." Do this on measurement-hygiene
  grounds (U1 + §4.1 carryover), **not** on an attrition claim the evidence doesn't support.
- **⚠️ Conflict with doctrine, named:** the ethics literature would push toward informed,
  explicit participation — telling her she is in a study. **Do not import that here, and say why:**
  Fernwood is not a study, it is her family's record of her own place, and framing it as research
  would be both false and corrosive to the one thing that is working. The transferable practice is
  **weighting and protection**, not consent theatre. What *is* worth importing verbatim is the
  purpose sentence Paul already wrote into `q-top-categories` — *"Once we know, we can lay the app
  out so each one is easy to reach."* **Telling her what her answer will be used for is the
  ethically load-bearing move, and it is already doctrine.**

---

# 5 · Sequencing view

If these were done in order:

**Phase 0 — before anything reaches her (this session).**
1. **U2** stop citing 1-of-35 (4 files) · **U5/U6** rewrite R1 and R4 · **U3/U4/U17** re-tag
   `persona-mom.md`. All Tier 1, all Paul-facing, all cheap, and all of them are **wrong facts
   currently steering other seats' work** — `ux-expert` reads the persona for its `user_context`.
2. **U1** retire the three un-reframed bloom cards. This is the highest-leverage single move in my
   lane: it makes `q-top-categories` the visible ask instead of the fifth item under three dead
   ones, it lets `q-weed-stiltgrass` render at all, and it removes the carryover contamination
   (§4.1) that would otherwise poison queue #1.

**Phase 1 — the measurement hygiene (W8·a/b, ux-expert's lane).**
3. The input-stack cleanup goes **before** any new ask. Two reasons, and the second is mine: it is
   cheap and Tier 1/2 — **and the card slot is occupied by `q-top-categories` anyway**, so nothing
   is lost by doing it first. **W8·b addendum from U4:** tune the **default** type scale;
   `body.text-lg` is a mode she has never turned on.

**Phase 2 — the return leg, which asks her nothing.**
4. **U7** ship the moss record into her view via the ribbon's `linkPhrase`/`linkCard`. **U9/U10**
   promote the Journal. Both are pure return-leg: they produce **objects she can see** for input she
   already gave. Under the promoted hypothesis (②) this is the highest-value work in the backlog,
   and it costs zero of her attention.
5. **U16** add `_askClass` / `_effort` / `_topicOrigin` to `questions.json`. One-line-per-card, and
   it is what makes every subsequent cycle cumulative rather than anecdotal.

**Phase 3 — the asks, one per cycle, in the queue order of §1·A.**
6. Wait for `q-top-categories`. **Retire it by hand the moment it answers** — it is unprobeable and
   holds the watermark. Then queue #1 (the discriminator) on the cleaned surface, **with the
   asymmetric-reading rule pre-committed in writing**. Then #2 in August.
7. **In parallel and not competing for the card budget:** queue #3 and #4, Paul in conversation.
   Per §4.5 these are not extras — they are the only interview leg the method has.

**Track A vs Track B ranking, since the brief asks:** **Track A first, decisively.** Track B is the
only deadline-bearing work but its deadlines are Paul's own and he is the only user — a slipped
GTI service costs money, not a relationship. Track A is where the **irreversible** risk sits: she has
had exactly **one** reinforced experience of contradicting the app and being answered. Extinction
after a single reinforced trial is fast, and B6 (household systems) is the one Track-B-shaped row
that is really Track A wearing Track B's clothes — **she proposed it, and it is the cheapest
possible demonstration that proposing something to this app makes it appear.** Rank B6 with Track A;
leave the rest of B where it is.

---

# 6 · What I could not determine

| Open question | Why it's open | What would settle it |
|---|---|---|
| **Is topic origin or effort/occasion the binding constraint?** Every row in §1·C confounds them. | No card has ever been offered in the cell *her-topic × needs-a-walk* or *ours-topic × from-a-chair-and-not-hypothetical*. | Queue #1 fills the second cell. The first fills naturally once asks are seeded from her inputs. Both need **U16** to be legible. |
| **Whether `q-strategy-pollinators`'s 15-day silence is about topic origin or about the hypothetical-future frame.** | Two explanations, one card. | The Mom Test says never ask about hypothetical futures at all — so the cleanest resolution is to **retire it** rather than to interpret it. Flagged, not recommended, because it is Paul's queue call. |
| **Whether `q-almanac-name`'s Yes is content-bearing or acquiescence.** `[§4.2]` | It was answered Yes on a card whose Yes was the pleasing answer. | Nothing available. **Claim only the engagement fact** (she tapped a never-before-engaged card class inside a day), never the content fact. Already scoped that way in U8. |
| **Whether her five categories are tabs-over-everything or an index into the repository.** | `q-top-categories` asks membership, not placement. | Queue #5, one cycle later. Do not infer it from a Yes. |
| **What actually happened in the 7 Guru conversations on her real device through 6/27.** | They were read at the time as "Paul's 2nd device?" and were never analysed as hers. Reading their content now is a **judgment call for Paul, not mine** — it is conversation content, and the AI boundary's ingress clause is about channels she routed here (Guru is one), but the quarantine clause is about her words about herself. | Paul's call whether to re-run the 7/02 conversation analysis against the corrected mapping. **My recommendation: yes, and it is probably the highest-value un-mined evidence in the project** — 7 real stewardship conversations from the make-or-break user that have never been read as hers. |
| **Whether the moss record is reachable by her at all.** | It is a plant record inside the Plants card; she fires `card_expanded` ~4× in 30 days. | U7's ribbon link *is* the test — `momack_followed` will say whether she took it, and that same event already proved she follows a ribbon link (7/28). |
| **Whether "Got it" will be used, and what a "Got it" without a reply means.** | Shipped after the last measurable window. | One cycle of data. Pre-commit: a "Got it" is a **receipt**, not satisfaction; never read it as "she felt heard." |

---

## Evidence log

- `2026-07-29: [validated] — tools/people.json _meta + .user-research/2026-07-02-garden-guru-conversation-analysis.md:108-109 — the device backing every "validated" behavioural claim in persona-mom.md (d-14nyhnjz) is PAUL's. Mom's real device (d-szqlt0h7) shows 7 Guru conversations, 0 text-size-toggle events, viewport 414x848, active span 5/21-6/27. The persona's telemetry tier does not survive.`
- `2026-07-29: [validated] — questions.json:28-30 — q-almanac-name (preference class, zero wrongness risk, seeded from her own words, answerable from a chair) was offered 7/28 and ANSWERED YES 7/29 08:54 ET, then folded and retired. Fourth answered confirm; first that is neither a plant nor a verdict.`
- `2026-07-29: [inferred, strong] — questions.json file order + viewer.html:9477,9489 — q-strategy-pollinators (also zero wrongness risk, also answerable from a chair, but OUR topic) has been inside the visible 5 continuously since 2026-07-14 and is unanswered at 15 days. Wrongness-risk predicts it is answered; it wasn't. Topic origin (authorship) fits the corrected data better than wrongness risk.`
- `2026-07-29: [inferred, strong] — same sources — every confirm card authored from OUR uncertainty markers and offered after 7/14 is unanswered (0 of 4, 15 days); the one card seeded from HER own words was answered in under a day. This is the sharpest statement the corrected data supports.`
- `2026-07-29: [inferred, strong] — plants.json:4720-4861 + the 7/26 audit — the moss card is over-determined (all three live hypotheses predict an answer), samples a cell already sampled positive by q-almanac-name, and is stale-premised because the moss record already names two plantings and two zones. It is no longer a discriminating instrument. Convert to a return leg.`
- `2026-07-29: [validated] — BACKLOG A1 corrected read (4878994) + people.json whatThisInvalidates + questions.json — the "offered 35 / viewed 33 / tapped 1 / answered 1" funnel is the wrong person's denominator. Corrected: ~10 offered, 4 answered. Still cited in BACKLOG A3, the rationalization brief, the mom-cycle Skill, and q-top-categories._note.`
- `2026-07-29: [validated] — viewer.html:9682,9723-9731 + momlib.py:445,460,710 + BACKLOG W8-c — momack_followed / momack_tapped / momack_acknowledged all ship; "Got it" writes a real feedback record that R2 correctly excludes; momack_followed fired from her device 7/28 12:28 ET. R4's "explicitly unmeasurable" is stale.`
- `2026-07-29: [validated] — check-mom-ack.py:26,194 + momlib.py comment on self-clearing detectors — R1 measures today-minus-acknowledgedThrough, a field Paul stamps, so it is clearable by an action other than the one whose absence it detects. arrivedAt/arrivalRef now exist in MOM_ACK_DATA, so arrival-to-acknowledgment latency is computable.`
- `2026-07-29: [validated] — viewer.html:9362 — /api/zone-feedback historical read is 0 entries across 207 days and the channel was rerouted onto the general-note path 7/26. My 2026-07-26 open question Q-D is closed and the R2 blind-spot finding is resolved.`
- `2026-07-29: [inferred] — her five relayed categories mapped against canon files — gardening covers 4 files, wildlife covers 3-4, and vehicles/equipment/house-systems are three values of ONE field in ONE file. Her navigation model is close to the inverse of the file layout in both directions; `group` is doing category work and `file` is doing work she expects to be invisible.`
- `2026-07-29: [inferred] — same — the five things absent from her list (weather, map/zones, Journal, celestial, fishing) are exactly the things that are not "things you tend or own." Her taxonomy is a stewardship/repository index, not a content taxonomy, and is compatible with the ratified glance-and-repository doctrine rather than a replacement for it.`
- `2026-07-29: [inferred] — external: NN/g attitudinal-vs-behavioural + the dual-role research literature — the A3 headline finding is a self-reported cause of past behaviour offered to a reassuring son in a private channel, which is the least reliable evidence combination in both literatures. Two independent reasons to demote it from "highest-confidence user finding" to one of three candidates.`
- `2026-07-29: [assumption — proposed mechanism] — SCED/N-of-1 standards — a one-shot A/B on one participant is not a design. Replace decisive single cards with an accumulating register: _askClass / _effort / _topicOrigin on every card in questions.json, read as an alternating-treatments design at Fernwood's own cadence.`
- `2026-07-29: [inferred] — acquiescence/satisficing literature — the bloom template ("should be in flower about now... does that match?") is an agree-shaped question with a Yes button aimed at a low-attention posture; all three verdict cards she answered were Yes. The 7/13 panel's agreeableness guardrail was right and is still un-acted-on.`
- `2026-07-29: [validated] — questions.json file order + viewer.html:9477,9489 — q-weed-stiltgrass is active:true and renders to nobody (6th of 5) since q-almanac-name was inserted first on 7/28.`
- `2026-07-29: [validated] — feedback-log.json — the general-feedback channel is now two-for-two on the full lifecycle (capture -> address -> acknowledge): the rainfall note 7/26 and the rainfall-range note 7/29. It remains the only channel of nine with a complete per-item lifecycle.`

## Open questions carried forward

- Re-run the 7/02 Guru conversation analysis against the corrected device mapping — **7 real
  stewardship conversations from the make-or-break user have never been read as hers.** Paul's call
  on the boundary; my recommendation is yes.
- Queue #3 and #4 (household-systems job shape; what she believes happens to what she says) remain
  the two highest-value questions in the project and both require Paul in conversation.
- Does an unanswered card ageing out silently help or read as the app forgetting? Watch item, not a
  finding — the attrition theory is still contradicted by her own words.
