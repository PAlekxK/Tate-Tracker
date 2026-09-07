# Lap 3 — RESEARCH BRIEF: what Paul was trying to do, and the board he can tick

- row: process (lap-2 close → lap-3 intake; no BACKLOG row of its own)
- objective: O3 (the migration) · O5 (the loops are the artifact)
- kind: research
- seat: `user-researcher` (F4 of the consolidation design — reads what arrived, does not rank)
- ready: agent-proposed 2026-09-07 — Paul rules
- cites: `.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md` · `.plans/2026-09-07-lap2-CLOSE-HANDOVER.md` ·
  `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md` · `cycle/release/CYCLE-LOG.md:858-931` ·
  `BACKLOG.md` rows 19 · 19b · 19c · 20, § C7-R1…R5, § FOCUS FREEZE · `MOM-CYCLE-LOG.md:1110-1134` ·
  `.user-research/persona-mom.md` · `.user-research/2026-09-07-what-carries-what-she-redoes.md`
- gate: ⛔ **Nothing here is ranked, shortlisted, recommended or built.** §4 is a **CENSUS with an
  initial indication** — `[paul-stated 2026-09-07]`: *"the options list we should build more
  extensively once we are in lap three and have collected all the feedback and input and data that's
  out there. So this is more of just a census of everything that's going on and an initial indication
  rather than a final checklist for me to pick from."* ⛔ **There is nothing here to pick from yet.**
  The commitment point comes **after** lap 3's sweeps, not before.

---

## 0 · THE EVIDENCE BASE, AND ITS SHAPE

**Read this before reading any tag below.**

| source | n | tag it earns | why |
|---|---|---|---|
| Paul's production feedback records, `est-e6696a:feedback:2026-09-07` | 10 records, 4 substantive | **`validated`** — a real person, his own words, in the store, timestamped | ⚠️ **n = 1, and he is the builder.** Every "the product failed a user" claim below is a claim about *one* user who also wrote the code |
| Paul's walk tonight, `1e2748d` | F1–F6 | `validated` where a screen state was measured (F4, F5); `paul-stated` where it is a preference or a ruling | his walk is the only reading of production by a human tonight |
| Four synthetic seats | 34 runs today | ⛔ **`assumption`, always** | `strict` is a PO-box household and is **structurally immune to every placed-household defect**; `wide-eyed`'s whole reason for existing (frost · hardiness · growing season) is **unreached after 7 runs**. If a build ships on four seats and `strict` is one, **three tested it** |
| Mom | **zero** | ⛔ nothing | invite `p-b91e4d` minted, sent by text ~12:05 ET, **still unspent**. Every claim about her comes from the FROZEN instance (`est-3c9f1a`) and is a claim about a **different product** |

⭐ **The one structural note about the evidence itself.** The record class that carries Paul's
biggest ask — `homes-second-home`, "show roles on this page" — posts a **constant id**
(`homes/index.html:243`), and the Worker de-duplicates per UTC day and answers `200 {duplicate:true}`
while the screen shows the success ack. **So the surface that collects "who else can see this place"
can hold exactly one note per day and silently drops the second.** That is measured
(`…-PRACTICE.md` §A.1), and it means the *frequency* of an ask on that surface is not readable from
the store. It bears directly on §3.

---

## 1 · THE JOBS — what he was trying to do, and where the product stopped him

Nine. Each carries **who it is about** (§2) and **whether the record already knew** (§3).

### J1 · "Get me back into my own place, on a device I have used before."
`validated (measured live, 1e2748d, with Paul)` — **three independent records must agree before a
person can see their own place, and tonight all three disagreed.** He needed three repairs: a dead
grant (whoami 404) → a grant born blank (`mint()` carries identity only; the 8 place facts ride on at
sign-in and **there is no sign-in door**) → data that arrived and was then hidden by the owner guard.

**Where the product failed him:** all three failures render the **identical dead screen**, so nothing
he could see distinguished *you are not signed in* from *your data is here and we are hiding it*.
`inferred` — that indistinguishability is the actual defect; each individual bug is a symptom.

### J2 · "Show me that this place is mine, with my facts on it."
`validated (measured)` — whoami returned `name: "Grant Park Condo"` + address + ranked interests while
the screen read **"Empty so far."** and **"Signed in as PaulKirsch"** — a username belonging to no
account (`estate/index.html:343`, read without the guard). He was looking at a correct record being
suppressed under a wrong name.

**Failure:** the page has no "I cannot confirm who this is" state. It has only *your place* and
*empty*, and it chose empty while holding the answer.

### J3 · "Make this place actually placed — weather, sky, what grows here."
`inferred, untested` — coordinates absent on his account row. His account was created **11:16 ET on
`c821051`**; W0 geocoding reached production **17:15 ET on `1e2748d`** — the account predates the
capability by six hours. Predicts that re-saving the address populates it.

**Failure (the general one):** an account created before a capability exists is **never backfilled**,
and nothing tells the household it is missing something. `inferred`.

### J4 · "Tell me what matters today without making me scan the whole page."
`paul-stated 2026-09-07` — two menus have evolved; the summary menu is the informative one; it is
redundant with the jump strip. His resolution: keep the strip at the top, **collapse the summary
intelligence into the cards**, and re-analyse *what a CLOSED card displays*.

⚠️ **The open question his resolution does not answer, flagged not decided:** the summary menu did
**two** jobs — it SUMMARISED and it RANKED (*"the most relevant information"*). Distributing summaries
into every collapsed card preserves the first and **drops the second**: *what matters today* becomes
*scan the whole page*, which is the job he opened with.

⛔ **Do not quote the "she navigates 100% by the jump strip" figure in support of this.**
`MOM-CYCLE-LOG.md:1115` says it; `:1816` says `jumpstrip_viewed`/`_tapped` *"have fired only from
Paul's device"*; `:1480/:1503/:1525` say there is **no post-`8718f46` reading**. Those are either
different windows or a live contradiction. **`contested` until re-measured.**

### J5 · "Show me who else can see this place, and let two households invite each other."
`validated (his words, in the store, 11:17 ET)` — *"We want to show roles on this page — I am the
owner for Grant Park and you can see Home members. Down the road I will want to invite mom to have
access to my condo and she will invite me to the house that she sets up."*

**Two distinct jobs inside one sentence, and they have different owners:**
- **now:** *see the roles that already exist on this page* — a display job.
- **later:** *cross-invitation between two real households* — an authority-and-mechanics job (C9).

### J6 · "Tell the product what kind of place this is, and have that change what it offers me."
`validated (his words)` — *"It's a condo property type. I'm right by the beltline and Grant Park
itself!"* and, from the place card, *"This card should be more focused on the property and things you
can glean from it: local events, festivals, etc. — especially since it's a condo in the city."*

**Failure:** *condo* had to be typed into a free-text note because **there is no property-type
input**, and the one card that should reflect it renders Pickens-County events at a Midtown address
(C7-R5). He is asking for the **input → value** contract he separately asked for at 11:30 ET.

### J7 · "Let me name a need you never anticipated, and see it land somewhere."
`validated` — `onboard-interests-other`: **"Houseplants!"** — a twelfth item, the class no synthetic
seat can produce. `read-onboarding.py`'s own docstring calls that free-text line *"the only line where
someone can name a need we never anticipated."*

**Failure:** nothing routes it. There is no path from *other* to a module, a card, or a row.
⭐ `inferred` — and it is not a random word: `~/.claude/user-research/houseplants.md` exists, so the
domain he named at setup is one he already keeps research on elsewhere. Worth a look before it is
treated as a passing enthusiasm.

### J8 · "Move a concept forward this lap without shipping it."
`paul-stated 2026-09-07` — zones get a dedicated session, concept → **design + user journey**,
⛔ explicitly **not released this lap**; and *"that's also how I wanna start designing our pipelines."*

**The blocker is a charter fact, not an opinion.** Dependency sequence is already agent-drivable.
**Value rank — which concepts enter which stage — is Paul's alone** by his own charters. A pipeline
needs both. ⚠️ And a stage ladder with **no WIP limit is not a pipeline, it is N queues**: the measured
disposal rate today was **1 of 12 artifacts approved**, with 22 files carrying `ready: agent-proposed`.

### J9 · "Leave a note and know it landed."
`validated (measured)` — the "Add a home" surface returns a success ack on a record the store threw
away (§0). This is *capture must not lie*, inverted, on the repo's own rule.

---

## 2 · INSTANCE OR ENGINE — for each job

The standing rule: over-indexing on one person's instance leaks into the engine
(`feedback_mom_is_a_test_subject_not_the_end_user`). Paul is a **city-condo owner in Atlanta**;
Fernwood is **2.6 rural acres**; Mom is a **third case who has not arrived**.

| job | THE PRODUCT (engine) | PAUL'S PARTICULAR HOUSEHOLD | how to tell them apart |
|---|---|---|---|
| **J1** identity/grant | ⭐ **entirely engine.** Nothing about it is about a condo | — | the seam is `mint()` vs sign-in; no place fact appears in it |
| **J2** disowned data | ⭐ **entirely engine.** Every multi-device household hits it | — | ⭐⭐ **and it is the one that will bite Mom first** — her invite opened on a device that ever held another grant renders zero rows **under someone else's name** |
| **J3** unplaced account | **engine** — "a capability shipped after an account exists never backfills" | **instance** — *his* account predates geocoding by six hours; Mom's will not | the general form is a backfill policy; the specific form is one row in KV |
| **J4** strip vs summary | **engine** — the glance/repository layering is the product's governing principle | ⚠️ **the evidence is instance-shaped**: the strip-first reading is Mom-at-Fernwood telemetry, contested, one device | his *preference* is engine input; her *behaviour* cannot carry the argument until re-measured |
| **J5** roles + invitation | ⭐ **entirely engine** — and it is the first requirement stated by **two** real households (Bob's succession, Mom's condo) | — | row 19's own note: *"this is not a Bob feature"* |
| **J6** property type | **engine** — a declared type driving the module set is the C5/C7 contract | ⭐ **instance** — Beltline · Grant Park · festivals · *"a condo in the city"* is Grant Park's content, not the engine's | the ASK generalizes; the CONTENT does not. C8 is where the content goes, gated |
| **J7** "Houseplants!" | **engine** — a route from *other* to somewhere is engine machinery | **instance** — whether *houseplants* becomes a module is a content call for his condo, and one voice | ⚠️ Mom's own `q-top-categories` answer (2026-08-03, `validated`) confirmed a **five**-item list as complete. Paul's twelfth item is **not** a correction of hers |
| **J8** pipeline | **neither — process** | — | it governs how items move, not what the product is |
| **J9** capture lie | **entirely engine** | — | one constant id, one Worker branch |

⭐ **The single sentence worth carrying out of this section:** *of nine jobs, six are engine, one is
process, and only two carry any Grant Park content at all — and both of those are content, not
mechanism.* Tonight's walk was unusually clean of instance leak. The place it can still leak is J6,
where "local events and festivals" is one urban household's answer to a question the engine has not
asked yet.

---

## 3 · WHAT THE BACKLOG ALREADY KNEW — and what has now been asked twice

| job | existing row(s) | duplicate of an earlier ask? | asked more than once? |
|---|---|---|---|
| **J1** | ⚠️ **row 20** covers the *journey* (login → select → arrive, "designed, recommended, and never built"); `.plans/2026-09-07-sign-in-door-PROPOSAL.md` exists, unruled. **No row covers the grant/facts split itself** | the *missing door* is old (row 20, `[paul-stated 2026-09-06]`); the **three-way disagreement is new tonight** | **YES — the journey.** 09-06 *"we need a very coherent view of it"* → 09-07 F6 *"address this in the next lap more cohesively."* Same word, two days apart |
| **J2** | ⛔ **no row.** It is a **regression introduced by lap 2's own door-card work** (`1e2748d`), found tonight | no | first time |
| **J3** | ⛔ no row. `read-geocodes.py` exists (built today) and reports it | no | first time |
| **J4** | ⭐ **C7-R1**, open since `[paul-stated 2026-09-04 ~5:40 AM]` — *"figure out the jump strip versus the summary menu"* | ⭐ **YES — exact duplicate of the question.** Tonight is not a new ask, it is **the answer to C7-R1**, 3 days later | **YES — asked 09-04, resolved 09-07.** ⭐ C7-R1 can be struck, and the *ranking* question opened in its place |
| **J5** | rows **19** (a person cannot found a second place) · **19b** (Paul ruled the shape: places list, `+`, quiet control back) · **19c** (settings on both surfaces) · **C9** (invite flow, authority ruled 09-03, mechanics not) | ⭐ **YES, three times over.** 09-03 C9 · 09-04 L-49 view-only role · 09-06 rows 19/19b/19c | ⭐⭐ **YES — TWICE TODAY.** `11:17 ET` in the production store, verbatim, *and again on tonight's walk* (relayed in the lap-3 brief; ⚠️ **it is NOT in `…-lap3-paul-feedback-CAPTURE.md`** — the evening restatement was not written down, which is itself a capture gap). ⚠️ And §0 means the store **could not have recorded a second same-day note on that surface anyway** |
| **J6** | **C7-R3** (manual-vs-automated population view) · **C7-R5** (events are Fernwood's and sit at the bottom) · **C7-R2** (an OFF module must look intentional) · `.plans/2026-09-07-input-to-value-matrix-PROPOSAL.md` (agent-proposed, unruled) | ⭐ **YES.** C7-R3 and C7-R5 are `[paul-stated 2026-09-04]`, from his first condo read | ⭐ **YES — 09-04 and 09-07**, both times about the same card, both times from the same condo |
| **J7** | ⛔ no row. C8 is the condo build-out and is **gated + not groomed** | no | first time |
| **J8** | ⛔ no row. `.plans/2026-09-07-lap-boundary-PROCESS.md` has cadences and a commitment point but **no stage ladder** | the *sequencing* ask is 09-07; R7 (a `product-steward` trial) is the nearest prior | **YES in substance** — *"I want the product manager help in terms of how to sequence it"* restates the R7 question he left open at 12:45 ET |
| **J9** | ⛔ no row (measured today by practice-steward, → engineering-partner) | no | first time |

⭐ **The repetition finding, stated plainly.** **Three threads have now been raised on two or more
separate days by the same person: roles-and-invitation (J5, four times, twice today), the coherent
login→arrive journey (J1, twice), and what populates each card (J6, twice).** Under this project's own
doctrine that is signal — and the honest reading is not *"he keeps asking"* but **"a row exists for
each of them and none has moved,"** because each is blocked on something that is not a build:
J5 on `scopeFor` having zero callers, J1 on a review of six artifacts nobody has read together, J6 on
a proposal that is `agent-proposed` and unruled.

---

## 4 · THE CENSUS — everything currently in play, and what is still to be collected

⛔ **This is not a decision surface.** No tick boxes, no ranking, no shortlist, no recommended set.
`[paul-stated 2026-09-07]` — the options list gets built **in lap 3, after the sweeps**. This is the
board as it stands tonight, with an honest note per row about what is not yet known.

**Read the third column first.** Lap 3 will run deterministic sweeps it has never run before —
`health-probe`, `watch-accounts`, a production feedback sweep across every account, `read-geocodes` —
and **Mom has still never arrived on the new product**. Several rows below will look different once
that data is in, and a few may dissolve entirely. A row whose evidence is incomplete says so.

**Stage** — kept, because it feeds the ladder Paul is designing (F3):
**DEFINED** = the change itself is known · **CONCEPT** = needs design and/or journey work first, and
may legitimately advance a stage in a lap and produce **no deploy**.

**Initial indication** — the strength of the evidence *is* the indication. No other ranking is implied:
⭐⭐ asked more than once, unprompted, on separate days · ⭐ measured live on production ·
`·` one user, one session · ⛔ nobody has looked at it yet.
**Evidence key:** `V` validated · `I` inferred · `A` assumption · `n=1` = one user, who is the builder.

### A · The identity seam (J1 · J2 · J3 · F6 — Paul asked that these be treated as ONE thing)

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **A1** | Walk + certify `4a3a61b` (the two knowingly-shipped defects: `isFinite(Number(null))`; the owner guard reaching 4 of 7 person-scoped reads) | ⭐ `V` — measured, fixed, on `main`, **unwalked**; the gate is per-sha | a certifying round. ⚠️ 3 of 4 seats can actually test it — `strict` cannot | CLOSE-HANDOVER §1 | **DEFINED** |
| **A2** | The reconcile never re-stamps `fw-onboard-owner`, so correct server data is fetched, stored, then suppressed | ⭐ `V` `n=1` — measured live tonight; falsifier written (F4) | ⛔ **whether it fires for anyone but Paul.** The device-with-a-prior-grant case has never been walked by a seat or a second person | none — **new** | **DEFINED** |
| **A3** | No *"we cannot confirm who this is"* state — the card renders zero rows under another person's name | ⭐ `V` on the condition (*"Signed in as PaulKirsch"*, an account that does not exist) | ⛔ what a real person does when it happens. This is the **Mom-first-open** risk and only her arrival answers it | none — new | **DEFINED** |
| **A4** | A **sign-in door** — the one path that reconciles credential ↔ facts has no door | `V` — the 8 place facts ride on at sign-in (`worker.js:595`); there is no sign-in | the row-20 review (C6) should run first — six artifacts have never been read together | row 20 · `sign-in-door-PROPOSAL` | **CONCEPT** |
| **A5** | Treat the seam as **one architecture item**, not six tickets | ⭐⭐ `paul-stated` — 09-06 *"a coherent view"* → 09-07 *"more cohesively"*. **Same ask, two days** | nothing external; it needs a design session, not more data | row 20 (journey half) | **CONCEPT** |
| **A6** | Coordinates absent → the household stays S0 (no weather, no sky, nothing that grows) | `·` `I`, **untested** — his account predates production geocoding by six hours | ⭐ **one cheap test** (re-save the address) — and `read-geocodes.py`'s first real sweep will say whether it is one row or a class | none — new | **DEFINED** (test first) |

### B · The glance (J4 — he ruled the shape tonight; two things stayed open)

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **B1** | Keep the jump strip; collapse the summary intelligence into the cards; re-analyse the **closed-card** state | ⭐⭐ `paul-stated` — a **ruling**, and it answers C7-R1 (open since 09-04) | what a collapsed card should actually say per module — undesigned | **C7-R1** | **CONCEPT → DESIGN** |
| **B2** | Where **RANKING** goes now the summary menu is gone — strip state dot · dynamic card order · accept the loss | `I` — the menu did two jobs and his resolution keeps one. **Unruled** | ⛔ nobody has watched anyone use either arrangement | new, under C7-R1 | **CONCEPT** |
| **B3** | The closed-card **empty case** — nothing dynamic to say → no summary line, possibly no card | `V` as doctrine (*"better to not display something than display something empty"*, 09-04 + the 09-07 lap-1 ruling) | the per-module empty list, which falls out of B1 | C7 § RULE | **DEFINED** |
| **B4** | Re-measure the jump-strip telemetry before anything is argued from it | ⛔ `contested` — `MOM-CYCLE-LOG:1115` vs `:1816` / `:1480` are either different windows or a live contradiction | ⭐ **a re-measurement, and it must enumerate every route that opens a card** (`card_expanded` once fired from 1 of 4 writers and the zero became a stated wrong finding) | MOM-CYCLE-LOG | **DEFINED** |

### C · Places, roles, invitations (J5)

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **C1** | Show **roles** on the places list — who owns this place, who its members are | ⭐⭐ `V` `n=1` — his words in the store at 11:17 ET **and restated tonight**. ⚠️ that surface can hold one note per UTC day (§0), so the store cannot show how often it has been asked | ⛔ whether a second real household reads "owner / member" the same way. Bob's case is stated, not observed | 19b · 19c · C9 | **CONCEPT → DESIGN** |
| **C2** | Cross-household invitation — he invites Mom to Grant Park, she invites him to her house | `V` as a stated *"down the road"* want; `I` on urgency | ⛔ both halves depend on households that do not exist yet (Mom's condo, Bob's two houses) | **C9** — authority ruled 09-03, mechanics not | **CONCEPT** |
| **C3** | Per-request scope — `scopeFor()` has **0 callers**; `scopeOf(env)` has **51 call sites**, ~30 carrying household data | `V` — measured 09-06. Everything above it is blocked on it | nothing external; it is engineering, and row 19 asks for **journey first, then build** | **row 19 ①** | **DEFINED** (large) |
| **C4** | Found a second place — `+` on the places list, quiet control back to it | ⭐ `V` — the **shape is already ruled** (19b), so this starts from a design, not a blank page | ⭐ **GAP 2** — whether a person reads `+` as *founding* or as *switching*. No seat can answer it | **19 ② · 19b** | **CONCEPT → DESIGN** |
| **C5** | Settings on both surfaces — **and the colour-precedence collision** (account `fw-accent`, live and rendering, vs estate `identity.theme.main`, ruled and unread) | `V` that both exist and neither knows about the other | ⛔ **Paul's ruling on which wins.** *Do not build two colour pickers before answering it* | **19c** | **CONCEPT** |
| **C6** | The row-20 review — read the six login→arrive artifacts together and say which recommendations survive | `V` — inventory taken 09-06; `R1-SA` predicted invalidated by founding | nothing external — it is a reading, and it gates A4/C4 | **row 20** | **DEFINED** (a review) |

### D · What fills a card (J6 · J7)

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **D1** | **Property type as a declared input**, driving the module set — he had to type "condo" into a free-text note | `·` `V` `n=1` — his own onboarding record | ⛔ the type vocabulary itself. One condo and one rural acreage do not make a taxonomy | C5/C7 module set | **CONCEPT** |
| **D2** | The **input-to-value matrix** — what setup asks · what each answer unlocks (automatic · research · build-out) · what each card needs before it stops being empty | ⭐⭐ `paul-stated 11:30 ET`; a filled proposal exists and is **unruled** | the BUILD-OUT column is unpriced until the coordinates question (§3 Q1) is ruled — the proposal says so itself | **C7-R3** · `input-to-value-matrix-PROPOSAL` | **CONCEPT** |
| **D3** | Events / neighbourhood as a domain; gate them per estate; move fresh dated content up | ⭐⭐ `V` on the defect (Pickens-County events at a Midtown address), `paul-stated` 09-04 **and** 09-07 | ⛔ blocked on **C7 Q4** — a new ingestion class and a third path through the AI boundary, which needs a ruling first | **C7-R5** | **CONCEPT** |
| **D4** | Route an unanticipated interest somewhere — *"Houseplants!"* currently lands nowhere | `·` `V` that he wrote it; `I` that it is a real domain (`~/.claude/user-research/houseplants.md` exists) | ⛔ **one voice.** Mom's `q-top-categories` (`validated`, 08-03) confirmed a **five**-item list complete. The next sweep's `read-onboarding` "what's missing" lines are the cheapest way to see whether anyone else names a twelfth thing | none — new | **CONCEPT** |
| **D5** | An OFF module must look intentional — the grid re-flows or the tile row declares itself | `paul-stated 09-04`, **not restated tonight** | whether it still bites after B1 changes the card layer | **C7-R2** | **DEFINED** |

### E · So lap 3 can hear anyone at all (the successor beat — this is what produces the data the rest of the census is waiting on)

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **E1** | `.private/fernwood-token-home` + `tools/feedback-sweep.py` — production feedback has **no deterministic reader** | ⭐ `V` — today's read was a person with `wrangler`; `read-onboarding --env home` is UNREADABLE by construction | ⛔ **this is the precondition for the census being complete.** Until it runs, "what's out there" is one person's memory | `…-PRACTICE.md` §C.3 | **DEFINED** |
| **E2** | The constant-id capture lie on "Add a home" — a second note the same UTC day is dropped behind a success ack | ⭐ `V` — `homes/index.html:243` + `worker.js:3082-3085` | a positive control: post the same control twice, assert two records | none — → engineering-partner | **DEFINED** |
| **E3** | Nothing watches `est-e6696a` — the estate Mom's unspent invite points at | ⭐ `V` — every mom-cycle reader hits the legacy worker | ⛔ **a RULING first: does the FOCUS FREEZE bind the new estate?** The sweep must not settle it by existing | `…-PRACTICE.md` F-b | **DEFINED after the ruling** |
| **E4** | The six-key labelling contract, as a **counted coverage line, never a grade** | `V` — 2 of 3 record classes carry no `context.surface` | its own falsifier: at 100% for two laps, delete it | §C.5 | **DEFINED** |
| **E5** | Dispose of the **11 walk runs never read** today (3 have no report file); their builds are superseded so the gate will never ask again | `V` — measured. R2 of the 09-06 ruling, a lap-2 pre-registration still open | a lap-close sweep that lists unread runs and disposes each (read · superseded-and-kept · discard) | `…-PRACTICE.md` F-a | **DEFINED** |

### F · Process (J8), and the record of the loop itself

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **F1** | The **stage ladder** (concept · design · journey · build · QA · released) with a **WIP limit per stage** | ⭐⭐ `paul-stated`. ⚠️ `V` that disposal is the binding constraint — **1 of 12** artifacts approved today, 22 files `ready: agent-proposed` | the honest WIP number for a solo operator. 1–2 per stage is a guess, not a measurement | none — new | **CONCEPT** |
| **F2** | Who may **value-rank** — a bounded seat, or agents lay out the board and Paul picks | `V` — a **charter fact**: no seat in the stack may rank | ⛔ Paul's ruling (R7). The `product-steward` trial is **INCONCLUSIVE at 1 round** and needs rounds 2–3 or it ends by drift | R7 · `product-steward` CHARTER | **CONCEPT — his ruling** |
| **F3** | `last_lap` cannot record that a lap closed — `outcome` reverted to `open` after he cleared it, and `lap` never increments | `V` — measured at close-out; **R6 and R7 both hang on a boundary nothing marks** | the state contract is Paul's: append-only closed-lap list, or rename `outcome` + keep a `laps_closed` count | CYCLE-LOG `did-not` | **DEFINED once the shape is picked** |
| **F4** | The **zones dedicated session** — concept → design + journey, ⛔ no production deploy | ⭐⭐ `paul-stated`; scope **not given** (which zone thread is open) | an 812-line `2026-09-06-maps-and-zones-PROPOSAL.md` **has not been read by any current window**. Read before scoping | zone hold stands (un-parks on a signal from Mom) | **CONCEPT** |
| **F5** | Two lap-1 pre-registrations still `disposition: open` — `instrumented-counted`, `second-viewport` | `V` — the two-sided rule says a retro must **discharge** them | their readings | CYCLE-LOG:826-846 | **DEFINED** |

### G · Known-broken and user-visible — wrong on **Paul's own dashboard** today

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **G1** | Four arithmetic/unit defects, all estate-independent: `sun-horizon.json` wrong by 60 min at 18 `:00` entries · every *"in N days"* is +1 (**`Math.round(-0.5)===0` makes yesterday render "Tonight"**) · visibility fetched in feet, labelled km (so the haze penalty can never fire) · "REGION · 7 DAYS" ends the day before yesterday | ⭐ `V` — all four verified directly at lap-2 close; **nothing checks the sun table** | nothing. These are the census's most decided rows | CLOSE-HANDOVER §3 | **DEFINED** (one session) |
| **G2** | `onboarding`'s *"we work out your weather and what grows there"* — the second half is delivered to **nobody** | `V` — frost · hardiness · growing season **unreached in 7 runs**; `paul-ruled: hold to next lap` | his own reframe (journey claim, not delivery claim) needs **a release condition**, or *"we'll explore together"* becomes permission never to deliver | CLOSE-HANDOVER §3 | **CONCEPT** |
| **G3** | Client-side gates (station · burn · terrain · sky) are **uninstrumented** — measured at zero while the same Worker carried 23 telemetry writers | `V`; `paul-stated` that instrumentation is a standing requirement | where instrumentation sits in the process — retro material, unsettled | CLOSE-HANDOVER §6 | **DEFINED** |
| **G4** | The door card's second-device timing hole; **its comment overstates 3 ways and understates 2** | `V` — found by the strict seat | fix the comment with the code, or the next reader inherits the wrong model | CLOSE-HANDOVER §3 | **DEFINED** |
| **G5** | The Wundermap link hands a third party the household's coordinates to **11 decimal places with no disclosure**, on a screen where the Google link has one | `V` | ⛔ Paul's call — *an embed is a silent disclosure; a link is a disclosed one*, and security is a stated selling point | CLOSE-HANDOVER §3 | **DEFINED** |
| **G6** | The `🛰️ NWS dark-window cloud` row flaps **per-load, not per-build**; no stall timeout, no user-facing failure line, only a `console.warn` | `V` — absent/absent/present/absent across four runs, `viewer.html` unchanged | whether it is upstream or ours. Its absence currently leaves zero trace | CLOSE-HANDOVER §3 | **DEFINED** |
| **G7** | `<title>Fernwood</title>` at the QA origin root — `check-estate-neutral --url` is 🔴 | `V`; **QA-only** (production rewrites it to "My Home") | nothing | CLOSE-HANDOVER §3 | **DEFINED** |

### H · Open, and nobody has spoken about it recently — included because the census is a census

⚠️ Every row here is real open work that no current thread would surface. Several are **frozen on
purpose** and are listed to be visible, not to be scheduled.

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **H1** | `FN_STORAGE_KEY` TDZ — **every vehicle card silently drops its field notes**, 18 throws per page load, swallowed by a `catch` | `V` — read off the live console 08-15; pre-existing, verified at the merge base | nothing. It has sat open since August | BACKLOG Tier-1 **row 10** | **DEFINED** |
| **H2** | 25 sound recordings (17 birds, 8 frogs) are **unaudited** — the pipeline cannot verify a recording *is* the species it is filed under | `V` — proven live: a juvenile Australian magpie was filed as the Morning Cicada and the tool reported success | ~25 min of filename-vs-binomial reading, no network | Tier-1 **row 11** | **DEFINED** |
| **H3** | `/api/zone-audio`'s `reviewed` field has **no writer** — reads `false` forever, in the dangerous direction | `V` — measured; a record Paul listened to still returns `false` | Paul picks: have the disposition write it (needs a Worker PATCH), or delete the field | **row 14** | **DEFINED once picked** |
| **H4** | *"Behind N"* on this repo is almost always a bot, and nothing says so — a routine event and a real anomaly print the same line | `V` — 90 days: `weather-recorder[bot]` 345 commits, `fernwood-deployer[bot]` 9, both perfectly in-lane | a machine-writer registry (author → allowed paths) | **row 15** | **DEFINED** |
| **H5** | The Worker deploy workflow's `paths:` **omits four digest sources** — editing a weed never redeploys Guru | `V` — verified 09-03 | four lines in the workflow; verify with a `workflow_dispatch` | **row 17** | **DEFINED** |
| **H6** | Six wildlife domains (amphibian · bird · fish · lizard · mammal · snake) have **no marker path**, so they can never produce a card however good the harvester gets | `V` — `check-domains.py` prints it every run | ⚠️ the risk when they land is **SUPPLY, not schema** — 8 cards already on the bench against a 5-slot cap | M1, CLAUDE.md | **CONCEPT** |
| **H7** | `group` is **double-booked in running code** — the action axis (`tend/fight/visit/run/place`) and the kind axis (`vehicle/equipment/household-system`) | `V` — `VOCABULARY.md` says so on its own face | a migration decision; `module` will need to name sets across both, which is exactly that seam | VOCABULARY | **CONCEPT** |
| **H8** | `JOURNAL_NAME` resolves to `<household> + " Almanac"`, commented *"(mom seat, round 3)"* — **a synthetic seat's preference standing where her validated answer ("Journal", folded 07-29) is not** | ⭐ `V` both halves | nothing — one grep settles it. It should be a decision, not a leftover | `what-carries-what-she-redoes` §5 | **DEFINED** |
| **H9** | The Open-Meteo proxy — `[paul-approved, queued]`; every walk round today was DEGRADED on the same two `archive-api` URLs | `V` — approved, not built. The walk procedure **cannot produce four countable runs back-to-back** without it | nothing; it is the Ambient-key argument again, one client instead of N | CLOSE-HANDOVER §4 | **DEFINED** |
| **H10** | `viewer.html` is ~17,900 lines / >1 MB and has **silently hit two ceilings**; the 1 MB cliff broke Guru's write-to-canon path for two weeks | `V` | nothing new — it grows every session and nothing watches the number | CLAUDE.md § Architecture | **CONCEPT** |
| **H11** | ⛔ **FROZEN ON PURPOSE, listed for visibility:** the mom-cycle's proactive legs (bench-card approvals, new asks, season notes, decision cards fernwood-1·4·5·6·8·9·11·12), Track B fleet lap 3 (FIRED on SEASON + INBOX, **deliberately unrun**), C8 the condo build-out, A3/Phase G observations-as-knowledge-layer, W6 the plant instance model | `V` — all carry their status and their gate | ⛔ **nothing. The freeze lifts on Paul's word and only that** | § FOCUS FREEZE | — |
| **H12** | ⛔ **Mom's catch-up debt, listed for visibility:** 81 arrivals · 17 individually dispositioned · **63 batch-cleared by watermark and never individually attested** · 1–2 open; and the Z-ACK debt (16 zone names with no arrival record at all) | `V` (metadata census, 09-06) | ⛔ five rulings owed (R1–R5 in `what-carries-what-she-redoes`) — and **no count of her outstanding items may render anywhere**, including zero | `what-carries…` §1 | **CONCEPT** |

### I · Instruments that will mislead lap 3's own sweeps if nobody fixes them first

⭐ **These are not features. They are the reason a census taken next week might read cleaner than the
world.** Every one was measured today.

| # | What it is | KNOWN today | STILL TO BE COLLECTED | Row | Stage |
|---|---|---|---|---|---|
| **I1** | `_view.json`'s `text` array is **deduplicated** — every *"appears N times"* / *"it disappeared"* / count-delta claim from that record is unsound, and it is structurally blind to a duplicated card | `V` — `journey-view.py:123`. A seat nearly filed a false finding on it | either de-dup deliberately at read time or stop making count claims from it | CLOSE-HANDOVER §4 | **DEFINED** |
| **I2** | **A stalled fetch is counted nowhere** — `pageErrors: []` and `failedActions: []` on a run where the main card never loaded | `V` — that is how a defect ran three rounds unseen | nothing distinguishes *"the weather rendered"* from *"the weather never arrived"* | CLOSE-HANDOVER §4 | **DEFINED** |
| **I3** | `check-estate-neutral` **tests for names**; the gauge leak was numbers and possessive pronouns and it read ✅ 311 needles / rendered=0 against the very origin four seats walked. Its bare form does not scan `viewer.html` at all | `V` | a payload-shaped check, or an explicit statement that it is evidence about names only | CLAUDE.md | **CONCEPT** |
| **I4** | `build-viewer.py --check` is **GREEN on a build with a JS syntax error** (it compares bytes); `--extract` destroys the template while `--check` stays green | `V`; ✅ `pages-deploy` catches the first, so nothing broken reaches an origin | the `--extract` round-trip divergence is **unruled** | CLAUDE.md | **DEFINED** |
| **I5** | The walker's password is **in clear** — 2× `transcript.json`, 4× `_view.json`, printed twice by `walk-brief.py`; redaction covers one file of three | `V` | — | CLOSE-HANDOVER §4 | **DEFINED** |
| **I6** | `transcript.personId` is a **harness field**, constant across a seat's runs — not a product behaviour. A seat retracted a finding over it | `V` | — | CLOSE-HANDOVER §4 | **DEFINED** |
| **I7** | ⛔ **The seat roster itself.** `strict` is a PO-box household, structurally immune to every placed-household defect; `wide-eyed`'s whole purpose is unreached after 7 runs; *"Please don't"* has never been tapped by any seat, ever | ⭐ `V` — each says so in its own run | ⭐ **whether the roster should change** is a design question nobody has opened. Today "4 of 4 seats pass" can mean three tested it | CLOSE-HANDOVER §5 | **CONCEPT** |

### J · Rulings owed by Paul — no build behind them, and several rows above wait on these

| # | The ruling | Who is blocked | Why it cannot be settled by an agent |
|---|---|---|---|
| **J-a** | Does the **FOCUS FREEZE** bind Mom's arrivals on `est-e6696a`? | E3, and every Mom row | it was written for the frozen estate; a sweep must not settle it by existing |
| **J-b** | **Who may value-rank** (R7 / the product-steward trial) | F1, F2, and the whole staged pipeline | a charter fact — no seat in the stack may rank |
| **J-c** | The **`last_lap` state contract** | F3, R6, R7 | two legal shapes, both correct; the choice is a contract |
| **J-d** | **Colour precedence** — account accent vs estate theme | C5 | two ruled concepts, neither aware of the other |
| **J-e** | **C7 Q4** — the AI boundary for a new ingestion class (events, neighbourhood) | D3 | a boundary ruling, and this boundary is his |
| **J-f** | The five catch-up rulings **R1–R5** (prepopulate scope · the answer-key measurement · visit-vs-link · the Z-ACK form · a relayed-capture path) | H12, GAP 1, GAP 2 | R2 in particular is **irreversible the first time anything is shown or pre-filled** |
| **J-g** | Which **zone thread** F4's dedicated session is about | F4 | scope was not given, and the 812-line proposal is unread |

---

## 5 · THE GAPS — what no amount of synthetic walking can tell you

Four seats walked 34 runs today and **neither of these is inside their reach.** `strict` cannot see a
placed household at all; `wide-eyed` has never reached the thing it exists to test; and *"Please
don't"* — the contact-refusal branch, the only route to a forgotten password — **has never been tapped
by any seat, ever**, because the harness cannot reach the radios.

### ⭐ GAP 1 — Does a real person who is not the builder get through the door at all?

**Why synthetic cannot answer it.** Every seat is minted by a harness that hands it a working grant.
**No seat has ever arrived at a device that already held someone else's grant** — which is exactly the
condition J2 says produces *"a permanently empty place with someone else's name printed on it."*
Mom's invite is out, unspent, and the most likely device it opens on is one that has held Paul's.
The seats cannot see this class; Paul's own walk found it only because he had three failures in a row.

**What it would establish:** whether the product's first impression on its make-or-break user is
*"there it is"* or *"this is someone else's."*

**Cheapest honest version — ~20 minutes, and it is already ruled to happen:** the transition is a
**guided visit in person** (`BACKLOG` ruling 3, 09-06). Do the F4 falsifier as part of it, on **her**
phone, before anything else: open the invite, and read four things — does the screen ever print a name
that is not hers · `text_size_served` (must be `lg`; her key does not cross the origin and she has
**never** fired the toggle in 37 opportunities) · `door_reached / door_opened / door_failed` · whether
any count of outstanding items renders anywhere. ⛔ **Paul's ruling is owed first** — the FOCUS FREEZE
was written for the frozen estate and whether it binds `est-e6696a` is his word, not a sweep's.

### ⭐ GAP 2 — Is "add a place" understood as **founding** or as **switching**?

**Why synthetic cannot answer it.** Rows 19/19b design a places list with a `+`. The prior
recommendation (`R1-SA`, *the masthead IS the control*) was made for **switching between two** and row
19b already predicts it does not survive **founding a third**. A seat will tap whatever affordance is
rendered; it cannot tell you whether a person understands that tapping `+` **creates a new household
that will then ask them twenty questions**. That is a mental-model question and only a person has one.

**What it would establish:** whether the places list reads as *my things* (safe to explore) or as
*an administrative console* — the register `VOCABULARY.md` §4 explicitly rejects.

**Cheapest honest version — one question, ~5 minutes, no UI shown.** At the guided visit, **before**
opening anything, ask a past-behaviour question in her own frame: *"if you wanted to look at Paul's
condo and then come back to your own place, how would you expect to do that?"* Then listen for the
noun she uses. ⭐ The reason this is high-value at n=1: **naming is the act she demonstrably
initiates** — 16 zone names at a kitchen table in one evening, against **0 taps in 35 in-app offers**.
Her word for the list is the single most reliable datum this product has ever been able to collect
from her, and it costs one question.

*(A third gap exists and is smaller: whether "Houseplants!" is a module ask or an enthusiasm. It is
answerable by asking Paul one question, not by research.)*

---

## 6 · WHAT I DECLINED

- **To rank anything, or to build a decision surface.** §4 is a census, grouped and not ordered; no
  row is recommended over another, and there is deliberately nothing to tick. `[paul-stated
  2026-09-07]` — the options list is built **in lap 3, after the sweeps**. Presenting one now would
  pull scope commitment earlier than his own process intends.
- **To present incomplete evidence as ready.** Every census row carries a *still to be collected*
  cell; where the honest answer is *nobody has looked*, it says ⛔ rather than a confidence.
- **To promote synthetic input.** The four seats are `assumption` throughout; no seat reading is used
  as evidence for a user need anywhere in this brief.
- **To claim anything about Mom at the new product.** She has not arrived. Every Mom claim here is
  cited to the frozen instance and labelled as such.
- **To invent a quote.** Every quoted string is from the production store, `CYCLE-LOG.md`, the capture
  file, or a `questions.json` prompt, and is cited.
- **To treat Paul's n=1 as a user base.** It is stated at the top of §0 and repeated in §4's key.
- **To design the fixes.** A2/A3/B3 name a falsifier; they do not name an implementation.

## Evidence log

- `2026-09-07: [validated] — est-e6696a:feedback:2026-09-07, 10 records / 4 substantive, read from KV, quoted in CYCLE-LOG.md:865-877 — condo property type + Beltline/Grant Park; "Houseplants!"; roles on the places page + future cross-invitation; the place card should carry local events and festivals.`
- `2026-09-07: [validated] — measured live on production 1e2748d with Paul (capture F4) — three independent records disagreed; whoami returned name+address+ranked while the card read "Empty so far." and "Signed in as PaulKirsch", a username belonging to no account.`
- `2026-09-07: [inferred, untested] — capture F5 — coordinates absent on the account row; account created 11:16 ET, W0 geocoding reached production 17:15 ET.`
- `2026-09-07: [paul-stated] — capture F2 — keep the jump strip, collapse the summary intelligence into the cards, re-analyse the closed-card state. Settles C7-R1, open since 2026-09-04.`
- `2026-09-07: [paul-stated] — capture F3 — a staged pipeline; zones advance concept→design+journey with no production deploy this lap; "I want the product manager help in terms of how to sequence it."`
- `2026-09-07: [contested] — MOM-CYCLE-LOG.md:1115 says she navigates 100% by the jump strip; :1816 says jumpstrip events fired only from Paul's device; :1480/:1503/:1525 report no post-8718f46 reading. Do not quote the figure until re-measured.`
- `2026-09-07: [validated] — .plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md §A.1 — homes/index.html:243 posts a constant id; worker.js:3082 de-duplicates per UTC day and returns 200 {duplicate:true}; the page shows the success ack.`
- `2026-09-07: [validated] — CLOSE-HANDOVER §5 — strict is a PO-box household and structurally immune to every placed-household defect; wide-eyed reached frost/hardiness/growing-season 0 times in 7 runs; the contact-refusal branch has never been tapped by any seat.`
- `2026-08-03: [validated] — Mom's own tap, questions.json:122 — q-top-categories answered "That's all of them" on a five-item module list. Her confirmed list is not corrected by Paul's twelfth interest.`
- `2026-09-07: [validated] — Mom's invite p-b91e4d minted and sent by text ~12:05 ET (CYCLE-LOG.md:858-863) and UNSPENT as of this brief. Nothing about her behaviour on the new product exists.`
- `2026-09-07: [assumption] — every synthetic seat reading referenced in this brief, per standing doctrine. None is used as evidence for a user need.`
- `Open, unrecorded: the evening restatement of the roles-and-invite ask is relayed in the lap-3 briefing and does NOT appear in .plans/2026-09-07-lap3-paul-feedback-CAPTURE.md. The capture file is F1–F6 only. Worth one line in the capture so the repetition is readable from the record rather than from a briefing.`
