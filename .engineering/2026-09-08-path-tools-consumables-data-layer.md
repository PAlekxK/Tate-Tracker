# Path evaluation — TOOLS, CONSUMABLES & SOURCING data layer

`engineering-partner · 2026-09-08 · mode: path-evaluation · no code exists yet`

**Scope** (a) tools + consumables as structured data · (b) guides reference rather than restate ·
(c) "can I start this job today?" · (d) generated shopping list · (e) multi-entity aggregation ·
(f) preferred brands / "the go-to" · (g) **the sourcing answer — "what exactly should I buy for this
thing I own?"** · (h) vendor / where-to-get-it knowledge.

**Grounded in** `vehicles.json` + `_meta` · `tools/build-viewer.py --check` ·
`tools/check-data-inline.py` · `tools/fleet_probe.py` · `tools/vehicle-brief.py` ·
`.private/service-records/{TOOLS,AMAZON-PARTS,EMAIL-RECEIPTS}.md` ·
`guides/bolores-door-panel-repair.md` · `guides/blue-thunder-starting-diagnosis.md` ·
`~/Developer/home-record/CLAUDE.md` · `~/Developer/bronco-parts/src/db.py` ·
`~/.claude/skills/fetch-tabs`, `fetch-statement` · `~/.claude/engineering-principles/`.

## ⭐ PAUL'S RULINGS — `2026-09-08`, on the three questions this file left open

Recorded here because this is the file that posed them. **These are decisions, not proposals.**

| Question this file left to Paul | Ruling |
|---|---|
| **Where does the registry live?** ("is the shop record a Fernwood fact or a Paul fact?") | ⭐ **Fernwood `.private/`, built with the CONFIG-SEAM shape** — `paul-decided 2026-09-08`. The recommendation as written. Lives where the evidence and the consumers already are; relocating later is a path change, not a rewrite. ⚠️ **This DEFERS the many-spines question, it does not answer it** — `home-record` and `bronco-parts` cannot reach the registry under this ruling, and that remains a known, accepted limitation rather than an oversight. |
| **Does the garden enter at v1?** | ⭐ **YES, v1** — `paul-decided 2026-09-08`, in his words: *"it's why I said don't scope narrowly."* Overrides the cheaper "vehicles first" path deliberately. **Consequences he accepted:** the garden has ZERO owned-supply rows anywhere in the portfolio and NO application rates exist (`turf.json` carries no quantity strings), so that data is sourced from scratch rather than seeded; and the Track A tone contract must be designed up front rather than retrofitted, because the garden rendering reaches Mom. |
| **Has a seasonal put-away ever cost anything?** (the J4 evidence gap) | ⭐ **YES — a second trip, or a machine missed** — `paul-stated 2026-09-08`. **This PROMOTES multi-entity aggregation from `assumption` to `validated`** and earns it a place in v1. It closes the one gap the user-research pass refused to let the battery saga fill: *"a strong adjacent story is exactly how a weak claim gets laundered."* ✅ **DISCHARGED same day** — Paul gave three recurring failure modes in his own words, `paul-stated 2026-09-08`. ⚠️ Grade honestly: this is **PATTERN testimony, not a dated incident** — his words were *"these are all general examples."* Sufficient to hold the job as real; **NOT sufficient to be cited as a measured event, and no count or frequency may be derived from it.** |

### ⭐ The three failure modes Paul named — `paul-stated 2026-09-08`

They are **not one job**, and only the second is the aggregation claim this was asked about:

| His words | The failure | Maps to |
|---|---|---|
| *"forgotten to replace an oil filter… on a vehicle that has one when I've done the oil"* | **Completeness WITHIN one job** — the sub-item skipped, on a machine that differs from its siblings | ⭐ **J7 — Mom's *"I don't wanna miss any"* job. Paul has it too.** The research had split these performers; this UNIFIES them on one job with two surfaces |
| *"had to go down to Jasper multiple times"* | **Aggregation ACROSS the trip** — the trip taken twice | J4 · `P-08` trip assembler. **This is the claim that was being tested, and it holds** |
| ⭐ *"not had the right tool and then ended up trying to improvise and breaking something"* | **Readiness failure with DAMAGE, not delay** | J3 · `P-09` readiness — but **at a cost class nobody had named until now** |

⭐⭐ **THE THIRD ONE IS NEW AND IT RE-PRICES THE WHOLE THEME.** Every cost modelled up to here was
time, money or a duplicate purchase — all recoverable. **Improvising with the wrong tool destroys
the thing being repaired**, which is unrecoverable and can exceed the value of every duplicate
purchase in the register combined. It also explains a behaviour already in the record without
needing a new theory: the extreme care over a $9.40 tip, and the refusal to run a bond step until
the right solvent was confirmed. ⚠️ **Readiness is not a convenience feature. It is damage
prevention.** No downstream artifact should present it as saving a trip.



| **Do buckets extend over the agronomy data?** (raised late — a "landscaping" bucket Paul thought might resolve plants-vs-weeds-vs-meadow) | ⛔ **SEPARATED — `paul-ruled 2026-09-08`: *"let's separate those questions."*** The bucket layer here is sized to TOOLS, CONSUMABLES AND SOURCING only. Any reorganisation of `plants.json` · `weeds.json` · `zones.json` · `turf.json`'s meadow regime is **its own thread**, routed to the lap-5 backlog-refinement window as a second, deliberately-unscoped seed. ⚠️ **Neither may become a dependency of the other, in either direction** — the stated reason for separating was that this theme is ready to move and must not stall behind a larger taxonomy question. |

### ⭐ ALL FIVE REMAINING DECISIONS RULED — `paul-approved 2026-09-08`

*"I'm good with your recommendation for all these at this point."* Each on the recommendation as
written in §14:

| # | Ruling |
|---|---|
| **Intake floor** | ⭐ **RETURNS-FIRST, and NO volume cap at v1.** Never propose from raw purchase count — it is anti-correlated with satisfaction here. Propose from *purchase → no return → a later use event*, and above all from **returns**. A cap set before a single lap has run is an invented number. |
| **Guide checkboxes** | ⭐ **Strip the ownership CLAIMS; KEEP the task checkboxes.** `- [ ] Degrease both faces` is a worklist item ticked at the bench and stays. `- [x] ✅ OWNED — acetone` is a fact that rots and goes. ⚠️ **Different things wearing the same syntax** — an implementer reading "remove the checkboxes" must not strip the worklist Paul reads on paper in a garage. |
| **`owned: "no"`** | ⭐ **`yes` and `unknown` ONLY at v1.** Add `no` when a specific case demands it; when added it MUST require naming where someone looked. |
| **Preference layer public?** | ⭐ **PRIVATE at v1.** Easier to publish something private than to unpublish something public; it carries its own redaction design; and a preference list is a map of holdings by implication. |
| **`source-a-part` — skill or fleet beat?** | ⭐ **Standalone SKILL, no cross-loop door yet.** Matches how 2026-09-08 actually happened — on-demand, no lap running. Per [[feedback_build_doors_on_measured_demand]]: build the door when the meter says so. |

### ⭐⭐ WHERE THIS IS HEADED — the Almanac chat, `paul-stated 2026-09-08`

*"how this all gets strung together and triggered within the Almanac chat box — you can eventually
ask a question there and it understands, oh, they're trying to fix something, I need to go to the
garage. Oh, they need a part, here's how I source that part."*

**A connection point already exists and is IN BUILD RIGHT NOW.** `.plans/2026-09-03-guru-retrieval-PLAN.md`
— row `BACKLOG.md § A6 · How to evolve Guru's capability`, objective **O2**, `class: engine ·
must-not-diverge`, `stage: build`, `ready: [paul-approved 2026-09-03]`. Its scope line is literally
the architecture Paul describes: **"from digest-stuffing to a core + lookups + retrieval."**

- ⭐ **"Lookups" is the extension point.** A sourcing/registry lookup joins a family that plan is
  already building — not a new mechanism. C6 already treats *"the vault as a lookup"* with a grant map.
- ⭐ **The private-data path is ALREADY RULED** — Guru Q4, `paul-stated 2026-09-03`: the private tier
  **joins, behind a login the box asks for mid-conversation.** The registry lives in `.private/`, so
  that is exactly the door it needs, and it does not have to be invented.
- ⚠️ **The open sub-question inside that ruling is where tools/consumables gets decided:** *which*
  private fields the box may speak. Live now, at step 7.

⛔ **TIMING is the only actionable part:** the lookup shape is being set THIS LAP; a hook for a future
registry lookup either exists in that design or does not. ⚠️ **A NOTE, not a dependency** — the tools
theme does not block on Guru and Guru must not block on it. Do not widen the guru-retrieval build for
a registry that does not exist; the honest ask is only that the lookup family not be closed.

**Still open after this:** whether the eight proposed principles (§15) get drafted for the library.

## ⛔ CORRECTION `2026-09-08` — THE BUCKET LAYER ALREADY EXISTS. Do not mint a rival.

> ### ⚠️ AMENDED SAME DAY — this heading over-claimed, and the over-claim was the same error again
> **§16's handoff note CONCLUSION STANDS: "different axes, don't share the word" is correct**, for
> the reason it gave — **a plant has no owner-purpose**; it is a subject of observation, not an
> asset with a use. What is recorded below is a REAL and USEFUL finding about vocabulary Paul has
> already ruled, **not** a refutation of §16.
> ⛔ **The bad step, named precisely:** `MODULES` bundles **domains** for estate-level switching.
> The tools bucket is **one string with three values on a catalog row**. Verifying that the
> CONTAINER spans both sides proved nothing about the PAYLOADS — `match-the-payload-not-the-container`,
> committed here while documenting that exact rule. Both this window and the lap-5 refinement
> window made it independently within one hour, on the project built to prevent it. **That is the
> most useful evidence this file contains about how hard the problem is.**

**A ruled bundling vocabulary already exists and must be reused rather than re-minted.**
Verified in source, not taken on report:
`tools/momlib.py:320-355`, `MODULES`, `C5 3a`, `[paul-stated 2026-09-03]`.

A module is **a named bundle of domains an estate switches atomically**. The declared bundles:

| module | `what` |
|---|---|
| ⭐ **`motor-pool`** | **"the garage — trucks, cars, bikes, the cart"** |
| **`equipment`** | "power tools and yard equipment — mowers, blowers, saws" |
| **`house-systems`** | "what keeps the house running — furnace, water heater, breaker panel" |
| **`garden`** | "what you tend and fight, and the ground it grows in" |
| **`place`** | "the ground itself — zones, the property record's spatial half" |
| **`wildlife`** | "what visits" |

⭐ **Paul asked on 9/08 for "a logical grouping — call it the garage." He had already built it on
9/03 and written `"the garage"` into `motor-pool`'s own `what` string.** This is the register's
founding failure mode — proposing to buy what is already on the shelf — reproduced by the design
process itself, on the very project meant to prevent it. Note it as evidence, not as an aside.

⚠️ **AND THE COMMENT ALREADY RULES OUT THE PARTITION ASSUMPTION** — the real error, which the
"don't share the word" framing missed entirely:

> *"Membership is NOT a partition — `zone` belongs to both the garden and the place.
> A domain is ON if ANY on-module claims it."*

Precedent for exactly the multi-membership this evaluation was agonising over:
**THREE modules over ONE domain** — `motor-pool`, `equipment` and `house-systems` all claim the
`vehicle` domain and each names the `group` it switches. `[paul-stated 2026-09-03]`:
*"let's call it motor pool … and then just separately we'll have power tools and equipment and
house systems."*

### What this changes

- ⛔ **Do NOT mint rival vocabulary.** Paul has already named these bundles; reuse `motor-pool` ·
  `equipment` · `garden` · `place` rather than inventing garage/landscaping words beside them.
  ⚠️ **But this is a NAMING constraint, not a mechanism ruling** — the tools bucket is a per-item
  field and `MODULES` bundles domains. Do not collapse the two because they share a vocabulary.
- ⭐ **THE REAL OPEN QUESTION, and it dissolves the vocabulary argument rather than settling it:**
  a module's members are DOMAINS, and **tools and consumables have no domain.** MEASURED
  `2026-09-08` off `tools/momlib.py`: `DOMAINS` holds exactly **11** keys — `plant · weed · bird ·
  mammal · amphibian · snake · lizard · insect · fish · vehicle · zone` — and **none** is tool,
  consumable, supply, part or material. So there is no `MODULES` entry to name yet, and the word
  was never the live question. The question is **whether tools and consumables join an existing
  module or need a domain of their own.** Smaller, better-posed, and it does not touch the slices.
- ⚠️ **Paul's 9/08 "garage" spans TWO existing modules, not one** — `motor-pool` (group `vehicle`,
  7) and `equipment` (group `equipment`, 10, where the mowers live). Confirmed independently by the
  lap-5 window. So `motor-pool` is not a drop-in name for what he described.
- ✅ **THE PLACE BRIDGE ALREADY EXISTS AND NEEDS NOTHING BUILT.** `MODULES["place"] =
  {"members": ("zone",), "what": "the ground itself — zones, the property record's spatial half"}`.
  That is exactly the location axis §16's handoff note proposed as the narrow real bridge to the
  agronomy thread — already declared, already named, and precisely **why** the "membership is NOT a
  partition" warning exists, since `zone` is claimed by both `garden` and `place`. If that bridge is
  ever wanted it is a question about **joining `place`**, not about building anything.
- ⚠️ **But Paul's 9/08 "garage" is BROADER than `motor-pool`** — he described *"vehicles, equipment,
  tools and supplies… used to repair and keep engines running,"* which spans `motor-pool` (group
  `vehicle`, 7) **and** `equipment` (group `equipment`, 10). So this is not a 1:1 match, and the
  open question is not *what to call the bucket* but **whether tools and consumables join existing
  modules or need a new domain to be members of.** They have no domain today.
- ✅ **§16's MEASUREMENT survives and is untouched** — same-category machines share ZERO maintenance
  interfaces (Husqvarna ∩ Kobalt = `[]`, one is cordless), different-category machines share four.
  Work is orthogonal to `group`/`category`, so requirements must still be DERIVED, never bucketed.
  The partition ruling above independently confirms it from Paul's own side.

**Two case studies do most of the work here.** The soldering iron is a **fitment failure at the
moment of purchase**. The Blue Thunder battery is a **provenance-and-lifecycle failure after
purchase**. They exercise different halves of the schema and neither alone would have produced the
right design.

---

## 0. The framing

### 0.1 ⭐ The headline product is the SOURCING ANSWER; the registry is what makes it trustworthy

Paul: *"I should've just come to you and been like 'what tips should I get exactly.'"*

That reframes the deliverable. It does **not** reframe the build order, and the reason is measured:
today's sourcing answer was only possible **because `TOOLS.md` already recorded which two irons he
owns.** Without the register, the same session would have made the same mistakes he did. Registry
and sourcing are not alternatives to sequence between — **the registry is the INPUT to the ask.**

What the reframe *does* change is **how small the first slice is** (see §2.1 and §11): the sourcing
ask needed a much thinner registry than a full inventory.

The doctrine split falls out of Paul's own rules with no interpretation required:

| | path | rule |
|---|---|---|
| *"What tips should I get?"* | **ASK — legitimately AI** | judgement question; nothing behind it to reach deterministically |
| *"What mount does my SP23L take? Do I own a 2.4 mm chisel?"* | **DETERMINISTIC — non-AI door** | *if the only way to learn what you own is to ask Claude, it is broken* |
| recording what the ask discovered | **CAPTURE — AI-free** | model proposes, deterministic tool applies, Paul gates |

It is also the accretive-corpus thesis literally instantiated: **generic catalog/web knowledge held
against Paul's ground truth.** Neither half answers the question alone — the web knows every Weller
tip family; only the register knows he owns exactly two irons and which.

### 0.2 Four questions, four truth conditions, four failure modes

The single biggest design risk is fusing these.

| Question | Truth condition | Characteristic failure | Case study |
|---|---|---|---|
| **DO I HAVE IT?** | an acquisition event | wrong in **both** directions | TOOLS.md's 4 misses |
| **DOES IT FIT?** | an interface match | container-vs-payload | soldering tips |
| **WHAT DO I BUY?** | a re-orderable identity + a reason | a tally masquerading as a judgement | drain plugs |
| **WHO HAS IT?** | a vendor + a checked date | a dead end re-derived from scratch | Bronco parts hunt |

(c) readiness, (d) shopping and (e) aggregation are **not features** — they are derived views over
the first two. Readiness and shopping are the *same query with opposite sign*. Building them as
three features is how this becomes three times bigger than it needs to be.

---

## 1. THE SOURCING ASK — shape, gates, and write-back

### 1.1 The worked example, measured

Answering *"what tips should I get"* took ~15 exchanges, 3 web searches and 2 full product-page
reads, and produced: the correct SKU for the digital iron (`WLTSETIR70-5`), a **GATED** answer for
the classic iron, the discovery that JOUNJIP welders are threaded not slip-over, the discovery that
Amazon was pushing a fourth wrong tip as a *"newer model"*, and the discovery that an 80 W welder
kit would have duplicated a welder and mesh already owned.

**Five wrong purchases avoided in one session.** That is the value case, and it is not hypothetical.

### 1.2 Q1 — What is the MINIMUM registry state that makes a sourcing ask reliable?

Today's ask needed exactly two facts: **which irons exist**, and **their tip family.** That's it.
Not levels, not quantities, not prices, not preferences, not vendors.

```jsonc
{ "id": "weller-sp23l", "name": "Weller SP23L Marksman 25W",
  "provides": [{ "iface": "tip-mount", "form": "shank-into-barrel", "dia_mm": 3.0,
                 "thread": "unknown", "confidence": "inferred" }] }
```

> ⭐ **The thin end of the wedge is much thinner than "an inventory": it is a catalog of the ~20
> things Paul owns that HAVE an interface, plus that interface.** Everything else in this document is
> an enrichment of that spine. This is the single most useful finding of the eval and it reorders
> §11.

### 1.3 Q2 — Write-back, and why it cannot be the model writing canon

Today's session generated durable facts that would otherwise be re-derived every time: a verified
ASIN + variant + date, a complete 2×2 trial-fit matrix, a **withdrawn** prior election, a fitment
trap (JOUNJIP threaded), a vendor (Elliott Electronic Supply), and a hard searched-negative (no ATOLS
variant ships a flat tip). **If sourcing cannot write back, the registry decays and every ask starts
from zero.**

But capture stays AI-free. So:

> **The sourcing session PROPOSES a patch; a deterministic tool APPLIES it after Paul's gate.**
> `shop.py --apply proposals.jsonl` validates against the schema and writes. The model never writes
> canon. This is the ratified *agent proposes, main session reviews* pattern, unchanged.

**And the write-back carries the grade it was learned at** — the house grades already exist:

| how it was learned | grade |
|---|---|
| trial fit on the bench, Paul-confirmed | `verified` |
| manufacturer package list / catalog page | `verified` |
| one reviewer who measured (the `#10-24` MT shank claim) | `hypothesis` |
| a forum post | ⛔ **quarantined** — *"a forum may send you to look; it may never tell you what you will find"* |

### 1.4 Q3 — Loop, skill, or conversation? **Position: a SKILL.**

**Not a loop.** A loop is for something *cyclical* that fires on a clock or stimulus and **rests**.
"Source a part" fires when Paul has a problem — it has no resting state to design and no cadence to
re-cadence. Wrapping it in loop machinery is the *"don't wrap finite work in loop machinery"* error,
and it would produce a `sourcing_probe.py` whose only honest verdict is always RESTING.

**Not ad-hoc conversation either** — it recurs, and doctrine wants a definable procedure with human
gates.

**A skill is exactly the shape, and Paul's stack already has two working examples:** `/fetch-tabs`
and `/fetch-statement` — ordered beats, evidence grades, **recorded searched-negatives**, and
verification-by-rendering rather than by HTTP status. *The sourcing skill is `/fetch-tabs` for
parts.*

Proposed beats:

```
0  RESOLVE from the registry what Paul owns and its interface.
   ⛔ REFUSE to proceed if the interface is `unknown` — emit the GATE (beat 5) instead.
   ⭐ This beat alone would have prevented both dead tip orders.
1  STATE the interface question in writing before searching
   ("we need a broad FLAT foot on a 5.2 mm SLIP-OVER rod"), not the product question.
2  SEARCH. Marketplace suggestions are leads, never answers.
3  VERIFY against a manufacturer or vendor-of-record source.
   ⛔ Assert on the payload: does this page name the mount, or just the brand?
4  RECORD searched-negatives with their instrument and date (§8.2).
5  EMIT: a BUY recommendation, a GATE, or a NEGATIVE — plus the proposed write-back.
6  HUMAN GATE. Paul's y/n. Then `--apply`.
```

### 1.5 Q4 — What the ask path does about UNKNOWNS

> ⭐ **`GATED` must be a first-class terminal verdict, and it must name the single cheapest
> measurement that would ungate it.**

Today the honest answer for one of two irons was *"gated on a caliper reading."* That is not a
failure to answer — **it is the answer**, and it is the thing that prevented a fifth wrong purchase.
`vehicle-brief.py` already states this posture: *"it converts a wrong answer into a flagged
uncertainty; it does not produce a right one."*

**The test that makes a gate real:** it must name a **bounded human action**, and satisfying it must
be cheaper than ignoring it.

- ✅ *"Caliper the extracted tip — 10 seconds, answers both questions."*
- ✅ *"One call to (770) 609-3111 answers purchase date AND warranty status."*
- ❌ *"More research needed."* — if the gate can't name a bounded action, the skill hasn't finished
  thinking.

---

## 2. QUANTITY AND DEPLETION — **three** modes, not two

**Verdict: a quantity-tracking model would decay into lying, and the record proves it.** In four
years and **101 dated receipt rows**, the record has never captured a single *decrement*. Every
status token is acquisition-side: `KEPT` · `INSTALLED` · `RETURNED` · `ON SHELF` · `ON ORDER`.

> **Acquisition is externally evidenced. Depletion produces no artifact.**
> Buying generates a receipt. Using the last of the acetone generates nothing.

That is not a discipline problem. The capture path for use-decrements does not exist and cannot be
built. **But the battery case forces a third mode that changes the answer:**

| depletion driver | examples | honest model | why |
|---|---|---|---|
| **none** — durable | irons, heat gun, mower, mesh | `owned: yes/no/unknown` | binary is true |
| **use** | acetone, sandpaper, oil, fertilizer, clips | `level` + `asOf`, **never a count** | no capture path for the decrement |
| ⭐ **time** | **batteries**, 2-part epoxy, gasoline, rubber, adhesives | **age computed from a provenance date + a class-declared expected life** | ⭐ **the driver — calendar time — IS externally evidenced** |

### 2.1 The time class is the one place a computed number is honest

`age = today − acquired.date` is arithmetic over a fact, not a prediction over an empty history.
`expectedLife` is a class fact with a source. So render **`3.5 yrs against a 3–5 yr class life`** and
let Paul decide.

> ⛔ **Compute AGE. Never compute REMAINING LIFE as a promise.** Same posture as the level's
> `asOf` — expose the age, don't predict the outcome.

⚠️ **Provenance must be able to hold a BOUND, not just a value.** The battery's molded case code
`LE010824-V` gives a **floor** — *"cannot be older than its case"* — not a date:

```jsonc
"acquired": { "notBefore": "2024-08", "confidence": "inferred",
              "source": "molded case code LE010824-V, read at 4x, hypothesis" }
```

That single shape retired an entire false line of reasoning in the battery file (*"if it's the 2017
original it's ~9 years old"*). Cheap, and load-bearing.

⚠️ **Live unflagged instance right now:** the J-B Weld syringes (2025-10-17) and 3M EZ Sand
(2026-06-22) on Paul's shelf are 2-part epoxies with shelf lives, and nothing in the record knows.

### 2.2 The winterization use case IS the time class

Decommissioning motorcycles for winter is largely a **battery-tender job**. So Paul's headline
aggregation example (e) and the battery case study are the same domain — which means the time axis
isn't a corner case bolted on, it's the spine of the one workflow he named first.

### 2.3 What stays specified vs. consumed

Quantity is dishonest on the *ownership* side and perfectly honest on the **requirement** side.
*"The DR200S takes 1.0 qt with a filter change"* is a manufacturer fact with a source, already in
`vehicles.json`.

> **Model quantity where it is SPECIFIED, never where it is CONSUMED.**

So (e) works: *"winterizing 3 bikes needs 3.2 qt of JASO MA2 10W-40 — buy 4 qt."* Never *"you have
1.5 qt, buy 2."* **The list answers how much the JOB needs, not how much is missing.**

### 2.4 Deliberately NOT modelled

- **Numeric counts on hand.** No capture path.
- ⛔ **Use-based consumption rates.** Highest-risk item in the proposal. Both mowers carry **zero**
  `serviceHistory` rows (BACKLOG P9); the bikes have almost none. A burn-down over an empty history
  is a *count with no predicate*, and worse, **it reads as measurement** so it carries authority it
  never earned.

### 2.5 The transferable industrial idea

**Two-bin kanban** solves depletion by making the *bin* the record — the empty bin **is** the signal,
no counting, no logging. Paul's version costs nothing: a buy-list on the shop wall. The system should
**receive** that signal and never compute it. Leave the rest of CMMS inventory (reservations,
issue/return, replenishment runs, cycle counts, stockroom locations) — all of it assumes a stockroom
clerk distinct from the technician. Paul is both, and has no stockroom.

---

## 3. THE ABSENCE PROBLEM — already solved in this repo; carry it over

`fleet_probe.py` returns **exit 2 = UNKNOWN, "NEVER read as RESTING."** `vehicle-brief.py --check`
reports UNKNOWN for an unreadable manual: *"a document that could not be checked must never look
like one that passed."* Native precedent, load-bearing.

```jsonc
"owned": "yes" | "no" | "unknown"      // unknown is the DEFAULT
```

- `yes` — an acquisition event exists.
- `no` — **a positive claim requiring its own evidence, exactly like `yes`.** "Searched and found
  nothing" is *not* `no`. The Amazon cancelled-orders gotcha is the measured case: a searched-negative
  on an instrument that structurally cannot see the thing.
- `unknown` — the default. *(The one exception that upgrades an absence to evidence is a properly
  instrumented searched-negative — §8.2.)*

### The trick that makes `unknown` real rather than a hole

A row that doesn't exist cannot carry a grade. So:

> ⭐ **Enumerate from the REQUIREMENT, join to the inventory. Never enumerate from the registry.**

This is the ratified *"Two lifecycles cannot share one dataset"* applied directly: the requirement
list is the complete-enumerated side, ownership is the appended side.

### Readiness output — three buckets, and it must be able to rest

```
READY    every requirement owned:yes                    → exit 0
ASK      n requirements unknown, printed as QUESTIONS   → exit 2
BLOCKED  n requirements owned:no with evidence          → exit 1
```

An unknown produces **one question, once**; Paul's answer writes a graded row. A check that re-asks
every run is `fleet_probe`'s *costly control* — an alarm permanently on is an alarm nobody reads.

### The shopping list has TWO sections, and this is not a style choice

```
BUY (n)        owned:no, or level:out.  Evidenced gaps.
ASK FIRST (n)  unknown.  "Do you have 320-grit? yes → I record it. no → it joins BUY."
```

The record's four documented misses were **three under-reports and one over-report**. Putting an
unknown in BUY reproduces the near-duplicate-purchase failure the register exists to stop. Silently
omitting it reproduces miss #2 (36 sq ft of CLD, invisible for six months). **A two-section list is
the only shape wrong in neither direction** — and the ASK block doubles as the coverage sweep.

---

## 4. IDENTITY AND FITMENT — the crux, sharpened by the battery

> **"Weller tip" names a MARKET. The mount names the INTERFACE.**
> A name match asks *are these the same words?* A compatibility question asks *do these two things
> mate on a shared, measurable interface?* Only the second is answerable.

### 4.1 ⭐ The battery adds a THIRD identity failure: a spec group in the identity slot

The record says `YTX7L-BS` on the vehicle card, in the guide, **and** in the open item. The battery's
own label says `XTAX7L-BS` (Xtreme AGM, Batteries Plus house brand). `YTX7L-BS` is the **JIS size
group** — a *fitment class*, not a product identity. It is a perfectly good fact **in the wrong
slot**.

> ⭐⭐ **Consistency across three surfaces is not correctness — it is one error copied three times.**
> That is the guide-goes-stale problem (§9) with a worked example, and the strongest argument in this
> document for *reference one identity, never restate it*.

**The schema fix makes the bug unrepresentable — two slots, never one:**

```jsonc
// on the VEHICLE (what will fit)          // on the INSTALLED OBJECT (what is there)
"requires": [{ "iface": "battery",         "identity": { "mpn": "XTAX7L-BS",
               "fitmentClass": "YTX7L-BS",               "brand": "Xtreme (Batteries Plus)",
               "confidence": "verified" }]                "confidence": "photo-read ×2, corroborated" }
```

You cannot write the class into the identity slot because there is no such slot. Same trick as §7.2's
preference key.

### 4.2 `provides` / `requires` — the general form

Each assertion is a `{dimension, value, unit, confidence, source}` object in the existing
`vehicles.json` house style.

```jsonc
"weller-sp23l": { "provides": [{ "iface":"tip-mount", "form":"shank-into-barrel",
                                 "dia_mm":3.0, "thread":"unknown", "confidence":"inferred" }] },
"yehveh-flats": { "requires": [{ "iface":"tip-mount", "form":"slip-over-rod",
                                 "dia_mm":5.2, "confidence":"verified",
                                 "source":"trial-fit paul-confirmed 2026-09-08" }] }
```

Compatibility = join on `iface`, then compare **the dimensions that iface declares load-bearing**.
`form` fails *before* diameter is consulted — which is Paul's own amended caliper rule
(*"ask the THREAD question FIRST, then diameter"*).

> ⭐ **The caliper rule is a fitment predicate. The schema's job is to hold it as data instead of as
> prose nobody re-reads at the moment of purchase.**

### 4.3 Interface families — the reusable half, and there are about ten

| iface | dimensions that decide | match semantics |
|---|---|---|
| `tip-mount` | form → then diameter | categorical exact, **then** ±0.2 mm |
| `engine-oil` | viscosity · standard-set · capacity | exact · **subset** (req ⊆ prov) · sum |
| `battery` | fitment class · terminal orientation · CCA/Ah | exact · exact · **≥ threshold** |
| `spark-plug` | thread ø/reach/seat · heat range · gap | exact · exact · settable |
| `thread` | nominal ø × pitch | exact |
| `fertilizer` | N-P-K · form · target | **ratio band** |
| `abrasive` | grit | ⭐ **ordered scale, sequence-aware** |
| `solvent` | active + concentration | **threshold** |

Those semantics differ — exact, subset, tolerance, ordered, threshold — which is precisely why *"a
compatibility field"* cannot work and a per-interface predicate can. ~10 families × 5–15 lines of
Python in one `fitment.py`, with `--selftest` proving each predicate **both ways** (house idiom).

⭐ The `abrasive` row: the sandpaper gap (80/120/220 + 400, **320 missing**) is not a presence bug —
it's an *ordered-sequence* bug. Only a sequence-aware predicate catches *"you can't jump 220 → 400."*

### 4.4 A compatibility answer must be able to say `cannot-tell`, and say why

`fits` / `does-not-fit` / **`cannot-tell (dimension X unmeasured)`** — which feeds §1.5's GATE
verdict directly.

### 4.5 Prior art — what to steal, what to leave

**ACES/PIES (automotive aftermarket).** Steal exactly one idea: the standard splits **the part**
(PIES — what it is) from **the application** (ACES — what it fits), and the application joins a
controlled vehicle-config vocabulary **plus a qualifier database (Qdb)** for conditions the config
can't express — *"fits vehicles with rear disc brakes."*

> ⭐ **The transferable insight is the qualifier axis: fitment is never fully expressible by the
> identity of the two things.** Paul's qualifiers: *"if the mount is threaded," "only at 91%
> concentration," "only if the panel is ABS."*

**Leave:** the four relational databases, XML interchange, the ~100k-row VCdb, brand/part-type
taxonomies, supplier feeds. That machinery exists so ten thousand suppliers can agree **without
talking to each other.** Paul is the only supplier and the only consumer. He needs the *shape*
(item ⟂ application ⟂ qualifier) at ~40 rows, in JSON, with no taxonomy authority.

**CMMS.** Steal exactly one relation: **asset → task → parts list (the BOM)**, which makes (b)(c)(d)(e)
fall out of one query — plus the word **commissioning** (§6.3), a rare case where enterprise
vocabulary earns its keep at hobby scale. Leave work orders, PM engines, criticality, MTBF. Fernwood
already has a *better* scheduling half (`rhythms[]`, `fleet_probe`'s seasonal signal).

**Agricultural input tracking.** Steal the habit of recording an input **by active specification and
rate** — *"46-0-0 urea at 1 lb N / 1000 sq ft"* — because the brand on the bag changes every season
and the spec doesn't. Container/payload arriving independently from a second domain. Leave plot-level
application logs, REI/PHI compliance, lot traceability.

**Grocy / Homebox.** Worth knowing, not worth adopting. Grocy's min-stock → shopping-list is literally
the requested feature, and Grocy is honest that it works because *groceries carry barcodes and get
consumed at a scanner*. Neither is true of a half-used can of acetone. Homebox is durable-goods only:
`{name, location, purchase info, photos, custom fields}` — an inventory with **no fitment concept at
all.**

> ⭐ **Finding: there is nothing off-the-shelf to adopt, and the reason is diagnostic — the market's
> home-inventory tools solve the easy half (what do I own) and none of the hard half (does it fit),
> because fitment is the part nobody generic can model.**

---

## 5. PROVENANCE — the battery's decision-relevant fact, and it is absent

> *"The record carries no purchase or install date."*

For a battery, **age is the single most decision-relevant attribute** — and it is **not recoverable
from receipts**: zero matches for `Xtreme`/`XTAX7L` anywhere in `.private/service-records/`, nothing
in `AMAZON-PARTS.md`, no battery row in `dr200s-2017/EXTRACTED.md`. **Because it was bought in a
store.**

> ⭐ **This is the second independent measurement that a receipts-seeded registry is structurally
> blind to in-store purchases** — the first being the total absence of garden consumables (§7.1).
> Here it has money attached.

So `acquired` is a first-class, gradeable field on the holding, `unknown` is its default, and the
*ask* for it must route to a bounded human action:

```jsonc
"acquired": { "date": null, "vendor": "batteries-plus-969",
              "evidence": "unknown",
              "openQuestion": "q-battery-purchase-date" }
```

---

## 6. WARRANTY, COMMISSIONING, AND VENDOR-HELD FACTS

### 6.1 💵 Warranty is a live asset — and it **reroutes the procedure**

There may be a live 12-month free-replacement warranty. Purchase date + vendor would surface it
automatically. And critically:

> ⚠️ **If under warranty, the load test must happen at Batteries Plus, not an auto-parts counter —
> a warranty claim wants their own tester's verdict on their own paperwork.**

**So a provenance field does not merely inform a buy decision; it changes which procedure runs.**

**Position — model the advisory, do NOT build guide branching.** Rendering conditional prose into a
garage document is a template engine, and a template engine over a 900-line hand-written guide is
over-engineering. Instead:

- `warranty: {term, from, source, confidence}`, derived from `acquired.date` + vendor policy.
- The **readiness output carries an ADVISORY line**: *"⚠️ possibly under warranty to 2025-08 — test
  at the vendor, not a parts counter."*
- The guide's **prose names both procedures with the condition stated**, once, by hand.

95% of the value at 5% of the cost. ⚠️ And the warranty term itself is *"unverified for this SKU"*
from a third-party listing — so it carries a confidence, and a low-confidence warranty produces
**"worth one phone call,"** never **"you're covered."**

### 6.2 ⭐ Commissioning — yes, but ONLY as an interface-declared requirement

The battery's own back panel confirms it is **dry-charge**: it shipped dry, was filled with acid at a
counter, and **required an initial charge after filling** or it was capacity-limited from day one.
So an item can be **OWNED but not correctly COMMISSIONED**, and no ownership register can see the
difference.

**Position: this is real and worth modelling — but a global `commissioned` field on every catalog row
would be over-modelling**, because ~95% of items have no commissioning step and the field would be
pure noise. Make it **opt-in per class**:

```jsonc
// interfaces.json
"battery-agm-drycharge": {
  "commissioning": { "required": true,
                     "step": "initial charge at low current after acid fill",
                     "failureIfSkipped": "capacity-limited from day one; sulfates" } }

// holdings — exists BECAUSE the class demands it
"commissioned": "unknown"
```

`unknown` here is a real question worth asking exactly once: *"did it come sealed in a box, or did
they fill it at the counter?"* — **and answering it explains an entire diagnostic file without
needing a second fault.** Generalizes cheaply: chain tensioning on first run, a tender's mode
setting, torquing a new mower blade.

### 6.3 ⭐ A FOURTH location class for truth — facts held by a VENDOR

The fact that closes battery-age lives at **Batteries Plus store #969, keyed to a phone number**. Not
in Paul's files, not on the object, not in email.

**What the registry records is not the fact — it is the ROUTE to the fact:**

```jsonc
{ "id": "q-battery-purchase-date",
  "question": "purchase/activation date + warranty status for XTAX7L-BS",
  "heldBy": "batteries-plus-969",
  "action": "call (770) 609-3111 with Paul's phone number",
  "cost": "one call", "payoff": ["closes age", "closes warranty"],
  "opened": "2026-09-08", "state": "open" }
```

This row belongs in the **ASK bucket** of the readiness output. It is exactly §1.5's bounded human
action with two payoffs — the shape that actually gets done, versus *"find out when he bought it."*

Four locations for truth, then: **his files · the object itself · a vendor's system · a human's
memory.** Only the first is greppable, and the register should say which one it is waiting on.

---

## 7. THE GO-TO / PREFERRED BRANDS — ⛔ the naive model is falsified

### 7.1 ⭐⭐ Measured: purchase frequency is ANTI-correlated with satisfaction

The hypothesis under test was: *repeat-purchase counts are arithmetic, not inference, so the go-to
falls out deterministically.* **The arithmetic works. The answer it produces is wrong, and wrong in
the worst direction.**

**Corpus: 101 dated receipt rows, `AMAZON-PARTS.md` + `EMAIL-RECEIPTS.md`, 2022-07 → 2026-08.**

| Most-purchased categories | buys | outcome |
|---|---|---|
| **Drain plugs** (M14×1.5, M12×1.25, Dorman 65209, DEEFILL M14.1, M12.1) | **5** | **4 returned**, 1 kept |
| **White dome-light LEDs** (GLOFE, D15, MODIPIM) | **3** | ⛔ **all 3 returned** |
| **Soldering tips** (ET 6-pack, YehVeh flats) | **2** | ⛔ **both dead** |
| **Jump starters** (LIFMOCER, AVAPOW) | **2** | 1 returned as inadequate |

Plus: **SKU-level repeat purchases = ZERO.** Brand repeats are five and all degenerate — **Dorman ×4
(3 of 4 returned)**, Chemical Guys ×3 (three different products, nothing since 2023), 3M ×2, NVX ×2,
Icyhaws ×2 **(one of which never actually happened)**.

> ⭐⭐ **A frequency-derived go-to would elect Paul's most-returned products.** The mechanism is
> obvious in hindsight: **you buy something once when it works, and repeatedly when it doesn't.**
> A purchase row is not an endorsement; in this corpus it is a churn signal.
>
> **This is much worse than sparse data.** Sparse data yields a weak answer. This data yields a
> *confidently wrong* one, which looks like it worked.

**Two further defects in the substrate itself, both measured:**

1. ⚠️ **`EMAIL-RECEIPTS.md` is event-grained, not purchase-grained.** "Dorman 901-302" appears at
   `2025-10-15` **and** `2025-10-21` — order confirmation and shipping notification for **one**
   purchase. A repeat-count over this file counts **notifications, not buys.**
2. **Where a genuine repeat exists it is a fitment distinction, not a preference.** Clips bought
   twice: 50pc for *73-86* (eBay 11/20) and Icyhaws for *87-91*. A brand counter reads that as
   *"he likes clips."*

And decisively, on Paul's own example: **zero soil, fertilizer, mulch or compost rows exist.** Garden
consumables are bought in person; `TOOLS.md`'s coverage warning already says everything non-Amazon is
unswept. A receipt-derived go-to is **permanently blind to the exact domain that prompted the
request.**

> ⭐ **Read: don't build a preference-learner. Build a preference-RECORDER, and let any tally be a
> PROPOSER that must clear a floor before it is allowed to speak.**

### 7.2 ⭐ The preference key is the JOB, not the brand — and the record proves it

Verbatim, `bolores-door-panel-repair.md:494`:

> *"**Dorman was checked and rejected** despite being a brand Paul has used twice on Bolores
> (742-251, 38424): their panel retainers are 2–15-review blister packs with 1–5 units in stock.
> **Wrong product shape for a bulk reclip.**"*

**Same brand, trusted and rejected, in the same file, on the same day, with reasons.** A row storing
`preferred_brand: Dorman` returns a wrong answer the first time it is asked about clips.

Note also *what the reason actually is*: not product quality — **pack shape and vendor stock depth.**
So the reason must be typed too, or the row is unreadable in six months.

**Position — invert the key. The job is the key; the product is the value:**

```jsonc
{ "for":    { "shape": "panel-retainer-clip",
              "use":   "bulk re-clip, 87-91 Bronco door" },
  "prefer": "icyhaws-50pc",
  "grade":  "ruled", "source": "paul-stated 2026-06",
  "against":[{ "item":"dorman-retainers", "reason":"fit-for-shape",
               "why":"blister packs of 1–5 units; wrong pack shape for a bulk reclip" }] }
```

> ⭐ **You cannot ask "what brand does Paul prefer?" because the schema has no slot for it.** Same
> trick as §4.1's class/identity split: make the wrong question unrepresentable rather than
> documenting that it's wrong.

Granularity, restated with this correction — the discriminator is **whether the thing has a fitment
interface**:

| level | legitimate when | example |
|---|---|---|
| **SKU / re-orderable id** | anything with an interface — tips, filters, plugs, clips, adhesives | `WLTSETIR70-5` |
| **product line + the spec that matters** | fungible-within-spec consumables where the SKU drifts and the spec doesn't | *"a JASO MA2 10W-40, 1 qt"* · *"the bagged soil conditioner, spec X, at store Y"* |
| **brand** | ⛔ **never a value on its own** — only a tiebreaker note inside a job-keyed row | *"prefers 3M for abrasives"* |

⭐ The **product-line** row saves the garden case, and it is where the ag lesson lands. It also forces
`whereBought` (vendor + store SKU or aisle note) as first-class — because for the entire garden half
**the vendor IS the identity** and no ASIN will ever exist. Which settles the capture path: not
receipts, but **a photo of the bag → Paul types the name once.** Deterministic, AI-free, correct on
the *first* purchase rather than the fourth.

### 7.3 ⭐ The schema needs an INTAKE state — a tally's only legitimate output is a question

Given §7.1, the preference layer needs **two datasets, not one** (two lifecycles again):

```
preferences.json         RULINGS. grade: ruled. The answer. Drains never; supersedes.
preference-intake.jsonl  PROPOSED QUESTIONS. append-only. Drains on Paul's answer.
```

`"You've bought this three times — is it your go-to?"` is the value.
`preferred: <most-bought>` is the failure.

An answered intake row is **gone**; a declined one is `declined` and **never re-proposed** — which
makes "never nag" structural rather than a promise.

**And the intake generator must be return-aware, or it generates exactly the wrong questions.** Given
the anti-correlation, the honest generator is nearly the *inverse* of a frequency count:

- ⛔ **never** propose from raw purchase count;
- ✅ propose from *purchase → no return → a subsequent use event*;
- ⭐ **propose from RETURNS**, which is the higher-signal half:
  *"You returned three different white 6000 K dome LEDs — is 'no white interior light in the Bronco'
  a ruling?"*

> ⭐ **The strongest deterministic signal in this corpus is the RETURN, not the purchase.** And it
> points at rejections — the half nobody writes down. That preference exists in the record today
> **only as a pattern of returns**, and is stated nowhere.

### 7.4 FOUR rejection kinds — and only two are preference

| kind | closed by | **scope of the verdict** | preference? |
|---|---|---|---|
| `fitment` | a caliper / a trial fit | **this SKU × this interface. NEVER the brand** | ❌ no |
| `fit-for-shape` | reading the listing (pack size, cut size, stock depth) | this SKU × this *use* — a **sourcing** fact | ⚠️ partly |
| `performance` | **use only** | this SKU × this job | ✅ yes |
| ⭐ `mechanism` | understanding *why* | ⭐⭐ **a whole material/chemistry class** | ✅✅ highest value |

> ⭐ **Design rule: a rejection's SCOPE is a property of its KIND, and the code must derive scope from
> kind rather than letting the author choose.** Otherwise a `fitment` rejection leaks upward and
> **poisons Weller — the brand that owns the one iron Paul actually wants to use.**

- **`mechanism` is the highest-value kind because it generalizes to products nobody has bought.**
  *Armor-All silicone → fisheye → therefore any silicone dressing, forever, including ones that
  don't exist yet.* That is a rule about the world, not about a product. Same class: *mineral spirits
  is never the last wipe before bonding*; *lacquer thinner is a blend, so a positive says less.*
- ⚠️ **`performance` outranks published specs and the code must say so.** The LIFMOCER **advertises
  3000 A** and the kept AVAPOW **1500 A** — *the spec sheet ranks them backwards from how they
  performed.* **The sourcing skill must be forbidden from "correcting" a performance rejection with
  catalog data.**

### 7.5 ⭐ "Never re-decide by ACCIDENT" — not "never re-decide"

Paul correctly **withdrew a settled election today** (the mesh-weld tip). A preference store that made
a settled choice hard to *deliberately* reopen would be worse than none.

- **Rulings supersede, never delete** (his outbound-record idiom). The withdrawn ruling is kept with
  its reason. Today's `⛔ WITHDRAWN 2026-09-08` prose is exactly this, done by hand.
- ⭐ **Forced substitution is an EVENT ABOUT THE WORLD, not a revision of the preference.** The 9/05
  sandpaper run came home 80/120/220/**400** because the shelf had no 320:

```jsonc
{ "acquired": "3m-cubitron-400", "against": "abrasive-320-requirement",
  "substitution": { "forced": true, "reason": "out-of-stock",
                    "gapRemains": true, "on": "2026-09-05" } }
```

> ⛔ **Absorbing a substitution into the preference is how a shelf shortage becomes a permanent
> belief** — and it would also silently close the 320 gap, which is still open.

---

## 8. VENDOR / WHERE-TO-GET-IT — the scarce knowledge for a 1989 truck

> For a 1989 Bronco, **the scarce knowledge is often the VENDOR, not the part.** Knowing Blue Truck
> Parts makes `DPPRK87` — brackets *engineered for the '87–91 panel specifically* — is hard-won
> research no catalog search reproduces cheaply.

Evidence already in the repo, and note how scattered: **Blue Truck Parts** (`DPPRK87`, order
`06-14809-51927`) · **LMC** (an entire catalog in `manuals/text/`) · **TAP Plastics** (ABS cut-to-size,
*"small pieces, both thicknesses — verified in stock; don't buy a 4×8 sheet"*) · **Polyvance**
(`2045-10`, *"industry standard"*) · **Icyhaws** (correct Ford `N801925-S`/`N802900-S`) · **Elliott
Electronic Supply** (only retail source found for Weller MT tips) · **Batteries Plus** (sole holder of
the DR200 battery's purchase history).

### 8.1 Q1 — Entity or attribute? **Position: a first-class but THIN entity.**

What earns it is not the vendor's identity — it's the vendor's **capabilities** and the **facts it
holds**, neither of which can hang off a purchase:

- *TAP cuts to size* — true independent of any purchase.
- *Batteries Plus holds purchase history keyed to a phone number* — true **before** any purchase is
  recorded here, and it is the only route to a fact Paul needs.
- *Elliott is the only retail source found for MT tips* — a fact about the **market**, not a purchase.

~10–15 rows. Keep it thin — **no order history (that's the holdings ledger), no catalog mirroring, no
stock sync:**

```jsonc
{ "id":"tap-plastics", "name":"TAP Plastics", "url":"…",
  "capabilities":["cut-to-size ABS sheet, small pieces"],
  "holdsFactsAbout":[], "caveat":"don't buy a 4×8 sheet",
  "checked":"2026-08-28", "staleAfter":"P180D" }
```

### 8.2 ⭐⭐ Q2 — SEARCHED-NEGATIVES: the highest-value, least-obvious piece

*"A lot of research"* means most of the work produced **dead ends**, and a dead end is expensive to
re-derive and recorded nowhere. The record already reaches for this by hand — *"3M 05895 is sold out
everywhere now"*, *"the older kit is discontinued"* — and Paul's stack already has the formal concept
(`/fetch-tabs` records searched-negatives on the file's own face; `/fetch-statement` keeps them **with
their date**).

> ⭐ **This is the one kind of absence that IS evidence** — because it has a *predicate*: who looked,
> where, with what instrument, when. That is exactly what the Amazon cancelled-orders gotcha lacked.
> It is the only way to distinguish **"never looked"** from **"looked, and it's gone."**

```jsonc
{ "for":"flat tip for ATOLS welder", "at":"manufacturer package list",
  "on":"2026-09-08", "result":"does-not-exist",
  "instrument":"ATOLS package contents, all variants",
  "confidence":"verified" }
```

⭐ **The `instrument` field is mandatory, or the row is worthless** — a negative from an instrument
that cannot see the thing is the failure this whole record keeps re-learning.

**And the four results decay differently — this is the rule that stops a searched-negative from
becoming a false absence:**

| result | example | decay | may suppress a re-search? |
|---|---|---|---|
| `does-not-exist` | no ATOLS variant ships a flat tip; no Weller tip is flat | **near-permanent** (manufacturer fact) | ✅ yes |
| `discontinued` | 3M `05895` | **permanent-ish**, monotone | ✅ yes |
| `out-of-stock` | *"verified in stock"* inverted | ⚠️ **rots in weeks** | ❌ **must expire** |
| `not-found` | a search that came back empty | ⚠️ says as much about the search as the world | ❌ **weakest; must expire** |

### 8.3 Q3 — Decay, and the `nextLook` idiom already exists

`fleet_probe.py`, verbatim: *"`deferred` + `nextLook` is how a physical check RESTS without a
schedule… a `deferred` item with no readable `nextLook` [is] just a nicer way to forget."* And an
unreadable date raises **UNKNOWN**, never a pass.

Apply it directly: every vendor fact and every rotting searched-negative carries `checked` and
optionally `recheckAfter`. **A vendor fact with no `checked` date is not a fact.**

⚠️ One asymmetry: *capability* facts (TAP cuts to size) decay over years; *stock* facts decay in
weeks. So `staleAfter` belongs on the **fact's class**, not as a global threshold.

### 8.4 Q4 — Paul as SELLER: note it, don't design for it

`~/Developer/bronco-parts` (parked) resells 100–300 Bronco parts, so parts knowledge runs both
directions. **One thing is nearly free and worth flagging; one is a hazard.**

- ✅ *Nearly free:* if the catalog's identity is `{mpn, fitmentClass, interfaces}`, bronco-parts'
  free-text `fitment` column could later read the same `interfaces.json`. **Mechanism graduates, data
  stays home.** A note, not a design.
- ⛔ *Hazard:* **"what I own" and "what I'd sell" must never be the same rows.** A part listed for sale
  and a part on the shelf have opposite lifecycles — one drainable, one durable. *Two lifecycles, one
  dataset*, again.

---

## 9. THE GUIDE-GOES-STALE PROBLEM

**Measured right now, not hypothetically.** `guides/bolores-door-panel-repair.md`:

- **line 66** — *"clip kit — OWNED … **+ ×2 MORE ON ORDER (2026-08-28)**"* → `TOOLS.md` miss #4:
  **that order was never placed.**
- **lines 582–583** — *"✅ mesh path stocked"* → `TOOLS.md` **withdrew exactly this on 2026-09-08.**

Plus §4.1's `YTX7L-BS` restated correctly-looking across **three** surfaces and wrong on all three.
The door-panel guide has been hand-patched with `WITHDRAWN`/`corrected` notes at least five times in
ten days. **It is losing this race**: N guides, one register, every register change is N edits, and
nothing triggers them.

### But "reference by id and render" is not simply right — three things break

1. **The ownership lines are not only ownership.** Line 63 is ~400 words of hard-won *reasoning* — why
   the stapler can't do mesh, why wattage isn't the spec, the JOUNJIP trap. Regenerate that block and
   you **delete the thinking** — exactly what *"Generated for anything that must track a mutable
   filesystem; **hand-written for the why**"* exists to prevent.
2. **Guides are read on a phone in a garage**, and by Claude. `{{tool:weller-sp23l}}` is worse for both
   if the render step didn't run.
3. ⚠️ **`guides/` is PUBLIC; the registry is private.** A rendered guide bakes private ownership state
   into a tracked file. The guide already knows — line 470: *"the order numbers live in `.private/…`,
   not here — this repo is [public]."*

### The answer: two zones, one marked generated block, **plus a drift-lint**

```markdown
<!-- STATUS BLOCK — GENERATED from the shop registry. Do not hand-edit. -->
| Requirement                               | Have it?                        | As of |
| broad-flat plastic-weld tip, 5.2 slip-over| ❌ NO — no owned iron mounts it  | 09-08 |
| ABS sheet 1/16"                            | ✅ yes (paul-stated)             | 09-08 |
| 320 grit                                   | ❓ unknown — ask                  | —     |
<!-- END GENERATED -->
```

Prose below stays hand-written and **stops carrying `- [x] ✅ OWNED` markers entirely.** The guide
declares `requires: [ids]` in front-matter; the block renders from that + the registry.

**The load-bearing half is the lint, not the renderer.** `check-guide-status.py` (sibling of
`check-data-inline.py`) fails when:

- a generated block is older than the registry's `lastUpdated`; **and**
- ⭐ the **prose** zone contains ownership vocabulary — `OWNED`, `ON SHELF`, `ON ORDER`, `on hand`, a
  `✅` adjacent to an item name — because that vocabulary now belongs to the block.
  **This is the rule that catches today's live contradictions; a renderer alone would not**, since the
  stale claims sit in prose the renderer never touches.
- Same check asserts the **public-repo redaction boundary**: the block renders **states only — never
  order numbers, ASINs or prices.**

**Residual, named rather than papered over:** this only works if each guide's `requires` list is
maintained. A new step needing a new tool, with nobody adding it, still goes silent.

---

## 10. ⚠️ CROSS-SPINE OWNERSHIP — options only; this one is Paul's

**Measured constraints:** `Tate-Tracker` is **PUBLIC** (Pages; `viewer.html` built + deployed), with
`.private/` gitignored. `home-record` is **LOCAL ONLY, no git remote ever** (its own CLAUDE.md).
`bronco-parts` is SQLite + parked. The registry's contents — what Paul owns, order numbers, ASINs,
prices — are a burglary shopping list and a spending record. **It stays private in every option.**

| Option | Shape | For | Against |
|---|---|---|---|
| **A** | in `Tate-Tracker/.private/` | zero new infrastructure; the `.private/` seam works; the check/build idiom is right there; **fastest to value by far** | Fernwood becomes de-facto owner of a non-Fernwood thing; garden + Mead St supplies inside a "Tate Mountain field journal"; strains the engine/instance split now that Fernwood generalizes to N estates — a personal tool registry is not an estate fact |
| **B** | own local-only repo (`~/Developer/shop-record`) | matches the many-spines grain — the subject is *Paul's durable stuff*, serving all three properties, belonging to none; clean handling class; precedent for cross-repo in-place reads (`photo-organizer` reads `vehicles.json`) | a real new repo: CLAUDE.md, backlog surface, one more thing to go stale, one more portfolio-map row; absolute cross-repo paths are brittle and path drift has burned him (7/09) |
| **C** | mechanism → `~/.claude/tools/`, data stays home | literally *"Only the mechanism graduates; the data stays home"*; decouples where CODE lives from where DATA lives | ⛔ **defers rather than answers**; and that same principle says promote on rule-of-three, not anticipated reuse — today there is **one** consumer |
| **D** | stays in Fernwood, exposed via a declared read seam (`shop-export.py --json`, like `household-export.py`) | consumers depend on an interface, not a layout; export can drop prices/order numbers | two artifacts to sync = a new drift surface, which *"a ledger earns its existence"* warns about |

### What the decision actually hinges on (stated, not answered)

> **Is the shop registry a Fernwood fact, or a Paul fact?**
> If garden consumables at Tate *and* paint supplies at Mead St both belong in it, it is a Paul fact
> and a per-estate repo will chafe within months. If in practice 90% is fleet-and-Tate, A is free and
> B is ceremony.

That is a question about how his life is shaped, not about his code. Per standing memory
([[project_many_spines_architecture]] — *measured and unsolved*), **I am not picking.**

**Two things I assert regardless:**

1. ⛔ **Do not copy rows between repos.** Reference by id; one owner. *(SSOT per record + a ledger
   earns its existence by answering a different question, not holding a different copy.)*
2. ✅ **Cheap hedge, take it now:** build in **A's location with C's shape** — data file plus a
   `tools/` reader that takes the registry path as an argument with a default. A later move to B, or
   promotion to C, becomes a **path change, not a rewrite.**

---

## 11. THE PATHS

| # | Path | For | Against | Verdict |
|---|---|---|---|---|
| 1 | **Extend `vehicles.json`** | zero new files; rides existing build + `--check` | tools are fleet-generic → duplicated across 23 entries or homeless; **garden has no vehicle**; the file is **public** | ❌ reject |
| 2 | **Just structure `TOOLS.md` better** | no code | the measured failure mode **is** hand-maintained prose drift | ❌ reject (its prose must survive — §12.8) |
| 3 | **One flat `shop.json`** | simplest thing that could work | fuses durable / consumable / preference / vendor lifecycles into one dataset — what *"two lifecycles cannot share one dataset"* forbids; first thing needing a rewrite | ⚠️ tempting, don't |
| 4 | **Thin files + one reader, requirement-enumerated** | one lifecycle and one writer per file; readiness/shopping/aggregation are three flags on **one** query; extends to garden with zero schema change; matches the house idiom exactly | more files than one; guides must gain front-matter | ✅ **RECOMMEND** |
| 5 | **SQLite** (the `bronco-parts` pattern) | real joins, which fitment wants | not diffable, not hand-editable, not greppable — **breaks the future-Paul-with-Claude property every other Fernwood record has**; at 40–100 rows JSON wins on every axis he values | ❌ reject |

### Recommended shape — Path 4, in Option A's location with Option C's shape

```
catalog.json          WHAT things are.    identity {mpn, fitmentClass} + provides/requires.
interfaces.json       HOW fitment is decided. ~10 rows; also declares commissioning + staleAfter.
holdings.json         WHAT I have.        acquisition events, provenance (bounds allowed),
                                          level+asOf, commissioned, substitutions.
preferences.json      WHAT I buy.         job-keyed RULINGS. supersede-never-delete.
preference-intake.jsonl  proposed questions. append-only, drains on Paul's answer.
vendors.json          WHO has it.         thin: capabilities, facts-held, checked/staleAfter.
searched-negatives.jsonl  WHERE I looked and did NOT find it. instrument + result + date.
open-questions.jsonl  ROUTES to facts held elsewhere (vendor, object, human memory).
guides/*.md           front-matter requires:[]  ← the BOM. The enumeration source.

tools/shop.py                 THE NON-AI DOOR.
                              --owned <iface> · --fits A B · --readiness <guide>
                              --shopping <guide…> · --ask · --apply <proposals> · --selftest
tools/check-guide-status.py   the drift-lint (block staleness + ownership vocabulary + redaction)
skills/source-a-part/         the ASK path. Beats 0–6, §1.4. Proposes; never writes canon.
```

**Why this is right for Paul specifically** — it is the *same* idiom he already maintains: JSON canon
+ `tools/*.py` reader + `check-*.py` linter + `--selftest` proving both directions + exit 0/1/2 with
UNKNOWN distinct + a skill for the procedural half. **Nothing here is a new pattern to learn or a new
dependency.** The learning value sits in the *fitment predicate* and the *searched-negative decay
rule* — both genuinely new and both transferable.

---

## 12. WHAT I WOULD BUILD FIRST — revised by the sourcing reframe

The reframe **changes the first slice** (§1.2): the sourcing ask needs a *thinner* substrate than the
readiness check, and it is the higher-value product.

### Slice 1 — the fitment spine (one afternoon)

`catalog.json` with **only the six objects in today's trial-fit matrix** — SP23L, WLSKD7012A, ET
6-pack, YehVeh flats, ATOLS, MT1 — each with one `provides`/`requires` assertion; `interfaces.json`
with **one** family (`tip-mount`); and:

```
python3 tools/shop.py --fits yehveh-flats weller-sp23l
  → does-not-fit  (form: slip-over-rod vs shank-into-barrel)
python3 tools/shop.py --owned tip-mount
  → weller-sp23l (3.0mm, thread UNKNOWN) · weller-wlskd7012a (WLT IR70 sleeve)
```

> ⭐ **Why this slice:** Paul has already produced the ground truth by hand — the complete 2×2
> trial-fit matrix, `paul-confirmed`. **The tool's acceptance test is reproducing a result he
> established on the bench.** That is a real falsifiable test on real data, and it is the exact input
> the sourcing ask consumed today.

### Slice 2 — the `source-a-part` skill

Beats 0–6 (§1.4), with **beat 0's refusal** and the **GATED verdict** (§1.5) as the two non-negotiable
gates, emitting proposals for `--apply`.

### Then, in order

3. `--readiness <guide>` over `bolores-door-panel-repair.md` + `requires:` front-matter.
   ⭐ First run should print `BLOCKED — no owned iron mounts a broad flat tip` **while the guide still
   says "✅ mesh path stocked."** One command, thesis proved.
4. `--shopping` — same query, opposite sign, **two sections**.
5. The generated status block + `check-guide-status.py`.
6. `preferences.json` — hand-type Paul's **existing** rulings (303 not Armor-All; mineral spirits never
   the last wipe; order by ASIN; Dorman rejected for retainers). **No derivation.**
7. `searched-negatives.jsonl` + `vendors.json` — backfill today's dead ends while they're fresh.
8. Provenance + time-depletion (§2.1) — battery, epoxies, fuel.
9. Garden rows — proves it is not a vehicle feature.
10. **Multi-entity aggregation LAST** — union the requires-lists, sum on the *requirement* side. Cheap
    once the BOM exists; a schema exercise before it.

---

## 13. WHAT I WOULD DELIBERATELY NOT BUILD

1. ⛔ **Numeric quantity-on-hand and USE-based consumption rates.** No capture path; predicts from an
   empty service history; **and a burn-down reads as measurement.** Highest-risk item here.
   *(Time-based age in §2.1 is a different thing and is fine.)*
2. ⛔ **Automatic promotion of an observed preference to a ruling.** §7.1 shows it would elect his
   most-returned products.
3. ⛔ **Conditional/branching guide rendering** for the warranty case. An advisory line does 95% of the
   job (§6.1); a template engine over a 900-line garage document does not.
4. ⛔ **A commissioning field on every item.** Opt-in per interface class only (§6.2).
5. ⛔ **Barcode / scanner capture.** Grocy needs it; Paul's shop won't sustain it.
6. ⛔ **A price / spend layer.** `TOOLS.md` already ruled it: *"an ownership register, not an accounting
   one."* Don't re-import a decision he made.
7. ⛔ **Live stock/availability sync.** A scrape that rots. Model it as a dated searched-negative with
   an expiry instead (§8.2).
8. ⛔ **Any generic taxonomy** (part types, categories, brand authority). ~10 interfaces, hand-written.
9. ⛔ **A UI / viewer card.** The registry is **private**; the viewer is **public**. A separate decision
   with its own redaction design.
10. ⛔ **Migrating `TOOLS.md`'s prose into JSON.** The prose **is** the *why* and it is excellent — the
    JOUNJIP trap, the caliper rule, the Amazon endpoint gotchas. Extract the ~40 machine-answerable
    facts; **leave the reasoning where it is.** Two zones, same as the guides.
11. ⛔ **A sourcing LOOP.** It has no resting state (§1.4). A skill, not a cycle.

---

## 14. ⚠️ PAUL'S DECISIONS, NOT MINE

1. ⭐ **Where the registry lives — A/B/C/D (§10).** Many-spines is measured and unsolved; standing
   instruction says don't build a fix without him. The sub-question that decides it: **is the shop
   record a Fernwood fact or a Paul fact?**
2. **Whether garden consumables enter at v1** or after the fleet half proves out.
3. **The intake floor and which signals generate questions** (§7.3) — I propose returns-first and
   explicitly *not* frequency. A threshold invented before a lap has run.
4. **Whether guides keep `- [x] ✅` ownership checkboxes at all.** I recommend removing them entirely.
   They are his documents and he reads them in a garage.
5. **Whether `owned: "no"` is worth capturing**, given how much evidence it costs to earn. It may be
   that `yes` and `unknown` are the only states his life produces.
6. **Whether the preference layer is eventually public.** It is the one piece that could be.
7. **Whether `source-a-part` is a skill he invokes or a beat inside an existing fleet flow.**

---

## 15. Principles this surfaced (proposed — NOT added to the library)

Offered for Paul's ruling; nothing written to `~/.claude/engineering-principles/` without it.

1. **Model the state the world can produce, not the state you wish it logged** *(cross-project)* —
   where an event leaves no artifact, a field tracking it decays to fiction. Model the coarse state the
   world *does* evidence, stamped `asOf` so its age is visible. Corollary: where the driver is calendar
   time, the driver **is** evidenced — compute age, never remaining life.
2. **Enumerate from the requirement, join to the inventory** *(cross-project)* — a record that does not
   exist cannot carry an "unknown"; only enumerating from the demand side makes absence representable.
3. **A compatibility question needs an interface, not a name** *(cross-project)* — the operational form
   of `[[reference_match_payload_not_container]]`: declare `provides`/`requires` on a named interface
   with load-bearing dimensions and explicit match semantics. **Corollary: give a spec-group and a
   product-identity separate slots, so writing one into the other is unrepresentable.**
4. **An observation may propose a ruling; it may never become one** *(cross-project)* — a tally that
   auto-promotes is a tally wearing a judgement's clothes. **Corollary measured here: in a purchase
   record, frequency is a churn signal — the RETURN carries more preference information than the buy.**
5. **A negative record must carry its reason, and its scope is derived from its kind**
   *(cross-project)* — fitment / fit-for-shape / performance / mechanism reject at different scopes;
   letting the author choose the scope lets a fitment failure poison a brand.
6. **A searched-negative must name its instrument, and expire by result-kind** *(cross-project)* — it is
   the one absence that is evidence, and only because it carries a predicate. `does-not-exist` and
   `discontinued` may suppress a re-search; `out-of-stock` and `not-found` must expire.
7. **A substitution is an event about the world, not a revision of the preference** *(cross-project)* —
   absorbing a forced substitution into a ruling turns a shelf shortage into a permanent belief, and
   silently closes a still-open gap.
8. **A gate must name a bounded human action, or it is not a gate** *(cross-project)* — "caliper the
   tip," "one phone call"; never "more research needed."

---

## 16. BUCKETS — the grouping layer `[appended 2026-09-08, after Paul's ruling block]`

Paul: *"is there a way to identify a logical grouping — call it the garage… that may make sense to
group from a user-experience point of view, a hierarchy point of view, and maybe even **data
retrieval** for that fleet repair or troubleshooting skill."*

The third motivation is the load-bearing one: **a bucket as a RETRIEVAL SCOPE** — the sourcing or
troubleshooting ask wants the machine, engine-side tools, automotive consumables and the vendors who
stock them, and emphatically **not** the fertilizer. That is a precision-and-context-budget concern,
not navigation.

### 16.1 ⛔ MEASURED: the existing `category` axis is orthogonal to work — proven, not asserted

Requirement sets computed from each machine's own `maintenance` block (`n/a` values excluded):

| machine | `category` | requirement set |
|---|---|---|
| Husqvarna Z254F | `lawn-care` | fuel · oil · oilFilter · airFilter · fuelFilter · sparkPlug · 2 blade sets · 2 belts · keys |
| **Kobalt KM2040X** | **`lawn-care`** | battery · batteryStorage · blade |
| Echo PB-7910T | `lawn-care` | fuel(50:1) · airFilter · fuelFilter · sparkPlug |
| **Stihl MS 290** | **`equipment`** | fuel(50:1) · airFilter · fuelFilter · sparkPlug · bar · chain |

```
same category (Husqvarna ∩ Kobalt),  shared work → []                                    ⛔ DISJOINT
diff category (Echo ∩ Stihl),        shared work → [airFilter, fuel, fuelFilter, sparkPlug]
```

> ⭐⭐ **Two machines in the SAME category share ZERO maintenance interfaces. Two machines in
> DIFFERENT categories share four.** `group`/`category` does not predict what work a machine needs.
> This is not a hierarchy problem — **it is proof the two axes are empirically independent**, which is
> the strongest possible argument that the bucket is a *different axis*, not a refinement of the
> existing one.

### 16.2 ⚠️ Correcting Paul's overlap read — right about supplies, wrong about equipment

He is **right** that garden *consumables* barely overlap: fertilizer, soil amendment and seed share
nothing with acetone and ABS rod. He is **wrong** that overlap is minimal overall, and the record
says so:

- **Seven `lawn-care` machines**, of which **five are engine-maintained** (Husqvarna, Echo PB-7910T,
  Echo PB-250LN, Homelite blower/vac, Homelite trimmer) and two are battery (Kobalt, EGO).
- **Plus two chainsaws** (`category: equipment`) that are landscaping-purpose engines.
- **So ~7 landscaping-purpose machines draw garage-shelf consumables** — engine oil, spark plugs,
  50:1 mix, bar-and-chain oil, stabilizer.

> ⛔ **The overlap is not minimal; it is seven machines wide, and it is exactly the set his headline
> job touches.** Winterizing is *precisely* the case where garden-domain machines need garage-domain
> consumables. Do not soften this.

⭐ A sharper way to say it: **2-stroke mix, bar oil and fuel stabilizer are landscaping-PURPOSE,
garage-SHELF consumables.** That single sentence is why purpose and place must not be one field.

### 16.3 ⭐ HOW MANY AXES — the word "garage" is doing three jobs at once

That conflation is the container/payload error in miniature, and naming it is the ruling.

| # | axis | question | valued | where it comes from | build? |
|---|---|---|---|---|---|
| 1 | **what it IS** | `group` / `category` | single | ✅ exists in `vehicles.json` | **leave alone — do not extend `category`** |
| 2 | ⭐ **what it's FOR** — *Paul's bucket* | garage · landscaping · household | **single** | hand-assigned, ~stable | ✅ **cheap, do it** |
| 3 | **what WORK it needs** | which interfaces it consumes | **many** | ⭐ **DERIVED from `requires[]`** | ✅ **free — already paid for by §4** |
| 4 | **where it physically IS** | shelf / room / property | single + `asOf` | hand-captured, **decays** | ⚠️ **skip at v1** |

**Paul's refined "landscaping bucket" is axis 2 — PURPOSE — and purpose is the better single-parent
than place**, because it does not move. A thing's shelf changes; what it is *for* does not. That
avoids the `asOf` decay problem that sinks axis 4 (things move and nobody logs the move), and it is
more meaningful than axis 1, which §16.1 just proved is orthogonal to work.

### 16.4 ⭐ The load-bearing motivation needs NO bucket at all — retrieval scope is derived

This is the most useful finding in this section: **the most expensive-sounding of Paul's three
motivations is the one already paid for.**

A job's retrieval scope = *everything that `provides` an interface the job's targets `require`, plus
the vendors who stock it.* Run against the real data, that scope:

- **automatically excludes the Kobalt** from an engine-oil query — it declares no `engine-oil`
  requirement. No human has to remember to exclude it.
- **automatically includes the Stihl alongside the Echo** on a 50:1-mix query, *across the category
  boundary that a bucket filter would have honoured and been wrong about*.
- **automatically excludes fertilizer**, because nothing in the job's requires-set names that
  interface.

> ⭐ **Derive the many-to-many; store only the single-valued.** A hand-maintained multi-membership tag
> set is a hand-maintained thing, and hand-maintained drift is this record's entire documented failure
> mode. *(Ratified: "Generate the derivable; drift-lint the rest.")*

So the strict-hierarchy-vs-tags question resolves as **neither**: tags are the right *semantics* for
axis 3 and the wrong *storage*. Single-parent for axis 2; computed for axis 3.

### 16.5 Testing Paul's hypothesis — *items get one home; JOBS span buckets*

| case | test | verdict |
|---|---|---|
| **Winterization** | Husqvarna's home = `landscaping`; the job is garage-shaped and pulls oil, plug, stabilizer, tender from `garage` | ✅ **holds** — machine has one home, job crosses |
| **Door panel** | every item's home = `garage` | ✅ holds trivially (single-bucket job) |
| **Mom's fertilizer zones** | fertilizer, spreader, zones all `landscaping` | ✅ holds trivially |
| **Heat gun** — plastic repair AND paint stripping | ⚠️ **this is not a test of the hypothesis.** Both are *garage* jobs. The heat gun has one home and serves two jobs in it — that exercises item↔**job** multiplicity (already handled), not item↔**bucket** multiplicity | ✅ not a falsifier; category error in the test |
| **Bar oil / 50:1 mix / stabilizer** — the one I went looking for | landscaping-purpose, garage-shelf. Home = `garage` (what shape it is, where it lives); reached by landscaping jobs through the job | ✅ **holds — and this is the case that best shows why it works** |
| **Chainsaws, Generac** | home genuinely ambiguous (land work vs shop-maintained; house-serving vs engine-maintained) | ⚠️ **ambiguous, not falsified** — see 16.6 |

> ⭐ **Verdict: the hypothesis HOLDS on every case, and for the right reason.** It separates *where a
> thing lives* (single-valued — a fact about the world) from *what a job needs* (many-to-many — a fact
> about work). **It dissolves the strict-vs-tags tension rather than trading against it**, because the
> multi-membership moves onto the JOB, which already has to name multiple items anyway. The
> coordinator's read is correct and it is better than the place-based axis I was going to propose.

**One refinement it needs, or it reintroduces the drift failure:** a job must not hand-list its items.

```jsonc
{ "job": "winterize-motorcycles",
  "targets": ["dr200s-2017", "drz400s-2001"],          // NAMED
  "needs":   "<derived from each target's requires[]>", // ⭐ DERIVED — never hand-listed
  "plus":    ["fuel-stabilizer", "battery-tender"] }    // NAMED, job-specific extras
```

**Targets named · requirements derived · extras named.** The many-to-many that crosses buckets is
*mostly computed*, so it cannot go stale the way a hand-tagged bucket would.

### 16.6 Why single-parent is SAFE here — the property that makes ambiguity affordable

The chainsaw's home is genuinely arguable. Single-parent forces a call; the call is somewhat
arbitrary. That is acceptable, and the reason is structural:

> ⭐ **The bucket is allowed to be slightly wrong because nothing load-bearing reads it.**
> Retrieval is by **interface** (§16.4). Shopping is grouped by **store** (§16.7). The bucket serves
> navigation and a coarse default filter — both forgiving. If a load-bearing query ever starts
> reading the bucket field, that is the signal the design has drifted.

### 16.7 Retrieval cost, honestly accounted

The coordinator asked what a job-spanning model costs when the query walks one hop instead of
filtering one field.

| | field filter | one hop (derived) |
|---|---|---|
| work | one pass, n≈100 | two passes, n≈100 |
| wall time | microseconds | **microseconds — unmeasurable at this scale** |
| **precision** | ⛔ returns the Kobalt's battery for an oil job; misses bar oil for a chainsaw job | ✅ correct by construction |
| legibility | one line a human holds in their head | three — **mitigated:** `shop.py --scope <job>` prints the resolved set, so nobody walks it by hand |

**The real cost is legibility, not compute, and it is bought off by printing the resolved scope.**
The benefit — precision — was the stated motivation. Endorse the hop.

⚠️ One honest limit: a derived scope is only as good as the interface declarations. A machine with a
thin `requires[]` gets a thin scope. **That is a feature** — the incompleteness is *visible and
fixable*, versus a hand-tag that is confidently wrong. But it means axis 3 does not work until the
fitment spine has coverage, which is slice 1 regardless.

And one thing derivation genuinely cannot do: a purely **associative** grouping with no interface
basis — *"the stuff I keep in the truck."* If Paul wants that, it is a stored set and it must be
**explicitly its own thing** (`kits`), never conflated with axis 3.

### 16.8 Does the bucket scope the SHOPPING LIST? ⛔ No — and this one matters

Store and bucket are different groupings, and giving the bucket this job would be actively harmful.

> ⭐⭐ **Bucketing the shopping list by domain would MANUFACTURE the very failure the aggregation
> feature exists to prevent.** A Home Depot run buys acetone (garage) *and* soil conditioner
> (landscaping). Split by domain, that becomes two lists — and the second trip is exactly the cost
> Paul just ruled is real (*"a second trip, or a machine missed"*, `paul-stated 2026-09-08`).

**The rule, stated once:**

> **The bucket is an INPUT FILTER on what enters the list. The STORE is the OUTPUT GROUPING.**
> Never the same field, never the same role.

⭐ Note this strengthens the case for `vendors.json` early: store-grouping needs `whereBought`
populated, and for the garden half the vendor **is** the identity (§7.2). Garden-at-v1 pulls
`vendors.json` forward.

### 16.9 ⛔ SCOPE BOUNDARY + HANDOFF NOTE — the agronomy data is a SEPARATE THREAD

⭐ **`paul-ruled 2026-09-08`: "let's separate those questions."** Any reorganization of Fernwood's
agronomy data — `plants.json`, `weeds.json`, `zones.json`, `turf.json`'s meadow regime — is **out of
scope for this theme** and gets its own backlog thread.

**Three things that ruling binds, stated so a future reader can check them:**

1. **The bucket proposal above is NOT contingent on the agronomy question.** §16.1–16.8 stand on
   `vehicles.json`'s 23 assets and the tools/consumables registry alone. Delete this subsection and
   nothing upstream changes.
2. **The schema is NOT sized to accommodate it.** `bucket` is one string on a catalog row with three
   values (`garage` · `landscaping` · `household`). There is no extension point, no namespace, no
   reserved vocabulary held open for plants. **If the other thread needs something, it should design
   it — not inherit a shape bent speculatively toward it.**
3. **The `landscaping` bucket means "an owned asset whose purpose is land work."** It does **not**
   mean "the landscaping domain." That distinction is the whole of the handoff note below.

#### Handoff note to the agronomy thread — *is this taxonomy coherently extensible there?*

**No — different axes, and sharing the word would be the container/payload error again.** The tools bucket
answers *"what is this owned asset FOR, so I can find it and service it."* The agronomy data answers
*"what is this living subject, where is it, and what regime governs it."* A plant has no
owner-purpose; it is not equipment, it is a **subject of observation** in a field journal.
`zones.json` is spatial, `turf.json` is a management **regime**, `weeds.json` is an identification
taxonomy, `candidates.json` is prospective. **Extending "landscaping" over them would make one word
mean *purpose of an owned asset* on one side and *domain of a living subject* on the other — the
container/payload error again, at the largest scale in the portfolio (314 KB of `plants.json` alone),
and with a Mom-facing rendering surface attached.** So: **two different groupings wearing one name —
do not share the word.**

⭐ **But there IS a narrow, real bridge, and it is a different axis than the one being proposed:**
`zones.json` is a **place** vocabulary, and the agronomy data is already organised spatially. If the
tools registry ever wants axis 4 (*where is it*, which §16.3 recommends skipping at v1), `zones.json`
is the natural vocabulary to borrow — and **that** would be coherent, because place genuinely is one
axis across both. **So the live cross-thread question is a PLACE question, not a bucket question.**

⚠️ **That bridge is a note for the other thread to consider on its own schedule, not a dependency of
this one.** This theme skips axis 4 at v1 (§16.3) and takes on no obligation toward `zones.json`.

### 16.10 What this adds to the build order

Slots into §12 with **no new slice** — it is two small additions to existing ones:

- **Slice 1 (fitment spine):** add `bucket` (one of `garage` · `landscaping` · `household`) to each
  catalog row. One string. No new file, no new structure.
- **After slice 3 (`--readiness`):** add `shop.py --scope <job|machine>` — the derived retrieval slice,
  printed. This is what the `source-a-part` skill's **beat 0** consumes, and it is the whole of Paul's
  load-bearing motivation.
- **Not built:** axis 4 (physical location), a stored many-to-many tag set, and any bucket-grouping of
  the shopping output.

⚠️ **One flag for a different owner:** if a bucket ever *renders* to a reader, its labels are
user-facing copy on a surface that reaches Mom (per the Track A tone contract in the ruling block).
That is `content-steward`'s call, not mine.

---

**Principle #9, proposed alongside the eight in §15:**

9. **Store what is single-valued; derive what is many-to-many** *(cross-project)* — when a grouping is
   genuinely one-to-many (a thing's home, its purpose) store it and accept that it may be slightly
   wrong, but only if nothing load-bearing reads it; when it is many-to-many (what work an item
   serves), **derive it from the relation that already exists** rather than hand-maintaining a tag set.
   A hand-maintained multi-membership is a hand-maintained thing, and hand-maintained drift is the
   failure mode. **Corollary: an input filter and an output grouping are different roles and must never
   share a field** — grouping a shopping list by domain instead of by store manufactures the second
   trip the feature existed to prevent.
