# Fernwood — backlog

**Single source of truth for Fernwood backlog statuses.** When any other doc (CLAUDE.md fragments, memory, design docs) disagrees, **this file wins** and the stale source should point here. First consolidated 2026-07-13; **re-organized into two tracks 2026-07-17** (intent-first rationalization — spec: `.plans/2026-07-17-backlog-rationalization.md`).

**Why two tracks (2026-07-17):** Fernwood carries **two products in one repo** — **Mom's field journal** (Track A: Mom-facing, field-journal tone, the whole W-series arc, plants/wildlife/weather/map) and **Paul's fleet & equipment tracker** (Track B: Paul-facing, utilitarian, deadline-bearing). Different users, tone, cadence, and definition of "done." They're split so each is legible on its own terms and the Mom arc doesn't read as accretion. Track C is cross-cutting infra/doctrine. **Shared reference** (KILLED / SHIPPED / reconciliation) is at the bottom.

**Status taxonomy:**
- **SHIPPED** — live in production (GH Pages + Worker).
- **ACTIVE** — being worked right now, or a live measurement phase.
- **DEFERRED** — decided-not-now; each carries the **gate** that would unblock it.
- **IDEATION** — raised, not yet designed or decided.
- **KILLED / SUPERSEDED** — abandoned or folded into something else.

The dated **"Pickup point"** trail was archived to `PICKUP-LOG-ARCHIVE.md` (2026-07-17) — it's history, not status. Read status here.

---

# TRACK A — Mom's field journal

*Intent: a hyper-personal field journal that helps Mom see and record what only she can know from standing on the ground — and gets more trustworthy the more of her ground-truth it folds back in. Glance → repository → loop. Capture stays deterministic and AI-free; AI lives only on the ask path, behind Paul's gate.*

## A1 · The engagement keystone — measure before you build ⭐

*Intent: the whole track is gated HERE. Does Mom actually engage? Nothing downstream ships until the signal fires — a **non-gimme answer AND a later-day return**. n=2 is one episode, not validation.*

| Item | What it is | Gate / next |
|---|---|---|
| **Mama's Perspective — validation gate** | Mom answered her **first 2 confirms** (7/13, both Yes → folded to canon). The loop was then **automated end-to-end** (7/14, full-panel design): harvest → serve → answer → read → assisted-fold → visible provenance chip (guess→"confirmed on the ground") + reseed, guardrails (cap 5), AI-boundary doctrine. Live queue now 5 varied cards (variety + bloom + a reflective "armchair" card). Loop spec: `CLAUDE.md` "Mama's Perspective" section; tools: `harvest-questions.py`, `fold-answer.py`, `read-mom-feedback.py`, `reinline.py`. | **Grow** = Mom answers a *non-gimme* (a "Not quite"/"Not yet") AND returns on a *later day* (user-researcher's V1+V2) → then build the deferred surface + AI log-summarizer. **Kill** = `offered`+`viewed`, zero `tapped` → dead affordance. Watch `momqueue_offered/viewed/tapped/answered` + `firstOfferedAt` latency. n=2 is one episode, not validated — don't over-scale. |
| **Zone-journey front door + funnel** | The position-1 front-door card → accessible one-zone voice walk → the existing AI-free recorder. **✅ v1 SHIPPED + LIVE 2026-07-17** (`b52ce03`; leads with Eastern Patio). Design + hypotheses: `.user-research/2026-07-17-zone-journey-panel-synthesis.md` (five-lens panel). "Trackable/automated" = a **hypotheses & signals register (H1–H5)** wired to a `flowId` funnel on `/api/metrics` + the **4-week time-box**. | **Read tool (`read-mom-funnel.py`) is the fast-follow** — events accrue now; the tool makes H1–H5 legible before the 4-week readout. Same Grow/Kill posture as the confirm-queue gate above. **v2 (gated on v1 lift):** the map-highlight, the richer journey, the off-device summarizer seat. |
| **W1** ✅ | **Fix capture** — open write-only `POST /api/feedback` (Paul's chosen auth model, 2026-07-16); await the POST, ack only on 2xx; durable outbox (replays her 7/15 words off the MacBook for free); a dark device must announce itself; `people.json` attribution is invalid (Paul shares his phone with her). | **✅ SHIPPED + LIVE 2026-07-16** (`33541bf`). Worker deployed; Pages serving it. **Verified end-to-end on the real origin:** a never-paired browser on `palekxk.github.io` POSTs to the Worker → `{"stored":1}` → ack reads "Noted — it's in the record. ✓". Worker properties (curl): unpaired POST 200; replay of the same id → `duplicate:true`, no double-write; GET still 401; 9KB → 413. Client (headless Chromium): offline → queued copy + words held; reload → replays + drains; send *and* disk both failing → honest failure copy, claims nothing, her text survives the ack timer. Baked `FEEDBACK_ENDPOINT` was required and unplanned: `cfg()` needs a token AND a url, so a dark device had nowhere to POST. **⚠️ Pages did not rebuild on the push** (served the 7/14 bundle for ~45 min); an **empty commit** re-triggered it and it went live in 60s. If a Fernwood change ever seems not to land, check `curl -s <pages-url>/viewer.html \| grep -c feedbackOutbox` before assuming the code is wrong. |

## A2 · The record about her place

*Intent: make the record about HER ground — her zones, her plants, her own photos of her own individuals — not a stranger's stock species photo.*

| # | Item | Status |
|---|---|---|
| **W2** | **Zones — Paul draws, she reconciles.** Paul walked them with her; he's sure; he draws (not relitigated). Tag each `heard-from-her` vs `paul-inferred`. Fix the `property.json.propertyZones` placeholder-stub SSOT break. **Demote the confirm button** — ask *"which of these is wrong?"*: a confirm cannot surface an omission, and her base rate is 2-for-2 Yes. The disagreement UI **already exists** (built May, never pointed at her). | **🟢 UNBLOCKED — Paul draws.** Schema v2 shipped + Worker deployed. Open Property card → **+ Add a place** → tap → name. 8 zone **names/ids survive** (`zoneId` refs) with **geometry cleared** — the v1 polygons were welded to the oblique 2015 image and are unsalvageable (git has them). **Then: assign `zoneId` on plants** (24/26 are null) — Paul's "most important part". **✅ 7 zones drawn + synced to canon 2026-07-17** (durable in git HEAD + KV, 7 geometries): Pond Area · Stable Grounds · Eastern Patio (Paul: *replaces* the old Eastern Garden placeholder) · Western Garden · Fairway Fringe · Lower 40 · Upper-Uber Wall Area. **Undrawn/reserved:** Fairway (holds the `fairway-turf` plant ref — draw later) · Parking Bank. **✅ Reconciliation DONE 2026-07-17** (`646d57e`+`c5e5e07`): renamed the 4 `-2` ids → canonical, dropped 6 empty ghosts (eastern-garden, pond-area-3, + 4 same-name empties); 55 vertices preserved exactly (verified via assertions before writing). Canon = **9 zones** (7 drawn: pond-area, stable-grounds, eastern-patio, western-garden, fairway-fringe, lower-40, upper-uber-wall-area · 2 reserved-empty: fairway, parking-bank). Plant refs valid: `fairway-meadow`→`fairway-fringe` now has geometry; `fairway-turf`→`fairway` awaits the fairway being drawn. Written via `/api/zone-save` (atomic KV + git + viewer re-inline), local pulled, `check-data-inline` clean. **→ NEXT: assign `zoneId` on the 24 null plants** (Paul-driven; the W2 payoff). Drawing-tool fix shipped same day (hollow scale-compensated vertex markers, `e3eeeed`). |
| **W3** ✅ | **"What's growing here?" — voice, not text.** Tap a zone → 🎤. Her constraint is *text*, not speech (22 A/A+ events). **Store the audio, not the transcript** (Web Speech mangles the nicknames we're mining for). Wire the existing `createVoiceCapture` to every free-response field. Map to position 1, time-boxed 4 weeks, **no wizard/counter/progress**. | **✅ CAPTURE SHIPPED 2026-07-17** — tap a zone → **🎤 "What's growing here?"** → her verbatim voice stored, AI-free. Backend: new **write-only, no-token, DURABLE** `/api/zone-audio` (mirrors the /api/feedback W1 doctrine so an unpaired device still captures; unlike /api/audio-upload's 1-hr TTL, which would delete her words before Paul heard them; blobs in token-gated KV, **never git** — repo is public). Reuses `createAudioCapture` (parameterized idle emoji/label). Honest ack: saves only on 2xx, else "couldn't save — try again" (no false success; audio too big for a localStorage outbox). Review: `tools/read-mom-zone-audio.py`. Worker deployed + curl-verified end-to-end. **The schema/instance-model gate is sidestepped for capture** (store audio, don't assign zoneId — folding stays Paul's off-device call). **→ front-door v1 SHIPPED 2026-07-17 (see A1).** |
| **W6** | **⭐ The instance model — the photo is an IDENTITY KEY (Paul's correction, 2026-07-16).** She wants **her own photos of her own plants** so it's unambiguous **which individual** we mean — there can be **multiples of the same plant across zones, or several in one zone**. Not sentiment, not ownership: a stock species photo is useless *by definition*. **This breaks the schema:** `plants.json` is **species-level** (26 records); reality is **instance-level** (variant × zone × count × her photo of *that* individual). So `zoneId` on a species record is incoherent where a species spans zones — **the 24/26 nulls may be partly a schema failure, not missing data** — and her 7/13 "yes, 'Lucifer'" answered for the *species* when the crocosmia may not all be Lucifer. Precedent already straining: the hydrangea hub-and-roster. **Needs its own path-eval; do NOT quietly widen `plants.json`. Reframes W3:** "what's growing here?" is not a lookup against the 26 — it's an inventory that doesn't exist yet. | IDEATION — blocks the deep "inventory against the 26" work (NOT the audio capture, which sidesteps it) |
| **W4** | **Photos on confirm cards** (her ask #4). Interim rule: **don't ask what you can't show.** Consider re-opening the two 7/13 answers folded to canon off photoless photograph-questions. | GATED on W3 photo path |
| **W0** | **Replace the basemap.** ~~Google Earth screenshot, macOS notification in the sky, oblique, March 2015.~~ | **✅ DONE 2026-07-16** (`b321060`). Now **NAIP 2022-01-10** — leaf-off, nadir, 1500×1500 @ 1.0 ft/px, no chrome, **public domain** (Esri may NOT be redistributed — that killed the Esri candidate; NAIP's leaf-off capture gives the same "see everything" legally). Georeference recorded in `_meta.bounds` + a `.bounds.json` sidecar. |
| **W2-SCHEMA** | **⭐ Vertices are now real WGS84 `[lon, lat]`; the basemap is a swappable VIEW** (schema v2, `b321060`). This is what makes the coming redraw the **last** one: a better basemap (newer NAIP, Paul's own drone ortho) is a **re-registration** (update `_meta.baseImage` + `bounds`), never a redraw. Verified: property anchor projects to frac **[0.5000, 0.5000]**; lon/lat→frac→lon/lat round-trips with **zero** error. 🚨 Fixed a latent data-destroyer first: `sanitizeZone` ran `clamp01()` on every vertex — fine for fractions, but a coordinate collapsed to `[1,0]` (image corner) while the Worker returned **200** and the chip said "live everywhere" — **third in the 7/15 bug family**. Now **rejects** out-of-envelope instead of clamping. Also de-hardcoded **4** coupling sites (incl. a CSS `aspect-ratio` that would have landed every tap offset from where polygons draw) and gave `ZONES_DATA` its first drift alarm. | **✅ DONE** |
| **Property map — zone-naming completeness pass** | The interactive zone map is **shipped** (lives at the top of the Property card, pan/zoom, tap/confirm). What's left is naming/populating the remaining zones + per-candidate `zoneAffinity`. | Paul's zone-naming pass. *(NB: the map surface itself is SHIPPED — the old "paused, don't build" note is stale.)* |
| **Plants-to-consider gaps** | GFC 2026-27 seedling catalog (~Jul 1), UGA nursery list refresh, TACF, HRI, Mt. Cuba genera. | Time/source-gated. |

**Drawing-tool refinements (from Paul's 2026-07-17 draw session — 7 zones drawn):**
1. **Vertex markers occlude the space being defined.** ~~They render at `r=16` SVG units *inside* the zoomed canvas, so at 6× zoom a marker is ~96px — it blocks the very ground you're trying to trace around.~~ ✅ Fixed 2026-07-17 (`e3eeeed`): hollow, scale-compensated (`r = k / scale`) markers.
2. **Basemap pixelates on zoom.** NAIP base is 1500×1500 native (~0.6 m/px sensor limit); `MAX_SCALE=6` magnifies ~10× past real detail → interpolation mush. No more true detail exists to show. Interim: cap/tune zoom so it can't over-magnify into blur. Durable: a sharper basemap — **Esri z19 (`base-esri-z19-wide.webp` already on disk) becomes usable once W-PRIV makes the repo private + Worker-served** (Esri can't be redistributed publicly), or Paul's future drone ortho. ⭐ Because vertices are now real WGS84 (W2-SCHEMA), a sharper basemap is a **re-registration, not a redraw** — today's 7 zones survive the upgrade.

## A3 · The loop (invite + fold back)

*Intent: the flywheel — pair a fresh localized signal with a calm, timely invitation for the one ground-truth only Mom can give, and fold it back visibly. **Gated on A1 proving the loop is wanted.** The three bloom/reaction items below are MERGED here (were separate DEFERRED rows) — they are one intent.*

| Item | What it is | Gate |
|---|---|---|
| **"is it open yet?" bloom ground-truth loop** | Invite + fold back ground-truth on bloom timing (the flywheel's concrete trigger). | Part of the loop; Mama's Perspective now carries the first bloom confirm (panicle hydrangea). Gated on A1. |
| **Bloom in "Worth noticing today" glance** | Surface bloom state in the top glance. | After de-crowding the "Peak this week" area. Gated on A1. |
| **Fairway / change-reactions confirm** | "Does the hub match the property?" reaction-to-a-change question (the Mama's Perspective schema already supports `kind: react`). | After confirms prove engagement; phrase as an observable, not a design review. Gated on A1. |
| **Phase G — observations as a knowledge layer** | Field notes feed other surfaces ("you noted the laurel opening April 25 last year — watch for it now"); the loop/flywheel's non-assistant surfaces. | Phase E proven **and** observation set ~50+ entries. |

## A4 · Don't overwhelm her — the solicitation-stack IA

*Intent: hold the line on input surfaces. The cure for sprawl is the defer-affordances doctrine, not more items. **Run the IA pass on A1 signal — not before.***

| # | Item | Status |
|---|---|---|
| **W8** | **⭐ Justify the whole top-of-app solicitation STACK** (Paul, 2026-07-17 — raised as v1 of the front-door card was going in). We are about to have THREE+ stacked solicitation surfaces at the top: the new **pinned front-door card** (W3) + the **carousel confirm cards** (Mama's Perspective) + the **free-response boxes** (composer + general feedback, W5). Each shipped for a good local reason; together they risk a wall of "give us input" for a reader who reads with difficulty. **Do NOT let this accrete silently** — at a deliberate point (once the front-door card is live + we have a little signal), run an **intentional IA pass**: does each surface earn its place, what's the hierarchy, can any consolidate? Pairs with **W5** (the boxes) + **W7** (confirm-card buttons) — this is the umbrella they both sit under. Design/IA, not a quick fix. | IDEATION — umbrella over W5 + W7; revisit once front-door has signal |
| **W5** | **The three boxes.** All three live in one `<section class="unified-input">`; the note + general field are the **same CSS class** 120px apart; composer and feedback toggle ask **the same sentence**. A label can't carry it for someone who reads with difficulty — **the disambiguator is a person**: *"Something to tell Paul about the app?"* **↑ Paul re-raised 2026-07-17 (direct-from-Mom, past feedback he's carried):** the general app-feedback box must be **clearly labeled and impossible to lose** — explore making it a **persistent side / expand-out button** rather than a third stacked box, so it never gets buried under the confirm cards. Pairs with **W7**. | AFTER W1 |
| **W7** | **Confirm-card button layout + the per-card "Add a note" question** (Paul, 2026-07-17, from the live screenshot). The confirm card stacks **Looks right / Not quite** then **Ask me later** then a dashed **+ Add a note** — Paul: the **button positioning is awkward**, and there are **too many text-entry surfaces** scattered across the app. **Open question:** does a **per-card "Add a note"** earn its complexity for a reader who reads with difficulty, or should note-adding funnel to the ONE general box (see W5) so we don't have notes-per-card *and* a general field competing? Design-only, no build; **feeds the position-1-card work** (it lives in this same carousel + input stack). | IDEATION — pairs with W5 |

## A5 · Get her off the public internet

*Intent: Mom is on the public internet; the repo leaks her. Decided; execute when Paul does the Cloudflare/Pages-plan work.*

| # | Item | Status |
|---|---|---|
| **W-PRIV** | **⚠️ Get Mom off the public internet — DECIDED 2026-07-16: repo private + serve `viewer.html` from the Worker.** Measured: **146 tracked files** name her, and **the served `viewer.html` mentions her 99×** in inline comments (design commentary, reading difficulty, behavior reads) — view-source reads it all, so repo-private alone does NOT fix it. **🚨 MUST RUN AFTER W1:** Pages and Workers are **different origins** and localStorage is origin-bound — migrating first would **permanently destroy her lost 7/15 words** (`tateTracker.momQueue.general.v1` on her MacBook) plus every device's answered-set, text-size pref, token, and PWA. **⚠️ Check first: Pages on a private repo needs a paid plan** — flipping to private on free takes Fernwood dark for Mom instantly. Purging does **not** unring the bell (public for months; SHA-reachable until GC; forks/caches persist). | **DECIDED — gated on W1 (✅ done); ready to execute on Paul's Cloudflare work** |
| **W-PRIV-PW** | **"A super simple password on Fernwood" (Paul's idea, 2026-07-16) — RIGHT IDEA, WRONG LAYER (today).** A client-side password on GH Pages is **theater**: verified 2026-07-16 that the repo is `visibility: public` and `raw.githubusercontent.com/PAlekxK/Tate-Tracker/main/viewer.html` returns **200 to anyone** — **155 lines of the served file mention her**. A JS prompt gates the *UI*; it cannot gate *bytes GitHub already hands out*, so nobody would ever meet the prompt. Same failure shape as the 7/15 bug: **feels like protection, verifies nothing.** **But the idea is sound one layer down** — a password only means anything where a **server** decides what to send, which is exactly W-PRIV's "serve `viewer.html` from the Worker." Once there, a shared secret is cheap and real. **Two constraints when it's built:** (1) **don't make Mom type it** — she reads with difficulty; use a long-lived signed cookie / magic link so she meets it approximately never; (2) it does **not** unring the bell (public for months; forks/caches/SHA-reachable). **Folds into W-PRIV — do not build separately.** | **IDEATION — gated on W-PRIV** |

## A6 · Guru & capture infra

*Intent: keep the assistant + capture path healthy. **Tool-use migration is the nearest real trigger — the digest is AT the ceiling now.***

| Item | What it is | Gate |
|---|---|---|
| **Tool-use migration** ⚠️ | Move Garden Guru off system-prompt digest-stuffing to tool-use. | digest >80K **or** observations >50. ⚠️ **digest is ~80K NOW — at the ceiling.** The closest-to-triggering item in the whole backlog; treat as near-term, not "someday." |
| **Streaming responses** | Stream Guru replies (~30 lines client). | If turns feel laggy on LTE. |
| **Conversation browse UI** | UI to browse KV-stored conversations. | v2 want. |
| **Durable photo-in-note** | Persist photos in saved notes (stripped for iOS quota). | Needs own scoping; mirror the audio_ref server-blob pattern. |
| **Phase H — audio identification** | Bird/sound ID; built end-to-end then hidden (👂 button `hidden`). | A mature free/single-vendor audio-ID path **and** a Mom-usage signal. |
| ~~**Guru re-inline verification (root-cause fix)**~~ | ✅ **ROOT-CAUSED + FIXED 2026-07-16** (`2adab8d`). The cause was the **GitHub Contents API's 1 MB cliff**: above 1 MB it returns HTTP 200, `encoding:"none"`, and an **empty** content string — no error — so `ghGetFile` handed back a successful-looking `""` and every re-inline found nothing to replace. **`viewer.html` crossed 1 MB on 2026-07-02 in `23ac94f` — "Garden Guru Phase 3: add and remove a plant from conversation."** The commit that shipped the add/remove write path is the commit that broke it; the feature disabled itself on arrival. **Lizard's Tail (7/05) was this.** The 7/06 verification (`d1da306`) detects the symptom but could never succeed — its verify read is the same broken call. Blast radius: all four viewer re-inline sites — promote-species, its verify, remove-species, zone-save — i.e. **Guru's whole write-to-canon path was dead for two weeks.** Fix: fall back to the **Blob API** (100 MB ceiling) when content is empty but size > 0. Verified live: contents → 0 bytes; blob → all 1,235,806; zone-save now `{"ok":true}`. ⚠️ **Watch:** `viewer.html` grows every session — the Blob API's ceiling is 100 MB, so there's headroom, but this is the second ceiling this file has silently hit. | **DONE** |

**Track-A KILLED (don't revive without new evidence):** the **24-row editable plant table** — all five experts rejected it as an **invalid instrument** (a null result can't distinguish "doesn't want ownership" from "can't read a table," but would read as the first and retire her one unprompted ask on a rigged test; ⭐ precedent: 0 uses / 104 sessions). The gap view is **Paul's** `tools/` script, not her surface. Also killed: **EXIF→zone auto-placement** (no georeference; and don't automate the highest-ownership moment in the plan); **baking the God-token** into the public deploy; **AI-for-drudgery** (AI-at-scale is what *produced* the 18 stock photos — "24 is your number, not hers").

**Doctrine amendments forced (proposed, unapplied):** retire **"open feedback → DON'T BUILD"** (she asked for it unprompted; her direct ask outranks the 7/13 panel inference) · the **AI boundary should be a *provenance* rule, not a model rule** (the stock photos + generic guides came from **zero AI calls** — the harm arrived by a route the rule doesn't cover) · `feedback_defer_affordances_pending_signal` — **this is the signal** that gate was waiting for.

---

# TRACK B — Fleet & equipment (Paul-facing)

*Intent: a precise, deadline-aware record of Paul's vehicles + equipment — what's owed, what's been done, what's still unknown. Different user (Paul), tone (utilitarian, high-precision), and cadence than Track A. Began as one "Vehicles card"; now a co-equal system.*

## B1 · Live obligations (deadline-bearing — the only clock-bearing items in the whole backlog)

*Intent: things with a real-world deadline. **Surfaced into the backlog 2026-07-17 from the session log** (they were only in the pickup-point trail + the session anchor) so archiving the log doesn't bury them. Owner: Paul.*

| Item | What it is |
|---|---|
| **GTI + Bolores registrations — OVERDUE** | GA registrations were due **June 3** (Paul's b-day); late penalty accruing. **GTI** needs a **2026 emissions test → then renew**; **Bolores** just renews (1989 = emissions-exempt). |
| **GTI 90k / DSG service + coolant verify** | DSG overdue at **82,698**; coolant reframed to "verify at next shop visit" (no verdict). Bundle the coolant dye/pressure check + brake-pad check into the next **Autobahn/DSG** or spare-key **dealer** trip — no special trip. |
| **GTI spare key — dealer booking** | Dealer job (~**$450–500** all-in; MQB Comfort-Access, locksmiths can't). Spec confirmed off Paul's own key: **FCC NBGFS12P01 / VW 5G0 959 752 BE**. Phone-vet + book; bundle with the **Jim Ellis Chamblee** recall trip. |

## B2 · The record

*Intent: the accumulating history + running needs per machine.*

| Item | What it is | Gate / next |
|---|---|---|
| **Vehicle records — rest of the fleet** | Extend the shipped GTI service-records pipeline to the Bronco's bigger paper pile, then others. | Agent-can-drive. |
| **Bronco door-panel repair** | Paul's stated "next big project"; guide + verified buy-list ready, panel is out of the truck. | Physical work, owner: Paul. |
| **Receipt-mining residuals** | Bolores ChatGPT-mining `CANDIDATE-ROWS.md` verify queue (cigarette-USB, BT-music flakiness, spare-tire bushings) + the Gmail/Amazon receipt de-dupe-and-fold (`.private/EMAIL-RECEIPTS.md` → `AMAZON-PARTS.md`). | Agent-can-drive; a few `[CONFIRM]` install-status flags need Paul. |
| **Off-machine backup target (R2 vs Google Drive)** | The only unbuilt piece of service-records durability. | Paul's decision; Apple Photos is the interim second copy. |
| **Per-vehicle mileage/hours + last-service anchors** | Add anchors to all 15 assets. | Needs Paul's odometer/service readings. |
| **Tiguan / F-150 profile enrichment** | Fill the near-empty vehicle profiles. | Needs Paul's history input. |
| **Guru-machines deferred bits** | On-card per-vehicle input; "which one?" disambiguation chip; notes-lister CLI. | ask-then-log made them unneeded; revisit on signal. |

## B3 · Data collection (was CLAUDE.md "Outstanding for Paul")

*Intent: specific facts to read/collect off the machines. **Folded here 2026-07-17** from CLAUDE.md's "Outstanding for Paul" list — read + update it here now.*

1. ~~**Husqvarna riding mower:** model sticker~~ ✅ **RESOLVED 2026-07-12 — it's a Husqvarna Z254F zero-turn (54"), read off the deck sticker; consistent with the Kawasaki FR691V engine already on file.** (Still open: the primary mower-belt P/N — first digits were worn illegible.)
2. **Homelite trimmer:** confirm UT33650A (straight shaft) vs UT33550A (curved shaft) — middle digit on EPA sticker is slightly ambiguous.
3. **Homelite blower/vac:** no model sticker found on the unit. Maintenance specs are inferred from the trimmer's engine family (HHCPS.0264AT). Acceptable for at-a-store reference.
4. **Annual: NASA SVS Dial-a-Moon visualization ID** — when SVS publishes the 2027 visualization (usually Dec/Jan), update the `DIAL_A_MOON_VIZ` constant in viewer.html (`year`, `parent` bucket, `id`). Find the new ID at svs.gsfc.nasa.gov/gallery/moonphase. Until refreshed, the moon hero hides cleanly once the year flips.
5. **Bolores paint codes — door-label photos:** Paul to send pics of the driver-door Vehicle Certification Label (EXT PNT + INT TR fields) to confirm the two-tone + interior codes. Researched candidates already in `vehicles.json` flagged `researched-pending-label`: upper = Medium Cabernet Red **2H / M6156**, lower = Light Chestnut **9T / 6190** (rule out Dark Chestnut); interior Chestnut is a TRIM code, not a paint M-code. Flip to `verified` once the label is read.
6. **GTI — confirm exact mileage:** anchored at ~81k from Paul's estimate (2026-06-28). Read the odometer next drive and update `gti-2016` `mileage` + the spark-plug/DSG/carbon framing if it's off. *(NB: 82,698 recorded 7/11 from the Express Oil invoice — reconcile.)*
7. **Tiguan paint color code:** read the VW data sticker (spare-wheel well under the trunk floor, or driver door jamb) before buying touch-up paint for the new "Paint touch-up" step — the touch-up has to match.
8. ~~**GTI spare key — own-key spec**~~ ✅ **RESOLVED 2026-07-14 (and it CORRECTED the assumption).** Paul read the FCC ID off his own working fob → **FCC NBGFS12P01 / VW 5G0 959 752 BE family / 315 MHz / MQB48 / HU66 / CR2025** (2015-19 MK7 GTI Comfort-Access flip key; web-verified). This is a **different, newer generation** than the card's prior `5K0 837 202 AK` / `NBG010206T` spec (which came from the Facebook Marketplace keys — the WRONG generation for this car). Card corrected; source any spare to **NBGFS12P01 / 5G0 959 752**, not the 5K0.
9. **Marietta dealer name:** verify it's still "Volkswagen of Marietta" when calling — the old "Jim Ellis VW Marietta" listing reads closed (possible rebrand/ownership change). Recorded under the current name in `gti-2016` `serviceContacts`.

## B4 · Photo layer

| Item | What it is |
|---|---|
| **Photo-library vehicle/repair-photo miner** | Mine the ~50K-photo library for per-vehicle machine + teardown shots; propose-then-confirm. **NB:** since prototyped — now its own project (`~/Developer/photo-miner/`, memory `project_photo_miner`). Effectively ACTIVE there, not a Fernwood-repo item. The `photo-seed.json` (68 Bolores truck images) is the standing seed to feed it. |

---

# TRACK C — Cross-cutting / infra / doctrine

*Intent: things that serve both products or the meta-stack.*

| Item | What it is | Gate |
|---|---|---|
| **Worker deploy automation — arm the secret** | GitHub Action `.github/workflows/deploy-worker.yml` is built + runs green, skipping the deploy until armed. **One-time: add repo secret `CLOUDFLARE_API_TOKEN`** (Cloudflare → API Tokens → "Edit Cloudflare Workers"; GitHub → repo Settings → Secrets → Actions). After that, Worker changes self-deploy on push. | Owner: Paul (token work). |
| **Citizen-science scaffolding** | Dormant code in viewer.html. | Paul's call: re-enable / drop / leave dormant. |
| **Batch document-mining playbook** | Generalize the triage→characterize→verify→fold receipt-mining pattern cross-project. | Until a 2nd project needs it. |
| **Expert-proposed principles (candidates)** | "reuse the mechanism, not the semantics"; "match structure to the reader's unit of meaning"; "widen the ask → implied the log". | Paul demote/keep call. |

---

# SHARED REFERENCE

## Recently shipped

**2026-07-17 — Zone-journey front door v1.** Position-1 launcher card + one-zone voice walk (leads with Eastern Patio) + the `flowId` funnel. Live (`b52ce03`).

**2026-07-14 — Plant look-fors → Plants tile.** The day's top *plant* look-fors lead the always-visible Plants tile as tappable "👀 Worth a look" rows; tapping routes to the composer pre-filled to log what she sees. Top-two, priority-led (narrow bloom/prune windows lead; routine turf only when nothing more urgent). One engine (`gatherPlantLookForCandidates`). Also: unified-input close-outs — button relabeled "Save & ask the Almanac"; fixed the conversation-open layout shuffle (Mama's Perspective stays pinned, composer + button stay together).

**2026-07-13 — Worker deploy automation** (built, awaiting the `CLOUDFLARE_API_TOKEN` secret — now Track C). **Save/Ask → ONE button "Save & ask the Almanac"** (log-first, then Garden Guru; `bc2cfff`) — writes her verbatim entry first (deterministic, AI-free, always succeeds), then fires Guru best-effort. Closes the 7/3 failure; **resolves the 2026-07-05 "Save/Ask two-button split" question** (hierarchy → one log-first button). Preserves [[feedback_no_ai_on_capture]].

## SHIPPED (the built base these build on)

Mama's Perspective (Mom confirm queue, 2026-07-13) · Unified input — one "Save & ask the Almanac" button, log-first (7/13; collapsed the 5/20 Save/Ask split; relabeled 7/14) · The Almanac card (5/21) · Garden Guru Phase E conversational layer (5/19) + redesign Phases 1–3 (7/02) + into-the-machines (7/07) · Phase D capture rebuild (5/19) · Phase F image input → auto-promote (5/21) · Concept A "Today + Reference Drawer" / computeLookFors (7/05) · structured `peakDates` (7/06) · Fishing granular + dynamic, own card (7/06) · Plants bloom-time + Hydrangea hub (7/12) · **Property zone map** in the Property card (interactive, 5/28) · Vehicles "what she needs" restoration list (6/12) + "what she's had done" service-records pipeline (7/09) + per-step tap-to-call contacts (6/28) + registration reminders (7/11) + manuals corpus (7/08) · Metrics capture (5/20) · analyze-fernwood.py (5/21) · Sources card (5/21) · Worth Considering candidates card (5/26) · drift-check tools + deploy-worker.sh · cross-device zone sync fix (5/28) · storage-quota / sanitize-at-boundary fix (5/26) · Mom no-glasses a11y · W1 capture-that-cannot-lie (7/16) · W0 NAIP basemap (7/16) · W2 zones drawn + reconciled to 9 (7/17) · W2-SCHEMA WGS84 vertices (7/16) · W3 zone-audio capture (7/17) · zone-journey front door v1 (7/17).

## KILLED / SUPERSEDED

| Item | Resolution |
|---|---|
| **⭐ "this matters" star** | KILL — 0 uses / 104 revisits; revisit frequency *is* her curation. (Still in code; retire on next touch.) |
| **Seeded prompts** | Deprecate — 0 usage; a standing control she doesn't operate. |
| **🚩 open-feedback / standing "leave feedback" box** | DON'T BUILD — "the star all over again." General feedback lives as the one quiet foot-line in Mama's Perspective + out-of-band to Paul. *(See W5/W8 — Mom's direct ask for a clearly-labeled feedback field is reopening this; her ask outranks the panel inference.)* |
| **Emailed Mom discovery interview** | DEAD — sent 5/29, refreshed 6/20+6/21, never returned; device + usage replaces it (the reframe behind Mama's Perspective). |
| **"prompt Mom for input" weed seed** | SUBSUMED into Mama's Perspective. |
| **Comprehensive UI/UX overhaul** | Dropped — let evidence commission targeted passes, not a speculative overhaul. |
| **Phase D classify-on-save** | Removed (kept dormant) — no-AI-on-capture principle. |
| **Classifier for machine-spec routing** | Rejected — the fused real message argues against routing. |
| **Weather Underground PWS (KGAJASPE279)** | Killed as a data source — the on-site Ambient Weather station is the sole source. Don't reintroduce. |
| **Two-box architecture (separate Field Notes + Garden Guru)** | Superseded by the unified input surface. |
| **Name "When you're out there"** | Superseded → **"Mama's Perspective"** (Paul's steer). |
| **Text-path plant-add (standing button)** | Don't ship — Paul-want, no Mom-signal; if ever built, funnel back to the photo path. |
| **Save/Ask two-button split (7/05 open question)** | RESOLVED 2026-07-13 — collapsed to one log-first "Save & ask the Almanac" button (hierarchy, not removal). |

## Reconciliation notes

**2026-07-17 (the two-track rationalization):**
- **Fernwood is two products in one repo** (Mom's journal + Paul's fleet tracker) — split into Track A / B so the Mom arc reads clearly and the fleet sub-system isn't interleaved through it. Spec: `.plans/2026-07-17-backlog-rationalization.md`.
- **Folded in:** CLAUDE.md's "Outstanding for Paul" (9 items) → **B3**; the CLAUDE.md "Backlog — raised 2026-07-05" fragment (all shipped/resolved) → pointer; "Backlog — Mom engagement SHIPPED" → pointer.
- **Merged:** the three loop items (bloom "is it open yet?" + bloom-in-glance + Fairway/change-reactions) + Phase G → **A3** (one intent).
- **Elevated:** Tool-use migration (digest AT the 80K ceiling now) → visible in **A6**; the GTI/Bolores live obligations (only deadline-bearing items) → **B1** (surfaced from the session log before archiving it).
- **Archived:** the dated pickup-point trail + the Phases-D/E/F/G roadmap prose → `PICKUP-LOG-ARCHIVE.md`.

**2026-07-13 (first consolidation):**
- **Mama's Perspective shipped, but three "authoritative" docs still said HELD / not-a-queue.** Paul steered the panel's "single confirm probe" into a navigable, continuously-populatable **queue** and it shipped the same day (git `a888ebb`). **Ground truth = code + RELEASE_NOTES + git HEAD.** CLAUDE.md + the memory index updated to SHIPPED; the dated design docs are left as historical point-in-time artifacts.
- **Property map** — code check confirmed it's SHIPPED (live in the Property card), not "paused." Only a zone-naming completeness pass remains (A2 above).
- **Photo-library miner** — CLAUDE.md said "not started"; it was since prototyped and moved to its own repo (`~/Developer/photo-miner/`). Tracked there now (B4).
