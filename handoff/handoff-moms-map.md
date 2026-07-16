# Handoff: Mom's map (Fernwood)

<!-- generated 2026-07-16 10:13 AM EDT · sources: /Users/paulkirschenbauer/Developer/Tate-Tracker@4cb3f83 · RECEIVER: verify shas vs HEAD before trusting any status below -->

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

**W0 (basemap) is next after W1 — and it BLOCKS W2 mechanically.** Do not let anyone draw zones
before it: vertices are fractional coords *of the basemap image*, so replacing the image moves
every polygon.

## 4. State & pointers

- **Repo:** `/Users/paulkirschenbauer/Developer/Tate-Tracker` @ `4cb3f83`
- **⚠️ 2 commits are UNPUSHED and deliberately so** (`4385fd6`, `4cb3f83`) — held pending
  **W-PRIV** (below). Do not push without Paul's call.
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

- **Green light required.** Paul explicitly held execution. Confirm before touching code.
- **Do not push.** W-PRIV is unresolved (see field 8).
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
- **The whole feedback record is Paul's memory.** Her verbatim is gone. The user-researcher
  flagged the relay as the weakest evidence in the analysis, and specifically that the
  ownership reading hangs on the emphasis on *she* selects the photo — the least verifiable
  token in a paraphrase. A competing read fits every datum: *she wants the record to be right
  and is agnostic about who fixes it.* Same feature, opposite bet.
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

**⚠️ W-PRIV — needs Paul, blocks push:**
`.user-research/persona-mom.md` **+ 19 other research files are tracked in the PUBLIC repo**
`github.com/PAlekxK/Tate-Tracker` — Mom's reading difficulty, her age, behavior analysis,
engagement history. The 2026-07-16 docs land in the same tracked dirs. Precedent suggests this
was accepted or never noticed; given the VIN `filter-repo` history, it deserves a deliberate
call. Options: accept · move Mom-personal research to `.private/` + purge history · keep
committing but stop pushing these dirs. **Until Paul rules: committed locally, never pushed.**

**Verified-deterministic (safe to rely on):** the four-stream 7/15 emptiness · the
`isConfigured()` gate chain · 24/26 `zoneId: null` · 18/26 stock photos · no `<img>` in the
MomQueue block · the basemap's macOS notification + 2015 oblique provenance · 6/8 zones `draft`
· the 15 idempotent `confirmed` events on "Fairway meadow" · `property.json.propertyZones` is
still the placeholder stub.
