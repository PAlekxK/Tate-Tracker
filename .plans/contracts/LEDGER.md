# Lane ledger — held by the hub session

**Hub:** `paulkirschenbauer-0b [45dbaa]` · opened 2026-09-04 PM ET
**Repo state at launch:** `main` @ 0bcbc86, tracking `origin/staging` (QA). Prod FROZEN.

| Lane | Topic | Writes | Status |
|---|---|---|---|
| A | business-analyst seat | `~/.claude/agents/` + foundation | launched |
| B | map-region smoothing | one new `.plans/` doc | launched |
| C | fictive test user | one new `.user-research/` doc | launched |
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
