# Handoff: fernwood-coordination
<!-- generated 2026-09-10 ~3:55 PM ET · sources: Tate-Tracker@7a4c109 [testing-arch@7586225 · backlog-rat@988a682 · onboarding-ask@cb5e46a] · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission
Coordinate four Fernwood build windows toward Paul's **READY TO INVITE** milestone. You hold no
authority the windows don't — you hold the **boundary**, and that is the only thing that lives
nowhere else.

## 2. Read first
- `.plans/2026-09-10-PLAN-OF-RECORD.md` — **the spine.** ① the milestone · ①c the standing
  elicitation lens · ② the readiness bar and holds · ④ the ruled model · ⑤ the sequence ·
  ⭐ **⑥b COORDINATION STATE** (authority boundary, one-writer-per-file, the relayed-claim hazard) · ⑦ open
- `.plans/2026-09-10-rationalization-PROPOSAL.md` (on `backlog-rat`) — **Paul has not read it.** Its
  §3 MOVE 1 + §4 band are one change; §7.4 stamps its own counts as already-stale
- ⭐ **`handoff/handoff-testing-architecture.md` — ON THE `testing-arch` BRANCH, not on `main`.** That
  window wrote its own 94-line handoff (`6f71e46`) plus the day's control lesson into `CLAUDE.md`
  (`ec28b57`). **You will not find either by reading `main`** — `git show testing-arch:handoff/handoff-testing-architecture.md`
- `.plans/2026-09-10-account-estate-model-SCOPE.md` §9 · `.plans/2026-09-10-testing-architecture-PLAN.md` §6

## 3. Next steps (ordered)
1. ⚠️ **STALE AS WRITTEN — re-measure before acting. `ListAgents` is the instrument.** When this was
   written both onboarding sessions read `waiting`; the first successor measured them **`busy`**.
   **Two keypresses were owed by Paul, not you:** close `onboarding-ask-b3` (duplicate of
   `onboarding-ask-82`, both in one worktree — my error), then clear the prompt the survivor is
   showing. Both read `waiting`; nothing has been written in either. **Ask before diagnosing.**
2. **Take the windows' parked reports** — `tate-tracker-ec` and `testing-arch-e2` were each asked for
   a state paragraph **and explicitly what they tried that did NOT work.** Fold both into ⑥b.
3. **Put the rationalization proposal to Paul** — one move, whole freeze block → ruling register.
4. **Then the four decisions in §5 below are his**, in that order.

## 4. State & pointers
| window | branch | state |
|---|---|---|
| `tate-tracker-ec` | `main` @ `7a4c109` | **clean, parked.** A1·A2·personFor·identity fix·election fix·`via:`·fixture stamp all landed |
| `testing-arch-e2` | `testing-arch` @ `7586225` | 12+ commits, mid fixture-lifecycle. **Not merged — merging is a milestone precondition, route it** |
| `onboarding-ask-82` | `onboarding-ask` @ `cb5e46a` | **0 commits.** Blocked. Brief + addendum at `~/.claude/handoff/brief-onboarding-activities.md` |
| `backlog-rat-3a` | `backlog-rat` @ `988a682` | **done.** Proposal committed, nothing applied |

⚠️ **UNCOMMITTED:** `backlog-rat`'s worktree holds a deliberately-untracked stale copy of the plan of
record — **do not commit it**; it would fork the document three windows steer by.

## 5. Guardrails — ⛔ these wait for Paul
- `git push origin main` — Mom's frozen production, 681/22 divergent. **Never, for any reason.**
- **Sending any invite** — outbound, and it IS the milestone.
- **Deploy to `home`** — Mom's estate. `paul` is authorized; `home` is not.
- **B3 `POST /api/estate`** — bound to the grant-key ruling; opens on his word.
- **The estate-place-record architecture call** — the build session recommends an estate gets its own
  place written once at founding rather than elected from members. I agree. **Unruled.**
- **Why Paul's real home address sits in `est-qa0001`** — his to rule, not to tidy.
- **One writer per file.** Cross-lane requests route through you; no window reaches into another's.

## 6. Done when
Paul sends two invites. Everything else is a precondition. ⭐ The milestone is an **event**, not a
state — *"we've done all the plumbing and infrastructure work we know of, and now we're ready to start
working on user-facing features."* It is also the gate that OPENS feature work.

## 7. Un-sealed judgment — NOT on disk anywhere else
- **B3 got bigger when Paul bound the grant re-key to it.** It is now the largest remaining item AND
  the only completely unexercised step — nobody has ever founded an estate through the product.
- **The founding journey (J0) is declared-but-unbuilt** and is a milestone precondition: *tested means
  walked*, and nothing walks the path Aida and Nigel must take.
- ⭐ **`other` — the ranking screen's catch-all — is uncovered by every seat**, and it is *"the only
  line where someone can name a need we never anticipated."* Do not let anyone dismiss it as a
  false positive; the testing window nearly did.
- **My read that the onboarding windows are on a trust prompt is INFERRED, not verified.**
- **Three fixes today were the same shape** — `via:`, `attributeToPerson`, the fixture stamp: *record
  provenance at write time rather than infer it at read time*. Expect the fourth.

## 7b. WHAT WAS TRIED AND DID NOT WORK — from the build window, verbatim-in-substance
⭐ **Read this before proposing anything in the credential/account path — every item below is a dead
option that looks alive.**
- **The first placement fix would have skipped exactly the rows needing it** — it looked up only
  `account:<personId>`, so an account written before Q1 (the condo's, precisely) reads absent and is
  silently left alone. ⭐ *A migration's repair path has to reach the un-migrated.*
- **Relaxing `attributeTo`'s guard** was the obvious fix and was wrong — its both-facts-from-one-row
  rule is what makes *"everything Mom said"* and *"everything about the condo"* separately answerable.
  Absence needed a **third state**, not a loosened second.
- **`check-estate-neutral.py` cannot certify neutrality.** It passed the canon-election bug clean on
  311 needles because **every needle is Fernwood's.**
- **Electing an estate's place from member rows** — removed, not improved. **No tie-break turns *"a
  member has an address"* into *"this estate is at this place."***
- **`need()` throwing on a missing fact** — right when every deployment was Fernwood, wrong the moment
  a household has an address and nothing else.
- ⚠️ **The stale edge fooled this session three times** — filtered deploy output hiding a stale upload,
  a wrong hostname read as a dead Worker, 500s from pre-fix code still being served. **Re-probe what is
  live; debugging the source is the trap.**

⚠️ **AND A CORRECTION TO §4: `via:` IS PARTIAL — 3 of 6 authored write paths.** `conversation` and
`observations` need a signature change through `handleChat`; `door` is `personId: null` by construction
and **correctly excluded**. It blocks nothing, but do not read "landed" as "complete."

⚠️ **`worker/digest.json` ≠ the per-estate digests.** `build-digest.py` builds Fernwood's bundled canon
from repo-root strict canon; `publish-digest.py` composes per-estate digests into KV. Different paths —
the election fix could not have touched the first. I confused these; don't repeat it.

## 7c. AMENDMENTS FROM THE FIRST READBACK GRADE — `2026-09-10 ~4:10 PM ET`

**⛔ CORRECTION — A2 IS COMPLETE, NOT PARTIAL.** The first successor read `canonIsThisEstate` = 1 and
`CANON_FOREIGN_OK` = 2 and concluded the retirements had not landed. **All three hits are inside the
COMMENT BLOCK explaining the deletion** (`worker.js:111,119,124`). Both are genuinely gone; the guard
is `canonFor`'s stamp comparison, which is stronger. ⭐ **This is the day's own lesson biting the
reader who quoted it** — *a count is not a mechanism*. **Grep, then read the line.**

**⭐ WHERE YOU RUN, AND WHO YOU ARE — this was missing and it blocks you.**
You **replace** `paulkirschenbauer-5d` as coordinator. Run in the **main worktree**
(`~/Developer/Tate-Tracker`). The outgoing coordinator **stops committing at this amendment** — it
wrote this file and nothing further. Once Paul clears that window you are the only writer in the
tree. **Until he does, do not commit.** The first successor was right to refuse and right to name it.

**⭐ THE STALL INSTRUMENT IS `ListAgents`** — busy / idle / waiting, per session. ⑥b says a closed
window and a blocked one look identical from outside and does not say what to use instead. **This is
what to use.** The commit-watchdog is a *stall* detector, not a *cause* detector, and it was itself
wrong twice today. **Run `ListAgents` before concluding anything about a window, and ask Paul before
diagnosing — he can see the window; you cannot.**

**⭐ THE COORDINATOR'S OWN FALSIFIER** — asked for and missing, and the question is fair:
> **Coordination has stopped being useful when the windows stop needing routing** — when no
> cross-lane request has come through in a working session, when no window has been corrected by
> another, and when Paul is answering gates faster than they are being composed. **At that point the
> windows should talk to Paul directly and this role should stand down.** ⚠️ Today it was *not* met:
> six relayed claims failed verification, three cross-lane routings were needed, and two windows
> corrected each other through this seat.

**⚠️ `backlog-rat`'s worktree has a MODIFIED TRACKED file too** — `cycle/release/cycle-state.json`
(`candidate_sha` 8d17e4e → 196e146). §4 warns only about the untracked plan copy. It reads as
generated output from `release-state.py`, not authored work. **Leave it; don't commit it.**

**⚠️ The rationalization proposal's §7.2 is itself out of date** — it says `SCOPE`'s Q6 is
byte-unchanged and calls it *"the more consequential half, still open."* It was fixed at `0e0926c`.
**The document about things reading as current when they aren't now has that property.** Say so when
you put it to Paul.

**⚠️ Step 2 of §3 is substantially DONE** — §7b folds in `tate-tracker-ec`'s parked report and
`e802b7d` points at `testing-arch`'s. Don't go asking for reports already on the page.

**🔴 AND THE FINDING THE FIRST SUCCESSOR SURFACED THAT THIS BRIEF DID NOT CONTAIN — verify it, then
raise it:** `publish-digest.py --check` now reports six of seven estates **cannot build — no
estate-level place record**. If that holds, **A1 is blocked on the unruled estate-place-record
architecture call**, which makes the readiness bar gated on a decision sitting in §5 as a guardrail
rather than on the sequence. It is a consequence of the election fix landing (electing a place from
member rows was *removed*, not replaced). ⚠️ **Labelled by its author as inference, not measurement** —
confirm against `household_property()` before putting it to Paul as fact.

## 8. Trust status
**Human-cleared (Paul, today):** the G1/READY-TO-INVITE wording · personalization inside · five owners
incl. himself · person-scoped credentials · `X-Estate` as disambiguator (ratified **knowing it retires
falsifier clause C2**) · usernames unique per deployment · `reader` capability · door records
deployment-scoped · `via:` stamp · Guru-working-at-launch + Aida/Nigel **held** · the nigel/aida
deletion (**reversed** from the morning kill — both events recorded in `cb5e46a`).

**⛔ MODEL-FLAGGED, NOT CLEARED — do not treat as fact:**
- the **1Password/Anthropic partnership** — from a voice note, unverified, marked so in `BACKLOG.md`
- the **iNaturalist redundancy** question — unexamined
- the **estate-place-record** proposal — engineering's recommendation, Paul has not ruled
- the testing window's **seat-portfolio hypotheses** — emitted as hypotheses with falsifiers, by design
- ⚠️ **SIX relayed claims failed verification today; three were mine.** Every one was caught by the
  *receiving* window measuring rather than accepting. **A relayed claim is a hypothesis.** The worst
  — *"no walk has ever entered J3"* — I relayed three times and verified zero.
