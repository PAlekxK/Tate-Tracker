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

## 6 · ⭐⭐ THE FALSIFIER WAS DISCHARGED THE SAME SESSION — and it corrected §3

§3 proposed the standing strand's **mowing-regime time-series test** as the instrument for the
borders terrain cannot see. **It was run immediately.** All seven NAIP frames (2010→2023, sun 33°→64°)
are **byte-identically registered** to the lidar frame — verified, not trusted.

### ⛔ First operationalisation: FALSIFIED

*"A mown edge is a persistent texture boundary."* Tested as `|∇(local range)|` on the border,
permutation-ranked per frame. **`the-meadow` scored a median 51.7** across the seven frames
(98·62·48·74·24·52·38) and **`the-turf` 55.0** (30·9·8·98·89·71·55) — squarely in the noise band
against a prediction of ≥85, and **wildly unstable frame to frame.** `measured`

⭐ Only **`lawn`** behaved as an edge (94.2 texture, 97.0 terrain) — the one zone both instruments
independently agree on.

### ✅ Second operationalisation: STRONGLY SUPPORTED — and it is a different claim

⛔ **Killing the hypothesis on one operationalisation would have been this corpus's own named error.**
The edge test asks *"is the border on a texture step?"*; the honest question for a management boundary
is *"is the inside different from the outside?"* Re-run as interior vs. a 1.15× dilated ring:

| zone | median ratio | per-frame (2010 → 2023) |
|---|---|---|
| ⭐ **`the-meadow`** | **0.71** | 0.55 · 0.71 · 0.65 · 0.67 · 0.80 · 0.90 · 0.82 |
| `house` | 0.84 | roof — smooth by construction |
| `the-turf` | 0.86 | 5 of 7 frames below 0.90 |

**`the-meadow`'s interior is distinctly smoother than its surround in ALL SEVEN FRAMES across thirteen
years.** That is a real, persistent, multi-date signal — and terrain scored the same zone **10.0**.

> ### ⭐⭐ THE CORRECTED FINDING, and it changes the algorithm class
> **The managed areas are detectable as REGIONS, not as EDGES.** Texture finds *that* the meadow is
> mown; it does **not** find *where* the mowing stops. Terrain finds the built edges; it cannot see
> the meadow at all.

⚠️ **This is a real amendment to §5**, which frames every step as an edge and whose §5b debates
livewire — an **edge-following** algorithm. For the managed half, **edge-following is the wrong
algorithm class**: it wants region-growing off a texture seed, with the line itself left to the
person. `inferred`

⚠️ **The region test has power only for LARGE zones.** Seventeen of 21 testable zones sit at
0.92–1.14 — no contrast — because a small zone's ring is tight and noisy. It is an instrument for
`the-meadow` and `the-turf`, not a general one. `measured`


## Falsifier

- **The split is falsified** if re-running with a non-rigid perturbation (per-vertex jitter) collapses
  the two columns together — that would mean the test measured *feature size*, not *derivability*.
- ~~**The mowing hypothesis (§3) is falsified** if the seven NAIP frames show no persistent tone
  boundary along `the-meadow`'s traced border.~~ ✅ **RUN 2026-09-08 — §6.** Falsified as an EDGE,
  supported as a REGION. The prediction was right about the signal and wrong about its shape.
- **The region finding is falsified** if the 0.71 contrast is an artifact of the dilation ring
  reaching into woodland — i.e. if it measures *meadow vs forest* rather than *mown vs unmown*. ⚠️
  **NOT YET SEPARATED**, and it is the obvious next control: test the ring against the unmown
  meadow margin only, not the tree line.
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
