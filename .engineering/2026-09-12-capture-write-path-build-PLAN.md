# BUILD PLAN · capture-write-path steps 1–4

- role: **engineering-partner / BUILD EXPERT audit** — the plan audit that precedes the build window
  (`[paul-stated 2026-09-10]`: *engineering-partner writes a distinct detailed build plan the build lane executes*).
- subject: `.plans/2026-09-07-capture-write-path-PLAN.md` — DESIGN PASS 2026-09-12 + §1, §3, §4, Falsifier, QA
- repo state when audited: **HEAD `45aae0c9`**, branch `main`, clean but for two untracked files.
  ⚠️ The brief cited `05f42bfb`; the standing backlog window committed `45aae0c9` on top of it at 15:36 ET.
  Nothing in `45aae0c9` touches `worker/`, `engine/` or `tools/` — every citation below was re-read at `45aae0c9`.
- ⛔ **NO FEATURE CODE WAS WRITTEN.** This session wrote this one file. No deploy, no merge, no push,
  no `BACKLOG.md` edit, no edit to the plan.
- mode: path-evaluation producing an ordered, independently-landable build sequence.

---

## ⭐⭐ READ THIS FIRST — three corrections to the design pass, ordered by consequence

The design pass is good work and most of it survives. These three are load-bearing and a build lane
that took the plan literally would ship a defect on each.

### ① ⛔ "Demote git to a **write-only mirror**" IS NOT ACHIEVABLE, and taking it literally FAILS FALSIFIER 3

The GitHub Contents API does not have a write-only update. `ghPutFile` (`worker/worker.js:3276`–:3292)
passes `sha` into the PUT body, and it gets that sha from the git READ at `:5089`
(`ghPutFile(env, "zones.json", …, existingZones.sha)` — `:5155`). A Contents PUT against a path that
already exists **without** its blob sha is rejected by GitHub, not accepted. The second commit is worse:
`:5158`'s `ghGetFile(env, "viewer.html")` is not fetched for a sha, it is fetched for the **file body** —
`:5165` does a regex replace on `viewerFile.contentText`. There is no version of that commit that does
not read first.

> ### ⭐ THE CORRECTED SHAPE
> Git is a **read-then-write mirror, held entirely behind the token guard** — not a write-only one.
> Both `ghGetFile` calls STAY; they move *down*, inside `if (gitOk)`, below the KV write.
> What step 1 actually removes from the household path is **the git read that supplies `_meta`**
> (`:5089` → `existingData` → `meta` at `:5102`) — and it removes it by giving `_meta` a different
> source, not by deleting the call.

**Why this matters more than it reads:** falsifier 3 is the one that protects Mom, and its test is
*"the same two commits and the same response before and after."* A git half rebuilt as write-only
produces **zero** commits at the frozen env, on the first save after deploy, silently — because the
PUT fails and (today) the throw is unhandled after the KV write already landed. The plan's own words
would have produced the exact failure its own falsifier exists to catch.

### ② ⛔ "The client already sends `_meta`" IS FALSE AT HEAD — the CAS has no round trip, and `stale-client` is DEAD CODE

Design pass §C2: *"the client already sends `_meta`, so the round trip exists and needs no new field,
no new state and no new store."* Measured at `45aae0c9`:

- `syncZonesNow`'s payload is exactly three keys — `{ zones, _deleted, deviceId }`
  (`engine/viewer.template.html:14252`–:14256).
- `syncZonesOnUnload`'s is two — `{ zones, _deleted }` (`:14297`–:14302).
- `grep -n "_meta"` over `engine/viewer.template.html` lines 13900–14450 returns **zero hits**.
- `refreshZonesFromCloud` adopts `cloud.zones` and `cloud._deleted` (`:14388`–:14389) and **never reads
  `cloud._meta`** — so the inbound half is dropped too. The client has no place to keep a version.

**Therefore the `stale-client` 409 at `worker.js:5107`–:5117 has never fired for the shipped viewer.**
`body._meta` is undefined → `clientSchema === undefined` → the `if` short-circuits on its first clause.
It was written to police the schema-v2→v3 move and was inert for the whole of it.

⭐ This is the second instrument in this file's blast radius that **reads as coverage and covers
nothing** (the first is `check-data-inline.py`, named in `sanitizeZone`'s own comment at `:5006`–:5008).
It is worth recording as a class, not an incident.

**Consequence for the build:** the CAS is **not cheap and not server-only.** It needs a client change in
`engine/viewer.template.html` — the file the plan itself marks *"NOT this session — the file is
uncommitted under another live lane"* — and it must ship **client first, server second, with a deploy
between**. Full treatment in **B3**, which I recommend does **not** ride with B1.

### ③ ⚠️ STEP 4's `build-digest.py` HALF IS ALREADY DONE — and a DIFFERENT failure is live

Plan step 4: *"`build-digest.py`'s unguarded `load()`… absent-aware `load()`."* Measured at HEAD:

- `_compose_all` is already thunk-based and only calls a claimed section's loader
  (`tools/build-digest.py:303`–:341, with the 2026-09-10 finding in its own docstring:
  *"a module that is OFF now costs no file, not merely no key"*).
- `canon_loader(canon_dir, materialise_empty=not strict)` (`:593`–:601) already materialises `{}` for a
  young canon and stays strict for Fernwood's.
- The core floor was already ruled **non-fatal for a young estate** `[paul-ruled 2026-09-10]` (`main()`,
  the comment above `assert_core_floor`).
- `CORE_INCLUDES` is already guarded — `for k in CORE_INCLUDES if k in digest` (`:562`).
- The selftest already carries the near-empty-estate case (`:820`–:825).

**RUN, not read** — `python3 tools/build-digest.py --estate home --out <scratch>` at `45aae0c9`:

```
RuntimeError: property.json holds neither an address nor an elevation —
refusing to derive a core with no place in it
```
…raised at `tools/build-digest.py:451`, because `instance/neutral-canon/` holds two files and its
`property.json` declares neither an address nor an elevation.

**That is not a zones defect and it is not on this plan's critical path.** It blocks building a
household *digest* — Guru's substrate — and has nothing to do with the zone write path. **Route it as
its own row with the measurement attached.** Folding it into step 4 would have had the build lane
"fix" a loader that is not broken and never reach the guard that is.

---

## THE BUILD SEQUENCE

Every step is independently landable and independently verifiable. **B0 must be first** — it is the
instrument every later step proves itself with, and its baseline must be captured before any handler
is touched.

| # | step | plan step | size | lands alone? |
|---|---|---|---|---|
| **B0** | The replay harness + the frozen-env baseline transcripts | (falsifier 3's instrument) | **S** | ✅ |
| **B1** | `handleZoneSave` — KV as prior state, git behind the guard, honest error paths, `zones:prev` | 1 | **M** | ✅ |
| **B4** | `ZONES_GIT_FALLBACK` + the four `wrangler.toml` comments | 2, 3 | **XS** | ✅ |
| **B5** | `check-zones-containment.py` — asserts via `/health` | 4 (first half) | **S** | ✅ |
| **B6** | Route the `build-digest.py` finding; no code | 4 (second half) | **XS** | ✅ |
| — | **B3** the compare-and-swap | 3 (design pass §C2) | **M+** | ⛔ own row — see B3 |
| — | **B7** the per-estate vertex envelope | (§3's named literal) | **S** | ⛔ own row — pairs with §5 |
| — | **B8** `tateTracker.zones.*` per-estate | (routed by ux-expert) | **XS** | ⛔ own row — see B8 |

---

## B0 · THE REPLAY HARNESS — and how falsifier 3 gets proved without deploying to the frozen env

**This is the answer to the brief's question 5, and it is the reason B0 is first.**

`worker/worker.js` is already a valid ES module that imports cleanly in node — proven, not assumed:
`tools/guru-replay.mjs:6` does `import { dispatchTool, CORE_TOOLS, … } from "../worker/worker.js"`, and
the named-export line at `worker.js:4185` sits beside the `export default { fetch }` at `:4187` on a
file the frozen deployment is running today. **So adding `handleZoneSave` and `handleZonesGet` to that
export line is deploy-neutral**: extra named exports beside the default fetch handler are already
shipped and already live.

**Build `tools/zone-save-replay.mjs`:**

1. **Stub `env`** — `{ GITHUB_TOKEN, GITHUB_REPO, GITHUB_BRANCH, ESTATE_ID, LEGACY_BEFORE,
   OBSERVATIONS: { get, put } }`. `legacyBefore()` THROWS on a missing/malformed `LEGACY_BEFORE`
   (`worker.js:1124`–:1129), so the stub must carry it or the harness fails for the wrong reason.
2. **Stub `globalThis.fetch`** with a recorder returning canned GitHub Contents responses built from
   the repo's **own** artifacts — real `zones.json`, and a `viewer.html` stub carrying a literal
   `const ZONES_DATA = {…};` so the regex at `:5163` has something true to match. Do not invent shapes;
   `ghGetFile` base64-decodes `data.content` (`:3270`–:3272) and a hand-rolled fixture that skips that
   is testing the harness, not the handler.
3. **Two arms.** `token` = the frozen shape (`ESTATE_ID=est-3c9f1a`, both GitHub vars set).
   `no-token` = the household shape (`ESTATE_ID=est-e6696a`, both absent).
4. **Emit a transcript**, not a boolean: ordered `[method, url, sha256(body)]` for every `fetch`,
   ordered `[key, sha256(value)]` for every `OBSERVATIONS.put`, then `[status, responseBody]`.
   A boolean assertion cannot answer *"the same two commits"*; a transcript can.
5. ⚠️ **Normalise the clock or the diff never stabilises.** `meta.lastBuilt` / `meta.lastBuiltAt` are
   `new Date().toISOString()` (`:5103`, `:5119`–:5120) and ride into both the response and the committed
   bodies. Replace every ISO-8601 match in the transcript with `<ISO>` before diffing. **This is the
   detail that makes a build lane abandon the harness at hour two** — spend the ten minutes.
6. **Capture the baselines AT HEAD, BEFORE B1 touches the handler.** Commit them as
   `tools/fixtures/zone-save-token-baseline.txt` and `…-no-token-baseline.txt`.

**Acceptance (B0):**
- `node tools/zone-save-replay.mjs --arm token` at HEAD prints exactly four GitHub calls, in order:
  `GET …/contents/zones.json`, `PUT …/contents/zones.json`, `GET …/contents/viewer.html`,
  `PUT …/contents/viewer.html`; one `OBSERVATIONS.put` to `est-3c9f1a:zones:all`; one to
  `est-3c9f1a:zones-last-seen:<id>`; response `{ok:true, zoneCount, tombstoneCount, lastBuilt, lastBuiltAt}`.
- `--arm no-token` at HEAD prints **zero** fetches, **zero** puts, and `503 {"error":"github-not-configured"}`.
- `--selftest` proves a deliberately altered transcript FAILS the diff. (House style — `check-storage-keys.py:157`,
  `post-deploy.py:301`+ both do this; a check that has never been seen to fail is not a check.)

> ### ⛔ WHAT THE HARNESS CANNOT PROVE — state it in the tool's own banner
> That the **deployed** frozen Worker is running this source. Re-verified live today:
> `GET https://fernwood.paul-kirschenbauer.workers.dev/health` returns **`build_sha: null`** and
> **`worker_blob: null`**. The frozen deployment is unstamped. The Worker's own comment at
> `worker.js:4213`–:4215 already rules on this: *"Null is UNKNOWN, and nothing downstream may read
> unknown as a pass."* So a green harness is evidence about **the file at HEAD**, and the gap between
> the file and the frozen deployment is **open and unmeasurable today**. Do not let it be reported as
> falsifier-3-discharged without that sentence attached.

---

## B1 · `handleZoneSave` — the reshaped step 1

**Files:** `worker/worker.js` only (`handleZoneSave`, `:5048`–:5181; plus the export line at `:4185`).
**No client change. No response-shape change. No new response keys.**

### The exact sequence

| # | what | notes |
|---|---|---|
| 1 | `if (request.method !== "POST") return 405` | unchanged (`:5049`) |
| 2 | **`const gitOk = !!(env.GITHUB_TOKEN && env.GITHUB_REPO);`** | replaces the early 503 at `:5050`–:5052. Same predicate `/health:4231` publishes. |
| 3 | parse · `missing-zones-array` · `sanitizeZone` · `invalid-zones` | **unchanged**, `:5054`–:5084 |
| 4 | tombstones | unchanged, `:5085`–:5087 |
| 5 | **read prior state from KV** — `keyFor(scopeOf(env), "zones", "all")` | replaces the git read at `:5089`. Three outcomes — see below. |
| 6 | **resolve `_meta`** | see **B2**. Replaces `existingData._meta` at `:5102`. |
| 7 | `stale-client` schema guard | **leave exactly as-is.** It is inert (correction ②) and B1 is not the place to arm it. |
| 8 | `meta.lastBuilt` / `meta.lastBuiltAt` | unchanged, `:5119`–:5120 |
| 9 | **`zones:prev`** — write the prior value before overwriting | NEW. One `put`. See below. |
| 10 | **KV write** — `keyFor(scopeOf(env), "zones", "all")` | `:5132`. **Stops being non-fatal** — see below. |
| 11 | device stamp | unchanged, `:5141`–:5150 |
| 12 | **`if (gitOk) { … }`** wrapping `ghGetFile` zones.json → `ghPutFile` zones.json → `ghGetFile` viewer.html → `ghPutFile` viewer.html | `:5152`–:5170, moved down and guarded. **Both reads stay** (correction ①). Whole block in a `try/catch`. |
| 13 | response | **byte-identical shape to today** — `{ok, zoneCount, tombstoneCount, lastBuilt, lastBuiltAt}` |

### Step 5 in detail — the KV read, and what replaces "git is still canon"

Three outcomes, and only the first two proceed:

- **`get()` returns `null`** → no prior record. **Legitimate — this is a household's first save.** `prior = null`.
- **`get()` returns a string that parses** → `prior = parsed`.
- **`get()` throws, OR returns a non-null string that does not parse** → ⛔ **REFUSE. `503
  {"error":"zones-store-unreadable"}`. Nothing written, no git touched.**

**The *why*, and it is the whole shape of this step.** The handler's own comment at `:5122` is
*"ALL-OR-NOTHING. The sanitized array below becomes the ENTIRE file."* A write built on a prior state
you could not read is not a partial write — it is a **blind whole-record replacement**. Today that is
survivable because git holds a copy and `git revert` exists. **B1 is the commit that removes `git
revert` from the household path**, so the read failing must stop being something you shrug at. A
null and a throw look identical downstream and mean opposite things: *"you have nothing yet"* versus
*"I cannot see what you have."* Treating them the same is the `capture must not lie` family the
`validVertex` comment at `:4923`–:4935 already names as three-deep in this repo.

> **The sentence that replaces the `:5134` comment**, verbatim, for the build lane to paste:
> ```
> // KV IS CANON. The comment that used to sit here — "KV write failure is non-fatal, git is still
> // canon" — stopped being true the moment a household could save: at a household there is no git,
> // so this put IS the record. A swallowed failure here reports success for a write that went
> // nowhere, which is the 2026-07-15 capture-loss shape and the third in that family.
> ```

### Step 9 in detail — `zones:prev`, and why it belongs in B1 rather than waiting for B3

The concept proposed it; the design pass dropped it in favour of the CAS. **Take both, in that order.**
The CAS (B3) is blocked on a client deploy and two seat returns; `zones:prev` is three lines, needs no
client, and is the only thing standing between a bad whole-record save and a permanent loss in the
window between B1 and B3.

- Before the put at step 10, if `prior !== null`, `put(keyFor(scopeOf(env), "zones", "prev"), priorRaw)`.
  Write the **raw string**, not a re-serialised object — a re-serialisation is a second sanitiser pass
  and `sanitizeZone`'s own comment (`:4990`–:5010) is a 20-line account of a fixed key list silently
  deleting schema fields. The undo copy must be the bytes, unexamined.
- One undo deep, and **it must not be called versioning**, in the code or in the backlog row.
  A second bad save consumes it.
- ⓘ `zones:prev` is a new KV *kind*. `tools/household-export.py` derives its kind roster from the
  Worker's call sites and `check-household-isolation.py` reuses that derived roster
  (`check-household-isolation.py:29`–:36, *"an instrument's scope must come from whatever declares
  reality"*), so the new kind is picked up automatically. Confirm it appears in an export run; do not
  hand-add it anywhere.

### Step 10 in detail — the KV write stops being swallowed

Today `:5133`–:5136 catches and `console.warn`s, then returns `{ok:true}`. After B1 that is a lie at a
household. **Recommended: throw-to-500 in BOTH arms** — `500 {"error":"zones-write-failed"}`, before
any git work.

⚠️ **This is a behaviour change at the frozen env, and it needs to be said rather than discovered.**
It is confined to a path that the happy-path transcript does not exercise, so **falsifier 3's diff
stays empty** — but a KV failure at the frozen env today still commits to git and returns `ok:true`,
and after B1 it would 500. The conservative alternative (fatal only when `!gitOk`) is written out in
the rulings section. My recommendation is both arms: *"git is still canon"* is precisely the belief
this plan retires, and leaving it live in one env leaves a second story about which store is real.

### Step 12 in detail — the git mirror's failure modes stop being the caller's problem

Three returns inside today's git half fire **after** the KV write has already succeeded:

- `:5159`–:5161 `return json({error:"viewer-html-missing"}, 500)`
- `:5166`–:5168 `return json({error:"zones-const-not-found-in-viewer"}, 500)`
- an unhandled throw from either `ghPutFile` (`:3286`–:3289 throws on any non-ok)

Each one tells a client that a save failed when the record already has it. Today that is nearly
harmless because git is canon; after B1 it is the same lie in the other direction. **Wrap the whole
`if (gitOk)` block in `try/catch`, log, and fall through to the normal 200.** The mirror failing is
an operator concern, not a resident's.

⛔ **What B1 must NOT do:** report *which* store persisted in the response. `persisted: "kv" | "kv+git"`
is plan **step 5**, its surface is Mom-facing, and its two seats have already been convened and have
already refuted one of that step's premises. Adding a key to this response body also puts a diff in
falsifier 3's transcript. **Do not bundle it.**

### Acceptance (B1)

1. `node tools/zone-save-replay.mjs --arm token` diffs **empty** against `zone-save-token-baseline.txt`.
   ⭐ *This is falsifier 3, discharged at the file level, with B0's caveat about the unstamped deployment attached.*
2. `--arm no-token`: zero `fetch` calls; puts to `est-e6696a:zones:all` **only** (no `zones:prev` on a
   first save, since `prior === null`); `200 {ok:true, zoneCount:N, …}`.
3. `--arm no-token` with a seeded prior record: puts to `zones:prev` **then** `zones:all`, in that order,
   and `zones:prev` holds the prior bytes verbatim.
4. `--arm no-token` with `OBSERVATIONS.get` throwing → `503 zones-store-unreadable`, **zero puts**.
5. `--arm no-token` with `OBSERVATIONS.put` throwing → `500 zones-write-failed`.
6. `--arm token` with `ghPutFile` throwing → `200`, KV put present, error logged. *(New behaviour; assert it explicitly.)*
7. `python3 tools/check-engine-manifest.py` · `python3 tools/check-vocabulary.py` — both clean.
8. Live, **at `qa` only** (`lab` cannot answer — no `SHARED_TOKEN`, so every request there is
   `unauthorized` before the gate): after deploying B1 to qa, `POST /api/zone-save` with a
   one-named-place-no-geometry body returns 200, and `GET /api/zones` returns that one place.
   ⚠️ **This spends a real row in `est-qa0001`** — the namespace the design pass declined to pollute.
   One zones record is not five unprovable account rows and it is the record under test, but it is
   still a write to a namespace whose `--teardown` refuses by design. **Paul's call — ruling R4 below.**

**Size: M.** The design pass moved XS→S; the git-read retention, the three-way read outcome, the four
error-path re-rulings and `zones:prev` move it again. Most of the cost is in getting the error paths
right, not in the happy path.

---

## B2 · ⭐ THE `_meta` RULING — the brief's question 2, answered rather than deferred

> ### THE RULING
> **A household's `_meta` is SERVER-MINTED and carries only what the server can know without a
> basemap.** Resolution order, replacing `const meta = existingData._meta || {}` at `:5102`:
>
> 1. **the prior record's `_meta` from KV**, if a prior record exists — this is what carries a
>    georeference forward once one exists, and it is what makes the frozen env's behaviour unchanged;
> 2. **`schemaVersion`**, seeded from a single engine constant when the prior record carries none;
> 3. **`lastBuilt` / `lastBuiltAt`**, stamped every save (unchanged, `:5119`–:5120).
>
> The client's `_meta` is **still never adopted** — the comment at `:5093`–`:5099` (*"THE SERVER OWNS
> `_meta`"*) stands unweakened and its stated reason (a stale cached viewer writing v1 bounds back over
> the georeference) is untouched by this change.
>
> ⛔ **The georeference keys stay ABSENT, never defaulted.** No `bounds: null`, no zeroed
> `baseImageWidth`. A null `bounds` reaching `ZoneGeo.lonLatToFrac` (`viewer.template.html:10791`–:10796)
> returns `[0, 0]` for **every** vertex — which paints every zone in the image corner. That is the exact
> 2026-07-16 defect the `validVertex` comment at `worker.js:4923`–:4935 was written about. An absent key
> renders nothing; a defaulted key renders a lie.

### Why `schemaVersion` must be seeded and not left empty

`meta.schemaVersion` is `3` at Fernwood (`zones.json` `_meta`). At a household with `meta = {}` it is
`undefined`, and the `stale-client` guard at `:5107`–:5109 requires `meta.schemaVersion !== undefined`
to fire. So an unseeded household is **structurally exempt** from the one version check the handler has.
Seed it from a named constant in `worker.js` (`const ZONES_SCHEMA_VERSION = 3;`) and pin it with a
one-line assertion in B5 that it equals `zones.json`'s `_meta.schemaVersion` at the frozen canon.

⭐ *The why, and it cuts against §3's own rule:* §3 says *"a constant that is true of exactly one
instance belongs in that instance's declaration, not in the engine."* `schemaVersion` is the
**opposite** — it is true of the CODE, not of any estate, so the engine is its right home. The rule
that generalises both is **a constant belongs wherever the thing it describes lives**, and the pin is
what stops the engine's copy and the canon's copy drifting.

### What an empty georeference costs — measured, not reasoned

| consumer | behaviour with `_meta` carrying no basemap | verdict |
|---|---|---|
| `renderPropertyMap` (`viewer.template.html:10861`) | `if (!meta.baseImage && !meta.baseImageFallbackPng) return '';` → **no map section renders** | ✅ intended `[paul-stated 2026-09-04: "better to not display something rather than display something that's empty"]` |
| every `ZoneGeo.*` call — `:10862`, `:10863`, `:10870`, `:10871`, `:10884`, `:10899`, `:10959`, `:11161`, `:11199` | **all nine are downstream of that `return ''`** and are never reached | ✅ verified by enumeration, not inspection |
| `ZoneGeo.FALLBACK_IMG` (Fernwood's path, typed in the engine) | resolves to `""` at a household — `PROPERTY_IMAGE_WEBP` is instance-derived (`:7512`) | ✅ no cross-estate image leak |
| ZoneJourney zone card (`:13880`–:13883) | the oriented mini-map is **deferred by comment**; name + swatch + mic + nav only | ✅ no dependency |
| `handleZonesSyncStatus` (`:5290`) | reads `_meta.lastBuiltAt` only — which B1 always stamps | ✅ |

**So: a household's zones are a NAMED LIST WITH NO MAP, and that is exactly ruling Z-10's
define-zones-first state.** `sanitizeZone:4957` already blesses it in its own words — *"An EMPTY vertex
list is valid: a named place that has no boundary drawn yet… It must round-trip."*

### ⛔ THE ONE THING THAT DOES NOT SURVIVE — `validVertex`, and it needs Paul (ruling R5)

`validVertex` (`worker.js:4936`–:4943) applies **Fernwood's** envelope — `ZONE_LON_MIN/MAX = -84.40 /
-84.33`, `ZONE_LAT_MIN/MAX = 34.52 / 34.58` (`:4920`–:4921) — to **every estate**. Its own comment calls
that box *"the property's neighbourhood, generously padded"*, which §3 already flags as a single-estate
sentence in a multi-estate function.

The household on `est-e6696a` is **a Midtown Atlanta condo**. Its latitude is roughly 0.8° south of
that band. Concretely: **every vertex from that place fails `validVertex` → `sanitizeZone` returns
`null` → the all-or-nothing check refuses the ENTIRE save with `400 invalid-zones`** and a hint reading
*"within the property envelope"* — a sentence that cannot be acted on, because the envelope named is
not that estate's.

**Is it reachable? Two answers, and they are different:**
- ⛔ **Not through the app today.** Drawing requires the map stage; the map requires a basemap; §5 defers
  the basemap. **The envelope gate and the basemap gate open together** — which is why `_meta` being
  empty is *safe* rather than merely *tolerable*: the same absence closes both halves.
- ⚠️ **Yes, out-of-band.** `tools/kml-to-zones.py:184` refuses on the same envelope, and an operator
  importing a KML traced over the condo hits it before any of this. That is an operator path, not a
  household one, but it is live today.

**Recommended shape (for the row, not this build):** the envelope becomes a **declared per-env var** —
`ZONE_ENVELOPE = "<west>,<south>,<east>,<north>"` — the same greppable, manifest-checkable shape B4
uses for `ZONES_GIT_FALLBACK`, for the same reason §3 gives. ⛔ **And it fails CLOSED**: an env that
declares no envelope accepts **no** vertices, rather than accepting all. *"REJECT, never clamp"*
(`:4923`) becomes *"reject, never widen."* A household that has declared no ground can name places and
cannot draw them, which is the honest state and is already today's effective behaviour.

**B7. Its own row. It pairs with §5's basemap deferral and should be lifted in the same lap as it.**

---

## B3 · THE COMPARE-AND-SWAP — assessed as asked, and I recommend it does NOT ride with B1

The brief asks four questions. Answering each:

### Is the recommended shape correct?
**The server half, yes.** Extending the existing `stale-client` 409 rather than minting a new mechanism
is right: it reuses a shaped error, a named reason and a written rule (*"A stale client is a rejected
write, not a silent downgrade"*), and it needs no new store.

**The premise it rests on, no** — see correction ②. The client sends no `_meta` and keeps no version, so
the round trip does not exist and the existing guard has never fired.

### Is it sufficient?
**Yes, for the failure it names — with one correction.** `lastBuiltAt` is a server-minted ISO string
stamped on every save, so it is a usable version token. The guard must handle **three** cases and only
the middle one is a conflict:

| client sends | prior record | verdict |
|---|---|---|
| no version | none | **accept** — a household's first save, the normal case |
| no version | exists | ⛔ **refuse** — this is the blind overwrite, and **it is today's shipped client** |
| a version ≠ server's | exists | ⛔ **refuse `409 stale-zones`**, response carries the server's `lastBuiltAt` + zone count |

Row 2 is why **B3 cannot ship server-first**: turning the refusal on before the new viewer is in the
field 409s every save from every device. **Client first, server second, with a deploy between.**

### Does it break the legacy env?
⛔ **Yes, outright, if shipped naively.** The frozen Fernwood serves a frozen viewer that also sends no
`_meta`, and its KV holds a prior record — row 2 of the table. Every save there would 409.
**That fails falsifier 3.** Two ways out:

- **(a) a declared per-env switch** — `ZONES_CAS`, and it is **default ON**, with the frozen env alone
  declaring `"off"` in top-level `[vars]`. ⭐ Note this **inverts** B4's default-OFF rule, and the
  inversion is principled: B4's switch guards a **leak** (off = safe), this one guards a **destructive
  write** (on = safe). The rule is not *"default OFF"* — it is **"default to the state that fails
  safe,"** and which literal that is depends on what the switch guards. *(Proposed as a principle below.)*
- **(b) refuse only on an explicit mismatch**, accept a missing version. No new var, cheaper — and it
  leaves the hole open for exactly the client that has it, which is the entire reason the CAS exists.

**I recommend (a).**

### What does the client do on a 409?
**The mechanism is mine; the surface is not.**

Mechanically it **must not retry**. Today `syncZonesNow`'s catch sets `failed` (`:14282`) and the boot
retry at `:14403`–:14417 re-POSTs the same stale payload on every load — an **infinite 409 loop** that
would also keep the resident's only visible chip state permanently red. So: stop the retry on 409,
**keep the local edit** (already safe — `persistAndRerender` writes `ZONE_STORE_KEY` at `:14019` before
the sync is scheduled, so nothing is lost), re-read canon, and surface a state that says somebody else
changed this.

⛔ **It must never silently adopt canon and discard her edit, and never silently overwrite.** That is a
**merge** decision and a merge decision belongs to a person. Which means the 409 needs a *surface* —
and that is step 5's territory, whose ux-expert and content-steward returns **have not been asked for
this state**. Route it; do not let the build lane invent a sentence.

### ⚠️ Is the hazard live or scheduled? — partially unverified, stated as such
The design pass frames multi-writer as arriving with step 6. Two things at HEAD suggest it is closer:
`handleZoneSave` writes **one** `zones:all` key per estate (`keyFor(scopeOf(env), "zones", "all")`,
`:5132`), and `worker.js:4853`–:4856 records that `est-e6696a` holds **two people's records on one
estate**. But `/api/zone-save` is `ADMIN_ONLY` (`:4847`), so the hazard needs **two administrators on
one estate** — and **I did not read the account rows and cannot say whether that holds today.**
⛔ Unverified. Worth one query before B3 is sized.

### ⭐ THE DISPOSITION
**B3 is its own row, sized M+**, blocked on: a viewer change in a file under another live lane · a
client-then-server deploy sequence · two seat returns for the 409 surface.

**But B1 must not ship without the hazard written into the record**, because B1 is what removes
`git revert` as the recovery. Two concrete obligations on B1:
- `zones:prev` ships **in B1** (step 9 above) — the cheap, client-free, one-undo-deep mitigation.
- B1's commit message and its backlog row state plainly: *zone-save is whole-record last-write-wins
  with one undo and no merge at a household until B3 lands.*

---

## B4 · THE DECLARED SWITCH AND THE COMMENTS — plan steps 2 and 3

**Files:** `worker/worker.js` (`handleZonesGet:5259`), `worker/wrangler.toml`.

- `handleZonesGet:5259` becomes
  `if (env.ZONES_GIT_FALLBACK === "true" && env.GITHUB_TOKEN && env.GITHUB_REPO) {`.
  **Keep the token clause** — two independent gates, and putting the cheap string compare first
  short-circuits before the secret read.
- `ZONES_GIT_FALLBACK = "true"` goes in **top-level `[vars]` only** (the frozen env's block, `wrangler.toml:24`–:37).
  Vars do not inherit into `[env.*]`, so every other deployment — and every deployment added tomorrow —
  gets the fallback OFF without anyone remembering to write anything. **Allow-list, never exclude-list**,
  which is the rule this file already states about `CANON_FOREIGN_OK` at `:55`–:58.
- **Write the missing ⛔ comments.** Measured at HEAD: the ruling exists at `:66` (lab) and `:146` (home)
  **only**; `[env.qa]` (`:42`) and `[env.paul]` (`:202`) carry none. And **all four must name zones** —
  the two that exist explain only the species half (*"a token here would promote species onto Mom's live
  branch"*). Add: *…and this deployment's zone saves would commit to Fernwood's repo.*
- ⛔ **Say what the comment cannot do, in the comment.** Re-verified: `GITHUB_TOKEN` appears in
  `wrangler.toml` **twice, both times inside a `⛔` comment, and zero times as a var assignment**
  (`grep -c "^GITHUB_TOKEN\s*=" → 0`). It is a *secret*. A comment does not survive `wrangler secret put`.
  *(The design pass said "zero times" — right on substance, off on the literal count. Corrected here so
  a build lane grepping for it isn't surprised into thinking the file changed.)*

**Acceptance (B4):**
- `grep -n ZONES_GIT_FALLBACK worker/wrangler.toml` → exactly one hit, above the `[env.*]` blocks.
- `python3 tools/check-engine-manifest.py` classifies the new var (QA list requires this — it is engine config).
- Replay harness `--arm no-token` against `handleZonesGet` with a seeded-but-absent KV and both GitHub
  vars set: returns `{zones: [], _meta: {}}`. *(Proves default-OFF without needing a sixth env — a cheaper
  and stronger form of falsifier 7 than provisioning one.)*
- ⚠️ **The QA list's two-estate assertion is stale.** It says *"run falsifier 7 against `home` and `bob`."*
  **`env.bob` was destroyed 2026-09-10** and survives only as a tombstone (`wrangler.toml:171`–:190;
  `post-deploy.py:35` carries the same ⚰️). Substitute `paul`. **Do not skip the two-estate form** — the
  plan's own §3 records that a single-estate green is how all three embedded-Fernwood-literal defects
  passed review.

**Size: XS.**

---

## B5 · THE CHECK — asserted via `/health`, per the design pass

**New: `tools/check-zones-containment.py`.** Structure it on `qa-write-probe.py`'s refuse-first shape
and `check-household-isolation.py`'s declare-the-unchecked banner (*"a suite that lists four tests and
silently runs one is how green-by-absence happens"*).

**Three assertions — one static, two live:**

1. **Static, no network.** Parse `worker/wrangler.toml`: `ZONES_GIT_FALLBACK` appears in **exactly one**
   block and that block is top-level `[vars]`. Any `[env.*]` declaring it → FAIL.
   Plus: `ZONES_SCHEMA_VERSION` in `worker.js` equals `zones.json`'s `_meta.schemaVersion` (B2's pin).
2. **Live, no token needed.** For every deployment, `GET /health` and assert `configured.github === false`
   for all but the frozen one. ⭐ **This is the assertion `wrangler.toml` cannot make** — the file does
   not contain the secret, and `/health:4231` publishes the identical predicate `handleZoneSave` gates on.
   ⛔ **Derive the URL roster, never type it** — import `worker_health()` from `tools/post-deploy.py:70`–:81
   (`ORIGIN` at `:33`–:35 already carries the bob tombstone). A second hand-typed roster is the drift this
   repo has paid for repeatedly.
   ⚠️ **Send a `User-Agent`.** Cloudflare's edge rejects UA-less `urllib` before the Worker runs; a
   403 here would read as a failed assertion about the Worker.
3. **Live, token-gated, and DECLARED UNCHECKABLE where the token is absent.** Where a token exists —
   prod (`.private/fernwood-token`) and qa (`.private/fernwood-token-qa`) — `GET /api/zones` and assert
   the non-frozen one returns `zones: []`. `home` and `paul` have **no local token**: report them
   **UNCHECKABLE by name**, never omitted and never a pass.
   ⓘ `GET /api/zones` **without** a `?d=` param is provably non-mutating — the device stamp at `:5271`–:5281
   is inside `if (deviceId && …)`. Do not pass `d`.

**Plus `--selftest`** proving each assertion can fail, per house style.

**Acceptance (B5):** the tool exits 0 at HEAD today; `--selftest` shows three red; the banner never reads
a bare ✅ while assertion 3 is partly unchecked.

**Size: S.**

⚠️ **Where it does NOT go:** `check-household-isolation.py` is deliberately **pure** — no network, no KV,
no deploy, *"so it runs on every commit and cannot be skipped because a token expired"* (its own
docstring). A live `/health` assertion inside it would break that property. New tool.

---

## B6 · ROUTE THE DIGEST FINDING — no code

Per correction ③. File a row carrying the measurement verbatim:

> `build-digest.py --estate home` raises `RuntimeError: property.json holds neither an address nor an
> elevation` at `tools/build-digest.py:451`; `instance/neutral-canon/property.json` declares neither.
> The absent-aware loader the plan asks for already shipped 2026-09-10 (`_compose_all` thunks, `:303`–:341;
> `canon_loader(materialise_empty=…)`, `:593`–:601). **The remaining blocker is the core-derivation guard,
> not the loader, and it is Guru-substrate work, not zone-write-path work.**

**Size: XS. This is a routing act; it is not a build step.**

---

## B8 · THE ROUTED STORAGE-KEYS ITEM — the brief's last question, ruled

> ### THE RULING: **its own row, XS — and the ux-expert note UNDERSTATES it.**

**Measured at HEAD.** `zones: "tateTracker.zones.v1"` and `zonesLastSyncedAt:
"tateTracker.zones.lastSyncedAt.v1"` are in `STORAGE_KEYS` (`viewer.template.html:7442`–:7443) and
**absent** from `STORAGE_KEYS_PER_ESTATE` (`:7450`, four `momQueue*` names). Used bare at `:11476`
(`ZONE_STORE_KEY`) and `:14040` (`ZONE_LAST_SYNCED_KEY`).

**It is not a shared cache. It is an automatic cross-estate WRITE.** Traced:
`loadZoneOverrides` reads `ZONE_STORE_KEY` into `ZONES_DATA.zones` at boot (`:13994`–:14002) → the boot
retry at `:14403`–:14417 finds `stored.savedAt > lastSynced` → calls `scheduleZoneSync()` → `syncZonesNow`
POSTs `ZONES_DATA.zones` to `/api/zone-save` (`:14252`–:14260). So on an origin serving two estates:
**edit at estate A, open estate B, and A's zones are written into B's record — with no user act beyond
opening the app.** The all-or-nothing write makes that a full replacement of B's record.

**Not reachable today**, and that is what makes it a row rather than a co-requisite: each deployment has
its own origin and localStorage is per-origin (`FAMILY_HOSTS` is one host per env — `wrangler.toml:37`,
`:53`, `:122`, `:165`, `:209`). It becomes reachable at the custom-domain / family-origin move, which the
comment at `:7450` already anticipates in exactly those words.

⛔ **But B1 is what arms it.** Today that stray POST 503s at a household. After B1 it succeeds.

**The fix is mechanical and the machinery already exists:** add both names to `STORAGE_KEYS_PER_ESTATE`,
wrap the two literals in `estateKey()` — and `carryOverEstateKeys()` (`:7455`–:7462) migrates existing
devices with **no extra code**. `check-storage-keys.py` then *enforces* it: `:96`–:109 fails on a bare
use of a per-estate key. **XS.**

**Why its own row and not folded into B1:** it touches `engine/viewer.template.html`, which is
uncommitted under another live lane; it is independently landable and independently verifiable; and
B1 has no dependency on it. **State the blocking condition on the row**: it must land before either
(a) a second estate is served from one origin, or (b) `zones` leaves any household's `absent` array on
a shared origin.

---

## OPEN RULINGS FOR PAUL

> ### ✅ DISPOSED 2026-09-12 — five of six are closed. Read this before the list below.
>
> ⛔ **Two were RULED BY PAUL. Three were TAKEN BY THE AGENT on the recommendation. Those are different
> kinds of thing and are never collapsed here.**
>
> | | disposition |
> |---|---|
> | **R3 · does the build window open now?** | ⭐ **PAUL RULED: NO — *after the design band actually clears.*** The band reads 3/2 and the honest split is **2 legitimately in design + 1 stale spec**: `.plans/2026-09-10-multi-tenancy-PLAN.md` leaves `design` when the lap-8 build plan's **P2 body half** lands (its header landed 09-11; its §"The four changes" did not). ⛔ **B0 does not start until then, no build exception is taken, and his 09-07 `concept`-stage stamp is NOT spent by this plan.** |
> | **R5 · nameable or drawable?** | ⭐ **PAUL RULED: NAMEABLE NOW, DRAWABLE LATER.** `validVertex`'s Fernwood envelope stays **its own row**, lifted in the same lap as §5's basemap deferral — the two gates open together. ⛔ **This build does NOT make a household's zones drawable.** Naming needs no basemap and no geometry (`sanitizeZone`: *"An EMPTY vertex list is valid"*). |
> | R1 · KV write failure fatal in both arms? | 🔵 **agent took the recommendation** — both arms, retiring *"git is still canon"* rather than leaving two durability models in one handler. |
> | R2 · `ZONES_CAS` default ON? | 🔵 **agent took the recommendation** — ON. *Default to the state that fails safe*; the asymmetry with `ZONES_GIT_FALLBACK` (default OFF) is the point — one guards a leak, the other a destructive write. |
> | R4 · spend one zones record in `est-qa0001`? | 🔵 **agent took the recommendation** — yes. One record **in the domain under test** is a different act from five unprovable account rows, and `qa` is the only non-frozen deployment where the gate is reachable. |
> | **R6 · the resident-facing noun for a zone edit** | ⛔ **STILL OPEN — Paul's.** Nothing here unblocks it; not needed until B3's 409 surface. |
>
> ⚠️ **The three 🔵 rows are agent judgement, reversible on his word, and must never be cited back as
> *"Paul decided."***

Format per the standing rule — question · recommendation · alternatives.

**R1 · Does a KV *write* failure 500 at the frozen env too, or only at a household?**
→ *Recommendation:* **both arms.** *"Git is still canon"* is the belief this plan retires; leaving it
live in one env keeps two stories about which store is real, and the divergence is confined to a path
the happy-path transcript never exercises, so falsifier 3 stays green.
→ *Alternative:* fatal only when `!gitOk`. Zero behaviour change at the frozen env, at the cost of one
handler holding two durability models.

**R2 · `ZONES_CAS` default ON (B3), when `ZONES_GIT_FALLBACK` is default OFF (B4)?**
→ *Recommendation:* **yes, and the inconsistency is the point.** B4's switch guards a leak (off = safe);
B3's guards a destructive write (on = safe). The rule is *default to the state that fails safe.*
→ *Alternative:* one uniform default-OFF rule. Simpler to state, and it hands every future env the
unsafe behaviour on the destructive-write switch.

**R3 · Does `ready: [paul-approved 2026-09-07]`, stamped against `concept`, authorise this build?**
→ *Not mine to recommend.* Carried forward unchanged from design pass §G1 because a build plan that
silently assumed it would be the thing that spent it.

**R4 · May B1's live verification spend one zones record in `est-qa0001`?**
→ *Recommendation:* **yes.** It is one record in the domain under test, not five unprovable account
rows, and `qa` is the only non-frozen deployment where the gate is reachable at all (`lab` holds no
`SHARED_TOKEN`). The alternative — the gate-kit route against `home` — is cleaner but couples B1's
verification to a gate-kit run.
→ *Alternative:* defer all live verification to the next gate kit. B1 then lands proved only at the
file level.

**R5 · `validVertex`'s Fernwood envelope (B7) — its own row, or blocking?**
→ *Recommendation:* **its own row, lifted in the same lap as §5's basemap deferral.** The two gates open
together and neither is reachable through the app before the other.
→ *Alternative:* fold it into this build. It is the only thing that makes a household's zones *drawable*
rather than merely *nameable*, so if the walk this build feeds is meant to include drawing, it is not
optional. **Paul's, because only he knows what the walk is for.**

**R6 · The resident-facing noun for a zone edit** — carried forward unchanged from design pass §G3 and
content-steward's open question. Unblocked by nothing here; B3's 409 surface will need it.

---

## HONEST SIZING

| step | size | why |
|---|---|---|
| B0 harness + baselines | **S** | ~half a day. The fetch stub and the clock normalisation are the whole cost. |
| B1 `handleZoneSave` | **M** | up from the design pass's S. The happy path is an hour; the four error-path rulings and their transcript assertions are the rest. |
| B4 switch + comments | **XS** | one line of handler, one var, four comments. |
| B5 the check | **S** | most of it is `--selftest` and the unchecked-declaration banner. |
| B6 routing | **XS** | no code. |
| **this build window** | **M–L** | B0 eats the front half and pays for itself at B1's first assertion. |
| B3 the CAS | **M+** | client + server + a deploy between + two seat returns. **Own row.** |
| B7 the envelope | **S** | mechanically small; the ruling and the fail-closed default are the work. **Own row.** |
| B8 storage keys | **XS** | two roster entries, two `estateKey()` wraps; the migration already exists. **Own row.** |

**The sequencing claim worth defending:** B0 before B1 looks like overhead and is not. Falsifier 3 is
the falsifier that protects Mom, the plan offers no way to run it without deploying to the frozen env,
and this audit found the one change (correction ①) that would have failed it silently. Without B0, B1's
only proof is a code read — which is exactly what the design pass was convened to stop relying on.

---

## WHAT I COULD NOT VERIFY

1. ⛔ **That the frozen deployment runs the source this plan edits.** Re-verified live today: its
   `/health` returns `build_sha: null` **and** `worker_blob: null`. The deployment is unstamped, so the
   file→deployment gap is open and unmeasurable. Every falsifier-3 claim here is about **the file at HEAD**.
2. ⚠️ **Whether `est-e6696a` has two administrators today.** `worker.js:4853`–:4856 records two people's
   records on one estate and `/api/zone-save` is `ADMIN_ONLY` (`:4847`), so the multi-writer condition
   needs two administrators. I did not read the account rows. It changes B3's urgency, not its shape.
3. ⚠️ **The frozen env's KV `_meta` versus git's `_meta`.** The design pass measured 18 zones in KV
   against 23 in git and did not chase it. I did not read the frozen KV either (it needs the prod token
   and I confined myself to unauthenticated reads). **B2's precedence order keeps `_meta` sourced from
   the prior record in both arms, so the frozen env's `_meta` still comes from the store it came from
   before** — but if that divergence extends to `_meta`, B1's token-arm transcript will show it as a diff
   on the committed body hash. ⭐ **Treat a non-empty diff there as this finding surfacing, not as a bug
   in B1**, and stop rather than patch.
4. ⚠️ **Live behaviour of the five non-zone capture endpoints** (falsifier 1's remaining half). Unchanged
   from the design pass: it is a gate-kit act against `home`, and nothing in this build plan depends on it.
5. **Read-only probes run from this session, all unauthenticated:** `GET /health` × 5 deployments
   (results identical to the design pass's table — `configured.github` true at the frozen deployment only);
   `python3 tools/build-digest.py --estate home --out <scratchpad>` (writes outside the repo).
   No writes to any KV namespace, no tracked file edited but this one.

---

## PRINCIPLES PROPOSED — not added; Paul's confirmation first

**① Default to the state that fails safe, not to OFF.**
*Statement:* A declared switch defaults to whichever literal is safe **for what that switch guards** —
OFF when it guards a leak, ON when it guards a destructive write.
*Why:* Came out of B3 vs B4 in this audit. "Default OFF" reads like a universal rule and is really a
rule about *leaks*; applied to a switch guarding a destructive write it hands every future environment
the unsafe behaviour by default. §3's *"it fails in the right direction"* is the real principle; "OFF"
was one instance of it.
*When it applies:* any new per-env `var` or feature flag.
*Avoid:* a uniform default, stated without naming what the switch guards.

**② A control that has never been observed to fire is not coverage.**
*Statement:* Before citing a guard as protection, show it firing — in a selftest, a fixture, or a log.
*Why:* `handleZoneSave`'s `stale-client` 409 (`worker.js:5107`) has been inert for its entire life
because the client never sends the field it reads. It is the second instrument in this blast radius to
read as coverage and cover nothing (`sanitizeZone`'s own comment names the first). This repo already has
the habit — `check-storage-keys.py:157` and `post-deploy.py:301`+ both prove their own failure modes —
it just is not applied to handler-level guards.
*When it applies:* any review that leans on an existing guard; any new guard.
*Avoid:* citing a code path as a protection on a read alone.

**③ Null and throw are different answers, and a store read must tell them apart.**
*Statement:* At a storage boundary, "there is nothing here" and "I could not look" must take different
branches. Never let an unreadable read degrade into an empty one.
*Why:* B1's KV read. With an all-or-nothing whole-record write downstream, collapsing the two turns an
unreadable store into a silent delete. This repo already states the rule for instruments —
`post-deploy.py:42`'s `Unreadable` exception, *"NEVER degraded to a pass"* — and this generalises it
from instruments to handlers.
*When it applies:* every read-modify-write against KV, a file, or an API.
*Avoid:* `catch (e) { data = null }` followed by a write.
