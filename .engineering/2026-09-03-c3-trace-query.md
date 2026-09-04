# C3 · THE TRACE IS A QUERY — the implementation shape

- row: `BACKLOG.md` § 📜 C3 · THE TRACE IS A QUERY, NOT A FILE — and the founding leak is located
- objective: O5
- class: engine
- seat: engineering-partner
- mode: path-evaluation (implementation half) — the method half is `practice-steward`, run in parallel
- date: 2026-09-03
- repo state: read-only; HEAD moved during this pass (C4/C5/C6 migration, second session). Every number
  below was derived at HEAD ≈ `415b1d1`. Nothing in the repo was written except this file.
- status: NOT READY — three of the row's stated measurements do not reproduce, and one of its two
  factual corrections is wrong. See §1.

---

## 0 · WHY THIS DOCUMENT LEADS WITH A RECONCILIATION

The row's design conclusion is **right** and I am recommending we build it. But every figure in the row
is a prior seat's claim, and I was asked to re-derive rather than inherit. Four of them do not survive,
one of them cannot be derived at all, and two of the row's own factual assertions are wrong. None of
that changes the design; all of it changes what the plan file may cite.

The rule this corpus already carries — *a count without its predicate is a defect* — is the reason the
row is not groomable as written: **the row states seven numbers and zero predicates.**

---

## 1 · RE-DERIVED NUMBERS vs THE ROW'S CLAIMS

### 1.1 The corpus size

| | row claims | I derive | predicate |
|---|---|---|---|
| artifacts in the citation graph | **98** | **162** | tracked `.md` + `.json` under `.plans/ .engineering/ .ux-reviews/ .user-research/ .content-reviews/ .ai-advisor/ .decisions/`, at HEAD 2026-09-03 |
| | | 122 | same seven dirs, **`.md` only** |
| | | 167 | seven dirs + `.design-options/` |
| | | 185 | seven dirs + the 23 tracked root canon `.md` files |

**98 is not reproducible under any predicate I could construct.** The corpus grew by ~10 files on
09-03 (the migration burst), so the seat's own day would have read ~152, not 98. Per-directory tracked
counts at HEAD: `.plans` 30 · `.engineering` 42 · `.ux-reviews` 39 · `.user-research` 30 ·
`.content-reviews` 4 · `.ai-advisor` 6 · `.decisions` 12 = **163 files, 162 of them `.md`/`.json`**
(one `.ux-reviews` file is neither).

> **Verdict: `unknown`.** The plan file must not cite 98. It may cite 162 with the predicate above.

### 1.2 The seed — and why in-degree 0 cannot be re-derived

The row seeds the graph at *"the activation research."* The path the readiness proposal uses for that
artifact is `.user-research/2026-09-02-activation-journeys.md`.

```
on disk:            no
in git, all refs:   0 commits (git log --all -- <path>)
ever deleted:       no  (git log --all --diff-filter=D over all seven dirs returns EMPTY —
                         no artifact has ever been removed from those directories)
```

**The seed does not exist and never did.** So `out-degree 5 / in-degree 0 / depth-1 6 / depth-2 10 /
closure 77 of 98` describe a node I cannot locate. `unknown`, all five.

⚠️ And it is not an isolated typo. Scanning all 304 tracked `.md`/`.json` files for artifact-path
citations, **20 distinct cited paths resolve to nothing — 43 citing-file instances.** Six of them are
2026-09-02 seat artifacts that downstream 09-03 plan files cite as though they exist:

| cited path | citing files | in git? |
|---|---|---|
| `.plans/2026-09-02-data-model-design.md` | 8 | never |
| `.ux-reviews/2026-09-02-login-door-and-selector.md` | 5 | never |
| `.content-reviews/2026-09-02-estate-naming-layer.md` | 4 | never |
| `.user-research/2026-09-02-activation-journeys.md` | 3 | never |
| `.user-research/2026-09-02-estate-manager-scoping.md` | 3 | never |
| `.user-research/2026-09-02-condo-feature-research.md` | 3 | never |
| + 14 others (`.private/…`, `.research/…`, `.audit/…`, two `.ux-reviews` json) | 17 | never |

⭐ **This is the strongest possible argument for the row's own design, and it is a number the row did
not have.** The trail is not merely unwritten — it is *asserted as written* in eight places. Any
readiness check that verifies "the cited file exists" (readiness §1.2 field 4) will fail against six
current plan files the moment it is pointed at them.

### 1.3 Artifact → artifact derivability

Row: *"48 of 98 (49%), no new convention."*

Derived over the 162-node corpus, edge = a citing file names a target's repo-relative path, or names
a target's basename uniquely:

```
nodes 162   edges 173
>=1 out-edge   68  (42%)
>=1 in-edge    79  (49%)
>=1 edge either way  106 (65%)
isolated (no edge at all)  56
dangling citations  15 distinct / 27 instances (within this node set)
graph build time, cold, 162 files:  0.07 s
```

**49% reproduces — as in-degree, not out-degree.** Whether that is the same measurement or a
coincidence I cannot tell, because the row states no predicate. Either way the honest headline is the
one the row does not print: **56 of 162 artifacts (35%) have no edge in either direction.** A trace
query over this graph is blind to a third of the corpus, and it must say so on every run.

### 1.4 Depth, and what actually bounds it

I cannot run the row's seed. Substituting the nearest live analogue,
`.plans/2026-09-03-c6-door-for-paul-PLAN.md`:

| | seven seat dirs (P1) | + root canon (P2) |
|---|---|---|
| out-degree | 4 | 7 |
| in-degree | 2 | 3 |
| depth 1 | +4 | +7 |
| depth 2 | +10 (=14) | **+58 (=65)** |
| depth 3 | +2 (=16) | +39 (=104) |
| forward closure | 23 of 162 (14%) | **123 of 185 (66%)** |

⭐⭐ **The depth bound is NOT what keeps the trace small. The hub rule is.** `CLAUDE.md` is cited 91
times and `BACKLOG.md` 42 times across the corpus; once either is traversable *as a source*, depth 2
returns the library. Three different seeds all converge on the same 123 nodes at depth 3 under P2.

So the row's *"the depth bound IS the design"* is half right and, as stated, would get built wrong.
The correct statement, measured:

> **Root canon (`BACKLOG.md`, `CLAUDE.md`, `PRODUCT-ENGINE.md`, `RELEASE_NOTES.md`, …) may be an edge
> TARGET but never a traversal SOURCE.** With that rule, depth 2 costs +10 and is readable. Without
> it, depth 2 costs +58 and is useless. *That* is what breaks if someone raises the bound.

### 1.5 Commit → artifact derivability

Row: *"5 of 100 — the only place a convention is owed."*

| predicate | all history (1,718 commits) | last 100 at HEAD | 100 ending at `7cf1f1d` (the seat's own commit) |
|---|---|---|---|
| body contains a `.dir/file.md\|json` path | **60 (3.5%)** | **0 (0.0%)** | 3 (3.0%) |
| ↑ or a bare `YYYY-MM-DD-slug.md` filename | 61 (3.6%) | 0 | 3 |
| body carries a `BACKLOG:` / `Trail:` / `Closes:` / `Verified:` trailer | **90 (5.2%)** | 0 | 3 |

**The ~5% figure reproduces — but for the trailer *shape*, not for commit→artifact citation.** The
artifact-path measure is 3.5% lifetime and **0 of the last 100**, which is the fact that matters:
adoption went to zero in exactly the window where artifacts are being produced fastest. Those 100
commits do have bodies (2,139 non-blank body lines); the citations simply are not in them.

### 1.6 The two factual corrections the row owes

**(a) `dbdff0b` is unreachable.**

```
git merge-base --is-ancestor dbdff0b HEAD   → NO
git rev-list --all | grep dbdff0b…          → 0
git for-each-ref --contains dbdff0b         → (empty)
git reflog --all | grep dbdff0b             → 3        ← the only thing keeping it alive
```

The reachable commit carrying identical text is **`9077df5`** — same author date
(2026-08-02 22:02:03 -0400), same subject, different parent (`a7f1dc1` vs `6b02f22`), six-file tree
delta. `dbdff0b` is a pre-rewrite orphan. **`git show dbdff0b` works on Paul's laptop and fails on
every clone, and will fail here too after any `git gc --prune`.** A citation nobody else can follow is
precisely the defect C3 exists to fix, so the row citing one is not a nit.

> The row should cite **`9077df5`**. I have not edited it (hard limit) — this is for the main session.

**(b) `~/Desktop/fernwood-button-options` still exists.** The row says it does not. Measured:

```
~/Desktop/fernwood-button-options/
  labeled-7-option-C-44px.png   147 KB  2026-08-02
  labeled-8-option-C-37px.png   148 KB  2026-08-02
  archive/                      (6 entries)
```

The *substance* survives — an out-of-repo Desktop path is untracked, undated by git, and dies on any
machine move — but the measurement is wrong, and it is the kind of wrong that reads as thorough. It
also sharpens the design: a query must classify an out-of-repo pointer as **`unverifiable`**, not
`missing`.

**(c) The leak itself: CONFIRMED, but the seat's grep could never have found it.**

The commit body says **`×-corner`** — U+00D7 MULTIPLICATION SIGN. The row quotes it as ASCII
`x-corner`. Measured:

```
git grep -i 'x-corner'  over tracked files  → 3 hits, all inside BACKLOG.md's own C3 row
git grep -i '×-corner'  over tracked files  → 0
git log --grep='x-corner'                   → 0 commits      ← the ASCII spelling MISSES the commit
git log --grep='×-corner'                   → 9077df5
```

And the artifact that should hold the reasoning,
`.ux-reviews/2026-08-02-button-system-weather-collapse-disclosure.json`: `corner` **0**, `×` **0**
(`dismiss` 5, `defer` 9 — it discusses the control and never the alternative).

> **The leak is real and independently confirmed. The row's own search method is latently broken**, and
> that is the single most important input to the implementation: a query over this corpus that greps
> raw bytes will silently return zero. **Unicode folding is not a nicety here; it is the design.**

### 1.7 The trail-file question (asked by the launching session)

**Confirmed: the 2026-09-02 `practice-steward` findings have no trail file.**

- `7cf1f1d` ("The trace is a QUERY…") changed **`VOCABULARY.md` only, +23 lines.**
- `grep -rl 'in-degree|98 artifacts|77 of 98|out-degree'` across all eight artifact dirs → **nothing.**
- `git log --all --diff-filter=D` over those dirs → **empty**, so it was never written-then-removed.
- The `.plans/` files dated 09-02 are `rationalization-PROPOSAL.md` and `vocabulary-PROPOSAL.md` —
  different subjects.

The findings exist in exactly two places: **prose inside `BACKLOG.md` § C3, and the body of `7cf1f1d`.**

⭐ Which is the same failure the findings are about. The seat that located a leak whose definition is
*"reasoning that lives only in a commit body"* left its own reasoning only in a commit body. That is
not irony to enjoy; it is evidence that **the record leg cannot be a human habit**, which is exactly
what §3 concludes.

**Consequence for grooming:** readiness field 4 (`seats:` → a citation to its trail file) **cannot be
satisfied for C3 today**, unless the row's own prose is accepted as the trail or this file is.

---

## 2 · THE QUERY — specification

### 2.1 Path and name

**`tools/trace.py`.** Not `check-trace.py`: `check-*` in this repo is the flag family — silent at zero,
exit 1 on a flag, wired into the session-start block. A query is the opposite shape (it prints on
demand, exit 0 with output) and naming it `check-` is how it would eventually get wired into a block
and become owable. `read-*` is taken by the mom-feedback readers. `trace.py` is a bare verb and reads
correctly at the call site: `python3 tools/trace.py "x-corner"`.

### 2.2 One positional argument, four resolutions

| you type | it resolves as |
|---|---|
| `.plans/2026-09-03-c6-door-for-paul-PLAN.md` | an artifact node — graph legs + commit legs |
| `c6-door-for-paul` | unique-basename → the same node |
| `viewer.html --code card-later-link` | a repo file + a code identifier → pickaxe leg |
| `"x-corner"` (anything unresolvable as a path) | a topic → the normalized prose leg |

### 2.3 Four legs, each with its measured behaviour

**Leg A — artifact → artifact (the citation graph).** Regex, exactly:

```python
ARTIFACT = r'(?<![\w/.-])((?:\.[a-z][a-z-]*/)[A-Za-z0-9][A-Za-z0-9._/-]*\.(?:md|json))'
ROOT     = r'(?<![\w/.-])(' + '|'.join(map(re.escape, ROOT_CANON)) + r')(?![\w-])'
```

Resolution order: exact tracked path → unique basename → **DANGLING**.

- *False positives, measured:* none from `ARTIFACT` on this corpus — the required dot-directory prefix
  plus `.md|.json` suffix is specific, and the lookbehind survives markdown backticks, parentheses and
  list bullets. `ROOT` **does** false-positive: `"the BACKLOG.md head says"` becomes an edge that
  carries no citation intent. This is the second reason for the hub rule in §1.4 — hubs as
  traversal sources import their false positives into every trace.
- *False negatives, measured partly:* a target named in prose without its path
  (*"the 08-31 sweep"*) is missed. In commit bodies this class adds only +1 over 1,718 commits.
  In artifacts I did **not** separately quantify it; the honest bound is the 56 isolated nodes —
  some are genuinely uncited, some are prose-cited. **`unknown`, ≤ 56.**
- Cost: **0.07 s cold** over 162 files. No index.

**Leg B — commit → artifact, free.** `git log --follow -- <artifact>`. Requires **no convention**:
every commit that touched the file is an edge. Measured: **100 of the last 100 commits touch a file in
an artifact directory.** This is the leg the row does not mention and it is the largest single source
of commit→artifact edges available today, at 100% coverage for its class. Cost <0.05 s.

**Leg C — commit → artifact, by citation.** Body contains an artifact path (3.5% lifetime, 0% recent)
or a `Trail:` trailer (§3). Same resolver as leg A, same dangling class. Cost: folded into leg D's
single pass.

**Leg D — the prose leg. This is the leak-catcher and it is not optional.** One pass over
`git log --format='%H%x1f%ad%x1f%s%x1f%B%x1e'`, each body normalized before matching:

```python
def norm(s):
    s = s.replace('×','x').replace('✕','x').replace('✖','x')
    s = s.replace('—',' ').replace('–',' ').replace('·',' ')
    return unicodedata.normalize('NFKD', s).casefold()
```

Measured: **1,718 commit bodies scanned in 0.06 s**; query `x-corner` returns `9077df5` and `7cf1f1d`.
The same query without folding returns nothing. Hyphen/space tolerance matters too — the corpus writes
`×-corner` but a reader will type `x corner`.

**Optional leg E — `--code <identifier>`.** `git log -S<id> -- <file>`. Measured: `-S'card-later-link'`
over `viewer.html` (2 MB, 1,718 commits) = **1.1 s**, returns 4 commits including `9077df5`. Slowest
leg by 20×, therefore opt-in.

### 2.4 Output shape

```
TRACE · x-corner                                    (resolved: topic)
graph: 162 nodes · 173 edges · 56 isolated · 20 dangling · hubs terminal

PROSE HITS · commit bodies, normalized (2)
  9077df5  2026-08-02  v2 button system — one shape, one green, stacked …
     "Paul's ×-corner hypothesis was researched and declined: glyph collision with
      the × answer, NN/g icon-ambiguity findings for 65+, off the reading path."
     touched: CLAUDE.md · RELEASE_NOTES.md · viewer.html
     trail:   (none)                                  ← the leak, named
  7cf1f1d  2026-09-02  The trace is a QUERY, not a file …

CITES (depth 1) · none — topic query has no artifact node
CITED BY (depth 1) · none

⚠ 0 artifacts in the corpus contain this string.
```

For an artifact subject, four blocks: `CITES (depth 1)` · `CITED BY (depth 1)` · `COMMITS THAT TOUCHED
IT` · `PROSE HITS`. Every run prints the **graph line** at the top. That line is not decoration: a
trace that prints three clean rows over a corpus with 56 isolated nodes and 20 dangling citations is a
number without its predicate, and this corpus has already been burned by exactly that (C2's own
correction).

### 2.5 Exit codes

| code | meaning |
|---|---|
| **0** | the subject resolved and the query ran — including "resolved, zero results" |
| **1** | the **subject** did not resolve (typo, or a path that dangles) |
| **2** | usage error |

⛔ **Dangling *targets* inside the result do NOT change the exit code.** They print as `⚠`. `trace.py`
is a query; a query that returns nonzero on the state of the corpus is a check wearing a query's name,
and a check is a thing that can be owed. If dangling-citation enforcement is wanted, it is a separate
`check-citations.py` — see open question 3, and note I am recommending *against* building it yet.

Exit 1 on an unresolved subject is the one place strictness is right: a mistyped subject that exits 0
with no output is an instrument reading clean while blind — the failure mode this corpus names
*match the payload, not the container*.

### 2.6 Index or cache: **no**

Cold, measured, on the live repo:

| leg | cost |
|---|---|
| graph build, 162 files | 0.07 s |
| all 1,718 commit bodies, normalized | 0.06 s |
| `git log -- <path>` | <0.05 s |
| **default run total** | **≈ 0.15 s** |
| `--code` pickaxe over `viewer.html` | 1.1 s (opt-in) |

An index would be a second artifact that can be stale, would need a freshness check, and the freshness
check is a thing that can be owed. At 0.15 s cold there is no case for one. Revisit only if the corpus
passes ~2,000 artifacts, which at the current rate is years away.

### 2.7 Why depth 1 — stated honestly

Depth 1 is a **reading budget**, not a correctness property. Measured at the analogue seed, full
forward closure with hubs terminal is only 23 of 162 — depth barely binds. Depth 1 gives ≤ ~7 rows;
depth 2 gives ~14 and is still readable. **The bound that must not move is the hub rule** (§1.4): with
root canon traversable, depth 2 jumps to 65 and depth 3 to 104 of 185. So the tool should expose
`--depth N` and *refuse* to traverse a hub as a source at any depth, rather than pretending the depth
number is the safety.

---

## 3 · THE COMMIT → ARTIFACT CONVENTION — the one thing owed

### 3.1 The existing convention, stated exactly

Commit bodies in this repo already carry **`Key: value` trailer lines** — a capitalized token at
column 0, `: `, then a value. Measured across all 1,718 commits:

| key | uses |
|---|---|
| `Co-Authored-By:` | 1,014 |
| `Claude-Session:` | 861 |
| `BACKLOG:` | 34 |
| `Paul:` · `Closes:` | 30 · 30 |
| `Bolores:` | 25 |
| `Verified:` | 13 |
| **`Trail:`** | **3** |

The four content-bearing keys (`BACKLOG` / `Trail` / `Closes` / `Verified`) appear on **90 of 1,718
commits = 5.2%** — that is the "~5%" the row names, and the same trailer regex reads all of them.

⚠️ **But only `Trail:` points at an artifact file, and only once**, `eac5648` (2026-08-31):
`Trail: .ux-reviews/2026-08-31-production-full-sweep.md.` The other two `Trail:` uses are prose;
`BACKLOG:` points at rows, not files. So **5.2% is trailer-shape adoption, not commit→artifact
adoption**, and the row's "5 of 100" conflates them. True commit→artifact adoption: **3.5% lifetime,
0% over the last 100.**

### 3.2 The writer-facing rule — one sentence

> **When a commit's reasoning came from, or produced, a seat artifact it did not touch, add
> `Trail: <repo-relative path>` as a trailer line — one path per line, with the other trailers.**

`Trail:` over a new `Exhibit:` for the reason the row already gives, now measured: it inherits three
existing uses and, because the parser also reads bare paths anywhere in the body (§3.3), **no history
is orphaned** — the 60 legacy commits are read by the same code.

The qualifier *"it did not touch"* is load-bearing. If the commit touches the artifact, leg B already
has the edge for free at 100% coverage. **The trailer is owed only for the ~3.5% case** — a commit
that reasons about an artifact without editing it. `9077df5` is exactly that case: it touched
`CLAUDE.md`, `RELEASE_NOTES.md`, `viewer.html`, and no seat artifact at all.

### 3.3 The parser

```python
TRAILER = re.compile(r'^Trail:[ \t]*(\S+)\s*$', re.M)      # authoritative form
BARE    = ARTIFACT                                          # §2.3, legacy form, same resolver
```

Both feed the same resolver as leg A, producing the same three classes: **resolved · dangling ·
local-only** (a path under a gitignored root such as `.private/` or `.research/`, or outside the repo
such as `~/Desktop/…` — present-or-not is unknowable from the repo, so it must not be called missing).

### 3.4 Will it stick? **Not as a human rule. Say so.**

The corpus's own measured lesson — hand-appended records reach 5/38 while tool-written reach 100% —
reproduces here, harder:

- `Trail:` has reached **3 of 1,718 commits = 0.17%** across four months of near-daily commits by the
  same author.
- The bare-path form reached **0 of the last 100** — zero **in the window where artifacts were being
  written most heavily.** A convention that collapses precisely when it is most needed is not a
  convention; it is an intention.

Two shapes have actually worked in this repo, and I recommend both over the human rule:

1. ⭐ **Tool-written.** The plan-stage writer already composes commit messages that touch
   `.plans/*-PLAN.md` (19 of roughly the last 40 commits). If it emits `Trail: <plan path>` into the
   message it is already building, adoption for that class is 100% and zero human memory is spent.
   This is the recommendation.
2. **Free-riding on git.** Leg B needs no convention at all and already covers every commit that
   touches an artifact — 100 of the last 100.

⭐⭐ **And the design must not be load-bearing on the convention.** The falsifier below (§4) is passed
by **leg D**, which needs no convention whatsoever. The trailer improves precision on ~3.5% of history;
it does not gate the value. If Paul decides not to adopt it, `trace.py` still answers his ask. That is
the honest framing, and it is the opposite of how the row currently reads.

---

## 4 · THE LEAK AS A TEST CASE — walking `9077df5` (née `dbdff0b`)

**Scenario.** November 2026. Paul or an agent is about to propose *"put a small × in the top-right
corner of each card to dismiss it."* Does the query surface the August research that already declined
it, with its three reasons?

| path | command | measured result | verdict |
|---|---|---|---|
| **A · topic word** | `trace.py "x-corner"` | 2 hits in **0.06 s**; top is `9077df5` with all three reasons quoted in context | ✅ **PASS** — *and only because of the Unicode fold*; the identical query on raw bytes returns **0** |
| **B · topic, vaguer** | `trace.py "dismiss"` (bodies, scoped to commits touching `viewer.html`) | 12 hits, `9077df5` among them | ✅ PASS, readable noise |
| **C · from the code** | `trace.py viewer.html --code card-later-link` | 4 commits in 1.1 s, `9077df5` included | ✅ PASS — needs no vocabulary, only that you are touching the control |
| **D · citation graph** | `trace.py .ux-reviews/2026-08-02-button-system-weather-collapse-disclosure.json` | that artifact contains `corner` **0**, `×` **0**; `9077df5` neither touched nor named it | ⛔ **FAIL at every depth** |
| **E · the sha in the row** | `git show dbdff0b` | works on Paul's laptop, **fails on any clone** (unreachable; reflog-only) | ⛔ FAIL |

### What D means — a finding about the design, not a detail to route around

**The citation graph cannot recover this leak. Only the prose leg can.** The graph legs answer
*"what did this artifact come from"*; the leak is a class the graph is structurally blind to —
*reasoning that never entered an artifact at all*. Since that class is the entire reason C3 exists,
the ordering in the row is inverted: **leg D is the feature; legs A/B/C are the context around it.**
A plan that builds the graph first and treats prose search as a stretch goal will ship something that
does not pass its own falsifier.

### What E means

A citation by sha is only as durable as the sha. `trace.py` should resolve any sha through
`git rev-list --all` before printing it and label an unreachable one **`local-only`** — the same class
as the Desktop folder. And the C3 row's sha should be corrected to `9077df5` (main session's call; I
have not touched `BACKLOG.md`).

### The falsifier, stated so the build can be graded

> **Build `tools/trace.py`. With no arguments beyond the topic, `python3 tools/trace.py "x corner"`
> must print `9077df5` with the three declined reasons, in under a second, on a fresh clone.**
> If it needs the exact `×` glyph, or the sha, or a convention that has not been adopted, it has
> failed and should be deleted rather than tuned.

---

## 5 · WHAT THIS MUST NOT BECOME

The row's strongest line is that the ceremony objection *dissolves* — nobody writes an empty record
because nobody writes a record. That property is not automatic; it has to be defended at three doors.

| door ceremony re-enters by | what structurally blocks it |
|---|---|
| **1 · The query grows a write.** A `--save` / `--record` flag, and suddenly a record is owed after every trace. | **`trace.py` has no write path.** No `open(..., 'w')`, no subprocess that is not `git log / ls-files / show / rev-list`. `--json` for piping is fine; `--save` is the flag to refuse, in the docstring, by name, so a future agent does not add it helpfully. |
| **2 · The trailer becomes a gate.** `check-backlog-ready.py` (or any check) starts failing on a missing `Trail:`, and every commit grows a compliance step. | **No check ever reads the trailer.** State it in the docstring of both files. A missing `Trail:` is a missing improvement, never a flag. |
| **3 · A cadence.** Anything that can print *"trace not run in N days."* | **No state file, no timestamp, no lap counter, nothing under `cycle/`, no row in any `*-status.py`, not in the session-start block.** Test, from the corpus's own ratified rule: *a loop can be owed; a procedure cannot.* The only evidence `trace.py` was not run is that nobody ran it — and that is correct. |

**A fourth, from Paul's standing rules.** *Deterministic things need a non-AI door.* `trace.py` is
already deterministic (no model anywhere in it). The converse also has to hold: if the tool is absent
or broken, the procedure must survive. So `--help` should print the two fallbacks a human can type
without it:

```
git log -i --grep=<word>            # the prose leg, unfolded — will MISS × ✕ · — variants
git log --follow -- <artifact>      # the free commit→artifact leg
```

Naming the fold's absence in the fallback is the point: it tells the reader why the tool exists.

**And where it is read is the parallel seat's call, not mine.** I will say only what the engineering
constrains: *not the session-start block.* That block is where things become owed, and it is the one
placement that would convert this procedure into a loop. Overlap with `practice-steward` — leave the
final siting to the main session.

---

## 6 · COST AND REVERSIBILITY

**Build.** One file, `tools/trace.py`, ~250–350 lines, stdlib + `git` only. Comparable in size and
shape to `check-backlog-drift.py`. One working session including a `--selftest` that drives each leg
against a known answer — and the selftest's first case should be the `x corner` falsifier, so the
build is graded by the thing it exists for.

**Touches.** Adds one file under `tools/`. Reads `.md`/`.json` under seven directories, 23 root canon
files, and `git log`. **Writes nothing, anywhere.** No schema change, no data file, no config, no
workflow, no check, no session-start line.

**Reversible.** Entirely: `trash tools/trace.py`. Nothing depends on it; no check reads it; no artifact
format changes. This is as close to a zero-commitment build as this repo has.

**Not reversible.** Exactly one thing: **`Trail:` lines, once written into commit bodies, are
permanent** — history rewriting is off the table in a repo with a live second session. Mitigation: the
line is inert if the convention is later dropped, and it is one line. At this project's stakes (a
personal portfolio repo, not a regulated audit trail) this is a **nice-to-have** risk, not an important
one, and it does not need a decision before the query ships. Ship the query; decide the trailer after.

**The one real cost, and it is a correctness cost not a build cost.** If `trace.py` prints a clean
trace, a reader may conclude *there is nothing else.* Measured: **56 of 162 artifacts are isolated**
and **20 distinct citations dangle.** That is why the graph line in §2.4 prints on every run and is
not a `--verbose` extra. A trace without its coverage is the same defect as a count without its
predicate, and this corpus has already made that error once this week.

---

## 7 · OPEN QUESTIONS FOR PAUL

1. **The C3 row cites `dbdff0b`, which is unreachable from every ref (`9077df5` is its reachable
   twin) — correct the row, or leave it and let the tool label unreachable shas `local-only`?**
   Options: correct only · resolver only · both. *Recommend both: a citation nobody else can follow is
   the exact defect C3 exists to fix, so fixing the row is the cheapest possible proof the design is
   right.*
2. **Six 2026-09-02 seat artifacts are cited by 09-03 plan files and none has ever existed in git —
   reconstruct them, mark the citing lines as unwritten, or leave them?** *Recommend: neither
   reconstruct nor rewrite now — add a `--dangling` listing to `trace.py` and let the main session rule
   row by row, because reconstructing a review from memory is the fabrication risk this corpus already
   guards against.*
3. **Should a separate `check-citations.py` flag dangling artifact citations at pickup?** Options: now ·
   in 30 days if the count grew · never. *Recommend the middle: 20 dangling is a one-time backlog, not
   a rate, and a check built on an unmeasured rate is a door built without demand.*
4. **The `Trail:` trailer — hand-written rule, tool-written by the plan-stage writer, or dropped
   entirely given it reached 3 of 1,718?** *Recommend tool-written or dropped. Do not ship a
   hand-written rule; this corpus has now measured that shape failing twice, and the falsifier passes
   without it either way.*
5. **Corpus boundary — do `.design-options/` (26 files, the concept stage) and the gitignored
   `.private/` + `.research/` count as artifacts?** *Recommend: include `.design-options/` (readiness §2
   already treats a `/design-options` run as a valid seat trail); exclude the gitignored roots but
   label citations into them `local-only`, never `dangling`.*
6. **Is C3 groomable at all right now, given readiness field 4 requires a citable seat trail and the
   09-02 findings have none?** Options: accept this file as the `engineering-partner` trail and the
   row's own prose as `practice-steward`'s · have the steward seat write its trail retroactively ·
   waive field 4 with a reason. *Recommend the first — the trail that exists is this file plus the
   parallel seat's proposal, and a retroactive 09-02 file would be a record written after the fact,
   which is the thing the whole readiness mechanism's falsifier forbids.*
7. **The FOCUS FREEZE says only migration/engine work is active; C3 is `engine` and objective O5, so it
   is inside the freeze — but is it inside Paul's *intent* for the freeze, which he stated as "just the
   large migration"?** Options: groom now · hold C3 until the freeze lifts · groom to READY and do not
   build. *Recommend the third: grooming costs nothing in flight and the WIP rule (one item between
   concept and QA) is not touched by a row that stops at `ready`.*

---

## 8 · OVERLAP WITH THE PARALLEL SEAT — declared, not resolved

`practice-steward` owns the method half (`.plans/2026-09-03-c3-trace-query-PROPOSAL.md`): what the
procedure is, where it is read, the procedure/trigger/record container split. Three places this file
necessarily touches method — flagged for the main session to reconcile, **not decided here**:

- **§5's placement constraint** (*not the session-start block*) is an engineering constraint with a
  method consequence. If the steward sites it in a skill's OPEN step, that satisfies the constraint.
- **§3.4's recommendation that the trailer be tool-written** is the record leg of the steward's
  three-way split. We appear to agree; the steward's framing governs.
- **§7 question 6** (whether this file can serve as the trail) is a readiness-mechanism question, not
  an engineering one.
