# Lane ledger — held by the hub session

**Hub:** `paulkirschenbauer-0b [45dbaa]` · opened 2026-09-04 PM ET
**Repo state at launch:** `main` @ 0bcbc86, tracking `origin/staging` (QA). Prod FROZEN.

| Lane | Topic | Writes | Status |
|---|---|---|---|
| A | business-analyst seat | `~/.claude/agents/` + foundation | ✅ AT GATE — `fa9d368`, marked UNSTAMPED. Paul stamps the foundation before the seat works |
| B | map-region smoothing | one new `.plans/` doc | ✅ AT GATE — `ecf9df1`, 400 lines. 3 items need Paul |
| C | fictive test user | one new `.user-research/` doc | ✅ AT GATE — `a0640ee`, 1 file / 417 lines. 6 items need Paul; #4 is BLOCKING |
| — | **round-1 exhibit picks** → `.decisions/fernwood-13.md` | **PAUL — not delegable** | open |
| D | UX sweep (queue #6) | `.ux-reviews/` | HELD — needs Paul at a terminal to triage |
| E | engine (queue #2/#4/#5) | viewer/engine + push to staging | HELD — the only lane that pushes; one session only |

## Why these three and not others
A, B and C were chosen because **none of them writes a path any other lane
writes, and none needs QA**. That last point matters more than it looks: a git
worktree would not carry `.private/` (gitignored), so a lane needing
`fernwood-token` or `cf-access-service-token.json` would fail in isolation.
Picking lanes that don't need QA removed the worktree problem instead of solving it.

E is held because QA is a single deploy target — even with isolated trees, two
lanes pushing to staging serialize at the remote.

## Collision surface actually checked at launch
- Tate-Tracker has exactly ONE worktree. No lane creates another.
- `~/.claude` had 7 uncommitted files from another session — lane A is warned by path.
- Two idle *cloud* sessions sit on Fernwood (`0e8b50`, `1ddc4a`). Idle, not writing.

## Gate reports — verified by the hub, not taken on trust

**Lane C (`a0640ee`) — claims re-checked independently 2026-09-04:**
- Scope honoured: exactly 1 file, 417 insertions. Not pushed (`git log origin/staging..HEAD`).
- `.user-research/2026-09-04-condo-dweller.md` left untracked and unstaged, as instructed. ✓
- ⭐ **The desktop claim VERIFIES, and is stronger than lane C stated.** It reported
  "14 @media queries, none above 660px." Re-measured: 14 `@media` matches, but **one is
  prose inside the file**, so 13 are real. More importantly the direction is absolute —
  **`viewer.html` contains no `min-width` media query at all.** Every `min-width` hit is a
  CSS property (44px tap targets etc.), never a breakpoint. So *"desktop is the mobile
  column centered in whitespace"* is not an interpretation; it is the file.
- ⚠️ The Hillyer model's ABSENCE is corroborated — the hub's own earlier grep also found
  no synthetic-Scott artifact. Two independent misses is not proof it doesn't exist, but it
  is enough to stop designing around it.

**Lane A (`fa9d368`)** — foundation + role file committed, explicitly UNSTAMPED. Correct:
its gate was "drafted, Paul stamps," not "in service."

**All four writers staged by explicit path.** Verified at 14:39 — the other session's five
uncommitted files in `~/.claude` (MEMORY.md, the finding ledger, the KV memory, cycle-state,
`feedback/`) are untouched by every lane and by the hub. The rule held under live concurrency.

---

## Run 1 — CLOSED 2026-09-04 ~2:45 PM ET. All three lanes reached their gate.

| lane | launched | gate artifact | disposition |
|---|---|---|---|
| A | 14:30 | `~/.claude/agent-foundations/business-analyst.md` (`fa9d368`,`9b7ddd6`) | reported · UNSTAMPED, awaiting Paul |
| B | 14:30 | `.plans/2026-09-04-map-region-smoothing-PLAN.md` (`ecf9df1`) | reported · awaiting Paul |
| C | 14:30 | `.user-research/2026-09-04-fictive-test-user.md` (`a0640ee`,`44754f9`) | reported · §8 RULED by Paul in-tab; 5 items open |
| hub | — | this ledger + meta seed (`a83c97c`) | closed |
| practice-steward | 14:30 | `~/.claude/agents/audits/2026-09-04-parallel-lanes.md` (`2ae41f3`) | reported |

**The `launched-at` / `gate` / `disposition` columns exist because of that audit's M2** — the
previous table read `launched | launched | launched` and could not distinguish a lane that
finished quietly from one that died at a permission prompt. Fixed on run 1 rather than run 3,
since the fix was three columns.

**Hub-verified, not taken on trust** (the audit's §6 named lane compliance as unverified):
- Lane B's measurements reproduce exactly — 23 zones, 437 vertices, 23/23 `draft`,
  **58 exactly-shared coordinates across 20 zone pairs**.
- ⚠️ Which confirms lane B's out-of-scope catch: `zones.json _meta.sharedBorders` states
  *"traced independently, by eye, with no vertex snapping."* **That is now false**, and false in
  the safe-looking direction. Left uncorrected deliberately: it is canon, and the hub proposes
  rather than edits.
- Lane C's desktop finding verifies and is stronger than it reported — `viewer.html` contains
  **no `min-width` media query at all**, so "the centered column" is the file, not a reading.
- Lane A's "the remit was already researched" verifies — `project_monetization_deferred` holds
  the 2026-08-13 study, the utility-vs-journal datum and the $1,500–5,000 shape.

**Cross-session `SendMessage` DELIVERS.** Listed as unverified at launch and again in the audit's
§6; four sessions reported in over the peer socket and all were received. Question closed.

⚠️ **OPEN, carried by no lane:** Paul's `[paul-ruled 2026-09-04]` layout contract currently lives
only in lane C's fixture document. A ratified layout contract does not belong in a test-fixture
design doc — it belongs where renderers and reviewers read it. Both candidate homes are outside
every lane's OWNS, and one of them is engine territory while prod is frozen. **Hub holds it; Paul
picks the home.**

### Lane B follow-up (`bebbfe3`) — hub-verified 2026-09-04

Paul answered in-tab: it was the **viewer's** map. Lane B's resulting finding —
*the 2026-08-31 snapping + smoothing work landed on the AUTHORING surface and never
reached the READING one* — **verifies**:

- `chaikin`: **0 hits in `viewer.html`, 3 in `tools/area-trace.html`.** The corner-cutting
  exists only where zones are drawn, never where they are read.
- ⚠️ **The join claim needed a second look, and the first check nearly cleared it wrongly.**
  A bare `grep -c stroke-linejoin viewer.html` returns **2**, which reads as "round joins are
  set." Both are unrelated: one is a 24px icon rule (`viewer.html:4272`), the other a sparkline
  polyline (`:8058`). **Neither touches a zone polygon**, so the zone map does render with the
  default miter join and lane B is right. Instance of [[reference_match_payload_not_container]]
  caught on a live check — the container matched, the payload did not.

**Acceptance criterion for anything shipping from that plan:** *does it render on `viewer.html`* —
never *does the tracer do it*.

### Lane C scope-widening (`3aada23`, `56b1185`) — hub-verified 2026-09-04

Lane C wrote OUTSIDE its OWNS, into engine territory the ledger had marked HELD, on Paul's
direct instruction. It declared this rather than letting the hub find it, and checked run 1 was
closed and the tree clean first. **Verified, and it holds:**

- ⭐ **Comment-only — PROVEN, not asserted.** A naive diff-grep looks alarming (prose lines
  inside a multi-line comment read as code, and the prose quotes `@media`/`min-width`/`;`).
  The rigorous test is comment-stripping both revisions and comparing: **identical for
  `viewer.html` AND `engine/viewer.template.html`**, +3319 bytes of comment, zero executable
  change. Mom's surface is unmoved.
- `python3 tools/build-viewer.py --check` → ✅ byte-identical to template + instance.
- Nothing pushed (10 commits still local).
- **The measurement reproduces exactly: 13 `@media` blocks, ZERO `min-width`** — 6×480px,
  1×540px, 4 prefers-reduced-motion, 2 hover. Lane C's correction of its own earlier "14" is
  right, and it corrects the hub's relay of that number too. A grep hit count included a prose
  reference; the block carries the accurate 13.
- ⭐ **Lane C corrected the instruction on a ground that mattered.** `viewer.html` is GENERATED.
  Writing the block there directly would have gone red on `--check` and been absorbed on the
  next `--extract`. It wrote the source template instead — and argued the ruling is ENGINE-class
  prose (a layout contract governing the shared renderer), so the template is right on the
  manifest's own terms, not merely mechanically.

**Hub endorses its two prose-not-tool guards.** Stating plainly that the contract is not
tool-enforced, *because* a lint counting `min-width` blocks would pass the day someone shipped a
bad wide layout without one, is the honest form: a green check that implies coverage it does not
have is worse than a declared absence.

## 🔶 PROPOSED preamble amendment for run 2 — NOT APPLIED, Paul's call

The preamble says OWNS binds, full stop, and has no clause for what lane C actually hit: a
direct instruction from Paul that widens scope after the run has closed. It behaved correctly by
improvising the right rule. Proposed wording, to make that repeatable rather than lucky:

> **OWNS binds for the duration of the run. Paul's direct instruction supersedes it — but a lane
> acting on one must first verify no other writer is live in the affected tree, and must DECLARE
> the widening to the hub in the same breath as doing it.** Silence is the violation, not the
> widening.

---

## Run 2 — OPEN 2026-09-04 ~3:05 PM ET

| lane | topic | writes | holds QA | launched | gate | disposition |
|---|---|---|---|---|---|---|
| D | Tier 1 map render (steps 1–2 only) | `engine/viewer.template.html` + rebuilt `viewer.html` | **YES — sole holder** | 14:52 | `6408706` + exhibit staged | **AT GATE** — verified; awaiting Paul on the dash + QA deploy |

> ⚠️ *Corrected 2026-09-04 (practice-steward).* This table read `status: launched` while the same
> file's "Lane D AT GATE" section said otherwise. The `launched / gate / disposition` columns that
> M2 produced were added to run 1's **retrospective** table and never carried into run 2's **live**
> one — **the fix landed on the record of the closed run, not on the instrument of the open one.**
> That is the same defect one level up.

`[paul-greenlit]` *"yes, greenlight tier 1 as its own lane."* **Lane B caught that the greenlight
bundles a decision Paul has not made:** Tier 1 is three steps and the third — the DASH — is his
authoring call, not agent work. Lane D asks about it and does not act. That catch is the clearest
argument yet for the routing rule: a lane that had simply executed "Tier 1" would have reversed an
honesty rule on Mom's surface.

**Standing rules now in force**
- Questions of scope / sequencing / ownership route to the hub `[paul-stated 2026-09-04]`.
- At most ONE lane holds QA for a whole run (practice-steward audit). Lane D holds it, and still
  does not push — prod is FROZEN, and Paul sees a local before/after first.

## Rulings Paul gave directly in lane tabs (the hub was holding two of these — both now moot)

- **Seat name** — *"I don't really care about the name."* → `business-analyst` STANDS. The hub's
  backing of a rename is withdrawn; the description carries the remit. **Registered in
  `~/.claude/agents/README.md`** now that the name is settled.
- **Bob's motive** — *"I talked about bob's motives in the voice notes."* → substance CONFIRMED.
  ⚠️ Two limits survive because he lifted neither: what is confirmed is the **substance, not a
  verbatim** (Bob is still never quoted), and a confirmed relay **does not open a channel** — the
  AI boundary and the quarantine clause still bind.
- **Research posture** — *"let the seat do all its own original research."* The 2026-08-13 study
  is now a **PRIOR to re-test, not an authority to cite.** This reversed a drafted commitment;
  lane A reversed it explicitly in the file rather than quietly.
- **Scope** — *"Fernwood to start, but will expand to the rest of the portfolio."* Fernwood is the
  first instance, not the subject. ⛔ Oculus and joint ventures are NOT in scope until he opens them.
- **The canvas** — the ~660px centered column IS the desktop design `[paul-ruled]`, now sited in
  `engine/viewer.template.html`.

## ⭐ Router drift, found while registering the seat — measured, not assumed
`~/.claude/agents/README.md` claimed **7 agents**; **9** carry frontmatter. It omitted
**practice-steward** (which has had a routing-table row since it was stood up) and
**business-analyst** (spawnable — it appears in the live agent-type list — while absent from the
router). **Two agents invisible at once.** This is the same defect the file's own 2026-08-02 note
documents about examiner-panel: that fix corrected the *number* and left it hand-written, so it
could only be right until the next agent. The line now carries the command that derives it.

## Lane A CLOSED — three items the hub took so they would not die with it

1. **Ritual steps 4, 5 and 7.3 still owe** for the business-analyst seat — the interview and
   resource-gathering never ran (the gate stopped before them), and the preload probe never ran
   because probing means spawning the seat. ⚠️ **7.3 has a history of failing silently:
   examiner-panel was born without its preload and nothing detected it.** Whoever first spawns
   this seat confirms both skill blocks actually arrived — a symlink that resolves is not proof
   the block loaded.
2. **The seat is UNSTAMPED.** First deliverable ① (the entitlement-vs-service-level reading of
   Paul's three tiers) is `[agent-proposed]`. Deliberately not run as a lane follow-on: it would
   skip the interview that is supposed to shape it, and the interview would then be reconciling
   against work it should have preceded.
3. ⭐ **THE UNWRITTEN TENSION has no home yet.** The 2026-08-13 study measured that within every
   niche the **utility** app beats the **journal** app by 100–10,000× in ratings volume — against
   Fernwood's ratified **field-journal, not task-manager** tone, which is load-bearing in two
   CLAUDE.md files. Nobody has written those two facts next to each other.
   **Hub's read: this is not a BACKLOG row.** A backlog row is work someone decided to do, and
   nobody has decided anything here. It is a DECISION, which makes `.decisions/` the right shape
   on this project's own terms. **Recommended to Paul rather than minted** — framing a decision he
   has not been asked yet is the part that should be his. Recorded here meanwhile so it cannot be
   lost, which is the failure mode item 3 was reported to prevent.

## Lane liveness — `python3 .plans/contracts/lane-watch.py [base-sha]`
A caller for `claude agents --json` + git's name-only log, per the audit's M3 (*give the door a
caller, don't build a watcher*). Reports, never gates. ⚠️ It **cannot** tell a hub write from a
lane's drift, so it names the path with its commit and asks a human — a checker that guessed
would be worse than one that asks.

### Lane D AT GATE (`6408706`) — hub-verified 2026-09-04

Every claim re-checked here, not relayed:
- **Scope honoured** — 2 files, both in OWNS: `engine/viewer.template.html` (the edit target)
  and `viewer.html` (rebuild output, never hand-edited). Nothing else.
- `build-viewer.py --check` → **byte-identical**. Not pushed.
- ⭐ **No data moved** — `git log 2e65319..HEAD -- zones.json data/` returns **0 commits**. The
  render-only constraint held in fact, not just in intent.
- **The Chaikin arithmetic reproduces exactly**: 437 stored vertices → 1,748 rendered, and 2
  iterations on closed rings must double twice (437→874→1,748). Reported figure matches computed.
- **The `is-draft` finding is real and is in the code** — `.pmap-zone.is-draft` sets
  `stroke-linecap: butt` for its dash ends, so with all 23 zones `draft` the round CAP is
  overridden everywhere and only the round JOIN does visible work today. Lane D did not touch it
  (dash grammar is Paul's) and left a comment so the next reader does not "fix" it.

⭐ **The vertex-identity assertion SHIPS rather than being observed once** — it re-runs every
render, publishes `window.__pmapVertexIdentityOK` so QA reads a verdict instead of scraping a
console, and uses `console.error` rather than `throw`, because a viewer that throws costs Mom the
page over a defect invisible on screen. At the condo the no-basemap early return sits above it, so
the flag is `undefined` (no map rendered) and never `false` — the falsifier stays honest.

⚠️ **Lane D stated the limit rather than overselling it:** at Mom's conditions (a 361px stage for
the whole property) the change is close to invisible; it shows the moment anyone zooms. The
exhibit says so on its face.

## 🔶 OPEN, no owner — surfaced by lanes, not assigned
- **The A/B lens fork** (lane C) — pointing an expectation lens at a REAL reader (at Fernwood,
  Mom) is a DISTINCT capability that inherits the quarantine clause and the administrator gate.
  Named out-of-scope in lane C's doc; needs Paul as its own decision.
- **The utility-vs-journal tension** (lane A) — recommended as a `.decisions/` card, not minted.
- **3DEP lidar coverage for Pickens is UNCONFIRMED** (§478) — it gates whether an adjacency
  exhibit can honestly be built at all, since 9 of 11 sliver pairs are sub-pixel on the current
  aerial. Minutes to check; not a lane.
- **The business-analyst seat is UNSTAMPED** — ritual steps 4, 5 and 7.3 owe, and the demographic
  work lane C needs is blocked behind them.

## 🔶 OPEN, no owner — added 2026-09-04 (running register; the hub's release condition discharges it)
- **`tools/qa-walk.py` measures ONE viewport** — hard-coded `414 × 848` at line 32, docstring
  "at HER conditions" at line 7. Deliberate and correct while only Mom's surface was in scope.
  ⚠️ **Paul has since ratified the centered column as the DESKTOP design and is himself a daily
  wide-view reader**, so desktop is in scope by his own ruling while the deterministic gate still
  covers one viewport — and two AI review passes are about to assume both are covered. **A coverage
  gap that reads as covered.** Surfaced by lane C while writing a consult prompt; not lane C's to
  fix. Held pending its ux-expert consult, which may rule a second deterministic viewport is not
  the right answer.
- **A spawned agent outlives the instruction that spawned it.** Lane C spawned two consults on
  Paul's direct instruction, declared it correctly, and named the running agents as the one thing
  that must not die with its window. The preamble's widening rule covers writes, not spawns.
  **New standard: declare a spawn AND name it as a dependency at close-out.** To fold into
  `_PREAMBLE.md` at the next run boundary — not now, because live lanes read their contract once.
