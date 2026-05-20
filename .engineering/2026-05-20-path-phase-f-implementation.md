# Phase F — Image input on Garden Guru (implementation path-eval)

**Date:** 2026-05-20
**Mode:** Path Evaluation (engineering-partner)
**Status:** Implementation read on the 10 questions ai-advisor handed off. Strategic sequencing (ship before vs. after unified-input) intentionally out of scope.

## User & deployment context

- **Primary user pulled in by Q4:** Mom. She is already doing photos-for-ID on Claude. Without image input, Garden Guru is structurally weaker than her existing workflow. Phase F is the move that closes that gap.
- **Secondary user:** Paul-mobile, on the property with a phone, asking "what is this?" (the rubric's Q1/Q3 killer use case).
- **Deployment context:** `mom-ready`. Family-internal, low traffic, low stakes — but the user with the lowest tolerance for friction. UX-correctness + latency > engineering elegance.
- **Robustness level:** `shippable`. Code should hold up under daily use; it doesn't need horizontal scaling, formal monitoring, or hardening against adversarial input.
- **Conventions to honor:** single-file viewer.html, vanilla JS IIFEs (no framework, no build step), Worker stays at `worker/worker.js`. KV daily-key pattern (`cost-log:YYYY-MM-DD`, `metrics:YYYY-MM-DD`). Existing fernwood principles: capture-path-stays-pure ([[no-ai-on-capture]]) and storage-mirrors-existing-shape.

---

## Headline recommendation

**Build it as a small, additive layer on the existing Garden Guru surface — not a separate "vision tab," not a new card.** One image attachment per ask, attached inline in the same composer as the textarea, sent base64 inline in the same `/api/chat` request the surface already uses. No new storage tier, no new auth surface, no separate `/api/vision` endpoint. The hooks land in five places: composer markup, the GardenGuru IIFE, the WorkerAPI fetcher (raises body limit posture), worker.js `handleChat` (widens `content` to multi-block), and the system prompt (adds the image-handling section in Q7).

Why this shape: the smallest version of the feature is also the most legible. Garden Guru already *is* the conversational surface; image input is just a richer payload on the same conversation. Adding a parallel surface or endpoint would split the mental model (and the cost log, and the conversation history) for zero gain.

---

## Trade-off space across the 10 questions

I'll group these where they collapse and keep them separate where they don't.

### Group A — The picker & UX surface (Q1, Q5, Q6)

**Q1 — Image capture/upload affordance.**

Best path: a single hidden `<input type="file" accept="image/*" capture="environment">` driven by a paperclip-style button next to the existing mic button in `.gg-input-row`. That one element gives Paul and Mom everything they need:

- On iOS Safari (PWA-installed or not): tapping the input prompts the native "Photo Library / Take Photo / Choose File" sheet. `accept="image/*"` plus `capture="environment"` gives that menu, and lets iOS default to rear camera if "Take Photo" is selected. Mom is one tap from her camera roll where the photo she just took already lives.
- On desktop: same element opens the native file picker. Drag-and-drop is an easy ~10-line bonus (a `dragover`/`drop` handler on the textarea or composer), but skip in v1 — it's a desktop-only nicety and Paul-desktop is the lowest-stakes performer per the rubric.

**Don't build a new image-input element next to Garden Guru.** Touch the existing surface. Concretely: a small `<button id="gg-image-btn">📷</button>` next to the mic, and below the textarea (when an image is attached) a small thumbnail strip `<div id="gg-image-preview">` with the rendered 200×200 client-side preview + an "×" to remove. One image cap for v1. That cap is principle, not arbitrary: Mom's mental model is "I want to know about *this* plant," singular. Multi-image comparison is a Paul-desktop power-user feature you can add in v2 if it shows up in usage. Don't pre-build for it.

**Q5 — Bridge to Field Notes.**

This is the highest-leverage UX question in the batch. Honor `no-ai-on-capture` strictly: the user explicitly converts an AI exchange to a field note, AI doesn't decide-and-save.

The affordance: after Garden Guru replies on a turn that included an image, the assistant turn bubble grows a small chip-style button `[+ Save to Field Notes]` at its bottom-right. Click → pre-fills the existing Field Notes inline composer with a body that's the user's original question + the assistant's identification (e.g., *"Photo I took by the pond. Garden Guru identified as Cardinal Flower (Lobelia cardinalis) — not currently on the curated list."*), opens the species picker pre-selected when the ID matches something in `*_DATA`, and attaches the thumbnail.

The "save photo or save thumbnail" call: store the thumbnail only (the 200×200 preview already generated client-side, base64 in the observation record). This keeps observations bounded (~20-30 KB per entry vs. 1-2 MB if full image), keeps localStorage usable as the fallback storage tier, and respects that the *field journal* artifact is a memory aid — a recognizable thumbnail is enough. Photo-quality preservation isn't what the journal is for; if Paul wants the original, it lives in Photos.app/iCloud where photos belong.

**Critical:** the chat → field-note bridge is an explicit user action. The AI never auto-saves. The conversation can be ephemeral; the field note is the user's deliberate artifact. This is the post-Phase-D pivot's exact logic applied at one level higher.

**Q6 — Resolution + downsample policy.**

Client-side downsample to **max 1568px on the long edge, JPEG 0.85 quality, before sending**. Reasons stacked:

1. **Anthropic resizes anything bigger before processing anyway** (per Vision docs: "If your input image is larger than this native resolution, it will first be resized"). Sending a 4032×3024 iPhone photo and letting Anthropic shrink it is just LTE upload tax for no model-side benefit.
2. **Worker request size limit** is 100 MB but practical Worker performance + latency budget says keep request bodies under ~2 MB. A 1568px JPEG at 0.85 quality is typically 200-400 KB.
3. **Standard resolution is plenty for plant ID.** Haiku 4.5 caps at 1568 tokens (1568px long edge); the cost analysis already used those numbers.
4. **No high-res mode for Haiku 4.5.** The 4784-token / 2576px tier is Opus 4.7 only. There's no high-res lever to pull here — standard is the only mode.

Implementation: `<canvas>` + `image.decode()` + `toBlob('image/jpeg', 0.85)` in client JS. ~25 lines. Don't reach for a library; this is a known well-trodden recipe.

### Group B — Worker + API integration (Q2, Q3)

**Q2 — Smallest change to `/api/chat`.**

The Anthropic API accepts the array-shaped `content` on any user message, in the same request that has a 3-block cached `system` array. **No conflict between image-in-user-message and cache_control-on-system.** The image lives in the user message; the cache breakpoints live on the system blocks; the 5-minute ephemeral cache holds regardless.

Smallest diff to `handleChat` (~10 lines):

```js
// Replace this:
messages: turns.map(t => ({ role: t.role, content: t.content })),

// With this:
messages: turns.map(t => {
  // If client sent a richer content array (image+text), pass it through.
  // Otherwise pass the string content as before (backward-compatible).
  if (Array.isArray(t.content)) return { role: t.role, content: t.content };
  return { role: t.role, content: t.content };
}),
```

That's literally the whole shape change. The Worker becomes a passthrough for whatever content shape the client sends, and trusts the client to construct image blocks correctly. (Per Anthropic Vision docs: image-then-text ordering performs best — the client should construct `[{type:"image",...}, {type:"text",text:"..."}]` in that order.)

**One important validation to add:** before the fetch, size-check the request body. Reject early if it exceeds ~5 MB with a clear error so a misbehaving client gets a 413, not a Worker timeout. Don't bother decoding/inspecting the base64; just check serialized size.

**Q3 — Image transport: inline base64 vs. URL.**

**Inline base64. No image-hosting tier. Don't build it.**

The competing path (R2/KV-stored image with URL reference) buys *nothing* at family scale and costs:
- A storage decision, a key scheme, an expiration policy, a CORS surface, an auth-vs-public posture.
- A second persistence path the user has to trust ("where did my photo go?").
- A failure mode where the URL outlives or under-lives the conversation.

Inline base64 means: image lives in the user message, fully transient with the conversation, no separate storage decision. At 200-400 KB per image, even storing the full base64 in the conversation KV record is fine (KV value cap is 25 MB; you'll never hit it). Revisit only if Phase F volume grows past family scale, which it won't.

This is also the right calibration for the principle library: vendor consolidation at hobbyist scale beats best-of-breed. KV holds conversations; KV holds the images inside the conversations. Cloudflare R2 doesn't need to enter the picture.

### Group C — Persistence (Q4, Q10)

**Q4 — Image persistence: store with conversation in KV.**

Two layers, calibrated by lifetime:

1. **Inside the conversation record (`conversation:<uuid>`):** store the user message's `content` array as-is, including the base64 image block. The conversation is the working artifact during the session. Currently `persistConversation` writes `{ role, content, ts }` — keep doing that, just let `content` be an array when it is one. The record gets bigger (~1-2 MB if multiple images), but KV per-key cap is 25 MB. Plenty of headroom for the 5-follow-up cap.
2. **In a Field Note (`tateTracker.observations.v1` localStorage + KV `observations` array):** store only the **client-rendered 200×200 base64 thumbnail** (the same one shown in the in-chat preview), as a new `photo` field on the observation. ~20-30 KB per entry. Field notes are the *durable* artifact and need to stay small enough that localStorage doesn't blow its ~5 MB quota at scale and KV doesn't fan out.

Don't introduce a hash. The temptation is "store the hash + thumbnail to deduplicate" — but Mom isn't deduplicating images of her plants over months, and the engineering complexity (hashing, dedup table, garbage collection of orphans) is wildly out of proportion to the saving. AHA principle applies; this is the wrong abstraction at this scale.

**Q10 — Phase G readiness.**

The schema change to observation records is one field: `photo: { thumbnail: "data:image/jpeg;base64,..." }`. That folds cleanly into Phase G — when batch roll-up runs, the photo is just additional metadata on the observation. The rollup process won't need the photo bytes; it's looking at text + categories + dates.

What to surface for Phase G now: the **decision to thumbnail-only** matters here. If you later regret it and want the full-resolution image accessible to Phase G's rollup or to a Photos.app integration, that's a one-time backfill problem from… wherever the originals exist (which is, by design, the user's camera roll, not the dashboard). The dashboard never claimed to be a photo archive; that role belongs to iCloud. Phase G should never need a full-res copy.

The one Phase G ergonomic worth doing now: tag the observation with `via: "garden-guru-chat"` when it was created through the chat-to-field-note bridge, vs. `via: "quick-capture"` from the inline composer. Phase G's analysis is sharper if it can see which entries originated from AI exchanges.

### Group D — Guardrails & safety (Q7, Q9)

**Q7 — Hard-fail tripwire for image ID.**

The Q8b/8c hard-fail risks are *louder* with image input because the model is more confident with visual evidence than with prose description. The system prompt addition (lands alongside the Phase F code, not after):

```
WHEN AN IMAGE IS ATTACHED
Look at what's in the image. Identify the most likely species or feature if you can do so confidently. Then anchor your answer to this property — but with care:

- If what's in the image clearly matches something in the property digest (e.g., the user photographed a mountain laurel and it's one of the seventeen we tend), name it and speak about it as one we tend. "That's the laurel by the porch, or one of its cousins — they're opening their first flush this week."
- If what's in the image is a real species you can name but it is NOT in the property digest, say so plainly. "Looks like a Cardinal Flower (Lobelia cardinalis) — not one of the seventeen we tend. Common enough in damp Blue Ridge edges; worth noting where you saw it." Never describe it as if it lives here.
- If you can't tell from the image, name what you'd need to see to be sure. "Hard to tell from this angle — the underside of the leaf would settle it." Don't guess.
- For wildlife in the image: ID is fine even outside the curated list (per the depth filter — that filter is for "don't claim it's been observed here," not "refuse to identify"). Same rule: don't claim it's been seen on the property unless the digest says so.

NEVER, with an image:
- Treat the image as confirmation that something IS on the property. The image confirms the user saw the thing somewhere; whether it's on this property is a separate claim the digest controls.
- Invent a care recommendation for a plant not in the digest. If the user wants advice, route to: "Not one of the seventeen we have a care entry for — happy to talk generally, but the property-specific guidance only covers what's in the journal."
```

That last clause is the most important. The single Q8c failure mode for Phase F is: *Mom photographs an azalea, Garden Guru identifies it as Encore Azalea (which isn't her cultivar), and tells her to do something based on Encore Azalea's general profile rather than Fernwood's specific 'George Lindley Taber' entry.* The system prompt has to make Garden Guru reach for the digest entry by name when the photo matches a property plant, and reach for honest-uncertainty when it doesn't.

**Hard-fail log already scoped:** `Tate-Tracker/.engineering/garden-guru-hard-fails.md` (per the rubric). Add Phase F section the same day the code ships; first hard-fail incident sets the baseline.

**Q9 — Cost ceiling tripwire.**

The existing `logChatCost` already captures `input_tokens` / `cache_creation_input_tokens` / `cache_read_input_tokens` / `output_tokens` per turn. Image tokens flow through `input_tokens` (or `cache_creation_input_tokens` if they were on a cached block — they won't be; images live in the uncached user message). **No code change to cost log required.** The image cost is already visible; it just lives in `input_tokens`.

What *would* be useful, if Paul wants per-image visibility: add `has_image: true` to the cost-log entry when the user message has any image block. One line in `logChatCost`. Then a future `tools/analyze-costs.py` can answer "how often is Garden Guru getting images?" — but that's a Phase G concern. **Skip for now** unless Paul actively wants the line. The data is already in the conversation KV record; the analysis script can derive it later.

The cost ceiling itself is fine without a tripwire. At ai-advisor's ~$2/mo estimate, even a 10x usage spike puts the project well under $25/mo — and Paul has eyes on the daily cost log already. Active tripwiring is overkill here.

### Group E — Performance (Q8)

**Q8 — Latency budget + benchmark methodology.**

Latency budget breakdown (Mom on LTE on the porch is the worst case):

| Stage | Estimate | Notes |
|---|---|---|
| Client-side downsample to 1568px JPEG 0.85 | 200-400 ms | iPhone-class CPU; canvas is fast |
| Upload 200-400 KB over LTE (typical 5-15 Mbps up) | 200-800 ms | Worst case ~1s |
| Worker → Anthropic round trip (cached 57K system + ~1568 image tokens) | 1.5-3 s | Haiku is fast; cache read amortizes most of the system prompt |
| Worker → client response (text reply) | 100-300 ms | Small payload |
| **End-to-end** | **~2-4.5 s** | Within the 5s mobile-break ceiling; near the 3s aspirational target |

**The shaky cell is Worker → Anthropic.** It dominates and you can't optimize it directly; you can only mask it.

Two latency moves worth making in v1:

1. **Pending state must be visible the moment the user taps Ask.** The current "Garden Guru is thinking…" placeholder is correct; verify it renders immediately on submit, not after the Worker call returns. Also disable the Ask button + show the thumbnail you're sending so the user has visual confirmation the photo went.
2. **Streaming responses (Phase E v2 punch-list).** Already a known item. Phase F makes this more valuable — the first token visible in 1.5s on a 4s total response is dramatically calmer than 4s of silence. **Don't gate Phase F on streaming, but pair them in the same shipping window if possible.** The two changes ship cleaner together; streaming on a text response is a ~30-line client diff per CLAUDE.md.

**Benchmark methodology (concrete, Mom-realistic):**

- Same device: iPhone X-or-newer, Safari, dashboard installed as PWA.
- Three connection conditions in iOS Settings → Cellular Data Options → Data Mode = Low Data Mode (forces 4G-ish behavior), OR use Network Link Conditioner profile "3G" / "LTE" / "WiFi" via Apple's free Hardware IO Tools.
- Three image profiles: small (iPhone selfie-ish, 1MB pre-downsample), medium (typical garden photo, 3MB), large (Pro-camera ProRAW-ish, 10MB).
- 5 runs each, captured via Playwright + the existing metrics-capture's per-event timestamps (or by hand if Playwright on-device LTE simulation is painful).
- Pass criterion: 90th percentile under 5s (hard mobile break), median under 3s (aspirational).
- Capture data via the existing metrics-capture's batched events — add two event types: `garden_guru_image_attached` (client-side, when image picked) and `garden_guru_image_reply` (when assistant reply received), with timestamps. Latency = diff. **This piggybacks on infrastructure that just shipped today** — no new measurement surface needed, just two more event types. (The principle that just landed in fernwood.md — capture-path-stays-pure with batching — applies cleanly here.)

---

## Summary table (the 10 questions, compressed)

| # | Question | Recommended path | Confidence | Effort |
|---|---|---|---|---|
| 1 | Capture affordance | Single `<input type="file" accept="image/*" capture="environment">`, paperclip-button in existing `.gg-input-row`. No drag-drop in v1. | High | Low |
| 2 | Worker `handleChat` diff | Pass-through any-shape `content`. ~10-line diff. Cache-control on system unaffected. | High | Low |
| 3 | Image transport | Inline base64. No R2, no image-hosting tier. | High | None (it's the absence of work) |
| 4 | Persistence | Full image in conversation KV; only 200×200 base64 thumbnail in observation records. | High | Low |
| 5 | Field Notes bridge | Explicit "Save to Field Notes" button on the assistant turn. Pre-fills inline composer, attaches thumbnail. No auto-save. | High | Medium |
| 6 | Downsample policy | Client downsample to 1568px long edge, JPEG 0.85, before upload. ~25 lines of canvas code. | High | Low |
| 7 | Hard-fail tripwire | New `WHEN AN IMAGE IS ATTACHED` section in `GARDEN_GURU_SYSTEM`. Ships with the code, not after. | High | Low (prompt edit + redeploy) |
| 8 | Latency | 2-4.5s estimated; pair with streaming if possible. Benchmark via existing metrics-capture + 2 new event types. | Medium | Low (instrumentation only) |
| 9 | Cost tripwire | None needed. Existing cost log already captures image tokens via `input_tokens`. Optional: `has_image: true` flag. | High | Trivial-or-skip |
| 10 | Phase G readiness | Schema additions: `photo.thumbnail` + `via: "garden-guru-chat"` on observation. Forward-compatible. | High | Trivial |

---

## Strongest risks

Three to flag for Paul:

1. **Q7 (Mom's azalea trap) is the highest-stakes risk by far.** A photo gives the model more confidence; that confidence is hardest to govern when the photo matches a *species* the digest knows but a *different cultivar* than the property has. The system prompt has to actively reach for the digest's specific entry before answering. Validate on Day 1: photograph the property's actual George Lindley Taber azalea, ask Garden Guru about it, and check the response references the digest entry by name rather than generalizing to "azaleas."

2. **Latency on LTE is genuinely uncertain.** The estimate is 2-4.5s, which straddles the mobile-break ceiling. If the benchmark comes back closer to 5s than 3s, streaming responses move from "nice to have" to "ship-blocker for the Mom path." Don't take the estimate at face value; benchmark first or be ready to ship streaming immediately after Phase F.

3. **The Field Notes bridge (Q5) is the part most likely to drift toward auto-save under polish pressure.** The pull is real: "Mom photographed a plant, Garden Guru ID'd it, of course we save it — why make her tap twice?" Hold the line. Auto-save violates `no-ai-on-capture`, and "two taps for a deliberate journal entry" is the right friction. The bridge surfaces the action; the user takes it.

---

## Principle candidates surfaced (to flag, not write)

Two candidates for `~/.claude/engineering-principles/fernwood.md` — surfacing only; awaiting Paul's confirmation before any update.

### Candidate 1 — Pass-through Worker for any-shape `content`

**Statement candidate:** When the Worker is a thin proxy to a model API, design endpoints to be *content-shape-agnostic* — let the client construct the content array and the Worker pass it through unchanged. Don't have the Worker enforce or transform content structure.

**Why it would matter:** Surfaced explicitly here for Q2 (image-attached content arrays). The same posture is already implicit in `/api/today-line` (passes user-supplied state through), `/api/classify` (passes body through). Phase F is the first time a client wants to send a structurally richer content payload than a string. Generalizing the principle now means future multimodal additions (audio? PDF?) need no Worker change — they're client-construction problems.

**When it applies:** Designing or extending Worker endpoints that wrap model APIs.

**Avoid:** Coercing client input into a single "blessed" shape inside the Worker. Translating between content schemas. Letting the Worker know what kind of content it's relaying.

**Hesitation:** This may already be implicit in how Paul has been building Workers. May not be principle-worthy if it's just "thin Worker = thin Worker." Worth a single-line check, not a long discussion.

### Candidate 2 — Field Notes is the user's deliberate artifact; AI sessions are ephemeral

**Statement candidate:** AI surfaces (Garden Guru, classify, future) operate in transient session memory by default. The durable artifact set (Field Notes) only receives content through an *explicit user action* converting AI-session output to an entry. Auto-saving an AI exchange to the journal — however well-meant — is a category violation.

**Why it would matter:** This is the next-layer generalization of `no-ai-on-capture`. The original principle was about *write-time AI calls* (don't classify on save). This is about *the inverse path* — don't take AI session content and auto-write it to the durable store. Same underlying logic (capture is deliberate, AI is opt-in), just applied at the other end of the data flow.

**When it applies:** Any Phase F+ feature where AI output could plausibly be persisted to Field Notes or another long-lived store.

**Avoid:** Auto-saving Garden Guru exchanges as observations. Auto-tagging photos with model-inferred species in the journal. AI as the convert-and-commit layer between ephemeral and durable.

**Tension to resolve:** With Phase G, AI *will* read the durable store (observations as a knowledge layer) and may write back enrichments (rollup summaries, cross-references). That's still principle-aligned — the rollup is a deliberate, scheduled batch action, not a per-event auto-write. The line is "deliberate vs. incidental," not "AI-touching vs. AI-free."

Neither is silently added. Both flagged for Paul's confirmation if either lands as worth promoting.

---

## What's NOT in this path-eval (per Paul's brief)

- **No actual code.** This is path-eval, not implementation. Concrete code shapes are sketched (the 10-line `handleChat` diff, the canvas downsample snippet) but as illustration of effort, not as patches to apply.
- **No decision on sequencing vs. unified-input.** Paul's strategic call.
- **No silent principle updates.** Two candidates above; both awaiting confirmation.

---

## Open questions surfaced for Paul

1. **Streaming-with-Phase-F vs. Phase-F-alone:** if the LTE benchmark comes back >4s reliably, do you want to ship streaming and Phase F together as one wave, or accept slower v1 and add streaming as a fast-follow?
2. **Multi-image cap:** v1 is one image per ask. Comfortable with that? (Paul-desktop might want comparison shots later, but Mom won't.)
3. **The "save to Field Notes" button copy:** literal "Save to Field Notes" is fine, but is there a voice-aligned variant you prefer? ("Keep in the journal," "Note this," etc.) Content-steward's territory if you want a proper read.
4. **`has_image` cost-log flag:** worth the one-line addition or skip until you actually want to analyze image cadence?
5. **Both principle candidates above** — keep, reject, or revise?
