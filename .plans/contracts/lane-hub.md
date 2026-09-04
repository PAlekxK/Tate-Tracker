# LANE HUB — the seat that holds the run

## STATUS: OPEN — run 2. RELEASE CONDITION: every lane CLOSED or explicitly re-carried, AND every 🔶 OPEN-no-owner row in the ledger assigned, minted, or dated into the next run.

Written 2026-09-04 on practice-steward's finding that the hub was the only seat in the run with
**no contract, no gate and no release condition** — while every lane had all three on disk.

## OWNS
- `.plans/contracts/` — this directory: the ledger, the preamble, every lane contract, `lane-watch.py`

⭐ **Why this file makes the watcher honest.** `lane-watch.py` lists every written path matching no
lane's OWNS. Before this file existed that list held **7 legitimate hub writes** and grew with every
one — *an alarm that is on by construction*, which is the thing you never install. With
`.plans/contracts/` declared here, a clean run reports zero strays and a genuine stray becomes
visible. No code change was needed: `owns()` already keys on `lane-*.md`.

## MUST NOT TOUCH
Any path in any live lane's OWNS.

⛔ **A LANE READS ITS CONTRACT ONCE, AT SPAWN.** The hub may rewrite a live lane's `## STATUS`
line — that is for the watcher and for humans, not for the lane. It may **NOT** change a live
lane's OWNS, MUST NOT TOUCH, task or GATE: the lane will never re-read it, so the file would
describe a contract nobody is operating under, and nothing detects the gap. **Changing those means
respawning the lane, not editing the file.**

> *Found by audit, not by luck.* This hub edited three LIVE lanes' contracts at 15:00 (`3623bbb`)
> while all three sessions were running. The edit was a `## STATUS` line only — harmless in content,
> and permitted by the rule above. **The hazard is the class, not that instance.** Written down
> because the next hub will not be that lucky.

## DUTIES — the four this run actually exercised
1. **Filter, don't relay.** Every lane question comes here first; most die here. Only a true gate
   reaches Paul — and the **LANE** asks him, in its own tab, where the context is. You tell him
   **which tabs** are waiting, never the question.
2. **Verify every gate report; never relay one.** Re-derive each claim yourself and record what the
   verification caught in the ledger's register — including when it caught nothing.
3. **Read liveness before closing a run** (`lane-watch.py`). A disposition stays `unknown` until you
   have actually looked. ⚠️ Its VANISHED check compares **counts, not identities** — read the names.
4. **Take what a closing lane is carrying, explicitly**, into the ledger. A finding that lives only
   in a closing session's context is the thing that gets lost.

## GATE
The run's ledger, with every lane at a terminal disposition and **no orphan left unowned**. The
release condition's second clause exists because the `🔶 OPEN, no owner` register is currently
carried by nothing — when this hub closes, nobody reads it. That is the two-sided pre-registration
rule (`paul-stated 2026-09-01`: a pre-registration must also be **discharged**) applied to orphans.
