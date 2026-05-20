# Fernwood — User Research

This directory holds user-research artifacts for Fernwood. They are written by the `user-researcher` agent (`~/.claude/agents/user-researcher.md`) and consumed by other agents — especially the `ux-expert`, which pulls from here to ground its reviews in audience.

## What's here

- **`persona-mom.md`** — Proto-persona for Mom. Make-or-break user. Joint primary alongside Paul.
- **`persona-paul-co-steward.md`** — Proto-persona for Paul as co-steward / builder-user. Names the structural risk of the builder being one of the users.
- **`jtbd-invest-time-well.md`** — Jobs-to-be-Done card for the underlying joint job ("invest finite time well on a place that matters"), with four forces (push / pull / anxiety / habit). Performed by both personas.
- **`jtbd-talk-to-the-property.md`** — JTBD card for the *inner* job Phase E introduces ("collapse the gap between noticing and knowing"). Sits inside the parent invest-time-well job, doesn't replace it. Three performers: Paul-mobile, Paul-desktop, Mom.
- **`journey-unified-field-assistant.md`** — Journey map across the three Phase E performers at the unified field-assistant surface. Names where the journeys overlap (one surface, voice rules, depth filter) and where they diverge (latency tolerance, reply shape, cost of failure).

## Who this is for

- **Paul** — to keep his audience model explicit, sourced, and revisable rather than carried in his head.
- **The `ux-expert` agent** — to populate the `user_context` block of its UX review JSON. Expected locations: `persona-*.md`, `jtbd-*.md`, `journey-*.md`. The ux-expert respects evidence tags (`assumption | inferred | validated`) and does not treat `assumption` material as ground truth.
- **Future agents** (`content-steward`, `voice-steward`) — same handoff pattern.

## Evidence tags

Every claim is tagged:

- **`assumption`** — Paul's hunch, the agent's inference, or material from desk research.
- **`inferred`** — supported by indirect signals (Paul's notes, behavior in related domains, project doctrine).
- **`validated`** — confirmed by direct observation or interview with a real person who fits the profile. Cites source.

These tags are non-negotiable. If a claim isn't tagged, it shouldn't be in the artifact.

## Behavioral validation pending (caveat)

These artifacts are built on Paul's direct words and on the user-researcher's synthesis of project doctrine. They have **not** been validated by direct conversation with Mom or by observed behavior in the app. Most claims are `inferred`, not `validated`.

What would move claims to `validated`:

- A direct conversation with Mom — Mom Test-style, asking about past behavior (what she actually reaches for now, when she last looked something up about the property, how she's felt about apps she's tried), not hypothetical futures.
- Observed app behavior in the first 30 days after launch — does Mom open it unprompted? How often? From where?
- A switching-moment interview (Bob Moesta-style) about a tool she last reached for to do part of this job.

Until that happens, treat these artifacts as a structured working hypothesis. They are good enough to guide design decisions; they are not good enough to override what Mom actually does once she has the app in hand.

## Residual unknowns (status)

- **Ambient vs. deliberate use** — *partially resolved (2026-05-11).* Ambient is now a confirmed real mode for Mom: phone, in bed, morning coffee or winding down, leisure-reading posture. Deliberate at-property use (porch, kitchen, in-the-moment lookup) remains `inferred` and not yet observed.
- **Appreciation as a standalone job (vs. only the appreciation half of a unified dual job)** — *mixed signal (2026-05-11), still not validated.* The bed/coffee context can serve both jobs lightly: appreciation as leisure-reading *and* low-commitment previewing of tomorrow's stewardship (what to do, what's blooming, weather). The standalone-appreciation case is **not** strengthened after all. Worth checking with Mom directly before splitting the JTBD card.
- **Which triggers actually fire first** — open. Bed-leisure-reading is a strong candidate but not the only one.
- **Mobile vs. desktop split** — open; bed/coffee context further reinforces phone-first, but doesn't rule out occasional desk use.

## Maintenance

- Last updated: 2026-05-11.
- Artifact `last_updated` and `evidence_level` fields are the source of truth for freshness.
- Open Questions sections in each artifact track the gaps the user-researcher knows about. Closing those gaps requires real-user input.
