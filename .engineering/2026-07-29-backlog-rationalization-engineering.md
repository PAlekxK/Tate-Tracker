# Fernwood backlog rationalization — engineering lens

**Date:** 2026-07-29 · **Seat:** engineering-partner · **Repo HEAD:** `54db096`
**Brief:** `.plans/2026-07-29-rationalization-brief.md` · **Tiers:** 1 FIX NOW · 2 CONFIRMED · 3 STEER

**Calibration stated up front.** Two users, one of whom is the reason the project exists. No revenue,
no SLA, no team. Every severity below is scaled to *that*, and where the outside literature assumes a
production team I say so and discount it. Nothing here recommends a framework, a bundler, npm, or a
test pyramid.

**Verification posture.** No status below is taken from `BACKLOG.md`. Every claim is checked against
git HEAD, the code, or a command whose output is quoted. Where I could not check, section 6 says so.

---

# 0 · THE TAXONOMY PROPOSAL

*Paul folded this in as a co-equal deliverable. It is answered here as a proposal, not a refactor —
per his instruction, no code was changed.*

## 0.1 What is actually broken (measured, not asserted)

I read every domain file and counted fields across the ten record lists
(`plants · weeds · birds · mammals · amphibians · snakes · lizards · vehicles · zones · candidates`,
~154 records total).

**Only `id` and `name` are present in all ten.** `emoji` 9/10 · `photo`+`attribution` 8/10 ·
`scientificName` 8/10 · `notes` 8/10 · `status` 6/10.

Three findings fall out, and the third is the one that matters.

**① `status` appears in six domains and means four unrelated things.**

| Domain | `status` values | What it actually means |
|---|---|---|
| weeds | `needs-confirmation` (5/5) | verification state |
| zones | `draft` (10/10) | verification state |
| birds / mammals | `resident`, `summer`, `winter`, `area-concern` | seasonal presence |
| vehicles | `"Active — coolant leak diagnosis ongoing"` (free prose) | operational condition |
| candidates | `considering` | pipeline state |

A shared field name carrying four meanings is worse than four different names, because every tool
that reads "status" has to know which domain it is in — and that is the same "assumed plants" trap
that shipped broken three times in one day, one abstraction level up.

**② Weeds carry the same fact twice.** All five weed records have `confidence: "inferred"` *and*
`status: "needs-confirmation"` — perfectly correlated, 5/5. That is a single-source-of-truth
violation already sitting in the data (`[[Single source of truth per record, declared explicitly]]`).

**③ ⭐ The honesty marker — the thing the whole project runs on — is expressed three incompatible
ways, and five domains cannot express it at all.**

| Shape | Where | Grain |
|---|---|---|
| `variety.confidence` / `bloom.confidence` | plants (3 varieties, 24 blooms) | per-attribute |
| top-level `confidence` | weeds (5/5) | per-record |
| `status: "draft"` | zones (10/10) | per-record, different name |
| **nothing** | **birds · mammals · amphibians · snakes · lizards · fishing — 67 records** | **—** |

Sixty-seven species records assert that an animal is present at this property, with no way to say
"we think." `CLAUDE.md` says *"honesty markers are mandatory, not decorative"* and *"a
confidently-wrong record is worse than an honestly-unsure one."* Five of ten domains structurally
cannot comply.

**That, not "weeds are plants," is the taxonomy problem.** `harvest-questions.py`'s inability to
harvest a weed is one visible symptom of it.

## 0.2 The reframe

The question is **not** "what should the domains be." It is **"what is a record, independent of
domain."** The evidence on the two halves points in opposite directions and both are strong:

**The domains are right — do not collapse them.**
- Mom derived `vehicles / equipment / household systems` herself, unprompted (B6).
- She asked for tabs by domain, naming *vehicles · equipment · house systems · gardening · wildlife*
  (W8·a).
- She named the Weeds section as the one she loves.

Two independent behavioural signals say the domain split matches her mental model. A single-store
"everything is an entity" model would throw that away for a schema convenience she would feel.

**The record envelope is wrong.** Each domain re-invented identity, provenance and presentation,
inconsistently, by accretion.

## 0.3 The proposal — envelope · facets · registry

### Layer 1 · THE ENVELOPE (shared, thin, mandatory)

Every record in every domain carries the same small named group. Not merged schemas — a *field group*
that means the same thing everywhere.

```
identity    id, name, emoji                          (already 9–10/10)
provenance  record: { confidence: verified|researched|inferred,
                      basis:      "<where it came from>",
                      askable:    bool,
                      verifiedOn: "YYYY-MM" }        (NEW — the missing universal)
presence    photo, attribution                       (already 8/10)
place       zoneId | zoneIds[]                       (plants only today)
```

Two deliberate calls inside that:

- **The marker is nested under `record`, not top-level `confidence`.** It has to be
  unambiguously distinguishable from a facet's confidence, and it must never collide with the four
  existing meanings of `status`.
- **`status` is retired as a shared name.** Each domain renames to what it means:
  `seasonalStatus` (wildlife) · `condition` (fleet) · `pipelineStatus` (candidates) ·
  zones' `draft` folds into `record.confidence` · and **weeds' `status: needs-confirmation`
  disappears entirely**, because it is a restatement of `record.confidence: inferred` + `askable`.

### Layer 2 · THE FACETS (per-domain, optional) — this is the piece that unblocks the harvester

A **facet** is an attribute that carries its own confidence. Plants have two (`variety`, `bloom`);
weeds have none, because their uncertainty is at record level. `harvest-questions.py` knows only
facets — which is exactly why a weed is invisible to it.

**The rule, one sentence: uncertainty lives either on the record (envelope) or on a named facet, and
the harvester reads both.** Then:

| Record | Uncertainty at | Card it yields | Class (per A3) |
|---|---|---|---|
| weed `crabgrass` | record | *"is this what's in the fairway?"* | observation |
| plant `clematis` | facet `variety` | *"what colour are the flowers?"* | observation |
| plant `lizards-tail` | facet `bloom` | *"is it out yet?"* | observation |
| bird `ruby-throated hummingbird` | facet `arrivalWindow` | *"we have them from late March — seen one?"* | **observation** |

**⭐ The payoff worth naming: the taxonomy fix and A3's "replacement card slate" are the same work.**
A3 says the real job is replacing verdict-class cards with observation-class cards, and that
`harvest-questions.py` "is structurally a verdict-ask factory." That is true *only because it reads
plants' facet markers*. With the envelope, the same harvester draws from ~154 records across nine
domains instead of 36 plants, and the wildlife ones are observation-shaped *by construction* — the
app says "we have this from a book, we've never watched it here," which asks no verdict of her.

That reframes the Track C row: it is not schema hygiene competing with A3, it is A3's supply problem
solved at the root.

### Layer 3 · THE REGISTRY (one declaration, six derived lists)

`momlib.ENTITY_SOURCES` is already 60% of a resource registry — it carries `(file, key, const)` for
two domains. Finish it: all domains, plus `label` (Mom-facing), `facets[]`, `harvestable`.

That single move closes four separate live gaps at once, because six places currently re-type the
same list by hand:

| Consumer | Today | After |
|---|---|---|
| `check-data-inline.py:65` `SOURCES` | 10 hand-typed rows; **7 inlined consts have a source JSON and no check** (F5) | derived |
| `build-digest.py:218–249` | 11 hardcoded `load("x.json")` calls | derived |
| `.github/workflows/deploy-worker.yml` `paths:` | **missing `weeds.json`** (F7) | generated |
| `harvest-questions.py:36` | `PLANTS = plants.json` only | derived |
| `momlib.ENTITY_SOURCES` | 2 of 10 domains | the declaration |
| `buildCard`'s `ENTITY_DATA` | irreducible JS copy — already drift-checked | unchanged |

This is `[[Generate the derivable; drift-lint the rest]]` — Paul's own promoted cross-project
principle — applied to the one list that has been re-typed six times.

## 0.4 The field-journal framing — where "things I tend / fight / visit" lands

Paul's live tension: the framing may want *things I tend · things I fight · things that visit ·
things that run the place*, where the data model wants shared fields.

**My read: that is a presentation grouping, not a data grouping, and it should stay one.**

The reason is falsifiable, not aesthetic: **the four-way split is a relationship between Mom and the
thing, and a record can change relationship without changing identity.** Virginia creeper is in
`weeds.json` and is *native* — fought or tended? Moss went from nonexistent to tended. A
`candidates.json` plant becomes a tended plant when it is planted. If relationship is the file
boundary, every one of those is a data migration. If it is a card grouping (or at most a
`relationship` field), each is an edit.

The 2025 content-modelling consensus says the same in its own words: *the content model describes
what the content is, not how it looks.* "Things I fight" is how it looks **to her** — which makes it
exactly right for the tabs, and exactly wrong for the files.

**And it is already out for her answer.** `q-top-categories` is live and leads the queue. So the
framing question is *not* blocking the schema work, and the schema work is *not* waiting on her.

## 0.5 What can be decided NOW vs. what needs an answer — and whose

**Decidable now. Paul's call only, and I recommend yes to all four:**

1. The envelope exists and is thin (identity · provenance · presence · place).
2. `status` retires as a shared name; each domain renames to what it means.
3. Uncertainty lives on the record **or** on a named facet; the harvester reads both.
4. The registry is one declaration everything derives from.

**Needs PAUL's answer — engineering judgment, not Mom's:**

- **Q-P1 · Do the 67 wildlife records get a backfilled honesty marker, and at what grain?**
  My recommendation, and it matters: **do not bulk-author it.** Set all 67 mechanically to
  `record.confidence: "researched"` — which is *true* (they came from range data, not from standing
  on the property) — and let `verified` accrue one record at a time from Mom's answers. Bulk-authoring
  67 confidence judgments is the same move that produced the 18 stock photos ("24 is your number, not
  hers"). Done this way, a 67-record authoring chore becomes 67 units of observation-class card
  supply.
- **Q-P2 · Is the registry Python (`momlib`) or a JSON descriptor both Python and the viewer read?**
  My call: **stay in Python.** The viewer can't consume either one (`ENTITY_DATA` is the irreducible
  copy regardless), so a JSON descriptor would be a *third* place — the exact trap `ENTITY_SOURCES`
  was created to close.
- **Q-P3 · Does `plants.json` split for W6?** See 0.7 — my read is no, and that is a smaller answer
  than the row assumes.

**Needs MOM's answer — exactly one thing, and it is already asked:**

- **Q-M1 · the card grouping / tab labels.** `q-top-categories`, live, leading the queue.
  **Capture path already exists and needs nothing new:** her tap or note → `POST /api/feedback` →
  `read-mom-feedback.py --pickup` → punch-list. It is a `_kind: reflective` card with no
  `_foldTarget`, so per the `unprobeable` rule it **will hold the feedback watermark until
  hand-retired** — same as `q-almanac-name` just did. Budget for that retire step; it is not optional.

**⭐ The most useful thing I can say about this whole question: the schema half does not need Mom.**
The Track C row offers "ask the team and/or ask Mom." Asking Mom about the record shape would be
asking her to adjudicate our work — the verdict class A3 just deprioritised as futile — about a thing
she cannot see. Ask her about the tabs (already done). Decide the schema without her.

## 0.6 The migration path — expand-and-contract, five steps, each independently shippable

The expand-and-contract literature transfers here almost unchanged, because its whole point is *never
needing a flag day* — and Fernwood's binding constraint (Mom's app must never break, and she is the
one person who checks the app against reality) is the same constraint at a millionth the scale. What
does **not** transfer is the CI/dual-write/triggers apparatus; at 154 records the "parity check" is
`check-data-inline.py`, which already exists.

| # | Step | Mom-visible? | Effort | Unblocks |
|---|---|---|---|---|
| 1 | **EXPAND** — add envelope fields alongside existing ones. Nothing removed. Viewer untouched. | none | M | — |
| 2 | **REGISTRY** — `ENTITY_SOURCES` → all domains + facets; rewire the six consumers. | none | M | F5, F7, digest coverage |
| 3 | **HARVESTER** — read envelope + facets. Still drafts `active:false` (Paul's gate intact). | **none until Paul flips a card** | S | the Track C row; A3 supply |
| 4 | **RENAME `status`** per domain; update render functions. Acceptance test = identical screenshot. | none if done right | M | — |
| 5 | **CONTRACT** — drop weeds' duplicate `status`, dead `currentSeasonNote`, the `propertyZones` placeholder (F2). | none | S | — |

**Steps 1–3 are the ones that pay. 4–5 are hygiene and can wait indefinitely.**

Note what step 3 means for the Mom-facing objection in the Track C row: wiring the harvester does
**not** put new cards in front of Mom. It drafts candidates as `active:false`. Paul's gate is
unchanged. The row treats "wiring it would serve new cards" as the blocker; that is true only of
`--append-drafts` **plus** Paul flipping `active:true`. The wiring itself is invisible.

## 0.7 W6 (the instance model) — a smaller answer than the row assumes

The row says `plants.json` is species-level, reality is instance-level, and 23 of 36 `zoneId` are
null (verified: 23 null / 13 set), which "may be partly a schema failure."

My read, offered as a hypothesis Paul should shoot at: **W6 probably needs no schema change to
`plants.json` at all.**

Decompose what "instance" is actually being asked to carry:

| Need | Where it belongs | Why |
|---|---|---|
| same species in several zones | `zoneIds: []` on the species record (envelope, Layer 1) | it is a cardinality fix, not a new entity |
| *her own photo of that individual* | the observation store (`.private` KV, tagged `{plantId, zoneId}`) | this is field-captured content, and `[[Field-captured free text lands in the private store; canon grows only by hand]]` already governs it |
| "the crocosmia here is Lucifer but that one may not be" | a facet's confidence, scoped by zone | a facet already carries confidence; scoping is one key |

That would let the 23 nulls be *answered* rather than *migrated around*, and it keeps the highest-PII,
highest-churn content (her photos, her notes about specific plants) out of the public repo — which is
where the existing principle already puts it. If that reading holds, W6 stops being a schema project
and becomes two small features. **It is worth Paul spending ten minutes disagreeing with this before
anyone designs an instance model.**

The `CLAUDE.md` taxonomy rule v1 does **not** need a v2 for any of this. The envelope is orthogonal to
the four cases in the rule; nothing above contradicts it. Bump to v2 only if Q-P3 resolves toward a
real instance entity.

---

# 1 · TIERED FINDINGS

Effort: S ≤ 1 hr · M ≤ half a day · L = more.
Owner: 🤖 agent end-to-end · 👥 agent drafts, Paul confirms · 👤 Paul.

## Tier 1 · FIX NOW — nothing blocks these

| # | Finding | Where | Eff | Own |
|---|---|---|---|---|
| **F1** | **⭐ Guru's digest contains a fake zone.** `property.json.propertyZones` still holds the template stub `zone-placeholder` / *"Example: Front Beds (East-facing, mid-slope)"* — and `build-digest.py` copies it into the digest (verified: 1 occurrence in `worker/digest.json`). Meanwhile the **real** 10 zones (`zones.json`) are excluded from the digest. So the only zone data Garden Guru has is an invented example, on a surface Mom reads. This is the 2,800 ft failure mechanism with a *known-fake* fact instead of a confabulated one. A6 ① understates it: the problem isn't only that Guru can't resolve zone ids — it's that it has a fabricated one to ground on. | `build-digest.py` `digest_property`; `property.json` `propertyZones` | S | 🤖 |
| **F2** | **Guru recites soil series the project has already falsified — 34 times.** `Cecil` ×18 and `Pacolet` ×16 inside `digest.plants.*.soilNotes` + `plants._meta.soilSeries`. Both are thermic Piedmont series capped near 900 ft and **cannot** occur at 2,959 ft (W9, `property.json` already corrected). In a ~114K-token context, 34 assertions beat the single correction in `property`. Removing a positively-falsified name is a correctness fix, not content authoring, and does **not** wait on the soil test — honestly-unsure beats confidently-wrong. Split: `plants._meta.soilSeries` is one edit (Tier 1); the ~17 per-plant prose lines are Tier 2 (F12). | `plants.json` `_meta.soilSeries`; digest | S | 🤖 |
| **F3** | **`check-mom-ack.py:229` asserts a behaviour that does not exist — CONFIRMED FALSE.** The line prints *"(read-mom-feedback.py and read-mom-zone-audio.py mark their own channel.)"*. `grep -rn mark_channel_read tools/` returns only `read-mom-feedback.py:518`, `check-mom-ack.py:113`, `momlib.py:552`, `scan-mentions.py:248`. `read-mom-zone-audio.py` never calls it. Consequence: the `zone-audio` channel can never clear by being read, so R2b will name it forever and the printed remedy points at a tool that doesn't do the thing. | `tools/check-mom-ack.py:229`, `tools/read-mom-zone-audio.py` | S | 🤖 |
| **F4** | **`CLAUDE.md`'s Architecture section is wrong about its own file, in the dangerous direction.** It says viewer.html is *"a single ~4,600-line file"* (measured: **17,879 lines / 1,527,907 bytes**) and that the JSON files *"are fetched at page load and the inlined copies serve as fallback."* **Only 4 files are fetched at runtime** — `questions.json`, `zones.json`, `weather-history.json`, `weather-bias.json`. `PLANTS_DATA`, `VEHICLES_DATA` and 15 other consts are **inline-only**; the inline is the sole runtime copy, not a fallback. This is the paragraph an agent reads before touching the data layer, and it says the opposite of the truth in the direction that makes a skipped re-inline look harmless. | `CLAUDE.md` → Architecture | S | 🤖 |
| **F5** | **7 inlined consts have a source JSON on disk and no drift check.** `check-data-inline.py:65` covers 10 consts. Unguarded: `PROPERTY_DATA · CANDIDATES_DATA · EVENTS_DATA · REFERENCES_DATA · SOURCES_DATA · SUN_HORIZON_DATA · TURF_DATA`. I verified all seven are **currently in sync** — this is latent, not live. But `PROPERTY_DATA` is the elevation/frost/soil calibration referenced 15+ times in the viewer, and the drift alarm exists precisely because canon-ahead-of-inline hid Lizard's Tail for weeks. Adding 7 rows is the interim; deriving the list from the registry (0.3 Layer 3) is the durable fix. | `tools/check-data-inline.py:65` | S | 🤖 |
| **F6** | **A watermark-holding card is staged to go live in August.** `q-fairway-grass-seedheads` carries `_foldTarget: "observedGrasses"`, which is not in `momlib.FOLD_FIELDS` — so `probe_target()` returns not-found and `question_state()` classifies it **`unprobeable`**. It is `active:false` today. The moment Paul flips it in August it pins the feedback watermark until hand-retired — the exact failure `q-almanac-name` just demonstrated, where every later answer of hers re-read as new. Fix: add `"observedGrasses": ("observedGrasses",)` to `FOLD_FIELDS` (one line), or accept it as a hand-fold and record that. Do it **before** August. | `tools/momlib.py:203` `FOLD_FIELDS`; `questions.json` | S | 🤖 |
| **F7** | **The auto-deploy workflow would silently miss weeds.** `deploy-worker.yml`'s `paths:` trigger lists 9 digest sources; `build-digest.py:225` also reads **`weeds.json`** (added `a73afbd`, 07-28), and `zones.json`/`turf.json` are candidates for the A6 ① add. Arming `CLOUDFLARE_API_TOKEN` today ships a workflow with a known silent gap — a weeds edit rebuilds locally but never redeploys. One-line fix, and it is a **prerequisite** to that row, not a follow-up. | `.github/workflows/deploy-worker.yml` `paths:` | S | 🤖 |
| **F8** | **Strip the Ambient key fallbacks from `record-daily-rollup.mjs`.** Lines 27–30 hold both 64-hex literals behind `process.env ||`. **The workflow already passes `secrets.AMBIENT_APP_KEY` / `secrets.AMBIENT_API_KEY`** — so in CI these fallbacks are dead code. Deleting them is independent of rotation and costs nothing. (The `viewer.html` half is NOT one pass — see F14.) | `tools/record-daily-rollup.mjs:27–30` | S | 🤖 |
| **F9** | **`build-digest.py:266` uses the wrong token ratio.** It estimates `chars // 4`; the measured ratio from the live cost log is **0.2693 tok/char** (3.71 chars/tok) — established in `research/2026-07-28-garden-guru-scope.md` and never applied. Current under-read: the script would report ~99K where the true cached prefix is **~113.6K**. A budget check that under-reads by 15% at exactly the ceiling it exists to watch is worse than no check. | `tools/build-digest.py:266–276` | S | 🤖 |
| **F10** | **Add a file-size tripwire to the session-start check.** The 1 MB GitHub Contents API cliff was found by two weeks of silent failure. Five lines that print `viewer.html` size against a stated threshold **and name the ceiling being approached** convert the next ceiling from an incident into a line of output. Ship this *before* the split (F13), because it is five lines and the split is a day. | new `tools/check-size.py` or into `check-data-inline.py` | S | 🤖 |

## Tier 2 · CONFIRMED — an answer already given; build it

| # | Finding | Where | Eff | Own |
|---|---|---|---|---|
| **F11** | **⭐⭐ The Guru test harness — ~15 lines of Worker unblock everything else.** Design in §3 below. Paul has already stated the intent (*"the first build is almost certainly the test harness, since nothing else can be changed safely without it"*, A6). Nothing is waiting on an answer. | `worker/worker.js` + new `tools/test-guru.py` | M | 🤖 |
| **F12** | **Sweep the falsified soil series out of ~17 plant `soilNotes`.** The prose half of F2. A positively-falsified series name is a confident-wrong claim; replacing it with the honest "unconfirmed until the W9 test" does not wait on the test. Reaches Mom's cards → wording gated. | `plants.json` `soilNotes` ×17 | M | 👥 |
| **F13** | **⭐ Split the DATA out of `viewer.html` — not the code.** Design in §2. viewer.html 1.53 MB → ~800 KB, no build step, plain `<script src>`, works over `file://`. This is the cheapest intervention with the largest safety payoff and it does not require any decision. | `viewer.html`, `tools/reinline.py` | M | 🤖 |
| **F14** | **Rotate the Ambient key — and build the Worker proxy FIRST.** ⚠️ **Sequencing hazard the backlog misses:** the station call is made **client-side** (`viewer.html:6571`), so "de-embed" is not a delete — the browser needs the key from somewhere. The only clean somewhere is a `GET /api/ambient` proxy on the Worker, which already holds secrets and already serves this client (~30 lines + a client swap). **If Paul rotates before the proxy exists, the next re-inline republishes the new key and the rotation is spent for nothing.** Order: proxy → rotate → strip. Rotation itself is Paul's (external account). | `worker/worker.js`; `viewer.html:6540–41, 6571` | M | 👤 then 🤖 |
| **F15** | **`check-claims.py` — the mechanism for the recurring failure class.** Design in §4. Three known claims to seed it with (F3, F4, F5). Ship it *before* the taxonomy migration, because a five-step migration across ten domains is exactly where "this file assumes plants" reappears. | new `tools/check-claims.py` | S | 🤖 |
| **F16** | **Steps 1–3 of the taxonomy migration (envelope · registry · harvester).** Mom-invisible throughout; step 3 still drafts `active:false` behind Paul's gate. Tier 2 rather than 3 because §0.5 shows nothing is genuinely blocked on an unasked question — the four decisions are Paul's to make in one sitting. | 10 JSON files, `momlib.py`, `harvest-questions.py`, `check-data-inline.py`, `build-digest.py` | L | 👥 |

## Tier 3 · STEER — a question not yet asked

Every row names ① the exact question and ② the capture path. **For this lens the question is almost
always Paul's, not Mom's** — the schema is invisible to her by construction.

| # | Finding | ① The question (verbatim) | ② Capture path | Own |
|---|---|---|---|---|
| **F17** | Wildlife honesty markers (Q-P1) | *"67 wildlife records assert an animal is present here with no confidence field. Do we set all 67 to `researched` mechanically — true, since they came from range data — and let `verified` accrue from her answers? Or do you want to author them?"* | Paul answers in session → the call goes into `CLAUDE.md`'s taxonomy rule (bump to v1.1) → the mechanical set is one script | 👤 |
| **F18** | Registry home (Q-P2) | *"Registry in `momlib` (Python, one declaration, viewer can't read it either way) or a JSON descriptor (more general, but a third place)? My rec: Python."* | Paul answers in session → recorded in `momlib.ENTITY_SOURCES` docstring | 👤 |
| **F19** | W6 instance model (Q-P3) | *"Does W6 need an instance entity at all, or is it `zoneIds[]` on the species record plus per-instance photos in the observation store? Shoot at §0.7 before anyone designs a schema."* | Paul disagrees or agrees in session → outcome to BACKLOG W6 + taxonomy rule revisit gate | 👤 |
| **F20** | Card grouping / tabs (Q-M1) — **the only one that is Mom's** | *Already asked.* `q-top-categories` is live and leads the queue. | **Exists, needs nothing new:** her tap/note → `POST /api/feedback` → `read-mom-feedback.py --pickup`. ⚠️ Reflective card, no `_foldTarget` → it **will pin the watermark** until hand-retired (`active:false` + `resolvedAt`). Budget that step. | 👤 |
| **F21** | Citizen-science dormant code | *"The citizen-science scaffolding in viewer.html has been dormant since May. Re-enable, delete, or leave? If you don't have a view, it's dead code and I'd delete it."* | Paul answers in session → one commit either way | 👤 |
| **F22** | Guru's own turns unaudited (A6 ④) | *"Auditing Guru's assistant turns against a canon fact table opens conversation content to a model. Do you ratify that boundary change, containment = assistant turns only, behind a deterministic pre-filter?"* | Paul ratifies or declines → `CLAUDE.md` AI boundary amendment | 👤 |

---

# 2 · KILL LIST

| Row | Why it should not be done |
|---|---|
| **`build-digest.py`'s 80K token gate** (`build-digest.py:212`) | A tripwire nobody has ever acted on. It was crossed by 2026-07-13 (`cache_creation = 95,147`), and the 2026-07-17 "de-urgent-ed, back under the ceiling" note was written **four days after** it had already fired. A6's vision row explicitly retires cost as the constraint. **Delete the gate; keep the printed number** (fixed per F9) as information, not as a threshold. A threshold that has been silently violated for 16 days is training everyone to ignore the output. |
| **A6 ③ — `candidates.json` + `devices.json` into the digest** | A6 itself rates them *"plausible, lower value, not urgent."* At a measured ~113.6K cached prefix — already past the ~100K retrieval-degradation line — adding ~8.2K of low-value tokens makes the *known* failure mode (retrieval degradation, the 2,800 ft mechanism) worse to fix nothing. Kill it, don't defer it. Zones + turf (①②) stay, because they fix dangling references. |
| **"Off-machine backup target (R2 vs Google Drive)"** (B2) | Tier 3 with no question anyone can ask and no capture path. It has sat as "Paul's decision" with Apple Photos as an interim second copy that is working. Either Paul picks one in ten seconds or it is not a real item. As written, nobody can start it. |
| **A framework / bundler / module migration for `viewer.html`** | Not on the board, and I want it explicitly off. See §2 below — every version of it puts a compile step between an agent and the live app, which is the one thing this architecture is actually buying. |

---

# 3 · STATUS CORRECTIONS

Everything here was checked against HEAD or a command whose output is quoted.

| # | The backlog says | Verified truth | Evidence |
|---|---|---|---|
| **S1** | Ambient keys sit at `viewer.html:6451-6452` (Track C, "pointer corrected" 07-28) | **`viewer.html:6540-6541`.** The pointer has now been wrong **twice**. A line number is the wrong way to record a security item in a file that grows every session — record the symbol `AMBIENT_APP_KEY`, which is greppable and stable. | `grep -n AMBIENT viewer.html` |
| **S2** | Ambient keys are exposed in three places incl. `.github/workflows/record-weather.yml` | **Two places, not three.** The workflow already passes `secrets.AMBIENT_APP_KEY` / `secrets.AMBIENT_API_KEY` — it is a correct *consumer*, not an exposure site. The job is `viewer.html` + `record-daily-rollup.mjs`. | `cat .github/workflows/record-weather.yml` lines 24–35 |
| **S3** | Ambient de-embed is "one agent pass" | **~4× that.** The station call is client-side (`viewer.html:6571`), so the browser needs the key. Removing the literal requires a Worker proxy (~30 lines + client swap). The `.mjs` half genuinely is one line. | `viewer.html:6571-6572` |
| **S4** | `CLOUDFLARE_API_TOKEN` "gates nothing" | **Correct, independently confirmed** — `tools/deploy-worker.sh` runs `npx wrangler deploy` on local auth with no token reference. **But** arming it today ships a workflow whose `paths:` list is missing `weeds.json` (F7). The row should read "optional, with a one-line prerequisite." | `grep CLOUDFLARE tools/deploy-worker.sh` → no match; `deploy-worker.yml` `paths:` |
| **S5** | Digest is "~98.7K" (A6, 07-28) | **~106.0K digest / ~113.6K total cached prefix** at HEAD, using the measured 0.2693 tok/char ratio. Already ~13.6% past the ~100K retrieval-degradation line **before** the A6 ①② zones+turf add. That row's "→ digest ~104K, which crosses the note" is understated — the line is already crossed. | `wc -c worker/digest.json` = 397,457; `GARDEN_GURU_SYSTEM` = 28,279 chars |
| **S6** | `viewer.html` is "a single ~4,600-line self-contained file" (`CLAUDE.md`) | **17,879 lines / 1,527,907 bytes.** 47.7% (729,349 B) is inlined data across 21 constants; the remainder is ~568 KB JS + ~201 KB CSS + markup. 431 functions. | measured, §2 |
| **S7** | The JSON files "are fetched at page load and the inlined copies serve as fallback" (`CLAUDE.md`) | **False for 17 of 21 consts.** Runtime fetches: `questions.json`, `zones.json`, `weather-history.json`, `weather-bias.json`. Everything else is inline-only. | `grep -n 'fetch(' viewer.html` |
| **S8** | `check-mom-ack.py:229` — "read-mom-zone-audio.py marks its own channel" | **False.** No `mark_channel_read` call in that file. | `grep -rn mark_channel_read tools/` |
| **S9** | W2 — "Fix the `property.json.propertyZones` placeholder-stub SSOT break" | **Still open, and worse than recorded:** the placeholder is not only in `property.json`, it is **in Guru's deployed digest** (F1). | `worker/digest.json` contains `zone-placeholder` ×1 |
| **S10** | W9 — "~15 plant `soilNotes` still name the removed Cecil/Pacolet series" | **Confirmed and quantified: 18 + 16 occurrences inside `digest.plants`**, i.e. reaching Guru, not just the cards. Tracked as card prose gated on the soil test; it is *also* a live grounding hazard that does not wait on the test. | digest walk, §0 |
| **S11** | `check-data-inline.py` guards "the inlined `*_DATA` constants" | Guards **10 of 21**. Seven consts with an on-disk source JSON are unguarded (F5) — all currently in sync. | `tools/check-data-inline.py:65` vs. const scan |
| **S12** | A6 ① — Guru "reads zone ids it cannot resolve" | True, **and** the only zone data it *can* see is the fake placeholder (F1). The row describes half the problem. | `worker/digest.json` |
| **S13** | 24 of 26 plant `zoneId` are null (W6/W2) | **23 of 36.** The record count moved (36 plants, not 26) and 13 now carry a zone. The gap is real but a third smaller than recorded. | `plants.json` scan |
| **S14** | Session-start checks | All four green at HEAD: `check-data-inline` exit 0 (10/10 in sync), `check-cards` exit 0, `check-digest-fresh` OK, `momlib.py` self-report clean, ribbon shipped=True through `2026-07-29T12:56:29Z`. | run this session |

---

# 4 · THE SINGLE-FILE ARCHITECTURE

## 4.1 Measured, not asserted

| | bytes | share |
|---|---:|---:|
| **Total `viewer.html`** | 1,527,907 | 100% |
| Inlined data (21 `*_DATA` consts) | 729,349 | **47.7%** |
| JavaScript (excl. inlined data) | ~567,000 | 37% |
| CSS | 201,112 | 13% |
| markup + misc | ~30,000 | 2% |

17,879 lines · 431 functions · zero base64 data-URIs (good — images are external).
Largest consts: `PLANTS_DATA` 215 KB · `VEHICLES_DATA` 163 KB · `REFERENCES_DATA` 46 KB.

## 4.2 Is single-file still right? Yes — but for a narrower reason than "no build step is nice"

**What it is genuinely buying, and it is load-bearing:** Garden Guru writes to canon *through the
GitHub Contents API* and re-inlines into `viewer.html`. There is no compile between a write and the
live app. A build step would put one there, on the path that promotes Mom's confirmed species into
the record. That is not a preference; it is the shape of the write path.

Second: one request for Mom on rural LTE. (Weaker than it looks — GitHub Pages serves HTTP/2, so
multiplexing blunts it — but non-zero.)

**What the literature actually says, and where it stops endorsing this.** Simon Willison's 2025 piece
on single-file HTML tools is the honest version of Paul's AI-aware-maintainability principle: *"a few
hundred lines means the maintainability of the code doesn't matter too much: any good LLM can read
them."* Note the cap. **Fernwood is 17,879 lines.** The literature endorses where this file *started*,
not where it is. And its counsel for the other end — *"for a production app with a team, absolutely
use modules, a bundler, and proper separation of concerns"* — is the enterprise assumption that does
not survive contact here: there is no team, no incident budget, and no reviewer to serve.

## 4.3 The real failure mode ahead

Not "the file gets too big to edit." Three specific things:

1. **⭐ No agent can read this file any more.** 1.53 MB ≈ 400K tokens. Every edit to `viewer.html` is
   now made by an agent that has only ever seen fragments of it through `grep`. **That is the ceiling
   that is live today**, and it is precisely the one Paul's AI-aware-maintainability principle exists
   to protect — the reader is future-Paul *with Claude open*, and Claude can no longer open it.
2. **Ceiling #2 already happened and cost two weeks.** The 1 MB Contents-API cliff returned HTTP 200
   with empty content — silent. Fixed with the Blob API (100 MB headroom), but **that class has other
   cliffs nobody has enumerated**, and the file is still growing every session.
3. **The re-inline is a merge-conflict machine.** A weather bot pushes ~4×/day; every canon edit
   rewrites a 200 KB const inside a file Paul hand-edits constantly.

## 4.4 The cheapest intervention that buys the most safety

**Recommended: split the DATA out, not the code. (F13, ~half a day, no build step.)**

Move the 21 inlined consts into one generated `data.js`, loaded by a plain `<script src="data.js">`
before the main script. **Not ES modules** — a plain script tag keeps the same globals, requires zero
changes to the 431 functions, and, critically, **still works over `file://`** (ES modules would be
CORS-blocked, breaking `CLAUDE.md`'s "open viewer.html directly in a browser"). What it buys:

- `viewer.html` 1.53 MB → **~800 KB.** Out of the 1 MB cliff class entirely.
- `reinline.py` writes a small generated file instead of surgically patching a 1.5 MB HTML document.
  The re-inline becomes near-trivial and the merge-conflict surface collapses.
- Guru's write-to-canon path touches a file whose *only* content is generated — a Contents-API write
  can no longer corrupt hand-written code.
- The data half becomes independently diffable, which is what makes the taxonomy migration (§0.6)
  reviewable at all.

**Then: pull the 201 KB of CSS into `styles.css`.** Same argument, simpler, no ordering risk. After
both, `viewer.html` is ~600 KB of homogeneous app code — still large, but it is *one kind of thing*,
and each half is independently editable.

**Ship F10 (the size tripwire) first**, because it is five lines and the split is a day.

**What I would NOT do, explicitly:** a framework, a bundler, npm, ES modules, or splitting 431
functions into modules. Every one puts a compile step between an agent and the live app and buys
nothing Paul has needed.

---

# 5 · THE GURU TEST HARNESS (F11) — the highest-leverage item on the board

## 5.1 The pollution, traced precisely

| Step | Code | Effect |
|---|---|---|
| a probe POSTs `/api/chat` | `worker.js:1084` | — |
| `persistConversation(env, conversationId, turns)` | `worker.js:1183` → `1059` | writes KV `conversation:<id>` |
| `handleConversations` lists prefix `conversation:` | `worker.js:1932` | the test transcript appears as a conversation |
| `momlib._channel_latest("guru", "/api/conversations")` | `momlib.py:640-642` | reads `updatedAt` → **an arrival** |
| `latest_mom_input()` → `check-mom-ack.py` R1/R2 | `momlib.py:658` | **the ribbon reads stale and Paul reads as owing Mom a reply** |
| `logChatCost` | `worker.js:1185` | pollutes `cost-log:<date>` (minor) |

**One precision the brief's framing is worth sharpening on:** `/api/metrics` is written **client-side
only**, so a `curl`-driven probe does **not** touch the funnel (`card_expanded`, launcher taps,
confirm funnel). The corrupted stream is *arrivals* — R1/R2 in the A1 metrics table. That is still
serious under Paul's measurement-hygiene principle, but it is one stream, not all of them, and knowing
which one is what makes the fix small.

**And a consequence nobody has written down:** a test conversation lands in the store the **Journal**
reads back — and the Journal is now *the most-opened card in the app* (41 of 139 expansions). So a
probe is not merely a telemetry smudge; **it is visible to Mom.** That alone makes the Worker fix
non-optional before any Guru work.

## 5.2 The Worker change — ~15 lines, one deploy, and it unblocks the whole A6 arc

The repo has solved this exact problem twice, so do not invent a third pattern:

- `momlib.is_instrumentation()` — tag at write (`context.test: true`), filter at read.
- `people.json → excludeFromEngagement`, whose own note states the governing rule:
  *"a flag that must be re-set per browser is a flag that will be missed."*

So the tag must be **structural and unforgettable — derived from something the harness cannot help but
set.** The conversation id is that thing.

```js
// One predicate, three call sites. Mirrors momlib.is_instrumentation.
const isSyntheticConversation = id => typeof id === "string" && id.startsWith("test-");
```

1. `handleChat` — **skip `persistConversation` entirely** when synthetic. A test transcript has no
   business in Mom's Journal.
2. `logChatCost` — still log, tagged `synthetic: true`, so spend stays honest *and* separable.
3. `handleConversations` — belt-and-braces prefix filter, so an older synthetic key can never
   resurface.

That is the entire fix to "Guru cannot be regression-tested." Everything else in A6 — tool-use
migration, the zones/turf digest add, corpus/RAG, the Guru-turn audit — is currently gated on it.

## 5.3 The harness — `tools/test-guru.py`, three layers in cost order

**Layer 1 — OFFLINE (default; wire into the session-start check; zero network, zero cost).**
This is where most of the value is, and it is the part the LLM-eval literature misses entirely for a
two-user app. **Every Guru regression to date has been a prompt-or-digest regression, not a model
regression:**

| Incident | Root cause | Catchable offline? |
|---|---|---|
| 2,800 ft told to Mom | grounding / digest framing | ✅ |
| digest stale 3 days (plants + fishing) | build step skipped | ✅ (already `check-digest-fresh`) |
| zones/turf invisible to Guru (A6 ①②) | digest coverage | ✅ |
| fake `zone-placeholder` in the digest (F1) | digest content | ✅ |
| four fence flows depend on digest-exact naming | coupling | ✅ |

Assertions:
- **Fact table over the digest** — every un-scoped elevation reads 2,959; every `2,800` sits inside a
  `fishing`/lake-scoped subtree (verified today: 12/13 fishing, 1 vehicles-incidental — the pinned
  disambiguation holds); the disambiguation block is present in `GARDEN_GURU_SYSTEM`; no
  positively-falsified fact (Cecil/Pacolet, `zone-placeholder`) appears anywhere.
- **Reference integrity** — every entity id the digest mentions resolves. Catches A6 ①'s dangling
  `observedZones` today.
- **Coupling** — the four fence-flow strings and the promote-species drafter's expected field names
  still exist in the digest shape.
- **Budget** — cached-prefix estimate at the *measured* 0.2693 tok/char (F9), printed, not gated.

**Layer 2 — REPLAY (cassettes; offline, deterministic, free).**
Record real `/api/chat` request/response pairs once; replay to prove *plumbing* — `audio_ref`
dereference, the 20-turn cap, the 5 MB 413, error mapping, fence parsing. This is the
`vcrpy` / `pytest-recording` pattern, and it is the one piece of outside practice that transfers
cleanly, because its whole point is *"talk to the real API exactly once, then be offline forever."*
Follow its security convention: redact the key out of the cassette.

**Honest call: design this layer, don't build it yet.** Fernwood's plumbing changes rarely; its prompt
changes constantly. Layer 1 pays first and pays more.

**Layer 3 — LIVE (`--live`, opt-in, synthetic-tagged, ~20 probes).**
A small `tools/guru-facts.json` of `{question, must_contain[], must_not_contain[], why}` —
**assertions, not golden outputs.** A golden-output test on an LLM is a flake generator; the
must-not list is where the value is:

```json
{ "q": "the pond has algae — what should I do?",
  "must_not_contain": ["2,800", "2800 ft"],
  "why": "2026-07-26: Lake Sequoyah's elevation pulled onto the property, told to Mom" }
```

Cost: 20 turns × (a ~113.6K cached prefix at cache-read rate + ~600 out) on Haiku — cents per run.
Run before and after a Guru change; never on a schedule.

**⭐ And one honesty clause, borrowed from `test-feedback-cycle.py`'s own hygiene check.** After a
`--live` run, the harness must assert that `check-mom-ack.py` reports the **same R1/R2 as before**.
That is the test-of-the-test, and it is the exact shape of the existing
*"HYGIENE — a synthetic row can NEVER claim she was acknowledged"* assertion. Without it the harness
is trusted on a promise rather than a measurement, which is the failure class this whole report is
about.

## 5.4 Why this is the one to do first

~15 lines of Worker + ~150 lines of Python. It is the gating dependency for every A6 item. And it is
the **only** item on the whole board that makes the measurement instrument *cleaner* rather than
noisier — which is exactly Paul's orienting principle for this run, applied to the one surface where
the instrument is currently corrupted by our own testing.

---

# 6 · THE RELIABILITY PATTERN — prose asserting another file's behaviour

## 6.1 Name the class

**An assertion about another file's behaviour, with no owner.** Instances, two of them found or
confirmed this run:

| # | Instance | Status |
|---|---|---|
| 1 | `check-mom-ack.py:229` — *"read-mom-zone-audio.py marks its own channel"* | **VERIFIED FALSE** (S8) |
| 2 | **NEW** — `CLAUDE.md` Architecture: line count and "fetched at page load / inlined as fallback" | **VERIFIED FALSE** (S6, S7). Highest-consequence of the set: it is the paragraph read before touching the data layer, and it is wrong in the direction that makes a skipped re-inline look harmless. |
| 3 | "assumed plants" × 3 files in one day | already recorded, already fixed |
| 4 | `BACKLOG.md` vs `manuals/INDEX.md` disagreeing ~10 days | already recorded |
| 5 | The 80K digest gate "de-urgent-ed, back under the ceiling" — written **four days after** the gate had already fired | found this run (kill list) |

## 6.2 The mechanism — and it is not new doctrine

The repo has already invented it twice without naming it:

- `momlib.entity_map_divergence()` **reads** `viewer.html`'s `ENTITY_DATA` binding and derives the
  comparison, replacing a hand-typed `RENDERABLE` set. Its own comment: *"a set that can itself go
  stale is a smoke detector with the battery out."*
- `check-data-inline.py` derives the JSON ↔ inline comparison rather than asserting sync.

And `momlib.py`'s header already states the governing principle in full:

> *"a status written down at one moment gets read later as if it were a measurement of the world at
> THAT moment. A derived value is self-dating."*

**So the mechanism is the existing self-dating principle extended from *status* to *claims about
behaviour*.** One rule:

> **A sentence that asserts what another file does is either a check or a lie-in-waiting.** When you
> write one, either (a) express it as an executable assertion in `tools/check-claims.py`, or
> (b) delete the assertion and point at the file.

Concrete shape — ~60 lines, and the design point is that **each claim's prose and its falsifier sit in
the same place**, so they cannot drift from each other:

```python
CLAIMS = [
  ("read-mom-zone-audio.py marks its own channel",
   lambda: "mark_channel_read" in read("tools/read-mom-zone-audio.py")),
  ("every inlined *_DATA const with a source JSON is drift-checked",
   lambda: not unchecked_consts()),
  ("viewer.html fetches its domain JSON at runtime",
   lambda: all(f'fetch("{f}' in viewer for f in RUNTIME_FETCHED)),
]
```

Every other file's comment then reads *"see `check-claims.py`"* instead of restating the behaviour.

**Relationship to the `falsifier/probe` idea already on the board:** same mechanism, second
application. The probe answers *"is this row still blocked?"* (`handoff/probe-proposal-2026-07-28.json`);
`check-claims` answers *"is this sentence still true?"* Both replace an asserted state with a derived
one. Under Paul's own promotion rule (*rule-of-three AND a stable interface*), two applications is the
second data point — worth noting, not yet worth promoting to the cross-project library.

## 6.3 Where it pays first

**Not on the three known instances** — those are one-line fixes each. On the **taxonomy migration**.
A five-step expand-and-contract across ten domains is precisely the situation where "this file assumes
plants" reappears, and by then the claims will be spread across six tools. Ship `check-claims.py` with
three claims **before** step 1, and grow it as the migration touches each site.

The outside framing for this is *architecture fitness functions* (Ford et al., and the 2025–26
practitioner writing on operationalizing ADRs): *"documentation does not stop drift — running checks
do; if a rule exists only in documentation, it's a candidate for a fitness function."* Correct, and it
gives the pattern a name Paul can use in an interview. **What does not transfer** is the apparatus:
ArchUnit / dependency-cruiser / PR-gated CI is a team's answer to a team's problem. Here the whole
thing is one Python file wired into a session-start check that already exists.

---

# 7 · EXTERNAL RESEARCH — source → the row it changes

| Source | What it says | The Fernwood row it changes | Discount applied |
|---|---|---|---|
| [Cosmic — Content Modeling Best Practices (2025)](https://www.cosmicjs.com/blog/content-modeling-best-practices-designing-scalable-headless-cms-architectures) · [Hygraph — complex datasets](https://hygraph.com/use-cases/model-complex-datasets) | **Reusable field groups + discriminated unions on a type key**, not one polymorphic mega-type and not N unrelated types. *"The content model describes what the content is, not how it looks."* | **Track C taxonomy row.** This is the direct source for §0.3's envelope + facets + `type` discriminator, and for §0.4's ruling that *things I tend / fight / visit* is a card grouping, not a file boundary. | Enterprise versions assume a CMS UI, editorial roles and content governance. None exists here. Kept: the shape. Dropped: everything about editors. |
| [TypeScript & Headless CMS (2025)](https://headlesscms.guide/guides/typescript-and-headless-cms) | Use **discriminated unions for variant-heavy content** and **versioned objects** (`seo_v1`, `seo_v2`) to migrate incrementally without mass refactors. | **§0.6 migration.** Justifies additive-first over a rewrite, and validates keeping `variety`/`bloom` as named facets rather than flattening them. | Versioned-object churn is overkill at 154 records; `schemaVersion` in `_meta` (already present) is the hobby-scale equivalent. |
| [Systemoverflow / pgroll — expand-and-contract](https://www.systemoverflow.com/learn/data-modeling-schema/schema-evolution/expand-and-contract-pattern-for-safe-schema-evolution) · [xata — pgroll](https://xata.io/blog/pgroll-expand-contract) | *"Add the new shape next to the old, move traffic in stages, drop the old only once the new has served long enough to trust."* Phases: backfill → dual-write → parity check → flip reads → drop. | **§0.6, all five steps.** Fernwood's "parity check" already exists as `check-data-inline.py`. | Triggers, dual-write plumbing and CI migration tooling are a distributed-systems answer. At 154 records in git, "roll back" is `git revert`. Kept: the sequencing discipline and never needing a flag day. |
| [Frictionless Data Package spec](https://specs.frictionlessdata.io/) | One descriptor lists N **resources**, each with its own schema, sharing field definitions; a **schema registry** is what libraries read. | **§0.3 Layer 3.** Names what `momlib.ENTITY_SOURCES` already half is, and justifies finishing it rather than replacing it. | The full spec (dialects, translations, tabular profiles) is for data publication. Fernwood needs ~6 keys per resource. Kept: the registry idea. |
| [Simon Willison — Useful patterns for building HTML tools (2025-12)](https://simonwillison.net/2025/Dec/10/html-tools/) | Single-file tools need no build step and any LLM can read them — **explicitly at "a few hundred lines."** | **§4.** The honest cap on Paul's AI-aware-maintainability principle. Fernwood is 17,879 lines / ~400K tokens, i.e. past the point where an agent can read it whole. Directly motivates F13. | Its other half — *"for a production app with a team, use modules and a bundler"* — is the enterprise assumption. **Explicitly discounted:** no team, no reviewers, and a build step would sit between Guru and the live app. |
| [vcrpy](https://vcrpy.readthedocs.io/en/latest/usage.html) · [pytest-recording](https://github.com/kiwicom/pytest-recording) · [Nayak — VCR tests for LLMs](https://anaynayak.medium.com/eliminating-flaky-tests-using-vcr-tests-for-llms-a3feabf90bc5) | Record HTTP once into cassettes, replay offline forever; redact auth headers in `conftest`. Deterministic, fast, free. | **§5.3 Layer 2** (the replay layer) and the redaction convention. | This is the *only* LLM-testing source that transfers cleanly. The 2025 "LLM eval platform" category (LangWatch et al., agent simulations, multi-layer eval) is priced and scoped for teams shipping to real users — for 0.54 turns/day it is pure overhead. **Explicitly discounted.** |
| [Splunk — exclude synthetic monitoring from analytics](https://help.splunk.com/en/splunk-observability-cloud/digital-experience-monitoring/synthetic-monitoring/set-up-splunk-synthetic-monitoring) | Standard practice is to filter synthetic traffic out of analytics — by IP at the analytics layer. | **§5.2.** Confirms the *shape* (tag synthetic, filter downstream) but the IP-based version is unavailable here. Fernwood's own `is_instrumentation()` / `excludeFromEngagement` are the better local precedent — **and its own note ("a flag that must be re-set is a flag that will be missed") is a sharper rule than the vendor guidance.** | Enterprise version assumes a separate analytics product with a filter UI. Here it is a five-character id prefix. |
| [Fitness functions / operationalizing ADRs (2025-26)](https://platformtoolsmith.com/blog/operationalizing-adrs-fitness-functions/) · [Architecture drift detection](https://earezki.com/ai-news/2026-06-08-architecture-drift-detection-keep-your-code-aligned-with-design/) | *"Documentation does not stop drift — running checks do. If a rule exists only in documentation, it's a candidate for a fitness function."* | **§6.** Gives the `check-claims.py` pattern a name and outside backing. | ArchUnit / dependency-cruiser / PR-gated CI is a team answer. Here: one Python file in a session-start check that already runs. **The local `momlib` self-dating principle is the stronger statement and predates the reading.** |

---

# 8 · SEQUENCING

**On the Track A/B ranking the brief asks for — the trade is partly false.** Reading Track B's open
rows: they are overwhelmingly *Paul-physical* (a trip to the truck with a light, a poke test, phone
calls to Larry and Super Upholstery, odometer readings). They barely compete for agent hours at all;
they compete for **Paul's** hours. The engineering-drivable backlog is almost entirely A and C. So:

> **B1 first because it is the only thing on the whole board with an external clock** (GTI spare key +
> service). Then C's instrument work. Then A. The A-vs-B question resolves into "Paul does B's physical
> items on his own schedule; agents work C then A" — which is not a ranking conflict, it is two queues.

**Within the engineering queue, in order, with the reason each position is what it is:**

| # | Item | Why here |
|---|---|---|
| **1** | **F11 — the Guru synthetic-conversation fix (~15 lines) + Layer-1 offline harness** | It is the gate on all of A6, it is the only item that *cleans* the instrument, and a stray test conversation is currently **visible to Mom** in the most-opened card. Ship the Worker predicate the same session. |
| **2** | **F1, F2, F9, F3, F6, F7, F8, F10** — the Tier-1 sweep | All ≤1 hr, all agent-drivable, no decisions. F1 and F2 are live grounding hazards on Mom's surface (a fake zone and 34 falsified soil-series assertions). F6 is time-sensitive — August. Do them as one commit-per-item pass. |
| **3** | **F15 — `check-claims.py`, seeded with F3/F4/F5** | Small, and it must land **before** the migration, not after. Fix F4 (`CLAUDE.md` Architecture) as its first claim. |
| **4** | **F5 → then F13 — the data split** | F5 (7 drift rows) is the interim; F13 makes the file editable-by-agent again and makes the migration diffable. Half a day, no decisions, large payoff. |
| **5** | **F17–F19 — Paul answers the three taxonomy questions** | Ten minutes of conversation. Everything after this is blocked on it, and nothing before it is. |
| **6** | **F16 — taxonomy steps 1–3 (envelope · registry · harvester)** | The big one. Mom-invisible throughout. Closes the Track C row *and* solves A3's card-supply problem at the root. |
| **7** | **F14 — Ambient: proxy → rotate → strip** | Genuinely deferrable (read access to one weather station), but the unpark trigger is met and the sequencing hazard (rotating before the proxy re-publishes the new key) is worth landing while it is in someone's head. |
| **8** | **F12 — the soilNotes prose sweep** | Reaches Mom, so it is gated on Paul's wording. Do it when he has an hour for authored content. |
| **9** | **A6's zones + turf digest add** | Held until after #1, because it is the first change that *needs* the harness — and after F1 the digest's zone story is coherent enough to add real zones to. |

**Two things deliberately NOT in the queue:** the taxonomy question does not wait on Mom (§0.5), and
W6 does not get designed until Paul has shot at §0.7.

---

# 9 · WHAT I COULD NOT DETERMINE

| # | Open | What would settle it |
|---|---|---|
| **U1** | Whether the `AMBIENT_APP_KEY` / `AMBIENT_API_KEY` GitHub Actions **secrets actually exist**. The workflow references them; if they are unset the CI runs have been silently using the hardcoded fallbacks all along, which changes F8 from "delete dead code" to "delete the only working credential path." | `gh secret list` on the repo, or one Actions run log. **Check before deleting the fallbacks.** |
| **U2** | Whether the Ambient key has ever actually been *used* by a third party. Blast radius is read-only and small, but "exposed 85 days" and "abused" are different facts. | Ambient's dashboard (Paul's account) — request counts / rate-limit history. |
| **U3** | Real gzip transfer size of `viewer.html` on GitHub Pages, and whether Pages is serving HTTP/2 to Mom's phone. This is the strength of the "one request is better for her" argument in §4.2. | `curl -sI --http2 -H 'Accept-Encoding: gzip' <pages-url>/viewer.html`. Not blocking — F13 is right either way. |
| **U4** | Whether `zoneIds[]` (§0.7) actually covers the real multi-zone plant cases, or whether some plant genuinely needs per-instance *care*. I could not tell from the data — 23 nulls hide the answer. | Paul assigning `zoneId` on even 5 of the 23 nulls (the W2 payoff, already on the board) would show whether any species lands in more than one zone. **That is the cheapest possible experiment and it is already queued.** |
| **U5** | Whether `RELEASE_NOTES_DATA`, `MOM_ACK_DATA` and `CELESTIAL_DATA` should be in a drift check. They have builders/derivations rather than a source JSON, so F5's fix does not obviously cover them. | 15 minutes reading `build-release-notes.py` and whatever generates `CELESTIAL_DATA`. Low stakes. |
| **U6** | Whether the four Guru "fence flows" and the promote-species drafter would actually break under a digest reshape. A6 ⑥ asserts they "depend on digest-exact naming and get rewritten"; I did not trace all five call sites. | Trace them as part of harness Layer 1's coupling assertions — the harness is where that knowledge should live anyway. |

---

## Principles this run would propose (NOT applied — Paul's confirm required)

Three candidates, all earned by evidence in this report rather than by reading:

1. **`A field name shared across domains must mean one thing`** *(project: Fernwood)* — `status` means
   four different things in six domains, and that ambiguity is the same class as "assumed plants" one
   level up. Statement: a name reused across record types is a promise about semantics; if two domains
   need different meanings, they need different names.
2. **`A claim about another file's behaviour is either a check or a lie-in-waiting`**
   *(cross-project candidate)* — §6. Extends the existing self-dating principle from *status* to
   *claims*. Second application of the falsifier/probe mechanism; note it, don't promote it yet.
3. **`Record a security finding by symbol, never by line number`** *(cross-project candidate)* — the
   Ambient pointer has been wrong twice in five days, and a stale line number on a security item is
   indistinguishable from "already handled." Cheap, general, and it generalizes to any long-lived
   pointer into a file that grows.
