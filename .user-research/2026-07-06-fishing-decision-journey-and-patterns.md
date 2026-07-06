---
type: journey
project: fernwood
journey_id: fishing-decision
last_updated: 2026-07-06
evidence_level: inferred
performer: Paul (builder-and-user hybrid — see caveat)
sources:
  - Distilled arc of Paul's 12 session decisions/nudges (2026-07-06, reworking the Fishing section)
  - fishing.json (conditionsModel, waterTempGuide, historicalWaterTemp — this session's build)
  - .ux-reviews/2026-07-06-fishing-forecast-refinement.json + fishing-section-reorg.json (ux-expert)
  - Tate-Tracker/CLAUDE.md (tone, backlog item), _about-paul.md, fernwood.md patterns
---

# Fishing decision — JTBD, journey, and reusable patterns (Lake Sequoyah)

> **Evidence caveat — read first.** Paul is both the builder and the primary user of this
> surface (he confirmed Fishing is "basically HIS surface," can run tactical unlike Mom's
> plant prose). His nudges are unusually strong signal — they *are* a user telling you what
> the job is. But they are **one person's stated design intent, not observed fishing-decision
> behavior**, and a builder's mental model is not a naive user's. So almost everything here is
> tagged **`inferred`** (his own words, indirect signal), never `validated`. The one cheap
> upgrade to `validated` is a think-aloud the next time Paul actually plans a Sequoyah trip
> (see "Applicable for the future" #3). Both ux-reviews independently flagged the missing
> fishing JTBD artifact — this is it, at the honest evidence level.

---

## 1. Job-to-be-done

**One-liner (his words, condensed):**
> *When I'm at the property or planning a day and thinking about fishing Lake Sequoyah, I want to glance and know whether it's worth going out today or tomorrow, what times to prepare for, and what gear to bring — so I can spend my scarce on-water time on the actual bite instead of guessing.*

This is a **decision job**, not a browse job. The deliverable is a go/no-go + a window + a
kit — "everything else about seasons is helpful context, but establish [the decision] as the
clear top-line takeaway" (nudge #7). "I won't be fishing the entire day" (#11) — time is the
binding constraint; the job is to spend it well.

### Functional dimension `inferred`
- Answer three things, in order: **is it worth going (today/tomorrow)? · when (which windows)? · what to bring (species/phase → gear)?**
- Time is scarce and non-continuous — he fishes *windows*, not days. "The valuable information of the peak times of each day is getting lost in the averaging" (#10). The job fails if the tool hands him a daily rating that buries the prime hour.
- Avoid the wasted trip / the wrong-window trip.

### Emotional dimension `inferred`
- **Trust is the load-bearing emotion.** His stated problem #1 was a *model he couldn't believe*: spring and fall lit up as "the same phase," two verdicts could contradict, color-coding was unexplained. A tool that's confidently wrong is worse than one that's honestly unsure — "let's not be false about how accurate we are" (#9). Confidence in the tool, not just confidence in the fishing.
- The quiet pleasure of a **well-timed** outing (hitting the falling-barometer feeding window) — competence, not urgency.
- Field-journal appreciation still lives underneath the tactics (the lake's Sam-Tate history, the place) — but on this surface it's demoted below the decision.

### Social dimension `inferred` — thin, and that's a finding
- Largely a solo/instrumental surface. Unlike the plant surfaces (make-or-break Mom, shared stewardship), Fishing has **no second make-or-break user** — Paul explicitly claimed it as his. The register can run warmer/more tactical as a result.
- Latent only: the property + lake are family-shared, so a "worth going this weekend" read *could* seed an invite. Not evidenced this session; noted, not built on.

---

## 2. Customer journey — "deciding whether/when to go fishing"

Mapped to Paul's stated **top→bottom hierarchy** (#12): immediate conditions + next ~4h at the
top → today's dawn/dusk windows → a less-granular multi-day view that **excludes bad times** →
quiet season context → per-species + annual-rhythm reference at the bottom.

| Stage | User need (his words where possible) | Emotion (-2..+2) | Which data source earns this stage | Friction the rework fixes |
|-------|--------------------------------------|:----------------:|-----------------------------------|---------------------------|
| **1. Impulse** — "could I fish today or tomorrow?" | An immediate, trustworthy top-line read the second the section opens | +1 | **On-site station (~0.3 mi)** — pressure/rain/wind; freshest + most local | Live pressure was buried at the *bottom* → "makes me feel like it's not that recent" |
| **2. Go / no-go (today)** | One verdict he can believe — not two engines racing | 0 → +1 if it reads clean | **conditionsModel** (season sets the ceiling; today's live signals set where you land under it) | Two contradicting verdicts (live star vs calendar worth-bar); multi-phase "NOW" from a single temp |
| **3. When (today)** | The peak windows, ranked, chronological dawn→dusk; "next 4 hours and how it shapes the next 24h" | +1 | **Sunrise/sunset (deterministic)** + pressure trend; **solunar down-weighted** | Windows ordered by *type* not clock; unexplained color legend; no bite-quality rank; **averaging hid the prime hour** |
| **4. Look ahead (this week)** | Less-granular multi-day view that **excludes** the times not worth going; confidence softened with horizon | +1 | **Near-term forecast (Open-Meteo)** — extended only as far as the data is clean | Every day got today's full granularity incl. slow windows → a wall of rows he has to reject himself |
| **5. Prep (gear/tactics)** | What to bring for the species/phase that's actually on | +1 | **Per-species phase model** (biology + angling research) + gear reco | Tactics buried; hype/urgency copy ("go now before it hits") fractured the calm read |
| **6. Deep reference** (planning a specific outing / off-season) | Full annual arc, per-species behavior, regs, lake lore | +1 (appreciation) | **Research library + DNR regs + season calendar + lake history** | Annual-rhythm content (12-mo strip, temp chart) was scattered mid-scroll instead of pooled at the bottom |

**The spine of the journey is freshness-descending / commitment-ascending:** the surface opens
on the fastest, most-local signal (does today work?) and descends toward the slowest, most-durable
(what is this lake, across the year?). Each source earns its altitude by **how fast it changes and
how directly it drives the decision** — not by how "important" or data-rich it feels.

### How the four sources fuse (the data-fusion picture)
1. **On-site Ambient station (~0.3 mi from the lake)** — the *unique local asset*. Pressure trend, rain/runoff, wind. Freshest + most local → **owns the top** ("NOW"). A generic fishing app cannot match a barometer a third of a mile from the water.
2. **Near-term forecast (Open-Meteo)** — extends the read forward; **sets the horizon** (a clean week, or only six hours — the data's reach decides, not a fixed template).
3. **Season / water-temp model** (angling biology + NOAA 1991–2020 normals, elevation-adjusted for 2,800 ft + thermal lag) — the **master driver but slow-moving**: it sets the *ceiling* on what's possible, then gets **demoted to a quiet context line**, carried honestly as an ESTIMATE (air-temp-derived), never crowned as the headline number.
4. **Domain research** (weighted: 2023 peer-reviewed study → temp strongest; pressure = consensus; **solunar explicitly down-weighted**, no correlation found) — this doesn't render as a stage; it **governs the weighting** of every other signal, so presentation weight follows evidence strength.

---

## 3. Reusable patterns (candidates for the pattern library)

These are the transferable principles beneath Paul's nudges. Presented as **proposals** — per
Mode 2, I don't silently write them into `cross-project.md` / `fernwood.md`. Several overlap
with candidates the ux-expert already logged this session (noted inline); Fishing gives some of
those their **second occurrence**, which is the bar for promotion.

**P1 · Decision-first over data-first** `inferred`
The surface's deliverable is the *decision* (go/no-go + window + kit), not a pile of facts. Lead
with the verdict; everything else is supporting context. → *Weather card* (lead with "what today
means for you," not a temp readout); *plants "peak this week"* (already moving this way — lead with
the plant **and its action**); *wildlife*. Cross-project: *financial viewer* (lead with the read,
not the data table).

**P2 · Right-altitude / anti-averaging** `inferred`
Keep granularity where the value lives. "The valuable information of the peak times... is getting
lost in the averaging that's giving us a daily rating." Don't roll a spiky, actionable signal up
into a smooth summary that hides the spike. → *plants peak-this-week* (per-window, not monthly dump);
*weather* (the actionable hour vs the daily average). Cross-project: any rollup/dashboard rating —
don't average away the thing worth acting on.

**P3 · Freshness must read as fresh** `inferred`
The most live, most local signal earns the top; **position encodes recency**. Live data buried low
reads as stale ("makes me feel like it's not that recent"). → *weather tile*; any live surface.
Cross-project: *financial viewer* (latest print up top). *(= ux-expert's candidate "Freshness sets
altitude" — Fishing is the pattern's 2nd occurrence; ready to promote.)*

**P4 · Horizon follows data confidence** `inferred`
Let the data's actual predictive reach set the forecast window — "don't make an arbitrary forecast
for today and tomorrow if the data's there to make it clean for a week. If it's only the next six
hours, do that." Don't fake precision to fill a template. → any forecast/projection surface.
Cross-project: *financial projections*, career-pipeline timing.

**P5 · Honest uncertainty / no false precision** `inferred`
An estimate must stay legibly an estimate **all the way through** — hedge near boundaries, never
launder a model read into apparent measurement. "Let's not be false about how accurate we are." →
*water-temp estimate* (air-derived, "$15 thermometer is the real tool"); *Garden Guru* honest-uncertainty
register; OCR/vision globally. Cross-project: *financial theses*, *Hillyer*. *(Ties to the global rule
"model-read values are hypotheses until verified.")*

**P6 · Leverage the unique local asset** `inferred`
Build the surface around the signal that's *uniquely yours* and can't be commodity-matched. The
on-site station 0.3 mi from the lake is the differentiator no generic fishing app has — so it earns
the top of the surface. → *elevation-adjusted phenology* (the property runs 8–12°F cooler → spawn +
bloom timing shifted, already baked in); *Bortle-3 dark sky*; *Etowah darters*. Cross-project: every
project has a proprietary signal (*financial own-series data*; Paul's *meta-stack* as a career asset).

**P7 · Source-hierarchy drives layout** `inferred`
Before designing a multi-source surface, **audit the sources and rank them** by evidence strength ×
freshness × actionability — then let that ranking drive presentation order and weight. Paul asked for
exactly this: "an audit of the SOURCES... to decide their priority, and let that drive presentation."
The fishing `conditionsModel` encodes it literally (weighted signals). → any multi-source Fernwood card.
Cross-project: *financial viewer* signal stack; *career* (which evidence leads a pitch). *(Companion to
ux-expert's "weight the surface by evidence strength, not grid symmetry.")*

**Two more, briefly:**

**P8 · Single-proxy conflation smell** `inferred` — *Paul's own diagnostic.* He caught the spring/fall
bug by feel: "the *same* behavioral cycle shown in both seasons." When one input variable (water temp)
maps to a state, but two genuinely different real-world situations share that input, a single-variable
model will conflate them — that's the tell the model needs a **second axis** (here: season / direction
of travel). Watch for it anywhere a state is derived from one proxy. Cross-project: any classification
off a single feature.

**P9 · Audience-calibrated register, per surface** `inferred` — Fishing is Paul's tactical surface, so
it can run **warmer and more tactical** than Mom's plant prose — *but* still no urgency/hype ("worth a
cast at dusk," never "BITING NOW!"), and the no-glasses legibility floor still binds because it renders
on the **shared** dashboard. One project, multiple audience registers; calibrate per surface, don't
flatten. *(Refines fernwood.md's "confidence cuts both ways" with a per-surface segmentation.)*

---

## 4. Applicable for the future

1. **The Weather card is the next surface to get this treatment.** It's the sibling of the Fishing
   panel and almost certainly carries the same failure the fishing rework fixed — a slow-moving
   temperature crowned as the field-journal headline (the ux-review's F5 explicitly cited the
   "weather-tile precedent"). Apply P1 + P3 + P5 there: lead with meaning, freshest signal on top,
   estimate stays an estimate.

2. **`conditionsModel` is a reusable engine template, not a one-off.** A deterministic, AI-free,
   evidence-weighted, source-ranked "should I / when should I" generator — the aquatic sibling of
   `computeLookFors` / `plantsAtPeakThisWeek`. The next candidates that fit the mold: **wildlife
   activity windows** (when's the deer/turkey/bird movement worth watching) and any future "is now a
   good time to X" surface. The pattern is proven twice now (plants, fishing).

3. **Validate the JTBD cheaply — one think-aloud.** This whole journey is `inferred` from Paul's
   design nudges, not observed behavior. The next time Paul actually plans a Sequoyah trip, have him
   narrate what he checks, in what order, from where, before he built any of this into the tool. That
   single self-ethnography upgrades the user_context from `inferred` → `validated` and is the exact
   follow-up both ux-reviews requested. (He is a legitimate user here — this is allowed, as long as
   we capture *revealed* behavior, not just *stated* intent.)

4. **Promote patterns on the second occurrence, not the first.** P3 (freshness sets altitude) and P7
   (evidence-weighted layout) now have a 2nd occurrence between the ux side and here — ripe to move
   into `cross-project.md` on Paul's go. The rest hold at 1 solid occurrence; log them, watch for the
   repeat before generalizing. (Evidence discipline — don't over-generalize from one surface.)

5. **Close the honesty loop by grounding the estimate.** P5 + P6 together point at one concrete move:
   wire the **real measured water temp** already in the app (USGS Etowah 00010 / the on-site station)
   in as a *calibration anchor* for the air-derived estimate. That turns "an estimate dressed as a
   reading" into "an estimate honestly anchored to the nearest real measurement" — the honest version
   of the leverage-the-local-asset play. (Eng/data-layer work; flagged, not scoped here.)

## Evidence log
- 2026-07-06: `inferred` — Paul's 12 session nudges (distilled arc) — JTBD one-liner, decision-first framing, right-altitude/anti-averaging, freshness-reads-as-fresh, horizon-follows-data, no-false-precision, source-hierarchy-drives-layout, single-proxy conflation catch, Fishing-is-his-tactical-surface.
- 2026-07-06: `inferred` — fishing.json `conditionsModel` (evidence-weighted signals, on-site station as strong secondary, solunar down-weighted) — corroborates P7 + the data-fusion picture.
- 2026-07-06: `inferred` — two ux-expert reviews (forecast-refinement, section-reorg) — independent corroboration of the hierarchy intent and the two-verdicts / multi-NOW / buried-pressure friction points.
- **Open:** no `validated` fishing-use observation exists. Upgrade path = one think-aloud on a real trip-plan (see #3 above).
