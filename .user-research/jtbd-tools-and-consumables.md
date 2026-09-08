---
type: jtbd
project: tate-tracker
job_set_id: tools-and-consumables
track: B (fleet & equipment) — with two jobs crossing into Track A
last_updated: 2026-09-08
evidence_level: mixed — graded per claim; see each card
sources:
  - .private/service-records/TOOLS.md (register + its COVERAGE preamble)
  - .private/service-records/AMAZON-PARTS.md (receipts substrate)
  - guides/bolores-door-panel-repair.md (a guide that consumes tool/supply state inline)
  - guides/blue-thunder-starting-diagnosis.md (the provenance/lifecycle case)
  - guides/drz400-connector-repair.md
  - vehicles.json (schema v3 — the stated parity target)
  - cycle/requests.jsonl (Track B's inbound door)
  - CLAUDE.md (tone contracts; the 2026-09-07 fertilizer relay)
  - Paul, voice-dictated scope, 2026-09-08
status: DRAFT — not confirmed by Paul. Feeds a backlog proposal.
---

# Tools & Consumables — the job set

⚠️ **This repo is PUBLIC.** No order numbers, account identifiers or prices appear
below. Where the evidence is a private row, the row is cited by file, not quoted.

⚠️ **These are DRAFT cards.** Ten jobs, none of them ratified. Evidence grades are
`assumption | inferred | validated` per the standing rule; a claim that cannot be
tagged is not made.

---

## 0. The finding that reorders the set

**Every recorded miss happened at a screen. Every fact that would have prevented it
lives on an object in another room.** `[validated]`

- The register read *"no soldering iron"* while two sat in the shop. The Home Depot
  station never was a receipt — it entered as a cart photograph, then as `paul-stated`.
- One iron had a broken tip jammed in it, so **its mount was physically unreadable**
  even standing in front of it.
- ABS sheet stock read `❓ no receipt found` for two months and closed on one sentence
  from Paul.
- `TOOLS.md`'s own extension procedure ends: *"Then ask Paul — no receipt sweep will
  ever show a store purchase, a gift, or a hand-me-down."*

The register is authored **where the decision is made** and never **where the truth
is**. That is not a coverage gap more sweeping closes; it is a missing capture moment.

⭐ **Consequence:** a registry seeded from the receipts substrate inherits the exact
defect that produced four wrong tips. Receipts say **what arrived**. They cannot say
**what fits**, **what was rejected**, or **when it was bought in a store**.

---

## The evidence-source axis — four classes, four loss modes

| Axis | Question | Truth lives | Lost how | Recoverable by |
|---|---|---|---|---|
| **OWN** | Do I have it? | the shelf | never captured | a sweep, or asking Paul |
| **FIT** | Does it work with what I have? | the object | never measured | a caliper |
| **PREFER** | Which one, and why not the others? | **Paul's head** | never written | **nothing — it is gone** |
| **SOURCE** | What exists that would work? | the market | n/a — always outside | search |

⚠️ **And a fifth location the record reaches for and the axes above do not cover: a
VENDOR holds facts about Paul's own property** (purchase date, warranty, what a shop
actually did). See J10.

⛔ **FIT and IDENTITY are not the same answer, and confusing them is invisible.**
`YTX7L-BS` is recorded as the DR200S battery's part number across three surfaces,
self-consistently. It is a **JIS size group**, not an identity; the battery's own label
reads `XTAX7L-BS`. **A battery ordered against the group would have fit** — nothing
fails at purchase. It fails months later at a vendor counter, where the number Paul
holds is not the number they can look up. `[validated]` — label read from a
high-resolution photograph, corroborated by a second independent photograph.
Third recorded instance of `[[reference_match_payload_not_container]]` in this repo.

---

## The chain — how the jobs actually connect

```
J3 finds the gap  →  J9 sources it  →  J2 vetoes at checkout  →  J6 records what arrived
                          ↑                    ↑
                    J8 (the go-to) short-circuits both when a ruling already exists
J10 recovers what only a vendor knows — and it gates J3 when a warranty reroutes the work
J4 / J5 / J7 are the aggregation family: many entities, one trip, nothing missed
```

---

## J1 — "Don't let me buy something I already own."

> When I'm about to place an order for a job I've scoped, I want to know whether this
> exact thing is already on a shelf, so I don't spend money and space on a duplicate.

- **Performer / where:** Paul, laptop or phone, cart open, ordering session. Not in the
  shop. `[validated]`
- **Trigger:** a guide or shortlist says *"buy."* Every 2026-08-28 and 2026-09-08
  near-miss was triggered by a checklist line, not by a felt need. `[validated]`
- **Done:** the buy is cancelled **and the record is corrected.** The bracket-kit case
  stayed half-done for two months because the guide stayed wrong after the receipt
  existed. `[validated]`

**Forces**
- **Push** `[validated]` — four confirmed misses in one session, all under-reporting.
- **Pull** `[validated]` — a duplicate is pure waste; the correct answer is free.
- **Anxiety** `[validated]` — the register has been wrong the *other* way too (two items
  read `ON ORDER` and had never been placed). An over-trusted register produces a
  stockout instead of a duplicate.
- **Habit** `[inferred]` — re-buying a $9 part is cheaper than checking.

---

## J2 — "Don't let me buy the wrong variant of a thing I own." *(the veto)*

> When I need a consumable that only exists in relation to a tool I own, I want to know
> which variant that specific tool takes, so I don't buy a fourth thing that fits nothing.

- **Performer / where:** Paul, at a screen, **with the tool in another room and possibly
  unreadable.** This is the defining condition. `[validated]`
- **Trigger:** a listing that is true and useless — *"for Weller soldering iron."*
  The platform then actively pushes the wrong thing (a "newer model" pointer to a tip
  for an iron Paul does not own). `[validated]`
- **Done:** the order is placed against a **mount**, not a brand — a ~5.2 mm slip-over
  rod, not "80 W plastic welder"; MT vs. WLT vs. ET, not "Weller conical 0.8 mm."

**Forces**
- **Push** `[validated]` — two tip orders already dead; a third (threaded-mount welder)
  and a fourth (the platform's own suggestion) caught by hand.
- **Anxiety** `[validated]` — resolving it needs a caliper reading that requires
  extracting a broken tip: a garage errand blocking a screen decision.
- **Habit** `[validated]` — brand matching is what every listing rewards.

⭐ **Most expensive job in the set; least served by a receipts substrate.**

---

## J3 — "Can I start this job today?"

> When I'm deciding whether to open a job, I want to know whether every path through it
> is stocked, so I commit to work I can finish rather than finding a gap at the bench.

- **Performer / where:** Paul at the bench — or more often at a desk, deciding whether
  the bench session is worth opening. `[validated]`
- **Trigger:** a window opening. `paul-decided 2026-08-28`: *"Restore the door panels,
  put them on, and then just be ready to take them off when there's a full painting.
  We're not gonna wait… because I don't want them to rattle or get worse in any of the
  cracks."* He reordered a whole project to avoid waiting on stock. `[validated]`
- **Done:** a per-**path** answer, not per-job.

⭐ **This job is already being done by hand, twice, and has already failed once.**
`TOOLS.md`'s *"three reinforcement paths"* table and the guide's *"Can I reinforce the
plastic from the backside? — YES, and it is fully stocked"* are both hand-authored
answers to exactly this question. **One was wrong** — it declared the mesh-weld path
stocked when no owned iron has a flat tip. `[validated]` Strongest existence proof in
the set.

⚠️ **Provenance can gate this job, not just stock.** See J10: if the battery is under
warranty, the load test must happen at the vendor, not an auto-parts counter. The work
itself changes. `[validated]`

---

## J4 — "Batch a seasonal, multi-entity task into one trip."

> When a whole class of machines needs the same seasonal treatment, I want one
> consolidated list across all of them, so it's one trip instead of five.

- **Performer / where:** Paul at a laptop, **ahead of time.** Low urgency, high
  aggregation. `[assumption]`
- **Trigger:** season change; or a batched physical trip (fleet lap 1 beat 4 already
  batches — check both mowers' bolts, pull a GTI plug). `[validated]`
- **Done:** a list ordered by **store**, not by machine, with quantities summed.

⚠️ **HALF OF THIS ALREADY EXISTS AND NOTHING READS IT.** `vehicles.json` v3
`maintenance` blocks carry per-entity spec **and capacity**, each with `confidence` and
`source`. Absent: (a) any on-hand quantity, (b) any cross-entity aggregation, (c) any
equivalent for equipment or garden. `[validated]`

⚠️ **THE INCIDENT IS STILL MISSING, and the battery case does not supply it.**
`guides/blue-thunder-starting-diagnosis.md` supplies J4's **domain** — seasonal storage
is real, consequential, months-long work — but not its **claim**. Nothing in that file
went wrong because five machines weren't considered together; nobody made two trips,
nobody missed a machine. **The aggregation payoff stays `assumption`.** Do not let a
strong adjacent story launder it.

⭐ **But the battery case RESHAPES J4's content.** Winterization is largely a battery
job, and a battery is neither a tool nor a consumable — it is a **condition**, carrying
per-entity rulings (`⛔ AGM/GEL profile, never STD`; `⛔ never REPAIR mode on a sealed
AGM`; `⛔ a charger is POWERED or FULLY DISCONNECTED, never attached and dead` — the
last measured at ~20 mA, ≈1.4 Ah over three days). `[validated]` So **J4 intersects J8**:
a seasonal list carries preferences, not just quantities.

⛔ **And it is aggregation across VARIANTS, not consolidation.** Paul's own phrasing —
*"here are all the **types** of oil"* — concedes this. The fleet's batteries span AGM,
flooded and lithium tool packs; the oils span VW 502.00, VW 508.00 and motorcycle
specs. **The specs forbid consolidation.** `[validated]`

---

## J5 — "Tell me how much, not just whether."

> When I know I own some of a consumable, I want to know whether I own *enough for this
> job*, so a half-empty bottle doesn't read as green.

- **Performer / where:** two places that behave differently — at a shelf holding a
  container (garage), or building the batch list (desk).
- **Done:** demand and stock in the same unit.

⭐ **The UNIT is often the real question, not the number.** The isopropyl row is the
worked example: Paul bought a bottle and the row stayed open, because the load-bearing
quantity is **concentration** (91/99% vs. 70%), not volume. *"Buying a bottle did NOT
close this row; reading its label will."* `[validated]`

⚠️ Quantity is meaningful only where the item is fungible. Half a mesh screen is not
half a job. `[inferred]`

---

## J6 — "Get what I'm holding into the record, right now, with dirty hands."

*Not in the original ask. Everything above depends on it.*

> When I discover a fact about a tool by handling it, I want to record it in seconds
> without leaving the bench, so the record stops being a receipts shadow.

- **Performer / where:** garage, mid-job, phone possibly the only device. `[validated]`
- **Trigger:** surprise. *"I have purchased them before."* · *"I've got some good
  brushes and cleaner."* · the driver-side washer twisting off and refuting the
  session's own prediction. `[validated]`
- **Done:** the fact is in the record **with its grade attached**, without a session
  having to be running.

**Evidence that this is the load-bearing gap** `[validated]` — the trial-fit 2×2 matrix,
the tip extraction, the washer result and the ABS-sheet confirmation all reached the
record only because Paul said them aloud in a session that happened to be open. Six
months of an entire plastic-welding kit existing in no record at all.

⭐ **SECOND PERFORMER — Mom, as a remote instrument.** `[validated]`
`blue-thunder-starting-diagnosis.md` is written partly *for her*: a shop card to print
and tape up; *"Mom presses, Paul reads"*; and *"⭐ THE NO-METER VERSION IS MOM'S…
'Did the third sound the same as the first, or slower?' That one sentence is the most
useful thing she can give over the phone."* Plus a proposed handlebar voltmeter so
*"it says 12.1"* becomes a number **she can read out over the phone.**

**Her version of J6 is not "get it into the record" — it is "get it to Paul."** Same
moment, same object, different channel. **The record currently receives neither.**
Consequence for this job set: per-machine facts need a **speakable** form, because the
channel is a phone call.

⚠️ Capture stays deterministic and AI-free per standing doctrine — a constraint on the
door, stated here because it bounds the job, not as a design proposal.

---

## J7 — "Don't let me miss one." *(different performer)*

> When I break out a consumable, I want the full set of places it has to go, so I
> don't finish thinking I might have skipped something.

- **Performer:** **Mom.** In the garden, mid-task, bag already open.
- **Evidence** `[inferred — strongest non-direct claim in this set]` — Paul, relayed,
  2026-09-07, in `CLAUDE.md`: *"she actually keeps asking very specifically for this
  zone layout… 'I'm breaking out the fertilizer — what plants? I don't wanna miss any.
  What zones have what plants that need the fertilizer?'"* Per this repo's doctrine,
  Paul-relayed input is real input. Held at `inferred`, not `validated`, because it is
  a paraphrase of a repeated ask, not a direct observation. **Promoting it needs her own
  words, and that is cheap to get.**
- **Done:** completeness — **not** one trip. Her success criterion differs from J4's.
  *She is not lost; she is worried about missing one.*

⚠️ **This job crosses a tone boundary.** `BACKLOG.md` is explicit that Fernwood carries
two products with *"different users, tone, cadence and definition of done."* Track B is
Paul's; register language is fine there. **J7's performer is on Track A**, where
*"you're overdue on 4 zones"* is forbidden and the standing anti-persona in
`persona-paul-co-steward.md` is literally *"the property-management professional who
wants a maintenance system of record."* Including garden is right — but it means one
substrate, **two renderings**, and the second has a hard tone contract. `[validated]`

---

## J8 — "Don't make me decide this again — and don't let me re-walk a path I ruled out."

> When I need to buy something I've bought before, or something in a category where I've
> already learned what works, I want my own past ruling in front of me, so I can act on
> it without re-reasoning — and so I don't quietly repeat a mistake I've already paid for.

- **Performer / where:** Paul, in a store aisle or a browser at restock. **Not the
  garage** — the object isn't there and doesn't need to be. The only job in the set whose
  evidence source is neither shelf nor object.
- **Trigger:** running out; a checklist line naming a *category* rather than a part;
  **or a substitution forced by what the shelf has.**
- **Done:** the purchase is made without re-reasoning, **and a forced deviation is
  noticed rather than silent.**

**Why it is a distinct job, not a facet of J1/J2** `[validated]` — **it still fires at
zero inventory.** Out of soil, own no bags, J1 and J2 have nothing to say, and the
answer is still needed. A job that survives an empty shelf is not an inventory job.

**Why it is ONE job and not two** — the positive face (*buy the go-to*) and the negative
face (*don't re-walk a rejection*) share performer, moment, trigger and success
criterion. What differs is only evidence availability, which is a data asymmetry: the
positive face leaves repeat purchases; **the negative face leaves either nothing, or a
trace that reads backwards** — a rejected jump starter sits in the receipts record as a
*purchase*, marked returned. `[validated]`

**Forces**
- **Push** `[validated]` — a settled verdict re-litigated within 11 days (recorded
  2026-07-22, *"re-confirmed unprompted"* 2026-08-02, now tagged `✅ SETTLED — do not
  re-open`). And a real preference — *no 6000 K white interior light in the Bronco* —
  that exists **only** as three separate returns and is written down as a ruling nowhere.
- **Pull** `[validated]` — the record already reaches for this by hand, under a heading
  reading *"Selection notes, so this isn't re-litigated later."*
- **Anxiety** `[validated]` — the cost is mostly **hazard, not time**. Lacquer thinner
  *"ruled out at the shelf"* because an unprinted blend flashes at several rates on a
  structural bond; mineral spirits as a last wipe is *"the one that kills a bond
  silently"*; silicone dressing is *the* fisheye contaminant. **All fail invisibly.**
  So a go-to must carry not only *which*, but *what happens if you deviate*.
- **Habit** `[validated]` — take what the shelf has and assume equivalence. That is
  exactly how 320 grit went missing from the 2026-09-05 run: nobody re-litigated
  anything; the shelf didn't have it.

### The rejection taxonomy — four kinds, only two are preference

| Kind | Instances | Recoverable by |
|---|---|---|
| **Fitment** | two dead tip orders · a threaded-mount welder · a platform "newer model" pointer | **measurement.** *Not preference.* |
| **Performance** | a 3000 A jump starter returned as *"not big enough… for the Bronco"*; the kept unit advertises **1500 A** | **use only** — the spec sheet **inverts** the verdict, and the record says so |
| **Mechanism** | silicone dressing *"never on this truck again"* · rigid filler on a flexing panel · lacquer thinner · mineral spirits last | **knowing why.** Highest value, least recoverable, only kind that generalises to unbought parts |
| **Fit-for-shape** | a brand trusted on the Bronco but rejected for panel retainers · assortment kits rejected for the repair, *"fine as practice terminals"* | **naming the use** |

⭐ **"Preferred brand" is not a property of a brand.** It is a property of
**(brand × part-shape × use)**. The same brand is trusted and rejected in the same file
on the same day, with reasons. A row reading `preferred brand: X` is wrong the first
time it is asked about clips. `[validated]`

⚠️ A ruling can also be *"brand doesn't matter"*: *"Foam is a no-name and that's OK…
there is no brand quality in it."* `[validated]`

### RULING vs OBSERVATION — it bites the job, not just the data

The go-to job's whole point is **acting without checking**. Every other job ends with
Paul verifying something; this one ends with him not verifying. **So an unruled tally
rendered as a go-to fails in the one place where nobody is looking.**

⭐⭐ **And a frequency-derived go-to is wrong in the direction that matters most:**
**the items with the most purchase rows are disproportionately the ones that failed and
got re-bought.** Drain plugs — five purchases, four returned, one kept: a tally would
elect a plug he sent back. Soldering tips — two purchases, zero endorsements. White
dome-light LEDs — three purchases, all returned. `[validated]`

⚠️ **Hand-kept tallies also drift.** A selection note calls a brand one Paul *"has used
twice on Bolores"*; the receipts substrate carries **three** Bolores rows for it. A
prose count, wrong by one, inside the file that exists to be right. `[validated]`

✅ **But observation does one thing a ruling cannot: surface a go-to nobody has ruled
on.** One detailing brand appears three times across three product lines with **zero
rulings anywhere** — a real default in Paul's head, never written. `[inferred]`
Same lesson as 2026-09-07: *an empty record is not an absent demand.*

> **Rulings answer the job. Observations feed the intake.**
> A tally's role is to **generate the question**, never to be the answer.
> `Observation → ask Paul → ruling.`

⚠️ **Job-side consequence for the "learning" framing:** the success criterion here is
*"I can act on this without checking."* **An inferred preference cannot meet that bar** —
not as a technical limit, as a job-side one.

---

## J9 — "Find me the right one." *(the sourcing job — J2's positive form)* **NEW**

> When a job needs a part, attachment or accessory I don't have, I want to be told what
> to buy — the specific thing, and why it's that one — so I stop shopping by brand name
> and guessing at mounts.

**Paul, verbatim, 2026-09-08:** *"the whole journey I've been on is a really good example
of where you could provide value — I should've just come to you and been like 'what tips
should I get exactly'. So that's a use case of you helping find and source replacement
parts, attachments, accessories."*

- **Performer / where:** Paul, initiating, at a desk. **Not at the moment of purchase** —
  before a candidate exists at all.
- **Trigger:** J3 returns a gap. The chain is `J3 → J9 → J2`.
- **Done — two branches, both wins:**
  1. **A SKU he can order now**, specified by **mount**, with the alternatives named and
     the near-misses ruled out; or
  2. ⭐ **A named gate** — *the one measurement that would resolve it* — plus an explicit
     refusal to recommend until it is taken, **plus what he can do meanwhile without
     resolving it.**

**Why distinct from J2, not the same job from the other side** `[validated]`
- **J2 can be answered from Paul's own record. J9 cannot** — it requires the market.
  Different evidence-source class (see the axis table).
- **Opposite failure modes.** J2 fails by letting a wrong purchase through. **J9 fails by
  confidently recommending the wrong thing** — strictly worse, because Paul has delegated
  and will not check. J9 shares J8's dangerous property.
- **Different cost structure.** J2 is a lookup. Today's real sourcing answer took roughly
  fifteen exchanges, three web searches and two product-page reads, and returned a
  concrete answer for one iron and *"gated, go measure"* for the other.

### ⭐ Yes — the honest unknown belongs in the definition of done, as the *primary* branch

**Every wrong tip in this story came from a source that could not say "I don't know."**
A listing reading *"for Weller soldering iron"* is confident, true and useless. The
platform's "newer model" pointer is confident and wrong. The 2026-09-06 election of a
2.4 mm chisel as *the* mesh-weld tip was confident and was withdrawn two days later.
`[validated]`

Paul's own doctrine already says this in a neighbouring domain, in this repo: *"an
honestly-unsure tool beats a confidently-wrong one, the same doctrine the app itself
runs on."* And the gated shape is already written down — `Substrate = __________`;
*"Do not buy MT until it has [answered both questions]."*

⭐ **Branch 2 is worth more than branch 1**, because branch 1 already exists in the world
and branch 2 does not. The value is the refusal.

⚠️ **Limit, and it is real: a gate Paul chooses not to walk stalls the job.** He deferred
the acetone substrate test for weeks — *"rather not do an acetone test… I could do one
later when it's fully clean."* So a capability that gates everything on a measurement
will stall. **The good version is what actually happened on 2026-09-08:** the answer
also surfaced the paths that were *not* gated — *"executable today with zero purchase."*
**Done = the gate + what is possible without resolving it.** `[validated]`

---

## J10 — "Recover a fact about my own property that someone else holds." **NEW**

> When a decision turns on a fact my record can't supply — when I bought it, whether
> it's still under warranty, what a shop actually did — I want to get that fact from
> whoever does hold it, so I stop reasoning from a floor value.

- **Performer / where:** Paul on the phone, or at a counter with the object in hand.
- **Trigger:** a decision blocked by a fact the record structurally cannot contain.
- **Done:** the fact is obtained **and folded**, with its source — *an order number, not
  another ask.*

**Why it is a job and not a one-off** `[validated]` — at least three independent
instances across three domains:
1. **Powersports battery.** The record carries no purchase or install date, *and age is
   the decision-relevant fact.* It is absent because it was bought **in a store**.
   The closing fact lives at the vendor, keyed to a phone number.
2. **A VW service invoice** photographed in the photo library, recording a service event
   the fleet record does not appear to hold — with a VIN that, as read, does not match
   the recorded vehicle. The shop holds the truth.
3. **The water heater** — `installedHere: "Not yet on record — no invoice in email;
   worth finding the paperwork, **it starts the warranty clock**."* Same warranty-
   provenance shape, a different domain entirely (appliance, not vehicle).

⭐ **Provenance reroutes WORK, not just purchases.** If the battery is inside a
12-month term, *"the store test should happen there, not at an auto-parts counter — a
warranty claim wants their own tester's verdict on their own paperwork."* `[validated]`
**None of J1–J9 has a fact changing a procedure.** This one does, and it gates J3.

⭐ **The escalation ladder this case makes visible** — four instruments tried for one
fact (battery age), and only the fourth could close it:

| # | Instrument | Result |
|---|---|---|
| 1 | receipts register | **silent** — store purchase |
| 2 | the vehicle card | carried a **spec group as an identity** |
| 3 | the molded case code, photographed | a **FLOOR only** ("cannot be older than its case"), and a model read |
| 4 | the vendor's purchase history | **the only one that closes it** |

⛔ **PRECONDITION — J10 cannot be served from a spec group.** The record must hold an
**identity** (`XTAX7L-BS`), not a fitment group (`YTX7L-BS`). Fitment-correct and
identity-wrong is invisible at purchase and defeats J10 months later at the counter.
This also feeds back into **J6**: what must be captured off an object is the identity,
and the identity often sits on a different face than the fitment spec.

⚠️ **The instruments for this job are measurably unreliable, and the record already
knows.** The cancelled-orders view *"is silently ignored on BOTH endpoints — there is
currently no known URL that reaches"* it, so a searched-negative there is a negative on
an instrument that cannot see the answer. And order mail does not land in the account a
search would sweep: *"A Gmail search of this account is not evidence about an order."*
`[validated]`

⚠️ **Degradation here is by TIME, not use** — a battery declines sitting still. That is
what makes purchase date decision-relevant at all, and it is why this job intersects J4.

---

## What matters most to Paul — the read, with a falsifier

**He wants an instrument he can trust, not a list of what he owns.** `[inferred]`

- His founding sentence asks for the negative case explicitly: *"a record of everything
  that I have **and don't have**."* Ordinary inventory asks lack that clause.
- What he actually built is mostly epistemics, not rows: a COVERAGE warning instructing
  the reader how to read an *absence*; an ORDERED-vs-OWNED rule (*"keep writing that
  caveat, and clear it with an order number"*); a two-question caliper gate; a trial-fit
  matrix promoted specifically because it outranks a listing read; three `⛔ WITHDRAWN`
  corrections of the file's own prior claims.
- **The parity target he named makes the same point.** `vehicles.json` v3's
  distinguishing feature is not completeness — it is per-value
  `confidence: verified | inferred | tbd` plus a `source`.
- His behaviour is trust-shaped, not thrift-shaped: an hour of attention on a
  sub-$10 part; a *free* test deferred rather than run on a dirty panel.

⚠️ **Honest split:** multi-entity aggregation is what he asked for **loudest**, twice,
unprompted. It has **no incident behind it** (see J4). The trust problem has a
documented incident history from 2026-08-28 through 2026-09-08. *What he asked for
loudest and what the record says he cares about most are not the same thing.*

### Falsifiers — pre-registered

1. **On the trust read.** Show two rows for one item — bare (`Weller SP23L — owned`)
   versus graded (`owned [paul-stated 2026-09-06, photos]; tip family MT; shank
   threaded-or-smooth ⚠️ UNVERIFIED`). **If he reaches for the bare one, or finds the
   graded one noisy at a glance, this read is wrong** and the emphasis should move to
   speed of lookup with provenance behind a disclosure.
2. **On ruling-vs-observation.** Generate the top-10 most-purchased brands straight from
   the receipts substrate and show him. If he finds it useful and broadly right, the
   observation channel is stronger than claimed and the split is over-engineered.
   **Prediction: it surfaces the returned drain plugs and the returned dome-light LEDs
   near the top, and he says those are exactly wrong.**
3. **On J9's honest unknown.** He lived through both halves on 2026-09-08 — a concrete
   answer for one iron, *"gated, go measure"* for the other. **Ask which half he'd keep.**
   If the gate reads as frustration rather than value, honesty is a caveat, not the
   product.
4. **On consolidation.** Has he ever bought two brands of the same *self-defining*
   consumable (gloves, degreaser, tape) and had an opinion? If not, consolidation is not
   a job. **Current evidence says not:** *"Foam is a no-name and that's OK."*
5. **On the registry itself.** If six months on, a purchase is still made against a
   listing title rather than a recorded mount, it never reached the moment it was built
   for. And if no row has ever entered **from the garage** — only from receipts — **J6
   was never solved and the register is still a receipts shadow.**

---

## Open questions

- **Mom's own words on the fertilizer ask.** One relayed verbatim promotes J7 from
  `inferred` to the strongest claim in the set.
- **Who buys the soil** — Paul or Mom? It decides which tone contract the garden half of
  J8 sits under. ⚠️ If **Paul buys and Mom applies**, a preference held by the buyer can
  be **silently violated by the applier**, who has no access to it.
- **One recalled winterization episode** — did a seasonal put-away ever cost a second
  trip? J4 is the only job with no incident behind it, and it is the headline use case.
- **Where Paul was standing** for each of the two dead tip orders. "At a screen" is
  inferred from the record's shape; if either was placed *in the shop with the iron in
  hand*, J2's context read is wrong and the set reorders.
- **Does Track B want its own persona?** `persona-paul-co-steward.md` is written entirely
  around Track A's appreciation/stewardship job and does not describe the man with the
  panel on the bench.
- **Mom-as-remote-instrument (J6)** — is this a recurring posture or one guide's design?
  If recurring, it is a third distinct Mom role and wants its own card.

---

## Evidence log

- `2026-09-08: [validated] — .private/service-records/TOOLS.md § Soldering irons + the trial-fit 2×2 — two owned irons, four tip systems, two dead orders, two more near-misses caught by hand.`
- `2026-09-08: [validated] — TOOLS.md § Plastic repair — ABS sheet stock confirmed owned, closing a guide line that read "no receipt found."`
- `2026-09-08: [validated] — guides/blue-thunder-starting-diagnosis.md — battery identity is XTAX7L-BS; YTX7L-BS is a JIS size group recorded as a part number across three surfaces.`
- `2026-09-08: [validated] — same file — warranty status reroutes where the load test happens; the closing fact lives at the vendor.`
- `2026-08-28: [validated] — TOOLS.md preamble — three under-reporting misses in one session; the register's founding quote asks for what he "has and doesn't have."`
- `2026-08-28: [validated] — TOOLS.md § Sound & insulation — the OPPOSITE error: two items recorded ON ORDER had never been placed.`
- `2026-09-07: [inferred] — CLAUDE.md, Paul relaying Mom — the fertilizer/zone ask; falsified a two-pass research finding.`
- `2026-09-08: [validated] — Paul, voice — the sourcing job, in his own words (J9).`
- `2026-09-08: [validated] — .gitignore carries only .private/ — this artifact is public; no order numbers, identifiers or prices reproduced.`
