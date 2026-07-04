# Garden Guru input/composer — fact base (2026-07-03)

**Purpose.** Paul flagged three things about the Garden Guru input surface: (1) voice/transcription "has problems," (2) the photo attachment shows "a different picture," (3) it might be worth modeling the whole input after a "universal iPhone UI so people know what to use." This document is the **fact base** for that decision — current state, verified root causes, and the load-bearing constraints any redesign must honor. **It is not a redesign and proposes no build.** Next step is a scoped ux-expert pass using this as input.

Sources: firsthand code read + live screenshot (this session); prior design docs digested — `.engineering/2026-07-02-garden-guru-redesign-plan.md`, `.user-research/2026-07-02-garden-guru-conversation-analysis.md`, `.user-research/2026-07-02-mom-behavior-interpretation.md`, `.engineering/2026-07-02-garden-guru-conversation-redesign.json`, `.ux-reviews/2026-05-20-unified-input-redesign.json`, `.engineering/2026-05-21-phase-h-tabled.md`.

---

## 1. Current composer — what's actually there (verified, live site, iPhone width)

Markup at `viewer.html` ~4199–4250. Top-to-bottom:
- **Textarea** — placeholder *"What did you see, or what would you like to know?"*
- **Icon row** — two labeled **emoji** buttons: 🎤 **Voice**, 📷 **Photo**. (A third, 👂 **Listen** BETA, is present in markup but `hidden` — Phase H, tabled.)
- **Image preview** + **audio preview** (hidden until used).
- **Conversation area** (grows in-thread; Phase 1 re-anchored the input to sit beneath the latest reply).
- **Two commit buttons** — 📓 **Save to journal** (no AI), 🌿 **Ask Garden Guru** (AI).

Screenshot captured this session (not committed): the two intent-buttons render at near-equal weight (green Save / tan Ask), controls are decorative emoji.

---

## 2. Issue-by-issue findings

### 2a. Voice / transcription — root cause is the primitive, not a small bug
- Voice dictation runs on the browser **Web Speech API** (`webkitSpeechRecognition`), `continuous=true` + `interimResults=true`, with an `onend` **auto-restart hack** to fake continuous capture (`createVoiceCapture`, viewer.html ~12790–12908).
- This API is **unreliable on iOS Safari** (continuous mode is effectively not honored; the restart hack fragments/duplicates/silently drops results) **and it streams audio to Apple's servers** — so it degrades on weak connectivity.
- **The property is rural / Bortle-3 dark-sky** — exactly where cell/wifi is often weak. Cloud speech recognition is the wrong dependency for this place. **This is the likely source of "transcription problems," and it is inherent to the approach, not a tuning fix.**
- History: voice-on-this-surface was silently broken from the 2026-05-20 redesign until re-wired 2026-05-21 — so it's been fragile before.
- Prior spec (not yet built) wanted the **mic inside the textarea's right edge** (iOS-native pattern), part of the *input*, not a route-button. Current build has it as a separate icon-row button. *(unified-input-redesign.json F8)*

### 2b. Photo "different picture"
- Photo attach = a labeled 📷 emoji button → hidden `<input type="file" accept="image/*">` → FileReader → preview thumb (viewer.html ~4224, ~13014).
- **Most likely meaning:** the controls are **decorative emoji** (🎤📷📓🌿) that render differently across iOS versions and don't match the native iOS glyphs people instinctively recognize — consistent with Paul's "universal iPhone UI" instinct. A prior UX principle already flags this: *"icons earn their place — true AND useful,"* no *"decorative emoji-as-glyph register-leak."* *(unified-input-redesign.json F8/F11)*
- **OPEN — needs Paul to confirm exactly what he sees** (emoji look? the iOS library-vs-camera picker? a wrong preview thumbnail?). Not yet reproduced as a functional bug; flagged for a device repro or a one-line description.

### 2c. "Model after a universal iPhone UI"
- There's real precedent **for** this and a real caution **against** a naive version — see §4.

---

## 3. The primary user (this is who the input serves)
- **Mom** — iPhone, viewport **393×793**; the make-or-break **daily** user (most-active device, 27/~40 days). *(conversation-analysis §4)*
- **No-glasses reading:** the *only* device using the A/A+ text-size toggle (shipped for her). Small/faint controls are an accessibility failure here. *(conversation-analysis; and memory: Mom reads with difficulty)*
- **Posture:** one-handed, reclined, half-engaged (bed/coffee), must read in ~1.5s of a glance. *(unified-input-redesign.json)*
- **Connectivity:** input must tolerate **slow/absent signal**; there's a documented offline case where the Worker is unreachable but local Save still works. (Reinforces §2a — voice's cloud dependency is a poor fit.)
- **Mental model = ASK, not log.** Her felt gap is *"I hoped it was logged, but I wasn't sure."* She's not a follow-up chainer — but the one 2-turn conversation in the corpus was her **trying to continue and hitting a wall**, so "doesn't follow up" ≠ "doesn't want to." *(mom-behavior-interpretation)*

---

## 4. Load-bearing constraints any redesign MUST honor

1. **Two-intent commit is deliberate and protected.** Save (deterministic, no-AI) vs Ask (AI) must stay **distinct, symmetric in weight, and never auto-routed by input shape.** This guards the no-AI-on-capture principle and the Phase-G knowledge layer (a Haiku diagnosis laundered into the captured record poisons the loop — log the human's words, not the model's). A naive iMessage clone has **one** send button and would break this. *(unified-input-redesign.json F2; conversation-redesign.json F4)*
   - **BUT a genuine open fork:** Mom may experience "tell the journal" and "ask the guru" as **one act, not two** (flagged for her judgment, not yet resolved). *(mom-behavior-interpretation Q3)*
2. **Adopt the chat SPATIAL model; reject the chat VISUAL register.** Phase 1's win was the universal-chat layout (input beneath the latest reply) — proposed durable principle *"conversational surfaces inherit the universal chat spatial model."* **But** it must NOT read as a chatbot/productivity-AI surface: both Mom and Paul have documented "ChatGPT-anxiety," and suggestion-chips risk reading as the ChatGPT pattern. Resolution already on record: familiar layout, field-journal skin (warm-tan, Crimson italic, quiet), *"discreet ≠ dormant."* *(unified-input-redesign.json F1/F2; redesign-plan)*
3. **Discreet ≠ dormant.** A plain bordered textbox reads as *broken* and Mom scrolls past it. The input must invite (journal-pull), not sit inert. *(unified-input-redesign.json F1)*
4. **Icons earn their place; differentiate by content, not color.** Don't re-introduce routing burden visually. *(unified-input-redesign.json F8/F11/F2)*

---

## 5. Already decided / shipped — do NOT relitigate
- **2026-07-02 Phase 1–3 (live):** re-anchored input to universal-chat layout; one calm suggested-follow-up chip (pull-not-push); post-reply "Note this on the [plant]" deterministic log; add⇄remove plant from conversation.
- **Open from that work:** exact **continue-affordance shape** was *explicitly handed to ux-expert* (continue-button vs sticky input vs invite-line); durable photo-in-note deferred (iOS ~5MB quota → text + "had a photo" flag); Paul owes a **real-phone test** of the four flows.
- **Phase H "Listen" (audio species-ID) is tabled, not broken** — hidden button, code preserved; tabled for vendor-diversification overhead + defer-pending-signal. Paul's "audio problems" = the 🎤 Voice mic, NOT Listen.

---

## 6. The real forks for the ux-expert pass (not for me to decide)
- **F1 — Voice:** given the cloud-API + rural-signal fragility, is the answer (a) keep browser dictation but make failure graceful, (b) move to a record→upload→transcribe-on-Worker model (durable audio blob, like the audio_ref pattern, transcribe server-side), or (c) de-emphasize voice for Mom (she likely won't talk to a phone in bed) while keeping it for Paul-mobile? Instrumentation idea on record: if mic use <5% at 90 days, simplify.
- **F2 — Familiarity vs the two-intent split:** how "iPhone-native" can the input look before it either (i) collapses Save/Ask into one send (breaks capture principle) or (ii) reads as a chatbot (register-leak)? This is *the* central question.
- **F3 — Controls:** replace decorative emoji with native-style glyphs (mic-in-textarea, a familiar camera control) without turning the field journal into a productivity app.
- **F4 — Photo "different picture":** pending Paul's exact description.

**Recommended next step:** a focused **ux-expert** review scoped to the composer, using this fact base + the current screenshot, to produce 2–3 concrete input layouts that reconcile F2. Grounded in Mom's real usage, evidence-led (as the 2026-07-02 pass was) — not a speculative overhaul.
