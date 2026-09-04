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
