---
type: test-fixture-design
class: SYNTHETIC — not user research
project: tate-tracker
last_updated: 2026-09-04
evidence_level: "n/a — this document describes a FIXTURE, not a person. It contains no user evidence and may never be cited as any."
lane: "C (fictive test user), parallel run 2026-09-04 PM ET"
sources:
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

## 2 · The Hillyer model — ⚠️ I could not find it

Paul's 1:47 memo: *"I think we've made like a synthetic Scott Hillyer in the Hillyer case for
example so something to model after that."*

**Searched and not found.** `~/LocalProjects/hillyer-case` contains **no synthetic-Scott
artifact** — no persona file, no simulator, no "read this as Scott would" agent. What is there
is the opposite class of thing, and the distinction matters enough to state:

| artifact | what it actually is |
|---|---|
| `Hillyer_Case_Master/SCOTT_DISAGREEMENTS.md` | a register of **what the real Scott actually disputed**, sourced to his marked-up PDF, his voice memo and his texts. Track-2 `[Scott]` — his account, logged, never adjudicated. Real evidence. |
| `_analysis/CRIB_2026-07-26_scott-sitdown.md` | a **prep sheet** anticipating his reactions in a real meeting — *"hand him the phone and stop talking."* Built from his record; not a model of him. |

Both are **models of a real person derived from that person's own words** — the exact inverse of
a synthetic persona. So there is no artifact to copy, and I have not invented what it probably
was. `[verified — filesystem search + read, 2026-09-04]`

**One thing from that corpus IS transferable**, and this design takes it: the Hillyer record's
governing discipline is that **a lower-grade source may never clear a higher-grade one** —
`[Scott]` is never a twin, OCR never clears Track-1, *"a source that derives from the record
cannot clear the record."* Translated here: **a synthetic occupant may never clear a question
about a real one.** That is §1's line 2, and it is the only inheritance claimed.

⚠️ If Paul knows of an artifact this search missed, that is the thing to read — this section is
a report of absence, not a conclusion that none exists.

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
thing that gets quoted. It carries a **designation**: `HARNESS-01`.

⚠️ **Naming note against `VOCABULARY.md` §4:** `tenant`, `resident`, `user`, `profile` and
*"estate manager"* are all rejected there, for reasons that hold here too. **`harness` is used
because the codebase already uses it** (`isTestHarness`) and it is the one word that says
*not a person* in its ordinary meaning. It is a schema word — like `estate`, it never reaches a
user-facing surface.

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

## 6 · The extensibility hook — noted, NOT built

Paul: *"could also then interface into testing hypotheses about different consumer groups like
older people right especially."*

The mechanism generalizes cleanly — `HARNESS-02`, `-03`, each a **segment hypothesis** with its
own instance, its own fences, its own tenure. **Do not build this now.** One harness has to earn
its keep first, and the whole design rests on accumulation that does not exist yet.

⛔ **And the guardrail to write down before anyone builds it,** because it is the point at which
this idea becomes actively harmful: **a synthetic older user is a hypothesis generator and never
evidence about older users.** This project already has *real* evidence about an older user —
sourced, hard-won, and repeatedly wrong when inferred instead of measured (the device mapping was
backwards for 26 days while reading as CONFIRMED). A synthetic segment must never be consulted
where a real record can be read instead, and its output can never be tagged above `assumption`.

---

# ═══ SEPARATE RULING — desktop and mobile review coverage ═══

**This is a review-process rule, not a persona feature.** It travelled in the same memo and is
kept apart on purpose.

> Paul, 2026-09-04 `[transcript-UNVERIFIED]`: *"we need to be sure that these reviews are done in
> desktop and mobile views, and that both views look really good."*

## 7 · What is actually true today — measured, not assumed

`[verified — `viewer.html`, read 2026-09-04]`

- **14 `@media` queries. Not one of them is a breakpoint above 660px.** They are `max-width: 480`
  / `540` (mobile narrowing) plus `hover` and `prefers-reduced-motion` feature queries.
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

⚠️ **This document is not the durable home for the ruling.** It is a test-fixture design; a
ratified layout contract belongs where renderers and reviewers actually read it — the doctrine
block at the top of `viewer.html`'s stylesheet (where the affirmative-grammar and strip↔card
contracts already live) and/or `~/.claude/design-principles/`. **Out of this lane's OWNS** —
flagged to the hub as a placement decision, carried here in the interim so the ruling is not
homeless.

## 9 · The wiring proposal — 4 edits to `~/.claude/skills/ux-sweep/SKILL.md`

⛔ **NOT MADE.** Per the lane gate, this lane does not edit the skill. Proposals only.

**Edit 1 — Setup step 4: a viewport SET, not a viewport.**
> *Pick the viewport **set** from the project's real readers: a **primary** (the owner's measured
> conditions — Fernwood: 414×848 at A+) and a **secondary desktop** (1440×900). The project's own
> measured her-conditions doctrine outranks any convention here.*

⚠️ **Fold this into the amendment already PROPOSED in the skill's 2026-08-31 log** (item (b), the
her-conditions line), so that one line is edited once rather than twice by two hands.

**Edit 2 — Pass 1's method line.** Add: *review at **both** viewports; resize and **re-walk** —
never infer the second from the first.* Grounded in the skill's own hazard that tab creation
silently resets width: what looks like desktop coverage today is an accident, not a pass.

**Edit 3 — Pass 2, three clauses.** (a) Re-verify each finding *at the width it was made at* —
a claim that reproduces at one width and not the other is **labelled with its width**, never
stated unqualified. (b) The coherence sweep gains one question: *does this hold at both widths?*
(c) ⭐ **The ratified-contract clause, now that §8 is settled:** *"there is no desktop layout / the
app doesn't use the wide screen"* is **DELIBERATE-PER-DOCTRINE**, naming the 2026-09-04 ruling.
Desktop findings are adjudicated against **"does the centered column read as deliberate here?"** —
never against a desktop layout that was decided not to exist.

**Edit 4 — Trail + run log.** The method note records **both** viewports; a run that reviewed one
**records that the other went unreviewed**, rather than letting silence imply it passed. That
posture is not new — it is the skill's own launcher rule, reused verbatim rather than re-minted.

**What this deliberately does not do:** add a third viewport (tablet), gate a sweep on desktop
parity, or imply the two widths carry equal weight. Mom's conditions remain primary; desktop
stops being invisible.

---

## 10 · What needs Paul

1. **§2 — the synthetic-Scott artifact was not found.** Does he know of one this search missed?
   The design does not depend on it; the request to model after it does.
2. **§3c(i) — a second synthetic identity in `people.json`** (`p-harness-tenure-v1`,
   `isTenureHarness`). It touches an attribution file with a history of costly errors; it should
   not be added by a lane.
3. **§3f — designation, not a name.** Recommend `HARNESS-01` with no biography. If he wants a
   name, it must be obviously non-real — never a plausible first name.
4. ~~**§8 — ratify the centered column as the desktop design, or commission a desktop layout.**~~
   ✅ **SETTLED `[paul-ruled 2026-09-04]` — the centered column IS the desktop design.** What
   remains is **placement, not the decision**: the ratified contract needs a durable home a
   renderer or a reviewer actually reads (`viewer.html`'s stylesheet doctrine block and/or
   `~/.claude/design-principles/`), which is outside this lane's OWNS. §8 carries it in the
   interim.
5. **§9 — the four `/ux-sweep` edits**, coordinated with the amendment already proposed in that
   skill's own log. Edit 3(c) now depends on the §8 ruling and should not ship without it having
   a durable home — a DELIBERATE-PER-DOCTRINE verdict that cites a ruling no principle file
   carries is a verdict the next sweep cannot verify.
6. **Sequencing.** Prod is frozen and Mom's feedback is held. Nothing here is urgent, and lap 0
   of a tenure costs real time. Recommend the wiring (§9, cheap, immediately useful) lands well
   before the harness (§3, a build).
