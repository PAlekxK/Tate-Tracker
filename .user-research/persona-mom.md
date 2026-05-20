---
type: persona
project: tate-tracker
person_id: mom
last_updated: 2026-05-11
evidence_level: inferred
sources:
  - Paul direct (multiple sessions, 2026-05 series)
  - Tate Tracker CLAUDE.md (project tone + user notes)
  - ~/.claude/agent-foundations/_about-paul.md (Tate Tracker user context)
---

# Mom — Make-or-break user

The user whose adoption decides whether Tate Tracker is worth building at all. Joint primary user with Paul. Not technophobic, but the adoption hurdle is real: anything the app asks of her has to feel earned, not imposed.

## Situation

`[inferred]` — Lives the property day-to-day in a way Paul (Atlanta-based) doesn't. Notices what's blooming, what's broken, what needs attention — but currently holds that knowledge in her head and her memory of past seasons, not in any shared system. The app is being introduced into an already-working life, not filling a desperate gap. That asymmetry matters: she doesn't *need* it; it has to earn its place.

`[inferred]` — Use is likely off-property too, not only at-property. Phone in bed with morning coffee or at night winding down — a leisure-mode reading session, not a deliberate stewardship task at a desk. The dashboard is competing with whatever else she'd reach for on her phone in those moments. (Source: Paul direct 2026-05-11.)

## Job-to-be-done

`[inferred]` — Enjoy and steward the property well, without the act of stewarding becoming work she resents. Wants to feel confident — knowing what's happening this month, what's coming, what each plant needs — and wants the noticing of the place (birds at the feeders, frogs at the pond, the seasons turning) to feel rewarding rather than instrumentalized.

## Triggers

`[inferred]` — **Morning coffee, in bed, waking up.** Phone-in-hand, low-attention. Looking for something interesting to read while the day starts — *and* potentially previewing the day ahead: what's worth doing on the property, what's blooming, what the weather looks like. Soft stewardship-flavored, not deliberate task-checking. (Source: Paul direct 2026-05-11.)

`[inferred]` — **Evening wind-down, in bed, powering down.** Same posture, same low-attention mode. Leisure-reading *and* a low-commitment glance at what's coming tomorrow on the property. End of day, forward-look without obligation. (Source: Paul direct 2026-05-11.)

`[inferred]` — Other likely entry points: noticing something on the grounds and wanting to know more (a bird she doesn't recognize, a plant past its best moment); a seasonal shift ("what should I be doing now that it's May?"); Paul mentioning something he's added or updated. Anti-trigger: a notification telling her something is "due" or "overdue." That kind of nudge will close the app, not open it.

## Constraints

- `[inferred]` — A simple, easy-to-remember password is acceptable. Low-friction authentication is the real constraint; password-free is not required. (Original "no password / Mom stops" hypothesis was contradicted by Paul on 2026-05-11: *"We could have a password. I don't think there's anything wrong with that. It would just need to be very easy to remember. I don't think there's a lot of confidential information there."*)
- `[inferred]` — Not gun shy about tech, but won't pursue a tool that has friction relative to the value she gets from it. The bar is "compelling enough to open" — not "tolerable to use once open."
- `[inferred]` — Mobile-first realistically. She'll open this from a phone on the porch or in the kitchen, not at a desk.
- `[assumption]` — Time and attention are scarce; she's not going to read long blocks of text or work through multi-step interactions.
- `[inferred]` — **Low-attention reading posture is a real use mode.** Bed, one-handed, reclined, half-engaged (waking up or winding down). Design has to read well at half-engagement — scannable, light cognitive load, no multi-step interactions, no tiny tap targets. (Source: Paul direct 2026-05-11.)

## Definition of success

`[validated, inline]` — "I open the **dashboard** when I want to, and I'm glad I did." The bar is dashboard engagement — she finds herself reaching for it unprompted (to check what's happening this month, to identify a bird, to remember which plant gets pruned when) and it pays off without making her feel managed. **Garden Guru engagement is upside, not the bar**; she doesn't need to use the assistant surface for the project to be working for her. The outcome ladder is: dashboard-opened-regularly (pass) → Guru-tried-once (gradient up) → Guru-becomes-pattern (gradient up further). Failure is dashboard-not-opened, full stop. (Source: Paul direct 2026-05-20, Garden Guru rubric interview Q11: *"if she uses the dashboard but doesn't use the guru, that's still a success. And it's a failure either way if she doesn't open the dashboard."*)

## Anti-persona

`[inferred]` — The productivity-app user who wants checklists, streaks, completion percentages, and reminder pings. Mom is not that user, and designing for that user breaks this one. Also not the casual visitor who's just curious about the property — Mom has a real stake in it, and the app should treat her as someone whose knowledge of the place exceeds what's in the app, not the other way around.

## Evidence log

- `2026-05-11: [inferred] — Paul direct — Mom likely uses the app in bed with morning coffee (waking up) or at night (winding down), looking for "something interesting to read." First concrete when/where for her solo use. Off-property, phone, leisure mode, low-attention.`
- `2026-05-11: [inferred] — Paul direct — A simple, memorable password is acceptable; low-friction auth is the real constraint. (Supersedes earlier "no password / Mom stops" assumption — contradicted by Paul this session.)`
- `2026-05-11: [inferred] — Paul direct — Mom is not gun shy about tech.` *(Re-sourced: the literal phrase "not gun shy" was Paul's, used in reference to plants/pruning. The Mom-and-tech read is the user-researcher's synthesis from Paul's broader framing of Mom as a real user, not a technophobe.)*
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q11 — dashboard engagement is the load-bearing success metric; Garden Guru engagement is gradient, not gate. Mom-uses-dashboard-without-Guru = success; Mom-stops-opening-dashboard = failure regardless of Guru usage.`
- `2026-05-20: [validated, inline] — Paul direct, Garden Guru rubric interview Q4 — Mom is already a Claude power-user with the photos-for-ID workflow. She has named "building up an understanding with Claude of the context specific to where our home is and the wildlife and weather there" as the difference maker. This makes Garden Guru a competitor to a tool she's already happy with, not a tool she's reaching for unprompted.`
- `2026-05-08: [validated] — Paul direct, project CLAUDE.md, foundation — Mom is the make-or-break user; if she doesn't adopt, the project fails.`
- `2026-05-08: [validated] — Paul direct, project CLAUDE.md — Tone must be field-journal, not task-manager; urgency language ("17 actions due," "3 alerts," "overdue") is wrong for this project.`
- `2026-05-07: [validated] — Paul direct — Photo aesthetic is naturalistic in-habitat shots; museum-specimen white-background photos are wrong.`

## Open questions (real-user validation pending)

- Behavioral: in the first 30 days after launch, does Mom open the app unprompted? How often? From where?
- Auth: what does "easy to remember" mean for her specifically — a family word, a shared phrase, a 4-digit code? Worth a single direct conversation before implementing.
- Mobile vs. desktop split: is the porch-and-kitchen mobile model correct, or does she sometimes use it more deliberately at a desk?
- Which triggers actually fire: is it noticing-something-on-the-grounds (the field-journal motive) or seasonal-orientation ("what should I be doing in May") that pulls her in first?
