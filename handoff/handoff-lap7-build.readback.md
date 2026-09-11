# Readback — lap 7 BUILD WINDOW · written by the incoming build lane

<!-- written 2026-09-10 ~11:20 PM ET · brief stamp 8267764 · HEAD when this was written: 7b36392 (moved under me THREE times while I read: af8d765 → 3dadbd4 → 7b36392)
     Nothing below is started. This is what I understand, what I measured, and what looks thin. Grade it. -->

## 0. The stamp, and what moved since it

- Brief stamped `8267764`. HEAD was `af8d765` when I opened (the brief's own commit), then **`3dadbd4`** (coordination: *"Row E · TEARDOWN — ran and committed … SEAM-9 is clear"*), then **`7b36392`** (coordination: *"L4 held-out draft landed; live seam gap verified"*). `git diff 8267764..7b36392` is the brief itself plus 40 lines of `CYCLE-LOG.md` and the held-out note under `.content/`. No code moved.
- **The brief's §3 is stale on one load-bearing point, in the safe direction.** It says the teardown lane is *mid-act in this working tree* with six files uncommitted. Measured: the teardown commit `6889d0d` landed at **22:20:25**, *before* the brief's stamp commit (22:21:41), and the six files are clean. `3dadbd4` says the same in prose. So the SEAM-9 blocker the brief tells me to wait on is already resolved; `instance/bob.json` is gone (`dcbc660`), `worker/wrangler.toml` etc. are committed.
- **Three windows are live.** `BACKLOG.md` is dirty in the shared tree right now (10+/10−, the backlog window mid-edit). I will not commit anything without `git commit --only <my paths>`, and I will not commit this readback at all unless told to.

## 1. What I understand the thread to be

Lap 7 of the release loop, build window. **One candidate** carrying five rows that Paul committed at beat 6 in his own words (`CYCLE-LOG.md` § Lap 7 · Beat 6 table), built exactly per `.plans/2026-09-10-lap7-build-PLAN.md` (58 steps by symbol, engineering-partner's, ratified ~10:58 PM with all eight §9 questions ruled **yes**):

| row | what | done means (short) |
|---|---|---|
| **P** | three preconditions | `build-viewer.py --check` green · `check-storage-keys.py` green · four engine pages classified |
| **D** | the Worker map — `viewer.html` derives its Worker from the host label like the other four pages (`PAGES_WORKERS` at `engine/viewer.template.html:7316` replaced) · `/estate/` and `/homes/` split refused / unreachable / broken | a capture from the condo's app lands in the condo's Worker; `watch-feedback.py --env paul` shows it |
| **C** | G6 telemetry: `card_order_served` at render (Q2), `pos`+`orderSource` on every open/exposure (Q3), `auto-*` vias on the four silent expands, `plant_expanded` distinct, `observeCards()` re-run, and **the reader `tools/read-glance-order.py`** | events fire at the candidate and the named tool reads them |
| **B** | the account lifecycle — Worker: `/api/session` reports the person's estate (B1), revoke at the right scope (B2), `putAccount` (B3), PO-box refusal before mint (B4), outcome-only failed-sign-in door record (B5), `POST /api/recover` constant-response + own limiter + `account-recovery` feedback record (B6, Q4), `watch-door.py` roster (B7) — Pages: sign-out card, locked-out card, email shown back **display-only** (Q1), one constant refusal string, inline recovery block, signed-out lede, ship nameless, quarantine on refusal | TIER 2 · 18's falsifier — walked as **J8** |
| **A** | the applied founding-flow design, 20 steps keyed to the closure's 45 rows: bare-origin door on local state, `#s-door`, landing branches on `estates.length` (needs B1), corner-circle bubble, gate card in place with `#s3` deleted, PO-box blocking at submit (needs B4), two-state ranking control, `Edit` editors on the receipt, sentence case, **TWO colours**, Stone default, shelf/masthead/punch items | five seats × J0·J2·J3·J8 at qa, each read unprimed; content-steward reads every walk; `release-gate` green; then Paul |
| **H** | harness: repair the three `#go3` lists (same commit as A7), declare J8, write `journey_lifecycle` (L01–L15, L13 human), gate ① content clause + UX artifact convention as one step (Q6), `post-deploy` blob compare (Q5) | selftests prove each clause can fail |

Plus **P3 edit 1** (Q8): `walk-brief.py` gains a *WHAT THIS BUILD COMMITTED* header so seat briefs carry L1 into the walk without a hand relay. Row **E** (teardown) is not mine and is already done.

Authorities in precedence: beat-6 table → the eleven rulings + the eight → the closure's 45 rows → design plan §4 → seat reviews. The two live traps: closure 34 (**two** colours; do not build pass 2's one field) and closure 38 (punch 10 *"Tell Paul it's wrong ›"*; do not apply — A14's `Edit` supersedes it).

Order I may not reorder: P → D → C → B → A → H; B1 before A3; B4 before A8; B2 before B8; A7 + H1 one commit; Worker before pages at every env. Freeze one sha before the battery; any fix after is a new sha and a new battery.

What I do **not** own: L1 (the commitment), L4 (the release note's words — content-steward's, held out), `BACKLOG.md` (forward rows to `tate-tracker-2a` by message), all copy (every sentence is a slot, human-confirmed), and any deploy to `paul` or `home`. Coordination is `tate-tracker-ea`.

## 2. Current state — measured, not read off the brief

| check | result at 3dadbd4 |
|---|---|
| `build-viewer.py --check` | 🔴 as the plan says — first diff at `viewer.html:7447`, `RELEASE_NOTES_DATA` is 09-07's, source has 09-10's. Rebuild with no flags fixes it (P1) |
| `check-storage-keys.py` | 🔴 `fw-journal-name` used by three pages, undeclared (P2); every other literal rostered |
| `check-engine-manifest.py` | 🔴 P1 six unclassified, four of them the pages this build edits (P3) |
| `journey-walk.py --selftest` | ✅ 60/60 |
| `release-gate.py --selftest` | ✅ 16 mutations; UX clause still prints UNCHECKABLE (the H4 sibling) |
| `qa-behind.py` | qa serves `318416a`, 118 commits behind HEAD |
| `release-state.py` | ARMED · beat 11/12 · owner paul · candidate `318416a` — reads lap 7 as open with lap 6's cleared sha; HEAD not deployed |
| `check-telemetry.py` | exit 1: 26 never-seen events, 10 hand-triggerable — pre-existing, none of them this build's names |
| `.content/2026-09-10-lap7-release-note-HELD-OUT.md` | **landed at `60e439d` / chronicled at `7b36392` while I was reading** (it did not exist at `3dadbd4`). 9 walk-gated bullets + 2 not-yet, each tagged with the walk that must pass; row C gets no bullet; bullet 7 (row D) is gated by a RECORD check — Paul's note visible at his origin with its 2026-09-10 timestamp — cut, not reworded, if absent |
| `.plans/2026-09-10-teardown-REPORT.md` | present in `6889d0d`; §6 has register rows for the backlog window, §5 two server-side proposals (fixture stamp on J0 founding) — not this build's |

Symbol spot-checks, all found where the plan says (plan cites are at `49c7187`; still true): `#go3` in `journey-walk.py` at `:646` `:759` `:927` · `PAGES_WORKERS` at template `:7316` (plan said `:7300–7320`) · `handleSession`'s `estates: [{ estateId: scope.id …` at `worker.js:1008` · `addressIsBox` at `:1220` · `refused:box` recorded, not blocking · `J8` unclaimed anywhere in `journey-walk.py` (J7 also unclaimed in code) · `refresh()` at `:67` re-mints for `durable-credential` arrivals at `:1446` (A10 holds) · `release-gate.py` `CLAUSES` at `:205`, the UNCHECKABLE line at `:277`.

## 3. The open decision(s)

**Per the brief: none — the eight are ruled.** I found nothing that forces a new one *before* starting. Three things below (§5) may become one mid-build; per the brief I would stop that step, name it to coordination, and continue the others.

The one standing human gate after the battery is Paul's walk (gate kit: two visible Chrome tabs, door link + `pkirsch`, one throwaway he names, the 3–40 username rule stated). Not mine to open.

## 4. What has NOT been tested or verified

- **No network probe, no deploy, no browser.** I have not run `pages-deploy`, `deploy-worker.sh`, `wrangler whoami`, or opened Chrome. Whether wrangler is authenticated in this shell is unknown until the first `lab` deploy (Bash sandbox must be off for it).
- **The plan's own unverified list, still unverified by me:** `walk-integrity.py` (relied on from CLAUDE.md), `watch-door.py`'s event roster beyond what I grepped, `homes/index.html`'s collapse (D4 — read it in the window, record a searched-negative if absent).
- **Whether `settings/account/` can show the email without a fresh sign-in — partially answered.** The page already fetches `/api/grant/whoami` with the stored grant on every load and prints `"Email on file: " + d.email` (`settings/account/index.html:212–226`), hiding the line when empty — which is exactly closure row 19's *absent* defect. `/api/session` returns `email` (`worker.js:988`) and so does `/api/profile` (`:4299`). **I did not confirm that `whoami`'s own response literal carries `email`.** If it does not, B10's three states need whoami to gain the field (a Worker edit not in the 58 steps). First thing to check in B10.
- **Paul's phone outbox (D8):** traced by the plan at HEAD, never exercised. The falsifier stays `watch-feedback.py --env paul` after his next load of the condo app — after the `paul` deploy, which is not mine.
- **Line numbers in the three teardown-touched files** (`pages-deploy.py`, `deploy-worker.sh`, `post-deploy.py`) are one commit stale in the plan; I will verify symbols, not lines (SEAM-9's own caveat).

## 5. What looks thin, or that the brief left me unsure of

1. **P3 edit 1 has no step, no symbol list, and a dependency the brief does not name.** The plan's 58 steps were written before Q8 was ruled, so P3 edit 1 is a 59th step with no `file:symbol`. Its definition (`.plans/2026-09-10-build-description-chain-DESIGN.md` § P3) is *"`walk-brief.py` gains a header printed from `cycle-state.json committed[]`"* — and **`committed[]` does not exist in `cycle-state.json`** (grep: no hit). That is **P1** of the chain design (an `id` column on the beat-6 table + a parser), which was ordered *before* P3 edit 1 and which nobody ruled into this window. `check-backlog-ready.py`'s new committed-by-ruling rung (`8267764`) already parses beat-6 tables of open laps, so the parser may be reusable. **My assumption unless told otherwise:** build the smallest honest version — the header reads the beat-6 table via that existing parser, writes nothing new to `cycle-state.json`, and I name P1 as *not built* rather than build it uninvited. Grade this.
2. **Two items owed to lap 7 by the last build lane's §8 are in neither the plan nor the brief.** (a) The **found-event reader** — `ev("found", ok|already|refused|unreachable)` fires on `/api/onboarding-metrics` and no tool prints its name; §8 says *"an event with no reader is not instrumentation"*. B7 touches `watch-door.py` anyway; adding `found` there is one roster line, but it is scope I was not given. (b) **L7-P1** (the two-person, one-context falsifier) is pre-registered for disposition at lap 7's close (`CYCLE-LOG:2451`) and appears in no step; §8 said *carried, not this lap's build*. I would name both to coordination at my first message and not build (a) unless told.
3. **Event-name divergence between the closure and the plan.** Closure L10 asserts a **`door_failed`** record; plan B5/B7/H3 say **`signin_failed`** (and `recovery_requested`). `worker.js:1136` has a closed roster `DOOR_EVENTS = [door_reached, door_opened, door_failed]`, validated on POST at `:1615`; `watch-door.py` counts `door_failed` by name. A server-side `waitUntil` write bypasses the POST validator, but a new name must be added to both the roster and the reader or the zero is unnamed. **My assumption:** the plan (later, engineering-partner's) wins on the name; the journey stop asserts whatever B5 writes. Flag if the closure's name was the ruled one.
4. **The recovery route has had no security read.** The closure's *What I did NOT decide* says *"security-steward is owed before that field is built"* for username recovery. `.engineering/2026-09-10-cross-device-signin-SECURITY.md` has L1/L2/L3 and **zero occurrences of "recover"**. The plan's B6 designs the shape (constant bytes, equal timing, own limiter, no oracle in the record) and Q4 ruled the channel — but nobody with the security seat has read it. I can build B6 to the plan's spec; whether that satisfies the closure's "owed before" is a judgement I should not make alone. Not a blocker for D/C; it is for B6/B12.
5. **The pull list differs between the brief and the chronicle.** Brief/plan §8: TIER 1 · 45·42·26·27·28·29·30·**31**·43·44·32·23 + TIER 2 · 10·13·18·**19·20·21·25**. `CYCLE-LOG` "Rows frozen at the pull" omits TIER 1 · 31 and TIER 2 · 19/20/21/25. The five extra rows are real A-row items (content reads every walk; password rule; Almanac naming; masthead alignment; mis-capitalised label). I will declare the brief's fuller list to coordination and let the backlog window reconcile the chronicle line.
6. **The battery's `content-steward reads every walk` step has no artifact path convention yet** (H4 is what invents it). Until H4 lands the content clause is UNCHECKABLE by construction. Fine, but the order matters: H4 must exist before the battery runs, not after — it is in row H, which the plan sequences last. I would land H4's convention *before* deploying qa for the battery.
7. **Q7 (`myhome-paul` is THE production origin) changes what row D's *done means* is measured against**, and nothing in D7 says which origin the falsifier reads. D7 says `--env paul`. Consistent with Q7; noting only that `home` (Mom's account `marguerite`) is never touched by me.
8. **A NEW P-STEP WAS ADDED TO THE CANDIDATE AT `7b36392`, AFTER THE BRIEF, AND THE BRIEF DOES NOT CARRY IT.** Coordination verified that `MOM_ACK_DATA` is a concrete literal in `engine/viewer.template.html` (`:12022`) with no per-instance seam, and `instance/paul.json` declares neither `ack` nor `questions` in its `absent` list — so Mom's ribbon and Mama's Perspective queue render at Paul's household today. Ruled: (1) `paul.json` gains `ack` + `questions` in `absent`, **rides lap 7's candidate as a P-step** (not a hotfix); (2) a per-instance ack seam is a lap 8 candidate — ⛔ writing Paul's ribbon line into the engine literal would invert the leak, so the held-out note's ribbon line for TIER 1 · 42 **cannot ship as drafted**. I read this as **P4**, one line in `instance/paul.json`, checked by `pages-deploy --env lab` refusing nothing and the `paul` build carrying no ribbon. It is instance-class, not engine, so it is inside the guardrails. Grade whether I have the two acts the right way round.
9. **`release-state.py` reads HEAD as undeployed and the candidate as `318416a`** — expected, but it means every state readout during this window will say "beat 11/12 · owner paul" until qa is redeployed. Not a fault; a thing to not misread.

## 6. What I would do next (on clear — nothing started)

**Will not touch until told:** nothing is blocked any more — the teardown is committed. I still will not edit `BACKLOG.md`, `CLAUDE.md`, `VOCABULARY.md`, `worker/digest.json`, or anything under `home`/`paul`/`legacy`.

First three steps, by symbol:

1. **P1** — `python3 tools/build-viewer.py` (no flags) → `--check` green → `git diff --stat engine/viewer.template.html` empty. Commit `--only viewer.html`.
2. **P2** — declare `fw-journal-name` in `onboarding/index.html`'s storage-key block (`:1216` is its only write) → `check-storage-keys.py` green. **P3** — add `class: engine` for `estate/`, `homes/`, `settings/account/`, `settings/place/` in `ENGINE-MANIFEST.md` → P1 count 6 → 2. **P4** (new, `7b36392`) — `instance/paul.json` `absent` gains `ack` + `questions`.
3. **Declare the pull** (the brief's fuller list) to `tate-tracker-ea`, naming §5 items 1–5 in the same message; then **D1** — replace `PAGES_WORKERS`/`PREVIEW_KNOWN` at `engine/viewer.template.html:7316–7335` with the host-label derivation the other four pages use (`grep -n PREVIEW_KNOWN` first: `:7331`, `:7335`, `:7356` read it), **D2** rewrite the stale hazard comment, then D3/D4.

Before declaring any candidate: both halves — `--check` + template diff empty **and** `pages-deploy.py --env lab --sha <sha>` (the headless load), plus the four selftests/checks in the brief. Then freeze, deploy qa, battery (J0·J2·J3·J8 × five seats, visible Chrome, 414×848×A+), content read, `release-gate.py`, hand to coordination.

## 7. Coordination's grade and rulings — received ~11:40 PM ET, recorded by coordination in CYCLE-LOG lap 7 at `8aa6504`

Grade: **CLEAN.** Rulings on §5, in force for this window:

1. **P3 edit 1** → build chain **P1** with it (an `id` column on the beat-6 table + the parser feeding `committed[]` in `cycle-state.json`), then the `walk-brief.py` header. Process tools, no app surface — the 59th step.
2. **`found` event reader** → one roster line in **B7** (`watch-door.py`). **L7-P1** stays pre-registered; disposed at close with evidence.
3. **Naming** → the existing closed roster name **`door_failed` with an outcome field**, not `signin_failed`. `recovery_requested` joins roster AND reader together or not at all.
4. **Security read on B6** → security-steward is running (roster + legibility on the recovery route), filed to `.engineering/2026-09-10-recovery-route-SECURITY.md`. Build B6 to the plan's spec; ⛔ **do not deploy qa with B6 in it until that read has landed and coordination has relayed it.**
5. **Pull list** → the brief/plan's fuller list is right; declare that one. The register has frozen it.
6. **H4** (content clause + UX-artifact convention) lands **before** the qa deploy for the battery.
7. **P4** = `instance/paul.json` `absent` gains `ack` + `questions` — a P-step, acknowledged.
8. Teardown committed (`6889d0d`); SEAM-9 clear; verify symbols, not lines, in the three deploy tools.
9. `release-state.py` reads beat 11/12 until qa is redeployed — known (TIER 1 · 47).

Every commit `git commit --only <paths>`. Report to `tate-tracker-ea` at: the pull · each row's close (D, C, B, A, H) · the frozen candidate sha · before deploying qa · after release-gate. This readback is not committed unless Paul or coordination says so.

**Waiting on Paul's keystroke in this window.** On clear: P1 → P2 → P3 → P4 → declare the pull → D1.
