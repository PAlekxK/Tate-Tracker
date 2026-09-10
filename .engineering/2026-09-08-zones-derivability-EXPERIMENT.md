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


## 7 · ⭐⭐ PAUL'S DIRECTION FOR THE PROCESS — `[paul-stated 2026-09-08]`, and his hedge is kept

> *"At each point, we should be kind of checking **what can't we tell** from the different views. It
> definitely seems like we're able to identify the house and a few other distinct shapes, so **that'll
> also be the order in which we apply this.** … Let's see the derived edges, or what you would propose
> as candidates, and what that process would look like as a starting point. And also bearing in mind
> **how could it iterate** — like **what's the clearest thing to click, maybe the house and the
> driveway, and then that allows you to re-process around that.** **I'm not sure**, but that's what
> we're trying to figure out here."*

⚠️ **Recorded as a DIRECTION, not a ruling — his own hedge (*"I'm not sure"*) is part of it.** It is
not numbered into the `Z-` register, which holds settled rulings. Three things in it are load-bearing
and none was in the plan before today:

### ① ⭐ CONFIDENCE IS THE APPLICATION ORDER, and it falls out of §3 for free
*"We're able to identify the house and a few other distinct shapes, so that'll also be the order in
which we apply this."* — the derivability table **is** that order. It was computed as a *measurement*
and he has re-read it as a **schedule**. `inferred`

### ② ⭐⭐ "WHAT CAN'T WE TELL" IS A PER-STEP OBLIGATION, not a closing caveat
This is the completeness doctrine (§0 ③, *"the surface must show what it does NOT know"*) **applied to
the operator pipeline rather than to Mom's surface.** Every step declares its own blind spot:

| view | what it tells | ⛔ what it CANNOT tell |
|---|---|---|
| lidar slope 2018 | built edges — pads, cuts, patio rims, terrace rings | anything mown; anything regraded since 2018; ≥30° (**the ramp clips**) |
| NAIP texture, 7 dates | **THAT** an area is managed | **WHERE** the management stops (§6) |
| NAIP 2022-01 optical | the only leaf-off frame | it has the **longest shadows on the property** (1.52×) — an edge-follower snaps to shadow |
| any of them | extent | ⛔ **a name. 0 of 16, permanently** |

### ③ ⭐⭐ ANCHOR-THEN-REPROCESS — the genuinely new idea, and it is not in §5
*"What's the clearest thing to click, maybe the house and the driveway, and then that allows you to
re-process around that."*

⛔ **§5's four steps are a ONE-WAY CASCADE** — frame → edges → regions → names. **This is a LOOP**, and
it is a different architecture: each confirmed anchor **re-scopes the search for the next one.**
`inferred`

⭐ **It is Z-11's cascade, re-derived on the operator side.** Z-11 says each ask to the householder is
scoped by her previous answer. This says each *derivation* is scoped by the operator's previous
confirmation. **Same shape, different actor** — and neither was reached from the other, which is the
strongest evidence the shape is real.

**Why an anchor buys more than one border, concretely:** the `house` is the highest-confidence object
in the frame (89th pctile on break-of-slope, 6.5 on raw slope — a flat pad with a sharp rim, which is
physically exactly right). Confirming it fixes **scale, orientation and a datum in a 2018 surface**.
Nine of the small planted zones sit within ~40 m of it, and their permutation scores are middling
largely because a ±12 m rigid shift is a *large* fraction of their own size — a constraint the house
edge would remove. `proposed`

---

## 8 · THE CANDIDATE PROCESS — what I would propose, as the starting point he asked for

⛔ **PROPOSED. Not built, not run.** §§1–6 are measurements; this section is design, and it is graded
as such so the two are never quoted at the same weight.

### The loop

```
   ┌─ 0 · FRAME ─────── downloads, not inferences (§5 step 1, unchanged)
   │
   ├─ 1 · ANCHOR ────── FETCH the anchors; PROPOSE only what no download covers.
   │                    (amended 2026-09-10, assessment §0: the house and the driveway are
   │                    DOWNLOADS — Microsoft footprint IoU 0.76, OSM way 9 m from the house.
   │                    Only main-parking is still a proposal: OSM gives a line, not the apron.)
   │                    Operator clicks ACCEPT / NUDGE / REJECT — the first card is "is this your house?"
   │        ⛔ REFUSE to propose anything below a confidence floor at this step.
   │
   ├─ 2 · RE-SCOPE ──── each accepted anchor CONSTRAINS the rest:
   │                    · a datum for the 2018-vs-2026 offset
   │                    · a local search radius for adjacent features
   │                    · a texture EXEMPLAR (mown grass sampled INSIDE the lawn)
   │
   ├─ 3 · PROPOSE ───── next tier of candidates, now cheaper and tighter
   │                    ↺ back to 1 until nothing clears the floor
   │
   └─ 4 · HAND OVER ─── ⭐ the remainder is stated as a REFUSAL, never a weak guess:
                        "these borders are not visible to any view we have — draw them"
```

### What each step emits, and the one rule that makes it honest

⭐⭐ **A candidate carries the VIEW it came from and what that view cannot see.** Not a confidence
number alone — *"from the 2018 terrain, which cannot see anything regraded since"* is actionable where
`0.87` is not. **This is the honesty encoding the plan already requires, moved onto the operator
track**, and it is what §5b's dead gradient-confidence idea was reaching for and got wrong.

### Three things it must NOT do — each is a trap this repo has already paid for

1. ⛔ **No cosmetic smoothing under an accuracy label** (§5b ②). Tier 1 shipped 09-04 and *"the map
   does not look meaningfully better."* A candidate that looks crisp because it was smoothed is the
   confidently-wrong instrument.
2. ⛔ **Never auto-accept.** *"We draw, they confirm"* means the machine proposes and a human rules —
   and at this step the human is **Paul**, not Mom. Nothing here reaches her.
3. ⛔ **Never fit a 2026 polygon to the 2018 surface.** The bounds file's own warning: where they
   disagree, the first hypothesis is **work done since**, not a bad trace.

### The first executable step, sized

~~**Render the break-of-slope ridges near the house as candidate polylines** beside the traced answer
key. **It answers the question that decides the whole approach: is a derived edge something a person
would ACCEPT, or is it a suggestive smear?**~~ ✅ **RUN — §9.** Answer: **neither.** It is a set of
real, acceptable FRAGMENTS that never close into a place — and the anchor's value turned out to be
scoping rather than extraction, which retires step 1 of the loop above as I drafted it.


## 9 · ⭐⭐ THE CANDIDATE RENDER — RUN `[paul-ruled 2026-09-08: "go ahead, run the candidate render"]`

**§8's first executable step is discharged.** Exhibit: `.engineering/zones-derivability/candidates.png`
(three panels, staged to `~/Desktop/ATTACH-THESE`). Code: `ridges.py`, `anchor.py`. `measured`

### ⛔ FIRST, THE NEGATIVE RESULT, because it is the bigger finding

**Seeded region-grow FAILS. Two formulations, both refused.** The obvious reading of *"click the
house and re-process around it"* is: operator clicks, machine returns a polygon. **It does not work.**

| formulation | idea | result |
|---|---|---|
| **slope-similarity** | grow while slope stays within 6° of the seed's | **6 of 10 leaked** past 400k px and were REFUSED — *including `house`*. Best IoU **0.40** |
| **break-as-barrier** | grow but never cross a ridge (watershed) | **worse** — 8 of 10 leaked. Best IoU **0.30** (`lower-40`) |

⭐⭐ **The cause is one sentence: THE RIDGES HAVE GAPS.** A rim with a single-pixel hole is not a
barrier, and a flood fill finds the hole every time. **There is no closed contour anywhere in this
frame.** ⛔ **Nothing was returned as a guess** — a runaway grow returns `None`, by construction.

### ✅ WHAT THE MACHINE *CAN* OFFER: fragments, and they are real

70 components ≥40 px; **8 span more than 40 m**; mean extent 18.5 m.

**Null control (200 rigid shifts, ±12 m) — because 98% coverage is exactly the number to distrust:**

| set | true border | a WRONG nearby border | lift |
|---|---|---|---|
| ⭐ the **7 TERRAIN-recoverable** zones | **98%** | 77% | **+21%** |
| ⛔ the **6 mis-led** zones | 63% | 65% | **−3%** |

**The split from §3 reproduces on a completely different statistic.** ⚠️ **And the raw 98% is
misleading on its own** — a wrong border already scores 77%, because ridge material is dense in the
built core. **Only the lift is evidence.**

⛔ **Precision is 45%.** *Fifty-five per cent of what the machine offers corresponds to nothing the
operator drew* — mostly drainage lines in woodland, visible as the red streaks in panel 3.

### ⭐ THE ANCHOR EARNS ITS KEEP — but not the way it was proposed

`house` cannot be *grown*. But **one click on it removes 41 of 70 candidates** (60 m radius →
**29 remain**). ⭐ **So the anchor's value is SCOPING, not extraction** — it cuts the operator's
accept/reject work by **59%** without deriving a single boundary.

> ### ⭐⭐ THE FINDING THAT CHANGES THE DESIGN
> **The machine proposes EDGES TO SNAP TO. It never proposes a PLACE.**
> Closure is the human's, and that is not a limitation to engineer away — **it is §5 step 3 exactly as
> written** (*"the regions | Paul, but now easy | closed against edges that already exist"*). ⭐ **The
> pipeline was right and the reason is now measured**: the edges exist, they simply never close.

⚠️ **This retires the region-grow idea in §8's step 1, which is mine, not Paul's.** His words —
*"what's the clearest thing to click… and then that allows you to re-process around that"* — survive
intact and are **supported**: the click re-scopes. It was my reading of it as *extraction* that the
measurement kills.

### What the exhibit shows, in one line each

| panel | |
|---|---|
| **STEP 0** | 70 fragments over the whole property — candidates in the woods that mean nothing |
| **STEP 1** | one click on the house; 29 survive; the rest go grey |
| **STEP 2** | green where a fragment sits on a traced border, red where it matches nothing. ⭐ **Green clusters in the built core; red runs through woodland and along the meadow** |

⭐ **`the-meadow` draws almost no candidates at all (13% coverage)** — visible as empty ground in every
panel. §6 already said why: it is a **region**, not an edge, and this is that finding rendered.


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

This file, plus ✅ **`.engineering/zones-derivability/`** — `geo.py`, `raster.py`, `field.py`,
`derivability.json`, `mowing.json`, `README.md`. The exhibit `zones-derivability.png` is staged to
`~/Desktop/ATTACH-THESE` (not committed — 1.1 MB, regenerable).

⚠️ **Deliberately not in `tools/`** — BUILD owns that path this lap, and Z-9 rules the operator layer
scaffolding.

⛔ **CORRECTED 2026-09-08, same session:** this section and the QA section below originally said the
code lived in the session scratchpad and was *"re-runnable"* from there. **The scratchpad is
session-scoped and dies with the window** — the claim was false the moment it was written, and it is
this corpus's own most-repeated shape (*a capability the loop cannot reach by running its own
procedure is not a capability it has*). The code is now landed and was re-verified from its new home:
frame identity ✅, `house` = 139.2 m² ✅.

## QA

Re-runnable from `.engineering/zones-derivability/`; deterministic under `seed 20260908`. The three
preconditions in §1 are the QA: frame identity, ramp direction, and the `house` footprint sanity
check. **If any of the three stops passing, every number in §3 is void.** `assert_same_frame()`
refuses rather than warns, so precondition 1 cannot be skipped silently.
