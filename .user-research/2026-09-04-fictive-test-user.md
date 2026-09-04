---
type: test-fixture-design
class: SYNTHETIC — not user research
project: tate-tracker
last_updated: 2026-09-04
evidence_level: "n/a — this document describes a FIXTURE, not a person. It contains no user evidence and may never be cited as any."
lane: "C (fictive test user), parallel run 2026-09-04 PM ET"
revisions:
  - "2026-09-04 (2) — §2 REWRITTEN: the Hillyer model is an expectation lens, not an artifact
     (Paul, in-session); §3f naming ruled `synthetic-<demographic>`; §6 demographic stated as a
     blocked dependency; the (B) fork named as out of scope; the @media count corrected 14 → 13."
sources:
  - "Paul, in-session 2026-09-04 — the Hillyer mechanism, the naming ruling, the separate identity"
  - ".private/voice-memos/2026-09-04-1346-fictive-test-user.txt (whisper transcript, [transcript-UNVERIFIED])"
  - ".private/voice-memos/2026-09-04-1347-synthetic-persona-desktop-mobile.txt (same)"
  - "tools/people.json — the existing p-harness-v1 synthetic identity + its two-half fence"
  - "viewer.html STORAGE_KEYS roster (read 2026-09-04) · tools/check-storage-keys.py · tools/qa-walk.py"
  - "~/.claude/skills/ux-sweep/SKILL.md (read, NOT edited — proposals only)"
  - "VOCABULARY.md §4 (rejected names) · .user-research/README.md (evidence-tag contract)"
---

# The standing harness — a fictive test user that builds its own instance

> # ⛔ READ THIS BEFORE READING ANYTHING ELSE
>
> **Everything in this document is SYNTHETIC. It is a test fixture. It is not a person, it
> does not stand in for one, and nothing it ever produces is evidence about a human being.**
>
> This file lives in `.user-research/` because that is where the reviewers look — **not**
> because it is user research. It is a different *class of evidence* from every other file
> in this directory:
>
> | this directory | what it is | may be cited as |
> |---|---|---|
> | `persona-mom.md`, `persona-paul-co-steward.md`, the `jtbd-*` and `journey-*` cards | models of **real people**, built from what they actually said and did | `assumption` / `inferred` / `validated` per the README contract |
> | **this file** | a **machine** we drive through the app on purpose | ⛔ **nothing.** It generates hypotheses and exercises code paths. It validates nothing. |
>
> **Three hard lines, none of them negotiable by a later session:**
> 1. ⛔ **It is never merged into, cross-referenced from, or used to update `persona-mom.md`
>    or any research about Bob's household.** If a harness run produces something that reads
>    like a finding about Mom, that is a finding about *the app*, phrased wrong.
> 2. ⛔ **It never speaks for anyone.** No quote it produces is a quote. No preference it
>    expresses is a preference. `user-researcher`'s standing rule already covers this —
>    synthetic input is `assumption` by default and *may never be promoted to `validated`* —
>    and this file does not create an exception to it.
> 3. ⛔ **It never touches a real estate's record.** Fences in §4. The prod half is permanent.

---

## 1 · What Paul asked for, and what this is

From the 1:46 PM memo (`[transcript-UNVERIFIED]` — substance used, phrasing not stamped as a
ruling): invent a fictive AI test user, so that as QA and UX reviews run, **one additional
test** asks what a typical user expects to see and how they interact — and *"that persona over
time should kind of build their own instance of the app to be sure that everything actually
tests,"* durable, **in addition to** the blind tests already run.

Two things in that are doing all the work, and they are easy to lose:

- **"build their own instance"** — the harness *accumulates*. It is not a reviewer that looks
  at a page; it is an occupant that leaves state behind. That is the whole reason it is worth
  building (§3).
- **"in addition to"** — it is additive to `/ux-sweep`'s un-primed pass, never a replacement
  (§5). This is not politeness about an existing tool; the two are *structurally* incapable of
  doing each other's job, and §5 says why.

**What it is, in one line:** a long-lived synthetic occupant of a QA-only instance of the app,
driven by an agent on a tenure cadence, whose accumulated state is a committed, restorable save
file — and whose reports are hypotheses handed to the doctrine pass, never findings.

---

## 2 · The Hillyer model — it is an EXPECTATION LENS, not an artifact

> **⚠️ This section previously read "I could not find it," and that framing was WRONG — not
> merely incomplete.** Corrected 2026-09-04 on Paul's own account. The first version reported an
> absence honestly and still misled, because *"we searched and found nothing"* reads as **settled**
> when the real answer was that we were looking for the **wrong class of object**.

**What it actually was** `[paul-stated 2026-09-04]`: an agent that read everything the case
produced *against Scott's own prior messages* — ingesting how he had written, what he had reacted
to, what he had rejected — **and then read each new outbound draft as if it were him receiving
it**, to predict what he would expect and whether the thing would land.

So it is not a persona document, a simulator, or a fixture. It is a **review posture**: a lens
applied to *our output*, grounded in a corpus of *the reader's own behaviour*.

### ⭐ Why two independent searches missed it — the durable finding

Both this lane and the hub searched, separately, and both found nothing. Neither search was
careless; **both were looking for a document.** A capability that exists as *an agent's behaviour*
leaves **no artifact to grep for** — no file, no filename, no distinctive string. It lived in how
a review was run, not in something the review wrote down.

**That is a real search failure mode and this corpus will hit it again.** When a capability is
described and the filesystem is silent, *"it does not exist"* and *"it is not a file"* are
indistinguishable from the outside — and the second is invisible to every tool we search with. The
fix is not a better grep; it is to ask **"would this have left an artifact at all?"** before
reporting an absence. `[verified — two independent searches, 2026-09-04]`

### What it changes here — the tenure becomes a corpus

This makes the accumulation in §3 do **double duty**, and is a stronger justification than the
four in §3b:

- The tenure is not only *state that exercises code*. It is a **record of what this occupant was
  shown, what it tapped, and what it passed over** — which is exactly the corpus the lens needs.
- So a new card, ribbon or flow is not judged in the abstract. It is judged as: *does this land
  for someone who has lived here six weeks and already passed over four of these?*
- **No cold reviewer can ask that question**, because the question is made of history.

### ⛔ AND IT FORKS — (B) IS OUT OF SCOPE FOR THIS DOCUMENT

The lens can be pointed at two different corpora, and they are **not the same capability**:

- **(A) pointed at the SYNTHETIC harness** — the corpus is its own tenure. No real person's words
  are involved anywhere. **No AI-boundary question arises.** ✅ **This is what this document
  designs, and the only thing it designs.**
- **(B) pointed at a REAL reader** — the literal Hillyer shape. At Fernwood that reader is **Mom**.
  It is arguably *permitted* — analysing the record on the way out is the one legitimate AI seat —
  but it inherits the **QUARANTINE clause** (model output derived from her words about herself
  never leaves `.private/` and never reaches her) and the **administrator gate**, and it is a
  **distinct capability with its own build-or-not decision**.

⛔ **(B) is deliberately NOT carried here.** Burying a decision about pointing a model at a real
person inside a *test-fixture design document* is the same defect this run flagged an hour earlier
about the canvas ruling: **a decision living somewhere nobody would look for it.** It is named
here in one paragraph and routed to the hub as its own row. Do not fold it back in.

### The discipline still inherited

Unchanged by the correction: the Hillyer record's governing rule is that **a lower-grade source
may never clear a higher-grade one** — `[Scott]` is never a twin, OCR never clears Track-1,
*"a source that derives from the record cannot clear the record."* Translated: **a synthetic
occupant may never clear a question about a real one.** That is §1's line 2.

*(The two real artifacts found by the original search — `SCOTT_DISAGREEMENTS.md`, a register of
what the real Scott disputed, and `CRIB_2026-07-26_scott-sitdown.md`, a prep sheet built from his
record — remain what they were: models of a real person from that person's own words. They are not
the thing Paul meant, and they are not a template for anything synthetic.)*

---

## 3 · ⭐ THE INSTANCE — the load-bearing half

Everything else here is ordinary. This is the part to get right.

### 3a · What "an instance" actually holds

Not a hypothetical. Measured against the running app `[verified — `viewer.html`'s own
`STORAGE_KEYS` roster, read 2026-09-04]`. A single browser's instance holds **20 rostered
keys**, in four classes:

| class | keys | why it matters to a harness |
|---|---|---|
| **identity** | `deviceId`, `maintainer`, `sync.v1`, `sync.audience.v1`, `lastSync.v1` | the fence lives here — this is what makes a record attributable, or safely not |
| **per-estate answer state** ⚠️ | `momQueue.answered.v1`, `.snoozed.v1`, `.offered.v1`, `.general.v1`, `ackSeen.v1`, `zoneJourney.launcherDismissed.v1` | **this is the state that only exists after weeks of use** — and the state a one-shot review can never produce |
| **capture** | `observations.v1`, `feedbackOutbox.v1`, `door.outbox.v1`, `zones.v1`, `zones.lastSyncedAt.v1` | the outboxes exist *for the offline case*, which is the site's permanent physical premise |
| **instrument** | `metrics.v1`, `metricsExclude`, `textSize` | how the record sees the occupant |

Plus the **server side**: `/api/feedback`, `/api/observations`, `/api/zone-audio`,
`/api/conversations`, `/api/metrics`. Those are the ones that can contaminate; §4 is about them.

### 3b · Why accumulation is the point — four things no inspection reaches

This is the argument that the harness earns its keep rather than being a fourth review lens.
Each is a real, currently-untested path in this repo:

1. ⭐ **The origin-move migration has no populated instance to migrate.** `check-storage-keys.py`
   exists because *"a key the origin-move migration does not know about is a key she loses"*
   (C4 2b). The only fully-populated instance of those 20 keys in existence is **Mom's phone**,
   and that is precisely the one you cannot practice on. A harness save file at week 12 is the
   migration's missing fixture. `[verified — the roster and the guard's own stated rationale]`
2. **Cross-device answer retirement was silently dead and nobody noticed for weeks.** The
   2026-08-31 sweep found `syncServerAnswers` failing (client asks 365d of `/api/feedback`,
   Worker caps at 90d → 400 → localStorage-only fallback). That defect is **invisible to a
   fresh instance** — it requires answered cards older than the cap. Only tenure finds it.
3. **The 5-slot cap under real supply pressure.** `MAX_VISIBLE` is 5, variety is a hard
   constraint, and the bench already holds cards. What the queue does after an occupant has
   answered, snoozed and passed over cards for six weeks has never been observed — and
   *"card 6 renders to NOBODY"* is a standing rule about exactly this surface.
4. **The offline outboxes.** `feedbackOutbox.v1` and `door.outbox.v1` exist because of the
   site's permanent premise — no cell, coverage falls off with distance from the house. Nothing
   has ever tested a queue that *sat overnight* and flushed on the next in-range load. A harness
   with a tenure can be put out of range on purpose.

**None of these are visible to a reviewer who loads the page cold.** That is the case for the
harness in one sentence: *it tests the app's memory, and memory is the only thing a fresh-eyes
pass structurally cannot see.*

⭐ **And a fifth, which outranks the four above — added 2026-09-04 with §2's correction.** The
tenure is also the **corpus the expectation lens reads against**. The four reasons here are about
*code paths a fresh instance cannot reach*; this one is about *a question a fresh reviewer cannot
ask*: **does this land for someone who has lived here six weeks and already passed over four of
these?** The accumulated record of what this occupant was shown, tapped and ignored is what makes
that question answerable at all. See §2.

### 3c · Where the instance lives

Three fences, and the machinery for all three already exists.

**(i) Identity — its own synthetic id, NOT the existing one.**
`tools/people.json` already carries `p-harness-v1` / `d-telemetrytest-harness-v1`,
`isTestHarness: true`, `excludeFromEngagement: true` — Paul-approved 2026-08-08 on the condition
*"that data doesn't pollute the rest of the data pool."*

⚠️ **The harness needs a SECOND id, sibling to that one, not a reuse of it.** `p-harness-v1` is
a **wiring prover**: it fires an event to show the event fires, accumulates nothing, and
`check-telemetry.py` reads `isTestHarness` specifically to keep *"we proved the wiring"* apart
from *"a human did this."* A long-lived occupant that answers cards and saves notes for months
is a categorically different record. Folding it into the prover's id would destroy the one
distinction that file was built to hold.

Proposed: `p-harness-tenure-v1`, `isTestHarness: true`, `excludeFromEngagement: true`, plus a
new `isTenureHarness: true` so a tool can tell "one walk" from "a simulated occupancy."

**(ii) Origin — QA only, permanently.** The existing fence has two halves and only one ever
dissolved: on `fernwood-qa.pages.dev` (its own KV namespace, `env=qa`, `kv_canary=qa`, proven by
`tools/qa-write-probe.py`, 8/8) **every path may be walked including POSTs**; on prod the write
paths are **never** safe, because they land in Mom's answer record and no metrics exclusion
covers that. The harness POSTs by design — answering cards *is* what it does — so it is a
**QA-half-only** creature. It never runs against `palekxk.github.io` or the prod Worker. Ever.

**(iii) Estate — its own instance file and its own canon.** The engine now takes
`instance/<name>.json` + canon at build time (`tools/build-viewer.py`). The harness gets its own
instance declaration and its **own** `estateId` — never `est-3c9f1a`. Consequence, and it is the
one that matters: a synthetic confirm answer resolves against *synthetic canon*, so it can never
flip a real plant's `confidence: inferred → verified`.

### 3d · The save file IS the artifact

**A save file that cannot be restored is a mystery blob, not a fixture.** The instance is
therefore a committed, human-readable snapshot, not whatever happens to be in a browser profile:

```
~/Developer/fernwood-private/harness/HARNESS-01/
  tenure.md              # the log: what it did each lap, what it expected, what it found
  state/week-04.json     # localStorage snapshot (all 20 rostered keys) + QA KV seed
  state/week-12.json
  restore.py             # seeds a browser profile + QA KV from a snapshot; --list, --verify
```

- **In the private sibling, not the public repo** — same class as the device register. The
  content is synthetic, but the shape of the state maps 1:1 onto Mom's, and this repo is public.
- **Restorable and disposable.** Any reviewer can drop into "week 6 of an occupancy" in one
  command; anyone can throw the whole thing away and re-run the tenure from lap 0.
- ⚠️ **`restore.py` must refuse to run against any origin whose `/health` does not read
  `env=qa`** — the same refusal `qa-write-probe.py` already implements. A restore that could
  point at prod is a loaded gun; make the gun refuse.

### 3e · The tenure — how it builds up

Laps, not a schedule. Each lap the harness does what an occupant *of that tenure* would do, and
the state it leaves is the fixture the next lap starts from.

| lap | posture | what it exercises |
|---|---|---|
| **0 · cold arrival** | has never seen it; arrives by whatever door a real person arrives by | the setup journey, first paint, what it expects vs. what it gets |
| **1 · first week** | curious, tries things, gets some wrong | capture paths, the queue's first offers, whether anything acknowledges it |
| **2 · month one** | has habits; ignores some things on purpose | `momQueue.offered` growth, the 5-slot cap, ribbon freshness |
| **3 · quarter** | long-lived state, some of it stale | retirement across devices, migration, the 90d cap class of defect |
| **∞ · out of range** | captures away from the house, comes back | the two outboxes, deferred sync, *capture must not lie* |

**Its report is three things and nothing else:** what it expected · what it got · where those
differ. It proposes no fixes and ranks no priorities. It hands hypotheses to the doctrine pass.

### 3f · The harness's profile — and why it has no name

It needs enough circumstance to behave consistently (an agent playing "a harness" will not act
like a first-time occupant), and **no more than that**:

- Reaches the app on a phone, through the same door a real occupant would.
- Ordinary competence: uses apps, doesn't read documentation, doesn't inspect anything.
- Expects a thing that says what's happening at a place. Reads the top; rarely opens what's
  behind a disclosure.
- Volunteers little unprompted; taps what moves it, not what asks it.

⛔ **It has no name and no biography, deliberately.** A plausible first name is exactly the thing
that gets merged into real-person research three months from now, and a biography is exactly the
thing that gets quoted.

### ✅ The naming ruling `[paul-ruled 2026-09-04]` — `synthetic-<demographic>`

**This lane recommended `HARNESS-01`. Paul ruled otherwise, and his form is better:** the name is
the word **`synthetic`** plus **the demographic it is meant to simulate**.

**Why it beats the recommendation, stated because the reasoning is the reusable part:** `HARNESS-01`
achieved *"this is not a person"* only for a reader who had opened this document.
**`synthetic-<demographic>` carries the warning label wherever the id travels** — every log line,
every commit message, every tool output, every stray grep hit six months from now. It is
self-declaring at the point of use, which is precisely the property the designation was reaching
for and did not have.

⚠️ **And the guardrail that must ride with it, ratified as written.** Naming it by demographic
makes it **LOOK like evidence about that demographic** — which is the one thing it can never be.
So §6's rule holds *harder* under this name, not softer: **a hypothesis generator, never evidence
about the group it names, and never consulted where a real record can be read instead.** The name
buys legibility at the cost of a resemblance to authority it does not have; the guardrail is what
pays for it.

⛔ **The demographic itself is NOT chosen here** — see §6's dependency. Until it is, the persona is
referred to structurally, never by a placeholder demographic that would then get quoted as if it
had been decided.

⚠️ **Naming note against `VOCABULARY.md` §4:** `tenant`, `resident`, `user`, `profile` and
*"estate manager"* are all rejected there, for reasons that hold here too. **`harness` survives as
the mechanism word** — the codebase already uses it (`isTestHarness`) and it is the one word that
says *not a person* in its ordinary meaning — but the **identity** is named `synthetic-…` per the
ruling above. Both are schema words: like `estate`, neither reaches a user-facing surface.

---

## 4 · ⛔ Contamination — the seven modes, named

House style in this repo is to enumerate the creep modes rather than assert safety. These are
the ways a synthetic occupant corrupts a real record. **Fences (i)–(iii) close 1–4 structurally;
5–7 are discipline and cannot be closed by code.**

1. ⭐ **A synthetic arrival fires the mom cycle.** *"The loop RESTS; her input fires it."* An
   arrival on `/api/feedback` is the trigger. A synthetic answer that reached the prod Worker
   would fire a lap on a machine's input — the worst failure available here, because it corrupts
   the *trigger* and not merely a number. → Closed by fence (ii): the harness cannot POST to prod.
2. **Synthetic sessions move the engagement gates.** `sessions-quiet` and `offers-passed` count
   sessions and offers. → Closed by `excludeFromEngagement` **and** by fence (ii); belt and braces
   is correct here, because the flag is per-tool and the origin is absolute.
3. **A synthetic confirm flips real canon.** → Closed by fence (iii): its answers resolve against
   its own canon under its own `estateId`.
4. **The ack ribbon covers synthetic input.** The ribbon exists to say *we heard you* and must
   refresh on **her** events. → Closed by (ii); `check-mom-ack.py` reads the prod Worker.
5. ⚠️ **Attribution drift.** The standing rule is *attribute from CONTENT, never from device
   shape* — and since the device register went private, an unmapped record reads UNMAPPED rather
   than being silently attributed. So a harness record must be **self-identifying in its own
   content**, not only by its id. Every synthetic note/answer/turn carries an explicit
   `[HARNESS-01 · SYNTHETIC]` marker in the text itself. If the id is ever lost, the content
   still says what it is.
6. ⚠️ **Its findings get cited as user evidence.** The one that will actually happen, months
   from now, in a document nobody re-checks. → Every harness report opens with the §1 banner, and
   its findings enter `/ux-sweep` **as pass-1-class claims to be adjudicated**, never as
   confirmed findings.
7. ⚠️ **Cross-estate backflow.** Bob's household gets the identical fences, its own `estateId`,
   its own QA origin. A harness is per-instance; there is no shared harness across estates.

⚠️ **Standing caveat on all of the above:** these fences make contamination *structurally hard*,
not impossible, and none of them checks that a harness run was *honest*. The
`check-arrival-dispositions.py` lesson applies — a mechanism can verify a disposition exists and
what attested it; it cannot verify the disposition is true.

---

## 5 · How it runs alongside `/ux-sweep` — and why it cannot replace pass 1

Paul was explicit: *"one additional test."* The structural reason, which is stronger than the
instruction:

- **Pass 1's entire value is that it is un-primed.** The skill is emphatic — *"un-primed means
  un-primed; leak no suspected issues, no backlog, no history."* It sees what familiarity hides.
- **The harness is primed by construction.** At lap 3 it has a tenure, expectations and habits.
  That is not a defect to correct; it is the asset. But it means **the harness can never be
  fresh eyes**, and fresh eyes can never test memory. Neither can be recovered from the other.

**Where it sits (recommended):** the harness runs on **its own cadence as a QA leg**, producing
a tenure report to its private log. `/ux-sweep`'s **pass 2** reads the most recent report as an
input alongside pass 1's findings and adjudicates both.

**Why not "pass 1b" inside the sweep:** the passes share one browser and are strictly sequential
for that reason; the harness carries a loaded session state that would have to be torn down
before fresh eyes arrive. And gating a sweep on a tenure lap couples two clocks that should be
independent. `[verified — the skill's own "sequential agents, one browser" friction]`

**Its relationship to the deterministic gates:** `tools/qa-walk.py` already renders QA headless
at her conditions and returns an **exit code** — that is the deterministic floor and stays
AI-free. The harness sits *above* it and never replaces it: the walk proves the page rendered;
the harness asks whether a resident of six weeks can still find anything. Same as everywhere
else here — **the deterministic thing keeps its non-AI door.**

**What it does NOT do:** substitute for `/mom-cycle` (that dispositions a real person's input) ·
ship anything · rank a backlog · write canon · reach any Mom-facing surface.

---

## 6 · Segments — the demographic is a NAMED DEPENDENCY, not a gap

Paul: *"could also then interface into testing hypotheses about different consumer groups like
older people right especially."*

The mechanism generalizes cleanly — each identity a **segment hypothesis** with its own instance,
its own fences, its own tenure. ⭐ **Plural is now assumed from the start** `[paul-ruled
2026-09-04]`: *"we may continue to evolve this or establish other personas to look through
things."* So the id scheme is built for many from day one rather than one identity that later has
to be split — the same mistake shape as folding this into `p-harness-v1` (§3c).

### ⛔ The dependency, and its blocker

**This document does not choose the demographic, and could not.** Paul ruled it *"should be
defined in conjunction with the customer researcher and our business researcher"* — the
`user-researcher` and `business-analyst` seats.

**That work is BLOCKED, and the blocker is stated here so the gap is not mistaken for an
oversight:** the `business-analyst` seat is **unstamped** — its onboarding interview and resource
gathering never ran. Running the demographic work first would make the interview a *reconciliation
against work it was supposed to shape*, which is the wrong order and hard to undo.

**Ordering (the hub's call, recorded here, not proposed by this lane):**
`stamp the seat → its interview + resource gathering → then the demographic work with both seats.`

⚠️ **Carry-forward for whoever first spawns `business-analyst`:** confirm both preload skill blocks
**actually arrived**. That step has a documented history of failing silently — `examiner-panel` was
born without its preload and nothing detected it. **A symlink that resolves is not proof the block
loaded.**

⛔ **Nothing here waits on that.** The design above is complete and testable without a demographic;
the demographic decides *which* segment the first identity simulates, not whether the mechanism
works. Do not hold this document open for it.

### ⛔ The guardrail — and the naming ruling makes it MORE load-bearing, not less

This is the point at which the idea becomes actively harmful: **a synthetic older reader is a
hypothesis generator and never evidence about older readers.** This project already has *real*
evidence about an older reader — sourced, hard-won, and repeatedly wrong when inferred instead of
measured (the device mapping was backwards for 26 days while reading as CONFIRMED). A synthetic
segment must never be consulted where a real record can be read instead, and its output can never
be tagged above `assumption`.

⚠️ **`synthetic-<demographic>` (§3f) raises the stakes on this paragraph.** A name that states a
demographic *looks* like a claim about that demographic every time it is read — in a report title,
a commit, a finding attributed to it. The name is still right, because it declares its own
synthetic nature wherever it travels. But the two properties arrive together: **the name makes the
fixture legible and makes its output easier to mistake for evidence.** This guardrail is the half
that pays for the other, and it does not get dropped when the demographic is chosen.

---

# ═══ SEPARATE RULING — desktop and mobile review coverage ═══

**This is a review-process rule, not a persona feature.** It travelled in the same memo and is
kept apart on purpose.

> Paul, 2026-09-04 `[transcript-UNVERIFIED]`: *"we need to be sure that these reviews are done in
> desktop and mobile views, and that both views look really good."*

## 7 · What is actually true today — measured, not assumed

`[verified — `viewer.html`, read 2026-09-04]`

- **13 `@media` blocks, and ZERO `min-width`.** ⚠️ *An earlier draft said 14 — that was a raw grep
  hit count including one comment reference. Re-derived deterministically with comments stripped,
  and reproduced independently by the hub: **7 `max-width` (480px and 540px only), 4
  `prefers-reduced-motion`, 2 `hover`.** Not one is a breakpoint above 660px.*
- **The layout is a 660px column, centered.** On a desktop window it is that same column with
  whitespace on both sides. There is no desktop layout; there is a mobile layout on a wide screen.
- **Two live `@media (hover: hover)` blocks** — a tile lift and a glance-row highlight. Both were
  reasoned about *from the phone side*: the 7/29 comment records that every "this opens something"
  affordance was desktop-only and therefore invisible on her iPhone, which is why the chevron was
  added. **So hover states exist, have never been reviewed as a desktop experience, and the tiles
  now carry both a touch affordance and a hover affordance simultaneously.**
- **`/ux-sweep` setup step 4 says "Pick *the* viewport"** — singular. The skill structurally
  produces one-viewport reviews, and its own friction log notes that creating a tab *silently
  resets to desktop width*. Desktop has been **incidentally seen and never deliberately reviewed.**

**And desktop is not hypothetical.** `people.json` records Paul on a laptop and an iPhone; he is a
real daily user of the wide view, and the product-engine direction means future readers will not
all be phone-first.

## 8 · ✅ THE CENTERED COLUMN IS THE DESKTOP DESIGN `[paul-ruled 2026-09-04]`

**The prior question, and how it was settled.** *"Both views look really good"* presumes a desktop
view exists as a **designed** thing. Measured (§7), it did not — desktop was the mobile column
centered in whatever whitespace remained, by omission rather than by decision. That made the
review ruling ambiguous: pointed at an undesigned surface it would have returned twenty findings
that were all one finding wearing different hats. Two options went to Paul — ratify the centered
column, or commission a desktop layout. **He ratified the column.**

**What is now ratified.** Fernwood renders **one layout at every width**: a single ~660px column,
centered, with no breakpoint above it. On a wide screen that is the intended presentation, not a
fallback and not an unfinished state. The reasoning it is ratified on: a single readable measure
suits a field journal, there is no reflow to keep honest, and there is exactly one layout to
maintain — which is the same argument the whole engine/instance split is built on.

**What it binds — three consequences, and they are the operative part:**

1. ⭐ **The desktop review question changes shape.** It is no longer *"where is the desktop
   layout?"* but **"does the centered column read as DELIBERATE at 1440px?"** — which has real,
   answerable sub-questions: the header gradient stretched across a wide masthead · hover states
   that now duplicate touch affordances the tiles already carry (§7) · whether the flanking
   whitespace reads as intentional margin or as a phone screenshot pasted on a desktop · what the
   fixed-position elements (the feedback FAB, the ack ribbon) do when the column is not the window.
2. ⛔ **A sweep may not re-litigate it.** *"The app doesn't use the wide screen"* is now a
   **DELIBERATE-PER-DOCTRINE** verdict in pass 2's vocabulary, naming this ruling — not a finding.
   Fresh eyes will raise it, correctly and unprompted, on the first run; that is pass 2's job to
   adjudicate, exactly as it protected the ratified strip↔card duplication contract.
3. ⚠️ **Ratified is not exempt.** A ratified layout can still be executed badly at a width nobody
   looked at. The ruling settles *what the design is*; it does not assert the design is currently
   well-executed on desktop — which is precisely what §9's wiring exists to find out.

✅ **HOME: `engine/viewer.template.html`, the stylesheet doctrine region** (`3aada23`, Paul's
direct instruction). The ruling is written as **"THE CANVAS — one column at every width,"** sited
as the outermost of the three systems: shape says what a *button* is, nesting says what a *row*
is, the canvas says what the *page* is — because the other two are spending space this one has
decided. Written to the **template**, not to `viewer.html`, which is generated;
`build-viewer.py --check` reads byte-identical.

Two things live in that block and not here, because they only bite at the source: **a `min-width`
block is now a claim that this ruling changed** (a second layout, needing Paul), and the block
states plainly that it is **not tool-enforced** — a lint counting `min-width` blocks would pass
the day someone shipped a bad wide layout without one. The honest check is a human at 1440px,
reached through §9's viewport set.

*This document keeps only the reasoning trail. The contract is at the source.*

## 9 · The wiring proposal — 4 edits to `~/.claude/skills/ux-sweep/SKILL.md`

⛔ **NOT MADE.** Per the lane gate, this lane does not edit the skill. Proposals only.

> ### ⚠️ THIS WORDING IS NOT FINAL — approved in principle, not ratified `[2026-09-04]`
>
> Paul: *"I'm good with approving all of these"* — **conditional on three things**, and until they
> resolve, nothing below is settled text:
> 1. *"as long as we have all this tracked so we can continue to assess how UX sweep works"* — a
>    **measurement** condition. Note the instrument may already exist: the skill's own *"run log —
>    MEASUREMENT (append every run, no exceptions)"*, which **Edit 4 already touches**. The
>    honest answer may be "nothing new is needed," and that is the answer to prefer.
> 2. *"as long as the UX expert approves as well **or we go with their recommendation**"* — ⭐ he
>    **pre-committed to their wording over this lane's** where the two differ. So a reader must not
>    treat the four edits below as this document's final position; they are the version submitted
>    for review.
> 3. *"the process steward should weigh in"* — added separately, on the ritual's structure.
>
> **Both consults were commissioned read-only and write nothing.** Whatever returns is folded or
> rejected *here* before any edit reaches the skill. ⛔ **Do not apply these edits from this
> document as it stands.**

### 📌 Rulings accumulated pending the fold — recorded as they land, not held in a session

*Consults are still returning; the edits below are rewritten ONCE, when all have landed. These are
recorded immediately so nothing lives only in a running window.*

**R1 · The desktop target is the LAPTOP CLASS, not the widest screen** `[paul-ruled 2026-09-04]`.
Asked whether he reads Fernwood on an external monitor: *"I sometimes have hooked up to an external
monitor, but I wanna focus on really my laptop screen and more of the standard display sizes
because that external monitor is really big."*

⭐ **This OVERRULES the ux-expert's "take the widest real width" tiebreaker.** Their argument was
sound on its own terms — the canvas ruling's risks (whitespace reading as unfinished,
window-anchored elements drifting off the column) grow monotonically with width, so the widest
width is the one that can *falsify* the ruling's execution. **Paul's ruling is a SCOPE decision,
not a measurement correction, and scope is his.** The secondary viewport is therefore the **modal
laptop-class width**, read from the record and stamped `[measured <date>]`, with
external-monitor sessions **excluded from the target** — not discarded as bad data.

**R2 · ⛔ THE `deviceClass` READER IS BROKEN — a verified defect, and it corrects a claim this
lane made** `[verified 2026-09-04, three points in the chain]`. Found by `practice-steward`;
re-verified here rather than relayed:

| where | what it says |
|---|---|
| `viewer.html:18547` (and the template) | emits **`deviceClass`** inside `deviceBlock()` |
| `worker/worker.js:2578` | stores the `device` object **verbatim** — no rename in transit |
| `tools/analyze-fernwood.py:150` | reads **`device.get("class")`** — ⛔ **a key that is never sent** |

So `deviceClass` resolves to `None`, and `analyze-fernwood.py:577`'s
`e["deviceClass"] or "unknown"` has rendered **`unknown` for every device on every run since the
field existed.** ⚠️ **The failure is invisible because `unknown` is exactly what a genuinely
unclassifiable device would print** — a plausible-looking table over no data. `deviceId` is read
correctly (`device.get("deviceId")` matches the emitter), so attribution works; **only the class
column is dead.**

⭐ **This corrects an earlier claim by this lane.** It was reported that `analyze-fernwood.py`
"renders a per-device `class` column ✅ readable." **The column renders; it has never contained
data.** The error was reading the renderer and the aggregation without tracing the key back to the
emitter — *the two halves agreed with each other and neither agreed with the source.* Fixing it is
engineering work and is not this lane's; it is a **prerequisite**, because nothing downstream can
be sized by device class until the reader reads.

⚠️ **The consequence to carry, because it follows from a principle adopted in the same breath:**
out-of-target is not out-of-existence. The page still renders at 2560 when he plugs in, and the
canvas ruling's risks are worst exactly there. Per the ux-expert's line — **usage share sizes
effort on POLISH; it does not gate BROKENNESS** — something merely *unoptimized* at external-monitor
width is correctly out of scope, while something *broken* there is still broken. The ruling narrows
what we optimize, not what counts as a defect.

### ✅ FOLDED — the edit set after three consults (ux-expert · practice-steward · engineering-partner)

**All three convergences first, because they agree and that is the signal:** ⛔ **do not type
`1440×900` into the skill.** All three independently reached it. The measured desktop width is
already in the record (`deviceBlock().viewport`, on every batch, read by nothing), and typing a
convention here reproduces the `390×844` defect one reader over — *measured for her, conventional
for him.* **Read it once before this ships.**

**Edit 1 — Setup step 4: a viewport SET, defined BY RELATION.** ⚠️ *Substantially rewritten; my
first draft had a defect that would have silently dropped mobile.*

> *Pick the viewport **set** from the project's real readers: the **primary** (the owner's measured
> conditions) plus **the other class — phone or desktop, whichever the primary is not** — at that
> project's own measured size for it. Each entry carries **width × height × text mode × pointer
> capability**, and each is stamped `[measured <date>]` or `[assumed]`. The project's own
> measured-conditions doctrine outranks any convention here, and it applies to **every** entry in
> the set: a measured primary beside an assumed secondary is the 8/24 defect wearing a second hat.
> Fernwood: primary 414×848 · A+ · touch `[measured]`; secondary laptop-class `[to be measured]`.*

- ⛔ **The defect this fixes.** My draft said *"primary + desktop secondary."* Measured by
  `practice-steward`: **all five operating-layer sweeps already run at 1440×900** — so there the
  primary IS desktop, and my wording yields **desktop + desktop**, a no-op that reads as compliance
  while silently dropping the mobile half of Paul's ruling on the project where mobile is the
  uncovered class. *By relation* fixes both projects with one rule.
- ⭐ **Pointer capability was missing from all four of my edits** (`ux-expert`). The two
  `@media (hover: hover)` blocks key on **pointer, not width** — so reviewing at 414 in a plain
  desktop browser fires hover rules Mom has never seen. **Every past "mobile" pass has been
  reviewing a tile lift and a row highlight that do not exist on her phone.**
- **Fold into the 8/31 log's proposed item (b)** — same line (`:83`), one edit. It also fixes what
  (b) alone would not: (b) adds the clause while leaving the wrong literal `390×844` in the same
  sentence.

**Edit 2 — Pass 1: RESET and re-walk, not resize and re-walk.** *Strengthened.*
Fernwood's instance state carries over between walks — `ackSeen`, `zoneJourney.launcherDismissed`,
`momQueue.offered`, `textSize`, plus every expanded card. The 8/31 sweep's FAB finding was
explicitly *"at rest on first paint"*; that class of finding is **structurally unreproducible** on a
second walk in a warm session, so the second viewport reads clean because the state is dirty. This
repo has already paid for the identical mechanism — the A/A+ harness where *"the A+ frame wrote
localStorage, and every later frame restored it — the instrument agreed with itself and was wrong."*
So: **resize · clear the rostered storage keys · re-navigate · re-walk from first paint**, and
**carry the verified-cleared state in the output.**

**Edit 3 — Pass 2.** (a) and (b) as drafted. **(c) replaced.**
(a) Re-verify each finding *at the width it was made at*; (b) a claim reproducing at one width and
not the other is **labelled with its width**, never stated unqualified — plus *once the column is
the design, the window edge and the design edge are two different places, so every window-anchored
element is re-checked at every width in the set.*

⭐ **(c) — my wording shielded a TOPIC, not a CLAIM, and would have suppressed real findings.**
`ux-expert` named two already in the blast radius, both derivable from source: the **masthead
composition** (`.header::before/::after`, 200px and 160px discs on a full-bleed band whose content
caps at 660px — at laptop width the discs and the gradient's lightest quarter fall outside the
column) and the **feedback ribbon** (`position: fixed; right: 0` — at 414 it occludes the ack
ribbon's tappable phrase; at laptop width it is orphaned out in the flanking whitespace: *same
element, opposite findings, both true*). Replacement:

> **(c) The canvas clause.** Exactly **one** proposition is DELIBERATE-PER-DOCTRINE at desktop
> width: *"Fernwood needs a distinct wide-screen layout, or a breakpoint above the ~660px column."*
> Cite `engine/viewer.template.html` § THE CANVAS — **read the block; do not take a report's word
> for it.** **The clause covers the DECISION, never the EXECUTION.** Before applying it, restate the
> finding as ***"at ‹width›, ‹element› ‹does what›."*** If it names an element, a measurement or a
> behaviour, **the clause does not apply.** Shield it only if it survives no restatement other than
> *"there should be a desktop layout."* **A shielded item is written down, never dropped.** ⭐
> **Three shields in three consecutive sweeps is itself a finding** — either fresh eyes keep seeing
> something the ruling does not cover, or its premise has moved. The premise is falsifiable: a
> reader class the ruling did not consider, or a job the single measure demonstrably fails, is
> **NEEDS-PAUL**, not a shielded item.

⚠️ **Edits 2 and 3(c) are a matched pair — ship together or ship neither.** Edit 2 creates pressure
toward exactly what the ruling forbids: a reviewer told *both views must look really good*, seeing
them differ, will recommend making them the same — which at this product means desktop CSS, means a
`min-width` block, which THE CANVAS defines as a claim the ruling changed.

**Edit 4 — the run log, not only the trail.** *Re-sited.*
My draft put coverage in the **trail** (per-run). A skip recorded only there is invisible across
runs — you would open three 60 KB files to see a pattern. **Paul's tracking condition is satisfied
by one line in the Refinement-log template**, all of it a byproduct of 3(a):

```
viewports: <primary WxH+mode> walked · <secondary> walked | SKIPPED (<why>) · findings by width: N primary-only / N secondary-only / N both
```

After three runs that answers exactly what he asked: *did the second width ever get walked · did it
find anything the first did not · what did it cost.* ⛔ **No duration or effort field** — frictions
absorbs it, and a per-leg timer on a two-agent ritual is a metric nobody fills. ✅ **And the
instrument needed nothing new** — 3(a) is the instrument; everything else is a rollup.

**Edit 5 — NEW. Setup step 1 must reach the ruling.** ⛔ **Without this, Edit 3(c) is unverifiable
and §10's claim that siting the ruling at the source fixed anything is FALSE.** Pass 1 is forbidden
source; pass 2's setup enumerates only `~/.claude/design-principles/*`. So pass 2 would take *the
skill's word* for a ruling it cannot open. One line: *"plus any ratified design contract sited at
the project's source (Fernwood: `engine/viewer.template.html`, the stylesheet doctrine region)."*

**Edit 6 — NEW, and it is a de-scoping.** The desktop leg is a **scoped checklist on pass 2**, not a
second full un-primed pass-1 walk.
- **The reason is structural, not economy:** pass 1's whole value is being un-primed, and §8(2)
  pre-writes the verdict it would reach at that width. A second un-primed walk pays full discovery
  price for a conclusion already written, every run, forever.
- **Pass 2 is already in the browser re-verifying and already holds the doctrine** needed not to
  re-litigate. Its desktop brief is bounded and already enumerated by THE CANVAS: masthead at width
  · hover states duplicating touch affordances · flanking whitespace as margin vs. accident ·
  fixed-position elements when the column is not the window · **plus re-check every CONFIRMED
  pass-1 finding at the secondary width and label it (3a).**
- ⚠️ **The cadence argument behind it, measured:** `check-ux-sweep.py`'s thresholds are 21d / 20
  commits / 3 laps, and **both** Fernwood sweeps overshot — 8/31 ran at 53 commits / 6 laps. Four
  days after that sweep it already reads `owed: true` at 55 commits. **The clock fires ~4× faster
  than the ritual runs; making the ritual heavier widens that gap rather than closing it.**

**What the set deliberately does not do:** add a tablet viewport · gate a sweep on desktop parity ·
imply the widths carry equal weight (a desktop-only finding caps at `major` unless it blocks a job)
· or touch `qa-walk.py` (see below).


---

## 9b · ⛔ What the consults surfaced that is NOT a `/ux-sweep` edit — UNOWNED ROWS

**None of these is this lane's to act on.** Recorded so they do not die with the window; routed to
the hub. Each is verified, not relayed.

1. ⭐ **`analyze-fernwood.py:150` reads `device.get("class")`; the emitter sends `deviceClass`.**
   A **one-word fix**. See R2 above for the full chain. ⚠️ **Fix it for the right reason:** not
   because the share matters, but because *a confident-looking `class` column full of `unknown` is
   worse than no column* — this repo's most-repeated failure class in its own words. Both
   `practice-steward` and `engineering-partner` found it independently; **106 days live**, through a
   device-mapping crisis, a funnel rewrite and a clean-slate re-derivation of `people.json`.
2. ⛔ **DO NOT BUILD a usage-share instrument** `[engineering-partner, and this is the recommendation
   to keep]`. Two real users. The answer is a sentence that will not move for months: *one person
   uses desktop, and he is the builder.* A percentage over a denominator of 2 is theatre, and
   `defer_affordances_pending_signal` governs instruments as much as affordances. ⭐ **The 106-day
   bug is the argument**: a number nobody missed for three and a half months is not a number anybody
   needs. **The gate that would change this is nameable: a third household.**
3. ✅ **DO read the widths once, by hand, before the edit set ships.** `deviceBlock().viewport` has
   shipped on every batch for months and no reader has ever touched it. One read turns the secondary
   viewport from `[assumed]` into `[measured]`, exactly as 414×848 became measured. ⚠️
   **`deviceClass()` cannot do this job and would mislead:** iPadOS Safari sends a Mac user-agent by
   default, so an iPad reads `desktop` — an error running in precisely the direction that inflates
   the number justifying desktop investment. **The field nobody reads is the more honest of the
   two.** ⚠️ Report the *distribution*, never an average: browser zoom moves `innerWidth`.
4. ⭐ **`/design-options` — a LIVE HTML exhibit is preferred over static desktop images**
   `[paul-ruled 2026-09-04: "we kinda prefer that over desktop static images as long as there's no
   huge barrier… that's a change we should examine if it's not already the case"]`.

   **Verified against the tool — it is NOT already the case, and Paul's memory is two real things
   blended:**
   - ✅ `exhibit.py` **does** emit a self-contained `compare.html` that opens in Chrome. That half
     is exactly as he remembers.
   - ⛔ **But its panels are base64-inlined PNGs** — static. `exhibit.py` takes `shot` (a PNG) and
     has no live/iframe mode.
   - ✅ **The INTERACTIVE one he remembers is real and was a one-off**: the 2026-09-04 onboarding
     round used a scratchpad composer (`compose-onboarding.py`) that inlined each screen as a
     **`srcdoc` iframe** in a 414-wide phone frame. The skill's own log already says it is *"worth
     folding into `exhibit.py` as an `--html` mode."* **So the change he is asking for is already
     pre-flagged by the skill against itself; nothing made it recur, so it did not.**

   ⭐ **And for DESKTOP specifically, live is not merely preferred — it is the better medium, and it
   dissolves a problem the consults raised.** The skill's own rule 8 is *never downscale when the
   subject is size*; two laptop-width screenshots side by side on a compare page are unreadable, and
   the subject here **is** width. A live frame at the measured width is scrollable and interactive
   and sidesteps it entirely.

   **The barrier is small, which was Paul's condition.** The capture harness **already loads the
   live app in an iframe** (`<iframe src="/viewer.html">` at 414×815) — a desktop exhibit is that
   harness at a different width, opened in Chrome instead of screenshotted. ⚠️ Two honest costs:
   the one-off composer was ~3.4 MB self-contained (a full-app live frame differs in shape from
   inlined `srcdoc` screens), and its own log records `browser_resize` returning success **without
   resizing, three runs running** — so `innerWidth` must be verified from inside the frame, per the
   rule already written there.

   ⚠️ Separately, `/design-options` is **reachable by name only** — unnamed in the session-start
   block, `MOM-CYCLE-MAP.md` and `/mom-cycle`: *instance five* of this repo's named failure shape.
   ⛔ But **do not give it a clock** — it is decision-driven, not accumulation-driven; a cadence
   would spend exhibit attention on laps with no decision in them.
5. ✅ **Monitor-after needs a recorded PREDICTION, not an instrument.** Every instrument exists
   (`check-telemetry.py --before`, `check-live.py`, the funnel and engagement readers). What is
   missing is something to compare the after-reading *to*. Three lines on the **lap entry** — not
   `RELEASE_NOTES.md`, which is Mom-facing field-journal prose: `predicts:` · `instrument:` ·
   `verified-live:`. ⚠️ **Most predictions will return UNMEASURED at n=1, and UNMEASURED is not
   "it did not work."** The payoff is not statistical: writing the line forces *"could this even be
   measured at our n?"* to be asked **before** the build — which is literally the ask.
6. **`qa-walk.py` stays at 414×848** `[both process and engineering seats agree]`. Its viewport is a
   **contract, not an estimate**; a gate whose threshold reads the record can quiet itself and
   re-baseline instead of failing loudly. ⛔ **And do NOT add a desktop `herConditions()`** — its
   first checks are page-scroll-sideways and elements-past-the-right-edge, which at laptop width with
   a ratified 660px column are **green by construction**. That would ship a control printing
   *"desktop checked, clean"* in a state where *"our check cannot see desktop defects"* prints
   identically. **The honest fix is a stated non-coverage**, in the `exit 3 = UNCHECKABLE, never
   green by absence` idiom this repo already uses.
7. ⚠️ **Two width-anchored contradictions, reported not resolved.** `design-principles/fernwood.md`
   carries *"answer controls above the fold at 414 × A+"* — a principle with **no defined verdict at
   the secondary width**, which pass 2 adjudicates against. And THE CANVAS is sited in `engine/`,
   shared by every instance **by construction**, while its reasoning is Fernwood's (a field journal
   wants one readable measure). **When the condo instance lands, an engine-sited canvas contract
   binds it.** Whether that is intended is Paul's.
8. **`5237293` is still listed "under review"** in `people.json._meta.whatThisInvalidates` — the one
   change known to have shipped on a bad reading. Starting a monitor-after discipline while its own
   counterexample stays open is worth noticing.

⚠️ **Empirical status of rows 2–3:** the width claims are **structurally verified, empirically
unverified.** It is proven that the field is captured on every batch and read by nothing; **no actual
value has been looked at.** No live read was run — network reads against the Worker were outside
this lane's authorization.

---

## 10 · Open items — one left

1. ~~**§2 — the synthetic-Scott artifact was not found.**~~ ✅ **CLOSED `[paul-stated
   2026-09-04]`** — it was never an artifact. It is an **expectation lens** (§2, rewritten), and
   the reason two independent searches missed it is now recorded as the more durable finding.
2. ~~**§3c(i) — a second synthetic identity in `people.json`.**~~ ✅ **CLOSED `[paul-ruled
   2026-09-04]`** — separate identity confirmed, *"because we may continue to evolve this or
   establish other personas."* Plural is assumed from the start (§6). The write itself is
   mechanical and outside this lane's OWNS.
3. ~~**§3f — designation, not a name.**~~ ✅ **CLOSED `[paul-ruled 2026-09-04]`** —
   `synthetic-<demographic>`, overruling this lane's `HARNESS-01`. Reasoning and the guardrail
   that rides with it are in §3f.
4. ~~**§8 — ratify the centered column, or commission a desktop layout.**~~ ✅ **CLOSED
   `[paul-ruled 2026-09-04]`** — ratified, and landed in `engine/viewer.template.html`'s doctrine
   region as **THE CANVAS** (`3aada23`). Nothing outstanding.
5. ⭐ **STILL OPEN — §9, the four `/ux-sweep` edits.** They change how every future review runs,
   so they are Paul's. ✅ Edit 3(c)'s precondition is met: the DELIBERATE-PER-DOCTRINE verdict now
   has a block at the source to cite, so a future sweep can *verify* the ruling it is being held
   to rather than taking a report's word for it. Coordinate with the amendment already proposed in
   that skill's own 2026-08-31 log so the viewport line is edited once.

6. ~~**Sequencing** (§9 wiring before §3 harness).~~ ⛔ **NOT THIS LANE'S.** Taken by the hub — a
   lane sees only its own work and cannot order the run. Recorded here so a reader does not
   mistake its absence for an oversight.

**Carried elsewhere, deliberately not on this list:** the **(B) fork** — an expectation lens
pointed at a *real* reader (§2) — is its own decision, routed to the hub, not folded in here. And
the **demographic** is a named dependency with a stated blocker (§6), not an open question for
this document.
