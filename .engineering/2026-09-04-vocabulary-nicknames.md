# engineering-partner · vocabulary-nicknames (concept registry · per-estate names · one resolver)

- plan: `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` (stage: proposal · DRAFT, seats not run)
- seat: engineering-partner · mode: path-evaluation + review
- read: `tools/build-viewer.py` · `engine/viewer.template.html` · `worker/worker.js` · `tools/build-digest.py` ·
  `tools/check-vocabulary.py` · `tools/place-claims.py` · `tools/qa-divergence.py` · `tools/check-qa-fixtures.py` ·
  `tools/check-storage-keys.py` · `tools/check-telemetry.py` · `tools/read-mom-funnel.py` · `tools/read-mom-engagement.py` ·
  `tools/analyze-fernwood.py` · `ENGINE-MANIFEST.md` · `VOCABULARY.md` §3b/3e/4 · `instance/fernwood.json` ·
  `.plans/2026-09-03-c4-environments-PLAN.md` §5b/5b-guards/5c · `.plans/2026-09-03-c6-door-for-paul-PLAN.md`
- NOT read (by instruction): `.private/**`, Mom feedback files
- deployment context: **mom-ready** · robustness: **shippable** · the customer is Mom on a 414 × A+ phone, at a place
  with no cell reception and heavy canopy (`CLAUDE.md` § THE SITE'S PHYSICAL PREMISE)

---

## 0 · Context this review is calibrated to

The plan is good and the shape is right: one internal id, per-estate display words beside it, provenance on every
word. What follows is not "this is wrong"; it is five places the plan's numbers or sequencing would bite, and two
places where a smaller design does the same job.

**The one thing I would change before anything else** is §1c's sentence *"The 12 hard-coded 'Almanac' strings become
`{{NAME:record.short}}` sites."* Make them **runtime `NAMES.record` reads, not build-time placeholders.** Reason
below (F1) — it collapses ~16 hand-written `extract()` regexes into one and is the difference between this landing in
a weekend and it becoming a `--extract` maintenance surface.

---

## 1 · Schema — is `{name, short, by, at, how}` enough?

**No, by two fields; and one of the plan's implicit fields should not exist.**

### What the running code actually needs, measured

Three renderers consume the record's word today, and they disagree about the article:

| site | role | shape it needs |
|---|---|---|
| `worker/worker.js` `LOOKUP_STRINGS_TEMPLATE` — *"not in {journal}"*, *"that part of {journal} needs the login"* | Guru honesty strings, **mid-sentence** | the word **with** its article: *"the Almanac"* |
| `engine/viewer.template.html` — the storage/sync failure strings (*"The Almanac isn't connected yet"*, *"The Almanac can't reach the network just now"*) | **sentence-initial** | capitalised article: *"The Almanac"* |
| `engine/viewer.template.html` — the field-notes intro and the household-systems prompt | mid-sentence, and they already do `"the " + JOURNAL_NAME` **with a hand-written `"the journal"` fallback** | bare word + article applied by the caller |

So the article is currently expressed **three different ways in three places**, one of which (`JOURNAL_WORD` in
`worker.js`) carries a comment admitting the derivation breaks for *"a name that takes no article."* The plan's
`{name, short}` does not resolve this — it just moves the ambiguity into the registry.

### The minimal shape I'd propose

```
"record": {
  "name":    "Fernwood Almanac",   // the full form. Always proper-cased. Masthead, tiles, card titles.
  "short":   "Almanac",            // BARE — never carries "the", never sentence-cased.
  "article": "the",                // "the" | null. How `short` is spoken inside a sentence.
  "proper":  true,                 // does the capital survive mid-sentence?
  "by": "paul", "at": "2026-07-30", "how": "instance"
}
```

Five content fields, three provenance. Everything else is **derived by the resolver, not stored**:

- **mid-sentence** = `article ? article + " " + short : short` → *"the Almanac"* · *"the journal"* · *"Housebook"*
- **sentence-initial** = uppercase the first character of the mid-sentence form → *"The Almanac"* · *"The journal"* ·
  *"Housebook"*. One rule, correct for all three cases. **No stored field.**
- **possessive** = `+ "'s"`, `+ "'"` when it ends in *s*. No rendered possessive exists today (the only *"the
  Almanac's"* in the template is inside a decision comment) — so **do not store it, do not build it** until a site
  needs it. Same for **plural**: zero rendered plurals; storing one now is the wrong abstraction, cheaply avoided.

### Why `proper` earns its place, and why it is not decoration

`proper` does no rendering work — `short` already carries its own casing. It earns its row because **it is the
lint's filter** (see §4). A proper noun (*Almanac*, *Housebook*, *Midtown Notes*) is greppable in engine text. A
common noun (*journal*, *notes*, *record*) is not distinguishable from ordinary prose, and a lint that greps for
*"journal"* across `engine/viewer.template.html` is red on day one and every day after — the **costly-control**
signature Paul has already ruled against and which `check-vocabulary.py`'s own N8 guard is written around
(*"a checker that fired on every legacy occurrence would be red forever on day one"*). `proper: false` means *the
lint does not chase this word*; that is a real decision and it belongs in the data.

### One naming hygiene note

Do not mint **`nickname`** as a schema key here. `vehicles.json` already carries `nickname` per record and
`build-digest.py`'s lookup rows pass it through — that would be `VOCABULARY.md` §5's `group` defect (one name, two
meanings, one repo) minted deliberately. The plan's *title* can say nicknames; the schema should say `names`.

---

## 2 · Build-vs-runtime split (§1c)

### "Synchronous-inline `<script>` that fetches before render" is not available

A browser cannot block first paint on `fetch` — it is async by construction. The only synchronous form is
synchronous `XMLHttpRequest`, which is deprecated, and which on Mom's device would **hang the page on the exact
condition the site's physical premise guarantees**: no cell, canopy, Wi-Fi that falls off with distance from the
house. A sync boot read turns "the Worker is slow" into "the app is blank." That option should come off the table
explicitly, not by omission.

### Recommended ordering — three layers, cheapest first

```
1. BUILT DEFAULT   the NAMES const filled by build-viewer.py   → always present, works offline, works from a file://
2. LOCAL CACHE     tateTracker.names.v1 in localStorage        → what FIRST PAINT actually reads
3. WORKER READ     GET <WORKER_BASE>/api/names, AFTER paint    → refreshes the cache; re-renders only if it differs
```

- **First paint never waits on the network.** Layer 2 falls back to layer 1 when absent or when its `estateId` does
  not match. Nothing blanks, nothing flashes on a normal load.
- **The rename flash is real but is aimed at the right person.** On a *second* device, the first load after a remote
  rename shows the old word, then swaps. That is one flash, once, for a rare event, at a family app's stakes —
  acceptable. On the device that *did* the naming, there is no flash at all: the onboarding step writes layer 2
  locally and re-renders before it POSTs, so she sees her own word appear as confirmation of her own act.
- **A failed read must be a no-op, never a revert.** The failure path is *keep what is on screen* — not "fall back to
  the built default," which would look like the app forgetting her word.
- **Her cached copy of `viewer.html`.** Pages + a phone cache means she can be running a build days old. Because the
  runtime row overrides, a rename reaches a stale build correctly — that is the split's real payoff and it is worth
  stating in the plan as the *reason* for the runtime layer, rather than "no rebuild and no deploy," which is a
  developer benefit.

### Two hard prerequisites the plan does not name

- `tateTracker.names.v1` must be added to `STORAGE_KEYS` in the template or `check-storage-keys.py` goes red — and
  more seriously, an unrostered key is a key the origin move (C4 2d, done **in person, on her phone**) leaves behind.
- `WORKER_BASE` is a **hard-coded Fernwood literal in the engine template**. See F2 — a runtime read must not ship
  before that is fixed or guarded.

---

## 3 · Where the row lives, and who may write it

### The key

`keyFor(env, "names")` → `<estate>:names` in `OBSERVATIONS`. Correct against `worker.js` as it stands:

- It is **not** date-keyed, so it uses `keyFor`, not `dateKey`/`blobKey`, and there is **no legacy predecessor** —
  no `LEGACY_BEFORE` dual-read is needed. Say so in the plan, because every other new key in this Worker has had to
  reason about the legacy window and a reader will assume this one does too.
- `estateId(env)` throws when `ESTATE_ID` is unbound, so the key cannot silently degrade to an unprefixed one.

### The read route, and the honest gate

Under C6 6a the read gate is `authOk(master) || (grant && hostAgrees)`. That means a **paired** device can read
`/api/names`; an unpaired one cannot. There is a real fork here and the plan should decide it rather than inherit it:

| option | cost |
|---|---|
| **credential-free `GET /api/names`** (the `/api/door` POST precedent) | anyone who knows the Worker URL learns the estate's chosen word. That word may be personal (*"Nana's book"*). A new ungated surface on a family app, added for a display string. |
| **gated `GET /api/names`** *(recommended)* | a rename reaches only paired devices — today, exactly Mom's phone and Paul's. Unpaired devices render the built default, which is correct and honest. |

Gated is right. The built default already covers the unpaired case *by design*, so gating costs nothing the layered
ordering doesn't already handle.

### The write route, and the authority mapping

`PUT /api/names` behind `grantFor` + `hostAgrees`. The mapping to C6/§3e that matters:

- ⛔ **Do not gate the write on `relationship`.** `VOCABULARY.md` §3e's invariant is explicit — *"anything that reads
  `relationship` to decide reachability is the defect this line names."* `relationship` is for the consent gate and
  the activation rule.
- ✅ **Add a third boolean beside `entry` and `vault` on the grant row** — `naming: on|off`. That reuses the shape
  `grant-mint.py` already writes and `grantFor` already returns, adds no new axis, and is greppable.
- ✅ **`by` comes from the grant, never from the body.** This is exactly `declarePerson`/`attributeTo`'s existing
  rule (a record arriving with a non-null `personId` throws; the grant is the only writer). The names row should
  follow it: the Worker stamps `by: "person:" + grant.personId`, `at` server-side, `how` from an enum
  (`onboarding | settings | instance | placeholder | skipped`). A client-supplied `by` is refused, not trusted.
- **Keep one level of history, no more.** `"everything is changeable"` plus Paul's journey-aware caveat argue for
  being able to answer *"what did we call it before, and when did that change?"* — one `prev: {name, short, by, at}`
  per row does that in bounded space. An unbounded log is over-built here.
- **`skipped` is a written value, not an absence.** The plan already says this; make sure the *row* carries it
  (`how: "skipped"`), because an absent row and a declined name print the same otherwise — the same defect
  `feedback-log.json` exists to prevent for notes.

### The QA fixture — and the gap in `_qaFixture`

Two different artifacts, two different rules, and **`check-qa-fixtures.py` can only see one of them**:

- **In `instance/fernwood.json` on staging** — a test word (`names.record = "the Housebook"`) used to exercise the
  build path **must** carry `_qaFixture`, because staging is main-in-waiting and the migration is a fast-forward. This
  is exactly what the check greps for and it will work.
- **In QA KV (`qa-OBSERVATIONS`)** — a fixture `<estate>:names` row **carries no marker and cannot**: the check reads
  `instance/*.json` at a git ref. A KV row is invisible to it. The row *cannot* reach prod (separate namespace), so
  the risk is not a leak — it is a later QA run reading a stale test word and nobody being able to grep for why.
  **Remedy: one line in the plan's migration checklist — "delete the QA `<estate>:names` fixture row" — since no
  check will ever say it.** State the boundary; an unstated one reads as coverage.

---

## 4 · The lint — `tools/check-concept-words.py`

### The move that removes most of the problem: lint the TEMPLATE, not the viewer

`engine/viewer.template.html` already has every re-inlined `*_DATA` const and `RELEASE_NOTES_DATA` replaced by
`{{DATA:…}}` / `{{RELEASE_NOTES}}` placeholders. So the whole class *"do not false-positive on canon data"*
**disappears by construction** if the lint targets the template. The plan does not say which file it reads; it
should, and it should say the template, and it should say *why* — that is a design win worth writing down.

### Detection, in order

1. **Targets**: `engine/viewer.template.html` + `worker/worker.js`. (Not `viewer.html` — see above.)
2. **Strip comments LINE-BASED.** Do not write a new stripper: the C5 5c harness already learned this the expensive
   way — *"comment stripping made LINE-BASED after the regex form swallowed 36% of the file and hid three real
   hits."* Read `check-condo-falsifier.py`'s stripper rather than restating it, the same discipline
   `build-viewer.py` follows for `check-data-inline.SOURCES` (*"the roster is read, not restated"*).
3. **Needle set** = registry defaults from `engine/concepts.json` + every `identity.names` value across the instance
   files, **filtered to `proper: true`**. Common-noun names are out of scope by construction (see §1).
4. **Identifier boundary — this is what kills every named false positive in one rule.** Reject a hit whose
   immediately adjacent characters match `[A-Za-z0-9_-]`. Measured against today's file, that single predicate
   clears:
   - `.ic-card--almanac` (9 CSS sites) — also already excluded by case-sensitivity
   - `buildAlmanacHistoryLink` / `wireAlmanacHistoryLink` (5 sites) — left boundary is `d`/`e`
   - `almanac_history_opened` (metric id), `almanac-card` / `almanac-history` (metric dimension values),
     `card-fieldnotes` (DOM id)
   - `tateTracker.*` — no concept word appears in one today, and the boundary rule protects it if one ever does.
     Storage keys are a **contract, never renamed** (`STORAGE_KEYS`' own comment: *"renaming them is out of scope by
     ruling"*), so they must be structurally excluded, not exempted row-by-row.
5. **Register + ratchet, `place-claims.py` shape.** `engine/concept-words.json`, one row per hit keyed by a stable
   sha1 of its line; `class ∈ unclassified | exempt-identifier | exempt-decision-prose | must-template`;
   `baseline.hardcoded` = count of `must-template` rows still present. `--check` is red when the baseline **grows**
   or when any row is `unclassified`. It flags; it never edits.

### ⚠️ The plan's *"Red on a hit"* is the wrong day-one behaviour

There are ~16 rendered hits today. A lint that goes red on all 16 the moment it is written is red before anyone can
act, and this repo's own recorded doctrine is that *a control whose alarm never clears is a control nobody reads*.
The ratchet is what makes it a ratchet: **it starts at today's truth and can only fall.** `place-claims.py` does
exactly this (`baseline.renderingAtCondo` set on first run) and says why in its own docstring. Copy that, including
the honesty about it: *"a truthful red on the moves, not on the tool."*

### Where it runs

CI (`build-viewer.yml`) unconditionally. For the session-start block: that list is already ~20 commands, and adding a
21st has a real attention cost. Put it **next to `place-claims.py`** — same shape, same reader, same disposition
move — and only after the register is fully classified, so its first appearance in the block is a line that can
actually be cleared.

---

## 5 · Migration sequencing — green at every step

### The invariant that decides the sequence

`build-viewer.py --check` compares `template + instance → viewer.html`, and `build-viewer.yml` runs it on **every
push to `main`/`staging`**. Therefore:

> **Any commit that touches `engine/viewer.template.html` or `instance/*.json` must rebuild `viewer.html` in the
> same commit.** There is no "green between commits" unless each commit is internally consistent.

And the second, sharper one: **`extract()` and `build()` are inverses and must move together in one commit**, or
`--selftest`'s round-trip assertion fails. `extract()` currently hand-writes one regex per identity site, three of
them with `count=1`.

### Proposed commits

| # | class | contents | control that must be green |
|---|---|---|---|
| **1** | TOOLING | `tools/check-concept-words.py` in **report mode only** + empty `engine/concept-words.json` register. **Also add `engine/concept-words.json` to `qa-divergence.py`'s `NOT_SURFACE`** — a register under `engine/` read by a tool, never by the build, exactly the precedent already set for `engine/place-claims.json`. (`engine/concepts.json` is build input and stays SURFACE, correctly.) | nothing changes |
| **2** | SURFACE, **bytes unchanged** | Add `engine/concepts.json` + `identity.names` to `instance/fernwood.json` carrying **today's exact values**; `build-viewer.py`'s IDENTITY lambdas read `names.*` with a fallback to `journalTile`/`stationName`. Both paths present, same output. | `--check` green · `viewer.html` untouched |
| **3** | SURFACE, **bytes unchanged** | Retire `journalTile`/`journalShort`/`stationName` from the instance file; drop the fallback; a missing `names.record` **FAILS LOUD** (the `display.defaultTextSize` precedent — a naming decision is a decision, not a fallback). ⚠️ **`build-digest.py::_identity_for` reads the same keys and must move in this same commit** — split them and `check-digest-fresh.py` goes red in the session-start block. | `--check` · `--selftest` (add the mutation) · `check-digest-fresh.py` |
| **4** | SURFACE | Introduce **one** `const NAMES = {{NAME:all}}` in the template + its single `extract()` regex; `JOURNAL_NAME` / `STATION_NAME` / `ESTATE_NAME` become derived aliases (`const JOURNAL_NAME = NAMES.record.name;`). No call site changes. `viewer.html` gains const lines; rebuild in-commit. | `--check` · `--selftest` round-trip · C5 5c 8-region hash **identical** (no rendered change) |
| **5** | SURFACE | Convert the ~16 rendered `Almanac` string sites to `NAMES.record` **reads** (see F1 — code, not placeholders). Rendered output at Fernwood is byte-identical because the value is the same string. **This is the commit the C5 5c control earns its keep on.** | `--check` · **C5 5c 8 regions hash-identical** · `herConditions()` clean at 414 × A+ |
| **6** | WORKER | `LOOKUP_STRINGS_TEMPLATE` `{journal}` → `{record}`; `JOURNAL_WORD` → a resolver over `core.identity.<names-key>` honouring `article`, with the old derivation retained while pre-cutover digests exist. Deploy + `guru-replay.mjs` fixtures. | `/health` · `check-digest-fresh.py` · replay fixtures |
| **7** | SURFACE | Metrics rename + its succession row (see §6). | `check-telemetry.py` reads the retired id as *retired*, not *never-fired* |
| **8** | TOOLING | Flip `check-concept-words.py` to `--check`; set the ratchet baseline; retire the `journalTile` reader everywhere. | lint green at baseline |
| **9** | SURFACE | The runtime layer: `STORAGE_KEYS += tateTracker.names.v1`, the post-paint read, `/api/names` GET+PUT. ⚠️ **Gated on F2** (`WORKER_BASE`). | `check-storage-keys.py` · the offline falsifier (see F9) |

### `qa-divergence.py --check`

Commits 2–5, 7 and 9 all touch `engine/` or `instance/` → **SURFACE**, so each needs a `- stage-note:` line in this
plan file. Write the note as **the first 40 characters of the commit subject**, not the sha — the tool's own comment
records that a sha moved under rebase on 2026-09-04 (`5d7760f` → `e1e608a`) and the subject did not. Also: the tool
refuses outright when `origin/main..origin/staging` cannot fast-forward, so back-merge before starting a nine-commit
run, not after.

---

## 6 · Metrics rename — `almanac_history_opened` → `record_history_opened`

### Measured: it has zero consumers

I grepped `tools/`, `worker/` and `.github/`. **No file reads `almanac_history_opened`.** Specifically:

- `read-mom-engagement.py`'s `JOURNAL_EVENTS` roster is `field_note_saved · entry_revisited · entry_starred ·
  conversation_started · conversation_turn · input_focused · input_abandoned` — the event is **not in it**.
- Its `ALMANAC_CARD_IDS` and `analyze-fernwood.py`'s copy of the same tuple read **`card_expanded` card ids**
  (`card-fieldnotes` et al.), not this event.
- `read-mom-funnel.py`'s `ASKS` funnel rows do not include it.

So the plan's framing — *"a rename of the metric is a migration"* — overstates the code-side cost. **No reader
breaks.**

### But the real cost is elsewhere, and it is the one the plan should name

A renamed event is a **new event with no history**. `check-telemetry.py` exists precisely because *"an event in the
source is not an event in the record"*, and both mom-readers are built around the rule that **an event first fired
inside the window publishes `?`, never `0`.** So the day after the rename, every zero `record_history_opened`
produces is uninterpretable until it fires once — and the 60 days of `almanac_history_opened` history in KV becomes
findable only by someone who knows the old name.

### Recommendation: **cut over, do not alias** — plus one thing the plan doesn't say

- **No alias.** Dual-emission doubles any later sum over both ids, and at n≈1 device the analytic value of unbroken
  continuity is near zero. Alias-for-a-lap is enterprise reflex; at this scale it buys a footgun.
- **Record the succession where the readers look.** Add a `RENAMES = {"almanac_history_opened":
  "record_history_opened"}` row (natural home: `check-telemetry.py`, which is the tool that would otherwise report
  the old id as *never fired* forever, or lose it silently). Then a retired id prints as *retired 2026-09-XX,
  succeeded by …* rather than as a permanently amber row or a hole in the record.
- **Leave the dimension values alone.** `source: "almanac-card" | "almanac-history"` and the DOM id
  `card-fieldnotes` are **identifiers stored inside existing records**, and both mom-readers already carry a
  standing note that *"the Almanac's DOM id never followed its rename."* Renaming them forks stored data for no
  display benefit.
- **The principle worth writing down, because the plan straddles it:** *an identifier that stored records are keyed
  by is a contract; an identifier only the source refers to is free.* `almanac_history_opened` **is** keyed data —
  so renaming it is a deliberate fork, taken because the id says the wrong referent, and it should land in the
  **same commit** as the display-word cutover so one date explains both.

---

## 7 · Findings

```json
{
  "review_id": "review-2026-09-04-vocabulary-nicknames",
  "project": "fernwood",
  "subject": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md — concept registry, per-estate identity.names, one resolver, a lint, a metrics rename",
  "review_date": "2026-09-04",
  "reviewer_mode": "review + path-evaluation",
  "user_context": {
    "primary_user": "Mom, on a 414x848 phone served A+ text, at a property with no cell reception and heavy canopy; Paul as administrator; a second estate (the condo paper model) as the portability test",
    "core_jobs_to_be_done": [
      "Read the record and have it call things by the words she uses",
      "Write a field note and have the app say where it went, in her word",
      "Ask the Guru something it does not hold and be told so honestly, in her word",
      "Name the record at first run without feeling she can get it wrong"
    ],
    "context_of_use": "Offline-prone, cached copy, one-handed, tone-sensitive; trust is the load-bearing emotion",
    "sources": ["CLAUDE.md (Mama's Perspective doctrine, THE SITE'S PHYSICAL PREMISE, her conditions)", "VOCABULARY.md sections 3b/3e/4", "questions.json (q-almanac-vs-journal-name, live)"],
    "assumptions_made": [
      "The onboarding naming SURFACE is out of this plan's scope by its own seat table; only the contract beneath it is reviewed here",
      "Not read by instruction: .private/** and the Mom feedback files"
    ],
    "user_context_confidence": "high"
  },
  "code_context": {
    "purpose": "Give every estate its own display words for a fixed set of internal concepts, with provenance, resolved once across the viewer build, the Worker and the digest",
    "stack": "No-build single-file HTML/JS viewer BUILT from engine/viewer.template.html + instance/<estate>.json by tools/build-viewer.py; Cloudflare Worker + KV; Python tooling; GitHub Pages",
    "conventions_observed": [
      "Rosters are READ, never restated (build-viewer.py reads check-data-inline.SOURCES)",
      "A decision FAILS LOUD rather than defaulting (display.defaultTextSize)",
      "Registers ratchet from today's truth and can only fall (place-claims.py)",
      "A control that is red on day one is a control nobody reads (check-vocabulary.py N8 guard)",
      "Every KV key carries the estate; a row for another estate is no row (keyFor / grantFor)",
      "Storage keys are a contract, never renamed"
    ],
    "deployment_context": "mom-ready",
    "robustness_level": "shippable",
    "assumptions_made": [
      "The condo instance lives in the private sibling and was not read",
      "engine/concepts.json does not exist yet (verified absent)"
    ],
    "code_context_confidence": "high"
  },
  "tooling_signals": {
    "type_check": "n/a",
    "linter": "n/a",
    "tests": "not-run",
    "notes": "Read-only review. No selftest, build or deploy was run; nothing was written outside .engineering/."
  },
  "principles_applied": [
    "Read the roster, never restate it (build-viewer.py, ENGINE-MANIFEST.md)",
    "A control red on day one is a control nobody reads (check-vocabulary.py N8 guard; place-claims.py ratchet)",
    "An unstated boundary reads as full coverage (check-telemetry.py; check-public-build.py exit 3)",
    "One name, one meaning, one repo (VOCABULARY.md section 5)",
    "Capture must not lie; the site has no network away from the house (CLAUDE.md)",
    "AHA — do not build the abstraction the code has not asked for"
  ],
  "findings": [
    {
      "id": "F1",
      "intent": "issue",
      "area": "framework-idiom",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1c; tools/build-viewer.py (extract/IDENTITY_MARKUP); engine/viewer.template.html",
      "observation": "The plan turns the hard-coded record-word strings into `{{NAME:record.short}}` BUILD-TIME placeholders. build-viewer.py's `extract()` is the hand-written inverse of `build()`: one regex per identity site, three of them using re.sub with count=1, and `--selftest` asserts extract-then-build round-trips the live viewer byte for byte. Sixteen new placeholder sites means sixteen new hand-written regexes that must each match exactly one place in a 1 MB template.",
      "risk_or_impact": "extract() becomes the maintenance surface of this feature. A regex that matches zero sites throws on --extract; one that matches the wrong site silently rewrites a different string; count=1 quietly converts only the first of several. --extract is the documented escape hatch when a writer edits viewer.html directly, so a brittle extract() breaks the recovery path, not just the build.",
      "principle_invoked": "Deep module / narrow interface (Ousterhout) — one build-time seam, not sixteen",
      "the_why": "The template already carries JS consts filled at build (ESTATE_NAME, JOURNAL_NAME, STATION_NAME). A JS string that is CONSUMED by code does not need to be filled at build at all — it can read a const at runtime. Filling at build is only necessary for MARKUP the build must produce (the title, the h1, tile labels). Runtime reads cost nothing at this scale and are also what the runtime KV override in section 1c needs anyway: a string baked at build cannot be overridden by a KV row, so build-time placeholders and the runtime layer actively fight each other.",
      "recommendation": "Emit exactly ONE build-time site: `const NAMES = {{NAME:all}};` (the whole resolved object literal), with one extract() regex in the const_re shape already used for ESTATE_MODULES. Convert the ~16 rendered strings to `NAMES.record` READS in code. Keep build-time IDENTITY placeholders only for the markup sites that genuinely have no JS (title, h1, tile labels, aria). This also makes the runtime override a one-line assignment rather than an impossibility.",
      "effort": "low"
    },
    {
      "id": "F2",
      "intent": "issue",
      "area": "safety-to-deploy",
      "severity": "critical",
      "location": "engine/viewer.template.html (WORKER_BASE, the environment block)",
      "observation": "`WORKER_BASE` is a hard-coded ternary between two literal Fernwood Worker URLs, in the ENGINE half of the template, derived only from whether the hostname ends in .pages.dev. The plan's runtime layer reads `<estate>:names` from the Worker at boot.",
      "risk_or_impact": "The condo's built viewer would boot-read FERNWOOD's KV names row and render Fernwood's word. This is the exact shape the C6 privacy seat's finding 1 names — two estates in one request — arriving through a new door that no existing check watches. It also means the runtime layer cannot actually work for any estate but Fernwood, so the feature's headline benefit is Fernwood-only while looking general.",
      "principle_invoked": "Every KV key carries the estate; a row for another estate is no row (worker.js grantFor / keyFor)",
      "the_why": "grantFor already encodes the correct posture: it refuses a row whose estateId does not equal this deploy's binding, because a credential that resolves to the wrong estate is worse than no credential. A boot read that trusts a hard-coded URL has no such check — it will succeed, return a well-formed row, and be wrong. A silent wrong answer is the failure class this repo pays for most.",
      "recommendation": "Two moves, both cheap. (1) Make the Worker base an instance value (`identity.worker` or similar) filled at build, the same way `identity.station` is — WORKER_BASE is a config value typed into engine code, which is exactly ENGINE-MANIFEST's P4 class. (2) Independently, have the read carry and verify the estate: the response includes `estateId`, and the viewer DISCARDS a row whose estateId does not match the built `instance.estate`. Belt and braces, mirroring grantFor. Gate commit 9 of the sequence on this.",
      "effort": "medium"
    },
    {
      "id": "F3",
      "intent": "issue",
      "area": "code-quality",
      "severity": "important",
      "location": "tools/build-digest.py (core.names, the digest's entity names index); worker/worker.js (CORE_SUBSTRATE_NOTE); plan section 1c",
      "observation": "`digest.core.names` ALREADY means the entity names index — id + name + markers for every plant, weed, zone, vehicle and bird the place keeps — and the Guru's own system prompt describes itself as holding 'a names index'. The plan proposes carrying the estate's display words as `core.identity.names`.",
      "risk_or_impact": "Two meanings of `names` inside one JSON object that an LLM reads as its system context. This is VOCABULARY.md section 5's `group` defect (one name, two meanings, one repo) minted deliberately, in the one place where the reader cannot be asked to disambiguate. build-digest.py's own selftest asserts against `core['names']` by that key, so a future reader has two right answers to 'where are the names?'.",
      "principle_invoked": "One name, one meaning, one repo (VOCABULARY.md section 5); check-vocabulary.py's V3 double-booking check",
      "the_why": "The repo already has a checker whose entire V3 case is `group` being double-booked, and a standing note that it 'awaits a migration decision'. Minting a second instance of the same defect, on the day a vocabulary registry is being introduced, is the one thing this plan should not do. The cost of avoiding it now is one word; the cost later is another migration decision that waits.",
      "recommendation": "Do not use `names` for the display words. `identity.words` reads correctly in both places (`core.identity.words.record.short`) and collides with nothing measured. Keep `core.names` as the entity index it already is. Apply the same word in `instance/<estate>.json` so the instance file and the digest agree.",
      "effort": "low"
    },
    {
      "id": "F4",
      "intent": "issue",
      "area": "code-quality",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 0 and 1c ('12 hard-coded Almanac strings')",
      "observation": "Measured on engine/viewer.template.html, 2026-09-04: 58 total occurrences of 'Almanac'. Outside line-initial comments: 36. Of those — 16 are USER-VISIBLE rendered strings (the Save & consult label, 2 storage/sync failure messages, 12 Guru suggest/status/actionbox strings, the thinking line, one patchTurn error), 2 are console.warn (developer-facing), 5 are function-name identifiers, 1 is a metric id, 2 are metric dimension values, and 9 CSS sites carry `.ic-card--almanac`. Separately, questions.json (fetched at runtime, Mom-facing) carries 5, one of which is the LIVE card `q-almanac-vs-journal-name` asking her whether to rename it.",
      "risk_or_impact": "A plan whose scope number is 12 sizes the work at roughly two-thirds of it. More importantly the questions.json class is not mentioned at all: that is CANON prose naming the record, which is place-claims.py's exact instance-prose-vs-engine-prose shape and belongs there, not here — and one of those rows is a card currently in Mom's queue on this very subject.",
      "principle_invoked": "Verify a row against the app before acting on it (CLAUDE.md standing rule)",
      "the_why": "This repo's most repeated recorded failure is a wrong SSOT row propagating — the CLAUDE.md architecture section said '~4,600 lines' of a 17,878-line file for months. A scope count in a plan is exactly that kind of row: nothing re-derives it, and the sequencing, the ratchet baseline and the lint's day-one register all key off it.",
      "recommendation": "Restate section 0 with the measured breakdown by CLASS, not one number: 16 rendered · 2 console · 5 identifiers · 1 metric id · 2 dimension values · 9 CSS · 5 in canon (questions.json) · 23 in RELEASE_NOTES.md. Route the canon-prose class to place-claims.py explicitly and say so, so the next reader does not re-discover it. Note q-almanac-vs-journal-name as live.",
      "effort": "low"
    },
    {
      "id": "F5",
      "intent": "suggestion",
      "area": "code-quality",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1b (the names schema); worker/worker.js (JOURNAL_WORD, LOOKUP_STRINGS_TEMPLATE); engine/viewer.template.html (the two 'The Almanac …' failure strings and the two '\"the \" + JOURNAL_NAME' sites)",
      "observation": "`{name, short}` does not carry the article, and the article is currently expressed three different ways: the Worker BAKES it into JOURNAL_WORD ('the Almanac'), the viewer PREPENDS it at two call sites with a hand-written 'the journal' fallback, and two failure strings need it SENTENCE-CASED. JOURNAL_WORD's own comment already admits the derivation breaks for 'a name that takes no article'.",
      "risk_or_impact": "The plan's falsifier — build the condo as 'the Housebook' and assert 'not in the Housebook' — passes only by luck of that word taking 'the'. A proper noun that takes no article ('Housebook', 'Midtown Notes') renders as 'not in the Housebook' or 'The Housebook isn't connected' depending on which of the three conventions the site used. Mom's surfaces are where a broken sentence costs trust.",
      "principle_invoked": "Falsehoods programmers believe about names (patio11) — an article and a capital are properties of a name, not of a template",
      "the_why": "Storing the phrase with its article baked in means every sentence-initial site needs a second stored form; storing it bare means every mid-sentence site re-derives the article. Storing `short` BARE plus a separate `article` lets one resolver derive both — mid-sentence is `article ? article + ' ' + short : short`, sentence-initial is that with its first character uppercased, and that single rule is correct for 'the Almanac' / 'the journal' / 'Housebook' alike.",
      "recommendation": "`{name, short, article, proper, by, at, how}`. `short` bare, `article` = 'the' | null, `proper` = does the capital survive mid-sentence. Derive sentence-case and possessive in the resolver; store neither. Store NO plural — zero rendered plurals exist, and a plural field now is the wrong abstraction (AHA). `proper` earns its row as the LINT's filter, not as a rendering field — see F6.",
      "effort": "low"
    },
    {
      "id": "F6",
      "intent": "issue",
      "area": "testing",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1e ('Red on a hit'); tools/place-claims.py (the ratchet); tools/check-vocabulary.py (the N8 guard)",
      "observation": "The plan specifies the lint as red on any hit. There are ~16 rendered hits in the engine template today, and the needle list as written includes common nouns ('Journal', 'field notes') that cannot be distinguished from ordinary prose.",
      "risk_or_impact": "The check is red the moment it is written, stays red through a nine-commit migration, and is red on words like 'journal' forever. That is the costly-control signature this repo has already ruled against twice in writing — check-vocabulary.py's N8 guard exists solely to avoid it ('a checker that fired on every legacy occurrence would be red forever on day one'), and place-claims.py's ratchet exists to solve the same problem.",
      "principle_invoked": "A control whose alarm never clears is a control nobody reads (paul-ruled, cited in check-vocabulary.py)",
      "the_why": "A ratchet converts an unactionable red into a measurable direction: it starts at today's truth, and only a NEW hardcoded word turns it red. That is what makes the alarm mean something on the day it fires. place-claims.py states this in its own docstring — 'a truthful red on the moves, not on the tool' — and the same sentence should appear here.",
      "recommendation": "Register + ratchet, place-claims.py shape: engine/concept-words.json, one row per hit keyed by a stable sha1, class in {unclassified, exempt-identifier, exempt-decision-prose, must-template}; baseline.hardcoded set on first run; --check red only when the baseline grows or a row is unclassified. Filter the needle set to proper:true names. Target engine/viewer.template.html (not viewer.html) so the inlined *_DATA consts are excluded BY CONSTRUCTION rather than by exclusion rules. Reject any hit whose adjacent characters match [A-Za-z0-9_-] — that one predicate clears .ic-card--almanac, buildAlmanacHistoryLink, almanac_history_opened, almanac-card, almanac-history and every tateTracker.* key at once. Reuse check-condo-falsifier.py's LINE-BASED comment stripper; do not write a new one (the regex form swallowed 36% of the file and hid three real hits).",
      "effort": "medium"
    },
    {
      "id": "F7",
      "intent": "issue",
      "area": "security",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1c (the runtime row 'written ONLY ... through a grant'); VOCABULARY.md section 3e; worker/worker.js (grantFor, declarePerson, attributeTo)",
      "observation": "The plan says the KV names row is written 'through a grant (C6 authority rules)' but does not say WHICH property of the grant authorises it. The nearest-looking axis is `relationship` (owner/contributor/member).",
      "risk_or_impact": "Gating on `relationship` would breach VOCABULARY.md section 3e's ratified invariant verbatim: 'anything that reads relationship to decide reachability is the defect this line names.' It is easy to reach for, because a naming right feels like an ownership right.",
      "principle_invoked": "Membership confers nothing; relationship is not an access axis (paul-stated 2026-09-03)",
      "the_why": "relationship exists for the consent gate and the activation rule. Reachability comes from the grant ROW's own capability flags — the row already carries `entry` and `vault` as independent booleans precisely so a new capability is a new flag, not a new reading of an existing field. Adding a third flag costs one line in grant-mint.py and keeps the invariant checkable by grep.",
      "recommendation": "Add `naming: on|off` beside `entry` and `vault` on the grant row; gate PUT /api/names on `grant && hostAgrees && grant.naming`. Stamp `by` from `grant.personId` server-side and REFUSE a client-supplied `by` — the same guard shape declarePerson already enforces (a record arriving with a non-null personId throws; attributeTo is the only non-null writer). `how` from a closed enum: onboarding | settings | instance | placeholder | skipped. Recommend a GATED read too: an ungated GET /api/names would publish an estate's chosen word to anyone holding the Worker URL, and the built default already covers the unpaired case.",
      "effort": "low"
    },
    {
      "id": "F8",
      "intent": "issue",
      "area": "safety-to-deploy",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1c (runtime override); engine/viewer.template.html (STORAGE_KEYS); tools/check-storage-keys.py; .plans/2026-09-03-c4-environments-PLAN.md 2d (the origin move)",
      "observation": "The runtime layer needs a local cache so first paint does not wait on the network. That is a new localStorage key, and the plan does not mention one.",
      "risk_or_impact": "check-storage-keys.py fails on any unrostered `tateTracker.` literal, so this is caught — but the reason the roster exists is worse than a red check: storage is per ORIGIN, and the custom-domain move (C4 2d) happens once, in person, on Mom's phone. A key the migration does not know about is a key she loses. Additionally, the family-door design means one origin may serve several estates, so a cache row that does not carry its estateId will render the wrong estate's word after a switch.",
      "principle_invoked": "A key the origin-move migration does not know about is a key she loses (C4 2b)",
      "the_why": "Without a cache, first paint either waits on a network the site's physical premise says may not exist, or flashes the built default on every load. With a cache, the only flash is the first load after a remote rename, on a device that did not do the renaming — one flash, once, for a rare event. That is the right trade at family scale, and it is why the key is not optional.",
      "recommendation": "Add `names: 'tateTracker.names.v1'` to STORAGE_KEYS in the same commit as the runtime read, and store `{estateId, names, fetchedAt}` — discard the row on an estateId mismatch (same posture as grantFor). Ordering: built default → cache at first paint → post-paint Worker read refreshes the cache and re-renders only on a difference. A failed or offline read is a NO-OP, never a revert to the built default: reverting would look like the app forgetting her word.",
      "effort": "low"
    },
    {
      "id": "F9",
      "intent": "issue",
      "area": "testing",
      "severity": "important",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 2 (Falsifier)",
      "observation": "The falsifier tests the condo build, the Guru's lookup string, the eight-region Fernwood hash, the lint, and a KV rename reaching the page without a rebuild. It does not test the OFFLINE path.",
      "risk_or_impact": "The one new failure mode this plan introduces to Mom's surface is 'the page now depends on a network read to know what to call things.' Her property has no cell reception and heavy canopy, and CLAUDE.md states that as a permanent founding premise, not a caveat. The falsifier as written would pass on a machine with perfect connectivity while the actual regression ships.",
      "principle_invoked": "Never propose a design whose mitigation is 'improve the signal' (paul-stated 2026-08-31)",
      "the_why": "A falsifier's job is to name the observation that would prove the design wrong. The observation that matters here is not 'the rename did not propagate' — it is 'the app got worse for the person it is built for, in the condition she is actually in.' Testing only the happy network path measures the feature, not the risk.",
      "recommendation": "Add two rows. (1) OFFLINE: load the built viewer at 414 x A+ with the Worker unreachable (block the origin in Playwright); assert the built word renders, no blank region, no console error, herConditions() clean. (2) STALE BUILD: load a viewer built BEFORE a rename with the cache primed to the new word; assert first paint shows the new word and nothing flashes. Both are Playwright flows, which is the standing testing posture here.",
      "effort": "low"
    },
    {
      "id": "F10",
      "intent": "suggestion",
      "area": "code-quality",
      "severity": "nice-to-have",
      "location": "tools/qa-divergence.py (SURFACE regex and NOT_SURFACE); the proposed engine/concept-words.json register",
      "observation": "qa-divergence.py classes anything under `engine/` as SURFACE, with a single exception already carved out: NOT_SURFACE = {'engine/place-claims.json'} — 'a REGISTER under engine/, read by a tool, never by the build.' The proposed concept-words register is precisely that same thing.",
      "risk_or_impact": "Low, but it is the difference between a truthful ledger and a noisy one. Every register update would show as a SURFACE commit needing a stage-note, when nothing Mom sees changed — and a ledger that cries surface on non-surface commits is a ledger people stop reading.",
      "principle_invoked": "A ledger that over-reports is a ledger nobody reads",
      "the_why": "engine/concepts.json IS build input (build-viewer.py reads it) and should stay SURFACE — correctly. engine/concept-words.json is a register a tool reads and the build never touches. The distinction already exists in the code with its reason written beside it; extending it is a one-line change that keeps the reason true.",
      "recommendation": "Add 'engine/concept-words.json' to NOT_SURFACE in the same commit that creates the register, with the same one-line reason. Leave engine/concepts.json as SURFACE.",
      "effort": "low"
    },
    {
      "id": "F11",
      "intent": "question",
      "area": "other",
      "severity": "nice-to-have",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md section 1c (the Guru's system prompt says the estate's words) and section 1d (her answer lands with by: person:<id>)",
      "observation": "Once a person names a concept, the resulting string is content SHE authored, and section 1c routes it into the Guru's system prompt via the digest identity block.",
      "risk_or_impact": "Not a breach — the AI boundary's QUARANTINE clause governs model output derived from her words ABOUT HERSELF, and a word for a card is a statement about the app, not about her. But the plan ships a person-authored string into a model context without naming that it is doing so, and the boundary's rule is that an unstated boundary reads as coverage.",
      "principle_invoked": "The AI boundary (2026-07-14, amended 2026-07-26 and 2026-09-02)",
      "the_why": "The plan waives the ai-advisor seat on the grounds that 'no model on any path here.' That is true of the capture path — her answer is stored deterministically — but not of the egress: her word reaches the prompt. The waiver is probably still right; the reasoning behind it should be one sentence in the plan rather than absent, so a later reader does not have to re-derive it.",
      "recommendation": "One line in section 1c: a person's chosen display word is app vocabulary, not self-description, so it is project material under the boundary and may ride in the identity block. If Paul reads it the other way, the alternative is that the Guru is told the CONCEPT ids and the honesty strings are templated client-side — more work, and probably unnecessary.",
      "effort": "low"
    },
    {
      "id": "F12",
      "intent": "praise",
      "area": "code-quality",
      "severity": "nice-to-have",
      "location": ".plans/2026-09-04-vocabulary-nicknames-PLAN.md sections 1a and 1b",
      "observation": "Two design calls in the plan are notably right and worth keeping when the rest is revised: (1) the internal id never moves, so a rename is a data change and never a code change; (2) a person's nickname and Paul's config word are the SAME SHAPE, distinguished only by `by`/`how` — no second file, no second mechanism.",
      "risk_or_impact": "n/a",
      "principle_invoked": "One mechanism, N writers (the c6 overlay finding, re-applied)",
      "the_why": "The second one is the load-bearing call. The natural instinct is to build a separate 'user preferences' store beside the config, and that is how you end up with two resolvers that disagree — the exact failure momlib.ENTITY_SOURCES was extracted to end after 'assumed plants' shipped broken three times in one day in three different tools. Making provenance a FIELD rather than a LOCATION means there is only ever one place to look.",
      "recommendation": "Keep both. State the second one in VOCABULARY.md section 3f when it lands, because it generalises beyond names.",
      "effort": "low"
    }
  ],
  "open_questions_for_user": [
    "The engine default for `record` is `{{place}} Record` — which renders as 'Fernwood Record' / 'Midtown condo Record'. Since skipping the naming step is expected to be the common path, this default is doing more work than the plan credits it with. Is it a word you would ship as-is?",
    "`identity.words` vs `identity.names` (F3) — the word `names` is already taken by the digest's entity index. Happy to take `words`, or do you want the entity index renamed instead?",
    "The metrics rename is a deliberate fork of 60 days of history for zero code consumers (measured). Worth it because the id says the wrong referent — confirm that is the trade you want.",
    "q-almanac-vs-journal-name is LIVE in Mom's queue right now, asking her whether 'Journal' fits better than 'The Almanac'. Should this plan wait on her answer, or does the registry ship first and her answer become its first `by: person:<id>` row? (The second reads better to me — it makes her answer a demonstration of the mechanism rather than a blocker on it.)"
  ],
  "follow_up_research_suggested": [
    "The questions.json 'Almanac' class (5 rows, canon prose naming the record) is place-claims.py's shape, not this plan's — route it there before the condo build renders Fernwood's genre promise in Mom's card copy.",
    "WORKER_BASE as a hard-coded instance value in engine code is ENGINE-MANIFEST's P4 class ('a config value copied into engine code — counted, and its detector is C5 step 4's lint, not built yet'). This is a live instance of the class that lint would catch."
  ],
  "principles_to_propose": [
    {
      "principle": "An identifier that stored records are KEYED by is a contract; an identifier only the source refers to is free.",
      "scope": "fernwood",
      "rationale": "The plan renames a metric id (keyed in KV metrics batches) while the standing practice leaves DOM ids, storage keys and repo paths alone. Both are right, and the line between them is currently implicit — which is why the plan straddles it without noticing. Naming the rule makes the next rename decidable in one read."
    },
    {
      "principle": "A ratcheting register starts at today's truth and can only fall; a lint that is red on the day it ships is a lint nobody reads.",
      "scope": "cross-project",
      "rationale": "Third independent instance in this repo (place-claims.py's baseline, check-vocabulary.py's N8 guard, and now the concept-words lint). It generalises well past Fernwood: it is the difference between a check that measures direction and one that measures backlog."
    },
    {
      "principle": "Fill at build only what MARKUP requires; let code read a const. One build-time seam beats N placeholders.",
      "scope": "fernwood",
      "rationale": "build-viewer.py's extract() is a hand-written inverse of build(), so every placeholder class is a permanent maintenance cost on the recovery path. It is also the enabling condition for any runtime override: a string baked at build cannot be overridden by a KV row."
    }
  ]
}
```
