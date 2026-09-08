# practice-steward trail — environments, estates and roles · 2026-09-08

Design output: `.plans/2026-09-08-environments-and-roles-DESIGN.md`. This file is the **method trail** —
what I read, what I measured, what I got wrong, what I declined, and what should be checked next time.
⛔ Nothing here is a finding about the product; findings live in the design file with their evidence.

- HEAD at start and end: **`13b98a4`**. ⚠️ The session snapshot handed me `a28e4fe` as tip; HEAD had moved
  to `13b98a4` by my first read. Verified `a28e4fe` is an **ancestor** of HEAD — same lineage, the main
  session's own commits, not a concurrent writer. Nothing committed by me.
- Working tree: two untracked plan files from today's journey work, plus my two outputs. **No tracked file
  was edited. No config, no `wrangler.toml`, no deploy, no mint, no `--confirm`.**
- Privacy sweep run on the design file before finishing: **zero** real addresses, zero personal data. The
  repo is public and two of the measured records are Paul's own; the design file refers to *"his real
  address"* and never quotes it.

---

## 1 · What I read, in order

`CLAUDE.md` (preloaded) → `worker/wrangler.toml` (every comment block) → `tools/pages-deploy.py` (all 407
lines) → `tools/release-gate.py` → `cycle/release/CYCLE-MAP.md` → `VOCABULARY.md` §1–§7 →
`.plans/2026-09-07-qa-access-DECISION.md` → `.plans/2026-09-07-review-gate-to-qa-DESIGN.md` (my own prior
seat) → `.plans/2026-09-08-setup-journey-PLAN.md` → `tools/grant-mint.py` → `worker/worker.js` (scope,
grant, canon) → `tools/reset-production-estate.py` → `tools/check-release-docs.py` →
`.github/workflows/deploy-worker-qa.yml` → `OBJECTIVES.md` → `BACKLOG.md` §sunset → `archive-frozen-estate.py`.

**The CYCLE-MAP-first order in my foundation held up.** The release map named the rung structure before
`wrangler.toml` could confuse me about it, and the map's own `⚠️ This table read ⬜ to build until
2026-09-07` note told me which of its rows to distrust.

---

## 2 · Instruments run (all read-only)

| tool | why | what it gave |
|---|---|---|
| `tools/access-map.py` | who holds what, derived from the register | ⭐ **the single richest read of the session** — six person rows that are Paul, three of them minted in QA; four owner grants at `est-e6696a`; zero grants at `est-9a74df`; eight rows with no consent |
| `tools/read-onboarding.py --env qa` | provenance split | `4 real · 463 synthetic · 44 unknown`; his four read `real unlinked` |
| `tools/check-storage-keys.py` | ⭐ **the second method for the 175-key claim** | 19 rostered / 18 in use — which is what proved 175 is a KV count, not a localStorage count |
| `tools/build-viewer.py --instance instance/qa.json --out /tmp/…` | size the neutral build without writing | 1,203,913 bytes vs tracked 2,216,135 |
| live HTTP reads of both `.pages.dev` origins | what is actually served now | QA is serving the neutral build via `pages-deploy.py`; four pruned paths answer `{"tombstone":true}` |
| a `python3` read of the frozen archive | verify 171/175 independently | `keyCount: 175`, 4 prefixed, 171 unprefixed, `unreadable: []`, 6,033,721 bytes |
| `git rev-list --left-right`, `git config branch.main.merge` | branch model | local `main` → `origin/staging`; `origin/main` ↔ `origin/staging` = 10 / 542 |

**Blocked, and correctly:** `reset-production-estate.py --estate est-qa0001` (dry run) was denied by the
permission classifier. ⭐ **I graded the finding `measured` by source read and said so in the design file
rather than downgrading it silently** — an execution-verified claim and a code-verified claim are not the
same claim, and this corpus's whole doctrine is that they must not print the same.

---

## 3 · ⭐ The methodology rule that actually earned its keep today

> **Never report a clean absence from one grep. Verify by a second method.**

It fired **three** times, and two of the three changed a conclusion:

1. **"nothing reads `cleared_sha`."** My own 09-07 design said so. `measured` today: `pages-deploy.py`
   now reads it and refuses on absence. **The prior finding was closed and I would have re-reported it.**
   Caught by reading the file instead of trusting my own artifact.
2. **"G3 can never fire."** `wrangler.toml:66-72` says so in its own text. `measured`: `env_agrees()`
   reads a **KV `env-canary`**, so the destination *is* confirmed by namespace. ⭐ **And the repair landed
   in the SAME COMMIT as the comment** — `cb29e08`, *"that killed G3, so G3b asks the destination who it
   is"* — so the comment describing an open defect and the fix for it were written together, and the
   comment has read as live ever since. Reporting it would have been reporting a stale self-indictment as
   a current defect.
3. **"175 localStorage keys."** Two independent methods (the archive dump and `check-storage-keys.py`)
   said KV, not localStorage, by an order of magnitude.

⚠️ **Lesson for this seat, recorded because it is about my own failure mode:** *a self-indicting comment is
evidence that a defect **existed**, never that it **persists**.* This corpus is unusually rich in files
that record their own defects, which makes them unusually easy to quote as current. **Two of the three
misses above were mine, from my own prior output.**

---

## 4 · Where I nearly went out of lane, and what stopped me

| moment | the pull | what kept it in lane |
|---|---|---|
| HOLE 3 (the two QA build paths) | it is the most alarming thing in the file and I wanted to say *fix this first* | ⭐ **the zero-value test.** *"A push to staging replaces a 1,203,913-byte build with a 2,216,135-byte one"* stays true with every affected item's value set to zero. *"Fix this before zones"* does not. I stated the criticality with its bytes and **explicitly declined the ordering** |
| the sunset order | same shape — it is genuinely dangerous to get wrong | the in-lane statement is *the steps are ordered by an irreversible dependency and the lockout must come third*. That is a claim about a write path. **Whether the sunset outranks anything is Paul's** |
| B5 / B8 (whose home is `est-e6696a`; is `paul` a home or a rig) | I could see which reading is more likely right | ⛔ it is a call about his family's data and his own intent. **Reported the contradiction with both files and both timestamps; picked neither.** This is the row the boundary exists for |
| Q1 (same estate id at two rungs?) | there is a defensible engineering answer | it is a claim about **identity** — whether his condo in QA *is* his condo. Declined |
| Q6 (repo private?) | — | it is about how private Mom's eight months need to be. Costed both, picked neither |

⭐ **The mid-task correction made this easier, not harder.** Paul's `dev is a playground` definition
**retired a contradiction I had already written up as open** (the `est-lab0001` vs `est-3c9f1a` fork) — so
the honest move was to shrink my own finding, not to keep it. Recorded in §2.2 of the design file as a
narrowing of Q1 rather than a deletion of it, because it still binds for the qa/production pair.

---

## 5 · What this seat should carry forward

1. ⭐ **The axis-collapse shape is new to my catalogue and I think it is general.** *One identifier
   pinning two independent axes, so a cell in the product of them cannot be named.* It is not the corpus's
   famous shape (*X and not-X produce the same observation*) — it is **the model cannot say the thing, so
   nobody notices it is missing.** Candidate for the principle library **after** it appears a second time
   somewhere else. ⛔ Not promoted; one instance is an anecdote.
2. ⚠️ **`VOCABULARY.md` has no environment section**, `measured` again today (`grep -c '\bdev\b'` → 0),
   and it was already flagged in the 09-07 flex-point audit's R2·c. **Second sighting, unfixed.** Every
   rename in §5 re-forks without it.
3. ⭐ **`.plans/` is tracked and this repo is public.** Two of today's measured records were Paul's own
   real data. **A seat reading live stores must run a privacy sweep on its own output before finishing**,
   and I did. Worth stating in the foundation rather than rediscovering.
4. ⚠️ **My 09-07 design's §4 (four renames) is now partly superseded by its own author.** It proposed
   `home → prod` as *"bookkeeping"*; today's costing shows it is **bookkeeping only if `name` is pinned
   first**, and that the Pages project cannot be renamed in place at all. ⛔ **A prior artifact of mine
   was wrong in the cheap direction and I found it by costing rather than by re-reading.** Costing is the
   check; re-reading is not.
5. **Open, unresolved, and named in the design file:** whether the `walked-at` clause (D3) has been owed
   long enough to be a pattern. It was named 09-07, is still `grep`-zero, and is the second time this loop
   has had a gate whose clause existed in prose and not in code.

---

## 6 · Falsifier for THIS trail

**If, at the next audit, §3's three verify-by-second-method saves turn out to have been the whole value of
the session** — i.e. the design's model was not used and only its corrections were — then this seat should
be doing audits and not designs on this subject, and the model in §1 of the design file was a framework
import wearing local clothes. **The tell:** Paul rules Q1–Q7 and the tier language does not appear in any
later artifact.

---

## 7 · AMENDMENT — Q1 ruled, same session

`[paul-ruled 2026-09-08]` **`(place, rung)` → one estate id.** Folded into the design file as §10; §0·1,
§1.4, §2.2, §6·B1, §7·S9 and §8·Q1 amended in place with pointers rather than rewritten.

**Two method notes worth keeping:**

1. ⭐ **I checked the ruling against the toml before writing a migration into the sequence.** Six
   deployments, six distinct ids, zero collisions — **the ruling ratifies the reverted state and asks
   nothing to move.** Had I assumed it implied a migration, the sequence would have grown a step that
   already exists. *Verify the world before writing the step.*
2. ⭐⭐ **The best find of the amendment was NOT the ruling — it was what the superseded line had been
   citing.** `wrangler.toml:64-70` justified sharing an estate id across environments by citing
   `estate.json:4` — *"an id is a COORDINATE, not a label."* Read directly, `estate.json:4` says only
   that **renaming a place does not rename its id.** It says nothing about environments. ⛔ **The
   doctrine that had to be superseded was the CITATION, not the source** — and the source is still true
   and must not be "corrected."
   > **The shape, and it is one I want to carry: a rule cited beyond what it says becomes doctrine at the
   > citation site, and the next reader quotes the citation rather than the rule.** This is the
   > seven-vocabulary-forks failure with one extra hop. ⛔ **Not promoted** — one instance, and promotion
   > is Paul's gate.

**⚠️ And the honest self-accounting: three of the five things newly wrong were mine** (§10.7 W1–W3),
including one — *"one home at two rungs"* — where **my own framing had imported the confusion the ruling
removes.** I was using `home` for `place` in the same document that argued the two axes had been
collapsed into one word. ⭐ **The correction I asked the corpus to make was one I had not made myself.**

---

## 8 · SECOND COMMISSION — the sequencing pass (`.plans/2026-09-08-sequence-SPINE.md`)

Read at HEAD `12a6a9d`. ⚠️ **HEAD moved twice more during the session** (`a28e4fe → 13b98a4 → 12a6a9d`),
all in this lineage. Nothing was written against a moving claim without re-reading it — two of the
findings I was handed had **already been fixed by the main session** while I was working, and I caught
both by grep rather than by being told.

### What the sequencing pass taught me about my own outputs

1. ⭐⭐ **The single best finding was one line inside a tool's docstring, not anything in a plan.**
   `grant-mint.py:205-215` says place facts ride onto a grant in **exactly one code path — signing in —
   "and there is no sign-in door… so a minted grant could not be hydrated by ANY route a person could
   reach."** ⭐ **`hydrate` exists because B2 does not.** That turned a flat list of ten unplaced findings
   into an ordered one: the `--rotate` warning is a **stopgap whose retirement condition is B2**, and
   naming that retirement now is what stops scaffolding becoming furniture.
   > **Method note: the dependency was recorded, in prose, in the tool that embodies it — and no plan
   > carried it.** Three plans were reconciled and none of them knew this. *A tool's own docstring is a
   > first-class ordering source in this corpus, and I had been treating tools as things to run.*

2. ⭐ **The sharpest lane finding is not about files.** *Parallel build serialises at the gate* — gate ①
   is per-sha and evidence expires when the build moves, so two lanes committing concurrently **spend
   each other's walk evidence**. Nothing about that is visible from a file-touch analysis, which is the
   analysis I would have done if I had ordered by blast radius alone.

3. ⚠️ **I placed one step by the wrong axis and said so in the file (§6).** Paul's customer-journey beat
   is described as an **end-of-lap** act; I placed it early because it *feeds* the synthetics. **That is
   reading a cadence question as a dependency question**, and it is exactly the class of call the
   boundary says is his. ⛔ **Flagged rather than quietly resolved.**

4. ⭐ **Deferrals turned out to be a third of the value.** §5 has eleven `do not` rows, and **three of
   them exist only because something was fixed or settled during the session** (the two QA build paths,
   the stale-origin non-gap, Q3). ⛔ **Without those rows the next reader re-raises all three**, which is
   this corpus's measured leak: *the alternative considered and rejected never gets written down.*

### ⚠️ Standing caution for this seat

**Two of the ten findings I was handed were already fixed.** I verified both. But the general risk is
that a commission's framing arrives as fact — and today one framing was measurably wrong (KV vs
localStorage, §7·2 above) and two were stale. ⭐ **Verify the brief, not only the corpus.** The brief is
an artifact like any other and it can drift between being written and being read.
