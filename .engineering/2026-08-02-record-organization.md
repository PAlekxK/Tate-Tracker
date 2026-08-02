# How should the record be organized, holistically?

**Answering Paul's 2026-07-28 question** — *"technically, weeds are plants, right? I think we need a
holistic view of how to organize all the information."* Raised off the `harvest-questions.py` weed
gap, which the BACKLOG row correctly reframed as a *symptom of an unanswered taxonomy question*
rather than a wiring bug.

**Method:** surveyed the actual field inventory of all 11 domain files rather than reasoning from the
domain names. Counts below are measured, not recalled.

---

## The finding: the domains are already right. The uncertainty contract is what's missing.

Three things the survey settles, and all three cut against a reorganization.

### 1. A universal spine already exists, unplanned

Every living-thing record in every domain already carries the same seven fields: `id`, `name`,
`scientificName`, `emoji`, `photo`, `attribution`, `notes`. Nobody designed that — it accreted — and
it is the same in plants, weeds, birds, mammals, amphibians, snakes, lizards and fish. There is
nothing to unify here; it is already unified.

### 2. The five wildlife files are one schema wearing five filenames

| file | records | shape |
|---|---|---|
| `birds.json` | 16 | `status` · `statusLabel` · `monthsPresent` · `peakMonths` · `habitat` · `voice` · `feeder` · `ebirdCode` |
| `mammals.json` | 19 | `status` · `statusLabel` · `monthsPresent` · `peakMonths` · `habitat` · `voice` |
| `amphibians.json` | 12 | `type` · `statusLabel` · `monthsActive` · `peakMonths` · `habitat` · `call` · `size_in` · `appearance` · `conservation` |
| `snakes.json` | 12 | `type` · `venomous` · `statusLabel` · `monthsActive` · `peakMonths` · `habitat` · `size_in` · `appearance` · `conservation` |
| `lizards.json` | 5 | same as snakes |

They diverge only in local extensions that genuinely belong to their subject (`feeder` is meaningless
for a snake; `venomous` is meaningless for a wren). All five also carry `propertyHighlights` and
`seasonalCalendar` at the top level. **Merging them would cost a migration and buy nothing.**

### 3. The real divergence is on ONE axis, and it is the honesty axis

Each record answers some subset of four questions. Three are in good shape; one is not.

| axis | question | state |
|---|---|---|
| **Identity** | what is it? | ✅ universal, seven shared fields |
| **Time** | when is it doing something? | ⚠️ every domain has one, each names it differently — `monthsPresent` / `monthsActive` / `care.*.months` / `bloom.dates` / `seasonNotes` |
| **Action** | what do we do about it? | ✅ correctly domain-specific — `care` / `combat` / `maintenance` / `serviceHistory` |
| **Honesty** | how sure are we? | 🔴 **four different shapes and one total absence** |

Measured state of the honesty axis:

- **`weeds.json`** — top-level `confidence` + `status`, plus real observation provenance
  (`observedOn`, `observedZones`, `observedBy`) and an explicit `momConfirm`. **This is the best
  design in the repo** and it is the newest, which is not a coincidence.
- **`plants.json`** — nested and partial: `variety.confidence` on **3 of 36**, `bloom.confidence` on
  **24 of 36**, a `_provenance` block on **8 of 36**. Also 178 `seasonNotes` with **zero** markers.
- **wildlife** — **0 of 64 records** carry any confidence field at all. Sixty-four records assert an
  animal is present on this property with no way to say *"we think."* (Already known as Tier-3 #7;
  the survey confirms the count and shows it is the same defect as the weed gap, not a separate one.)
- **`vehicles.json`** — per-value `confidence` inside `maintenance`, a fifth shape again.

---

## Why this is exactly why `harvest-questions.py` can't be wired

The BACKLOG describes the harvester as "the one remaining plants-only site." **That understates it.**
It does not merely read `plants.json` — it hardcodes two *field shapes*:

```python
v = p.get("variety")
if isinstance(v, dict) and v.get("value") and v.get("confidence") != "verified" and v.get("askable"):
b = p.get("bloom")
if isinstance(b, dict) and b.get("confidence") == "inferred" and isinstance(b.get("dates"), list):
```

So repointing it at `weeds.json` would find **zero** candidates — not because the file is wrong, but
because weeds express uncertainty top-level while the harvester only knows the nested plant shape.
That is precisely why `crabgrass`, `virginia-creeper` and `wild-violet` — all `confidence: inferred`
and `status: needs-confirmation`, i.e. *explicitly marked as askable in their own vocabulary* — can
never be harvested, while two weeds got hand-authored cards.

**The harvester does not need to learn about domains. It needs to stop knowing about `variety` and
`bloom` and start knowing about "a marker."**

---

## The answer to "technically, weeds are plants"

Biologically, yes. **But the split in this record has never been biological — it is what you DO.**
You *tend* a plant and you *fight* a weed, and those want different fields (`care` months vs
`combat`, `seedTiming`, `lookFor`), a different voice, and a different question to Mom.

Mom proved which axis is hers. Unprompted, she derived **vehicles / equipment / household systems** —
a split by what you do with the thing, not by what it is. The field-journal framing already floated in
the BACKLOG ("things I tend / things I fight / things that visit / things that run the place") is that
same action axis.

**So: biology is a PROPERTY of a record, not a folder.** Weeds stay their own domain. `scientificName`
already carries the taxonomy for anyone who wants it, and nothing is lost.

---

## Recommendation — three moves, dependency-ordered. None is a reorganization.

**M1 · One uncertainty contract, every domain.** A single way to say *"we think X, and someone standing
on the property could settle it"* — usable top-level on a record **or** on any single field. Weeds
already has essentially this shape; adopt it as the contract rather than inventing a new one. Then
rewrite `harvest-questions.py` to harvest **any marker in any domain** via `momlib`, instead of two
plant field names. *This is the whole unblock; everything else is optional.*

**M2 · One temporal accessor, not one field name.** Add a `momlib` resolver that answers "when is this
observable" for any record, reading whichever key that domain already uses. **Do not rename fields
across 64+ records** — the rename buys nothing the accessor doesn't, and costs a re-inline of every
domain plus a viewer sweep.

**M3 · Declare the action group in each `_meta`.** `tend` / `fight` / `visit` / `run-the-place`.
`vehicles.json` already carries a `group` field doing exactly this. This is metadata, not migration —
and it is the thing that would let Mom's navigation follow her own mental model later, without
committing to any UI now.

### What this unblocks
Weed cards · wildlife cards (64 records that can finally say "we think") · **season-note cards**, the
producer that Tier 3 of the season-notes reframe depends on.

### What it explicitly does NOT do
Merge any file · rename any field · touch Mom's surface · answer the UI question.

### The risk to watch, and it is not the schema
M1 plus a domain-agnostic harvester means **new cards in front of Mom**. The binding constraint
becomes the 5-slot visible cap immediately — the bench already holds 8 drafted and 0 approved. So M1
must ship with Paul's clear gate untouched, and the thing to monitor is **card supply**, not the data
model. A harvester that can suddenly see four domains is a supply problem wearing a schema costume.

---

*Status: recommendation, Paul's call. Nothing here has been implemented.*

---

## SHIPPED the same day — M1 (structure) and M3, Paul-approved

Paul approved M1 and M3 and added the requirement that shaped the build:
*"let's have a holistic structure that allows all these various files and categories of content to be
somewhat modular across, especially some of the capture surfaces that we're building. And we want to
limit how much they diverge as they continue to be enriched over time."*

**Landed:**

- **`momlib.DOMAINS`** — the one declaration, all 10 domains, each carrying `group` (M3's action axis),
  `time`, `markers` and `cardable`. `EntitySource` widened to `Domain` **without moving positions 0–2**,
  so every existing index and attribute read still means what it did.
- **`momlib.markers(record, dtype)`** — M1's core. Normalises weeds' top-level `confidence`, plants'
  nested `variety`/`bloom`, vehicles' per-value `maintenance.*.confidence` and zones' `status` into one
  shape. Supports `*` in a marker path. Infers `askable` from each domain's own vocabulary
  (`askable` flag · `status: needs-confirmation` · else non-verified-means-ask).
- **`ENTITY_SOURCES` is now DERIVED** from `cardable`, so `entity_map_divergence()` keeps guarding
  precisely what it guarded before. Verified: the map is byte-identical for positions 0–2 and
  divergence is still `[]`.
- **`tools/check-domains.py`** — the anti-drift mechanism, wired into the session-start block. Asserts
  every domain resolves, declares a known group, has its inlined const present, and that every declared
  temporal key exists on real records. Reports honesty coverage per domain. **And it catches the case
  nothing could see before: a domain file appearing on disk that nobody declared** — undeclared files
  must land in `DOMAINS` or in `NON_DOMAINS` *with a reason*, so "we decided this isn't a domain" and
  "nobody looked" stop being the same state.

**Regression-checked, all passing:** `check-cards.py`, `test-feedback-cycle.py` (incl. its RESOLVE leg),
`rationalize-bench.py`, `check-data-inline.py`.

**First run's standing output** — six domains with no way to admit a guess at all:

| domain | group | records | marker paths | with marker | askable | wired |
|---|---|---|---|---|---|---|
| plant | tend | 36 | 2 | 21 | 21 | card |
| weed | fight | 5 | 1 | 5 | 5 | card |
| vehicle | run | 16 | 1 | 14 | 0 | — |
| zone | place | 10 | 1 | 10 | 0 | — |
| bird · mammal · amphibian · snake · lizard · fish | visit | 64+3 | **0** | 0 | 0 | — 🔴 |

**Not done, deliberately:** backfilling markers onto the wildlife domains (authoring judgement about
what is actually uncertain, not a migration), and rewriting `harvest-questions.py` to consume
`markers()`. The second one puts new cards in front of Mom, so it ships behind Paul's clear gate with
card supply as the thing to watch.

---

## Two canon gaps the season-note lint surfaced — recorded, NOT fixed

`tools/check-season-notes.py`'s useful residue (2 of 6 findings) both point the same direction:
**the prose knows something the structured record does not.** Neither was corrected, deliberately —
both would change what renders on Mom's plant cards, and the correction is a botanical judgment, which
makes it a model read. *A model-read value is a hypothesis until a deterministic source or Paul
confirms it.*

**1 · `dwarf-papyrus` (Cyperus prolifer) — `bloom: null`, but the note describes flower heads.**
Its May note reads *"The flower heads root too — it sprouts plantlets, which is what the name means."*
So the plant visibly flowers and the record cannot say when.
⚠️ **The obvious fix is the wrong one.** Adding a `bloom` window with `confidence: inferred` would
immediately make it harvestable — and the card would ask *"is it in flower yet?"* about a **persistent
umbel that is present all season**. That is a question with no answer, on a 5-slot surface, to a reader
whose engagement is fragile. The honest resolution is probably an explicit *"no distinct bloom event"*
declaration the lint can read — which is a **schema decision**, not a data entry, and belongs with the
M1 marker work rather than being smuggled in here.

**2 · `garden-phlox` — the July note says deadhead; `care.prune` months don't include July.**
*"…deadhead the spent trusses to keep it going"* renders in July, while the prune months are
Apr · May · Nov · Dec. Deadheading phlox through its bloom is ordinary practice, so the likeliest read
is that **the care data is incomplete, not that the note is wrong** — but "likeliest read" is exactly
what this project does not promote to canon unaided.

**Both are the same shape as the finding that motivated M1:** the record's structured half and its
prose half disagree, and only the prose was ever authored with the whole plant in mind.
