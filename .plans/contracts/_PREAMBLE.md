# Lane contract — shared preamble (every lane reads this first)

You are ONE LANE in a parallel Fernwood run launched 2026-09-04 PM ET.

**Hub session:** `paulkirschenbauer-0b [45dbaa]`. It holds the ledger
(`LEDGER.md`, this directory) and is the only session that pushes.

## The five hard rules

1. **Write ONLY your OWNS paths.** They are listed explicitly in your lane file.
   Anything not named is another lane's or the hub's. If your work genuinely
   needs a path outside OWNS, **SendMessage the hub and wait** — do not take it.
2. **NEVER `git add -A`.** Stage explicit paths, always. Measured twice in this
   portfolio: 2026-07-14 on this repo (a viewer.html change absorbed into
   another session's commit) and 2026-08-28 in `~/.claude`. `git add -A` in a
   shared tree commits whatever is on disk, including other lanes' work.
3. **Commit your own edits the moment they exist**, by path. An uncommitted edit
   in a shared tree is *unowned* — the next `git add` from any window claims it.
   Do not hold edits while you compose a report.
4. **Do NOT push, do NOT switch branches, do NOT create worktrees.** Local `main`
   tracks `origin/staging` (QA) and `prod` tracks `origin/main` (Mom's live
   page). Getting that backwards ships to Mom. The hub pushes.
5. **Report to the hub at your gate** — `SendMessage` to `paulkirschenbauer-0b`.
   Say: what you produced, the path, what you did NOT do, and what needs Paul.

## Standing project constraints (not negotiable by a lane)

- **Prod is FROZEN. Mom's feedback is HELD.** Touch no Mom-facing surface.
- **The AI boundary:** AI never touches an estate's people or their words. It may
  draft for approval on the way in, or analyze the record on the way out — the
  **administrator's eyes** sit between the model and the estate's people, both
  directions. (`CLAUDE.md`, paul-ratified 2026-09-02.)
- **Capture stays deterministic and AI-free.** AI lives on the ask path.
- **`estate` is a schema word and never reaches a user-facing surface.** Read
  `VOCABULARY.md` §4 before proposing any name — it records what was rejected and
  why, including *"estate manager"* itself.
- Voice-memo transcripts that seeded these lanes are at
  `.private/voice-memos/` (gitignored). ⚠️ They are **whisper transcriptions —
  model reads, not verified quotes.** Use them for substance; do NOT stamp any
  phrasing as a verbatim `[paul-stated]` ruling. Paul has not yet reviewed the
  wording.

## ⭐ ROUTE QUESTIONS TO THE HUB `[paul-stated 2026-09-04]`

**Every question of scope, sequencing or ownership goes to the hub — you do not answer it in
your tab.** Single source of truth. Route: what happens next · who owns a piece of work ·
whether something becomes a BACKLOG / canon / principle-library row · whether you may widen
scope · what another lane is doing · anything that would have you describing the shape of the
overall run.

**You DO still answer Paul directly about your own lane** — its content, findings, reasoning and
artifacts. He uses lane tabs deliberately and should not have to come to the hub for what you
just produced. The split is: *your work, you answer; the run's shape, the hub answers.* You only
see your own lane, and answering from that view is how two windows start disagreeing — which is
the whole thing this rule prevents.

⚠️ It is easy to over-answer by one step. Describing what is in front of him next is fine;
**offering to do it is not** — that is a sequencing decision. A lane caught itself doing exactly
this on run 1, after the fact, and flagged it. Flagging beats silence; not doing it beats both.

## 🔶 WIDENING SCOPE — operating rule, NOT YET RATIFIED

The hub is running on this and has told lanes so, but Paul has not stamped it. Treat as live;
expect it to change:

> **OWNS binds for the duration of the run. Paul's direct instruction supersedes it — but a lane
> acting on one must first verify no other writer is live in the affected tree, and must DECLARE
> the widening to the hub in the same breath as doing it.** Silence is the violation, not the
> widening.

Derived from run 1, where a lane hit this with no rule to follow and improvised all three parts
correctly. Written down so the next lane does not have to be that careful to be that lucky.

## What you are NOT

You are not the hub. You do not re-plan the queue, re-order other lanes, or
decide what Paul works on next. You end at your gate and report.
