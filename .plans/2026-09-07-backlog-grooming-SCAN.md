# BACKLOG GROOMING — every item lap 3 did NOT commit, put on the ladder and grouped into slates

- row: process (no BACKLOG row — a grooming pass, same posture as `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` and `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`)
- objective: **O5** — *the loops, checks and seats that build Fernwood are themselves the portfolio artifact.* Bears on **O3**: a lap that can be loaded from a slate is a lap that transfers to instance 2.
- class: engine · **declared** — this is process machinery. ⚠️ If any slate below is ever read as an ORDER, it has been misused; see the gate.
- question: for every item **not** in lap 3's committed scope — what rung is it honestly on, what artifact would prove the next rung, what specific thing blocks it, what should be struck, and which items could be loaded together as ONE lap
- kind: scan
- seats: user-researcher → `.user-research/2026-09-07-beat7-what-matters-most.md` (READ, not commissioned — its seven wants are the collapse key that stops five rows being groomed for one thing)
        practice-steward → waived: this pass grades STAGE and GROUPING, not method. The method audit of this same ladder is `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`, written today by that seat.
        ux-expert · content-steward → waived: no surface is designed and no copy is drafted here.
        ai-advisor → waived: no model boundary is proposed here. J-e is closed for now (`BRIEFING §7`).
        engineering-partner → ⛔ **NOT WAIVED. OWED, and this file inherits the hole.** `CYCLE-LOG` beat 10 records that no engineering view has run this lap, against Paul's own J-b ruling. **Slates 1, 2, 5 and 6 are engineering-shaped and no builder has sized any of them.** Their stage grades are honest; their *cost* is unpriced.
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ **NOTHING EXECUTES AND NOTHING IS RANKED ACROSS LANES** `[paul-ruled 2026-09-07, J-b]`. No BACKLOG row was edited, no canon touched, no plan header changed. Every kill below is a **proposal with a citation**. Criticality is stated only *inside* a lane, only with evidence.
- trails-read: `BACKLOG.md` (3,868 lines) · `PRODUCT-ENGINE.md` · `.plans/2026-09-07-lap3-BRIEFING.md` · `.plans/2026-09-07-lap3-RESEARCH-BRIEF.md` §4 · `.plans/2026-09-07-lap3-OPTIONS-BOARD.md` · `.plans/2026-09-07-lap3-CONSOLIDATION.md` · `.user-research/2026-09-07-beat7-what-matters-most.md` · `cycle/release/CYCLE-LOG.md` (beat 10, read-only) · `OBJECTIVES.md` · `tools/check-backlog-ready.py` (the ladder's own definition)
- cites-does-not-edit: `cycle/release/*` · `tools/*` · `worker/*` · `zones.json` · `.plans/2026-09-07-zones-PLAN.md` · `.plans/2026-09-07-derived-first-draft-PLAN.md` — three sessions are live in this repo tonight and two of those trees are theirs
- stage-note: 2026-09-07 — written after beat 10 committed lap 3's eight items. Paul's ask: *get every backlog item that is NOT in lap 3's committed scope to a clear, honest status … so that future development laps can be loaded from slates instead of re-derived each time.*

---

## 0 · THE ANSWER, ON ONE SCREEN

**Eleven slates.** Nine are Fernwood's to load; two belong to sessions running right now and are named
only so nobody grooms them twice. A slate is *one lap's worth of work that shares a surface, a
dependency or a seam* — so a lap is not five unrelated errands.

**Twelve kills**, every one with a citation. Three of them are rows this pass **verified as already
fixed in the running code** — the failure mode CLAUDE.md calls this repo's most repeated one, found
three more times tonight.

⭐ **The finding that matters most for how the board is read.** Of the remaining work, **the largest
single group is not blocked on a decision and not blocked on a person — it is blocked on nobody having
written down that it is one thing.** Slate 2 (the leak band) is five separately-recorded defects that
are one defect; slate 1 is four separately-recorded arithmetic bugs on one card. Grooming them into
slates is most of the work of doing them.

⛔ **And the finding that should be read first, because it is uncomfortable.** The census this pass was
handed says **"47 rows in play."** Its own table sums to **64** (57 excluding the seven rulings). Every
downstream artifact that reasons from "47" — including the customer-wants consolidation, which says
*"of the 47 census rows, roughly 24 are not about a customer"* — is reasoning from a number nothing
derived. `measured`, §5.

| | |
|---|---|
| slates proposed | **11** (9 loadable · 2 owned elsewhere) |
| kills proposed | **12** — 3 verified-fixed · 5 superseded by a ruling · 2 premise overtaken · 2 notes that were never work |
| blocked, with the blocker named | **7** |
| plan documents in `.plans/` | **93** · 39 `agent-proposed` (awaiting Paul) · 11 `paul-approved` |
| ⭐ §9 · the per-release ask/telemetry/attribution contract | **ruled 2026-09-07** — four fields at the build commit; canon lines drafted, not applied |
| ⭐ §10 · the build sequence | weather → LEG 0 → zones → **the per-estate canon store** (not "plant capture") |
| WIP bands right now | design **1/2** · build **1/1 (+3 declared exceptions)** · concept **11**, uncapped by ruling |

---

## 1 · THE LADDER, AND THE ARTIFACT THAT PROVES EACH RUNG

The ladder is `tools/check-backlog-ready.py`'s `STAGES`, as Paul ruled it 2026-09-07 (A-2 added
`design` and `journey`; R4 → B added `draft`):

`draft → ready → concept → design → journey → build → qa → shipped → retro`

**What proves each rung** — the rubric this pass graded against. A rung is only claimed where the
artifact exists; where it does not, the grade is the rung below and the missing artifact is named.

| rung | what it means | the artifact that PROVES it |
|---|---|---|
| **draft** | a pre-concept item. Raised, not yet argued | a file exists and says what the thing is. No approval stamp needed — `draft` sits *before* `ready` |
| **concept** | the idea is argued and findable | **a proposal with a BACKLOG row and exactly one objective id.** No row = an orphan, and the readiness check says so |
| **design** | how it would work is written down | **a plan whose seats are declared or waived, each with a reason** — and each seat trail OLDER than the plan (seats shape WHAT before the plan drafts HOW) |
| **journey** | a person's path through it is drawn | **an artifact under `.user-research/` drawing that path INCLUDING the failure paths.** ⛔ A happy-path walkthrough is not a journey; the failure branches are the half that earns the rung |
| **build → qa → shipped → retro** | out of scope for this pass | — |

⚠️ **Two caveats the tool states about its own ladder, carried here so nobody reads more into a grade
than is there.** ① The comparison is by list index, so `design` and `journey` read as strictly
sequential and **they are not** — the honest reading is *the furthest rung reached*, not the last one
worked on. ② `design` is legal as both a KIND (what a document is) and a STAGE (where an item is).

⭐ **AND THE BAR IS THE V1, NOT THE FEATURE** `[paul-stated 2026-09-07, BRIEFING §8]`. A row is ready
to build when its **first version** is clear — what it does, for whom, how we would know it worked,
what it needs. ⛔ **The corollary is enforced in every slate below: a v1 must NAME what it defers.**
Every slate's "v1 / defers" line exists because of that ruling. *"We'll refine it later"* is only
honest if the refinement has somewhere to live.

---

## 2 · ⭐ THE SLATES — the deliverable

⛔ **READ THIS BEFORE THE TABLE.** The slates are **not ordered**. They are numbered so they can be
referred to. Grouping is by **kind** — what a slate shares — exactly as instructed:

| grouping key | slates |
|---|---|
| **one SURFACE** (the same screen or card) | 1 · 4 |
| **one SEAM** (the same code boundary or contract) | 2 · 5 · 6 |
| **one DEPENDENCY** (nothing in it is safe until X lands) | 3 · 7 |
| **one AUDIENCE** (a different person is the user) | 8 · 9 |
| **the loop's own record** | 10 |
| **owned by another live session — named, not groomed** | 11 · Z |

---

### SLATE 1 · THE NUMBERS ON THE WEATHER AND SKY CARD
**Shared: one surface.** Everything that renders a *number* on the card Mom demonstrably opens.

| in it | source | stage | why here |
|---|---|---|---|
| four arithmetic/unit defects | census **G1** | **concept → build-ready** | `sun-horizon.json` wrong by 60 min at 18 `:00` entries · every *"in N days"* is +1 · visibility fetched in feet, labelled km · *"REGION · 7 DAYS"* ends the day before yesterday |
| the dark-window cloud row flaps per-load | census **G6** | **concept** | no stall timeout, no user-facing failure line, only a `console.warn`; absent/absent/present/absent across four runs on an unchanged file |
| a stalled fetch is counted nowhere | census **I2** | **concept** | `pageErrors: []` and `failedActions: []` on a run where the main card never loaded — **this is the instrument that would have caught G6**, which is why it belongs in this slate and not in slate 7 |
| define the timing words | seed **P-19** | **draft** | *"worth a look" · "peak this week" · "this month"* — three phrases that nudge her, none with a written predicate |

- **plan already exists:** `.plans/2026-09-07-weather-card-PLAN.md` (`stage: concept`, unstamped) and `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md`. **So this slate is one Paul stamp away from `design`, not a blank page.**
- **v1:** fix the four arithmetic defects + give the cloud row a stall timeout and one honest failure line. **Defers:** P-19's predicates (document them; showing them is a separate call) and any change to what the card *contains*.
- **blocked on:** nothing. All four G1 defects are **estate-independent** — no ruling, no person, no data about anyone.
- ⭐ **criticality, inside the customer lane, with evidence:** `W7` — *the numbers have to be right because she can check them.* The precedent is the strongest single piece of user evidence this project owns: 2026-07-26, the one time a user disbelieved a number here, **she was right by 14×**, standing in rain the grid cell never saw. `validated`.
- **verified tonight:** `daysUntil()` at `viewer.html:16832` computes `Math.round((noon-of-target − midnight-today)/86400000)`, so today reads **1** and yesterday reads **0** (`Math.round(-0.5) === -0` in JS). The G1 claim is **true at HEAD**, unfixed. `measured`.

---

### SLATE 2 · ⭐ THE LEAK BAND — Fernwood's own content inside engine code
**Shared: one seam.** Correct code, with a comment explaining why it was safe, that became false the
moment a second household existed. **Five known sites, one class, one instrument that cannot see it.**

| in it | source | stage |
|---|---|---|
| Fernwood's rain gauge served to Roswell, Dahlonega and Bangor | `BRIEFING §5.1` · `BACKLOG` § INTEGRATIONS | **concept** — fix site named (`engine/viewer.template.html:9118`) |
| Georgia's burn ban rendered in Maine | `BRIEFING §5.1` | **concept** |
| an April-in-Jasper placeholder shown as live conditions, with alerts generated from it | `BRIEFING §5.1` | **concept** |
| 23 zone names reachable via an unguarded fetch | `BRIEFING §5.1` | ⛔ **zones — see slate Z** |
| **every household invited to record *"the first hummingbird at the feeder… the morning the laurel opened"*** | `BRIEFING §5.1`, found by the copy seat | **concept** |
| `check-estate-neutral` tests for NAMES only | census **I3** | **concept** |
| instance content living in engine code, second worked example | `PRODUCT-ENGINE.md` §750 | **concept** |

- **v1:** fix the five sites; add ONE payload-shaped assertion to the neutrality check (or state on its face that it is evidence about names and nothing else). **Defers:** a general instance/engine content contract — that is C5's `class:` axis and already has a home.
- **blocked on:** nothing.
- ⛔ **THE SEARCH PATTERN FOR THE SIXTH, and it belongs in the slate rather than in a person's memory:** *a comment saying "this is safe because…" whose premise is about Fernwood.*
- ⚠️ **Why the instrument row is IN this slate and not in slate 7.** On 2026-09-07 `check-estate-neutral` read **✅ 311 needles / rendered=0** against the very origin four seats walked, while Fernwood's gauge record was rendering at a stranger's house. **The leak was numbers and possessive pronouns; the check tests for names.** A green there is evidence about names and about nothing else. `measured` — CLAUDE.md carries this warning in its own session-start block.
- ⭐ **criticality, inside the engine lane:** this is the only class on the board that is **wrong for every household except Fernwood** and gets *worse* with each household added. `inferred` from the class, `measured` at five sites.
- ⚠️ **Confirmed at HEAD tonight:** `engine/viewer.template.html:20752` still opens the field-note surface with *"the first hummingbird at the feeder, the night the chorus started, the morning the laurel opened."* `measured`.

---

### SLATE 3 · PLACES, ROLES, SETTINGS — a person owns more than one place
**Shared: one dependency.** Nothing in this slate is safe until the front door lands and per-request
scope is real. This is the natural **lap-4** slate, and its shape is already ruled.

| in it | source | stage | note |
|---|---|---|---|
| show roles on the places list | census **C1** · BACKLOG **19b · 19c · C9** | **concept → design** | asked **four times across separate days**, unprompted |
| found a second place (`+` on the list) | census **C4** · BACKLOG **19 ② · 19b** | **concept → design** | ⭐ shape already ruled 09-06, so it starts from a design |
| settings on both surfaces | census **C5** · BACKLOG **19c** | **concept → design** | ⚠️ the colour-precedence half is **KILLED** — see §4.K4 |
| per-request scope | census **C3** · BACKLOG **row 19 ①** | **design** (large) | the enabler under everything above |
| cross-household invitation | census **C2** · BACKLOG **C9** | **concept** | authority ruled 09-03; **mechanics open** — four candidate shapes, none chosen |
| the top level is arranged per person | seed **P-24** | **draft** | *"my mom might choose between condo, Tate and Tiguan; my brother sees the Tiguan nested within Fernwood"* — a constraint on C4/C9, not a feature |
| the row-20 six-artifact review | census **C6** · BACKLOG **row 20** | **concept** — *a reading, not a build* | ⭐ **this is the cheapest thing in the slate and it gates two others** |

- **v1:** the row-20 review first (read the six login→arrive artifacts together, say which recommendations survive), then roles-on-the-list read-only. **Defers:** invitation mechanics, per-person top level, and anything Bob-shaped.
- ⛔ **BLOCKED ON:** committed item **5 — the front door.** Named specifically: the bug this slate would sit on top of only happens *to someone who already exists*, and until the returning step list (committed item 4) exists, no walk can be that person. **This slate cannot be certified before those two land, however well it is built.**
- ⚠️ **`scopeFor()` re-measured tonight and the census number moved:** the census says *"`scopeFor()` has 0 callers; `scopeOf(env)` has 51 call sites."* At HEAD it is **one caller** — `worker.js:3593`, and that call **discards its own result** (`// eslint-disable-line no-unused-vars`) — against **58** `scopeOf(` occurrences. The row's substance stands; its numbers are stale. `measured`.
- ⭐ **criticality, inside the customer lane:** `W3`. ⛔ **And read the count correctly:** *"asked four times"* measures **how long the row has been stuck**, not how much anyone needs it — the pipeline had only a build-and-ship lane, so a concept blocked on a ruling had nowhere to go. `validated`, and it is the researcher's own correction.

---

### SLATE 4 · WHAT ACTUALLY FILLS A PLACE CARD
**Shared: one surface.** What a household's setup answers buy them on screen.

| in it | source | stage |
|---|---|---|
| property type as a declared input | census **D1** · **C7-R3** | **concept** — the type *vocabulary* is the open half |
| the input-to-value matrix | census **D2** · **C7-R3** | **concept** — a filled proposal exists, unruled |
| events / neighbourhood as a domain, gated per estate | census **D3** · **C7-R5** | **concept** |
| route an unanticipated interest somewhere | census **D4** | **concept** |
| an OFF module must look intentional | census **D5** · **C7-R2** | **concept → build-ready** |
| the closed-card empty case | census **B3** · C7 § RULE | **concept → build-ready** |
| what a collapsed card should say per module | census **B1** · **C7-R1** | **concept → design** |
| where RANKING goes now the summary menu is gone | census **B2** | **concept** — unruled |

- **plans already exist:** `.plans/2026-09-07-input-to-value-matrix-PROPOSAL.md` and `.plans/2026-09-07-place-card-AI-BOUNDARY.md`, both `stage: concept`, both unstamped.
- **v1:** D5 + B3 (an OFF module and an empty card both look intentional) — these are the two that are *decided*, and they are the enabling half of everything else on the card. **Defers:** the property-type vocabulary, the events ingestion class, and B2's ranking question.
- ⛔ **BLOCKED ON, specifically:** **B2**, and it is a ruling not a build. Paul's B1 resolution keeps the summary menu's *summarising* job and drops its *ranking* job — so *what matters today* becomes *scan the whole page*, which is the job he opened with. Nobody has ruled where ranking goes.
- ✅ **UNBLOCKED and worth saying so:** J-e is **closed** `[paul-ruled 2026-09-07]` — start with LINKS, which is membership-by-rule, so no AI boundary is owed today. ⭐ The re-open trigger is precise and belongs in the code: **the first time anything SELECTS or FILTERS what appears on the card.**
- ⭐ **criticality, inside the customer lane:** `W2` is **the largest cluster on the whole board** (17 ids, 3 of the 4 fold records) and the only want Paul has framed as a question about what the product should *be*. ⚠️ And the non-obvious half: it probably matters **more** to Mom than to Paul — her measured depth is **2=0 and 3=0**, she reads card faces, so *"nothing here yet"* on a face is not a step on the way to content, **it is the content**. `inferred`, one device, one window, a claim about a different product.

---

### SLATE 5 · HOW ANY RECORD ADMITS A GUESS
**Shared: one seam** — `momlib.DOMAINS`' honesty markers, the contract every domain declares.

| in it | source | stage |
|---|---|---|
| six wildlife domains have no marker path at all | census **H6** · CLAUDE.md **M1** | **concept** |
| one provenance + confidence field across every domain | seed **P-17** (recurrence **3**) | **draft** |
| wildlife confidence markers — 67 records assert presence with no way to say *"we think"* | Tier-3 **#7** | **draft** |
| `group` is double-booked in running code | census **H7** · `VOCABULARY.md` | **concept** |

- **verified tonight, exactly as written:** `check-domains.py` prints **amphibian · bird · fish · lizard · mammal · snake** at **0 marker paths** — 67 records across the six. Plant has 2 paths / 23 marked; weed 1 / 5; insect 1 / 16. `measured`.
- **v1:** back-fill the marker path for the six wildlife domains. **Defers:** P-17's single cross-domain provenance schema (that is a bigger call, and `hold full internally, show less` is its unwritten rule), and the `group` migration.
- ⛔ **BLOCKED ON — and the blocker is SUPPLY, not schema, which CLAUDE.md already warns about.** A harvester that can see four more domains **puts new cards in front of Mom**, and the 5-slot cap binds immediately with 8 already on the bench and none approved. **So this slate cannot ship past the marker back-fill without Paul's gate on the card queue.** Naming that up front is the point of grouping it this way.
- ⚠️ Back-filling the markers themselves is **authoring judgement, not a migration** — it is a person deciding what this record honestly does not know.

---

### SLATE 6 · CAPTURE MUST NOT LIE
**Shared: one seam** — the write path, and what it tells the person who just wrote.

| in it | source | stage |
|---|---|---|
| the constant-id capture lie on "Add a home" | census **E2** | **concept → build-ready** |
| the per-estate capture write path (leg 0) | Tier-2 **row 8** | **concept** — plan exists |
| a true sync disclosure a person could not interpret | `W5` / **F8** | **concept** |
| the ask path and the save path share one error surface | `W5` / **F9** | **concept** |
| `/api/zone-audio`'s `reviewed` has no writer | Tier-1 **row 14** · census **H3** | **draft** — Paul picks the shape |
| capture in the field has **no network**, by permanent site premise | `CLAUDE.md` § THE SITE'S PHYSICAL PREMISE | **concept** |

- **plan already exists:** `.plans/2026-09-07-capture-write-path-PLAN.md` (`stage: concept`, gated at Paul's stamp).
- **verified tonight:** `homes/index.html:243` posts a **constant** `id: "homes-second-home"`; the Worker de-duplicates per UTC day and returns `200 {duplicate:true}` **while the screen shows the success ack**. `measured`. And `worker/worker.js:1909` writes `reviewed: false` at create with **no writer anywhere that sets it true**. `measured`.
- **v1:** E2 — make a second note on the same day store, and make the ack tell the truth. **Defers:** F8/F9's copy (content-steward's, and it reaches a person), the offline capture design, and `reviewed`'s shape.
- ⛔ **BLOCKED ON:** `reviewed` needs **Paul to pick** — have the disposition write it (needs a Worker PATCH) or delete the field. Two legal shapes, and picking is not an agent's.
- ⭐ **criticality, inside the customer lane:** `W5`, and the argument is doctrinal rather than aesthetic. *"Everything is changeable"* is a **promise of reversibility**, and CLAUDE.md's own rule is *it must be TRUE: never call a thing changeable and then make changing it costly.* ⛔ **A promise of reversibility is unenforceable on a record whose destination the person cannot read.** `inferred`, and her documented fear is getting things wrong.
- ⚠️ **GAP 3** — *does a person know where their writing went, and who can see it?* — lives here. It is **no longer a research gap that a visit closes** (ruling 3b); it is work the product owes.

---

### SLATE 7 · THE HARNESS THAT WILL MISLEAD THE NEXT SWEEP
**Shared: one dependency** — every one of these is a property of the synthetic-walk instrument, and
committed item **4** (the returning step list) lands in this band. **This is item 4's successor slate.**

| in it | source | stage |
|---|---|---|
| `_view.json`'s `text` array is deduplicated | census **I1** | **concept** — every *"appears N times"* claim from that record is unsound |
| a stalled fetch counted nowhere | census **I2** | *also in slate 1 — deliberately; it is the same defect read from two sides* |
| `build-viewer.py --check` is GREEN on a build with a JS syntax error; `--extract` destroys the template | census **I4** | **concept** — the `--extract` round-trip divergence is **unruled** |
| the walker's password is in clear in three files | census **I5** | **concept → build-ready** |
| `transcript.personId` is a harness field, not a product behaviour | census **I6** | ⛔ **KILL — see §4.K11** |
| ⭐ the seat roster itself | census **I7** | **concept** — *nobody has opened this design question* |

- **v1:** I5 (redaction across all three files) + I1 (either de-dup deliberately at read time, or stop making count claims from that record). **Defers:** I7 — whether the roster should change is a design question, not a fix.
- ⛔ **NOT GROOMED FURTHER, and I did not touch it:** `tools/*` is off-limits this session and another session is in that tree.
- ⭐ **criticality, inside the process lane, with evidence:** **I7.** `strict` is a PO-box household, structurally immune to every placed-household defect; `wide-eyed`'s whole purpose is unreached after 7 runs; *"Please don't"* — the contact-refusal branch, **and the only route back from a forgotten password** — has never been tapped by any seat, ever. So *"4 of 4 seats pass"* can mean three of them tested it. `measured`, each seat says so in its own run.

---

### SLATE 8 · THE FLEET AND HOUSEHOLD RECORD  *(Track B · WORK lifted, PUSH frozen)*
**Shared: one audience** — Paul is the user, and `vehicles.json` is the schema.

| in it | source | recurrence | stage |
|---|---|---|---|
| ⭐ **asset lifecycle + residency** — active/decommissioned/not-ours/former, and location-bound vs person-bound | **P-02** | 2 | **draft** — ⭐ **the prerequisite; it unblocks P-01 and P-26** |
| the reminder engine — a clock keyed to the real world | **P-01** | **3** | **draft** — *"`B1` reads: no clock at all right now"* |
| the project arc as a record type | **P-04** | **3** | **draft** |
| labels, plates and decals as an identifier source | **P-07** | 2 | **draft** — pairs with P-14 |
| machine lore — normal-but-alarming · incidents · stuck-on | **P-05** | 2 | **draft** |
| a negative finding is a record, and may contradict a receipt | **P-06** | 2 | **draft** |
| readiness — do I already own what this job needs | **P-09** | 1 | **draft** |
| aliases resolve to one asset; *"motor pool"* is his answer, unrecorded | **P-03** | 1 | **draft** — cheap, free to record now |
| the order bank — a standing basket per vendor | **P-10** | 1 | **draft** |
| B3 data collection · V4 VIN photographs · fleet lap 3 (FIRED, deliberately unrun) | BACKLOG **B3 · V4 · H11** | — | **concept** |

- **v1:** **P-02 alone.** Two fields, one row. **Defers:** everything else in the slate, and it says so honestly — P-01's whole design depends on a decommissioned machine not generating a clock.
- **blocked on:** nothing technical. ⚠️ **PUSH is frozen for Track B** `[paul-stated 2026-09-06]` — WORK is lifted, so this slate may be built and may not ship to her surface.
- ⚠️ **Recurrence is a FLOOR, never a ceiling.** May–June has no conversation record at all (the 30-day retention default deleted it before `31aa229`), so a count of 1 may mean *"said once"* or *"the other times were deleted."* `measured`, and the mine says so on its own face.

---

### SLATE 9 · PAUL'S OWN DOOR — the capture surface he does not have
**Shared: one audience.** ⭐ **B0 measured this hole from the code side and the idea mine found it in
his own words three windows running. They are the same hole.**

| in it | source | recurrence | stage |
|---|---|---|---|
| ⭐⭐ where the things that live only in his head go | **P-12** | **3** | **draft** — *"He is asking the question, which means the answer is unclear to him"* |
| ⭐⭐ a one-at-a-time answer queue — **offline, voice-capable** | **P-13** | 2 | **draft** |
| Track B has no ask loop — the only thing the two tracks do not share | BACKLOG **B0** | — | **concept** |
| a deterministic status door for Fernwood | **P-14** | 2 | **draft** |
| the trip assembler — every open item dischargeable by being somewhere | **P-08** | 1 | **draft** |
| paper output — a test sheet you carry to the machine | **P-11** | 1 | **draft** |

- ⭐ **The strongest evidence in the whole seed corpus is here, and it is unusual because it WORKED.** P-13's second expression — *"show me pictures of plants with a hypothesis of the zone, and I confirm"* — he invented on the spot minutes after a generic photo review stalled, **and it is what actually moved data that night.** `validated`.
- ⚠️ **P-13 is Mama's Perspective aimed at him.** Building it twice is exactly the divergence this repo pays for repeatedly. **Any v1 here reuses the ask→fold→acknowledge path or explains why it cannot.**
- ⭐ **P-11 and P-14 both answer standing global rules, which is why they are cheap and keep getting skipped.** P-11 (paper) is the only output channel that works where there is *"no cell reception… coverage falls off with distance from the house."* P-14 is `~/.claude/CLAUDE.md` § *deterministic things need a non-AI door*, in Paul's own words about this repo: *"the click that checks Fernwood goes through Claude too. I would rather avoid that."*
- **v1:** P-14's Fernwood half — its own checks publish results on a cadence instead of waiting for a session to run them. **Defers:** the command centre (that is operating-layer's, and V-1 says so), and P-12/P-13's capture surface.
- **blocked on:** nothing. ⚠️ Scope carefully against operating-layer — half of P-14 is not Fernwood's.

---

### SLATE 10 · THE LOOP'S OWN RECORD  *(named and handed over — I did not touch it)*
**Shared: the loop's own machinery.** ⛔ `cycle/release/*` is off-limits this session and another
session is in it right now (`0aea9b3`, 22:22 tonight).

| in it | source | stage | note |
|---|---|---|---|
| the stage ladder + WIP limits | census **F1** | ✅ **partly RULED tonight** (A-2, A-3) — the bands are live in the checker |
| the `last_lap` state contract | census **F3** · **J-c** | ⛔ **BLOCKED — a ruling Paul owes.** One shape was applied tonight; ratify or reverse |
| who may value-rank | census **F2** · **J-b** | ✅ **RULED** — ⛔ **but the charters still contradict it, see below** |
| dispose of the 11 unread walk runs | census **E5** | **concept** |
| the six-key labelling coverage line | census **E4** | **concept** — carries its own falsifier: at 100% for two laps, delete it |
| the tool census — what has no caller, what must become engine | seed **P-15** | **draft** — `C3` audited skills; **nothing has audited `tools/`** |
| every deferred gate needs a reader | seed **P-27** | **draft** — ⚠️ tagged `assumption`; it is the miner's proposal, **not Paul's want** |
| file the rulings that reached no working list | `OPTIONS-BOARD 2e` | ⚠️ **unverified — see §5.V6** |

- ⛔ **THE ONE THING IN THIS SLATE THAT IS ACTIVELY UNSAFE TO LEAVE:** Paul's J-b ruling asks every seat to state criticality in its own lane, and **three seat charters currently forbid it in as many words** — `user-researcher` (*does not pitch features*), `practice-steward` (*may never say one item matters more than another*), `product-steward` (*may not RANK anything*). **Until that edit lands, a seat asked to weigh in is being asked to violate its own foundation.** `measured`, BRIEFING §7 states it. **This file complied by stating criticality only inside a lane, with evidence — which is the distinction the charters need to carry.**

---

### SLATE 11 · MOM'S CATCH-UP AND THE FROZEN INSTANCE  *(owned by the other window)*
⛔ **Named so nobody grooms it twice.** `[paul-stated 2026-09-07: "keep the other session focused on
the old version of Fernwood that's been frozen"]`

H12 (81 arrivals · 17 dispositioned · **63 batch-cleared and never individually attested** · 1 open) ·
the catch-up rulings R1–R5 (**R2 is answered** — J-f, she starts blank) · M3 (`tateTracker.textSize`
syncs nowhere — **re-verified tonight: `worker.js` contains ZERO mentions of it**) · M2 · the sunset
order · `.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md` (`stage: concept`).
**Gated on:** Mom having a real production account `[paul-stated 2026-09-07, rule 6]`.

### SLATE Z · ZONES AS A FEATURE  *(owned by the dedicated session)*
⛔ **Not groomed, not read past its header, not touched.** Tier-2 **row 7** is the epic; `J-g` scoped it
as *the breadth is the job*; `.plans/2026-09-07-zones-PLAN.md` is at `stage: design` and
`.plans/2026-09-07-zones-plants-v1-journey.md` is its journey artifact. ⭐ **It is the named test of
whether a lap can advance a concept a rung and ship nothing without reading as a failed lap.**

⚠️ **AND ROW 9 IS NEW TONIGHT — NOT FOLDED, NOT MERGED, NOT RATIONALISED.** `BACKLOG.md` **TIER 2 ·
row 9** — *Process B, the derived first draft from an address* — landed hours ago, stamped
`[paul-approved 2026-09-07]`, plan at `.plans/2026-09-07-derived-first-draft-PLAN.md`. Rows **7** and
**8** are the same vintage. ⛔ **A grooming pass's most likely error is treating an hours-old row as an
accretion, and this file explicitly does not.** Row 7's tier placement is flagged **in the row itself**
as Paul's to confirm; if it is re-tiered, the reason line is the evidence and must travel with it.

---

## 3 · BLOCKED — and on the specific thing, not on "a decision"

⛔ **Nine.** Each names the exact thing that would unstick it and who owns that thing. **A row blocked
on a ruling is not a row that failed; it is a row the pipeline had nowhere to put** — which is the
briefing's own diagnosis of why three threads were asked on separate days without moving.

| # | what is blocked | blocked on — **specifically** | whose |
|---|---|---|---|
| **B-1** | **slate 3** entire (places · roles · settings) | committed items **4 + 5** — the returning step list and the front door. The defect fires only for *a person who already exists*, and **39 of 39 lap-2 walks ran `--fresh`**, so no seat has ever been that person. Until both land, a fix here **cannot be proven** | in flight, another session |
| **B-2** | **slate 4**'s ranking half (census **B2**) | **a ruling nobody has made.** Paul's B1 resolution keeps the summary menu's *summarising* job and drops its *ranking* job, so *what matters today* becomes *scan the whole page* — the job he opened with | **Paul** |
| **B-3** | **slate 5** past the marker back-fill | **the card queue's 5-slot cap and Paul's approval gate.** 8 cards already on the bench, **none approved**; wiring four more domains to the harvester puts new cards in front of Mom | **Paul** |
| **B-4** | **slate 6**'s `reviewed` field (Tier-1 row 14) | **Paul picks one of two legal shapes** — have the disposition write it (needs a Worker PATCH), or delete the field | **Paul** |
| **B-5** | **slate 10**'s `last_lap` state contract (census **F3** · **J-c**) | **J-c, still open.** One shape was applied tonight; it wants ratifying or reversing. R6 and R7 both hang on a boundary nothing marks | **Paul** |
| **B-6** | **any seat being asked for criticality** | **the charter edit.** Three foundations forbid in as many words what J-b now asks for. The reconciling sentence exists (BRIEFING §7) and **has not landed in any charter file** | **Paul / the charters' owner** |
| **B-7** | **C8** — the condo build-out | **a compound gate, stated in the row:** C4 · C5 · C7 shipped **and** the FOCUS FREEZE lifted. Not groomed by design — *"a fresh request by construction when the gate opens"* | **Paul** |
| **B-8** | **slate 11** entire | **Mom having a real account on production** `[paul-stated 2026-09-07, rule 6]`. Her invite `p-b91e4d` was minted ~12:05 ET and is **unspent** | **the world** |
| **B-9** | **C9**'s chosen invite shape | ⚠️ **a release condition that is a FACT, not a date:** shape (A) is safe *only while Fernwood is the only estate with people in it*. It must be re-ruled **before instance 2 activates any person who is not Paul's family** — not because it degrades, but because the thing that makes it harmless disappears | **Paul, on that event** |

⭐ **Six of the nine are Paul's, and none of them is large.** B-2, B-4 and B-5 are each one sentence.
That is the shape the briefing predicted: *the backlog captured them correctly; the pipeline only ever
had a build-and-ship lane.*

---

## 4 · ⭐ THE KILL LIST — twelve, each with its citation

> **A backlog that only grows is a backlog nobody can read.** Every strike below is a **proposal**. I
> edited nothing. Where two registers disagree, both are named so the disagreement is visible rather
> than resolved by an agent.

### 4a · Verified FIXED in the running code — three, and this is the class CLAUDE.md calls this repo's most repeated failure

**K1 · `FN_STORAGE_KEY` TDZ — `BACKLOG.md` Tier-1 row **10** and census **H1**.**
> ✅ **FIXED 2026-08-31, `eac5648`** — *"FN_STORAGE_KEY TDZ (field notes now on first paint; was 44
> silent errors/load)"*, in Paul's own commit, from the 2026-08-31 two-pass UX sweep.

`measured` at HEAD: `const FN_STORAGE_KEY` is declared at `viewer.html:14813`, **above**
`renderVehicleItem` (`:14842`) and `renderVehicles` (`:15052`), with a comment explaining exactly why
it lives there. The row says *"has sat open since August"*; it had been fixed **7 days before** the
census copied it forward as `V` — *"read off the live console 08-15; pre-existing, verified at the
merge base."* ⭐ **The census inherited a stale BACKLOG row and re-stamped it as verified.**

**K2 · The Worker deploy workflow's `paths:` — `BACKLOG.md` Tier-1 row **17** and census **H5**.**
> ✅ **FIXED 2026-09-03, `a80dda7`** — *"C6 2a–2c + Guru 1a–1d: … deploy paths."*

`measured` at HEAD: `.github/workflows/deploy-worker.yml` lists `weeds.json`, `insects.json`,
`zones.json` and `turf.json`, under a comment that names the fix — *"the four digest sources the list
forgot."* ⚠️ **The census dates its own verification to 2026-09-03, the same day the fix landed.**

**K3 · A `door` reader — census **T1** / OPTIONS-BOARD **2a**.**
> ✅ **SHIPPED tonight, `72b9276`** — `tools/watch-door.py`, 22:05 ET: *"read the two channels nothing
> read — and it found 18 failures on production."*

⚠️ **Its sibling T2 is NOT killed** — it is committed lap-3 item 3 and shipped at `b8aa535` while this
file was being written. Neither is groomed here.

### 4b · Superseded by a ruling — five

**K4 · Colour precedence, *"which wins"* — census **C5**'s second half and **J-d**.**
> ✅ **RULED 2026-09-06** — `VOCABULARY.md §3g`: **the SCREEN decides.** Inside a place (or its
> settings, or anything derived from it) the place's colour paints; in account settings, the profile
> colour. **They have separate territories and never compete.**

Withdrawn from the briefing at `effebd3` — *"J-d was never open: colour precedence was ruled
2026-09-06 and re-asked anyway."* ⛔ **The `19c` row and census C5 still carry the collision framing.**
Strike the *"which wins"* clause; keep the settings work, which is real.

**K5 · *"A synthetic seat's preference is in the build where Mom's validated answer isn't"* — census **H8**, beat-7 §2.4(a).**
> ⛔ **WITHDRAWN 2026-09-07, `75627a2`.** `BACKLOG.md:476` records **Journal → Fernwood Almanac** as
> **Paul's own ruling, 2026-07-30**, made knowingly against her answer with its reasoning written
> down. The `(mom seat, round 3)` comment covers the *household-prefixed form*, not the name.

`measured` at HEAD: `engine/viewer.template.html:7259` still reads
`JOURNAL_NAME = window.__HOUSEHOLD_NAME + " Almanac"` with that comment — **the code is unchanged and
correct; the finding about it was wrong.** ⭐ And it is **overtaken from the other direction too**:
committed lap-3 item **7** lets each household name its own Almanac, which dissolves the argument
rather than settling it.

**K6 · Tier-3 row **#8**, *"Getting her to adopt Almanac."***
> ✅ **DROPPED FROM TRACKING 2026-08-02** `[paul-stated]` — *"go ahead and drop number seven, like, you
> don't need to keep track of that."* Not reversed, not decided against — **no longer a tracked item.**

⛔ **Two registers in one file disagree today.** § WAITING ON PAUL records the drop; the **Tier-3
table still carries the row live** at `BACKLOG.md:487`. Strike the Tier-3 row; the § WAITING ON PAUL
entry already holds the history, and *"do not re-add a card"* is written there.

**K7 · GAP 2 — *is "add a place" founding or switching?***
> ⛔ **`[paul-ruled 2026-09-07, ruling 3b]`** — *"Do not schedule GAP 2; ask it only if a natural
> moment arises before she opens the app, and treat it as gone otherwise."*

It was valuable **only** before she had seen the UI, and the link is already in her hands. ⭐ **The
honest form of the strike: this is not a question we decided not to ask, it is a measurement whose
window closed silently.** Recording that is the whole value of striking it rather than letting it rot
as an open row nobody schedules.

**K8 · The guided visit, as a mechanism.**
> ⛔ **SUPERSEDED by ruling 3b** `[paul-ruled 2026-09-07]` — *"let's not gate anything on a Mom visit
> or depend on it."*

`BACKLOG.md` § ruling 3 is already struck. ⚠️ **What is NOT yet struck is everything downstream that
still reads as if a visit will happen** — the BRIEFING's GAP-1 protocol (*"on HER phone, before
anything else… read four things"*) describes an act that no longer has an occasion. **Keep GAP 1's
question; strike its protocol.** Its instrument is now T1/T2, both of which shipped tonight.

**K9 · Z-ACK — the acknowledgment owed for the 23 zones.**
> ✅ **CLOSED `[paul-ruled 2026-09-07]`** — *"Don't worry about the acknowledgment to Mom. I'll take
> care of it in person."* ⛔ **Do not design a ribbon, a card, a message or a surface for it.**

`BACKLOG.md:1678` still carries the section as *owed, gated*. Strike it. ⭐ The reason is worth
keeping in one line: **the thing owed was never a feature** — the product would only ever have been a
proxy for a person saying thank you, and a proxy would have been worse than the thing itself.

### 4c · Premise overtaken — two

**K10 · The two lap-1 pre-registrations — census **F5**.**
> ✅ **DISCHARGED.** `BRIEFING §6`: the lap-2 RETRO *"discharges both lap-1 pre-registrations."*
> `48b0474` (19:51 tonight): *"gate ① now prints its coverage; **second-viewport retired**."*

**K11 · Decision cards `fernwood-5` and `fernwood-6`.**
> ⚠️ **`fernwood-5`'s premise is overtaken** — it asks how lap 2 is timed; laps 3–8 have since closed.
> ⚠️ **`fernwood-6`'s premise is FALSE** — it says `check-cards` exits 1. **Verified tonight: it exits
> 0.** `measured`.

⛔ **Answering a card whose premise reality has changed is the same failure as a stale proposal
header.** Both should be **re-minted or retired, not answered as written** — which the pointer block
itself already says, and which nothing has acted on.

### 4d · Never work — one

**K12 · `transcript.personId` is a harness field — census **I6**.**
A **finding that was correctly recorded and then filed as a row.** It has no v1, no falsifier and
nothing to build: the fact is *a seat retracted a finding because it misread a harness field for a
product behaviour.* ⭐ **That belongs in the walk harness's own documentation, next to the field.**
Same shape as I5's redaction note — one is work, the other is a caution.

---

## 5 · VERIFIED AGAINST THE APP — seven rows checked, five had drifted

> **The mandate: verify a row against the app before acting on it.** Three rows were found wrong in
> one session by checking them against the running product; this pass checked seven and found **five**
> that had moved. Two of the five are already in the kill list (K1, K2); the rest are corrections, not
> strikes — the row is real, its numbers are not.

| | claim as written | what is true at HEAD | grade |
|---|---|---|---|
| **V1** | ⭐⭐ *"the census — **47** rows in play"* (`BRIEFING §4`, and every artifact downstream of it) | **64.** The briefing's own table sums A6 + B4 + C6 + D5 + E5 + F5 + G7 + H12 + I7 + J7 = **64**; **57** excluding the seven rulings. **No arithmetic produces 47.** ⛔ The customer-wants file reasons from it — *"of the 47 census rows, roughly 24 are not about a customer"* — so a downstream ratio is built on it | `measured` |
| **V2** | ⭐⭐ `viewer.html` is *"~17,900 lines"* and *">1 MB"* (`CLAUDE.md` § Architecture; census **H10**) | **22,921 lines · 2,179,006 bytes (2.08 MB).** ⚠️ **+28% lines and more than DOUBLE the ceiling that already broke Guru's write-to-canon path for two weeks.** The CLAUDE.md paragraph carries a note that its *previous* number had gone stale by 4× and *"nothing re-derived it."* **It has gone stale again, in the same file, in the same way** | `measured` |
| **V3** | `scopeFor()` has **0 callers**; `scopeOf(env)` has **51** call sites (census **C3**) | `scopeFor(` has **one** caller — `worker/worker.js:3593` — and that call **discards its own result** (`eslint-disable-line no-unused-vars`). `scopeOf(` occurs **58** times. ⭐ **The row's substance is intact and arguably sharper:** the function is not merely uncalled, it is called and ignored | `measured` |
| **V4** | *"DECISION CARDS OPEN — **11 of 12**"* | **13 cards exist** in `.decisions/` — `fernwood-13` was minted 2026-09-04 and the pointer count never moved. ⚠️ The block's own instruction is *"read the count from `decisions.jsonl`, never from this line"*, and the line still states a count | `measured` |
| **V5** | *"the sound pipeline — 17 birds, 8 frogs, unaudited"* (Tier-1 row **11**) | **Exactly 17 and 8.** ✅ Row correct as written | `measured` |
| **V6** | *"File the **20** decisions that nothing has acted on"* (OPTIONS-BOARD **2e**) | ⚠️ **UNVERIFIED — the number appears in that one file and nowhere else in the repo.** No trail, no derivation. ⛔ Per this repo's own rule — *derive a gate's pending count, don't list it* — **whoever grooms 2e should derive the number, not restate it.** Until then it is a claim, not a measurement | `unverified` |
| **V7** | *"`check-cards` exits 1"* (decision card `fernwood-6`) | **Exits 0.** → K11 | `measured` |

### ⭐ 5.1 · One more, found by running the instrument rather than reading it

`tools/product-steward.py` reports **T2 · a seat trail exists and nothing cites it** — three seat
reports that no ranked surface points at: `.ux-reviews/2026-09-06-places-settings-navigation.json` ·
`.user-research/2026-09-04-fictive-test-user.md` · `.engineering/2026-09-06-environment-pipeline.md`.
**It read four an hour ago**; `.user-research/2026-09-07-beat7-what-matters-most.md` dropped off the
list because **this file cites it in `trails-read:`**. `measured`.

⭐ **That is a small, precise demonstration of what grooming is for, and it argues for the practice
rather than for this document:** a seat's whole output was structurally unreachable, and one citation
line in one file closed it. **The remaining three are commissioned work nothing can reach** —
places-and-settings navigation belongs to **slate 3**, the fictive test user to **slate 7**, the
environment pipeline to committed item **1**. ⛔ I did not cite them, because citing a trail I have not
read would be exactly the false attestation the tool exists to catch.

---

## 6 · NOT GROOMED HERE, AND WHY

| | why |
|---|---|
| **lap 3's eight committed items** | ⛔ Off-limits by instruction and by beat 10: *"after this point the plan does not keep evolving."* Two of the eight (**2 · Access** and **3 · the onboarding read route**) landed while this file was being written |
| **`cycle/release/*` · `tools/*` · `worker/*` · any zones file** | ⛔ Off-limits, and **three sessions are live in this repo tonight.** Where a slate names something in those trees, it names it and stops |
| **zones (slate Z) and Process B (Tier-2 row 9)** | Owned by the dedicated session. **Read only far enough to confirm they are not stale** — both are hours old and stamped |
| **the frozen instance (slate 11)** | Owned by the other window `[paul-stated 2026-09-07]` |
| **`H11` — the FOCUS FREEZE list** | ⛔ Listed for visibility, never scheduled. *"Nothing. The freeze lifts on Paul's word and only that."* **A grooming pass may not groom a freeze** |
| **anything about Bob** | ⛔ **Nobody has asked him anything.** Every claim is `assumption`, and the census says so |
| **ranking, of any kind, across lanes** | ⛔ `[paul-ruled 2026-09-07, J-b]`. Criticality appears exactly four times above, each inside one lane, each with evidence and each in a slate |

---

## 7 · WHAT I NEED FROM PAUL — the human gates, in the order they unstick things

⛔ **Nothing below is a request to build.** Each is a sentence, and each releases something.

1. ⭐ **The twelve kills** — strike, keep, or strike-with-a-different-reason. **K6 and K9 are the two
   where two registers in the repo currently disagree with each other**, so leaving them is not
   neutral.
2. **B-2** — where does *ranking* live now the summary menu is gone? (slate 4 cannot finish without it)
3. **B-4** — `/api/zone-audio`'s `reviewed`: write it, or delete the field?
4. **B-5 / J-c** — ratify or reverse tonight's `last_lap` shape.
5. **B-3** — may the wildlife marker back-fill proceed knowing it **increases card supply** against a
   5-slot cap with 8 unapproved cards on the bench?
6. **B-6** — the charter edit. Until it lands, every seat you ask for criticality is being asked to
   break its own foundation.
7. ⚠️ **V1 and V2 are not decisions, they are corrections** — but both live in files other sessions
   are reading right now, and **V2 is in `CLAUDE.md`**, which every session loads. Say whether I fix
   them or hand them over.
8. ⭐ **The slates themselves:** are these the right groupings? A slate is only worth having if a lap
   can be loaded from it without re-deriving. **If any grouping reads as arbitrary, it is — and the
   fix is to say which seam it should share instead.**

---

## Evidence log

- `2026-09-07: [measured] — BACKLOG.md Tier-1 row 10 / census H1 (FN_STORAGE_KEY TDZ) is FIXED at HEAD. viewer.html:14813 declares the const above renderVehicleItem (:14842) and renderVehicles (:15052); the fix landed 2026-08-31 in eac5648, whose own message reads "field notes now on first paint; was 44 silent errors/load".`
- `2026-09-07: [measured] — Tier-1 row 17 / census H5 is FIXED at HEAD. .github/workflows/deploy-worker.yml lists weeds.json, insects.json, zones.json, turf.json; landed 2026-09-03 in a80dda7 — the same date the census gives for verifying it broken.`
- `2026-09-07: [measured] — census T1 is SHIPPED: tools/watch-door.py, commit 72b9276 at 22:05 ET. T2 shipped at b8aa535 while this file was being written and is committed lap-3 scope, not groomed here.`
- `2026-09-07: [measured] — the census holds 64 rows, not 47. A6+B4+C6+D5+E5+F5+G7+H12+I7+J7 = 64; 57 excluding J. The "47" figure appears in BRIEFING §4's heading and in the beat-7 consolidation's ratio and is derived by nothing.`
- `2026-09-07: [measured] — viewer.html is 22,921 lines / 2,179,006 bytes. CLAUDE.md § Architecture states "~17,900 lines (>1 MB)". The same paragraph records that its previous figure had gone stale by 4×.`
- `2026-09-07: [measured] — worker/worker.js: scopeFor( has ONE caller at :3593, marked eslint-disable-line no-unused-vars (the result is discarded); scopeOf( occurs 58 times. Census C3 says 0 and 51.`
- `2026-09-07: [measured] — viewer.html:16832 daysUntil() = Math.round((noon-of-target − midnight-today)/86400000): today → 1, yesterday → 0 (Math.round(-0.5) === -0). Census G1's "+1" and "yesterday renders Tonight" are true at HEAD, unfixed.`
- `2026-09-07: [measured] — check-domains.py: amphibian · bird · fish · lizard · mammal · snake each report 0 marker paths across 67 records. plant 2 paths / 23 marked; weed 1 / 5; insect 1 / 16. Census H6 exact.`
- `2026-09-07: [measured] — homes/index.html:243 posts a constant id "homes-second-home"; worker.js de-duplicates per UTC day behind a success ack. worker.js:1909 writes reviewed:false at create and nothing anywhere sets it true. Census E2 and Tier-1 row 14 both stand.`
- `2026-09-07: [measured] — engine/viewer.template.html:7259 sets JOURNAL_NAME = <household> + " Almanac" with the "(mom seat, round 3)" comment, unchanged. The code is correct; the FINDING about it was withdrawn at 75627a2, and BACKLOG.md:476 records the rename as Paul's own 2026-07-30 consolidation ruling.`
- `2026-09-07: [measured] — engine/viewer.template.html:20752 still opens the field-note surface with "the first hummingbird at the feeder, the night the chorus started, the morning the laurel opened" — Fernwood's own content, offered to every household. The fifth instance of the leak class, found by the copy seat.`
- `2026-09-07: [measured] — worker/worker.js contains ZERO mentions of textSize; viewer.html:22801 is the only writer. M3 stands. The engine comment at :7215 notes the key "retires with the toggle (C6 Q1)", so M3's live blast radius is the frozen instance and the migration.`
- `2026-09-07: [measured] — sounds/birds/ holds 17 files and sounds/frogs/ 8. Tier-1 row 11's counts are correct as written.`
- `2026-09-07: [measured] — check-cards.py exits 0. Decision card fernwood-6's premise ("it exits 1") is false. .decisions/ holds 13 cards; the pointer block says "11 of 12".`
- `2026-09-07: [measured] — check-backlog-ready.py at HEAD: 127 flags across 37 plans; WIP design 1/2, build 1/1 (+3 declared exceptions), concept 11 uncapped; 8 typed documents carry no header block at all. .plans/ holds 93 files: 39 ready: agent-proposed, 11 paul-approved.`
- `2026-09-07: [measured] — tools/product-steward.py T2 reports 3 uncited seat trails (places-settings-navigation · fictive-test-user · environment-pipeline). It reported 4 before this file cited beat7-what-matters-most in trails-read:.`
- `2026-09-07: [measured] — cycle/release/CYCLE-LOG.md beat 10 commits 8 items in 2 phases and records three unknowns and one accepted risk (phase 1 holds four items against a build band of 1/1).`
- `2026-09-07: [paul-ruled] — ruling 3b (BACKLOG.md § 3b): nothing is gated on a Mom visit; GAP 2 is to be treated as gone. Z-ACK closed, discharged in person. J-a, J-b, J-e, J-f ruled (BRIEFING §7). J-d withdrawn — ruled 2026-09-06, VOCABULARY.md §3g.`
- `2026-08-02: [paul-stated] — "go ahead and drop number seven… you don't need to keep track of that" — the Almanac-adoption row is dropped from tracking; § WAITING ON PAUL records it and the Tier-3 table does not.`
- `2026-09-07: [inferred] — the largest remaining group is not blocked on a decision or a person but on nobody having recorded that several rows are one thing (slates 1 and 2). Inferred from the row counts, not measured: 4 arithmetic rows on one card, 5 leak sites in one class.`
- `2026-09-07: [proposed] — all eleven slates, all twelve kills, and every v1/defers line. Nothing here is ruled and nothing executed.`
- `⛔ Unverified and named as such: OPTIONS-BOARD 2e's count of 20 rulings carried into no working list — the figure exists in that file alone, with no derivation anywhere in the repo.`
- `⛔ Not assessed, by instruction: lap 3's eight committed items · cycle/release/* · tools/* · worker/* · every zones artifact · the frozen instance · anything about Bob.`

---

## 8 · ⭐⭐ THE ZONES ARTIFACT AS A TEMPLATE — and every slate mapped against it
`[paul-asked 2026-09-07, late: "that's a good kind of template for how to establish long-term vision and a
shorter term… whether we have that v1 build plan as sufficient for the next build lap… and we can start to
map everything against that"]`

Added after §7 at Paul's ask, having read `handoff/handoff-zones-decisions.md` and
`.plans/2026-09-07-zones-PLAN.md` §0 · §6 · §7 · §8 · §9. ⛔ **Read-only. I edited nothing in that lane.**

### 8.1 · What the template IS — nine parts, named so they can be reused

The zones artifact is not one document, it is a **shape**. Naming its parts is what makes it a template
rather than a good file someone admired.

| | part | what it does that a normal plan does not |
|---|---|---|
| **T1** | **A rulings register** — Z-1…Z-12, **verbatim**, numbered, each with a *"where the consequence lives"* column | it makes a spoken decision **findable**, which is this repo's own ratified rule: *a load-bearing ruling that is not in the register is not in force* |
| **T2** | **A decisions table** — R-Z1…R-Z6, each **ruled · parked · withdrawn**, with what it cost | ⭐ a *parked* and a *withdrawn* decision are recorded as **outcomes**, not as silence. R-Z5 says *"do not re-raise as a blocker"* in the artifact itself |
| **T3** | ⛔ **A retractions section, read-before-anything-older** — the four things this session took back | **the part almost nothing else in this repo has**, and the one that saves the most time. Two of the four had already reached other artifacts as findings |
| **T4** | **Findings that outlive the v1** — the durable claims, held **apart from the build** | *a named place, geometry optional* survives whatever gets built. Separating them stops a good finding dying with a deferred feature |
| **T5** | **Horizons** — `LEG 0 · V1 · NEAR · LONG · STANDING RESEARCH`, ⭐ **each naming what the one below defers**, and ⛔ **no state column** | this is Paul's own v1 rule made structural. The state column was removed after going stale **within hours** — each plan's `stage:` is the state |
| **T6** | **The V1, argued against itself** | ⭐ §6's third bullet argues the v1 is *"the case with the LEAST automation leverage"* — a plan that states its own weakest point is one you can trust the rest of |
| **T7** | **DEFERS, numbered — and ⛔ REFUSED kept separate** | *deferred* and *refused* are different promises. Most backlogs collapse them, and then a refusal quietly reads as a queue |
| **T8** | **OPEN vs NOT-OPEN**, with *"do not re-raise"* named | closes the loop that produces repeat asks. Five open, five not — and the five not-open are named individually |
| **T9** | **Repo conditions + the method lesson** | ⭐ *"true of the layer queried, false of the question asked"* — five claims reported verified that were not, **three caught by seats, not by the author.** *Budget for that, or install the control* |

⭐ **AND THE PATTERN THAT HOLDS IT TOGETHER, which is §0's:** superseded material is **marked in place, not
edited away**, behind a *read this first* pointer. Four things in the plan's body are wrong and are labelled
wrong rather than deleted — so a reader who arrives at the body from a search still gets the correction.

### 8.2 · Is the v1 sufficient to load the next BUILD lap?

> **For the next lap: yes. For its BUILD band: not yet — and the artifact says so on its own face in three
> places, which is exactly what a good plan is supposed to do.**

| what says so | where |
|---|---|
| **LEG 0's first act may rewrite the plan** — the R-Z6 probe returned `HTTP 401`, so it is **UNCHECKABLE, never "empty"**. *"It may rewrite the plan rather than patch it"* | handoff § What is OPEN ①· R-Z6 |
| **Content-steward DRAFTING is owed** — a review has run, the copy has not been written. The v1 reaches a person, so copy is not a finishing step | handoff § OPEN ③ |
| **Z-12 is a stance, not a design** — *"needs user-researcher + content-steward before anything is built"* | handoff § OPEN ④ |

⭐ **So the honest lap shape is already written in the artifact, and it is not "build the v1":**
**probe first → let the answer rewrite or confirm LEG 0 → then the v1 amendment.** LEG 0 is *"a gate move,
not a build"* (§0 ④, engineering-partner, verified) — which is why it is loadable now and the v1 is not.

⚠️ **One WIP fact to weigh, not an objection:** the build band is **1/1 with three declared exceptions
already**, and lap 3's phase 1 took a knowing four-against-one exception. **LEG 0 would be the fifth
in-flight build item.** That is Paul's call and it is a real cost, not a rule violation.

### 8.3 · ⭐ The epic is one rung ahead of its own header

`measured`: `.plans/2026-09-07-zones-PLAN.md` reads `stage: design`. But
`.user-research/2026-09-07-zones-plants-v1-journey.md` **exists and carries §W.4 · Failure paths** —
*she declines · says nothing · contradicts herself · renames something we already named · corrects
something and cannot say why*. **By the rubric in §1 of this file, that is the `journey` rung.**

⛔ **I am not moving it — it is another session's file.** But it is worth Paul knowing that the one item
that has reached the highest rung on the ladder is under-reporting itself, and the ladder's own caveat
covers this: **it records the furthest rung reached, not the last one worked on.**

⚠️ **And one honest wrinkle in the instrument, which is not a defect to fix tonight.**
`check-backlog-ready.py` flags the zones plan twice — *"engineering-partner's / ux-expert's trail is NEWER
than the plan — seats shape WHAT before the plan drafts HOW."* **The flag is true.** The plan was drafted,
then three seats reviewed it, **and that review is what produced §0 — the single best section in the
template.** So the checker is currently penalising the practice that made the artifact good. ⭐ **The
distinction the rule is missing: a seat that SHAPES a plan should precede it; a seat that REVIEWS one must
follow it.** → `slate 10`, and it is the process session's, not mine.

### 8.4 · ⭐⭐ EVERY SLATE MAPPED AGAINST THE TEMPLATE — and the finding is about cost, not quality

`measured` — presence of each part, per slate. ✅ present · 🟡 partial or scattered · ⬜ absent.

| slate | T1 rulings | T2 decisions | T3 retractions | T4 findings | T5 horizons | T6 v1 | T7 defers | T8 open/not | plan file? |
|---|---|---|---|---|---|---|---|---|---|
| **Z · zones** | ✅ 12 | ✅ 6 | ✅ 4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ `design` |
| **6 · capture must not lie** | 🟡 | 🟡 | ⬜ | ✅ | ✅ *(it IS zones' LEG 0)* | ✅ | 🟡 | ✅ | ✅ `concept` |
| **4 · what fills a card** | 🟡 C7-R1…R5 | ⬜ | ⬜ | 🟡 | ⬜ | 🟡 | ⬜ | ⬜ | ✅ ×2 `concept` |
| **1 · the numbers** | ⬜ | ⬜ | ⬜ | 🟡 | ⬜ | 🟡 | ⬜ | ⬜ | ✅ `concept` |
| **3 · places · roles · settings** | 🟡 19b · 19c | ⬜ | ⬜ | 🟡 | ⬜ | ⬜ | ⬜ | 🟡 | 🟡 proposal |
| **2 · the leak band** | ⬜ | ⬜ | ⬜ | ✅ *the search pattern* | ⬜ | ⬜ | ⬜ | ⬜ | ⛔ **none** |
| **5 · honesty markers** | ⬜ | ⬜ | ⬜ | 🟡 | ⬜ | ⬜ | ⬜ | ⬜ | ⛔ none |
| **7 · the harness** | ⬜ | ⬜ | ⬜ | ✅ *I1 · I4 · I7* | ⬜ | ⬜ | ⬜ | ⬜ | ⛔ none |
| **8 · the fleet record** | ⬜ | ⬜ | ⬜ | 🟡 | ⬜ | ⬜ | ⬜ | ⬜ | ⛔ none |
| **9 · Paul's own door** | ⬜ | ⬜ | ⬜ | 🟡 | ⬜ | ⬜ | ⬜ | ⬜ | ⛔ none |

> ### ⭐⭐ THE READING, and it changes what grooming is for
>
> **The template exists exactly ONCE, and it was produced by a dedicated session with Paul in the room.**
> Slate 6 is the only other one close, and it got there by being **carved out of that same session**.
>
> ⛔ **So the template is a SCOPING-SESSION output, not a grooming output** — and that is the answer to
> *"can we map everything against it."* Three of its nine parts **cannot be produced without Paul**:
> **T1** (his rulings, verbatim), **T2** (his decisions), and **T6** (a v1 argued *with* him — Z-3, Z-4
> and Z-10 are all his). No amount of reading the record manufactures those.
>
> ⭐ **But five of the nine can be prepared IN ADVANCE, from the record, with no session at all:**
> **T3** retractions · **T4** durable findings · **T5** horizons · **T7** defers/refused · **T8**
> open vs do-not-re-raise. **This file is those five parts, for nine slates at once** — §2 is T5 + T7,
> §3 is T8, §4 is T3, §5 is T4.

### 8.5 · What that implies for how a lap gets loaded — proposed, Paul rules

**A two-step, and it makes the expensive half small:**

1. **GROOMING PREPS THE SHELL** — T3 · T4 · T5 · T7 · T8, from the record, no session. **Done for nine
   slates as of this file.**
2. **ONE SCOPING SESSION PER SLATE FILLS T1 · T2 · T6** — Paul in the room, rulings recorded verbatim,
   the v1 argued with him. **Zones cost one evening and produced twelve rulings and six decisions.**
3. **The plan is then loadable**, and the checker can grade it because every field it wants exists.

⭐ **Why this is worth the shape rather than just doing the work:** the briefing's own diagnosis is that
three threads were asked on separate days without moving **because each was blocked on something that was
not a build, and the pipeline only had a build-and-ship lane.** A scoping session is that missing lane —
**zones is the proof it works**, and it is the named test of whether a lap can advance a concept a rung and
ship nothing without reading as a failed lap.

⚠️ **The cost, stated plainly rather than buried:** at one evening per slate, nine slates is nine evenings
of Paul's attention. ⛔ **That is a reason to pick which slates get one — not a reason to skip the step.**
The five prepared parts are what make the choosing possible, and **a slate can also legitimately be told:
you get a v1 and no epic.** Not everything is an epic; zones is one because Paul ruled it one (Z-2).

---

## 9 · ⭐⭐ THE PER-RELEASE ASK & ATTRIBUTION CONTRACT `[paul-ruled 2026-09-07, late]`

⛔ **Recorded because it is load-bearing and because this repo's own ratified rule is that a
load-bearing ruling which is not in the register is not in force.** Paul: *"Yes. That sounds good."*
⛔ **Nothing here is applied to canon** — §9.6 drafts the canon lines for his go.

### 9.1 · The rulings, verbatim

| | ruling | scope |
|---|---|---|
| **RC-1** | *"we also want to have, with each new release, a new set of questions that we ask for confirmation or to inform next steps. But that needs to be something that's included and related to each build commit for each lap."* | every release |
| **RC-2** | *"we need for each backlog item to be associated with a telemetry ask **and check**."* | every backlog item |
| **RC-3** | *"as well as an update message to the acknowledgment ribbon — 'hey, here's a new feature.' Should be linked to any feedback that they provided, which, again, we're ideally asking for. So there is a clear link."* | every item that traces to feedback |
| **RC-4** | *"with a hyperlink they can click to just take them down to that section."* | the ribbon line |
| **RC-5** | *"at one point we had created some kind of rules or intentions for that whole section of Mom's feedback… that's probably something we should dig up and look at as an initial template for what we ask for with each build release."* | §9.3 is that dig |

### 9.2 · The contract — four fields, verifiable AT THE BUILD COMMIT

⭐ **`at the build commit` is RC-1's own words and it is the half that makes this a gate rather than a
document.** A field that is true at the commit is checkable; a field that is true "for the lap" is
remembered.

| # | field | what it is | what already exists |
|---|---|---|---|
| **F1** | **the ask** | the question(s) this item ships with — *confirm* or *inform next steps* | `questions.json` + `postAnswer`; the harvest → bench → `--approve` path. ⚠️ **the binding constraint is SUPPLY**: 5-slot cap, 8 cards on the bench, **none approved** |
| **F2** | **the telemetry ask AND its check** | the event the item fires, **and the reader that reads it** | 23 telemetry writers in the Worker; `read-mom-funnel.py` / `read-mom-engagement.py` are the reader shape |
| **F3** | **the ribbon line + its hyperlink** | *"here's a new feature"*, attributed to the feedback that caused it, linked to where they can see it | ✅ **built 2026-07-29** — `MOM_ACK_DATA.links = [{phrase, card}]`, an underlined phrase **inside** the sentence, `linkCard` a **field, not a hard-coded case**, so any card can be the target. **Nothing to build; it becomes required** |
| **F4** | **the release note** | the changelog half, for changes that do **not** trace to feedback | `RELEASE_NOTES.md` + `build-release-notes.py` → the *Recent updates* card |

> ### ⭐ RC-2's "AND CHECK" IS THE LOAD-BEARING CLAUSE, and tonight proved it twice
> `measured` — `GET /api/door` existed and **no tool called it**; `/api/onboarding-metrics` had **no
> GET route at all** and was write-only, so **every onboarding signal from two laps was invisible**.
> **A telemetry ask without a reader is the exact failure**, and RC-2's phrasing already excludes it.
> ⭐ This also **settles census G3**, which had been sitting as *"where instrumentation sits in the
> process — retro material, unsettled."* It sits on the item, at its build commit.

> ### ⚠️ THE ONE TENSION, and Paul's own prior ruling resolves it rather than this file
> The ribbon is **ATTRIBUTION, NOT INFORMATION** `[paul-stated 2026-08-04]`: *"it refreshes on HER
> events, never on ours"* — and **a ribbon that fires on our shipping cadence is a changelog wearing
> the ribbon's clothes, which is the named failure mode.** RC-1 ships a release every lap; RC-3 wants
> a ribbon line with it. **They only agree because RC-3 says *linked to any feedback that they
> provided*.**
>
> **So the contract reads:** a release that **traces to something they gave** earns a ribbon line
> with its hyperlink (F3); one that does not gets a **release note only** (F4). ⭐ **And the loop
> closes on itself: F1's asks are what CREATE the attribution that makes F3 legitimate** — which is
> the same input-to-value cycle Paul stated at 11:30 ET the same day.

### 9.3 · ⭐ THE DUG-UP TEMPLATE — the ask-design corpus, assembled from six places `[RC-5]`

**It was never written down as one thing. It is scattered across a JSON field, a Python template bank,
a tool's approval gate, CLAUDE.md's standing rules and two BACKLOG sections.**

| # | source | the rule |
|---|---|---|
| **T-a** | `questions.json._ordering` | ⭐ **THE RANKING AXIS** `[paul-ruled 2026-07-29]`: *an answer that unblocks a **BUILD** outranks one that fills a **canon gap**, which outranks a **verdict on our own guess**.* Observation/expertise cards lead · verdict cards trail · **preference cards last — no canon target, so no fold path and nothing to probe** |
| **T-b** | `harvest-questions.py` `TEMPLATES` | ⭐⭐ **AN ASK IS NOT FINISHED UNTIL IT NAMES THE OBSERVABLE.** `variety` ships **deliberately unservable**, with a bracket a human must fill — *"no generic string can produce one, and the old string's 'Does that match what's out there?' **sounded finished**, which is exactly how a verdict card gets flipped live by accident."* `identity` needs no human because the record states its own check (`momConfirm.confirmBy`). **Where the record names the check, the ask writes itself; where it does not, a human writes it — and the template refuses to look finished until they do** |
| **T-c** | BACKLOG § TIER 3 | **A row without ① the question and ② how the answer gets captured is on the kill list.** ⭐ **Structurally identical to RC-2** — the same rule, already ruled, for asks instead of telemetry. Strong precedent for making RC-2 a gate |
| **T-d** | `rationalize-bench.py` | **The human gate:** `approvedForServe` is stamped by nothing but `--approve`, run by a person — *"multiple supply streams feed the bench and each will grow its own approval rules; this gate is the floor under all of them."* And **variety is a HARD constraint, a filter not a tiebreaker** — a pure information-value sort stacks all five slots with bloom cards |
| **T-e** | `CLAUDE.md` § four standing rules | one affirmative grammar everywhere she taps · the ribbon covers **everything since her last input, each phrase linked** · the queue ordered by information value · her feedback checked first · **"everything is changeable"**, with its journey-aware caveat |
| **T-f** | BACKLOG § A4 / W8 | **the brake on sprawl** — do not add a surface; the cure is the defer-affordances doctrine, not more items. W8·a resolved the input stack to four cards |
| **T-g** | `CLAUDE.md` § the AI boundary | **card phrasing is the deterministic template bank, NOT AI.** Authored content reaching a person is human-confirmed. Eight forbidden creep modes |

### 9.4 · ⚠️ THE MEASURED CONTEXT THAT MUST RIDE WITH THE TEMPLATE

⛔ **Any contract built on the confirm queue inherits these, and they are measured, not argued.**

- ⭐⭐ **`_ordering`'s own field carries its correction:** *"every `momqueue_offered` event ever recorded
  on her device carries **position 0** — she has never been offered a card at position 1–4."* Since
  `05db30a` the queue renders **one question at a time** behind *"Another question ›"*, and
  `momqueue_tapped` is **3 across 60 days**. ⛔ **The effective visible set is 1, not 5** — so
  *"position 6+ renders to nobody"* is true of position 1+ as well.
- **Every ask-shaped affordance is 0 of 35**; the one affordance that merely MOVES her is 5 of 5.
- **Depth 2 and depth 3 are both zero** — she reads card faces and does not open individuals.
- ⚠️ All of the above is **one device, one window, on a DIFFERENT product** (the frozen instance). A
  deviceId is a browser bucket, not a person.

### 9.5 · ⛔ THE ONE RULING OWED BEFORE THE FIRST LAP RUNS UNDER THIS CONTRACT

> **Decision card `fernwood-11` — *"is the confirm queue the wrong instrument, or the right one asked
> wrong?"* — is OPEN**, and it is the instrument RC-1 would run on every lap.

⭐ **This is a sequencing point, not an objection.** The contract can say safely and now: **every item
ships with an ask, a telemetry check, and a ribbon line where it traces to feedback.** *Which surface
serves the ask* is `fernwood-11`, it is one ruling, and it is worth taking **before** the first lap
runs under the contract rather than after — otherwise the contract's first act is to put more cards
into a surface measured at 0 for 35. ⚠️ See also BACKLOG § **A-ASK** — the ask design is scoping work
Paul has seeded, *"not a change to make quietly."*

### 9.6 · The canon lines, DRAFTED not applied — Paul's go, and his choice of site

⛔ **I have not edited `BACKLOG.md` or `CLAUDE.md`; three lanes are live in this repo tonight.**

**① For `BACKLOG.md`, as a ruling block near the standing rules:**

> **⭐⭐ EVERY ITEM SHIPS WITH AN ASK, A CHECK AND AN ATTRIBUTION** `[paul-ruled 2026-09-07]` — *"with
> each new release, a new set of questions… included and related to each build commit for each lap"* ·
> *"each backlog item associated with a telemetry ask and check"* · *"an update message to the
> acknowledgment ribbon… linked to any feedback that they provided… with a hyperlink they can click to
> take them down to that section."* Four fields, verifiable **at the build commit**: **the ask** ·
> **the telemetry event and its reader** · **the ribbon line and its `links:[{phrase,card}]` target,
> where the item traces to feedback** · **the release note otherwise.** ⛔ The ribbon stays
> ATTRIBUTION, not information (2026-08-04) — a change nobody caused belongs in *Recent updates*.
> Template for the ask: `.plans/2026-09-07-backlog-grooming-SCAN.md` §9.3. ⚠️ Which surface serves the
> ask is decision card `fernwood-11`, open.

**② For `CLAUDE.md` § Design-time default, one line:**

> **Every item ships with an ask, a telemetry check, and an attribution** `[paul-ruled 2026-09-07]`.
> Four fields at the build commit — ask · telemetry event **and its reader** · ribbon line with its
> hyperlink where the item traces to feedback · release note otherwise. **A telemetry event with no
> reader is the failure this exists to prevent** (`door` had a route and no caller;
> `onboarding-metrics` had no route at all). Full contract + the assembled ask template:
> `.plans/2026-09-07-backlog-grooming-SCAN.md` §9.

---

## 10 · ⭐ THE BUILD SEQUENCE — derived from dependencies, not from value `[paul-asked 2026-09-07, late]`

⛔ **This orders by DEPENDENCY, which is derivable. It does not rank by value, which is Paul's**
`[J-b]`. Where two items have no dependency between them, this file says so rather than choosing.

| | item | why here | verified |
|---|---|---|---|
| **1** | ⭐ **WEATHER v1** | ⭐ **the only one of the four that does not touch the write path.** Its capture is two opt-in answers via `postAnswer` → `/api/feedback`, and the five capture handlers work at `home` today | `measured` |
| **2** | ⛔ **LEG 0 — the per-estate capture write path** | **not zones.** The zones plan's own words: *"THE FIRST THING TO BUILD IS NEITHER ZONES NOR PLANTS — IT IS THE PER-ESTATE WRITE PATH."* It has a plan, a BACKLOG row (TIER 2 · 8) and a waiting session; ⚠️ its first act (the R-Z6 probe, `HTTP 401` = UNCHECKABLE) **may rewrite it rather than patch it** | `measured` |
| **3** | **ZONES v1 — zones × plants, species level** | Z-10/Z-11's cascade: address → zones → plants in those zones. Stage `design` with a journey artifact | — |
| **4** | ⛔ **NOT "plant capture" — the PER-ESTATE CANON STORE**, of which plant capture is the first consumer | **§10.1** | `measured` |

### ⭐⭐ 10.1 · ZONES AND PLANT CAPTURE ARE NOT THE SAME SIZE, and the difference sets the sequence

`measured` at HEAD tonight: `handleZoneSave` (`worker.js:3916`), `handlePromoteSpecies` and
`handleRemoveSpecies` (`:2969`) **all open with the identical gate** —
`if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) return 503` — and there are **9 `ghPutFile` sites** writing
`plants.json`, `viewer.html`, the photo, the audio and `zones.json`. ⛔ **Mom's production instance has
no `GITHUB_TOKEN`, deliberately and permanently** (`wrangler.toml`: a token there would promote species
onto her live branch).

⭐ **But underneath the identical gate the two are different:**

| | zone-save | plant capture |
|---|---|---|
| what sits under the git gate | ⭐ **a KV write ~80 lines below** (`:3999`), whose own comment reads *"KV first because it's the freshness path; git commits remain as long-term canon"* | ⛔ **nothing.** Canon **is** `plants.json` in this repo, and re-inlining `viewer.html` is part of the write |
| therefore LEG 0 is | **a gate move** — the 503 is at the wrong granularity | ⛔ **a data-model decision** |

> ⛔ **So plant capture is the first item where the cascade stops being a build and becomes a question:
> where does a household's plant record LIVE, if not in this repo?** And it lands on **W6** —
> species-level vs instance-level — **deferred since July**. The zones v1 ships at species level and
> *names what fires W6*; **plant capture is what fires it.**

⭐ **The recommendation, and it is a naming change rather than a scope change:** after zones, put **the
per-estate canon store** on the board, with plant capture as its first consumer. Sizing it before a lap
opens is cheap; discovering it mid-lap is the failure this whole grooming pass exists to prevent.

---

## 11 · ⭐ THE GLANCE CONSOLIDATION — jump strip · summary tiles · cards `[paul-raised 2026-09-07, late: "I'd like to go ahead and add [it]… let's see what questions are outstanding"]`

**Slate 4's glance half, pulled out because Paul asked for it by name.** `measured` at HEAD — all three
layers are live: `.jump-strip` (`engine/viewer.template.html:4206`), `renderDashboardStrip()`
(`:18534`), and the cards. C7-R1's framing stands: *three layers repeat one thing — emoji · tile line ·
big card.*

⭐ **It looks straightforward and two of its four parts are. The third is the whole point of the
feature and it is unruled.**

| | question | state |
|---|---|---|
| **G-a** | ⛔ **WHERE DOES RANKING GO?** (census **B2**) | 🔴 **OPEN — Paul's, and it is the load-bearing one** |
| **G-b** | Re-measure the strip's telemetry before anything is argued from it (census **B4**) | 🔍 **HUNT — and the current evidence is `contested`** |
| **G-c** | The closed-card **empty** case, and an **OFF** module looking intentional (**B3 · C7-R2 · D5**) | ✅ **DECIDED — build-ready** |
| **G-d** | Which layer is the door, which the glance, which the room (**C7-R1**) | 🟡 **half-ruled 2026-09-07** |

### G-a · the one that is not straightforward
**The summary menu did TWO jobs — it SUMMARISED and it RANKED.** Paul's 2026-09-07 resolution (*keep
the jump strip; collapse the summary intelligence into the cards; re-analyse the closed-card state*)
preserves the first and **drops the second** — so *"tell me what matters today"* becomes *"scan the
whole page"*, **which is the job he opened with.** `inferred`, and it is census B2 verbatim.
Three candidates, none ruled: **a state dot on the strip · dynamic card order · accept the loss.**
⛔ **The consolidation is the easy half; the thing the menu was FOR is the hard half.**

### G-b · the evidence is contested and must not be argued from until re-measured
`MOM-CYCLE-LOG:1115` says she navigates 100% by the jump strip · `:1816` says those events fired **only
from Paul's device** · `:1480/:1503/:1525` report **no post-`8718f46` reading**. Either different
windows or a live contradiction. ⛔ **W4 currently has NO Mom evidence at all.**
⚠️ **The re-measurement must enumerate every route that opens a card** — `card_expanded` once fired
from **1 of 4 writers** and the zero became a stated wrong finding. `measured`: **5** `card_expanded`
sites at HEAD.

### G-c · decided, and owed only its detail
*"It's better to not display something rather than display something that's empty"* `[paul-stated
2026-09-04, re-ruled 09-07]`, plus *an OFF module must look intentional — the grid re-flows or the tile
row declares itself.* What is owed is the **per-module empty list**, which falls out of the design
rather than preceding it.

### G-d · half-ruled
The 09-07 ruling settles the **strip** (it stays — it is the door) and the **cards** (they become the
glance). ⛔ **It says nothing about the tile row**, and `renderDashboardStrip()` is still a third layer
at HEAD. That is the actual consolidation decision and it is one sentence.

> ### ⛔ THE DESIGN CONSTRAINT THAT MUST SURVIVE THE CONSOLIDATION
> `validated` — **the jump strip is the ONE affordance measured 5 of 5.** Every ask-shaped affordance
> is **0 of 35**. The strip's whole virtue is that **it MOVES her and does not ASK her.** ⛔ Whatever
> the consolidation does, it must not turn the strip into something that asks — that is the single
> cheapest way to lose the one thing on this product that works.

### The row, DRAFTED not applied — bundled with §9.6 for Paul's go on canon

> `| **🧭 THE GLANCE CONSOLIDATION — jump strip · summary tiles · cards, three layers repeating one thing** `[paul-raised 2026-09-07]` | ⚙️ engine · declared. Shape ruled 09-07 (strip stays · summaries collapse into cards · re-analyse the closed state); ⛔ **G-a — where RANKING goes — is unruled and is the point of the feature**; G-b's telemetry is `contested` and must be re-measured enumerating every card-open route first. → `.plans/2026-09-07-backlog-grooming-SCAN.md` §11 · census B1–B4 · C7-R1/R2 | — |`

### 11.1 · ⭐ TWO SEATS RAN 2026-09-07 late — and both landed on the same answer to G-a

Trails: `.ux-reviews/2026-09-07-glance-consolidation.json` · `.user-research/2026-09-07-glance-measurement-procedure.md`.
⛔ Nothing executed. ⚠️ Both were re-briefed mid-flight with Paul's clean-slate engagement ruling
(§11.2) and both say in their own output what it changed.

**⛔ G-a IS ANSWERED, and by a fact neither seat had to argue for:** `orderCardsByRanking()`
(`engine/viewer.template.html:18186`) — *"⭐ THE RANKING DECIDES THE ORDER `[paul-stated 2026-09-06]`:
'we're building it based on this input that you provided us.' A person who put Gardening first found
it fifth."* `measured`. **Card order is ALREADY the household's own declared ranking.**

So frequency ranking does not fill an empty slot — **it overwrites a declared order with an inferred
one on the same axis, nine days later.** Both seats recommend against it, independently:
- **ux-expert:** recall dies (position is the only wayfinding on a 16-card page) · the ranking measures
  its own past output and locks in · the strip and the page diverge on day one, putting the one working
  affordance in disagreement with the page it points at · the face saying *"You put Gardening first"*
  starts contradicting where Gardening sits.
- **user-researcher:** ⭐ **construct mismatch** — *"how often accessed"* measures **habit**, a stable
  trait; W4 asks *"what matters TODAY"*, a state. A frequency ranking returns the same order every day,
  so it is **structurally incapable of answering the question the feature exists for.** Falsifier: if a
  household's most-accessed card is also its most-recently-changed on most active days, access is a
  serviceable proxy and the objection withdraws.

⭐ **Where the instinct should go instead** (ux-expert's order): frequency ranks the **synthesis line**
— a worklist by construction, which is where the ratified rule says a ranking belongs — **or** frequency
**proposes** a change to her declared order and she ratifies it, which makes *"everything is
changeable"* do real work rather than being asserted.

**⛔ AND THE PROPOSAL AS STATED WOULD REGRESS A SHIPPED FIX** — `measured` tonight:

| surface | reaches |
|---|---|
| **jump strip** (6) | Weather · Vehicles · Equipment · Household Systems · Gardening · Wildlife |
| **tile row** (7 sub-lines) | Weather · Plants · Wildlife · **Astronomy** · **Fishing** · **Journal** · **Property** |

**Four cards reach the top of the page ONLY through the tile row.** Deleting it restores exactly the
defect BACKLOG Tier-2 row 1 was shipped to fix on 2026-07-29 — *the Journal was the most-opened card in
the app (41 of 139 expansions) sitting 8th of 13 with no dashboard tile; she asked to look back and
still could not find it.* ⭐ **The fix is a TRANSFER, not a deletion** — and Paul has already made one
himself (09-07 beat 3: the Journal tile was removed for households *because* "Look back ›" existed).

⭐ **The tile row is four jobs wearing one component, and only ONE is duplicated:** ① the summary text
(genuinely duplicated — deleting it removes a second weather engine by construction, occurrence 4 of
*one engine, one verdict*) · ② above-the-fold access for four cards the strip does not reach · ③
**adjacency** — eight cells in one visual field become sixteen faces, no two of which are ever on
screen together at 414 × A+ · ④ the aerial image, the only visual of the place above the cards.
⚠️ **G-a's real loss is ADJACENCY, not ranking.**

**The two questions that gate the build:** ⓐ an **additive second strip row** (her six untouched and
first) — yes/no; ⭐ it satisfies Paul's own constraint, since a row of destinations **moves** and does
not **ask**. ⓑ does a **synthesis line** exist, and is it one phrase or two.

### 11.2 · ⭐⭐ THE CLEAN-SLATE ENGAGEMENT RULING `[paul-ruled 2026-09-07, late]`

> *"we've been building out all these acknowledgment strips and asking all these questions and just
> trying to prove out the mechanism and conceptualizing. So let's start fresh on our engagement rate
> data and understand that this is just a starting point — but try to take a clean slate view in terms
> of not over-indexing on Mom's past ignoring of our request for input."*

⛔ **RETIRED:** any inference of the form *she did not respond to asks → she will not.* That window was
**mechanism-proving on a prototype**, on a product now frozen. The new product's engagement record
starts at **n=0**.

✅ **SURVIVES — facts about the MECHANISM, not claims about her:** the queue renders one card at a time
and every offer carries `position: 0` (so the visible set is 1, not 5) · the strip figure is
`contested` and fired only from Paul's device · the card-open counter fires from a subset of the routes
that open cards.

⭐ **Not an oscillation.** Paul falsified the same inference himself earlier on 2026-09-07, producing
the standing rule *"an empty engagement record is not an absent demand."* This generalises that
correction from one finding to the whole record.

⚠️ **THREE THINGS THE RULING TOUCHED, each reported rather than silently rewritten:**
1. ⛔ **`renderEmptyCards()` (`engine/viewer.template.html:18403-18404`) has the retired count written
   into ENGINE CODE as the stated rationale for a shipped design decision.** The behaviour may still be
   right; **its justification is now inherited rather than checkable.**
2. The ux seat **withdrew ground 2 of its own F13** from this morning's pass, and deleted an
   engagement-based argument from F7 — which now stands on the governing principle and layout
   arithmetic alone.
3. A Fernwood candidate principle, *"demonstrated engagement sets altitude"*, rests entirely on the
   retired record. **Unratified and one occurrence, so nothing needs unwinding** — but the next review
   will pick it up and use it unless it carries a note.

### 11.3 · Corrections this pass made to its own earlier claims
- ⛔ **`card_expanded` has 2 emit sites, not 5** (`:8005` header · `:17781` programmatic). The other
  three greps are comments. **The "5 sites" figure was this file's and it was a grep count.**
- ⛔ **Nine routes open a card; two are instrumented.** Two of the silent ones are the **arrival
  screen** — they fire for every brand-new household.
- ⛔ **No event carries a position, an ordinal or the served order, and there is no `card_collapsed`
  event at all** — so *born-open* and *never-opened* are the same record, and the #1 card auto-opens
  silently. **Position 1 is over-exposed and under-counted at once**; the two biases do not cancel.
  ⭐ **This is RC-2 (§9) arriving on its first test case.**
