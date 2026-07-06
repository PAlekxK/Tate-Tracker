# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Session-start check — is the dashboard showing all of canon? (run at every Fernwood pickup)

**Run this first thing when picking up Fernwood, before other work:**

```bash
python3 tools/check-data-inline.py
```

It compares the source JSON (`plants.json`, `mammals.json`, `birds.json`, …) against the inlined `*_DATA` constants in `viewer.html`. Exit 0 = in sync (say nothing, move on). Exit 1 = **drift** — surface it.

The drift that matters most is **canon-ahead**: a species present in the JSON but *missing from the inlined data*. That almost always means **Garden Guru added it to canon but the re-inline step didn't land**, so a real, confirmed addition is sitting invisible on the dashboard. This is exactly how **Lizard's Tail** hid unnoticed until 2026-07-05.

When drift shows, don't auto-fix — the point is a **human signal that the addition is legit**:
1. Surface the specific species to Paul, framed as "added to canon (likely via Garden Guru) but not yet on the dashboard — legit?"
2. Get Paul's confirm that it's a real addition (his call, not an automatic one).
3. Only then `python3 tools/check-data-inline.py --fix`, verify clean, add a release note, commit.

(Root-cause fix still open: make Guru's promote flow verify its own re-inline commit landed, so this drift can't open silently in the first place.)

## Backlog — raised 2026-07-05 (Concept A session)

- **Save/Ask two-button intent split — revisit (design, Paul-raised).** Paul isn't convinced the app needs both "Save to journal" and "Ask Garden Guru" buttons. *Don't just remove them* — the split is the on-screen form of Paul's own capture-path principle ([[feedback_no_ai_on_capture]]): Save = deterministic, AI-free, logs verbatim words; Ask = the AI path. Collapsing forces either all-capture-through-AI (breaks the principle), intent-guessing on the capture path (what Phase D pivoted away from), or do-both-every-time. The 7/2 Mom evidence ("I hoped it was logged but wasn't sure") argues for a *distinct* Save. Likely resolution is **hierarchy, not removal** — make Save the primary action, Ask the quiet secondary — but confirm what's actually bugging Paul (clutter vs choice-friction vs one-intent-dominates) first. Consider a ux-expert read since this was an evidence-based decision.
- **Refined "Peak this week" — needs a structured peak field (data work).** Audit 2026-07-05: all 23 plants carry peakWindows (88 total), but **~40% (35/88) don't parse** via `parseShortDateRange` — it only reads "Abbrev D–Abbrev D"; it misses full month names ("May 15–June 5"), month-only ("Mar — before growth begins"), prose-only ("After first hard frost flattens leaves"), and multi-window ("Mar …; Jun …"). There's also a year-wrap bug (winter-spanning windows parse to negative spans). Net: the peak-this-week surfaces (tile + card panel) are **under-inclusive** today. Right fix = add a machine-readable peak field to the schema (e.g. `peakStart`/`peakEnd` as MM-DD, keep the prose for display), which removes both the parser fragility and the prose-only cases. Deep winter (Dec–mid-Jan) is legitimately empty — that's fine, it has a calm fallback.
- **Fishing data — make it granular + dynamic (Paul-raised).** Push `fishing.json` past coarse seasonal notes toward **time-of-day** guidance and **live weather-station-driven** conditions — e.g. how an incoming rain front (read from the on-site Ambient station / Open-Meteo) shifts the bite. Make the fishing view respond to real conditions rather than static month text. Scope TBD; ties to the empirical-sources-in-the-data-layer direction.

## Pickup point — last session ended 2026-07-05

**Concept A ("Today + Reference Drawer") built end-to-end, then iterated with Paul into a leaner IA. All shipped, pushed, LIVE on GH Pages (Tate-Tracker HEAD `630d742`).** Plan + handoff note at `.engineering/2026-07-05-concept-a-today-drawer-plan.md`; design source `.design-research/2026-07-05-journeys-ia-patterns.md`.

### What shipped (9 commits, all pushed)
- **Concept A Phase 1** (`4e22846`) — reference drawer: 6 living cards (Weather, Plants, The Fairway, Wildlife, Sky & Stars, The Almanac) + 5 durable cards behind one collapsible **"Reference"** shelf.
- **Phase 2** (`9cc7925`) — `computeLookFors(now)`: pure, deterministic, AI-free "what's worth noticing this week" generator (narrow/opening plant windows + bird arrivals/departures + active peak mentions; deduped, capped 4, day-of-year-rotated; copy only from the §5.3 template bank; amphibians deliberately skipped — no calm template).
- **Phase 3** (`8c5358f`) — the look-for surface + tap→composer pre-warm (fills an editable starter, never clobbers typed text).
- **Lizard's Tail re-inlined** (`ec950ef`) — Guru-added to `plants.json` but never re-inlined (22→23); Paul confirmed legit; now shows in the Plants card.
- **Drift-check wired into pickup** (`7867755`) — the "Session-start check" section above runs `check-data-inline.py`; surfaces canon-ahead drift (the Lizard's-Tail failure mode) for confirm-before-`--fix`.
- **Peak this week promoted** (`fc54923` + `630d742`) — Plants tile leads with peak (each plant **with its action**) over the monthly dump (demoted to a "This <month>" breadcrumb); new **"Peak this week"** panel inside the Plants card (plant + care pill + window). Shared `plantsAtPeakThisWeek()` helper.
- **IA reorder** (`f9b6a1f`) — retired the standalone "Today at Fernwood" glance; **Garden Guru composer moved to the TOP** (under header, above tiles); look-fors folded into the Plants card as **"Worth noticing today"** (card kept named "Plants" — Paul's pick over a rename). Final order: header → composer → tiles → cards → drawer.

### ⚠️ Owner: Paul — review live on phone (in progress)
1. **Tap a look-for → Save**, confirm your words land in the Almanac on the real device (only the phone can close this). Look-fors now live *inside* the Plants card — open it to see/tap them.
2. Two open UX judgments (flagged, not decided): **(a)** look-fors are now behind a tap (inside Plants) — too buried vs. always-visible? **(b)** "peak this week" now appears in the tile + the in-card panel + "Worth noticing today" — a lot of "this week" in the Plants area; merge/thin?

### Backlog raised this session — see the "## Backlog — raised 2026-07-05" section above
Save/Ask two-button split (revisit hierarchy vs the capture-path principle) · refined "Peak this week" needs a structured peak field (~40% of peakWindows don't parse — audit done this session) · fishing data granular + dynamic (time-of-day + weather-station-driven) · root-cause: make Guru's promote flow verify its own re-inline landed.

## Pickup point — last session ended 2026-07-02

**Garden Guru conversational redesign — Phases 1–3 built, verified, and DEPLOYED LIVE.** Worker deployed (version `123ea421` @ tate-tracker.paul-kirschenbauer.workers.dev); viewer pushed to GH Pages (Tate-Tracker HEAD `23ac94f`). Commits: analysis+plan `508010c`, Phase 1 `c8fb1a1`, Phase 2 `a3130ef`, Phase 3 `7d8eba2`.

### What drove it (evidence, not inference)
Pulled all 16 real Garden Guru conversations from KV (through 2026-07-02) → `.user-research/2026-07-02-garden-guru-conversation-analysis.md`. Ran the full expert panel (ux / eng / ai-advisor / user-researcher) + got Mom's direct answers to 4 verification questions. Findings: follow-ups were blocked by a **missing affordance, not missing demand** (15/16 conversations one-turn; the telemetry's "no follow-up demand" was backwards); Mom (`d-14nyhnjz`, confirmed via her answers = the active daily user) is a **satisfied one-shot user whose real gap is logging-with-confidence** ("I hoped it was logged but wasn't sure"); two capture intents (log-on-known vs add-new). Full settled plan: `.engineering/2026-07-02-garden-guru-redesign-plan.md`.

### What shipped
- **Phase 1** — re-anchored the conversation UI to the universal chat model (compose area drops beneath the latest reply via CSS flex-order); follow-up photos work; one calm **suggested-follow-up chip** (pull, not push — a `suggest-followup` fence, never a question in Guru's prose); turn-continuity in `GARDEN_GURU_SYSTEM`.
- **Phase 2** — **log-an-observation** on a known plant: a `suggest-log` fence → deterministic "Note this on the [plant]" affordance → writes the reader's **verbatim words** (never Guru's diagnosis) to the AI-free ObservationStore, with an unmissable "Noted ✓" confirmation. Closes the recurring "became Paul's manual INQUIRIES.md entry" loop.
- **Phase 3** — **add ⇄ remove a plant** from conversation. Add: seeding interview → `suggest-add` fence carrying the reader's facts as `userNotes` (the authoritative superseding layer) → double-confirm → `/api/promote-species` drafter (extended to honor user-supersede + draft honest-and-thin). Remove: `suggest-remove` → double-confirm → new `/api/remove-species` (removes from plants.json + re-inlines `_DATA` + commits; reversible via git + the add flow).

### Cross-cutting rules baked in
Capture stays deterministic (fence carries routing metadata only; the record is the reader's words) · user notes supersede book/generic · house-voice honesty ("by the book X, but here Y") · pull-not-push · every new affordance instrumented (followup/log/add/remove `_offered`/`_used`).

### ⚠️ Owner: Paul — verification the mocks couldn't do (now that it's live)
1. **Test the four flows on your phone** — confirms Guru actually emits the right fences + the drafter honors user-supersede (the one gap browser-mocks can't close).
2. **First real plant-add: use a disposable plant** — that flow writes canon to live plants.json via GitHub; add a throwaway, confirm it reads honest-and-thin in the house voice, then remove it, before it matters.

### Backlog (panel-surfaced, not yet done)
- Correct `tools/people.json` — mark `d-14nyhnjz` as Mom (currently guessed "Paul's old iPhone"; behavior refutes that).
- Durable photo-in-note (stripped for the iOS localStorage quota; likely path = mirror the audio_ref server-blob pattern) — needs its own scoping.
- Write up the durable principles the panel proposed (ux: "a correct 'no' still owes a next move," "conversational surfaces inherit the universal chat spatial model"; ai-advisor: "the fence is the bridge"; eng: "log the human's words not the model's") into the principle libraries.

---

## Pickup point — last session ended 2026-06-28

**Vehicles card — per-step service contacts (tap-to-call) + GTI cost/scope reconcile.** All committed + pushed (Tate-Tracker HEAD `3b58d3e`).

### New feature — "who to call," right on each restoration step
- New per-vehicle **`serviceContacts`** array on `vehicles.json` + a per-item **`contactId`** (string OR array) on restoration items. `renderRestoContact()` in viewer.html renders a calm, tappable contact (name + `tel:` phone + address · hours) on each shop-bound step so Paul can pull up the step and call to book. The **role line shows only on multi-vendor steps** (e.g. the 3-dealer spare-key step); single-shop steps stay lean. New `.resto-contact*` CSS (forest-green tappable link, field-journal tone, not a CTA button).
- Restoration items can now also carry an **`image`** (tap-to-enlarge thumbnail; `.resto-photo` CSS). Two wired in: **Bolores audio** (`images/vehicles/bolores-audio-ref-infinity-kappa63xf.png` — Infinity Kappa 63XF 6.5" two-way door speakers, logged on the renamed **"Amp, speakers + subwoofers"** item; amp+subs still to source), and the **Tiguan paint** conditions (`tiguan-paint-application-conditions.png` — new **"Paint touch-up"** item, weather-gated: <50% humidity, shade, >50°F brush/>70°F spray).

### GTI — Autobahn wired in + cost/scope catch-up
- **Autobahn Performance** set as the service contact on all shop-bound GTI steps — vetted this session: APR/Dinan/IE-certified indie, 4.9★ (250+ reviews), 2yr/24k warranty, (770) 409-8288, 6476 Buford Hwy NE. (It's where Paul's Stage 1 tune was done.) Spare-key step offers **three VW dealers**: Jim Ellis Chamblee (470) 410-3552 (by Autobahn), Jim Ellis Kennesaw (770) 370-3615, Volkswagen of Marietta (770) 955-6565 (both on the Jasper run).
- **Spark plugs → `done`** (Paul replaced within ~last 1k mi, correct NGK PFR7S8EG, ~81k). **Air & cabin filters → Paul DIY** (off Autobahn; part #s in the detail). **GTI mileage anchored ~81k** (was assuming ~90k) — "past due" softened to "due."
- **Cost estimate** researched + saved to gitignored **`.research/2026-06-28-gti-autobahn-cost-estimate.md`**. Full Autobahn visit **~$1,400–2,600** (up to ~$3,500 if it needs motor mounts / walnut-blast carbon); a dealer runs **~40–60% more** on the must-dos. The **coolant-leak step** carries the expected cost + a **two-wave** phasing plan (teardown-sharing jobs — PCV, chain read, walnut — ride Wave 1 with the water pump; DSG/brake flush/mounts = Wave 2). The **spare-key step** notes the dealer free-inspection verdict (skip the inspection-as-shopping-list; grab the free recall check + a written estimate as a price benchmark).

**Owner: Paul** — the four new outstanding items below (confirm exact mileage, Tiguan paint code, GTI key part #, verify Marietta dealer name). Nothing AI-blocked.

---

## Pickup point — last session ended 2026-06-21

**Creeping fig reframed from "tender seasonal that dies" → overwintering keeper (Mom's field observation), plus a Mom-interview probe-add about direct Claude access.** All committed + pushed (Tate-Tracker HEAD `e22ac0a`).

### Creeping fig — softened + winter tips + observation baked in (`5a985be`)
- Mom observed (spring 2026) the property's creeping fig came through the previous winter **outdoors** and leafed back out. Per the observations-as-knowledge-layer principle (and "Paul's/Mom's direct phenology outranks book hardiness"), reframed the whole `plants.json` entry: guide / currentSeasonNote / frostSensitivity now lead with "it wintered over here," **winter-protection guidance added** (deep mulch 4–6 in over roots+crown before hard cold, frost cloth/sheet/cardboard on the coldest nights, sheltered out-of-wind siting). Cuttings demoted from "the only way to keep it" → optional insurance. The `inspect` "frost-watch" subcategory renamed **"Winter protection"** (months → Oct/Nov), action is protect-and-help-through not watch-it-die. `prune` no longer says "won't be alive outdoors." `indoor-pests` scoped to the optional cuttings backup only.
- `PLANTS_DATA` re-inlined via `wire-photos.py --category plants`; `check-data-inline.py` clean. Release note added (2026-06-21, newest-first) + the 2026-06-20 note's "isn't winter-hardy" claim softened; `build-release-notes.py` re-run.
- **New durable rule (memory `feedback_fernwood_outdoor_by_default`):** Fernwood plants are **outdoor by default** — no indoor plants on the property; only frame a plant around indoor life if it specifically is one. Indoor mentions OK only as an explicit optional backup (cuttings on a windowsill). Scanned all 22 plants — nothing wrongly defaults to indoor.

### Mom — progress-note email corrected + "Garden Guru vs. claude.ai" interview probes added
- **Email (`c70d648`):** the progress-note's creeping-fig bullet now credits Mom's observation ("You were right…"). `.user-research/2026-06-20-mom-progress-note.md`.
- **Interview probe-add (`e22ac0a`)** — Paul raised: should Mom get direct/"unlimited" Claude *via Fernwood*, and what would that enable vs. claude.ai (website) vs. his terminal (Claude Code)? Reframe given to Paul: she **already has** unlimited Claude (claude.ai); the real variable is *where the property-context lives* (capped Garden Guru she leaves for claude.ai vs. a fuller in-Fernwood assistant) and that website-Claude can converse but **can't change the app** (that's terminal-only; Phase F add-species is the one narrow write-path). user-researcher drafted, main session mirrored + exact-match-verified into all three files (guide + moderator prompt + email inlined block): Phase-1 follow-on ("was that the end of it / where did you go?"), a **GATED** Phase-4 block (laptop-story + same-thing-or-two-things perception probe) that only runs if she narrates asking Fernwood questions at all (per telemetry: 5-turn cap has NEVER fired — find out if Guru is even in her repertoire first), a NOT-do "never reveal Guru and laptop-Claude are the same thing" rule, and a new "Garden Guru vs. claude.ai — the boundary she lives" findings header. Email "On the interview" line kept deliberately vague to avoid priming her mental model.
- **⚠️ Owner: Paul (send).** Fresh Gmail draft **`r-6058242175176791653`** (addressed to Paul — swap `To:` → Mom, review, send). Prior draft `r-7367943961009632534` was **deleted by Paul unsent** — nothing to clean up. Held per review-before-send.

**Still awaiting Mom's discovery transcript** (sent 2026-05-29, refreshed 2026-06-20 + 2026-06-21) — now also unblocks the "direct Claude access / where the property-context lives" question; the gated probe finds out first whether Garden Guru is even in her repertoire.

### GTI — spare-key plan added + Marketplace-key verified + consolidated service email (`4a012a6`)
- **New `vehicles.json` restoration item** on `gti-2016`: "Spare key — source + program" (status `sourcing`). Car has ONE working KESSY flip key → cheap "add-a-key" job, not all-keys-lost. Spec: `5K0 837 202 AK` family / FCC `NBG010206T` / 315 MHz US / HU66 / 4-button flip-key-WITH-KESSY. `VEHICLES_DATA` re-inlined. Full strategy in `.research/2026-06-12-gti-vw-service-shops.md` (gitignored).
- **Verified the Facebook Marketplace keys** Paul photographed (`Desktop/Claude/612260695…jpg`): both read `5K0 837 202 AK` / FCC `NBG010206T` (date codes 21/12, 28/13). Correct type + KESSY variant + frequency + blade → hardware very likely compatible. **Decisive catch: they're USED + MK7 is MQB** → key registration needs dealer FAZIT (online) or an MQB-capable locksmith, and a used fob still married to another VIN can refuse to program. Decision rule: only buy if seller confirms virgin/resettable AND a locksmith/dealer will program used MQB keys; else a new aftermarket fob (~$35–80) programs clean. Programming (~$60–150) is the gated cost either way. ⚠️ Paul to verify his own key's part-number/suffix/frequency.
- **Consolidated GTI email** — Paul DELETED the prior GTI-service draft; replaced with ONE brief (Gmail draft **`r-4523879000825113833`**, addressed to Paul): fewest-trips shape + service plan (leak + 90k items) + shop shortlist (FREED/Lewis/Eurofed/Precision + 6 phone-vet Qs) + recalls (16V647 etc., dealer/free, VIN-first) + spare-key verdict + next-actions checklist. Owner: Paul (read/act).

## Pickup point — last session ended 2026-06-20

**Bolores restoration logging, a creeping fig add, and a Mom-interview refresh around "can Mom add a plant herself."** All committed + pushed (Tate-Tracker HEAD `89d7f8c`).

### Bolores — `vehicles.json` → `bronco-1989`
- **Dash bezel → `done`.** The rear-window/defrost switch screw-bosses had cracked; Paul rebuilt them with heat-shrink tubing as a form + JB Weld. Logged as a reusable `techniques` entry ("Screw-boss rebuild"). First `done` restoration item — added a calm `done` chip style in viewer.html.
- **New "Rear window & tailgate operation" item → `testing`.** Motor replaced + wiring patched; window runs when the switch is pressed by hand. Open: verify the switches now that they're seated solid, and tune the tailgate angle (on a slope its weight pulls the glass out of the channel — the strikers are adjustable, needs playing with). Added a `testing` chip style.
- **Driver door panel → `planned`** (repair-in-place, was "source a replacement"). Plan: back-reinforce cracks with heat-formed ABS, flexible-fill + color-match the front, rebuild broken clip pockets. Full guide at **`guides/bolores-door-panel-repair.md`** (materials list + the load-bearing **ABS-vs-PP material check** that decides the adhesives). **Paul's stated next big project.** **(2026-06-20 deepened — panel is now OUT of the truck):** research confirmed it's a molded rigid thermoplastic, almost certainly **ABS** (reproductions are vacuum-formed ABS; still confirm with an acetone test before bonding — if it does nothing it's PP and needs a $56 promoter). Guide now carries **both back-reinforcement methods** (mesh-reinforced weld vs. solid ABS backing patch, with when-to-use) + a **verified, in-stock buy list** (hot-stapler, Polyvance mesh, TAP cut-to-size ABS, Icyhaws clip kit, Blue Truck `DPPRK87` post kit, 3M EZ Sand 35887/05887 — the old 05895 is dead). Shopping-list **email regenerated → Gmail draft `r8257733625489893231`**; ⚠️ Paul to delete the superseded draft `r5682025350058292993`.
- **Paint codes researched** (`vehicles.json` → `paint`, flagged `researched-pending-label`): upper = Medium Cabernet Red **2H / M6156**, lower = Light Chestnut **9T / 6190**; interior Chestnut is a TRIM code, not a paint M-code. ⚠️ **Outstanding (Paul):** photos of the driver-door cert label (EXT PNT + INT TR) to confirm → flip to `verified`. Now item #5 in "Outstanding for Paul".

### Plants — creeping fig added
- `plants.json` + re-inlined `PLANTS_DATA` (`check-data-inline.py` clean, 22 plants). *Ficus pumila*, grown **outdoor/tender** at 2,959 ft (Paul confirmed) — entry leads with the frost story (not winter-hardy in 6b) + an overwinter-via-cuttings calendar. **`photo: null`** (emoji fallback renders fine) — a real photo is a TODO (an AI task; `fetch-photos.py` + re-inline). Release note added (2026-06-20) + card rebuilt.

### Mom — "can Mom add a plant herself?" (the text/conversation path)
- **Three-expert review** (ux-expert, engineering-partner, user-researcher) at `.engineering/2026-06-20-path-text-path-add.md` + `.ux-reviews/2026-06-20-text-path-add-affordance.json`. **Convergent verdict: don't ship yet.** Photo-add is *validated*; text-add is an *assumption* (a Paul-want, no Mom-signal — the star + seeded prompts are the 0-usage precedent). Eng surprise: the promote pipeline is already photo-agnostic; one Worker system-prompt section (`worker.js` ~454–484) gates the "add" fence to photos. If ever built, the right shape is a **funnel back to the photo path** ("snap a photo and I'll add it"), triggered on *unknown-species-identified*, NOT a standing text→canon button. **This is a proposal gated on Mom's transcript — NOT a locked decision** (see `feedback_agent_proposals_not_validated`).
- **Interview refreshed to test it:** split the add-impulse question by path (photo vs words) in both the guide (`.user-research/2026-05-28-mom-discovery-interview-guide.md` — Scenario B follow-up + paired Phase-4 Qs + research Q8 / H7) and the operational moderator prompt (`2026-05-28-mom-moderator-prompt.md`, synced).
- **Progress-note email drafted** — `.user-research/2026-06-20-mom-progress-note.md` + Gmail draft **`r-7367943961009632534`**. Warm "what's new + interview refreshed + do it if/when you want," re-includes the full updated paste-prompt. ⚠️ **Owner: Paul** — adjust, swap `To:` to Mom, send. Held per review-before-send.

### Backlog / direction
- Reviewed the Fernwood backlog. **A comprehensive UI/UX overhaul was considered but is ON HOLD** — the right move is to let Mom's discovery transcript *commission* a targeted, evidence-led UX pass rather than a speculative overhaul (the 0-usage star + seeded prompts are the precedent). Un-gated high-value items: property-map **zone-naming pass** (Paul-input), creeping fig photo (AI), GFC seedling catalog opens **~July 1**.

**Still awaiting Mom's discovery transcript** (sent 2026-05-29, refreshed 2026-06-20) — unblocks the text-add decision, the star / seeded-prompt fates, and Fernwood prioritization.

---

## Pickup point — last session ended 2026-06-13

**DR-Z400S electrical fault — diagnosed end-to-end with Paul wrenching at the property; located, pending splice.**

Real-world field-diagnosis session over chat: the 2001 Suzuki DR-Z400S's "total power loss when steering" fault was traced to a **broken/fatigued conductor in the steering-head harness** (the bundle that flexes when the bars turn). The trail, done with a multimeter (Gardner Bender GMT-312, analog — set to DCV 50): battery good (12.7V) → main fuse good (the live one of the two 20A blade fuses reads 12.7V on both ends; the other is Suzuki's unwired spare) → red feed wire hot (12.7V) at the green 2-pin connector up by the bars → **wiggling the steering-head harness flickers the headlight on/off = a make-and-break in a conductor right at the flex point.** Matches the original symptom; the water that killed the speedo points to the same area.

- **Logged in `vehicles.json` → `drz400s-2001`:** the restoration item "Electrical fault" moved `diagnosing` → `ready`, with the full diagnosis trail + splice/test next steps baked into the detail; the vehicle `status` now reads "fault traced to a broken wire in the steering-head harness (located, pending splice)." Committed `1b79c27`, pushed (rebased over a weather-bot update; live as `3cc5d38`/later).
- **Next steps (in the record):** disconnect battery neg → pinpoint the exact inch (single-wire wiggle → binary-search pinch) → cut back to bright copper + splice with solder + adhesive heat-shrink, leave slack, route clear of the turn-stops → clean the green connector pins → test (continuity → key-on headlight → lock-to-lock → horn/brake). Once power's solid, the **speedo rebuild** (still `planned`) moves back to the top.
- **Status:** owner is Paul (physical splice at the property). When he confirms it runs clean through full steering, flip the electrical item to resolved and bump the speedo.

---

## Pickup point — last session ended 2026-06-12

**Vehicle & Equipment card — major enrichment pass + a privacy hardening.**

- **New `restoration` "what she needs" running-list** per vehicle (`vehicles.json` → ordered array of `{item, status, detail}`, rendered as a collapsible panel with status chips: sourcing / diagnosing / ready / due-soon / planned / quoting / down-the-road / long-term — ordered most-critical → farthest out; field-journal tone, no alert language). Built for **Bronco "Bolores"** (10 items — door panel/lock/bezel, fluids, clear coat, seat, headliner, soundproofing, amp+subs gated on the door panels), **GTI** (8-item 90k shop list; coolant leak = known EA888 Gen3 water-pump/thermostat), **DR200S** (recommission + first oil + bent handlebars→replace), **DR-Z400S** (recommission + electrical-fault diagnosis + speedo rebuild), **golf cart**.
- **Golf cart corrected electric→gas** — `g22a-2005` was modeled as 48V electric; it's the gas G22A (357cc OHV, 11.4 hp = 8.5 kW misread as a motor rating). Verified specs: NGK BPR4ES, air filter JN6-E4450-00, no spin-on oil filter (internal screen), 10W-30 ~1.16 qt.
- **VINs added** to Tiguan/GTI/F-150/Bronco (decodes confirmed the F-150 4.2 Essex V6 + Bronco 5.8 351W).
- **PII hardening — the repo is PUBLIC (GH Pages):** VINs masked to the decodable head on the cards (last-6 production serial hidden); license tags + State Farm policy #s live only in gitignored `.private/vehicle-records.md`; **full VINs purged from ALL git history** via `git filter-repo` + force-push (verified 0 remaining; backup bundle deleted). Never put full VINs/plates/policy#s in vehicles.json/viewer.html again.
- **Weather bot demystified:** the `weather-recorder[bot]` commits are a scheduled GitHub Action (`.github/workflows/record-weather.yml`), **NOT drift**. Operating ritual (`git pull --rebase` first) + a safe history-rewrite runbook are documented in `tools/SCHEDULING.md`.

**Parked:** fleet profile-review enhancement — add per-vehicle **mileage/hours + last-service anchors** (needs Paul's odometer/service readings; everything else turned out well-specced). Also: confirm the cart's actual spark plug / air-filter P/N against the parts when next up at the property.

**GTI service — vetted shop plan ready** (`.research/2026-06-12-gti-vw-service-shops.md`, local working notes). For the 90k + coolant leak: **FREED Performance (Cumming)** = top tune-friendly pick on the Jasper corridor; **Lewis Motorwerks / Eurofed (Decatur)** intown; **Precision (Canton)** closest to property; **Jim Ellis VW Kennesaw** for the free recall check (16V647 EVAP likely applies). Paul's next: run the VIN at nhtsa.gov/recalls + phone-vet the top 2 + book.

**Still awaiting Mom's transcript** from the 2026-05-28 discovery interview (below) — unchanged; comes back when she has a quiet half hour.

---

## Pickup point — last session ended 2026-05-28

**Three work streams landed:**

### 1. Phone zone sync bug — fully closed

Diagnosed and shipped end-to-end. Phone had no live cloud read path for zones; it relied entirely on inlined `ZONES_DATA` (deploy-tail stale) + localStorage (wholesale-shadowing). Three commits:

- `61c1001` — minimal fix: `refreshZonesFromCloud()` in viewer.html fetches `zones.json` from GH Pages on boot with cache-bust; reconciles against localStorage's unsynced-edits buffer.
- `92c882e` — path-eval §2 + §3: Worker writes `zones:all` KV on save; new `GET /api/zones` (KV-direct read with git fallback, stamps per-device lastSeen); new `GET /api/zones-sync-status` (canon + devices). Client prefers KV-via-Worker; falls back to GH Pages. Chip gets new `live` state — polls `/api/zones-sync-status` after save, flips to "live everywhere" when canon + all known devices match. Audience-mode toggle in Sync settings (quiet for Mom-default; verbose for Paul-style diagnostic visibility).
- Worker deployed twice (versions `c2800508` then `c87827d5`).

**iOS Safari PWA cache note:** Paul had to kill Safari once per viewer.html push to bust the app-shell cache. The cloud-read fix solved the *data* freshness problem; *viewer.html itself* still rides the iOS HTTP cache. Different bug — not in scope.

Path-eval doc lives at `review/2026-05-27-path-cross-device-sync-architecture.md`. Phone zone sync bug memory deleted from auto-memory (resolved).

### 2. Sources card editorial pass — F4 patches

`7e95d3a` shipped four marketing-adjective slip patches in `research-resources.md` (rebuilt `references.json`). Per content-steward review at `review/2026-05-21-reference-card-voice.md` — the F4 finding ("anchor the first sentence, strip ad-copy register"). Patches: Warnell Outreach, Lady Bird Wildflower Center, NASA SVS Moon, ATTRA Sustainable Agriculture. Four borderline cases left as-is (anchor was doing legitimate work despite superlative form).

### 3. Mom discovery interview package — drafted, Gmail draft queued

Reframe Paul locked: this is honest *discovery* (how is the app useful today, how to prioritize next), NOT validation. Paul's model of Mom-as-user has been built from his side of the conversation; the interview surfaces hers.

Four artifacts at `.user-research/2026-05-28-*`: `mom-discovery-interview-guide.md` (research design), `mom-moderator-prompt.md` (Claude voice-mode system prompt), `mom-email-draft.md` (Mom-facing wrapper with prompt inlined), `reading-the-output.md` (synthesis playbook for after transcript returns). Two edits applied post-draft: cut Scenario D (Job 10 was Paul-want, leading the witness); softened meta-feedback closing question from research-jargon to plain language.

**SENT to Mom 2026-05-29.** The package was regenerated before sending (commit `e359d06`): added (1) a Phase 1 Garden Guru story-probe ("tell me about a time you asked Fernwood a question… what did you do after it answered") to surface the 2-turn-ceiling signal; (2) **Scenario D** — a guided "find + react to The Fairway card" task (Paul's call to get Mom's live first-reaction to the new turf/meadow section, accepting the lighter discovery value); (3) a dedicated "Reaction to the new Fairway section" findings header. A fresh Gmail draft (`r153055942713180127`) was created from the regenerated version (MCP can't edit an existing draft); the stale 2026-05-28 draft `19e6ed935970d98c` is Paul's to delete.

**Now awaiting Mom's transcript** (self-serve, no deadline — comes back when she has a quiet half hour). When it lands, run it through `reading-the-output.md`. This unblocks the downstream Phase E / Path E gate decisions: the star-affordance call (meta-feedback Q + zero-usage telemetry), Fernwood prioritization (which unserved jobs are real; is the 2-turn Guru pattern a ceiling), and the first read on whether The Fairway lands. See [[project_fernwood_mom_interview_format]].

---

## Prior pickup — last session ended 2026-05-26 (afternoon + evening)

**Two work streams landed:**

### 1. Storage-quota incident + fix (afternoon)

Mom hit `Could not save the entry — local storage may be full or blocked` in the field; Paul reproduced same-day. Two commits on `main`:

- `c040862` — strip base64 from local conversation saves, graceful quota failure, Rebuild local from cloud affordance in Sync settings, Worker `persistConversation` strips blobs from `conversation:<id>` KV
- `c7e2781` — defensive `sanitizeEntryForStorage` at `fnSaveAll` boundary (idempotent, catches legacy fat data from any source), new `POST /api/admin/clean-observations` worker endpoint (auth-gated, idempotent)

**Worker status:** Version `77b520bc-31dd-4e75-a0b4-17a578b0c07e` deployed. `/health` confirms KV + Anthropic + GitHub configured.

**One-time KV cleanup ran 2026-05-26.** Hit `/api/admin/clean-observations` with the SHARED_TOKEN: 15 observations total, 4 fat (photo conversations), `observations:all` shrank 4,109,859 bytes → 13,027 bytes (4 MB saved). Idempotent re-run confirmed.

**Confirmed working on Paul's iPhone same-day.** Mom's unblock path when Paul next sees her phone: Sync settings → Rebuild local from cloud. The cloud copy is now 13 KB so the local write fits comfortably.

**Storage shape now in production** (see [[fernwood-almanac-save-model]] storage-shape section):
- localStorage (`tateTracker.observations.v1`) — text-only conversation snapshots + per-turn `hasPhoto`/`hasAudio` flags
- Worker `conversation:<id>` KV — lean (placeholders for image/audio blocks)
- Worker `observations:all` KV — lean
- Rich content's only homes: in-memory `GardenGuru.turns` during a session, and Phase F-promoted Git canon (the species' photo file in the repo + inlined `IMAGE_DATA`)

**The defensive principle Paul should keep applying:** sanitize at the storage boundary (lowest write helper), not only at the source. The first fix stripped only at `saveCurrentConversation`; the boundary-level `sanitizeEntryForStorage` at `fnSaveAll` is the bulletproof layer that catches sync-refresh, rebuild, and any future writer. See [[feedback_sanitize_at_storage_boundary]].

**Token-rotation thought (optional):** Paul pasted the SHARED_TOKEN into chat to run the cleanup. Low-risk to leave (token only authenticates to personal Fernwood Worker; worst case is Anthropic bill / journal tampering), but if cleaning up: pick new random value, `wrangler secret put SHARED_TOKEN` from `worker/`, re-paste into Sync settings on each device.

### 2. "Worth Considering" candidates card (evening)

Activated the long-dormant plants-to-consider thread. Discovery → schema → build, all in one session per Paul's "go ahead and implement" call.

**Decisions locked (4-question interview):**
- Win-state: operational + reference (start with 3-5 plantable fall 2026 / spring 2027, structured to grow into the durable reference)
- Surface: dashboard "Worth considering" card (heaviest option from the menu) with structured JSON
- Sourcing depth: programs + named nurseries + freshness tags (last-verified per entry)
- Approach: discovery pass first → schema + build in same session (sessions 2+3 collapsed)

**Discovery doc:** `.research/2026-05-26-plants-to-consider-discovery.md` (gitignored — working notes, not production). Surfaced the four-tier landscape (rationale × property-fit × sourcing × certification), the GNPS Blue Ridge Communities matrix as the property-fit canonical reference (corrected my earlier "Mesic Cove + Montane Oak" mental model — at 2,959 ft the property is **Cove Forest + Low-to-Mid Elevation Oak Forest** with potential **Seepage Wetlands** in the spring drainage; Montane Oak Forest is typically above 3,500 ft), and the 5-question Paul-interview that locked scope.

**Built and shipped on `main`:**
- `candidates.json` — 10 candidates across 6 categories (restoration, keystone, rich-cove, cultivar-trial, bird-pollinator, native-grass). Schema mirrors plants.json fields enough that promotion ("considering" → "planted") is clean.
- `sources.json` — 7 programs + 6 nurseries with `lastVerified` freshness fields. Freshness convention: < 6 mo green, 6-12 mo amber, > 12 mo faded.
- `viewer.html` — new "Worth considering" card between Vehicles and Sources. CSS uses Crimson serif for plant names (matches reference card pattern), light-green community-fit chips, source rows with freshness dots, amber "next event" callout for time-sensitive sales. Mom-no-glasses readable (19px plant names, generous line height). Tap-to-expand entry rows.
- `plants-to-consider.md` — updated to point at the discovery doc + refreshed next-steps.
- Init wiring: `renderCandidates()` called alongside `renderReferences()` at page init.

**First batch — 10 candidates:**
- **Restoration:** American chestnut, Eastern hemlock
- **Keystone:** White oak
- **Rich-cove:** Pink lady's slipper
- **Mt. Cuba cultivar trial:** Smooth (wild) hydrangea ('Haas' Halo' is the trial winner)
- **Birds + pollinators:** Flame azalea, Cardinal flower, Christmas fern, Common witchhazel
- **Native grasses:** Autumn bentgrass (*Agrostis perennans*) — **flagged as Mom's pick**

**Mom's pick:** Autumn bentgrass came from Mom; renders with a purple "Mom's pick" badge. The species is property-appropriate (native perennial bunchgrass, partial shade, mesic to wet soils — fits the spring drainage seepage zone). iNaturalist + Native Plant Trust + Lady Bird Johnson Wildflower Center all confirm the habitat match.

**Imminent flag:** **GNPS North GA Mountains chapter native plant sale — Saturday May 30, 2026, 8am-1pm, Union County Farmers Market, Blairsville, ~45 min from Fernwood.** Cash/check only. Captured in `sources.json` as the `gnps-ngm-sale` program with the May 30 date in the `next` field; the card renders this as an amber-bordered callout under each candidate that references it (flame azalea, cardinal flower, witch hazel, etc.). Most ecologically-aligned single sourcing event of the year.

**Known gaps to chase later:**
- UGA SBG/GNPI 2025 nursery list PDF is 404 at source — fell back to 2019 list for 4 nurseries (Native Forest Nursery, Baker Environmental, Rock Spring Restorations are marked "2019 SBG/GNPI list — needs 2026 confirmation"). Contact `jceska@uga.edu` for current URL.
- TACF GA chapter — confirm current landowner participation pathway.
- HRI — current resistant-hemlock-stock sourcing path.
- GFC 2026-2027 seedling species catalog (publishes ~July 1).
- Mt. Cuba current top picks for genera beyond hydrangea (monarda, baptisia, echinacea, coreopsis) — would extend the cultivar-trial category.

**What Paul should do next session:**

1. **Check Mom's phone** the next time he sees her: Sync settings → Rebuild local from cloud. Confirm her Garden Guru conversations come back from KV.
2. **Walk through the new "Worth considering" card** with Mom in mind — anything missing, anything off-tone, candidates to add or drop. Mom's bent grass pick is in there.
3. **Zone-naming pass** for the map view (still paused). The candidates card has no `zoneAffinity` yet — once zones lock, populate per candidate so Phase E can answer "what could I plant near the pond?"
4. ~~**Phase F Option C smoke test**~~ ✓ **Closed 2026-05-26.** Validated by real-usage history (4 image-bearing conversations in KV between 5/21–5/22). Two species correctly auto-promoted with the 3-commit pattern (Pop Star Hydrangea 5/21 14:45 EDT — b98f83c/3cb59e9/5f13bed; Spiderwort 5/22 16:39 EDT — 1e9d8fc/f9a0f84/babcf34). Two correctly skipped because already canonical (Butterfly Weed already in plants.json from 5/16; Black Bear already in mammals.json). The suggested-species dedup fence is doing its job — the safer of the two failure modes is validated. Step A "Not quite" branch + Step B "Skip this one" branch still untested; not blocking. Revisit if `analyze-fernwood.py` rollup or hard-fail log (`.engineering/garden-guru-hard-fails.md`) surfaces a regression. Note: f291ae8 (5/21 17:42 "Phase F prompt fix: visual-feature consistency check vs Haiku force-fit") landed 12 min after the Butterfly Weed conversation — that's an early iteration trigger worth logging if remembered.
5. **Garden Guru E2E smoke test — partially validated** (queued from Phase E ship 2026-05-19). Of the 5 originally-scoped dimensions, 3 are covered by real usage in the saved KV conversations (in-context retrieval ✓ multiple examples; honest-uncertainty register ✓ poison-ivy conversation 5/20; property-anchored advice ✓ rhododendron/laurel fertilizing 5/22). **Still open:** (a) 5-turn cap — all saved conversations are 2-turn; cap message has never fired in real use; (b) reset flow — never deliberately exercised; (c) vague-description handling — the brown-bird-at-feeder conversation 5/20 showed Guru *guess with hedges* rather than *ask clarifying questions*; rubric language says ask, observed behavior says guess — Paul judgment call on whether to accept the drift or iterate the system prompt.
6. ~~**Telemetry rollup**~~ ✓ **v1 run 2026-05-26 (manual rollup via wrangler, no `FERNWOOD_TOKEN` setup).** Report at `.audit/2026-05-26-telemetry-rollup.md`. **Six headline findings:** (a) Adoption is real — two unmapped iPhones actively using daily, most-active has 27 sessions / 341 events in 6 days; (b) Strong evidence the most-active unmapped iPhone (`d-14nyhnjz`) is **Mom** — it's the only device that used the A/A+ text-size toggle Paul shipped 5/22 (12 events); (c) Phase F Option C confirmed doing real work — 4 image conversations, 2 species_promoted, matches git log (Pop Star + Spiderwort); (d) Cost ~$0.86 over 6 days = ~$5/mo — comfortably below the $2/mo Phase F bench estimate; (e) **Star affordance has zero usage** across 6 days / 104 entry_revisits — Paul-judgment moment: reposition, kill, or accept that revisit-frequency IS the implicit "this matters" signal; (f) `conversation_capped: 0` — all 10 conversations are 2-turn, cap mechanism is shipped without need. **Open follow-ups from the rollup:** confirm Mom-is-`d-14nyhnjz` next time Paul sees her phone + update `tools/people.json`; decide star/seeded-prompts fate; investigate why mapped Paul iPhone went silent after 5/21; iOS `session_end` reliability (27 starts vs 1 end on the likely-Mom device).

---

## Prior pickup — last session ended 2026-05-21 (evening)

**Phase F shipped end-to-end and pushed.** All four Phase F commits + Option C extension live on `main`:
- `fb417fd` Session 1 — Worker (image content support + suggested-species fence + pending-species queue)
- `0b58aba` Session 2 — Client UI (single button "Add to the journal", 📷 image attach, canvas downsample, content-routed submit, suggestion chips)
- `bfea0d2` Session 3 — `tools/review-pending-species.py` CLI gatekeeper
- `bab7cf7` Option C — two-step confirm + auto-promote to Git canon

**Status:** Worker deployed at version `75bffec5-19f5-4ba5-8c1e-c8d8196da84b`; `/health` shows `configured.github: true` (Paul set the three GitHub secrets — `GITHUB_TOKEN`, `GITHUB_REPO`, `GITHUB_BRANCH`); 7 commits pushed to `origin/main`; GH Pages deploys ~1–3 min later. Mom now has the full photo → ID → two-step confirm → auto-promote loop on her phone.

**Architecture pivot (2026-05-21 evening):** Phase F was built first as Option A (Mom suggests → Paul reviews via CLI → Paul promotes manually). Mid-session Paul pivoted to Option C: Mom has full promotion rights; two-step confirm gates the cost (drafter + GitHub commits only after both Yeses); direct-to-Git writes (Worker commits the AI-drafted full v3 schema entry + viewer.html re-inline + photo file via GitHub Contents API). The Option A pending-species queue + CLI tool remain as the **fallback path** when GitHub commits fail. This explicitly softens `feedback_tate_tracker_depth_filter` — the canon now grows from "what Paul observes" to "what someone at the property has photographed *and* confirmed twice." Trade-off accepted; the SCHEMA_DRAFTER prompt nudges toward elevation-aware drafting; flagged for iteration if quality is poor.

**What Paul should do next session:**

1. **Phase F Option C smoke test** (load-bearing — gates everything else). Hard-refresh `palekxk.github.io/Tate-Tracker/` (wait ~1–3 min after the push). Tap 📷, pick a photo of a plant or animal that's NOT in the curated 17/etc., walk through Step A + Step B, watch the auto-promote (drafter call + 3 commits to `PAlekxK/Tate-Tracker`) + the live timer count up. Verify:
   - Garden Guru reply is in field-journal voice; ends with the ID + plausibility (NOT with "want to add?")
   - Step A chip: "Does that look right?" (Yes / Not quite)
   - Step B chip after Yes: "Worth adding to the Almanac?" (Yes, add it / Skip this one)
   - "Drafting the entry…" → ~3–7 sec → "[Name] added. Elapsed: 0:14" with live timer
   - GH commits appear in `https://github.com/PAlekxK/Tate-Tracker/commits/main` — three per promotion (JSON, viewer.html, photo)
   - After 1–3 min, refresh dashboard → new entry visible in the right tab
2. **Watch for AI-drafted schema quality issues.** The SCHEMA_DRAFTER prompt is load-bearing for canon quality. If the drafted entries have regional rather than 2,959-ft-specific phenology, iterate the prompt at `worker/worker.js` `SCHEMA_DRAFTER_SYSTEM` and redeploy. Cost per promotion: ~$0.04 (vision call + drafter call).
3. **Garden Guru E2E smoke test still open** (queued from Phase E ship 2026-05-19). 5 representative questions covering in-context retrieval, honest-uncertainty register, vague descriptions, 5-turn cap + reset flow.
4. **Check telemetry after a couple weeks.** `cost-log:YYYY-MM-DD` accumulates per-call spend; `pending-species:YYYY-MM-DD` only fills on Option-A fallback. Run `analyze-fernwood.py` for the rollup; `review-pending-species.py --list` for the (hopefully empty) fallback queue.

**Where the Phase F design trail lives:**
- `.engineering/2026-05-21-path-phase-f-image-input.md` — engineering-partner path-eval that locked Option A's shape
- `review/2026-05-21-phase-f-input-copy.md` — content-steward voice/copy memo (button label, helper text)
- `~/Documents/Claude/handoff/master-plan-2026-05-21.md` W2.5 section — P1–P8 (Option A) + C1–C3 (Option C) decisions
- `[[master-plan-2026-05-21]]` — master plan memory pointer

**Where the Phase E design trail lives** (still active for any next-session expert review):
- `PHASE_E_BRIEF.md` — full feature brief (the input to the 5-expert review)
- `PHASE_E_SYNTHESIS.md` — synthesized findings from the 5 experts
- `PHASE_E_MVP.md` — locked decisions + implementation spec
- `PHASE_E_DESIGN.md` — original 9 design questions (Q1 + others resolved through walkthrough)
- `.ux-reviews/2026-05-19-phase-e-unified-field-assistant.json`
- `.engineering/2026-05-19-path-phase-e-architecture.md`
- `.user-research/jtbd-talk-to-the-property.md` + `journey-unified-field-assistant.md`

**Open Phase E iterations (still not yet done):**
- **Conversation browse UI.** KV has all conversations; no UI to browse them yet. v2.
- **Streaming responses.** Non-streaming v1; add streaming (~30 lines client) if turns feel laggy on LTE.
- **Tool-use migration.** System-prompt stuffing of the ~57K-token digest is fine until digest >80K OR Phase G observations >50 entries.

**Phase H — Audio identification (TABLED 2026-05-21 evening):** Built end-to-end then tabled the same day pending a free / single-vendor audio-ID path. Full decision trail at `.engineering/2026-05-21-phase-h-tabled.md`. TL;DR:

- **What got built:** Worker `/api/audio-upload` endpoint, audio_ref dereferencing in `handleChat`, OpenAI gpt-4o-audio integration (`identifyAudioViaOpenAI` + `SOUND_ID_OPENAI_SYSTEM`), audio commit in `handlePromoteSpecies`, `GARDEN_GURU_SYSTEM` extension for audio-ID-result context, client-side `createAudioCapture` + `UnifiedAudio` + `GardenGuru.askWithAudio`, 👂 Listen button in the unified-input icon row.
- **What's hidden:** The 👂 button is `hidden` in HTML (`viewer.html:3054`). Mom sees Voice + Photo only. All underlying code preserved.
- **Why tabled:** (1) Anthropic doesn't support audio yet; (2) OpenAI works but adds vendor diversification overhead for a feature Mom hasn't yet asked for; (3) free paths exist (BirdNET self-host, Hugging Face Inference API, Cornell's iOS browser-TFJS when shipped) but none mature/zero-effort today; (4) `feedback_defer_affordances_pending_signal` says wait for actual Mom-usage signal from Phase F before speculative-building Phase H.
- **How to re-enable:** Remove the `hidden` attribute on `#ui-audio-btn` in viewer.html. Set `OPENAI_API_KEY` Worker secret (if staying with OpenAI) OR rewrite `identifyAudioViaOpenAI` for whichever audio-ID backend you pick. Verify `/health` shows `configured.openai: true` (or the new vendor's flag).
- **Watch for:** BirdNET-Live iOS support (Cornell), Anthropic audio Messages API (SDK #1198), Hugging Face inference quality for bird ID (~30 min landscape pass when revisited).

**Other open threads on the backlog** (from the punch list earlier this session):
- Citizen-science decision — dormant scaffolding in viewer.html; re-enable, drop, or leave dormant is Paul's call
- Property map view — paused; imagery + 7 zones + prototype committed; pickup whenever
- Phase G observations as knowledge layer — defer until Phase E proves itself + observation set is rich (>50 entries)
- Phase F image input — benched 2026-05-20 then **un-bench recommended 2026-05-20** by ai-advisor (Q4: Mom is already a Claude+photos power-user; without Phase F, Garden Guru is structurally weaker than her existing tool). Strategic recommendation: sequence Phase F next-after-metrics-capture-baseline. Cost analysis: ~$2/mo at expected usage; Claude Vision is the right primitive with hybrid posture (Claude-primary + honest uncertainty + optional specialist link-out). engineering-partner Phase F implementation path-eval still queued.
- Mt. Cuba reference / native-cultivar trials — captured in `plants-to-consider.md`; revisit when planning new plantings
- ~~**Reference / Further Reading card**~~ ✓ **v1 shipped 2026-05-21.** New "Sources" card at the bottom of the card stack (after Vehicles). Title: **"Sources"**; no subtitle (Paul's call, overrode content-steward's "The Library" + "What we read to learn this place" recommendation toward the utilitarian end of the spectrum). Stacked accordions, one per category, all collapsed by default; per-entry = title link + Crimson-italic framing line (Paul's existing "Why it's relevant here" prose). Two-layer source-of-truth: `research-resources.md` stays the long-form research notebook (working voice, includes "Dashboard integration idea" + "Depth tier" lines, prefatory Top finds + Quick reference tables); `references.json` at repo root is the published shape (curated label rewrites, dashboard-idea + depth-tier lines hidden, prefatory sections skipped). `tools/build-references.py` regenerates `references.json` from the markdown — re-run when the notebook gains entries. Inlined into `viewer.html` as `REFERENCES_DATA` const per the existing pattern. Reviews: `review/2026-05-21-reference-card-voice.md` (content-steward) + `.ux-reviews/2026-05-21-reference-card.json` (ux-expert). **Open editorial follow-up:** ~5-10 entries have marketing-adjective slips in the first sentence of "Why it's relevant" (e.g., DarkSky "exceptional for the Eastern US"); content-steward flagged these as needing a light pass against the anchor-the-first-sentence pattern. Not blocking — defer until Paul reads through the card and confirms the sample.
- ~~**Metrics capture (added 2026-05-20)**~~ ✓ **v1 shipped 2026-05-20.** Path C from `.engineering/2026-05-20-path-metrics-capture.md`: client `MetricsCollector` IIFE buffers events to `tateTracker.metrics.v1` localStorage; flushes via Worker `POST /api/metrics` (with auth fail-soft); KV daily key `metrics:YYYY-MM-DD` mirrors the existing `cost-log:YYYY-MM-DD` shape. **15+ events instrumented** (audited 2026-05-20 evening): session_start/end, input_focused, input_abandoned, card_expanded, subtab_switched, card_section_viewed, filter_changed, field_note_saved, **entry_starred / entry_unstarred / entry_revisited** (curation), conversation_started/turn/capped, conversation_reply_dwell, seeded_prompt_used. The curation events specifically answer the "does anyone come back to a saved entry?" question without new instrumentation — relevant to the meta-feedback channel validation gate (see [[project_fernwood_almanac_save_model]]). Privacy: structural events only; no field-note bodies or conversation content. **Stable per-device ID** (`tateTracker.deviceId` in localStorage, survives UA churn) enables clean per-device clustering; deviceId→person lookup table is the manual step still needed before per-user (Paul vs Mom) analysis. Device-class auto-detection (mobile/tablet/desktop) via UA. Self-exclusion via `tateTracker.metricsExclude="1"`. Analysis tool `tools/analyze-metrics.py` is queued (the data accumulates in KV either way).
- **Dormant `/api/feedback` endpoint (noted 2026-05-20 evening)** — `worker/worker.js` has a fully-built POST/GET `/api/feedback` handler: sentiment-tagged (`landed | so_so | missed`), context-tagged (default `{type: "general"}`), with `note` text up to 2000 chars, deviceId-aware, sessionId-aware. KV key `feedback:YYYY-MM-DD` mirrors the cost-log/metrics shape. **The viewer is not wired to call it** — no client code POSTs to this endpoint. Dormant infra sitting available. Relevant if the 🚩 "flag for Paul" affordance ever gets promoted from Path E to Path C (see [[project_fernwood_almanac_save_model]] → Meta-feedback channel section): the feedback record shape is a cleaner data model than adding a `flaggedForPaul` boolean to entry objects. Decision when promoting: extend `/api/feedback` or add boolean to entries — engineering-partner's original recommendation assumed boolean-on-entry; the dormant endpoint changes the trade-off.
- ~~**Analysis + reporting tool (added 2026-05-20)**~~ ✓ **v1 shipped 2026-05-21.** Path-eval at `.engineering/2026-05-21-path-analyze-fernwood.md`. Implementation:
  - **Worker** (`worker/worker.js`): two new GET endpoints — `/api/cost-log?start=&end=` (mirrors metrics GET shape) and `/api/conversations?start=&end=` (KV `list({prefix: "conversation:"})` + filter by startedAt/updatedAt in range, returns metadata only — id, startedAt, updatedAt, turnCount; no turn content). Router + `/health` endpoint list + top-of-file docstring all updated. **Deploy required: `cd worker && npx wrangler deploy`.**
  - **Python script** (`tools/analyze-fernwood.py`): one script, six report sections (Adoption + Garden Guru engagement marked load-bearing for T+30 Mom interview; Cost, Usage, Almanac activity, Per-device summary as nice-to-have). Stdlib only — no `pip install`. Takes `--start --end --exclude-device --out`. Env vars `FERNWOOD_TOKEN`, `FERNWOOD_WORKER_URL`. 90-day client-side cap. Idempotent. Includes Haiku 4.5 pricing constants for dollar estimates (footnoted with `PRICING_VERSION = "Jan-2026 Haiku 4.5"` so the script reads honestly when pricing drifts).
  - **Optional per-person attribution:** if `tools/people.json` exists with shape `{ "people": [{ "name": "...", "deviceIds": [...] }] }`, the device table shows person names. v1 doesn't ship a `people.json`; the manual deviceId→person mapping is a follow-up Paul does when he has the device IDs in hand from the first real report.
  - **Followups still open:** (1) deploy the Worker; (2) populate `tools/people.json` after first report run; (3) consider auto-derived per-person rollups in v2 once `people.json` exists.
- ~~**Unified-input UX redesign (Q10, added 2026-05-20)**~~ ✓ **Shipped 2026-05-20 evening, live for all users.** Same-day arc: locked the design after live E2E test → implemented behind feature flag → flag removed per Paul's "let's have everyone on the same version" call. Path-evals: `Tate-Tracker/.ux-reviews/2026-05-20-unified-input-redesign.json` (ux-expert) + `Tate-Tracker/.engineering/2026-05-20-path-unified-input.md` (engineering-partner). See [[project_fernwood_almanac_save_model]] for the architecture decision. **What shipped:** single textbox + two action buttons ("Save" no-AI quick-log / "Ask Garden Guru" AI conversation); auto-save everything to almanac on action; per-entry "this matters" star/pin affordance; star filter on the almanac view; 3 seeded in-voice prompts in collapsed-empty state; conversation auto-save on reset/cap/session-end. **Trade-off Paul accepted:** no metrics pre-change baseline (instrumentation shipped same-day; pre-change window is minutes, not days). ~~**Open naming question**~~ ✓ **Resolved 2026-05-21.** Card title `Field Notes` → **`The Almanac`**; subtitle `The journal you keep about this place` → **`Notes on the estate`** (Paul's call after content-steward review at `review/2026-05-21-saved-entries-naming.md`). Intro line "The journal generates the almanac" kept verbatim (load-bearing under the new title — teaches the voice/form dual-frame). ~~Legacy `#quick-capture` + `#garden-guru` cleanup pass~~ ✓ **Completed 2026-05-21.** Removed: both DOM sections, all `.quick-capture-*` / `.garden-guru` / `.gg-*` / `.fn-capture-*` / `.fn-mic-hint` CSS, `VoiceCapture` + `GuruVoice` instances, `createVoiceCapture` factory (~110 lines — git history preserves for reuse), `renderGardenGuru` + `wireGardenGuru`, the capture/mic block of `wireFieldNotes` (sync-modal wiring kept). Refactored `fnSaveInlineEntry()` to accept text as a parameter (no longer reads from the now-deleted legacy textarea). File shrank from ~9810 → 9241 lines. ~~**New open thread:** `#ui-mic-btn` on the unified-input surface is rendered but never wired to a voice handler~~ ✓ **Resolved 2026-05-21.** Restored `createVoiceCapture` factory; instantiated `UnifiedVoice` against `ui-textarea` / `ui-mic-btn` / `ui-mic-hint`; wired the mic button in `UnifiedInput.wireUI()` (toggle on click + hide + show fallback hint when SpeechRecognition unsupported). `fnSaveInlineEntry()` extended to accept `{ inputMode }` so the voice-vs-text metrics signal works again — saveBtn detects `UnifiedVoice.isRecording()` and passes the mode through, then stops capture; askBtn stops capture if active before delegating to `GardenGuru.ask`. Added `.ui-mic-hint.error` CSS rule to colorize error states (parity with the old `.fn-mic-hint.error`). Voice on unified-input has been silently broken since the 2026-05-20 redesign; this restores it.

## Project purpose & tone

Fernwood is a **personal property reference dashboard** for 282 Church Mountain Road, Jasper, GA 30143 — a rural mountain property at 2,959 ft elevation in the Blue Ridge, within Tate Mountain Estates. "Fernwood" is the property's name; "Tate Mountain Estates" is the surrounding 1920s mountain development, separate from the nearby town of Tate. It is hyper-personalized, not a generic app.

**Project rename history:** Originally "Tate Tracker" (named for Col. Sam Tate / Tate Mountain Estates); renamed to "Fernwood" on 2026-05-19 to name the actual property rather than the surrounding development. Repo path, GitHub repo, Worker URL, localStorage keys, and most internal var names retain `tate-tracker` / `tateTracker` for now — those are infrastructure-level identifiers, not user-facing, and renaming them carries data-migration risk (existing observations). Rename them only if a clear reason emerges.

**Tone is everything here.** This is a fun, evocative reference tool — a field journal, not a task manager. Language like "17 actions due" or "3 alerts" is wrong for this project. Prefer "What's happening in May" or "Worth checking this month." The dashboard should feel like looking out at the land, not a to-do list with deadlines.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd /Users/paulkirschenbauer/Documents/Claude/Projects/Tate-Tracker
python3 -m http.server 8765
# then open http://localhost:8765/viewer.html
```

## Release notes — update every release

**Every user-facing change ships with a release note.** When a release lands something Mom or Paul would notice on the dashboard (a new card, a new affordance, a visible behavior change), add a `## YYYY-MM-DD — Title` entry to `RELEASE_NOTES.md` (newest stays at top, field-journal voice, bullets describe what changed *for the user* — not the engineering), then run `python3 tools/build-release-notes.py` to re-inline `RELEASE_NOTES_DATA` (latest 5) into viewer.html. The "Recent updates" card renders it. Purely behind-the-scenes work (refactors, data plumbing) doesn't need an entry. If a release shipped without a note, backfill it.

## Architecture

`viewer.html` is a single ~4,600-line self-contained file: all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework. The JSON files (`plants.json`, `fishing.json`, etc.) are the source of truth for data — they are fetched at page load and the inlined copies in `viewer.html` serve as fallback. When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 17 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
- `FISHING_DATA` — Lake Sequoyah species profiles, scoring weights, seasonal notes.
- `BIRDS_DATA` / `AMPHIBIANS_DATA` — Species with `monthsPresent`/`monthsActive`, status (resident/summer/winter/migrant).
- `VEHICLES_DATA` — Fleet registry with status badges.
- `PROPERTY_DATA` — Microclimate, soil series, watershed, elevation notes.

Live data is fetched async at init from three sources: the **on-site Ambient Weather station** (MAC `D8:F1:5B:15:28:B8`, via `api.ambientweather.net`) for current on-property conditions; **Open-Meteo** (`api.open-meteo.com` forecast + `archive-api…` ERA5) for the forecast and the historical grid baseline; and **RainViewer** for radar. The logged daily record (`weather-history.json`, maintained by the `record-weather.yml` GitHub Action + `tools/record-daily-rollup.mjs`) is 100% the on-site station. NOTE: the old Weather Underground PWS `KGAJASPE279` is **no longer used** — only a Wundermap deep-link remains. Don't reintroduce it as a data source.

### CSS conventions

Color utilities are defined per care type and reused throughout:

```css
.c-{type}   /* colored text */
.b-{type}   /* solid background */
.bg-{type}  /* solid background (alias) */
.br-{type}  /* left border color */
.t-{type}   /* combined with .tag for action pills */
```

Care types: `prune`, `propagate`, `fertilize`, `water`, `repot`, `inspect`

**Action pills** (`.tag.t-{type}`) are the unified label element across all four plant views. Use this class — never invent new badge/chip patterns for care actions. The corresponding JS constants:

```js
const CARE_TYPES = { prune: { label, icon }, propagate: ..., ... }
const CARE_COLORS = { prune: "#c0622f", propagate: "#3d8a5e", ... }
```

### Key rendering functions

| Function | What it renders |
|---|---|
| `renderWeather()` | Full weather card with forecast, radar, PWS panel |
| `renderRainfallPanel()` | Rainfall context with rv-badge status chips |
| `renderFishing()` | Fishing tab content (lives inside Wildlife card; writes to `#wildlife-tab-content`) |
| `renderProperty()` | Property profile card |
| `renderPlantList()` | By Species view (calls `renderPlantCard` per plant) |
| `renderThisMonthPlants()` | This Month view grouped by care type |
| `renderTimeline()` | 3 Month view |
| `renderCalendarBody()` + `renderCalendarLegend()` | Full Year heatmap |
| `renderBirds()` / `renderAmphibians()` | Wildlife tabs (Birds, Amphibians) |
| `renderDashboardStrip()` | Top 4-tile teaser strip (Weather, Plants, Wildlife, Vehicles) |

### Plant view tabs

Four tabs share the `#plant-view-tabs` switcher. `switchPlantView(view)` controls visibility. Timeline and Full Year are rendered on demand (not at init). The active filter for By Species is stored in the module-level `activeFilter` variable.

### Card expand/collapse

Cards expand/collapse via `.expanded` class toggled on `.main-card` when its `.main-card-header` is clicked. CSS controls visibility of `.main-card-body` (display none → block). There is currently no animation — cards hard-toggle.

## Design system

**Fonts:** `Crimson Text` (serif) for the header title and plant guide prose. `DM Sans` for all UI chrome, labels, data, and tags.

**Header:** Dark forest green gradient (`#183524 → #2a6040 → #3a8a58`). Decorative circles in `::before`/`::after` at low opacity.

**Body background:** Soft green gradient (`#edf7e6 → #e2f0d8`). Max content width 660px, centered.

**Cards:** White, `border: 1.5px solid #d8eacc`, `border-radius: 18px`. Card icons are 42×42px rounded squares with context-appropriate gradients.

## Elevation calibration

**Property is 2,959 ft, not 1,750 ft.** The original data was written with a stale assumption (1,750 ft, derived from Lake Sequoyah's ~2,800 ft mistakenly attributed to the property). `property.json` is the source of truth: 2,959 ft confirmed via Open-Meteo elevation API at coordinates 34.5496°N, 84.3674°W (May 2026), 1,424 ft above KJZP baseline (1,535 ft).

Cleanup completed 2026-05-13 across `plants.json`, viewer.html's inlined `PLANTS_DATA`, and README.md:
- Numeric `elevation_ft`, "~1,750 ft" prose references, hardiness zone (7a → 6b), and KJZP delta strings all corrected.
- Frost-date `_meta` (`lastFrost_50pct`, `lastFrost_90pctSafe`, `firstFrost_50pct`) shifted from April 30 / May 21 / October 20 → May 3 / May 24 / October 17 to match `property.json` `atPropertyElevation`.
- Schema notes / data sources updated from "+7 days spring / -7 days fall" to "+10 days spring / -10 days fall."
- All `peakWindow` and `currentSeasonNote` dates in the **8 original plants** (white-pine, azalea, hydrangea, dogwood, boxwood, holly, mountain-laurel, japanese-maple) shifted +3 days for Jan–Jul dates / -3 days for Aug–Dec dates. The 5 plants promoted from `plants.draft.json` (pyracomeles, deutzia, clematis, hosta, iris-pond) were authored at 2,959 ft and needed no shift.

**Known imprecisions:** the +3/-3 shift relies on lapse-rate math (7 days per 1,000 ft); Paul's direct phenological observation is more authoritative if anything reads obviously off. Some descriptive prose still uses vague phrases ("mid-May to early June," "early summer") that weren't shifted — those are approximate to begin with and should be tightened only if a specific entry reads wrong on the ground.

## Forward direction — toward a field assistant (Phases D / E / F)

**Raised by Paul mid-C2 on 2026-05-18.** The Field Notes card I built in Phase B is a structured log. What Paul actually wants is a *field assistant* — a conversational interface that already knows this property in depth (every plant, every species, every past observation, the soils, the elevation, the frost dates, the lake) and that he can talk to in plain language, including photo input ("here's a picture of my Azalea. What's wrong with it?"). The structured journal becomes a side effect of the conversation, not the primary surface.

This is a real product shift. The current Field Notes UI (form modal with category/species pickers) is a stepping stone, not the destination. The path:

| Phase | Scope | Status |
|---|---|---|
| **D — Capture UX rebuild** | Replace the Field Notes modal with a single always-visible text box + mic at the top of the card. Drop the category and species pickers from the user-facing form entirely. Timestamp captured automatically. A `POST /api/classify` Claude call assigns category/speciesId behind the scenes after save. | ✓ Shipped 2026-05-19 (commit 783e72c). Worker `/api/classify` endpoint live; inline composer + async classify wired; fuzzy species matching against curated *_DATA. **Pivot 2026-05-20:** capture path becomes pure-text log per the no-AI-on-capture design principle Paul articulated this session ([[feedback_no_ai_on_capture]]). Classify-on-save call **removed from `viewer.html` 2026-05-20** (commit pending); `classifyEntry()` function (lines ~8412–8423) + Worker `/api/classify` endpoint kept dormant for possible reuse in the future batch roll-up (Phase G). |
| **E — Conversational layer** | Multi-turn chat with the full property context as the system prompt — plants/birds/mammals/amphibians/snakes/lizards/fishing/property + active observations + current weather. | ✓ MVP shipped 2026-05-19 (commit 3c8236c) as **Garden Guru**. Paul opted for a simpler shape than the synthesis recommended: explicit "Ask Garden Guru" button on a separate surface (not a unified intent-routing surface with Quick Capture). 5 follow-ups per conversation. ~57K-token digest stuffed into system prompt; cache_control breakpoints for cost. Conversations + cost log persisted to KV. **2026-05-20:** Paul stepped back from the E2E smoke test to do design work with user-researcher — decoding "what good looks like for Garden Guru" via an Evaluation Rubric artifact. Interview in progress (Q12 effectively answered: scope = the two-track design as it stands post-D-pivot). Tool-use deferred per migration triggers. |
| **F — Image input** | Photo upload on the chat surface (mobile-first — camera roll + capture). Use Claude's vision endpoint. Decide whether images persist with their associated entry (visual journal) or are transient Q&A inputs only. | **Benched 2026-05-20** per design conversation — but the 2026-05-20 Garden Guru rubric interview surfaced this as the killer use case for both Paul-mobile (Q1, Q3) and Mom (Q4: she is already doing the photos-for-ID workflow on Claude). Garden Guru without Phase F is strictly worse than what Mom already has. Bench is worth re-examining; engineering-partner + ai-advisor hand-off queued. Strategic question stays Paul's; the artifact just stops calling Phase F definitively down-the-road. |

**Constraints to honor:**
- The depth filter still applies: the assistant references only the property's actual scope (the 17 curated plants, 17 mammals, etc.), not regional completeness.
- Field-journal voice in both directions — the assistant doesn't lapse into "Here are 5 tips for caring for your Azalea." It speaks as someone who knows *this* azalea on *this* property.
- All API costs flow through the existing Worker with the existing `X-Tate-Token` auth. Per-call cost matters because conversations are multi-turn; consider Haiku for routine turns and reserve Sonnet/Opus for image-vision or long-context queries.

**Phase G — observations as a knowledge layer (direction raised 2026-05-19):** Field notes shouldn't just live as a structured log; they should feed back into other dashboard surfaces and sharpen recommendations over time. Concrete examples: Plants card "You noted the laurel opening April 25 last year — watch for it now"; Wildlife "Your first hummingbird last spring was April 18"; today-line grounded in recent observations not just live state; conversational assistant (Phase E) referencing past notes every turn. Don't build until Phase E lands and the observation set is rich enough (~50+ entries) to be useful. Voice rule: when a callout cites a past observation, it should sound like memory ("you noted X last year") not like a database row. See memory `project_tate_tracker_observations_feedback_loop.md` for the full thread.

**Plants to consider planting (direction raised 2026-05-19):** A curated reference for native species, protected/at-risk plants worth fostering, and anything that supports the local ecology — distinct from `plants.json` which tracks what's *already* on the property. Initial framing + seed entries in `plants-to-consider.md` at the repo root. Pulls heavily from existing research-resources.md Cat 2 (chestnut + hemlock restoration, rich-cove special-concern flora, GPCA partner network, Mt. Cuba Center trial reports for native cultivars, ethical-provenance nursery list). When this thread becomes active: decide on structured schema (mirror plants.json) vs free-form markdown, and start populating zone-affinity hints once map zones are stable. Connects naturally to the map view (zone affinity per candidate), Phase E (assistant can answer "what could I plant near the pond"), and Phase G (observations that find a species already present can promote it from "considering" to "found").

**Property map view (direction raised 2026-05-19):** A spatial surface — currently everything is by-time (calendars, peak windows, months). Paul wants a map of the property with sections/numbers/icons showing roughly where plants live. Explicit scope note from him: *doesn't need to be down to exact coordinates, but at least groups of plants in different little areas of the property.* Zone-level granularity is enough.

This is structurally different from existing surfaces because it introduces a spatial axis. It connects to several existing threads but doesn't depend on any of them:
- Microclimate aspects (south-southwest / north-northeast / east / west) on the Property card already imply zones — those could be the seed zone vocabulary.
- Each plant could gain a `location` or `zoneId` field on `plants.json` pointing to one of the named zones.
- Wildlife habitat zones could overlay later (fairway edge, forest interior, pond, near-spring) — the `habitatContext` field in `mammals.json` and `birds.json` already names some of these informally.
- Field-note observations could carry an optional zone in Phase G, turning the map into "where on the property has X been seen."

Open questions for when the thread becomes active:
- **Zone vocabulary** — what zones does Paul actually think in? Candidates: front fairway, pond edge, north-side slope, east-side plantings, the house perimeter, the spring drainage, deep woods. Needs his naming pass before any code.
- **Map base** — aerial photo from Google Earth (photographic), hand-drawn diagram (Sand County Almanac aesthetic, but commissioning art), or stylized SVG zones with no base image (lightest). Probably the SVG-zone path for v1; revisit later.
- **Interaction model** — click a zone → list the plants in it (and later, wildlife seen + observations made there); click a plant → highlight its zone; hover for preview.
- **Where it lives** — new tab in the Plants card, or new main card, or appended to Property card. Map view feels heavyweight enough for its own card.
- **Scope of overlays** — plants only (v1), or plants + wildlife habitat + observations from the start?

Don't start building until Paul has done a zone-naming pass. The hardest part of this thread isn't the SVG or the renderer — it's deciding what zones the property has and how they correspond to where plants actually live.

## Outstanding for Paul

1. **Husqvarna riding mower:** model sticker (under seat or rear fender) — need the specific Husqvarna SKU like TS354XD / YTH24K54 / GTH54LS.
2. **Homelite trimmer:** confirm UT33650A (straight shaft) vs UT33550A (curved shaft) — middle digit on EPA sticker is slightly ambiguous.
3. **Homelite blower/vac:** no model sticker found on the unit. Maintenance specs are inferred from the trimmer's engine family (HHCPS.0264AT). Acceptable for at-a-store reference.
4. **Annual: NASA SVS Dial-a-Moon visualization ID** — when SVS publishes the 2027 visualization (usually Dec/Jan), update the `DIAL_A_MOON_VIZ` constant in viewer.html (`year`, `parent` bucket, `id`). Find the new ID at svs.gsfc.nasa.gov/gallery/moonphase. Until refreshed, the moon hero hides cleanly once the year flips.
5. **Bolores paint codes — door-label photos:** Paul to send pics of the driver-door Vehicle Certification Label (EXT PNT + INT TR fields) to confirm the two-tone + interior codes. Researched candidates already in `vehicles.json` flagged `researched-pending-label`: upper = Medium Cabernet Red **2H / M6156**, lower = Light Chestnut **9T / 6190** (rule out Dark Chestnut); interior Chestnut is a TRIM code, not a paint M-code. Flip to `verified` once the label is read.
6. **GTI — confirm exact mileage:** anchored at ~81k from Paul's estimate (2026-06-28). Read the odometer next drive and update `gti-2016` `mileage` + the spark-plug/DSG/carbon framing if it's off.
7. **Tiguan paint color code:** read the VW data sticker (spare-wheel well under the trunk floor, or driver door jamb) before buying touch-up paint for the new "Paint touch-up" step — the touch-up has to match.
8. **GTI spare key — own-key spec:** read the part-number/suffix/frequency off Paul's own working key before sourcing a fob (confirm `5K0 837 202 AK` / `NBG010206T` / 315 MHz).
9. **Marietta dealer name:** verify it's still "Volkswagen of Marietta" when calling — the old "Jim Ellis VW Marietta" listing reads closed (possible rebrand/ownership change). Recorded under the current name in `gti-2016` `serviceContacts`.

## Location constants

| Field | Value |
|---|---|
| Address | 282 Church Mountain Road, Jasper, GA 30143 |
| Coordinates | 34.5496°N, 84.3674°W (confirmed via Google Maps + Open-Meteo elevation API, May 2026; previous 34.52, -84.46 pointed near Jasper town center and was wrong) |
| Elevation | 2,959 ft (confirmed; 1,424 ft above KJZP baseline) |
| USDA Zone | 6b (elevation-adjusted); 7b official county |
| Last frost 50% | May 3 |
| Last frost 90% safe | May 24 |
| First frost 50% | October 17 |
| On-site station | Kirschenbauer Ambient Weather station, MAC `D8:F1:5B:15:28:B8` (source of `weather-history.json`) |
| Sky quality | Bortle 3 (rural dark sky) |
