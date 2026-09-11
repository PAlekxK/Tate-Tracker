# Canon ingestion — when an estate's Guru learns something new

- row: proposed — a row beside TIER 2 · 12 (the per-estate canon store), which this mechanism is the first consumer of `[paul-ruled 2026-09-10 ~11:00 PM ET: "proposed sounds good"]`
- objective: O2
- class: engine · declared
- stage: draft
- seats: engineering-partner → owed: the recompose path, its allowlist and its measured cost (§3 · §6) are code claims nobody has reviewed
         ai-advisor → owed: what a model route may learn from and when (§4's "must NOT trigger" list is the AI-boundary half)
         ux-expert → waived: no surface is drawn here
         content-steward → waived: no copy reaches a person
         user-researcher → waived: no claim about a person is made
- ready: agent-proposed 2026-09-10 — Paul rules. ⚠️ Its core is already RULED on the board (`.plans/2026-09-10-OPEN-ITEMS.md` ①: *ingestion on the confirmation clock*); the allowlist, first light, cost and the eager/lazy fork (§3 · §5 · §6 · §8) are still proposed.
- stage-note: 2026-09-10 ~11:00 PM ET — header added by the backlog-refinement window on Paul's word; the body below is untouched and predates the header.

**Paul asked for** *"a good suggestion for what that ingestion time and process would be."*
This is the answer. It is a PROPOSAL — nothing here is `[paul-ruled]` yet.

The ruling it serves `[paul-stated 2026-09-10]`:

> *"we should be taking whatever information we get from them, confirming it via kind of our
> feedback surfaces, and updating what the garden guru can access as a database as it goes —
> but it should work from virtual first light even if it has a very limited database compared
> to the legacy Fernwood."*

Three requirements are packed into that sentence and they pull in different directions:
**it must work on day one** · **it must get better as people use it** · **and what it learns
must have been CONFIRMED, not merely said.** The proposal is mostly about the third.

---

## 1. The recommendation in one line

> **Ingestion runs on the CONFIRMATION clock, not the arrival clock — a record enters an
> estate's canon at the moment a human settles it, and never at the moment it is captured.**

Everything below follows from that one choice.

## 2. Why the arrival clock is the wrong one, concretely

Capture is deterministic and AI-free by doctrine, and a captured note is **verbatim and
possibly wrong** — that is the whole point of capturing it verbatim. Mom's rainfall report was
right and the app was wrong by 14×; her "household systems" coinage was right and our
correction of it was wrong. **Both are arguments for capturing raw and against ingesting raw.**

If arrival triggered ingestion, then within one turn of a model:

- an unconfirmed guess becomes authoritative context the Guru answers FROM,
- and the Guru's next answer becomes evidence for the guess.

That is not a data-freshness problem, it is a **provenance laundering** problem, and it is the
same class as the canon-election defect this build already paid for once (`est-qa0001`'s Guru
answering *"clear skies over Mead Street"* because canon was elected from whoever had an
address). ⛔ **An estate's canon must contain only things somebody stood on the property and
settled.**

## 3. What TRIGGERS a recompose — the allowlist

An allowlist, not a blocklist. Anything not named here does not trigger ingestion.

| # | trigger | who confirms | why it qualifies |
|---|---|---|---|
| **T1** | **An estate is founded** (`POST /api/estate`) | the founder, by founding | first light — §5 |
| **T2** | **A confirm-card answer is folded** | the person who tapped, plus the fold | this is *already* the mechanism; it generalizes unchanged |
| **T3** | **An owner or member edits the household record** — adds a plant, names a zone, registers a vehicle | the editor, by editing | a deliberate authored act, not a captured one |
| **T4** | **A Guru promotion a human approved** | the approver | already gated; `promote-species` exists |
| **T5** | **The place changes** — address corrected, elevation re-derived, zone re-read | the deriver + the owner | canon's spine; everything else hangs off it |

⭐ **T2 is the load-bearing row and most of it already ships.** Mama's Perspective is a
confirmation surface that produces exactly the signal ingestion needs. **This proposal is
largely the claim that the existing fold step is the correct and only shape, generalized
per-estate.**

⚠️ **But the recompose is OPTIONAL today and that is a real gap in this direction.**
`fold-answer.py` rebuilds the digest only behind `--deploy` (`:131`); without the flag it
prints the two commands and exits. So a confirmation can land, retire its card, advance the
watermark and update the ribbon — **while canon never learns it.** The loop looks closed from
every surface that reads it, and the Guru still answers from the old record. ⭐ Under this
proposal the recompose stops being a flag and becomes **part of the fold**, which is the
smallest change that makes T2 true rather than nearly-true.

## 4. What must NOT trigger a recompose — and this list is the proposal's teeth

| | why not |
|---|---|
| ⛔ **A journal note arriving** | unconfirmed, verbatim, possibly wrong — and it is HER words, which the quarantine clause keeps out of anything derived |
| ⛔ **A Guru turn** | **a question is not a fact.** Ingesting turns closes the loop model→canon→model with no human in it |
| ⛔ **Zone audio, a photo, a transcript** | a transcript is a MODEL READ (`[transcript-UNVERIFIED]`); it may support a human's confirmation and may never be one |
| ⛔ **Feedback about the APP** | scoped to the account, not the estate `[paul-ruled 2026-09-10]` — it is not canon at all |
| ⛔ **Metrics, door records, onboarding records** | outcomes, never people; nothing here is a fact about the place |
| ⛔ **An administrator read** | reading is not writing, and this is exactly the back door the production access ruling closes |
| ⛔ **A schedule — a cron, a nightly, an "every N hours"** | ⭐ **the single most important row.** A timer recomposes on OUR cadence over a record only THEY can change, so it manufactures churn indistinguishable from learning. It is the same defect the ribbon doctrine already names: *it goes quiet when she does.* **Canon should too.** |

## 5. First light — what an estate knows on day one

At `POST /api/estate` the digest composes **inline, from derived place alone**:
address → coordinates → elevation → USDA zone → frost dates. That is ~2 KB against Fernwood's
**611 KB** of four accumulated years — and it is enough for a Guru that can answer *where am I,
what zone am I, when is my last frost*, which is a real product on day one.

⚠️ **Two writers of one fact, and it is the defect shape this build keeps finding.** The Worker
will compose inline at founding; `tools/publish-digest.py` composes the same digest locally.
**They must produce byte-identical output for identical inputs**, verified by a drift-lint that
compares FIELD BY FIELD — not by fingerprint equality, which tells you *that* they diverged and
never *where*. `publish-digest.py` already has `fingerprint()` and `body_of()` (which correctly
excludes `rebuiltAt`, because a timestamp is not drift); the lint is the missing half.

⛔ **First light must not inherit Fernwood.** The bundled 611 KB digest is stamped `est-3c9f1a`
and `canonFor()` already refuses a digest whose stamp disagrees with the caller. **That guard
stays.** A new estate with no digest gets `null` and a Guru that says it does not know yet —
which is honest, and is strictly better than an estate whose first answer is about somebody
else's pond.

## 6. What it costs — measured, not estimated

A recompose is: read the household record from KV → chain the canon loaders → write one key.
**Single-digit KV ops, one write, sub-second.** At Fernwood's size the payload is 611 KB; at a
first-light estate it is ~2 KB. KV's per-key ceiling is 25 MB, so **size is not the constraint
and will not be for years.**

⭐ **So cost is NOT the reason to debounce.** The reasons are correctness and provenance:

1. **A digest must not change under a live conversation.** A turn that starts against digest A
   and finishes against digest B is unreproducible, and the Guru's own answer becomes
   unattributable.
2. **Every recompose must be attributable** — who confirmed what, when. A recompose nobody can
   name the cause of is the thing that makes canon un-auditable.

**Debounce shape:** fold N answers in one sitting → **one** recompose at the end of the sitting,
stamped with the set of confirmations that caused it. Not a time window — a **transaction
boundary**, which is what a fold session already is.

## 7. Where it FAILS SAFE — the part I would review first

⛔ **A compose that cannot read its inputs must REFUSE TO PUBLISH.** Not publish a partial
digest; not publish an empty one.

This is **green by absence**, this repo's most-repeated failure, and canon is its worst possible
site: a compose that reads a KV error as *"this estate has no plants"* and publishes accordingly
has **silently deleted the estate's memory**, and every downstream check reads green because the
digest exists and is well-formed. `publish-digest.py` had exactly this bug (`except Exception:
return None` in `household_property()`) and was fixed to distinguish a genuine 404 from an
unreadable key. **The inline composer must be written to that same standard on its first day,
not patched to it later.**

Three failure rules:

1. **Unreadable ≠ absent.** A 404 is a fact about the key; any other error is a fact about the
   read, and only the first may be composed from.
2. **Refusal is loud and the OLD digest stands.** The previous canon is correct-but-stale, which
   is recoverable; a truncated canon is a silent lie, which is not.
3. **The refusal names the estate and the key it could not read**, so the repair is one command
   rather than an investigation.

## 8. Eager or lazy — the one real fork, with a recommendation

|  | eager (compose at confirmation) | lazy (mark dirty, compose at next Guru call) |
|---|---|---|
| the human sees it land | ✅ **yes — they are still there** | ❌ no |
| cost | one compose per sitting | one compose per idle estate that is never asked |
| failure is visible | ✅ at the confirmation, to a person | ❌ inside somebody's next question |

⭐ **Recommend EAGER**, and the deciding argument is not performance — it is the project's own
loop-close doctrine. *The user must see their reading replace the estimate, or it feels
extractive.* A lazy compose defers the close to a moment nobody is watching, and moves the
failure into a stranger's next question.

**Keep the dirty flag anyway**, as the REPAIR path: an eager compose that refused (§7) leaves the
estate marked dirty, and that flag is what a check can read to find estates whose canon is behind
their confirmations. ⭐ **That check is the reader clause** — an event with no reader is not
instrumentation, and this proposal should not ship a dirty flag nothing reads.

## 9. What this proposal does NOT settle

- **Who may confirm, once a household has two people.** T2–T4 say "a human"; with an owner and a
  member that is under-specified, and it is a capability question, not an ingestion question.
- **Whether an administrator may confirm at an estate they hold no relationship to.** The
  production-access ruling says they hold none until invited; whether ingestion inherits that is
  Paul's.
- **Retraction.** Everything here is additive. *"She confirmed it and was wrong"* has no path,
  and **"everything is changeable" is a promise this proposal cannot currently keep.**

⭐ **Of the three, retraction is the one I would raise first** — it is the only one that makes a
promise already live on Mom's surfaces untrue.
