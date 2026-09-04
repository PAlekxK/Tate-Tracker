# vocabulary-nicknames · One concept registry; every estate — and the person living there — names each thing; the internal id never moves
- row: BACKLOG.md § FREEZE block → "THE DEVELOPMENT GOAL" (amended 12:05 PM ET: naming is a first-run step the person answers) · § C7 (identity.journalTile/journalShort are agent placeholders)
- objective: O3 (the Product Engine) · feeds the onboarding plan (queue #7)
- class: engine · declared (viewer identity fill · Worker honesty strings · digest identity · a lint)
- seats: content-steward → .content-reviews/2026-09-04-vocabulary-nicknames.md
         engineering-partner → .engineering/2026-09-04-vocabulary-nicknames.md
         ux-expert → deferred to the onboarding plan (the naming STEP is a first-run surface; this plan is the registry beneath it)
         user-researcher → deferred to the onboarding plan (same reason)
         ai-advisor → waived: no model on any path here; capture is deterministic by rule
- depends-on: .plans/2026-09-03-c5-record-prep-PLAN.md (identity block · instance/<estate>.json)
- depends-on: .plans/2026-09-03-c7-condo-paper-model-PLAN.md (the placeholders this retires)
- ready: DRAFT — both seats RAN 2026-09-04 ~1:20 PM ET and are folded in below (§4); Paul has not stamped
- stage: proposal
- stage-note: SEATS FOLDED 2026-09-04 ~1:25 PM ET — content-steward (`.content-reviews/2026-09-04-vocabulary-nicknames.md`, 15 findings) + engineering-partner (`.engineering/2026-09-04-vocabulary-nicknames.md`, 12 findings); the main session verified the load-bearing claims (WORKER_BASE is a Fernwood literal in the engine template; `almanac_history_opened` has zero consumers; `digest.core.names` is the entity index; 9 hard-coded "Mama's Perspective" sites). §1a–§1f stand as drafted EXCEPT where §4 amends them.
- stage-note: drafted 2026-09-04 ~12:10 PM ET from Paul's ask (*"a pretty robust proposal"* — people may name things themselves; the internal name is what we call it, recorded beside their nickname) and the three-referent comment in the viewer (2026-07-30) — see §0.

## 0 · What is true today, measured 2026-09-04

Three things a word can point at, and the code already knows it (`engine/viewer.template.html`, the CARD 2 comment, 2026-07-30):

| referent | Fernwood's word | who named it | where it RENDERS | filled from |
|---|---|---|---|---|
| **the place** | *Fernwood* · *"An Appalachian Almanac for …"* | Paul | masthead title · h1 · subtitle · address line · property tile + sub | `instance/fernwood.json` identity: `name` · `taglinePrefix` · `addressLineSuffix` · `propertyTileSub` ✅ |
| **the record** (the knowledge door: canon + library + the Guru's voice) | *the Fernwood Almanac* · *the Almanac* | Paul (7/30) | Guru card title (×3 sites) · *"Save & consult the Almanac"* · 5 Guru status lines · 6 storage/sync messages · Worker honesty strings · digest identity | identity `journalTile` / `journalShort` — **misnamed: they name the RECORD, not her journal** — and **12 hard-coded "Almanac" strings** the fill never reaches |
| **her words** (what she wrote, looked back at) | *Journal* · *field notes* | **Mom** (7/29: *"is there a way to look back at these, eg in the journal?"*) | dashboard cell *"Look back at what you've written"* · the field-notes card · *"field notes — to sort"* · *"Saving to the field notes…"* · `almanac_history_opened` (a metrics name that says the wrong referent) | hard-coded engine words |
| **rooms of the record** | *the safe* (vault) · *the library* (references + manuals) | Paul (9/04, steward-reviewed) | Guru honesty strings only | hard-coded by ruling: engine furniture, names an object in a house |
| **the station** | *Fernwood Weather Vane* | Paul | weather card | identity `stationName` ✅ |
| **the product** | `myhome.place` · her icon label *"Fernwood Tracker"* (hers, untracked) | ruled 9/03 | address bar · her home screen | not a build concern; the label is hers and lives nowhere in the repo |

The condo today: `journalTile: "Midtown Notes"`, `journalShort: "the Notes"`, tagline *"A field journal for a home in the city"* — all marked PAPER-MODEL placeholders. `VOCABULARY.md` §4 rules "Almanac" non-portable (a genre promise) and rejects log · tracker · guide · manager · hub · portal · dashboard for the same reason.

**The defect in one sentence:** the key that names the record is called `journal`, the record's word is typed into twelve engine strings the instance cannot reach, and nothing records WHO named a thing.

## 1 · The proposal

### 1a · A concept registry — the internal vocabulary, fixed, in `engine/concepts.json`
One row per nameable concept. The **id** is what we call it internally, forever; code, keys, metrics, docs and the seats speak in ids. Each row carries the engine's **default** display (used when nobody has named it), the **article rule**, and the **surfaces** that render it (so the lint knows where to look).
```
{ "id": "record",  "meaning": "the knowledge door — canon + library + the Guru's voice", "default": {"name": "{{place}} Record", "short": "the record"}, "portable": true,  "nameable-by": ["instance", "person"] }
{ "id": "journal", "meaning": "what the person wrote, looked back at",                   "default": {"name": "Journal", "short": "the journal"},           "portable": true,  "nameable-by": ["instance", "person"] }
{ "id": "place",   "meaning": "the estate itself",                                       "default": null (REQUIRED at build),                                "portable": false, "nameable-by": ["instance"] }
{ "id": "safe",    "meaning": "the vault, as the reader meets it",                       "default": {"short": "the safe"},                                   "portable": true,  "nameable-by": [] }
{ "id": "library", ... }  { "id": "station", ... }  { "id": "guru", "meaning": "the voice", ... }
```
`nameable-by: []` = engine furniture (Paul's 9/04 ruling on *the safe*): a fixed word, never a nickname. **The registry is engine; it never carries an estate's word.**

### 1b · Per-estate names — `instance/<estate>.json` → `identity.names`, each with provenance
```
"names": {
  "record":  { "name": "Fernwood Almanac", "short": "the Almanac", "by": "paul", "at": "2026-07-30", "how": "instance" },
  "journal": { "name": "Journal",          "short": "the journal", "by": "person:<id>", "at": "2026-07-29", "how": "her words" }
}
```
A missing row → the registry default. **A person's nickname and Paul's config word are the same shape, distinguished only by `by`/`how`** — no second file, no second mechanism (the c6 overlay finding, re-applied). The **internal id** is the key, so nothing is lost when the word changes: the estate's `names.record` moved from *"the Notes"* to whatever she says, and `record` is still `record` everywhere.

### 1c · One resolver, every surface
- **Viewer (build time):** `{{IDENTITY:journalTile}}` and friends become `{{NAME:record.name}}` / `{{NAME:record.short}}` / `{{NAME:journal.short}}` …; `build-viewer.py` fills from `names` → registry default, FAILS LOUD on an unknown id. The 12 hard-coded "Almanac" strings become `{{NAME:record.short}}` sites (measured list in §0). JS gets ONE object `NAMES = {record:{name,short}, journal:{…}}` and the existing `JOURNAL_NAME` const retires.
- **Worker (deploy time):** digest `core.identity` carries `names` verbatim; `LOOKUP_STRINGS_TEMPLATE`'s `{journal}` becomes `{record.short}` (the strings already MEAN the record: *"not in the Almanac"*). The Guru's system prompt says the estate's words for record/journal once, in the identity block.
- **Runtime (after onboarding names a thing):** the Worker holds the estate's `names` in KV (`<estate>:names`), written ONLY by the onboarding step / a settings surface through a grant (C6 authority rules); the viewer reads it at boot and overrides the built-in `NAMES` — so a rename needs no rebuild and no deploy. The build-time fill is the DEFAULT; the KV row is the person's word.
- **Metrics:** event ids speak concept ids (`record_history_opened`, not `almanac_…`) — a rename of the metric is a migration; the seat says whether to alias or cut over.

### 1d · Naming as a first-run step (the onboarding plan owns the surface; this plan owns the contract)
Deterministic, no AI: one question per `nameable-by: person` concept, in the estate's default word — *"What do you want to call the place where everything about this home lives? (we call it the record)"* — her answer lands in KV with `by: person:<id>`, `how: "onboarding"`, `at`. Skipping keeps the default and records that she skipped. The Guru, the cards and the honesty strings say her word from the next load. **The internal name is shown beside the box, once, so it is never a secret** (*"recorded as that estate's name for the record"*).

### 1e · A lint — `tools/check-concept-words.py`
Greps engine text (template markup + JS string literals + Worker strings, outside the `*_DATA` consts and comments) for any estate's display word or registry default (*Almanac · Journal · field notes · Weather Vane …*) that is NOT a `{{NAME:…}}` site. Red on a hit; the `place-claims.py` shape (register + ratchet). Session-start block + CI (`build-viewer.yml`).

### 1f · Migration of what exists
`journalTile`/`journalShort` → `names.record`; `stationName` → `names.station`; the condo placeholders → `names.record = {name:"Midtown Notes", short:"the Notes", by:"agent", how:"placeholder"}` until a person names it. **Fernwood byte-identical after the pass** (the C5 5c control: eight rendered regions hashed before/after). `VOCABULARY.md` gains §3f (the registry) and §4 keeps its rejections.

## 2 · Falsifier
Build the condo with `names.record` = *"the Housebook"*, load QA, ask the Guru a lookup that misses: it must say *"not in the Housebook"*; the card title, the save button and the storage messages must say the same word; Fernwood's eight regions hash-identical; the lint finds zero literals. Then set a KV `names` row by the runtime path with a different word and reload without a build: the viewer and the Guru say the new word.

## 3 · Open for Paul (after the seats)
1. The condo's record word until she names it (Housebook recommended; Ledger; Notes).
2. Whether `journal` is nameable by a person, or stays the engine word because Mom named it once (her word is the precedent for the mechanism, and also the argument for leaving it).
3. The metrics rename: alias (both ids reported for a lap) or cut over.

## 4 · AMENDMENT after the seats (2026-09-04 ~1:25 PM ET) — what changed, and why

Both trails are cited, not restated. Where the seats agree with §1 nothing is repeated here; every line below OVERRIDES the section it names.

**§1a ids — split and extend.** `record` and `guru` are two things (the corpus vs the voice that answers from it): `guru` gets `default: null` and renders nowhere as a word. Add **`perspective`** (the question queue, "Mama's Perspective" — 9 hard-coded engine sites, and a name that is HERS at Fernwood and false at a condo), the **reference drawer**, and a ruling row for **module labels** ("Gardening" is false at a gardenless condo) — the steward's list. `safe` and `library` stay furniture.

**§1a defaults — adopt `{{place}} Record` / `the record`.** Decisive: *"the record"* is already live reader-facing copy in her save confirmations, so it is a word she has met. Fill rule: a name must work as a title, an object and a subject (*"the record"*, *"in the record"*, *"the record has no…"*).

**§1b key + schema — `identity.words`, not `names`.** `names` is taken (`digest.core.names` is the entity index the Guru's own prompt describes). Row shape: `{name, short, article, proper, by, at, how}` — `short` stored BARE (no article), `article` derives *the/a/none*, `proper` (true for *Almanac*, false for *record*) drives sentence-case and is the lint's filter; derive possessive; store no plural.

**§1c — runtime reads, not sixteen placeholders.** The engineer measured **16** rendered "Almanac" sites, not 12, and `build-viewer.py`'s `extract()` is a hand-written inverse — sixteen placeholders means sixteen recovery regexes, and a build-baked string cannot be overridden by the KV row §1c itself promises. So: ONE built object (`WORDS = {{WORDS}}`, one placeholder, one regex) and every site reads `WORDS.record.short` at render. The Worker/digest half stands. ⛔ **Gate on a prerequisite the plan had not seen:** `WORKER_BASE` is a hard-coded Fernwood literal in the engine template, so a condo build would boot-read FERNWOOD's KV words row — "two estates, one request" through a new door. The Worker base becomes instance config before any runtime words row ships.

**§1d — nameable ≠ asked-at-setup, and `journal` IS nameable.** Nameable by a person: `record` · `journal` · `place` · `station` · `perspective`. Her having named the journal once is the argument FOR the mechanism, not against it. The steward's caution, recorded whole: **every ask this project has authored is 0-for-30 with her** — so the setup step pre-fills the default, shows the internal word once *in the sentence* (never the word `estate`, which is banned from any surface), and a skip costs nothing and records that she skipped. Paul's ruling that naming is a first-run step stands; the steward's four question drafts are in the trail and go to the onboarding plan.

**§1e — a RATCHET, not "red on a hit".** Sixteen hits on day one makes a red nobody reads. `place-claims.py` shape: a register with a baseline, red only when the count GROWS; lint the TEMPLATE (so canon excludes itself), with an identifier-boundary rule that clears CSS classes, storage keys and metric ids in one stroke.

**§1c metrics — cut over.** `almanac_history_opened` → `record_history_opened`; zero consumers in `tools/` or the Worker (verified), so no alias lap; the succession is recorded in the event's comment.

**§1f — migrate by REFERENT, not by key.** `journalTile` fills TWO referents at three sites (the Guru card title = the record; the dashboard cell label = the journal), so `journalTile → words.record` would rename her Journal cell "Fernwood Almanac". Each site is classed to its referent first; the migration is per site.

**§3 open for Paul — revised.**
1. ~~Housebook / Ledger / Notes~~ — the steward rejects all three (a condo unit is not a house — the same day's place-claims ruling; Ledger says money; *the Notes* is plural and is the journal's word). **Recommendation: the engine default, *the record*, until she names it.** If Paul wants a warmer placeholder: *the Homebook* (*home* is the ratified claim-word — "your homes").
2. ~~Is `journal` nameable~~ — yes, per §1d.
3. ~~Metrics alias vs cut-over~~ — cut over.
4. NEW: stamp the amended scheme so §1–§4 become the build spec (items 2 and 7 on the independent queue depend on it).
