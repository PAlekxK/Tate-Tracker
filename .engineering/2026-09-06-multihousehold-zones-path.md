# Zones / map in ONE production environment — path evaluation

**Mode:** path-evaluation (engineering-partner). **Date:** 2026-09-06. **Status:** PROPOSAL — nothing
built, nothing deployed, nothing committed. No file in this repo was modified except this one.

**Question asked:** *what does zone/map capability have to become to work in one production
environment serving many households, and what is the cheapest honest path to a testable version?*

**Amended mid-session, twice**, and both amendments change the answer:
- ⭐ `[paul-ruled 2026-09-06]` **short term, WE draw and THEY confirm.** *"For the short term let's
  focus on you and I defining the zones and presenting them for confirmation."* Reasons stated:
  older/less tech-friendly readers, mobile drawing is hard, AI is ceilinged because it needs
  knowledge of the land.
- ⭐ Three `[paul-stated 2026-08-31]` rows still tagged IDEATION with no owner — **LAYERS**,
  **ONE GEOMETRY**, **THREE DATES** (`BACKLOG.md` 473–478). Tonight is meant to rule on them.

**Read for this:** `.plans/2026-09-06-one-environment-DECISIONS.md` · `worker/worker.js`
(`handleZoneSave` :3617, `handleZonesGet` :3815, `handleZonesSyncStatus` :3858, `handleZoneFeedback`
:3751, `handleZoneAudio` :1690, `validVertex`/`sanitizeZone` :3510–3586, `scopeOf`/`keyFor` :655–720,
`ghGetFile`/`ghPutFile` :2271–2330) · `worker/wrangler.toml` · `zones.json` · `viewer.html`
(:7394 `ZONES_DATA`, :13267–13620 the sync + hydrate path) · `ENGINE-MANIFEST.md` ·
`LAND-SOURCES.md` · `tools/fetch-basemap.py` · `tools/pages-deploy.py` ·
`tools/household-export.py` · `onboarding/index.html` · `.plans/2026-09-04-map-region-smoothing-PLAN.md`
§4/§4b · `momlib.DOMAINS` (executed, not read) · `~/.claude/engineering-principles/`.

**Context establishment.** Customer: two distinct people. (1) The **householder** — Mom today, Bob
next; older, reads with difficulty, on a phone, at a place with no cell reception. Their job is *see
my place and tell you when you got it wrong.* (2) The **operator** — Paul, on a laptop, in the
terminal. Their job is *turn an address into a map somebody else recognises.* Under the new ruling
these are now genuinely different products with different stakes, and most of the near-term work is
the operator's. Deployment context: `mom-ready` for the householder surface, `internal-only` for the
operator pipeline. Robustness: `shippable` for anything Mom or Bob touches, `working` for the
pipeline — but see B0, because "working" is not the same as "silently lossless."

`code_context_confidence: high` (everything below was read or executed).
`user_context_confidence: medium` — no `.user-research/` artifact covers a *second* household; the
only evidence of how a person names places is the 2026-08-30 session with Mom, n=1, and
`.plans/2026-09-04-map-region-smoothing-PLAN.md` §4b already flags the risk of designing it out.

---

## 0 · The one-paragraph answer

The **read** half is already multi-household and needs almost nothing. The **write** half persists
through a GitHub helper that **has no household concept and is outside the conversion entirely** —
which makes *"geometry stops living in a git repo"* a precondition for every path, not an option
among several (§3, §3b prices it). Under Paul's new ruling the write half **does not need to become
multi-household**, because the operator writes KV directly and the householder never writes geometry.
What the householder writes is a **confirmation**, which is not a save, and
which should ride the feedback machinery this repo has already hardened rather than the zone-save
path. The genuinely new engineering is a **per-household basemap**, and the genuinely new *product*
question is that the basemap is what makes this US-only. Two schema decisions (**geometry kind** and
**layers-with-dates**) are cheap today at 23 records and one household, and expensive later; take
them now. And there is a **live data-loss bug** in `sanitizeZone` that is destroying schema-v3 fields
on every zone edit right now — fix that before anything on this page.

---

## 1 · The blockers, ranked

### 🔴 B0 · `sanitizeZone` silently deletes `partOf` and `provenance` on every zone save — TODAY, at Fernwood

**Not a multi-household problem. It is losing data now, and nothing can see it.**

`sanitizeZone` (`worker.js:3537`) returns an object built from a **fixed key whitelist**: `id, name,
type, color, vertices, status, createdAt, createdBy, updatedAt, lastEditedBy, history`. Schema v3
shipped 2026-09-01 and added **`partOf`** — `the-green` carries `partOf: "the-turf"` plus a
`provenance` block. Neither key is in the whitelist.

The client posts the **whole zone set** on every edit (`viewer.html:13488`, `payload.zones =
ZONES_DATA.zones`), and the server rebuilds every zone from the whitelist and writes the result to
KV, to `zones.json`, and back into `viewer.html`'s `ZONES_DATA`. So:

> **The next rename, drag, or delete anyone makes on the map deletes `the-green.partOf` and its
> `provenance` block from canon, commits the deletion, and re-inlines it into the file Mom loads.**

`check-data-inline.py` cannot see it — the Worker writes both sides, so both are consistently
stripped and the drift check stays green. This is the **exact failure `_meta.fold_2026_08_31`
predicted** — *"the zone-save round-trip rebuilds `{_meta, zones}` wholesale and would silently drop
any other key, so lines stay in the plan file until a schema v3 adds them"* — except it came true one
key early, for the key that same schema bump added. The deferral named its own hazard, the hazard
fired on a different key, and nothing noticed.

**Why it matters at these stakes:** `partOf` is the only structural claim in the file that Paul
*stated* rather than derived (`GEOMETRY PROPOSES, PAUL RULES`). Losing it silently is losing a human
ruling to a whitelist.

**The right shape** is not "add `partOf` to the whitelist." A whitelist that must be widened by hand
every time the schema moves will fail again — this is its second escape already. The right shape is
**a round-trip assertion**: POST a zone carrying every key the current schema declares, GET it back,
assert deep-equal, and fail the test suite when a key does not survive. That is the same discipline
`test-feedback-cycle.py` applies to notes ("capture is not a loop"), applied to geometry.
**Effort: low.** Do it first.

---

### 🔴 B1 · THE GITHUB WRITE PATH HAS NO HOUSEHOLD IN IT — a class, not a zone bug

> ⭐ **Corrected and widened 2026-09-06 by the session that owns `worker.js`, and re-verified here.**
> My first draft said *"the zone handler is bound to one repo."* That was true and too small.

`ghPutFile` has **eight call sites** — `2672`, `2698`, `2746`, `2773` (species promotion: canon JSON,
`viewer.html` re-inline, photo, audio), `2833`, `2846` (species removal: canon JSON, `viewer.html`),
`3724`, `3738` (zones: `zones.json`, `viewer.html`). Every one takes its destination from
`env.GITHUB_REPO` + `env.GITHUB_BRANCH` — **Worker secrets, one value per script.** Not one of them
takes a scope, a grant, or an estate id.

> **The KV path is per-estate and converting. The GitHub path is per-*repo* and has no estate concept
> to convert. It is not BEHIND the conversion — it is OUTSIDE it.**

That reframing matters for three reasons, and it is a stronger statement than the zone one:

1. **It is not fixable by the conversion's mechanisms.** The conversion's inventory is the greppable
   `scopeOf(env)` roster (55 hits); the eight GitHub writes contribute **zero**, because their
   destination is not a KV key. Every hardening in `.plans/2026-09-06-one-environment-DECISIONS.md` —
   the attenuated KV handle, the type-split scope, `keyFor` throwing on a deployment scope —
   **operates on KV and is structurally blind to `ghPutFile`**. `2026-09-06-one-production-environment.md`
   mentions zones zero times, and would not be wrong to: zones are not the subject, the *helper* is.
2. **Zones are simply the first feature where a HOUSEHOLDER triggers it.** The six species sites are
   reached through Garden Guru's promote flow — an operator-shaped act today. The two zone sites are
   reached by a **map edit**, which is the first thing on this list a second household would do
   unprompted. That is why it surfaced here and not six months ago, and it is why the class should be
   named now rather than fixed one handler at a time.
3. **It has never been a tenancy question before, so nothing frames it as one.** `handleZoneSave` has
   no `scopeFor`, no grant read, no `estateId` comparison — not as an oversight, but because for its
   entire life there has been exactly one household and exactly one repo.

**⚠️ AND IT IS CONTAINED RIGHT NOW — precisely, and this is not a leak.** The `home` Worker reports
`"github": false` on `/health`; no GitHub credentials are bound to it, and the same holds for `bob`,
`paul`, `lab`. So **a second household saving a zone in production today does not write into
Fernwood's repo and does not re-inline Mom's `viewer.html` — it errors.** With Mom's instance frozen
as a deliberate data control, **erroring is the correct behaviour and is being left that way on
purpose.** Nothing here is an incident, and it should not be reported as one.

⛔ **What that containment IS, stated plainly: a CONFIGURATION property, not a structural one.** The
absence of a credential is the only thing between a stranger's zone save and Fernwood's repo, and it
evaporates the moment anyone binds GitHub credentials to a household Worker **for any reason at all**
— most obviously to make promote-species work per household, which is a normal, wanted feature. The
`wrangler.toml` comments that create the containment (*"⛔ NO `GITHUB_TOKEN`, ever"*) give their
reason as **promote-species writing onto Mom's live branch**; not one of them names zones. So whoever
removes it will be solving a different problem and will not know they are also unlocking this.

⚠️ **One more layer, which is luck and should be named as luck.** `validVertex:3512` hardcodes
`lon −84.40..−84.33 / lat 34.52..34.58` — a ~6 km box around Fernwood — so a far-away household's
zones would be rejected as `invalid-zones` with a hint saying *their units are wrong*. **A units check
accidentally acting as a tenancy check, strongest exactly where you need it least:** a neighbour in
Tate Mountain Estates — a plausible early customer — passes it cleanly.

**Cost to clear:** ⛔ **the fix is not "make `ghPutFile` tenant-aware."** A repo-per-household is a
GitHub account, a token, a Pages project and a rate limit per family, which is the deployment-per-
household model the DECISIONS file just retired for stronger reasons. The fix is to **stop persisting
household-authored content to git** (§3, D1) and to **fence the endpoint** in the meantime (D7).
Effort: low to fence, medium to retire for zones, and **the species sites are a separate, later
decision on the same class** — they are not blocking anything tonight and should not be bundled in.

---

### 🟠 B2 · `handleZonesGet`'s git fallback is a cross-household READ, and it fires on the failure case

`handleZonesGet:3826` — if KV is empty *or the JSON does not parse*, it falls back to
`ghGetFile(env, "zones.json")`, which is Fernwood's file. Under one production environment with a
GitHub token present, **Bob's phone would be served Fernwood's 23 zones and their names.** The
fallback fires precisely when something has gone wrong, which is when nobody is watching.

**It is contained by the same configuration property as B1** — `/health` reads `"github": false` on
`home`, so today the fallback simply does not fire and a household with no zones gets an empty map.
Not a live leak. But it is the *same single configuration fact* doing the work, which means one
credential binding turns both B1 and B2 on at once, silently, in opposite directions (a bad write and
a bad read). Two defects behind one accident is worse than two defects behind two.

This is the conversion's own falsifier `T3` in miniature: *"authorized for some estate" leaking into
"authorized for this estate."* **Delete the fallback, or gate it on the resolved estate being the
legacy estate.** ⛔ And it must not fail *green*: a household with no zones should return an empty
map, and a household whose KV value fails to parse should return a **loud error**, not somebody
else's property. Effort: low. **Ride this with the conversion's readers-first slice.**

---

### 🟠 B3 · A household origin has no map surface at all

`tools/pages-deploy.py:67` — `HOUSEHOLD_ALLOW` is eight named files: `onboarding/index.html`,
`estate/index.html`, `homes/index.html`, both `settings/*`, `qa-build.json`, `favicon.ico`,
`index.html`. **`viewer.html` is not in it, and neither is `images/`.** So even with perfect geometry
in Bob's KV, Bob's phone has nothing that draws it, and no basemap bytes to draw it on.

⭐ **This is good news, not bad.** The allow-list is the right posture (fails toward a 404, never a
disclosure) and `estate/index.html` is already engine-classified and estate-neutral. The map belongs
in the neutral shell, built to serve any estate — **not** in `viewer.html`, which is 53% instance by
the manifest's own measurement and carries the street address. `F5` in the DECISIONS file already
says the neutral shell is what makes one production environment reachable *without touching
`viewer.html`*; the map is the same argument. Effort: medium (it is a real renderer), but it is
product work, not tenancy work.

---

### 🟠 B4 · There is no basemap for a second household, and no pipeline that could make one

Zones are drawn on a **registered** basemap; `onboarding/index.html:11` already rules zones out of
first run for exactly this reason — *"there is no basemap for an address we do not have."* What a
per-household basemap actually requires, measured against what exists:

| stage | today | generalises? |
|---|---|---|
| address → coordinates | onboarding captures address components and builds a **Google Maps link** (`:1049`). **There is no geocoder anywhere in this repo.** | ⛔ **missing entirely.** Every stage below is keyed on a point. |
| coordinates → available imagery | `fetch-basemap.py` `DEFAULT_ITEM` is a hardcoded Fernwood NAIP quarter-quad id; `--item` takes one by hand. `LAND-SOURCES.md` documents the STAC *search* in prose; **the tool implements only item-fetch.** | ⛔ needs a STAC search by intersecting point. ~40 lines. |
| choosing which capture | human judgement, informed by the sun/shadow/leaf table | ⭐ **must stay human, and today is not even surfaced per household.** `sun_and_season()` already computes it. |
| fetch + write bounds | `fetch_crop` + `.bounds.json`; bbox math is latitude-aware | ✅ clean, once it takes coordinates as arguments instead of from `momlib.config` |
| tracing | `tools/area-trace.html` opened by hand, base image path baked in | ⚠️ the cost centre — see below |
| naming | a conversation (2026-08-30, Mom, 16 areas named unprompted) | not an engineering stage; it is an interview |
| validate | `zone-topology-report.py` + `validVertex`'s envelope | envelope is Fernwood-typed; **derive it from the estate's own registered bounds ± a pad** — then it is a units check *and* a tenancy check, derived rather than typed |
| load into the household's store | ⛔ **does not exist.** `zone-save` is the only writer and it writes git. | the gap |
| appear on the phone | `handleZonesGet` ✅ | ready today |

**⭐ The product boundary, and it deserves to be said out loud: NAIP is US-only, and NAIP is the
whole reason this is free.** Public domain, redistributable, committable, and therefore cacheable for
offline use. Outside the US there is no equivalent — Esri/Google are **display-only** (this repo
already refuses Esri as a committed base for exactly that reason, `fetch-basemap.py` docstring), and
paid tiles meter per view. So the honest statement is:

> **US households get a stored, redistributable, offline-capable basemap. Non-US households would get
> a live tile layer that cannot be stored, cannot be served offline, and may cost money.** Given the
> site premise — no cell reception, coverage falling off with distance from the house — that is a
> *materially worse product*, not a licensing footnote.

**Cost per US household: $0 in imagery**, ~430 KB of storage for one 1500×1500 webp (ship webp only;
the 1.9 MB PNG fallback is 2015-era support and should not be stored per household), plus **operator
hours** — which is the real cost and the one that scales linearly.

**⚠️ And several stages have no failure mode because they have only ever run once.**
`fetch-basemap.py` has no handling for a quad with **no leaf-off capture** — Fernwood happened to have
one, and `LAND-SOURCES.md` calls that *"luck, not policy."* Nothing handles a household outside NAIP
coverage. `register-gearth-frame.py` has run against one frame. The bounds file has never been wrong.
And **no tool has ever been asked which household it is for.**

---

### 🟡 B5 · There is no per-household state for "where is this map in the pipeline"

At n=1 the state is in Paul's head. At n=3 it is the thing that rots. Nothing records whether a given
estate has a basemap, has traced zones, has named them, or has had any confirmed.

The cheap answer is the one this repo already uses everywhere, and `F2` in the DECISIONS file states
its shape: **derive the stage from artifacts that exist** (does this estate have a `zones:all` key? a
basemap blob? any zone not `draft`?), print one line per household, and **read UNCHECKABLE — never
green — when the derivation finds no households.** Effort: low, and it is the control that makes N>1
legible at all.

---

### 🟡 B6 · Inlining geometry into `viewer.html` is not a path at N — confirmed, and here is the replacement

Measured: `viewer.html` is **2,078,223 bytes**; `ZONES_DATA` is **41,380 bytes** for 23 zones (~1.8
KB/zone). The file has silently hit two ceilings, one of which (the 1 MB Contents-API cliff) returned
HTTP 200 with an empty body and broke the write-to-canon path for two weeks. The blob fallback fixed
the **read**; the **write** still ships ~2.8 MB of base64 per zone edit and does not verify the bytes
it landed.

So no, N households' geometry cannot be inlined — and the correct replacement **already exists and is
already the primary path**: `refreshZonesFromCloud()` (`viewer.html:13559`) fetches `/api/zones`
first and treats the inline copy as cold-start fallback only. The illustrated-map row wants an SVG
renderer reading *the same record*; that is one more consumer of the same endpoint, not a second
store. **The record is served, never inlined. The inline copy retires with git.**

⚠️ **But do not trade a working offline map for a broken one.** Today `ZONES_DATA` is the offline
copy. `BACKLOG.md`'s field-capture row already records that `viewer.html` **has no service worker and
no manifest** — off Wi-Fi it does not degrade, it does not load — so offline is already broken for the
whole surface and removing the inline copy breaks nothing that works. **But the new estate shell
should be born with a service worker caching the basemap blob and the zones response**, because at a
place with no cell reception the map is the single surface where offline matters most.

---

## 2 · The three IDEATION rows — which are prerequisites, which are downstream

Asked for a plain ruling. Here it is.

### 🗂 LAYERS — **PREREQUISITE.** And for multi-household the argument is stronger than the row states.

The row argues layers because aerial/lidar/illustrated/parcel is a stack, not a choice. True. But the
multi-household argument is structural and the row does not make it:

> **Different households will have different *available* imagery, and the difference is not a
> preference — it is a fact about their coordinates.** Some quads have a leaf-off capture, some do
> not. Some have 0.6 m, some only 1.0 m. `LAND-SOURCES.md` records **3DEP coverage for Pickens County
> as unconfirmed** — for the county Fernwood is in. A parcel layer exists for some counties and not
> others.

`_meta` today carries **six scalar `baseImage*` fields plus one `baseImageLicense` string** — a
one-picture-per-place model. It cannot express "this household has NAIP 2022 only" and "that one has
NAIP ×3 + hillshade + plat" as the same shape. So the pipeline would be forced to make a choice, per
household, at acquisition time, that it cannot make honestly and can never revisit.

⭐ **And the license is per-layer, not per-place** — NAIP is public-domain committable, Esri and
Google Earth are display-only, and the Tate lot drawing *must never be committed to this public
repo*. A single `baseImageLicense` string cannot carry a mixed stack, and getting that wrong is a
licensing error, not a cosmetic one.

**Ruling: `_meta.layers[]` replaces the `baseImage*` scalars.** Each layer:
`{id, kind, source, url, bounds, width, height, capturedAt, license, redistributable, defaultOn,
opacity, order}`. Server-owned, exactly as `_meta` already is (`worker.js:3670` — *"THE SERVER OWNS
`_meta`"*, and that comment's reasoning holds unchanged). The viewer's single hard-wired `<img>`
becomes an ordered list. **Do this before chasing sharper imagery** — the row is right that a stack
makes new imagery an addition instead of a migration.

### 📏 ONE GEOMETRY — **PREREQUISITE, and it is ONE decision, not three.**

The evidence is decisive: **The Path is stored as a 17-vertex polygon** and therefore reports an
acreage and a median slope that mean nothing. That is a mis-modelling, not a bad trace, and the row
correctly forbids tidying it away. What is currently unrecordable: paths, walls, the driveway, water
lines, fences, **the property line itself**, and — from the 2026-09-04 voice memo — shut-off valves
and repair locations.

**Are lines / points / polygons one schema problem or three? One store, one record shape, three
validators.** They share everything — `id`, `name`, `type`, `color`, `status`, `history`,
`createdAt/By`, `updatedAt/By`, `partOf`. They differ only in the geometry member. So:

```
geometry: { kind: "polygon" | "line" | "point", coordinates: [...] }
```

which is GeoJSON's own answer, in a file that already stores WGS84 in GeoJSON axis order and already
round-trips through KML (`zones-to-kml.py` / `kml-to-zones.py`).

⛔ **Do not add a `lines` key beside `zones`.** That is the third parallel array, and
`momlib.DOMAINS` exists precisely to stop that pattern — the same argument that made five wildlife
files one declared schema.
⚠️ **But validation genuinely differs.** `sanitizeZone`'s "0 or ≥3 vertices" is polygon-specific and
would silently reject every line; a line needs ≥2 and no closure; a point needs exactly 1. **One
schema, three validators, dispatched on `kind`.**

**Why now and not at Path 3:** at 23 records and one household this is a migration script. At N
households it is a fleet migration. It is also what settles B0's whitelist (the sanitizer gets
rewritten anyway) and what unblocks the illustrated map, the plat overlay, and Model A coverage — all
of which `.plans/2026-09-04-map-region-smoothing-PLAN.md` §4b names as blocked on this and nothing
else.

### 🕰 THREE DATES — **the CONSTRAINT is standing; its SCHEMA consequence is a prerequisite; its analysis is downstream.**

- **Constraint (standing, now):** ⛔ never snap or auto-correct polygons to the lidar. That fits 2026
  ground to a 2018 surface. Already stated; nothing here changes it. It generalises to every
  household the moment there are two dated layers, which is immediately.
- **Prerequisite:** `capturedAt` as a first-class field **on every layer**, which is exactly the
  `_meta.layers[]` shape above. Folded in. A basemap pipeline that carries a filename and not a
  provenance record cannot express this at all.
- **Downstream:** the inversion — *where lidar and current ground disagree is a map of where the
  earth was moved.* Genuinely valuable, entirely deferrable, and Fernwood-only until a second
  household has two dated surfaces.

### 🎨 Illustrated map, 📐 plat overlay — **DOWNSTREAM.** Both are blocked on LAYERS + ONE GEOMETRY, and both get cheap once those land.

---

## 3 · Where geometry should live

> ⛔ **THIS IS NOW A CONSTRAINT ON THE OPTIONS, NOT A PREFERENCE.** B1 establishes that the GitHub
> write path has no household concept and is outside the conversion's reach. Therefore: **any maps
> feature that persists by writing to the repo cannot be multi-household at any point on the current
> roadmap.** "Geometry stops living in a git repo" is not one path among several — it is a
> precondition for *every* path that ends with a second household's map. The only real question is
> what that costs, and §3b prices it.

**Is JSON-in-a-repo defensible as a durable store for user-authored geometry? No.** Three
independent reasons, all already on this repo's record:

1. **Size.** The write path re-uploads a 2.08 MB HTML file per zone edit. The 1 MB cliff already
   broke this exact path for two weeks. N households multiplies the file, not the risk tolerance.
2. **Publicity.** Git commits here are **public**. Zone names are the most personal content in the
   record — *"the bank," "St Francis garden," "The Bluff."* `check-estate-neutral.py` exists because
   a household surface must not name another household; committing every household's place names into
   one public repo is the opposite policy, enforced nowhere.
3. **Concurrency.** `ghPutFile` passes the sha, so a second concurrent writer gets a GitHub 409,
   which `ghPutFile` **throws** (`:2324`) and `handleZoneSave` does not catch — the caller gets a 500
   carrying a raw GitHub message. At one author that never happens. At one operator plus a retry, it
   does.

**Recommendation:**

| what | where | why |
|---|---|---|
| geometry (`<estate>:zones:all`) | **KV — already there, no change** | 41 KB against a 25 MB value limit; read on every load; exactly KV's access pattern. `handleZonesGet` already keys it correctly. |
| basemap bytes | **KV, as an `arrayBuffer` value, served through a new `GET /api/basemap`** | ~430 KB/layer, well inside the limit. |
| Fernwood's `zones.json` | **stays as the legacy instance record; stops being a write target** | it is the historical trail and `ENGINE-MANIFEST` classifies it instance. Freeze it, do not delete it. |

⭐ **The reason basemaps go to KV and not R2 is `household-export.py`, and this is the load-bearing
argument.** That tool's whole claim is *"the coverage statement is the product; the bytes are a side
effect"* — it enumerates KV **by construction** from `worker.js`'s own `keyFor`/`dateKey`/`blobKey`
call sites, so a new KV kind is covered the moment it is written. **R2 is not in that tool at all.**
Putting basemaps in R2 would make its coverage claim false *without a single word in it changing* —
it would report a complete export of a household whose basemap was never exported. That is the F2
shape exactly: an instrument whose scope must be derived from whatever declares reality.

So: **KV now** — one store, one exporter, one coverage claim, no new binding — which is also Paul's
own principle *"Storage mirrors existing shape."* **Move to R2 when** basemap count × size gets real
(say >20 households or >50 MB), **or** when direct public URLs are wanted — and when you do, **widen
`household-export.py` in the same commit.** Not the next one.

⛔ **And one hard ordering constraint that is easy to walk past.** `household-export.py`'s own
docstring: the escape hatch for a mistake is *"delete the namespace,"* **the first write by a second
household destroys that hatch**, and the export tool must exist *before* that write. **Loading Bob's
polygons into the shared production namespace IS that first write.** A `wrangler kv put` is not
harmless here. Run the export, read its coverage statement, then load.

### 3b · What leaving git actually costs — priced, because it is not free

`zones.json` is read as a **file** by 17 tracked things (grep). Sorted by what breaks and how badly:

| dependent | what it needs the file for | cost if geometry moves to KV |
|---|---|---|
| ⛔ `tools/build-digest.py` | `digest_zones()` reads `zones.json` from disk; **`CORE_INCLUDES = ("property", "zones", "turf")` is a declared FLOOR** with a non-zero exit | **the sharpest coupling on the list.** The digest is built at deploy time from files on disk. If a household's geometry lives only in KV, that household's Guru **cannot answer "where is the fern garden"** — and the floor means the build *fails* rather than degrades. **Fix: the digest builder fetches `/api/zones` for the estate it is building, instead of reading a path.** That is a real change and it is the one that must land with the move, not after. |
| ⛔ `tools/check-live.py` | `zones.json` is one of the **five tracked live assets** whose byte-identity to HEAD proves a ship | it stops being a Pages asset, so the row must be **removed with a reason**, not left to fail. ⚠️ And there is a drift guard that re-derives the roster from `viewer.html`'s fetches — so removing the asset and leaving `refreshZonesFromCloud`'s `fetch("zones.json")` fallback in place makes the guard fire. **Both move or neither.** |
| 🟠 `tools/check-data-inline.py` + `tools/build-viewer.py` | the `("zones.json","ZONES_DATA","zones","zones")` SOURCES row; `build-viewer.py` reads that roster | ✅ **this cost is a saving.** Once geometry is served, `ZONES_DATA` retires and the row is deleted. `build-viewer.py` already has a `zones` `EMPTY_SHAPE` (`{"declaredAbsent": true}`), so the built viewer degrades cleanly by design. |
| 🟠 `zones-to-kml.py` / `kml-to-zones.py` | the Google Earth round trip — a genuinely useful operator tool | **keep it, re-point it.** These become `--env <household>` tools reading and writing the API instead of the file. ⭐ This is the *good* version: today the round trip only works for whoever has the repo checked out; through the API it works for any household. |
| 🟠 `momlib.DOMAINS` · `check-domains.py` · `harvest-questions.py` | `zones.json` as the domain's canonical file | the domain row's file field becomes an endpoint or a per-estate cache path. **Non-trivial** — `DOMAINS` is the manifest everything derives from, and this is the first domain that would not be a file. ⚠️ Worth flagging as the seam where "one instance = one repo of JSON" first breaks; the other 10 domains will follow eventually. |
| 🟡 `area-trace.html` · `zone-capture.*` · `zone-topology-report.py` · `draw-zones.py` | load a local file to draw against | operator tools on Paul's laptop — give them `--env` and a fetch, or let them work on an exported file and load it back. Cheapest of the group. |
| 🟡 `register-gearth-frame.py` · `fetch-historical-topo.py` · `fetch-trace-hires.py` | read `_meta.bounds` for the georeference | follows `_meta` wherever it goes. Trivial. |
| 🟡 `.github/workflows/build-viewer.yml` · `deploy-worker.yml` | CI reads the file | follows `check-data-inline` / `build-digest`. |

**⭐ And the one thing genuinely lost: git-as-audit-trail.** This repo gets real value from it — every
zone edit is a dated commit with a message and a diff, recoverable forever, readable by a human
without a tool. KV has none of that: it is last-write-wins with no history.

**How much of that value is actually lost, honestly:**
- **Partially replaced already, in-record.** Every zone carries its own `history[]` (`at`, `by`,
  `action`, `details`), capped at 100 entries by `sanitizeZone`. That is a per-record audit trail
  that travels *with* the record into KV, and unlike git it survives a store migration.
- **Partially replaced by the exporter.** `household-export.py` writes a dated snapshot of everything
  a household holds. Run it on a cadence and you have point-in-time recovery — coarser than a commit
  per edit, but it is the mechanism this repo has already decided is the durable copy.
- **Genuinely lost:** the diff. "What changed in this polygon between July and September" stops being
  answerable. ⚠️ **For a hobby map at n=3 households that is an acceptable loss.** For Fernwood
  specifically it is not zero — the 23 traced zones are the output of a session with Mom that cannot
  be repeated — which is a second reason **Fernwood's `zones.json` freezes in place rather than being
  deleted.** The history stays in git; the file just stops being written to.

**Verdict on the price: acceptable, with two must-dos in the same commit** — `build-digest` fetching
instead of reading (or the household's Guru silently loses its map vocabulary), and `check-live`'s
roster + the viewer's `zones.json` fallback moving together (or the drift guard fires).

---

## 4 · Confirmation is a different write — and it should ride the feedback machinery

`[paul-ruled]` *we draw, they confirm.* That makes the confirmation path the **product**, not a
follow-up. Three findings:

### It must not share a door with `zone-save`

A confirmation is **per-zone, small, householder-authored, never geometry**. A save is **whole-set,
operator-authored, entirely geometry**. Routing a tap through `zone-save` means a householder's "yes
that's right" round-trips 23 polygons through an all-or-nothing full-file rewrite, and a bug in that
path deletes a map. The blast radii are not comparable. (Principle already in the library:
*two lifecycles cannot share one dataset.*)

### The feedback machinery already has the three things a confirmation needs, and `zone-save` has none of them

A watermark that cannot bury an unanswered item · an explicit fold step · and a lifecycle contract
enforced by `test-feedback-cycle.py`. CLAUDE.md's standing rule is binding here: *a new input channel
does not ship until a note arriving on it can be surfaced, protected from the watermark, and closed.*
**A zone confirmation is a new input channel.**

⚠️ Note what `/api/zone-feedback` actually is today: a **free-text "describe a place" note**, keyed
to a date, **never linked to a zone id**. It is a suggestion box, not a confirmation channel. It is
not the answer; it is evidence that the answer was needed and got built as storage instead of a loop.

### ⭐ The wiring is already half-done, and I did not expect this

`momlib.DOMAINS` **already carries a `zone` row**, executed and read this session:

```
'zone': ('zones.json', 'zones', 'ZONES_DATA', 'place', (), ('status',), False)
```

— file, list key, viewer const, `group: place`, no time axis, **`markers: ('status',)`**,
`cardable: False`. So the domain manifest already declares *`status` is where this domain admits a
guess*, and `momlib.markers()` already normalises it. The remaining work is the documented **two-place
change**: flip `cardable` to `True`, and add `ZONES_DATA` to `buildCard`'s `ENTITY_DATA` in
`viewer.html` — `ENTITY_SOURCES` is *derived* from `cardable`, so `entity_map_divergence()` and
`test-feedback-cycle.py`'s RESOLVE leg will fail loudly if only one side lands. That is the mechanism
working as designed.

⚠️ **Supply, not schema, is the risk** — CLAUDE.md says so explicitly, and 23 zone cards against 5
visible slots with 8 already on the bench would flood Mom's queue. **Rate-limit at harvest** (one or
two zone cards at a time), not merely at ranking. `MAX_VISIBLE` is 5 and variety is a *hard filter*,
not a tiebreaker — a domain that can generate 23 cards is exactly what that filter was built for.

### What `status` should mean, and who may mint it

Today the enum is `draft | confirmed | flagged`, **all 23 zones are `draft`, and nothing anywhere
writes any other value.** The field is decorative. `BACKLOG` already shipped the *rendering* of it
(dashed stroke on non-`confirmed`, `4878994`) and flagged the consequence: *the whole map reads
dashed, and the fix is to confirm the zones we trust, not to soften the rendering.* This is that fix.

Proposed meanings:

| value | means | who may write it |
|---|---|---|
| `draft` | drawn by the operator; nobody at the place has seen it | the drawing tool. Honest default. |
| `confirmed` | **a person standing at the place said the name and the extent are right** | ⛔ **only a fold of a householder answer.** Never the operator, never the drawing client. |
| `flagged` | a person said it is wrong; **carries their words** | the fold of a "not quite" answer |

⛔ **And the rule that makes the field worth anything: `sanitizeZone` must REFUSE `confirmed` from a
drawing client.** Right now the whitelist accepts any value in `validStatuses` from any caller. If an
operator's tool can mint `confirmed`, the field stops meaning "someone stood there" the first time
anyone hand-edits a JSON — and this record's whole doctrine is that a confidently-wrong marker is
worse than an honestly-unsure one.

⚠️ **A `flagged` zone stays rendered.** It is still the best guess anyone has, and hiding it loses the
map. It is a work item for the operator, not a deletion.

⭐ **And the visible close is the point.** The plant card's provenance chip flips from *"our read from
a photo"* to *"confirmed on the ground · <month>"*, and CLAUDE.md names that as **the** loop-close —
she sees her read become the truth of the place. The zone equivalent is the same words on the map
legend. Without it, "we draw, they confirm" is extraction: we take her knowledge and she sees nothing
change.

---

## 5 · Is "we draw, they confirm" a real reprieve on the write path?

**Real on `/api/zone-save`. A trap if read as a reprieve on "the write path."** Priced honestly:

**Real, and worth taking.** Nobody but the operator exercises the GitHub binding, so a second
household's map can ship without converting B1. That saves a genuine chunk of work and it is not
illusory.

**Trap A — the reprieve is not enforced by anything.** `/api/zone-save` sits below the auth gate at
`worker.js:3465` and is reachable by **any administrator-capability credential** on the shared
Worker. "Bob will not draw" is a statement about Bob's behaviour, not about the system. Under one
production environment, an administrator grant at Bob's estate reaching `/api/zone-save` is a
**cross-household write**, not a permission error.
⭐ **So take the reprieve by deleting the reachability, not by trusting the plan.** Fence the
endpoint: refuse unless the resolved grant's estate equals the legacy estate. A reprieve you can
revoke by shipping an unrelated feature is not a reprieve.

**Trap B — it converts a structural blocker into a manual step nobody has designed.** The
coordinator's read, and it is correct — but price it precisely: the manual step **is** the near-term
product per Paul's ruling, so designing it is the work, not overhead. **The trap is the step staying
*undesigned*** — living as shell history on one laptop, which is exactly where all the zone tooling
already lives (§6). B5 is the specific cost.

**Trap C — the moment a householder taps "not quite," you need a write path again.** True, and it is
the good news: you need a *different* one, and §4 says it already half-exists. Do not build it as
zone-save-with-permissions.

**Trap D, which nobody has named — the operator does not have knowledge of the land either.** Paul's
stated reason AI is ceilinged is that it needs knowledge of the land. **Paul has never walked Bob's
property.** So a Paul-traced first pass at a house he has not visited is only as good as what Bob
told him — which means the **confirmation loop is the load-bearing half, not the drawing.**
⭐ **Practical consequence: draw coarse, name plausibly, correct fast.** Do not spend Fernwood-grade
precision (23 zones, 46-vertex traces, sliver analysis) on a first pass at a house nobody has stood
on. That precision was earned by Paul standing there. Somewhere else it is false confidence rendered
at 0.6 m/px.

---

## 6 · Is the zone tooling engine-shaped or place-shaped? And is the manifest honest?

`ENGINE-MANIFEST.md` classifies `tools/` as `class: engine, tier: MUST-NOT-DIVERGE`. Measured
coupling (grep for `momlib.config` use and Fernwood coordinate/name literals):

| tool | momlib refs | Fernwood literals | verdict |
|---|---|---|---|
| `fetch-basemap.py` | 4 | 2 | engine algorithm, **Fernwood defaults** (`DEFAULT_ITEM`, `DEFAULT_DATE`, coords from `momlib.config`) |
| `zones-to-kml.py` | 3 | 5 | engine algorithm, Fernwood-bound |
| `register-gearth-frame.py` | 2 | 0 | close to place-shaped already |
| `zone-capture.py` · `kml-to-zones.py` · `zone-topology-report.py` | 0 | 1 each | one literal each; cheap |
| `area-trace.html` · `zone-capture.html` | — | base image path baked in | needs a basemap+bounds it can be pointed at |
| `worker.js` `validVertex` | — | **the whole envelope** | ⛔ engine *server* code with one estate's bounding box typed in |

**Is the manifest honest? Yes about the class, and it declares its own blindness about the coupling
— but one row is measurably incomplete.**

The manifest already states that its checker cannot see *"a config value copied into engine code"* —
that is **P4, "counted, and its detector is C5 step 4's lint, not built yet."** Honest. But
`mixed_in_dirs["worker/worker.js"]` names its instance literals as *"2,873 ft ×5 blocks, the station
MAC default"* — **and does not name the zone envelope**, which is four typed coordinates of one
estate sitting in the engine's server half. That is a one-line correction to a row that is otherwise
doing its job.

**The honest summary: the zone tools are engine algorithms wearing instance defaults.** Converting
most of them is *"take the coordinate as an argument."* Genuinely cheap. The two exceptions are
`area-trace.html` (needs a pointable basemap) and `validVertex` (should derive its envelope from the
estate's registered bounds — which turns a typed literal into a derived check that is simultaneously
a units guard and a tenancy guard).

---

## 7 · Three paths

⛔ **All three share one precondition, and it is not negotiable: geometry stops being written to the
repo.** Per B1, the GitHub write path has no household in it and cannot acquire one through the
conversion, so a maps feature that persists to git is single-household forever. **There is no fourth
path where the repo stays the store.** What differs between A, B and C is what you build *on top* of
a served store — not where the store is.

### Path A — "Operator pipeline + read-only household map" (the deliberately minimal one)

**Build:** geocode step (US Census Geocoder — free, no key) → STAC search by point → basemap fetch +
bounds → basemap into KV + `GET /api/basemap` (written with `scopeFor` from birth) → a map view in
`estate/index.html` → `tools/zone-load.py --env bob` wrapping the KV put → delete `handleZonesGet`'s
git fallback → fence `/api/zone-save` → **and the two §3b must-dos: `build-digest` fetches instead of
reading, and `check-live`'s roster + the viewer's `zones.json` fallback move together.**

**Not built:** no householder write, no confirmation, no schema change, no lines, no layers.

**Testable:** Bob's phone renders 20 named polygons over his own house. Real demo, roughly a week.

⛔ **But it is a read-only map, and this repo's governing principle says a glance without a loop is
extractive.** Path A alone is a demo, not a product.

### Path B — Path A **+ the confirmation loop on the existing feedback machinery** ⭐ RECOMMENDED

**Adds:** `zone.cardable = True` + `ENTITY_DATA` row · a zone-confirm card type in
`harvest-questions.py`, **rate-limited at harvest** · `fold-answer.py` writing
`status: confirmed | flagged` + a provenance line · the map legend rendering *"confirmed on the
ground · <month>"* · the `sanitizeZone` round-trip assertion from B0 · `sanitizeZone` refusing
client-supplied `confirmed`.

**Why this one.** *We draw, they confirm* **is literally a confirm-card queue**, and this project has
already built, broken, debugged and hardened one over three months — watermark protection, the fold
step, the ack ribbon, `question_state()`, the entity-resolution map, a test suite that asserts every
leg. Building a second confirmation mechanism beside it would be this repo's most repeated failure
(a second definition of "settled"). And `momlib.DOMAINS` already declares the marker path. **The
cheapest correct thing here is also the thing that is already 60% built.**

**Trade:** zones become the second domain in Mom's loop and supply pressure is immediate. Mitigate at
harvest, not at ranking.

### Path C — Model A coverage + lines + points + layer stack, geometry as a first-class multi-kind store

The full thing `.plans/2026-09-04-map-region-smoothing-PLAN.md` §4b points at. Blocked on Paul's
adjacency rulings, on lines-in-the-schema, and on a store that holds three primitives.

⛔ **Do not start.** ⭐ **But take two of its decisions now** (D2, D3 below) — they are a migration
script today and a fleet migration later.

### Recommendation

**Path B, sequenced as A-then-loop, with D2 and D3 decided up front and B0 fixed tonight.**

Trade-off, on the dimensions that matter here:

| | A | **B** | C |
|---|---|---|---|
| complexity | low | low-medium (reuses a built mechanism) | high |
| scalability | fine to ~10 households | same | the only one that scales the *drawing* |
| future features | blocks nothing | opens the illustrated map once D2 lands | is the future features |
| future-Paul-with-Claude | one new endpoint | **one new endpoint + one flag in a manifest he already reads** | a new subsystem |
| learning value | GIS pipeline plumbing | **the loop-design lesson generalises to every domain** | topology/coverage theory — real, but not now |

---

## 8 · What Paul must decide, with my recommended answers

| # | question | recommendation |
|---|---|---|
| **D1** | Does geometry stop being a git artifact? | **Yes — and per B1 this is a precondition, not a preference.** KV is canon for zones from the second household onward; Fernwood's `zones.json` **freezes** as the legacy instance record (the git history of Mom's 23 traced zones is kept, the file just stops being written); `zone-save`'s GitHub half is **retired**, not converted. Priced in §3b: two must-dos in the same commit (`build-digest` fetches; `check-live` + the viewer fallback move together), one real loss (the per-edit diff), two partial replacements already in hand (`history[]`, `household-export.py`). |
| **D1b** | Do the **six species** `ghPutFile` sites get the same treatment? | **Not tonight, and do not bundle them.** Same class, different urgency: they are operator-triggered, they block nothing on this roadmap, and promote-species-per-household is its own design question. ⛔ But record that **they are the reason someone will one day bind a GitHub credential to a household Worker** — which is what turns B1 and B2 on. Whoever does it must be told what else it unlocks. |
| **D2** | `geometry: {kind, coordinates}` now, or `zones` + `lines` + `points` later? | **Now**, at 23 records and one household. One record shape, three validators. ⛔ No parallel arrays. |
| **D3** | `_meta.layers[]` with per-layer `capturedAt` + `license` + `redistributable`, replacing the six `baseImage*` scalars? | **Yes, in the same schema move as D2.** It is the prerequisite the LAYERS row identifies, and the multi-household argument (available imagery differs per household; licence differs per layer) is stronger than the one the row makes. |
| **D4** | Does confirmation ride Mama's Perspective rather than a new endpoint? | **Yes.** `momlib.DOMAINS` already declares `markers: ('status',)`; it is a two-place change with a test that fails loudly on half of it. |
| **D5** | What does `confirmed` mean, and who may mint it? | *A person standing at the place said the name and extent are right.* **Only a fold of a householder answer.** `sanitizeZone` refuses `confirmed` from a drawing client. `flagged` stays rendered and carries her words. |
| **D6** | Basemap store: KV or R2? | **KV** — one store, one exporter, one coverage claim. Move to R2 at >20 households or >50 MB, **and widen `household-export.py` in the same commit**. |
| **D7** | Is `/api/zone-save` fenced or retired? | **Fenced this week** (refuse unless the grant's estate is the legacy estate), **retired** when `zone-load.py` writes KV directly. |
| **D8** | Is "draw your own map" US-only? | **Say yes, in writing, now.** It is a NAIP consequence and it collides with the offline premise. Better a named boundary than a discovered one. |
| **D9** | *(not a decision — a bug)* B0 | Fix `sanitizeZone`'s whitelist and add the round-trip assertion **before the next zone edit**. |

---

## 9 · Sequencing against the one-production-environment conversion

Plainly:

- **The operator pipeline is INDEPENDENT. Start it now, in parallel.** Geocode → STAC search →
  basemap → bounds → KV load runs on Paul's laptop, touches no `worker.js`, and cannot be broken by
  the conversion. It is the long pole and it has no dependency. ⛔ Except the `household-export.py`
  ordering constraint in §3 — the KV load *is* the first second-household write.
- **The read path is INDEPENDENT and already correct.** `handleZonesGet` keys by
  `keyFor(scopeOf(env), …)` and becomes `scopeFor` in the conversion like every other reader. ⭐ Any
  **new** endpoint (`/api/basemap`) must be written with `scopeFor(request, env, grant)` **from
  birth** — a new site should never be born needing conversion.
- **B2 (git fallback) and D7 (fencing zone-save) RIDE WITH the conversion**, in its readers-first
  slice. They are the same defect class the conversion's `T3` falsifier exists to catch.
- **The confirmation loop WAITS for `T2` (sharing) to pass.** A confirmation is a person-authored
  record; the entire point of the conversion is getting person↔estate right. Building a fold path
  against a scope model mid-flip means writing it twice.
- **The schema move (D2 + D3) is INDEPENDENT of the conversion** — it is a data-shape decision, not a
  tenancy one — **but it must land before a second household's geometry exists**, or it becomes a
  fleet migration. That makes it *earlier* than the conversion in practice, not later.

- ⭐ **The git departure (D1) is a PRECONDITION and it is independent of the conversion**, because it
  is a store decision, not a tenancy one. It can be done today, at one household, with the two §3b
  must-dos, and it makes every later slice cheaper. **It is the single highest-value thing on this
  page after B0**, because until it lands there is no path to a second household's map at all.

**Net: map work does not wait for the conversion. Two slices of it ride along; the rest is
parallel — and the precondition (leaving git) is available now.**

---

## 10 · What I could not verify

1. ✅ **RESOLVED — no longer open.** I could not verify whether GitHub credentials were bound to the
   `home` Worker; the session that owns `worker.js` checked and `/health` reports **`"github": false`**.
   So B1 and B2 are **contained, not live**, and the containment is deliberate. ⚠️ Recorded here
   because the *shape* of the finding survives its resolution: **the containment is configuration, not
   structure**, and nothing in this repo currently tells the person who binds a credential what else
   they are turning on. That is the residual risk, and it is a one-line comment's worth of work to
   close (see D1b).
2. GitHub's Contents API **write** ceiling for a 2.08 MB `viewer.html`. Writes have evidently
   succeeded historically; I found no documented limit and did not test one.
3. Whether NAIP coverage and quality generalise — I did not run a STAC search for a second address,
   and `LAND-SOURCES.md` records 3DEP coverage for **Pickens County itself** as unconfirmed.
4. What `estate/index.html` actually contains. I confirmed it is in `HOUSEHOLD_ALLOW` and is
   estate-neutral; I did not audit its markup for map scaffolding.
5. Whether R2 is enabled on Paul's Cloudflare account.
6. Census Geocoder rate limits at N, and its accuracy on rural addresses — a rural rooftop geocode is
   often a **road-centerline interpolation**, which for a mountain property could be hundreds of
   metres off. ⚠️ This is a `model-read-is-a-hypothesis` case: the geocode must be shown on a picture
   and confirmed by the operator before any basemap is cut from it. The onboarding "Verify address on
   Google Maps" link is already that human step — it just does not record a coordinate.
7. Whether tonight's concurrent session has already changed any of this. I read the tree as of my
   session start and wrote only this file.
8. Whether Bob (or any second household) would accept a Paul-traced map at all. That is a
   `user-researcher` question, it is n=0, and it is upstream of everything here.

---

## 11 · Principles I would propose after this (NOT added — proposing only)

1. **Enumerate writers by DESTINATION, not by helper — a store with no tenant concept is outside the
   conversion, not behind it.** When a system grows a tenant dimension, the inventory of what must
   change is usually built from the helper that already carries the tenant (here: 55 `scopeOf(env)`
   sites). Any store reached by a *different* helper contributes zero rows and reads as complete. The
   tell is a persistence path whose address comes from deploy config rather than from the request —
   it has never had a tenant, so it cannot be *converted*; it has to be *replaced or fenced*.
   *(Scope: cross-project. From B1 — eight `ghPutFile` sites, one repo secret, zero of the 55 rows.)*
2. **A field whitelist at a storage boundary is a schema copy, and it will drift.** Sanitizing by
   rebuilding from a fixed key list silently deletes every field added later. Either derive the
   allowed keys from the schema declaration, or assert a full round-trip in the test suite — never
   hand-maintain the list. *(Scope: cross-project. From B0 — `partOf` shipped 09-01 and is being
   deleted on every save since; and `_meta.fold_2026_08_31` had already predicted this exact shape
   for a different key.)*
3. **Containment by CONFIGURATION must say what it contains, at the configuration.** An absent
   credential, an unset binding or an unbound namespace can be a legitimate and even *preferred*
   control — failing is often the correct behaviour. But it is only safe while the person who
   restores it knows the full list of what restoring it turns on. When a config comment gives one
   reason and the setting actually guards several things, the others are undefended the day someone
   solves the stated problem. **Write the whole list where the setting lives, not in a design doc.**
   *(Scope: cross-project. From B1/B2 — `"⛔ NO GITHUB_TOKEN, ever"` names promote-species and does not
   name zones; the same absent credential is holding back a bad write AND a bad read, and one binding
   turns both on at once.)*

Say the word and I will draft each in full (statement / why / when it applies / avoid / example) for
your confirmation before anything is written to `~/.claude/engineering-principles/`.
