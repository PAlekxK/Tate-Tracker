---
type: persona
project: tate-tracker
person_id: mom
last_updated: 2026-05-27
evidence_level: validated
sources:
  - Paul direct (multiple sessions, 2026-05 series)
  - Tate Tracker CLAUDE.md (project tone + user notes)
  - ~/.claude/agent-foundations/_about-paul.md (Tate Tracker user context)
  - .audit/2026-05-26-telemetry-rollup.md (first real-usage telemetry, 6-day window 2026-05-20..2026-05-27, likely-Mom device d-14nyhnjz-...)
---

# Mom — Make-or-break user

The user whose adoption decides whether Fernwood is worth building at all. Joint primary user with Paul. Not technophobic, but the adoption hurdle is real: anything the app asks of her has to feel earned, not imposed.

**Status update 2026-05-27 (telemetry):** Adoption is no longer hypothetical. The `d-14nyhnjz-...` device — viewport 393x793 (iPhone Pro), 27 sessions / 341 events over 6 days, the only device that touched the A/A+ text-size toggle (12 events) — is best read as Mom's. Confirmation step is still Paul-sights-her-phone, but every behavioral signal lines up. The persona below now distinguishes what telemetry *validates*, what it *demotes*, and what it *flags* as newly unknown.

**Status update 2026-07-02 (40-day conversation-content read):** The window extended from 6 days to ~40, and we now read the actual turn *content*, not just event counts. See `.user-research/2026-07-02-mom-behavior-interpretation.md` for the full read. Headlines:
- `[validated]` **Adoption is durable, not a spike.** Active 27 of ~40 days *through today*; ran a photo-bearing Guru conversation today. The 2026-05-27 "Guru-becomes-pattern: NOT YET" and the 4-day-silence worry are both retired — Guru use is now an **emerging pattern**, not a one-off.
- `[validated]` **Her Guru questions are the stewardship-lookup the rubric predicted** — fertilize/transplant timing, soil amendment, ID, seasonal diagnosis. None idle.
- `[inferred, single-observation]` **A new job the persona didn't hold:** log a *seasonal change on a plant she already knows* + diagnose + get advice, in one breath (today's lily-pad utterance). Distinct from Job 3 (ID the unknown) and Job 5 (promote a new species). N=1, probable-Mom; verification Q's drafted to firm it up. It currently dead-ends into Paul's manual work.
- `[contested]` **The anti-persona "multi-turn probably misses her" causal claim is softened** — the only 2-turn conversation in the whole corpus (5/28 creeping-fig, probable-Mom) was her *trying to continue* and hitting a UI wall, not choosing to stop. She's still not a chain-eight-follow-ups user; but "doesn't follow up" ≠ "doesn't want to."
- Device→Mom remains `[inferred, strong]`, still awaiting a Paul-sights-her-phone confirmation.

## Situation

`[inferred]` — Lives the property day-to-day in a way Paul (Atlanta-based) doesn't. Notices what's blooming, what's broken, what needs attention — but currently holds that knowledge in her head and her memory of past seasons, not in any shared system. The app is being introduced into an already-working life, not filling a desperate gap. That asymmetry matters: she doesn't *need* it; it has to earn its place.

`[validated — 2026-05-27]` — **Use is daily and recurring**, not occasional. 27 sessions over 6 days = ~4.5 sessions/day on the likely-Mom device. The "the app has to earn its place" framing held — and the app has earned it, at least at the open-the-thing level. Source: `.audit/2026-05-26-telemetry-rollup.md` engagement-by-device table.

`[inferred — partially validated 2026-05-27]` — Use is likely off-property too, not only at-property. Phone in bed with morning coffee or at night winding down — a leisure-mode reading session, not a deliberate stewardship task at a desk. The dashboard is competing with whatever else she'd reach for on her phone in those moments. (Source: Paul direct 2026-05-11.) **2026-05-27 update:** telemetry confirms phone-as-surface (iPhone Pro viewport, mobile device class) and confirms daily cadence consistent with morning/evening pull-ups, but does NOT yet validate the specific bed-and-coffee posture — that requires direct conversation with Mom. Session times per event would help if Paul wants to look at the hour-of-day distribution.

## Job-to-be-done

`[inferred]` — Enjoy and steward the property well, without the act of stewarding becoming work she resents. Wants to feel confident — knowing what's happening this month, what's coming, what each plant needs — and wants the noticing of the place (birds at the feeders, frogs at the pond, the seasons turning) to feel rewarding rather than instrumentalized.

`[validated — 2026-05-27]` — **The dashboard's at-a-glance cards carry most of the job.** Per telemetry: Plants and Weather tied for most-viewed (60 views each on likely-Mom device); Wildlife at 54; Celestial 47; Property 45. Card-section-viewed dominates the event mix (194 of 341 events ≈ 57%). She is scanning the cards, not deep-diving. The "lay out the place at a glance" job is the one Fernwood currently serves best. Source: `.audit/2026-05-26-telemetry-rollup.md` card-popularity table.

`[validated — 2026-05-27]` — **She returns to saved entries at scale.** 55 `entry_revisited` events on her device alone (104 across all devices) vs. 0 stars. Revisit-as-curation is the actual behavior; the star affordance is not part of how she uses the app. The "this matters" interaction exists — it's just expressed as "I come back to this entry," not as "I tap a star." See updated open questions below.

## Triggers

`[inferred]` — **Morning coffee, in bed, waking up.** Phone-in-hand, low-attention. Looking for something interesting to read while the day starts — *and* potentially previewing the day ahead: what's worth doing on the property, what's blooming, what the weather looks like. Soft stewardship-flavored, not deliberate task-checking. (Source: Paul direct 2026-05-11.) Still `inferred` — telemetry shows daily phone use but doesn't tag time-of-day to the bed/coffee posture specifically.

`[inferred]` — **Evening wind-down, in bed, powering down.** Same posture, same low-attention mode. Leisure-reading *and* a low-commitment glance at what's coming tomorrow on the property. End of day, forward-look without obligation. (Source: Paul direct 2026-05-11.)

`[inferred]` — Other likely entry points: noticing something on the grounds and wanting to know more (a bird she doesn't recognize, a plant past its best moment); a seasonal shift ("what should I be doing now that it's May?"); Paul mentioning something he's added or updated. Anti-trigger: a notification telling her something is "due" or "overdue." That kind of nudge will close the app, not open it.

`[inferred — strengthened 2026-05-27]` — **The "what's new" / "what got promoted" pull is real.** Two image-bearing Garden Guru conversations on her device led to 1 `species_id_confirmed` and 1 `species_promoted` (Spiderwort, 5/22). She's not just reading — she has put species into the canon. Source: `.audit/2026-05-26-telemetry-rollup.md` event-types table.

## Constraints

- `[inferred]` — A simple, easy-to-remember password is acceptable. Low-friction authentication is the real constraint; password-free is not required. (Original "no password / Mom stops" hypothesis was contradicted by Paul on 2026-05-11: *"We could have a password. I don't think there's anything wrong with that. It would just need to be very easy to remember. I don't think there's a lot of confidential information there."*)
- `[inferred]` — Not gun shy about tech, but won't pursue a tool that has friction relative to the value she gets from it. The bar is "compelling enough to open" — not "tolerable to use once open." **Strengthened 2026-05-27:** the bar has been cleared. The compelling-enough-to-open question is answered by 27 sessions in 6 days.
- `[validated — 2026-05-27]` — **Mobile-only realistically.** Telemetry shows zero desktop activity from her device pool; viewport 393x793 (iPhone Pro). The earlier "porch or kitchen, not at a desk" reading was correct. Promoted from `inferred` to `validated`.
- `[assumption]` — Time and attention are scarce; she's not going to read long blocks of text or work through multi-step interactions.
- `[inferred]` — **Low-attention reading posture is a real use mode.** Bed, one-handed, reclined, half-engaged (waking up or winding down). Design has to read well at half-engagement — scannable, light cognitive load, no multi-step interactions, no tiny tap targets. (Source: Paul direct 2026-05-11.) **2026-05-27:** the 2-turn ceiling on all 10 Garden Guru conversations is consistent with low-attention posture — she's not getting drawn into multi-turn exchanges. (Could also mean the assistant isn't pulling her in — see open questions.)
- `[validated — 2026-05-27, promoted from validated-inline]` — **Mom has a hard time reading and may not use the app with reading glasses on.** Now backed by direct usage: 12 `text_size_changed` events on her device — the *only* device that touched the A/A+ toggle Paul shipped 5/22 for exactly this reason. The accessibility constraint isn't just a stated preference; she is actively reaching for the affordance designed for it. Implication unchanged: small body copy, faint helper text, and meaning carried by text labels alone are accessibility failures here. Icon + size + color must carry intent independently of fine print. (Original source: Paul direct 2026-05-22. Behavioral confirmation: `.audit/2026-05-26-telemetry-rollup.md`.)

## Definition of success

`[validated — strengthened 2026-05-27]` — "I open the dashboard when I want to, and I'm glad I did." The bar is dashboard engagement — she finds herself reaching for it unprompted (to check what's happening this month, to identify a bird, to remember which plant gets pruned when) and it pays off without making her feel managed. **Garden Guru engagement is upside, not the bar**; she doesn't need to use the assistant surface for the project to be working for her. The outcome ladder is: dashboard-opened-regularly (pass) → Guru-tried-once (gradient up) → Guru-becomes-pattern (gradient up further). Failure is dashboard-not-opened, full stop. (Source: Paul direct 2026-05-20, Garden Guru rubric interview Q11.)

**2026-05-27 status:**
- Dashboard-opened-regularly: ✅ PASS — 27 sessions / 6 days.
- Guru-tried-once: ✅ PASS — 2 conversations, both with images, 1 species promoted to canon.
- Guru-becomes-pattern: ❌ NOT YET — 2 conversations over 6 days isn't a pattern; both happened on or before 5/22; nothing in the last 3 days of the window.

The headline: the project is succeeding at its load-bearing metric. Garden Guru is alive but not yet habit.

## Anti-persona

`[inferred]` — The productivity-app user who wants checklists, streaks, completion percentages, and reminder pings. Mom is not that user, and designing for that user breaks this one. Also not the casual visitor who's just curious about the property — Mom has a real stake in it, and the app should treat her as someone whose knowledge of the place exceeds what's in the app, not the other way around.

`[inferred — added 2026-05-27; causal claim CONTESTED 2026-07-02]` — Also not the "power-user conversationalist" who chains 8 follow-ups with the AI. Telemetry: her conversations are single-turn. She asks; she gets an answer; she stops. **BUT — the 2026-07-02 content read contests *why*.** The only 2-turn conversation in the entire corpus (5/28, probable-Mom, "our journal") was her *trying to continue* — to add a plant — and hitting a dead-ending UI, not choosing to be done. So "she doesn't follow up" can no longer be read as "she doesn't want to"; behavior can't separate *didn't want to* from *couldn't find how* (verification Q1 is built to). She is still not a chain-eight-turns user, and the low-attention posture is real — so the anti-persona holds in spirit. What's dropped is the confident inference that affordances assuming any continuation "probably miss her." A *re-presented input box after a reply* (a surfacing fix, not a chat-history browser) may be exactly what her one blocked follow-up wanted.

## Evidence log

- `2026-07-02: [validated] — 2026-07-02 Garden Guru conversation analysis (40-day window + turn content) — d-14nyhnjz active 27 of ~40 days through today, photo-bearing Guru conversation today. Durable adoption; novelty-decay and 4-day-silence worries retired; Guru is an emerging pattern.`
- `2026-07-02: [validated] — same — her full Guru question corpus is property-stewardship shaped (fertilize/transplant/amend/ID/seasonal-diagnosis). Confirms the eval-rubric Q5 wedge as her real Guru job.`
- `2026-07-02: [inferred, single-observation] — same — today's lily-pad utterance fuses log + diagnose + advise on an already-known plant. Candidate NEW job distinct from Job 3 (ID) and Job 5 (promote species). N=1, probable-Mom; dead-ended into Paul's manual INQUIRIES.md entry (commit b0d728f). Verification questions drafted.`
- `2026-07-02: [contested] — same — the only 2-turn conversation in the corpus (5/28 creeping-fig, probable-Mom "our journal") was a user trying to CONTINUE and hitting a UI wall. Softens the 2026-05-27 anti-persona multi-turn causal claim; the single-turn pattern may be a dead-ending UI, not disposition.`
- `2026-05-27: [validated] — Telemetry rollup (.audit/2026-05-26-telemetry-rollup.md) — likely-Mom device d-14nyhnjz-... shows 27 sessions / 341 events over 6 days. Adoption is real. The single strongest validation event since project start.`
- `2026-05-27: [validated] — Telemetry rollup — 12 text_size_changed events on her device (only device that used the A/A+ toggle). The no-reading-glasses constraint is now behaviorally validated, not just stated.`
- `2026-05-27: [validated] — Telemetry rollup — All 2 of her Garden Guru conversations are 2-turn. Multi-turn engagement is not part of her pattern (yet).`
- `2026-05-27: [validated] — Telemetry rollup — 0 stars in 55 entry_revisited events on her device (0 across 104 revisits all-devices). The star affordance is not part of how she uses the app. Revisit-as-curation IS the behavior; tapping a star is not.`
- `2026-05-27: [inferred — instrumentation gap] — Telemetry rollup — 27 session_starts vs 1 session_end on her device. iOS Safari is not reliably firing the unload-style handler; retention/engagement metrics derived from session_end will undercount her. Not a behavioral signal about her — a measurement gap.`
- `2026-05-27: [validated] — Telemetry rollup — Plants (60) and Weather (60) are most-viewed cards on her device. Wildlife (54), Celestial (47), Property (45). Field-notes is 43 views with 18 expands (highest expand-rate) — when she opens field-notes, she opens deeply.`
- `2026-05-22: [validated] — Paul direct, real-user observation — Mom asked a question of Garden Guru via the new two-button surface (shipped same day, commit 5de6e1b). The exact failure mode from earlier that day (text-only questions silently logged to the Almanac under the auto-routing single button) did not reproduce.`
- `2026-05-22: [validated] — Paul direct — Mom has a hard time reading; may use the app without reading glasses on. UX needs accessibility-first treatment: large legible type, high contrast, icons/shape/color carrying meaning independently of label text.` *(Now behaviorally validated by 2026-05-27 telemetry — see above.)*
- `2026-05-11: [inferred] — Paul direct — Mom likely uses the app in bed with morning coffee (waking up) or at night (winding down), looking for "something interesting to read." First concrete when/where for her solo use. Off-property, phone, leisure mode, low-attention.`
- `2026-05-11: [inferred] — Paul direct — A simple, memorable password is acceptable; low-friction auth is the real constraint. (Supersedes earlier "no password / Mom stops" assumption — contradicted by Paul this session.)`
- `2026-05-11: [inferred] — Paul direct — Mom is not gun shy about tech.` *(Re-sourced: the literal phrase "not gun shy" was Paul's, used in reference to plants/pruning. The Mom-and-tech read is the user-researcher's synthesis from Paul's broader framing of Mom as a real user, not a technophobe.)*
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q11 — dashboard engagement is the load-bearing success metric; Garden Guru engagement is gradient, not gate. Mom-uses-dashboard-without-Guru = success; Mom-stops-opening-dashboard = failure regardless of Guru usage.`
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q4 — Mom is already a Claude power-user with the photos-for-ID workflow. She has named "building up an understanding with Claude of the context specific to where our home is and the wildlife and weather there" as the difference maker. This makes Garden Guru a competitor to a tool she's already happy with, not a tool she's reaching for unprompted.`
- `2026-05-08: [validated] — Paul direct, project CLAUDE.md, foundation — Mom is the make-or-break user; if she doesn't adopt, the project fails.`
- `2026-05-08: [validated] — Paul direct, project CLAUDE.md — Tone must be field-journal, not task-manager; urgency language ("17 actions due," "3 alerts," "overdue") is wrong for this project.`
- `2026-05-07: [validated] — Paul direct — Photo aesthetic is naturalistic in-habitat shots; museum-specimen white-background photos are wrong.`

## Open questions

Updated 2026-05-27. Items that telemetry closed are removed; items it opened are added.

### Closed by telemetry (was open at 2026-05-22)
- ~~Behavioral: in the first 30 days after launch, does Mom open the app unprompted? How often?~~ → **YES, ~4.5 sessions/day on the likely-Mom device. Closed.**
- ~~Mobile vs. desktop split: is the porch-and-kitchen mobile model correct?~~ → **Mobile-only confirmed. Closed.**

### Still open from prior sessions
- Auth: what does "easy to remember" mean for her specifically — a family word, a shared phrase, a 4-digit code? Worth a single direct conversation before implementing.
- Which triggers actually fire first: is it noticing-something-on-the-grounds (the field-journal motive) or seasonal-orientation ("what should I be doing in May") that pulls her in first? Per-event timestamps could partially answer this (time-of-day distribution), but the cleanest answer is still asking her.

### New questions opened by 2026-05-27 telemetry
- **Why zero stars in 55 revisits?** Three candidate explanations:
  1. *Star is invisible.* The affordance is there but she doesn't see it (size, color, position fail). Implies a UX iteration.
  2. *Entries aren't experienced as discrete things to mark.* She reads them but doesn't think of them as objects-to-curate. Implies the star is conceptually wrong, not visually wrong.
  3. *Revisit IS her curation.* She comes back to entries she values; tapping a star to also say "I value this" is redundant. Implies the star should be killed or replaced with a passive "you came back to this 4 times" surfacing.
  
  These three look different in implication. Distinguishing them needs either a Mom conversation or instrumentation that captures *where her eyes go* on an entry card (not feasible without screen recording, which would be invasive). T+30 interview is the realistic path. Priority: high.

- **Why all 2-turn Garden Guru conversations?** Two candidates:
  1. *Two turns are enough.* The answers are good enough that she doesn't need to follow up. Implies Guru is working as intended for her use mode.
  2. *Two turns are all she has patience for.* The follow-up affordance isn't compelling, or she doesn't realize multi-turn is possible. Implies a discoverability issue OR a use-mode mismatch (her job-to-be-done with Guru is one-shot Q&A, not conversation).
  
  Distinguishable in a T+30 interview by asking about a specific recent question and what she did with the answer. Priority: medium.

- **What happens in the 4 days between her last Guru conversation (5/22) and the end of the window (5/27)?** She's using the dashboard daily but not Guru. Has the novelty worn off? Is the use case (photo ID) seasonal and she just hasn't seen something unfamiliar this week? Or is there something about the affordance that isn't pulling her back? Priority: medium — wait for a longer window before reading too much into 4 days.

- **The `session_end` instrumentation gap.** 27 starts vs 1 end on iOS Safari. Mostly an engineering issue (consider `visibilitychange` instead of `unload`), but worth knowing it distorts any retention metric that depends on session_end firing. Flagged here so the user-research artifacts don't accidentally cite "session length" as if it's reliable for her device. Priority: low (engineering decision).

- **Did she notice the "Worth Considering" card that shipped 5/26 (4 expands on 5 views across all devices, including her pick — autumn bentgrass)?** Card popularity table shows 5 views / 4 expands but doesn't split by device in the published rollup. If she's expanding it and has touched the bentgrass entry that's labeled her pick, that's a strong signal of co-authorship she'll respond to. Worth a check next rollup. Priority: medium.
