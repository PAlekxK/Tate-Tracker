# Path eval — how QA declares what Fernwood-live does not

- date: 2026-09-04
- mode: path-evaluation
- seat: engineering-partner
- asked by: Paul, 2026-09-04 — *"do an analysis about whether this is the best way — it sounds good to me overall"*
- prompted by: `[paul-stated 2026-09-04 ~1:25 AM ET]` *"this is where we start to potentially diverge from the live
  Fernwood mom sees… we need to make additions in a way that's trackable."*
- read: `PRODUCT-ENGINE.md` § THE SEQUENCE · `.plans/2026-09-03-c4-environments-PLAN.md` (3a–3g, 5b, 5c) ·
  `.plans/2026-09-03-c6-door-for-paul-PLAN.md` step 5b · `tools/build-viewer.py` · `tools/qa-divergence.py` ·
  `tools/check-live.py` · `tools/git-merge-generated.py` · `.github/workflows/build-viewer.yml` ·
  `.github/workflows/deploy-worker-qa.yml` · `estate.json` · `instance/fernwood.json` ·
  `BACKLOG.md` § BUILD IT ALL IN QA (+ the 2026-09-04 amendment)
- stakes: one live reader (Mom), one live page. Not enterprise. Severity is calibrated to *she loads a page that
  says the wrong thing about her house*, which is a trust cost, not a security or data-loss cost.

---

## The recommendation, first

**Take none of A–D as posed. Take (E): keep ONE divergence mechanism — the `staging` branch — and commit the
QA-only value directly into `instance/fernwood.json` on `staging`, with a rebuilt `viewer.html` committed beside
it. Then add a small FIXTURE REGISTER that names, per key, every value that is QA-only and must never reach
`main`.**

The register is the new thing. The branch is not — it already exists, it already carries the divergence, and
`qa-divergence.py` already tracks it at commit granularity with a stage-note gate. What is genuinely missing is
not a *layering* mechanism for the instance file. It is a *check at the boundary where QA values could cross
into prod*.

### The argument in one paragraph

Look at what actually diverges for the first real case. C6 5b's design is already correct: the vault card's
**code** is invisible by construction when `vault.rooms` is empty, so the card, its CSS and its render condition
are prod-safe and can ship to `main` normally — the same declared-absence vocabulary `build-viewer.py` already
uses for `absent: []` and `estate.json` already uses for modules. **The only thing that must not migrate is one
key holding one fixture value.** An overlay file, a forked instance, an env axis in the schema, or a client
origin gate are all mechanisms for layering a *file*. You have a one-key problem. Build the guard at the key.

---

## The trade-off space

| | (A) `fernwood.qa.json` overlay, applied at QA deploy | (B) fork `instance/fernwood-qa.json` | (C) origin gate — `IS_QA_ORIGIN` | (D) env-conditional keys, `--env qa` at build | **(E) branch + fixture register** |
|---|---|---|---|---|---|
| **Complexity** | New layering semantics, a deploy-time build step, a branch-conditional in CI | Lowest new machinery, highest duplication | Zero new machinery — the mechanism is already shipped | New env axis inside the instance schema; every reader must now ask "which env" | One new ~80-line tool + one register file. No new semantics |
| **Byte-identity (`--check`)** | 🔴 **Breaks.** `--check` on `staging` would verify a `viewer.html` that nothing serves | 🔴 Same break | ✅ Untouched | 🔴 Same break, plus `--check` needs to know the branch | ✅ Untouched, and now checks the artifact each branch actually serves |
| **`check-live --ref HEAD`** | 🔴 **Breaks or must be weakened.** Served ≠ commit. Weakening it to "compare against CI's own rebuild" makes the check circular | 🔴 Same | ✅ Untouched | 🔴 Same | ✅ Untouched on both origins |
| **Trackability (Paul's word)** | Partial — the overlay is diffable, but one overlay commit can carry N features; ledger granularity drops | Poor — a fork drifts silently in the *unmeasured* direction | 🔴 Worst — the divergence lives in an `if` inside 2 MB of engine code; nothing enumerates it | Partial — same as A | ✅ Best — commit-level ledger (already built) **plus** a per-key declared list |
| **C4 5c falsifier** (same engine renders the condo from its own instance) | Risk — an overlay is a second identity mechanism laid over the first | 🔴 Fails the spirit — two files, one `estateId`; contradicts `estate.json`'s "one file says which estate this checkout IS" | Risk — a *third* renderer-gating mechanism beside modules and declared-absence | 🔴 Fails — the condo has no environments; contaminating the instance contract with an env axis is engine debt for every future estate | ✅ Untouched — one instance file per estate, no env awareness anywhere |
| **Shadowing at migration** | 🔴 **This is A's real failure mode.** An overlay key that shadows a real instance key is invisible until the day the overlay stops being applied | 🔴 Worse — the fork *is* permanent shadowing | ✅ N/A, but replaced by a worse one: a host-shaped gate that rots the day the custom domain lands | 🔴 Two environments' truth in one file — the exact shape Paul flagged | 🟡 Real, and it is what the register exists to catch — at merge, at cherry-pick, and at the migration |
| **Cache/CDN** | Deploy becomes non-deterministic: the same sha can upload different bytes if canon or the overlay moved | Same | None | Same | None — Pages keeps uploading `git archive` of the commit |
| **Future-Paul-with-Claude** | "Which file won for this key?" is a two-file question with no tool to answer it | Two files to keep in sync by hand | "Why is this dark?" is a grep through 18,000 lines | Worst — the schema now has a hidden dimension | One file per estate; one register that prints itself |
| **Learning value** | Teaches config layering — real, but the lesson you'd learn is *why not to* | Low | Low | Medium | Teaches the durable one: **a derived artifact's branch divergence is a rebuild, never a merge** |

### The three findings behind that table

**① The deploy-time build is the disqualifier for A, B and D, and it is not a nit.**
This repo's most expensive lesson is written in `check-live.py`'s own docstring: *a commit is not a ship, and a
push is not a ship either*. That check works because **the bytes on the origin are the bytes in the commit** —
`deploy-worker-qa.yml` uploads a `git archive` export for exactly that reason. The moment CI builds `viewer.html`
at deploy time, `check-live --base QA --ref HEAD` goes red by design and has to be weakened into "compare the
served file to a fresh rebuild," which is CI checking its own arithmetic. At the same moment
`build-viewer.py --check` on `staging` starts verifying a committed `viewer.html` that nothing loads. You would
be running two green checks over an artifact nobody serves while shipping an artifact nothing checks. That is
strictly worse than no check, because it reads green.

Note what A's benefit actually is, stated plainly: **the overlay's only real gain is keeping
`instance/fernwood.json` byte-identical across branches so it never conflicts on a merge.** That is a
merge-hygiene benefit, and it is bought at the price of hollowing out the two checks that verify what Mom loads.
A register buys the same safety without touching either check.

**② (C) is right for environment shape and wrong for instance shape — and this distinction is worth keeping.**
`IS_QA_ORIGIN` is correct today for `WORKER_BASE`, the ` · QA` title marker and the `/qa-build.json` banner:
those are facts about *which environment this is*, and a hostname is the honest source for that. A vault room is
a fact about *which estate this is*. Two reasons not to stretch the gate over it:
- The regex is `/\.pages\.dev$/`. The C4 plan already schedules a custom domain (`<family-a>.myhome.place`), and
  Pages already serves preview hosts. A host-shaped gate rots the day the host changes, and it rots toward
  *lighting the feature up on her page*, not toward hiding it.
- The migration act becomes **deleting a gate from engine code** rather than flipping a declaration in a
  config file. That puts a code edit at the single riskiest moment in the plan. Migration should be a data change.

Also: Paul's own standing rule — *reuse the vocabulary before adding a state*. Rendering is already decided by
two declared mechanisms (`estate.json` modules, and the instance's `absent` / declared-empty). A client-side env
gate would be a third, with different failure semantics from both.

**③ The shadowing hazard is real under (E) too, and it does not wait for the migration.**
`BACKLOG.md`'s branch consequence note is explicit: local `main` is the QA integration line, and prod-needed
changes go out by cherry-pick onto a `prod` branch. The 6a stage-note records the discipline already in use —
`git diff origin/main prod -- viewer.html instance/ engine/` must be EMPTY. That works *because nothing SURFACE
has diverged yet*. The day `instance/fernwood.json` carries a fixture room, that diff is no longer empty, and the
question "is this cherry-pick safe" stops being answerable by eye. The register is what makes it answerable —
at the cherry-pick, at any merge, and at the migration, by the same check.

---

## What (E) is, concretely

Three changes. All small, all reversible, none touching the engine contract.

### 1. `tools/qa-fixtures.json` — the declared list

A tracked register on **both** branches (TOOLING class in the ledger, so it never pollutes SURFACE). One row per
QA-only value:

```
{ "key": "vault.rooms", "file": "instance/fernwood.json",
  "qaValue": ["qa-contacts"], "prodValue": [],
  "why": "C6 5b fixture room — proves the card renders; Fernwood's real room is 5c, Paul's",
  "retiredBy": ".plans/2026-09-03-c6-door-for-paul-PLAN.md 5c" }
```

`why` and `retiredBy` are the load-bearing fields, not `qaValue`. A fixture with no named retirement is a
permanent fork wearing a fixture's clothes.

**Reinforce it where the value shape allows:** C6 3a already minted `est-qa0001` / `est-qa0002`. Keep that —
prefix every QA fixture *id* with `qa-`. A value that carries its own provenance can't be missed by a register
that drifted (*match the payload, not the container*). It doesn't work for a theme colour, which is why the
register is primary and the prefix is reinforcement.

### 2. `tools/check-qa-fixtures.py` — the caller, because a register with no caller is a comment

- **default:** print each row with its current value in the working tree and on `origin/main`. This is the
  glanceable "what does QA declare that prod does not" surface, per key.
- **`--check`:** exit 1 if any row's `qaValue` is present in a ref destined for `main`. Run it against the
  working tree when the branch is `main` or `prod`, and against the merge result at the migration.
- **`--selftest`:** plant a fixture value in a scratch instance file and prove it goes red. Fail CLOSED on a
  missing or unparseable register — the same posture `check-storage-keys.py` takes (exit 2 on a missing roster).

Wire it into: `build-viewer.yml` (runs on both branches already, and `instance/**` is in its `paths:`), the
session-start block in `CLAUDE.md` beside `qa-divergence.py --check`, and the pre-push path for `main`/`prod`.

### 3. Print the register inside `qa-divergence.py`, and write the migration procedure down

`qa-divergence.py` today answers *which commits*. Add a `DECLARED FIXTURES` section so it also answers *which
values* — one command for Paul's "declared, diffable thing," rather than two tools he has to remember to pair.

And record the migration as a stage-note in the C4 plan, because this is the sentence that prevents the accident:

> **At the migration, set the registered keys to their `prodValue` on `main`, run `build-viewer.py`, and commit.
> Never merge `viewer.html`.** `build-viewer.py --check` proves the rebuild happened; `check-qa-fixtures.py
> --check` proves no fixture rode along.

This is not a new idea in this repo — `.gitattributes` + `tools/git-merge-generated.py` already say exactly this
about `worker/digest.json`: *a conflict in a derived file is never a disagreement about intent, so a machine
gives the answer, and for a pure function of its sources the answer is REGENERATE.* If the 2 MB `viewer.html`
conflicts turn out to be a real friction (see the falsifier below), the cheap fix is a third merge driver,
`fernwood-viewer` → rebuild — not a change of architecture.

---

## The falsifier

**(E) is wrong the moment a QA fixture value reaches `origin/main` or Mom's served page.** Concretely, either of:
- `check-qa-fixtures.py --check` goes red on `main` or on a `prod` cherry-pick branch, **or**
- the rendered prod page contains a fixture room title / any `qa-` prefixed id (a Playwright read at 414 × A+
  against `palekxk.github.io`, the same conditions every other release check runs at).

If that fires, the branch-plus-register model was not enough separation and the overlay's stronger physical
split has earned its cost — at which point pay for it properly, by moving the build to commit time with an
explicit `--overlay` flag, never to deploy time.

**Secondary falsifier, for the part of the recommendation most likely to be wrong:** if committing a divergent
2 MB `viewer.html` on `staging` produces merge or cherry-pick friction that *actually blocks a release once* —
not "is annoying," but blocks — then the "prod's viewer is the only committed viewer" property that A buys is
worth revisiting. First response is the merge driver, not the overlay.

---

## What this must NOT do

1. **Must not build `viewer.html` at deploy time.** It hollows out `build-viewer.py --check` and
   `check-live.py --ref HEAD` simultaneously, and both go green while doing it.
2. **Must not put an environment axis into the instance schema or the engine.** The condo has no environments; it
   has an instance. Anything conditional on `qa` inside `instance/*.json` or `build-viewer.py`'s contract is debt
   every future estate pays.
3. **Must not create a second instance file carrying the same `estateId`.** `estate.json`'s own rule — one file
   says which estate this checkout IS — is what the C4 5c falsifier rests on.
4. **Must not use `IS_QA_ORIGIN` to gate an instance-declared feature.** Keep the origin gate for environment
   facts (`WORKER_BASE`, the QA banner, the title marker) and nothing else. A host regex is not a feature flag.
5. **Must not merge `viewer.html` at the migration.** Rebuild it from the merged inputs and let `--check` prove it.
6. **Must not let a fixture exist without a named retirement.** `retiredBy` is what keeps the register from
   quietly becoming a permanent second product.

---

## Praise, on the record

**C6 5b's design is already the right shape and should not be changed by any of this.** Rendering the vault card
only when `vault.rooms` is non-empty, and declaring Fernwood's as `rooms: []` — *declared empty, never absent* —
means her surface is untouched **by construction** rather than by a gate someone has to remember. That is the
same vocabulary `absent: []` and the module block already use, reused rather than reinvented. The entire question
in this document only exists because that design pushed the divergence down to a single declared value, which is
exactly where you want a divergence to live.

**And `qa-divergence.py` is already most of the answer to Paul's ask.** Classing by surface, requiring a plan
stage-note for every SURFACE commit, and reading subjects rather than shas because *a sha moves under rebase and
a subject does not* — that is the trackability requirement, built. The register is a per-key complement to it,
not a replacement.

---

## Open questions for Paul

1. **Does the register live at `tools/qa-fixtures.json` or inside `instance/fernwood.json`'s `_meta`?** I
   recommend `tools/` — the ledger classes `instance/` as SURFACE, and a register that changes should not
   register as a change to her surface. But an argument exists for keeping the declaration next to the thing it
   declares. Your call.
2. ~~**Does the theme colour, when it comes, get a fixture row or a real prod value?**~~ — **answered while this
   file was being written.** `identity.theme` landed in `instance/fernwood.json` mid-analysis (another live
   session), and its own `_note` settles it: *"this value must be derived from what she sees today, not typed
   here."* That makes it a **real prod value staged on the branch, NOT a fixture** — the branch plus
   `qa-divergence.py` already track it correctly, and it must NOT get a register row. The general rule it
   establishes, which is the useful part: **a value that will eventually be true at Fernwood is a staged prod
   change; only a value that must never be true at Fernwood is a fixture.** If the register ever grows a row for
   something in the first category, the register is being used as a backlog and has drifted from its purpose.
3. **Should `check-qa-fixtures.py` run at the pre-push guard for `main`, or only in CI?** CI catches it after the
   push, which for `main` means after Mom's page has already rebuilt. I lean pre-push, but that guard path has
   its own recorded defect (the 3a `tail` incident — never pipe a guard), so it wants to be added carefully.

---

## Principles this would propose (not added — proposing only)

**A derived artifact's branch divergence is a rebuild, never a merge.** — scope: cross-project. Rationale:
`viewer.html`, `worker/digest.json` and `weather-history.json` are all pure-or-near-pure functions of tracked
sources. `git-merge-generated.py` already ratifies this for two of them; the third is about to need it. The
general form — *when two branches disagree about a generated file, regenerate from the merged inputs; picking a
side is guessing* — generalizes past Fernwood.

**A test fixture that crosses into production is a data problem, not a config-layering problem.** — scope:
cross-project. Rationale: the instinct when QA needs different values is to build a layering mechanism. The
cheaper and more honest instrument is a register naming which values are fixtures plus a check at the boundary
they must not cross — because the layering mechanism has to be correct at every read, while the register only
has to be correct at one gate.

---

# RE-ANSWER — 2026-09-04, with the freeze as the premise

Paul: *"since we've frozen content on the live version, or at least frozen new changes — does that help us? I want
to go about this in the easiest and cleanest way possible."*

**Yes. It helps a lot, and it simplifies rather than changes the answer.** Two things collapse.

## What the freeze actually changes

**① `staging` is not a QA branch. It is `main`-in-waiting.** `origin/main..origin/staging` is not "QA extras" — it
is *the entire unreleased release*. That reframes the whole problem: there is no ongoing risk of a fixture
"crossing into prod," because nothing crosses. There is exactly **one** crossing event, ever: the migration.

**② So the fixture register collapses to a migration checklist.** Paul's instinct in the ask is right. A continuous
guard on `main` would be over-engineering against a boundary the freeze already holds shut. Drop it.

**Revision to my earlier answer:** I put the register in `tools/` because `instance/` is SURFACE class in the
ledger. Under the freeze that objection dissolves — everything on `staging` is SURFACE-divergent anyway and every
SURFACE commit already owes a stage-note. So **put the declaration next to the value**, inline:

```
"vault": { "rooms": ["qa-contacts"],
           "_qaFixture": "C6 5c retires this — Paul authors the real room" }
```

No second file, no drift between register and value, and the check is a grep for `_qaFixture`.

## The finding that matters — measured just now

I checked whether the migration can be a **fast-forward** (`git push origin staging:main`), and the answer is
*almost*:

```
main ancestor of staging?  NO
origin/main..origin/staging   23 commits   (the release)
origin/staging..origin/main    1 commit    ← the only blocker
  88051ad  digest: rebuild on deploy 2026-09-04T09:24Z [skip ci]
```

**The cherry-pick path is not the problem.** Both prod cherry-picks (`3c71b60`, `0d166b1`) are ancestors of
*both* branches — that discipline is working. The single fast-forward blocker is a **CI bot commit**:
`deploy-worker.yml` commits `worker/digest.json` back to `main` after every prod Worker deploy
(`contents: write`, `[skip ci]`). It will recur on every prod Worker fix.

And `worker/digest.json` is one of the two files that already has a merge driver — `fernwood-digest` → **REGENERATE**.
So the blocker is both trivial and already solved; it just has to be *cleared*, not *resolved at migration*.

## The one path

**Make the migration a fast-forward, and keep it one back-merge away from being available at all times.**

Why fast-forward rather than a curated merge, in one sentence: **a merge produces a new commit whose `viewer.html`
was never served anywhere, at the single riskiest moment in the project.** A fast-forward ships the exact sha that
was already deployed to QA, loaded at 414 × A+, and passed `check-live`. The bytes Mom gets are the bytes that were
tested. That is the whole argument, and it outranks every other consideration here.

The migration then reads as five lines:

1. **On `staging`:** remove every `_qaFixture` (set the real values), `python3 tools/build-viewer.py`, commit.
2. **QA deploys it.** Verify there: `check-live.py --base QA --ref origin/staging` 5/5 · `herConditions()` clean at
   414 × 848 × A+ · `qa-walk.py` 0. ⭐ **The fixture removal is itself tested, on QA, before it is prod.**
3. **Gates:** `grep -c _qaFixture instance/*.json` = 0 · `build-viewer.py --check` green ·
   `git rev-list --count origin/staging..origin/main` = 0.
4. **Ship:** `git push origin staging:main`. One command, no merge commit, no resolution.
5. **Prove:** `check-live.py --wait 180` · `check-mom-ack.py` · `/health` on `fernwood`.

## The 2 changes (down from 3)

**1. `qa-divergence.py --check` also asserts the fast-forward is still available.** One git call —
`git rev-list --count origin/staging..origin/main` must be 0 — and a remedy line naming the back-merge. **This is
the valuable half of the whole re-answer:** it turns *"will the migration be clean?"* from something Paul finds out
on migration day into a signal that is green (or not) every session. Today it reads 1, and the remedy is one
command: `git merge origin/main` on staging.

**2. Back-merge `main` into `staging` as the last step of the prod cherry-pick procedure** — after the deploy, so
the bot's digest commit is included. Record it as a stage-note in the C4 plan beside the existing, working check
(`git diff origin/main <prod-branch> -- viewer.html instance/ engine/` must be EMPTY). Keep that one; it is what
kept the cherry-picks clean and it is why this is a one-commit problem instead of a real merge.

*(The `_qaFixture` marker is a convention, not a change — it costs one key in a file you are already editing.)*

## Falsifier

**`git rev-list --count origin/staging..origin/main` is non-zero for anything other than the digest bot, or stays
non-zero across sessions.** That would mean `main` is growing real work `staging` does not have, the fast-forward
premise is false, and a curated merge has to be designed properly rather than avoided. One stale bot commit is a
back-merge; a pattern is a different architecture.

Secondary: a `_qaFixture`-marked value is present in `origin/main` after the migration.

## What NOT to do

1. **Do not cherry-pick to `main` without back-merging to `staging`.** That single omission is the only thing that
   can destroy the fast-forward.
2. **Do not resolve a `viewer.html` merge conflict at the migration.** If you are resolving, you are about to ship
   bytes that were never served. Back out and get to a fast-forward instead.
3. **Do not build a continuous fixture register while the freeze holds.** The freeze is the isolation; a second
   mechanism over it is over-engineering. Build it only if the freeze lifts before the fixtures retire.
4. **Do not let a prod fix carry a SURFACE file.** `worker/` only. The existing EMPTY-diff check stays mandatory.
5. **Do not combine fixture removal with the migration push.** Remove on `staging`, verify on QA, *then* ship —
   otherwise the first time the prod values are exercised is on her page.

## Unchanged by the freeze

- **The theme colour needs nothing.** Its own `_note` marks it a real prod value; it just rides the fast-forward.
- **The condo is untouched** — a different estate, its own instance file, built via `--instance/--out`, sited in
  `fernwood-private`. Orthogonal to all of this.
- **Both build checks stay honest.** `build-viewer.py --check` is live and meaningful on `staging`; on frozen `main`
  it is green over a static artifact — harmless, and no branch conditional is needed anywhere.

## One watch-item

Under the freeze, **every** SURFACE commit on `staging` is divergence and owes a stage-note, so the ledger grows
monotonically for as long as the freeze lasts (23 today). That is the right cost for Paul's trackability ask — but
this repo has a recorded failure mode: *a control that is red on every signal is one nobody reads.* If unrecorded
SURFACE commits ever accumulate past ~10, the discipline has failed rather than the tool, and the honest fix is to
record them in a batch, not to loosen the gate.
