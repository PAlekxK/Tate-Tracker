# Interests reframe — independent verification (window `onboarding-ask-82`)

**Not the deliverable.** `onboarding-ask-b3` owns the reframe and the plan note; two windows were
launched on the same brief (`~/.claude/handoff/brief-onboarding-activities.md`) and b3's
implementation landed in the working tree at 16:02:31 on 2026-09-10, seconds before this window's
first read of the file. Per the concurrent-session guard this window wrote nothing to
`onboarding/index.html` and committed nothing. This file records what it verified, so the reading
survives if that window does not.

## Verified GREEN — the machinery is intact

| claim | how it was checked |
|---|---|
| 11 ids, their ORDER, `builds` and `soon` are byte-identical | `git diff` — every changed line is a `label:` or `desc:` |
| `read-onboarding.py` is unaffected | it parses the `>`-joined **ids**, not labels; `--selftest` 0 failures |
| the walk harness is unaffected | `journey-walk.py:293` clicks `button.interest[data-id="…"]` |
| the page still runs | every inline `<script>` parses under `new Function` |
| estate-neutrality | `check-estate-neutral.py` → `onboarding/index.html rendered=0` |
| **Mom's existing answers do not orphan** | the id is the join and is unchanged; her stored ranking is a `{id,label,soon}` snapshot in her own `localStorage`, so `estate/index.html:411` still replays the words she actually chose under; `viewer.html`'s `byLabel` fallback (for pre-id records) still resolves the OLD labels because `EMPTY_CARD_COPY` is unchanged |

## Two findings the diff does not name

### ⛔ 1 · The reframe retires Mom's coined phrase
`house-systems`: **"Household systems" → "Keeping things running"**. That word is protected by name
in `viewer.html`'s `EMPTY_CARD_COPY` — *"'Household systems' is Mom's own coined phrase and is
protected — do not normalise it"* — and by CLAUDE.md's standing rule, *adopt her words, never improve
them… if she names a thing, that is its name.* She coined it, hedged that it might be wrong, and was
right.
**Resolution that costs nothing:** `"Keeping the household systems running"` — the verb the reframe
wants, wrapped around the noun that is hers.

### ⚠️ 2 · All five built modules now carry two names
`EMPTY_CARD_COPY` in `viewer.html` is unchanged, so the onboarding ask and the app disagree:

| id | ranked as (onboarding) | shown as (app) |
|---|---|---|
| house-systems | Keeping things running | Household systems |
| equipment | Working with tools | Equipment and tools |
| garden | Growing things | Gardening |
| motor-pool | Looking after a vehicle | Vehicles |
| wildlife | Watching what comes around | Wildlife |

Not cosmetic: the ask-next chip (`viewer.html:18527-18532`) writes **its own** label into
`fw-onboard-interests` — the same store `estate/index.html` replays as *"What I'll build first"* — so
one reader's own list can carry both vocabularies, on the screen whose entire job is showing that we
heard them. (It cannot produce a *duplicate* row: ask-next filters modules already ranked.)
`viewer.html` belongs to another window, so this is either coordinated or recorded as a known
divergence — not left silent.

## Two brief claims that failed verification

- **"Five tools read `builds`" — FALSE.** `grep -rn '\bbuilds\b'` finds **zero** consumers outside
  `onboarding/index.html`. What those five tools read is the module/domain *vocabulary* `builds`
  names. What is actually wired today: ranked **ids** → `saveProfile` → grant/account
  (`worker.js:826, 3877, 4142`) → `viewer.html` `READER_RANKING` (card order + idea cards) and
  `estate/index.html`; `read-onboarding.py` tallies the ids. **The ranking→module-switch path does
  not exist yet.** ⭐ That is exactly what makes the new *"It doesn't switch anything on or off"*
  sentence true today — and a lie the day it is wired. The sentence needs that note beside it.
- **The addendum's 🔴 on the address screen is OVERSTATED** — the same noise hazard the lens's own
  rule warns about. `onboarding/index.html:584` already renders: *"We work out your weather and what
  grows there from this address. Paul — who built this — is the only other person who sees it. You
  can fix it before saving."* → USE ✅ · WHO SEES IT ✅ · pre-save reversibility ✅.
  **Genuinely missing:** the NOT-use clause, and post-save reversibility. `ok2` ("Not quite") posts a
  dispute and opens a note box; it does **not** reopen the form — so the honest clause is *tell Paul
  and he fixes it*, and that is true (`worker.js:1138-1156` re-geocodes a changed address and drops
  the stale coordinates rather than keeping them).
  **The 🟠 on the account screen is CONFIRMED**, with a bonus: the comment at `:398` asserts the
  reversibility clause is present because `/api/account/username` re-keys the row — the rendered `<p>`
  says only *"Anyone who shares a place with you sees this."* The comment claims copy the markup does
  not contain.

## One product call being made in copy

The diff cites the only free text anyone has ever typed into *Something else* — **"Houseplants!"** —
as the warrant for `garden`: "Gardening" → "Growing things" / "Anything planted".
`feedback-dispositions.json:102` ruled that record **a twelfth interest, NOT a module request**, and
*"whether to build anything for it stays Paul."* Widening the label to reach a windowsill absorbs it
into the garden module ahead of that ruling. Defensible — a houseplant is a plant record — but it is
his call, not copy's.

## Copy nits, all pre-confirm (authored content is human-confirmed before it ships)

- *"…spend time on **here**?"* re-opens the ambiguity the block's own ⭐ comment rules against —
  **ABOUT HER PLACE, NOT ABOUT THE SCREEN**. "at your place" was carrying that.
- *"Only **I** see it"* answers WHO SEES IT with an unnamed first person, while every other
  disclosure on the page names him (`:584`, and the feedback box's "comes straight to Paul").
- The chrome above the list goes ~20 → ~45 words across four paragraphs, on the screen
  content-steward already flagged as carrying the most reading in the journey. The contract is owed;
  lines 3 and 4 could merge.

## One thing the diff got right that is easy to undo later

**"Something else" must keep that exact label.** `viewer.html:18476` suppresses that idea card by
`label.toLowerCase() === "something else"`. Rename it and "Something else" renders as an idea card in
the app. Recorded here because nothing checks it.
