# ZONES — can the map be RECREATED systematically? A measured first answer

- row: BACKLOG.md ▶️ NEXT · TIER 2 · 7 (the zones epic) — the standing research strand `[Z-8]`
- objective: O3
- class: engine · declared
- kind: design
- question: `[paul-ruled 2026-09-08]` *"We need to recreate the zones systematically. We can use the
  zones I've already drawn as a reference/answer key roughly"* + *"let's build this tool… all in dev
  and just test it out for Fernwood since we already have all the pictures there… let's see
  programmatically and experiment how this would actually work."*
- seats: none commissioned — this is a measurement, not a design. It EXISTS to tell the seats what is
  worth designing.
- depends-on: .plans/2026-09-07-zones-PLAN.md
- stage: concept
- gate: ⛔ **NOTHING SHIPPED.** No deploy, no origin, no canon write, no `zones.json` edit, no paid API,
  no network call except the read-only probes already recorded in the plan's §9a. Dev only, as ruled.
- stage-note: 2026-09-08 ET — run in the zones window. Code lives in the session scratchpad, NOT in
  `tools/`, because the BUILD window owns `tools/*` this lap and because Z-9 rules the operator layer
  **scaffolding**: it is not worth a permanent home until it earns one.

**Grades:** `measured` (run at HEAD today) · `inferred` (from two measured facts) · `proposed` (mine).

---

## 0 · THE ANSWER IN ONE LINE

⭐⭐ **Terrain recreates the BUILT places and cannot see the MANAGED ones — and the split is clean
enough to plan around.** Of 23 zones, **7 borders are recoverable from free lidar already on disk**,
**6 are actively mis-led by it**, and **10 carry no signal either way.** `measured`

⛔ **That is not a disappointment; it is the shape of the pipeline.** It says Z-5's structure-first
ordering is not merely *cleaner* — **the structure is the only part a machine can do at all.**

---

## 1 · WHAT WAS RUN — and the three checks that had to pass first

| check | result |
|---|---|
| **Frame registration** — is the lidar really drop-in? | ✅ `measured`. Bounds are **byte-identical** to `base-naip-2022-01-leafoff`, both 1500×1500. **Verified, not trusted.** 0.306 m/px, 459 m square |
| **Ramp decode** — the slope PNG is **RGB, a 491-colour ramp, not grayscale** | ⚠️ `convert("L")` on a colour ramp is the *match-the-payload* trap: it returns a plausible number that need not be monotonic. **Direction established empirically instead** — see below |
| **Georeferencing** — do the polygons land where they should? | ✅ `measured`. `house` rasterises to **139 m² (~1,500 sq ft)** — a real house footprint. 23 zones total **10,674 m² = 2.64 acres** |

### ⭐ The ramp direction was read off the answer key, not assumed

| zone | mean ramp | what its NAME claims |
|---|---|---|
| `the-bank` | **143.8** | a bank — steep |
| `the-bluff` | **149.7** | a bluff — steep |
| `the-turf` | 200.5 | mown — gentle |
| `the-meadow` | **216.5** | meadow — gentle |

**The terrain layer ranks the zones in the order their names imply**, with the two steep-named zones
darkest and the two gentle-named lightest. `measured`. That is what licenses `convert("L")` here —
monotonicity was **checked**, and it is also independent evidence the lidar carries real signal about
these particular places.

---

## 2 · THE TEST — and why the obvious one had to be thrown away

**First attempt (discarded): boundary gradient vs. interior gradient.** Median ratio **1.07**, 14 of
23 above 1.0. Reads as "no signal" — but it is **confounded**: nine planted zones are 12–25 px across,
so their "interior" pixels sit within a few px of their own boundary and both samples hit the same
ground. **The test could not answer the question for exactly the zones that matter most.**

**What replaced it: a permutation test.** Each zone's own polygon is rigidly shifted **200 times** by
up to **±40 px (±12 m)** — a plausible mis-trace — and the true border's mean statistic is ranked
against those. Deterministic (`seed 20260908`). ⭐ **This asks the question an edge-follower actually
faces: is the TRUE border better than a NEARBY WRONG one?**

Two competing hypotheses were run, because they are different physics:

| | hypothesis | result |
|---|---|---|
| **BREAK** | a border is a line where slope **CHANGES** (`\|∇slope\|`) | ⭐ **the discriminator** — 5 zones ≥90th pctile, 4 ≤10th; it *separates* |
| **WALL** | a border is a line of **HIGH slope** | ✂️ mushier — median 64, only 2 ≥90. Retains less |

⭐ **Internal validation nobody designed for:** `house` scores **89 on BREAK and 6.5 on WALL** — a flat
pad with a sharp rim. That is physically exactly right, and it is the strongest evidence the
instrument is measuring what it claims.

---

## 3 · THE RESULT

| ✅ recoverable (≥85th pctile) | | ⛔ terrain points the WRONG way (≤15th) | |
|---|---|---|---|
| `eastern-patio` | 97.5 | `western-fern-azalea-garden` | 8.5 |
| `lawn` | 97.0 | `the-bluff` | 9.0 |
| `main-parking` | 95.0 | `the-green` | 10.0 |
| `fern-garden` | 90.5 | `the-meadow` | 10.0 |
| `lower-40` | 90.0 | `stable-grounds` | 13.0 |
| `house` | 89.0 | `lower-parking` | 15.0 |
| `the-green-ring` | 85.5 | | |

**No signal (10):** `the-bank` 59 · `the-turf` 31.5 · `pond-area` 44.5 · `eastern-woodlands` 44 ·
`st-francis-garden` 35 · `the-green-terrace` 56 · `western-upper-patio` 44.5 · `western-lower-patio`
59 · `western-garden` 65.5 · `hosta-garden` 69.5. `measured`

### ⭐ What the two columns actually are — `inferred`

The recoverable set is **small, hard-edged, and near the house**: a patio rim, a parking cut, a lawn
edge, a building pad, a terrace ring (43–169 m²). The mis-led set is dominated by **large open
expanses** — `the-meadow` alone is 4,761 m².

⭐⭐ **And the inversion is the most useful single finding here.** `the-meadow`'s true border sits on
*flatter* ground than a random nearby placement. Read physically: **its border is the edge of MOWING,
not a landform.** Shift it any direction and it climbs the valley sides. So the second class is not
"hard" — **it is a MANAGEMENT boundary, and terrain is the wrong instrument for it by construction.**

⭐ **The plan already names the right instrument and did not know it was for this:** the standing
research strand's live item **"the mowing-regime time-series test"** (§7). Seven NAIP frames,
2010→2023, at identical registration. **A mown edge is visible as a texture/tone boundary that
persists across dates and moves when management moves.** `proposed`.

---

## 4 · WHAT THIS DOES TO THE PIPELINE (§5)

| step | §5's claim | this experiment |
|---|---|---|
| **1 · the frame** | downloads, not inferences | untouched — still right |
| **2 · the edges** | model proposes · Paul accepts | ✅ **supported, and now SCOPED**: terrain proposes the *built* edges credibly. It must not be pointed at meadow/turf borders |
| **3 · the regions** | closed against edges that already exist | ⚠️ **this is where the honest limit sits.** Only ~7 of 23 borders have a terrain edge to close against |
| **4 · the names** | 0 of 16 derivable, permanently | untouched |

⭐⭐ **Z-5 is strengthened and made concrete.** *"Build from points of interest and walls, then
subdivide"* is not a preference about tidiness — **the walls are the part that exists in the data**,
and the subdivision is where the human is irreplaceable. `inferred`

---

## 5 · WHAT THIS IS NOT — stated before anyone quotes the 7

- ⛔ **n = 23, one property, one operator.** Nothing here generalises to household N yet.
- ⛔ **The permutation favours small distinctive features.** A ±12 m rigid shift moves a 43 m² zone
  clean off its feature and a 4,761 m² zone barely off itself. **The two columns are not on one
  scale** and must not be ranked against each other.
- ⚠️ **THE LIDAR IS 2018; THE GROUND IS 2026.** The bounds file's own warning is load-bearing here:
  the western garden and patio area *"we have kind of reshaped with heavy equipment."* Those four
  zones score **44.5 · 59 · 65.5 · 69.5** — middling, exactly as a stale surface would read. ⛔ **A low
  score there is first evidence of WORK DONE SINCE, never a bad trace.**
- ⛔ **This measures a DERIVABILITY CEILING, not correctness.** It says how much of a hand-drawn map
  terrain could have proposed. It does not say the hand-drawn map is right.
- ⚠️ **The ramp is CLIPPED at 30°** — 8.7% of the frame sits on the floor, and 30° cannot be told from
  45°.

## Falsifier

- **The split is falsified** if re-running with a non-rigid perturbation (per-vertex jitter) collapses
  the two columns together — that would mean the test measured *feature size*, not *derivability*.
- **The mowing hypothesis (§3) is falsified** if the seven NAIP frames show no persistent tone
  boundary along `the-meadow`'s traced border. ⭐ It is cheap and it has not been run.
- ⛔ **The whole approach is falsified for the v1** if Paul's answer key is itself not stable — and
  `[paul-stamped 2026-09-08]` is *"our best answer so far,"* which is deliberately not a survey.

## Files touched

**None tracked but this file.** Experiment code (`geo.py`, `raster.py`, `field.py`), the derivability
table (`derivability.json`) and the exhibit (`zones-derivability.png`) live in the session scratchpad
and are staged to `~/Desktop/ATTACH-THESE`. ⚠️ **Deliberately not in `tools/`** — BUILD owns that path
this lap, and Z-9 rules the operator layer scaffolding.

## QA

Re-runnable from the scratchpad; deterministic under `seed 20260908`. The three preconditions in §1
are the QA: frame identity, ramp direction, and the `house` footprint sanity check. **If any of the
three stops passing, every number in §3 is void.**
