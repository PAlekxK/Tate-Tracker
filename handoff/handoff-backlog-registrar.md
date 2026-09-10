# Handoff: backlog-registrar

<!-- generated 2026-09-10 ~7:15 PM ET · source: Tate-Tracker@27d4f1a (verify vs HEAD before trusting status) -->

## 1. Mission

**You are the BACKLOG REGISTRAR — a standing lane, created by Paul today.** His words:

> *"A backlog rationalization and maintenance session, since there are so many work items… a **standing
> expert** that's helping keep track of everything and that they can all **forward their updates to**
> and questions and so on, and help identify **how we can package work together**."*
> — and later: *"let's just put that in our backlog so we don't have too many things roaming around."*

⭐ **You are `BACKLOG.md`'s SOLE WRITER, as a SCRIBE — not an author.** Lanes forward rows to you; you
transcribe them **verbatim, attributed to the lane and its sha**. You flag and propose in your own
clearly-marked voice, separately. ⛔ **You never author a status, never re-tier, never delete, never
split a section** (splitting is a judgment edit, not a move).

**The load-bearing property:** every status in the file becomes attributable to **the lane that measured
it** — strictly stronger than before, where a status was attributable to whichever session last had the
file open.

## 2. Why you exist as a WINDOW and not a subagent

You ran today as a subagent of the coordinating session and **lanes could not message you** — a zones
lane tried and could not find you, so the coordinator had to relay by hand. **Forward-to requires a peer
session.** Paul approved you as your own window. **That is the whole point: lanes address you directly.**

## 3. Read first — you wrote most of this

- `.plans/2026-09-10-backlog-registrar-PROPOSAL.md` — **your own charter** (`e7352b7`, corrected `1699865`)
- `.plans/2026-09-10-PLAN-OF-RECORD.md` — the spine. **⑥c is the live lane board; ⑥e is your stub**
- `.plans/2026-09-10-G1-RULING-PACKET.md` — what Paul owes, ranked
- `.plans/2026-09-10-backlog-management-AUDIT.md` — a `practice-steward` audit **running now** on
  *"how do we manage the backlog intelligently"* + the product-steward trial. ⛔ **Do not duplicate it**
- `BACKLOG.md` (4,327 lines) · `OBJECTIVES.md` (15 lines) · `.decisions/` (22 cards) · `VOCABULARY.md`

## 4. Your standing findings — carried forward, all yours

1. 🔴 **The register lies to its own instrument.** One link syntax, `→ READY ·`, welded to a status
   `BACKLOG.md:14` defines as *"cleared by Paul."* **Four live rows write it and disclaim it in prose the
   tool cannot see** (`:139`, `:248`, `:1441`, `:3297`). ⛔ **You refused to write four more and were
   right.** Fix is `.decisions/fernwood-22.md` option (c): a status-free `→ PLAN ·` syntax. **④ in the
   packet, Paul's.**
2. 🔴 **The register has learned to explain away its own alarm** — three plans say *in their own headers*
   that the orphan flag is expected and is not a defect to repair.
3. ⚠️ **"28 orphans" is a one-directional predicate**, not a finding — 18 declare a `row:` in their own
   header; `POINTER_PAT` only looks at the BACKLOG side.
4. ⭐ **The cadence, corrected after your own spec failed its own test:**
   ```
   Backlog-Register: <BACKLOG section or row> — <what changed in one clause>
   Backlog-Forwarded-By: <lane> @ <sha>        # only when transcribing another lane's status
   ```
   ⛔ **Same final paragraph as `Co-Authored-By:`, no blank line** — git parses trailers only from the
   last paragraph. **Sweep with the parse, never `--grep`:**
   `git log --format='%h %(trailers:key=Backlog-Register,valueonly)' | grep -v '^[0-9a-f]* *$'`
   ⚠️ `Register:` was rejected — already double-booked by `eac5648`, and it was never a trailer at all.
   **Recorded as rejected with its reason so nobody re-proposes it.**
   ⚠️ **A trailer registers what was COMMITTED.** Your sweep must **print what it could not place**, never
   drop silently.

## 5. Open on your desk

- **The `Backlog-Register:` format has NOT reached the lanes.** ⭐ **Now that you are a window, tell them
  yourself.** Lanes: `tate-tracker-ec` · `onboarding-ask-b3` · `paulkirschenbauer-b8` · the walk-harness
  lane · the coordinator (`tate-tracker-af`).
- **A live production defect owed a row** — `viewer.html:18481`'s sentence-case regex matches **1 of 5**
  `soon` labels; *"You put Papers and documents first."* renders today. `onboarding-ask-b3` measured all
  five. **Owed whichever way Paul rules on the reframe** — it is not part of that packet.
- **Paul's wording ruling** (keep `Gardening`; ship the address clause + four contract lines) and the
  ⭐ **evidence correction** that carries it: the *"Houseplants!"* signal was **Paul's own account**
  (`pkirsch`, Grant Park Condo); `.user-research/2026-09-08-localized-feed-and-property-type.md:401`
  already said *"Paul's twelfth interest"* and two 09-10 docs re-narrated it anonymously.
- **The product-steward trial** — your verdict was *renew one round conditionally, or kill*; the
  `practice-steward` audit now has it.

## 6. ⛔ Two things only PAUL can close

1. ⭐ **`BACKLOG.md` is written by TWO existing loops (mom + fleet).** You are a **third** writer unless
   they forward too. **One door, or it isn't a door.**
2. **Is a `-PROPOSAL` a DOCUMENT or an ITEM?** ⑥ in the packet. One ruling discharges **10 orphans**, most
   of the 22 ungraded suffixes, and the expected-orphan habit.

## 7. Guardrails

⛔ Never `git push origin main` · never deploy · nothing outbound · never write another lane's files
(`worker/worker.js`, `viewer.html`, `onboarding/index.html`, `homes/index.html`, `tools/journey-*.py`,
`tools/publish-digest.py`, `zones.json`). **Route cross-lane through the coordinator, `tate-tracker-af`.**
⚠️ `cycle/release/cycle-state.json` is generated output touched by a post-commit hook — **never commit it.**

⭐ **A relayed claim is a hypothesis. Fourteen have failed verification in this thread today** — three of
the coordinator's, one of yours, three in a single brief. **Measure before asserting; label inference as
inference.** ⭐ **Grep, then read the line** — a count locates, it does not establish. And the day's
sharpest correction, from a lane about itself: **verify a reversibility promise against the actual route
back before writing it.**

## 8. Your own falsifier

You wrote it: *"a discipline that needs a second tool open is the one nobody follows."* **If no lane has
forwarded you anything in a working session, the door is not a door and you should say so rather than
sweeping an empty inbox.**
