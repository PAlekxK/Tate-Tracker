---
type: jtbd
project: fernwood
job_id: weather-card-reader-jobs
last_updated: 2026-07-14
evidence_level: inferred
performer: Paul (remote-check) + Mom (daily glance) — see persona-mom.md, persona-paul-co-steward.md
sources:
  - viewer.html renderWeather() (~6568) + renderWeatherSummary/generateGardenerInsight/renderAmbientStationPanel/computeBurnStatus (read 2026-07-14)
  - Paul's voice-dictated problem statement (this task) — his stated design intent, not observed behavior
  - CLAUDE.md "glance and the repository" (2026-07-06), tone/purpose; fernwood.md patterns; 2026-07-06 fishing-decision journey (the sibling rework)
  - Memory: Mom = confirmed daily user (d-14nyhnjz via 7/02 interview + telemetry); reads with difficulty (meaning via size/color/position)
---

# Weather card — reader's jobs (input to the ux-expert reorg)

> **Evidence note.** Almost everything here is `inferred` (Paul's stated design intent + established
> context) or `assumption` (no weather-specific user signal exists). Mom is a `inferred`-confirmed
> *daily user*, but what she wants *from the weather card specifically* has never been observed —
> tag it honestly and treat the ux reorg as a bet, not a validated spec. Weather renders on the
> **shared** dashboard, so unlike Fishing (Paul's tactical surface) its floor is set by Mom.

## 1. Who's here, and the core jobs

**Two readers, different postures.** Paul reads *remotely* (Atlanta, ~1.5 hr away); Mom reads *in place*, daily.

**J1 · Mom, daily glance — the anchor job** `assumption`
*When I look at the dashboard today, I want to know what it's like out and whether there's anything I should or shouldn't do in the garden — without reading a table — so I can go about my day.* This is the job the "Today" gardener-insight line already serves. Meaning must arrive through **size/color/position**, not label text (her accessibility constraint). Decision-shaped but low-stakes: "water at the base today," "excellent garden window," or simply "mild morning."

**J2 · Mom + Paul, exception salience** `inferred`
*When something is off-normal (frost tonight, storm coming, active fire risk), I want it to be unmissable without reading, so I don't miss the one day it matters.* The 360 quiet days make the glance feel static — the job is that the rare loud day breaks through. This is why obligation-free calm and a real exception channel have to coexist.

**J3 · Paul, remote check** `inferred`
*When I'm in Atlanta thinking about the property, I want to know what it's actually doing up there right now, so I can feel connected and catch anything that needs attention before I'm on site.* Two motives fused: **reassurance** ("all normal up there") and **exception-detection** (frost/storm/heavy-rain/drought). The measured on-property station read is the payload — it's the thing a generic weather app for "Jasper, GA" can't give him.

**J4 · Paul, plan the trip / the work** `inferred`
*When I'm deciding when to drive up or which day to do outdoor work, I want the near-term forecast, so I can pick a day and a window.* This is the same decision-job shape as Fishing — weather is its substrate. Lower frequency, but it's what the 7-day / hourly strips are *for*.

**Anti-persona** `inferred`: the reader who wants a full meteorological instrument panel — barometric trend charts, UV, solar radiation as headline numbers. Those exist in the data and belong in the repository layer; leading with them would bury J1/J3.

## 2. The ONE question of "now" — and why the three reads fragment it

Both readers ask "now" the same single question:
> **"What's it doing at the property right now — and does that change what I'd do today?"**
> One measured-present fact, fused with a so-what.

The card currently answers that one question in **three separate blocks, in an order that inverts the natural read**:

- **Source-status bar (top)** answers a question the reader didn't ask *first*: *"is the data fresh?"* That's trust **plumbing** — legitimately reassuring, but it's occupying the prime glance slot with metadata instead of weather.
- **"Today" insight** answers the *so-what* (meaning) — but sits **above** the conditions it interprets, so the interpretation arrives before the thing being interpreted.
- **"Right now"** answers the literal *what* — but is **itself split**: the measured station hero (temp/wind/rain/dew, the unique local asset) then a separate row with the **modeled** Open-Meteo condition word + today's **H/L** (a forecast, not a "now") stapled on under the same "Right now" header.

So the reader's single fused question (present fact + meaning, with freshness as quiet reassurance) is smeared across **meta → meaning → fact**, and the "fact" block quietly mixes measured-present with modeled-forecast. That's the "clobbered together" feeling: not too much data, but the *sequence* is backwards and one label ("Right now") is covering two different time-horizons and two different trust levels.

## 3. What "fresher = higher" means for THIS reader

Order by how live/local/decision-shaped each signal is (the "freshness sets altitude" principle):

- **Glance (top, fused):** the **measured on-property station read** (temp, wind, rain, dew) **+ the one-line so-what** ("frost tonight," "muggy — water at the base," or "comfortable garden window"). The number and what it means, together, as the headline — with the station's live-dot woven in as quiet freshness reassurance (retire the standalone source bar into this). This is the single clean current read Paul asked for.
- **Near-horizon reference (mid):** the **modeled** layer — condition word, today's H/L, 7-day, hour-by-hour. Decision-shaped for J4, but a step down in freshness (model, not measurement) and clearly *forecast*, visually separated from the measured "now" (Paul's explicit ask). **Keep measured vs. modeled legible** — trust is the load-bearing emotion; don't let the fusion blur which numbers are read off the property and which are predicted.
- **Repository (bottom):** rainfall context (25-yr percentiles), inside sensors, methodology footer, and the static regulatory burn baseline. Present for credibility and the keen drill-in; must not flood the glance.

## 4. Where the burn ban actually sits in the reader's mental model

Paul is **mostly** right — but the header hides two different things under one label:

- **The static regulatory baseline** — "statewide ban May 1–Sep 30 / permit required." It has **zero freshness** (identical every summer day — exactly the "constant" thing he's tired of seeing up top). → **Bottom, reference layer**, near methodology. Paul is right about this half.
- **The dynamic fire-risk signal** inside the same function — an active **NWS Red Flag / Fire-Weather alert** (severe), **D2+ drought**, or **10+ days since meaningful rain**. These **change** and are **safety-shaped** — they're a rare exception, which is J2's whole point. → When elevated/severe, this should **rise into the alerts / "Worth knowing" channel** at the top; when normal, stay silent/bottom.

So the reader's model isn't "burn ban" as one block — it's **a static rule (bottom) + an event-fresh risk (rises to the glance only when it trips).** That's cleaner than a wholesale "burn → bottom," and it matches how the alert engine already works.

## 5. Open questions the reorg should resolve (reader-side)

1. **Meaning-first or measurement-first for Mom?** She reads with difficulty and takes meaning from size/color/position. Does the *so-what* line ("water at the base today") become the **biggest** element with the temp as support — or does she anchor on the temperature number first and read meaning second? This decides which element is physically largest at the top of the card. `assumption` — no observed signal; a candidate for a single Mom think-aloud.
2. **Does the condition *word* earn its place?** When the measured station read is right there, does Mom need the modeled "partly cloudy" at all (she can see the sky), and when station-measured and Open-Meteo disagree, which is THE current read? Reader-side: is the model's job here *forecast only*, leaving "now" entirely to the station?
3. **Is Paul's remote glance reassurance or exception-detection?** If it's exception-detection, the top of the card should be **near-invisible on a normal day** and loud only on frost/storm/fire — which changes what "top of card" even shows 360 days a year. If it's reassurance, the calm current read stays visible daily. Likely both, but the ranking between them sets the default-state design.

## Evidence log
- 2026-07-14: `inferred` — Paul's voice-dictated problem statement (one clean live current read, forecast visually separate, single top summary, burn drops to bottom) — J3/J4, the three-reads fragmentation, the burn split.
- 2026-07-14: `inferred` — code read (generateGardenerInsight = the meaning layer; renderAmbientStationPanel = measured station hero; the "Right now" block staples modeled condition + H/L under the same header; computeBurnStatus fuses a static regulatory baseline with dynamic Red Flag/drought/dry-day risk) — §2 fragmentation and §4 burn split are grounded in the actual functions.
- 2026-07-14: `inferred` — Mom = confirmed daily user, reads with difficulty (memory); `assumption` — her weather-card-specific jobs (J1/J2) have never been observed.
- **Open:** no `validated` weather-use observation for either reader. Cheapest upgrade = one Mom think-aloud on a normal morning (resolves Q1/Q2) + a Paul remote-check narration (resolves Q3), same self-ethnography move the fishing journey flagged.
