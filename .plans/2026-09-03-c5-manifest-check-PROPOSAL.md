# C5 · THE ENGINE MANIFEST'S CHECKER — designing the control, not the roster

**Mode:** design (audit-grounded) · **Seat:** `practice-steward` · **Date:** 2026-09-03 · **Item:** `BACKLOG.md` § "C5 · RECORD PREP", scoped to `.engineering/2026-09-03-c5-record-prep.md` §4 + §5a
**Nothing here is decided. No canon changed. Ends at Paul's gate.** My seat is the CHECK; the roster's contents are not mine, and nothing below ranks any artifact. Citations are file + section + role, never a line number — C4 § the rename moves this tree; every measurement names its command so it can be re-run.

---

## §0 · FOUR MEASUREMENTS THAT CHANGE THE DESIGN

| # | The plan / seat says | I measured | Consequence |
|---|---|---|---|
| **0a** | C4 plan § 5a: the check is `0 unclassified` | ⭐ **The unclassified set is TWO files, not hundreds.** `momlib.DOMAINS` classifies 11 root JSONs and `check-domains.py`'s `NON_DOMAINS` 15 — **26 of 28**. Only `COMMS-CHANNELS.json` and `arrival-dispositions.json` sit in neither (`git ls-files`, cross-read against both declarations) | **A zero-red day-one gate is reachable** (§2), and the derivation must **read those declarations, never re-type them** (§3) |
| **0b** | §5a: a lint over *"a declared roster of (value, canonical path, allowed locations)"* | 🔴 **That shape cannot see the founding instance.** `git grep -c "October 17" -- tools` → **0 hits in `tools/`** (only `worker/worker.js`, `worker/digest.json`). The fleet probe's threshold block holds `FROST_MONTH, FROST_DAY = 10, 17` — canon's value **re-expressed in another type**, which no roster keyed on the canonical string can match | ⭐ **Key the lint on the CANONICAL PATH with a per-row detector**, not on a value literal (§4). A value-roster ships green over the one leak this item was founded on |
| **0c** | §0d: the coordinate is **12 tracked files** | **40**, unscoped: `git grep -l "34\.5496" \| wc -l`. Both true, different predicates — §0d scoped to `tools/ worker/ *.html`. **8 of the 40 are `images/property-map/*.bounds.json`** (georeference, where the coordinate IS the payload); **8 more are domain JSONs' `_meta`**, carrying the address, `elevation_ft` and a third spelling, `34.5496°N, 84.3674°W` | **Allowed-locations is not a nicety, it is 28 of 40 rows.** A lint without it is red forever from day one — the N8 shape (§2) |
| **0d** | §0e: `PROPERTY_DATA` is *"the one `*_DATA` const with no re-inline path and no alarm"* | ⚠️ **Six are.** Of the 10 consts outside `check-data-inline.py`'s `SOURCES`, six are named nowhere in `tools/`, `worker/` or `.github/`: `CELESTIAL` · `EVENTS` · `PROPERTY` · `REFERENCES` · `SOURCES` · `SUN_HORIZON`. And 🔴 **`REFERENCES_DATA` has drifted too — 5 paths** by the repo's own `deep_diff`, from the same editorial pass as `PROPERTY_DATA`'s 4 (*fairway* → *clearing* / *turf* / *meadow*) | ⭐ **0e is not one const — it is one un-re-inlined rename pass surfacing in two unrostered consts.** The fix is roster coverage (§3), and it sets §2's rollout |

⚠️ **0e · A CITATION IN THE SEAT DOC RESOLVES TO NOTHING.** §4 sequences the manifest *"with C4 step 13"*
and says *"C4 step 15 turns a predicate on."* **The C4 plan has no step 13 or 15** — its § Sequence labels
are `1a`–`5d`; the manifest is **5a**, the repo split **5d**. Reported, not repaired: which step it ships
with is a sequencing call, and that plan is at Paul's gate.

## §1 · WHAT THE MANIFEST DECLARES

**Recommendation: class DERIVED from layout, with a declared exception table — and the derivation reads
the three rosters that already exist rather than restating them.**

Not on tidiness. `PRODUCT-ENGINE.md` § the shared entity-resolution map records *assumed plants* shipping broken in three places in one day because each re-implemented one lookup; its standing rule is **"never a third map."** A hand-typed roster over 694 tracked files is a fourth register of facts `momlib.DOMAINS`, `NON_DOMAINS` and `check-data-inline.SOURCES` already hold — and 0a shows they answer 26 of 28 root JSONs.

| declaration | how | why not the other way |
|---|---|---|
| **class** (`engine` · `config` · `instance` · `mixed` · `private-pointer`) | **derived** from a dir→class table over the 25 tracked top-level directories, plus the three rosters for root JSONs | 694 files; a hand roster is the rot class measured three times here (12→18 keys, 11→13 prefixes, 22-vs-12 consts) |
| **engine → divergence tier** (`FREE` / `DECLARED` / `MUST-NOT-DIVERGE`) | ⛔ **declared**, one row per file | `PRODUCT-ENGINE.md` § the divergence contract's test is *"is there a consumer that degrades"* — a judgment, and its own falsifier says a tier with no nameable consumer belongs in FREE. A derived tier automates that failure |
| **config → canonical SOURCE** | ⛔ **declared as a dotted canon path** (`frostDates.atPropertyElevation.firstFall_50pct`), never as the value | 0b: the value has three spellings in this tree; the path has one. The path is what makes a re-typed copy detectable (§4) |
| **instance** | nothing | per the brief and `.plans/2026-09-02-data-model-design.md` §4 |

⭐ **The ruling that `tools/` and `worker/` stay put is what makes derivation work, not what breaks it.** *"Invert ownership, not the directory"* (`BACKLOG.md` § C4's RULED table) means the table carries two explicit rows — `tools/ → engine`, `worker/ → engine` — more honest than an `engine/`-prefix rule that would silently reclassify them if they ever moved.

⚠️ **`mixed` must be first-class, with a declared shrink target.** Without it `viewer.html` (53% instance, data-model §3) is either unclassified — a gate nobody can clear — or force-fit, reporting green over the product's largest divergence surface. `mixed` **is** the third state this repo keeps re-inventing: *declared absence vs. drift*, the distinction `NON_DOMAINS` exists to make. Reuse it; do not mint a fourth.

**Falsifier:** if the dir→class table needs more than ~30 rows, or if any directory must be split below depth 1 to be classifiable, derivation is not carrying its weight. *Today: 25 top-level dirs, and `images/` — the largest at 232 files — is homogeneous instance at depth 1.*

## §2 · WHAT FAILS, WHAT ONLY COUNTS

**Paul's own rule governs and is not negotiable here:** *a control red on every signal from day one is one nobody reads* (`CLAUDE.md` § the backlog-drift check, on `sectionsAddedSince` deliberately not firing). So every predicate carries its **measured day-one state**.

| # | predicate | day-one, measured | ships as |
|---|---|---|---|
| **P1** | a tracked file whose class is neither derived nor declared | **2 files** (0a), declared in the exception table in the same commit | ⛔ **FAILS** — the coverage proof |
| **P2** | an exception row whose file no longer exists, **or whose reason string is empty** | **0** (the table is new) | ⛔ **FAILS** — dead-waiver rot |
| **P3** | an `engine`-class file differing from the engine source of truth | **not evaluable** — no engine remote until C4 § 5d | 🟡 `skipped: no engine remote declared` — never `pass`, never `0 findings` |
| **P4** | a `config` value re-typed into an `engine`-class file | **≥1 known** (the fleet probe's threshold block), and its detector does not exist yet (0b) | 🔢 **COUNTED**, self-arming |
| **P5** | an `instance` const in `viewer.html` outside `check-data-inline.SOURCES` | **10 consts, 2 drifted** (0d) | 🔢 **COUNTED**, self-arming |

⭐ **An arming condition, not a date.** A date ("graded from 10-01") is a deadline nobody set. The honest condition is **the count reaching zero, with the check arming itself when it does** — it prints `counted: N (arms at 0)` and fails from the run after N hits 0. Same shape as `CLAUDE.md` § the drift rule, where *applying* the work resets the clock as a side effect.

⚠️ **P5 cannot be armed by adding the 10 consts to the roster today:** two are drifted, and clearing drift is not the checker's call — `CLAUDE.md` § the drift rule says *"don't auto-fix… surface it to Paul… only then `--fix`."* Viewer and canon disagree about the word *fairway*; **which is right is content, not method.** I report the contradiction and stop.

⛔ **Falsifier, stated because it is the risk I am creating:** a counted predicate whose count never reaches zero is a permanently-amber control — the N8 defect one notch quieter. *Test at C5's retro: if P4 or P5 is still counted and non-zero, the arming condition failed and the predicate wants scoping down or dropping.*

## §3 · THREE CHECKS ALREADY OVERLAP — one tool, and it CALLS them

**One tool, `tools/check-engine-manifest.py`** — I reach §4's conclusion by a different route, and the route changes the build.

| existing check | the question it owns | what the manifest must NOT re-derive |
|---|---|---|
| `check-domains.py` | *is every domain declared, and is an undeclared domain-shaped file on disk?* — its `NON_DOMAINS` already carries a reason string per row, the exception-table shape | root-JSON classification (0a: 26 of 28) |
| `check-data-inline.py` | *does each rostered `*_DATA` const match its source, by parsed compare?* | const-vs-source identity, and the roster itself |
| C4 § 5b `build-viewer.py --check` / § 5d cross-repo | *is the built or copied artifact byte-identical?* | byte-identity — that is P3, `skipped` until 5d exists |

**The manifest's own contribution is exactly one thing: coverage.** *Is every tracked file classified, and does each class have a live owner?* It imports `momlib.DOMAINS`, reads `NON_DOMAINS` and `check-data-inline.SOURCES`, and **fails when a roster it depends on grows a member the manifest cannot place** — the drift none of the three can see alone.

**Who owns the `PROPERTY_DATA` drift after this lands: `check-data-inline.py`, by roster expansion — and the manifest is what makes the omission loud.** Not a new tool: the gap was never a missing capability (that tool already deep-compares, and absorbed `turf.json` on 2026-08-31 for this same reason, per its own `SOURCES` comment). The gap is that **nothing enumerates the consts the roster does not cover** — 10 of 22, six with no producer at all (0d). P5 is that enumeration. *One source, N readers.*

⚠️ **Two exclusions the expansion must carry as stated reasons, not silence:** `CELESTIAL_DATA` **is not JSON** (`json.loads` fails at its second character — unquoted keys), so it has no parsed-comparable source; and `PROPERTY_DATA.climate.monthlyNormals` is **mutated at runtime** after the ERA5 fetch, so that subtree is a cache and would fire on every load. *Two things sharing one const is the finding.*

## §4 · CONFIG-DERIVATION ENFORCEMENT — path-keyed, with a stated blind spot

**A value-literal roster is falsified by measurement (0b).** The shape that survives is keyed on the canonical path, each row carrying its own detector and its allowed locations:

```
{ canonical: "frostDates.atPropertyElevation.firstFall_50pct",
  detector:  "month-day-pair",     # 10, 17 — a TYPE-CHANGED copy, invisible to any string grep
  allowed:   ["property.json", "viewer.html:PROPERTY_DATA", "worker/digest.json"],
  reason:    "the digest is built from canon; the viewer const is inlined instance data" }
```

**What it can see** — three detector kinds, each proven by a planted positive control before shipping: a **literal** copy (`34.5496`, whose one substring covers all three spellings, per 0c); a **type-changed** copy (`10, 17` vs `"October 17"` — the founding instance, and the only kind a value-roster misses); and an **absent consumer** (a canon path with zero readers, e.g. `firstFallRiskBegins`) — **counted, never failed**, because a field nothing reads is a claim about content.

**What it cannot see**, stated so the check does not read as coverage: a value **computed** rather than typed (`2873 / 1000 * 7`); a copy in a **binary or image sidecar**; a copy in a **variable assembled at runtime** — the same limit §0a found on the KV keys, where *"a grep is a good falsifier and a bad source"*; and **whether the canonical value is correct** (`check-domains.py` § "WHAT IT CANNOT DO" already says this in its own voice, and this tool inherits the sentence).

⛔ **Not proposed: deriving the roster from `property.json`'s leaves.** Engineering's open question 8 prices it right — it would flag every incidental number in the tree, and 0c already sizes that: 28 of 40 coordinate hits are legitimate. That is the permanently-red control.

**Falsifier:** plant `FROST_MONTH, FROST_DAY = 10, 17` in a scratch tool and run the lint. **If it does not fire, the design is decorative** — exactly the test a value-roster fails today.

## §5 · WHERE IT RUNS, AND THE MUTATIONS IT MUST BE SEEN TO FAIL

| leg | what runs | why |
|---|---|---|
| `CLAUDE.md` § session-start block | P1 · P2 · P3-skipped · P4/P5 counted | C4 § 5a already sites it here. ⚠️ **Cost, stated:** that block holds **19** `python3` commands today; this is the 20th, and the third whose output is a *count* rather than a verdict |
| C4 § QA (the `[env.qa]` leg) | the **full** run, P3 included, once an engine remote exists | the only place a cross-repo predicate runs without touching prod |
| `build-viewer.py --check` (C4 § 5b) | P5 only, as the build's precondition | a build emitting a const outside the roster has created an unguarded copy *in that run*; next pickup is a lap late |

⛔ **P3 does not belong at session start even after 5d** — it needs a network read of another repo, and a pickup check that reddens on a blip teaches everyone to ignore it. `--full` opts in.

**Mutations** (the shape `check-backlog-ready.py --selftest` already uses — *"proves every flag by mutation"*): an unclassified file planted in a fixture → **P1 fails**; an exception row pointing at a deleted file, **and** one with an empty reason string → **P2 fails** (a waiver with no reason cannot be audited); a type-changed config value (`10, 17`) in an engine file → **P4 counts, then clears on removal**; a new `*_DATA` const absent from the roster → **P5 counts**; a `momlib.DOMAINS` member the dir→class table cannot place → **P1 fails** (the cross-roster predicate). Plus two controls that are the point: ⭐ a **clean fixture must exit 0**, and an **unreachable engine remote must print `skipped`, never `pass`** — *unknown is never counted as healthy*; ⭐ pointed at a fixture whose `viewer.html` is a **404 page** it must **throw**, not score zero consts as clean (memory `reference_match_payload_not_container`).

## §6 · WHAT IT DELIBERATELY DOES NOT DO

- **Grade the divergence tiers.** Assignment is Paul's (`PRODUCT-ENGINE.md` § the divergence contract: *"the ASSIGNMENTS are Paul's"*). It verifies a tier is **stated**, never that it is right.
- **Resolve a drift.** Where viewer and canon disagree it reports both sides and stops; `--fix` stays behind Paul's confirm.
- **Move, rename or reclassify a file.** It flags; it never edits — same posture as `check-backlog-ready.py` and `check-backlog-drift.py`.
- **Decide what a `mixed` file should become.** It records the declared shrink target and reports whether the mixed share moved, as a count, not a grade.
- **Check any value's correctness, or how long a classification has been stale.** No output of it may call a file *overdue*.

## §7 · PRE-REGISTERED QUESTION, AND WHERE IT DISCHARGES

**To be written into C5's plan at `ready`, and answered in that file's `## Retro`:**

> **Did either counted predicate (P4 · P5) reach its arming condition by the time C5 closed — and if not, what was the count on the closing run?** *"Still counted, N unchanged" is a valid recorded answer*, and the more informative one.

**Why this one:** it is the only pre-registration that can falsify §2's central choice, and it is **discharge-enforced rather than remembered** — verified by reading the tool, `check-backlog-ready.py` flags *"at `shipped` with no `## Retro` — the pre-registered question has not been answered"*, and its `--selftest` proves that flag by mutation. That closes the gap memory `feedback_retro_improvement_closes_a_cycle` records, where a lap wrote the exact question that would have caught its own defect and never asked it. ⚠️ **State the prior question's disposition at C5's lap START**, not only at close — silent ≠ carried.

## §8 · OPEN QUESTIONS FOR PAUL

1. Do P4 and P5 arm on **the count reaching zero**, or on a date you set (§2)?
2. Is `mixed` an acceptable class now, or does the manifest wait for C4 § 5b's split so nothing needs it (§1)?
3. `NON_DOMAINS` already classifies 15 root JSONs with reasons — should the manifest **read** it, or should those rows migrate into the manifest and leave `NON_DOMAINS` deriving from it (§3)?
4. `COMMS-CHANNELS.json` and `arrival-dispositions.json` are the two files nothing classifies — declare them in the manifest's exception table, or in `NON_DOMAINS` beside their siblings (0a)?
5. The *fairway* → *clearing* / *turf* / *meadow* rename landed in `property.json` and `references.json` and never reached their inlined consts — is canon right and the viewer stale, or the reverse (0d)?
6. Does C5 sequence the manifest with C4 § **5a** as that plan's own labels say, making §4's *"step 13 / step 15"* a stale reference to correct (0e)?
7. Should the session-start block take a 20th line, or do the three counting checks collapse behind one summary line so pickup stays readable (§5)?
8. Is a 25-row dir→class table acceptable to hand-maintain, given every new top-level directory then needs a row before its files can pass P1 (§1)?
