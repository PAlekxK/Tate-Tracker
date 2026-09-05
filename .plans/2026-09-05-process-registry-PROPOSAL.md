# PROCESS REGISTRY — every recurring step, who performs it, and how automation candidates SURFACE · PROPOSAL
- row: process (portfolio-level; see §6 — **this file is written in Tate-Tracker because that is where the seat was standing. The thing it proposes does not belong here.**)
- objective: O5
- class: engine · must-not-diverge (a second registry of "who does what" is the defect this exists to prevent)
- seats: practice-steward (this file)
        `/team-audit` → deferred: §5's reading site is the meta-stack cycle's own beat 1; that cycle owns the instrument
        engineering-partner → deferred: nothing is built until Paul rules
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- ready: agent-proposed 2026-09-05 — **Paul rules**
- stage: draft

> **Assignment** `[paul-stated 2026-09-05 ~2:20 AM ET]`: *"Our process — we should really be keeping a
> registry of all the processes and steps, and over time we can identify all the opportunities to
> automate things. You know, as we scale, that'll be especially important."*
>
> **Method only. This file ranks no step and recommends no automation.** §4 says what would have to be
> measured for a ranking to be *possible*. The ranking is his.

---

## 1 · ⭐ THE FINDING THAT SHOULD SET THE SCOPE — most of this already exists, and it is barely used

`~/.claude/handoff/doors.json` `[paul-ruled 2026-08-31]` is a registry of recurring surfaces, and it
already carries the exact axis Paul asked for tonight, under the key **`checkable_by`**:

> `script` = a cron/tool can read it with no one present · `agent` = a Claude session can check it on
> request · `human` = only Paul.

Three values. **Paul's "Paul · agent · deterministic tool" is the same axis, already ratified, already
in a file, already read by a surface (`comms.py`).** And its note fields already carry current-state,
target-state and blocker in prose — *"Agent-checkable today via the session's Gmail MCP; script-checkable
once the gmail.readonly consent lands"* — which is exactly the address-validation row's shape.

⛔ **And its `_doc` line contains the whole rot-resistance design, already ruled:**
> *"CONFIG, NO DATES: attest state lives in handoff/door-checks.json (written only by tools/checked.py)."*

**Measured 2026-09-05, and this is the number the proposal has to survive:**

| | count |
|---|---|
| doors registered | **12** (6 `human` · 4 `agent` · 2 `script`) |
| doors with **any** attest in `door-checks.json` | **1** (`door:gmail-gkw`, 2026-09-03) |

**The attest mechanism is correct, ratified, five days old — and has been used once across six eligible
doors.** Any registry whose evidence depends on Paul remembering to record a performance inherits that
rate. **This is the single fact that should shape the design**, and §3 is built around it.

---

## 2 · WHAT AN ENTRY IS — a step's IDENTITY and performer class. Never its state.

```jsonc
"step:address-standardise": {
  "label": "standardise a captured address to the postal-authority form",
  "scope": ["fernwood", "estate-engine"],        // steps span projects; that IS the scale signal
  "performed_by": "human",                       // doors.json's `checkable_by` values, verbatim
  "automatable": "script — blocked: USPS business registration (CRID/MID); apis.usps.com answers 401, not 404",
  "evidence": "type-C · attest",                 // §3
  "note": "⛔ SUGGEST, never decide: her typed words stay the record; the lookup degrades open."
}
```

Five fields and a note. **No dates, no counts, no status.** A config row with no state cannot rot in the
dangerous direction — it can only be *incomplete*, which is a visible and much safer failure than a
status line that reads current while the world moved.

⭐ **`automatable` must have a legal value `never — <reason>`, and this is not a nicety.** Test it on the
cascade's gate 2: *Paul walks the build in lab, his own profile.* That is a recurring manual step and it
must **never** be automated — it is the AI boundary's own requirement, and Paul's own doctrine puts the
gate on the irreversible act. **A registry that can only point toward automation is a ratchet whose
end state is removing Paul from his own gates.** `never` is what stops it being one.

---

## 3 · ⭐ WHAT EMITS THE EVIDENCE — three types, and only one of them costs Paul anything

The rot-resistant move is not "log every step." It is to notice that **most steps already record
themselves, and the ones that do not are a small, boundable set.**

| type | the step's completion… | derivable from | cost to Paul |
|---|---|---|---|
| **A · self-recording** | changes a tracked artifact — a commit, a `- stage-note:`, a fold, a canon edit | git, `.plans/`, cycle logs | **zero** |
| **B · blocking** | gates something that records its own waiting — a plan at `stage: qa`, a `waiting_on` row in the anchor, an `ask-cycle.py` exit-3 refusal | `focus.py`, `demand.py`, `inbox-refusals.jsonl` | **zero** — the *blocked thing* does the recording |
| **C · silent** | changes nothing any tool reads — check the paper mail; standardise an address by hand | ⛔ **nothing. Only an attest.** | one act, per performance |

**Type B is the design's centre of gravity, and it is `demand.py`'s exact mechanism reused rather than
reinvented.** Its evidence is *"captured by the tool that refused, at the moment of refusal"* — nobody
has to remember. The same asymmetry applies here: **a manual step that blocks something is free to
measure; a manual step that blocks nothing is the one that rots silently.**

⚠️ **Address validation is Type C today, and that is precisely why the BACKLOG row's warning is right.**
The address lands in `est-e6696a`, is perfectly usable un-standardised, and blocks nothing — so no
artifact anywhere gets older, redder or louder while it goes unperformed. *Capture is not a loop.*

⛔ **Therefore the registry may not be built attest-first.** §1's measurement says an attest-first
registry would report ~1 performance in 6. Build it **A and B first**, where the evidence already
exists, and let Type C be the small declared remainder — each one named, each one carrying the reason
no machine can see it. **A Type-C step with no attest reads `unobserved`, never `clean`.** That
tri-state is already this corpus's discipline (`neglect-sweep.py`: `clean` / `fired` / `dark`), and
`unobserved` is never counted as healthy.

---

## 4 · THE RANKING AXIS — and an honest statement that half of it does not exist

The brief is right that frequency alone is wrong. Decomposed by what is actually obtainable:

| axis | derivable today? | from what |
|---|---|---|
| **frequency** | ✅ yes | count of performance records |
| **latency-owed→done** | ✅ yes, for Type B | the blocked artifact's own age; this is `demand.py`'s *"HOW LONG it has been trying"* |
| **duration / effort per run** | ⛔ **no. No cost data exists anywhere in this corpus.** Nothing times a human step | — |
| **error-proneness** | ⚠️ partial, n≈0 | rework — the same object handled twice |
| **blocker** | declared, not derived | the entry's `automatable` field |

> ### ⭐ RECOMMENDATION ON THE AXIS: rank on nothing.
> **Publish frequency, latency and the blocker; let Paul rank.** Two reasons, and neither is deference
> for its own sake. (a) A composite score built on one real axis and one absent one would be
> **precision manufactured out of a missing measurement** — the corpus's most-repeated failure shape.
> (b) Ranking work by value is outside this seat by charter.
>
> ⚠️ **And do not collect duration by asking him to time himself.** That is a standing tax on the
> scarcest thing in the portfolio, levied to feed a ranking he can produce by looking at the list.
>
> **Falsifier:** if, across the first ten steps he picks to automate, his picks correlate with neither
> frequency nor latency, then the two derivable axes are the wrong ones — collect what he actually
> used and replace them.

---

## 5 · WHERE IT IS READ — two surfaces, both existing, and they must NOT be merged

⭐ **This is the crux the brief named, and the answer is that "owed" and "automation candidate" are
different questions with different clocks. Merging them is what would produce the nag.**

**a · The OWED half → `~/.claude/tools/focus.py`.** Its own docstring: *"what is YOURS ALONE, that no
loop will bring you."* A Type-B or Type-C step that is owed is exactly that. It already exists, already
reports its own denominator, already separates `owner` / `waiting_on` / `cycle` on three orthogonal
axes, and is already the non-AI door. **A manual step that is owed becomes a row there; nothing new is
rendered anywhere.** Per-occurrence, and it disappears when done.

**b · The AUTOMATION-CANDIDACY half → the meta-stack cycle's beat 1** (`/team-audit cycle`,
`~/.claude/rituals/meta-stack/CYCLE-MAP.md`). That loop already owns *work nothing triggers*, already
emits **coverage and denominators, never verdicts**, and already runs the `clean`/`fired`/`dark`
discipline in `neglect-sweep.py`. Aggregate, periodic, per-step-class — never per-occurrence.

⛔ **NOT a new loop, and no clock.** Nothing computes a step's age against a target. Nothing says a step
is *late*. The candidacy view is read when that cycle laps and at no other time — which is the same
"accumulation, not cadence" posture `check-ux-sweep.py` and `check-backlog-drift.py` already run on.

⚠️ **The likely shape it takes there is a TENTH neglect signature** — the nine existing ones ask *does
this mechanism fire?*; none asks *does this recurring act have a performer and a surface?* A1
(UNINSTRUMENTED HAZARD) is the closest and is still a different subject: A1 enumerates *properties of
the world with no watcher*; this enumerates *acts with no record*. **Proposing a signature is method and
therefore mine; the instrument lives in `~/.claude` and is that cycle's, so implementation routes to
`/team-audit`.** ⚠️ `~/.claude` is harness-protected — a `claude -p` mission cannot write there and
fails looking like success (memory `reference_harness_protected_repos`).

---

## 6 · PER-PROJECT OR PORTFOLIO? **Portfolio, in `~/.claude/`.** Recommended, with the counter stated.

1. **The precedent already ruled it.** `doors.json`'s `_why`: one mailbox was declared by three loops
   under one string with **two different freshness limits**, and one phone under four different names.
   *"Human-door check cadence belongs to the DOOR."* Steps have the identical property — you validate an
   address once, however many estates the person belongs to.
2. **Scale is Paul's own stated payoff**, and a per-project registry is structurally blind to it: it
   cannot see that the same step recurs in three projects, which is the automation signal.
3. **The reading surfaces are already there** — `focus.py`, `cycles.py`, `demand.py`, `neglect-sweep.py`
   are all portfolio-level. A per-project registry would need a new reader per project.

⚠️ **Counter, stated honestly:** the *evidence* is per-project (Fernwood's commits, health-record's
chronicle), so a portfolio registry reads from many repos and can go dark on any one of them without
saying so. Mitigation is the existing one, not a new one: **report the denominator on every run**, as
`focus.py` and `cycles.py` both already do, and render an unreadable project as `dark`, never as clean.

---

## 7 · ONE MECHANISM OR TWO, WITH THE CASCADE? **Two. And the doctrine that separates them is ratified.**

| | release cascade | process registry |
|---|---|---|
| unit | one release (one plan file) | one recurring step class |
| shape | **finite** — a release ships once and the record is terminal | **cyclical** — a step is performed again forever |
| trigger | the release | nothing; it is read, never fired |
| failure if merged | a step would need a "gate," or a release would need an "automation state" | — |

`feedback_cyclical_vs_finite_projects` `[paul-stated 2026-08-10]`: *loops REST and fire one at a time ·
finite = burn the backlog down.* **Don't wrap finite work in loop machinery.** A cascade is finite work;
a step registry is a standing lens. Two mechanisms.

**What they genuinely share is one thing, and it is worth naming:** the `derived` / `asserted` split.
The cascade's gate-2 artifact records what was read off the origin and, separately and labelled, Paul's
word. `checked.py` does the identical thing for a door — *"a fact only Paul can produce, so it is
recorded as an ASSERTION… and rendered as one."* **Same split, arrived at independently, twice.** That
is a candidate portfolio principle and it is not mine to promote.

⭐ **And the join between the two is one row, not a merge:** *"Paul walks the build in lab"* is
`step:gate-2-walk`, `performed_by: human`, `automatable: never — the AI boundary requires the
administrator's eyes.* The cascade produces its performance records for free (Type A). It is also the
registry's most important first entry, because it is the one that proves `never` is a real value.

---

## 8 · SMALLEST FIRST ACT — useful ALONE, needs no registry, no tool and no ruling

> **Give the address-validation channel a DOOR.** `doors.json` already carries `door:fernwood-app`
> (`checkable_by: script`), whose note names *"feedback / observations / zone-audio / conversations /
> metrics — read by the Tate-Tracker tools."* Those tools read Fernwood's `est-3c9f1a`. **`est-e6696a`
> is covered by nothing.** Either widen that door's declared scope or declare a second one — and the
> declaration itself is what makes the gap visible to `comms.py` today.

**Why this and not the registry:** it discharges the exact defect the BACKLOG row names — *a channel
with no lifecycle goes unanswered while the record looks green* — using only ratified machinery, and
`checked.py` already supplies the "record it done" half with a `--note`. One config row, one existing
reader, no new concept.

⚠️ **What it does NOT do, stated so it is not oversold:** a door answers *"has anyone looked at what
arrived?"* It does not answer *"was the address standardised?"* The door is the necessary first half
(the channel gets a lifecycle); the step registry is the second. **Do not let the door's green stand in
for the step's done** — that substitution is this repo's `check-mom-ack` lesson exactly.

Ordered after it: (2) declare the first ~10 entries **Type A and B only**, from evidence that already
exists; (3) the candidacy view as beat 1's tenth signature, via `/team-audit`; (4) Type-C attests last,
if §1's 1-in-6 rate improves — and **not at all if it does not.**

---

## 9 · WHAT I DELIBERATELY DID NOT DESIGN

1. **Which steps to automate, or in what order.** Paul's, by charter. §4 gives him the two derivable
   axes and refuses to compose them into a score.
2. **A completeness target.** There is no "all the processes" to enumerate — a step nobody has written
   down emits nothing, so the registry is necessarily incomplete and must say so on every run.
   ⛔ **No coverage percentage.** A denominator nobody can establish makes any percentage decorative,
   and `reference_match_payload_not_container` is the standing warning.
3. **A clock, a cadence, a due date or a staleness limit for any step.** *A lap that has not run is not
   late.* The same holds for a step.
4. **Any change inside `~/.claude/tools/` or the meta-stack CYCLE-MAP.** Proposed; implementation is
   `/team-audit`'s.
5. **The USPS-vs-Census provider decision.** Content, and already sitting correctly in the BACKLOG row.
6. **A duration-capture habit.** §4 — the measurement would cost more than the ranking it feeds.
7. **Promotion of the `derived`/`asserted` split to portfolio doctrine** (§7). Twice-derived is
   evidence, not a mandate; it is his gate.

---

## 10 · HOW THIS PROPOSAL GETS FALSIFIED

| falsifier | observed | consequence |
|---|---|---|
| **the registry is a wishlist** | after 3 months, most entries have never emitted a performance record | it is a list of intentions — **delete it**; the doors registry was enough |
| **Type C swallows it** | more than ~a third of entries are Type C | the derivation premise is wrong; the thing needed is a habit, not a registry, and habits are not this seat's to install |
| **it became a nag** | any surface prints that a step is *late*, or a candidacy view fires outside a meta-stack lap | §5's split broke; revert |
| **it duplicates `doors.json`** | ≥half the entries are doors already registered | it should have been three new fields on `doors.json`, not a second file |
| **the axes are wrong** | §4's falsifier fires | replace them with what Paul used |
| **`never` is never used** | no entry is marked `never — …` after 20 entries | the ratchet is running; every human gate is being framed as un-automated rather than deliberate |

---

*Every claim above was read in the named file or produced by executing the named command at ~2:35 AM ET
on 2026-09-05. The 12-doors / 6-human / 1-attest figures are live reads of
`~/.claude/handoff/doors.json` and `~/.claude/handoff/door-checks.json`. **UNVERIFIED:** whether any
project outside Fernwood, life-record and `~/.claude` carries recurring-manual-step prose — a
case-insensitive grep across four CLAUDE/BACKLOG files returned 8 · 47 · 1 · 21 hits, which sizes the
declared surface but is a keyword proxy, not a census.*
