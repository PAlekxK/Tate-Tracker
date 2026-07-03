# Garden Guru — conversational model for the capture/diagnose/log blur

**Advisor:** ai-advisor · **Date:** 2026-07-02 · **Mode:** consult
**Charge:** design the conversational/AI model (not UI, not code) for a Garden Guru that
holds a back-and-forth AND can help log/add to the journal, driven by the
`.user-research/2026-07-02-garden-guru-conversation-analysis.md` findings.
**Companion surfaces:** UI/affordance → ux-expert; the observation-write endpoint + photo
persistence → engineering.

---

## The one-line recommendation

Guru stays an **ask-path AI** that answers in prose and, when the reader signals capture
intent or states a discrete field observation, **emits a structured `suggest-log` proposal
fence** — the exact same move it already makes with `suggest-species`, but pointed at the
*observation/almanac* layer instead of *canon*. The front-end renders a deterministic
confirm; on confirm, **deterministic AI-free code writes the reader's own words** to the
observations store. Guru proposes the capture; it never performs it, and it never authors
the captured text. One new fence closes both the lily-pad case and the creeping-fig case.

---

## (a) The capture/diagnose/log blur — where the seam is

Today's utterance carried three intents in one breath:

1. **Diagnose** ("what could be driving that") — **ask path, AI.** Guru already does this well.
2. **Care advice** ("see what we can do to help the plant") — **ask path, AI.** Guru does this.
3. **Log/capture** ("log that," "populate our field notes") — **capture path. Must be
   deterministic and AI-free** (CLAUDE.md rule; `feedback_no_ai_on_capture` 3-layer model).

The seam sits **between the diagnosis and the write**, and it is drawn by *who authors the
bytes that land in the capture store*:

```
USER UTTERANCE  (diagnose + advise + log, one breath, + photo)
      │
      ▼
  /api/chat  ── AI (ask path) ──►  PROSE: diagnosis + care advice
      │                            (lives in the conversation record = AI inference by nature)
      │
      └── emits  <!--suggest-log-->  = a PROPOSAL carrying routing metadata only
                 │
   ═══════════════ SEAM ═══════════════   AI stops here. It has proposed, not captured.
                 │
                 ▼
  Front-end renders "Add this to the Almanac?"  ── deterministic
                 │   (the human is the clearer: confirms the target + approves/edits
                 │    THEIR OWN words)
                 ▼
  Deterministic AI-free write  (reuse the existing almanac/`fnSaveAll` → observations path,
                 │              NOT the AI schema-drafter used by promote-species)
                 ▼
  observation record = USER'S OWN WORDS + confirmed speciesId + timestamp
```

**Two different things get stored in two different places at two different trust classes:**

- The **observation** (what Mom saw) → the observations/almanac store. **Human-authored,
  AI-free. Trust = captured field note.**
- The **diagnosis** (Guru's read: thickening canopy + shifted July sun angle) → stays in the
  **conversation record**, which is *already* auto-persisted to KV. **AI inference. It is
  never promoted into the observation body.**

This is the 3-layer model made concrete: *capture* (user words → observations) is AI-free;
*ask* (diagnosis → conversation) is AI; and the fence is the **bridge that lets the ask
surface *propose* a capture without *performing* one.** Guru saying "worth logging" in prose
is fine; Guru saying "I've logged it" would be a lie — the client owns the write, exactly as
the current suggest-species rule already forbids Guru from claiming it added a species.

**The load-bearing structural guard (strong recommendation):** the `suggest-log` fence
carries **no free-text observation body** — only routing metadata. The observation text is
supplied **deterministically by the front-end from the reader's own turn** (it has the
textarea content / transcript locally). Result: there is *literally no field* for AI-authored
prose to enter the capture store. The model can only propose the *action* and the *routing
target* — both of which the human then clears. This is "capture stays AI-free" enforced
structurally, not by convention — the same philosophy as the Houseplants import-boundary lint
and `feedback_sanitize_at_storage_boundary`.

Resolving "lily pads" → a canonical `speciesId` is a **characterize step** (mechanically
matching captured text to canon), so its output is **flagged inference the human confirms**,
never an authoritative auto-tag. Cleanest: let the front-end do it deterministically via the
**fuzzy species-match against `*_DATA` that already exists from Phase D** (`classifyEntry`),
and let the confirm button be the human clearing the match. Guru naming the target in the
fence is fine *as a proposal*; the human's Yes is the clearance (`AI verification flags,
never clears`).

---

## (b) Add-from-conversation — two cases, ONE fence

Both cases are field notes, not canon growth. Neither should touch the AI schema-drafter.
They share a single new fence, distinguished by `noteType`:

### (i) New plant not yet observed here — creeping fig (`noteType: "intent"`)

Guru's refusal to fabricate property knowledge is **correct** (depth filter / observations-as-
knowledge). The failure was the **dead-end**, not the stance. Redesign: Guru still refuses to
invent care knowledge, but instead of ending the exchange it **captures the intent**:

> "Not one of the seventeen we tend — so I can't speak to it from this slope yet. But worth
> noting you're trying it on the masonry wall; a season or two of watching will tell us how it
> takes here."  → emits `suggest-log` with `noteType: "intent"`, `target.speciesId: null`.

The depth filter is preserved because **we are not writing to `plants.json` canon** — canon
promotion still requires the observed-over-a-season path (or the photo→`suggest-species` route
for a confirmed ID). We are writing a **field note / intent record** into the observations
layer. That closes the exact loop that became Paul's manual `plants.json` edit three weeks
later.

### (ii) Observation on an existing plant — lily pads (`noteType: "observation"`)

Guru answers the diagnosis/advice in prose and emits `suggest-log` with
`noteType: "observation"` and the resolved/proposed `target` (pond water-lily). Confirm →
deterministic write of the reader's words as a seasonal field note tied to the species. This
is the capture the current photo→`suggest-species`→promote pipeline **does not serve** (that
pipeline adds *new species to canon*; this records an *observation on a known one*).

### The fence contract (parallel to `suggest-species`)

```
<!--suggest-log
{
  "noteType": "observation" | "intent",
  "target": {
    "kind": "plant" | "bird" | "mammal" | "amphibian" | "snake" | "lizard" | "fish" | "animal-other",
    "speciesId": "iris-pond" | null,      // null for intent / not-yet-on-property
    "commonName": "pond water-lily"        // for display + deterministic fuzzy-match
  } | null,
  "observedOn": "2026-07-02"
}
-->
```

Notice what is **absent**: no observation-text field. The capture body is the reader's own
turn, supplied by the front-end. `suggest-species` stays exactly as it is (it serves a
different job — new-species-to-canon, which legitimately uses the AI drafter).

**Durable upgrade (recommend, per `fernwood.md` "Forced tool-use is the structured-output
primitive"):** promote *both* fences from parsed HTML comments to **forced tool-use with a
typed `input_schema`**. For `suggest-log` specifically — because it straddles the capture
boundary — a typed schema is the structural guarantee that the fence can't be malformed and
can't grow an observation-text field someone later "just adds." The schema *is* the boundary.

**Honesty about uncertainty is preserved the same way `suggest-species` does it:** emit the
fence only when capture intent is real (an explicit "log this" OR a discrete stated
observation); keep the target honest (`speciesId: null` when it isn't a confident match);
never fabricate an observation the reader didn't make. Inventing a claim in the reader's name
is the one blocking direction (`Its-voice, no twin — the person is the clearer`); omitting or
routing is the human's call at confirm.

---

## (c) System-prompt changes to `GARDEN_GURU_SYSTEM`

The plumbing is already multi-turn; the prompt is written turn-agnostic. Five additions
(surgical — the voice/scope/uncertainty sections are good and stay):

1. **Turn-taking / continuity (new short section).** It is a continuing conversation. Don't
   re-introduce, don't re-establish context already in the thread, don't summarize the
   conversation back. Carry the voice unchanged across turns (the field-journal register is
   fixed every turn, follow-ups included).

2. **`WHEN THE READER WANTS TO LOG / RECORD AN OBSERVATION` (new section, the big add).**
   - Triggers: explicit capture language ("log this," "add to our field notes," "record
     that," "populate our journal") **OR** a discrete concrete observation about a known
     feature ("dieback on the lily pads," "first bloom on the laurel," "saw a bear at the
     salt lick").
   - Behavior: answer the ask parts (diagnosis, advice) in prose as normal, **then** emit a
     `suggest-log` fence proposing the capture. Resolve `target` to a known species when
     named/obvious; else `noteType: "intent"`, `speciesId: null`.
   - **Do not write anything yourself and do not claim it's been logged.** "Worth logging" in
     prose is fine; "I've added it" is false — the client does the write on confirm. (Mirrors
     the existing suggest-species "do NOT ask about adding — the client renders buttons" rule.)
   - **The captured text is the reader's, not yours. Never put your diagnosis in the log.**
     Your analysis stays in the reply; the field note is their words.

3. **Not-yet-on-property → capture the intent, don't dead-end (new rule under the depth
   filter).** When the reader wants to track/add a plant that isn't one of the seventeen,
   hold the depth filter (don't invent care knowledge) **but** offer to note the intent via
   `suggest-log` (`noteType: "intent"`). This is the explicit fix for the creeping-fig
   dead-end.

4. **Multi-intent is normal — serve both.** A single utterance may carry a question *and* a
   log request. Answer in prose and propose the log in the fence; don't make the reader
   choose one.

5. **Pull, not push — don't nag.** Emit a log fence **only** when capture intent is signaled
   or a discrete observation is stated. Do **not** append a log proposal to every turn — a
   "want to log this?" on an idle "is it a good time to fertilize" is productivity-app
   nagging, against the field-journal tone (`project_tate_tracker_tone`) and
   `feedback_defer_affordances_pending_signal`. Restraint is the default (`Altimeter, not
   autopilot`).

---

## (d) Model / cost sanity

Current: Haiku 4.5, ~57K-token digest, two `cache_control: ephemeral` breakpoints (system
prompt + digest), ~$0.86 / 6 days ≈ **$5/mo**. Multi-turn + the log loop change the profile
only slightly, and mostly in Paul's favor:

- **Keep Haiku 4.5.** The lily-pad diagnosis (praised in the analysis) proves Haiku +
  curated context is enough. The wedge is curation, not raw capability
  (`cross-cutting: wedge is curation + surface`) — don't reach for Sonnet unless diagnosis
  quality on hard cases actually falters, and then escalate selectively, not by default.

- **The log loop adds ~zero marginal AI cost.** `suggest-log` is a few extra output tokens
  inside the existing chat completion; the write is deterministic (no AI). Contrast with
  `promote-species`, which pays ~$0.04 for a second drafter call. **Logging an observation
  must not go through an AI drafter** — that's both the cost argument and the capture-AI-free
  argument pointing the same way.

- **Multi-turn amplifies cache value — mind the TTL.** Follow-ups within the cache window read
  the ~57K prefix at **0.1×** base rate. Fernwood uses the default **5-minute** ephemeral TTL.
  Within a single field sitting, Mom's turns are likely <5 min apart → cache hits. If she
  pauses longer, the next turn re-pays the full prefix. Anthropic's **1-hour TTL**
  (`cache_control: {type: "ephemeral", ttl: "1h"}`) costs **2× on write** and needs **≥3
  reads inside the hour** to beat the 5m option. **Recommendation: stay on 5m for now**; only
  test 1h if telemetry shows follow-up turns routinely landing 5–60 min apart. At ~$5/mo the
  stakes are tiny either way — don't optimize ahead of the data.
  ([Anthropic prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching),
  [caching cost guide 2026](https://jobsbyculture.com/blog/prompt-caching-engineers-guide-2026))

- **Keep dynamic content in Layer 3.** The `suggest-log` routing, the observed-on date, the
  asked-about observation — all per-call, all belong in the live-state (Layer 3) block, never
  the cached prefix (`fernwood.md`: three-layer geometry). Adding the log behavior is a
  *system-prompt* change (Layer 1, stays cached) — that's free per-turn after the first write.

- **Digest-size line still holds.** Stuffing is fine until digest >80K or observations >50
  entries; as field notes accumulate (and if Phase G ever folds them into the digest), watch
  the 80K breakpoint and migrate to tool-use retrieval then, not now.

---

## Dependencies to hand off (not in my scope)

- **engineering:** the deterministic observation-write endpoint (or reuse of `fnSaveAll` /
  the observations KV path); the forced-tool-use migration of both fences; **photo
  persistence for a logged observation** — the analysis's forensic note shows
  `leanTurnForStorage` already strips the image block from the saved conversation, so if a
  logged note should keep its photo, that needs a home decided (text-only note is fine for v1
  and needs nothing).
- **ux-expert:** the confirm surface — specifically whether the capture body is the verbatim
  turn or an editable-prefilled box the human trims (I recommend verbatim-with-optional-human-
  edit; **defer any AI-tidied prefill** pending Mom signal). Also the re-presented input box
  that unblocks follow-ups (the analysis's finding #1 — a surfacing fix, not a build).

---

## Punch list

1. Add the `WHEN THE READER WANTS TO LOG AN OBSERVATION` section + the `suggest-log` fence
   contract to `GARDEN_GURU_SYSTEM` (changes #1–#5 above).
2. Front-end: on `suggest-log`, render "Add to the Almanac?"; on confirm, deterministically
   write the **reader's own turn text** + confirmed `speciesId` + date via the existing
   AI-free observations path. No AI in the write.
3. Wire the creeping-fig intent case (`noteType: "intent"`, `speciesId: null`) — this closes
   the dead-end that became Paul's manual `plants.json` edit.
4. (Durable) migrate `suggest-species` **and** `suggest-log` to forced tool-use with typed
   schemas — the schema is the capture-boundary guard.
5. Keep Haiku + 5m cache TTL; revisit TTL only if follow-up-gap telemetry warrants.
6. Confirm with Mom (her interview / behavior) whether "tell the journal" and "ask the guru"
   feel like one action or two — the analysis flags this as the open question that this design
   answers with "one box, one utterance, two trust-classed destinations."
