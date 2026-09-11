# Row T — WHAT A BUILD WINDOW CARRIES THAT NO DOCUMENT SAYS

<!-- Written 2026-09-11 by the row-T build window, at coordination's question "is there anything you
     are carrying that is not written down". Everything below was learned by BUILDING and would be
     rediscovered at full cost by a fresh window. It is not a summary of the plan; the plan is fine.
     ⛔ This file exists because a seam's real cost is invisible from outside the window paying it. -->

## 1 · THE PER-STEP VERIFICATION BATTERY — run after every step, before every commit

Nothing names this anywhere. It is the invariant coordination tracks ("five frozen verdicts unchanged,
corpus frozen at all N commits") and no document says how to produce it.

```bash
python3 tools/release-gate.py --selftest            # the gate
python3 tools/walk-integrity.py --selftest          # the counter
python3 tools/release-state.py --selftest           # the published state (added at T5; had none)
python3 tools/journey-walk.py --selftest            # the harness  (73 clauses)
python3 tools/walk-notes.py --selftest              # the consolidation reader (added at T8)
python3 tools/verify-corpus-manifest.py             # the frozen past is still frozen
for sha in a3beb8d d7d6c9f 12912b9 87c7aae bfa3f23; do   # ⛔ NO VERDICT MAY MOVE
  python3 tools/release-gate.py --sha $sha >/dev/null 2>&1; printf "%s=%s " "$sha" "$?"; done; echo
# expected at every step so far: a3beb8d=1 d7d6c9f=1 12912b9=1 87c7aae=1 bfa3f23=1
```

⚠️ `87c7aae` is **🟡 exit 1**, not ✅ — every CELL passes, content green, UX sweep unfiled, so it is
NOT a bare pass. Two people have flattened that distinction in writing; it is the one the gate draws
most carefully.

## 2 · THE PREDICATE REFLEX — the single most valuable habit in this lap

**Before reporting any number, name the predicate that produced it, and test it by a path its author
did not use.** Measured cost of not doing this, today, in this row alone:

| the predicate | what it claimed | what was true |
|---|---|---|
| `steps[].ok` | 0 failed actions at `87c7aae` | the field DOES NOT EXIST; real answer 12 across 7 runs |
| exact `## Findings` | 3 reports wrote findings | 6 did — the heading varies |
| `- ` bullets only | 0 findings in the corpus | 37 — the corpus uses bold-numbered paragraphs |
| fingerprint alone | 8 distinct observations | 23 — it collapsed across journeys |
| non-exclusive buckets | census 59/4/201/23 | 59/4/199/21 exclusive; the published pair sums to 287 over 283 |
| a truncated grep | "the row names no field path" | it named one, past the cut |

⛔ **Every one failed SILENTLY and in the FLATTERING direction** — under-reporting, which nobody
questions. A confident wrong predicate and a correct one print the same way: a number.

## 3 · WHAT I HAVE LEARNED TO DISTRUST IN THIS CORPUS

- ⛔ **Exact string matching against anything human-authored.** Headings, report bodies, seat prose.
  Three failures inside one step (T8). Use prefix/normalised matching and RECORD the variant seen.
- ⛔ **`grep` output read for an ABSENCE claim.** A truncated window reports absence for anything past
  the cut. Count occurrences (`grep -c`) when the claim is "it is not there". Caught both windows twice.
- ⛔ **A field named in a plan.** `steps[].ok`, `steps[].action`, `--no-deploy` — all cited, none exist.
  Re-derive the schema from the RECORD (`json.load` + key census), never from the document.
- ⚠️ **A count of lines MENTIONING a thing, as a proxy for the thing.** Cost coordination a wrong
  ruling on whether `instrumented` gates anything.
- ⚠️ **Any claim scoped to "the lap 7 battery" stated as "at any build".** That is how J2 came to be
  declared unwalkable while two clean walks of its own procedure sat on disk.

## 4 · MECHANICAL TRAPS — each cost a failed run to find

- **The selftest harnesses DIFFER PER TOOL.** `journey-walk.check(name, ok, why)` requires all three
  args (a 2-arg call raises TypeError). `walk-integrity.check(name, ok, why="")` does not.
  `release-gate` uses inline `ok &= bit` with no helper. Copying a clause between tools fails.
- **`WALKS` · `CELLS_DIR` · `LENSES_FILE` are module globals that selftests swap.** Python allows ONE
  `global` declaration per name per function body — a second one is a SyntaxError ("used prior to
  global declaration"). They are declared once at the top of `release-gate.selftest()`; add new ones
  there, not at the point of use.
- **`release-state.py` writes ONLY with `--write`** — but `.git/hooks/post-commit:9` runs it with
  `--write` after EVERY commit, so a commit that moves gate output ALWAYS leaves `cycle-state.json`
  dirty. That is designed (`[paul-ruled 2026-09-07]`), one-commit-behind by construction, and
  reverting it is futile. Fold it into the next commit.
- **`walk-integrity.report(rows, countable_only=True)` still prints run paths** — redirect stdout in
  a selftest or the output is unreadable.
- **`timeout` is NOT installed** (BSD userland). **`${PIPESTATUS[0]}` is bash-only** and expands to
  empty in zsh — use `${pipestatus[1]}`, 1-indexed. A hook blocks the bash form.
- **`rm` is blocked under `~/Developer`** by `guard-destructive.py`. Use `trash`.

## 5 · OBLIGATIONS THAT OUTLIVE A WINDOW

- ⛔ **CYCLE-MAP beat 8 carries a NOT-YET-ENFORCED marker.** T6 was applied at step 8 when its ruled
  position is 21, so the cell declares ahead of the code (`change-scope.py` and the byte proof do not
  exist until T11/T12). **The marker comes off at T21 and NOT BEFORE** — the acceptance run is the only
  step that can prove every clause rather than assert it. ⭐ **It must be WIRED INTO the `--report`
  generator**, which should refuse to emit clean evidence while the map still declares ahead of the
  code. An obligation nobody is wired to discharge is not an obligation.
- ⛔ **T17 must read `failedActions[]`**, not `steps[].ok`. Its mechanism is unaffected — the
  normalisation already operates on strings, which is what `failedActions[]` holds.
- ⛔ **T9's controls must include the NEGATIVE one**: the pre-T9 record shape (full value present)
  must FAIL the clause. A mutation proving only the new shape passes cannot tell an elider from a
  non-elider. And `#uword`/`#uword2` want parity with `journey-walk.py:1745`'s existing `<password>`
  mask, not mere length-elision — that line already ruled a password's LENGTH is not wanted either.
- ⛔ **Do NOT back-fill the frozen corpus.** It is the past T21 depends on, the manifest hashes it, and
  a rewrite failing `verify-corpus-manifest` is the mechanism working.

## 6 · THE ONE THING THAT IS NOT WRITTEN DOWN AND CANNOT BE

Row T's steps are individually small and the errors are not in the steps — they are in the PREDICATES
the steps are described with. The plan's prose is reliable; its field paths and counts are not. A
window that treats the documents as a specification will ship working code against fields that do not
exist. **Treat the plan as intent and the record as authority, every time.**
