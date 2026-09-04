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

## What you are NOT

You are not the hub. You do not re-plan the queue, re-order other lanes, or
decide what Paul works on next. You end at your gate and report.
