# THE JOURNEY TEST CYCLE — iterative proving of the onboarding journey, bare-logic and functional · PROPOSAL
- row: process (no BACKLOG row yet — same posture as the 09-03 readiness and 09-05 cascade proposals)
- objective: O5
- class: engine · must-not-diverge (a second definition of "this journey was proven" is the defect this exists to prevent)
- seats: practice-steward (this file)
        ux-expert → cited, not commissioned: `.ux-reviews/2026-09-05-account-creation.md` (private sibling) is the current read; §5 rules how the SKILL is used, never what it should find
        engineering-partner → deferred: nothing is built until Paul rules; §2 beat 2 and §6 are the handoff
        ai-advisor → waived: the one AI seat (the receiving agent) is already sited by the 09-04 audit §B.5; its mechanics are that seat's, not mine
        `/team-audit` → deferred: the browser-transport question (§2 beat 4a) is stack, not work
- depends-on: .plans/2026-09-04-three-environments-PLAN.md
- depends-on: .plans/2026-09-04-process-wiring-AUDIT.md
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- ready: agent-proposed 2026-09-05 — **Paul rules**
- stage: draft

> **Method only. This file ranks no feature and no finding.** It says how a journey gets proven,
> repeatedly, and what a lap leaves behind. It never says which finding matters, what the flow should
> say, or when to ship.
>
> **Assignment** `[paul-stated 2026-09-05 ~5:15 AM ET]`: *"I really hope we can start running some
> iterative cycles of testing out the journey and its functionality, using the UX review skill — and
> call practice-steward to figure out exactly how to do it. Be sure that things are proved out from a
> bare-logic point of view and a functional point of view before it gets to me. And that should really
> be the full onboarding journey."*
>
> ⛔ **Nothing here sends anything.** Mom is gate 3. The message is read as an artifact; Paul sends it.

---

## 0 · WHERE THIS SITS AGAINST WHAT IS ALREADY WRITTEN

| document | relationship |
|---|---|
| `2026-09-04-three-environments-PLAN.md` § RELEASE CASCADE | **ruled, not re-derived.** Gate 1 persona → gate 2 Paul → gate 3 Mom |
| `2026-09-04-process-wiring-AUDIT.md` §A.3, §B.5, §B.6 | **the procedure's origin.** This file executes §B.5 and answers the three things it left open: the clock's shape, the `/ux-sweep` seam, and the failability ritual |
| `2026-09-05-release-cascade-tracking-PROPOSAL.md` | **the state layer.** That file says how a walk becomes cascade state. This one says how the walk happens and repeats. **They join on the same artifact** (§3) |

### Three places this file CHANGES the 09-05 cascade proposal — stated plainly, as asked

1. ⚠️ **§4c's identity marker is CORRECTED and its METHOD is replaced.** That file says assert
   `<title>Your place</title>`. The live document reads `<title>My Home</title>`
   (`onboarding/index.html:7`). The string was wrong within eight hours of being written, which is the
   argument, not the embarrassment: **an identity marker hand-typed into a plan is a hand-kept fact
   and it rots.** The runner must **derive** the marker from the working tree — the `<title>` text and
   the `id="s…"` roster parsed out of `onboarding/index.html` at run time — and assert the served
   document matches the tree. Same posture as `build-viewer.py --check`: no fact a human types is
   state.
2. ⚠️ **§3 reason 2 is TOO STRONG.** It says a new `check-*.py` "goes red on delivery" because
   `check-cycle-map.py` globs `check-*.py` and requires each match to be named in `MOM-CYCLE-MAP.md`.
   Measured: `check-cycle-map.py:65` carries a **`NOT_IN_LOOP` exemption register** with a reason
   string per entry (2 entries today). So a clock **may** be added — it is registered there with its
   reason. And it **must** be: naming a release-cascade clock in `MOM-CYCLE-MAP.md` would forge a
   mom-cycle leg that does not exist, which is worse than the flag it avoids.
3. ⭐ **§6.3's declining to design a clock is SUPERSEDED for the walk, and STANDS for the cascade.**
   Paul has now asked for iterative cycles of the journey specifically. §1 designs that clock. The
   *cascade* still gets none, for the reason §6.3 gave.

---

## 1 · WHAT FIRES A LAP

> ### ⭐ THE TRIGGER IS THE JOURNEY SET CHANGING. Nothing else fires it.
> Not a schedule. Not a lap close. Not Paul's say-so — **his word always overrides and always starts a
> lap on request, but an override is not a trigger**, and a design that lists him as one has designed
> him as the clock.

### 1a · How that reconciles with *"iterative cycles"*

They are the same thing, and the reconciliation is the load-bearing part of this section.

**A lap's own output arms the next lap.** A walk produces findings → findings produce fixes → a fix to
this journey is by definition a commit to the journey set → the clock arms. While the artifact is
immature the loop is self-sustaining and *looks* like a cadence. When the journey stops changing it
goes quiet by itself. **Iteration is the consequence of accumulation, never a beat on a calendar** —
which is the only shape that survives Paul's own rule that a loop that has not run is not late.

A lap that closes with **zero findings and zero fixes does not re-arm.** That is correct. It is also
the reading that most needs a name, so:

### 1b · Three readings, not two — `unwalked` is not `owed`

`quiet | owed | unwalked`, the corpus's own tri-state idiom (`quiet|fired|unobserved`), and the reason
is Paul's no-permanently-red rule:

| reading | predicate | renders as |
|---|---|---|
| `quiet` | a baseline walk exists, the set has moved less than the thresholds | state, silent |
| `owed` | a baseline walk exists, the set has moved past a threshold | ⚡ a fired gate, disposed at the lap's opening gate sweep (act · fold · snooze · kill) |
| `unwalked` | **no walk has ever been recorded** — there is no baseline to measure from | **state, printed once, never a flag** |

Without `unwalked`, a clock delivered today reads `owed` from the moment it exists and keeps reading
`owed` for as long as Paul chooses not to walk. That is a control whose alarm is on by construction.
With it, *nobody has ever walked this* and *the walk is overdue* stop printing the same thing — which
is this repo's most-repeated failure shape, not a nicety.

### 1c · The journey set — declared in the runner's source, not in prose

Measured today, the set that can move the journey:

- `onboarding/index.html` — the document itself
- `engine/viewer.template.html` — carries onboarding blocks (verified by grep, 2026-09-05)
- `worker/worker.js` — `/api/grant/whoami` (`:2919`, `:2924` — the 404 that is byte-identical to a
  missing route) and `POST /api/feedback` (`:2875`, the no-token write path the flow depends on)
- `tools/grant-mint.py` — the credential the link carries
- `instance/*.json` identity and credential keys
- ⚠️ **the message text — which has NO tracked home.** `ls .plans/ | grep -i onboard` is empty and no
  template file exists. **The message is half the journey (§B.5: it is side 2's entire input) and a
  change to it can arm no clock, because there is nothing to watch.** Reported, not fixed: where the
  message lives is a content-and-privacy call.

### 1d · The falsifiers — both directions, because only one of them is cheap to notice

| # | falsifier | what would be observed | consequence |
|---|---|---|---|
| **F1** | **the set is drawn too WIDE** — the clock is a cadence in disguise | it reads `owed` on releases where nothing about the journey moved (e.g. a `viewer.html`-only or copy-only burst arms it) | narrow the set, or delete the clock and let the onboarding plan's `## QA` carry it alone |
| **F2** | **the set is drawn too NARROW** — and this is the dangerous one | a journey defect is found by Paul at gate 2, or by Mom, on a build where the clock read `quiet` | widen the set by exactly the file that carried the defect, and record the move |
| **F3** | ⛔ **the set is structurally uncoverable** | a journey defect ships with **no commit anywhere** — an Access policy change, a KV binding, a Worker deploy, a rotated token | **a git clock cannot see this and must say so on its own face.** Measured precedent: the 09-04 KV write-cap took prod surfaces dark with no code change; the Anthropic workspace-header change killed prod Guru with no code change |

**F3 is not a defect in the design; it is the honest boundary.** The clock watches commits. It must
print that it watches commits, or its silence will be read as a claim about the environment.

**Zero runs owed for a month with the journey unchanged is the clock working, not failing.**

---

## 2 · WHAT ONE LAP DOES — the beats, executable by a session with no memory of this one

**Notation:** `[det]` = deterministic, no model. `[agent]` = a spawned seat. `[paul]` = his gate.

### Beat 0 · ARM — dispose the gate `[det]`
At pickup, `check-journey-walk.py` reads `quiet | owed | unwalked`. `owed` is a fired gate and gets a
disposition at the lap's opening gate sweep: **act · fold · snooze · kill** (CYCLE-SPINE gate-sweep
amendment). A snooze is Paul's and increments the snooze counter. **Nothing auto-opens a lap.**

### Beat 1 · FIX THE TARGET — resolve what you are actually walking `[det]`
```
git rev-parse HEAD
curl -H "$(access headers)" https://fernwood-qa.pages.dev/qa-build.json      # .sha
curl <qa-worker>/health                                                       # .env, .kv_canary, .estateId
```
⛔ **Fail closed, three ways, before anything else runs:**
- `qa-build.json .sha` ≠ the sha you intend to walk → **STOP.** You are walking a different build.
- `/health .env != "qa"` or `.kv_canary != "qa"` → **STOP, exit 2, nothing written**
  (`qa-write-probe.py`'s established refusal — reuse it, do not re-derive it).
- ⛔ **Never lab.** Every path on lab returns the same 19,621-byte document with HTTP 200, including
  `/nonexistent` (measured 09-05). A routing defect is undetectable there, and `servedSha` is
  unresolvable because lab has no `qa-build.json`. A gate-1 stamp earned on lab is unverifiable by
  construction.

### Beat 2 · PROOF A — BARE LOGIC `[det]` — `tools/journey-logic.py`
The path table, forced state by state, against the **real document** in headless Chromium at her
conditions (414×848), with the Worker's responses controlled by route interception for the fault
paths and live for the happy path. Every row asserts **which screen resolved** and **what was
written**. One exit code.

The table, read off `onboarding/index.html` today — this is the enumeration, and it is the artifact's
own content:

| # | forced state | must resolve to | why it is a path and not a feature |
|---|---|---|---|
| 1 | `?g=<valid>` on a known Pages host | `s1`, and `?g` **stripped from the address bar** | the credential must not survive in history |
| 2 | no `g`, no `fw-grant` in storage | `s-nolink` | |
| 3 | `?g=<unknown/revoked>` → whoami 404 | `s-nolink`, **byte-identical to path 2** | X and not-X must print the same *to her* and must be distinguishable *to the runner* |
| 4 | whoami rejects (offline) | `s-nolink` **with the offline copy**, never the bad-link copy | the page's own comment rules this; nothing else checks it |
| 5 | unknown Pages host | `s-nolink` — `WORKER` resolves null, fail-closed | a copy served elsewhere must never write into her silo |
| 6 | `fw-onboard-step` = `2` / `3` / `4` | `s2` / `s4` / `s4` | the resume table; `3→4` is deliberate and untested |
| 7 | submit with any required field empty | stays on `s2`, names **what is missing**, focuses the first gap | |
| 8 | **duplicate submit, identical text** | `{stored:0, duplicate:true}` accepted → `s3` | |
| 9 | **duplicate submit, CORRECTED text** | a **new** record lands; the correction is not a silent no-op | this is the real 09-05 finding, in assertion form |
| 10 | POST returns `{stored:0}` without `duplicate` | stays on `s2`, retry copy, button re-enabled | a 200 is not proof of a write |
| 11 | **storage cleared after the link was consumed** | resolves to *something stated*, not to an accident | the link strips `?g`, so a cleared browser has no way back |
| 12 | **new device, link re-tapped** | `s1` | |
| 13 | **wrong document** — the Access login page (HTTP **200**) | **exit 2**, never clean | `qa-walk.py`'s `.main-card` guard does NOT transfer: `onboarding/index.html` has **zero** `.main-card` |

⛔ **Row 13 is not optional.** The Access login page returns 200, and `herConditions()` once scored a
GitHub 404 page as clean. The runner asserts the **derived** identity marker (§0.1) or it can walk a
login page and report green.

Paths 11 and 13 are where the honest reading is *"resolves to a stated outcome"*, not *"resolves to
the right outcome"* — **what the right outcome is, is a content call and is not mine.**

### Beat 3 · GATE — A must be green before B runs `[det]`
Ordering, not ranking. A functional walk over a broken path spends an agent's entire read on a defect
the table names in seconds, and — worse — **a fluent walker narrates a coherent experience of a broken
flow.** Sequencing here is a cost and contamination control.

### Beat 4 · PROOF B — FUNCTIONAL `[agent]` — the two sides, per §B.5
**Side 1 — MINTING, first, fully primed.** Given a person and an estate: mint the grant, produce the
link, produce the message. Assert the refusals fire (`grant-mint.py` G1/G2). **Its only output is the
message text and the link.** Deterministic clauses land in the plan's `## QA` `accept:` block.

**Side 2 — RECEIVING, second, radically un-primed.** Its entire input is the message text, verbatim.
No URL passed separately, no token, no estate id, **no repo access.** An agent that can read
`.private/` will resolve by hand whatever the message failed to carry, and its report will read clean.

- **4a · Transport.** The browser must carry the Access credential. Options and the host-scoping
  argument are in the cascade proposal §4c (A now for the deterministic half; C over B for the agent
  half). ⚠️ **That choice is stack, not work — `/team-audit` and `engineering-partner` own it.**
- **4b · Write safety.** Registered fixture deviceId, `_qaFixture` inline on anything reaching a
  tracked `instance/*.json`, and **two negative controls that are not optional under the freeze**:
  prod's readers do not see the writes, and `read-mom-feedback.py --pickup` / `check-mom-ack.py`
  output is **unchanged** by the run. A walk that manufactures an arrival-shaped record puts a phantom
  behind a line that is currently holding her arrivals unread.
- **4c · A named operational risk with a named fallback.** `/ux-sweep`'s run-4 friction: a subagent's
  own classifier refused a **relayed** authorization to write, and *that refusal was correct*. Side 2
  types and submits. Mitigation: the QA-only condition is a **standing condition at the top of its
  prompt**, never a mid-run relay. **Falsifier:** if side 2 refuses to submit, the split is wrong —
  the main session drives the browser and side 2 observes.

### Beat 5 · ADJUDICATE `[agent]`
`/ux-sweep` pass 2's contract, reused verbatim (§5): re-verify side 2's load-bearing claims against
the rendered surface before accepting any of them; adjudicate against every file in
`~/.claude/design-principles/`; verdicts **CONFIRMED-VIOLATION · DELIBERATE-PER-DOCTRINE · PARTLY ·
NEEDS-PAUL**; each load-bearing claim carries its `RE-VERIFIED: <command or surface> — <date>` line.
A claim that will not reproduce becomes a QUESTION, never a finding.

### Beat 6 · TRAIL `[det]`
§3. Three writes, and one control that must run **after** them (§5c).

### Beat 7 · CLOSE `[paul]`
- Findings → the fix list. **Fixes are gated; Paul rules.** Fixing re-arms the clock (§1a) — that is
  the iteration.
- **Zero findings → record `unproven at this lap`, never `validated`** (§6d).
- Pre-registered self-improvement, discharged: what did this lap change about the *walk*?
  **"None — pre-registered metric unmoved" is a valid recorded outcome.**
- Mark the lap closed in the trail (S4). Record any threshold tune.

---

## 3 · WHAT A LAP LEAVES BEHIND — §1b confirmed, and amended in four places

**Confirmed:** the pointer-in-the-plan shape (`- gates:`), `.plans/walks/` as the home, the
`derived` / `asserted` split with nothing typed in `derived`, and `derived.servedSha` + `derived.env`
as the load-bearing pair. **Amended:**

```jsonc
{
  "plan": ".plans/2026-09-05-onboarding-PLAN.md",
  "gate": 1,
  "ranAt": "2026-09-05T06:10:00-04:00",
  "derived": {
    "origin": "https://fernwood-qa.pages.dev",
    "servedSha": "…", "servedSubj": "…", "env": "qa", "estateId": "est-qa0001",
    "walker": "p-qa-synth-1", "exit": 0,
    "identity": {                                  // ⭐ AMENDMENT 1 — derived from the TREE, not typed
      "expect": {"title": "My Home", "views": ["s1","s2","s3","s4"]},
      "expectFrom": "onboarding/index.html@<sha>",
      "served":  {"title": "My Home", "views": ["s1","s2","s3","s4"]}
    },
    "journeySetSha": "…",                          // ⭐ AMENDMENT 2 — what the clock resets against
    "paths": [                                     // ⭐ AMENDMENT 3 — the bare-logic proof IS a record
      {"id": 3,  "forced": "whoami-404",      "resolved": "s-nolink", "ok": true},
      {"id": 9,  "forced": "corrected-resubmit", "resolved": "s3",    "ok": true, "wrote": "new-record"},
      {"id": 13, "forced": "access-login-page", "resolved": "EXIT2",  "ok": true}
    ],
    "mutations": {"ran": 5, "caught": 5, "ids": ["m-guard","m-worker-hardcode","m-fp-grant-only","m-stored-zero","m-wrong-doc"]},
    "isolation": {"plant": "link-stripped-from-message", "held": true}   // ⭐ AMENDMENT 4 — §6c
  },
  "asserted": { "by": "p-7f3a2c", "verdict": "pass", "findings": ["…"] }
}
```

**Why `mutations` rides in the artifact and not only in the tool's selftest:** a suite proven able to
fail *once at build time* and a suite proven able to fail *on this run* are different claims, and
without the field they print the same. A reader six weeks later can see the assertions were live.

**Why `paths` rides in it:** it is the only durable record of *what was enumerated*. A later reader
comparing two walks can see a path appear — which is how the table's own growth becomes visible
instead of remembered.

**What is still single-method, stated rather than implied:** the corroboration read (a walk leaves the
walker's `personId` on rows in that estate's KV) remains dark while `/api/feedback` stores
`personId: null` against a presented credential — the 09-05 gate-1 finding. **That is a capability-model
call and it is Paul's.**

**And the judgment half stays separate:** side 2's report + beat 5's adjudication →
`.ux-reviews/YYYY-MM-DD-journey-walk.md`. One `- stage-note:` on the onboarding plan binds both and is
already read by `qa-divergence.py --check`. **One note, two readers, no third tracker.**

---

## 4 · ⭐ THE TWO PROOFS — why neither may ever stand in for the other

Paul named two tests. They fail in opposite directions, and the reason is structural, not a matter of
rigor.

| | **bare logic** | **functional** |
|---|---|---|
| **the question** | does every declared path resolve? | does a person get where they are going? |
| **oracle** | the developer's own stated intent, transcribed into assertions | a reader's experience |
| **where it lives** | `tools/journey-logic.py`, beat 2 | beats 4–5, two agents |
| **who runs it** | any session, CI, per-commit | the main session drives; side 2 is a spawned seat |
| **cost** | seconds · one command · zero model tokens | two agents · a browser · an adjudication round · **and one consumable un-primed read** |
| **its structural weakness** | ⭐ **an oracle problem** — it can only fail on paths someone thought to enumerate | ⭐ **a coverage problem** — one walk takes ONE path; a clean happy-path walk is silent about the other twelve |

> ### The rule, and it is the whole of §4
> **Bare logic has an oracle problem; functional has a coverage problem. Neither weakness is repaired
> by applying the other's strength harder.** Running the functional walk three times does not
> enumerate a revoked grant. Adding twenty assertions does not tell you whether the wait screen reads
> as abandonment.

**What each failure looks like, from this repo's own record — not hypothetically:**

- **Functional standing in for logic.** `herConditions()` scored a GitHub 404 page as clean
  (2026-09-01). The Cloudflare Access login page returns **HTTP 200**. A fluent un-primed agent handed
  a message and a URL can walk a *login page* and write a coherent report about a first-run
  experience that never happened. **Only an assertion on a derived identity marker catches that.**
- **Logic standing in for functional.** The current UX read names the untested seam directly: *"the
  onboarding step reads to her as a conversation rather than as a card — this is the untested seam the
  entire flow rests on."* **No assertion can fail on that**, at any density.

**The economic consequence, which is why the trigger must not fire the expensive half on churn:**
un-primedness is a **consumable**. Once an agent has walked the flow, that agent can never be
un-primed on it again, and neither can its transcript. The cheap proof is free and may run per-commit;
the expensive proof is rationed and fires on accumulation. **That is a cost argument, not a value
ranking — I am not saying which proof matters more, and that question is not mine.**

**And one boundary carried from §B.5, restated because it binds hardest here:** a clean journey walk
is a **precondition for sending the message, never evidence that the trial will succeed.** The
receiving agent is a fluent reader with no fear of getting things wrong; her documented constraint is
the fear of getting things wrong.

---

## 5 · ⭐ THE `/ux-sweep` TENSION — the sharpest question in the brief, ruled

Paul said *"using the UX review skill."* The 09-04 audit §A.3a measured that the skill's setup step 3
puts this **verbatim into both agent prompts**: *never tap answer/Yes/No, never Save/Send/Log/submit,
never type into fields.* A walk of account creation types an address and submits it.

> ### RULING: the skill is **CITED and PARTIALLY REUSED at a named seam. It is not invoked, and the run is not filed as a sweep.**

### 5a · What transfers, what does not — part by part

| part of `/ux-sweep` | verdict |
|---|---|
| ⭐ **ENTER THROUGH THE USER'S DOOR** `[paul-stated 2026-08-06]` | **transfers wholesale, and is the ancestor.** The journey walk is that rule extended from one door to a multi-step journey. Cite it; do not re-derive it |
| **Pass 2's adjudication contract** — re-verify before adjudicating · canon vs candidate · the four verdicts · `RE-VERIFIED:` lines · punch list gated on Paul | **transfers wholesale.** ⭐ **This is the part Paul means by "the UX review skill"** — it is what makes a fresh read honest, and it is fully portable |
| **Pass 1's un-primed calibration** | transfers in **shape**; its prompt's safety rule inverts (§5b) |
| **Setup 3 — the no-typing safety rule** | ⛔ **does not transfer and may not be waived on a sweep** |
| **Setup 2 — serve locally, md5 the bytes** | does not transfer. The walk runs on QA; the freshness proof is `qa-build.json`, not an md5 |
| **Setup 4 — 390×844** | superseded by the project's measured her-conditions, 414×848 + A+ (the skill's own 8/31 log proposes this correction) |
| **The sweep clock and the run log** | ⛔ **must not be touched by a journey walk** (§5c) |

### 5b · Why a flag on the skill is the wrong shape

Not because a flag is inelegant. Because **the safety rule is the skill's identity** — it is what makes
`/ux-sweep` safe to point at a production surface with a live backend. A flag that suspends it means
the next agent reading the skill can no longer know whether the rule is in force for the run it is in.
**A sweep-with-typing and a sweep-without-typing would file the same artifact under the same name into
the same directory.** X and not-X, same observation.

⭐ **And the swap is only legitimate because the rule is REPLACED, not deleted.** The journey walk is
not *less* safe; it is safe by a **different, stronger, already-implemented mechanism** —
`qa-write-probe.py`'s refusal (`/health` must read `env == "qa"` **and** `kv_canary == "qa"` or exit 2
having written nothing), registered fixture ids, and two negative controls. **State the replacement in
the walk's own trail**, or a later reader sees a ratified safety rule that was simply ignored.

**Falsifier for this ruling:** if a journey walk's writes ever appear in a mom-cycle reader's output,
or on prod, the replacement mechanism did not hold — the walk goes back behind the blanket
prohibition, and Paul must be told that gate 1 cannot include submission and is therefore weaker than
it reads.

### 5c · ⛔ A MEASURED HAZARD — the journey walk can silently steal the sweep's clock

`check-ux-sweep.py:96–108` qualifies a run in `Tate-Tracker/.ux-reviews/` by **filename**
(`ux-sweep|two-pass`) **OR by CONTENT** — any `.md` with a date in its name carrying `^#{1,3}\s*pass\s*1`
and `pass\s*2` headers. That content check was added 2026-09-01 precisely because filename matching had
missed a real run.

**So a journey-walk trail filed to `.ux-reviews/` with `## Pass 1` / `## Pass 2` headers would reset
the holistic sweep clock** — and a sweep that was genuinely owed would read `quiet`. The clock reads
`owed` today (52 viewer commits against a limit of 20, measured 2026-09-05), so this is live, not
theoretical.

**Three controls, all cheap:**
1. **Sections are `## Side 1 — minting` / `## Side 2 — receiving`.** Never "pass." §B.5's own
   vocabulary already does this; it must be *stated*, because a writer who has just read `/ux-sweep`
   will reach for "pass" by reflex.
2. **The filename contains neither `ux-sweep` nor `two-pass`.** `YYYY-MM-DD-journey-walk.md`.
3. ⭐ **A deterministic check, not a hope:** run `python3 tools/check-ux-sweep.py --json` **before and
   after** filing the trail (beat 6). `lastSweepFile` must be **unchanged**. A convention that has to
   be remembered at file-creation time is one that will be missed — that sentence is the checker's own,
   in its own source.

---

## 6 · THE MUTATION HABIT — the smallest ritual that plants a defect

*"A gate that is never seen to fail is not a gate"* applies to this walk first. The ritual has **three
targets**, because the walk has three things that can be silently blind.

### 6a · Target 1 — the assertion set. `journey-logic.py --selftest`, and it runs EVERY lap as beat 2's precondition
Five mutations applied to a **scratch copy** of `onboarding/index.html` in a temp dir (never the tree),
each of which must flip **one named assertion** to red:

| id | mutation | must fail |
|---|---|---|
| `m-guard` | delete `if (!grant \|\| !WORKER) { show("s-nolink"); return; }` | path 2 |
| `m-worker-hardcode` | replace the `PAGES_WORKERS` lookup with a fixed Worker | path 5 (fail-closed on an unknown origin) |
| `m-fp-grant-only` | drop `"\u0000" + text` from the fingerprint | **path 9** — the real 09-05 defect, reproduced |
| `m-stored-zero` | relax `res.stored === 0 && !res.duplicate` to `res.stored === 0` | path 10 |
| `m-wrong-doc` | serve the Access login bytes for every request | path 13 |

**Green requires both halves: every mutation caught, AND the unmutated run clean.** A mutation that
flips nothing means the assertion set has a hole exactly where that mutation is. Cost: seconds. This is
already the repo's proof standard (`check-arrival-dispositions.py` 14/14 by three mutations;
`check-backlog-drift.py` 16/16).

**When it fires: every lap, inside beat 2.** Not a separate ritual — a separate ritual is a capability
someone has to remember to invoke, which is the failure `check-ux-sweep.py` exists to end.

### 6b · Target 2 — the walker's document identity. `m-wrong-doc`, and it is the one that must exist
This is the *machine* half of the same defect the login page creates for the agent. It is in 6a's table
and is called out separately only because it is the mutation most likely to be dropped as redundant.
It is not redundant: it is the only one that proves the runner can tell **the product** from **a
200-status page that is not the product**.

### 6c · Target 3 — the receiving agent's ISOLATION. The zero-cost plant
Side 2's whole validity rests on its input being the message and nothing else. That constraint has
never been tested, and its failure is invisible: **a contaminated agent produces a better-looking
report, not a worse one.**

> **The plant: for one lap, strip the link out of the message before handing it over.**
> If side 2 reaches the flow anyway — from repo access, from a guessed `fernwood-qa.pages.dev`, from
> memory — **the isolation is not holding and every report it has written is contaminated.** If it
> stops and says *"this message does not contain a way in,"* the constraint is proven and that is
> itself a finding about the message.

Cost: zero. Nothing is deployed, nothing is broken, no un-primedness is spent — a missing link teaches
the agent nothing about the product. **When it fires: on the first lap, and on any lap where the
walking harness or the transport changed.** Recorded as `derived.isolation` (§3).

⛔ **A second, cheaper-looking plant that I am NOT proposing:** deploying a deliberately broken build to
QA so the agent can catch it. It costs a deploy, it risks a fixture reaching a tracked file, and it
proves less than 6a does for more. Named here so it is not re-proposed.

### 6d · What the mutation habit CANNOT prove, and the empirical control that covers it
No plant proves the *functional* half can catch a **judgment** defect — that a screen reads wrong. The
only instrument for that is `/ux-sweep`'s own measurement, `caught-unprompted: N`, appended per run.

> **The empirical rule:** if **three consecutive** functional walks return zero unprompted findings
> while the logic suite finds any, the functional half is theatre under this topology — **delete or
> re-scope it; do not tune it.**

**And the register's honesty line, carried from day one:** gate 1 is **PROVEN at n=1** (the 09-05 walk
caught two real defects plus one in the gate itself). **Gates 2 and 3 have never run and are
UNPROVEN.** The first cascade that passes all three first time is *unproven*, not *validated*.

---

## 7 · WIRING — where it is read, and the two registers that must be edited

1. **The clock** — `tools/check-journey-walk.py`, read at pickup beside `check-ux-sweep.py` and
   `check-backlog-drift.py`. One line in `CLAUDE.md`'s session-start block. **Silent at `quiet`.**
2. ⭐ **`check-cycle-map.py`'s `NOT_IN_LOOP` register (`:65`) gains one entry with its reason** —
   *"release-cascade clock; not a mom-cycle leg."* **Not `MOM-CYCLE-MAP.md`**: naming it there would
   forge a leg the loop does not have, and the map's own rule is that adding a leg forks the doctrine.
3. **The runner** — `tools/journey-logic.py`. Does **not** match `check-*.py`, so it needs no register
   entry (same as `qa-walk.py`).
4. ⛔ **IT DOES NOT FIRE THE MOM LAP.** `MOM-CYCLE-MAP.md`: *"The loop rests. HER INPUT is what fires
   it."* Nothing here touches `position()` or `mom-cycle-status.py`.
5. **The cascade state** — the walk artifact is what the 09-05 proposal's `gates:` pointer points at.
   No second register.

**Spine conformance, stated as coverage and not graded:** S1 the walk artifact carries `ranAt` and the
lap's outcome · S2 beat 7 is Paul's gate, machine-visible on the plan's `stage-note` · S3
`journey-logic.py --selftest`, seen to fail by five mutations, sited at the measured risk (the 200-status
wrong document) · S4 the lap is marked closed in the trail · S6 n/a — this is a beat set inside the
release cascade, not a thirteenth loop on the board. **Whether it should become one is Paul's.**

---

## 8 · WHAT WOULD PROVE THIS WHOLE DESIGN WRONG

| # | falsifier | consequence |
|---|---|---|
| 1 | the clock reads `owed` on releases where the journey did not move | §1d F1 — narrow the set or delete the clock |
| 2 | a journey defect reaches gate 2 or gate 3 on a build the clock read `quiet` | §1d F2 — widen by exactly the file that carried it |
| 3 | `journey-logic.py --selftest` passes with a mutation that flips nothing | the assertion set has a hole where that mutation is; the green is decorative |
| 4 | side 2 reaches the flow from a link-stripped message | §6c — the isolation is not holding; every prior report is contaminated |
| 5 | filing a journey trail moves `check-ux-sweep.py`'s `lastSweepFile` | §5c — the walk stole the sweep's clock |
| 6 | three functional walks, zero unprompted findings, while logic finds defects | §6d — delete or re-scope the functional half |
| 7 | **Paul overrides a walk's verdict twice** | strip every verdict from this mechanism; print evidence only. **A reversal is my defect, not his inconvenience** |
| 8 | a walk's writes appear in a mom-cycle reader or on prod | §5b — the safety replacement failed; the walk loses submission |

---

## 9 · ⛔ WHAT I DECLINED TO CHOOSE, AND WHY EACH IS PAUL'S

1. **Which findings from the 22 in the current UX read get fixed, or in what order.** Content. Not mine
   at any altitude.
2. **What the "right" outcome is for paths 11 (cleared storage after the link is consumed) and 12 (new
   device).** The path table asserts a *stated* outcome; **what should happen to a person who clears
   her browser is a product decision.**
3. **Where the message text should live** (§1c). It is half the journey set and has no tracked home.
   Where it goes is a content-and-privacy call.
4. **The `personId: null` fix** (§3). Capability model.
5. **What a gate passes ON** — the `accept:` clauses per feature. Content; the 09-03 proposal §3a is
   the home and is still unruled.
6. **Whether "each and every feature" includes loop work that carries no plan file.** The contradiction
   with C4 §9 Q3 is recorded in the 09-05 cascade proposal §2 and is **unchanged** by this file. Three
   readings; only he can pick.
7. **The browser transport** for side 2 (§2 beat 4a). Claude stack — `/team-audit` and
   `engineering-partner`.
8. **Whether the journey test becomes a thirteenth loop on the board** (§7). It is designed here as a
   beat set inside the cascade. Promoting it is his.
9. **Every threshold in §1** — days, journey-set commits, laps. A **first cut, unratified**. Tune from
   what runs show; record the move.

---

## 10 · SMALLEST FIRST VERSION — useful even if the rest is rejected

> **Beat 2's path table, run once by hand against QA, recorded in one file.**

No clock, no new tool, no ruling. It produces the enumeration — which is the asset — and it is what the
09-05 walk should have had. Ordered after it:

1. `.plans/2026-09-05-onboarding-PLAN.md` (header drafted at 09-04 audit §B.6) so the walk has a join
   key. **Still the cheapest act in the whole thread and still not done.**
2. `tools/journey-logic.py` with §6a's five mutations.
3. Beats 4–5, the two-sided functional walk, with §6c's isolation plant on lap 1.
4. `tools/check-journey-walk.py` + the `NOT_IN_LOOP` entry — **last**, because a clock over a ritual
   nobody has run yet measures nothing.

---

*Every repo claim above was read in the named file at ~6:00 AM ET on 2026-09-05:
`onboarding/index.html:7` (title) and its script block (paths 1–12) · `tools/check-ux-sweep.py:80–108`
(the content qualifier) and its live `--json` output (`owed`, 52 viewer commits, last sweep
2026-08-31) · `tools/check-cycle-map.py:41,65` (the glob and the `NOT_IN_LOOP` register) ·
`tools/qa-walk.py` (the `.main-card` guard) · `tools/qa_access.py` · `tools/qa-write-probe.py:1–34`
(the refusal) · `worker/worker.js:2875,2919,2924` · `~/.claude/skills/ux-sweep/SKILL.md` setup 3, pass
2, run-4 friction. **The lab measurements, the `.main-card` count of 0 and the empty
`ls .plans/ | grep -i onboard` are carried from the 09-04/09-05 measurements and were not re-run here.**
**UNVERIFIED:** whether `CF_ACCESS_CLIENT_ID`/`SECRET` are set as repository secrets — check by a
workflow run, not by re-reading the workflow.*
