# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Session-start check — is the dashboard showing all of canon? (run at every Fernwood pickup)

**Run these first thing when picking up Fernwood, before other work:**

```bash
python3 tools/check-data-inline.py         # viewer.html inlines vs source JSON
python3 tools/check-digest-fresh.py        # Garden Guru's digest vs source JSON
python3 tools/read-mom-feedback.py --pickup # Mama's Perspective — surface Mom's NEW answers (silent if none)
```

`check-data-inline.py` compares the source JSON (`plants.json`, `mammals.json`, `birds.json`, …) against the inlined `*_DATA` constants in `viewer.html`. Exit 0 = in sync (say nothing, move on). Exit 1 = **drift** — surface it.

`check-digest-fresh.py` compares `worker/digest.json` (bundled into the Worker at deploy — Garden Guru's context) against a fresh rebuild from the source JSONs. Exit 0 = fresh; exit 1 = **stale digest**, meaning Guru is serving outdated data because a source changed but the digest wasn't rebuilt + redeployed (this happened 2026-07-07: plants + fishing were stale three days). Fix: `python3 tools/build-digest.py && (cd worker && npx wrangler deploy)`. Non-mutating — it restores the on-disk digest after checking.

The drift that matters most is **canon-ahead**: a species present in the JSON but *missing from the inlined data*. That almost always means **Garden Guru added it to canon but the re-inline step didn't land**, so a real, confirmed addition is sitting invisible on the dashboard. This is exactly how **Lizard's Tail** hid unnoticed until 2026-07-05.

When drift shows, don't auto-fix — the point is a **human signal that the addition is legit**:
1. Surface the specific species to Paul, framed as "added to canon (likely via Garden Guru) but not yet on the dashboard — legit?"
2. Get Paul's confirm that it's a real addition (his call, not an automatic one).
3. Only then `python3 tools/check-data-inline.py --fix`, verify clean, add a release note, commit.

(Root-cause fix still open: make Guru's promote flow verify its own re-inline commit landed, so this drift can't open silently in the first place.)

`read-mom-feedback.py --pickup` surfaces the ground-truth Mom has settled in **Mama's Perspective** since Paul last reviewed (it reads the Worker's `/api/feedback`; token from `.private/fernwood-token`). Prints a short "N new answer(s)" block with a drafted **ready-to-fold** canon edit per Yes/No answer, or **nothing at all** when there's nothing new (calm, no-noise — matches the app's tone). It **never writes canon** — promotion into `plants.json` (flip a variety's `confidence` inferred→verified, or correct it to what she said) stays Paul's call. When Paul has folded her answers in, run `python3 tools/read-mom-feedback.py --mark-reviewed` to advance the watermark so they stop showing as new. (Note: the viewer now reconciles answered questions against the Worker on load, so a Yes/No answer stops being served on all of Mom's devices automatically — `active:false` in `questions.json` is now just housekeeping, not required to stop re-asking her.)

## 📋 Canonical backlog → `BACKLOG.md`

**Live status for every Fernwood thread lives in `BACKLOG.md` (repo root) — read status there, not from the dated "Pickup point" log below (that log is historical, not current status).**

## Backlog — Mom engagement & feedback — ✅ SHIPPED 2026-07-13 as "Mama's Perspective"

> **Status: SHIPPED** (supersedes the "HELD" trail below). Paul steered the panel's held single-probe into a navigable, continuously-populatable **queue** — **"Mama's Perspective"** — and it shipped 2026-07-13 (git `a888ebb`; `questions.json` + `MomQueue` in viewer.html; RELEASE_NOTES; Worker `/api/feedback` live). Now in the ~2–3 wk validation gate (Grow/Kill in `BACKLOG.md`). The paragraph below + the panel synthesis + the `project_fernwood_prompt_mom_input` memory are the historical HELD design trail — point-in-time, now superseded.

- **Mom engagement/feedback — five-lens panel RAN + CONVERGED; build decision HELD (Paul, 2026-07-13).** The whole parked Mom-feedback backlog was reassessed holistically under a hard reframe: **the discovery interview will never happen — the device + her usage must generate the signal.** ⭐ **Master brief (single entry point):** `.user-research/2026-07-13-mom-engagement-panel-synthesis.md` — it links all five reviews (user-researcher/ux/eng/ai-advisor/content-steward, all 2026-07-13) + the grounding corpus. **Converged recommendation:** ship ONE contextual confirm ("is this crocosmia 'Lucifer'?") on the plant entry, AI-free capture, instrumented offered→viewed→tapped funnel, hard kill metric — *as a prove-before-build probe*, NOT a standing queue (that's the ⭐-star trap). **Backlog reassessment folded in:** ⭐ star → KILL; 🚩 open-feedback → DON'T BUILD; seeded prompts → deprecate; the weed "prompt-for-input" seed → SUBSUMED into this; change-reactions → DEFER; **Save/Ask split → still open, separate thread.** **HELD:** only Paul's go/no-go to BUILD v1 remains — nothing needs re-running. (Superseded seed brief: `.plans/2026-07-13-mom-prompted-input-scoping.md`.)

## Backlog — raised 2026-07-05 (Concept A session)

- **Save/Ask two-button intent split — revisit (design, Paul-raised).** Paul isn't convinced the app needs both "Save to journal" and "Ask Garden Guru" buttons. *Don't just remove them* — the split is the on-screen form of Paul's own capture-path principle ([[feedback_no_ai_on_capture]]): Save = deterministic, AI-free, logs verbatim words; Ask = the AI path. Collapsing forces either all-capture-through-AI (breaks the principle), intent-guessing on the capture path (what Phase D pivoted away from), or do-both-every-time. The 7/2 Mom evidence ("I hoped it was logged but wasn't sure") argues for a *distinct* Save. Likely resolution is **hierarchy, not removal** — make Save the primary action, Ask the quiet secondary — but confirm what's actually bugging Paul (clutter vs choice-friction vs one-intent-dominates) first. Consider a ux-expert read since this was an evidence-based decision.
- ~~**Refined "Peak this week" — needs a structured peak field (data work).**~~ ✅ **SHIPPED 2026-07-06** — machine-readable `peakDates` ({start,end} MM-DD) + the year-wrap-aware `mmddRangeActive` helper are live on all 88 windows; the prose stays for display. (Confirmed by the 2026-07-12 bloom-pass engineering review — the new `bloom` field reuses this same proven mechanism.)
- ~~**Fishing data — make it granular + dynamic (Paul-raised).**~~ ✅ **SHIPPED (Passes 1–3, 2026-07-06, LIVE).** `fishing.json` gained a versioned `conditionsModel` (evidence-weighted signals) + season-tagged phases; the view is now a station-driven, time-of-day forecast (dawn/dusk windows scored on their own hour's pressure/rain/wind) promoted to its own standalone card. See the 2026-07-06 pickup point below.

## Pickup point — last session ended 2026-07-14 (fleet Gmail receipt sweep + DR-Z overhaul recovery + GTI plugs + auto-deploy)

**A vehicle-records session, then a first live agent-run Worker deploy.** All shipped + pushed (Tate-Tracker HEAD `7fc54d7`); **Worker redeployed by the agent** (version `977075b2`, `/health` OK). Full-detail lives in the gitignored `.private/service-records/` + `.research/`.

### What happened
- **Whole-fleet Gmail receipt SECOND pass** (learning from 7/13: the first pass keyed on subjects/Amazon-eBay and missed body-level order confirmations). Ran 4 parallel body-level sweeps over the 4 GB mbox (VW · Ford · DR-Z400S · small-engine). **Net-new folded to `.private/service-records/`:** (1) **Bronco audio source receipt** — Creative Audio Feb 2026, order #1000140355, the missing purchase record for the Infinity Kappa 63XF door speakers (amp/subs confirmed still unbought); (2) **GTI racing plugs** — two NGK.com orders (R7437-9 2022 / R7437-8 2025), which also deterministically corroborate the OCR'd Eurofed tune-plug read. **Confirmed ABSENT (don't re-hunt):** F-150 (only watched eBay offers), golf cart / mower / EGO / Homelite / Kobalt (Gmail is not a source for small-engine parts — Amazon export only), no perf-parts vendor for the VWs. Two PayPal items positively ID'd (BCG; a diesel DPF-regen service) — both already non-fleet.
- **DR-Z400S 2025 overhaul — 2 of 3 items recovered.** Paul pulled the **Partzilla order #11-8290276 ($165.90, the mystery PayPal)** → **grips + start/stop switch (37200-13E30 RH switch)** recovered with part #s. **Radiators STILL outstanding** — not in that order, not in Gmail; Paul checked Partzilla, no other orders. Origin unknown; parked pending his recall.
- **GTI spark plugs — resolved + researched + card updated.** The tuned car runs **NGK R7437-8** (installed, running well) — the correct APR Stage-1 heat range; the R7437-9 Paul "used to use" is the Stage-3 plug (over-cold) and now hard to find, which explains the switch. Researched the full setup (`.research/2026-07-14-gti-spark-plug-setup.md`); card's spark-plug spec + restoration detail now carry a **next-change reminder** (gap 0.024″ — ships 0.028″, close it down; ~25 Nm/18 ft-lb; no anti-seize; ~20k-mi interval). Superseded the old stock-PFR7S8EG note.
- **Auto-deploy proven agent-runnable.** `tools/deploy-worker.sh` runs end-to-end when the Bash **sandbox is disabled** — the past "Worker deploy is Paul-only / classifier blocks it" belief was really just the sandbox. Agent can now deploy Fernwood when asked (see [[reference_fernwood_worker_deploy]]).

### ⚠️ Owner: Paul
1. **DR-Z400S radiators** — the last un-recovered overhaul part. Try to recall where they came from (in-store / other vendor / other account); surfaces if a receipt turns up.
2. **(Optional)** the GitHub-Action hands-off deploy is now a nice-to-have, not a blocker (agent can deploy unsandboxed).
3. **Watch:** Guru digest is at ~80k tokens (the tool-use-migration ceiling) — no action today, but it's at the line before the next big data add.

## Pickup point — last session ended 2026-07-14 (weather card reorg + source-citation system)

**Weather card reworked end-to-end with the ux-expert + user-researcher, shipped + pushed + LIVE on GH Pages (Tate-Tracker HEAD `fa40ceb`). viewer.html + release notes only — no Worker/digest change.** Two commits: the IA reorg (`9450a82`) + the citation system (`fa40ceb`). Design trail: `.ux-reviews/2026-07-14-weather-card-reorg.json` + `.user-research/2026-07-14-weather-card-reader-jobs.md`.

### What shipped
- **IA reorg (glance → repository, mirrors the fishing card):** one meaning-first glance headline at top (the `generateGardenerInsight()` sentence + suggestion), which now ALSO drives the collapsed header via `renderWeatherSummary()` (one engine, can't diverge). Then **Right now** (measured) → **Forecast** (7-day + hourly merged into ONE block, one citation) → **Rainfall** (mid-card) → **Inside** → **Burn status** (bottom reference; a *severe* NWS fire alert promotes up to the top "Worth knowing" strip) → methodology.
- **Source-citation system (per Paul):** top status bar is now the KEY — each source named once (📡 Fernwood Weather Vane / 🌐 Open-Meteo) with live status; each box cites with just the minimal colored oval + live dot. New `srcChip()` + `liveDot()` helpers. Canonical `ICON LEGEND` comment table above `srcChip()` = single source of truth, synced with the on-screen methodology footer.
- **Station renamed** "Kirschenbauer" → **"Fernwood Weather Vane"** everywhere. Rainfall gauge (📡) kept distinct from its regional 25-yr ERA5 comparison (📊). Fixed the confusing "☁️ Sky" oval. **Forecast icon rationalized ☁️ → 🌐** (a cloud conflated source with sky content; globe = "from off the property").

### Design principles written (candidates, in `~/.claude/design-principles/`)
Three, all Paul-stated/ratified, `[candidate — 1 occurrence]`: **provenance-honesty** (cross-project) · **modeled-flush-with-measured-borrows-authority** (fernwood) · **an icon *system* needs a maintained legend + per-symbol rationale** (cross-project). The ux-expert's "split by freshness not topic" was **dropped** (topic is the outer axis; already covered by "Freshness sets altitude").

### ⚠️ Owner: Paul
1. **Safari-kill on the phone** to bust the iOS cache, then eyeball the reworked card on-device.
2. The three candidate principles await a second sighting before promotion (nothing to do now — noted for provenance).

## Pickup point — last session ended 2026-07-14 (unified-input polish + plant look-fors bumped to the Plants tile)

**Three UI changes shipped, merged to `main`, and LIVE on GH Pages (Tate-Tracker HEAD `dc2a067`). No Worker/digest change — all `viewer.html` + release notes.** Statuses folded into `BACKLOG.md` under "✅ Just shipped (2026-07-14)."

### What shipped
- **Composer ordering fix** — when a Garden Guru thread opened, "Mama's Perspective" jumped *below* the conversation and the text box drifted from its button. Root cause: `.unified-input` engages flex-`order` on `.conversation-active` (conversation `-3`, input-row `-2`) but `.mom-queue` and `.ui-actions` had no `order` → defaulted to `0` and fell below. Pinned `.mom-queue` to the top and kept `.ui-actions` with the composer. Browser-verified order: Mama's Perspective → thread → textbox → button.
- **Button relabel** — "Log to the Almanac" → **"Save & ask the Almanac"** (Paul's pick), so it reads as save *and* answer. Behavior unchanged (still log-first).
- **Plant look-fors → Plants tile check-prompt** — the day's top *plant* look-for now leads the always-visible Plants tile as a tappable **"👀 Worth a look"** row; tap pre-fills the composer (`"Checked the [plant] — "`) to log ground-truth (the loop). "Worth noticing today" list stays in the Plants card ("do both" — Paul). Refactored the plant half of `computeLookFors` into shared `gatherPlantLookForCandidates(now)`; new `plantCheckPrompts()`/`wirePlantCheckPrompt()`. Caught + fixed a `MetricsCollector` TDZ throw (the first synchronous `renderDashboardStrip()` runs before the `const` initializes; `typeof` still throws in a const's dead zone → guarded with try/catch).

### ⚠️ Owner: Paul
1. **Safari-kill on the phone** once to bust the iOS app-shell cache, then eyeball all three on-device.
2. **Judgment call on the tile prompt** — it shows **one** plant look-for (today the mow/fairway one). Want it biased toward *flowering* plants over turf, and/or show **two**? Both ~1-line changes.
3. Feature branch `claude/conversation-order-button-label-ku1ef8` is fully merged into `main` (identical) — safe to delete whenever.

## Pickup point — last session ended 2026-07-13 (Amazon full-export parts fold + GTI plate-light + prompt-Mom seed)

**The full Amazon "Request My Data" export (`~/Desktop/Claude/Your Orders/`, 1,231 orders) replaced the 10-screenshot reads — deterministic dates/prices/ASINs.** Shipped + pushed + Worker deployed (Tate-Tracker HEAD `8add29e`). Live on GH Pages.

### What shipped
- **GTI plate-light DIY fix** (`serviceHistory`, verified) — cleaned/reseated the rear license-plate light connectors after a bulb-out flicker; same reseat-and-tape technique as the DR-Z, recurrence-watch. Private plate/reg facts (plate CQV7939 / **Fulton** county / **JUN 26 sticker = expired**, corroborates the past-due reg) in the gitignored `gti-2016/EXTRACTED.md`.
- **GTI coolant tank** — Paul **installed** the expansion/overflow reservoir tank himself (Feb 2026). New `serviceHistory` row + a context line on the coolant restoration item (suspect swapped, predates July's clean pressure test — NOT called solved).
- **DR-Z400S spark plug** filled in: **NGK #1275 (CR8E)**, Paul-confirmed (corrects the earlier "cart spare" guess — cart runs BPR4ES).
- **Bronco installs woven in** — Dorman 742-251 window motor + Dorman 38424 tailgate striker (rear-window/tailgate item) and Icyhaws door clips (door-panel item), Paul-confirmed installed.
- **Amazon parts analysis folded** — durable master catalog `.private/service-records/AMAZON-PARTS.md` (39 fleet parts, per-vehicle, priced, tagged kept/returned) + reconciliations into GTI/Bronco/new DR-Z `EXTRACTED.md`. **Methodology catch:** order-level refund ≠ item returned; fixed via refund-amount matching. Corrections: DR-Z **starter was returned**; Bronco **manual + clips kept** (only the $10.88 keychain came back); **M12.1×1.5 is the drain-plug keeper**.
- **Trimmer Outstanding #2 → UT33650A** confirmed (straight-shaft photo; card already read that).

### ⚠️ Owner: Paul
1. **GTI spare-key spec (Outstanding #8)** — the key photos confirm the *form* (MQB 4-button flip, HU66) but the part #/FCC live on the **internal fob sticker**; split the fob + shoot it to close it.
2. ~~**Bronco restoration statuses**~~ ✅ resolved 2026-07-13: "Rear window & tailgate operation" → **done** (window + tailgate operate correctly after the motor/striker work). "Driver door panel" stays open — worked on, not done (Paul's next big project).
3. ~~[CONFIRM] install-status flags~~ ✅ **resolved 2026-07-13** (batch): Bronco tailgate/door parts + dome all installed; DR-Z running all 4 parts (#1275 installed); audio baffles on-hand (gated on door panel); cart drain plugs one-returned/one-kept. Only 3 tools stay 'refund-ambiguous' (multi-item orders, not worth chasing).

### Deferred (agent-can-drive)
- ~~**Gmail mbox receipts → fold**~~ ✅ **FOLDED 2026-07-13.** Full Gmail export (`~/Downloads/All mail Including Spam and Trash-002.mbox`, complete ~14K-msg history) mined → 36 receipts (gitignored `.private/service-records/EMAIL-RECEIPTS.md`, de-dup-reconciled). **Finding: records were already well-built — most receipts corroborate; few net-new.** Shipped: DR200S serviceHistory row (OEM handlebars). Folded to private: Bronco eBay net-new parts (window switch/dome/door clips/latch clips/lock actuator), DR-Z air-fuel screw+filter, Tiguan fender flare. **All residuals resolved 2026-07-13:** PayPal = not vehicle (ignored); Tiguan fender flare = damage repair (on serviceHistory); eBay part install-status batch-confirmed (Bronco tailgate/door parts installed, DR-Z parts installed, audio baffles on-hand). Reusable mbox-parser pattern proven.
- **Mom engagement/feedback — panel done, build HELD.** Five-lens panel ran + converged 2026-07-13; the weed "prompt-for-input" seed is subsumed. Reframe: interview is dead, device+usage drives signal. ⭐ Master brief: `.user-research/2026-07-13-mom-engagement-panel-synthesis.md` (links all 5 reviews + corpus). Converged v1 = one AI-free contextual confirm probe (crocosmia='Lucifer'?), instrumented funnel, hard kill metric; NOT a standing queue. Only Paul's go/no-go to BUILD remains. Also still-open: the **Save/Ask two-button split** (separate thread). Memory [[project_fernwood_prompt_mom_input]].

## Pickup point — last session ended 2026-07-12 (Bronco Amazon parts + dome-light record)

**A short, focused thread off the vehicle-records work: chased down "what did I buy for the Bronco's dome lights."** Answer wasn't in the 62-frame receipt folder — it was in Paul's **Amazon order history** (10 screenshots he sent). Committed locally (Tate-Tracker HEAD after commit), **UNPUSHED + Worker NOT redeployed** — Paul holds the push/deploy.

### What shipped
- **New `done` restoration item on Bolores** — *"Interior lighting — dome, map & dash (warm LED)."* Paul re-bulbed the overhead dome + the two flanking map lights + some dash indicators to **warm 2700K (SEALIGHT 194)** after trying and returning the cooler 6000K white sets ("too sterile"), and fitted a new plastic dome cover. `vehicles.json` → re-inlined `VEHICLES_DATA` (parity verified) → digest rebuilt → release note added.
- **Full Paul-era Amazon parts haul catalogued** into `.private/service-records/bronco-1989/EXTRACTED.md` (gitignored) — a new "Paul-era parts haul" section: Bronco electrical/body/interior/reference parts + a clean NOT-Bronco split. **Screenshot reads = item + date only** (no prices/order#s; titles truncated).
- **Golf cart parts reconciled** (no card change — its card was already right): spring-2026 service used an **oversize M12×1.5 drain plug** (stock had stripped; several sizes bought+returned; Paul believes M12×1.5 was the keeper). **GTI confirmed has NO aftermarket drain plug.** NGK **#1275** plug is an **on-hand spare, not installed** (cart still runs BPR4ES).

### ⚠️ Owner: Paul
1. **Deploy to take it live** — `git pull --rebase` (weather bot) → push (GH Pages) → `cd worker && npx wrangler deploy` (Worker deploy is Paul-only; classifier blocks the agent). Then Safari-kill on the phone to see the Bolores card.
2. **One tiny confirm** — the *"just in the shop, not applied to anything"* item: I read it as the **NGK #1275 spark plug**; confirm it wasn't the **APE fuel filter** (also parked on-hand, unassigned cart/dirt-bike/mower).

### Deferred (agent-can-drive next)
- **Catalog the *rest* of the Amazon Bronco parts onto the card** — Dorman 742-251 power-window regulator, Dorman 75450 door-lock rod clips, Dorman 38424 tailgate support, fuse kit, dielectric grease, connectors, switches, plastic restorer, Chilton manual — with per-item install status from Paul.
- **Finish the original ask** — "talk through the proposed jobs / maintenance / service history" for the GTI + Bronco (the verification flags F-1…F-5 / F-A…F-F were surfaced but not walked end-to-end).

## Pickup point — last session ended 2026-07-12 (bloom-time + Hydrangea hub; fleet records from photos)

**A big multi-thread session — all shipped, pushed, and Worker deployed (Tate-Tracker HEAD `eea8e14`).** Photos Paul sent from the property drove two workstreams: a plant Almanac enrichment (bloom-time + a hydrangea reorganization, run through the eng+ux expert panel) and a fleet-records catch-up from sticker/placard photos.

### What shipped
- **Plants schema v5 — bloom-time + Hydrangea hub-and-roster** (`040d10a`). New plant-level `bloom` field `{window, dates[] (MM-DD via mmddRangeActive), confidence, note}` on 18 flowering plants (foliage/structure omit it); observed-on-property windows tagged `verified`, book `inferred`; flows to Guru's digest. viewer: `renderBloomRow()` — calm "In bloom" card row (warm rose, lights up in-window, Mom text-lg scaled) + `renderRoster()`. The generic Hydrangea entry became an overview **hub** (old-wood/new-wood education + a roster naming each hydrangea); DreamCloud + Pop Star keep their own cards; **new Panicle Hydrangea card**. Fixed the duplicated `'NCHA3'` cultivar code → reliable trade names. Expert path-evals committed (`.engineering/2026-07-12-path-bloom-and-hydrangea.md` + `.ux-reviews/2026-07-12-bloom-and-hydrangea.json`) — **both rejected care-first**; chose hub-and-roster (ux) + bloom-as-plant-state (eng). Browser-verified (26 plants, 18 bloom rows, 11 in-bloom-now on 7/12, no JS errors).
- **Crocosmia + Garden Phlox** added (`6e1cd75`) — photographed blooming on-property.
- **Fleet records from photos** (`eb917c8`): Husqvarna **Z254F** (closed Outstanding #1), DR200 handlebars → done, new **EGO 56V string trimmer** (ST1620T), verified tire pressures (GTI 37 / Tiguan 38 / F-150 35 psi) from the door placards. VINs kept out of the public JSON.
- **`tools/deploy-worker.sh`** (`8850612`) — reusable rebuild-digest → freshness-check → `wrangler deploy` → `/health`; the repeatable fix for the 7/7 stale-digest drift. Deployed twice this session; Guru serves all the new data.

### ⚠️ Owner: Paul (residual)
1. **Mom ground-check on 2 plant IDs** — crocosmia (may be 'Lucifer') + the white mophead (may be 'Annabelle'); both went in flagged as photo-reads.
2. **`NCHA3` cultivar codes** — softened to trade names; the plant tags confirm exact codes if precision is wanted.
3. **Data still to collect** (equipment/vehicles): Homelite trimmer shaft digit, Z254F mower-belt P/N, GTI spare-key spec, Tiguan + Bolores paint codes, EGO manual PDF, and battery/charge specs for the two cordless tools (EGO 56V, Kobalt 40V). Registrations still overdue (GTI + Bolores June 3; GTI needs a 2026 emissions test first).

### Deferred (promote on signal)
Bloom in the "Worth noticing today" glance (after de-crowding the "Peak this week" area); the "is it open yet?" ground-truth loop; two expert-proposed principles held as candidates ("reuse the mechanism, not the semantics"; match structure to the reader's unit of meaning).

## Pickup point — last session ended 2026-07-11 (GTI July service record + registration renewal reminder)

**Folded the GTI's 7/11 Express Oil visit into the service record, reframed the coolant thread as observations (no verdict, per Paul), and shipped a new registration-renewal reminder on every vehicle card.** Committed + pushed (Tate-Tracker HEAD `9e98372`); Worker redeployed by Paul (`/health` ok @ 5:23 PM ET — serving the fresh digest).

### What shipped
- **GTI serviceHistory** gained the 7/11 Express Oil visit (oil + tire rotation + brake-fluid flush; cooling system pressure-tested → **no active leak**) and the 6/30/25 emissions PASS. Mileage now VERIFIED **82,698** (retires the long-open "confirm exact mileage"). DSG flagged past-80k / overdue. Brake-fluid flush → `done`; the invoice's "with friction replacement" resolved to **fluid-only, no pad work** (Paul confirmed) — but no pad *measurement* was recorded, so "Brakes — quick check" stays open (rides the next shop visit).
- **Coolant reframed → "Coolant — verify at next shop visit," status `planned`, no conclusion drawn.** Holds two observations side by side: a single-source (unverified) Cannon 9/15/25 invoice note that the reservoir was found empty + topped off, AND the 7/11 clean pressure test. Per Paul: don't make a call, don't chase — bundle the verify into an already-happening visit (spare-key **dealer** trip = free coolant/brake eyeball + recall check; or the overdue **DSG at Autobahn** = the real dye/pressure read). Woven into the coolant/brakes/spare-key steps.
- **NEW capability — registration renewal reminder.** Each vehicle now carries a `registration` block (owner + `renewMonth`/`renewDay` + `emissionsRequired`); `renderRegistrationLine()` (viewer.html, before `renderVehicleItem`) renders a calm, birthday-keyed glance on the Vehicles card — quiet far out, warms within ~5 wks, softens to "worth handling" just past the date, rolls forward. Field-journal tone (no alarm; `.vehicle-reg` CSS, soft beige/gold/terracotta). GTI + Bolores = Paul / **June 3** (currently show past-due); Tiguan + F-150 = Mom / **Sept 21** (calm). Browser-verified all 4 render correctly.

### ⚠️ Owner: Paul (residual)
1. **Real-world tags OVERDUE** — GTI + Bolores registrations were due June 3 (Paul's birthday), now ~5–6 wks late (GA late penalty accruing). GTI needs a fresh **2026 emissions test → then renew**; Bolores just renews (1989 = emissions-exempt).
2. **Mom's county (open data point)** — Tiguan & F-150 (Mom's, renew Sept 21) are marked emissions `"verify"`: exempt if garaged in Pickens/Jasper, tested if metro-Atlanta. Once Paul says, finalize their two cards.
3. **GTI DSG service overdue** (82,698, past the 80k interval) — highest-value while-in-shop item for the next Autobahn trip; bundle the coolant dye/pressure verify + brake-pad check with it.

## Pickup point — last session ended 2026-07-10 (GTI oil-gate softening + people.json Mom fix)

**Applied the pre-decided oil-gate softening from the 7/09 reintegration backlog and fixed the telemetry people-map. Committed, pushed, and the Worker redeployed — Garden Guru serves the corrected guidance.** Tate-Tracker HEAD `68727bb` (pushed to GH Pages); Worker version `549ee062` (`/health` ok).

### What shipped
- **GTI oil gate softened → spec, not viscosity.** Reframed the "requires 5W-40 / don't put 5W-30 in it" language to **gate on VW 502.00 approval**: a 502.00 5W-30 is manual-legal (the owner's manual allows 5W-40 *or* 5W-30), 5W-40 preferred for the Stage-1 tune; the real walk-away is a generic/dexos 5W-30 with **NO** 502.00. Applied in `vehicles.json` → `gti-2016` (oil.value + Express Oil restoration detail + serviceContact notes), the inlined `VEHICLES_DATA` (parity, JSON re-validated), and `.research/2026-07-08-gti-express-oil-coupons.md`. Digest rebuilt + Worker deployed. **Closes reintegration-backlog #1.**
- **Call guide added to the repo** — `.research/2026-07-09-gti-express-oil-call-guide.md` (gitignored). **Closes reintegration-backlog #2.**
- **`tools/people.json` corrected** — `d-14nyhnjz` confirmed = Mom (via her 7/02 discovery interview), not the old "probably Paul's old iPhone" guess; added a Mom entry. Exact deviceId left empty (the map exact-matches and the full id is truncated in past notes) — **fill it from the next `analyze-fernwood` run.**

### ⚠️ Owner: Paul (residual)
- GTI shop booking still open (the 7/08 two-shop plan stands). Coupon clocks: $39.99 oil + MID726 **expired 7/11**; free rotation/alignment + $20-off (YDCD26) run to 7/31.
- Reintegration-backlog #3 loose ends: the earlier Worker-redeploy question is now moot (redeployed this session ✓); still confirm **exact GTI mileage** next drive.

## Pickup point — last session ended 2026-07-09 (vehicle service-records pipeline — GTI trial)

**New capability shipped: mine photos of paper service records → onto the vehicle card + a private backup.** Committed + pushed (Tate-Tracker HEAD `30d9f5d`); Worker redeployed (Guru serving the fresh digest, verified `/health` ok). This activates the "future thread" flagged in [[project_fernwood_vehicles_card]] and reuses the Hillyer reader discipline. Full mined detail: `.private/service-records/gti-2016/EXTRACTED.md` (gitignored). Capability memory: [[project_vehicle_service_records]].

### What shipped (`gti-2016`)
- **New `serviceHistory[]` + a "what she's had done" card panel** — 10 rows, 2021→2026 (date · mileage · shop · summary), provenance chips (`inferred` = OCR read, `verified` = Paul-confirmed), mirrors the "what she needs" restoration panel. Re-inlined `VEHICLES_DATA` by hand (parity verified).
- **Shop tier repositioned:** Express Oil (stop 1) → **Eurofed (preferred specialist** — new contact; it's the real APR tune shop, holds the history, 4.7★, 24/24 warranty, chain-so-get-it-in-writing caveat) → **Autobahn (alternative** — demoted; the false "where your tune was done" claim removed).
- **Coolant leak reframed** — open + undiagnosed (Express Oil diagnosing first); 2022 Autohaus water-pump replacement attached as *context*, NOT called a recurrence (Paul's steer). Mileage anchored to verified **79,582 (1/2/26)**; recall step notes the 3/2025 suction-jet-pump recall was already done; light "have Express Oil eyeball the brakes" item.
- **New tooling:** `tools/service-records/intake.py` (deterministic AI-free intake) + `service-records.manifest.json` (committed PII-free durability catalog). Raw scans + full detail (VIN/address/costs) stay gitignored in `.private/`. Capture from Apple Photos via **osxphotos** (installed via `uv tool`).

### ⚠️ Owner: Paul
1. **Express Oil tomorrow** — get the coolant leak diagnosed; hand them the "pump already replaced 2022" context now on the card.
2. **Eyeball the GTI card on the phone** (Safari-kill for the cache) — open "▸ what she's had done."
3. **DECISION — off-machine backup target (R2 vs Google Drive).** The only unbuilt piece of the durability design; Apple Photos is the interim second copy, the committed manifest makes any loss detectable. Once chosen, wire `backup.sh` — same setup then serves the Bronco's bigger paper pile next.

### Oil-gate feed
Every Express Oil change on record used **Valvoline 5W-30**, not 502.00 5W-40 — reinforces the open "soften the oil gate to spec-not-viscosity" backlog item (a 502.00-approved oil is the real gate).

### 🔭 Backlog idea (raised 2026-07-09) — photo-library vehicle/repair-photo miner (FULL-TEAM RESEARCH, not started)
The service-records trial mined the *documents*; this mines the *photos*. Paul takes lots of pictures **while fixing / tearing things apart**, plus photos of the vehicles themselves — scattered across a ~50K-asset Apple Photos library. **Idea:** a tool that uses existing/new albums as seeds (the **Bolores/Bronco** album, a **new dirt-bikes** album Paul just started) to scan the library and **identify + PROPOSE** additional per-vehicle photos (the machine + its repair/teardown shots), to enrich the vehicle cards and feed the eventual narrative "book" of work done. **Deterministic where possible** (album membership, EXIF date/geo, burst/filename clustering) **+ a trainable/learned layer** (visual match to a given vehicle) — always **propose, human confirms** (honors the capture-path discipline; AI on the ask path). For the full expert team to scope + research: engineering-partner (matching + storage), ai-advisor (deterministic-vs-learned split, on-device vs API vision, the "we can train it" mechanism), ux-expert (how proposals surface for confirm). Connects [[project_photo_library_overhaul]] (the 50K-asset library) + [[project_vehicle_service_records]] (the photo/book layer) + osxphotos (already installed). NOT started — capture only.

## Pickup point — last session ended 2026-07-08 (manuals corpus)

**Manuals for the whole fleet — research pass + a 📖 link on every card, shipped & pushed (Tate-Tracker HEAD `710b6a6`).** Reference materials for all 15 vehicles/equipment assembled into a new `manuals/` corpus and linked on each card; the links flow to Garden Guru's digest.

### What shipped
- **18 manuals found, downloaded, and text-extracted** covering all 15 machines (7 vehicles + 8 equipment). New **`manuals/`** dir: `pdf/` (source PDFs — **gitignored**, ~197 MB local-only, since the repo is public) + `text/` (pdftotext extractions — **committed**, ~3.9 MB; the searchable substrate a future Guru retrieval layer would read) + **`INDEX.md`** catalog (source, authority, pages, model-match confidence) + **`download.sh`** reproducer.
- **`manual: {label, url}` added to all 15 `vehicles.json` entries** (was only the DR200S); re-inlined `VEHICLES_DATA` **by hand** (note: `check-data-inline.py` does NOT track vehicles — the const at `viewer.html:~4989` is a one-line JSON blob, replace it directly); rebuilt the digest. Card shows the 📖 link (browser-verified rendering, incl. equipment); links flow into Guru's digest — **links only, no manual text** (digest is at **~76K of the 80K** tool-use-migration ceiling; folding manual text in would blow past it — this validated the "links only" call).
- Release note added (2026-07-08 "A manual for every machine").

### Notable resolutions
- DR200S "owner's manual" was actually the **262-pg factory service manual** (owner's-manual card link stays the readable manua.ls viewer). Swapped a 14-pg DR-Z400S stub for the **full 431-pg service manual** (bike is mid electrical/speedo repair). Trimmer model ambiguity resolved (**UT33550A is not a real Homelite model**). Husqvarna mower anchors on the verified **Kawasaki FR691V engine manual** pending its model sticker; Homelite blower/vac uses a best-match 26cc manual (no sticker on the unit).

### ⚠️ Owner: Paul
1. **Worker redeploy** — the card links are live on GH Pages, but Guru's *live* digest only updates on `wrangler deploy` (the auto-mode classifier blocked the agent from running it). Paul ran `cd worker && npx wrangler deploy` via `!` at session end — **confirm it landed** so Guru serves the new links (Worker health was OK at deploy time).
2. The two best-guess links (**Husqvarna** mower, **Homelite** blower/vac) become exact once their model stickers are read — already tracked in "Outstanding for Paul" #1–#3.

## Pickup point — last session ended 2026-07-08

**GTI service plan built out on the Vehicles card — Express Oil is Stop 1, Autobahn is the specialist net.** All committed + pushed (Tate-Tracker HEAD `2d391cf`). Full plan/questions/prep/price-table: `.research/2026-07-08-gti-express-oil-coupons.md` (gitignored); the 4 coupon email PDFs archived at `.research/express-oil-coupons-2026-07/` (gitignored, local-only; originals in Gmail `from:expressoil.com`).

### What shipped (`vehicles.json` → `gti-2016`, re-inlined into viewer.html)
- **New `expressoil` service contact** = "STOP 1 — go here first" (Paul's regular oil shop, down the street, 404-659-6225, ASE-certified, does European). Carries the prep (phone-ahead **VW 502.00 5W-40** gate + coupons in Gmail), the one-trip visit checklist, the "walk out with a written water-pump estimate" goal, and quote sense-checks (WP under ~$650 = plastic pump/no housing; over ~$1,300 = dealer pricing).
- **New restoration step "Oil change + coupon visit (Express Oil)"** (due-soon): gate on 502.00 → stack free tire rotation (RTE026) + free alignment check (ASR026) → free coolant-leak look + pressure test (**G13 pink only**) → written estimate.
- **Coolant-leak step** now lists **both shops** (`["autobahn","expressoil"]`) — free look/estimate at Express Oil, repair defaults to Autobahn unless Express Oil clears the bar (metal-impeller pump, VW/VCDS diagnostics, warranty).
- **Brake fluid flush** reassigned → **Express Oil-first** (`["expressoil","autobahn"]`) on the oil trip **if they use DOT 4 LV** (shares no labor with the DSG); Autobahn fallback.
- **DSG** stays Autobahn (temp-controlled fill wants the specialist; sub-$250 quote = just a drain-and-fill). GTI `notes` carry a one-line plan summary.
- Garden Guru **digest rebuilt** + release note expanded.

### ⚠️ Owner: Paul
1. **Phone Express Oil (404-659-6225) before going** — confirm they stock VW 502.00 5W-40 + out-the-door price with $20-off (coupon is standard-oil-only, voids with your own oil). If they can't do 502.00, skip the oil there but still go for the free leak look.
2. **Coupon clock:** the **$39.99 oil price + mechanical coupon (MID726) expire July 11**; free rotation/alignment + $20-off oil (YDCD26) run to July 31.
3. **Confirm exact GTI mileage** (anchored ~81k) next drive.
4. **Redeploy the Worker** so Guru's refreshed digest goes live: `cd worker && npx wrangler deploy` (the classifier blocks the agent from running it in auto mode). The card itself is already live via GH Pages.

## Pickup point — last session ended 2026-07-07

**Garden Guru brought fully into the machines — ask + capture — shipped end-to-end across 5 phases, live + pushed (Tate-Tracker HEAD `194e18f`; Worker `5ca657a6`).** Plan + full trail: `.plans/2026-07-07-garden-guru-machines.md`. Expert reviews: `.ux-reviews/2026-07-07-*` + `.engineering/2026-07-07-*`. Root cause was a real 7/3 refusal (KV `conversation:mr55wd27-sommb`) that turned Paul away twice — on the ask AND the log.

### What shipped
- **Phase 0** — cleared a 3-day-stale digest (plants+fishing had drifted, never redeployed); confidence-gate in `build-digest.py` now flags everything `!= "verified"` (was only inferred/tbd — latent bug).
- **Phase 2** — **specs-vs-know-how**: machine SPECS come only from the digest ("not logged — check the manual"); general KNOW-HOW (cold-start, hold-vs-tap) gets answered plainly. REGISTER reframed "two voices to toggle" → "one caretaker's range." Refusal rule: decline the actual question, never answer an easier adjacent one. **No classifier** (experts unanimous — the fused real message is the argument against routing).
- **Phase 3** — **log machine notes from the conversation**: "Note this on the [DR-Z]" fence → `resolveVehicleByName` (refuses to guess between the two Suzukis) → `fnSaveNoteOnVehicle` writes the reader's VERBATIM words to the private ObservationStore tagged `vehicleId` (NOT vehicles.json — PII/public-repo). Renders on the vehicle card under **"field notes — to sort"**; Paul promotes keepers into `restoration[]` by hand. "Desert Storm" nickname added to the DR-Z.
- **Phase 4** — machine answers render distinctly (`<!--register:machine-->` → `.ui-turn-machine` shop-note styling, Mom-legible); unconfirmed-spec hedge moved to a leading non-droppable token; **new `tools/check-digest-fresh.py`** drift alarm wired into the session-start ritual (so the Phase 0 staleness can't recur silently).
- **Phase 5** — 11 principles distilled into the ux + engineering libraries (in `~/.claude/`, **uncommitted**).

### ⚠️ Owner: Paul
1. **Phone-verify the loop** (device-only): ask *"hold or tap the starter on a cold start?"* (know-how answer), *"what oil does the lawnmower take?"* (spec or honest "not logged"), then *"log that as a backlog item on the DR-Z"* → lands on the vehicle card under "field notes — to sort."
2. **Phase 5 principle libraries** are uncommitted in `~/.claude` — commit them? And engineering-partner promoted *"widen the ask → implied the log"* to a **full** cross-project principle despite single-occurrence — demote to candidate, or keep?

### Deferred (in the plan, revisitable)
On-card per-vehicle input (ask-then-log made it unneeded), a "which one?" disambiguation chip (name-only fallback covers the rare ambiguous case), a notes-lister CLI for un-promoted notes.

## Pickup point — last session ended 2026-07-06

**Fishing granularity Passes 1–3 — shipped end-to-end and LIVE on GH Pages (Tate-Tracker HEAD `128aa74`, pushed).** Plan `~/.claude/plans/imperative-growing-platypus.md`; UX blueprint `.ux-reviews/2026-07-06-fishing-section-reorg.json`; journey `.user-research/2026-07-06-fishing-decision-journey-and-patterns.md`. The governing "glance & the repository" principle was written to CLAUDE.md this arc.

### What shipped (Pass 3, on top of the Pass 1+2 engine)
- **Fishing promoted to its own top-level card** (`#card-fishing`), right after Wildlife — removed from the Wildlife tab row + `switchWildlifeTab`. Fronted by a **full-width dashboard Fishing tile** (verdict + operative window), driven by the same engine as the card (`buildFishingDays`/`fishingVerdict` — one engine, tile & card can't disagree).
- **Internals reordered to the A–G IA:** A NOW (verdict on top + live *station* read, pressure-led, measured-vs-modeled legible) → B TODAY → C LOOK AHEAD → D SEASON (one quiet modeled line) → E/F PREP → seam → G REFERENCE (species tabs/phase arc · season strip + temp chart · regs · lake badge).
- **One-engine fix:** `renderFishSpecies` now drives its "NOW" marker from `speciesPhaseFor()` — exactly one season-aware phase, agreeing with the top verdict (killed the multiple-NOW bug).
- **Post-ship refinements (this session, with Paul live):** verdict copy rebuilt from the window's tier so words match the ●●● rating ("**Prime window at dusk**", not "worth a run"); **Look Ahead grouped by day** = best 2–3 good windows/day, **capped at the best 4 days**, with a **"Rest of the week"** note giving each unshown day a *why* (weather cause like "heavy rain — blown out" vs. "also good — just below the top days").
- Deleted dead Pass-2 helpers (`updateSolunarWindows`, `windowRank`, `goWord`, `dayPressureVerdict`, `rainRunoffScoreForDay`). Browser-verified 0 JS errors throughout; release note added.

### Owner: Paul — live review on phone
Take a look at the Fishing card + tile on the real device. Two knobs if anything reads off: the Look Ahead **day cap is 4** (one-char change to 3), and the day-ranking picks *strongest* days (can look non-consecutive, e.g. skip Fri for Sat — honest but worth an eyeball).

### Watch-items (deferred, not bugs)
- In-season the air-temp-derived `estimateLakeTemp` can read below the month's climatological floor, tripping "still warming" with a flat progression (placeholder/live-air artifact, pre-existing Pass-1 model — not Pass 3).
- `rainRunoffScore` proxies rain for both water *level* and *clarity*, which can diverge (logged in the plan; don't fix unless asked).
- `MEMORY.md` is ~22.7KB, near the 24.4KB read limit — wants a compaction pass sometime.

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
- `~/.claude/handoff/master-plan-2026-05-21.md` W2.5 section — P1–P8 (Option A) + C1–C3 (Option C) decisions
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

## Governing design principle — the glance and the repository (2026-07-06)

The single most important structural principle for Fernwood. It came out of the 2026-07-06 fishing-section rework, corroborated independently by a ux-expert audit and a user-researcher journey. Every rich domain (plants, fishing, wildlife, weather, vehicles) must be layered this way, not flattened.

**Three strands:**

1. **The glance (decision layer).** A small, foregrounded, near-horizon read that answers "what's relevant to me *right now*?" — usually decision-shaped, driven by the freshest, most-localized data available. *Worth noticing this week* (plants), *is it a good time to fish today/tomorrow* (fishing). This leads. It is a **curated, time-relevant projection of** the repository, never a competing source.

2. **The repository (reference layer).** The deep, researched backing — care calendars, species phase tables, regs, historical temps, the full body of hyper-local research — held **in the parent card** as an on-demand store. It must exist (it's the credibility, and the depth a keen user drills into) but must **not flood the reader by default.** When a surface feels overwhelming, the answer is **relocate depth, don't delete it**: surface the near-horizon decision, shelve the rest one level down.

3. **The loop (invite + fold back) — the flywheel.** The glance is also the moment to **invite the one input only someone at the property can give.** Pair a fresh localized signal with a calm, timely call-to-action for ground-truth, and **visibly fold that truth back in.** The honest-uncertainty flag is the hook: the place we admit "~65°F, *estimated*" is exactly where we invite "log the real reading." This is the moat — anyone can show a grid forecast; only *this* property's accumulated ground-truth can't be commodity-matched, and it only accrues if the glance keeps inviting it. The virtuous cycle: **fresher local data → better glance → more trust → more input → fresher local data.** (This operationalizes the Phase-G "observations as a knowledge layer" thread with a concrete trigger.)

**Disciplines the loop must respect:** capture stays deterministic / **AI-free** (the invitation is on the ask-path; the logged reading is the user's verbatim ground-truth, see [[feedback_no_ai_on_capture]]); calm, not naggy (a field-journal *"seen it yet?"*, contextual + timely, **never a standing "add data" button** — that's the affordance-without-signal trap, see [[feedback_defer_affordances_pending_signal]]); and **close the loop visibly** (the user must see their reading replace the estimate or move the recommendation, or it feels extractive).

**Two ordering mechanisms** sit underneath this (promoted to `~/.claude/design-principles/cross-project.md`, 2026-07-06): **Freshness sets altitude** (order a surface by how live/local/actionable each signal is; position encodes recency) and **Source-hierarchy drives layout** (rank sources by evidence × freshness × actionability, and let that ranking drive presentation — for Fernwood: on-site station → forecast → season/phase-as-context → invisible research plumbing).

**Trust is the load-bearing emotion** (a confidently-wrong model is worse than an honestly-unsure one): keep *measured* signals visually distinct from *modeled* ones, and estimates legibly estimates at every altitude.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd ~/Developer/Tate-Tracker
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

1. ~~**Husqvarna riding mower:** model sticker~~ ✅ **RESOLVED 2026-07-12 — it's a Husqvarna Z254F zero-turn (54"), read off the deck sticker; consistent with the Kawasaki FR691V engine already on file.** (Still open: the primary mower-belt P/N — first digits were worn illegible.)
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
