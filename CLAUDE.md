# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Pickup point — last session ended 2026-05-26 (afternoon + evening)

**Two work streams landed today:**

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

## Architecture

`viewer.html` is a single ~4,600-line self-contained file: all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework. The JSON files (`plants.json`, `fishing.json`, etc.) are the source of truth for data — they are fetched at page load and the inlined copies in `viewer.html` serve as fallback. When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 17 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
- `FISHING_DATA` — Lake Sequoyah species profiles, scoring weights, seasonal notes.
- `BIRDS_DATA` / `AMPHIBIANS_DATA` — Species with `monthsPresent`/`monthsActive`, status (resident/summer/winter/migrant).
- `VEHICLES_DATA` — Fleet registry with status badges.
- `PROPERTY_DATA` — Microclimate, soil series, watershed, elevation notes.

Live data is fetched async at init from Open-Meteo (weather + pressure), RainViewer (radar), and the Weather Underground PWS API (KGAJASPE279 — the nearest personal weather station).

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
| PWS | KGAJASPE279 (Weather Underground) |
| Sky quality | Bortle 3 (rural dark sky) |
