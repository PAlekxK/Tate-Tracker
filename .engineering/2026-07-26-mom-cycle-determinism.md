# Path-eval — making the Mom-feedback cycle deterministic where it can be

**Date:** 2026-07-26 · **Mode:** path evaluation · **Agent:** engineering-partner
**Trigger:** two failures on 2026-07-26 — an 8-day-stale acknowledgment ribbon, and a fold
punch-list that reported already-folded answers as pending.
**Privacy:** this repo is PUBLIC. Mom's verbatim words are in `.private/mom-feedback-2026-07-26.md`
(gitignored) and are referenced, never quoted, here.

---

## 0. Context established before critiquing

- **Customer:** Mom, the make-or-break user (`.user-research/persona-mom.md`, `_about-paul.md`).
  Reads with difficulty. Her stated blocker, in her own words on 7/26, is **fear of being wrong**
  — not disengagement, not modality (`BACKLOG.md` A3, `.private/mom-feedback-2026-07-26.md`).
  Evidence tag: **validated** (user-stated, unprompted, twice, corroborated by which cards she
  answered and by what she did instead).
- **Paul's intent for this cycle:** four legs — she gives input → it lands in the record → **it is
  reflected back TO HER so she knows she was heard** → she is asked for more. Leg 3 is the one
  that failed, and it is the leg whose whole purpose is emotional reassurance.
- **Stack/conventions:** no build step, single-file `viewer.html` with inlined `*_DATA` consts,
  source JSON as SSOT, Python tools in `tools/`, session-start `check-*.py` family that exits
  0/1. Cloudflare Worker + KV for the record. **Reuse the check-family pattern; don't invent.**
- **Deployment context:** family-internal, public repo, `mom-ready`. Robustness level: **shippable**
  for anything Mom sees; `working` for Paul-side tooling.
- **Stakes:** nothing here loses money or breaks the law. The costs are (a) Mom spends a week
  doubting answers that were already correct and already in the record — the exact opposite of
  what the surface is for; and (b) Paul's session time is spent on phantom to-dos that then
  propagate into the backlog and briefs. Calibrate accordingly: **no enterprise scaffolding.**

`code_context_confidence: high` · `user_context_confidence: high`

---

## 1. The class, not the instances

Both failures are the same shape:

> **A status was written down at one moment and read later as if it were a measurement of the
> world at *that* moment.**

The ribbon asserted "we heard you about the panicle hydrangea." True on 7/22. Read on 7/26 as
though it were current. The punch-list asserted "these three are ready to fold." True on 7/13.
Read on 7/26 as though it were current.

The **tell both share is that neither claim carried a clock.** A derived value is self-dating —
you recompute it and it is true right now, by construction. An asserted value is a timestamped
claim that needs someone to maintain its "as of," and nobody ever does. `MOM_ACK_DATA` literally
had an `answeredOn` field with no defined meaning and no consumer; the punch-list had no notion
of "as of what canon" at all.

**Two principles already in the library cover this, and neither had crossed into Fernwood's Mom
loop:**

1. **"Derive a gate's pending-count; don't list it" (cross-project, 2026-07-01)** — surfaced from
   the Hillyer eyeball queue, which reported ~41–53 pending when 3 were. `read-mom-feedback.py`
   is the same bug, one repo over: it lists every answered confirm rather than reconciling
   staged-against-cleared. The principle even names the downstream harm — *"an inflated
   pending-count rots the gate toward rubber-stamp."* That is exactly what happened: the phantom
   propagated into `BACKLOG.md`, a user-researcher brief, and three agent reports unchallenged.
2. **"A deploy-bundled context artifact needs a rebuild-and-diff drift alarm" (Fernwood,
   2026-07-07)** — surfaced from the stale Worker digest. `MOM_ACK_DATA` is a deploy-baked
   artifact (it ships with `viewer.html` on push) whose source can change without it rebuilding.
   It is now the **only** Mom-facing baked constant with no drift alarm — the same sentence that
   was true of `ZONES_DATA` in July before it got one, and of `digest.json` in July before
   `check-digest-fresh.py`.

That's the real finding for Paul: **this wasn't a novel failure. It was two known principles that
never got a mechanism in this corner of the repo.** A principle without a check is a policy
statement, and a policy statement is what stayed stale for 8 days.

---

## 2. Where state is asserted instead of derived — the full inventory

| # | Where | What it stores | What would derive it | What breaks today |
|---|---|---|---|---|
| **S1** | `MOM_ACK_DATA` in `viewer.html:9033` | The message Mom sees + `answeredOn` (a date nothing reads) | max(input timestamp across `/api/feedback`, `/api/observations`, `/api/zone-audio`, off-system) vs. what the ribbon covers | **The 8-day staleness.** Nothing computes it, nothing checks it, and there is no field on the object that could even *express* what it covers. |
| **S2** | `read-mom-feedback.py:200-209` fold punch-list | "answered + definitive sentiment ⇒ ready to fold" | live canon confidence at the fold target, plus the card's own resolution state | **The phantom to-do.** It ignores `q.active` (which it *does* compute two lines earlier for the `[retired…]` tag) and never touches `plants.json`. Same in `--pickup` (line 239). |
| **S3** | `.private/mom-feedback-state.json` → `lastReviewedTs` | "everything through this instant has been dealt with" | nothing — pure assertion | `--mark-reviewed` stamps the max ts of **every** record shown, not the ones acted on (`read-mom-feedback.py:285-292`). And `fold-answer.py:198` invokes it after folding **some**. Fold one card and an unrelated unfolded answer stops being "new" forever. **This is the one path in the cycle that can silently lose Mom's input.** |
| **S4** | `questions.json` → `active` | Two opposite things: *never-served draft* and *retired-after-fold* | — | The field that names the state can't distinguish them; `resolvedAt` is the accidental discriminator. Live proof: `q-wisteria-summer-cascade-bloom` (`active:false`, no `resolvedAt`) = draft. `q-panicle-hydrangea-bloom` (`active:false`, `resolvedAt:2026-07-22`) = retired. Consumers disagree on what it means: harvest treats both as covered, fold-answer treats only `active:true` as foldable, read-mom-feedback ignores it entirely. |
| **S5** | `questions.json` → `resolvedAt` / `resolution` | Free-text claim that a fold happened | for probeable targets, the canon field itself | Written by `fold-answer.py` for auto-folds, hand-written for judgment folds (run 1). Nothing verifies it against canon. The 'Annabelle' fold landed in the hydrangea **roster** — a place no generic probe can point at — so for that card the assertion is all there is. |
| **S6** | `harvest-questions.py:62-70` `covered_ids()` | "an entity is covered if any question mentions it" | "the uncertainty marker is still open" | **Counts artifacts instead of deriving state** — Paul's own words for the class. Two consequences: a draft Paul *declined* suppresses that entity's re-harvest permanently; and a card whose canon premise has since been settled is never retired (run-1 finding #1, still open). |
| **S7** | `.private/mom-queue-watch-state.json` → `pingedAnswerIds` | Which answers we've already pinged about | — | Overwritten each run with `answered_open`, which only includes `active:true` cards — so the memory silently drops entries when a card retires. Low harm (worst case: a duplicate ping). |
| **S8** | `.private/mom-funnel-watch-state.json` → `stage` | Monotonic engagement ratchet | derivable from the events each run | Can only advance; a regression is invisible. Low harm, deliberate design. |
| **S9** | `people.json` device→person map | Attribution | — | **Already known invalid** (`BACKLOG.md` A1: shared phone; Safari ITP evicts the id). Any future "Mom's latest input" derivation inherits this — see §3.4. |
| **S10** | `BACKLOG.md` A1/A3 rows, agent reports | Narrative status transcribed from a tool's output | the tool, re-run | Not code, but it's where the phantom did its damage. **A derived fact transcribed into prose becomes an assertion the moment it's pasted.** |

**The counter-example, and it's the model to copy:** `read-mom-funnel.py` derives everything —
H1–H5 and the GROW/HOLD/KILL verdict are computed from raw events on every run, with the
attribution caveat printed rather than hidden. `check-data-inline.py` and `check-digest-fresh.py`
both derive by rebuild-and-compare. **Fernwood already knows how to do this.** The Mom loop is
where the pattern didn't reach.

---

## 3. The design — keeping leg (3) honest

### 3.1 The one structural change: give the ribbon a clock

Add one field to `MOM_ACK_DATA`:

```js
const MOM_ACK_DATA = {
  message: "...",                          // Paul's words. Unchanged, human-authored.
  acknowledgedThrough: "2026-07-26T13:06:00Z",  // NEW — the newest input this ribbon covers
  channels: ["text", "guru"],              // NEW, optional — which channels it covers (for the check's message)
  questionId: null                         // keep; now optional
};
```

`acknowledgedThrough` is the whole trick. It converts "is the ribbon stale?" from an unanswerable
question into a comparison. `answeredOn` should be retired or redefined — today it's a date with
no consumer and no defined meaning, which is how it managed to be simultaneously present and
useless.

**Why a timestamp and not a question id:** input now arrives through four channels, only one of
which has a question id. The ribbon's promise is "we've heard everything you've given us up to
here," and only an instant can express that.

### 3.2 `tools/check-mom-ack.py` — the session-start check

Same shape as its two siblings: read-only, exit 0 = silent, exit 1 = surface it.

**What it reads**
1. `MOM_ACK_DATA` parsed out of `viewer.html` (regex the const, `json.loads` — same technique
   `check-data-inline.py` and `reinline.py` already use). **Keep the constant as the SSOT — do
   not add a `mom-ack.json`.** Every other inlined const has a source JSON because it's fetched
   at runtime or shipped in the Worker digest; the ribbon is neither. A parallel JSON here would
   be exactly the duplication `[[feedback_single_source_of_truth]]` warns against, and would add
   a re-inline step to a one-object constant.
2. `GET /api/feedback` — mom-queue answers + general notes (via `read-mom-feedback.py`'s existing
   `_get` / `resolve_token`).
3. `GET /api/observations` — Guru turns. Her 7/26 questions came through here.
4. `GET /api/zone-audio` index — voice captures.
5. `.private/mom-input-log.json` — **the off-system channel.** A tiny gitignored ledger:
   `[{ "ts": "...", "channel": "text", "summary": "moss + buttermilk; household systems idea" }]`.
   Gitignored because it's about her; the summary is Paul's non-verbatim descriptor, never her
   words. This is the only new artifact the design introduces, and it earns its existence by
   answering a question no other store can (`[[a ledger earns its existence by answering a
   different question]]`): *did she say something to Paul that never touched the app?*

**What it computes**

```
latest_input   = max(ts across all four channels)
acknowledged   = MOM_ACK_DATA.acknowledgedThrough
shipped        = (viewer.html is clean in the worktree)
                 AND (git log origin/main..HEAD -- viewer.html is empty)

exit 1 if latest_input > acknowledged        → "the ribbon doesn't cover her latest input"
exit 1 if not shipped                        → "the ribbon is written but not pushed"
exit 0 otherwise                             → print nothing
```

The `shipped` half matters as much as the freshness half: `CLAUDE.md` already says *"shipping
means a push (Pages serves `viewer.html`), not just a commit."* A ribbon Paul wrote, committed,
and didn't push is exactly as stale to Mom as one he never wrote. That sentence is currently
another policy statement with no mechanism; this is the mechanism, and it's four lines.

**What it prints on failure** — the evidence, never the words:

```
STALE  The acknowledgment ribbon doesn't cover Mom's latest input.
       ribbon covers through : 2026-07-22 18:41 ET
       newest input          : 2026-07-26 09:04 ET  (4 days later)
       channels since        : guru (2 turns, 8:57 + 9:00 AM ET) · text-ledger (1 entry)
       ↳ Name what she actually gave. Update MOM_ACK_DATA.message + acknowledgedThrough,
         then COMMIT AND PUSH (Pages serves viewer.html).
       ↳ If none of that input was hers, stamp it:
         python3 tools/check-mom-ack.py --acknowledged-through 2026-07-26T13:04Z
```

**What it must not do:** write the message, generate a message, or advance
`acknowledgedThrough` on its own. It computes the *trigger* and the *evidence*; the human
computes the *words*. See §4.

### 3.3 Offline and failure posture

If the Worker is unreachable, **still run the local half** (ledger + push state) and print one
line — *"couldn't reach the Worker; the app-side channels are unverified"* — and **exit 0.** A
session-start check that hard-fails on a bad network is a check Paul learns to skip, and a check
that gets skipped is worth less than no check. This matches the existing family: `mom-queue-watch`
and `read-mom-funnel` both return quietly on a fetch failure. The loud failure is reserved for the
case where we *know* the ribbon is stale (`[[Match failure posture to stakes, not to the
artifact's name]]`).

### 3.4 The attribution boundary — the check asks, it never asserts

The check **cannot know** whether a given input was Mom's. Shared phone, `people.json` invalid,
Safari ITP splits the id — `BACKLOG.md` A1 documents all of it. So the output above is phrased as
a **prompt for judgment**, not a claim: *"input landed that the ribbon doesn't cover"*, and the
`--acknowledged-through` stamp exists precisely so Paul can say "that was me testing" in one
command.

This is the right seam. Attribution is a judgment call Paul already makes every run (he
attributed run 1 at "99%"). Automating it would be inventing certainty the data doesn't contain —
the same error class as the model-read rule in the global CLAUDE.md.

### 3.5 Wire it in three places, compute it once

```bash
# CLAUDE.md session-start block — one added line
python3 tools/check-mom-ack.py                # is the ribbon current, and did it ship?
```

- **Session start** — where Paul already looks.
- **`mom-queue-watch.py`** — widen its trigger. Today it pings only when *a fold is waiting*
  (`answered + active:True`), which is why 7/26 was silent: she gave input through three channels
  and answered zero cards. It should ping on **"she gave input we haven't acknowledged"** — the
  same computation. Import it; don't reimplement it.
- **`fold-answer.py`** — after a successful fold, print the ribbon reminder with the folded
  entity named. A fold is by definition new acknowledged-through material.

**One derivation, three consumers.** Which brings up the module:

### 3.6 `tools/momlib.py` — the shared definition (rule-of-three has fired)

Three tools currently carry a **verbatim copy** of the same `_load()` helper
(`fold-answer.py:44`, `mom-queue-watch.py:44`, `read-mom-funnel.py:57`) purely because
`read-mom-feedback.py` has a hyphen in its name and can't be `import`ed. And there are now
**three mutually inconsistent definitions of "pending"** across four tools (S2/S4/S6).

This is not premature abstraction — AHA says don't abstract before you know the shape, and the
duplication here has *already produced divergent behavior and a real bug*. Extract:

```python
# tools/momlib.py  (underscore name → plain `import momlib`)
resolve_token()  _get()  flatten()          # moved from read-mom-feedback.py
question_state(q, canon) -> "draft" | "open" | "settled-in-canon" | "resolved" | "unprobeable"
latest_mom_input(channels) -> (ts, [channel...])
ribbon_state(viewer_path) -> (acknowledged_through, shipped)
```

`read-mom-feedback.py` keeps its CLI and imports the library. This is the one refactor I'd
actually spend time on, and the reason is maintainability-with-Claude: when future-Paul asks
"what counts as settled?", there should be **one function to read**, not four opinions to
reconcile.

---

## 4. Fixing `read-mom-feedback.py`

### What it should read

For each answered confirm, resolve state instead of assuming it — this is `question_state()`:

| Card condition | Derived state | Bucket |
|---|---|---|
| `active is not True` **and** `resolvedAt` present | `resolved` (assertion-backed) | Already settled |
| `active is not True` **and** no `resolvedAt` | `draft` — an answer against a never-served card | ⚠️ Anomaly — print loudly |
| `active is True`, target probeable, canon says `verified` | `settled-in-canon` | **Stale-premised card — retire it** |
| `active is True`, target probeable, canon says `inferred` | `open` | **Ready to fold** |
| `active is True`, no `_foldTarget` / unmapped ref / roster-level fold | `unprobeable` | Can't verify — check by hand |

The probe resolves `entityRef.type` → source file (`plant`→`plants.json:plants`,
`weed`→`weeds.json:weeds`) and `_foldTarget` → field (`variety`→`variety.confidence`,
`bloom`→`bloom.confidence`, `confidence`→`confidence`). **It must not assume plants** — three
live cards point at weeds (`q-weed-stiltgrass` is `active:true` with `_foldTarget: "confidence"`),
and `fold-answer.py` today silently degrades them to "entity not found in plants.json."

**Where a probe doesn't exist, say so — don't fake one.** The 'Annabelle' fold landed in the
hydrangea roster; no generic field probe can see it. Print it as an assertion, labelled as one,
with its `resolvedAt`. Honest labelling beats a probe that lies. This mirrors the app's own
`confidence: inferred` doctrine — an honestly-unsure tool is better than a confidently-wrong one.

### What it should print

Three buckets, not one list. Only the first is a to-do:

```
Ready to fold — canon still says inferred
  • q-clematis-variety   plants.json `clematis`  variety.confidence: inferred → verified

Already settled — nothing to do
  • q-crocosmia-lucifer          plants.json `crocosmia` variety.confidence = verified   (folded 2026-07-14)
  • q-panicle-hydrangea-bloom    plants.json `hydrangea-panicle` bloom.confidence = verified (folded 2026-07-22)

Card is open but canon already settled — retire the card
  • (none)

Can't verify automatically — check by hand
  • q-white-mophead-annabelle    no _foldTarget; fold landed in the hydrangea roster (resolved 2026-07-14)
  • q-weed-stiltgrass            weeds.json `japanese-stiltgrass` — no auto-fold rule for weeds yet
```

Two smaller fixes belong in the same edit, both already logged as run-1 findings and never done:

- **Template by `_foldTarget`** — a bloom card currently prints *"lock the variety she
  confirmed"* (`fold_suggestion()`, line 141). Run-1 finding #3.
- **Render ET, not UTC** — `(ts)[:10]` shifts evening answers a day. Run-1 finding #4, and a
  standing global rule.

### The watermark (S3) — the one that can lose her input

Smallest safe fix: `fold-answer.py:198` should pass `--mark-reviewed-through <max ts of the
answers it actually folded>` instead of invoking a bare `--mark-reviewed` that stamps everything
in view. Likewise `--mark-reviewed` on its own should stamp only what it just listed as
actionable.

Durable fix, and the one I'd rather have: **once the punch-list derives from canon, the watermark
stops being load-bearing at all.** "Is this worth surfacing?" becomes "is its target unsettled?"
— a derived question — and `lastReviewedTs` demotes to a display nicety on the *already settled*
bucket. That's the same insight as everything else here, applied one layer down.

---

## 5. Where determinism does NOT belong

Explicit, because the whole point of automating the trigger is to protect the judgment.

| Do not automate | Why |
|---|---|
| **The ribbon's wording** | `CLAUDE.md`: *"Name what she actually gave, specifically — a generic 'thanks for your feedback' does not tell her she was heard."* A template can only produce the generic version, which is worse than nothing at the exact moment she's doubting herself. The check computes *that* she is owed a line and *what evidence* exists; Paul (or an agent drafting for his approval) writes the line. It reaches Mom → human-confirmed before it ships. |
| **Canon promotion** | Doctrine, unchanged. `fold-answer.py` stays per-edit approval-gated. **Never put `--yes` in a scheduled job.** |
| **Card wording** | The A3 "fix the ask" work is a design response to her stated fear of being wrong. That is the highest-value open item in this cycle and it is entirely human. Nothing here touches it. |
| **Attribution** | §3.4. Shared device; inventing certainty is the failure class the global rule already names. |
| **A "Not quite" correction** | An ID change is judgment. Unchanged. |
| **Retiring a stale-premised card** | The check should *propose* it; Paul confirms. Precedent: `check-data-inline.py --fix` is deliberately gated behind Paul confirming the drift is legit, because *the drift is a human signal that an addition is real.* Same logic here. |
| **The A1 gate re-cut** | Whether a Guru *question* counts as engagement is a product judgment (BACKLOG A1, open). Don't encode it in a script while it's undecided. |

The through-line: **derive the trigger, never the words; compute what's owed, never what to say.**

---

## 6. Ranked by leverage

| # | Item | Effort | Why here |
|---|---|---|---|
| **1** | **`tools/check-mom-ack.py` + `acknowledgedThrough` + the session-start line** | ~2h | Leg 3 is the cycle's stated purpose and has **zero** mechanism. Everything else in this list is a mechanism that's wrong; this one is missing. Includes the not-pushed check, which is free. |
| **2** | **Derive `read-mom-feedback.py`'s punch-list from canon; three buckets** | ~1h | Cheapest fix here and it already cost real money — a wrong claim in four artifacts. **Ship this one first chronologically** even though it ranks second by impact. Fold in the `_foldTarget` template + ET rendering while you're in the file. |
| **3** | **Scope the watermark to what was actually folded** | ~30m | The only path in the cycle that can *silently lose* an unfolded answer of hers. Small, but it's the one with a data-loss shape. |
| **4** | **Widen `mom-queue-watch.py` to "unacknowledged input," reusing #1** | ~30m | Explains the 8-day silence: the watcher was watching folds, and she gave input through three non-fold channels. Nearly free once #1 exists. |
| **5** | **`tools/momlib.py`** — shared `question_state()` + the `_get`/`_load` helpers | ~1.5h | Rule-of-three has fired (3 verbatim `_load` copies, 3 definitions of "pending"). Do it *while* doing #1–#4 so they land on one definition instead of adding a fourth. |
| **6** | **`harvest-questions.py`: derive `covered_ids` from the marker, not the artifact** | ~1h | Fixes run-1 finding #1 (stale-premised cards never retired) and unblocks re-harvest of entities whose draft Paul declined. Distinguish `declined` from `retired` — which needs S4 resolved first. |
| **7** | **Document the `active` overload; add `state` as a derived helper, not a schema migration** | ~20m | 16 questions. A status-enum migration is not worth it yet; a documented convention + one helper is. Revisit at ~40. |

### What I would NOT build

- **A generated ribbon message.** Violates the doctrine and would produce worse copy than
  silence at the moment it matters most.
- **A Worker-side "ack API" that computes the ribbon at page load.** The current bake-at-build
  design is *correct* — it works on an unpaired device, needs no token, and reads none of her
  data on her own surface. Don't touch it. Add the clock; keep the mechanism.
- **A normalized Mom-activity event store / input bus.** Dozens of records a month. Four `GET`s
  and a `max()` is the right size. `[[Storage mirrors existing shape; analysis lives in tools/]]`.
- **A `mom-ack.json` source file.** Parallel copies of a one-object constant with no runtime
  consumer. §3.1.
- **A status-enum migration on `questions.json`.** Tempting, genuinely cleaner, not worth it at
  n=16. Item 7 is the 20-minute version of the same value.
- **Unit tests for these scripts.** Not Paul's posture and not proportionate. The one testing
  spend I'd consider is a single Playwright assertion that the ribbon renders with the current
  `acknowledgedThrough` — and even that ranks below all seven items above.
- **A launchd job for the ribbon check.** It belongs in the session-start block Paul already
  reads. A fourth notification channel dilutes the three that exist.
- **Any "auto-fix" flag on the ack check.** The gap between "the ribbon is stale" and "here are
  the words" is exactly where the human belongs.

---

## 7. Nits (do them in passing, don't schedule them)

- `track("momack_shown", { questionId: MOM_ACK_DATA.questionId })` (`viewer.html:9227`) — with
  `questionId` now `null`, the metric has no discriminator. Track `acknowledgedThrough` instead;
  that's how you'd ever learn whether a *fresh* ribbon changes her behavior versus a stale one.
- `fold_suggestion()` builds a filename as `f"{kind}s.json"`. Works for plant/weed/zone by luck.
  A two-entry dict is clearer and fails loudly on an unknown type.
- `mom-queue-watch.py` overwrites `pingedAnswerIds` with `answered_open` (S7) — the memory
  forgets retired cards. Worst case is a duplicate ping; note it, don't chase it.

---

## 8. Principles to propose (NOT yet added — Paul's confirmation required)

**A. Promote to `cross-project/` — "A reassurance surface needs a staleness alarm, not a policy"**
*Statement:* Any surface whose job is to tell a person they were heard must carry a machine-readable
"what this covers" marker and a check that fails when new input arrives past it. A written rule to
refresh it is not a mechanism.
*Why:* Fernwood's ack ribbon went 8 days stale during the exact week the user doubted whether her
input mattered. The 7/22 design tied refresh to the fold step; when Paul corrected that in
`CLAUDE.md`, the correction was still prose. The surfaces whose value is *emotional* are the ones
where staleness is invisible to the builder and maximally costly to the reader.
*Avoid:* A refresh rule with no check. A freshness field nothing reads (`answeredOn`).
Auto-generating the reassurance text to guarantee freshness — that trades staleness for
meaninglessness.

**B. Add to `fernwood.md` — "Derive the punch-list from canon, not from the record of answers"**
*Statement:* In the Mom loop, "what's waiting for you" is computed from the live state of the
target (canon confidence, card resolution), never from the existence of an answer record.
*Why:* This is `[[Derive a gate's pending-count; don't list it]]` applied here. It had already been
promoted cross-project on 2026-07-01 and did not reach this loop; the result was a phantom to-do
that propagated into the backlog, a researcher brief, and three agent reports before Paul's
"check current canon confidence" step caught it.
*Avoid:* A punch-list built from a feed query alone. Transcribing a derived count into prose
without naming the command that derives it.

**C. Candidate (watch for a second occurrence) — "A cross-project principle isn't adopted until a
check exists in each repo that needs it"**
Both 7/26 failures were covered by principles already in the library. The library records the
*lesson*; only a check enforces it. Worth considering a periodic sweep: for each promoted
principle, which repos have the mechanism? Flagging as a candidate rather than proposing it —
it's a doctrine-process claim, not an engineering one, and it may belong to the `/team-audit`
flow instead.

---

## 9. Open questions for Paul

1. **Threshold.** Should `check-mom-ack.py` exit 1 on *any* uncovered input, or after a grace
   period? I've specced "any," because grace periods are knobs nobody tunes and the
   `--acknowledged-through` stamp clears a false alarm in one command. If it cries wolf on your
   own test taps within a week, that's the signal to add a threshold.
2. **The off-system ledger.** Is `.private/mom-input-log.json` a thing you'd actually keep
   current, or does the text channel just get manually stamped via `--acknowledged-through` when
   you refresh the ribbon? The second is less honest (nothing records that a channel fired) but
   has zero upkeep. Your call — I'd start with the ledger and kill it if it goes unwritten twice.
3. **S4.** Do you want `active:false` split into `draft` / `retired` now, or is the documented
   `resolvedAt` discriminator enough until questions.json grows? I've ranked it 7th, i.e. "not
   now," but it's the prerequisite for item 6.
