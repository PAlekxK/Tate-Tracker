# Lane ledger — held by the hub session

**Hub:** `paulkirschenbauer-0b [45dbaa]` · opened 2026-09-04 PM ET
**Repo state at launch:** `main` @ 0bcbc86, tracking `origin/staging` (QA). Prod FROZEN.

| Lane | Topic | Writes | Status |
|---|---|---|---|
| A | business-analyst seat | `~/.claude/agents/` + foundation | ✅ AT GATE — `fa9d368`, marked UNSTAMPED. Paul stamps the foundation before the seat works |
| B | map-region smoothing | one new `.plans/` doc | ▶ in flight (plan file staged, uncommitted) |
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
