## fernwood-12 · does a non-plant `suggest-add` fence get built, or does the Guru refuse gracefully?

- project: Tate-Tracker
- loop: tate-tracker
- source: G1, found 2026-09-01 in the conversation that opened mom lap 8; interim shipped the same day (Worker `3cc3d422`)
- options: extend-the-fence-to-all-domains | leave-it-at-a-graceful-refusal

### Why it's here
Mom asked for the refrigerator under household systems, gave the model number, the ice maker and the
absence of a dispenser — and the Guru's closing turn told her **"It's in the record now."** Nothing had
been written. It has no path to canon. Had lap 8 not run within the half hour, her request would have
sat behind a completion message telling her it was handled.

⭐ **The diagnosis sharpened during the fix, and it is the reason this card exists.** The prohibition
*already existed twice* in `GARDEN_GURU_SYSTEM` — *"you NEVER say 'I've logged it'"* — but both copies
were scoped to the **journal/log** path. Her request went down the **add-a-new-thing** path, whose rule
is *"help them add it, honestly"* backed by a `<!--suggest-add` fence whose `kind` is **`plant`**. There
is no fence for machines, household systems, wildlife or zones. **So the real defect was a missing
MECHANISM, not a missing rule: a path with no honest exit produces a dishonest one.**

✅ Interim shipped: a domain-general ban on completion claims in any domain, plus an explicit note that
the fence is plants-only and what to do instead (reflect the facts back, say it is noted, stop).

### What it means
- **extend-the-fence-to-all-domains** — her request gets a real mechanism instead of a graceful
  refusal, and the thing she is demonstrably willing to do (talk to the Guru) starts producing
  structured proposals. ⚠️ It is **not** forbidden by the AI boundary — forbidden mode 2 is *AI
  auto-folding to canon*, and a fence is a **proposal for a human** — but it is a new surface on her
  ask path, and every domain needs its own grounding questions and schema.
- **leave-it-at-a-graceful-refusal** — the interim stands: the Guru gathers facts, reflects them back,
  says it is noted, and a human builds the card on the next lap. Honest, already shipped, and costs her
  a wait she cannot see.

### Recommendation
**extend-the-fence-to-all-domains**, but scope it to `household-system` and `vehicle`/`equipment`
first rather than all at once — those are the domains she has actually asked about, and the
refrigerator gives a worked example of exactly which grounding questions matter. ⚠️ Note the coupling:
this is the one option on the board that would make the Guru a *producer* of canon proposals, so it
should be decided **after** fernwood-11, not before — if the answer there is "latch onto what she
starts," this is how that gets built, and if it is not, this is a surface with no demand behind it.
