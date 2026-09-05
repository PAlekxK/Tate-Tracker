# onboarding · Account setup from a link — the transition Mom arrives through
- row: BACKLOG.md § ⭐⭐ THE DEVELOPMENT GOAL — Mom is the trial; the transition is a LINK, not a visit
- objective: O3
- class: engine · declared
- seats: user-researcher → ../fernwood-private/.user-research/2026-09-04-onboarding-journey.md
         ux-expert → ../fernwood-private/.ux-reviews/2026-09-05-account-creation.md
         engineering-partner → .engineering/2026-09-05-account-credential.md
         content-steward → waived: FOR NOW, and this is a DEBT not a judgement — every word on onboarding/index.html and the invite message is Mom-facing authored content and no content seat has read either; must not stay waived past gate 2
         ai-advisor → waived: naming and every first-run capture is deterministic by rule (capture stays AI-free); no model is on this path
- depends-on: .plans/2026-09-04-vocabulary-nicknames-PLAN.md
- depends-on: .plans/2026-09-03-c6-door-for-paul-PLAN.md
- depends-on: .plans/2026-09-04-three-environments-PLAN.md
- ready: [paul-approved 2026-09-05] — stamped in session, after reading it. THE DEVELOPMENT GOAL
  [paul-stated 2026-09-04 ~11:55 AM ET] authorises the work itself.
  ⚠️ The stamp does not rewrite the history: this file was still written AFTER the surface was already
  deployed to QA, and closing that drift is what it is for. The gate-1 walk it records ran BEFORE the
  stamp, not because of it.
- stage: qa
- wip-exception: this opens no new WIP. It gives an identity to work already deployed to QA, which
  under the ratified join key had nowhere to carry cascade state. Writing it lowers drift, not raises it.
- stage-note: GATE 1 WALKED 2026-09-05 ~4:15 AM ET on QA @ 408ff94 — evidence
  `.plans/walks/2026-09-05-onboarding-gate1.json`. Proof A (bare logic) 15/15 paths against the bytes
  QA serves, mutation suite 5/5. Proof B (functional) run un-primed, isolation plant PASSED.
  ⭐ It caught a P0 the reading never did: `step()` threw on EVERY call since a2b7b68 (`var show`
  shadowed `show()`), so the entire journey was down and the trailing `.catch` rendered the outage as
  "No connection right now." Fixed in 408ff94 with the masking defect. F1 (her address rendered as one
  run-on line on the confirm screen) fixed after the walk. Two of the walker's claims were REJECTED as
  harness artefacts on adjudication — see the artefact's `rejected` block before re-raising either.

## Files touched
- `onboarding/index.html` — the four views (`s1`–`s4`), the two failure screens (`s-wait`, `s-nolink`),
  the grant handoff out of the address bar, the address capture and its fingerprint.
- `worker/worker.js` — `/api/grant/whoami` (`:2919`, `:2924` — the 404 byte-identical to a missing
  route) and `POST /api/feedback` (`:2875`, the no-token write path the flow depends on).
- `tools/grant-mint.py` — the credential the link carries; G1/G2 refusals proven by `--selftest`.
- `tools/journey-logic.py` + `.js` — PROOF A of the gate-1 walk.
- `tools/journey-view.py` — the receiving side's viewer (host-scoped Access cookie).
- `instance/*.json` — identity and credential keys.

## Sequence
1. ✅ **The four views, on QA.** Shipped; walked end-to-end 2026-09-05.
2. ✅ **The link carries the credential** and it leaves the address bar on first load.
3. ✅ **Gate 1 runs on demand and leaves checkable evidence.** `journey-logic.py` + the walk artefact.
4. ⬜ **The account step** — `.engineering/2026-09-05-account-credential.md` has the design (an account
   row alongside the grant; `grantFor()` untouched). ⚠️ Ship the **A+ base size first**: activation
   research says the loudest new-phone failure is the words getting smaller, and login would be blamed
   for it. ⛔ **Model-recommended, NOT built, NOT ruled — Paul's.**
5. ⬜ **`personId` on the answer.** Measured 2026-09-05: TWO independent causes, and fixing either alone
   attributes nothing — (a) the page sends no `X-Grant` on the feedback POST (`index.html:505`);
   (b) the Worker routes that POST above the grant gate (`worker.js:2875`). ⛔ Capability model — Paul's.
6. ⬜ **Gate 2 — Paul walks it on lab, his own profile.** Never run.
7. ⬜ **Gate 3 — Mom.** The invite is Paul's own outbound act, gated, and it ends the hold.

## Falsifier
**If a gate-1 walk passes three consecutive journey changes while Paul at gate 2 finds anything the
walk could structurally have caught, the path table is testing its own expectations** — widen it by
exactly the file that carried the defect and record the move. Conversely, if the walk starts reporting
findings that adjudication rejects as harness artefacts more often than it reports real ones, the
harness is the product under test and the walk should be rebuilt, not tuned. (Lap 1 ran 2 rejected
against 1 confirmed plus 6 judgement findings — a ratio to watch, not yet a verdict.)

## QA
- `python3 tools/journey-logic.py --selftest` — 5/5 mutations caught, unmutated run clean. **Runs as
  beat 2's own precondition, every lap.** A suite that has only ever passed has proven nothing.
- `python3 tools/journey-logic.py` — 15/15 paths against the bytes QA actually serves. Fails closed on
  a wrong build, a non-`qa` env, or lab.
- `python3 tools/grant-mint.py --selftest` — G1/G2 refusals, and `--dry-run` proven byte-inert.
- ⛔ **Never lab.** Every path there returns the same 200 document, including `/nonexistent`, and the
  identity marker this walk asserts is satisfied by lab's catch-all — a routing defect is invisible.
- ⚠️ Proof A drives the page with the Worker **intercepted** on fault paths. It proves the page's
  logic, not the Worker's behaviour, and no live write was made to QA KV on lap 1.

## Open before stamping
1. **The invite message has no tracked home.** It is half the journey (side 2's entire input) and a
   change to it can arm no clock, because there is nothing to watch. Where it lives is a
   content-and-privacy call — Paul's.
2. **Content seat unread** on every Mom-facing word here, including the walker's ambiguity findings
   ("Where is it?" — the property, or her own address?).
3. **The cascade tracking design is PROPOSED, not ruled**
   (`.plans/2026-09-05-release-cascade-tracking-PROPOSAL.md`,
   `.plans/2026-09-05-journey-test-cycle-PROPOSAL.md`). This plan carries its walk pointer as a
   `stage-note:` rather than a `gates:` key, because that key does not exist until Paul rules.
