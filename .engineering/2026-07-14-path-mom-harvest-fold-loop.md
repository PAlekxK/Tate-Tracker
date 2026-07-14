# Path eval — Mama's Perspective: the harvest → fold → log loop (+ a pipeline-integrity bug)

**Date:** 2026-07-14
**Mode:** Path Evaluation (engineering-partner)
**Subject:** The automation spine behind "Mama's Perspective" — how canon uncertainty becomes candidate cards (HARVEST), how a confirmed answer folds back into canon (FOLD), where raw Q&A durably lives (LOG), and a genuine integrity bug in `check-data-inline.py` (FLAG).
**Stakes:** Hobby project, primary user = Mom. Calm/AI-free-capture/human-confirmed-fold doctrine LOCKED by Paul. Severity calibrated accordingly.

**Customer grounding:** Mom is the confirm-card answerer (ground-truth only someone on the land can give); Paul is the operator who harvests, folds, and maintains canon. The loop's whole value is the moat named in the "glance & repository" governing principle: *fresher local ground-truth → better glance → more trust → more input.* Every recommendation below protects two things: that the loop stays deterministic where Paul locked it, and that Mom's verbatim words never leak onto the public web.

---

## The single biggest engineering risk

**`check-data-inline.py` is content-blind, and the fold loop's entire payload is content edits to existing entries.** The guard that's supposed to protect the inline-sync invariant checks only the *id-set* of each category — so a prose/field edit to an entry whose `id` didn't change reads as "in sync," and `--fix` (which only acts on the drift list) does nothing. That is *exactly* the mutation class every fold produces (flip a `confidence`, correct a variety, edit a note). Wire up assisted-fold on top of a content-blind check and **silent dashboard staleness becomes the default outcome of every fold** — Mom confirms "Lucifer," Paul folds it to `plants.json`, and `viewer.html` keeps rendering the old prose with the check saying green. **Fix the check before building the fold pipeline.** Details in FLAG below.

---

## 1. HARVEST — how canon uncertainty becomes candidate cards

### The key finding that reframes the question
Uncertainty is **already a first-class structured field in one place**: `confidence` lives on the `bloom` block of every flowering plant (21 occurrences; values `verified | inferred | high | null`), and it already flows to the Guru digest. Variety-level uncertainty, by contrast, is still **prose** — the Lucifer confirmation was folded into `scientificName` as the string `"Crocosmia 'Lucifer' (montbretia)"`, with no structured marker. So the schema foundation you'd build on *already exists and is proven*; the real question is whether to (a) generalize it beyond `bloom` and (b) add a hint that separates "uncertain" from "uncertain **and Mom can settle it**."

### The three realistic paths

| | A — Regex-harvest prose | B — Structured-first (`confidence` + `askable`) | C — Hybrid: structured harvest + regex drift-lint |
|---|---|---|---|
| **Complexity** | Low to write, high to *trust* — brittle patterns, endless false-positive tuning | Medium — a small schema addition + a trivial filter | Medium — B plus a secondary lint that never gates |
| **Scalability** | Degrades as canon grows; every new prose phrasing is a missed or false hit | Scales cleanly — new uncertain fact = one tagged field | Scales like B; lint keeps the tagging honest as canon grows |
| **Future features** | Dead-ends — prose can't carry an `askable` audience or a per-fact resolution state | Opens per-fact provenance, digest hedging, multi-audience asks | Same as B |
| **Future-Paul-with-Claude** | Opaque — the harvest logic *is* a regex zoo; you re-derive intent every time | Legible — "scan for `confidence:inferred` + `askable`" is a one-sentence mental model | Legible; the lint is self-documenting ("you wrote 'estimate' but didn't tag it") |
| **Learning value** | Teaches you why text-scraping structured meaning is a trap (patio11 territory) | Teaches schema-as-contract + derive-vs-scan | Best — teaches both, plus "generate the derivable, drift-lint the rest" |

### Recommendation: **C, weighted heavily toward B.**

**The schema.** Treat `confidence` as the general per-fact honesty marker it already half-is, and add an optional sibling `askable` on the same fact block. Minimal shape, reusing what `bloom` established:

```jsonc
"bloom": {
  "window": "July into August",
  "dates": [{ "start": "07-01", "end": "08-31" }],
  "confidence": "inferred",
  "askable": "mom-observable",          // NEW — this uncertainty is settleable from the ground
  "askHint": "has it opened yet?"        // NEW, optional — a STUB for Paul, not shipped copy
}
```

For variety-level uncertainty (the Lucifer/Annabelle class), give it the same treatment rather than leaving it in prose — a small structured block on the plant, e.g. `"variety": { "value": "Lucifer", "confidence": "inferred", "askable": "mom-observable" }`, and let the display string derive from it. That kills the "brittle prose scan" problem at its source: the thing you harvest is a declared fact, not a sentence.

**Why `askable` is load-bearing and not gold-plating:** not every `inferred` is Mom-answerable. `confidence:inferred` on a hardiness zone is book-knowledge she can't settle by looking; `confidence:inferred` on a variety name or a bloom date *is* ground-observable. Without the `askable` filter, harvest floods Paul with un-askable inferreds and he hand-filters every run — which is the manual step the tool exists to remove. `askable` is the exact filter from "uncertain" to "uncertain AND she can settle it."

**The tool.** `tools/harvest-questions.py` — deterministic, AI-free, propose-only:
1. Walk `plants.json` (and later other canon) for fact blocks where `confidence in (inferred, null)` **and** `askable` is truthy **and** no live `questions.json` row already covers that `entityRef`.
2. Draft a candidate card (`kind:"confirm"`, `answerMode:"yesno"`, `entityRef` auto-filled from the plant id + fact path, `askHint` as a *stub* prompt).
3. Print them as a punch-list; Paul approves/edits into `questions.json` by hand. **Never writes `questions.json` itself** — that's the human gate the LOCKED "Paul approves before live" decision requires.

**Keep the regex — but demote it to a lint, not the harvest.** A secondary pass scans prose (`estimate`, `possibly`, `we read it off`, `off the book`) and flags any fact that reads uncertain in prose but carries **no structured `confidence`/`askable`**. That's the "you forgot to tag this" safety net — it catches the gap between Paul's writing habit and the schema, without ever being the thing harvest trusts. This is the cross-project **"Generate the derivable; drift-lint the rest"** principle applied verbatim: derive candidates from structure; lint the prose for untagged honesty.

**Cross-lens flag (content-steward / ux):** `askHint` is a *stub for Paul*, never AI-authored shipped copy. The Mom-facing prompt in `questions.json` stays Paul-authored (it already is) and is content-steward's register to tune — harvest drafts a placeholder and marks it `DRAFT — rewrite before live`. Auto-generating the ask *copy* would be AI on the ask-path (allowed by doctrine) but the calm/tone bar means prompt wording is a content decision, not a harvest side-effect. Keep the seam.

---

## 2. FOLD — the assisted one-tap canon edit

`read-mom-feedback.py` already drafts the fold suggestion (`fold_suggestion()` → "flip `plants.json` `<id>` confidence inferred→verified" or "correct it — she says: '<note>'"). What's missing is the *execution* spine. The good news: **every step except "apply the edit" is already a tool.**

The deterministic spine (chain in code; halt at the human gate):
1. **Draft the exact `plants.json` diff** — flip the mapped `entityRef.id`'s fact `confidence: inferred → verified`, or apply her correction to the field. **← the one judgment step; this is where the tool halts and shows Paul the diff.**
2. Apply on Paul's approval.
3. **Re-inline** `PLANTS_DATA` (see seam note).
4. **Rebuild digest** — `tools/build-digest.py`.
5. **Deploy** — `tools/deploy-worker.sh` (agent-runnable unsandboxed, per the 2026-07-14 finding).
6. **Retire the card** — flip `questions.json` `active:false` + write the `resolution` line (matches the two already-resolved rows).
7. **Advance the watermark** — `--mark-reviewed`.

### Recommendation: a **separate `tools/fold-answer.py`**, not an extension of `read-mom-feedback.py`.
`read-mom-feedback.py` is deliberately read-only — its docstring makes "never writes canon" a contract, and that contract *is* the doctrine boundary (reading feedback is safe/automatic; folding to canon is the human-gated step). Bolting a canon-writer onto the reader muddies exactly the line Paul locked. Cleaner: `fold-answer.py` **imports** `fold_suggestion` from the reader (single source of truth for the draft logic) and owns the write orchestration. The reader stays a reader; the folder is the orchestrator that halts at the diff.

This is the cross-project **"Chain the deterministic spine in code; halt at the human gate"** principle — the halt is between step 1 (show diff) and step 2 (apply). Everything downstream of the approval is mechanical and should run without re-prompting.

### Seam to fix first: decouple re-inline from attribution-merge.
`wire-photos.py --category plants` is what `check-data-inline --fix` and any fold would call to re-inline — but it *couples* re-inline with an `_attribution.json` re-merge (it rewrites `plants.json` with photo/attribution fields before inlining). For a fold you want **re-inline only**, no attribution side-effect. Extract a standalone re-inline (a tiny `tools/reinline.py --const PLANTS_DATA`, or a `--reinline-only` flag) so `fold-answer.py`, `check-data-inline --fix`, and future callers share **one** re-inline mechanism (single-source-of-truth for the inline write). This also de-risks the FLAG fix below.

---

## 3. LOG — where raw Q&A durably lives

Raw answers already persist in Worker KV (`feedback:YYYY-MM-DD`), and the Worker comment already names the boundary: *"feedback contains user-authored note text — same boundary as observation bodies."*

### The paths: (A) keep in KV + export on demand · (B) commit a durable mirror file · (C) a field-journal surface showing Mom her own answers back.

### Recommendation: **A — KV as system-of-record, export-on-demand to a gitignored `.private/` file. Do not commit verbatim notes. Defer C.**

**Why not B (committed mirror):** two independent disqualifiers.
- **Privacy is load-bearing and this repo is public GH Pages.** Mom's verbatim notes — especially the open-channel "something about the app?" line — are personal text. Committing them *publishes* them, forever, in git history. Same instinct as **"a secret in a client-inlined env var is already published"**: anything in the public repo is published. The only thing that should ever reach public canon is the *curated ground-truth Paul folds by hand* (variety confirmed, date verified) — which the FOLD loop already does. Her raw words are not that.
- **A committed mirror is just a second copy of KV** — it fails the cross-project **"a ledger earns its existence by answering a different question, not holding a different copy"** test.

**Why A works:** the "durability" worry is really "can I lose KV / is it backed up." Answer it with an **export**, not a commit. Add `--export` to `read-mom-feedback.py` that writes the raw range to `.private/mom-feedback-log.json` (gitignored, merge-append, watermark-independent). That's your durable research archive — offline, private, and it answers a *different* question than KV (long-horizon local record vs. live store), so it earns its existence. Matches the fernwood principle **"field-captured free text lands in the private store; canon grows only by hand."**

**Why defer C (a surface that shows Mom her past answers):** it's a genuinely nice loop-close, but it's a speculative affordance with no signal yet (**defer-affordances-pending-signal**), it's Phase-E/observations-layer shaped, and it raises its own "close the loop visibly" design work. If ever built, it reads from **KV live**, never from the committed file. Park it.

---

## 4. FLAG — the `check-data-inline.py` content-drift bug + fix

### Root cause (confirmed by reading the code)
`species_ids()` reduces every entry to `{item["id"]}` and `check_all()` compares only those **id-sets** plus the count:
```python
missing_in_inlined = json_ids - inlined_ids   # ids only
extra_in_inlined   = inlined_ids - json_ids
```
Edit prose/fields on an entry whose `id` is unchanged → `json_ids == inlined_ids` → **"OK … in sync"** printed → `any_drift = False` → `--fix` gets an empty `drift_categories` and re-inlines nothing → `viewer.html` stays stale. Exactly the failure Paul hit after the bloom/hydrangea prose edits.

**This is the mirror image of an existing cross-project principle** — *"A build script that overwrites a hand-edited artifact must reconcile membership, not just fields."* That principle warns about scripts that preserve *fields* but wipe *membership*. `check-data-inline` is the **inverse**: it verifies *membership* and ignores *fields*. Same coin, other face. Content drift is the blind spot.

### The fix — deep content compare
In `check_all()`, after the id-set check passes, compare the **full parsed structures**, not just ids:
```python
if inlined != json_data:            # parsed dict/list deep-equality
    # report the first N differing paths, e.g.
    #   DRIFT PLANTS_DATA: plants.crocosmia.scientificName
    #     inlined: "Crocosmia (montbretia)"
    #     source : "Crocosmia 'Lucifer' (montbretia)"
```
Key subtleties to get right (teach-as-you-go):
- **Must be a PARSED compare, never a text compare.** The inlined const is `json.dumps(data, ensure_ascii=False)` (single-line, minified); the source file is `indent=2`. A byte/text diff would false-positive on formatting every time. Parse both, compare objects — Python dict equality is deep and key-order-independent; list equality is order-sensitive, which is correct here (entry order is meaningful).
- **Report the differing path, not just "they differ."** Walk both structures and surface the first handful of divergent key-paths + old/new values, so the message is actionable ("which entry, which field") rather than "something drifted."
- **`--fix` already works once detection fires** — it re-inlines the whole blob via the re-inliner. So the fix is *purely in detection*. (Do route it through the decoupled re-inliner from §2's seam note, not the attribution-coupled `wire-photos`.)
- This directly closes Paul's open root-cause note *"make re-inline verify itself"* — a deep check is the verification.

### Two adjacent gaps worth noting (not blocking)
- **`vehicles.json` is not in `SOURCES` at all** — its `VEHICLES_DATA` const is hand-inlined and entirely untracked by this check. That's a latent instance of the *same* bug on a different const; the fold loop is plants-only today so it's not urgent, but it's the next place this bites.
- The single-line-blob regex extraction (`const NAME = ({.*?});`) is fine today because each const is one minified line; if a const ever gets pretty-printed inline, the non-greedy `.*?` could truncate at the first `};`. Not a today-problem; flagging for the file.

---

## Conflicts with locked decisions / other lenses

- **No conflict with the LOCKED reseed/fold doctrine.** Structured-first harvest *strengthens* the "deterministic HARVEST" Paul locked (declared fields are more deterministic than prose scans). The fold orchestrator keeps the "Paul approves before apply" gate exactly where Paul put it.
- **Content-steward seam:** `askHint` stubs and `questions.json` prompt copy stay Paul/content-steward-authored — harvest drafts placeholders only.
- **ux-expert:** none of this changes the Mom-facing surface; it's all operator-side plumbing. The deferred "show Mom her answers" surface (LOG option C) would be a ux thread if it ever wakes up.
- **ai-advisor:** the whole spine is deterministic and AI-free by design — no hand-off needed. (If harvest ever auto-drafts prompt *prose* with a model, that's an ask-path AI decision to route to ai-advisor first. Recommend it doesn't.)

---

## Decisions for Paul

1. **Do you want the FLAG fix (deep content compare) as a standalone first ship, ahead of the fold pipeline?** (Strong recommend: yes — it's the guard the fold loop leans on.)
2. **Schema call:** promote `confidence` to a general per-fact marker + add `askable`/`askHint`, including lifting variety-uncertainty out of prose into a structured `variety` block? Or keep variety in prose and only harvest `bloom`-style blocks for now?
3. **Fold tool shape:** separate `tools/fold-answer.py` (recommended) vs. extending `read-mom-feedback.py`?
4. **LOG:** confirm KV + gitignored `.private/` export, no public commit of verbatim notes?

## Principles to propose (pending Paul)
- **cross-project:** "An inline/derived-copy integrity check must verify *content*, not just *membership*" — the content-face companion to the existing membership principle (line 125). Surfaced by this bug.
- **fernwood:** "Uncertainty is a structured field, not a prose phrase — harvest from the field, drift-lint the prose." (Candidate — 1 occurrence; watch for a second sighting.)
