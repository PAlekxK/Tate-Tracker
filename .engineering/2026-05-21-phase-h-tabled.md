# Phase H — Tabled (decision memo)

**Date:** 2026-05-21 (evening)
**Status:** **Tabled.** All code preserved (Worker + viewer); 👂 Listen button hidden from the UI. Re-enabling is a one-attribute removal once a free ID path is built.

## What was shipped + what's now hidden

Three commits landed Phase H end-to-end:
- `6805ddf` — labeled icon row + Listen (BETA) button (UI restructure)
- `2619583` — MediaRecorder client + askWithAudio + Worker `/api/audio-upload` + OpenAI integration + audio commit on promote
- `3e8005f` — drift-check tool + AI-ID process audit

A subsequent commit on this same day **hides the 👂 button** (HTML `hidden` attribute on `#ui-audio-btn`). Everything underneath stays intact:
- The audio capture client (`createAudioCapture`, `UnifiedAudio`) is loaded but unreachable from the UI.
- `GardenGuru.askWithAudio` is exposed but no call site invokes it (the submit button never sees `attachedAudio` because no one can attach audio).
- Worker `/api/audio-upload` is registered + functional; would store audio in KV if anything POSTed to it (nothing will).
- Worker `handleChat`'s audio_ref dereferencing logic is preserved; without an `OPENAI_API_KEY` secret set, it would 502 — but with the button hidden, no request reaches it.
- `handlePromoteSpecies` Step 6 (audio commit) is preserved.
- `SOUND_ID_OPENAI_SYSTEM` constant + `identifyAudioViaOpenAI` function preserved.

**Why preserve vs. delete:** the build is ~500 lines net across two files. The capture + upload + structured-fence architecture is reusable for any future audio-ID backend (BirdNET, Hugging Face, Anthropic-when-they-ship-audio). Throwing it out to revert would lose ~3 sessions of work; keeping it costs nothing (dead code paths, no runtime cost since the button is hidden).

## The discussion trail (how we got here)

1. **Initial ask (2026-05-21 evening):** Paul wanted to extend the Phase F image-ID flow to audio — bird calls, frog choruses, mammal vocalizations.
2. **Landscape pass 1 (Claude WebSearch):** Anthropic Messages API doesn't support audio content blocks as of May 2026 (SDK issue #1198 open since Feb, no timeline). Three paths surfaced: BirdNET, spectrogram hack, defer.
3. **First lock:** Paul picked **Path 1 — BirdNET integration (birds-only)**.
4. **Path-eval landed (engineering-partner):** recommended **OpenAI gpt-4o-audio** over BirdNET — multi-species coverage, $0.04-0.06/turn, vendor-swap-back to Anthropic stated as design intent. Path-eval surfaced 5 R-questions; Paul approved "Build OpenAI integration now (skip the spike)."
5. **Build shipped:** 3 commits over ~1 hour. Worker deployed. UI labels added: 🎤 Voice / 📷 Photo / 👂 Listen (BETA). `OPENAI_API_KEY` flagged as Paul-only setup.
6. **Cost question raised:** Paul asked "I thought we weren't using OpenAI because of the cost?" — surfacing that his BirdNET lock had been overridden by his subsequent OpenAI lock without him fully internalizing the trade-off.
7. **Honest recap given:** OpenAI at Mom's cadence ≈ $10/year (cheapest shippable option). BirdNET self-hosted ≈ $60/year container or $0 on free tier with cold-start latency. Browser TFJS model on iOS = "coming soon."
8. **Second lock:** Paul picked **"Switch to BirdNET (birds-only, no new LLM vendor)"**.
9. **Followup question:** "is there any free option we can use for audio ID that you've found?" — surfacing that the cost concern wasn't the only driver; vendor diversification + the principle of free-as-baseline matters.
10. **Honest reply on free options:** Three free-ish paths — BirdNET on free-tier container, Hugging Face Inference API (1,000 free requests/day, model availability unverified), BirdNET-Live iOS (coming soon). Path-eval hadn't explicitly evaluated Hugging Face — a real gap.
11. **Third lock:** Paul picked **"Defer Phase H — keep the UI as 'coming soon'"**.
12. **Final decision:** Paul: "OK let's just table this whole feature for now. We can keep the code, document our discussion/decision/next steps well." Then: "Let's deactivate the 'Listen' icon from the viewer entirely so that the user isn't even aware."

## Why this was the right call

- **Vendor-diversification cost is real.** Two LLM APIs to manage (Anthropic + OpenAI), two keys, two cost logs, two failure surfaces — for a feature serving Mom ~4×/week. The maintenance overhead is meaningful even when the dollar cost is trivial.
- **No free-and-mature path existed today.** BirdNET-self-host requires infra time Paul hasn't budgeted. Hugging Face requires landscape research that hadn't been done. BirdNET browser-TFJS isn't shipped on iOS yet. OpenAI is the only thing that *works today* — and you decided that "works today" wasn't sufficient justification for a permanent vendor add.
- **Mom's actual usage signal hasn't validated demand.** Phase F just shipped (1 successful auto-promote — the hydrangea). The audio-ID intent is hypothetical until Mom has been using Phase F for weeks and has expressed "I wish I could submit a call too." Building speculative features ahead of usage signal violates `feedback_defer_affordances_pending_signal`.
- **The capture architecture is preserved for future.** When any of the three free paths matures (Cornell ships iOS, Hugging Face validation lands, a new free-tier service emerges), the swap-in point is the `identifyAudioViaOpenAI` function. Everything else stays as-is.

## Next steps (when this comes off the table)

In rough order of likelihood / desirability:

1. **Watch for BirdNET-Live iOS support.** Cornell's app page says "coming soon." If/when shipped, audio ID runs entirely client-side — zero infra cost, no vendor surface, no Worker call needed. Highest-quality path; just needs Cornell to ship.
2. **Hugging Face Inference API landscape pass.** ~30 min of WebSearch + a few test calls would confirm whether a free-tier-hosted bird-ID model exists with acceptable quality. If yes, the Worker swap is small (`identifyAudioViaOpenAI` → `identifyAudioViaHuggingFace`).
3. **Anthropic Messages API audio support.** Track SDK issue #1198. When Anthropic ships, the entire Phase H architecture collapses to a one-function migration — Worker passes the audio block directly to the existing `/v1/messages` call, no second vendor needed, no audio_ref indirection, no synthetic context injection.
4. **BirdNET self-hosted on free-tier container** — last resort if the above don't materialize and Paul really wants the feature.

## How to re-enable when ready

Three steps:

1. Remove the `hidden` attribute from `#ui-audio-btn` in `viewer.html` (~line 3054).
2. Confirm the backend is wired (set `OPENAI_API_KEY` if staying with OpenAI, OR rewrite `identifyAudioViaOpenAI` for the new vendor).
3. Verify `/health` shows the relevant `configured.*` flag.

That's it. The UI flow, capture pipeline, structured fence, and auto-promote audio commit are all in place.

## Lessons surfaced

1. **Path-eval recommendations override prior-locked choices silently if I let them.** When the engineering-partner recommended OpenAI over Paul's locked BirdNET, I should have framed the question as "do you want to override your BirdNET choice?" rather than "do you want OpenAI?" — the latter loses the comparison context. Worth being explicit when an agent recommendation conflicts with an earlier user lock.
2. **"Free" is not just about dollar cost.** $10/year IS effectively free against Paul's stack budget. The "no new LLM vendor" framing was the real concern. Listen for the underlying principle, not just the literal word.
3. **Landscape passes have to be honest about gaps.** The path-eval didn't evaluate Hugging Face. I should have done that landscape work *before* surfacing OpenAI as the recommended path, or flagged the gap loudly. The `landscape-research-before-deep-work` principle I'd just promoted didn't get applied to itself.
4. **`feedback_defer_affordances_pending_signal` applies here.** Phase F just shipped; demand for audio-ID is hypothetical until Mom's actual photo-flow usage produces a "I wish I could submit a call too" signal. Speculative-feature build is the failure mode this principle guards against. Should have caught it earlier in the Phase H decision tree.

## Related artifacts

- `Tate-Tracker/.engineering/2026-05-21-path-phase-h-audio-input.md` — the engineering-partner path-eval (~1,650 words) that recommended OpenAI
- `Tate-Tracker/.engineering/2026-05-21-ai-id-process-audit.md` — process audit triggered by the drift bug discovered during Phase H build
- `Tate-Tracker/CLAUDE.md` — Phase H entry updated to reflect tabled status
- `~/Documents/Claude/handoff/master-plan-2026-05-21.md` — W2.5 section to note Phase H tabled
- Memory: `[[feedback_defer_affordances_pending_signal]]`, `[[wedge-is-curation]]`, `[[landscape-research-before-deep-work]]`
