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

## ⭐ WHERE A QUESTION GOES — hub first, then ASK PAUL IN YOUR OWN TAB `[paul-stated 2026-09-04]`

**Supersedes the first version of this rule, which sent everything to the hub and had the hub
relay gates to Paul. That was wrong** — it stripped each question of the context that made it
answerable, and Paul had to answer blind in a window that held none of the material.

**The sequence, every time:**

1. **CHECK WITH THE HUB FIRST — always**, including things you are sure are Paul questions.
   No exceptions, and no "this one is obviously his."
2. **The hub answers what it can**, routes what is actually another lane's, and kills what is
   already settled elsewhere. Most questions die here. That is the point.
3. **If the hub confirms it is truly a gate for Paul, YOU ask him — in YOUR OWN TAB**, with the
   surrounding context visible. ⛔ **Do not hand it back to the hub to relay.** He wants to look
   up, see the full context, and answer where the work is.
4. **The hub tells Paul WHICH TABS are waiting — never the question itself.** A pointer, so he
   has one place to see what is pending without the questions being torn out of their context.

**Why it is this shape.** A gate needs its evidence in the same window as its question. Relaying
one into the hub window turns a decision he could make in ten seconds into a decision he has to
reconstruct. Meanwhile the *filtering* genuinely belongs to the hub, because you only see your own
lane and cannot know a neighbour already answered it.

**The bar for step 3 is "truly a gate"** — it changes what gets built, it is authoring or taste or
priority, or it is his to rule on by doctrine. Not "I would like a second opinion," and not
"confirm what I just did." Those stop at step 2.

⚠️ It is easy to over-answer by one step. Describing what is in front of him next is fine;
**offering to do it is not** — that is a sequencing decision and it belongs to the hub. A lane
caught itself doing exactly this on run 1, after the fact, and flagged it. Flagging beats silence;
not doing it beats both.

## Answering Paul when he asks YOU something

He uses lane tabs deliberately. **Answer freely about your own lane** — content, findings,
reasoning, artifacts, why you did what you did. You are the best window for that and the hub is
only a relay. What still routes to the hub is the *run's shape*: what happens next, who owns a
piece of work, whether something becomes a canon or backlog row, whether you may widen scope.

## 🔶 WIDENING SCOPE — operating rule, NOT YET RATIFIED

The hub is running on this and has told lanes so, but Paul has not stamped it. Treat as live;
expect it to change:

> **OWNS binds for the duration of the run. Paul's direct instruction supersedes it — but a lane
> acting on one must first verify no other writer is live in the affected tree, and must DECLARE
> the widening to the hub in the same breath as doing it.** Silence is the violation, not the
> widening.

Derived from run 1, where a lane hit this with no rule to follow and improvised all three parts
correctly. Written down so the next lane does not have to be that careful to be that lucky.

## ⭐ WHEN YOU ARE DONE — CLOSE OUT AND SAY SO `[paul-stated 2026-09-04]`

**A lane at a terminal state does not sit.** When your gate is met, your questions are answered or
routed, and you hold nothing another lane needs — **close out and tell Paul the window is ready to
clear.** Do not wait to be noticed. A lane holding quietly is indistinguishable from a lane still
working, and it is a latent second writer in the tree for as long as it sits.

**Before you declare ready-to-clear, verify — and report the answers, not the conclusion:**
1. Everything you produced is **committed by explicit path**; nothing of yours is uncommitted.
2. Nothing is running in the background in your session.
3. Your contract's `## STATUS` line is accurate, including its RELEASE CONDITION.
4. You **name anything you were carrying that must not die with you** — an open dependency, an
   unanswered question, a finding that lives only in your context. The hub takes those explicitly.
   Something that exists only in a closing session's head is the thing that gets lost.
5. Ask the hub before closing, and say what closing would destroy. Run 1's lane A did exactly this
   and its two closing questions found **two real defects in the hub's own tooling** — a watcher
   that could not tell a clean finish from a death, and a report that read a cross-repo lane's work
   as "did nothing." **The close-out check is not a formality; it is the last review of the run.**

## What you are NOT

You are not the hub. You do not re-plan the queue, re-order other lanes, or
decide what Paul works on next. You end at your gate and report.
