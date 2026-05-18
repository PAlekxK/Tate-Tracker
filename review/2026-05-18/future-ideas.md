# Tate Tracker — Future Ideas (Research-Mode Pass)

**Date:** 2026-05-18
**Author:** user-researcher (agent)
**Scope:** Creative expansion ideas for Tate Tracker. Future-direction half of a holistic review running in parallel with UX and copy reviews.
**Seed prompt from Paul:** "Maybe it's worth adding local mammals like raccoons and so on. So let's see what suggestions we can come up with."

This document holds four artifacts:

1. A proto-persona for Paul-as-user (the harder question: what does this dashboard actually *do for him*?)
2. JTBD cards — six jobs the site is or could be hired for, with attention to ones under-served by what's shipped
3. An expansion idea list grouped by category, each tagged with effort signal, field-journal fit, and JTBD served
4. A "things to ask Paul" list — discovery questions, not feature specs

Plus a short closing section: top 3 ideas to talk through and the discovery work that would unlock them.

All claims tagged `assumption | inferred | validated`. Synthetic / AI-generated reasoning is `assumption` by default.

A note on scope: I am **not** re-introducing Mom as a separate persona here. She remains the make-or-break user (per the existing `persona-mom.md`), and the field-journal tone is largely her constraint. But this brief is about *creative expansion* and Paul-as-user is the under-examined half. Mom's needs are surfaced as guardrails throughout, not re-personified.

---

## 1. Proto-persona: Paul-as-user, re-examined

This builds on the existing `persona-paul-co-steward.md` but pushes harder on the question Paul asked: what does the dashboard *actually do for him*, beyond "track property facts"? The existing artifact frames Paul-as-co-steward (with Mom). This one isolates the part of him that is the dashboard's solo user — the builder-user looking at his own work, deepening his own relationship to the place.

```yaml
type: persona
project: tate-tracker
person_id: paul-builder-user-future-lens
last_updated: 2026-05-18
evidence_level: inferred
sources:
  - persona-paul-co-steward.md (existing artifact)
  - jtbd-invest-time-well.md (existing artifact)
  - CLAUDE.md (Tate Tracker, esp. research-resource backlog and tone notes)
  - _about-paul.md (Tate Tracker user context)
  - Paul's brief 2026-05-18 (mammals seed + "what's the dashboard's real job")
```

### Situation
`[inferred]` — Atlanta-based, visits the property periodically rather than daily. Has accumulated ~85 verified research resources, photographs, audio recordings, weather history, and ~50+ tracked species/items across plants, birds, amphibians, fishing, snakes, lizards, vehicles. The dashboard is now substantial — past the "MVP" inflection point. He's looking at it less as "what's missing" and more as "what could it *become*."

`[inferred]` — He treats the build as a way of being on the property *between* visits. Adding the moon image, the streamflow gauge, the Cherokee land context, the bat-house spec — each is an act of attending to the place even while not standing on it.

### Job-to-be-done (Paul's solo half of it)
`[inferred]` — Build a layered, durable record of *this specific place* — biologically, hydrologically, historically, climatologically, celestially — so that owning the property becomes an act of attention rather than asset management. The dashboard is the field journal *and* the long-term scaffolding for noticing more.

The job is partly about the place (knowing it deeply) and partly about himself (being the kind of person who knows a place deeply). That second half is real and worth naming: Tate Tracker is identity work as much as it is reference work. The hobbyist-developer anti-persona (already named) is the version that fails this — the version that builds for the pleasure of building and never knows the place better as a result. The depth/accumulation of the research library is evidence Paul is *not* in that failure mode, but the structural risk doesn't go away.

### Triggers (for Paul's own use, separate from Mom)
- `[inferred]` — A research thread to follow (Cherokee history, endemic darters, Bortle calibration, NTFP forest farming) — the desk-time mode.
- `[inferred]` — A visit coming up; previewing the property in advance.
- `[inferred]` — A build session where Tate Tracker is the current project focus.
- `[inferred]` — On-property moments where the app is a lookup tool (what's that bird? what's this plant past its peak?).
- `[assumption]` — Showing the property to someone else — the app as a way of telling the place's story.

### Constraints
- `[validated]` — Field-journal tone is non-negotiable.
- `[inferred]` — Builder-user bias: features that pay off for Paul-the-builder may not pay off for Mom-the-other-user. Already explicitly guarded against in the existing persona; keep flagging it.
- `[inferred]` — Time is finite. The app shares his attention with consulting work, Bolo Boys, the Claude Code meta-project, and life. Anything proposed has to earn its place against those.
- `[inferred]` — Mobile and desktop both — different surfaces serve different jobs.

### Definition of success (Paul's solo half)
`[inferred]` — Three layered conditions, ordered weakest to strongest:
1. He reaches for the dashboard unprompted to look something up.
2. The dashboard tells him things he didn't already know — about the place's history, ecology, weather patterns, sky.
3. Over time, the *property itself* feels richer to be on because of what the dashboard surfaces. The depth and texture of the place becomes legible in a way it wouldn't be without the journal.

Failure modes (worth naming because they're easy to slide into):
- The app becomes a build-toy with no use-value to Paul on the actual property.
- Features get added because they're technically interesting, not because they earn their place against the field-journal job.
- Adding more without weeding — the dashboard accumulates surface area faster than it earns it, and density starts hurting the leisure-reading posture Mom needs.

### Anti-persona (sharper version for the future-lens)
- `[inferred]` — The dashboard-builder who collects features. The dashboard-as-Pinterest version, where everything that could be relevant is added because it could be relevant. Field-journal posture rejects this — a field journal is curated by use, not by ambition.
- `[inferred]` — The smart-home / IoT / sensor-network maximalist. More telemetry, more dashboards, more screens. Tate Tracker is *quieter* than that — sensors serve the journal, not the other way.
- `[inferred]` — The gamified-naturalist. Streaks, completion percentages, "you've identified 12 of 17 frogs" badges. Identity-as-collection. Wrong project.

### Evidence log
- `2026-05-18: [inferred] — Paul's brief — "mammals like raccoons and so on" is a *seed*, not a demand. The phrasing invites breadth. Paul is asking what the dashboard could become, not asking for a feature ticket.`
- `2026-05-18: [inferred] — Research-resources doc and CLAUDE.md backlog — Paul has been a heavy researcher. The volume and care of the research library is itself evidence of the depth-and-attention job, not just the stewardship-of-this-property job.`
- `2026-05-13 to 2026-05-18: [validated] — Tate Tracker CLAUDE.md — Recent shipped work (USGS streamflow, USGS quakes, NWS skyCover, NASA Dial-a-Moon, snakes + lizards tabs) is heavily place-context-oriented, not task-oriented. Paul is biased toward the appreciation half of the dual job in his own build choices.`
- `2026-05-13: [validated] — Paul retired the "Etowah darters in our streams" callout when ground-truth didn't support it. He polices his own claims for property-relevance. The dashboard is meant to be *honest*, not just impressive.`

### Open questions (carry forward, do not resolve here)
- Is Paul's solo job genuinely separable from the Mom-co-steward job, or are they the same job at different intensities? My read: same underlying job ("invest finite time well on a place that matters"), but Paul's version weights the depth/identity layer heavier, and Mom's weights the leisure-reading and present-tense awareness heavier. Worth checking with Paul.
- Is there an audience-of-one-or-two failure mode Paul wants to guard against — for example, building something so personal it could never be shared even with a curious friend or family member? Or is full-personal-and-private the design intent?
- Showing-the-place-to-others is in triggers as `[assumption]`. Worth testing — has Paul ever opened Tate Tracker to show someone else? What did that feel like?

---

## 2. Jobs-to-be-Done cards

The existing single JTBD (`jtbd-invest-time-well.md`) frames the *unified* joint job. For expansion thinking, it helps to split it into more concrete jobs — some are well-served by what's shipped, some aren't. The under-served ones are where future-direction thinking pays off most.

I'm using the JTBD card format from my standard playbook (situation → motivation → outcome), with the four forces (push / pull / anxiety / habit). Brief framework refresher: a JTBD is the *progress* a user is trying to make, framed in their own situation. The four forces are Push (pain in current state), Pull (attraction to the new thing), Anxiety (worries about switching), and Habit (inertia keeping them in the old way).

Status notation per job: **Well-served** = the site already does this; **Partially served** = some surfaces exist but the job isn't complete; **Under-served** = the site barely touches this and there's room to grow.

### JTBD-1: "When I'm wondering what's happening on the property right now, I want a low-attention read of the place, so I can feel oriented without doing work."

**Status: well-served, but worth a check.** The dashboard strip + weather card + the "this month" plant view already do this. The risk is over-loading the front door — more cards make this job harder, not easier.

- **Push** `[inferred]` — Without the app, "what's happening" is held in head/memory and is fragmented.
- **Pull** `[inferred]` — Field-journal scannable read at a glance.
- **Anxiety** `[inferred]` — The dashboard becoming dense enough that "low-attention" stops being possible.
- **Habit** `[inferred]` — Phone is already where you check the weather and the news.

**Performers:** Both Paul and Mom. This is the bed-with-coffee mode (per `persona-mom.md`) and the morning-of-visit mode (Paul).

**Design implication for future ideas:** Anything new should fight for its place in the surface scan, or live one click deep. Expansion ≠ dashboard-strip-expansion.

### JTBD-2: "When I'm about to do something on the property (prune, plant, fish, walk in the woods), I want property-specific guidance, so I can act with confidence."

**Status: well-served for plants, fishing, vehicles. Under-served for activities.**

- **Push** `[inferred]` — Guesswork costs time and confidence both. ("Should I prune the hydrangea now or wait?")
- **Pull** `[inferred]` — A property-tuned answer, not a generic-zone answer. (The 2,959 ft elevation calibration is exactly this.)
- **Anxiety** — `[validated, inline]` from Paul: "We also don't wanna be so gun shy about [pruning/fertilizing] that we don't do things we could be doing to make them more beautiful." Permission to act, not only warnings.
- **Habit** `[inferred]` — Default Google search is the alternative; it returns generic content not calibrated to elevation.

**Performers:** Both, but Paul more for active stewardship; Mom for plant-care timing especially.

**Under-served slices:**
- **Outdoor work windows** — when is it actually a good day to be outside? (The "ideal garden window" gardener-insight rule is the closest existing surface.)
- **Watching/listening** — best times to look for owls, listen for frog choruses, watch meteor showers. Stargazing has the bones (Tonight's Sky); herp-activity-tonight does not.
- **Fishing on Lake Sequoyah** — partially served; the "should I go fishing now?" question still has friction.

### JTBD-3: "When I encounter something on the property I don't recognize, I want to identify it and learn about it, so the place becomes more legible to me."

**Status: partially served.** Plants + birds + amphibians + snakes + lizards + fishing cover most of what's commonly seen. The big absences are mammals (Paul's seed), insects/moths/butterflies/pollinators, mushrooms/fungi, ferns and native wildflowers, trees beyond what's planted, and rocks/geology.

- **Push** `[inferred]` — You see something interesting, then forget it.
- **Pull** `[inferred]` — A field-journal-style entry on what it is, when it's around, what it does.
- **Anxiety** `[inferred]` — Encyclopedic dumps that fail the leisure-reading posture.
- **Habit** `[inferred]` — Pulling out Merlin or iNaturalist on the spot, which works but doesn't *accumulate* into the property's journal.

**Performers:** Both. This is the curiosity-driven trigger for Mom (notices a bird, wants to know) and a major thread for Paul.

**Big under-served slice:** Mammals. Paul's seed. Beyond that, insects/moths/butterflies — large signal-to-effort given the site's existing biodiversity framing.

### JTBD-4: "When I'm not on the property, I want to feel connected to it, so visiting doesn't feel like resetting from zero."

**Status: under-served, and the most interesting Paul-specific job.**

- **Push** `[inferred]` — Atlanta-based; the property's day-to-day shifts happen without him. Mom holds the day-to-day; Paul holds the long-arc context. They're different relationships to the same place.
- **Pull** `[inferred]` — A live signal that the place is *here, now, doing things*. Streamflow rising. Quake registered. Moon phase tonight. Frogs calling this week. Fog at the property right now (camera?). Pressure dropping ahead of a front.
- **Anxiety** `[inferred]` — Surveillance vibe. Not "what's the security camera showing" — that's wrong project. Closer to "looking out a window from somewhere else."
- **Habit** `[inferred]` — Texting Mom to ask.

**Performers:** Heavily Paul. Mom less so — she lives it.

**Why this matters for expansion:** The recent live-data work (USGS streamflow, NWS sky cover, station hero) is exactly this job. Any expansion that makes the dashboard feel more *currently alive on the property* serves this job. Anything static, well-researched, but inert serves it less.

### JTBD-5: "When I want to deepen my relationship to this place's history and ecology, I want layered context I can read into, so the property feels more dimensional over time."

**Status: partially served — research-resources doc has the material; viewer.html surfaces only a thin slice.**

- **Push** `[inferred]` — The property is more than its current state. It's on Cherokee land. It drains to one of the most biodiverse small rivers in North America. It's in the keystone-genera zone for Blue Ridge Lepidoptera. Without surfacing this, you live on the *picture* of the place, not the *place*.
- **Pull** `[inferred]` — Cherokee land context, Tate Mountain Estates / Col. Sam Tate history, Etowah biodiversity story, dark-sky context, keystone plants ecology, prescribed-burn neighbor activity, climate-shift framing.
- **Anxiety** `[inferred]` — Becoming a mini-Wikipedia. Density without invitation. Lecturing-the-reader tone.
- **Habit** `[inferred]` — Read once, forget. The dashboard's job is to keep this layer *re-encounterable.*

**Performers:** Heavily Paul. Some of this is over Mom's threshold of interest; some is exactly her cup of tea (she lives the place, the layered history makes it richer for her too).

**Why under-served:** Almost everything in the "surface-fact callouts" section of CLAUDE.md's research-derived backlog is this job, and most of it isn't shipped yet. This is *high-signal, low-effort* territory.

### JTBD-6: "When I'm preparing to enjoy the night sky, the seasons, or a notable celestial event, I want a field-journal-grade preview, so I can show up to the moment ready."

**Status: well-served for tonight's-sky and moon. Under-served for seasonal arc.**

- **Push** `[inferred]` — Astronomy events are easy to miss without preview.
- **Pull** `[inferred]` — Bortle 3 location, dark-sky context, NASA dial-a-moon image, NWS sky cover live, meteor shower calendar.
- **Anxiety** `[inferred]` — Becoming an astronomy app. The site is a *property* journal; astronomy is one layer.
- **Habit** `[inferred]` — Stellarium, SkyView, almanac sites.

**Performers:** Paul more. The March 3, 2026 lunar eclipse callout candidate would serve this directly.

**Under-served slices:** Seasonal arc (when does the sun set earliest, when does the warbler chorus peak, when does the first frost typically land — connecting weather/wildlife/plants on a year-long ribbon). Phenology, in other words. See ideas list.

---

## 3. Expansion idea list

Each idea is tagged:
- **Effort** — rough signal: ★ very small, ★★ small, ★★★ medium, ★★★★ large, ★★★★★ build a new thing.
- **JTBD** — which job(s) this serves (JTBD-1 through JTBD-6 above).
- **Field-journal fit** — clear pass / pass with care / watch out / no.
- **Evidence basis** — for ideas tied to research-resources.md or CLAUDE.md backlog, I cite.

### Category A: Wildlife coverage expansion

#### A1. Mammals card / tab — Paul's seed
**Description:** A new wildlife tab parallel to Birds / Amphibians / Snakes / Lizards / Fishing. Likely species set for a 2,959 ft Blue Ridge property: white-tailed deer, black bear (and bear-aware notes), eastern gray squirrel, eastern chipmunk, raccoon, opossum, red fox, gray fox, coyote, bobcat, eastern cottontail, groundhog, striped skunk, possibly woodland jumping mouse (Blue Ridge specialty per nps.gov), various bats (already a partial story via the bat-house idea).
**Why field-journal fit:** Mammals are *the* category Paul named, and they fit the existing pattern (species + monthsActive + sound where applicable + photo + range/behavior notes). Some species (bears, coyotes) carry real safety notes the way snakes do — handle in the same calm, info-not-alarm voice the snakes card uses.
**Watch out:** Trail-cam imagery temptation. Don't slide into surveillance posture — keep the field-journal frame ("often seen at dusk along the fairway clearing" not "detected at 2:34am"). Don't include hunting-season data unless Paul wants the dashboard to take that voice.
**Effort:** ★★★ (similar to snakes + lizards build — schema, JSON, renderer, photos, sounds for the few vocal ones like coyote/owl-equivalents-among-mammals... mammals are mostly silent for site purposes).
**JTBD:** JTBD-3 primarily; JTBD-2 for safety/encounter awareness.
**Evidence:** Paul direct 2026-05-18 (seed); Blue Ridge Parkway NPS mammal checklist as candidate source list (web search 2026-05-18); SREL has mammal accounts as well as herp accounts — extends the citation pattern already used for amphibians/snakes/lizards.

#### A2. Moths & butterflies (Lepidoptera) card
**Description:** A Lepidoptera tab. North Georgia is a Lepidoptera hotspot — the keystone-plants framing on the Plants card is literally about Lepidoptera support. Pair the consumer (caterpillars/moths/butterflies) with the producer (oak ~400+ species, willow, cherry, blueberry, goldenrod) already on the Plants side.
**Why field-journal fit:** Moths especially are deeply field-journal — many species show up to porch lights, can be observed without disturbance, and the seasonal arcs are vivid. Butterflies are the more obvious half (eastern tiger swallowtail, monarch, spicebush swallowtail).
**Watch out:** Lepidoptera has ~12,000 NA species; curation is everything. Aim for ~15–25 most-likely-at-this-elevation, not comprehensiveness. Native Plant Finder by NWF (in research-resources.md) gives an authoritative species list for 30143.
**Effort:** ★★★ — similar build to birds, but photo curation harder (Wikimedia Commons has good coverage for big-name species, thinner for micromoths).
**JTBD:** JTBD-3, JTBD-5 (ties to keystone-plants story).
**Evidence:** research-resources.md lines 209, 244 (Native Plant Finder, Xerces); CLAUDE.md research-backlog "keystone genera for Blue Ridge ecoregion" item.

#### A3. Fireflies — small dedicated callout
**Description:** Pickens County is in the range of synchronous fireflies (*Photinus carolinus*) which famously synchronize in Great Smoky Mountains NP. Multiple eastern firefly species occur at this elevation. A seasonal callout (May–July) — what species are out, when peak emergence is, where to look.
**Why field-journal fit:** Excellent — fireflies are a uniquely field-journal phenomenon. Low effort, high resonance, seasonally bounded.
**Watch out:** Don't promise synchronous-firefly viewing on the property without ground-truth from Paul or someone who's observed it.
**Effort:** ★★ — could be a property-card callout or a Lepidoptera-card sub-section. Doesn't need its own tab.
**JTBD:** JTBD-1, JTBD-3, JTBD-5.
**Evidence:** General North GA naturalist literature; Xerces firefly conservation materials.

#### A4. Pollinators / native bees panel
**Description:** Partially in the backlog (Xerces SE region PDF, SE Bumble Bee Atlas, UGA B 1483/B 1349). Could land as a sub-section of the Plants card ("who's pollinating these?") or a Wildlife tab.
**Why field-journal fit:** Solid — pollinator activity is observable, seasonal, and the keystone-plants story already gestures at it.
**Watch out:** Visual ID is hard for bees and many flies (mimics). Lean on observable behavior windows, not species-level ID.
**Effort:** ★★ for a Plants-card callout / ★★★ as its own tab.
**JTBD:** JTBD-3, JTBD-5.
**Evidence:** research-resources.md lines 107, 114, 121, 244, 251, 346.

#### A5. Mushrooms / fungi — seasonal callout, not full coverage
**Description:** Not a full ID guide (too risky if anyone ever forages off it), but a field-journal callout: "Late summer — chanterelles likely in oak-hickory shade; chicken-of-the-woods often on standing dead oak." Observation, not foraging guidance. With a clear "don't eat anything you ID from this dashboard" line.
**Why field-journal fit:** Strong for *observation*. Treat fungi as something to notice and photograph, not eat.
**Watch out:** Liability and accuracy. Even with clean disclaimers, an ID app for fungi is a different commitment than an "interesting to read about" callout. Stay on the latter side.
**Effort:** ★★ as callouts; ★★★★ if it ever becomes a real ID tool.
**JTBD:** JTBD-3 (curiosity), JTBD-5 (ecology layer).
**Evidence:** General; not in research-resources.md.

#### A6. Trees — separate from cultivated Plants
**Description:** The current Plants card is about *cultivated/planted* species (hydrangeas, hostas, etc.). A separate Trees layer would cover the *naturally occurring* canopy and understory: oaks (chestnut oak, northern red oak, white oak), tulip poplar, eastern hemlock (sadly hemlock woolly adelgid-relevant), hickories, sourwood, dogwood (in the wild not just planted), red maple, sweetgum, mountain laurel as wildling.
**Why field-journal fit:** Strong. The trees *are* the property in a way the planted bed isn't. Pairs with the "Native Trees of Georgia" GFC field guide in research-resources.md.
**Watch out:** Don't duplicate planted-dogwood with wild-dogwood data. A trees card has a different schema focus — observation, identification, ecology — rather than "when to prune."
**Effort:** ★★★.
**JTBD:** JTBD-3, JTBD-5.
**Evidence:** research-resources.md lines 149 (GFC Native Trees of Georgia), 79 (B 987).

#### A7. Native ferns + wildflowers — observable, ephemeral
**Description:** Already flagged as a "surface fact" idea in research-resources.md (Pickens hosts ~30 fern species). Could grow into a Wildflowers callout that's strongest March–May (spring ephemerals: trillium, bloodroot, hepatica, foamflower).
**Why field-journal fit:** Excellent — wildflower ephemerals are *exactly* field-journal-grade. They're noticed-on-walks, peak briefly, reward attention. Aligns with the existing leisure-reading mode.
**Effort:** ★★ as a seasonal callout; ★★★ as a sub-tab.
**JTBD:** JTBD-3, JTBD-5, JTBD-6 (seasonal arc).
**Evidence:** research-resources.md lines 86 (UGA B 987-3 Wildflowers), 93 (B 987-2 Ferns).

### Category B: Place-context and history (already mostly in backlog — flagging because under-shipped)

#### B1. Cherokee land context — Property card subsection
**Description:** Already in CLAUDE.md backlog. Static, low-effort. Honest framing: this was Cherokee territory until 1838; Talking Rock Creek ~6 mi was a settlement; link to EBCI Natural Resources for ongoing stewardship.
**Why field-journal fit:** Strong — it's part of *what this place is*. Field journals are honest about land they're written on.
**Watch out:** Tone. Don't make it performative. Quietly placed, accurately stated, linked, not foregrounded with a banner.
**Effort:** ★.
**JTBD:** JTBD-5.
**Evidence:** CLAUDE.md research-derived integration backlog; research-resources.md lines 856, 869.

#### B2. Tate Mountain Estates / Col. Sam Tate history
**Description:** Lake Sequoyah (6.2 mi) built ~1929 by Col. Sam Tate. The "Tate" in Tate Tracker has a real, local-historical referent. Already in backlog.
**Effort:** ★.
**JTBD:** JTBD-5.
**Evidence:** CLAUDE.md backlog; research-resources.md line 16.

#### B3. Geology and soil story
**Description:** The property sits on a Hayesville-Cecil-Pacolet soil complex on Blue Ridge metamorphic bedrock (likely biotite gneiss, quartzite, schist). The watershed drains to the Etowah. Add a quiet geology callout — what the rocks under the property are, why the elevation is what it is, what the soil's parent material is.
**Why field-journal fit:** Strong. Geology is a slow, deep layer that pays the property card off the way Cherokee land context does.
**Effort:** ★★ — one-time research, static content.
**JTBD:** JTBD-5.
**Evidence:** USDA NRCS Hayesville/Cecil/Pacolet OSDs are already in property.json data sources.

#### B4. Climate-shift "Pickens County in 2050" link
**Description:** Already in research-resources.md (Climate Explorer per-county view). One paragraph + link. Honest about what the property's future climate envelope looks like.
**Watch out:** Risks doom-scroll energy if framed wrong. Field-journal framing: "Worth knowing what's coming for this place."
**Effort:** ★.
**JTBD:** JTBD-5.
**Evidence:** research-resources.md line 701.

### Category C: Phenology and seasonal arc (the strongest under-served theme I see)

#### C1. "What's likely happening this week" — synthesized seasonal narration
**Description:** Already in CLAUDE.md (the "AI-synthesized conditions brief" idea). A single italic paragraph at the top of the dashboard, updated daily or weekly, that synthesizes weather + plants + wildlife + sky into a sentence or two: *"Mid-May at 2,959 ft — mountain laurel opening, spring peepers giving way to gray treefrogs, oak pollen heavy, lake warming toward bass territory, lunar libration showing the western limb tonight."*
**Why field-journal fit:** This is the *most* field-journal-grade idea on the page. It's the voice of the journal itself.
**Watch out:** Requires a server proxy for the Claude API call. Quality bar matters — a stale or generic version is worse than not having it. The fallback (rule-based, the way `generateGardenerInsight` already works) is honestly pretty close — Paul might want to grow the rule-based version first and add LLM synthesis later.
**Effort:** ★★ rule-based extension of existing gardener-insight engine; ★★★★ if going full LLM-synthesis with backend.
**JTBD:** JTBD-1 (low-attention read), JTBD-4 (presence-from-afar), JTBD-5 (depth), JTBD-6 (seasonal arc).
**Evidence:** CLAUDE.md "Dynamic AI summarization."

#### C2. Year-on-a-ribbon — phenology timeline view
**Description:** A single year-spanning ribbon at the top of (or inside) the Property card showing major property phenology events on one strip: last frost, first leaf-out on red maple, mountain laurel peak, peeper chorus, firefly emergence, monarch passage, first frost, first hard freeze. Drawn from species data already in the dashboard plus a few additions.
**Why field-journal fit:** Excellent — this is the *shape of the year* on this specific land, which is field-journal as it gets.
**Effort:** ★★★ — design + new render; the data mostly already exists in `monthsActive`/`monthsPresent` fields.
**JTBD:** JTBD-5, JTBD-6, JTBD-1.
**Evidence:** No direct backlog item; this is a re-presentation of existing data, not new data.

#### C3. Nature's Notebook / USA-NPN integration
**Description:** USA-NPN is the federal phenology citizen-science network. There's a "Local Phenology Leader" program. Could be an enrollment callout in the Plants card; or, for the data side, plug into national phenology models that compare Paul's elevation/location to species norms.
**Watch out:** Same citizen-science-as-data-upload concern that deactivated FrogWatch et al. on 2026-05-13 (per CLAUDE.md). Don't re-introduce without checking.
**Effort:** ★★.
**JTBD:** JTBD-2, JTBD-5.
**Evidence:** WebSearch 2026-05-18; not yet in research-resources.md.

### Category D: "Live presence" — the dashboard as a window onto the property right now

#### D1. Audio "what's calling right now" — bird/frog activity by hour
**Description:** The amphibians card already has a "calling now" badge for frogs whose `monthsActive` includes the current month. Extend: time-of-day-aware ("Peepers usually start ~30 min after sunset," "Barred Owls late evening"). Optionally, an "if you stepped outside right now, you'd likely hear…" line based on time/season.
**Why field-journal fit:** Excellent. Audio noticing is one of the most field-journal-grade modes of attention.
**Effort:** ★★ — time-of-day windows added to existing data; UI surface is small.
**JTBD:** JTBD-2, JTBD-3, JTBD-4 (especially — Paul-in-Atlanta seeing "barred owl likely calling now").
**Evidence:** Existing amphibians "calling now" pattern.

#### D2. Lake-Sequoyah-style live water conditions for the property's actual seeps/pond
**Description:** Hard without instrumentation. But if Paul ever installs a soil-moisture sensor on the property and exposes it the way the Ambient Weather station is exposed, the field-journal posture could absorb it (without going IoT-maximalist).
**Why field-journal fit:** Watch out — risks tipping into telemetry-dashboard mode if it accretes.
**Effort:** ★★★★ (hardware + integration). Probably not worth pursuing now; flagging because it would extend the existing station-as-eye-on-property pattern.
**JTBD:** JTBD-4.
**Evidence:** Speculative.

#### D3. Property webcam or sky-cam — pass with care
**Description:** A single quiet view onto the property — sky, fairway, pond. Field-journal-mode: a still image refreshed periodically, not a security-cam livestream. The window-from-elsewhere version of JTBD-4.
**Why field-journal fit:** Possible but easy to ruin. The difference is "looking out the window" vs. "checking the security feed." Frame matters.
**Watch out:** Hardware, hosting, the surveillance vibe, the privacy reset if Mom or anyone is on camera.
**Effort:** ★★★★.
**JTBD:** JTBD-4.
**Evidence:** Speculative.

#### D4. Air quality (AirNow) + drought monitor (USDM)
**Description:** Both in the backlog, both need server proxies (CORS).
**Why field-journal fit:** AQI fits if it's framed as observation ("smoke from a far-off burn drifting in today"), not alert. Drought status is a quiet pill.
**Effort:** ★★ each, once a proxy exists.
**JTBD:** JTBD-1, JTBD-2, JTBD-4.
**Evidence:** research-resources.md lines 783, 709; CLAUDE.md backlog.

#### D5. Long-term weather history visualization — earn the file's accumulation
**Description:** The `weather-history.json` rollups are accumulating (5+ months of data now). Currently used for nothing visible. As soon as the file has 6–12 months, the rainfall and temperature blocks could compare *the property's own record* against ERA5/normals: "Wettest May on our record," "Cooler than our 12-month average."
**Why field-journal fit:** Excellent — this is the journal *being* a record over time. The shift from "ERA5 estimate of normals" to "what this station actually saw" is the journal coming into its own.
**Effort:** ★★ once 6 months of data exists; the rendering logic is the work.
**JTBD:** JTBD-5 (deepening), JTBD-1 (orientation).
**Evidence:** CLAUDE.md "Phase 6 — long-term archive."

### Category E: Quieter formats and reframings

#### E1. A "this week on the property" digest — once-a-week summary view
**Description:** An off-dashboard format (or a special card view) that summarizes the prior week — rainfall, what bloomed, what called, what was seen, any seismic activity, any notable weather. A weekly issue of the journal, in effect.
**Why field-journal fit:** Strong — this is journals as journals are. Could be email-delivered (to Paul, and maybe to Mom if she wants it).
**Watch out:** Email pushes toward "subscription" feeling; that's the wrong frame. Maybe it's an in-app archived view, not a push notification.
**Effort:** ★★★ (synthesis logic + render; email = ★★★★ with backend).
**JTBD:** JTBD-4, JTBD-5, JTBD-6.

#### E2. Paul's own observations — a notes/sightings field he can append
**Description:** A first-class place for *Paul's own observations* to land in the journal. He sees a luna moth on May 22 — that goes into the property's record. Currently the dashboard is all third-party data and his curation; none of it is *his* direct observation.
**Why field-journal fit:** This is the most field-journal-y idea here. A real field journal is *written in*, not just read.
**Watch out:** Requires storage (no backend currently). Could start as a local-storage thing or a notes-to-JSON-PR workflow. Mom might or might not use it; Paul almost certainly would.
**Effort:** ★★★ local-only; ★★★★ with sync.
**JTBD:** JTBD-3, JTBD-5; also serves Paul's identity-work half of JTBD-5 directly.

#### E3. Weed the dashboard — a counter-move against accumulation
**Description:** Not an addition. A periodic prune of what's lost its purchase. The site's surface area is growing fast; the field-journal posture rewards curation over completeness. A formal "what's earning its place" review (annual? semi-annual?) would protect the leisure-reading job.
**Why field-journal fit:** Excellent — preserves the posture that makes everything else work.
**Effort:** ★ (it's a recurring practice, not a feature).
**JTBD:** JTBD-1 (low-attention read survives the growth).

#### E4. Print-it-once field-journal export
**Description:** A printable PDF version of the dashboard — a one-page or few-page property field-journal snapshot for the current month or season. Hung in the kitchen or kept in a drawer. Acknowledges that field journals live offline too.
**Why field-journal fit:** Genuinely interesting — and emphatically not productivity-app territory.
**Effort:** ★★★.
**JTBD:** JTBD-3, JTBD-5.

### Category F: Small surface-fact callouts already in the backlog (cluster reminder)

These are all in CLAUDE.md's "Research-derived integration backlog" — listing here as a reminder that the *highest signal-to-effort* expansion isn't new categories, it's shipping the surface facts already researched:

- Cherokee land subsection (Property card)
- Tate Mountain Estates / Col. Sam Tate history (Property card)
- Bortle 3 reference ("Stephen C. Foster is Bortle 2 — Georgia's only IDA-certified site") (Property card)
- Keystone genera for Blue Ridge ecoregion (Plants card)
- Burn-ban seasonal banner (Property card)
- Homegrown National Park registration (Property card)
- ~30 of Georgia's native fern species (Property card)
- "Eligible for Birds Georgia Wildlife Sanctuary certification" (Property card)
- Long view: Pickens County in 2050 (Property card)

Each is ★ effort. Each serves JTBD-5. Each fits field-journal posture if written carefully.

---

## 4. Things to ask Paul (discovery questions, not feature specs)

Per Teresa Torres's continuous-discovery posture, the right move before committing to any of these ideas is to ask *discovery questions* — questions about Paul's behavior and reasoning that will sharpen which job needs serving most. Not "do you want feature X?" Questions about what he *does* with the property, what he *reaches for*, what the dashboard *isn't catching* right now.

These are framed Mom-Test-style (Rob Fitzpatrick): ask about past behavior, not hypothetical futures.

### About the dashboard's actual job for Paul

1. When you last opened Tate Tracker for your own use (not building it, just using it), what were you looking up? Did you find it?
2. What's the last thing you looked up about the property *outside* the dashboard? (Google search, asking Mom, paging through a book, opening Merlin/iNat.) Walk me through it. — *This is the classic Bob Moesta switching-moment question. It tells us where the dashboard isn't yet competitive with what Paul already does.*
3. Have you ever shown the dashboard to someone else? What was that like? Which parts did you point at?
4. Is there a thing you've *wanted* the dashboard to tell you that it doesn't?

### About the place itself

5. What's the last thing you noticed on the property that you wanted to know more about? (A bird, a plant, a sound, a track, a weather pattern.) Did you look it up? Where?
6. Are there mammals you actively see on the property, vs. ones you know are around but rarely encounter? (Helps calibrate the mammals card — is this a "what I'm seeing" list or a "what's on this land" list?)
7. Have you walked the woods at night on the property — would you, or do you? — *Bears on field-journal voice, owls, frogs, fireflies all hinge on this.*
8. Has anyone in the family done any kind of foraging or wild-plant-identification on the property? — *Decides whether mushrooms/ferns/wildflowers are deep-observation territory or whether there's a "with care" foraging layer.*

### About Mom's actual use (since she's the make-or-break user and most of this is from Paul's hand)

9. Has Mom opened Tate Tracker since you last asked? What did she look at? What did she tell you afterward, if anything? — *The 30-day open-rate behavioral check from her open-questions list.*
10. If Mom started using something on the dashboard, you'd probably know. Has anything changed?

### About the future direction

11. Of the recently-shipped pieces (USGS streamflow, NASA moon image, snakes/lizards, sound recordings, citizen-science scaffolding), which ones *you* actually look at when you open the app? Which ones do you mostly never visit?
12. When you imagine the dashboard a year from now, what's the change you most want? More breadth (mammals, moths, ferns)? More depth (each thing the dashboard already covers gets richer)? More liveness (the place feeling more present-tense)? More history (the dashboard remembering)?
13. Is there a kind of card or content you've thought about adding and decided against — that would help name what *doesn't* belong here.
14. Does the dashboard ever feel too full to scan? Where, when?

### About the AI synthesis idea (parked in CLAUDE.md)

15. The "today on the property" italic line — would you want that synthesized once a day (running on a backend), or is the current rule-based gardener-insight close enough? What does the difference need to be worth?

### About Paul's own observations going into the journal

16. Have you ever taken a property note somewhere (Notes app, photo with caption, anywhere) that you'd want the dashboard to absorb? Where do those live now?
17. Is the dashboard meant to stay read-only, or is having a place for *your* observations and Mom's part of the long arc?

---

## 5. Top 3 ideas to talk through, and the discovery work that would unlock them

Picking the three I think are most worth Paul's time, given the field-journal posture, the under-served jobs, and what's been shipped recently.

### Top pick 1: Mammals card (Paul's seed, with discipline)

**Why:** Paul named it. JTBD-3 (identification + curiosity) is partially served and mammals are the obvious gap. The build pattern is well-established (snakes and lizards landed in the same shape). Field-journal fit is clean if the trail-cam/surveillance temptation is resisted.

**Discovery that would unlock it:**
- Q5 + Q6: which mammals does Paul actually encounter, vs. know are there? Calibrates whether the card is "what I'm seeing" (start with deer/raccoon/squirrel/chipmunk/skunk/opossum, the visible ones) or "what's on this land" (extends to bobcat/coyote/black bear/red fox, the harder-to-see ones).
- Q7: bear/coyote handling tone. Mirror snakes-card calm-info voice, but only after confirming Paul wants safety notes here at all.

**Effort:** ★★★. Schema, JSON, renderer (parallels existing reptile renderer), photo curation (Wikimedia Commons coverage is good for mammals), sounds optional.

### Top pick 2: Ship the surface-fact callouts cluster (the ★ effort cluster from the backlog)

**Why:** This is the *highest signal-to-effort* expansion available right now. Cherokee land context, Tate Mountain Estates history, Bortle 3 reference, keystone genera, burn-ban banner, Homegrown National Park registration — each is a paragraph of static content. Each serves JTBD-5 (deepening). Collectively they'd transform the Property card from "facts about this address" into "the dimensional story of this place."

**Discovery that would unlock it:**
- Q13: Anything in this cluster Paul has thought about and decided against? (e.g., is there a reason the Cherokee-land subsection isn't shipped yet — sensitivity, tone-not-yet-found, just hadn't gotten to it?)
- Q14: How much density can the Property card absorb without breaking the leisure-reading posture? — *Especially for Mom.*

**Effort:** ★ per item, ★★ for the cluster delivered well. The bottleneck is voice-crafting, not engineering.

### Top pick 3: Year-on-a-ribbon phenology view OR the "this week on the property" digest (one of these two)

**Why:** The single biggest *untouched* job is the seasonal-arc / phenology layer (JTBD-6's under-served slice, plus JTBD-5). Both these ideas are different solutions to the same job. Both leverage data already in the dashboard rather than requiring new external integrations. Both feel deeply field-journal-grade in a way that no current view does — the dashboard currently does "what's happening this month" well but doesn't do "the shape of the year on this land" at all.

The ribbon version (C2) is more visual and ambient — it lives in the dashboard. The digest version (E1) is more narrative and temporal — it lives in a "week ending May 18" archive. They serve subtly different jobs (ambient vs. retrospective).

**Discovery that would unlock it:**
- Q11: When Paul opens the dashboard for himself, which existing surfaces does he actually look at? — *Helps decide whether a new ambient ribbon will get attention or compete for screen real estate with current ones.*
- Q12: Breadth vs. depth vs. liveness vs. history — which is Paul's most-wanted vector for the next year? — *If "history," then phenology + weather-history-visualization (D5) cluster together as the strongest play. If "breadth," mammals + Lepidoptera win. If "liveness," the synthesized today-line (C1) wins.*

**Effort:** ★★★ for either.

### Honorable mention — the AI-synthesized "today" line (C1)

The most field-journal-grade single idea on this whole page, but the discovery question (Q15) is whether the lift from a rule-based to LLM-driven version is worth a backend, given that `generateGardenerInsight` is already doing real work. If Paul is willing to stand up a small server proxy (he might be doing this anyway for AirNow / NCEI / USDM), C1 becomes much cheaper and the system effects across the dashboard are large. Worth raising specifically as a "do this *with* the proxy work, not separately" framing.

---

## Closing note

The dashboard has shipped a lot in the last two weeks. The deferred Etowah Darter callout is a tell — Paul is curating away from anything that overclaims, even when it's interesting. That instinct points away from "add everything in the research library" and toward "ship the small, accurate, deepening pieces, and protect the leisure-reading posture as the dashboard grows."

The biggest creative-stretch idea here is the framing in Section 1's persona — that Tate Tracker is identity work as well as reference work. If Paul recognizes that framing, several ideas (E2 Paul's own observations, E1 weekly digest, C2 year-ribbon, the AI-synthesized today-line) all serve it together and would together form a coherent next major arc. That arc would be larger than mammals — but mammals is a fine concrete first step.
