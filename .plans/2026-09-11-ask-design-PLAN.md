# ask-design · THE ASK PLAYBOOK — how this product asks a household for input, folds the answer into that household's own record, attributes it back, and reads it per release · first template: the weather card's card-intro ask

- row: BACKLOG.md § 🌱 A-ASK (decision card `.decisions/fernwood-11.md`) · § 🃏 CONTENT · CARDS · TIER 2 · 11's `ask` field (lap 9 · A)
- objective: O3
- class: engine · declared
- question: how does the product ask ANY household — not Fernwood, not Mom — for the input only they can give, so that the answer lands on their own record, changes what they see on the same screen, and is attributed back; and can one reader say what has been asked, answered and folded across every ask the product has made
- capture: deterministic and verbatim on every path in this plan — a tap → a DECLARATION on the household record (§4) plus a counted event; a typed line → the feedback store, bounded, `.private/` only. No model on the capture path, by rule
- seats: user-researcher → .user-research/2026-09-11-ask-design-READ.md
         content-steward → .content/2026-09-11-ask-grammar-DRAFT.md
         ux-expert → .ux-reviews/2026-09-11-ask-design-surface.md
         security-steward → .engineering/2026-09-11-ask-design-SECURITY.md
         ai-advisor → .ai-advisor/2026-09-11-ask-design-boundary.md
         engineering-partner → owed, not waived: the ledger SPEC in §9 is written here from the lap-8 plan's R0 placeholder; its BUILD is engineering-partner's lap-8 rider and the seat re-audits the spec at lap 8's open (`.plans/2026-09-11-lap8-build-PLAN.md` R0: "where the two disagree, that plan wins"). Two live defects security found (§11) are engineering's to fix, not this plan's
         practice-steward → waived: §10 maps the per-release reading onto beats that already exist and adds none; if a lap shows the mapping needs a beat, that is a practice-steward audit, commissioned then
- depends-on: .plans/2026-09-07-weather-card-PLAN.md
- depends-on: .plans/2026-09-11-legacy-toolchain-INVENTORY.md
- depends-on: .plans/2026-09-10-build-description-chain-DESIGN.md
- depends-on: .plans/2026-09-11-lap8-build-PLAN.md
- ready: agent-proposed — Paul rules (§13). Written by the ASK DESIGN window (`handoff/handoff-ask-design.md`, brief at `ef84c20`; readback graded clean by coordination) `[paul-ruled 2026-09-11 ~1:50 AM ET: "I say go on both"]`
- stage: concept
- stage-note: 2026-09-11 — the DESIGN artifact is complete (every seat declared with a trail or a reason); the `design` rung is claimed when Paul stamps `ready:`, not before — `check-backlog-ready.py` reads a design with no stamp as built without the gate, and it is right to. DRAFTED at `e7c566f`+ in a design window that touched no surface, no BACKLOG.md, no CLAUDE.md, no VOCABULARY.md. Five seats convened in parallel with one bounded question each; this file synthesizes and CITES them — where two seats disagree, §13 names both and recommends. ⛔ Nothing here ships from this window: every string is a DRAFT for Paul's confirmation, and the weather ask is lap 9 · A's to build.

> ⭐ **THE ONE-LINE.** An ask is authored content the product puts in front of a person; its answer is that
> person's, captured verbatim, landed on their household's own record as a **declaration**, read by the card
> that asked **on the same screen**, attributed back where a ribbon exists, and counted by one reader — and the
> product asks **only for what it cannot derive.**

> ⭐⭐ **THE LEAD SEAT'S FINDING, AND IT REORDERS THE WORK** (`.user-research/…READ.md` §0, `validated`): **an ask on
> this product has never once been shown to change what the person who answered it sees.** Every ask ever
> answered here changed something the person was shown next (Mom's two taps; Paul's full ranking); every ask that
> changed only what WE know is in the zero column. So **the receipt outranks the questionnaire** — if only one of
> the two can ship, ship the visible receipt on a smaller ask. §4 and §5 exist for this.

**What each seat returned, one line each** (the trails are cited throughout; this is the index):

| seat | trail | the one line |
|---|---|---|
| user-researcher (LEADS) | `.user-research/2026-09-11-ask-design-READ.md` | R1–R6; the W-10↔09-11 tension is two ACTS (provisioning at setup, curation at the card); a multi-select is ONE asked field; the journey with four failure paths, one of them today's measured state; the beat-3 line |
| content-steward | `.content/2026-09-11-ask-grammar-DRAFT.md` | the grammar in nine rules; the weather ask DRAFTED (recommended + alternate) with nine per-sentence falsifiers, two red today; eight questions for Paul |
| ux-expert | `.ux-reviews/2026-09-11-ask-design-surface.md` | placement E (the split, drawn one notch later than the weather plan); the close in the card at runtime; the cap on `_ordering`'s axis; `renderAskNext()` = one component, two hosts; ten findings, two critical |
| security-steward | `.engineering/2026-09-11-ask-design-SECURITY.md` | the ESTATE is the subject, any member writes, UNION never election; who-sees is the clause that makes the record legal; health-adjacent; the ledger never per-estate; two live defects |
| ai-advisor | `.ai-advisor/2026-09-11-ask-design-boundary.md` | the >10 threshold does not govern an intro ask — a three-cards gate; the model reads the PRODUCT never the PERSON; served deterministically, never by the Guru; fernwood-11/12 are opposite in boundary terms |

> ⛔ **WHAT THIS IS NOT.** Not a build (lap 9 · A builds the weather ask; lap 8 R0 builds the ledger) · not a
> ruling on `fernwood-11` (§7 recommends; Paul rules) · not a licence to ask more (the elicitation ruling inverts
> that: FEWER fields, many derived facts) · not a second home for Mom's confirm-card lifecycle, which stays exactly
> as CLAUDE.md § Mama's Perspective states it and is CITED here as the first ask family.

---

## 0 · Paul's words — the rulings this file is built from, verbatim, dated

| when | his words | what it fixes here |
|---|---|---|
| 2026-07-29 | *"The card queue is ordered by INFORMATION VALUE TO US"* (`questions.json._ordering`) | the ordering axis (§3) — cited, not re-derived |
| 2026-08-04 | *"we want to be clear in messaging as she gets used to providing feedback that everything is changeable… without beating her over the head with it"* · *"eventually we can stop really mentioning that"* | the changeable clause and its decay (§6) |
| 2026-08-04 | the ribbon is *"we heard you… we actioned these things because of you"* · *"we don't wanna add all that wording"* | attribution by structure (§5) |
| 2026-09-01 | *"whatever she's interested in is what we need to latch onto"* | prefer instrumenting a door they open over authoring an ask (§3) |
| 2026-09-06 | *"Ask them what they want to see next. Ask questions about what to show rather than show empty stuff."* | `renderAskNext()` — the dormant card-intro ask (§1, §3) |
| 2026-09-07 | *"each backlog item associated with a telemetry ask and check"* — the four-field contract | every ask ships as a row field (§10, P2) |
| 2026-09-07 (W-10) | *"Six sounds good."* → the radar/station opt-ins sit BESIDE THE ADDRESS at setup | the setup site for PROVISIONING asks (§3) |
| 2026-09-07 (W-13) | *"let's use that as fodder to ask people"* — the advisory layer | the weather ask's fodder, not its answer (§8) |
| 2026-09-10 | *"are we asking the right questions to really drive personalization for each account and estate at each step?"* — and it is NOT "ask more" | the elicitation rule as a check (§3) |
| 2026-09-11 ~1:15 | *"ask questions when we first introduce a card, like the weather: are you interested in UV, air quality? What do people want from a data point of view in their dash view? I think that little questionnaire helps us then decide what are the different sub-components of weather that we present and how we highlight it."* | the card-intro ask; the INTENT the shape must serve (§3, §8) |
| 2026-09-11 ~1:50 | *"I say go on both."* | this window and the ledger rider |

---

## 1 · What exists — the record, measured at `e7c566f`, so nothing below is designed twice

| piece | where | state | what it teaches the playbook |
|---|---|---|---|
| the confirm-card lifecycle (harvest → bench → serve → answer → fold → ribbon) | `harvest-questions.py` · `rationalize-bench.py` · `MomQueue` · `fold-answer.py` · `momlib.question_state()` | live at Fernwood; declared absent at `paul`, `home`, `qa` | the FIRST ask family. Its gate (a human `--approve`), its cap (`MAX_VISIBLE` 5, effective 1), its axis (`_ordering`) and its fold are borrowed below, never restated |
| the answer record | `questions.json` — 22 cards: 5 `resolved` · 5 `unprobeable` · 1 `open` · 11 `draft` | `momlib.question_state()` | **5 answers settled and folded** in fourteen months (ai-advisor §1 names them); `momqueue_tapped` 3 in 60 days. ⚠️ The *"0-for-35"* reading is N exposures of ~1 distinct card, and that card was defective (`q-weed-stiltgrass`, head slot 08-03→08-24) — **the distinct-`questionId` count is still unrun** (user-researcher §3.1; forward row) |
| the onboarding ranking | `onboarding/index.html` `INTERESTS` (11) → `POST /api/feedback` `{type:"onboarding"}` | live; read by `read-onboarding.py` | the product's **primary learning instrument** (its docstring); captured with no wording stamp (TIER 1 · 36); reaches the app as display copy only (INVENTORY §4·3) |
| **the dormant card-intro ask** | `engine/viewer.template.html:18522` `renderAskNext()` | **dead in both branches** (`:18525` and `:18527` — the resting is deliberate, the second gate is not what the comment describes) · `ask_next_added` has no reader · chips have no selected state (a tap makes the chip vanish) | the nearest existing shape to Paul's ask, at MODULE granularity. ux-expert §4: **one component, two hosts** — keep it, fix three things, host it at sub-component scope inside a card |
| the ask contract, in code | `tools/elicitation-lens.py` `CONTRACT = {use · not-use · who-sees · reversible}` | live as a reading posture (`fernwood-17`) | ⭐ the grammar's four clauses already exist as a check. §2 cites them; security §1 makes `who-sees` the clause that makes the record itself legal |
| a declaration on the household record | `worker.js:1402` `writeEstatePlace()` → `{…, declaredBy, declaredAt, placeSource}` | live (the place) | the MODEL for where a preference lands (§4) — security: *copy it field-for-field* |
| the ribbon | `engine/viewer.template.html:12022` `MOM_ACK_DATA` — a concrete literal | build-time; no per-household seam (TIER 1 · 50); lap 8 row G gives it an instance seam | attribution is unbuildable for any household but Fernwood until G lands, and for a FOUNDED household until a runtime ribbon exists (§5) |
| the four-field contract's carrier | chain design P2: `ask · telemetry · ribbon · note` on the committed row | **ruled, not built** — zero `ask:` keys in any plan | the ledger's intended input (§9); until built the ask field is register prose |
| readers per channel | `read-mom-feedback.py` · `read-onboarding.py` · `watch-feedback.py` · `elicitation-lens.py` | live | none joins served → answered → folded → row. That join is the ledger (§9) |
| tonight's worked ask | `.content/2026-09-11-recovery-copy-DRAFT.md` — Paul-confirmed | drafted; B6/B16 build it | the FORMAT for an ask draft, reused by the content trail |
| the existing change controls | `/settings/place/` holds name · journal name · colour; `#card-told` says *"change it whenever you like"* of a contact preference | ⛔ **no control exists at either site** (ux-expert F2, `template:19989`) | EVERYTHING IS CHANGEABLE is already claimed falsely once; a second preference must not ship the same way |

---

## 2 · THE GRAMMAR — `.content/2026-09-11-ask-grammar-DRAFT.md` §3, nine rules; the four that bind every future ask

1. **The four contract clauses in ≤3 sentences, in this order: derivation → use → audience → reversibility.** Phrase-presence is what the lens detects (*used to · nothing else · only you / Paul · change / whenever you like*) — ⭐ **written because they are true, never to pass the needle**; a clause that passes the lens and is false is worse than an absent one.
2. **Ask about the WANT, never the VALUE.** A person cannot be wrong about what they want — which is why an interest ask is the one ask class in this product with no wrong answer, and the one safe for a reader whose fear is getting it wrong. (content B2: the harvest bank's central move — *our claim in the subject position, graded by her* — INVERTS on an interest ask; never lift that template onto this one.)
3. **ONE affirmative grammar** — filled green + ✓ on the act that writes; secondary = outlined neutral, **named for the state of the card, never the reader**: *"Leave it as it is."* ⛔ Never *Not now / Skip / Maybe later* — `check-cards.py` lints deferral-shaped labels and is right to. ⚠️ The bank has **no multi-select grammar** (B4); the chip pairing in §8 is an EXTENSION of rule 1, and Paul rules its form (§13·4).
4. **The receipt credits, it does not thank, and it does not narrate itself** — *"UV and pollen — you asked for these."* Four words, under the thing, no ✓ (the glyph was spent on the tap). And it asserts the act performed and no act beyond it: no *"next time you open it"* until the write survives a reload (F7).

Also binding, cited: one narrator and no *"we"* `[paul-ruled 2026-09-05]` — ⚠️ **all 22 live harvest prompts say "we"** (content B1); the confirm queue and any new ask will speak in two voices on one screen until the bank is re-voiced (forward row). What an ask never says: apology · reassurance-for-its-own-sake · praise of the answer · a time claim · a completion claim without a write · a notification promise (there is no channel) · a count of what is unanswered.

⚠️ **One edit the security read forces on the recommended draft before Paul sees the words:** *"only you and Paul can see them"* is FALSE at any estate with a second grant — the declaration lives on a member-readable estate row (§4a). The who-sees clause must name **the household**: *"everyone at this place can see your picks, and so can Paul."* Security §1: this clause is not decoration; without it the record is out of tier.

---

## 3 · WHEN the product asks, the SHAPE, and the CAP — user-researcher §2–§3 · ux-expert §1, §3

### 3a · Two kinds of ask, two sites — the W-10 ↔ 09-11 tension is two different ACTS, not a contradiction

> **PROVISIONING asks belong at setup, beside the address (W-10). CURATION asks belong at the card, on its face, at its first appearance (Paul, 09-11).**

| kind | what it is | site | examples |
|---|---|---|---|
| **provisioning** | a fact about the PLACE that must be answered before the card can be built that way — a credential, a fetch we will not make unasked, an applicability fact the address cannot give | setup, beside the address — *where the promise about their data is made* | the household's own station (W-6: a *yes* unlocks live readings AND starts accrual) · the radar |
| **curation** | what an EXISTING card emphasises — costs nothing to build, nothing to reverse, answered better by a person who has seen the card, **and the referent is on the screen** (recognition, not recall) | the card's own face, first appearance, born open | UV · air quality · pollen · wind · frost/freeze · dry spells |

⛔ **The binding clause (R2):** a curation ask may never gate the card. **Falsifier:** if the weather v1 cannot render a useful face before the curation ask is answered, R2 is wrong for this card and the ask moves to setup.
⚠️ **This recommends AGAINST one line in the weather plan** — `0-PRIME-C`'s *"one multi-select at setup plus a free text"* for the eight advisory classes is that plan's EXTRAPOLATION of W-10, which ruled only the two opt-ins. Both seats flag it; **Paul rules** (§13·1). ⚠️ The seam: a person who declined radar at setup must not be re-asked at the card — one declaration, two doors; and the station has a curation half (*foreground its numbers?*) that rides the card's chips only where the household said yes at setup.

### 3b · The four moments, graded (user-researcher §2)

| moment | evidence | grade | falsifier |
|---|---|---|---|
| setup | W-10; the one moment attention is already committed | ruling `validated` · attention `assumption` | a setup step's completion rate falls when opt-ins are added |
| a card's first appearance | Paul's words; the referent is on screen | intent `validated` · effect `assumption` | ⭐ **the ask's view rate at or below the depth-2 rate (0) means the SITE is wrong whatever the content** — face, or retire it |
| after a signal the person gave | ⭐ the strongest siting evidence in the record: **both** asks Mom ever tapped originated in something she said first | `validated` (two taps) | an ask with no antecedent answers at the same rate — then the antecedent was never the variable |
| a standing ask | ⛔ never — `feedback_defer_affordances_pending_signal` | doctrine | — |

### 3c · The SHAPE — a finding, not an assumption (user-researcher §3; ux-expert F5)

> **Paul's *"little questionnaire"* and the elicitation ruling never conflicted.** The lens's metric is derived-facts-per-asked-FIELD — it constrains what a person must SUPPLY. A multi-select of chips is **one asked field with N options**; nothing typed, nothing derivable. The compression to *"ONE ask"* came from the confirm queue's cap (effective visible set 1) — **and the card-intro ask is not in that queue and does not spend that slot.**

What the person needs to be able to say: **show me this** (chips) · **not this** (an explicit decline, recorded DISTINCTLY from silence — R4) · **something you didn't list** (one free-text door — R5, the shape that produced *"Houseplants!"*) · **I'll change my mind later** (and it must be TRUE, from the card) · ⚠️ *this one, only when it matters* (a threshold, not a presence — flagged by the researcher, untested; §13·13).
**Bound:** ≤5 chips on the face, applicability-filtered by W-9 first (ux F5: eight chips ≈ 300 px of ask above the card's content at 414×A+); the remainder lives in Settings, never behind a disclosure. **Falsifier for the free-text door:** if it returns nothing across the first ten households while chips return selections, cut it; if it returns a class never offered, it is the most valuable control on the surface — which has already happened once, at n=1.

### 3d · The CAP, as a rule on `_ordering`'s existing axis (ux-expert §3) — no new axis

1. **One ask per SCREEN** (not per card — *ONE INVITATION PER MODULE* is already in code for this reason).
2. **One introduction at a time**, in `READER_RANKING` order; the intro ask rides the introduction and dies with it.
3. **A card-intro ask is BUILD-class** on `_ordering`'s axis (its answer changes what renders), so it outranks canon-gap and verdict cards — **and therefore suppresses the confirm queue for that load** rather than sitting beside it. Two asks on one screen is a 1-slot budget spent twice.
4. **Bounded by construction:** offered at most TWICE, only while its card is being introduced; then it retires into the change control (§5b). That bound is what stops build-class asks starving the canon queue. **Falsifier (researcher):** if the second offer converts at a materially different rate from the first, exposure was the variable and the bound is the wrong instrument.
5. **Open at once, per household: at most one.** Anything beyond benches through the existing `--approve` gate. No second queue.
6. **Silence is not a no** (R4): `unanswered` and `declined` are different records and never render the same — the project has already spent two research passes reading one silence as a verdict.

### 3e · The elicitation rule as a CHECK — and the derived-not-asked list for the weather card
Never ask for a VALUE the address derives: UV index · AQI · climate normals · frost dates · hardiness · elevation (W-7 makes each of these a CONFIRM at the place card — a different instrument, the weather plan's) · sunrise/sunset · the region label. The card's PRESENCE derives from the ranking. The radar and station opt-ins are provisioning (setup). **What is left is small, and that is the sign the ask is well-sited, not a problem.**

---

## 4 · THE FOLD — an answer lands on the household's own record, and there are TWO substrates

| ask family | what the answer IS | where it lands | the fold's write | who reads it |
|---|---|---|---|---|
| **a CANON-FACT ask** (Fernwood's confirm cards) | a fact about the world the person can check | `_foldTarget` → a field in instance JSON via `fold-answer.py`, re-inline, deploy | a **human-approved canon edit** | the provenance chip |
| **a PREFERENCE ask** (the card-intro ask) | a fact about the PERSON — what they want shown | ⛔ **nowhere durable today** (INVENTORY §4·4: module state is a BUILD artifact; `renderAskNext()` writes `localStorage` + a feedback record nobody reads) | **a DECLARATION on the household record**, written by the capture path itself — a preference needs no human in its fold | the card, at render, on the next page load |

⛔ **A family of intro asks shipped as `_kind: reflective` cards would PIN THE FEEDBACK WATERMARK BY DESIGN** (INVENTORY §4·2; ai-advisor §2 names it the loop's blocking prerequisite): a reflective card is the one state canon can never clear. **The declaration fold target must exist before ask #1 ships.**

**The declaration, PROPOSED — security-steward §1 rules the tier; copy `writeEstatePlace()` field-for-field:**

```
<estate record>.declarations["weather-intro"] = [          // a UNION across people — never a single winner
  { value: ["uv","pollen"],                                  // verbatim ids as shown; a decline is value: [] with declined: true
    wording: "<the label set shown — TIER 1 · 36 generalized: an answer rides with its wording>",
    declaredBy: <personId from the RESOLVED GRANT — never a literal; declarePerson() throws on one>,
    declaredAt: <ISO>, declaredVia: "card-intro",
    changedFrom: <previous value | null>,                    // makes EVERYTHING IS CHANGEABLE visible and true
    clauseVariant: 3 }                                       // which changeable clause was shown (§6, no two consecutive the same)
]
```

- **SUBJECT: the ESTATE, never the grant** (security ✅ — a grant is authorization class; widening it drags preferences into `fernwood-private/grants.json` via `PLACE_FACTS`). **Any member may write** — the first member-authored estate-record write in the product, and the ruling that costs input (owner-only) is refused by name: Mom is a member at a house she does not own.
- ⛔⛔ **UNION, NEVER ELECTION.** `writeEstatePlace()`'s own comment records the defect: electing one row by rank put a real address into a test estate's prompt *"because every estate had exactly one placed member."* A preference is a SET across people; each element carries its own `declaredBy`. Free to get right today; a migration the day two people have one.
- **Where the estate record lives:** the per-estate KV row W-8 ruled for the station credential, the history store and estate-persistent notes — this is its fourth consumer. The weather plan's D2 already says the radar answer *"becomes the estate's declared switch"*; the declaration IS that switch, held where a page load can read it. INVENTORY §4·4's blocker closes by this, not by a rebuild.
- **The capture record — RECOMMENDED: NO feedback record for a chip tap.** Three seats converge: content Q6 (a pick POSTed to `/api/feedback` becomes an ARRIVAL in the mom cycle and makes *"used for this card and nothing else"* false) · security §2 (if one is written: `context.type:"card-interest"`, `surface` omitted, attributed only via `attributeTo` from the resolved grant, ⛔ `deviceId`/`sessionId` forbidden beside a personId, ⛔ never the derived value) · ux (a preference is about the APP, the queue is about the WORLD — two acts at one door). So: the declaration is the record; a counted event `ask_answered {askId, chosen:<n>, declined:<bool>}` feeds the ledger; `watch-feedback.py` must never print a preference as an arrival. **The free-text line is different** — it IS her words and goes to the feedback store, bounded, verbatim (§4a). Paul rules (§13·6).
- **Falsifier (INVENTORY §5.3, adopted; researcher failure path (b)):** tap, reload — if the card is byte-identical, the ask is not shippable. One minute to run.

### 4a · The tier — security-steward's roster, the rulings that bind the build (`.engineering/…SECURITY.md`)
- ✅ the declaration on the ESTATE record, any member writes, union · ✅ the ribbon attributes the ACT and the PLACE · ✅ the free-text box, **prompt BOUNDED to the card** (*"what else about the weather at this place should the card show?"* — an unbounded *"anything else"* invites health, absence and neighbours into a tier that cannot hold them), verbatim, `.private/` only · ✅ the ledger per-ask, per-env.
- ⚠️ **must change in spec:** the ask discloses WHO SEES the answer before the tap (the household, and Paul) — without it `declaredBy` on a member-readable row is out of tier · union never election · the ledger never per-estate (§9) · free text gated per estate on the administrator's relationship or an `administrator-reads` consent entry (**RR-8, proposed**) — ⚠️ the seat could not open `../fernwood-private/.plans/2026-09-02-data-model-design.md` §7 and ruled from CLAUDE.md's paraphrase; **someone reads §7 directly before that gate is built.**
- ⛔ **must not:** the preference on the grant · a single-winner preference · a derived value (a UV reading) stored beside a person · *"your answer changed this"* on any surface an estate with >1 grant can render · a per-estate answered-count at production or legacy.
- ⭐ **The finding that is new:** weather-advisory interest is **health-adjacent** (asthma, allergies, sun sensitivity, a child) — both the researcher (§1.3) and security (§1) reached it independently. The 09-02 up-front-agreement duty was written for notes and voice; nothing covers an inference about a body, and at Bob's houses the administrator is a stranger. **The remedy is disclosure, not suppression** — stripping `declaredBy` would kill the only trust credit the ask generates.

---

## 5 · ATTRIBUTION — the same screen first; the ribbon second, and only where one exists

### 5a · The close is IN THE CARD, at runtime, immediately (ux §2a · content §1b · researcher R3)
The tap changes the thing under the thumb: the sub-component appears **in place in the same card** with a quiet first-run tag — *"UV and pollen — you asked for these."* — that decays after a set number of opens. ⛔ **Do not gate the close on the ribbon**: the ribbon is a build-time literal until row G; a close that requires a rebuild is not a close.
⚠️ **The tag's second-person form renders only where the estate holds exactly ONE grant, computed at render, never assumed** (security §5·2). At a shared house the form is act-and-place: *"UV and pollen — asked for here, 16 Sep."* Content-steward drafts that variant next; the single-grant assumption is the one that put a real address in another estate's prompt.

### 5b · The none state and the change control (ux §2b–c · content §1d)
- **Chose nothing → no ribbon line, no told-row, no *"you chose nothing"*.** The card renders its base set in its ordinary voice; the ask retires after its second appearance.
- **After retiring, the ask demotes to one quiet line at the foot of the card body — the CANONICAL change control:** *"Showing: UV · pollen · **Change**"* (content's *"More for this card ›"* is the none-chosen form). **Mirror in `/settings/place/`**, which holds the FULL list including classes the card is not showing. `#card-told` gets a read-only receipt row that LINKS to the card — a reference, not a second editor. ⛔ **Turning a thing OFF must never remove its own control** — that is why the Settings mirror is load-bearing, not optional. **Falsifier:** a person shown their card and asked how they would remove air quality walks straight there.

### 5c · The ribbon — where it stands, measured
| household | ribbon today | what the attribution leg needs |
|---|---|---|
| Fernwood (`legacy`, Mom) | `MOM_ACK_DATA` literal — live, correct | nothing new; a declaration-driven line is one more `links` entry |
| an INSTANCE-FILE household (`paul`, `home`, `qa`) | the SAME literal — Mom's ribbon at Paul's condo (TIER 1 · 50) | **lap 8 row G** — G1 instance-supplied; G2 *"none is the honest empty"* |
| a FOUNDED household (J0 — no file under `instance/`) | ⛔ **unreachable by construction** — a build-time seam has nothing to substitute | a RUNTIME ribbon reading the household's declarations and dispositions from the record. **In no lap.** Forward row (§12) |

**The rule for whether a preference earns a ribbon line at all** (content §1c, proposed as a principle): **a card-intro ask earns a ribbon line only when its answer changed something the reader can go and look at.** *"Leave it as it is"* earns none; a ribbon that fires on every ask is a receipt machine, which is the changelog failure in ribbon clothes. The line's grammar: *"<date> — what your picks changed:"* + one phrase per declaration, `links:[{phrase, card}]` — and at a shared house, no *"you"* (security §5).

---

## 6 · THE DECAY of "changeable" — cited, plus the two rules this file adds

CLAUDE.md standing rule 5 binds (one short varied clause on the thing they just gave; never a footer; never twice running; retired on Paul's read; and TRUE). Content §3·8 supplies the bank (five variants; the variant used rides the declaration as `clauseVariant`).
1. ⛔ **The clause may not be said at all until an off-switch exists** (content Q5, ux F2). Lap 9 · A builds the *Change* control (§5b) or the clause is CUT, not softened. Saying nothing beats saying it falsely.
2. **Retirement per household, by evidence of the act:** the clause retires for a household once a declaration there carries a non-null `changedFrom` — they learned it is cheap by doing it. For Mom, retirement stays Paul's read (08-04). **Falsifier:** a household that changed one answer never changes another → the clause retired too early; revert to per-ask.

---

## 7 · AI IN ASKS — `.ai-advisor/2026-09-11-ask-design-boundary.md`; the three rulings for Paul

1. **The ">10 answered across reseed cycles" threshold does NOT govern a card-intro ask — it measures the wrong thing.** It is a cost-benefit gate on the CONFIRM loop (*"phrasing was never the bottleneck"*), asking whether the harvester mints enough near-identical cards for phrasing labour to recur. An intro ask is authored once per CARD. And the count, said out loud: **5 settled answers in fourteen months; the confirm-card gate is not met and nothing here opens it.** **Recommended replacement gate: count CARDS — hand-author until the same ask has been written for three cards and the third is visibly the same shape as the first.** Falsifier both ways: card 3 diverges → no template, gate stays shut; cards 1–3 so alike a deterministic bank produces them → **the model's seat never opens, and that is the likelier and better outcome.**
2. **If a model may draft — the definable loop is drawn in the trail (ten steps, ONE model seat at step 3), with structural containment:** forced tool-use whose `options[]` enumerate the card's real sub-components and whose `foldTarget` enumerates household-record keys — an ask for a thing the card cannot render has nowhere to land. **The model reads the PRODUCT, never the PERSON:** ✅ sub-components, grammar, the taxonomy as a shape, prior authored asks · ⛔ this household's ranking (modes 4, 8) · ⛔ address-derived facts (step 2 subtracts them deterministically; handing the model a forbidden set is strictly worse) · ⛔ **prior ANSWERS, any household — the clause most under pressure, ruled explicitly: no** (modes 1, 4, 8; that reading is the administrator's, off the ledger). Pre-registered self-improvement: the administrator's EDIT rate — >50% rewritten → the seat closes; zero rejections and zero edits across three cards → demote to a template and delete the model call.
3. **`fernwood-11` = keep-asking-and-instrument-her-doors · `fernwood-12` = extend-the-fence (household-system, vehicle/equipment first).** The two cards are usually spoken of as one direction and are OPPOSITE in boundary terms: Guru-as-CAPTURE puts the model's understanding, not her words, into the record — modes 1 and 4 by construction, unenforceable rather than amended, and it fails physically where there is no signal, which is where she stands when she has something to say. ⭐ **The point specific to this window:** a conversationally delivered intro ask is not an ask/capture violation — but it IS a gate violation, because a runtime-composed ask cannot be human-confirmed before it reaches a person. **So the card-intro ask is served deterministically from the card, never by the Guru.**

The trail's §5 drafts THE RULE for AI in asks in the boundary's own in/out/administrator form — **proposed for `~/.claude/ai-playbook/fernwood.md`, not written; Paul confirms first.**

---

## 8 · THE WEATHER CARD'S CARD-INTRO ASK — the first template, four fields (DRAFT — nothing ships from here)

| field | value |
|---|---|
| **ask** | content-steward's recommended draft (`.content/…DRAFT.md` §1), on the card's face at first appearance, born open: title *"What else do you watch the weather for?"* · two sentences carrying derivation → use → audience → reversibility (⚠️ with the who-sees edit from §2: the household, and Paul; ⚠️ and the changeable clause CUT until the *Change* control exists) · chips **≤5 on the face, applicability-filtered** from the six the seat kept (UV · Air quality · Pollen · Wind · Frost and freeze · Dry spells — ⛔ *Severe weather* and *Fire weather* CUT: warning-shaped, and there is no push channel; an advisory opted into and not received in time is worse than one never offered) · the free-text **door** (ux: the existing `.empty-invite-ask-btn` → `FeedbackRibbon.open({section:"card:weather"})` pattern, not a textarea on the face) with the **bounded** prompt *"What else about the weather at this place should the card show?"* · affirmative/secondary per §13·4 · **derived, never asked:** §3e's list |
| **telemetry → reader** | `ask_served {askId, exposure:1\|2}` and `ask_answered {askId, chosen:<n>, declined:<bool>}` → **`tools/ask-ledger.py`** (§9); the declaration → the card at render (the visible receipt IS the reader a person sees); the free-text line → `read-onboarding.py`'s WHAT'S MISSING (it reads that store). ⛔ Both readers named or the field is `none — <reason>` |
| **ribbon → card** | *"<date> — what your picks changed: UV and pollen are on the weather card now"* → `card-weather` — **only where a ribbon exists at that household (§5c), only when the answer changed something visible, and never with "you" at a shared house.** Otherwise the in-card tag is the attribution |
| **note** | `RELEASE_NOTES.md` *"The weather card asks what you want on it"* — lap 9 · A's, not this window's |

**The journey it must survive** (researcher §4): arrives → reads the face → sees the ask ON THE FACE (in a body it does not occur: depth-2 = 0; the `wide-eyed` seat opened none of four collapsed cards) → taps → **the card changes on the same screen** → returns and it remembered, the ask gone → changes it later from the card. **Failure paths, each with its rule:** answers nothing → defensible default, `unanswered` never `declined`, at most two offers · **answers and nothing changes → TODAY'S MEASURED STATE** (R3 exists for this) · cannot find how to change it → the control is on the card (§5b) · a second member lives there → the answer carries its author, the card says whose preference shaped it or curation is per-person, the who-sees clause names the household — and the within-estate cross-person instrument (board ⑤·1) is a precondition of shipping into a multi-member house.

---

## 9 · THE ASK LEDGER — `tools/ask-ledger.py`, SPEC (the build is lap 8 R0; this spec wins where they disagree)

**One question, on its face:** *what has this product asked, how often, what came back (as counts), and where did it go?* ⛔ **What it does NOT answer:** whether an ask was GOOD (`elicitation-lens.py`, cited by row) · WHO answered (never a person; per-env only) · whether a fold was RIGHT (`momlib.question_state()` says).

### 9.1 · Inputs, by file, each with its UNREADABLE condition (exit 3, never green by absence)
| input | supplies | UNREADABLE when |
|---|---|---|
| the committed rows' four fields — **P2's carrier when built**; until then `BACKLOG.md` row prose | the ask each item ships with · its reader · its ribbon target | ⚠️ P2 unbuilt. Fallback: parse the row's `**ask**` cell; a row with no findable cell prints `UNREADABLE — no ask field on <row>` per row; exit 3 while any committed row is unreadable. **P2 is the named dependency**; the carrier wins over prose where both exist and the disagreement prints |
| `questions.json` + `momlib.question_state()` | every confirm/reflective card and the ONE definition of settled — ⛔ imported, never re-derived | missing / unparsable / import failure |
| `engine/asks.json` (new, PROPOSED) — `[{askId, family:"card-intro", card, wordingVersion, _source:"authored"\|"drafted", addedAt}]`, the sibling of `questions.json` for asks with no entity | the card-intro register; `_source` so drafted-vs-authored is readable (ai-advisor step 6) | absent → `no card-intro asks registered` (a fact; exit 0 for this input only, on the day it ships) |
| the metrics store per env — `ask_served` · `ask_answered` (and `momqueue_offered` for the confirm family) | served and answered as COUNTS — ⭐ **DISTINCT asks, never exposures** (researcher §3.1: an offer count without its distinct-ask denominator has misled this project once) | no token · unreachable · **a legacy unprefixed key era** (absence under a prefix is a fact about the prefix — `watch-activity.py`'s trap) · **`served` derivable and `answered` not** (a ratio with an unknown denominator is the false-green this corpus is built against) |
| `GET /api/onboarding-metrics` | the ranking's served/offered | **lap 8 R1** — until then `UNREADABLE — R1` |
| the estate record's `declarations` read route | what is currently in force per ask | does not exist until lap 9 · A → `UNREADABLE — no declarations route` |
| `.private/feedback-log.json` | where each free-text note went — ⛔ **structurally unable to read a note**: the tool's inputs are registers and counts; a tool that CAN read a note will one day print one | absent → the disposition column is UNREADABLE |

### 9.2 · Output — one row per ask, per ENV. ⛔ NEVER PER ESTATE, at any size (security §4)
`legacy` is Mom alone; `home` and `paul` are one account each — a per-estate row is a person's answer with a number in front of it, and k=2 is not anonymity either. Per-estate reading belongs to the administrator's own read of their household, not to a portfolio instrument. Where an env's n is 1, the row prints **`n=1 — not reported`** (a state distinct from `0` and from `unread`) — or the env is omitted and the omission printed, if even that string says too much (Paul's call, §13·11).

```
ask-ledger · env=qa · P2 carrier: ABSENT (reading row prose — 3 of 5 committed rows UNREADABLE)
ASK                    FAMILY      SOURCE    SERVED(distinct)  ANSWERED  DECLINED  FOLDED INTO                    LINKS TO       LENS
q-clematis-variety     confirm     authored  12                1         0         plants.json variety.confidence  TIER 2 · 3     cited
q-strategy-pollinators reflective  authored  4                 1         —         unprobeable BY DESIGN           A-ASK          —
onboard-interests      ranking     authored  UNREADABLE(R1)    33        —         READER_RANKING (display only)   TIER 1 · 36/37 —
weather-intro          card-intro  authored  0                 0         0         declarations.weather-intro      TIER 2 · 11    —
```
- `unprobeable BY DESIGN` is a state, never `unanswered` · **LINKS TO** — an ask with no row is a finding (orphan), and a committed row naming an ask the ledger cannot find is the mirror finding · `DECLINED` is R4 made visible.

### 9.3 · Exit codes and the selftest, so every clause can FAIL
exit 0 all readable and resolved · exit 1 a finding (orphan ask · row with no ask · fold target that cannot be probed) · exit 3 any UNREADABLE — **`report()` contains no bare `return 0`** (`walk-founding.py`'s clause, copied). `--selftest` mutations: an ask with no row · a row with no ask · an unprobeable fold target · a P2 carrier disagreeing with prose (carrier wins, disagreement prints) · an n=1 env (not reported, never 0) · a missing token (exit 3) · an exposure count offered as a distinct count (refused) · a note in reach (refused by construction).

### 9.4 · Falsifiers
For the tool: if every ask it lists already had a reader, it measured nothing — delete it (R0's line). For the contract: two consecutive laps of `none — <reason>` on every row → ceremony (P2's falsifier). For this spec: if lap 8's build finds an input this table does not name, the spec was written from the wrong side of the seam — R0 says what it found and this section is amended, not defended.

---

## 10 · THE PER-RELEASE READING — beats that already exist (`cycle/release/CYCLE-MAP.md`); no new beat

| beat | what it reads about asks | instrument | today |
|---|---|---|---|
| **6 · COMMIT** (Paul) | every committed row carries its four fields | P2's carrier; `check-backlog-ready.py` once P2 lands | ⛔ P2 unbuilt |
| **7 · BUILD** | the ask is in the build; the ledger lists it `SERVED 0` | `ask-ledger.py --env qa` | R0, lap 8 |
| **8 · SYNTHETIC LOOP** | the walk met the ask, and was asked WELL | `elicitation-lens.py` · `ask-ledger.py --env qa` | lens live; ledger R0 |
| **1 · OPEN** | what arrived on every ask channel at real estates — including UNREADABLE | `watch-feedback.py` · `read-onboarding.py` · `ask-ledger.py --env <real>` | `home` unreadable by construction |
| **2 · DISPOSE** (Paul) | every real-estate answer disposed | as today | live |
| **3 · READ** (user-researcher) | ⭐ **two lines proposed for the exit condition** (researcher §5): *"Read the lap's ASKS, not just its records: how many DISTINCT asks were served, to how many households, how many answered, what each answer changed on a screen, and which asks have no reader — count distinct asks, never exposures; exit 3 = UNREADABLE."* And **the standing question is two questions now: what has Mom asked you for lately — and what has anyone else.** `validated`: this repo holds ZERO words from Bob, whose two houses are lap 9's premise | the ledger + the lens | pending Paul |
| **12 · DEPLOY & CLOSE** | the attribution shipped where a ribbon exists; the card's own tag renders | `check-mom-ack.py` (Fernwood); a generalized ack check is a forward row | Fernwood only |

---

## 11 · Found on the way, not in the brief — live defects the seats measured (engineering's; forwarded, not fixed here)
- ⛔ **`handleFeedback` copies `deviceId` from the body unconditionally, then `stampVia` attributes the person — an attributed row can carry both TODAY** (security §2). The browser-bucket→person join `watch-activity.py` refuses to assert, routine on every attributed record.
- ⛔ **`GET /api/feedback` (and `zones`) read `dateKey(scopeOf(env), …)` — the DEPLOYMENT's scope, not the caller's** (security ⚠️1). Harmless while a deployment holds one household; **the lap-8 single-origin production makes every member's feedback read a cross-household read on the day the deployments collapse.** `scopeFor()` exists and is not used there.
- `renderAskNext()` returns in both branches (`:18525`, `:18527`) — the second gate is not what the comment describes (INVENTORY, all three UX/UR/content seats).
- `ask_next_added` has no reader; chips have no selected state (ux F1).
- `#card-told:19989` claims a contact preference is changeable and no control exists at either site (ux F2).
- All 22 live harvest prompts say *"we"* against the one-narrator ruling (content B1).
- The distinct-`questionId` count over the lap-8 window is still unrun — one command (`read-mom-funnel.py` is the door); every 0-for-35 reading inherits that denominator (researcher §3.1).

---

## Files touched
None by this window. Named for the builds it feeds: `engine/asks.json` (new, §9.1) · `tools/ask-ledger.py` (lap 8 R0) · `worker/worker.js` (the declarations write + read route, union-never-election — lap 9 · A) · `engine/viewer.template.html` `renderAskNext()` as one component in two hosts (lap 9 · A) · `/settings/place/` the mirror control (lap 9 · A) · `BACKLOG.md` rows by message (§12).

## Sequence
1. Paul rules §13 — nothing below moves before that.
2. **Lap 8 R0** builds the ledger to §9; R1's GET first or the served column reads UNREADABLE. **Lap 8 row G** lands the ribbon's instance seam.
3. **Engineering** takes §11's first two defects before lap 8's single-origin production — they are on its critical path, not this plan's.
4. **Lap 9 · A** builds the weather ask to §8: the declaration write/read (§4) · the in-card receipt (§5a) · the *Change* control and its Settings mirror (§5b) · `engine/asks.json`'s first entry · the words confirmed by Paul before the build. ⛔ **In this order: the receipt before the questionnaire** (the lead seat's finding).
5. **P2** gives the four fields a carrier; the ledger switches from prose without a reader change.

## Falsifier
The playbook is wrong if, one lap after the weather ask ships: (a) `ask-ledger.py --env <real>` cannot print the ask's row from the record; (b) a tap does not change the next page load; (c) the elicitation lens flags the ask for asking a derivable value; (d) a household that answered cannot, a week later, name one thing about their weather card that is different (the receipt failed and the content never mattered); or (e) no household answered AND Paul reports one asked him for something the card could have offered — the second half is the standing question, and its absence is not evidence.

## QA
- `ask-ledger.py --selftest` (every clause fails on its mutation) · `--env qa` after a lap-8 battery prints the seats' asks as distinct counts.
- `elicitation-lens.py` over the lap-9 battery: all four contract clauses present on the intro stop; no `asked-what-it-could-derive` finding.
- A walk at qa at 414×A+ (`herConditions()`): the ask on the FACE with the card's first content row above the fold (ux F5) · tap → the card changes in place without scrolling (F1) · reload → it held · the *Change* control reachable in ≤2 taps from the card and from Settings (F2) · third load → the ask is gone and the control is still there (F10) · exactly ONE ask-shaped affordance on the introduction load (F4).
- `check-estate-neutral.py --url <qa>` and `check-canon-scope.py`: a declaration at one household never renders at another.

---

## 12 · Forward rows — to the backlog window by message, never typed here into BACKLOG.md
1. **The runtime ribbon for FOUNDED households** (§5c) — attribution unreachable at J0 by construction; in no lap.
2. **`engine/asks.json`** — the card-intro ask register, sibling of `questions.json` (§9.1).
3. **The declarations write/read route** — union-never-election, `writeEstatePlace()`'s shape; lap 9 · A's step (§4).
4. **The *Change* control and its Settings mirror** — lap 9 · A; the changeable clause is CUT until it exists (§5b, §6).
5. **`handleFeedback` writes `deviceId` beside a personId** — live, engineering, before lap 8's single origin (§11).
6. **`GET /api/feedback` / `zones` read the deployment's scope, not the caller's** — live, engineering, on lap 8's critical path (§11).
7. **`renderAskNext()` double return + `ask_next_added` no reader + chips no selected state** (§11).
8. **`#card-told` claims a changeable contact preference with no control** (ux F2).
9. **Re-voice the 22 harvest prompts** — *"we"* → one narrator (content B1); its own pass.
10. **Run the distinct-`questionId` count** over the lap-8 window (researcher §3.1) — one command.
11. **RR-8, proposed roster row** — free-text asks gated per estate on the administrator's relationship or consent; and **read `fernwood-private` §7 directly** (security).
12. **Beat 3's exit condition gains the two ask lines** (§10) — a CYCLE-MAP edit, Paul's.
13. **Three principle candidates** for the libraries (content §7 ×2, ux ×3) and **the AI-in-asks rule** for `ai-playbook/fernwood.md` (ai-advisor §5) — proposed, not written.

## 13 · Open for Paul — question · recommendation · the alternative, each from a named seat
1. **Site of the advisory classes** — the card's face at first appearance (curation), setup only for provisioning (station · radar)? *Recommend yes* (ux F3, researcher R2). Alt: absorb them at setup as `0-PRIME-C` extrapolated — the plan's line, not your ruling.
2. **Shape** — one multi-select, ≤5 chips on the face applicability-filtered, plus a free-text door? *Recommend yes* (researcher §3, ux F5). Alt: the confirm queue — rejected by all three seats (watermark pin, 1-slot cost, wrong act at that door).
3. **Six classes, not eight** — cut *Severe weather* and *Fire weather* (no channel to warn)? *Recommend six* (content Q2). Alt: eight with an honest degradation line on those two, or hold both until a channel exists.
4. **Per-tap commit or one submit button over the chip set?** *Recommend per-tap commit with a persistent selected state* — the existing component's grammar, nothing to lose, the receipt renders in place immediately (ux F1). Alt (content Q3a): one *✓ Add these* button — one write, one receipt, makes *changeable* honest before the tap. Either way rule 1 is being EXTENDED to a chip set for the first time.
5. **The declaration's subject** — the ESTATE record, a union across people each carrying its author, any member writes? *Recommend yes* (security §1; researcher (d)). Alt: per-person curation — cleaner in a shared house, but two people's cards diverge on one screen and the ribbon has nothing household-wide to say.
6. **Does a chip tap enter the feedback channel?** *Recommend no* — the declaration is the record, a counted event feeds the ledger; only the free-text line is an arrival (content Q6; security §2 rules the record's shape if you say yes).
7. **Does a preference ever earn a ribbon line?** *Recommend only when it changed something visible, act-and-place at a shared house, never "you"* (content §1c, security §5) — and it is unbuildable until row G. Alt: reserve the ribbon for answers about the world.
8. **The AI-draft gate** — replace the >10-answered threshold, for intro asks only, with *three cards hand-authored and the third the same shape as the first*; the model reads the product never the person; **served deterministically, never by the Guru**? *Recommend yes* (ai-advisor §1–2). The human gate moves in neither direction.
9. **`fernwood-11` / `fernwood-12`** — keep-asking-and-instrument-her-doors · extend-the-fence (household-system, vehicle/equipment first)? *Recommend both* (ai-advisor §4 concurs with the cards). Option 3 would require the boundary rewritten, not amended.
10. **Your name on an engine ask** — carry the recovery draft's Q1 ruling here rather than re-ask (content Q7).
11. **The ledger at n=1 envs** — print `n=1 — not reported`, or omit the env and print the omission? (security §4.)
12. **The changeable clause** — cut until the *Change* control ships (recommend), and retire per household on evidence of a change (§6)?
13. **The threshold chip** — *"this one, only when it matters"* (researcher §3.2·5) — hold out of v1? *Recommend hold.*
14. **Beat 3's two ask lines** into CYCLE-MAP (§10) — and the standing question as two: Mom, and anyone else.
15. ⭐ **The three the seats could not supply from here, for beat 3:** what has Mom asked you for lately · what has Bob (or anyone who is not Mom) asked you for · which of the advisory classes you have ever wanted yourself, at the condo.
