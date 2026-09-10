# READBACK — the ZONES lane · the incoming window, 2026-09-10 ~5:55 PM ET

- brief read: `handoff/handoff-zones-session.md`, stamped `dd377ba`
- HEAD when I opened: `9c48664` (two commits past the stamp). HEAD when I finished reading: `3b0ae79`
  (three past). **The tree moved twice while I read.** Six `claude` processes are live on this machine,
  three of them resumed handoff threads (`backlog-refinement`, `build-founding-walk`, this one).
- delta `dd377ba..3b0ae79`: `BACKLOG.md` (TIER 1 · 23, 24 added; 23 re-pointed), the build-description
  chain DESIGN, the refinement readback, and **this brief itself** (`7e934b8`). ⭐ **No file this lane owns
  moved** — `git log dd377ba..HEAD -- <the six lane paths>` is empty. The stamp is trustworthy for my scope.
- written BEFORE any work. Nothing edited, nothing run that writes, except `anchors.py --offline` in my own
  directory (it rewrites `frame-anchors.png`; `git status` on the dir is clean afterwards, so the exhibit is
  deterministic).

## 1 · What I understand the lane to be

**Zones as a feature, at `stage: design`, under the G1 line.** Paul stamped the STAGE on 09-07, not a build.
The lane does design, research, and dev-only instruments in `.engineering/zones-derivability/`; it ships
nothing, deploys nothing, edits no canon (`zones.json` explicitly), calls no paid API, touches nothing that
reaches Mom or Bob. Bob is gate 3 of the cascade, never gate 1.

The epic is three `BACKLOG.md` TIER 2 rows — **7** the feature · **8** the per-estate capture write path
(LEG 0, co-requisite) · **9** Process B, the derived first draft from an address — now at `:252-254` (the
brief says `:250-252`; two TIER 1 rows landed above them since). Their relationship is Z-10 (zones first,
plants second, the frozen plant record does not travel), not a rank.

The primitive is a **NAMED PLACE, geometry optional** (Z-5 structure-first). v1 = zones × plants, and the
v1's list half is an **amendment to `renderThisMonthPlants()`**, not a build (plan §0 ①). The operator
pipeline is four staged steps (frame → edges → regions → names), with Paul's 09-08 direction — *anchor,
then re-process around it*, his hedge kept — layered over it as a loop. The 09-08 render then measured
that **the machine proposes edges to snap to and never a place** (no closed contour anywhere; seeded
region-grow refused 6 of 10 and 8 of 10); the anchor's value is **scoping, not extraction** (one click on
the house removes 41 of 70 candidates). The 09-10 assessment then found that **two of the three
"highest-confidence objects" are DOWNLOADS**: the house (Microsoft footprints, IoU 0.76, 1.5 m centroid)
and the driveway (OSM service way, ends 9 m from the house, every zone within 21 m of the network). The
third, `main-parking`, is not — OSM gives a line, the parking is a 168 m² polygon. So the first human act
is *"is this your house?"*, not *"accept this derived edge."*

## 2 · Current state — what I verified myself, at `3b0ae79`

| claim in the brief | verified how | result |
|---|---|---|
| eight zones commits since 09-08 | `git log -1` on each sha | ✅ all eight exist, dated as described (09-08 17:52–18:32; 09-10 16:32, 16:36) |
| `anchors.py` reproduces the assessment | `python3 anchors.py --offline` | ✅ IoU 0.76 · footprint −2 m E −2 m N · seed way 9 m · every zone within 21 m · spine +30 m = 408 × 433 m, 23/23 · hand frame clipped 17/61 spine vertices · a 3rd building at +120 E / −144 S (R-A3's building) |
| canon holds 23 | `zones.json` | ✅ 23 |
| production serves 18 | plan §9a, `measured 2026-09-08` (production KV, schemaVersion 2, stamp 08-31) | ⚠️ **not re-measured today** — I did not hit `/api/zones` at prod. ⭐ And `viewer.html`'s inlined `ZONES_DATA` also holds **23** — so "18" is a fact about the **served KV record only**, not about any file at HEAD. Three copies exist (file 23 · inline 23 · served 18) |
| row 7's register text is stale | `BACKLOG.md:252` | ✅ still says *"Ten rulings Z-1 … Z-10"* and *"awaiting Paul's `ready:` stamp"* — both false (twelve; stamped 09-07) |
| plan §8 all DEFERRED, §8·7 REFUSED | read §8 | ✅ as stated |
| R-Z1 resolved free · R-Z2 use what is free · R-Z5 parked · R-Z6 closed by measurement | plan §9, §9a | ✅ |
| content-steward DRAFTING owed | plan header, seats line | ✅ *"review run 2026-09-07; DRAFTING still owed"* |
| `tools/fetch-frame.py` / `tools/frame-sources.json` | `ls` | ⛔ **neither exists** — assessment §8 step 2 writes "register entries" into a file that has not been created |
| Bob's address ever run through `anchors.py` | `.private/` listing | ✅ nothing there — R-A5 has not been done, consistent with GATED |
| R-Z6 fix (B+C+D) landed in `worker.js`/`wrangler.toml`? | not checked | ⚠️ the brief does not claim it; plan §9a says *"NOT WRITTEN, routed to the lane that owns the Worker."* I did not grep for a per-env zones switch. Unknown |

## 3 · The open decisions — Paul's, to bring to him in this window

1. **R-A1 … R-A6** (assessment §7), as the brief lists them. Two carry amendments the brief does not
   mention: **R-A4's field list changed** in the amendment — `footprint` (stored, CDLA-Permissive) ·
   `drivewayHint` (OSM, ODbL — *source + timestamp, not canon*; the record is the human's retrace) · `frame`
   · `tier` · `coverage`. And **tier X gained a threshold** (no footprint within 100 m → refuse and ask).
2. **Which set is the answer key** for R-Z4 — 23 in canon or 18 served — and the two copies are drifting.
   Bringing the served record up to canon is a change to the frozen instance and Paul's alone.
3. **The copy contradiction inside the plan** (§0 ②): is the completeness gap permanently normal (§6b) or a
   defect to grow out of (*"12 → 0 is progress"*)? Nobody has ruled.
4. **R-A6 in its sharpest form**: plan §8·4 DEFERS *"any automated extent proposal"* from the v1, while the
   assessment §5b proposes anchors written **at founding**, silently, as inferred facts. Both are stamped
   artifacts of this lane. R-A6 asks whether that is feature work under G1 — but it is also a question of
   whether the assessment amends the plan's §8·4 or contradicts it.
5. **The playbook line** the web-research seat proposed (*"check the shipped product before building the
   detector"* — NAIP building detection tops at IoU 0.43, Microsoft ships 0.75) — not written; Paul's call
   whether it is a second example under `feedback_check_standards_before_building` or a Fernwood pattern.

## 4 · What has NOT been tested or verified

- **The 18-zone served record** — measured once, 09-08, with the master token. Not re-probed today.
- **Whether the 09-08 session ran as its brief.** The brief calls this unverifiable. ⚠️ The file's own
  history is evidence the brief did not cite: the 09-08 brief was **edited twice that evening** —
  `71c31a6` (*"all six recommendations approved — the one in MY lane applied"*) and `f0d94f5` (*"record a
  live concurrency failure"*, which the brief itself attributes to *"the 09-08 zones window"*). A window
  that edits its own brief to record what happened to it was almost certainly running as that brief.
  Not proof; stronger than "the record does not say."
- **Everything the assessment lists under *"What I could not verify"***: OSM driveway coverage in rural
  Pickens (n = 1) · the NIR water threshold (band fetched, pond not tested) · the Georgia statewide parcel
  layer's terms (403 says *account*, not *free account*) · the parcel's acreage (R-A2) · whether
  `derive-property.py` can carry the anchor fields (docstring read, not the writer) · **and the IoU 0.76
  itself as a quality claim**: if the hand-traced `house` was drawn from a roof outline, the two agree by
  shared source. The 1.5 m agreement with the hand-confirmed Google Maps anchor is the independent control.
- **The licence reading** (CDLA vs ODbL) is the seat's, from the sources' own pages. Not independently read.
- **Every `file:line`** in the plan older than an hour — the tree moved twice during this readback alone.
- **The two read-only checks engineering pre-registered on 09-07** (POST the five capture endpoints at
  `home`; GET `/api/zones` at `home`) — plan §0 says *"neither has been run"*; §9a's `/health` probe
  answered the second by predicate, not by exercising the route. Still not exercised.
- **R-Z6 B+C+D** — whether any of it has since landed in the Worker lane. Not grepped.
- **`guard-concurrent.py`** — I read its `--help` only; I did not `start` a slot, because the brief warns a
  green check may be another session's baseline and I have not been cleared to work.

## 5 · What I would do first — after the readback is graded, in this order

1. **Nothing that writes, until graded.** Then `git status <file>` before every write; explicit-path
   `git add` only; small commits; never touch `cycle-state.json` or `digest.json`.
2. **Bring §3 items 1–4 to Paul in this window** — R-A2 and R-A3 are ten minutes of facts only he has
   (acreage and lot shape off qPublic; *is the 175 m² building at the east end of the driveway branch yours?*).
   The answer-key question decides what every later measurement is measured against. Record his words
   verbatim; **message refinement**, do not edit the row.
3. **Message refinement the register edits it is owed** (brief §7 + assessment § Register edits owed) so
   they are queued for when its freeze lifts — I cannot apply them.
4. **The one executable step that needs no ruling and no network: the amendment's ⑦ test** — buffer the
   OSM driveway at 2.5 / 4 / 6 m and score against `main-parking` and `lower-parking`, on cached JSON in my
   own directory. It decides whether *"derive the drive, the person draws the apron"* is real. The brief's
   §6 step list **omits this test**; the amendment inserts it between steps 2 and 3.
5. **R-A5 (Bob's address) only on Paul's explicit word**, and only to `.private/`, nothing sent.
6. **Step 2 of assessment §8** (`fetch-frame.py` register entries) — not from this worktree. See §6 below;
   the brief does not say who lands it.

## 6 · Where the brief left me unsure, or looks thin

1. **`LAND-SOURCES.md` is listed as MINE (§1) and its promotion edit is listed as REFINEMENT's (§7,
   assessment register edit 4).** One of those is wrong. My reading: I own the file; the *register* (rows
   7–9) is refinement's; the LAND-SOURCES promotion is a lane edit I may make. Please confirm.
2. **The "supersedes" sha is wrong.** The brief says the 09-08 brief lives at `9a762b0` — that commit
   (*GROOM & BUCKET continued*) does not contain the file. It was added at **`1092809`** (09-08 17:44) and
   last stood at **`f0d94f5`** before today's rewrite. Harmless, but a sha citation that fails
   `git show` is the class this repo flags.
3. **Who lands `tools/fetch-frame.py`?** The assessment says *"`tools/*` is a BUILD-window path — lands via
   the coordinator."* The brief's window table gives the build window three named files and
   `tools/journey-walk.py`; nobody is named for a new tool in `tools/`. If step 2 is mine to *write* but
   not to *land*, the brief should say where it is handed.
4. **Two scripts one letter apart.** `anchor.py` (09-08: the click-scoping experiment) and `anchors.py`
   (09-10: the downloads). The brief names only `anchors.py`; the experiment §9 cites `anchor.py`. Both are
   real and different. Worth a line so the next reader does not run the wrong one.
5. **The brief's "18 served vs 23 canon" is stated as if two copies exist.** There are three (file, inline
   `ZONES_DATA`, served KV), and the inline copy also says 23. Say which of the three, every time.
6. **§8's "no readback exists for the 09-08 session"** — true, but see §4: the brief's own edit history is
   evidence it does not use. The uncertainty reads larger than the record supports.
7. **The amendment's changes to R-A4 and the frame rule (tier X threshold, `drivewayHint`) are not carried
   into the brief's §5.** A reader who brings R-A1/R-A4 to Paul from the brief alone would present the
   pre-amendment version.
8. **"Bob is gate 3 of the cascade"** — I understand this as: address → frame → anchors (Paul confirms at
   Fernwood) → names → plants; Bob's data enters only after the Fernwood loop is proven. If "gate 3" means
   something more specific (a numbered cascade gate in a file I did not read), tell me which.
9. **G1 itself** — the brief cites *"the plan-of-record's G1 line"* without naming the file. I did not
   chase it; I am taking *"features are out of scope until G1 is met"* on the brief's authority. If G1's
   definition matters for R-A6, I need the pointer.
