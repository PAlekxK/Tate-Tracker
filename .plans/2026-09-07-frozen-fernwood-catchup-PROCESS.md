# HOW THE CATCH-UP IS RUN — the gate, the unit of work, the ledger, and the line nothing crosses early · PROCESS

- kind: process
- row: process (no BACKLOG row — same posture as the 09-06 freeze register and the 09-06 conversion design)
- objective: O3 → O1
- class: engine · declared (process machinery; no module, no item and no feature is ranked here)
- seats: practice-steward (this file)
        engineering-partner → not commissioned here; §2 states what the generator must be, never how it is coded
        ai-advisor · ux-expert · content-steward · user-researcher → not commissioned
- depends-on: .plans/2026-09-06-freeze-register-PROCESS.md
- depends-on: .plans/2026-09-06-migration-readiness-STATE.md
- depends-on: .plans/2026-09-06-feedback-freshness-CENSUS.md
- depends-on: .plans/2026-09-06-conversion-method-DESIGN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- stage: concept
- gate: ⛔ **NOTHING IN THIS FILE EXECUTES.** Every act named here waits on G0 (§1) unless §4 places it
  explicitly before the line. `[paul-stated 2026-09-07 ~10:20 ET]` — *"let's have everything gated on her
  getting her link to set up in prod."*

> **Method only.** This file says how the catch-up is *run*. It never says which module comes first, which
> of her items matters more, or what any single item's disposition should be. Every disposition is Paul's.
>
> **Grades:** `[measured]` = read or executed against this repo on 2026-09-07 and cited · `[inferred]` =
> derived from two measured facts · `[assumption]` = neither, and marked so it can be shot down · `[R]` =
> reported by another artifact or the other live session, not re-verified here.
>
> ⛔ **Read-only run.** No tracked file was edited, nothing was committed, nothing pushed, no network call
> was made, no channel was fetched, and no value in the archive was opened — §2's key-family counts come
> from `json.load(...)["values"].keys()`, never from a value.

---

## 0 · WHAT MOVED UNDER THIS FILE WHILE IT WAS BEING WRITTEN, AND ONE POINTER THAT LEADS NOWHERE

Three rulings of 2026-09-06 evening are already in `BACKLOG.md:137-248` and they change the shape of the
catch-up materially. They are **not re-derived here**; they are the frame.

| ruling | where | what it does to this design |
|---|---|---|
| **Rule 4 — the hold on Mom's feedback is LIFTED FULLY** (*"OK lift it fully"*) | `BACKLOG.md:190` | Read, disposition and act are all released. **Track A · C is LIFTED at HEAD, not HELD.** The one constraint: every action lands on the NEW instance, never on the control; **no acknowledgment goes back to her without Paul.** ⭐ This removes what would otherwise have been this plan's hardest structural blocker — a tranche that must read her words cannot run on a held channel |
| **Rule 5 — the map arrives EMPTY** | `BACKLOG.md:203-217` | Zones do not migrate. The 23 traced zones and her 16 names are an **answer key** and **grounding**. General shape: *what we know informs the design, it does not pre-fill her work.* ⭐ **This narrows `carry` from a default to an exception** — see §2.3 |
| **Rule 3 — the transition is a GUIDED VISIT** | `BACKLOG.md:170-186` | Supersedes *"a link, not a visit."* The control is an **ARTIFACT**. The sunset order is already written: drain her phone *during the visit* → re-archive + `--verify` → rotate `SHARED_TOKEN` → tag the sha → disable Pages → stop the bots |

⚠️ **A pointer in the register leads to a file that does not exist** `[measured 2026-09-07]`. Rule 6
(`BACKLOG.md` ~:252) names the plan of record as `.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md`;
`ls .plans/2026-09-07*` returns nothing, and this file is `…-PROCESS.md`. **Reported, not resolved** — either
another seat owes the `-PLAN` file or the register's pointer needs correcting, and which is Paul's or the
authoring session's call, not mine. It is a live instance of §6·F4.

---

## 1 · THE GATE — stated so it can pass or fail

### 1.1 · G0, in one line

> **G0 · A household member record positively identified as Mom exists on production `home` / `est-e6696a`.**

**Why the gate is the CONSEQUENCE and not the ACT.** Paul's words on 2026-09-07 are *"her getting her link
to set up in prod"*; Rule 3 of 2026-09-06 says the transition is a **guided visit**, in person. Those two
sentences describe different human acts — a send, and a visit — and a gate written on either one has to
pick, which is not mine to do. **Both produce the same observable, and only that observable has a
deterministic signal.** So G0 is written on the observable. Under either reading of the act, G0 cannot be
true before it happens and is true immediately after. `[inferred]`

### 1.2 · ⛔ THE PREDICATE MUST NOT BE THE RESET TOOL'S — the same test is fail-CLOSED there and fail-OPEN here

The candidate signal named in the brief and in the register is `tools/reset-production-estate.py`'s abort on
any `real` record. **It is the wrong predicate for a start gate, and the reason is structural, not stylistic.**

`reset-production-estate.py:87-110` `[measured, read from source]`:

> *"→ ('synthetic'|'real'|'unknown', why). ⛔ NEVER GUESSES TOWARD SYNTHETIC. A record is synthetic only on a
> POSITIVE marker; anything carrying a human-looking identity that does not match a declared synthetic is
> `real`; everything else is `unknown`."*

That polarity is exactly right for a **destructive** tool: an unproven record must block a delete. Pointed at
a **start** gate the same polarity inverts — a leftover record nobody can attribute reads `real`, and the
catch-up opens on it. ⭐ **A safety predicate reused as a start signal runs backwards.** And it lands squarely
on this stack's most-repeated shape: *a real account and an unattributable one produce the same observation.*

Three further reasons not to reuse it, each measured:

1. It is a **destructive tool**. Running it to ask a question means invoking the one command whose header says
   *"After Mom onboards it must never be run again."* A status read must never be a dry run of a deleter.
2. Its classifier depends on `.private/synthetic-identities.json` being present; `reset-production-estate.py:140`
   prints *"no synthetic-identities file — NOTHING can be proven synthetic this run"* `[measured]`. A missing
   file makes **every** record read `real` — i.e. the gate would pass on an absent file.
3. It is scoped to the reset's target, not to a named person. **Mom's household is `est-e6696a`; a real record
   on it is not necessarily hers.**

### 1.3 · What G0's signal must be — the requirement handed to the production window

**This window does not build it and does not own production.** The requirement, stated and not designed:

| # | requirement | why |
|---|---|---|
| **G0-R1** | A **read-only, exit-coded** predicate. No delete path, no `--dry-run` of a deleter | a status read must be safe to run at every session start |
| **G0-R2** | Scoped to **`est-e6696a`** specifically, derived from whatever declares reality (`wrangler.toml`), never a typed literal | the 09-06 control shape: *an instrument's scope must be DERIVED, and a derivation that finds nothing reads UNCHECKABLE — never green* |
| **G0-R3** | ⭐ **Requires a POSITIVE identity match. `unknown` FAILS the gate, and so does `synthetic`.** Three states in, one passes | §1.2. This is the inversion, made explicit |
| **G0-R4** | A **paired negative control**: a synthetic identity on `est-e6696a` must make the check read NOT-PASSED, proven by mutation, not asserted | *"a selftest that only ever passes has proven nothing"* |
| **G0-R5** | Unreachable store / missing token → **`UNCHECKABLE` (a distinct exit), never `not yet`** | `read-onboarding.py`'s own doctrine, and see G0-R6 |
| **G0-R6** | ⚠️ **`.private/` holds `fernwood-token` and `fernwood-token-qa` and nothing for `home`** `[measured, `tools/read-onboarding.py:26-42`, read from source]`. Production is **unreadable by construction today.** The token must exist or G0 reads UNCHECKABLE forever | a gate that can never be evaluated is not a gate |
| **G0-R7** | The human act that produces G0 — the send, or the visit — leaves a **dated line in the register**, labelled an **attestation** | an outbound act is not observable from this repo. Register §4(f) precedent: say which claims are attested and which are measured |

**G0's own precondition, reported not designed:** the production window states the link comes only after Paul
walks production `[R, other window, 2026-09-07]` — i.e. **release-cascade gate 2 precedes G0.** That belongs in
the register as a stated dependency so G0 is not read as reachable today.

### 1.4 · G0 is ONE gate, and it is not the only one

G0 opens the work. It does not authorise any individual act inside it. §3's T3, T5 and T6 carry their own human
gates, and §4 draws the line that each act is tested against. The spine's S2 explicitly refuses *"exactly one"*.

---

## 2 · THE UNIT OF WORK, AND THE LEDGER

### 2.1 · The unit of WORK is the module; the unit of the LEDGER is the item — and they must not be the same

Paul's framing is *"as we unlock different modules"* `[BACKLOG.md:141]`. So a **tranche = one module**, and the
manifest is already declared in code — `tools/momlib.py:333-362` `[measured]`: **garden · motor-pool ·
equipment · house-systems · wildlife · place**, plus `NON_DOMAIN_MODULES` weather · sky · neighbourhood.

⛔ **But a module is not a disposition.** This repo has already paid for that exact error: on 2026-08-10 a whole
day's arrivals were cleared by **one** sibling record's self-identification, and the 08-09 Fairway recording
rode along unheard for four days — which is why `arrival-dispositions.json` is *"keyed by (channel, recordId)
so a batch can never be cleared by one of its members"* `[measured, that file's `_meta.purpose`]`. And it is why
**63 of her 81 arrivals sit `baselined` — covered by a watermark, never individually attested** `[measured, the
09-06 census §2a; `BACKLOG.md:200` states the same number]`.

> ⭐ **So: the tranche is module-grained; the ledger is item-grained; and the generator must REFUSE a
> module-level disposition.** Closing a module means every one of its rows left `undecided` on its own row.

### 2.2 · The row set — five sources, and the classification is TOTAL, not filtered

Modelled on G1 of `.plans/2026-09-06-conversion-method-DESIGN.md:128` — *"the conversion ledger — TOTAL, not a
count. An unclassified site is RED."* **A filtered-out row and a never-looked-at row produce the same
observation**, so nothing is filtered; everything is classified.

| # | source | rows | grain | measured today |
|---|---|---|---|---|
| **A** | the newest frozen archive, **key names only** | **175** | one KV key | `metrics` 91 · `conversation` 35 · `cost-log` 22 · `feedback` 10 · `zone-audio-blob` 6 · `est-3c9f1a:*` 4 · `zone-audio` 3 · `env-canary` 1 · `observations` 1 · `zones-last-seen` 1 · `zones` 1. **171 of 175 legacy unprefixed** `[measured, `.private/frozen-fernwood-archive/frozen-2026-09-06T000836.json`, `keyCount: 175`, `unreadable: []`]` |
| **B** | canon in git that is hers | **23** zones + `plants.json` + `vehicles.json` records | one record | `zones.json` holds **23** zones, all `status: draft` `[measured]` |
| **C** | channel arrivals | **81** | one arrival (channel, recordId) | 17 individually dispositioned · 63 baselined · 1 undispositioned as of 09-06 `[measured, 09-06 census §2a]`; **2 undispositioned as of 09-07** `[R, brief]` |
| **D** | browser-local state on her phone | **19** `tateTracker.*` | one storage key | `viewer.html`'s `STORAGE_KEYS` roster holds **19**, not the 18 the brief states `[measured, regex over `const STORAGE_KEYS = Object.freeze({…})`]`. ⭐ **6 of the 19 exist nowhere but her phone** — `feedbackOutbox.v1`, `door.outbox.v1`, and the four `momQueue.*` `[measured; `BACKLOG.md:177` states the same six]` |
| **E** | her 16 zone names | **16** | one name | ⭐ **Machine-derivable with no model and no guessing:** `zones.json` `history[].details.namedBy` carries `"mom, 2026-08-30 (naming session)"`; the predicate returns exactly **16** ids, and the 7 that are not hers are `house · the-turf · the-meadow · western-fern-azalea-garden · main-parking · the-green-terrace · hosta-garden` `[measured]` |

**Total, day one: 314 rows** (175 + 23 + 81 + 19 + 16), before `plants.json`/`vehicles.json` records are
expanded. `[measured, sum of the above]` ⚠️ **E is a sub-grain of B and is deliberately double-counted**: a zone
is one row as a *shape* and one as a *name*, because rule 5 disposes them differently — the shape does not
migrate, the name is an answer key **and** an unpaid acknowledgment (`BACKLOG.md` § Z-ACK). Any generator that
collapses them loses that distinction. The denominator must therefore always be printed with its predicate.

### 2.3 · The disposition enum — and rule 5 moves the seam

The brief's four words are `carry · re-collect · stays-in-the-control · drop`. **Rule 5 breaks the first one.**
*"What we know informs the design, it does not pre-fill her work"* means the dominant destination for most of
her items is **the build**, not her data — and there is no word for that in the four. Following the standing
rule (reuse the vocabulary; add a state only on demonstrated need), one word is added and two are sharpened:

| word | means | who may write it |
|---|---|---|
| **`informs-build`** ⭐ *new* | the item changes what the module IS — a design input, a copy change, a backlog row on the new product. **Lands in the product, never in her data.** This is rule 5's general shape given a slot | Paul |
| **`re-collect`** | only she can supply it; the module asks her afresh, in the new instance or in person. Her old answer is grounding for **how** we ask, never the answer we pre-fill | Paul |
| **`answer-key`** *(was "stays in the control")* | stays on the frozen control and is **actively used to measure** the from-scratch build at the tranche's close. Renamed because *"stays"* is passive and rule 1's whole point is that the control is a **benchmark**, not a shelf | Paul |
| **`carry`** | moves verbatim into the new instance. ⚠️ **Narrowed by rule 5 to an exception**: every `carry` row must name why it is not a pre-fill of her work. The clean case is the drained outbox — something she already wrote and intended to send | Paul |
| **`drain`** | browser-local only: flushed from her phone **during the guided visit, while online, before lockout** (rule 3's first step). Not a data decision — a physical act with an owner and a moment | Paul (it is his visit) |
| **`drop`** | ruled not to travel. **Requires ruler, date and his words** — a drop with no ruler is the failure this ledger exists to stop | Paul |
| **`undecided`** | day one, and **the only value that counts down** | the generator, by default |

Plus a separate, orthogonal column — **`whose`** ∈ `hers · paul · instrument · mixed · unknown`. It is a
separate axis because attribution is a known defect class here (memory `project_fernwood_device_misattribution`:
attribute from authored **content** only). `metrics`/`cost-log`/`env-canary` are `instrument` by key family;
zones are `hers`/`paul` by the `namedBy` predicate; **`conversation:*` is `unknown` until a human reads it and
must never be swept into `instrument` to make a count tidy.** `[measured — 35 conversation keys, attribution not
derivable from key names]`

### 2.4 · Where the ledger lives, and why it is not public

**`.private/catchup-ledger.json`** (generated) + **`.private/catchup-dispositions.json`** (hand-ruled).

The obvious counter-argument is good and it loses on one measurement: `arrival-dispositions.json` and
`feedback-log.json` both live in the public repo precisely because they hold *"never her words … only where the
record went"*. So why not this one?

> ⛔ **Because "a key name is content-free" is FALSE for this corpus.** Measured today: two of the 175 archived
> key names are `est-3c9f1a:cache:ambient:<station-mac>:288:1788582600000` — a **hardware address of the
> weather station at her house**, embedded in the key. `[measured]` The two existing ledgers hold ids the
> product minted; this one holds names the *world* minted, and that is a different safety claim.

**The public surface is a QUERY, not a copy** — the doctrine this repo already ratified for the trace
(`BACKLOG.md` § C3: *"THE TRACE IS A QUERY, NOT A FILE"*) and for held arrivals (register §3). `tools/catchup-ledger.py --status`
prints counts with their predicate; nothing is committed. A copied roll-up would rot in the safe-looking
direction within a day; a query cannot.

### 2.5 · What generates it — deterministic, read-only, and content-free BY CONSTRUCTION

**`tools/catchup-ledger.py`** — proposed, not built. Requirements, in the shape this repo already uses:

- **Reads:** the newest `.private/frozen-fernwood-archive/frozen-*.json` (**`values` keys only — never a value**);
  `zones.json`, `plants.json`, `vehicles.json`; `arrival-dispositions.json` + `feedback-log.json` (ids only);
  `viewer.html`'s `STORAGE_KEYS` block **by importing `check-storage-keys.py`'s own regex, never a second copy**
  (that file has been wrong three times in one day about its own scope — `tools/check-storage-keys.py:24-53`
  `[measured]` — and a fork would inherit the wrong one silently); `tools/momlib.py`'s `MODULES` for the module enum.
- **No network. No model. No writes outside `.private/`.** `[the capture-path rule: her words move verbatim with
  provenance; no model on the carry path]`
- ⭐ **Content-free by construction, proven by mutation, not by care.** The single most instructive local defect:
  `BACKLOG.md:88-90` said `read-mom-feedback.py --pickup` prints *"a COUNT… and nothing more"*, and
  `read-mom-feedback.py:556,578-580` prints her note verbatim at every session start `[measured, 09-06 register §3]`.
  **The ruling was right and the mechanism was winning.** So: a selftest plants a recognisable sentinel string
  into a fixture archive's `values` and asserts it appears **nowhere** in any output stream. A tool that only
  ever passes has proven nothing.
- **Fail-closed:** unreadable archive → `UNCHECKABLE`, distinct exit, **never "0 rows"**. Unknown module on a row →
  the row is `unclassified` and the run is RED, never silently dropped.
- **Refuses a module-level disposition** (§2.1).
- **`--record`** writes a disposition — ruler, ISO date, Paul's verbatim words, the module, the row id — into
  `.private/catchup-dispositions.json`. Same posture as `check-arrival-dispositions.py --record`
  (`arrival-dispositions.json` `_meta.writtenBy` `[measured]`). **A disposition an agent inferred is not a
  disposition.**

### 2.6 · The columns

`id · module · source(A–E) · sourceRef · grain · whose · provenance · disposition · ruledBy · ruledAt · words · check · checkState`

**`check` and `disposition` are two columns on purpose.** A disposition is what Paul ruled; a check is what
proves it happened. Collapsing them is precisely the checkbox-not-world drift (§6·F1) — 7 of 8 drifted artifacts
found on 09-06 erred in the safe-looking direction `[measured, 09-06 STATE headline]`.

| disposition | the check that proves it landed | `checkState` |
|---|---|---|
| `carry` | a **read-only per-record existence probe** against `home`/`est-e6696a` returns the record. ⚠️ **Does not exist — handoff H2** | pending → passed/failed |
| `re-collect` | an ask exists in her new household's queue **and** an arrival answered it, **or** she declined and the decline is recorded. ⭐ A decline must be recordable — the mom-cycle already carries `offers-passed` for exactly this, because *"declining is invisible to a record that only logs answers"* (`MOM-CYCLE-MAP.md:88`) | pending → passed/declined |
| `answer-key` | the row is present in the newest verified archive **and** the tranche's close records the comparison it was kept for | pending → passed |
| `drain` | the key is absent from her device **and** its payload has an arrival record on the new instance. ⚠️ Only observable during the visit | pending → passed |
| `informs-build` | a named, dated artifact on the new product carries it — a plan line, a backlog row, a commit sha | pending → passed |
| `drop` | the row carries `ruledBy` + `ruledAt` + `words`. **Nothing else.** | n/a → passed |
| `undecided` | none. It is the denominator | n/a |

---

## 3 · THE LAP SHAPE

### 3.1 · ⭐ RULED: FINITE burn-down, run as module tranches inside the EXISTING mom-cycle. Not a new loop.

Memory `feedback_cyclical_vs_finite_projects`: *loops REST and fire one at a time; finite = burn the backlog
down; don't wrap finite work in loop machinery.* Four reasons, in the order they bind:

1. **The set is closed, enumerable and has a bottom** — 314 rows measured today (§2.2), and once the frozen
   instance stops accepting writes (rule 3's sunset) it cannot grow. A finite set with a bottom is a burn-down.
   `[measured + inferred]`
2. **It has no trigger of its own.** Its trigger is *"as we unlock different modules"* — the new product's
   schedule, owned by the other window. A loop needs its own trigger; minting one here would create a 15th loop
   whose fire condition is another loop's output, and the portfolio already has a named failure for a signal
   that is really a completion probe (`CYCLE-SPINE.md`, `signals[].kind`: *"if nobody ever works this, can it
   start succeeding?"* — a tranche's completion cannot). `[inferred]`
3. **A host loop already exists, already owns this content, and already carries all six spine elements.** The
   mom-cycle has eight legs, three human gates, eleven checks each born from a named failure, a state artifact
   and a parsing map `[measured, `MOM-CYCLE-MAP.md`]`. And its channel is now LIFTED, with its own map already
   predicting this exact backlog: *"when the freeze lifts, the first mom-cycle lap starts with a backlog of
   unread arrivals — that is by design, not neglect"* `[BACKLOG.md:88-90]`.
4. **The spine forbids the retrofit anyway.** *"No loop is retrofitted by this file. Each loop adopts the spine
   on its own next lap."* Building a parallel spine for finite work would be adopting it twice.

⚠️ **The falsifier, pre-registered:** if the catch-up outlives three module tranches **and** starts generating
work that nothing else triggers — asks that need their own cadence, arrivals with no home — then it is a loop
and this ruling was wrong. The meter is P3 below.

### 3.2 · The tranche — eight beats, mapped onto the mom-cycle's legs, adding no new ritual

| beat | what happens | maps to | owner | closing condition |
|---|---|---|---|---|
| **T0 · SWEEP** | read the freeze register; assert G0 passed; assert the module is unlocked on the new product; dispose any fired item-gates | leg 0–1 + the ratified gate-sweep amendment | ai | G0's check exits PASSED; the register names the module |
| **T1 · RE-TAKE** | `archive-frozen-estate.py --verify` → 0 GONE → re-archive | *(new; sited here, see below)* | ai | `unreadable: []` and a `keyCount` ≥ the prior archive's |
| **T2 · GENERATE** | `catchup-ledger.py` → this module's rows, plus the whole-set `undecided` denominator | leg 1 (the deterministic sweep) | ai | every row classified; zero `unclassified` |
| **T3 · 👤 RULE** | **Paul rules the disposition of every row in this module**, batched, one pass. `--record` captures his words verbatim | leg 3 (RESOLVE, Paul at tier 2) | **Paul** | zero rows left `undecided` **in this module** |
| **T4 · EXECUTE** | the deterministic half — `carry` writes, `informs-build` artifacts filed, `drain` scheduled into the visit | leg 5 (SHIP) | ai | every executed row has a `check` named |
| **T5 · 👤 THE ASK** | `re-collect` rows become **invitations**, drafted, and Paul approves the exact words | leg 6 (GATE) | **Paul** | he approves the text; ⛔ **rule 4: no acknowledgment reaches her without him** |
| **T6 · 👤 PROVE + CASCADE** | every check run **live**, at her conditions (414 × A+); then synthetic → Paul → **Mom is gate 3** | legs 6e / 7-QA | ai, then **Paul**, then **Mom** | every `checkState` is `passed`, `declined`, or a named, dispositioned failure |
| **T7 · CLOSE** | the tranche's counts written to `MOM-CYCLE-LOG.md`; the register's module row updated; the **answer-key comparison recorded**; pre-registrations discharged | leg 7 (CLOSE) | ai | S4's predicate: the chronicle and the state artifact agree that this tranche closed |

**Two exits, and the seam is named.** `informs-build` rows leave the tranche into the **release loop** (the other
window's); `re-collect` rows leave into the **mom-cycle's own ask machinery**. A row that cannot name its exit is
not dispositioned. `[inferred]`

⭐ **Why T1 is at beat 1 and not beat 6** — the siting sentence the spine asks for (S3, and it is at 1/12 in the
portfolio): *a carry executed from a stale archive carries the wrong thing, and there is no eraser after Mom
onboards (`reset-production-estate.py` must never run again). The verify therefore sits before the first
disposition is even read, not before the last write — because a disposition ruled against a stale roster is
already wrong by the time it is executed.*

### 3.3 · Checks seen to fail, sited at the measured risk

| check | seen to fail | sited at | why there |
|---|---|---|---|
| `archive-frozen-estate.py --verify` | ✅ **yes, and it named the miss.** The 2026-09-06 00:03:42 run archived 174/175 and reported `metrics:2026-05-29` in `unreadable`; the 00:08:36 run got 175/175 `[measured, both files present on disk]` | **T1** | the tool's positive control has fired against reality once. That is the strongest S3 evidence in this plan |
| `check-arrival-dispositions.py` | ✅ **yes — it exists because of a failure.** 2026-08-10: a whole day's arrivals cleared by one sibling record's self-identification; selftest 14/14, proven by three mutations `[measured, `MOM-CYCLE-MAP.md:256`]` | **T3** | module-batching is that same failure re-armed. The check is what makes "a module is not a disposition" a mechanism instead of a sentence |
| `check-storage-keys.py` | ✅ **yes, three times in one day**, each time green over a surface it did not scan — viewer-only, then two hand-named files, then a one-level glob `[measured, `tools/check-storage-keys.py:24-53`]` | **T2** | source D feeds the ledger from this roster, and it has been wrong in the green direction three times |
| **G0's negative control** | 🔴 **not built** (G0-R4) | **T0** | stated as unbuilt rather than assumed. A gate whose failure has never been observed is a claim |

### 3.4 · Pre-registered retro questions — mandatory to attempt, conditional to produce

Per the ratified amendment: *"None — pre-registered metric unmoved" is a VALID recorded outcome.* Each carries a
`disposition` ∈ `open|answered|carried|dropped` and an `answered` needs evidence naming something runnable or readable.

| # | question | how it is answered |
|---|---|---|
| **P1** | How many rows left `undecided`, and into which dispositions? | `catchup-ledger.py --status`, per module, with its predicate |
| **P2** | ⭐ **How many dispositions did Paul reverse after ruling them?** | count in `.private/catchup-dispositions.json`. **This is the seat's own defect meter** — two reversals in one class and the class stops being proposed |
| **P3** | Did any item refuse to belong to exactly one module? | the `unclassified` count. Falsifies the unit of work (§2.1) and the finite ruling (§3.1) |
| **P4** | ⭐ Did the `re-collect` asks get answered, declined, or ignored? | the prior is hard: **every ask-shaped surface in the app is 0-for-35; one evening at a kitchen table produced 16 names** `[measured, 09-06 maps proposal §9]`. If re-collect goes 0-for-N, the disposition is not viable and the in-person path is the only live one |
| **P5** | Did anything land in her new household that no ledger row authorised? | the leak test. Answered by the other window's household-scoped read |

### 3.5 · The awareness surface — one line, no new board

**No new board, no new state artifact, no lap counter.** The mom-cycle's existing surface carries it, and the
line is a **count with its denominator and predicate** — never a grade, never an age, never a nag:

```
catch-up · 314 rows · 41 undecided · modules closed 1/6 · archive verified 2026-09-07
```

`tools/catchup-ledger.py --status` joins `CLAUDE.md`'s session-start block so the number has a **non-AI door**
(*deterministic things need a non-AI door*), and the same string renders on the loop board via `render.py`.
⛔ **No staleness age is computed and nothing nags.** A tranche that has not run is not late.

---

## 4 · PRE-GATE vs POST-GATE — where the line sits

### 4.1 · The line, in one sentence

> **An act is POST-GATE if it (i) reaches Mom, (ii) writes into her new production household, or (iii) touches
> the frozen instance's live store. Everything else is preparation.**

(i) and (ii) are Paul's standing rule — *the gate sits on irreversible acts, never on work*. (iii) is his 09-07
ruling as the register already records it: *"every act on the frozen instance — archive re-take, dispositions
landing on the new instance, the sunset order in rule 3 — waits on a real account for Mom existing on production"*
`[BACKLOG.md ~:250]`.

### 4.2 · The two columns

| PRE-GATE — preparation, may run today | POST-GATE — waits on G0 |
|---|---|
| writing the **register line** that records this ruling (§5.3) | the archive **re-take** (§4.3) |
| this file, and any seat file | any **write** into `home` / `est-e6696a` |
| **building `tools/catchup-ledger.py`** + its selftest and mutation controls | **T3** — Paul ruling dispositions |
| a **DRY RUN of the generator against the archive on disk** — read-only, local, no network, values never opened; every row lands `undecided` | any **ask or acknowledgment reaching Mom** |
| deriving the module enum, the `namedBy` predicate, the storage roster (all local, all measured above) | the **drain** of her phone (it is a step of the visit) |
| **drafting** the `re-collect` ask copy — never sending | rotating `SHARED_TOKEN`, tagging, disabling Pages, stopping the bots |
| the production window building the **G0 predicate** (§1.3) | anything in rule 3's sunset order |

⭐ **The dry run is the load-bearing pre-gate act.** It converts every "we will need to decide N things" into a
measured N before the gate lifts, and it costs nothing reversible. Its output is a roster of 314 `undecided`
rows — **a burn-down with its denominator already known on day one**, which is the thing this repo's registers
have repeatedly lacked.

### 4.3 · The archive re-take: POST-GATE, as ruled — and the reason it is right

**Ruled post-gate by Paul on 2026-09-07** and this file does not reopen it. The structural reason it is the
correct placement, stated so nobody re-derives it as an oversight:

- ⭐ **The archive is made current by ADJACENCY to the lockout, not by a cadence.** Rule 3's order already has it:
  drain her phone → **re-archive + `--verify`** → rotate the token → tag → disable Pages → stop the bots. Any
  archive taken before her final write is incomplete by construction, so a scheduled re-take would be stale the
  moment it finished. `[inferred from `BACKLOG.md:180-186` + 09-06 STATE Q4's ordering]`
- **A cadence here would be the permanently-amber control Paul rules against.** *"Archive is N hours old"* is red
  forever by design. The honest instrument is a **dated stamp** — `archivedAt`, `keyCount`, `unreadable[]`,
  `verifiedAt` — printed, never graded.
- **The cost of waiting is bounded and known:** as of 2026-09-07 ~10:15 ET the live namespace held **177 keys vs
  175 archived · 0 changed · 2 gone (both TTL-expired `cache:ambient:*`) · 4 added** `[R, brief, live KV read by
  the main session]`. **The control is intact; the archive is one feedback arrival behind.** That is a stated,
  dated residue, not a defect.

⚠️ **One contradiction, reported and not resolved.** The ruling says *every act on the frozen instance waits*, and
the measurement that produced the ruling was itself a live read of the frozen namespace, made the same morning
`[R, brief]`. So either read-only measurement is outside the gate, or it is inside it and has already been
crossed once. **Both readings are defensible and the choice is Paul's** — it is one line in the register, and §7's
first ruling asks for it. Fail-closed until then: **this window makes no network call to `est-3c9f1a`.**

---

## 5 · THE FREEZE REGISTER

⚠️ **The register is a proposal, not an installed thing.** `freeze.json` does not exist and `tools/freeze.py` does
not exist `[measured, 09-06 register §7]`. Today the canonical register is `BACKLOG.md` § FOCUS FREEZE, whose own
header claims primacy. **I may not edit it** — §5.3 is drafted text for the session that owns it.

### 5.1 · What rows change at gate-lift, in order

| # | row | today | at gate-lift | why this order |
|---|---|---|---|---|
| **R1** | **Track A · C (channel)** | ✅ **LIFTED** `[BACKLOG.md:190, rule 4]` | **unchanged** — recorded so nobody re-freezes it | it is already lifted; the register must say so or the next session re-derives a hold that is gone |
| **R2** | **Catch-up · W (work)** | ⛔ **UNDECLARED** — no register cell names this work | → **ACTIVE**, release condition = **G0** | first, because work must be *declared* before it can be scheduled. An UNDECLARED cell reads red, never green |
| **R3** | **Production · W** | 🟢 ACTIVE | gains the tranche as declared work and **names the ledger as its state** | second: R2 says the work exists; R3 says where its state lives, so the state is never a transcript (§6·F4) |
| **R4** | **Track A · P (push)** | 🧊 FROZEN to human commits | ⛔ **UNCHANGED — FROZEN.** Written as an explicit row | the catch-up writes only to the NEW household. **An unstated row reads as permission**; this is the single most likely wrong act |
| **R5** | **Bots · destination** (S9) | ⛔ UNDECLARED. `weather-recorder[bot]`, `cron: "0 */6 * * *"` `[measured, `.github/workflows/record-weather.yml:6`]` | ruled **before** the final re-take | ⭐ **the final archive is not final while a cron still writes.** Paul's call — it is his weather history |
| **R6** | **The control · currency** | claim: 175 keys, 0 unreadable, taken 09-06 00:08:36 | → a **dated stamp** after the post-gate re-take | **last, and adjacent to the act.** It is the only row whose truth has a moment |

### 5.2 · What the register still cannot check, said plainly

One axis of three is machine-checkable (P, on the pre-push hook). **W is an attestation and C cannot prove nobody
read.** This plan adds nothing to that and should not pretend to: what it adds is that the *catch-up's* state
lives in a ledger a tool computes, so the one thing that historically drifted — *what is done* — is derived rather
than typed.

### 5.3 · The register line that records THIS ruling, now — drafted for the owning session

> ⛔ **Pre-gate, and it is the first act.** A ruling that is not in the register is not in force. This paragraph is
> drafted for `BACKLOG.md` § FOCUS FREEZE by the session that owns that file; **this seat did not write it there.**

```markdown
**⭐ 7. THE CATCH-UP'S GATE, UNIT AND LEDGER** `[agent-proposed 2026-09-07 — Paul rules]` — process of record
for rule 6's *"manual process between you and me"*: `.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md`
(stage `concept`).
- **GATE G0** — a household member record **positively identified as Mom** exists on `home` / `est-e6696a`.
  Written on the observable, not the act, because "her link" (09-07) and "a guided visit" (rule 3) are two
  acts with one consequence. ⛔ **NOT** `reset-production-estate.py`'s `real` abort: that predicate never
  guesses toward synthetic, which is fail-CLOSED for a delete and fail-OPEN for a start gate — an
  unattributable record would open it. Read-only, `unknown` FAILS, paired negative control, `UNCHECKABLE`
  when the store is unreachable. ⚠️ `.private/` has no `fernwood-token-home`, so production is unreadable
  by construction today. **Predicate owed by the production window.** Precondition: Paul walks production
  (cascade gate 2) precedes G0.
- **UNIT** — a tranche is one **module** (`momlib.MODULES`: garden · motor-pool · equipment · house-systems ·
  wildlife · place). ⛔ **A module is NOT a disposition** — the ledger is item-grained and refuses a
  module-level ruling (the 08-10 batch-clear failure).
- **LEDGER** — `.private/catchup-ledger.json`, generated read-only by `tools/catchup-ledger.py` from key
  names, canon and rosters; **no network, no model, values never opened**, proven by mutation.
  **314 rows day one** (175 archive keys · 23 zones · 81 arrivals · 19 storage keys · 16 of her names).
  Private because 2 archived key names embed the weather station's hardware address. The public surface is
  a QUERY (`--status`), never a copy.
- **SHAPE** — ⭐ **FINITE burn-down in module tranches, run inside the existing mom-cycle. No new loop, no
  new state artifact, no lap counter.**
- **THE LINE** — post-gate = (i) reaches Mom, (ii) writes into `est-e6696a`, (iii) touches the frozen live
  store. Everything else is preparation; the generator's **dry run against the on-disk archive is pre-gate**.
  The re-take stays **post-gate and adjacent to the lockout** per rule 3's order.
- ⛔ **Track A · P stays FROZEN.** The catch-up never writes to `origin/main` or to her surface.
- ⚠️ Rule 6 cites `.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md`; that file does not exist. Correct the
  pointer or write the file.
```

---

## 6 · FAILURE MODES THIS REPO HAS ALREADY PAID FOR, AND WHAT GUARDS EACH

| # | the failure, with its instance | the guard in this design |
|---|---|---|
| **F1** | ⭐ **The checkbox is not the world.** `BACKLOG.md:74` read *"lap 3 … stays unrun on purpose"* for 26 hours after lap 3 closed `[measured, 09-06 STATE Q1·1]`. **7 of 8 drifted artifacts erred toward *more frozen / more open*** | **`disposition` and `check` are two columns** (§2.6). The roster is derived from the world every run; only the ruling is hand-written. **No hand-typed count of what is done exists anywhere** |
| **F2** | ⭐ **"Routed" = invisible.** `fleet_probe.py:112` counts a row only when `status == "open"`, so 6 of 15 rows vanished and the zero-branch printed *"inbox clear (N filed, all handled)"* `[measured, 09-06 census §1]` | ⛔ **No disposition value removes a row from the count.** Every value renders with the full denominator; `undecided` is the only value that counts down; a total that cannot be computed prints `UNCHECKABLE`, never 0 |
| **F3** | ⭐ **The weather cron republishes the "frozen" site.** `cron: "0 */6 * * *"`, 447 commits; Pages rebuilds from `origin/main` — *"her 'frozen' site has republished every six hours since the ruling"* `[measured, `.github/workflows/record-weather.yml:6`; `BACKLOG.md:144`]` | R5 makes the bot a **register row with a declared `permittedWriters`**, ruled **before** the final re-take. And this plan does not claim the control is static: **the final archive is not final while a cron still writes** |
| **F4** | ⭐ **A disposition that lives only in a transcript is not state.** Z-ACK — her sixteen names, the largest contribution she has made — lived only in `MOM-CYCLE-LOG.md` and *"was not findable as open work"* `[measured, `BACKLOG.md:1585`]`. Four rulings 09-04→09-06 existed in no file. And today: the register points at a plan file that does not exist (§0) | **A ruling is not in force until it is a ROW** with `ruledBy` + `ruledAt` + his verbatim `words`. A tranche cannot close with a ruling that exists only in the chronicle. The chronicle records what the lap did; **the ledger holds what is true** |
| **F5** | ⭐ **The safe-looking direction.** *"Closing a thread and recording the closure are two acts and only the first has a natural trigger"* | The ledger's error direction is deliberately **toward `undecided`** — it over-reports open work and can never under-report it. **Landing is proven only by the `check` column**, run live, at her conditions, after the write |
| **F6** | ⭐ **A batch cleared by one of its members.** 2026-08-10: one Guru turn's self-identification cleared a day of arrivals; **63 of 81 arrivals are `baselined` and were never individually attested** `[measured]` | The generator **refuses a module-level disposition** (§2.1/§2.5). And the 63 baselined arrivals enter the ledger as **rows**, not as a cleared batch — their `whose` is `unknown` until someone looks |
| **F7** | ⭐ **The sanctioned tool violated the sanctioning ruling.** `read-mom-feedback.py --pickup` prints her words at every session start while `BACKLOG.md:88-90` said it prints *"a COUNT… and nothing more"* `[measured]` | The generator is content-free **by construction, proven by a planted-sentinel mutation test** (§2.5) — not by care, and not by a docstring |
| **F8** | ⚠️ **A safety predicate reused as a start signal runs backwards** (§1.2). New here; no local instance yet, which is why it is named before it happens | G0-R3: `unknown` FAILS. G0-R4: a paired negative control |

---

## 7 · ⛔ PAUL MUST RULE — four, ordered

1. **G0's predicate: does `unknown` fail?** I recommend yes — a start gate must require positive evidence, and
   `reset-production-estate.py`'s classifier is deliberately the opposite polarity (§1.2). Ruling this settles
   what the production window builds. **One sentence.**
2. **Does read-only MEASUREMENT of the frozen namespace sit inside or outside the gate?** The 09-07 ruling says
   *every act on the frozen instance waits*; the measurement that produced the ruling was a live read of it
   (§4.3). Both readings are honest; only you can say which you meant. Until you do this window makes **no**
   network call to `est-3c9f1a`.
3. **The disposition enum.** Rule 5 (*informs the design, does not pre-fill her work*) breaks `carry` as a default
   and there is no word for the bucket most rows will need. I propose adding **`informs-build`**, renaming
   *stays-in-the-control* → **`answer-key`** (it is a benchmark, not a shelf), and narrowing `carry` to an
   exception that must justify itself per row (§2.3). **Vocabulary is yours; I have proposed, not adopted.**
4. **The bots' destination (R5), before the final re-take.** It is your weather history and I will not choose.
   The only structural fact: **an archive taken while a cron still writes is not final.**

*(Not on this list, deliberately: which module goes first, any item's disposition, whether the Z-ACK debt is
discharged by building the map with her in person. The first two are yours by definition; the third is already
open as yours at `BACKLOG.md:211` and lands inside the `place` tranche — it needs a form before that tranche can
close, and naming that is as far as method goes.)*

---

## 8 · HANDOFFS TO THE PRODUCTION WINDOW — requirements only, nothing designed here

| # | requirement | why it blocks |
|---|---|---|
| **H1** | **The G0 predicate** — read-only, exit-coded, scoped to `est-e6696a` by derivation, positive identity required, `unknown` and `synthetic` both fail, paired negative control, `UNCHECKABLE` when unreachable. **Must not be `reset-production-estate.py`** | without it there is no gate, only a claim |
| **H2** | **A read-only, household-scoped per-record existence probe** — "does record R exist on `est-e6696a`?" | every `carry`, `drain` and `re-collect` check in §2.6 is unprovable without it, and P5's leak test is unanswerable |
| **H3** | **`fernwood-token-home` in `.private/`** — measured today: `read-onboarding.py`'s `TOKENS` map names it and `.private/` has only `fernwood-token` and `fernwood-token-qa`, so production reads **unreadable by construction** | H1 and H2 both read UNCHECKABLE forever without it |
| **H4** | **The invite / visit act leaves a dated register line**, explicitly labelled an **attestation** | an outbound act is not observable from this repo; an attestation labelled as a measurement is worse than none |
| **H5** | **State cascade gate 2 as G0's precondition in the register** — the production window reports the link follows Paul's walk of production | otherwise G0 reads as reachable today |
| **H6** | **Confirm the ledger's landing surface** — where a `carry` writes on `home`, and that nothing there is pre-filled ahead of her (rule 5) | a `carry` with no destination is `undecided` wearing a ruling |

---

## 9 · WHAT I DECLINED

- **Ordering the six modules.** Structure cannot say which unlocks first; the product's schedule and your
  real-world context do.
- **Ruling any row's disposition**, including the obvious-looking ones. The generator defaults everything to
  `undecided` precisely so no agent can supply one.
- **Resolving *"her link"* (09-07) vs *"a guided visit"* (rule 3).** I made the gate the observable consequence so
  it does not need resolving. If you meant them as different gates, G0 is wrong and §7·1 is where to say so.
- **Deciding whether the Z-ACK debt is discharged by building the map together.** Already yours.
- **Editing anything.** No tracked file was touched; `BACKLOG.md`'s register line is drafted in §5.3, not written.
- **Designing the Worker, the origins, onboarding or tenancy.** The other window's, entirely.

---

## 10 · FALSIFIERS

| claim | what would show it wrong |
|---|---|
| G0 is the right gate | a state of the world where the catch-up should run and no Mom record exists on `est-e6696a` — or one where the record exists and the catch-up must **not** run |
| `unknown` must fail G0 (§1.2) | you rule that an unattributable real-looking record on her household is sufficient evidence she has set up |
| The unit of work is the module | any item that cannot be placed in exactly one of the six without losing meaning → P3's `unclassified` count > 0 |
| The ledger's 314 rows are the right grain | a question you ask that `channel · id · key · module · disposition` cannot answer without opening a value |
| FINITE, not a loop (§3.1) | the catch-up outlives three tranches **and** generates work nothing else triggers → then it needs its own trigger and I was wrong |
| The ledger must be private | a re-measurement showing no archived key name carries a device or personal identifier — my case rests on **two** keys, and two is a thin margin |
| `informs-build` is needed | every row in the first tranche fits `carry`/`re-collect`/`answer-key`/`drop` without strain → then it is a fifth dialect and should be deleted |
| The re-take belongs post-gate | her frozen instance takes a write that the post-gate re-take cannot recover — i.e. adjacency is not enough and a cadence was needed |
| This process is worth its upkeep | at the first tranche's close, zero rows moved out of `undecided` by a ruling that needed the ledger to be found — then prose was sufficient and this is ceremony |
| §2.5's mutation test is sufficient | a sentinel value reaching any output stream, or a value read on any path |

## 11 · WHAT THIS FILE DID NOT DO, SO NOBODY INFERS COVERAGE

- **Did not read Mom's feedback**, open any archived value, fetch any channel, or make any network call. Every
  count above comes from key names, canon files, rosters and source code.
- **Did not run** `check-arrival-dispositions.py`, `read-mom-feedback.py`, `archive-frozen-estate.py`, or any
  production tool. §2.2's arrival figures are `[measured]` by the 09-06 census and `[R]` from the brief.
- **Did not verify KV live.** The 177-vs-175 comparison is the main session's, cited as `[R]`.
- **Did not rank** a module, an item, a vehicle, a note, a zone or a feature.
- **Did not build anything.** `tools/catchup-ledger.py` does not exist; every property in §2.5 is a requirement.
