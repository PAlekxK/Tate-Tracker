# Readback — the STANDING BACKLOG SESSION (backlog-refinement)

<!-- written 2026-09-11 ~10:1x AM ET · read at HEAD d0016beb → 670eec3a → de0bd282 (moved three times during the read)
     Brief read: handoff/handoff-backlog-refinement.md, last touched at d0016beb (10:06), four vintages deep. -->

## 0. Stamp verification — and the thing the protocol nearly missed

The brief is **four documents in one file**, and its header stamp is the **oldest** thing in it:

| block | its own stamp | verified |
|---|---|---|
| §1–§7 | header: `2026-09-10 ~5:45 PM ET · Tate-Tracker@cf2a078` | `cf2a078` is an ancestor; **~17 h and hundreds of commits stale** |
| §8 | `2026-09-10 ~10:05 PM · 7631c34` | ancestor ✅ |
| §9 | `2026-09-11 ~3:55 AM · 7450b9d` | ancestor ✅ |
| §10 | written by the lap-8 coordination window | landed at `d0016beb`, 10:06 — **~1 minute before I read it** |

Every sha named (`cf2a078`, `7631c34`, `7450b9d`, `87c7aae`, `2010eee5`, `326791c`, `e5626b7`, `dcbc660`) is an ancestor of HEAD. Nothing is forked or orphaned. **So the brief is trustworthy — but a reader who verifies only the top stamp verifies the wrong block.** §9 says so explicitly (*"§6's task list is stale on its face; read §8 then this section, not §6"*), which is the correction working. I read §8 → §9 → §10 as authoritative and §1–§5 as standing mission text only.

⚠️ **Commit density measured:** 69 commits in the 22:00 hour, 40 in 17:00, 39 in the 09:00 hour. **HEAD moved three times in the ~8 minutes I spent reading.** The brief's own "half-life of about an hour" for a `file:line` is, at this cadence, generous.

## 1. What I understand this thread to be

A **standing, continuing conversation with Paul over `BACKLOG.md`** — not a build lane, not the coordinator. Three jobs:

1. **Refine rows** with Paul in real time, in his words, transcribed not authored.
2. **Keep the register honest** — carry forwards from the other live lanes into `BACKLOG.md`, with the `Backlog-Register:` / `Backlog-Forwarded-By:` trailer convention (verified: **231 commits** already use it).
3. **Maintain the derived two-lap queue** (`BACKLOG.md` § ⏭ THE NEXT TWO LAPS, line 95) that a build session pulls from at its commit phase.

The ownership seam §6 flagged is **resolved and I should not re-raise it**: §9 records `[paul-ruled "fold it in"]` — this window is the **ONE DOOR** to `BACKLOG.md`. The registrar lane's "sole scribe" reading was folded into this one.

⛔ The freeze is on the **pull**, not the document. One writer per file. Never `git push origin main`. Never commit `cycle/release/cycle-state.json` or `worker/digest.json`.

## 2. Current state as I measure it, not as the brief asserts it

- **Lap 7 CLOSED** at `87c7aae`, 09:51 EDT, production serving both real households. Confirmed in the chronicle at `:3618`.
- **Lap 8 HOLDS** for `.plans/2026-09-11-testing-revamp-PLAN.md`; **row T lands whole and FIRST** `[paul-ruled 09:47]`. This **supersedes** the 09:10 lap-9 placement, and therefore supersedes `CYCLE-LOG.md:3316` in the §10.A queue. Verified at `:3605`.
- `release-state.py` prints **ARMED · beat 11/12 · owner: paul · candidate `87c7aae`** — lap 7's residue, not lap 8. `check-backlog-ready.py --ladder` agrees: *"no lap is open — nothing is committed by ruling right now."* The two instruments are consistent.
- `check-backlog-drift.py`: **rested**, last rationalization today (0 d), 178-line head gap. The third rationalization landed. No grooming owed.
- `BACKLOG.md` is **4,899 lines**, 45 plan headers on the ladder, **20 proposals awaiting Paul's word**, 30 `.plans` suffixes graded by nothing.
- **The revamp plan** was untracked when I started and is committed as of `670eec3a` (*"the plan is written (44413e87)"*). It carries `stage: ready`, `ready: agent-proposed` — **Paul reads it before lap 8 opens.**

## 3. The open decision

**Whose call lap 8's opening is, and it is not mine.** The sequence as I read it: Paul reads the revamp plan → the lap-8 coordination window opens the lap → row T lands first in its beat-6 table. My window contributes the **register carries** so that table is built on rows that are true, and nothing else.

Beneath that, the decisions genuinely sitting with Paul (from §9, none blocking):
the lap-8 build plan's Q0–Q8 · the ask-design plan's §13 (fifteen rows) · lap 10's Q-10·2 and Q-10·5 · the product-name plan's `ready:` stamp · the receipt-first reorder of the weather card · the small-lap-9 shape.

## 4. What is NOT tested or verified — plainly

**By the outgoing window, declared:** the 174 qa accounts and 7 lab households (no KV read). Whether deploying the new Pages build to qa affects existing accounts. Every `file:line` older than an hour.

**By me, this session:**
- I ran **no** browser walk, **no** KV read, **no** deploy-adjacent check. Everything above is git, the chronicle, and four repo instruments.
- I did **not** read the twelve chronicle lines in §10.A — I verified the grep returns exactly those twelve line numbers and read `:3498`, `:3605` and `:3618`. The other nine are unread.
- I did **not** read the nine finding documents behind §10.C (`…-SECURITY.md`, `…-LENSES.md`, `…-SIZING.md`, `…-MODEL-POLICY.md`, the practice audit).
- §10.C's claim that **three of TIER 2 · 22's four items are done** is unverified by me. The row exists (line 305); whether the J3 fixture, field notes and bare door are actually done I did not probe.
- The teardown, row 33's collision, and the Worker-map state are all as the brief left them. I touched none of it.

## 5. Four things the brief left thin, or that look wrong

**① `W1–W11` is an ID COLLISION, and it is not cosmetic.** §10.B tells me to carry "Paul's walk W1–W11" as rows. `BACKLOG.md` **already uses `W0` through `W11`** as ids — the Track A zones/map series (`W2` = *Zones, Paul draws she reconciles*; `W9` = *Soil truth, test by zone*; `W2-SCHEMA`). Filing the walk findings under those labels would double-book twelve ids in the file whose whole job is to be the one true list. **`VOCABULARY.md` §4 doctrine says a double-booked key is exactly the failure to name before it lands.** I need a naming ruling before I carry §10.B — my recommendation is a distinct prefix (`PW1…PW11`, Paul's walk) and a one-line note at the series head saying why.

**② The §9 row-freeze has no recorded lift.** §9 declares a freeze on the lap-7 rows (TIER 1 · 45 · 42 · 26 · 27 · 28 · 29 · 30 · 31 · 43 · 44 · 32 · 23; TIER 2 · 10 · 13 · 18 · 19 · 20 · 21 · 25) *"until the coordinator lifts it."* **Lap 7 has since closed.** Every "frozen" mention in the chronicle is a **candidate** freeze (a build sha), not this row freeze, so I can find no lift. Several §10 carries land on frozen rows (TIER 1 · 25, TIER 1 · 41/46, TIER 2 · 22). **Does a lap's close lift its row freeze automatically, or does it need an explicit word?** I will not write to those rows until the lap-8 coordinator says.

**③ §10.C's "seat trails in a public repo" may be half-filed, and the halves are different claims.** `BACKLOG.md:1200` (the RULING REGISTER) closes *the surname* in two seat trails and pushed history as measured, no rewrite. SEC-R3-4 is a **different** claim: that seat artifacts as a class live in a public repo (.content 16 · .practice 3 · .engineering 83 · .user-research 48). The brief routes the standing rule to CLAUDE.md's AI-boundary section, with coordination editing CLAUDE.md and me filing the row. **I read those as two findings, not one already-closed one** — but the adjacency is close enough that I want it confirmed before I file a row next to a register line that looks like it.

**④ SEC-R4-1 is genuinely unfiled.** `fw-grant` / WebKit / SEC-R4 return **zero hits** in `BACKLOG.md`. So that carry is real work, not an already-closed box. By contrast **TIER 1 · 59 is filed** (line 276) — what is owed there is *running* the distinct-`questionId` count, not filing it. The §9 owes are a mix of "file it" and "run it" and the brief does not separate them.

**Thin, lower stakes:** §10.B cites *"the coordination brief §6"* without naming which file; three coordination briefs exist and I would be guessing (`handoff-fernwood-coordination-lap8.md` is my read). §10.C's nine findings are named by id only — each costs a document read I have not budgeted.

## 6. One live signal nobody in this thread owns

`read-mom-feedback.py --pickup`, run this session:
- **2 undispositioned arrivals** (1 Guru, 1 cards) — and the standing rule is that a disposition is **per record**, never per batch.
- **1 thing she told us that nothing has answered**: *(2026-09-06) "Vehicles"*.
- Her last card answer was **2026-08-20, 22 days ago** — past the 21-day `answer-age` threshold.

That is the mom-cycle's lane, not mine. I am naming it because the session-start block is run by whoever picks up this repo and this window is the one that ran it.

## 7. What I would do next, in order

1. **Put the two blockers to Paul as one short question each** — the `W1–W11` id collision (recommendation: `PW*`) and whether lap 7's close lifts its row freeze. Both are cheap and both gate writes.
2. **Carry §10.A** — read the nine unread chronicle lines in context, carry each as a forward, `git commit --only BACKLOG.md`, register trailer, abort guard (`test "$(git rev-parse --short HEAD)" = "<expected>" || exit`) before anything history-touching.
3. **Carry §10.C's unfiled findings**, starting with SEC-R4-1 (measured unfiled) and the UR-§5 two record shapes; probe each against the file before calling it open.
4. **Correct TIER 2 · 22's row** to say which of its four items are done, once verified — the brief says three are and the row does not.
5. **Regenerate § ⏭ THE NEXT TWO LAPS from `--ladder`**, never retype it, once lap 8's shape is known.
6. **Then hold open** for Paul's refinements as they come.

⛔ I will not touch `worker.js`, the HTML surfaces, the walk harness, or any `.plans/*-PLAN.md` a build lane owns. I will not rewrite another lane's status prose — flag and route only. I will not push.

## 8. Blind spots I am carrying forward

`git status BACKLOG.md` and a HEAD re-read before **every** write — three windows commit on this tree and HEAD moved three times during this readback. `registrar-sweep.py`'s matcher drops `§` and splits on `·`, so name a heading by its words. `.plans` `depends-on:` lines must be bare paths. A Bash heredoc of long quoted markdown can be refused by the auto-mode classifier — use Edit with anchored strings, or a Python line-range move for blocks. `wrangler kv key list` without `--remote` returns `[]` exit 0. `watch-feedback.py` prints a stale "checked Nh ago" line when it did not read.
