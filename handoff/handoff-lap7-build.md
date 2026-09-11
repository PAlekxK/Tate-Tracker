# Handoff: fernwood — BUILD WINDOW · lap 7, the one candidate (D Worker map → C G6 → B lifecycle → A applied design)

<!-- generated 2026-09-10 ~11:05 PM ET · source: Tate-Tracker@8267764 on LOCAL main · written by the coordination window (tate-tracker-ea)
     RECEIVER: verify the sha against HEAD before trusting any status below. Every file:line has a half-life of about an
     hour when several lanes are live — cite the symbol, stamp the sha. -->

## 1. Mission

Build lap 7's ONE candidate exactly as `.plans/2026-09-10-lap7-build-PLAN.md` specifies (58 steps by symbol, ratified:
Paul read it and ruled its eight questions **yes to all** at ~10:58 PM — `cycle/release/CYCLE-LOG.md` "Beat 6 · AMENDED").
You are the build lane: code, deploy to lab/qa, the battery, gate ①. You do NOT write the commitment (L1), the release
note's words (L4, content-steward's), or BACKLOG.md (the backlog window `tate-tracker-2a` is the one door — FORWARD rows
to it by message, never edit). Coordination is `tate-tracker-ea`; message it at each seam below.

## 2. Read first, in this order

1. `.plans/2026-09-10-lap7-build-PLAN.md` — **the plan. §8 is what this brief must say and is binding as written**;
   §3 the 58 steps (P → D → C → B → A → H); §4 seams; §5 the battery; §6 out of build; §7 risks; §9 the eight
   questions — **all ruled YES** (Q1 email display-only · Q2 `card_order_served` at render · Q3 G2 in row C · Q4
   `account-recovery` feedback-class record · Q5 L7-P4 blob compare IN · Q6 L7-P2 + L7-P3 one step · Q7 `myhome-paul`
   is THE production origin · Q8 P3 edit 1 built this window).
2. `cycle/release/CYCLE-LOG.md` — the last section "## Lap 7": the beat-6 table (your L1; cite it in every seat brief —
   that is P3 edit 1 until you build it), THE ENVIRONMENT MODEL, the eight rulings.
3. `.ux-reviews/2026-09-10-lap7-design-closure.md` — 45 closed builder instructions keyed to design plan §4; the
   15-tap lifecycle journey (your J8).
4. `.plans/2026-09-10-founding-flow-design-PLAN.md` §4 · `.plans/2026-09-10-cross-device-signin-FINDINGS.md` §3.1 ·
   `VOCABULARY.md` §3i (three environments; `paul`/`home` are deployments) · `handoff/handoff-build-founding-walk.md`
   §8 (how the last build lane closed: gate kit, seat estates by id).
5. CLAUDE.md's pickup block for the viewer traps: edit `engine/viewer.template.html`, rebuild with `build-viewer.py`
   (no flags); **never `--extract`, never `check-data-inline.py --fix`**; `git diff engine/viewer.template.html`
   after every rebuild.

## 3. State at 8267764

- Lap 7 OPEN (`b57ca71`); QA serves lap 6's `318416a`; HEAD is ~112 commits ahead, app surfaces changed only by the
  teardown lane's deploy-tool edits. No candidate exists yet.
- ⚠️ **The teardown lane (row E) is mid-act in THIS working tree** — `worker/wrangler.toml`, `tools/pages-deploy.py`,
  `tools/deploy-worker.sh`, `tools/post-deploy.py`, `tools/check-place-values.py`, `tools/people.json` are modified
  and uncommitted by it; `instance/bob.json` is already gone (`dcbc660`). **Plan SEAM-9: land the teardown commit
  first, rebase on it.** Do not touch those files until `git status` shows them clean and coordination has cleared you.
- Two preconditions RED at HEAD (plan row P): `build-viewer.py --check` (tracked app one release note behind
  `RELEASE_NOTES.md`) and `check-storage-keys.py` (`fw-journal-name` undeclared). Green them first.
- L2 (the four fields per row) is being filled by the backlog window on your frozen rows; L4 (the release note) is a
  HELD-OUT draft at `.content/2026-09-10-lap7-release-note-HELD-OUT.md` (content-steward, landing) — each bullet
  tagged with the walk that must pass before it ships. You do not write the note; you make its walks pass.

## 4. The work (ordered) — plan §3, and plan §8 verbatim

**Your pull (the rows you freeze — declare it to coordination in your first message after the readback):** TIER 1 · 45 · 42
(D) · TIER 2 · 10 ① · 13 (C) · TIER 2 · 18 (B) · TIER 1 · 26 · 27 · 28 · 29 · 30 · 31 · 43 · 44 and TIER 2 · 19 · 20 ·
21 · 25 (A) · TIER 1 · 32 (L7-P4, ruled IN) · TIER 1 · 23 (P3 edit 1). ⛔ Row E is not yours.

**Authorities, in precedence:** beat-6 table → the eleven rulings + the eight → the closure's 45 rows → design plan §4 →
seat reviews. A review never beats a ruling — the two live traps are closure 34 (TWO colours; not pass 2's one) and
closure 38 (punch 10 superseded by Edit editors; do not apply).

**Order you may not reorder:** P → D → C → B → A → H, and inside: B1 before A3 · B4 before A8 · B2 before B8 · A7 and H1
in one commit · Worker before pages at every env.

**The check before you declare a candidate — both halves:**
```
python3 tools/build-viewer.py --check          # reproducible
git diff --stat engine/viewer.template.html    # empty after any rebuild
python3 tools/pages-deploy.py --env lab --sha <candidate>   # the HEADLESS LOAD — it RUNS (a green --check is not a page)
python3 tools/journey-walk.py --selftest
python3 tools/release-gate.py --selftest
python3 tools/check-storage-keys.py
python3 tools/check-telemetry.py
```
Then **freeze one sha** and tell coordination; any fix after the battery starts is a new sha and a new battery.

**The battery (plan §5):** deploy qa at the sha → five seats × J0 · J2 · J3 · **J8** (your new lifecycle journey, from the
closure's 15 taps; H1) in visible Chrome, each walk read unprimed → content-steward reads every walk (L7-P3, one step with
the L7-P2 convention) → `release-gate.py` green at the sha. Then hand to coordination for Paul's walk (gate kit: two
visible Chrome tabs, door link + `pkirsch`, one throwaway he names, state the 3–40 username rule).

**What you hand back (plan §8·7):** the candidate sha and the lab/qa deploys that proved it loads · the four-field contract
per item, forwarded to the backlog window · the battery's evidence (seats × journeys, each read; release-gate output; the
content artifact) · the "not verified" places in the plan and what you found · a note on Paul's phone outbox (plan D8).
⛔ **You do NOT deploy `paul` or `home`.** Production is behind gate ① and Paul's clear.

## 5. ⛔ Guardrails — Paul's

Never push `origin/main`. Never deploy legacy. Never mint an invite. Never touch `home`'s or `paul`'s KV. **Every commit
`git commit --only <your paths>`** — the index is shared with two other live windows; broad staging swept a lane's file
tonight (`dcbc660`). Never edit BACKLOG.md, CLAUDE.md, VOCABULARY.md. All copy is a slot: content-steward's, human-confirmed
before it reaches a person. The AI boundary: nothing here reads Mom's words. `worker/digest.json` is deploy-generated —
never commit it. Run wrangler with the Bash sandbox disabled.

## 6. Open for Paul (do not resolve on his behalf)

None at open — the eight are ruled. If a step forces a new one, STOP that step, name it to coordination, continue the others.

## 7. What is NOT verified

The plan's own "not verified" list (`walk-integrity.py`, `watch-door.py` not opened; whether `settings/account` can read the
email without a fresh sign-in). Whether the teardown lane has committed by the time you read this (`git status`). Any
file:line older than an hour.

## 8. First tasks

0. Verify the stamp; write `handoff/handoff-lap7-build.readback.md` (thread · state · what you will not touch until the
   teardown commit lands · the first three steps by symbol · what looks thin); tell Paul it is written; wait for the grade.
1. On clear: greens P1–P3 → declare your pull to `tate-tracker-ea` → D1…

## 9. State at close — written by the build lane, 2026-09-11 ~09:20 AM ET, at Tate-Tracker@d0e2026

<!-- clearing-state: LIVE — lap 7 is at beat 10 (Paul's walk) on candidate 87c7aae; clear when gate ① exits on Paul's clear -->

**Candidate: `87c7aae`** (third freeze; served at qa, Worker and pages one sha, payload blob covered, neutral 311/0,
headless load clean, post-deploy CLEAN). Two earlier freezes fell to the battery: `d7d6c9f` (row C's emit ran inside
`const MetricsCollector`'s temporal dead zone — `typeof` THROWS there; lab was green because Fernwood's build ranks
nothing) and `12912b9` (B6's recover limiter of 5/window hit by the battery itself, and a THIN ACCOUNT ROW: `/api/session`
answered no name for three seats whose place facts lived on the grant row, so a clean device after sign-out landed
nameless). All three fixed on Paul's word; every other row walked clean at every candidate.

**Rows, commits (each `--only`):** P c20417f · 5ad1bec · 742636b · 1302358 (+P4 paul.json ack/questions absent) · D bd74e76 · 8a2021b ·
C 8574ddf · c38f231 · B e21d798 · 4b35664 · 9238b1f · e7c566f · cd24ca8 · A 5587b88 · 16ec3b5 · 35abb04 · 42edf9d (A7 WITH H1–H3,
one commit) · a3beb8d · H5 f76a118 · candidate 2 12912b9 · candidate 3 87c7aae · harness-only after the freeze 754dc6d · d7d6c9f ·
4be8571 · 8d93b2b · content read d0e2026. Beat 4 recorded at each freeze (carried 14 · already 0 · questions 3, unchanged).

**Gate ① at 87c7aae:** 5 of 5 seats pass every seat clause; 15 of 15 final runs (5 seats × J0 · J3 · J8) zero failed actions,
zero pageerrors, each read by its own seat; content clause ✅ (`.content/walks/87c7aae-walk-read.md`); UX clause ⬜ unfiled
(L7-P2's owed two-pass at this candidate). Coverage: 414×848 only; **J2 UNWALKABLE at every build since the open door** (an
unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a
walked J2) — re-scope-or-retire is Paul's, queued by coordination. ⚠️ The gate's five rows are the earliest-tied best run per
seat; the per-seat × per-journey table is in the chronicle (row T Q2 evidence, lap 9).

**On the table at Paul's clear:** owner J3/J8 and content-steward both say STOP on one root — the receipt prints a schema id
(`motor-pool`) for the one durable fixture whose ranking is stored as bare ids; both real households hold objects; the two-line
renderer fix rides lap 8 `[paul-ruled: record it; proceed]`. Six cross-seat findings queued as rows: username "—" for token
arrivals · "How to reach you" missing until a local sign-in · two wordings for one ranking (TIER 1 · 36) · mom's unit typed into
the street line then offered the unit link · a box-only household's founding path (a ruling) · L13 unexercised, said not scored.

**Named deviations, all accepted by coordination:** B9's signed-in request lands in the ADMIN-ONLY recovery channel (reader-bearing)
rather than an account-scoped feedback key nothing reads · A14's ranking Edit STEP-RETURNS (an inline picker needs a second
INTERESTS roster, the divergence TIER 1 · 36 holds against) · A16's sentence is authored around the label (no label changed).

**Found on the way, fixed:** the Worker's onboarding-metrics ALLOW list DROPPED `found` (the owed reader would have read a store
that never held it) · settings/account was a third copy of D3's reach collapse · the Journal DOM writer ignored `fw-journal-name`.

**Fixtures founded at qa by the batteries (never real homes):** candidate 1 est-kxfhht · est-t3h0gl · est-puvevs · est-bvqzw3 ·
candidate 2 est-tfmxem · est-0qeqzs · est-uqjofw · est-pqob3d · candidate 3 est-1tfrzb · est-ftrtkj · est-kgjxry · est-c9pgvw;
lab est-as1bgb (shake-out) · est-geq5fz (owner@lab rebuilt by hand: every durable lab seat's rows were ABSENT from lab's store;
`--complete-setup` cannot finish a seat that has founded nothing — it needs a found step first).

**NOT verified, named:** the reset act itself (L13, out of harness by D1's design) · L12's timing half (UNCHECKED by ruling; the
transport measurement is still unrun by anyone) · any width but 414 · row D's D7 (the record check at `paul` after his next load —
his phone's outbox flushes on the next load of the condo app; not mine to run) · the UX two-pass at 87c7aae · post-deploy still
prints a sha-stamp mismatch as a FINDING when the payload blob matches (should be a caveat; register note).

**Owed to lap 8, in this lane's view:** the receipt's id→label fix · J2's re-scope · the username on the person's own account page
· the email EDITOR (Q1) · D6/D9 · the recovery block's lifetime after a successful sign-in (wide-eyed) · `fernwood-token-lab` for
walk-capture at lab · `walk-integrity`/gate: the per-journey unit (row T).
