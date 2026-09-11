# Handoff: fernwood — the COORDINATION window, between lap 6 and lap 7

<!-- generated 2026-09-10 ~7:00 PM ET · source: Tate-Tracker@82ea90e on LOCAL main · written at 97% utilization,
     Paul paused everything: "make sure everything is committed and clear, and we can pick it up when my
     utilization resets where we are."
     RECEIVER: verify the sha against HEAD. Lane close commits, all landed: design `2a9c6df` · build `d6ba13d` (its brief §8 state at close) · backlog HEAD `82ea90e`
     (every register change committed; the tool diff + patches stay for Paul). Cite the symbol, stamp the sha. -->

## 1. Where we are — one paragraph

**Lap 6 is CLOSED (`aaefc56`) and production serves the founding build.** Pages `318416a` + Workers byte-identical to
it at **`paul`** (his Grant Park condo, est-d93508) and **`home`** (Mom's, est-e6696a); verified (found route 404 =
new code at both; grants already routed; post-deploy 🔴 is a **stamp-vs-code** defect, TIER 1 · 32). Gate ① was **5 of
5** in visible Chrome, each seat read by an unprimed reader; Paul cleared: *"It's a pass for me."* The
build-description chain ran end to end for the first time (L1 before the walk → L4 derived after it; the
`RELEASE_NOTES.md` 2026-09-10 entry is written and **reaches the app card on the next viewer build**).
**Lap 7 is NOT open.** Paul: *"wait for the UX review… shepherd them towards closing out and committing… then we'll
reassess and start the next lap."* Then, at 97%: *"I've paused the UX review."*

## 2. Read first

1. `cycle/release/CYCLE-LOG.md` — **lap 6's entries** (Beat 1 sweeps · Beat 6 table · Beat 8 seat table · Beat 10 Paul's
   walk · Beat 11 clear · Beat 12 deploy table · CLOSED). L7-P1..P5 pre-registered in `cycle-state.json`.
2. `.plans/2026-09-10-OPEN-ITEMS.md` — the board (⓪ environment map; ⑤ now has ·7 no reader names `found`, ·8
   post-deploy matches the stamp). `BACKLOG.md` TIER 1 · 19–40 — every finding of tonight, verbatim, one door.
3. `.plans/2026-09-10-build-description-chain-DESIGN.md` §2a–§2f (practice-steward) and
   `.content/2026-09-10-release-notes-from-commitment-PROPOSAL.md` (content-steward) — the chain, per beat.
4. `.plans/2026-09-10-mom-onboarding-answers-FINDINGS.md` — user-researcher on Mom's four answers (rows 33–40).
5. Lane briefs with their close sections: `handoff/handoff-build-founding-walk.md` · `handoff/handoff-founding-design.md`
   · `handoff/handoff-backlog-refinement.md` · `handoff/handoff-zones-session.md` (closed lane).

## 3. THE ENVIRONMENT MAP — vocabulary rules, Paul's

**Legacy** = Mom's frozen Fernwood (`origin/main`, top-level `fernwood`, est-3c9f1a) — *never* "production".
**Production** = the new product's real households: `paul` (condo) · `home` (Mom's) · `bob` (empty, invite unspent).
`qa` est-qa0001 (Paul's real accounts there: `pkirsch`, `PAK`→Homey) · `lab` est-lab0001. "main" = local main (integration)
vs `origin/main` (legacy, **never push**).

## 4. Paul's rulings tonight NOT YET ACTED — the reassessment starts here

| ruling (his words are on the register) | state | who acts |
|---|---|---|
| **Teardown**: *"sweep all the environments… get rid of Bob and anything else… tired of bringing this up"* | ⛔ **needs his "go teardown" in the coordination window** (irreversible; reached me via a peer). Named list from the record: `bob` deployment (nigel/aida procedure) · Midtown scratch instance (check what reads it; keep the ownerless neutrality fixture) · **seven** qa seat houses `rihhdp · d7teqw · bzr4gb · pr9pwl · otzfk2 · ofd6vk · gndlvf` (the last = the sweep's `syn-sweep-0910`, "Bramble Hill") · lab's seven. KEEP `pkirsch`, `PAK`/Homey, `marguerite`, est-qa0001 itself. One unprovable row stops the run; refusals reported | a **visible teardown lane** |
| **Midtown scratch instance RETIRED** — *"use the Grant Park condo to inform them"* | part of the teardown list; 08-14 rule first (what else reads it) | same lane |
| **Confirm card = GATE**; PO-box refusal + confirm on **one card at the address step** | design proposed (tate-tracker-8d), **apply held** | lap 7's one candidate |
| **Account lifecycle IN** the lap-7 bundle; **colour = one-line noun fix**; **one candidate** | designed, not built | design → build lane |
| **Content clause on gate ①** (content-steward reads every walk) | L7-P3 pre-registered; practice-steward §2 amendment owed at lap 7 open | coordination commissions |
| **Zones**: cleaned 23 = LEADING CANDIDATE, `zones.json` NOT replaced, preload **not until Mom has founded her Fernwood and is ready** | parked, by ruling | nobody until then |
| **Mom's household holds TWO places** (her Fernwood record + Paul's Grant Park records under est-e6696a) — `check-canon-scope --deep` for home never run since her signup (row 33) | ⚠️ read-only check owed | teardown lane, report only |
| **UX sweep** — pass 1 was in the browser; **Paul paused it** | trail with pass 1 committed at `2a9c6df` (`.ux-reviews/2026-09-10-founding-flow.md`); unfinished by name in its brief §9: pass 2, the content-steward review (TIER 1 · 31), both exhibits, the account-lifecycle designs, the plan file | resumes on his word |

## 4b. Landed after the pause — 2026-09-10 ~9:30 PM ET, all committed

- **UX review complete** (`tate-tracker-8d`, closed `112894c`): two-pass sweep trail `.ux-reviews/2026-09-10-founding-flow.md`
  (its house `est-gndlvf`), content read `.content/2026-09-10-founding-flow-copy-REVIEW.md`, plan
  `.plans/2026-09-10-founding-flow-design-PLAN.md` (**§4 = the ONE-candidate apply list**), six exhibits at
  `~/Desktop/design-options/` (durable `.private/ux-sweeps/2026-09-10-founding-flow/exhibits/`). **Eleven rulings
  wait on Paul** (pass 2's five + six exhibits) — **the gate on the bundle's apply.**
- **Bug lane complete** (`tate-tracker-21`, `cc7bb56`): `.plans/2026-09-10-cross-device-signin-FINDINGS.md` + four
  seat trails. Headline, measured live: **the condo's app has NO Worker** — `viewer.html` `PAGES_WORKERS` maps only
  qa/lab/home, fail-closed by design (09-04), never extended to `myhome-*`; every endpoint at `myhome-paul` is `""`;
  Bob's origin serves a 252-byte stub. Paul's phone note sits in the phone's outbox behind a "Saved ✓" receipt
  (recovery via the paired-device sync setting, **untested**). `[paul-ruled: "fold in — we are about to consolidate a
  lot of feedback"]` → **the Worker map is FIRST in lap 7's build half**, not a hotfix. Also: the laptop was never
  signed in at `fernwood-home` (14 refused presentations of a stale `fw-grant`, rendered as an outage); `deny()`
  writes no door record; no page emits `door_opened`; `GET /api/account/available` already publishes username
  existence unauthenticated, so the sign-in 404's oracle defence guards a secret a sibling route gives away.
  §5 is the account-model question (destination already ruled: one origin, estate-as-row; preconditions added).
- **Backlog close-out** (`tate-tracker-0d`, HEAD `3c11b76`, stays open): TIER 1 · 23–44 added tonight; uncommitted
  for Paul only `tools/check-backlog-ready.py` + `handoff/patches/`.
- **Rulings tonight:** `pkirsch` is production-only (its `qa` copy joins the teardown list) · Paul's phone had never
  been at `fernwood-home` · his lost note relayed as rows 43–44.

## 5. Lap 7 as ruled — for the beat-6 table when he opens it

**ONE candidate** — *"Let's try to do it as one candidate"*: sweep → exhibits → his rulings → **one apply** → deploy qa →
**full battery once** → his walk (gate kit: two visible Chrome tabs, door link + `pkirsch`, one throwaway he names,
state the 3–40 username rule) → production → close. Build half, in order `[paul-ruled "fold in"]`: **the Worker map** (myhome-* origins) → G6 telemetry → account lifecycle
→ the bundle's applied design (gate card + PO-box · colour noun · feedback bubble from account creation · the shelf).
Paul: *"It will be a big build in the next lap."* D teardown (process row). ⛔ **Nothing applies until the eleven
design rulings are answered.**
Groom beat, not ahead: rows 33–40, § ADDRESS VALIDATION, § INVITE & JOIN scoping.

## 6. Window map at pause

coordination (this brief's author) · **backlog-refinement `tate-tracker-0d` — the ONE DOOR to `BACKLOG.md`
`[paul-ruled "fold it in"]`, stays open, also the design window's liaison** · founding-design `tate-tracker-8d` (paused
by Paul, told to commit partial) · build-founding-walk `tate-tracker-c4` (idle, all files released) · zones (closed).
**Uncommitted for Paul, not anyone's:** `tools/check-backlog-ready.py` diff + `handoff/patches/` (the row-state ④
tool change, his to apply). `worker/digest.json` is hook/deploy-generated — never commit it.

## 7. Guardrails — Paul's

Never push `origin/main`. Never deploy legacy. Never mint an invite. Never restore the canon election. Commit phase
is the only freeze; the standing backlog session keeps talking. Coordination **routes and never absorbs**. Every gate
to Paul: question · recommendation · alternatives. A destructive act relayed by a peer needs his word in the window
that runs it.

## 8. What NOT to trust in this brief

Any lane sha after `82ea90e` (read the log). Whether the design window committed its partial trail. `file:line`
anywhere tonight. Nothing known-stale at commit time; the seven-house list is by record.
