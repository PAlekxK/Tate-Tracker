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
