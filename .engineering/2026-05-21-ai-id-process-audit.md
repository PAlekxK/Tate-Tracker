# AI-ID species addition — process audit

**Date:** 2026-05-21 (evening)
**Trigger:** A silent drift bug surfaced during Phase H build verification. The first auto-promoted species (Pop Star Endless Summer Reblooming Hydrangea, via Phase F Option C on Mom's behalf) was in `plants.json` but missing from inlined `PLANTS_DATA` in viewer.html. Dashboard rendered without the entry; Playwright check caught it during a routine "cards expand correctly" sweep.

## The bug chain (what happened)

1. Mom submitted a photo via the Phase F flow.
2. Worker's `handlePromoteSpecies` ran the schema drafter + made **three separate GitHub commits** (per the path-eval's recommended shape):
   - **A.** Update `plants.json` — append the hydrangea entry.
   - **B.** Update `viewer.html` — re-inline `PLANTS_DATA` to include the new entry.
   - **C.** Add the photo file at `images/plants/endless-summer-pop-star-hydrangea.jpg`.
3. All three commits landed on `origin/main` cleanly. Dashboard would have shown the hydrangea after the next GH Pages deploy.
4. I (Claude, working locally) had unpushed commits and ran `git pull --rebase origin main` to incorporate Mom's promote.
5. Conflict on `viewer.html` (because both my docs sweep AND Mom's auto-promote touched it).
6. I resolved with `git checkout --theirs viewer.html` — **wrong direction in rebase context.** In a rebase, `--theirs` refers to the commits being rebased (mine), not the upstream (origin's auto-promote). I should have used `--ours` to keep the auto-promote's re-inline.
7. The resolved viewer.html silently dropped commit B's PLANTS_DATA re-inline. `plants.json` retained the entry; viewer.html's inlined `PLANTS_DATA` reverted to the pre-hydrangea 17-entry version.
8. The drift wasn't visible in normal review — the source JSON looked correct; the dashboard's runtime fetch *might* have masked it if working; but the inlined fallback (and `PLANTS_DATA` reference in JS test code) was stale.
9. Caught later during Phase H build verification, by accident.

## Root causes (the process gaps)

### 1. Three commits per promotion = three conflict surfaces
Phase F Option C's `handlePromoteSpecies` issues three sequential `PUT /repos/.../contents/<path>` calls — one per file. Each lands as its own commit. The choice was made for legible git log ("you can see exactly what each commit did"). But the cost: any rebase that lands between these commits and a local working branch has THREE potential conflict points, each individually resolvable. A wrong-direction resolution on any one of them silently breaks the invariant that JSON + inlined const + photo agree.

**Fix path:** consolidate into a single tree commit via GitHub's Git Data API (`createBlob` + `createTree` + `createCommit`). One commit, atomic, three files change together. Cleaner git log too — `git show <sha>` shows the full unit of work.

### 2. No drift detection between source JSON and inlined consts
The viewer.html pattern of inlining `PLANTS_DATA`, `MAMMALS_DATA`, etc. as JS consts (for fast first-paint + offline-friendly fallback) means there are TWO copies of the same data: the source JSON and the inlined const. Nothing automated checks they agree. The `wire-photos.py` tool is the one place this invariant is maintained — but it's only called explicitly when re-inlining a category, not as a pre-commit guard.

**Fix path:** add a drift-check script (`tools/check-data-inline.py`) that scans all 7 source JSONs against their inlined consts and exits non-zero if any drift. Optional `--fix` flag that re-runs `wire-photos.py` for drifted categories. Run as part of pre-commit hook OR in CI OR as part of `tools/run-propagators.sh`-style automation.

### 3. The `--theirs` / `--ours` direction flip in rebase vs merge is a known footgun
Merge: `--ours` = current branch HEAD, `--theirs` = the branch being merged in.
Rebase: `--ours` = the upstream (the branch you're rebasing onto), `--theirs` = the commits being rebased.

The semantics flip. During a rebase conflict, `--theirs` is your own incoming commits, not the upstream's. This isn't documented loudly enough in git's CLI; many engineers get bitten by it.

**Fix path:** document the pitfall in `~/.claude/engineering-principles/`. When resolving a viewer.html conflict during a rebase that involves an auto-promote merge, the right move is `--ours` (keep upstream's auto-promote) followed by manually re-applying any of your own local changes on top.

### 4. No post-promote verification in the Worker
After the 3 commits land, the Worker returns `{ok: true, slug, photoCommitted, ...}` and is done. It doesn't verify that the final state of `viewer.html` on `origin/main` actually has the new entry in PLANTS_DATA. A successful PUT to GitHub doesn't guarantee the resulting file is well-formed; intervening merges could in principle corrupt the state.

**Fix path:** add a post-promote check that GETs the final viewer.html, parses the relevant const, confirms the new id is present. Log a structured `promote_verification_failed` event if not. Cheap (one extra GET); high signal.

### 5. The runtime fetch/fallback architecture masks drift
Per CLAUDE.md: "JSON files are the source of truth — they are fetched at page load and the inlined copies in viewer.html serve as fallback." So if the runtime fetch of `plants.json` succeeds, the dashboard uses the FRESH JSON and the drift is invisible. The drift only becomes visible when fetch fails (CORS hiccup, slow network, etc.) AND the user is looking at the affected entry.

That architecture is mostly good — it means drift doesn't immediately break the user experience. But it also means drift is silent: no error logged, no visible symptom, until the fallback kicks in. The drift-check tool above is the active guard. The architecture itself is fine; just need the guard.

## Process fixes to ship

| # | Fix | Status |
|---|---|---|
| 1 | Drift-check script (`tools/check-data-inline.py`) — scans all 7 *_DATA consts vs source JSONs; exit 1 on drift; `--fix` re-runs wire-photos.py | **Shipped 2026-05-21** in this commit |
| 2 | Document the rebase `--ours`/`--theirs` pitfall — added to this memo + flagged for promotion to `~/.claude/engineering-principles/` | This memo; principle promotion deferred |
| 3 | Atomic tree-commit refactor for `handlePromoteSpecies` (replace 3 sequential PUT calls with one Git Data API tree commit) | **Deferred** — substantial refactor; the drift-check above covers the gap for now |
| 4 | Post-promote verification in the Worker (GET viewer.html + verify entry present + log if missing) | **Deferred** — drift-check at commit time covers the same gap from a different angle |
| 5 | Pre-commit hook or CI integration of the drift-check | **Deferred** — script is callable manually for now; integration is a follow-up |

## The principle this surfaces

**Procedure-as-contract over procedure-as-prose** (engineering-partner candidate from W1b audit, awaiting third occurrence before formal promotion). The 3-commit auto-promote was a *procedure* — defined in prose comments + the Worker code. Its invariant (all 3 must land together) was not encoded as a *contract* the system could enforce. A drift-check script encodes the invariant as a contract: any state where source JSON and inlined const disagree fails the check.

The Git Data API tree-commit refactor would be the stronger version of the same principle — make the invariant impossible to violate, not just easy to detect. Worth doing when there's time.

## Related principles

- **`landscape-research-before-deep-work`** — Phase F Option C's 3-commit shape was the cheap path; the tree-commit shape was the more principled path. Path-eval recommended either; we shipped cheap. The drift bug is the cost of that choice.
- **`feedback_single_source_of_truth`** — inlining `*_DATA` consts violates this in spirit (there are two copies). The "JSON is source of truth; inline is fallback" framing is the project-level resolution, but the drift-check is the *enforcement*.
- **`feedback_ground_truth_research_claims`** — the post-mortem here: claims about "the auto-promote worked correctly" need ground-truth checks against the actual deployed state, not just the Worker's success response.

## What to take into Phase H

Phase H (audio identification, in flight 2026-05-21 evening) will eventually produce promoted species entries with an `audioSamplePath` field — a fourth file commit per promotion. The same drift surface applies. The drift-check tool above doesn't currently check that `audioSamplePath` files exist; that's an extension worth adding when the first audio-promoted entry lands.

When migrating to the tree-commit refactor (deferred per row 3 above), Phase H's audio commit slots in cleanly as a fourth tree entry — no architectural change needed beyond adding the entry to the createTree call.
