# Testing architecture — state of the window, 2026-09-10

Branch `testing-arch`, worktree `~/Developer/.tt-worktrees/testing-arch`, 14 commits off `main`.
⛔ **Not merged.** The merge is a milestone precondition and is routed by the coordinating session,
not taken unprompted.

## What the window was for

`.plans/2026-09-10-testing-architecture-PLAN.md` — split the JOURNEY from the READER. The brief said
ship P0 + P2 first. Both landed, and the plan's own headline claim turned out to be stale, which is
the first thing a successor should know: **verify a plan's claims before building on them.** Two of
its load-bearing statements were false by the time I read them.

## Built

| | |
|---|---|
| **P0** `b70c0a9` | A fresh walker arrives on an invite that has never been spent. 227 runs on record, not one of them an invited stranger. |
| **P2** `8da746f` | `walk-fixtures.py` — can a seat still enter the journey we think it walks. |
| **P1** `666a49a` | `JOURNEYS` as named data; J2 gets the walker it lost; `journey` + `lens` in the transcript. |
| **J0** `06be8bd` | Founding-owner declared as a standing coverage hole with its blocker (`POST /api/estate`, B3). |
| **J5** `fb883f2` | Bare-door built. Its first walk found a live defect. |
| gain | `e96296f` | The walk measures what the household GAINED. |
| lens | `8740605` `59ffbe4` | `elicitation-lens.py` — are we asking well. |
| canon | `928048d` | `check-canon-scope.py` — whose place is in this household's model prompt. |
| seats | `aa651cd` | `seat-portfolio.py` — are these the right seats. |
| fixtures | `7586225` `ec28b57` | `household-fixtures.py` — mint · list · tear down. |

Every tool has a `--selftest`; all green. Every new clause is proven by mutation, not by assertion
alone. All are wired into `CLAUDE.md`'s pickup block — a capability the loop cannot reach is not one.

## In flight / held

- ⛔ **The merge.** Routed by the coordinating session when the build side is ready.
- ⛔ **`publish-digest.household_property()`** — the canon-election defect below. Build session's file.
- ⛔ **The `/api/profile` write path** — fixed by the build session at `b09a80e` while I was measuring
  it. Their reconciliation is better than either of my two reports; read it.
- ⚠️ **`household-fixtures --teardown` refuses everything today** (201 rows: 1 person, 200 unmarked).
  That is correct. `31c7dec` landed the `fixture: true` stamp on `main`; this branch predates it, so
  the reader/writer agreement clause reads UNCHECKABLE rather than passing or failing. It resolves
  when the branches meet.
- ⚠️ **`.private/` here is a SYMLINK to the main tree's.** Identities are server-side accounts, not
  per-worktree, so sharing is correct — but it is shared mutable state.

## ⛔ WHAT DID NOT WORK — read this before re-deriving it

**① The elicitation lens's first run produced 16 findings and 13 were noise.** It counted **37 asked
fields** for a journey that asks ten — it swept in a feedback box, a composer textarea and file input
on three app stops, and contact radios — then flagged a RETURNING walk, which types nothing by
definition, for "asking 6 fields and gaining nothing", and printed the same ask three times because
three checkpoints photograph one screen. ⭐ **A lens that manufactures findings is worse than no lens:
it spends a reader's attention and teaches them to skim it.** The fix was to derive an ask from the
walk's own typing. **I nearly shipped the noisy version because its three real findings were real.**

**② J5's first walk was a false green.** The landing shot fired while `/api/session`'s PBKDF2 round
was still in flight, recorded the sign-in form as the destination, and reported **zero failed
actions**. A green run that had entered nothing. The fix had to live in the journey (`B03-signing-in`
as its own stop), not in `journey-view.py` — that tool is untouched by this work by design.

**③ I broke J2's fixture by walking it.** I built a durable unfinished identity for J2; the first J2
walk finished it, which IS the journey, and J2 had no fixture again twenty minutes later. ⭐ **A
journey that changes the world consumes its own entry state** — J1 spends its invite, J2 finishes its
record. Both are provisioned per run now. A durable J2 identity is a contradiction.

**④ My first canon-scope report asserted a direction it could not know.** It printed "qa carries
paul's name" and "paul carries qa's name" — two claims from one collision. It cannot know which
household is entitled to a place. *"At most one of them can be right"* is the strongest true claim.

**⑤ I proposed a field name for the fixture stamp and the writer shipped a different one.**
`syntheticFixtureRun` vs `fixture`. **The tool that reads never gets to name it** — adopt the written
one and keep your argument as a documented refinement, not a competing marker.

**⑥ A selftest clause that contained its own subject.** `"walk-invites" not in src` went red on the
line asserting it. Compute the needle, or ask the compiled function what it touches.

**⑦ I diagnosed a healthy deployment as a missing one** by probing `fernwood-paul` — `env.paul` and
`env.bob` are `myhome-<env>`. An hour. The host map is now borrowed from `post-deploy.py` instead of
being re-typed a third time.

## Open findings not mine to fix

1. 🔴 **A household's canon is elected by RANK from every placed row the estate holds.**
   `publish-digest.household_property()`; `est-qa0001` has 174 placed rows under 5 place names and it
   chose one — the only real person's among the synthetics. **A household is not a ranking**, and this
   is structurally guaranteed the moment a household has two placed people (`J7 second-member`).
2. ⚠️ **The address screen carries none of the ask contract** — no use, no not-use, no reversibility.
   Highest-leverage field in the product. Routed to the onboarding window.
3. ⚠️ **J0 founding-owner is unwalkable** and sits on the READY-TO-INVITE milestone.

## The rule to carry

⭐⭐ **A control can be entirely correct and still not cover the thing you rely on it for.** Three
instances in one day; written up in `CLAUDE.md` above the governing-design-principle section. Name
the question a control answers, name the question you are relying on it for, read them side by side.
