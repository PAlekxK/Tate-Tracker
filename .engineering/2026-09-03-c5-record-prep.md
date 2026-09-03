# C5 · RECORD PREP — pricing the data model's five reversible steps

**Mode:** path evaluation · **Seat:** `engineering-partner` · **Date:** 2026-09-03
**Item:** `BACKLOG.md` § "C5 · RECORD PREP" · **Depends on:** C4 (ruled 2026-09-03)
**Nothing here is decided. No canon changed, nothing written, nothing deployed.** Ends at Paul's gate.

**Citation convention.** Files are cited by **repo-relative name + role**, never by line number — C4
renames the repo root and the inversion moves `tools/` under `engine/`. Where a claim rests on a
measurement, the command is named so it can be re-run.

---

## §0 · FIVE MEASUREMENTS THAT CHANGE THE ITEM — run today, not restated

| # | The plan says | I measured | Consequence |
|---|---|---|---|
| **0a** | data-model §3: the Worker has *"11 KV namespaces"* | **13.** The roster omits `zones:all` — a **singleton** key holding the whole zone canon, not date-keyed — and `zones-last-seen:<deviceId>`. `grep -oE 'OBSERVATIONS\.(get\|put\|delete\|list)' worker/worker.js` → **45 call sites**, several building the key in a variable, so no grep enumerates them all | Step 1 needs **one key-builder**, not a patched list. A roster of 11 already rotted — same class as C4's 12→18 storage keys. *A grep is a good falsifier and a bad source* |
| **0b** | C5 asks what the four Mom-cycle readers need changed *"(they read these keys)"* | ⭐ **They read no KV keys.** `read-mom-feedback.py`, `read-mom-engagement.py` and `mom-cycle-status.py` all go through the shared library's HTTP getter against `/api/feedback?start&end` and `/api/metrics`; `check-mom-ack.py` touches neither. **No tool invokes `wrangler kv`** — the only `wrangler` calls are the two deploy paths | ⭐⭐ **Step 1's blast radius is the Worker alone**, if the HTTP contract holds. The largest cost reduction available in C5, and it inverts the step's assumed shape |
| **0c** | data-model §5: the prefix is *"the only irreversible thing"* because a second contributor's words *"interleave inside one key"* | The hazard is **person**-shaped; the prefix is **estate**-shaped. Two contributors at **one** estate still interleave under any estate prefix — and C4 already ruled instance 2 gets **its own Worker + KV namespace**, which fixes the cross-estate case without a prefix | ⭐ **The deadline moves off the key and onto the record** (§1, §6). The prefix is still worth doing, for a smaller and different reason |
| **0d** | data-model §4 names the fleet probe's `FROST_MONTH` as *the* config leak | The class is **12 tracked files**. `grep -rl '34\.5496'` over `tools/ worker/ *.html` → eight Python tools, `analyze-weather-bias.mjs`, `area-trace.html`, `viewer.html`, `worker/digest.json`. Only **5** tools read `property.json` at all, and **2 of those re-type the coordinate anyway**. The station MAC sits as `AMBIENT_MAC_DEFAULT` **inside the Worker** — engine code holding instance data | Step 5 is not one constant. §5a argues for a lint, not a 12-file rewrite |
| **0e** | — (recorded nowhere) | 🔴 **`PROPERTY_DATA` — the viewer's 19,158-byte inlined copy of `property.json` — HAS ALREADY DRIFTED, unguarded.** Parsed diff → **4 paths**: `location.aspect.description`, `location.aspect.implication` (viewer says *"fairway clearing"*, canon says *"open clearing"*), `microclimate.southFacingFairway` vs canon's `southFacingClearing`. **No tool in `tools/` or `.github/` references `PROPERTY_DATA`** — the one `*_DATA` const with no re-inline path and no alarm. ✅ The Guru digest is clean (0 stale hits in its property block) | ⭐ **Step 5's derivation source is itself duplicated into an unguarded copy.** Currently inert: the app reads only 4 paths and none of the drifted ones — **19 KB of config to serve four reads.** *Trace a field to its consumer, not to its institution* |

⚠️ **0f · A RULING LANDED WHILE THIS WAS BEING WRITTEN, and it moves §1.** Commit `1241a77`
(2026-09-03 12:05 ET, in a concurrent session) amends C4's custom-domain row with **ONE DOOR FOR
EVERYONE** `[paul-stated]`: *the domain names the PRODUCT, not Fernwood… the estate is chosen behind
it by grant, never by the address… **isolation is by grant***. That is a **different isolation
mechanism** from data-model §2 rule 1's *one database per estate*, and it is the mechanism C4's
earlier row assumed away when it ruled *"instance 2 gets its OWN Worker + its OWN KV namespace."*
One door means **one Worker resolving the estate at runtime** — which it can only do from a
credential, and there is no credential until step 6. ⭐ **So the prefix becomes MORE load-bearing
under this ruling, not less** (§1). Verified against the commit, not the row — *a verification is
true at an instant, not for a day.*

**One more, which decides §3:** `momlib.DOMAINS` declares **11** domains; `check-data-inline.py`'s
`SOURCES` roster checks **12** consts. The extra is `turf.json`/`TURF_DATA` — which
`check-domains.py`'s `NON_DOMAINS` explicitly declares **not a domain** (*"care regimes, not
entities"*). `viewer.html` carries **22** `*_DATA` consts, so **10 have no drift alarm at all**
(`CANDIDATES · CELESTIAL · ENTITY · EVENTS · MOM_ACK · PROPERTY · REFERENCES · RELEASE_NOTES ·
SOURCES · SUN_HORIZON`).

---

## §1 · THE KV WRITE-PATH PREFIX

**Three jobs are collapsed into one step and they have different answers** — the whole finding here.
It maps onto a principle already on the shelf: *isolation is a guarantee; awareness is a heads-up;
never let a safety claim rest on the second.*

| job | what delivers it | status after C4 |
|---|---|---|
| **Isolation** — instance 2 cannot reach Fernwood's record | a **separate KV namespace** per estate | ⚠️ **contested by 0f** — `[env.qa]` proves the pattern, but *one door for everyone* means one Worker choosing the namespace from a credential that does not exist yet |
| **Separability** — a stray writer's rows are findable and removable afterwards | an **estate prefix** on the key | ⛔ not built |
| **Attribution** — whose words these are | a **`personId` on the record** (step 2), null when unknown | ⛔ not built — and this is what §5 actually feared (0c) |

**Recommended shape: `<estateId>:<existing-prefix>:<existing-suffix>`, built in exactly one place.**

- **Left prefix**, because KV's only range operation is `list({prefix})` and it keys off the left. Two
  calls use it — `conversation:` (the Guru-probe cleanup) and `zones-last-seen:`. ⚠️ **Their failure
  mode is silence**: a stale prefix returns zero and the cleanup reports success having done nothing —
  the *empty-container-as-valid-answer* class. Needs a positive control, not a code read.
- **One builder, because 45 call sites cannot be held by discipline.** `k(env, ...parts)` reads the
  estate from a **Worker binding** and **throws** when it is absent — never defaults. Bindings are
  non-inheritable per environment (C4 §1.2), so a forgotten one fails loud.
- **Legacy readable by a declared window, not a fallback.** ⛔ Not `get(new) || get(old)` — a silent
  fallback makes *"the prefix works"* and *"the prefix is broken"* render identically. One constant
  `LEGACY_BEFORE = "<cutover date>"`; the unprefixed key is read **only** for earlier dates.
- ⚠️ **`zones:all` is the awkward one** — a singleton holding the whole zone canon, with no date
  window to hide behind. Prefix it in the same commit as its reader; verify by reading it back.

**Does C4's QA namespace make the prefix unnecessary? Complementary — and per 0f the prefix is now
the load-bearing half.** The namespace buys isolation *between environments*; the prefix buys
**separability between estates inside one namespace**, which is what *one door for everyone* requires
until a credential exists. And it covers the case no namespace can: C4's finding 0c, that
`POST /api/feedback` and `POST /api/zone-audio` are **ungated by design**, so nothing distinguishes a
QA writer from Mom. If a QA build ever ships pointing at the prod Worker, the namespace does not save
you and the prefix is the only thing that makes the damage separable afterwards.

**What the four named tools need: nothing** (0b) — *provided the HTTP contract is unchanged.* That is
a design constraint on step 1: **keep the estate coordinate out of the API path and off the query
string.** A `?estate=fernwood` would change all four readers **and** violate rule 3 directly — *a
property id in a URL is a client's claim about itself.* The estate belongs in the **binding**, which
is the server's own knowledge.

| | Effort | Rev. | What could break | The deterministic check |
|---|---|---|---|---|
| key-builder + 45 sites routed through it | ~3 h | ✅ additive | the two `list()` calls go silently empty | in **QA**: plant a key under the new prefix, assert `list()` finds it and that the unprefixed key is **not** returned |
| legacy read window | ~1 h | ✅ | pre-cutover reads 404 | `GET /api/feedback` over a range spanning the cutover returns **both** eras; a range wholly before it is non-empty |
| `zones:all` prefixed | ~1 h | ⚠️ one-way | zone canon reads empty → the map projects against nothing | read-back equality on the full payload in QA before prod |

**Falsifier:** if the estate coordinate cannot be sourced from a binding alone — if any handler needs
it from the request — rule 3 is unimplementable on this stack and step 6 (auth) must precede step 1.
*Test: after the builder lands, grep the handlers for a request-derived tenant; the count must be zero.*

---

## §2 · MINTING `estateId` / `personId` / A GRANT AS DATA

⭐ **`personId` already exists.** `tools/people.json` is the deviceId→person register and its
`people[].name` values are already the pseudonymous handles **`paul` · `mom` · `telemetry-test`** — no
real name in a tracked file, satisfying the rule VOCABULARY §3b states (*the name rule governs
tracked files*). **Step 2 promotes an existing handle to a declared id; it does not invent a
register.** *Reuse the vocabulary before adding a state.*

⭐⭐ **The backwards-attribution hazard already has a recorded boundary.** That file's `_meta` carries
`attributionIsValidFrom` — *"FULLY valid 2026-07-28 onward; USABLE-WITH-A-CAVEAT from 2026-07-13"* —
plus `CLEAN_SLATE` and `whatThisInvalidates`. So *pre-identity records stay unattributed* is
enforceable by **citing that field**: any tool stamping a `personId` reads it and writes **null**
earlier. That null must be **declared, never absent** — an absent field and a person we could not
identify are the same observation, the failure class this whole item exists on.

| id | home | class | why there |
|---|---|---|---|
| `estateId` | ⭐ a **new `estate.json`** at the instance root | instance | `property.json` already means *facts about this place*, and VOCABULARY §4 rules `property` unusable as the tenant noun. Putting `estateId` in it re-mixes the two meanings the vocabulary work just separated |
| `personId` | `tools/people.json`, promoted to a first-class `id` beside `name` | instance (the register) | already there, already public-safe, already carries the validity boundary |
| the **grant** | ⭐ **`fernwood-private`** — the local-only sibling C4 ruled into existence, and named as the condo directory's home in commit `ca41a88` (2026-09-03, concurrent session) | outside the estate | rule 2 — *an estate never knows who owns it.* A `grants.json` in the public repo would invert rule 2 structurally **and** publish a person↔place map, the third-party class C4's push-hold protects. ⚠️ Register it in `guard-secret-push.py`'s `NEVER_PUBLIC` **at creation** |

**The `estateId` value — recommended `fernwood`, with a rule attached.** The trade is legibility
(greppable, debuggable, matches C4's *"the instance is `Fernwood`"*) against rename-proofing (opaque
`est-001` never migrates). Because a written KV key is effectively permanent, the resolution is not
to pick opaque — it is to **declare that the id is a coordinate, not a label**: *renaming the place
does not rename the estateId*, recorded in `estate.json` beside the value. *Record the referent, not
the reference.* ⚠️ Paul's call (§7) — the opaque id's cost is paid by every future debugging session;
the legible id's cost is paid **only if** the rule isn't written down.

**Effort ~2 h · fully reversible · nothing can break** (nothing branches on any of the three).
**Check:** `check-vocabulary.py` already fails on `propertyId` (V1) and on a double-booked key (V3) —
run it as the positive control that the new file uses canon's word. Plus one assert that
`git grep -l estateId` returns the **declaring files only**.

---

## §3 · THE MODULE-SET DECLARATION

**None of `momlib.Domain`'s seven fields names an estate — and none should.** `Domain` is engine-class
(data-model §4: *identical across properties; a divergence here is a defect*), so an eighth
per-estate field puts a per-estate value inside an engine declaration. **The on/off value belongs in
the estate's config; the module→domain membership belongs in the engine.**

| | **A · per-domain switch** (`estate.json: domains: {plant: on, turf: on…}`) | **B · named bundle** (engine `MODULES` membership + `estate.json: modules: {garden: off}`) |
|---|---|---|
| Effort | ~2 h — one block, one resolver | ~4 h — membership map in the shared library, estate block, resolver, overlap rule |
| Expresses *"the condo has no garden"* | ⛔ **no** — four rows that can drift; a half-off garden is representable | ✅ one atomic declaration |
| ⭐ Reaches `turf` | ⛔ **no, measured.** `turf` is not in `momlib.DOMAINS` and *is* declared a non-domain — yet `TURF_DATA` is a real re-inlined const and PRODUCT-ENGINE names turf a garden member. **"Garden off" would leave turf rendering** | ✅ membership is a set, so it can name a non-domain member |
| Vocabulary | ⚠️ contradicts **ratified** canon — VOCABULARY §3 stamped `module` as *the ON/OFF unit per estate, a named set of one or more domains* | ✅ matches it |
| Drift risk | four rows, no invariant | one row; the overlap rule lives in one function |
| Learning value | low | teaches the engine/config seam on a concrete case |

**Recommendation: B.** Not on tidiness — on the measurement that **A cannot reach `turf`**, so the
first module Paul actually named (*"the condo has no garden"*) is the one A gets wrong. ⚠️ **Marked
Paul's call per the brief** — but choosing A means reopening VOCABULARY §3, and §7's own falsifier
(*if `module` and `domain` are used interchangeably, the granularity question was answered by
convenience*) is aimed at exactly that.

⚠️ **Membership is not a partition** — `zone` belongs to both *the garden* and *the place*. So the
resolver is one engine function, `enabled_domains(estate)`, where a domain is on if **any** ON module
claims it: written once, not re-derived at five call sites. **And step 3 forces VOCABULARY §5's live
defect** — `module` names sets across domains whose `group` is the *action* axis and across
`vehicles.json` records whose `group` is the *kind* axis. This step is the seam that was predicted to
bite. Flagged, not decided (§7.6).

### The five consumers — OFF vs ON-but-EMPTY

| consumer (role) | **OFF** | **ON-but-EMPTY** |
|---|---|---|
| `harvest-questions.py` — drafts confirm cards from canon uncertainty | skip the domain. **One `continue` in the existing loader**, which already has one for `cardable` | iterate, produce zero candidates — **correct, and reportable as a gap** |
| `check-domains.py` — domain conformance | print a **third row state: `declared off`** — neither 🔴 nor absent. ⭐ And its undeclared-file sweep **inverts**: a non-empty domain file at an OFF module is a **finding**, because that is undeclared data. *Declared absence vs. drift*, made checkable | check as today; an empty list stays a finding |
| `build-digest.py` — the Guru's context (its `main()` is a hand-written literal dict, roster #3) | **omit the key entirely** + one `_meta` line: *"this estate declares no garden."* ⛔ Not `"plants": []` — an empty array still invites the model to discuss plants. This is the 41%-of-digest saving | include normally |
| `renderDashboardStrip()` — four tiles | **don't render the tile**; the strip reflows rather than leaving a hole. ⚠️ **The largest of the five**: it fills `#dash-plants-sub` and siblings, ids that exist in **static HTML**, so OFF is a markup change, not a data check. Right shape: render from a declared tile roster × the estate's module set | render the tile in its existing empty state |
| the engagement signals (`mom-cycle-status.py`'s `offers-passed` · `sessions-quiet`) | ⭐ **exclude off-module offers from the denominator** — a non-tap where there are no plants must not count. When the module set is **unreadable**, publish `?` and never fire: the file already has that idiom for an unmeasured offer count | count normally — she was genuinely offered something |

**Effort ~4 h + ~2 h per consumer · reversible · what breaks:** a consumer reading the raw `DOMAINS`
dict instead of the resolver silently keeps old behaviour — the awareness-not-isolation failure.
**Check:** a `--selftest` building a synthetic gardenless estate in a temp dir, with **a clean case
and a firing case**; flip `garden: off` at Fernwood in the fixture and assert `build-digest` omits
`plants`/`turf`/`weeds`/`zones` **and** the strip loses a tile.
**Falsifier:** if a gardenless fixture still yields a plant question, a plants digest key, or a plants
tile, the declaration is decorative and the unit was chosen wrong.

---

## §4 · THE ENGINE MANIFEST + CHECKER

**Derived or declared? Neither alone — derive the class, declare only the exceptions, and make
*unclassified* a failure.**

- **Pure derivation from C4's directory split** (`engine/` · `config/` · `instance/`) has zero drift,
  but cannot classify what stays at the root (`README.md`, `.github/workflows/`, `CLAUDE.md`,
  `BACKLOG.md`) and cannot express **config**, which is data living in the instance.
- **A pure declared `ENGINE-MANIFEST.md`** is a hand-kept roster over hundreds of files — the class
  this repo has now measured rotting **three times** (12→18 storage keys, 11→13 KV prefixes,
  22-consts-vs-12-checked).

**Recommended:** class = the top-level directory; a short declared exception table with a **reason
string per row**; four failing predicates:

1. any tracked file whose class is neither derivable nor declared → **fail** (the coverage proof);
2. an exception row whose file no longer exists → **fail** (a dead waiver is the rot mode);
3. an `engine`-class file differing from the engine source of truth → **fail** (byte-identity);
4. a config **value** present in an engine-class file → **fail** (the `FROST_MONTH` class; §5a's lint).

⚠️ **The hazard the plan doesn't name: `viewer.html` cannot be classified.** It is 53% instance / 47%
engine by data-model §3's own measurement, and `worker/worker.js` is engine code carrying the station
MAC. So the manifest needs **`mixed` as a first-class class with a declared shrink target** — not an
unclassified hole, or the checker reports green over the largest divergence surface in the product.
Honest first roster: `viewer.html` (mixed → split at the inversion) · `worker/worker.js` (mixed → MAC
to config) · `worker/digest.json` (build artifact → per-instance).

**Same tool as C4's byte-identity check, or two? One tool, four predicates, one skipped.** C4's
`check-engine-sync.py` answers *"is this copy identical to the engine repo?"* — cross-repo, exists
only after the split. The manifest answers *"is every file classified and does its content match its
class?"* — within-repo, exists now. **Build one `check-engine-manifest.py` whose predicate 3 reports
`skipped: no engine remote declared` until the split exists**, so C4 step 15 *turns a predicate on*
rather than adding a tool. A second tool is a second definition of engine-class — and data-model §4
already says why: *two probes are how two definitions of "a lap is owed" are born.*

**Effort ~5 h · reversible (a doc + a checker; nothing moves) · nothing breaks at runtime.**
**Check:** its own `--selftest` on a temp fixture — a planted unclassified file must fail, a planted
dead waiver must fail, a clean tree must pass. **Ships with C4 step 13**, not before: a manifest
written earlier is a hand-roster the split would have derived.

---

## §5 · DE-HARDCODE THE IDENTITY BLOCK + DERIVE CONFIG FROM CANON

### 5a · Config derivation — a lint, not a 12-file rewrite

| re-typed copy | canonical path | consumers | note |
|---|---|---|---|
| `FROST_MONTH, FROST_DAY = 10, 17` in the fleet probe's threshold block | `frostDates.atPropertyElevation.firstFall_50pct` = **"October 17"** | 1 (the fleet loop's SEASON signal) | the value moved once already (Oct 20 → Oct 17) |
| — (no copy, **no consumer**) | `frostDates.atPropertyElevation.firstFallRiskBegins` = **"September 29"** | **0** | a canon field nothing reads — the probe's second anchor |
| coordinate pair `34.5496 / -84.3674` | `location.coordinates` | **12 tracked files** (0d) | 2 of them read `property.json` *and* re-type it |
| elevation `2,873 ft` | `location.elevation.estimated_ft` | basemap fetcher (⚠️ **once inside emitted data**, not a comment), KML exporter comment, the viewer masthead | an emitted stale copy propagates into a produced artifact |
| `AMBIENT_MAC_DEFAULT` | the station's device record | the Worker | engine-class code holding instance-class data |

**Recommendation — two moves, ~4 h, and don't touch the 12 files yet:**

1. **One accessor in the shared library** — `momlib.config("location.coordinates.latitude")` — reading
   the estate's config canon and **raising on a missing path**. Never a default: a config accessor
   that falls back is how a wrong value ships looking correct.
2. **A drift lint** over a declared roster of `(value, canonical path, allowed locations)`, failing
   when a literal appears anywhere else. That turns a 12-file refactor into a 1-file check plus
   incremental migration — *generate the derivable; drift-lint the rest.* ⚠️ **Roster rows must carry
   allowed-locations, not just a value**, because `viewer.html`'s inlined instance data legitimately
   contains the coordinate; a lint that fires forever is the costly-control shape already ruled
   against. **Positive control:** plant `34.5496` in a scratch tool, prove it fires, remove it, prove
   it clears.

⭐ **Fix 0e in the same pass — it is smaller than it looks.** `PROPERTY_DATA` is 19,158 bytes serving
**four** read paths, already drifted in 4 places, with no alarm. Don't move it to a config file —
**shrink it to what the engine reads** (`location.coordinates.approximateLat/Lon`, `climate.*`) and
add the remainder to `check-data-inline.py`'s roster. ⚠️ One wrinkle: the app **mutates**
`PROPERTY_DATA.climate.monthlyNormals` at runtime after fetching ERA5 normals — that subtree is a
**cache, not config**, and must be excluded from the drift check or it fires on every load. Two things
sharing one const is the finding; splitting them is the fix.

### 5b · The identity block — and why it lands *after* C4's build step

**The band is genuinely bounded, confirming §3's *"not soaked"* verdict at the markup level:**
`<title>`, `<h1>`, the `header-subtitle` div (*"An Appalachian Almanac for 282 Church Mountain
Road"*) and the `header-address` div (*"Jasper, GA · 2,873 ft on the Blue Ridge"*) sit in **one
contiguous header block**, plus the unified-input section's `aria-label` naming *"the Fernwood
Almanac."*

⚠️ **But the obvious implementation is a regression on Mom's surface.** The masthead ships as **static
HTML** — it renders before any JavaScript runs. A runtime config fill introduces a flash-of-wrong-name
and, on a JS failure, **an empty header on her phone.**

⭐ **So substitute the identity block at BUILD time, not read it at runtime** — exactly the build step
C4 accepted (*"a build step is an accepted price"*). This is the first concrete thing that step buys
and the reason 5b sequences **after** the inversion. If the build step is deferred, the fallback is a
runtime fill with today's text left as the static default — two copies of the masthead, needing their
own lint. Build-time is strictly cheaper.

⛔ **The product name in Mom-read prose (*"the Fernwood Almanac"*) is flagged, not decided** —
`content-steward`'s, VOCABULARY §4 already rules *"Almanac" as a portable noun* out, and **0f makes
the product's name a prerequisite of C4 step 2a**, so this is now upstream of 5b rather than beside it.

**Effort: 5a ~4 h · 5b ~3 h after the build step · both reversible. Checks:** 5a — the lint's positive
control plus `check-data-inline.py` passing with `PROPERTY_DATA` newly in its roster. 5b — the C4
sequence's ship check at her real conditions: **the masthead renders the estate's name with
JavaScript disabled.**

---

## §6 · ORDER, AND WHAT SHIPS INDEPENDENTLY

⭐ **Three of the five need nothing from C4 and can start now.** The row's *"Depends on C4"* is true of
the KV prefix and the manifest — **not of the other three**, and holding all five costs weeks for no
reason.

| # | Step | Independent of C4? |
|---|---|---|
| **1st** | **§2 · mint the ids** | ✅ **yes** — ~2 h, nothing branches, prerequisite for naming anything in the other four |
| **2nd** | **§3 · the module declaration** | ✅ **yes** — no split, no build step, no environment. ⭐ And it is the prerequisite for **C7's "no garden" falsifier**, which C4's own sequence (step 14) wants to run |
| **3rd** | **§5a · the config lint + accessor + the 0e fix** | ✅ **yes** — one new file, one roster, zero runtime change |
| 4th | **§1 · the KV prefix** | ⛔ **after C4's `[env.qa]`** — the only place a write path can be exercised without touching her record. ⚠️ Per **0f** this step got *more* important, not less: under *one door for everyone* the prefix is the only estate boundary that exists before auth |
| 5th | **§4 · the manifest + checker** | ⛔ **with C4 step 13** (the directory split) — it *is* that act |
| 6th | **§5b · the identity block** | ⛔ **after C4's build step** — runtime fill is a regression on her surface |

**One re-ordering against data-model §8, argued.** §8 puts the KV prefix **first** on the strength of
its deadline. Per 0c that deadline is mis-attributed: the interleave hazard is person-shaped, and
C4's namespace-per-instance ruling already covers the cross-estate case. **The genuinely
deadline-bearing item is the `personId` field on the feedback record — step 2**, which §8 prices as
*"hours, zero risk."* Step 2 moving to first is not a preference; it is the deadline following the hazard.

---

## §7 · WHAT I DID NOT DECIDE — Paul's calls

1. ⭐ **The module unit** — domain (A) or named bundle (B). I recommend **B**; the measured reason is
   `turf`, which A cannot reach. Choosing A means reopening VOCABULARY §3.
2. ⭐ **The `estateId` value.** I recommend **`fernwood` plus the written rule that the id is a
   coordinate, not a label**; opaque (`est-001`) is defensible and the trade is in §2.
3. ⛔ **The product name in Mom-read prose** — flagged, not decided; `content-steward`'s.
4. **Whether the grant register lives in the private local-only sibling.** I recommend yes, on rule 2
   plus the person↔place-map argument — but it is the first artifact to leave the public repo by design.
5. **Whether `mixed` is an acceptable manifest class**, or whether the manifest waits for the inversion.
6. **Whether `group`'s double-booking (VOCABULARY §5) is renamed now** — step 3 is the seam that was
   predicted to bite; I did not decide the migration.
7. **Whether the API contract is frozen** as §1's design constraint. Wanting an estate coordinate on
   the API surface later is a rule-3 conversation and changes 0b's cost from zero.

## §8 · OPEN QUESTIONS

1. Is a **second contributor at Fernwood** (not at a second estate) foreseeable — the case no key
   prefix fixes and only a `personId` on the record does?
2. Does `estate.json` hold **only** ids and the module set, or also the thresholds §2c classes as
   **C-edge** — which belong to the *grant*, not the estate?
3. When `attributionIsValidFrom` says *"usable-with-a-caveat from 2026-07-13,"* does a `personId`
   stamp write the id or null for records inside that window?
4. Should `check-domains.py`'s `NON_DOMAINS` table become the manifest's config/instance classifier,
   given it is already doing half of §4's job?
5. Does the permanent 🔴 on the six markerless wildlife domains clear under a module declaration, or
   does it need `markers` before an OFF state can honestly quiet it?
6. Is `worker/digest.json` **engine-built config** or an **instance artifact** — it carries the
   coordinate pair and is bundled at deploy, so its class decides who owns its drift alarm?
7. Does `frostDates.atPropertyElevation.firstFallRiskBegins` (**zero consumers**) want one, or should
   canon drop it — a field nothing reads is a claim nothing checks?
8. Should the config lint's roster be **hand-declared** or **derived from `property.json`'s leaf
   values** — derivation is drift-proof but would flag every incidental number in the repo?
