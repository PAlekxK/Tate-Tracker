# Zone-journey front door — five-lens panel synthesis (design + hypotheses)

**Date:** 2026-07-17 · **Repo HEAD at synthesis:** `1c39eb0` · **Status:** DESIGN + HYPOTHESES ONLY — no build this pass (Paul's call).
**Single entry point** for the panel that scoped the W3 voice-capture *front door*. Master brief; links the five lens returns below.

## The question Paul raised
W3 shipped 7/17: on the property map, tap a zone → speak "what's growing here?" → durable AI-free `/api/zone-audio`. But it is **discovery-dependent** — Mom won't navigate into the (collapsed, buried) map to find it. Paul: add a **prompt card at position 1 of the existing carousel** (the most important card) that *invites* her into a short guided journey to talk through the zones, landing on the already-built capture. Run the expert team **with hypotheses** so we learn from how she interacts, and keep it **trackable + automated**.

**Paul's two framing decisions (this session):** (1) design + hypotheses first, then build; (2) the panel decides the flow shape (one-zone vs. sweep) as a hypothesis, not a pre-commit.

## The five lenses (source returns)
- **user-researcher** — JTBD + card-level journey map + n≈2 validation traps.
- **ux-expert** — the position-1 card's look/feel + the in-flow interaction (the zone-pick is the make-or-break moment) + the honest close.
- **engineering-partner** — build by reusing the card-queue mechanism (launcher = *head-line*, not a stepper item) + the instrumentation schema.
- **content-steward** — the copy (invitation, gate, per-zone prompt, close), variants.
- **ai-advisor** — the ask/capture AI boundary + the automated learning loop + the one strategic risk.

---

## Where all five converged (high confidence)

1. **Ship the minimal instrumented invite FIRST; let the data earn the fuller journey.** Independently flagged by 4 of 5 (user-researcher, engineering, ai-advisor, ux) against the *same* doctrine — [[feedback_defer_affordances_pending_signal]], the star-trap, n≈2. A heavy multi-step "journey" built on a capture surface with ~0 demonstrated engagement is the affordance-without-signal trap. **Point the automation at the learning loop, not at an elaborate live UI.**

2. **One-zone-at-a-time, NOT a sweep** — with an *optional* "another spot?" that lets sweep behavior **emerge and be measured** rather than be assumed. All five. Reasons: matches Mom's proven one-card carousel rhythm; a single zone is a complete, satisfying unit at half-engagement; a sweep reintroduces a counted sequence (the task-manager shape the field-journal doctrine bans); it's the smaller build. Paul's "capture as many as possible" instinct is **tested as H2**, not shipped.

3. **The card is a *front door / launcher*, structurally distinct from the confirm cards.** Confirm cards ask a Yes/No fact (three peer buttons). The front door *launches a flow* → **one forward primary action** + one quiet dismiss. That single-primary-vs-three-choice asymmetry is itself the signal (readable without reading the words) that this card is different. Engineering: implement it as a **head-line** that mirrors the existing general-feedback foot-line (authored, singleton, never-answered, handled *outside* the confirm stepper) — **not** as a new kind inside the stepper, which would entangle it with the answer/retire machinery in ~4 places.

4. **The zone-pick is the highest-risk moment — and it must NOT be raw polygon-hunting** (ux's *critical* finding). Today, picking a zone = hunting small text-labeled polygons on a noisy leaf-off aerial (and `fairway` + `parking-bank` have empty geometry, so they don't render at all). That is exactly the interaction Mom's accessibility model rules out. **Re-express the pick as the one-at-a-time stepper she already owns:** one zone name large in serif + its color swatch + its patch highlighted on the map above + one big **🎤 "Tell me about this spot"** + `‹ ›` to move. Sourced from **all** zones (named list includes the empty-geometry ones; they just don't get a highlight until Paul redraws). This solves the accessible-pick problem *and* embodies the one-zone hypothesis by construction.

5. **The gate is a button, not a screen.** Collapse "invite → ready-gate → map" into ONE moment: the invitation card's two buttons *are* the gate. No separate "are you ready?" interstitial (over-scaffolding). The one legitimate job of a gate — set expectation + pre-warn the OS mic-permission dialog — becomes a framing line on the card, not a screen.

6. **The close is "heard," not falsely "filed."** Drive the ✓ from the *real* `zone_audio_saved` 2xx result, reusing the existing honest-ack copy. The success screen of a guided flow is the single most tempting place to re-introduce the 2026-07-15 silent-lie ("All done ✓" with nothing saved). Audio is too big for the localStorage outbox, so offline = honest "couldn't save, try again," never a false close. Then one gentle, equal-weight next move ("Another spot ›" / "All done for now").

7. **"Trackable + automated" = put the automation in the INSTRUMENT, not the affordance.** The automation Paul wants lives in instrumentation + a read/summarizer + adjudication — mirroring the Mama's-Perspective harvest→fold machine — while the user-facing affordance stays minimal until the numbers justify more.

8. **The AI boundary already governs this** (the 2026-07-14 rule, unchanged): capture stays AI-free; the one *new* wrinkle is **live sequencing must be deterministic** (which zone next = a code set-difference of un-talked zones), never a live AI pick to Mom mid-flow — because "analyze the record" is blessed only *behind Paul's gate*, and a live flow can't pause for the gate. Behavioral metrics (taps, timings, zoneIds, durations) are capture-path-legal; her *voice/words* are the thing no model may touch before storage.

9. **Reuse existing plumbing; don't spawn parallels.** The grow recorder is already right (route the flow's mic straight into it, zone pre-selected). Extend `mom-queue-watch.py` to also see new zone-audio blobs (don't build a third watcher). `read-mom-zone-audio.py --pickup` is already wired into session-start.

10. **This absorbs the deferred W3 follow-ons.** "Promote map to position 1" + "house-voice line" = *this card*. The 4-week time-box = the H1 kill/keep window. **W6 (instance model) is NOT unblocked** and must not pretend to be — the journey captures audio only and assigns **no `zoneId` to canon**; folding stays Paul's off-device call. W6 keeps blocking the deeper "inventory against the 26 plants" work, not this.

---

## The recommended flow (v1 — the smallest version that tests H1 *honestly*)

> Note: v1 is a touch larger than "invite → existing map → existing tap-pick → mic" because the **accessible zone-pick must be in v1** — if v1 makes her hunt polygons and she abandons, we've *confounded* "the invitation doesn't work" (H1) with "the pick is inaccessible." The correct minimal removes that confound.

1. **Front-door card** at carousel position 1 — permanent, never retires (a standing door). Calm journal-green accent (not a fill, not an alert color), the destination's own **🎤 "What's growing here?"** glyph, one evocative serif invite line, **one primary button** + one quiet dismiss, and a one-line expectation/mic-permission pre-warn. *Tests H1, H3.*
2. **One-zone stepper pick** — one zone at a time: name large + color swatch + patch highlighted on the map above + big **🎤 "Tell me about this spot"** + `‹ ›`. Sourced from all zones. *Tests H2 + the accessible-pick question.*
3. **Speak** — reuse the existing grow recorder unchanged (30s cap, AI-free `/api/zone-audio`, honest acks).
4. **Close** — honest ✓ ("Saved — thank you ✓" only on real 2xx) + "Another spot ›" / "All done," return to carousel with the door still at position 1. *Tests H5.*
5. **Instrument the funnel** (below) + the read tool. **Do not build:** a gate screen, a dedicated sweep mode, a "what you've recorded" tracker, any AI.

**Copy (content-steward's picks — choose before any string ships):**
- Invite headline: *"You know these gardens better than I do."* (sub: *"When you've got a minute, tell me about one — in your own words. I'll listen."*) — flips *being tested* → *being consulted*.
- Gate buttons: **"I've got a minute"** / **"Another day"** (decline presumes a return, never reads as failure).
- Per-zone prompt: *"When you're out in the [Western Garden], what would you point out to me?"* (pulls the plants *she'd* single out; no quiz pressure).
- Close: *"Got it — that's the [Western Garden] in your words now. Come tell me about another whenever you like."* (lands ownership; open door, no counter). **No "in the record ✓"** until capture is verified — promise *heard*, not *filed*.

---

## Hypotheses & signals register — the trackable artifact

The automation Paul asked for. Each hypothesis has a prediction, the deterministic signal that settles it, and a pre-registered verdict so we read *counts*, not a story. All signals ride `MetricsCollector → /api/metrics` (behavioral, capture-path-legal) — **never** `/api/feedback` or `/api/zone-audio` (her words). The one new field that makes it work: **`flowId`** — a per-attempt id minted on the launcher tap, threaded through every step, so one walk stitches into one journey (don't infer journeys from timestamps under her multi-device reality).

| # | Hypothesis | Predict | Watch (event → field) | Verdict rule |
|---|---|---|---|---|
| **H1** | She won't engage the mic without the invitation; the invitation *is* the instrument. | Zone captures appear only once the card ships; organic map-discovery stays ~0. | `launcher_offered/viewed/tapped` vs. `zone_audio_saved` with entry-path = card vs. organic. Baseline = W3 shipped 7/17, discovery-only. | Post-card captures ~all follow a card tap, baseline ≈ 0 → **holds**. |
| **H2** | One-zone yields richer capture + higher completion than a sweep. | ~1 (occasionally 2) zones/session, each a real spoken note. | zones-per-`flowId`; `durationMs` ordered within a flow; where a multi-zone attempt stops. | Reliable 1 + occasional "another" → one-zone-with-optional-continue right; routine 4–5 with non-declining duration → sweep earns promotion. |
| **H3** | The light button-gate lifts completion vs. dropping her on the map. | High tap→saved completion; little pre-speech abandonment. | `launcher_tapped → flow_zone_picked → zone_audio_started → zone_audio_saved` drop-off. | Most who tap "I've got a minute" reach a saved capture → gate sufficient; heavy mid-flow drop → expectation-setting too thin. |
| **H4** | Voice beats any typed affordance for her. | Voice captures complete; the typed general field stays ~0. | voice-capture completion vs. general-field engagement. | Near-refuted already (0-for-3 on text/standing controls); watch for contradiction. |
| **H5** | She returns across days only if each sitting is short + closes with a visible "saved." | A later-day return with a fresh capture. | repeat `zone_audio_saved` across distinct calendar days from one `deviceId`; offer→save latency (`firstOfferedAt`). | A second-day return with a new capture validates H5 **and** the whole front-door thesis (mirrors the Mama's-Perspective Grow signal). |

**Funnel events to add** (extend `MetricsCollector`): `launcher_offered` (`position`), `launcher_viewed` (IntersectionObserver — the star's fatal ambiguity was no view signal), `launcher_tapped` (mint `flowId`), `flow_zone_picked` (`flowId`, `zoneId`), and **add `flowId` to the existing** `zone_audio_started` / `zone_audio_saved` (+ `durationMs`), `flow_closed` (`flowId`, `completed`, `lastStep`, `saveResult`). Return-on-a-later-day needs no new event (existing `ts` + stable `deviceId`).

**The read tool is part of "automated," not optional.** `/api/metrics` is written but analysis is manual today. Add a small `read-mom-funnel.py` (or extend `analyze-fernwood.py`) computing offered→viewed→tapped→saved + later-day-return count, reported against the **4-week time-box** start date. Extend `mom-queue-watch.py` (same 9am/7pm launchd job) to also surface "N new zone recordings waiting."

**Program-level verdict (deterministic, pre-registered — AI never writes it):**
- **GROW** — she starts unprompted across ≥2 reseed cycles AND ≥N zones get durable recordings AND ≥1 recording folds to canon (loop closed end-to-end at least once) → then build the fuller journey / summarizer surface.
- **KILL** — offered ≥X times, started 0; or started once, never returned (the Mama's-Perspective hard-kill shape).
- **HOLD** — everything between; the honest default at low n (abstention is a valid forced answer).

---

## The AI boundary for this feature (unchanged rule, applied)
- **May touch (Paul-gated):** draft invite/journey copy (but prefer the deterministic template bank first); off-device, post-storage, summarize ONE stored recording into ONE canon-candidate (plant→zone), flag-never-place; deterministically *screen* which zones are un-talked (set-difference — code, AI at most narrates).
- **Must NOT touch:** the capture itself; her raw voice through any model **before** storage (no transcribe-at-capture, no "clean up what she said"); **live journey sequencing** as an AI pick to Mom in real time; any transcript shown back to Mom; the Grow/Hold/Kill verdict.
- **At low n:** the summarizer is barred from cross-recording aggregation (one recording → one candidate); no "here's the pattern across her recordings" until ~15–20 (line-43 threshold). A transcript is a model read of her voice → a **hypothesis until Paul checks it against the audio** (model-read-flags-never-clears).

---

## Phased plan
- **v1** — the recommended flow above (front-door card + accessible one-zone stepper pick + existing recorder + honest close + funnel + read tool). Tests H1/H3/H5 + the accessible-pick question. 4-week time-box = the H1 kill/keep window.
- **v2 (gated on v1 lift)** — only if v1 shows the invite moves the needle: the richer journey affordances, the Paul-gated off-device summarizer seat, the weekly scorecard digest. Sequencing rule: **H1 before the journey** — don't polish a wizard nobody enters.
- **Not this pass:** any code (Paul's call). W6 instance-model stays blocking the deeper inventory work.

---

## Open decisions for Paul
1. **Head-line vs. carousel-dot (cosmetic/implementation fork).** Engineering recommends the launcher as a *head-line* above the confirm stepper (cleanest code; no carousel dot). Paul's words were "the first one" *in* the carousel. **Reconciliation:** render it at the top of `#mom-queue` as a standing, non-answerable card — reads as "the first, most important card" to Mom (Paul's intent) while staying out of the confirm answer-path (engineering's concern). The only open bit is cosmetic: does it get a carousel dot or sit visibly above the dots? **Recommend: above the dots** (it's a door, not one of a set to page through).
2. **Build v1 now, or hold at design?** This pass is design-only per your call. Say go to build v1.
3. **This absorbs + retires** the deferred W3 "promote map to position 1" + "house-voice line" items — confirm they fold into this rather than staying separate.

## Candidate principles (HELD as hypotheses — not written to any library this pass)
- **A front door is a card, not a wizard** — for a discoverable-only capability serving a non-exploring user, entry belongs at position 1 of a grammar she already knows, distinguished by *one forward action* (launches) vs *a choice* (asks). (ux)
- **For a text-difficult user, a spatial pick must reduce to a named, highlighted, one-at-a-time confirm.** (ux)
- **The gate is a button, not a screen.** (ux)
- **A launcher is a head-line, not a queue item** — reuse the mechanism's *shape*, not its answer-semantics. (engineering)
- **Behavioral telemetry is capture-path-legal; content is not.** (engineering/ai-advisor)
- **Stitch a multi-step flow with a per-attempt `flowId`; never infer journeys from timestamps.** (engineering)
- **A guided "close" screen is the most tempting place to re-introduce a false-success lie — drive it from the real write result.** (engineering)
- **Authored-content-to-Mom stays deterministic even when it reads the record** (live sequencing = code screen, not AI pick). (ai-advisor)
- **At low n, cap AI at one-item summary; script the verdict.** (ai-advisor)
- **Put the automation in the instrument, not the affordance.** (ai-advisor)
- **"You can't measure appetite for a feature a non-navigating user can't find — the invitation is the instrument."** (user-researcher)

Each wants a second occurrence before promotion ([[feedback_agent_proposals_not_validated]] + the 3-runs discipline).

## Cross-links
BACKLOG.md **W3** (this front-doors it), **W7** (confirm-card button layout — same carousel/input stack), **W5** (general-feedback box — the neighboring input surface), **W6** (instance model — stays blocked). Doctrine: [[feedback_defer_affordances_pending_signal]], [[feedback_no_ai_on_capture]], [[project_fernwood_mom_reading_accessibility]], [[project_tate_tracker_tone]], the "glance & the repository" governing principle + the loop's AI-free capture discipline.
