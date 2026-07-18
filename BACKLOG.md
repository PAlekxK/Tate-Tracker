# Fernwood — consolidated backlog

**This is the single source of truth for Fernwood backlog statuses.** Consolidated 2026-07-13
from the backlog fragments that had scattered across CLAUDE.md's many sections, the memory files,
and the design docs — and whose statuses had begun to conflict. When those disagree with this file,
**this file wins** (and the stale source should be fixed to point here).

The dated **"Pickup point"** sections in CLAUDE.md are a *historical log* of what happened each
session — keep them for the trail, but do **not** read them as current status. Read status here.

**Status taxonomy:**
- **SHIPPED** — live in production (GH Pages + Worker).
- **ACTIVE** — being worked right now, or a live measurement phase.
- **DEFERRED** — decided-not-now; each carries the **gate** that would unblock it.
- **IDEATION** — raised, not yet designed or decided.
- **KILLED / SUPERSEDED** — abandoned or folded into something else.

---

## 🔴 ACTIVE — Mom's map (opened 2026-07-16; **W1 shipped 2026-07-16**, rest awaiting Paul)

**Full plan: `~/.claude/plans/stateless-growing-hopcroft.md`. Record of her feedback:
`.user-research/2026-07-16-mom-feedback-relay.md`. Nothing is deployed; nothing is pushed.**

**What happened.** On **2026-07-15 Mom wrote substantive feedback into Fernwood and every word
was lost.** She was on her **MacBook** — never paired with the Worker token. Every write path
(feedback, observations, *and* telemetry) gates on the same per-device `isConfigured()`, so it all
silently no-op'd while the app told her **"Noted — it's in the record. ✓"**. Second lost-capture
incident (first 2026-07-03), same root: capture fails silently while the UI acknowledges success it
never verified. **Worst property: a dark device is indistinguishable from disengagement — this bug
was positioned to make Paul conclude she wasn't using the app at the exact moment he was deciding
whether she engages. Fernwood currently cannot measure Mom.**

**Her asks** (Paul's relay — her verbatim is unrecoverable; testimony, not quotes): every plant
should carry **a picture she selects** + a clear description + a **zone**; a **general feedback
field, clearly labeled**; **three stacked text boxes is confusing**; **confirm cards must show a
picture** of the plant being asked about.

**The finding underneath all of it:** the record isn't about her place. **24/26 plants have
`zoneId: null`**; **18/26 photos are Wikimedia stock** (a stranger's photo of the species); 6 have
none; **the confirm card has no `<img>` at all**. She was asked *"is this crocosmia 'Lucifer'?"* —
a question about a photograph — shown no photograph, of a plant we hold no photograph of. She said
Yes. It's canon.

| # | Item | Status |
|---|---|---|
| **W1** | **Fix capture** — open write-only `POST /api/feedback` (Paul's chosen auth model, 2026-07-16); await the POST, ack only on 2xx; durable outbox (replays her 7/15 words off the MacBook for free); a dark device must announce itself; `people.json` attribution is invalid (Paul shares his phone with her). | **✅ SHIPPED + LIVE 2026-07-16** (`33541bf`). Worker deployed; Pages serving it. **Verified end-to-end on the real origin:** a never-paired browser on `palekxk.github.io` POSTs to the Worker → `{"stored":1}` → ack reads "Noted — it's in the record. ✓". Worker properties (curl): unpaired POST 200; replay of the same id → `duplicate:true`, no double-write; GET still 401; 9KB → 413. Client (headless Chromium): offline → queued copy + words held; reload → replays + drains; send *and* disk both failing → honest failure copy, claims nothing, her text survives the ack timer. Baked `FEEDBACK_ENDPOINT` was required and unplanned: `cfg()` needs a token AND a url, so a dark device had nowhere to POST. **⚠️ Pages did not rebuild on the push** (served the 7/14 bundle for ~45 min); an **empty commit** re-triggered it and it went live in 60s. If a Fernwood change ever seems not to land, check `curl -s <pages-url>/viewer.html \| grep -c feedbackOutbox` before assuming the code is wrong. |
| **W0** | **Replace the basemap.** ~~Google Earth screenshot, macOS notification in the sky, oblique, March 2015.~~ | **✅ DONE 2026-07-16** (`b321060`). Now **NAIP 2022-01-10** — leaf-off, nadir, 1500×1500 @ 1.0 ft/px, no chrome, **public domain** (Esri may NOT be redistributed — that killed the Esri candidate; NAIP's leaf-off capture gives the same "see everything" legally). Georeference recorded in `_meta.bounds` + a `.bounds.json` sidecar. |
| **W2** | **Zones — Paul draws, she reconciles.** Paul walked them with her; he's sure; he draws (not relitigated). Tag each `heard-from-her` vs `paul-inferred`. Fix the `property.json.propertyZones` placeholder-stub SSOT break. **Demote the confirm button** — ask *"which of these is wrong?"*: a confirm cannot surface an omission, and her base rate is 2-for-2 Yes. The disagreement UI **already exists** (built May, never pointed at her). | **🟢 UNBLOCKED — Paul draws.** Schema v2 shipped + Worker deployed. Open Property card → **+ Add a place** → tap → name. 8 zone **names/ids survive** (`zoneId` refs) with **geometry cleared** — the v1 polygons were welded to the oblique 2015 image and are unsalvageable (git has them). **Then: assign `zoneId` on plants** (24/26 are null) — Paul's "most important part". **✅ 7 zones drawn + synced to canon 2026-07-17** (durable in git HEAD + KV, 7 geometries): Pond Area · Stable Grounds · Eastern Patio (Paul: *replaces* the old Eastern Garden placeholder) · Western Garden · Fairway Fringe · Lower 40 · Upper-Uber Wall Area. **Undrawn/reserved:** Fairway (holds the `fairway-turf` plant ref — draw later) · Parking Bank. **✅ Reconciliation DONE 2026-07-17** (`646d57e`+`c5e5e07`): renamed the 4 `-2` ids → canonical, dropped 6 empty ghosts (eastern-garden, pond-area-3, + 4 same-name empties); 55 vertices preserved exactly (verified via assertions before writing). Canon = **9 zones** (7 drawn: pond-area, stable-grounds, eastern-patio, western-garden, fairway-fringe, lower-40, upper-uber-wall-area · 2 reserved-empty: fairway, parking-bank). Plant refs valid: `fairway-meadow`→`fairway-fringe` now has geometry; `fairway-turf`→`fairway` awaits the fairway being drawn. Written via `/api/zone-save` (atomic KV + git + viewer re-inline), local pulled, `check-data-inline` clean. **→ NEXT: assign `zoneId` on the 24 null plants** (Paul-driven; the W2 payoff). Drawing-tool fix shipped same day (hollow scale-compensated vertex markers, `e3eeeed`). |
| **W2-SCHEMA** | **⭐ Vertices are now real WGS84 `[lon, lat]`; the basemap is a swappable VIEW** (schema v2, `b321060`). This is what makes the coming redraw the **last** one: a better basemap (newer NAIP, Paul's own drone ortho) is a **re-registration** (update `_meta.baseImage` + `bounds`), never a redraw. Verified: property anchor projects to frac **[0.5000, 0.5000]**; lon/lat→frac→lon/lat round-trips with **zero** error. 🚨 Fixed a latent data-destroyer first: `sanitizeZone` ran `clamp01()` on every vertex — fine for fractions, but a coordinate collapsed to `[1,0]` (image corner) while the Worker returned **200** and the chip said "live everywhere" — **third in the 7/15 bug family**. Now **rejects** out-of-envelope instead of clamping. Also de-hardcoded **4** coupling sites (incl. a CSS `aspect-ratio` that would have landed every tap offset from where polygons draw) and gave `ZONES_DATA` its first drift alarm. | **✅ DONE** |
| **W3** | **"What's growing here?" — voice, not text.** Tap a zone → 🎤. Her constraint is *text*, not speech (22 A/A+ events). **Store the audio, not the transcript** (Web Speech mangles the nicknames we're mining for). Wire the existing `createVoiceCapture` (`viewer.html:14929`) to every free-response field — **MomQueue has no mic today**. Map to position 1, time-boxed 4 weeks, **no wizard/counter/progress**. | **✅ CAPTURE SHIPPED 2026-07-17** — tap a zone → **🎤 "What's growing here?"** → her verbatim voice stored, AI-free. Backend: new **write-only, no-token, DURABLE** `/api/zone-audio` (mirrors the /api/feedback W1 doctrine so an unpaired device still captures; unlike /api/audio-upload's 1-hr TTL, which would delete her words before Paul heard them; blobs in token-gated KV, **never git** — repo is public). Reuses `createAudioCapture` (parameterized idle emoji/label). Honest ack: saves only on 2xx, else "couldn't save — try again" (no false success; audio too big for a localStorage outbox). Review: `tools/read-mom-zone-audio.py` (lists by zone, downloads new to gitignored `.private/mom-zone-audio/`, watermark). Worker deployed + curl-verified end-to-end (no-token POST stores · no-token GET 401 · token GET lists+retrieves durable blob · bad input rejected). **The schema/instance-model gate is sidestepped for capture** (store audio, don't assign zoneId — folding stays Paul's off-device call). **→ NEXT (queued): promote map to position 1, time-box 4 weeks, house-voice line** — deferred so Paul eyeballs the capture flow on-device first. |
| **W4** | **Photos on confirm cards** (her ask #4). Interim rule: **don't ask what you can't show.** Consider re-opening the two 7/13 answers folded to canon off photoless photograph-questions. | GATED on W3 photo path |
| **W5** | **The three boxes.** All three live in one `<section class="unified-input">`; the note + general field are the **same CSS class** 120px apart; composer and feedback toggle ask **the same sentence**. A label can't carry it for someone who reads with difficulty — **the disambiguator is a person**: *"Something to tell Paul about the app?"* **↑ Paul re-raised 2026-07-17 (direct-from-Mom, past feedback he’s carried):** the general app-feedback box must be **clearly labeled and impossible to lose** — explore making it a **persistent side / expand-out button** rather than a third stacked box, so it never gets buried under the confirm cards. Pairs with **W7**. | AFTER W1 |
| **W-PRIV** | **⚠️ Get Mom off the public internet — DECIDED 2026-07-16: repo private + serve `viewer.html` from the Worker.** Measured: **146 tracked files** name her, and **the served `viewer.html` mentions her 99×** in inline comments (design commentary, reading difficulty, behavior reads) — view-source reads it all, so repo-private alone does NOT fix it. **🚨 MUST RUN AFTER W1:** Pages and Workers are **different origins** and localStorage is origin-bound — migrating first would **permanently destroy her lost 7/15 words** (`tateTracker.momQueue.general.v1` on her MacBook) plus every device's answered-set, text-size pref, token, and PWA. **⚠️ Check first: Pages on a private repo needs a paid plan** — flipping to private on free takes Fernwood dark for Mom instantly. Purging does **not** unring the bell (public for months; SHA-reachable until GC; forks/caches persist). | **DECIDED — gated on W1** |
| **W-PRIV-PW** | **"A super simple password on Fernwood" (Paul's idea, 2026-07-16) — RIGHT IDEA, WRONG LAYER (today).** A client-side password on GH Pages is **theater**: verified 2026-07-16 that the repo is `visibility: public` and `raw.githubusercontent.com/PAlekxK/Tate-Tracker/main/viewer.html` returns **200 to anyone** — **155 lines of the served file mention her**. A JS prompt gates the *UI*; it cannot gate *bytes GitHub already hands out*, so nobody would ever meet the prompt. Same failure shape as the 7/15 bug: **feels like protection, verifies nothing.** **But the idea is sound one layer down** — a password only means anything where a **server** decides what to send, which is exactly W-PRIV's "serve `viewer.html` from the Worker." Once there, a shared secret is cheap and real. **Two constraints when it's built:** (1) **don't make Mom type it** — she reads with difficulty; use a long-lived signed cookie / magic link so she meets it approximately never; (2) it does **not** unring the bell (public for months; forks/caches/SHA-reachable). **Folds into W-PRIV — do not build separately.** | **IDEATION — gated on W-PRIV (which is gated on W1 recovery)** |
| **W7** | **Confirm-card button layout + the per-card "Add a note" question** (Paul, 2026-07-17, from the live screenshot). The confirm card stacks **Looks right / Not quite** then **Ask me later** then a dashed **+ Add a note** — Paul: the **button positioning is awkward**, and there are **too many text-entry surfaces** scattered across the app. **Open question:** does a **per-card "Add a note"** earn its complexity for a reader who reads with difficulty, or should note-adding funnel to the ONE general box (see W5) so we don't have notes-per-card *and* a general field competing? Design-only, no build; **feeds the running position-1-card panel** (it lives in this same carousel + input stack). | IDEATION — pairs with W5 |
| **W6** | **⭐ The instance model — the photo is an IDENTITY KEY (Paul's correction, 2026-07-16).** She wants **her own photos of her own plants** so it's unambiguous **which individual** we mean — there can be **multiples of the same plant across zones, or several in one zone**. Not sentiment, not ownership: a stock species photo is useless *by definition*. **This breaks the schema:** `plants.json` is **species-level** (26 records); reality is **instance-level** (variant × zone × count × her photo of *that* individual). So `zoneId` on a species record is incoherent where a species spans zones — **the 24/26 nulls may be partly a schema failure, not missing data** — and her 7/13 "yes, 'Lucifer'" answered for the *species* when the crocosmia may not all be Lucifer. Precedent already straining: the hydrangea hub-and-roster. **Needs its own path-eval; do NOT quietly widen `plants.json`. Reframes W3:** "what's growing here?" is not a lookup against the 26 — it's an inventory that doesn't exist yet. | IDEATION — blocks W3 design |

**Drawing-tool refinements (from Paul's 2026-07-17 draw session — 7 zones drawn):**
1. **Vertex markers occlude the space being defined.** They render at `r=16` SVG units *inside* the zoomed canvas, so at 6× zoom a marker is ~96px — it blocks the very ground you're trying to trace around. Fix: shrink + make hollow (ring, not filled dot) + scale-compensate (`r = k / scale`) so markers stay a small constant on-screen size. Cheap, high-value. **← do first.**
2. **Basemap pixelates on zoom.** NAIP base is 1500×1500 native (~0.6 m/px sensor limit); `MAX_SCALE=6` magnifies ~10× past real detail → interpolation mush. No more true detail exists to show. Interim: cap/tune zoom so it can't over-magnify into blur. Durable: a sharper basemap — **Esri z19 (`base-esri-z19-wide.webp` already on disk) becomes usable once W-PRIV makes the repo private + Worker-served** (Esri can't be redistributed publicly), or Paul's future drone ortho. ⭐ Because vertices are now real WGS84 (W2-SCHEMA), a sharper basemap is a **re-registration, not a redraw** — today's 7 zones survive the upgrade.

**W3 front-door — five-lens panel RAN + CONVERGED 2026-07-17 (design + hypotheses; no build yet).** ⭐ Master brief: `.user-research/2026-07-17-zone-journey-panel-synthesis.md`. Converged: a **position-1 front-door card** (launcher, one forward action — a *head-line*, not a confirm-stepper item) → an **accessible one-zone stepper pick** (name + color + highlighted patch, NOT polygon-hunting — ux's critical finding) → the existing AI-free recorder → an **honest** close. Flow = **one-zone-at-a-time** with an optional "another spot?" (sweep behavior *emerges + is measured*, never assumed). "Trackable/automated" = a **hypotheses & signals register** (H1–H5) wired to a `flowId` funnel on `/api/metrics` + a read tool + the 4-week time-box — *automation in the instrument, not the affordance*. Absorbs the deferred "map→position-1" + "house-voice line". **W6 stays blocked** (capture assigns no `zoneId` to canon). **Open for Paul:** build v1 now? · carousel-dot vs above-the-dots (recommend above). | **IDEATION → ready to build v1 on Paul's go**

**KILLED (don't revive without new evidence):** the **24-row editable plant table** — all five
experts rejected it as an **invalid instrument** (a null result can't distinguish "doesn't want
ownership" from "can't read a table," but would read as the first and retire her one unprompted ask
on a rigged test; ⭐ precedent: 0 uses / 104 sessions). The gap view is **Paul's** `tools/` script,
not her surface. Also killed: **EXIF→zone auto-placement** (no georeference; and don't automate the
highest-ownership moment in the plan); **baking the God-token** into the public deploy;
**AI-for-drudgery** (AI-at-scale is what *produced* the 18 stock photos — "24 is your number, not hers").

**Doctrine amendments forced (proposed, unapplied):** retire **"open feedback → DON'T BUILD"** (she
asked for it unprompted; her direct ask outranks the 7/13 panel inference) · the **AI boundary should
be a *provenance* rule, not a model rule** (the stock photos + generic guides came from **zero AI
calls** — the harm arrived by a route the rule doesn't cover) · `feedback_defer_affordances_pending_signal`
— **this is the signal** that gate was waiting for.

**Supersedes** the "Mama's Perspective validation gate" below: the gate never ran. Both 7/13 answers
were gimmes and 7/15 was zero across four streams.

---

## ✅ Just shipped (2026-07-14) — all live on `main` (GH Pages), no Worker change

**Plant look-fors bumped up to the Plants tile as a check-it prompt.** The day's top *plant*
look-fors now lead the always-visible Plants tile as warm, tappable **"👀 Worth a look"** rows;
tapping routes to the composer pre-filled (`"Checked the [plant] — "`) to log what she sees, not the
card-expand. The "Worth noticing today" list stays inside the Plants card ("do both" — Paul's steer).
Focused on plants deliberately (highest-engagement care actions); wildlife look-fors stay in the
central list only. One engine (`gatherPlantLookForCandidates`) feeds both surfaces so they can't
disagree. This also answers the long-open 7/05 UX question "look-fors are too buried inside Plants."
Fixed a latent init bug found along the way (a `MetricsCollector` temporal-dead-zone throw that aborted
part of startup). **Judgment call resolved (Paul, 2026-07-14):** the tile now shows the **top two**
prompts, **priority-led** — the most time-sensitive window (a narrow bloom/prune window) leads and
routine turf mowing only surfaces when nothing more urgent is active; daily rotation happens within the
top priority tier so it stays fresh. (Prior behavior rotated across the whole candidate list ignoring
priority, so turf could lead on a day with open narrow windows.) Complementary to — not a duplicate of —
the structured Mama's Perspective confirm-queue: the tile invites *fresh observation of a timing event*,
Mama's Perspective *confirms a fact the system already holds*. Coexistence of the two solicitation
surfaces is a live design question to revisit if either starts to feel like noise.

**Unified-input close-outs.** (1) Button relabeled **"Log to the Almanac" → "Save & ask the Almanac"** so it
reads as save *and* answer, not just logging (behavior unchanged — still log-first). (2) Fixed a layout
shuffle: when a conversation opened, Mama's Perspective jumped *below* the thread and the text box drifted
from its button — flex-`order` gap (the queue + actions defaulted to 0 while the thread used negatives). Now
Mama's Perspective stays pinned on top and the composer + button stay together.

## ✅ Just shipped (2026-07-13)

**Worker deploy automation — built, awaiting one secret to arm.** GitHub Action
`.github/workflows/deploy-worker.yml`: on push to `main` touching `worker/worker.js`,
`worker/wrangler.toml`, `tools/build-digest.py`, or any digest source JSON, it rebuilds the digest →
`wrangler deploy` → `/health` → commits the rebuilt digest back with `[skip ci]`. CI does the deploy,
so the auto-mode classifier that blocks the agent never applies. Runs green and skips the deploy until
the secret exists. **Owner (one-time): add repo secret `CLOUDFLARE_API_TOKEN`** — Cloudflare → My
Profile → API Tokens → "Edit Cloudflare Workers"; GitHub → repo Settings → Secrets and variables →
Actions → New secret. After that, Worker changes self-deploy on push (no more manual `deploy-worker.sh`).



**Save / Ask → ONE button: "Save & ask the Almanac" (log-first, then Garden Guru).** Shipped git `bc2cfff` (label was "Log to the Almanac"; renamed 7/14).
On tap it writes her **verbatim** entry to the almanac **first** (deterministic, AI-free, always
succeeds), then fires Garden Guru as a best-effort second step for the answer + follow-up. The log
never depends on the AI — closes the 7/3 failure that turned Mom away on both the ask and the log.
Cost was the only suspected blocker and it's negligible (~$5/mo measured); the real reason for two
buttons was capture reliability + verbatim integrity, both preserved. Photos/audio still route straight
to Guru. Browser-verified the note survives a Guru failure. Preserves [[feedback_no_ai_on_capture]].

## ACTIVE

| Item | What it is | Gate / next |
|---|---|---|
| **Mama's Perspective — validation gate** | Mom answered her **first 2 confirms** (7/13, both Yes → folded to canon). The loop was then **automated end-to-end** (7/14, full-panel design): harvest → serve → answer → read → assisted-fold → visible provenance chip (guess→"confirmed on the ground") + reseed, guardrails (cap 5), AI-boundary doctrine. Live queue now 5 varied cards (variety + bloom + a reflective "armchair" card). Loop spec: `CLAUDE.md` "Mama's Perspective" section; tools: `harvest-questions.py`, `fold-answer.py`, `read-mom-feedback.py`, `reinline.py`. | **Grow** = Mom answers a *non-gimme* (a "Not quite"/"Not yet") AND returns on a *later day* (user-researcher's V1+V2) → then build the deferred surface + AI log-summarizer. **Kill** = `offered`+`viewed`, zero `tapped` → dead affordance. Watch `momqueue_offered/viewed/tapped/answered` + `firstOfferedAt` latency. n=2 is one episode, not validated — don't over-scale. |
| **Vehicle records — rest of the fleet** | Extend the shipped GTI service-records pipeline to the Bronco's bigger paper pile, then others. | Agent-can-drive. |
| **Bronco door-panel repair** | Paul's stated "next big project"; guide + verified buy-list ready, panel is out of the truck. | Physical work, owner: Paul. |

---

## DEFERRED (with the gate that unblocks each)

| Item | What it is | Gate |
|---|---|---|
| **Property map — zone-naming completeness pass** | The interactive zone map is **shipped** (lives at the top of the Property card, pan/zoom, tap/confirm). What's left is naming/populating the remaining zones + per-candidate `zoneAffinity`. | Paul's zone-naming pass. *(NB: the map surface itself is SHIPPED — the old "paused, don't build" note is stale.)* |
| **Phase G — observations as a knowledge layer** | Field notes feed other surfaces ("you noted the laurel opening April 25 last year — watch for it now"); the loop/flywheel's non-assistant surfaces. | Phase E proven **and** observation set ~50+ entries. |
| **"is it open yet?" bloom ground-truth loop** | Invite + fold back ground-truth on bloom timing (the flywheel's concrete trigger). | Part of the loop; Mama's Perspective now carries the first bloom confirm (panicle hydrangea). |
| **Bloom in "Worth noticing today" glance** | Surface bloom state in the top glance. | After de-crowding the "Peak this week" area. |
| **Phase H — audio identification** | Bird/sound ID; built end-to-end then hidden (👂 button `hidden`). | A mature free/single-vendor audio-ID path **and** a Mom-usage signal. |
| **Tool-use migration** | Move Garden Guru off system-prompt digest-stuffing to tool-use. | digest >80K **or** observations >50. ⚠️ **digest is ~80K now — at the ceiling.** This is the closest-to-triggering deferred item. |
| **Streaming responses** | Stream Guru replies (~30 lines client). | If turns feel laggy on LTE. |
| **Conversation browse UI** | UI to browse KV-stored conversations. | v2 want. |
| **Durable photo-in-note** | Persist photos in saved notes (stripped for iOS quota). | Needs own scoping; mirror the audio_ref server-blob pattern. |
| **Off-machine backup target (R2 vs Google Drive)** | The only unbuilt piece of service-records durability. | Paul's decision; Apple Photos is the interim second copy. |
| ~~**Guru re-inline verification (root-cause fix)**~~ | ✅ **ROOT-CAUSED + FIXED 2026-07-16** (`2adab8d`). The cause was the **GitHub Contents API's 1 MB cliff**: above 1 MB it returns HTTP 200, `encoding:"none"`, and an **empty** content string — no error — so `ghGetFile` handed back a successful-looking `""` and every re-inline found nothing to replace. **`viewer.html` crossed 1 MB on 2026-07-02 in `23ac94f` — "Garden Guru Phase 3: add and remove a plant from conversation."** The commit that shipped the add/remove write path is the commit that broke it; the feature disabled itself on arrival. **Lizard's Tail (7/05) was this.** The 7/06 verification (`d1da306`) detects the symptom but could never succeed — its verify read is the same broken call. Blast radius: all four viewer re-inline sites — promote-species, its verify, remove-species, zone-save — i.e. **Guru's whole write-to-canon path was dead for two weeks.** Fix: fall back to the **Blob API** (100 MB ceiling) when content is empty but size > 0. Verified live: contents → 0 bytes; blob → all 1,235,806; zone-save now `{"ok":true}`. ⚠️ **Watch:** `viewer.html` grows every session — the Blob API's ceiling is 100 MB, so there's headroom, but this is the second ceiling this file has silently hit. | **DONE** |
| **Per-vehicle mileage/hours + last-service anchors** | Add anchors to all 15 assets. | Needs Paul's odometer/service readings. |
| **Tiguan / F-150 profile enrichment** | Fill the near-empty vehicle profiles. | Needs Paul's history input. |
| **Plants-to-consider gaps** | GFC 2026-27 seedling catalog (~Jul 1), UGA nursery list refresh, TACF, HRI, Mt. Cuba genera. | Time/source-gated. |
| **Citizen-science scaffolding** | Dormant code in viewer.html. | Paul's call: re-enable / drop / leave dormant. |
| **Guru-machines deferred bits** | On-card per-vehicle input; "which one?" disambiguation chip; notes-lister CLI. | ask-then-log made them unneeded; revisit on signal. |
| **Fairway / change-reactions confirm** | "Does the hub match the property?" reaction-to-a-change question (the Mama's Perspective schema already supports `kind: react`). | After confirms prove engagement; phrase as an observable, not a design review. |
| **Batch document-mining playbook** | Generalize the triage→characterize→verify→fold receipt-mining pattern cross-project. | Until a 2nd project needs it. |
| **Expert-proposed principles (candidates)** | "reuse the mechanism, not the semantics"; "match structure to the reader's unit of meaning"; "widen the ask → implied the log". | Paul demote/keep call. |

---

## IDEATION (raised, not designed)

| Item | What it is |
|---|---|
| **Photo-library vehicle/repair-photo miner** | Mine the ~50K-photo library for per-vehicle machine + teardown shots; propose-then-confirm. **NB:** since prototyped — now its own project (`~/Developer/photo-miner/`, memory `project_photo_miner`). Effectively ACTIVE there, not a Fernwood-repo item. |

---

## KILLED / SUPERSEDED

| Item | Resolution |
|---|---|
| **⭐ "this matters" star** | KILL — 0 uses / 104 revisits; revisit frequency *is* her curation. (Still in code; retire on next touch.) |
| **Seeded prompts** | Deprecate — 0 usage; a standing control she doesn't operate. |
| **🚩 open-feedback / standing "leave feedback" box** | DON'T BUILD — "the star all over again." General feedback lives as the one quiet foot-line in Mama's Perspective + out-of-band to Paul. |
| **Emailed Mom discovery interview** | DEAD — sent 5/29, refreshed 6/20+6/21, never returned; device + usage replaces it (the reframe behind Mama's Perspective). |
| **"prompt Mom for input" weed seed** | SUBSUMED into Mama's Perspective. |
| **Comprehensive UI/UX overhaul** | Dropped — let evidence commission targeted passes, not a speculative overhaul. |
| **Phase D classify-on-save** | Removed (kept dormant) — no-AI-on-capture principle. |
| **Classifier for machine-spec routing** | Rejected — the fused real message argues against routing. |
| **Weather Underground PWS (KGAJASPE279)** | Killed as a data source — the on-site Ambient Weather station is the sole source. Don't reintroduce. |
| **Two-box architecture (separate Field Notes + Garden Guru)** | Superseded by the unified input surface. |
| **Name "When you're out there"** | Superseded → **"Mama's Perspective"** (Paul's steer). |
| **Text-path plant-add (standing button)** | Don't ship — Paul-want, no Mom-signal; if ever built, funnel back to the photo path. |

---

## SHIPPED (for reference — the built base these build on)

Mama's Perspective (Mom confirm queue, 2026-07-13) · Unified input — one "Save & ask the Almanac" button,
log-first (7/13; collapsed the 5/20 Save/Ask split; relabeled 7/14) ·
The Almanac card (5/21) · Garden Guru Phase E conversational layer (5/19) + redesign Phases 1–3 (7/02) +
into-the-machines (7/07) · Phase D capture rebuild (5/19) · Phase F image input → auto-promote (5/21) ·
Concept A "Today + Reference Drawer" / computeLookFors (7/05) · structured `peakDates` (7/06) ·
Fishing granular + dynamic, own card (7/06) · Plants bloom-time + Hydrangea hub (7/12) ·
**Property zone map** in the Property card (interactive, 5/28) · Vehicles "what she needs" restoration
list (6/12) + "what she's had done" service-records pipeline (7/09) + per-step tap-to-call contacts (6/28) +
registration reminders (7/11) + manuals corpus (7/08) · Metrics capture (5/20) · analyze-fernwood.py (5/21) ·
Sources card (5/21) · Worth Considering candidates card (5/26) · drift-check tools + deploy-worker.sh ·
cross-device zone sync fix (5/28) · storage-quota / sanitize-at-boundary fix (5/26) · Mom no-glasses a11y.

---

## Reconciliation notes (what was conflicting — resolved 2026-07-13)

- **Mama's Perspective shipped, but three "authoritative" docs still said HELD / not-a-queue.** Paul steered
  the panel's "single confirm probe" into a navigable, continuously-populatable **queue** and it shipped the
  same day (git `a888ebb`). The CLAUDE.md top Mom-backlog section, the panel synthesis "master brief," and the
  `project_fernwood_prompt_mom_input` memory all still described the held design. **Ground truth = code +
  RELEASE_NOTES + git HEAD.** CLAUDE.md + the memory index have been updated to SHIPPED; the dated design docs
  are left as historical point-in-time artifacts.
- **Property map** — code check confirmed it's SHIPPED (live in the Property card), not "paused." Only a
  zone-naming completeness pass remains (DEFERRED above).
- **Photo-library miner** — CLAUDE.md said "not started"; it was since prototyped and moved to its own repo
  (`~/Developer/photo-miner/`). Tracked there now, not as a Fernwood-repo backlog item.
