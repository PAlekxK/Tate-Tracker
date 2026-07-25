# Fernwood — soil-sampling plan (by zone)
**2026-07-25** · owner: Paul (physical sampling) · unblocks the §2.3 / §5 soil findings in
`.engineering/2026-07-23-hyperlocalization-audit.md`

## Why this exists

The audit found the soil layer is unsound two ways at once:

1. **No soil test has ever been run** (Paul confirmed 2026-07-25), yet ~18 plant `soilNotes`
   assert a specific native pH ("4.5–5.5 range") and make amendment recommendations
   ("boxwood wants it sweeter") **as settled fact**.
2. The pH range those notes inherit comes from soil **series that cannot occur here** — the
   audit showed Cecil and Pacolet are Piedmont series capping at 900 ft, cited for a 2,959 ft
   property. So both the number *and* its provenance are wrong.

A $7–10 test per sample replaces the whole modeled layer with measured ground truth. And
because Fernwood already has a **zone model** (9 zones drawn), we can do it **by zone** —
which is worth doing, because soil pH genuinely varies across a property this varied (a limed
turf fairway, an acidic woodland edge, and a pond margin are three different chemistries).

**14 of 27 plant records want soil *sweeter* than the assumed native 4.5–5.5** (hydrangea,
dogwood, boxwood, holly, japanese-maple, clematis, hosta, butterfly-weed, wisteria, spiderwort,
fairway-turf, and others). If the real pH is higher than assumed — which the wrong-series
provenance makes entirely possible — a chunk of the app's amendment advice may be unnecessary
or backwards. That is the concrete stakes: we may be telling Mom to lime beds that don't need it.

## The test (UGA Extension, through Pickens County)

- **What:** UGA Routine Soil Test (S1) — pH, buffer pH (lime requirement), P, K, Ca, Mg, Mn, Zn.
  Add **organic matter** (~$5) on at least one sample; consider **texture/particle-size** on one
  bed sample to settle the audit's open Tallapoosa-vs-Ashe/Edneyville series question.
- **Cost:** ~$7–10/sample routine; some counties $15 first + $6 each additional. Confirm current
  Pickens County pricing when booking.
- **Where:** Pickens County Extension office supplies the bags + submission form and forwards to
  the UGA lab (Athens); results back in ~1–2 weeks, emailed, with lime/fertilizer recommendations
  keyed to a stated crop.
- **When:** **Fall is the ideal window** — it leaves time for lime (which acts slowly) to work
  before spring, and the lab queue is shorter than the spring rush. Target: this fall.

## Method (per zone)

For each sampling unit:
1. Take **10–20 cores** scattered across the unit (not one spot — soil is patchy). A trowel,
   auger, or a $15 soil probe all work; a probe is much faster for 20 cores.
2. **Depth by use** (this is why zones sample differently):
   - Turf / lawn: **4"**
   - Garden / perennial beds: **6"**
   - Trees & shrubs / woodland: **8–12"**
3. Composite the cores in a clean plastic bucket (not galvanized — zinc contamination), mix well,
   air-dry, fill the bag to the line (~2 cups).
4. Label with the **zone id** so results map straight back to canon.
5. On the submission form, state the intended planting per unit so the lime/fertilizer rec is
   relevant (e.g. "acid-loving shrubs" for the woodland edge, "fescue lawn" for the fairway).

## Which zones to sample — a tiered plan

There are 9 drawn zones. Testing all 9 is ~$70–90 and fine if Paul wants completeness, but the
chemistries cluster, so here's a **prioritized** cut. Recommend **Tier 1 now (5 samples, ~$50)**,
add Tier 2 if the results show spread.

**Tier 1 — distinct chemistries, high plant stakes (5 samples):**
| Sample | Zone(s) | Depth | Why it's its own sample |
|---|---|---|---|
| **Fairway turf** | `fairway` | 4" | Managed cool-season turf, likely limed history — the one unit expected to run *higher* pH. Governs `fairway-turf` advice directly. |
| **Ornamental beds** | `eastern-patio` + `western-garden` | 6" | The cultivated perennial/shrub beds — where the "wants it sweeter" plants live. The highest-stakes chemistry. |
| **Woodland / acid edge** | `fairway-fringe` + `lower-40` | 6–8" | Native forest-edge, expected most acidic — the baseline the azalea/mountain-laurel/dogwood ("acid is home") claims rest on. |
| **Pond margin** | `pond-area` | 6" | Wet, distinct; holds the two irises + lizard's tail + sarracenia (which *wants* acid/wet). Different moisture and chemistry. |
| **Upper wall / stable** | `upper-uber-wall-area` + `stable-grounds` | 6" | Disturbed ground near structures — often amended/limed by old construction; worth one read. |

**Tier 2 — add only if Tier 1 shows real spread (2 samples):**
`parking-bank` (compacted, roadbase-influenced) and splitting the combined beds/woodland units
if their neighbors diverge.

**Rule of thumb:** combine two zones into one sample only if you'd give them the *same*
amendment. The moment results (or your eye) say two zones differ, split them next round.

## How results fold back into the app

This is the loop-close — the same "modeled → measured" move the variety chip already does.

1. **Add a per-zone soil block to `zones.json`** — `soil: {phMeasured, bufferPh, testDate,
   sampleDepth_in, organicMatterPct, source: "UGA S1"}`. This is the SSOT: measured pH lives on
   the **zone**, not restated in every plant.
2. **Rewrite the ~18 plant `soilNotes`** to reference the zone's measured value instead of
   asserting a native range — and only where the plant's `zoneId` is assigned (see dependency).
   Where a plant has no zone yet, hedge the note honestly ("no test on this bed yet") rather than
   assert the old inferred range.
3. **Correct the series/pH provenance** in `property.json` per audit §2.3 (drop Cecil/Pacolet)
   regardless of test results — that fix doesn't wait on sampling.
4. **Property-card surface:** the Property card already recommends the $9 test. Once results land,
   flip that from a recommendation to a result ("tested Oct 2026: fairway 6.2, woodland 4.8…"),
   with the test date visible — measured, dated, honest.
5. **Mama's Perspective seed (optional):** "we finally had the soil tested — the beds by the
   patio came back sweeter than we thought" is a natural, non-extractive loop-close she'd notice.

## Dependency

The per-plant fold (step 2) is **gated on `zoneId` assignment** — 24 of 27 plants still have
`zoneId: null` (BACKLOG **W2**, Paul-driven). The **zone-level** capture (step 1) and the
**provenance correction** (step 3) do **not** wait on that and can land as soon as results are in.
Sampling itself waits on nothing.

## Checklist

- [ ] Call Pickens County Extension — confirm current price, get bags + forms
- [ ] Buy a soil probe (~$15–20) — pays for itself at 20 cores × 5 samples
- [ ] Pull Tier 1 (5 composited samples, labeled by zone id, correct depth per use)
- [ ] Add organic-matter to the ornamental-beds sample; texture to one bed sample
- [ ] Submit; log the submission date
- [ ] On results: add `soil{}` to `zones.json`; correct `property.json` provenance; re-inline; commit
- [ ] Rewrite `soilNotes` for zone-assigned plants; hedge the rest
- [ ] Flip the Property-card recommendation to a dated result

**Sources:** [UGA Soil Test Handbook (SB 62)](https://secure.caes.uga.edu/extension/publications/files/pdf/SB%2062_2.PDF) ·
[UGA C896 — Soil Testing for Home Lawns, Gardens](https://extension.uga.edu/publications/detail.html?number=C896)
