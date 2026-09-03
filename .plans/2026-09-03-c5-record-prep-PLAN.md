# c5-record-prep · Record prep — the data model's reversible steps
- row: BACKLOG.md § C5 · RECORD PREP — the data model's reversible steps 1–5
- objective: O3
- class: engine · must-not-diverge
- seats: engineering-partner → .engineering/2026-09-03-c5-record-prep.md
         practice-steward → .plans/2026-09-03-c5-manifest-check-PROPOSAL.md
         content-steward → waived: the product name in Mom-read prose is now upstream in the naming decision (C4 step 2a); this plan substitutes the identity block from config and never authors the string
         ai-advisor → waived: no model on the path
         ux-expert → waived: nothing she sees changes; the identity block renders identically until config differs
         user-researcher → waived: no user question in this item
- depends-on: .plans/2026-09-03-c4-environments-PLAN.md
- stage: ready

Drafted by the planning agent 2026-09-03 from the row, C4's RULED table and its three-levels ruling (decided, not
re-argued: product apex · family door per family · instance by grant; two example families for planning; the app served
from Cloudflare), both seat trails, the data-model design §2–§5/§8, `PRODUCT-ENGINE.md` § THE MODULE SET IS A DECLARATION
and § THE DISCRIMINATOR IS SITING, `VOCABULARY.md` §2–§5, `OBJECTIVES.md`. Files are cited by **name relative to the repo
root + role, never by line number** — C4 renames the root. **Reconciled while drafting:** the seat's §4 cites C4 "step
13/15", which do not exist — C4's labels are 1a–5d; the manifest is **5a**, the build step **5b**, the repo split **5d**
(P3 arms there). Measured: the private sibling the grant register is sited in **does not exist yet** — C4 step 1b creates
it, so 2c below carries that one ungated dependency; a new root JSON trips `check-domains.py`'s undeclared-file sweep, so
`estate.json` lands with its `NON_DOMAINS` row in one commit; `viewer.html` carries **22** `*_DATA` consts, `check-data-inline.py`
rosters **12**, six have no producer at all. C4's plan is still being amended (its Q1/Q3), so `check-backlog-ready.py`
will flag this file's `depends-on` whenever C4 moves — the discharge is a re-read against C4's new text, never a re-date.
**Order** (the seat's §6, with the deadline following the hazard): 1 personId on the record → 2 ids as data → 3 the module
declaration → 4 the config accessor + lint → 5 manifest + checker (with C4 5a) → 6 the KV prefix (with C4 3a `[env.qa]`)
→ 7 identity block + instance config (with C4 5b). **Steps 1–4 ship with no C4 dependency** except 2c.

## Files touched

**Step 1 — personId on the record.** `worker/worker.js` (`handleFeedback`, `handleZoneAudio`, `handleZoneFeedback`,
`persistConversation`, the observation store's lowest write helper: every record gains `personId: null`, declared, beside
`deviceId`); `tools/momlib.py` (one `person_for(record)` resolver reading `tools/people.json` and its `_meta.attributionIsValidFrom`);
`tools/test-feedback-cycle.py` (CAPTURE leg asserts the field; a new ATTRIBUTE leg). No reader changes: the four
Mom-cycle readers go through the HTTP getter and never touch a key (seat §0b).
**Step 2 — ids as data.** New root `estate.json` (`estateId`, the coordinate-not-label rule, later the module block);
`tools/check-domains.py` `NON_DOMAINS` (+1 row with a reason); `tools/people.json` (`id` beside `name`, people only);
`tools/check-vocabulary.py` (V1/V3/V5 run as controls, no change). **2c only:** `grants.json` in the private sibling
(C4 1b) + `~/.claude/hooks/guard-secret-push.py` `NEVER_PUBLIC` — the sibling is already registered there by C4 1b.
**Step 3 — the module declaration.** `tools/momlib.py` (`MODULES` membership + `enabled(estate)` / `enabled_domains(estate)`);
`estate.json` (`modules:` block); the five consumers: `tools/harvest-questions.py` (the loader), `tools/check-domains.py`
(a third row state + the inverted sweep), `tools/build-digest.py` (`main()`'s literal dict), `viewer.html`
`renderDashboardStrip()` + the static strip markup (a declared tile roster), `tools/mom-cycle-status.py` (`engagement_signals`
denominator); `tools/check-digest-fresh.py`, `tools/check-cards.py` (controls, unchanged); a `--selftest` fixture builder.
**Step 4 — config accessor + lint + the 0e roster.** `tools/momlib.py` (`config(path)`, raising); new
`tools/check-config-derivation.py` (path-keyed roster with per-row detector + allowed locations; later called as P4);
`tools/fleet_probe.py` (the threshold block derives from canon — the founding leak); `tools/check-data-inline.py`
(`SOURCES` gains a whole-document row kind: `REFERENCES_DATA`, `PROPERTY_DATA` minus the `climate.monthlyNormals` cache
subtree, with reasons; `CELESTIAL_DATA` excluded with its reason — not JSON); `references.json`/`property.json` or their
consts, whichever side Paul rules (Q4). `CLAUDE.md` session-start block (one line, or folded — Q7 of the proposal).
**Step 5 — manifest + checker (C4 5a).** New `ENGINE-MANIFEST.md` (dir→class table, exception table with reason strings,
declared divergence tiers, `mixed` rows with shrink targets), new `tools/check-engine-manifest.py` (P1·P2 fail; P3
`skipped`; P4 calls step 4's lint; P5 enumerates consts outside `SOURCES`) + `--selftest`; `CLAUDE.md` session-start block.
**Step 6 — the KV prefix (C4 3a).** `worker/worker.js` (one key builder; the 45 `OBSERVATIONS.*` sites; `LEGACY_BEFORE`;
the two `list({prefix})` calls; `zones:all` + `zones-last-seen:`), `worker/wrangler.toml` (`ESTATE_ID` var per env, non-inheritable),
`tools/qa-write-probe.py` (C4 3f — gains the plant/list/read-back legs). **Never:** the API path or query string.
**Step 7 — identity block + instance config (C4 5b).** `engine/viewer.template.html` (masthead placeholders: `<title>`,
`<h1>`, `header-subtitle`, `header-address`, the unified-input `aria-label`), `instance/fernwood.json` (identity derived by
`momlib.config`, never re-typed), `tools/build-viewer.py` (substitution at build), `worker/worker.js` (`AMBIENT_MAC_DEFAULT`
retired — the binding is required), `tools/check-config-derivation.py` roster (allowed locations gain the instance file).
**At the stamp:** `BACKLOG.md` § C5 gains `→ READY · .plans/2026-09-03-c5-record-prep-PLAN.md`; this file gains `- ready:`.

## Sequence

Each step: **who** · **reversible?** · **the deterministic check**. Existing tools first; new checks prove themselves by mutation.

**1a · `personId` on every new record** — agent · reversible (additive field) · the Worker stamps `personId: null` at
its lowest write helper for feedback, zone-audio, zone-feedback and conversations. **Null is declared, never absent**: an
absent field means *pre-step record*, a null means *written after the field existed and nobody could say* — different
observations, kept different. No handler reads a person from the request (there is no credential until C6). Check:
`python3 tools/test-feedback-cycle.py` CAPTURE leg asserts the stored record carries the key; `bash tools/deploy-worker.sh`
`/health` OK; the next real record on prod (Mom's or Paul's, read via `GET /api/feedback`) carries `personId: null`.
`--live` is **Paul's** to run — it is a prod write.
**1b · The resolver, with the boundary built in** — agent · reversible · `momlib.person_for(record)` maps `deviceId` →
`people[].id` **only for records dated on/after `_meta.attributionIsValidFrom`'s fully-valid date**; earlier → `None` with
the reason string from `_meta`; the caveat window (07-13 → 07-27) → `None` unless Paul rules otherwise (Q3 of the seat's §8).
It is the **only** writer of a non-null person anywhere. Check: a new ATTRIBUTE leg in `test-feedback-cycle.py` — a fixture
record dated 2026-07-01 on a registered device resolves to `None`; one dated 2026-08-01 resolves to the id; `git grep -l
personId -- tools worker` lists the declaring files only.
**2a · `estate.json` + its `NON_DOMAINS` row** — agent · reversible · root file: `estateId` (value: Q2), a `_meta` line
*"an id is a coordinate, not a label — renaming the place does not rename the estateId"*, nothing else yet. Positive
control first: with the file present and **no** `NON_DOMAINS` row, `python3 tools/check-domains.py` must **fail** (the
undeclared sweep); add the row with a reason; it exits 0. Then `python3 tools/check-vocabulary.py` exit 0 (V1: no
`propertyId`; V5: `location` not minted); `git grep -l estateId` = the declaring files only.
**2b · `personId` promoted in the register** — agent · reversible · `tools/people.json` `people[].id` beside `name`
(`paul`, the handle for Mom — Q3, `telemetry-test`); no real name enters a tracked file. Check: `check-vocabulary.py` exit 0;
1b's leg reads `id`, not `name`.
**2c · The grant register** — agent · reversible · **after C4 1b**: `grants.json` in the private sibling — one row
`(personId, estateId, relationship: set, capability: single)` per VOCABULARY §2; **nothing reads it yet**. Rule 2 stands:
the public repo carries no person↔place map. Check: `python3 ~/.claude/hooks/guard-secret-push.py --selftest` passes with
the sibling in `NEVER_PUBLIC`; `git -C <sibling> remote -v` prints nothing; `git grep -c grants.json` in the public repo = 0.
**3a · `MODULES` + the resolver + the `modules:` block** — agent · reversible · under unit B (Q1): `momlib.MODULES` maps
a module name → member set (domain keys, plus `turf` named as a non-domain member **with a reason** — the measurement that
decided the unit); `estate.json: modules: {garden: on, fleet: on, wildlife: on, place: on}` (Fernwood: everything on);
`enabled_domains(estate)` = a domain is on if **any** ON module claims it (`zone` is in both *garden* and *place* —
membership is not a partition). Every consumer calls the resolver; none reads `DOMAINS` for on/off. Check: with Fernwood's
block, `python3 tools/check-domains.py`, `check-cards.py`, `check-digest-fresh.py` all exit 0 **unchanged** — the ON path
is untouched by construction, and `worker/digest.json` is byte-identical before and after.
**3b · The five consumers, OFF vs ON-but-EMPTY** — agent · reversible · one behaviour each, stated so the fixture can assert it:

| consumer (role) | module **OFF** | module **ON, file empty** |
|---|---|---|
| `harvest-questions.py` (drafts cards from markers) | skip the domain — one `continue` beside the existing `cardable` one | iterate, zero candidates, **reported as a gap** |
| `check-domains.py` (conformance) | third row state **`declared off`**, neither 🔴 nor absent; the undeclared sweep **inverts**: a non-empty file at an OFF module is a **finding** (undeclared data) | check as today; an empty list stays a finding |
| `build-digest.py` (Guru's context) | **omit the key** + one `_meta` line *"this estate declares no garden"* — never `"plants": []` | include normally |
| `renderDashboardStrip()` (four tiles) | **the tile is not rendered**; the strip reflows. Tiles render from a declared roster × the module set, not from ids fixed in static HTML | the tile in its existing empty state |
| engagement signals (`offers-passed` · `sessions-quiet`) | **off-module offers leave the denominator** — a non-tap where there are no plants is not a signal about her; unreadable module set → `?`, never fires (the idiom already there) | count normally — she was genuinely offered something |

Check: a `--selftest` building **two fixtures in a temp dir** — Fernwood (all on) must be a no-op against today's outputs;
a gardenless estate (`garden: off`) must yield **zero plant/weed/turf/zone candidates**, a digest with **no** `plants`/
`weeds`/`turf`/`zones` keys and the `_meta` line, a `check-domains` run printing `declared off` for those rows and 🔴 for
a planted non-empty `plants.json`, and `offers-passed` excluding a synthetic plant-card offer. **The strip is a viewer
change:** it ships through C4's QA origin if 3 exists by then, otherwise at Paul's gate after `herConditions()`
`clean:true` at 414 × A+ — at Fernwood the rendered strip is identical (four tiles), which is the point.
**3c · The second falsifier, planned not built** — the condo (C7) proves one estate can declare *no garden*; **a
family-B estate under its own family door** (C4's planning example) proves the declaration is **per estate across a
family**, not per deployment — two estates behind one door with different module sets and no fork. Both fixtures live in
the private sibling; neither carries a third party's name. Pass = the same `engine/` renders all three module sets;
fail = an `engine/` edit is needed for the second family, and the unit was chosen wrong.
**4a · `momlib.config(path)`** — agent · reversible · reads `property.json` (later the instance file) by dotted path and
**raises** on a missing path — never a default. Check: a unit case for a missing path raising; `fleet_probe.py`'s
threshold block replaced by `config("frostDates.atPropertyElevation.firstFall_50pct")` parsed once, and `python3
tools/fleet_probe.py --selftest` still passes (its SEASON cases pin the date).
**4b · The path-keyed lint** — agent · reversible · `check-config-derivation.py`: roster rows `(canonical path, detector,
allowed locations, reason)`; three detector kinds — literal (`34.5496`, one substring for all three spellings),
**type-changed** (`10, 17` for *"October 17"*), absent-consumer (counted, never failed: `firstFallRiskBegins` has zero
readers — Q7 of the seat). Allowed locations are 28 of 40 coordinate hits (`images/property-map/*.bounds.json`, domain
`_meta`, `viewer.html:PROPERTY_DATA`, `worker/digest.json`), so day one is not red forever. Check — its `--selftest`:
plant `FROST_MONTH, FROST_DAY = 10, 17` in a scratch tool → **fires**; remove → clears; plant `34.5496` in an allowed
location → silent; a value the lint cannot see (a computed `2873/1000*7`) is **listed in its docstring as a blind spot**.
**4c · The 0e roster** — agent drafts, **Paul rules Q4 first** · reversible · `check-data-inline.py` reports the 4 + 5
drifted paths (`PROPERTY_DATA`, `REFERENCES_DATA`) and **stops** — which side of *fairway → clearing* is right is content.
After the ruling: `--fix` in the ruled direction, then both consts join `SOURCES` as whole-document rows with the
`climate.monthlyNormals` subtree excluded (a runtime cache, or it fires on every load) and `CELESTIAL_DATA` excluded with
its reason. Check: `python3 tools/check-data-inline.py` exit 0 with 14 rostered; the P5 count in step 5 drops 10 → 8 → the
six with no producer (Q5).
**5a · `ENGINE-MANIFEST.md` + `check-engine-manifest.py`** — agent · reversible (a doc + a checker; nothing moves) ·
**ships with C4 5a**, not before — class **derived** from the dir→class table (`tools/` → engine, `worker/` → engine as
explicit rows: *invert ownership, not the directory*) plus the three rosters it **reads** (`momlib.DOMAINS`, `NON_DOMAINS`,
`check-data-inline.SOURCES`); a declared exception table (the two unclassified root JSONs, `COMMS-CHANNELS.json` and
`arrival-dispositions.json`, each with a reason); tiers declared per engine file, never derived; `mixed` first-class with a
shrink target (`viewer.html`, `worker/worker.js`, `worker/digest.json`) — Q6. Predicates: P1 unclassified → fail; P2 dead
or reasonless waiver → fail; P3 engine-identity → `skipped: no engine remote declared` until C4 5d, never `pass`;
P4 = step 4's lint, **counted, arms at 0**; P5 consts outside `SOURCES`, **counted, arms at 0**. Check — `--selftest` by
mutation: planted unclassified file → P1; a waiver to a deleted file **and** one with an empty reason → P2; a `DOMAINS`
member the table cannot place → P1; `10, 17` in an engine file → P4 counts then clears; a new `*_DATA` const → P5 counts;
a clean fixture → exit 0; an unreachable engine remote → `skipped`; a fixture whose `viewer.html` is a 404 page → **throws**.
Then one line in `CLAUDE.md`'s session-start block (or the three counting checks behind one summary line — Q7).
**6a · One key builder** — agent · reversible (additive) · **after C4 3a** · `keyFor(estateId, ...parts)` →
`<estateId>:<prefix>:<suffix>`; `estateId` comes from the `ESTATE_ID` binding (per-env, non-inheritable — a forgotten one
**throws**); C6 later passes the grant-resolved id through the same signature. **Never from the path or query** — the
four readers' HTTP contract is unchanged, which is why they need zero changes. All 45 sites routed; a grep is the
falsifier, not the source. Check, in QA only: `qa-write-probe.py` plants a record, `GET` returns it, the KV listing shows
`<estateId>:feedback:<date>` and **no** unprefixed key from this run; `grep -c 'searchParams.get("estate")\|body.estateId'
worker/worker.js` = 0.
**6b · The legacy window** — agent · reversible · one constant `LEGACY_BEFORE = "<cutover date>"`; unprefixed keys are
read **only** for earlier dates — ⛔ never `get(new) || get(old)`. Check: `GET /api/feedback` over a range spanning the
cutover returns both eras; a range wholly before it is non-empty; `python3 tools/read-mom-feedback.py --pickup` and
`check-mom-ack.py` unchanged on prod after deploy.
**6c · The two `list({prefix})` calls + `zones:all`** — agent · reversible **while the unprefixed keys are not deleted**
(deletion is a separate later act, after 7 days of `/api/zones-sync-status` agreeing) · `conversation:` cleanup and
`zones-last-seen:` listing take the prefix; `zones:all` is copied to its prefixed key in the same deploy as its reader.
Positive control (their failure is silence): plant a prefixed conversation in QA, the cleanup must **count 1**, not 0;
`zones:all` read back under the new key **equals** the old payload byte-for-byte before prod; `handleZonesSyncStatus`
lists the planted device.
**7a · Instance config, derived** — agent · reversible · **with C4 5b** · `instance/fernwood.json` identity (name,
subtitle, address line, coordinates, elevation, KJZP, frost anchors, the station-MAC *reference*) is **generated** by
`momlib.config` from `property.json`, never typed; the lint's allowed locations gain it. Check: regenerate → `git diff`
empty; `check-config-derivation.py` exit 0 with the file present.
**7b · The masthead substituted at build** — agent · reversible · placeholders in `engine/viewer.template.html`;
`build-viewer.py` fills them; the built `viewer.html` is **static HTML** — no runtime fill, so no flash and no empty header
on a JS failure. The product name string is **not authored here** (C4 2a's naming decision supplies it; until then the
placeholder resolves to today's text so the built file is byte-identical to the committed one). Check: `build-viewer.py
--check` exit 0; `curl -s <QA viewer> | grep -c '{{'` = 0; Playwright at 414 × A+ **with JavaScript disabled** shows the
estate name in `<h1>`; `herConditions()` `clean:true`.
**7c · The Worker's instance data** — agent · reversible · `AMBIENT_MAC_DEFAULT` retired; `env.AMBIENT_MAC` required, the
proxy answers 503 `ambient-not-configured` without it — engine code holds no station. Check: `/health` reports
`configured.ambient:true` on prod; a QA deploy without the var → 503 from `/api/ambient`, never Fernwood's readings.

## Falsifier

For the design as a whole — each observation, and how it is measured:
- **A re-typed config value ships green.** Measured: 4b's planted `10, 17` does not fire, or `fleet_probe.py --selftest`
passes after `property.json`'s frost date is moved and the probe's date does not move with it. If true, the lint is
keyed on the wrong thing and step 4 is decorative.
- **A `personId` lands on a pre-identity record.** Measured: 1b's fixture dated before `attributionIsValidFrom` resolves
non-null; or `git grep personId` shows a second writer; or any record on prod dated before the step carries a non-null
person. If true, attribution by inference has been built — the class every rule here forbids.
- **A module OFF renders an empty tile, or a plant question, or a plants digest key.** Measured: 3b's gardenless fixture
— `#dash-plants-sub` present at 414 × A+, a candidate with `entityRef.type: plant`, or `"plants"` in the digest. If true,
the declaration is decorative and the unit was chosen wrong (the seat's own falsifier).
- **The identity block flashes the wrong name.** Measured: 7b with JavaScript disabled shows a placeholder, an empty
`<h1>`, or a name that differs from the instance file; or `grep -c '{{' viewer.html` > 0 on the built file.
- **The estate cannot come from a binding alone.** Measured: 6a's grep > 0 — a handler reads a tenant from the request.
If true, rule 3 is unimplementable on this stack and C6 must precede step 6.
- **A stale prefix returns an empty container as success.** Measured: 6c's planted conversation is cleaned as `0`, or
`zones:all` reads back empty under the new key. If true, the `list()` calls are silent and the prefix is a heads-up, not
a guarantee.
- **The counted predicates never arm.** Pre-registered (proposal §7), answered in this file's `## Retro`: *did P4 or P5
reach zero by the time C5 closed — and if not, what was the count on the closing run?* "Still counted, N unchanged" is a
valid answer and the more informative one; if so the predicate wants scoping down or dropping.
- **The readiness mechanism is ceremony** (readiness §5): the seats' findings did not change the build — measured as the
count of steps here that exist only because a seat measured something (today: 1, 2c, 3a's `turf`, 4b's detector kind, 5a's
two files). Zero at retro is a valid, informative answer.

## QA

**Agent may exercise, and where.** Steps 1–5: **locally** — every tool, every `--selftest`, both fixtures in the
scratchpad, `python3 -m http.server 8765` + `herConditions()` for 3b. The Worker deploy for 1a is the agent's job
(`deploy-worker.sh`, sandbox off) — it is additive and `/health` proves it. Step 6: **only on the C4 QA Worker**, only
after C4 3f is green (`/health` → `env:"qa"`, `kv_canary:"qa"`) — plant, list, read back, delete. Step 7: on the QA origin
via Playwright at 414 × A+, JavaScript on and off. On prod, permanent: **read-only** — `GET /api/feedback`, `/health`,
`check-live.py`, `check-digest-fresh.py`; never `POST /api/feedback`, never her device, never a KV delete.
**Agent may NOT:** run `test-feedback-cycle.py --live` (a prod write); rule the *fairway* drift or run `--fix` on it;
write a non-null `personId` anywhere but 1b's resolver; put a real name or a family name in a tracked file; delete an
unprefixed key; author the product-name string; write `- ready:`.
**Paul verifies:** Q1–Q5 rulings before the steps they gate; `--live` after 1a; the drift direction (4c); the `mixed`
rows and the tiers in 5a; `check-live.py --wait 180` after any viewer ship; a read of the gardenless fixture's strip.
**Mom's presence: nothing.** No surface she reads changes shape — the strip at Fernwood renders four tiles as today, the
masthead renders the same words, no origin moves, no storage key changes, no card is added. If any step needs her phone,
the plan is wrong and the step stops.
**Expected outputs, named:** `check-domains.py` → the existing table plus, at Fernwood, no `declared off` rows;
`check-config-derivation.py --selftest` → `planted 10,17: fires · removed: clears`; `check-engine-manifest.py` →
`P1 0 · P2 0 · P3 skipped: no engine remote declared · P4 counted: N (arms at 0) · P5 counted: N (arms at 0)`;
`qa-write-probe.py` → `prefixed key present · unprefixed absent · list count 1`; `check-backlog-ready.py` → silent.

## Open before stamping

> **✅ RULED 2026-09-03 `[paul-stated]` — Q1 · Q2 · Q3 · Q4. Three remain (Q5 · Q6 · Q7).**
> - **Q1 → B, the named bundle.** *"bundle makes sense."*
> - **Q2 → `fernwood`, and the id may be a record, not a bare string.** *"if estateId needs a dict or something with
>   both the human and data ids that's fine by me."* So: an opaque data id **plus** a human handle, both recorded, the
>   coordinate-not-label rule attached to the data id.
> - **Q3 → opaque `personId`; the display name is SUPPLIED BY THE PERSON at setup and lives in the account record, never
>   in a tracked file.** Paul widened this into a journey statement: *"we need to have within the journey a set-up phase
>   and allow people to set their own name — they'll get some kind of invite, set up an account, and that will include
>   setting up their profile and providing their name, and it's on us to then use that name to track feedback in that
>   account instead of the device ID. And I also hope we can streamline the syncing issue — that's kind of manual now —
>   to sync devices into this account. That's a bigger thing to step back and look at and make sure we have well
>   described."* Captured as its own item: `PRODUCT-ENGINE.md` § THE SETUP JOURNEY; ⚠️ it collides with the
>   user-researcher's ACTIVATION model (*"recognized, never registered"*; *"display name is habit"*) and that collision
>   is surfaced there, not resolved here. **For THIS plan:** step 1b's resolver mints the opaque id; the caveat-window
>   (07-13 → 07-27) records resolve to **null** — identity is not applied backwards.
> - **Q4 → canon wins.** *"let's go with the canon that we established and align everything to that."* 4c's `--fix`
>   direction is canon → consts; the P5 count follows.


1. **Q1 The module UNIT** — domain (A) or named bundle (B). The seat recommends **B** on one measurement: `turf` is not
   in `momlib.DOMAINS` and *is* a real inlined const, so *"garden off"* under A leaves turf rendering; A also reopens
   VOCABULARY §3's ratified `module`. Paul's call; 3a cannot start without it.
2. **Q2 The `estateId` value** — `fernwood` (legible, matches C4's *"the instance is Fernwood"*) **plus the written rule
   that an id is a coordinate, not a label**, recorded beside the value; or opaque (`est-001`), whose cost is paid by every
   future debugging session. Recommend `fernwood` + the rule.
3. **Q3 Mom's `personId`** — her name must not enter a tracked file (VOCABULARY §3b's rule already holds: the register
   carries handles). `mom` is already the handle and public-safe, but it names a *relationship to Paul*, and at her own
   estate she is the owner; under Q2's rule an id must not be a label. Options: keep `mom` with the rule attached, or mint
   an opaque `p-…` and keep `mom` as the display handle. Also: does the 07-13 → 07-27 caveat window resolve to the id or null?
4. **Q4 Which side of *fairway → clearing / turf / meadow* is right** — canon (`property.json`, `references.json`) or the
   inlined consts. Content, not method; 4c's `--fix` direction and the P5 count both wait on it.
5. **Q5 The six unguarded consts** (`CELESTIAL` · `EVENTS` · `PROPERTY` · `REFERENCES` · `SOURCES` · `SUN_HORIZON`) —
   each gets a producer and a roster row, or is retired from the viewer. P5 cannot reach zero until each is one or the other.
6. **Q6 `mixed` as a manifest class now**, or the manifest waits for C4 5b so nothing needs it. Recommend now — a gate
   nobody can clear is a gate nobody runs.
7. **Q7 The grant register in the private sibling** — recommend yes (rule 2 + the person↔place map argument); and is the
   API contract **frozen** with the estate never on the path or query — recommend yes, it is what keeps 0b's cost at zero.
8. **Not decided here, flagged:** `group`'s double-booking (VOCABULARY §5) — step 3 is the seam predicted to bite; the
   migration is its own decision, not this item's.
