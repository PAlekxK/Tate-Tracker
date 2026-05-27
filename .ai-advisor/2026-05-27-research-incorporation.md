# Fernwood — Research incorporation directions + Phase G minimum shape + star verdict

**Date:** 2026-05-27
**Mode:** ai-advisor consult
**Prompt:** A. 5-8 directions for incorporating more info/research into the dashboard; B. Phase G minimum viable shape; C. Verdict on the ⭐ affordance.

**Read to ground this:** CLAUDE.md (pickup), `candidates.json`, `sources.json`, `references.json` (8 categories, 145 entries via `tools/build-references.py`), `events.json`, `research-resources.md` (~85+ entries, Top finds + Quick reference + Cat 1-8), `.audit/2026-05-26-telemetry-rollup.md`, PHASE_E_DESIGN.md Q3/Q6, PHASE_E_MVP.md, project memory listed in the prompt.

---

## Framing — the constraint stack

Six rails everything below has to ride between:

1. **No AI on capture.** Capture/log/save is deterministic. AI is only on explicit ask (Garden Guru, Phase F image ID, future Phase G batch roll-up — user-triggered).
2. **Field-journal voice, not task-manager voice.** Memory, not database rows. "You noted X last spring" not "3 alerts."
3. **Depth filter.** Property scope, not regional completeness. "Worth Considering" softens this by extending canon to "what someone at the property could plant/observe" — but only against curated candidates Paul has vetted.
4. **Ground-truth research claims** before they get card-level callouts (the Etowah darters demotion is the canonical example).
5. **Mom-no-glasses** carries meaning via icon/size/color/position — not by fine-print labels.
6. **Cost ~$5/mo current; stay in that range** absent strong reason. Telemetry confirms current spend ([rollup](../.audit/2026-05-26-telemetry-rollup.md)).

The wedge is **curation + surface** — the same principle that won Phase F over consumer Claude (`~/.claude/ai-playbook/fernwood.md`). Every direction below earns its room either by (a) being something general Claude can't do because it doesn't have the curated data, (b) compounding with each year of observations, or (c) making the surface Mom already opens more rewarding to open.

---

## A. Eight directions for incorporating more info/research

Ranked roughly by signal-to-effort. The top three are the strongest picks.

---

### 1. Seasonal "What's on the property right now" callouts driven by curated reference data (no AI)

**One paragraph.** A small editorial block at the top of each major card — Plants, Wildlife, Celestial, Property — that surfaces the 1-3 most relevant research-backed facts for the current week, drawn from `references.json` framing lines and the existing `peakWindow` / `monthsActive` data already in `plants.json` / `birds.json` / `amphibians.json` / `events.json`. No new data — recompose what's already curated. Pure JS at render time. Example for late May at 2,959 ft: "Mountain laurel is in its peak window. Hummingbirds have returned and are at the feeder. The North GA chapter native plant sale is Saturday in Blairsville." Each line points to the underlying card section. Lives as a single `.season-callout` strip beneath the Today line on the dashboard, or as a small block at the top of each card body (preferred — meaning travels with the card).

**Effort:** S (1 session, ~150 lines JS + CSS; entirely deterministic; uses existing `peakWindow` / `monthsActive` / `events.json.dates` / `next` fields).

**Cost:** Free. No API calls.

**Constraints stressed:** None of the AI ones. Tone: needs a content-steward pass on the callout phrasing template ("Worth checking this week — laurel is in its peak window" vs "Mountain laurel peak: May 21-June 4"). Mom-no-glasses: the block has to use the same 19px serif Crimson treatment the Worth Considering card uses for plant names.

**Validation question.** *Does the most-active iPhone (likely-Mom, `d-14nyhnjz`) start expanding cards more — specifically, does `card_section_viewed` rise on the section the callout points to? Does Paul notice himself reading the dashboard differently the week it ships?*

**Why this is #1.** The single richest under-used asset on the project is `references.json` framing lines + `peakWindow` data. Zero AI, zero cost, zero new constraints, and it directly answers the headline ask. The dashboard already knows mountain laurel peaks May 21-June 4 — it just doesn't say so on the front of the card. Telemetry already confirms `card-plants` and `card-wildlife` are the most-viewed cards; this makes those views more rewarding without taxing them.

---

### 2. "Worth Considering"-style curation pattern, extended to **observable** species and **referenceable** history

**One paragraph.** The Worth Considering card (shipped 5/26) is the project's best-shaped surface for moving research from `research-resources.md` into card-level visibility while staying within the depth filter. Extend the same pattern to two new cards: (a) **Worth watching** — observable wildlife/plants that aren't yet on the property but plausibly could appear given the elevation, watershed position, and Bortle 3 (e.g., barred owl after dark, fox squirrel along the front fairway, fall warbler migration windows, the 2026 lunar eclipse window). (b) **Place stories** — a small rotating card surfacing 1-2 history/heritage stories from research-resources.md Cat 7 (Cherokee place-names on Talking Rock Creek, Mount Oglethorpe as the original AT terminus, the Connahaynee Lodge fire, Pickens Union flag, Cherokee marble use ~800 AD). Same shape as Candidates: structured JSON (`watching.json` / `stories.json`), serif-Crimson headers, framing line in field-journal voice, source links. The depth filter still applies — every entry has to pass Paul's "this is actually Fernwood, not regional fluff" gate. Same `lastVerified` freshness convention.

**Effort:** M for each card (1-2 sessions per card; mostly content curation work, not engineering — schema mirrors candidates.json, the renderer is ~80 lines).

**Cost:** Free. Pure curation.

**Constraints stressed:** Depth filter hardest — Paul must vet each entry against "would I realistically encounter this on the property?" The 2026 lunar eclipse passes; "barred owl in the area" needs Paul's confirmation he's actually heard one or has a specific reason to expect one. Ground-truth check applies — Mount Oglethorpe is "on the slopes of" the property (Cat 7) but is it visible from the property line? Verify before promoting.

**Validation question.** *Does either card crack the top-half of `card_section_viewed` within 30 days? Does Mom or Paul mention specific content from either card in a Garden Guru conversation? (That second signal — research bleeding into ask-path use — is the real product win.)*

**Why this places #2.** It's the durable shape. Candidates proved card-level structured curation works; replicating it for the rest of the research library converts ~85 entries from "appendix" into surface-level material card-by-card. Lower per-card velocity than #1, but each card adds permanent surface area. The history card especially compounds with #6 below.

---

### 3. Phenology spine: per-species "the property's own calendar" learned from observations + grounded in research

**One paragraph.** The biggest gap in the curation right now is that `peakWindow` for each plant is research-derived (NOAA normals + elevation adjustment) rather than property-derived (Paul's actual observation of when the laurel opens in *this* cove with *this* aspect at *this* elevation). The phenology spine direction is: for each species in `plants.json` / `birds.json` / `amphibians.json` etc., maintain a small `propertyPhenology` field that's populated by Paul (and Mom, when their entries cite a species + date). The dashboard reads from `peakWindow` (research) for the first year; switches to `propertyPhenology` (observation) once 2+ years of entries exist. The transition is the Phase G win — the dashboard knows *this* azalea on *this* slope. Rendering: a small "Last year you noted…" line beneath the peak-window callout. Field-journal voice — memory, not database rows. The first season this fires for a species, it should feel like the journal remembered.

**Effort:** L (~3-5 sessions). Schema (`propertyPhenology: { firstBloom: [{year, date, source}], firstSighting: [...] }`); index over `tateTracker.observations.v1` keyed by speciesId; render integration on each card; Paul-curation tool to confirm/correct AI-classified observations before they enter the phenology index. **Depends on Phase G being live** (this *is* the killer Phase G consumer — see section B).

**Cost:** Low. Phase G batch roll-up runs Haiku to extract `{speciesId, eventType, date}` triples from accumulated observations once per week or on-demand. At current cadence (~6 saves in 6 days, plus 10 conversations) a weekly batch over a year is ~50K input tokens cached + small outputs = under $1/month.

**Constraints stressed:** No-AI-on-capture preserved (extraction runs in batch, user-triggered). Depth filter strongly satisfied — this is the most property-specific surface possible. Ground-truth filter sharpens automatically (the only data that enters is what Paul actually observed). Voice constraint is the hardest part — the rendering language has to feel like memory ("Last year, the laurel opened by the spring on April 28" not "Per observation log entry o-2025-04-28-mountain-laurel-bloom").

**Validation question.** *After one full season of accumulation, does Mom or Paul ever say (in a Garden Guru turn or in conversation) "remember when…"-style language back at the dashboard? Does the Worth-Checking-This-Week section (direction #1) feel different when it's grounded in last year's date vs. NOAA normals? This is the ultimate Phase G validation.*

**Why this places #3 (and is the strategic pick).** This is what observations *should* compound into. Until it lands, every entry Mom and Paul save is a sunk cost — read once, never read again. Phase G's whole promise is that observations stop being sunk. This direction is what makes Phase G worth building. Effort is L because it's a real feature; but the architectural shape is small (one batch job, one new JSON field per species, one render line). Land #1 and #2 first to prove the curation-as-research pattern; land this next.

---

### 4. Sources card "what's new in the library" surfacing

**One paragraph.** `references.json` is rebuilt from `research-resources.md` via `tools/build-references.py`. Add a `dateAdded` field per entry (default to `_meta.lastBuilt` for existing entries; populated correctly going forward). The Sources card gets a small "Recently added" indicator on entries added in the last 60 days — green dot or a faint "new" chip, no badge counters. Paul stops doing research in silence — Mom can see when a new entry lands. Bonus: the rebuild script can write a one-line release-note style entry into the Release Notes card when new sources land ("Added GNPS Habitat Certification reference" — voice still field-journal, content-steward pass needed on the template). Connects to **builder velocity is not project velocity** — making research additions visible turns silent build-time into project-time.

**Effort:** S (1 session — extend the rebuild script, add a CSS chip, optional Release Notes hook).

**Cost:** Free.

**Constraints stressed:** None significantly. Tone: chip wording matters but is light. Mom-no-glasses: needs to be a green dot or color-change, not micro-copy.

**Validation question.** *Do Sources card views rise after a research-resources.md update lands? Does Paul use it himself as an editorial nudge to write release-notes for additions he otherwise would not have surfaced?*

**Why this matters.** Smallest mechanical change with the largest second-order effect on Paul's discipline: research that doesn't reach the surface is research that doesn't get used. Pairs well with #1 (a new reference framing line becomes available for the seasonal-callout pool).

---

### 5. Property history overlay — small, manual, place-anchored history block on the Property card

**One paragraph.** The Property card currently never gets expanded (telemetry: 0/45). The summary is enough. But there's a missing dimension: the property card knows location/elevation/microclimate/soils but says nothing about who lived here before, what the development around it is, and what the land remembers. From research-resources.md Cat 7 (17 entries) there are 5-8 anchors specific enough to surface: Cherokee land 1793-1838, Sanderstown / Talking Rock Creek / Long Swamp Creek as Cherokee communities, Sam Tate's 1928 development, the 1930 Lake Sequoyah dam completion, the 1946 Connahaynee Lodge fire, Mount Oglethorpe as the original AT terminus, the marble heritage going back to ~800 AD, the Pickens Union flag. A small "Place memory" sub-card or third tab on the Property card surfacing one rotating item per visit, each with a research-resources.md framing line. Rotation is deterministic — hash(date) % N. This is the heaviest version of direction #2's place-stories option, lived in the Property card instead of as a standalone.

**Effort:** S-M (1-2 sessions; content curation is the bulk).

**Cost:** Free.

**Constraints stressed:** Ground-truth filter — "Cherokee land" passes (documented). "Mount Oglethorpe was the AT terminus" passes (documented). "Lake Sequoyah named for the silversmith who created the syllabary" passes (Top finds #9). Anything that says "your land was…" needs the same property-scale check as the darters did. Some entries are about Tate Mountain Estates or Pickens County, not the specific 282 Church Mountain Road lot — those need a "framed as: the development around you" voice register, not "your land."

**Validation question.** *Does the Property card start getting expanded? Does the Place Memory item ever come up in a Garden Guru turn (Mom or Paul asking "wait, what's this about Sanderstown")?*

**Why it's here.** The Property card is a known under-used surface. The research backlog has the material to fix it. This is one of the cheapest ways to convert dormant research into dashboard surface.

---

### 6. Cross-species linking — "when X blooms, Y arrives" callouts

**One paragraph.** Phenological co-occurrence is one of the most evocative field-journal patterns. When the trout lily blooms, the ruby-crowned kinglet leaves. When the laurel opens, the rose-breasted grosbeak passes through. When the rhododendron is in peak, the hummingbird population spikes. Build a small `coOccurrence.json` (manually curated, depth-filtered to species on the property) and a small `.cross-species-callout` block that fires when one species enters its peak window. Sourcing: Audubon + Birds Georgia + Cornell BNA + Paul's own observation pattern, vetted against actual property species. This is what general AI cannot do (no curated species set, no property scope); it's the wedge incarnate.

**Effort:** M (curation-heavy — 1-2 sessions to build the co-occurrence map at depth-filter scale; render is light).

**Cost:** Free.

**Constraints stressed:** Depth filter — every link has to be species-pair Paul actually expects on the property, not regional pairs. Ground-truth filter — Phase G will start surfacing actual co-occurrence in the observation data; the manual map should defer to observed pairs as they emerge. Voice — the callout needs to read as observation, not data ("the laurel and the grosbeak share the same week here" not "Co-occurrence: Kalmia latifolia + Pheucticus ludovicianus").

**Validation question.** *Does anyone reference a cross-species link back in a Garden Guru turn? Does it survive the 2nd-year accuracy check when Phase G's observation data lands?*

**Why it's here.** It's the pattern that most makes the dashboard feel alive. But it stresses the depth filter hard, and it doesn't compound the way phenology does — once curated, the map is static unless Paul refreshes it. Better as a 2nd-year direction than a now direction.

---

### 7. "What's blooming nearby" — passive surfacing of GNPS native plant sale dates + nursery freshness as actionable surfaces

**One paragraph.** `sources.json` already tracks `lastVerified` and `next` event dates for programs/nurseries. The Worth Considering card surfaces the May 30 GNPS sale as an amber callout. Extend the same pattern: a small "Next sourcing window" line that surfaces the nearest-in-time sale across all `programs[]`, regardless of which candidate it sources — so the GFC seedling catalog opening July 1 surfaces in late June without needing to be tied to a specific candidate; Connect to Protect's Plantapalooza in spring surfaces ahead of spring. Also: faded `lastVerified` chips on nurseries that haven't been re-checked in 12+ months become visible as a Paul-side editorial nudge ("the 2019 SBG/GNPI nursery entries need 2026 confirmation" — currently buried in the Worth Considering card notes).

**Effort:** S (1 session — calendar logic + the freshness-aware chip).

**Cost:** Free.

**Constraints stressed:** Voice — the line has to feel like a friendly nudge, not a notification ("Sources card has 3 sales coming up this season"). Mom-no-glasses: dates need to be at 16px+ with amber color (not red — Fernwood doesn't do urgency).

**Validation question.** *Does Paul actually go to one of these sales because the dashboard surfaced it (and not because he separately tracked it)? Does the nursery freshness chip turn into committed time spent verifying entries?*

**Why it's here.** This is the action-bridge. Most directions above are "the dashboard tells you more about the place"; this one is "the dashboard moves you to do something on the property." It's modest in effort but pairs with #2 — once Worth Watching exists, the same sale calendar serves both.

---

### 8. Passive bridge from `research-resources.md` additions into a "curation queue" the dashboard exposes (not the same as #4)

**One paragraph.** Different from #4 (which surfaces new entries in the *Sources* card). This direction: when Paul adds a research entry with a Dashboard integration idea in `research-resources.md`, the build script writes that integration idea into a `.research/integration-backlog.json` file that the dashboard surfaces — but **only to Paul, on the desktop view, behind a query param or a click-to-show toggle**. It's a Paul-side workshop view: every research entry with a not-yet-shipped integration idea shows up as a small triage queue. Doesn't ship to Mom. Closes the loop between research-resources.md ideation and the actual surface-building backlog. Connects to **builder velocity is not project velocity** by making the integration backlog visible as part of the dashboard's own meta-state.

**Effort:** S (1 session — script extension + dashboard URL-param-gated render).

**Cost:** Free.

**Constraints stressed:** Mom-no-glasses irrelevant (not shipped to Mom). Voice irrelevant. Mostly an engineering tidiness move.

**Validation question.** *Does Paul use it? If not in 30 days, kill it.*

**Why it's here.** It's the smallest direction; it makes Paul's research work visible to himself in the dashboard rather than as a separate file. Useful but not load-bearing — last on this list because it's adjacent to the user-facing question.

---

## B. Phase G — minimum viable shape

**The smallest first slice that proves the loop: observations feeding back into other surfaces.**

### What it is (the slice)

A **species-tagged observation index** built by a user-triggered batch script, surfaced through one render line on Plants tab cards.

Concretely:

1. **Trigger.** A `tools/rollup-observations.py` script Paul runs manually. Same shape as `tools/analyze-fernwood.py`. v2 can become weekly cron via a Worker scheduled trigger — explicitly out of scope for v1. **No on-save AI** preserved.

2. **What it does.** Fetches conversation + entry text from KV (`/api/conversations`, `/api/admin/clean-observations` already exists for reads; a small new GET endpoint may be needed). Runs one Haiku-4.5 call (the dormant `/api/classify` shape, exhumed) per accumulated entry that hasn't been processed yet, extracting `{speciesId | null, eventType: "sighting" | "bloom" | "habitat-note" | null, date, confidence}`. Writes results into a new KV key `observations:index:v1`. Idempotent — entries already in the index are skipped. Hard fail on hallucinated speciesIds (must match an id in `plants.json`/`birds.json`/`mammals.json`/`amphibians.json`/`snakes.json`/`lizards.json`/`fishing.json` — the same fuzzy-match logic Phase D's classifier had).

3. **What it surfaces (one render line only).** On each plant card's `currentSeasonNote` block, append a single line if the species has any entries in the index: *"You noted this last year on April 28."* (Format: most recent `eventType` of the most-recent prior year, in field-journal voice.) Nothing else. No filter, no detail view, no "see all entries." One line. Memory.

4. **What it does NOT do in v1.**
   - No automatic cross-species linking (that's direction #6, not Phase G itself).
   - No `propertyPhenology` taking over from `peakWindow` (that's direction #3 once Phase G has 2+ years).
   - No Garden Guru system-prompt augmentation with the index (that's a Phase G+ — adds cost and complexity).
   - No write-back into Garden Guru turns ("turn this conversation into an observation"). Conversation auto-save already covers logging; the index is downstream.

### Cadence

**On-demand for v1.** Paul runs the rollup script when (a) the observation set has grown enough to be worth re-indexing, or (b) he wants the dashboard to reflect a recent observation. **Weekly cron via Worker scheduled trigger is the v2 affordance** — wait until v1 proves the loop is worth it.

### Where it crosses the AI line and where it stays safe

- **Safe (capture path):** Save still saves raw text only. Conversation auto-save still saves raw text only. No AI runs on save. *Unchanged.*
- **Safe (ask path, deliberate):** Paul running `tools/rollup-observations.py` is deliberate, batch, user-triggered. The script is the AI seam. Same architectural shape as Phase F's promotion path or `analyze-fernwood.py`.
- **Watch:** If a future iteration adds the index to Garden Guru's system prompt context (so Guru can say "your records show you saw the laurel open April 28"), that's still ask-path (Guru is invoked deliberately) but it does increase per-turn cost and context size. Defer.
- **The cliff:** Don't let "wouldn't it be nice if it ran on save" be the v2 framing. The whole architecture rests on capture staying deterministic. (`~/.claude/ai-playbook/cross-cutting.md`)

### First validation gate

After 30 days of v1 in production: does the "You noted this last year on…" line ever appear, and does Mom or Paul respond to it (expand the card, save a new entry, mention it in a Guru turn)? If the line never appears (observation set too sparse), Phase G v1 is premature — defer until observation count is higher. If it appears but no one engages, the rendering needs work, not the architecture.

### What this v1 leaves for later

- The full Phase G feedback-loop vision in `project_tate_tracker_observations_feedback_loop.md` (today-line ground-in-recent-observations, Garden Guru turn-by-turn observation reference, full propertyPhenology takeover) is the **direction**. The species-index + one render line is the **smallest step that proves the loop works**. Everything else is the next step after this one earns it.

---

## C. Verdict on the ⭐ star

**Kill it.** Replace the implicit curation hypothesis with the implicit curation signal that's already running.

### The argument

The telemetry is unambiguous: **0 stars across 104 entry revisits over 6 days** (`.audit/2026-05-26-telemetry-rollup.md`). The hypothesis was that users would curate by tapping a star to elevate a "this matters" entry. The signal is that **users curate by revisiting**. Revisit-to-save ratio is ~17:1; revisits are happening at scale. The act of returning to an entry *is* the "this matters" signal.

That observation also makes the future 🚩 "flag for Paul" affordance redundant in the same way (`feedback_defer_affordances_pending_signal.md` — both ux-expert and engineering-partner converged on "don't build the flag until the star has proven the pattern"; the star did not prove the pattern).

### The replacement

Reframe the almanac view's filter from a starred / unstarred toggle into a **most-revisited** sort. Entries that have been opened more than once in the last 30 days surface at the top. The "this matters" semantic is preserved (curation by Mom and Paul, not by Paul-as-product-designer) without forcing a new gesture.

The implementation cost is minimal — `entry_revisited` metrics already populate this signal. Read the metrics KV (already accessible via `analyze-fernwood.py`'s endpoints) at render time, or — better — sync per-device revisit counts into `tateTracker.observations.v1` as a `revisitCount` integer per entry and sort by that locally.

### What about the meta-feedback channel?

The 🚩 promotion gate in `project_fernwood_almanac_save_model.md` was conditional on T+30 Mom-interview signal + star-affordance validation. The star failed to validate. **The 🚩 build doesn't get unlocked** — and that's a clean answer, not a punt. Paul's interim workaround (read the almanac, surface meta-feedback manually) stays the right shape. The T+30 Mom interview should now ask: *"When something doesn't feel right or you have an idea, how do you tell me?"* — open-ended, no app-channel presupposition.

### Why kill rather than redesign

Redesigning the star (bigger, more obvious, different icon, different placement) is the design-review trap. The signal isn't "the affordance was wrong" — it's "the interaction pattern this affordance assumed doesn't exist as a Mom/Paul behavior." Spending engineering time relocating it is paying ongoing maintenance on a UI element no one is using. Better to harvest the same outcome (curated highlights) from the revisit signal that's already running, and free the right-side icon slot for something that might earn it later.

### Migration

- Remove the ⭐ button from each entry's row and the ⭐ filter chip from the Almanac card.
- Remove the `starred` / `entry_starred` / `entry_unstarred` boolean and event types from the data layer (keep the KV key alive for historical reasons — zero existing entries use it).
- Add a "Most revisited" sort option to the Almanac view next to "Most recent."
- Update the meta-feedback channel section of `project_fernwood_almanac_save_model.md` to record this verdict.
- Note this in CLAUDE.md pickup as a closed item.

---

## What this advisory implies for the next session

Punch list, in order:

1. **Decide on direction #1.** It's the lowest-risk, highest-leverage, zero-cost change. If Paul wants to ship it, the next session is small.
2. **Decide on the star.** Kill, redesign, or accept revisit-frequency-as-signal. The advisory recommends kill + sort by revisits.
3. **Confirm Mom = `d-14nyhnjz`** before any of this lands — the validation questions all reference Mom behavior, and that mapping is the load-bearing measurement infrastructure (rollup followup #1).
4. **Sequence #2 (Worth Watching + Place Stories) and #5 (Property history overlay) together** — they share curation work from research-resources.md Cat 7 and would benefit from one editorial pass.
5. **Phase G minimum shape (section B) waits** until #1 and #2 ship and an observation set has grown beyond the current 6-entry baseline. Direction #3 (phenology spine) is the killer Phase G consumer — but it needs 2 seasons of data before it can replace research-derived `peakWindow`, so the v1 species-index shape (one "you noted this last year on…" line) is the right slice now.
6. **Directions #6 (cross-species), #7 (sale calendar), #8 (research-integration backlog) sit in the next-quarter queue.** They're durable but not load-bearing.

---

## Open advisory follow-ups for Paul

These didn't fit the headline ask but are worth surfacing:

- **The Sources card is the dashboard's most under-engaged card** (28 views, 2 expands per the rollup). Direction #4's "Recently added" indicator is the smallest thing that might change that ratio; if it doesn't, the card may need to be re-framed (or the categories restructured). Worth a separate session if the indicator doesn't move the needle in 30 days.
- **`peakWindow` data is the dashboard's most under-surfaced asset.** It's per-species, property-elevation-adjusted, and only currently shown inside the Plants card body. Direction #1 fixes that. If it lands and works, the same pattern should be considered for the Wildlife card (`monthsActive` is the bird/amphibian equivalent and is similarly under-surfaced).
- **Phase G architecturally is small.** Most of the design work has been done in the dormant `/api/classify` endpoint (Phase D), `tools/analyze-fernwood.py` (the analysis pattern), and `worker.js handlePromoteSpecies` (the GitHub-write pattern). The minimum shape recombines existing pieces.

---

## Sources

- Anthropic API pricing 2026 — Sonnet 4.6 $3/$15 per MTok; Haiku 4.5 $1/$5 per MTok; cache reads at 10% of base input ([Anthropic Pricing](https://platform.claude.com/docs/en/about-claude/pricing); [Claude API Pricing 2026 — BenchLM](https://benchlm.ai/blog/posts/claude-api-pricing))
- `~/.claude/ai-playbook/fernwood.md` — wedge is curation + surface, ask vs. capture path
- `~/.claude/ai-playbook/cross-cutting.md` — builder velocity, ask vs. capture, prompt-caching as first-pass concern
- Fernwood telemetry rollup 2026-05-26 — usage signal grounding the star verdict and the validation questions
