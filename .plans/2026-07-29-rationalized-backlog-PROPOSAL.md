# Fernwood — the rationalization, proposed (2026-07-29)

**Status: PROPOSAL. Nothing here has been applied to `BACKLOG.md`.** Paul's spec said *"Do NOT start by
editing — read the tracks, check them against git and the live app, then propose the reordering."* This
is that proposal. On his go, it replaces the `▶️ NEXT` table and the TOP ITEM block; the tracks below
them stay as the decision record.

**Panel:** ux-expert · user-researcher · engineering-partner · content-steward · ai-advisor, plus a
mechanical verification sweep (140 rows classified). Reports in `.ux-reviews/`, `.user-research/`,
`.engineering/`, `.content-reviews/`, `.ai-advisor/`, `.plans/2026-07-29-verification-sweep.md`.
Brief: `.plans/2026-07-29-rationalization-brief.md`.

---

## 0 · Read this first — the instrument was broken, so the priorities were wrong

Two discoveries reorder everything, and both are about **measurement**, not features.

### ⭐ The funnel that justified the project's headline finding counted the wrong person

`tools/people.json` is unambiguous: the device mapping was **backwards until 2026-07-28**, and its own
`_meta` says *"Do not cite any pre-2026-07-28 funnel verdict; re-derive it."* Paul's builder device was
recorded as Mom's for 26 days.

**"Offered 35 → viewed 33 → tapped 1" is not her.** Corrected: **~10 offered → 4 answered.** That is not
a disengaged user. Everything downstream of that number needs re-reading:

- **The fear hypothesis loses its quantitative leg.** What remains is her self-report — n=1, offered to
  a reassuring son, which this project already classifies as its weakest evidence.
- **A rival fits better.** Every card authored from *our* uncertainty markers and offered after 7/14 is
  unanswered (0 of 4). The one seeded from *her own words* — `q-almanac-name` — was answered **in under
  a day**. **Topic origin predicts the data; fear does not.**
- **`persona-mom.md`'s whole telemetry tier is Paul's device** — sessions, card popularity, "0 stars in
  55 revisits", viewport. It is the file ux-expert reads for user context. It must be re-derived.
- **She has never once used the A/A+ toggle** (Paul's device fired it 22×). The reading-difficulty
  constraint still stands on Paul's testimony — but **`body.text-lg` is being tuned for a mode she has
  never turned on.** Fix the *default* type scale instead.
- **Three irreconcilable funnel figures** (35/33/1 · 9→3 · 60/42/2) sit in three sections with nothing
  saying which is current.

### ⭐ Paul's own measurement-hygiene point is literally true, and it has a named cost

Five free-text doors into one room — the composer, *Write back*, *＋ Add a note*, the *General feedback*
tab, and the hidden correction field. Every note already carries `context.section`, **so the record can
tell them apart while she cannot.** We are collecting well-labelled data about a choice she was never in
a position to make. And the composer's placeholder is two asks in one field:

> *"What did you see, or what would you like to know?"*

An observation log **and** a question to the assistant, sharing one box and one button. A tap there is
uninterpretable between those intents without inspecting the payload.

**Consequence for ordering: clean the instrument before running any new experiment through it.**

---

## 1 · Status corrections — work that is already done

The verification sweep found **9 SHIPPED-BUT-READS-OPEN**, 8 stale pointers, 6 duplicate sets, 2
open-but-reads-shipped. The ones that change what to do next:

| # | The row says | Reality | Evidence |
|---|---|---|---|
| 1 | `▶️ NEXT` #1 rainfall legibility + #2 ribbon deep-link are the top two items | **Both shipped together 2026-07-26** | `0ef98e5`; `viewer.html:1646, 2242, 2287, 5195-5202`, `9669-9691` |
| 2 | **W8·b ①** — the rainfall type inversion, *used as the worked Tier-1 example in the axis table* | Written 7/29 describing the **pre-fix** state. Size parity already shipped | 8 `body.text-lg` rainfall rules exist, not zero |
| 3 | Rainfall residual: *"Still open: tell her"* | **She was told 7/26** — `acknowledgedToHer: true` | `feedback-log.json`, `f2cd8a7` |
| 4 | `q-almanac-name` AWAITING HER ANSWER | **Answered Yes 7/29 8:54 ET.** Card is "Journal"; rename shipped; watermark released | `questions.json`, `10af162` |
| 5 | A2 W2: fairway + parking-bank undrawn, canon = 9 zones | **All 10 drawn 7/22** | `cf51af2` |
| 6 | Moss record is open | **Shipped 7/26** — her buttermilk slurry credited to her by name | `plants.json:4720`, `4bec1bd` |
| 7 | B6 naming pass awaiting content-steward | **Shipped** — `Machines`, three-way split | `viewer.html:11778` |
| 8 | `"Ask me later"` still on cards | **Does not exist** in any Mom-facing file; `check-cards.py:35` lints for it | grep: zero hits |
| 9 | Ambient keys at `viewer.html:6389-90`, then `6451-52`; also in the workflow | **`6540-6541`. Wrong for the third time.** Workflow uses `${{ secrets.* }}` — the real 2nd site is `tools/record-daily-rollup.mjs:28,30` | verified |

**⚠️ Correction #2 is the delicate one:** the axis table's own Tier-1 exemplar has shipped. **Delete
W8·b ①, don't fold it** — otherwise the typography pass re-fixes a fix. The axis itself is unaffected
and remains the right cut.

**Governing lesson, and it recurs:** *record the symbol, not the line number.* A stale line number on a
security item is exactly how it gets read as already handled — three times now on one row.

---

## 2 · TIER 1 · FIX NOW — nothing blocks these

Ordered by consequence. All agent-drivable; none needs an answer from anyone.

| # | Item | Why now | Size |
|---|---|---|---|
| **1** | **🚨 Bolores: the falsified tire size still renders, still stamped `verified`** | `specs.tires` = 35 (verified off the actual tires 7/29). `maintenance.tires` = **33**, `"confidence":"verified"`, still carrying the exact sentence *"Size read off the actual sidewalls"* that `7494b46` **proved false** — and it is **in Guru's digest**. The 7/29 fix reached one asserting line, not both. This is the project's own doctrine unmet: *a clear must reach every asserting line* | S |
| **2** | **🚨 Guru's digest holds a FAKE zone and none of the real ones** | `"Example: Front Beds"` (`zone-placeholder`) is in the digest; `eastern-patio`/`stable-grounds` score **zero**. The assistant carries a fabricated location and not one true one — on the surface Mom's voice walks and her map are built on. This is the 2,800 ft mechanism with the fabrication pre-loaded | S |
| **3** | **🚨 Every text box triggers an iOS Safari zoom** | All three inputs are under the 16px threshold — `.ui-textarea` 14, `.mom-queue-correction` 15, `.feedback-panel-input` 15.5. **She taps a box and the page zooms**, leaving her at ~1.2× with the layout wider than the screen. Three numbers. Never seen because nobody reviewed at 390px | S |
| **4** | **🚨 The carousel arrows silently destroy typed-but-unsent notes** | `prev`/`next` do `idx = …; render()` (`viewer.html:10175, 10190`) with **no read of the textarea**. The codebase already knows this hazard — `showAck(keep)` has an explicit no-wipe path commented *"her text stays exactly where she left it."* **The arrows never got the same guard.** Last silent-loss path in the loop; uncovered by `test-feedback-cycle.py` | S |
| **5** | **Guru recites falsified soil series 34×** | Cecil/Pacolet are Piedmont, capped ~900 ft; the property is 2,959 ft. Also still in `plants.json._meta.soilSeries` and `property.json.sources[]` — W9 claims property.json "is already corrected." **17** plants name them in `soilNotes`, not "~15" | M |
| **6** | **7 cards are `active:true` against a visible cap of 5** | `q-strategy-pollinators` and `q-weed-stiltgrass` **render to nobody** — stiltgrass has been served to no one while carrying a photo she took | S |
| **7** | **Retire the 3 un-reframed verdict cards** | Three of five visible slots are un-reframed bloom/verdict cards, two with **no "I haven't looked" label at all**. Retiring them makes `q-top-categories` the visible ask, lets stiltgrass render, and clears carryover contamination before any new experiment | S |
| **8** | **Two green affirmatives 190px apart meaning different things** | `Got it` (ack) and `That's all of them` (confirm) share a visual grammar, so *"I read your note"* and *"your guess is right"* are the same gesture. Directly corrupts the signal Paul steers on | S |
| **9** | **Fix the ask template once** — `harvest-questions.py:112` | Corrects **7** staged/live cards at a stroke. Subject = the thing on the property, never our claim; the hedge is *the record's* gap, said once, anchored with "here"; buttons describe what she'd see; the third button is a **state**, always present | M |
| **10** | **The blue collision on the rainfall card** | `.rain-cell.rain-active` navy (`viewer.html:1659`) is the same family as the regional block, so blue encodes both *"notable"* and *"regional source"*. Her own 4.42″ gauge figure wears it. Hue = source only; salience via fill + weight | S |
| **11** | **`CLAUDE.md` is wrong about its own codebase** | Documents `viewer.html` as "~4,600 lines"; it is **17,878**. Also claims JSON is fetched with inline as fallback — only 4 of 21 are fetched | S |
| **12** | **`check-mom-ack.py:229` asserts a behaviour that does not exist** | Claims `read-mom-zone-audio.py` "marks its own channel" — it never calls `mark_channel_read` (zero `momlib.` references). Confirmed exactly | S |
| **13** | **A live release note promises a feature that is gone** | `RELEASE_NOTES.md:80` — *"Anything you've starred stays starred"* — while the star UI is retired | S |
| **14** | **Sub-44px targets + the `✓`** | The 30px ack buttons are the only sub-44 targets in the stack. And **remove the `✓`** — a check is the completion mark in every icon library, already means *settled* elsewhere in this app, and sits directly above a queue of unanswered cards, so it reads as the first row of a checklist. Let the dated line lead | S |

---

## 3 · TIER 2 · CONFIRMED — she already answered; build it

| # | Item | The answer that authorizes it |
|---|---|---|
| **1** | **Make the Journal reachable** | She asked *"Is there a way to look back at these?"* and answered the naming card **Yes**. It is the **most-opened card in the app** (41 of 139 expansions) sitting **8th of 13 with no dashboard tile.** She asked to look back and still cannot find it |
| **2** | **Acknowledge the moss — a return leg, not an ask** | She gave it 7/26; the record has it, credited to her by name; **she has never been told.** Point the next ribbon at the moss record via the shipped `linkPhrase`/`linkCard`. Asks nothing, produces an object she can see |
| **3** | **Household systems currently renders to nobody** | 7 vehicle, 9 equipment, **0 household-system.** She proposed the category unprompted and derived the taxonomy herself. The cheapest possible demonstration that proposing something to this app makes it appear |
| **4** | **W8·c — rainfall month + year** | Her direct ask, 7/29. Station history is already local; presentation only |
| **5** | **Read `/api/feedback` by `context.section`** | The instrument itself. The data is already captured — nobody has ever read it by door |
| **6** | **Guru synthetic-conversation fix** (~15 lines, `worker.js`) | Test turns persist to `conversation:<id>`, which `/api/conversations` lists, which reads as an **arrival** — so probing makes Paul read as owing Mom a reply. Worse: a test conversation lands in the store **the Journal reads back**, so it is visible to Mom. One `origin` predicate at three call sites |

---

## 4 · TIER 3 · STEER — each carries its question and its capture path

*A row without both is on the kill list, per Paul's rule.*

| # | Question | Ask via | Capture path |
|---|---|---|---|
| **0** | `q-top-categories` — **in flight**, leads the queue | Card (live) | ⚠️ Unprobeable — **pre-schedule the hand-retire** (`active:false` + `resolvedAt`) or it pins the watermark exactly as `q-almanac-name` did |
| **1** | **The real discriminator** — zero-wrongness but **our** topic: *"We've never written down what's actually coming to the feeders this summer — only what the books say should be. From where you sit, are the hummingbirds still working the feeders, or have they thinned out?"* | ONE card, after Tier 1 #6–7 clear the queue | Needs a `_foldTarget` → a dated `observedHere` line on the Birds card, **in her name**. Answers → our-topic asks are repairable. Silence → topic origin binds and `harvest-questions.py`'s whole supply chain is dead |
| **2** | `q-fairway-grass-seedheads` — already staged verbatim | Flip `active:true` **in August** when seed-heads emerge | Existing fold path; second sample in the same cell as #1 |
| **3** | *"The last time something in the house needed a repair or a part — what were you trying to find, and where did you end up looking?"* | **Paul, in conversation** | Paul relays → B6. Two different builds hide behind one ask. Does not consume the card budget |
| **4** | *"When you wrote in that the rainfall number looked wrong — what did you figure would happen with that?"* | **Paul, in conversation** | Paul relays → the whole return-leg design |
| **5** | **Guru turn audit** — opens conversation content | **Paul ratifies**, not Mom | v1 needs no AI at all: the fact table gives exact strings, so `2,800` in an assistant turn is a regex hit. That shrinks the ask from *"AI may analyze conversation content"* to *"a script may grep our own output"* |
| **6** | **W6 instance model** — what is the real shape? | **Paul** | Design doc first. **Not Mom's** — asking her to adjudicate a schema is the exact class A3 just deprioritised |
| **7** | **Wildlife confidence markers** — 67 records assert an animal is present with no way to say "we think" | **Paul** | Schema call; see §6 |

**Pre-commit, in writing:** a miss on #1 is **not** evidence for the authorship hypothesis until the
input-stack cleanup ships and the card is re-offered on a clean surface. Otherwise a null gets over-read
exactly the way the A1 gate was.

---

## 5 · KILL LIST

| Kill | Because |
|---|---|
| **The moss card as an experiment** | The experiment already ran — `q-almanac-name` was the same cell (zero wrongness, her words, answerable from a chair) and was answered in a day. Moss is **her** topic, so all three hypotheses predict she answers: **it discriminates nothing.** And the record already shipped. Convert to a return leg (Tier 2 #2) |
| **W8·b ①** (rainfall type inversion) | Shipped 7/26. Deleting it prevents the typography pass re-fixing a fix |
| **The 80K digest gate** | A tripwire nobody acts on, computed by an estimator that under-reads ~13–15%, proxying a **$2.47 lifetime** cost constraint. It was crossed 16 days before someone wrote "back under the ceiling" |
| **"Does per-card Add-a-note earn its place?" as a question for Mom** (W7) | Verdict-shaped, about our own design, and answerable from telemetry we already hold (`context.section`) |
| **Add-a-photo-on-card** | Adds a **sixth** input affordance to the surface we are disambiguating |
| **"Tell her a wrong answer costs nothing"** | Reassurance the product has not demonstrated erodes rather than reassures. The queue header already says it once, correctly. Two mechanisms do the work instead: make wrongness structurally impossible, and fire a receipt at the disagreeing tap — *"Noted — the record had it wrong, and now it doesn't"* |
| **R2-vs-Drive backup row** · **candidates/devices into the digest** · **LLM-judge in harness v1** · **vector DBs** · **any framework/bundler migration** | No askable question, or over-engineering for a two-user app at 0.54 turns/day |

---

## 6 · The taxonomy question (folded in by Paul, answered here)

**The problem is not "weeds are plants."** It is that **the honesty marker — the thing this whole
project runs on — is expressed three incompatible ways, and 67 records cannot express it at all.**
Only `id` and `name` are universal across the ten domain files. `status` appears in six domains meaning
four unrelated things. Weeds carry the same fact twice. **Birds, mammals, amphibians, snakes, lizards
and fishing have no confidence field at all** — 67 assertions that an animal is present here, with no
way to say *"we think."*

**The domains are right** (Mom derived vehicles/equipment/household-systems herself and asked for tabs
by domain — two behavioural signals). **The record envelope is wrong.**

Proposal: a thin shared **envelope** (identity · `record.confidence{value, basis, askable, verifiedOn}`
· photo/attribution · zoneId) + per-domain **facets** (an attribute carrying its own confidence —
`variety`, `bloom`, and now `arrivalWindow` on a bird) + one **registry** that six hand-typed lists
derive from. One sentence unblocks the harvester: ***uncertainty lives on the record or on a named
facet, and the harvester reads both.*** Migration is expand-and-contract, five steps, **all
Mom-invisible** — step 3 still drafts `active:false` behind Paul's gate, so wiring the harvester does
**not** put cards in front of her, contrary to how that row is written today.

**The payoff that makes this urgent rather than tidy:** the taxonomy fix and A3's "replacement card
slate" are **the same work.** `harvest-questions.py` is a verdict-factory *only because it reads
plants' facets*. With the envelope it draws from ~154 records across nine domains — **and the wildlife
ones are observation-shaped by construction**, which is exactly the card class the evidence now favours.

*"Things I tend / fight / visit"* is a **card grouping, not a file boundary** — a record changes
relationship without changing identity (Virginia creeper is a native in `weeds.json`). That half is
already out to Mom as `q-top-categories`.

---

## 7 · Track A vs Track B — the ranking that has never been made

**Track A first, decisively — with one carve-out.**

- **Carve-out: B1's deadline-bearing GTI work stays on its own clock.** It is the only thing in the file
  with a real-world deadline; it does not queue behind UX.
- **Everything else in Track B waits.** Not because Mom's product matters more, but because **Track B's
  decisions come from Paul's own knowledge and are unaffected by the noise, while every remaining Track
  A decision is being made through a corrupted instrument.** Track B is *pausable without loss*; Track A
  is currently *accruing bad evidence*.
- **Exception inside the exception: B6 household systems is Track A wearing Track B's clothes.** She
  proposed it. It belongs in Tier 2.

---

## 8 · The proposed sequence

1. **Tier 1 #1–#4** — the four with a wrong fact or a data-loss path. Half a day.
2. **Tier 1 #6–#8** — clear and disambiguate the queue **before** any new card is offered.
3. **Tier 2 #5–#6** — make the instrument readable (`context.section`) and un-corruptible (`origin`).
4. **The input-stack consolidation** — three named doors (to-you / about-the-place / tell-Paul), one ask
   at a time, no two adjacent surfaces sharing a button shape or a green fill. **Fewer surfaces than
   today, not more.**
5. **Tier 2 #1–#3** — Journal reachable, the moss acknowledgment, household systems renders.
6. **Tier 3 #1** — the discriminator card, on a clean surface, with the null pre-committed.
7. Taxonomy steps 1–3, then the Guru harness.

---

## 9 · What needs Paul, and nothing else does

1. **Go / no-go on this proposal** replacing the `▶️ NEXT` table + TOP ITEM.
2. **Ambient key rotation.** ⚠️ Sequence matters and was previously wrong: the station call is
   **client-side**, so **rotating before a Worker proxy exists republishes the new key.** Correct order:
   proxy → rotate → strip. Exposed 84+ days; blast radius stays small (read access to one station).
3. **The zone map reads all-dashed** — all 10 zones are `draft`, and Paul has not eyeballed it. If that
   reads as *"nothing here is settled,"* the fix is to confirm the zones we trust, not soften the render.
4. **178 season notes await his spot-check** on the plants he knows best.
5. **Three relayed conversations** (Tier 3 #3, #4, and the naming follow-up) — the only interview leg
   the method has, given the app-only channel. Schedule them as first-class work.
