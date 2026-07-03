# Garden Guru conversational redesign — build plan (settled 2026-07-02)

Grounded in `.user-research/2026-07-02-garden-guru-conversation-analysis.md` (real KV
transcripts) + the four-agent panel (ux-expert, engineering-partner, ai-advisor,
user-researcher) + Mom's direct answers to the four verification questions + Paul's
decisions across the 2026-07-02 planning conversation. This doc is the source of truth
for the build; the agent artifacts hold the detailed reasoning.

## What the evidence settled
- **Follow-ups: the affordance was missing, not the demand.** 15/16 conversations were
  one-turn; the one 2-turn conversation (the other active user, not Mom) used its second
  turn to ask to add a plant. The plumbing (multi-turn, photo-on-any-turn, 6-turn cap)
  already exists — the UI dead-ends after a reply.
- **Mom is a satisfied one-shot user** (her words: "I got what I needed", "never had the
  need to send a second photo") — BUT that pattern is confounded by the broken affordance
  she was never offered a way past. Her real felt gap: **"I hoped it was logged, but I
  wasn't sure"** (the lily-pad observation → became Paul's manual INQUIRIES.md entry).
- **Her mental model is ASK, not log** ("I was asking a question about what might be
  wrong") — so the log is an *offered byproduct* of an answer, never a mode she enters.

## Cross-cutting rules (every phase)
1. **Capture stays deterministic (no AI on capture).** Guru proposes a log/add via a
   structured fence carrying **routing metadata only** (which plant, what type) — the
   front-end performs the write using the **user's verbatim words**. Guru's diagnosis
   lives in the conversation transcript (ask-path, flagged inference), never in the
   captured record. The fence has no free-text body, so AI prose cannot enter capture.
2. **User notes supersede everything.** A user observation outranks book/generic text in
   both wording and the actual care recommendation (the creeping-fig pattern as law).
3. **House-voice honesty.** Auto-drafted content grounds in location + horticultural data
   exactly like existing entries and says "by the book X, but here Y" — never states
   property-specific behavior as bald fact.
4. **Pull, not push.** Suggestions are calm, ignorable UI chips beneath the reply — never
   Guru's prose asking the user a question (the push behavior the eval rubric says makes
   Mom disengage).
5. **Instrument every new affordance** (impressions + taps) so a null result reads as
   "saw it, passed," not "couldn't see it" (the seeded-prompt/star confound).
6. **Stay calm for the one-shot flow** — new affordances appear only when there's a real
   next move; they never nag a satisfied user.

## Phase 1 — Re-anchor + follow-ups + suggested follow-ups  (view-layer; ship first)
- **F1 (critical):** re-anchor the conversation to the universal chat model — thread
  grows; the input + a weighty continue affordance live directly **beneath the latest
  reply**. Fixes the split-input dead-end (textarea above / Ask button below the thread).
- **F3:** co-locate a Photo action with the continue affordance (follow-up photo where the
  eye is). `askWithImage()` already works on any turn.
- **Suggested follow-ups (F2, KEPT per Paul):** at most one contextual, post-answer chip
  drawn from the reply's content ("More about the pond in July"), in UI chrome, pull-not-
  push, instrumented. Distinct from the dead seeded prompts (those were cold/pre-
  conversation; these ride existing engagement).
- **System prompt:** add a turn-continuity section (it's a continuing conversation — don't
  re-introduce or summarize back each turn).
- Reuse the proven confirm-chip visual weight/position; never a fainter chip, never a
  louder CTA (F6).

## Phase 2 — Log-an-observation on a known plant  (the Mom win)
- After Guru answers about an **already-known** plant (inCanon), offer a deterministic
  calm affordance beneath the reply: "Note this on the [lily pads]" → writes the user's
  verbatim words + speciesId + date via the existing AI-free observation store.
- **Unmissable "noted ✓" confirmation** — directly answers "I hoped it was logged but
  wasn't sure." How loud it needs to be: calibrate against Mom's Q2 (she expected it to
  land *somewhere in Fernwood*).
- Route by context (known vs unknown species), never a mode-picker (F4).
- **Text-first:** persist words + plant + date + a "had a photo" flag. Photo-in-note
  tabled (see Backlog).
- ai-advisor's `suggest-log` fence, `noteType: "observation"`.

## Phase 3 — Add ⇄ remove a plant  (full, no gating per Paul)
- **Add:** a short Guru **seeding-interview** (2–3 questions: where it's planted, aspect,
  what they've already seen) front-loads the user's facts as the top provenance layer →
  an honest, location-grounded, user-superseding entry drafted to `plants.json` canon.
  Double-confirm (like species-promote). Entry born honest-and-thin, fattens into rich
  canon as real observations land.
- **Remove:** symmetric capability (Paul's addition) — reversibility lowers the cost of a
  premature/wrong add, which is what makes shipping full add acceptable on light signal.
- `suggest-log` fence `noteType: "intent"` for a not-yet-on-property plant is the lighter
  cousin; full canon draft is the confirmed path.
- Honors the depth filter via rule #3 (house-voice honesty) + rule #2 (user supersedes),
  NOT via refusing to add.

## Tabled / backlog (scoped later, not this build)
- **Durable photo-in-note** — stripped today for the iOS ~5MB localStorage quota
  (`leanTurnForStorage`). Likely path: mirror the existing **audio_ref** pattern (blob →
  Worker `/api/audio-upload` → `recordingId`; thin ref in the turn). Needs its own scoping.
- **Structured provenance field** — entries carry provenance in prose, not a machine field;
  supersession is a voice convention. Fine at current scale; revisit if auto-adds grow.
- **`tools/people.json`** — mark `d-14nyhnjz` as Mom (currently guessed "Paul's old iPhone";
  behavior strongly refutes that). Attribution is inferred-strong, not ground-truthed.
- **Durable principles** the panel surfaced (write on Paul's go): "a correct 'no' still
  owes the user a next move," "conversational surfaces inherit the universal chat spatial
  model," "log the human's words not the model's," "capture-intent before canon,"
  "the fence is the bridge (ask-path AI proposes a capture without performing it)."

## AUTONOMOUS EXECUTION PLAN (Phases 2 & 3) — added 2026-07-02

Paul authorized autonomous execution of Phases 2 + 3 (no per-boundary check-in). Build
locally, verify each phase end-to-end via mocked-worker browser drive, commit locally,
hold deploy. Resolved open-questions (my defaults, noted per consultant mode):
- **Observation destination:** plant-scoped — write an observation with `speciesId`/
  `speciesName` set to the target; it lands in the one field-notes store (tagged to the
  plant). No separate stream.
- **Body = the reader's verbatim words**, taken from the reader's own turn(s), NEVER
  Guru's diagnosis (the capture-path guard). Guru's diagnosis stays in the conversation.
- **Lily pads specifically** aren't in canon (no waterlily entry), so logging on them is
  a Phase-3 add-then-log, or a zone note. Phase 2 mechanism is verified against an
  in-canon plant; adding a real waterlily entry is a nice-to-have, not a blocker.

### Phase 2 — log-an-observation  (files: worker/worker.js, viewer.html)
**Worker:**
1. New `GARDEN_GURU_SYSTEM` section "WHEN THE READER WANTS TO LOG AN OBSERVATION": if the
   reader is recording something noticed about an IN-DIGEST plant/feature, answer in prose,
   then emit a `suggest-log` fence — never say "I've logged it," never author the note body.
2. Fence: `<!--suggest-log\n{ "noteType":"observation", "target":{ "speciesId":"…","name":"…" } }\n-->`
   Rules: emit only for a known (in-digest) target; speciesId must exist in the digest;
   if the plant isn't in canon, do NOT emit (that's Phase 3's add path).
**Client:**
3. Extend fence parsing: `parseLogFence()` → `assistantTurn.logSuggestion = {noteType, target}`
   (strip before species-fence parse, same as follow-up).
4. Under the reply, render a calm deterministic affordance "Note this on the [name]"
   (confirm-chip weight; NO "does that look right" — the user's words + a known target need
   no ID adjudication). On tap → `fnSaveObservationFromConversation(readerText, speciesId,
   speciesName)` (clone of fnSaveInlineEntry with those fields set; body = the reader's most
   recent user-turn text). Then swap to "Noted on the [name] ✓ — it's in the field notes."
5. Instrument `log_offered` (on render) + `log_saved` (on tap).
**Acceptance:** mock reply w/ suggest-log → chip renders, fence stripped; tap writes an
ObservationStore entry with speciesId set + body = reader's words (verified not Guru's);
confirmation shows; metrics fire.

### Phase 3 — add ⇄ remove a plant  (files: worker/worker.js, viewer.html)
**Add (seeding interview → canon draft, double-confirm → GitHub):**
1. Worker system-prompt section "WHEN THE READER WANTS TO ADD A NEW PLANT (not in digest)":
   run a SHORT seeding interview across turns (multi-turn now works) — where planted /
   aspect / what they've already seen. When enough, emit `suggest-add` with a drafted entry
   grounded in location+horticultural data in house-voice ("by the book X, but per your note
   Y"), reader's seeding answers as the SUPERSEDING top layer.
2. Fence: `<!--suggest-add\n{ draft plants.json entry incl. provenance + seedingAnswers }\n-->`.
3. Client double-confirm (reuse the two-step confirm-chip weight) → POST to promote path
   (reuse `/api/promote-species` drafter+commit machinery, text-driven variant) → commits
   to plants.json on GitHub. Honest-thin entry; fattens as observations land.
**Remove (symmetric, Paul's addition):**
4. Worker `suggest-remove` fence when the reader asks to remove an IN-CANON plant →
   client double-confirm → new `/api/remove-species` (mirror promote: remove entry from
   plants.json + commit). Reversibility lowers the cost of a premature add.
5. Instrument add_offered/add_confirmed, remove_offered/remove_confirmed.
**Acceptance:** mock the add fence → seeding chips + double-confirm render; promote payload
carries the drafted entry + seeding answers as top provenance; remove fence → double-confirm
→ remove payload targets the right speciesId. (Verify with mocks; do NOT commit test plants
to the real repo.) House-voice honesty + user-supersedes rules hold in the drafted entry.

### Observation entry shape (reference, from fnSaveInlineEntry)
`{ id, date:"YYYY-MM-DD", createdAt:ISO, category, speciesId, speciesName, zoneId, body, classifyPending:false }`

## Guardrails on shipping
- Build + verify **locally**; hold the **deploy/push** of the public repo for Paul's
  explicit go (Bolo-style hard rule; this repo is public GH Pages).
- Fix nothing on the capture path that lets Guru's words become the logged record.
