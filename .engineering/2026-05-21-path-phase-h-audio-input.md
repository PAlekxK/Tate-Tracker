# Phase H — Audio identification (path-eval)

**Date:** 2026-05-21 (evening)
**Mode:** Path Evaluation (engineering-partner)
**Builds on:** `.engineering/2026-05-21-path-phase-f-image-input.md` — the Option C image flow this proposes to extend to audio.
**Status:** Pre-implementation design pass. Paul has said "let's implement Phase H"; this memo defines the design before code touches the Worker or `viewer.html`.

---

## Paul's verbatim ask

> "For the Fernwood Almanac, let's capture that we want to have a call/audio identification capability as well. Will need to be sorted out to differentiate from the voice to text in the UI."

That's the shape: photo-ID → sound-ID, riding the same Garden Guru conversation surface and the same two-step confirm + auto-promote contract Phase F just shipped. The UX disambiguation question (audio capture vs. voice-to-text) is the load-bearing one — same hardware, different intent.

---

## A. Landscape pass (the load-bearing first move)

Per `~/.claude/engineering-principles/landscape-research-before-deep-work.md` — and because this path is downstream of an assumption Paul flagged as needing verification ("the Claude API audio support exists"). Below: what the actual situation is, with sources.

### Anthropic Messages API — does it support audio content blocks?

**No. As of May 2026, the Anthropic Messages API supports text + image content blocks only.** The vision documentation at `platform.claude.com/docs/en/docs/build-with-claude/vision` lists image as the sole non-text input modality. The supported image media types are JPEG, PNG, GIF, WebP — no audio types.

There is an open feature request — `anthropics/anthropic-sdk-python#1198`, filed February 2026 — asking for an `audio` content block analogous to `image`. As of this writing the issue is still open, unassigned, with no official response from Anthropic and no timeline commitment. A user proposed a base64-as-text workaround in comments and the Anthropic engineer who responded confirmed it does not work — the model cannot perceive audio waveforms encoded as text bytes.

**That kills the "extend Phase F shape directly" path.** Phase F's elegance was that the user message just became a multi-block array with an `image` block alongside `text`, and the rest of the pipeline (cached system, Garden Guru voice, structured suggestion fence, Option C promote) flowed unchanged. With no `audio` block type, this path doesn't exist as a one-line extension.

### What does work, then?

Three viable approaches, in order of fit to Paul's project shape:

1. **Multi-model: route the audio turn through OpenAI GPT-4o Audio (or Gemini 2.5 Pro), get back a textual ID, hand that ID back to Garden Guru as a tool result.** Both models natively understand audio (not just transcribe it). Quality on non-speech sounds like bird/frog calls is unverified by either vendor, but the model has been documented as able to answer "what is in this recording?" generically. Cost shape: GPT-4o Audio inputs are ~$100/M audio tokens (roughly $0.10 per minute of audio); Gemini 2.5 Pro audio is in the same range. Concretely, a 15-sec clip = ~$0.025 per turn. *Pros:* keeps Phase F's conversational shape; Garden Guru still narrates with field-journal voice on the final reply. *Cons:* adds a second API vendor + key + cost log; quality on faint or overlapping bird calls likely worse than the specialist model below; introduces a second failure surface.

2. **Specialist model: BirdNET (Cornell).** The gold-standard open-source model for bird sound ID — 6,000+ species, MIT-licensed code, CC-BY-NC-SA model weights (research/non-commercial; family-internal dashboard qualifies). It is *the* species-ID model behind Merlin Sound ID. **But:** no hosted public REST API. Deployment options are (a) host inference yourself (Python + TensorFlow, won't fit in a Cloudflare Worker — needs a GPU or at minimum a long-running container), (b) use the TensorFlow.js browser model (BirdNET-Live PWA does this — Android-only today, "iOS coming soon" per Cornell's app page), or (c) `birdnetlib` Python on a local machine. *Pros:* best-in-class quality for birds; runs on-device when the JS model is available; free at hobbyist scale. *Cons:* birds only — no frogs, no mammals, no insects; deployment overhead is real (Worker can't host it); iOS Safari support is "coming soon," not shipped; would require Paul to stand up a separate inference path (e.g., on a Raspberry Pi at home, or a small Fly.io / Render container) just for this feature.

3. **Defer Phase H until Anthropic ships audio content blocks.** Track issue #1198. Capture the Phase H design in CLAUDE.md (already done) and pick it up when Anthropic ships, which would let the Phase F shape extend cleanly without a second vendor.

**The honest read for Paul's project:** Option 1 (multi-model via GPT-4o or Gemini) is the only path that ships Phase H *now* and matches the Phase F shape. Option 2 is best-quality-for-birds but has real deployment overhead and a scope gap (no frogs, no mammals — Mom and Paul will record both). Option 3 is the cheapest in engineering effort but loses the feature until an unknown future date.

I'd add a fourth option Paul should know about explicitly: **(4) ship the audio-capture UI now with the recording → Garden Guru link, but route the audio through OpenAI for ID, and design the audio-vendor as a swap-out — when Anthropic ships native audio, swap the call site, keep everything else.** That's Option 1 with a stated migration path. It's what I'd recommend.

### Landscape footnote — what doesn't help

- **OpenAI Whisper API.** Speech-to-text only. Designed for human language; won't classify a Wood Thrush song.
- **eBird API.** Sightings database, not audio ID.
- **Merlin Sound ID.** Consumer app only, no public API.

---

## B. Recommended path

**One cohesive design** — building on Phase F's Option C pattern, with the audio routed through OpenAI GPT-4o Audio (or Gemini, swappable) for the actual ID, then handed back to Garden Guru for the field-journal-voice narration + the existing `<!--suggest-species ... -->` fence + the two-step confirm + auto-promote flow.

| Choice | Pick | One-line why |
|---|---|---|
| 1. UX differentiation | **(a) Separate icons — 🎤 stays voice-to-text; 👂 is the new audio-ID button** | Cleanest cognitive model for Mom; preserves existing voice flow; the icon difference teaches the intent difference without copy |
| 2. Recording surface | **On the unified input, next to 🎤 + 📷** | Single input bar, three intents: photo, sound, voice (transcribe). Mom's existing model already supports two buttons next to the textarea |
| 3. Audio vendor (initial) | **OpenAI GPT-4o Audio** | Native audio understanding; pay-per-call (no infra); designed to be swapped when Anthropic ships native audio |
| 4. Pipeline shape | **Audio → Vendor ID call → Garden Guru narrative turn → existing fence + two-step confirm + auto-promote** | Reuses the Phase F flow end-to-end; vendor swap touches one function |
| 5. Encoding | **WebM/Opus, mono, 16 kHz, 8–30 sec cap** | Smallest viable for bird/frog calls; widely supported by MediaRecorder including iOS Safari 14.4+ |
| 6. Storage | **`sounds/<category>/<slug>.webm` parallel to `images/<category>/<slug>.<ext>`** | Matches Phase F image storage convention; GitHub Pages serves audio files unchanged; HTML5 `<audio>` element plays inline |

### How it threads together (the happy path)

1. Mom hears a bird she doesn't recognize. Taps the new 👂 button on the unified input.
2. Native browser permission prompt (mic). Recording starts; the button shows recording state (pulsing red ring, parity with how the 🎤 voice button already signals recording). A small timer chip ("0:08 / 0:30") shows under the textarea.
3. She taps 👂 again to stop (or it auto-stops at 30 seconds). Client encodes the recording as WebM/Opus, mono, 16 kHz. Typical 15-sec clip ≈ 30 KB.
4. The audio attaches as a small preview row above the textarea (▶ play button + filename + × remove), parallel to how the 📷 image attaches as a thumbnail today. The submit button relabels to **"Have Garden Guru take a listen"** (voice-parallel to the Phase F image relabel "Have Garden Guru take a look").
5. She taps the submit button. Client POSTs to `/api/chat` with a JSON body whose user message includes a new client-side shape: `{ role: "user", content: [{ type: "audio_ref", recordingId: "...", duration_ms: ... }, { type: "text", text: "what is this?" }] }`. The `audio_ref` shape is a Phase H invention — the Worker dereferences it server-side (see step 7).
6. The audio blob is uploaded *separately* via a new `POST /api/audio-upload` endpoint that returns a recordingId. Two endpoints (upload, then chat) keeps the chat payload small + lets the Worker's existing 5 MB ceiling stay reasonable.
7. Worker receives the chat call, dereferences the `audio_ref` to fetch the blob from KV (`audio-blob:<recordingId>`, ephemeral 1-hour TTL), and routes it to the audio vendor: a `POST` to OpenAI's `gpt-4o-audio-preview` (or `gpt-audio-1.5`) with the audio + a tightly-scoped prompt: "*Identify the species or sound in this recording. If it's a bird, frog, mammal, or other animal vocalization, give common name + scientific name + confidence. If it's not an animal sound, say so plainly. Be honest about uncertainty.*" The vendor returns a textual ID block.
8. Worker takes the textual ID block and constructs a synthetic Garden Guru turn: the original user "what is this?" + a system-injected tool-result-style note ("*The audio identification service returned: [ID block]*"), and runs that through the existing Garden Guru Anthropic call (cached system + property digest + live state). Garden Guru narrates in field-journal voice, applies the depth filter (is this one of the species the journal tracks?), emits the `<!--suggest-species ... -->` fence with the appropriate `kind` (bird / amphibian / mammal / etc.) when confidence is medium-or-higher.
9. Client renders the prose + the **Step A** chip ("Does that sound right?") — note the verb shift from "look" to "sound" — and the **Step B** chip on Yes ("Worth adding to the Almanac?"). Yes-Yes triggers `POST /api/promote-species`, which now also accepts an optional `audioRecordingId`. `handlePromoteSpecies` fetches the audio blob from KV, commits it to GitHub at `sounds/<category>/<slug>.webm` (fourth commit per promotion, alongside JSON / viewer.html / photo). Promoted entries gain an optional `audioSamplePath` field referenced by the renderer.
10. Auto-promote completes (timer ticks ~5–10 sec for the drafter + GitHub commits). New entry shows up in the dashboard 1–3 minutes after the GH Pages rebuild. The species card includes an inline `<audio controls>` element when `audioSamplePath` exists.

### Why the parts fit

- **(1a) Separate icons** is the only option that keeps both intents discoverable on a single tap. Mode toggle (b) and context-picker (c) both add a teach-step Mom doesn't need. "Garden Guru only" (d) splits Mom's mental model — she'd have to *enter Garden Guru first* to record a sound — and the unified input shipped specifically to flatten that surface. Three icons next to a single textarea (mic / photo / sound) is the natural growth path of the unified-input pattern, and the icon space is still well below clutter threshold.
- **(3) Audio vendor swap-out as a design principle.** Phase F is locked to Anthropic because Anthropic supports image. Phase H ships against OpenAI (or Gemini) because Anthropic does not yet support audio. The two-call structure (vendor for ID, Anthropic for narrative) is *not* engineering elegance — it's the honest acknowledgment that Anthropic owns the voice but not the ears, and a single-call architecture would require choosing between voice and ID. Both calls is correct until Anthropic ships audio, then a one-function-site swap collapses it to one call.
- **(5) WebM/Opus, mono, 16 kHz, 30-sec cap** — Opus is the bandwidth-efficient codec MediaRecorder produces natively on Chrome + Firefox + iOS Safari 14.4+. 16 kHz mono is plenty for bird/frog calls (BirdNET trains on 48 kHz but downsamples internally; OpenAI accepts what you send). The 30-sec cap bounds vendor cost ($0.05 worst case per submission).
- **(6) Storage parallel to images.** `sounds/<category>/<slug>.webm` mirrors the `images/<category>/<slug>.<ext>` pattern already shipped. The renderer just adds `<audio controls src="sounds/...webm"></audio>` to the species card body when present. No new conventions, no new directory shape, no new mental model.

### What Mom can do alone vs. what Paul has to do

**Mom alone:** Tap 👂. Record. Stop. Tap "Have Garden Guru take a listen." Read the reply. Tap "Yes" twice. Done — the recording is in the Almanac, the audio file is in Git, the species card has a play button. Same shape as Phase F, just with sound instead of light.

**Paul has to do:** Same as Phase F — watch for SCHEMA_DRAFTER quality issues and iterate the prompt when needed. Plus a new thing: monitor the audio vendor cost log (separate from Anthropic) and the swap-when-Anthropic-ships migration when that day comes.

---

## C. Recording infrastructure

### Capture

MediaRecorder API + `getUserMedia({ audio: true })`. Browser support is solid: Chrome, Firefox, Edge, Safari 14.4+ (iOS), Samsung Internet. The flow is identical to the existing `createVoiceCapture` factory's permission-grant step, but writes to a Blob instead of feeding SpeechRecognition.

Construct with explicit constraints:
```js
const stream = await navigator.mediaDevices.getUserMedia({
  audio: { sampleRate: 16000, channelCount: 1, echoCancellation: false, noiseSuppression: false }
});
const recorder = new MediaRecorder(stream, { mimeType: "audio/webm;codecs=opus", audioBitsPerSecond: 24000 });
```
Why disable echoCancellation + noiseSuppression: those are tuned for human speech. They will degrade bird/frog calls (which often look like "noise" to a denoiser). Disable both.

### iOS Safari quirks (the Phase F image equivalent)

Three to expect:

1. **MIME type fallback.** Older iOS Safari (14.4 to 15.x) prefers `audio/mp4`; newer versions (16+) handle `audio/webm;codecs=opus` natively. Use `MediaRecorder.isTypeSupported()` to pick; fall back to `audio/mp4` and adjust the upload extension accordingly. The Worker accepts whichever; OpenAI accepts both.
2. **First-tap permission.** Same as the existing 🎤 voice button — first tap requests mic permission and may need a second tap to actually start recording after grant. Handle this with the same UX pattern already in `createVoiceCapture`.
3. **No client-side transcoding library.** Unlike Phase F's canvas-downsample trick (which is two function calls on the platform), iOS Safari doesn't expose a JS-native audio transcoder. If a user records 30 sec mono Opus 24 kbps, the upload is ~90 KB — well under the 5 MB ceiling — so transcoding isn't needed. **Don't add an FFmpeg.wasm dependency for this; the encoding choices in step 5 above keep raw uploads small enough.**

### Encoding choice rationale

| Codec | Container | Bitrate | iOS Safari support | Vendor support | Verdict |
|---|---|---|---|---|---|
| Opus | WebM | 24 kbps mono @ 16 kHz | 14.4+ | OpenAI, Gemini, BirdNET | **Primary** |
| AAC | MP4 | 32 kbps mono @ 16 kHz | All | OpenAI, Gemini | **Fallback for older iOS** |
| MP3 | MP3 | Requires lame.wasm; not native to MediaRecorder | All (playback) | OpenAI, Gemini | Avoid (transcode overhead) |
| WAV | WAV | Uncompressed; ~512 kbps | All | All | Avoid (size — 1 MB per 15 sec) |

**Cap recording length at 30 sec.** That's enough for two phrases of a Wood Thrush song or one chorus of spring peepers. Longer is bandwidth + cost + diminishing ID quality (the vendor will get distracted by overlapping species).

### Worker-side handling

Audio blob arrives at `POST /api/audio-upload` as `multipart/form-data` or as raw bytes with `Content-Type: audio/webm`. Worker validates size (< 5 MB), generates a `recordingId` (nanos + 4-char random suffix, mirroring the pending-species ID shape), writes to KV at `audio-blob:<recordingId>` with `expirationTtl: 3600` (one hour — survives the chat turn + the two-step confirm). Returns `{ recordingId, duration_ms_estimate }`.

The chat turn then references `recordingId` in the content block; Worker dereferences and forwards to OpenAI; on `/api/promote-species` success, the same `recordingId` is read again and committed to GitHub at `sounds/<category>/<slug>.webm`.

---

## D. Cost

### Per submission (recommended path)

| Cost component | Value |
|---|---|
| Audio upload (Worker → KV) | $0 (within free tier) |
| OpenAI gpt-4o-audio-preview ID call (15-sec clip) | ~$0.025 |
| Anthropic Garden Guru turn (cached system + digest + ID-as-text + narrative output) | ~$0.018 (per Phase F math; ID-as-text is small) |
| Anthropic SCHEMA_DRAFTER call (on Yes-Yes only, ~50% of submissions) | ~$0.020 |
| GitHub Contents API (4 commits on promote) | $0 (free tier well above family usage) |
| **Per submission, ID only** | **~$0.04** |
| **Per submission, ID + promote** | **~$0.06** |

### Per month (Mom's expected cadence)

Mom's expected pattern: ~2–3 audio submissions per visit, similar to photo cadence. Visits: ~10–15/year for Mom plus Paul-mobile use. So ~30–60 audio submissions/year, ~50% leading to promote.

**Annual:** 30–60 submissions × $0.04 + 15–30 promotes × $0.02 = **$1.50–$3 per year for Phase H.**

That's well within Paul's stated $0.40–$1/month estimate — actually below it.

**Caveat:** OpenAI doesn't have an equivalent of Anthropic's prompt-caching, so every audio submission pays full freight on the vendor call. The cached Anthropic system + digest still saves on the Garden Guru narrative call (which runs unchanged), so cache discipline is preserved on the side where it matters most.

### When Anthropic ships audio (swap-out)

When `audio` content blocks land in the Messages API, the OpenAI call vanishes. The audio attaches directly to the user message; the cached Anthropic system + digest absorbs the ID + narrative in a single turn. Estimated cost per submission drops from ~$0.04 to ~$0.02 (matches Phase F image cost). Migration is one function in `worker.js` (`handleAudioId`), one if-statement at the call site, one removed environment variable.

---

## E. Architecture sketch (file by file)

Order matters — Worker first, then client, then schema.

| # | File | Change | Effort |
|---|---|---|---|
| 1 | `worker/worker.js` | Add `OPENAI_API_KEY` to required env list at top-of-file docstring. Add `/health` endpoint entry. | Trivial |
| 2 | `worker/worker.js` | New `POST /api/audio-upload` endpoint. Accepts up to 5 MB; writes blob to KV `audio-blob:<id>` with 1-hour TTL; returns `{ recordingId }`. | Low (~30 lines) |
| 3 | `worker/worker.js` | Extend `handleChat`: detect `audio_ref` content blocks; for each one, fetch the blob from KV, POST to OpenAI gpt-4o-audio-preview with the species-ID prompt, replace the `audio_ref` block with a synthesized text block `[Audio ID: <vendor-returned-text>]` *before* the Anthropic call. This keeps the Anthropic side ignorant of audio. | Medium (~60 lines — the OpenAI call shape + error handling) |
| 4 | `worker/worker.js` | Extend `GARDEN_GURU_SYSTEM`: add a `WHEN AN AUDIO ID IS PROVIDED` block, parallel to the existing image block. Same shape — narrate in field-journal voice, apply depth filter, emit `<!--suggest-species ... -->` fence with `kind` set appropriately. **Important:** the prompt must explicitly say *don't reference the audio identification service or expose the vendor name*; the user-facing narration is one continuous Garden Guru voice. | Low-Medium (prompt-eng pass) |
| 5 | `worker/worker.js` | Extend `KIND_TARGETS` to add `soundDir` field for each kind: `images/birds` → `sounds/birds`, etc. Where there's no audio for a kind (e.g., `plant`), `soundDir: null` (skip the audio commit gracefully). | Trivial |
| 6 | `worker/worker.js` | Extend `handlePromoteSpecies`: if request includes `audioRecordingId`, fetch the blob from KV, base64-encode, commit to GitHub at `<soundDir>/<slug>.webm` (or `.mp4` fallback), add `audioSamplePath` to the drafted JSON entry. Mirror the existing photo-commit pattern. | Low (~30 lines — parallel to photo commit logic) |
| 7 | `worker/worker.js` | Add OpenAI cost-log entry (or a separate `openai-cost-log:YYYY-MM-DD` daily key) so per-vendor spend is auditable. Update `analyze-fernwood.py` later to read both. | Low (~15 lines) |
| 8 | `viewer.html` (CSS ~line 2270) | New rules: `.ui-audio-btn`, `.ui-audio-recording` (pulsing red ring state), `.ui-audio-preview` (parallel to `.ui-image-preview`), `.ui-audio-preview-player` (▶ inline player). ~40 lines mirroring the image-button styles. | Low |
| 9 | `viewer.html` (markup near line 2940) | Add `<button id="ui-audio-btn" type="button" aria-label="Record a sound">👂</button>` next to the 📷 button. Add `<div id="ui-audio-preview" hidden>` with inline `<audio controls>` + filename + × remove, parallel to `#ui-image-preview`. | Low |
| 10 | `viewer.html` (JS new IIFE) | `UnifiedAudio` IIFE — owns MediaRecorder lifecycle, button state, timer, blob storage. Parallel to `createVoiceCapture` (the 🎤 voice-to-text one) but writes a Blob, not a transcript. Exports `start()` / `stop()` / `getBlob()` / `clear()` / `isRecording()`. Hooks into the same `UnifiedInput.wireUI` pattern. | Medium (~120 lines — MediaRecorder + iOS fallback + timer UI) |
| 11 | `viewer.html` (JS — `UnifiedInput`) | Submit handler: when audio blob exists, first POST to `/api/audio-upload`, get back `recordingId`, then include `{ type: "audio_ref", recordingId }` in the user-message content array sent to `/api/chat`. After Step B Yes-Yes, include `audioRecordingId` in the `/api/promote-species` payload. | Medium (~50 lines) |
| 12 | `viewer.html` (JS — `GardenGuru`) | Step A chip copy: when the suggestion came from an audio submission, the chip label reads "Does that sound right?" (instead of "Does that look right?"). Detect by checking whether the original user content array contained an `audio_ref` block. Step B copy unchanged. | Trivial |
| 13 | `viewer.html` (renderer) | When a species card has `audioSamplePath`, render `<audio controls preload="none" src="sounds/.../slug.webm"></audio>` in the card body. Native browser controls; no custom player. | Low (~5 lines per renderer — birds, amphibians, mammals) |
| 14 | `viewer.html` (metrics events) | New event types: `audio_attached`, `audio_uploaded`, `audio_id_received` (with vendor latency), `audio_species_suggested`. Three lines each in the existing `MetricsCollector` pattern. | Trivial |
| 15 | Schemas | Extend `birds.json`, `amphibians.json`, `mammals.json` v3 schema to include optional `audioSamplePath: string | null`. Document in `README.md` if a schema doc exists. The SCHEMA_DRAFTER prompt should mention the field but not invent paths — the Worker fills it on the promote commit. | Low |
| 16 | Deploy + smoke-test | `cd worker && npx wrangler deploy`; set `OPENAI_API_KEY` secret in Cloudflare; Paul records 2–3 test sounds (try a known bird + a frog chorus + a Mom-voice "what's that?" to confirm it routes correctly even though that's not a species); verify the 4-commit promote. Playwright smoke test on the unified input — 3 buttons present, all wired. | Medium |

**Total estimated effort:** Worker changes (steps 1–7) — 1 focused session. Client changes (steps 8–14) — 1–2 sessions, MediaRecorder + iOS fallback being the chunk. Schema + deploy + smoke (steps 15–16) — 1 session. **3–4 working sessions**, same shape as Phase F.

**Honest about the non-trivial pieces:**
- Step 10 (`UnifiedAudio` IIFE) — MediaRecorder + iOS MIME-type fallback + recording-state UI. Same effort class as the Phase F canvas-downsample chunk. Plan to iterate on a real device.
- Step 4 (Garden Guru prompt update for audio path) — needs a few iteration rounds. The model will sometimes lose the field-journal voice when the upstream ID came from a different vendor; the prompt must explicitly tell it not to reference "the audio identification service" or anything like it. Treat the prompt as load-bearing same as the image prompt.
- Step 11 (two-call sequencing on the client) — the upload-then-chat split is a small but real latency cost. Two sequential round-trips. Worth considering whether to fold the upload into the chat POST as a multipart body — but multipart inside a JSON-everywhere Worker is awkward. Stay with the two-step for v1.

---

## F. Two reasonable alternatives

### Alternative 1 — "BirdNET specialist + Garden Guru narrative"

Replace the OpenAI call with a self-hosted BirdNET inference service. Deploy `birdnetlib` on a small container (Fly.io free tier, Render small dyno, or a Raspberry Pi at the property). Worker POSTs the audio to that service, gets back a structured species list with confidence, hands the top match to Garden Guru.

**Wins over recommended:** Best-in-class quality for birds (the model is *the* state of the art). Free per-call once the container is paid for ($5/mo at the smallest paid tier; free on Fly.io's hobby tier). On-device PWA option (BirdNET-Live) eventually available on iOS.

**Loses:** Birds only. Frogs, mammals, insects all fall back to OpenAI or fail. Real deployment overhead — Paul stands up a second service, monitors it, handles its outages. Worker is no longer the single backend; there's a second hop. The CC-BY-NC-SA model license is fine for Fernwood (family-internal, non-commercial) but it's a constraint to document.

**When it wins:** If Paul finds OpenAI's bird-call quality is genuinely poor after T+30 days of real use *and* the audio scope ends up being 80% birds anyway, the BirdNET upgrade is worth the deployment hop. Hold this in reserve.

### Alternative 2 — "Defer Phase H until Anthropic ships audio"

Don't build now. Track issue #1198. Keep the Phase H thread alive in CLAUDE.md. When Anthropic ships audio content blocks, the path becomes a one-line extension of Phase F (just like Paul's original mental model assumed).

**Wins over recommended:** Zero new vendor surface. Zero swap-out work later (because Anthropic supports it natively when implemented). The architecture stays minimal: one Worker, one vendor, two endpoints.

**Loses:** Mom doesn't get audio ID. The feature stays a "captured idea" in CLAUDE.md indefinitely — Anthropic's timeline is unknown, and the issue has been open since February with no response. If you wait for it, you may wait a year. The shape of Phase H is well-understood now; building it gives Mom a real capability she'd use; deferring locks her into "you can describe what you heard, but you can't show it to the journal."

**When it wins:** If Paul looks at the multi-vendor architecture and decides "two vendors for one feature is more complexity than this hobby project earns" — that's a fair calibration call. The principle [[don't migrate working infrastructure without a functional reason]] cuts both ways: *adding* infrastructure also needs a functional reason. The functional reason here is real (Mom wants the feature; the vendor swap is a one-function migration), but it is not unanswerably real.

---

## G. Risks + open questions for Paul

### R1. The vendor swap-out commitment (the load-bearing one)

The recommended path adds OpenAI as a second vendor *specifically* with the design intent of swapping back to Anthropic when audio content blocks ship. That's a real commitment — the OpenAI call site must be encapsulated cleanly (`handleAudioId(blob, env)` returning `{ idText, latency_ms, cost }`), and the swap is then a 10-line PR.

**Open question for Paul:** Are you comfortable carrying two LLM vendors for an unknown duration? Tradeoff is real — two API keys, two cost logs, two failure modes — but the engineering surface is small. My read: yes, because the swap-out is genuinely a one-function migration and the value to Mom is real.

### R2. Quality of OpenAI gpt-4o-audio on non-speech

The vendor will identify *something* on a bird call, but neither OpenAI nor Gemini publishes accuracy numbers on non-speech species identification. The model is trained primarily on speech + music. Bird/frog/mammal call quality is unknown.

**Open question for Paul:** Want to budget a $2 test session early in the build — record 5 known calls (a Wood Thrush, a spring peeper chorus, a barred owl, an unknown sparrow, a chipmunk alarm) before wiring the full pipeline, just to see if the vendor's quality clears the bar? If quality is poor, Alternative 1 (BirdNET) becomes the lead path, with the OpenAI call as a frogs/mammals fallback. My recommendation: yes, do the $2 spike before committing to the full Worker changes.

### R3. Audio file storage growth

`sounds/<category>/<slug>.webm` files at ~30 KB per 15-sec clip × ~15 promoted-and-committed audio submissions per year = ~450 KB/year. Negligible at the GitHub repo size scale. *But:* if Paul opens this to more use ("let me record this for the journal even without an ID") the storage shape changes. Today's Phase F path commits a photo only on Yes-Yes; Phase H mirrors that. **Keep this discipline** — audio files commit to Git only on confirmed promote, not on raw recording.

### R4. iOS Safari MediaRecorder MIME-type fallback

Older iOS Safari (14.4 to 15.x) supports MediaRecorder but with limited codec selection — `audio/mp4` instead of `audio/webm;codecs=opus`. Newer iOS (16+) handles WebM/Opus natively. The fallback is small in code (3-line `isTypeSupported` check) but worth flagging because Mom's iPhone version is unknown.

**Open question for Paul:** What's Mom's iPhone running? If iOS 16+ we're fine; if older, the fallback path matters more (and the OpenAI vendor accepts MP4/AAC equally well, so the user impact is zero — just an extra MIME branch in the upload).

### R5. Audio-confidence threshold — when to suppress the fence

Phase F's prompt instructed Garden Guru to emit the `<!--suggest-species ... -->` fence only when confidence is medium-or-higher. Audio confidence is generally lower than vision confidence for the same species (more ambiguous; more overlapping species at once; more noise). The vendor will return a confidence number — should Phase H route through a confidence-threshold gate before letting Garden Guru emit the fence?

**Open question for Paul:** Want a stricter threshold for audio than for image? My recommendation: yes — only emit the suggestion fence if the vendor returns `confidence >= 0.7` (or whatever the vendor's scale is). Sub-threshold IDs become prose-only ("sounded like a Wood Thrush, but not certain enough to call it") — Mom can still re-record if she wants to nail it down.

---

## H. What stays parked

- **BirdNET self-hosted inference.** Alternative 1 above. Park it; revisit if OpenAI audio quality is poor in T+30 days.
- **Audio-only journal entries.** "I just want to save this sound, no ID needed." Out of scope for Phase H — the principle [[no AI on the capture path]] still holds; if Mom wants to save a raw sound, the path is the existing Save button with a description, not an audio-only capture flow.
- **Multi-clip audio (a chorus + a single call recorded together).** v1 is single recording per submission. If Mom wants to ID a chorus + a specific call within it, she records each separately.
- **Streaming audio identification (real-time, BirdNET-Live style).** Out of scope. Phase H is capture-then-identify, not continuous-listen.
- **Audio metadata (location, time, weather correlation).** The Worker has all the live state; could attach property weather to the recording for higher-fidelity ID. Defer to a future Phase H.1 if quality benefits warrant it.

---

## I. Principle candidates surfaced

Two candidates from this path-eval. Neither is silently added — both await Paul's engagement.

### Candidate 1 — Vendor swap as a stated design intent

**Statement candidate:** When a feature requires a capability the primary vendor doesn't yet support, an alternate vendor is acceptable *only* if the call site is encapsulated cleanly enough that the swap-back to the primary vendor (when capability lands) is a one-function migration. State the swap-back intent in code comments and in the path-eval; revisit the swap-back annually.

**Why it matters:** Phase H is the first time Paul's project shape genuinely needs a non-Anthropic vendor for a real reason. The temptation to leave the multi-vendor architecture in place once it's working is real — but the engineering principle here is to capture the swap-back *as a design intent*, not as a "we'll get to it." Without that discipline, the swap-back never happens and the architecture quietly drifts to permanent multi-vendor.

### Candidate 2 — Capability gates before architecture commits

**Statement candidate:** Before committing to a multi-vendor or multi-system architecture for a feature, verify the primary vendor's capability matrix against the feature's requirements. The verification is the load-bearing first move — skipping it is how projects accumulate vendors they didn't need.

**Why it matters:** The Phase H path-eval explicitly turned on this verification ("does Anthropic support audio?" — no, as of May 2026). Had Paul started building under the assumption Anthropic supports audio, half a session would have been wasted before the gap surfaced. This generalizes Paul's existing principle `landscape-research-before-deep-work.md` — the *inward* version of the landscape pass, asking "does our current vendor support this?" before the *outward* "what have others built?" pass.

---

## TL;DR for Paul

1. **Anthropic does not support audio content blocks as of May 2026.** Issue #1198 open since February, no response, no timeline. The "Claude API audio support exists" assumption in CLAUDE.md needs to be revised — it does *not* exist.
2. **Recommended path:** ship audio capture now with the recording → OpenAI gpt-4o-audio for ID → Garden Guru for narrative + fence → existing two-step confirm + auto-promote pipeline. Vendor swap-out is a stated design intent for when Anthropic ships native audio.
3. **UX: separate icons.** 🎤 voice-to-text stays; 👂 audio-ID joins; 📷 photo-ID already shipped. Three intents, three buttons, one input.
4. **Cost:** ~$0.04–0.06 per submission; ~$1.50–3/year at Mom's expected cadence. OpenAI is more expensive than Anthropic per call but volume is low.
5. **Effort:** 3–4 working sessions, same shape as Phase F. The hardest pieces are MediaRecorder + iOS MIME fallback (one chunk) and Garden Guru prompt iteration for the audio path (another chunk).
6. **Five open questions** above (R1–R5) before code starts. The most load-bearing: are you OK carrying two LLM vendors temporarily, and do you want a $2 vendor-quality spike first?

If yes-yes on R1 and R2, this is implementable as the next session's work.
