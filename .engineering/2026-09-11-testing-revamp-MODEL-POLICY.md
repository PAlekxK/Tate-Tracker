# THE MODEL POLICY — one tier per act in the testing cycle · lap 9 · row T

- row: T (the testing architecture) — the **MODEL POLICY** section required by `handoff/handoff-testing-revamp.md` §1c
- seat: **ai-advisor (consult mode)** — owns the tiering recommendation. `engineering-partner` wires where the tier is set. **Paul rules the tier per act.**
- objective: O5 (the loop itself)
- stage: recommendation · `ready: agent-proposed — Paul reads and rules`
- stamped: **2026-09-11 09:45:05 -0400** from `date` · **HEAD `7958a620`** from `git rev-parse --short HEAD`
  ⚠️ The brief was issued at `394c18d4`; HEAD moved twice while this was written. Every symbol below is cited by NAME, never by line.
- read-only: nothing under `tools/` or `~/.claude/agents/` was edited. No tool was run that writes.
- ⛔ **No synthetic's typed text is quoted anywhere in this file.** Counts, ids, file names and pixel dimensions only.

> ### The ask, verbatim `[paul-stated 2026-09-11 ~7:25 AM ET, brief §1c]`
> *"One thing we should definitely have within this is some sense of what's the right model to use for
> everything, so that we control that. Can we use a slightly dumber model for just a walk-through, but
> more powerful models for the reading? That would be a good layer to lay in here."*

---

## 0 · THE ANSWER FIRST, and it inverts the question

**The walk-through already uses no model at all.** Six harness tools drive, capture and gate the whole
battery with zero model calls (readback §1, by grep: `journey-walk` · `walk-brief` · `walk-capture` ·
`release-gate` · `walk-integrity` · `journey-view`). So *"a slightly dumber model for the walk-through"*
has nothing to buy — the drive is already free, and it must stay free for reasons that are doctrinal,
not economic (§4).

**Three findings, in the order that changes what row T builds:**

1. ⭐⭐ **The reading tier is not set by anyone. It is inherited from `~/.claude/settings.json`, a file
   outside this repo, which today reads `"model": "claude-fable-5-1[1m]"`.** The five reading lenses are
   ad-hoc subagent spawns by the driving session, so they run at whatever that session runs at. **Fernwood's
   release evidence is produced at a tier set by a global preference that changes for unrelated reasons and
   that no Fernwood check reads.** That is the defect. The tier question is downstream of it.
2. ⭐ **The inherited tier is DEARER than the declared one, not cheaper.** Fable 5.1 is $10/$50 per MTok;
   Opus 5 — what every agent file under `~/.claude/agents/*.md` that sets a tier sets — is $5/$25
   ([pricing](https://platform.claude.com/docs/en/about-claude/pricing), fetched 2026-09-11). So the reads
   have been running at **2× the price of the repo's own declared tier, by accident.** Nobody chose this
   and nobody could have noticed.
3. ⭐⭐ **The money is noise and the wall clock is the constraint.** Order-of-magnitude (§5): the entire
   reading half of a lap costs **~$20, band $10–$60**. The most aggressive defensible downgrade saves
   **~$16 a lap.** The same reading half costs **27 minutes median per report** (audit §8b) and produced
   the one product defect no deterministic reader in this repo could reach (audit §8a). **A tier policy
   argued on dollars would be optimising the wrong axis by two orders of magnitude.**

**So the recommendation is not "downgrade the reads." It is: DECLARE every tier, downgrade only the acts
that are CLASSIFICATION, and build most of the new checks with no model at all.**

---

## 1 · THE POLICY TABLE — one row per act

**Column 3 is the load-bearing one.** An act that needs *nothing* gets no model however cheap models get;
an act that needs *judgement across screens* gets the top tier however dear they get. Cost breaks ties
between acts that need the same thing — it never moves an act between rows of column 3.

| # | act | tier | what the act needs from a model | reasoning |
|---|---|---|---|---|
| 1 | **DRIVE** — `journey-walk.py` runs a declared action list in a browser | ⛔ **NONE** | nothing | Measured: zero model calls in the six harness tools. A model choosing what to type would make the transcript unreproducible AND would be a model **writing into a real store** — see §4. **Permanently none, by doctrine, not by cost.** |
| 2 | **CAPTURE** — `transcript.json`, `capture.json`, the 38 PNGs per run | ⛔ **NONE** | nothing | *Capture stays deterministic and AI-free* (CLAUDE.md, standing). `walk-brief.py`'s own docstring already forbids the summarising version: *"A tool that summarised or characterised the screens would be doing the reader's job and contaminating the very thing it is staging."* **Permanently none.** |
| 3 | **SEAT BRIEF** — `walk-brief.py` renders the screens in order | ⛔ **NONE** | nothing | Same clause. It ORDERS and RENDERS; it never judges. Measured this morning: 35,290 characters (~8.8k tokens) for one 19-stop run. |
| 4 | **READ — per lens** (5 lenses × the declared journeys = 15 cells at lap 7's shape) | ⭐ **TOP TIER — recommend `claude-opus-5`, DECLARED** (today: inherited Fable 5.1, undeclared) | **judgement across screens** | This is the act that found the receipt rendering stored ids where the person's words belong (audit §8a, on `owner/2026-09-11T083409/R01-arrive.fold.png`). The transcript was **clean** — the ids are correct. Seeing that defect requires holding three things at once: what the walker typed, what the frame shows, and that those are different *registers of language*. That is not classification. ⚠️ Recommending Opus 5 over the inherited Fable 5.1 is a **cost-and-declaration** move (half the price, and it is the tier every agent file already names), **not a capability claim** — I have no evidence ranking the two. §2's A/B is what settles it. |
| 5 | **CONTENT READ** — content-steward over all counted runs | ⭐ **TOP TIER — `claude-opus-5`** (already declared, `~/.claude/agents/content-steward.md` frontmatter `model: opus`) | **judgement across screens + voice** | ⭐ **The only act in the cycle whose tier lives in a file today.** It is also the act that turned §8a into a STOP. Keep it, cite it as the precedent for §3, change nothing. |
| 6 | **SYNTHESIS a — the CONSOLIDATION of the non-blocking channel** (T-i; 63 bullets across 15 reports, 6 relayed by hand, **0 mechanical readers** — audit §8d) | **`claude-sonnet-5`** | **classification + grouping** — cluster near-duplicate bullets, key them to a journey/stop, propose rows | A **new act with no incumbent**, so it can be born cheap with its falsifier attached. ⛔ **It groups and proposes; it never DISPOSES.** Disposition stays the lap's opening gate sweep (act · fold · snooze · kill), Paul's. A consolidator that could kill a bullet would be a scorer, which the audit's do-not-build list forbids. |
| 7 | **SYNTHESIS b — the beat-10 write-up / chronicle entry** | **the session's own tier — NOT policy-controlled; DECLARED so nobody is surprised** | judgement | This is the driving window, a human-in-the-loop session, not a spawned act. Its tier is `~/.claude/settings.json`. **Say so on the policy's face** rather than pretending the policy covers it — an overstated boundary reads as a promise (CLAUDE.md). |
| 8 | **GATE** — `release-gate.py`, `walk-integrity.py`, `post-deploy.py`, the headless PAGEERROR load, `check-estate-neutral` | ⛔ **NONE — and this is a rule, not a default** | nothing | Measured zero today. ⭐ **A model may never set the gate's exit code.** The release condition must be reproducible from the artifacts by a second reader at another time; a judgement is not. This is the tool-boundary principle: *prompts shape behaviour, boundaries enforce it.* |
| 9 | **STATIC CHECK — M7, every `href="#"` control changes the visible region** (S11; from Paul's own walk, W2/W5) | ⛔ **NONE** | nothing | A DOM/AST read, zero browser. It is the cheapest instrument that could have found two of Paul's six findings. **Spending a model here would be strictly worse**: slower, non-deterministic, and unreproducible at a later sha. |
| 10 | **STATIC CHECK — the identical-failure read** (M4/S10: N of N lenses fail the same assertion ⇒ SUSPECT HARNESS, stop) | ⛔ **NONE** | nothing | ⚠️ **This one LOOKS like a model job and is not.** Once gate ① is keyed on **(journey, lens)** (Q2, ruled), "did every lens fail the identical assertion" is string equality over transcripts. It is computable the moment S1 lands. Do not spend a model on arithmetic. |
| 11 | **STATIC CHECK — the route classifier** (S5: changed files → Worker routes → journeys, for impact-scoped re-runs) | ⛔⛔ **NONE — the most dangerous downgrade candidate in the cycle** | nothing | ⭐ **This classifier decides what NOT to test.** A model here would silently shrink coverage in a way no artifact records. It must be a declared per-journey route list diffed against the routes a change touches, with page bytes as the second proof — **and it must fail CLOSED: a changed file the classifier cannot classify declares FULL COVERAGE.** Same doctrine as `household-fixtures.py --teardown`: *an unprovable row is a STOP, not a SKIP.* |
| 12 | **FRAME READ — the build lane's shake-out** ("is this build alive / is the control there", today done inline by the driving session at whatever tier it is running) | **`claude-haiku-4-5-20251001`** — and make it an ACT, not an inline habit | **classification only** — presence/absence against a fixed question list | The cheapest tier that answers *did the page render · is there a visible error · does each named control appear*. ⛔ **It reports presence and absence and is forbidden to make product judgements** — the moment it opines on whether a screen is *good*, it is doing act 4's job at act 12's tier, which is the one genuinely bad outcome available here. Falsifier is a real historical build: §2c. |
| 13 | **FIXTURES / TELEMETRY READERS** — `household-fixtures.py`, `walk-fixtures.py`, `read-glance-order.py`, `check-telemetry.py`, `watch-door.py` | ⛔ **NONE** | nothing | Measured none. No case for one. Listed so the table is a roster and not a sample. |

### 1a · What the table is NOT evidence about — stated on its own face
Per CLAUDE.md's *"a control can be entirely correct and still not cover the thing you rely on it for"*:
this policy assigns a tier to an act. **It says nothing about whether the act is worth doing** (that is the
audit's cost-per-finding question), **nothing about whether a lens is the right lens** (`seat-portfolio.py`),
and **nothing about whether the reading happens at the right time** (S12, lens cadence — unruled, Paul's).
A lap could hold this policy perfectly and still read the wrong walks at the wrong sha.

---

## 2 · A FALSIFIER PER DOWNGRADE — the minimum A/B that does not grow a second harness

⚠️ **Stated first, because the readback (§4.11) already flagged it and it must not be lost:** no run in the
corpus has ever been read by more than one tier. **Every tier in §1 ships UNFALSIFIED until the A/B runs.**
The table is a *declaration to be tested*, not a settled ruling. Say that in the plan, on its face.

Three instruments, cheapest first. Together they are ~1 extra read per lap and zero extra browser minutes.

### 2a · THE FROZEN REGRESSION CORPUS — offline, no lap required, run any time
Three findings that are **known-true, known-hard, and each invisible to the drive axis** (analysis §2b):

| # | fixture | the finding a tier must produce |
|---|---|---|
| **F-a** ⭐ | `owner/2026-09-11T083409/R01-arrive.fold.png` + that run's `walk-brief.py` output (J3) | the receipt is showing **stored ids** where the person's own words belong |
| **F-b** | the J8 account-page frame + brief from any of the 15 counted runs at `87c7aae` | the **username renders as a dash** on the one walk where the person needs it |
| **F-c** | the recovery-path frames from `wide-eyed` / `mom` at `87c7aae` | the block still **promises a hand reset after a successful sign-in** |

**The rule, and it is absolute on F-a:** a candidate READ tier is handed the identical brief and frames, with
the identical seat instructions, and must report the finding. **A tier that misses F-a fails — no averaging,
no score.** F-a is the entire evidentiary case for having five readers at all (audit §8a); a tier that cannot
reach it has removed the reason the act exists.
⛔ Cost: three reads, ~$1–$4 total, **no walk, no browser, no lap.** Run it before proposing any tier change.
⚠️ Its own limitation, stated: it tests the FLOOR (can this tier see a known defect), never the CEILING
(would it have found something the incumbent missed). §2b is what tests the ceiling.

### 2b · THE SHADOW READ — one walk per lap, read twice, findings diffed
- **Once per lap, at the certified candidate, ONE already-completed run** — declared in the beat-6 cell list,
  preferring the run whose journey changed most — **is read a SECOND time by the alternate tier.**
- **Identical inputs, guaranteed:** the same `walk-brief.py` output, the same frames, the same seat brief.
  The artifacts are immutable at a sha, so this costs **zero browser minutes and zero new walks** — it is not
  a second harness, which the audit's do-not-build list forbids by name.
- **Diff on FINDINGS, never on prose.** Key each finding by the triple **(journey, stop, claim)**. Output three
  buckets: `both · only A · only B`. Prose style is not evidence; a cheaper tier that writes worse sentences and
  finds the same defects has not failed.
- **Ruling bar:** a downgrade is permitted only if the cheaper tier's **blocking** findings are a superset-or-equal
  of the dearer tier's **across two laps**. One lap is an anecdote — the same n=1 discipline this project applies
  to Mom's engagement.
- ⛔⛔ **THE SHADOW READ NEVER GATES THE RELEASE.** It is evidence about the policy, not a clause in gate ①.
  A tier experiment that can block a ship is how an experiment becomes a ceremony.
- **Filing:** `.practice/tier-ab/<sha>-<journey>-<lensA>-vs-<lensB>.md`, one result line in the lap's `CYCLE-LOG`.
  Two laps of these is the evidence Paul rules on.
- **Cost:** one extra read (~$0.3–$1.3), run in parallel with the fifteen → **~0 added wall time.**

### 2c · THE FRAME-READ FALSIFIER — and it has a real historical fixture
The act-12 downgrade to Haiku is falsified against **the 2026-09-06 corpse build** already recorded in
CLAUDE.md: a patch left four unterminated strings, a top-level parse error killed the script, the page rendered
as static markup, and **four seats walked it.** Handed those frames, a Haiku frame read must report *static
markup / the named controls are absent*. If it reports the build as alive, the tier is wrong for the act.
⚠️ Note what this falsifier does NOT cover: `pages-deploy.py` already refuses on PAGEERROR, so the frame read is
not the only guard against that class — it is the guard for the class where the page parses and renders wrongly.

### 2d · One experimental-design constraint, and it is easy to get wrong
⛔ **Do not run a mixed-tier lens roster** (e.g. two lenses at Opus, three at Sonnet, in one lap). It confounds
lens with tier: when the cheap lens finds less you cannot tell whether the **posture** was thin or the **tier**
was. **Uniform tier across lenses within a lap; vary the tier across laps or in the shadow read.** This costs
nothing and it is the difference between the A/B producing a reading and producing an argument.

---

## 3 · WHERE A LENS'S TIER IS DECLARED — recommendation, and why it is enforceable

The readback (§4.12) is right that this precedes the tiering. Four candidates were named. My recommendation is
a **hybrid, split by whether the act is STABLE or CHURNING** — because only one of the four mechanisms actually
binds at spawn time.

### ✅ RECOMMENDED

**(A) For the STABLE, FEW acts — the content read (5), the consolidation (6), the frame read (12): an agent
file's `model:` frontmatter under `~/.claude/agents/`.** This is the **only mechanism in the stack that is
binding at spawn**, and the repo already relies on it: `content-steward.md` carries `model: opus` today and is
the one act in the cycle whose tier is not an accident. Two new agent files (consolidator, frame-reader) is the
whole of the wiring. ⚠️ **Those files live in Paul's GLOBAL stack, not this repo — so minting them is his call,
not row T's.**

**(B) For the CHURNING lens roster — a per-lens data file, `cycle/release/lenses.json`, carrying `tier` per
lens; plus the tier RECORDED IN THE RUN'S OWN RECORD, and `release-gate.py` refusing to count a read whose
recorded tier is absent or does not match the declaration.**

Why a data file and not agent files for the lenses: Q3 ruled a lens is a **reading posture only**, the roster is
explicitly unsettled (`seat-portfolio.py`: `map-points` and `other` uncovered, `handover` flagged as a journey
wearing a lens's clothes), and minting a global agent per lens would push a churning, Fernwood-specific roster
into Paul's global stack, where `check-release-docs.py` cannot see it.

Why the gate clause is the load-bearing half: it converts *remembered* into *measured*, and it is the shape this
repo already trusts — `check-arrival-dispositions.py`'s rule that **a disposition is keyed to the record, so
nothing but looking at that record can supply it.** It also makes the §2 A/B auditable retroactively, which it
needs anyway: a shadow read is worthless if you cannot prove which tier wrote which report.

⚠️ **THE HONEST LIMIT, stated rather than implied.** Nothing can *force* a driving session to spawn a lens at the
declared tier — the Task spawn takes the model from an agent file or inherits the session's. **(B) is therefore a
DETECTOR, not a preventer:** the gate refuses to *count* a mismatched or undeclared read. That is weaker than
`guard-destructive.py` and stronger than a sentence in a document, and the plan must say so in those words. An
overstated boundary is worse than an unstated one.

### ⛔ REJECTED, with the reason

| option | why not |
|---|---|
| **the seat brief header** (`walk-brief.py` writes it) | ⭐ **Wrong direction of enforcement, and it is the exact failure this stack has already paid for.** The brief is read by a seat that **has already been spawned at some tier**. A line saying *"you should be Opus"* is a behavioural instruction to a model that already exists — a prompt where a boundary is needed. It also breaks `walk-brief.py`'s own rule that it renders and never instructs. |
| **the agents' frontmatter, for the LENSES** | Binding, but the wrong home for a churning Fernwood roster (above). Correct for the three stable acts — hence the split. |
| **CYCLE-MAP.md** | Prose. `check-release-docs.py` exists **because** CYCLE-MAP and the code diverged, and it found two drifts on its first live run. The CYCLE-MAP should **cite** the tier file, never restate it. |
| **leaving it inherited** (today) | The status quo means Fernwood's release evidence tier is set by `~/.claude/settings.json` — outside the repo, changed for unrelated reasons, read by no Fernwood check. **That is the defect this section exists to close.** |

---

## 4 · THE BOUNDARY WITH THE AI-BOUNDARY DOCTRINE

✅ **CONFIRMED: this policy changes nothing about the AI boundary.** DRIVE and CAPTURE are assigned **NONE**,
which is the answer the boundary already requires — reached here independently, from what the acts need. Rows
1, 2 and 3 of §1 are **not cost decisions and may not be revisited on cost.**

**Where a "cheaper walk-through model" would VIOLATE it, concretely — the three temptations, named so they can
be refused by name:**

1. ⛔⛔ **A model DRIVING the walk** (choosing what to type, navigating freely instead of running a declared
   action list). The walker types into a **real store**: `est-qa0001` holds 201 account rows — 174 fixtures and
   **Paul's own real accounts mixed in** — and `check-canon-scope.py` measured another person's home address in
   that same namespace. A model choosing what to type is **a model writing to an estate's record**. That is
   forbidden creep mode (2) (AI auto-folding to canon) in its harness costume, and it destroys the walk's
   reproducibility at the same time. **The drive is a declared action list, permanently.**
2. ⛔ **A model on CAPTURE — "cleaning", normalising or summarising the transcript or the frames** before a
   reader meets them. Forbidden creep mode (1) (*AI cleaning/classifying at capture — store verbatim*), and
   `walk-brief.py`'s docstring already forbids the summarising version by name.
3. ⛔ **A model as the GATE's verdict.** Not an AI-boundary clause strictly, but the same enforcement principle:
   a release condition must be deterministic and re-derivable. Also the *deterministic things need a non-AI door*
   rule — **if the only way to learn whether the release passed is to ask a model, this is broken.**

⚠️ **And the clause that is NOT engaged today but will be the moment someone reaches for it.** The reading seats
read **synthetic walkers**, so the quarantine and ingress clauses are not in play. **This policy does not
authorize a reading seat over a REAL household's session, walk or words at any tier.** The moment a real
member's screens were staged for a reading seat, the ingress clause binds (*an agent may read only what was
routed to the project; the administrator's eyes sit between the model and the estate's people, both
directions*), and that is a separate ruling of Paul's — never a consequence of a tier table.

---

## 5 · COST — order of magnitude, marked INFERRED

⚠️ **INFERRED. Every figure below is a band.** Measured inputs are marked ✅; everything else is a modelled
assumption stated so it can be corrected. **No API usage record for these reads exists** — that is itself a
finding, and the cheapest fix is §3(B)'s recorded tier field.

**Prices** ([Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), fetched 2026-09-11,
per MTok input/output): **Fable 5.1** $10/$50 (cache read $0.25) · **Opus 5** $5/$25 (cache read $0.50) ·
**Sonnet 5** $2/$10 (cache read $0.20) · **Haiku 4.5** $1/$5 (cache read $0.10).

**Measured anchors for ONE read:**
- ✅ `walk-brief.py` output for a 19-stop run: **35,290 characters ≈ 8.8k tokens**
- ✅ **38 PNGs per run** (19 stops × fold + full); a fold is **1242×2544 px** → after the API's longest-side
  resize ≈ **1,600 image tokens each** → **~30k tokens** if a seat views every fold
- ✅ `REPORT.md` at `87c7aae`: **6.1–6.7 kB ≈ 1.5–1.7k tokens** of final prose
- *inferred*: ~50k billed base/write input, ~300k cache-read input across the seat's turns, ~15k total output

| act | today (implicit) | recommended | note |
|---|---|---|---|
| **15 lens reads** | **≈ $20** (Fable 5.1, inherited) | **≈ $12** (Opus 5, declared) | the whole reading half |
| **1 content read** | ≈ $3 (Opus 5, declared) | ≈ $3 | unchanged |
| **consolidation** | $0 — *the act does not exist; 63 bullets, 0 readers* | ≈ $0.2 (Sonnet 5) | a **new** cost that buys a channel that is currently decorative |
| **frame reads** | ≈ $1, inside the driving session | ≈ $0.3 (Haiku 4.5) | |
| **drive · capture · gate · the 3 static checks** | **$0** | **$0** | and permanently so |
| **per lap** | **≈ $24** · band **$10–$60** | **≈ $15** · band **$6–$40** | |
| *floor, if the reads went to Sonnet 5* | — | *≈ $8/lap* | **the most aggressive defensible cut saves ~$16 a lap** |

⭐⭐ **THE DECISIVE NUMBER, and it is the one Paul should rule on.** At Fernwood's cadence, the deepest available
downgrade of the READ act saves on the order of **tens of dollars a month**, against a risk of losing the §8a
class of finding — the only product defect of lap 7 that **no deterministic reader in this repo could reach**,
found by a reader looking at one frame. **That trade is not close.** The reading is where the money should go.

⭐ **Where the real cost is, and it is not tokens.** Audit §8b: reading wall time **median 27 minutes** per
report, 15 reports, ~25 minutes of wall clock in parallel — against **51.9 browser-minutes for 45 walks**.
The three levers that actually shorten a lap are **none of them tier changes**:
1. **Stop reading nothing.** 23 of 45 walks were never read; 22 permanently (audit §8c). The waste is unread
   walks, not dear reads.
2. **Make convergence computable.** The username dash was reported **5 times to learn one thing** (analysis §2b).
   Under the (journey, lens) unit that is a count, not five paragraphs a human de-duplicates.
3. **Declare the tier** so it stops being an inherited accident — which, today, also halves the read's price as
   a side effect.

---

## 6 · WHAT PAUL MUST RULE

**The tier per act is his. The falsifier design is mine and is above.**

| # | the ruling | my recommendation | what it costs to be wrong |
|---|---|---|---|
| **M-1** | **The READ tier**: declared `claude-opus-5`, or left inherited (Fable 5.1), or cut to Sonnet 5 | **declare Opus 5** — half the current price, the tier every agent file already names, no capability claim either way until §2 runs | a cut to Sonnet risks the §8a class for ~$8/lap |
| **M-2** | **May the SHADOW READ run** (§2b) — one extra read per lap, filed under `.practice/tier-ab/`, **never gating** | **yes** — it is the only thing that turns this table from a declaration into a ruling; ~$1 and ~0 wall time | without it every tier here stays unfalsified, indefinitely |
| **M-3** | **Where the tier is declared** (§3): agent frontmatter for the 3 stable acts + `cycle/release/lenses.json` + a gate clause for the churning lenses | **the hybrid**, and accept that (B) is a **detector, not a preventer** | the status quo leaves release evidence keyed to a file in `~/.claude/` |
| **M-4** | **Mixed-tier lens roster within a lap** | ⛔ **no** — uniform within a lap; vary across laps (§2d) | a confounded A/B produces an argument, not a reading |
| **M-5** | **Two new agent files in his GLOBAL stack** — a consolidator (Sonnet 5) and a frame-reader (Haiku 4.5) | **yes**, because frontmatter is the only mechanism that binds at spawn | otherwise both acts inherit, and the policy has two more holes |
| **M-6** | **The consolidation act is born at Sonnet 5** and **never disposes** — groups and proposes only | **yes** | a consolidator that could kill a bullet is the scorer the audit forbids |
| **M-7** | **Rows 1 · 2 · 8 (DRIVE · CAPTURE · GATE) are NONE by doctrine and may not be revisited on cost** — a standing clause, not a lap decision | **yes** | §4 names exactly how a cheap "walk-through model" would breach the AI boundary |
| **M-8** | ⚠️ **Accept that this policy ships UNFALSIFIED** and prints that on its own face until two laps of §2 evidence exist | **yes** | a tier table presented as settled is the *control-that-does-not-cover-your-question* failure, applied to itself |

**Not Paul's, and named so nobody waits on him:** §2's A/B design · the finding-triple diff key · the frozen
corpus's three fixtures · the fail-closed rule on the route classifier · the refusal of the seat-brief header
as a declaration site.

---

## 7 · WHAT THIS RECOMMENDATION DID NOT READ

The five lens REPORT.md files in full (findings sections and counts only, via the audit and the analysis) ·
any API usage or billing record (**none exists for these reads** — §5's per-read shape is modelled, not
metered) · `journey-walk.py`'s action-list bodies · how many of the 19 folds a reading seat actually views
(the 30k image-token figure is a **ceiling**, not a measurement) · any capability comparison between Fable 5.1
and Opus 5 (**none was available; §2 is how it gets made**) · lap 8, which has not opened.
