# Handoff: Mom's map (Fernwood)

<!-- generated 2026-07-16 10:31 AM EDT · sources: /Users/paulkirschenbauer/Developer/Tate-Tracker@f63d77e · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission

Execute the **W1 capture fix** for Fernwood — and nothing else — on Paul's green light. Mom's
7/15 feedback was silently destroyed by the app; until capture is honest, nothing about her
engagement is measurable and no other workstream is worth starting.

## 2. Read first

1. **`~/.claude/plans/stateless-growing-hopcroft.md`** — the whole plan (W-PRIV, W0–W5), the
   verified facts, the killed ideas. **This is the primary. Read it before anything.**
2. **`BACKLOG.md` → `## 🔴 ACTIVE — Mom's map`** — the SSOT status table. (Fernwood rule:
   BACKLOG.md wins over CLAUDE.md pickup-points for status.)
3. **`.user-research/2026-07-16-mom-feedback-relay.md`** — what she asked for + the root-cause
   evidence. Note its provenance header: it is **Paul's recollection, not her words.**

Do NOT read the 10 panel docs unless a specific decision needs re-litigating — the plan already
carries their conclusions. Their trail is listed at the bottom of the plan.

## 3. Next steps (ordered)

**Gate: do not start until Paul says go.** He asked for the plan to be recorded and held.

1. **W1.1 — Worker.** `worker/worker.js` **already contains this edit** (committed `4385fd6`):
   unauthenticated `POST /api/feedback` ahead of the auth gate, rate-limited 20/IP/5min via KV
   (fail-OPEN), 8KB cap; `GET` still token-gated. Review it, don't rewrite it.
2. **W1.2 — `viewer.html`.** `postFeedback()` (~`:8697`) must stop gating on `isConfigured()`,
   **await** the POST, and return success. `sendGeneral()` (~`:8682`) and `answer()` (~`:8848`)
   ack **only on a real 2xx**. Fix `showAck` (~`:8862`) doing `host.innerHTML = ""`
   unconditionally — it would make the failure copy's "your words are still here" a lie.
   Exact copy: `review/2026-07-16-ownership-surface-voice.md`. **Ship the landed + failed acks
   only.**
3. **W1.3 — Outbox.** Durable localStorage queue; replay on load + after failure. `ANSWERED_KEY`
   must not retire an answer that never landed. **Only after this exists** may the queued/offline
   ack from step 2 ship — it asserts a mechanism that doesn't exist yet.
4. **W1.4 — Dark-device banner.** `isConfigured() === false` must announce itself on load and
   never fake a ✓.
5. **W1.5 — `tools/people.json`.** Don't re-guess the mapping. Record that device attribution is
   invalid (Paul shares his phone with Mom) and stop reading engagement from it.
6. **Release note + re-inline + deploy.** Per `CLAUDE.md`: add a `RELEASE_NOTES.md` entry, run
   `python3 tools/build-release-notes.py`, then `tools/deploy-worker.sh` **with the Bash sandbox
   disabled** (see `[[reference_fernwood_worker_deploy]]`).

7. **Confirm her 7/15 words landed.** The outbox should upload them from her MacBook on next open.
   Check with `python3 tools/read-mom-feedback.py`. **This gates W-PRIV** (see below).

**Then W-PRIV, then W0.** Do not reorder — see the two hard constraints in field 5.

## 4. State & pointers

- **Repo:** `/Users/paulkirschenbauer/Developer/Tate-Tracker` @ `f63d77e` (+ this brief's own commit)
- **⚠️ ALL commits from 2026-07-16 are UNPUSHED and deliberately so** (`4385fd6`, `4cb3f83`,
  `f63d77e`, …) — held pending **W-PRIV**. **Do not push without Paul's call**; a push sends this
  session's Mom docs to the public repo, which is the exact problem W-PRIV exists to fix.
- **Nothing is deployed.** The Worker edit is committed but inert until `wrangler deploy`.
- Worker: `https://tate-tracker.paul-kirschenbauer.workers.dev` · token `.private/fernwood-token`
  (header is `X-Tate-Token`, **not** Bearer) · read her answers with
  `python3 tools/read-mom-feedback.py`
- Key line numbers (verify against HEAD): `viewer.html:13149` `isConfigured()` · `:13232` metrics
  flush gate · `:8697` postFeedback · `:8691` the unconditional ack · `:14929` `createVoiceCapture`
  · `:15042` `UnifiedVoice` · `:4803` the one-section three-textarea problem · `:3703`
  `.mom-queue-correction`
- Basemap (W0): `images/property-map/gep-2015-03-leafoff.webp`. Candidates already on disk:
  `images/property-map/aerial-esri-z17..z19.jpg`, `naip/`, `tools/fetch-aerial.py`.

## 5. Guardrails

### 🚨 Two hard constraints — read these before touching anything

**1. NEVER migrate the origin before W1 ships and her words are recovered.**
`palekxk.github.io` and `*.workers.dev` are **different origins**; localStorage is origin-bound.
Her MacBook's `tateTracker.momQueue.general.v1` is **the only surviving copy of her 7/15 feedback**.
Serving from the Worker first makes it **unreachable forever** — and takes every device's
answered-set, A/A+ text-size pref, token config, and installed PWA with it. Order is forced:
**W1 → confirm her words landed → localStorage migration script (must run on the OLD origin) →
Worker serving → repo private → purge.** Reversing this solves the privacy problem by destroying
the evidence the whole thread exists to recover.

**2. Check the GitHub plan tier BEFORE touching repo visibility.**
Pages on a private repo needs Pro/Team. **Flipping to private on a free account takes Fernwood
dark for Mom instantly, with no warning.** If there's no Pro, the Worker migration must land first.

### Standing
- **Green light required.** Paul held execution. Confirm before touching code.
- **Do not push.** W-PRIV is decided but unshipped (see field 8).
- **Do not widen `plants.json` to fake instance-level data.** The species-vs-instance break (W6)
  is a real schema decision needing its own path-eval — see the plan's identity-key section.
- **Do not build the 24-row plant table.** Five experts killed it as an *invalid instrument*.
  If it resurfaces, read the plan's "Killed" section before re-arguing.
- **Do not automate zone assignment** (no EXIF→zone: no georeference exists) and do not
  AI-generate her content. The AI boundary holds: *AI never touches Mom's surface or her words.*
- **Capture stays deterministic and AI-free** ([[feedback_no_ai_on_capture]]).
- **Do not ship the offline/queued ack before the outbox exists.**
- Fernwood is a **field journal, not a task manager** — no urgency/alert language, no counters,
  no progress bars on her surfaces.
- `git pull --rebase` first: a weather bot pushes to this repo ~4×/day ([[project_fernwood_weather_bot]]).

## 6. Done when

An **unpaired browser** (fresh profile, no token) can submit general feedback and:
(a) the Worker returns 2xx, (b) the record is visible via `tools/read-mom-feedback.py`, (c) the
ack she sees is true. Then: airplane-mode → queued ack → reconnect → it replays. Then: break the
URL → honest failure ack, her text still on screen.

**The tell that it really worked:** Mom's lost 7/15 words upload themselves the next time she
opens Fernwood on her MacBook, with no instructions given to her.

## 7. Un-sealed judgment

- **The MacBook root cause is established by ELIMINATION, not positive proof.** An unconfigured
  device is invisible *by construction* — it cannot be positively confirmed. Every competing
  hypothesis is dead (metrics flushed fine on 7/15 and gate on the same `isConfigured()`, so
  token-loss-on-a-paired-device is out; no unknown device appears because it can't) and Paul
  independently said she was on her MacBook. It fits perfectly. It is still inference.
- **~~The ownership-vs-agnostic debate~~ — RETIRED 2026-07-16 by Paul, do not reopen.** Two rounds
  of panel speculation (mine: "she wants to own the data"; the researcher's: "she wants the record
  right, agnostic about who fixes it") were **both wrong**, and it was never a paraphrase artifact.
  **The photo is an IDENTITY KEY**: she wants her own photos of her own plants so it's unambiguous
  **which individual** we mean — there can be multiples of the same plant across zones or several in
  one zone. Functional, not sentimental. A stock species photo fails *by definition* — it cannot
  point at *that* hydrangea. **This breaks the schema (W6, species-level vs instance-level) and
  reframes W3.** See the plan's identity-key section before designing anything.
- **The relay is still Paul's memory** on the *other* three asks (labeled feedback field, three
  boxes, photos on cards) — her verbatim is gone. Weight accordingly; but #1 is now settled
  by Paul directly.
- **Unresolved, worth watching:** the panel's "one card at a time" alternative *is* the queue
  already shipped (n=2). The rebuttal — that it ran under a dark device, photoless cards, and two
  gimme questions, so it never really ran — is mine, and Paul hasn't ruled on it.
- **Paul plans to try manual recovery** of her words off the MacBook when he next sees her ("may
  not be a few days"). Not blocking; the outbox may beat him to it.

## 8. Trust status (per open item)

**Human-cleared (Paul's calls, 2026-07-16):**
- Auth model — open write-only `POST /api/feedback`. Chosen explicitly over a baked write-token
  and over fixing pairing.
- **He draws the map.** He walked the zones with her specifically; "100% sure." Settled — do not
  reopen.
- Always offer free-response + voice dictation on her surfaces.
- Skip blocking on MacBook recovery.

**Model-flagged, NOT cleared — treat as proposals, not facts** ([[feedback_agent_proposals_not_validated]]):
- Every panel recommendation across both rounds (W0 sequencing, demoting the confirm button,
  store-audio-not-transcript, map-to-position-1, the 4-week time-box).
- The reading that she's engaging rather than feature-shopping.
- The claim that the basemap has been setting the ceiling on zone work (a correlation: the only
  2 `confirmed` zones are the only 2 legible features — suggestive, not proven).
- The doctrine amendments in the plan (retire "open feedback → DON'T BUILD"; make the AI boundary
  a provenance rule). **Proposed, unapplied.**

**⚠️ W-PRIV — DECIDED 2026-07-16, gated on W1, blocks push:**
Paul: *"keep all the info about mom out of public accessibility."* **Chosen: repo private + serve
`viewer.html` from the Worker** — Fernwood is a two-person family app and doesn't need a public URL.
Measured exposure: **146 tracked files** name her, and **the served `viewer.html` mentions her 99×**
in inline comments (design commentary, her reading difficulty, behavior reads, panel findings) —
**view-source reads all of it, so repo-private alone does NOT fix it.**
**Sequencing is forced by the origin/localStorage landmine — see field 5, constraint 1.**
**Honest limit:** this has been public for months. Force-pushed commits stay SHA-reachable until
GitHub's GC, forks/clones keep what they took, search engines may have cached the Pages site.
**The purge stops the bleeding; it does not guarantee retrieval — do not tell Paul it's erased.**
`filter-repo` runbook from the 2026-06-12 VIN purge: `tools/SCHEDULING.md`.

**Verified-deterministic (safe to rely on):** the four-stream 7/15 emptiness · the
`isConfigured()` gate chain · 24/26 `zoneId: null` · 18/26 stock photos · no `<img>` in the
MomQueue block · the basemap's macOS notification + 2015 oblique provenance · 6/8 zones `draft`
· the 15 idempotent `confirmed` events on "Fairway meadow" · `property.json.propertyZones` is
still the placeholder stub.
