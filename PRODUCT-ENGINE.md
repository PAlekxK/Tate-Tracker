# PRODUCT ENGINE — Fernwood as the first instance

**Stood up 2026-09-01** by extracting `BACKLOG.md`'s C0 section, which had grown to **429 lines —
23% of a 1,829-line file**. `BACKLOG.md` is *Fernwood's decision record*; this is about a **product
engine that explicitly transcends Fernwood**. Different grain, so a different file — the same move
this repo already made for `MOM-CYCLE-MAP.md` and `cycle/fleet/CYCLE-MAP.md`.

> ⛔ **STILL CAPTURE-ONLY. Nothing is scoped, nothing is decided, no build has started.**
> `paul-stated 2026-09-01`: *"that's a whole nother big work stream that will need to involve a lot
> of research probably in all the experts weighing in, but I wanna capture that for a backlog for
> later."*

---

## ▶️ THE SEQUENCE — read this before anything below it

The findings below are evidence, not a plan. **This is the plan.** The dependencies are real: do
not start at step 3.

| # | Do | Gated on | State |
|---|---|---|---|
| **1** | ~~Fleet laps 1-2~~ | — | ✅ **BOTH CLOSED 2026-09-01.** ⚠️ This row read *"OPEN at beats 4 + 6"* until 2026-09-02 — **beat 6 RAN** (Paul ruled; 5 Bolores items closed) and lap 2 closed after it. Beat 4 is **carried to lap 3 on Paul's instruction**, held by a signal (STALE-OPEN fires ~2026-10-29), not by a promise. 🟠 **The loop is FIRED again today** — SEASON + INBOX |
| **2** | ~~Review the two conversation mines~~ | — | ✅ **BOTH LANDED 2026-09-01**, reviewed. 6 material findings · **217 images staged** · 4 new door entries. See below |
| **3** | ~~`user-researcher` interview~~ | step 2 | ✅ **RAN 2026-09-02** as seat 1 of a 5-seat panel → `.user-research/2026-09-02-estate-manager-scoping.md` |
| **4** | Agile PM artifacts | step 3 | 🟡 **partly delivered** by seat 1 (persona set + JTBD). ⛔ Its JTBD verdict is that the owner surface has **no evidenced job** — read it before commissioning more |
| **5** | Architecture options, priced | step 4 | ✅ **RAN 2026-09-02** → `.engineering/…` + `.ai-advisor/…`. Options only; nothing decided |

### ✅ PAUL RULED, 2026-09-02 — three answers, and one of them OVERRIDES WRITTEN DOCTRINE

**① The tenancy unit is ONE DATABASE PER PROPERTY, with an owner→property GRANT LIST.**
`[paul-ratified 2026-09-02, chosen from three modelled options]`. Fernwood is one database; each of
Bob's houses is its own. **A property never knows who owns it** — access is a grant row, so a fourth
house is one new database plus one row. This is what `engineering-partner` recommended independently.

**② ⚠️ MOM WILL LOG IN AND SELECT A PROPERTY. This REVERSES the no-login rule, deliberately.**
`[paul-stated 2026-09-02]`, asked directly, with the existing doctrine put in front of him:

> *"I think yes, we have Mom login and pick a house — and again the login is part of just an overall
> hardening of the text and PII that we've talked about, that also probably has some backlog
> mentions. And Mom has a condo as well, so we can go ahead and say that will be a future requirement
> for her and is also part of our backlog roadmap. So definitely that journey of logging in and then
> selecting a property will eventually have to work for both."*

⚠️ **CORRECTED 2026-09-02 — THIS WAS NOT A REVERSAL, AND CALLING IT ONE WAS THIS SESSION'S ERROR.**
It was first recorded here (and reported to Paul) as *"reverses the no-login rule, deliberately."*
Then `~/.claude/agent-foundations/_about-paul.md:58` was read, and it has said since **2026-05-11**:

> *"**Low-friction authentication is the constraint, not password-free.** A simple,
> easy-to-remember password is acceptable — Paul confirmed 2026-05-11 that nothing on the dashboard is
> confidential. The original 'no password / Mom stops' hypothesis was **Paul's prior framing,
> contradicted on 2026-05-11**."*

⭐ **So Paul did not overturn a standing rule — he RESTORED a position he had already taken in May,
which a September document had drifted away from.** The *"no login, deliberately"* framing entered
in **this file, on 2026-09-01**, four months after the shared base recorded that framing as already
contradicted. Two sources disagreed and the newer, narrower one was treated as doctrine.

✅ **What IS genuinely new today, and it is the part that matters:** *"nothing on the dashboard is
confidential"* **stops being true** under R7 — receipts, contractor contacts and another household's
data go behind it. So the *reason* for auth changes from identity-and-convenience to **there is now
something to protect**, and that is a real change even though the login itself is not.

⚠️ **But note the word "EVENTUALLY," and do not spend it early.** This is a **roadmap requirement,
not a near-term change**. Nothing about her door changes today, and the old rule's *reasoning* still
governs how the new door gets built: her documented fear is getting things wrong, and the glance she
demonstrably opens is the weather card. **What must never sit behind the login is a live design
question, not a settled one.**

⭐ **AND THE CONDO IS THE BIGGER FACT.** Mom is now a **multi-property user** — not merely a
contributor at Fernwood. That makes her the **third** multi-property user and **the only one with real
behavioural evidence**. It directly contradicts `user-researcher`'s *"the tenancy model is visible to
owners and invisible to contributors"* and *"the contributor journey must not change at all."* That
seat has been sent the new facts and asked to revise in place rather than let the finding stand.

**③ THE ONE BOX MUST COVER THE WHOLE ESTATE — stated as a REQUIREMENT** `[paul-stated 2026-09-02]`:

> *"We've talked about how to expand the chat box's coverage to be able to cover basically all the
> information that would be part of one estate. That is an end goal still — where you go in and talk
> to the Garden Guru, it should be able to reference everything in that estate's database. I know
> there are several challenges and design decisions that need to be made to do that, but that is a
> requirement."*

⭐ **This makes `ai-advisor`'s RUNG 3 (deterministic lookup tools) MANDATORY, not optional — and it
retires the "bigger window" answer.** The 61 `serviceHistory` rows and the 30-breaker directory are
**dropped before the context window is reached**, so no model with a larger window can reach them. A
digest that ships everything cannot scale to *everything*; the requirement is only satisfiable by
retrieval, not by inflation. ✅ It also confirms scope: **one estate at a time**, which is why the
cross-property ceiling finding was never a constraint on his design (see the correction below).

⛔ **Open, and it is the crux:** does *"everything in that estate's database"* include the **private
tier** — the 254 receipts, contractor contacts, breaker directory — once authenticated? That is
exactly what ②'s PII hardening would unlock, and it is being put to Paul.

---

### 🗳 PANEL RAN 2026-09-02 — three seats converged. **AT PAUL'S GATE; nothing is ruled.**

Seats: `user-researcher` · `engineering-partner` · `ai-advisor`. Brief:
`.plans/2026-09-02-estate-manager-scoping-brief.md`. `ux-expert` and `content-steward` **held** —
copy is surface-coupled and shape depends on where the personalization boundary lands.

⭐⭐ **UNANIMOUS, from three independent lenses: do not build an estate-manager loop or owner
surface yet.** Not *later, when convenient* — **the evidence for it does not exist.**

| seat | why not |
|---|---|
| `user-researcher` | The one owner job unservable per-property (*"tell me which of my places needs me"*) is **unevidenced for both known users.** Paul has one property and his per-property loops serve him; Bob has never been asked |
| `ai-advisor` | **All three candidate triggers fail** — divergence is N=1 (a check that cannot be *seen to fail*, against S3); a new instance fires once (an event, not a cycle); machinery propagation is **already `claude-meta-stack`'s**, so building it = a second meta-stack scoped to 2 of 14 loops |
| `engineering-partner` | The **record scoping** is real and has a deadline; the **surface** does not. Separate them |

**What all three say to do instead:** scope the record now (owner → property → contributor as a
**naming and config contract** — not a database, not a URL scheme), classify what is engine vs
config vs instance, and **write the promotion gate** that says when estate-manager earns loop
status. `ai-advisor`'s proposed gate: instance 2 deployed **and** an `engine` artifact *observed* to
diverge once.

⛔ **The name should not be used.** `user-researcher`: *"manager"* is the task-board vocabulary
Fernwood's own tone rule forbids, and a product-sounding name on an internal loop gets shipped by
accident. `ai-advisor`: it is doing **three** jobs — tenancy model · Paul's build-management seat ·
cross-instance conformance — and the middle one is **a missing SEAT, not a missing loop** (route to
`/team-audit`).

⚠️ **The main session's skill-vs-cycle partition was attacked by BOTH technical seats and does not
survive as stated.** The *axis* holds (a skill is how work is done; a cycle is what makes it happen
unasked). The *cut* was wrong: `fleet_probe.py` is **~85% mechanism**, and leaving the **probe**
per-instance is how two probes drift into two definitions of *"a lap is owed."* Engineering: three
layers (detector · declaration-as-data · human disposition). ai-advisor: four (procedure · probe ·
config · state). ⛔ Both also say **do not extract the fleet skill yet** — one lap, still open at two
of Paul's gates, against the standing *three runs before a Skill* rule.

**Parked on Paul, correctly:**
- **Mom-cycle lap 7 is OPEN at leg 6** — the ack ribbon is held until he does more zone work.
  `MOM-CYCLE-LOG.md` § Lap 7. A later run must not read `R1 ack staleness 🔴` as neglect.
- ~~**Is "Bob's house" the Tate Commons ask, or a second one?**~~ ✅ **ANSWERED 2026-09-02** —
  a personal household record, **more than one place under one profile**. See the resolved
  block below. **Scoping is unblocked.**

**Independent, take when there is room:**
- ⚠️ **UX sweep — OWED AGAIN as of 2026-09-02** (24 viewer commits since the 08-31 run, limit 20). The line below is the 09-01 reading and is kept for its lesson, but **read the live checker, not this bullet.** ~~**NOT OWED. The checker was wrong** (fixed 2026-09-01).~~ A full
  two-pass production sweep ran **2026-08-31**, 17 of 18 punch items shipped; `check-ux-sweep.py`
  matched the FILENAME and the trail is named `production-full-sweep.md`, so its own clock went
  blind to it and reported 29 days. Now reads **rested · last 2026-08-31 (1d)**.
- ✅ **Contractor normalization — PROPOSED 2026-09-01**, `.plans/2026-09-01-contractor-register-proposal.md`.
  ⭐ The register **already exists** (`serviceContacts[]`, with judgment in Paul's own prose) — on
  **1 vehicle out of 22**. Three moves + four questions for him. Nothing applied.
- ✅ **D4 pre-glance stack ledger — RAN 2026-09-01**, `.plans/2026-09-01-preglance-stack-ledger.md`. Stack is **1,958px at A+ / 1,790 at A**; **Mama's Perspective is 68% of it**, the served question card alone 36%. Measurement only, nothing changed. 🔴 **Paul rules on the trim.**

⚠️ **Step 1 is deliberately first and is NOT part of this workstream.** It is ready, it is fired,
and it is the natural destination for both mines' candidate entries. Do it while the research runs.

---

## 🗂 WHERE THE 2026-09-01 SESSION'S OUTPUT LIVES

One session produced a lot across two repos. This is the index; each row is the durable home.

| Thread | Lives in |
|---|---|
| **The product engine** (this file) | `PRODUCT-ENGINE.md` ← you are here |
| Contractors · breakers · shut-off valves | `BACKLOG.md` § 🧑‍🔧 CONTRACTORS & TRUSTED PEOPLE |
| Track A/B tested; Track B has no ask loop | `BACKLOG.md` § B0 |
| `--bench`/`--apply` reverse each other | `BACKLOG.md` § A3 (fix proposed, **not applied**) |
| Mom-cycle lap 7 — open, held at leg 6 | `MOM-CYCLE-LOG.md` § Lap 7 |
| Claude-corpus vehicle mine (59-day window) | `.plans/2026-09-01-vehicle-conversation-mine.md` |
| ChatGPT-archive fleet mine + images | `.plans/2026-09-01-fleet-chatgpt-archive-mine.md` · manifest in `.plans/` · images in `.private/chatgpt-fleet-images/` |
| Contractor register proposal | `.plans/2026-09-01-contractor-register-proposal.md` |
| Fleet lap 1 (open at Paul's gates) | `cycle/fleet/CYCLE-LOG.md` § Lap 1 · `BACKLOG.md` Track B § FLEET LAP 1 |
| `corpus_search --sessions` ignores its query | `~/Developer/operating-layer/BACKLOG.md` |

⚠️ **A lot of this session's reasoning lives only in COMMIT MESSAGES** (2026-09-01, `7071162`
onward). If a claim here looks unsupported, `git log` before assuming it was invented.

---

## 🧭 THE EXPANSION MODEL `[paul-stated 2026-09-02, after stepping away]` — CAPTURE ONLY

> *"Our expansion model — I want this in addition to our dev/QA/production environments, but really
> use **Fernwood as a test bed for everything**. We've really proved the internal basic mechanics and
> core components. So what we'll want to do is the data migration — modularize everything that makes
> the Fernwood renderer, in a way that it can accept data to personalize everything. We'll figure out
> the right balance, but ideally we have pretty **standard engines that produce everything based on
> data specific to Fernwood versus Bob's house**. Then I'd want to expand Fernwood to just be **Mom's
> profile**, and give her a login and the ability to select Fernwood from there. That would be a great
> first step. Then from there we could add **her condo in Atlanta** — and that condo is going to be a
> very different look. **There's no garden**, right? More of an urban side, local events. The weather
> is still relevant. We have to think through how else we make something much more **low maintenance,
> still engaging**, and highlight the uniqueness of that property and **the community around it**."*

### The sequence, as he stated it

| # | Step | Note |
|---|---|---|
| 1 | **Modularize the renderer** — standard engines, per-property data | The migration in `.plans/2026-09-02-data-model-design.md` |
| 2 | **Fernwood becomes Mom's profile** — she logs in and selects Fernwood from it | *"a great first step"* |
| 3 | **Add her Atlanta condo** as the second property | Urban, gardenless, community-facing |

⭐ **THIS SETTLES AN OPEN QUESTION: instance 2 is HER CONDO, not Bob's house.** The data-model doc
listed it undecided; `user-researcher` had independently reached the same candidate on different
grounds (the only test case whose occupant's calibration is *already measured*, the most different
domain mix, and the only one that tests the owner/contributor role flip). Two paths, one answer.

### ⚠️ Four things this collides with — surfaced, none decided

1. ⛔ **`user-researcher` recommended MODELLING the condo, NOT SHIPPING it to her** — *"her attention
   is the scarcest resource, she is demonstrably still in the learning period, and Fernwood's own
   adoption question was re-opened 2026-08-01 and never re-closed."* Paul's model ships her **a login
   AND a second property**. Both are coherent; they are not the same plan. **His call, and it should
   be made knowingly rather than by sequence.**
2. **"Mom's profile" collides with the naming verdict.** `content-steward` held, with more confidence
   than anything else it filed, that the multi-property shell should be called **nothing** — *"naming
   it creates it"*, and every instance already has a name. A profile she logs into and selects from is
   a surface that needs to be *something she opens*. Unresolved.
3. ⚠️ **HER NAME MUST NOT ENTER THIS PUBLIC REPO.** She is "Mom" in every tracked file. Naming the
   profile for her would put it in the UI and in public git. **A deliberate decision, not a copy
   detail.**

   > ⛔ **AND THIS PARAGRAPH'S OWN VERIFICATION WAS FALSIFIED 40 MINUTES LATER, BY THIS SESSION, IN
   > THIS FILE.** It read *"the name Paul used appears **nowhere** (verified 2026-09-02)."* That was
   > true when written. The same session then wrote her first name into **§ PERSONALIZATION, 100 lines
   > below**, while explicitly holding the position that it should not be written — and committed it
   > (`701af7a`). Caught by the `user-researcher` seat, not by the author.
   >
   > **Scope, measured:** one occurrence, one commit, **never pushed** — `origin/main` was still at the
   > previous day's HEAD. Removed from the working tree 2026-09-02.
   > ✅ **RULED 2026-09-02 `[paul-stated]`: *"It doesn't need to appear, but we don't need to do a huge
   > scrub if it showed up at one point."*** So: **no history rewrite.** The name stays in `701af7a`
   > and will reach GitHub whenever this branch is pushed — accepted knowingly, having been told that
   > pushing publishes it. **This question no longer holds the push.**
   >
   > ⭐ **The forward rule, which is the operative half: her name does not appear in tracked files.**
   > Not in `viewer.html`, not in a card, not in a profile label, not in a commit message. If a
   > surface ever needs to name her, that is a decision to make deliberately — not a copy detail, and
   > not something that arrives by an agent using a name it was told in conversation.
   >
   > ⭐ **The lesson is the one this repo keeps paying for:** *a verification is true at an instant,
   > not for a day.* A claim of the form "X appears nowhere" is a **measurement with a timestamp**, and
   > this file treated it as a standing property — which is why the same document could assert the
   > absence and contain the thing.
4. ⭐⭐ **"No garden" is the sharpest engine-vs-instance test that exists**, and it should be treated
   as the migration's real falsifier rather than a content note. Plants are **41% of the Guru digest**;
   the care calendar, `seasonNotes`, bloom windows, the honesty markers and the entire
   harvest → confirm-card → fold → ribbon pipeline all hang off a growing thing. **At the condo they
   have nothing to attach to.** If the "standard engine" cannot render a property with no plants
   without a fork, the modularization is not done — and that is knowable *before* shipping her
   anything.

### 🏙 THE CONDO'S CONTENT — Paul's idea capture `[paul-stated 2026-09-02]`

> *"She's right by a big park — so what are the free events in the park, what's the schedule of
> events there? What new restaurants are opening in the area? What's the latest positive local news?
> What's the weather?"*

**Location, at the only specificity this public file may carry:** a **Midtown Atlanta condo adjacent
to a large park.** ⛔ The street address and unit number are in `.private/condo-location.md`,
gitignored, with the handling rule. Do not restate them anywhere tracked.

⭐⭐ **THE STRATEGIC PROBLEM HIDING IN THAT LIST, and it is worth more than the features.** Every item
is **external, live, and public** — events, restaurants, news. **Fernwood's entire model is the
opposite:** internal, accumulated, and about things on the property, where the moat is precisely that
*only this property's record exists.* Anyone can build a park events feed. **Nobody can build
Fernwood's record.**

**So a condo built as a local-info feed inherits none of the thing that makes Fernwood work.** The
resolution that keeps the project's own principle intact is to make **her relationship to the place**
the record: what she has been to, what she liked, what she wants to go back to, what she noticed on a
walk. That is the same invite → fold → acknowledge loop, pointed at an **urban** ground truth instead
of a garden — and it is the one thing about Midtown that is hers and not Google's.

⚠️ **Three constraints it collides with, none of them small:**

1. **A NEW INGESTION CLASS.** Fernwood has never pulled live external editorial content. Weather is
   the closest and it is measured instrument data. **Events, openings and news are none of those.**
2. ⛔ **"Positive local news" is an EDITORIAL SELECTION, which is judgment** — and the AI boundary is
   silent on it, because Fernwood has never had a surface where a model chooses *what she sees*
   rather than drafting something Paul approves. **That is a third path through the boundary and it
   needs a ruling before it is built**, not after.
3. **The offline premise inverts.** Fernwood is built around no cell service and Wi-Fi from the house.
   Midtown assumes connectivity — and *"the community around it"* implies live external data by
   definition. **The offline-first constraints are Fernwood's, not the engine's**, and this is the
   second road to that same finding.

### 🆕 And a domain family that does not exist yet

*"Local events… the community around it."* `momlib.DOMAINS` declares five action groups — `tend` ·
`fight` · `visit` · `run` · `place` — every one of them about a *thing on the property*. **A
neighbourhood, its events and its people are none of these.** The condo is not a subset of Fernwood's
model with the plants removed; it needs at least one domain family Fernwood has never had, and that
family is **outward-facing** where every existing one is inward-facing.

⚠️ Note the tension with the site premise: Fernwood's design is built around *no cell service, Wi-Fi
from the house only.* An urban condo inverts that completely — connectivity is assumed, and
"community around it" implies live external data. **The offline-first constraints are FERNWOOD's, not
the engine's**, and the manifest currently cannot tell those apart.

### Then Bob — the transfer test `[paul-stated 2026-09-02]`

> *"That would set us up decently to stand up **Bob's basic structure**: having a login, a menu to
> select his property, then opening up the property — which we could start **seeding with data and
> watching how it all grows**. That would be a good test bed of **how the tools we built to build
> Fernwood transfer** to another place."*

⭐ **Note what is being tested, because it is not the app.** *"The tools we built to build Fernwood"* —
the harvest, the fold, the re-inline pipeline, the checks, the loops. The transfer question is about
the **authoring machinery**, not the rendered surface. That is a different (and harder) claim than
"the renderer is data-driven."

### 🎨 PERSONALIZATION — the dimensions and their costs `[paul-raised 2026-09-02, OPEN]`

> *"There is going to be a need for some layer of personalization… some design principles like color,
> certainly maybe font size. So let's think about what's the degree of personalization we can offer
> along which dimensions, and what the cost of all that is."*

**Five dimensions, and they do not cost remotely the same.** Measured 2026-09-02, agent-proposed, for
Paul's ruling:

| # | Dimension | Cost | Read |
|---|---|---|---|
| 1 | **Data** — which plants, vehicles, zones, systems | **~free** | This IS the migration. The whole point |
| 2 | **Identity** — property name, subtitle, photo | **cheap, but AUTHORED** | `content-steward`: an authored string per estate, never a recipe. A content act, not an engineering one |
| 3 | **Which domains exist** — the condo has no plants but has a neighbourhood | **moderate** | Forced by *"no garden"* regardless. `momlib.DOMAINS` already declares domains; making the SET per-property is the work |
| 4 | **Accessibility** — text size, contrast | ⚠️ **near-zero if modelled right; harmful if modelled wrong** | ⛔ **NOT a personalization dimension.** It is **C-person** — it belongs to the PERSON and travels with them |
| 5 | **Visual system** — colour, typography, spacing | ⛔ **the most expensive, and it buys the least** | See below |

⛔ **THE COLOUR TRAP, stated plainly because it was the first example raised.** Fernwood's colours are
not decoration — **they are semantics.** `CARE_COLORS` plus **29 distinct `.c-/.b-/.br-/.t-` utility
classes** encode *which care action this is* (prune · propagate · fertilize · water · repot ·
inspect). A per-tenant palette does not restyle the app; it **breaks the meaning**, and it breaks it
for the reader who most depends on consistent signals. The 2026-08-31 sweep's own finding is the
warning: Fernwood carried **"110 buttons, 31 visual signatures and 10 radii"** and cleaning that up was
real work. **Per-tenant theming multiplies exactly that surface by N** — and `/ux-sweep`'s informed
pass would then have N palettes to adjudicate against a shared principle library.

⭐ **And font size is a CATEGORY ERROR as a branding axis.** It is already per-person and
device-stored (`tateTracker.textSize`, reported as `text_size_served`). **Mom's** measured
**414 × A+** must follow *her* to the condo — filing it as per-property styling would reset her
accessibility every time she switches places. **That is the C-person / C-edge split from the data
model, arriving on a second road.**

**The honest summary:** *personalization along DATA and IDENTITY is nearly free and is the entire
proposition; personalization along the VISUAL SYSTEM is the most expensive thing on the list and buys
the least, because the visual system is where the quality lives and where consistency is load-bearing
for a reader with difficulty.* ⚠️ **Agent-proposed, not ruled** — and if Paul wants visual identity per
estate anyway, the cheap version is a **single accent token plus the property photo**, leaving the
semantic palette untouched.

### ⭐⭐ THE BETTER FRAME — a DIVERGENCE CONTRACT, not a personalization budget `[paul-stated 2026-09-02]`

> *"Another way to think about it is: can we define what's okay if it deviates between the different
> profiles? Like different font rules — if the different owners have different preferences, that's
> okay, it's not gonna hamstring us to have the font be different. But there probably are some things
> that we don't wanna change between the two unless we absolutely have to."*

⭐ **This reframes the question and it is better than the cost framing above.** *How much
personalization can we offer* is a budget question with no natural answer. *What is safe to diverge*
is a **contract**, it is declarative, and **it can be checked.**

⭐⭐ **AND PAUL ALREADY HAS THIS CONTRACT, ONE LEVEL UP.** `~/.claude/rituals/CYCLE-SPINE.md` is
exactly this shape for **loops**: a minimal MANDATORY spine (S1–S6), everything else
**optional-with-a-declared-reason**, and a dropped element (S5) that was cut precisely because *"a
standard nobody adopted is not a standard everybody violates."* **The estate question is the same
contract applied one level down** — reuse, not a new framework.

**Its design rule is the test being reached for here, and it is already measured:**

> *"Spine membership should track **'something breaks visibly'**, not 'it would be tidy'… the keys
> that drifted are exactly the ones with **no consumer that degrades** when they are missing."*

**So the test for every dimension is one question: IS THERE A CONSUMER THAT DEGRADES WHEN THIS
DIFFERS BETWEEN ESTATES?** Not *is it nice to share* — *what visibly breaks.*

| tier | test | examples (agent-proposed) |
|---|---|---|
| **FREE to diverge** | nothing degrades | text size (per-PERSON anyway) · property name, subtitle, photo · which domains exist · all record data · an accent token |
| **DIVERGE WITH A DECLARED REASON** | something degrades, but the estate may have a real cause | domain *set* (the condo has no plants — a declared absence, not a fork) · the offline-first constraints (**Fernwood's premise, not the engine's**) · trigger thresholds · whether a contributor loop exists at all |
| ⛔ **MUST NOT DIVERGE** | a consumer degrades visibly, and the estate has no standing to overrule it | the **semantic colour system** (`CARE_COLORS` + 29 utility classes encode MEANING) · capture stays deterministic and **AI-free** · the **AI boundary** · the fold + **watermark clamp** (divergence here is silent data loss) · the affirmative grammar (one learnable signal, `[paul-stated 2026-07-29]`) · check/probe contracts |

⚠️ **The middle tier is the load-bearing one**, exactly as it is in the spine: *declared* absence is
not drift. The condo having no plants is a **declaration**, and it should read as one — while the same
absence undeclared would be a broken migration. **That distinction is the whole mechanism**, and it is
what a checker could enforce.

⭐ **Falsifier for this frame:** if a dimension lands in MUST-NOT-DIVERGE and nobody can name the
consumer that degrades, it belongs in FREE and the contract is being used to enforce tidiness — which
is the failure the spine already named and dropped an element over.

⚠️ **Agent-proposed. The tiers above are a first cut, and the ASSIGNMENTS are Paul's** — the frame is
his, the placement of any given row is not yet ruled.

### 🔌 THE MODULE SET IS A DECLARATION, AND NOTHING CAN EXPRESS IT TODAY `[paul-stated 2026-09-02]`

> *"One thing that's gonna be important to keep track of is **which modules we're turning on or off
> for different properties** — the condo has no garden, but Fernwood does. If we have users that do or
> don't have vehicles or tools, there will sometimes be a **different mix and match of the components**
> within different estates."*

⭐⭐ **THIS IS WHAT MAKES THE MIDDLE TIER ENFORCEABLE**, and it is the same shape as ~70 of this
portfolio's failure classes:

> **A module that is OFF and a module that is ON BUT EMPTY produce the same observation — and they
> mean opposite things.**

An empty `vehicles.json` at Fernwood is a **gap** (someone should add vehicles; the harvester should
keep asking). No vehicles at a condo is a **declaration** (asking would be nonsense). **Today nothing
can tell them apart.** Verified 2026-09-02: `momlib.Domain` carries **seven** fields — `key · file ·
const · group · time · markers · cardable` — and **not one of them says whether an estate is using
this domain.**

**Five consumers that degrade, which is exactly the spine's membership test being met:**

| consumer | what goes wrong |
|---|---|
| `harvest-questions.py` | drafts confirm cards from honesty markers. At an off module it would draft **nonsense for that estate**; at an on-but-empty one it should arguably ask. It cannot tell |
| `check-domains.py` | already prints 🔴 for six wildlife domains with no marker path. At a gardenless condo that red is **permanent and correct**, which is the **N8 · COSTLY CONTROL** signature Paul has already ruled against — *a control whose alarm never clears is one nobody reads* |
| the Guru digest | ships the whole property record every turn, already **~127K tokens / 62–70% of the window**. A gardenless estate would carry plant scaffolding it can never use, and invite the model to discuss things that do not exist |
| `renderDashboardStrip()` | four tiles including Plants. At the condo that is not an *empty* card — **it should not render at all** |
| ⭐ **the engagement signals** | `offers-passed`, `sessions-quiet` and the funnel all key on what she was offered and did not take. **Counting "she did not tap the plant card" at a property with no plants would be a false signal ABOUT HER** — the exact class the 08-15 empty-answer-record finding exists to prevent, arriving at a second property |

⛔ **That last row is why this is not a tidiness question.** A wrong denominator here produces a wrong
claim about a person, on the surface this whole project is built to protect.

### ⚠️ Open, and it is Paul's: what is the UNIT that turns on and off?

He said **"modules"** and **"components."** The repo says **domains**. They are not obviously the same
granularity — **"the garden" is not a domain**, it is `plant` + `weed` + `turf` + `zone` and the care
calendar that binds them. Whereas *vehicles* maps cleanly to one domain, and *tools* is today a
**group inside `vehicles.json`**, not a domain at all.

**So the on/off unit is either a domain, or a named bundle of domains, and that choice changes the
declaration's shape.** ⚠️ Do not settle it by picking whichever is convenient when the code is
written — a bundle chosen implicitly is how a second vocabulary starts.

### 🧭 JOURNEYS, AND A MODULE THAT MIGHT NOT BELONG TO A PLACE `[paul-raised 2026-09-02]`

> *"What are the customer journeys we have to think through and test and model? The login, for
> example — and can we test these? And future enhancements: once you log in and see your two estates,
> is there also potential for a **finance tab** or something there? Is there potential to **promote
> vehicles out of the estates and have it top level**, so you've got a condo and then vehicles —
> that ability to switch things around?"*

⭐⭐ **THE PRECISE FORMULATION, using the ratified vocabulary: he is asking whether a `module` can be
scoped to a PERSON instead of to an ESTATE.** Today every module is estate-scoped by construction.
The axis he has found is: **does this module belong to a PLACE, or to a PERSON?**

| module | scoped to | why |
|---|---|---|
| plants · zones · weather · household systems | **place** | they cannot be anywhere else |
| **vehicles** | ⚠️ **arguable** | a machine moves, and its owner does not change when it does |
| **finance** | **person** | not about a place at all |

⛔ **AND THIS CONTRADICTS A RULING FROM EARLIER THE SAME DAY, WHICH IS THE POINT OF SAYING SO.**
`.plans/2026-09-02-data-model-design.md:153` records **"A MACHINE BELONGS TO THE ESTATE"**
`[paul-ratified 2026-09-02]`, chosen from three options — the rejected one was *"to a person, sited at
an estate."* **He is now feeling the pull of the option he did not pick**, and that is a legitimate
reason to revisit: the ruling was made on simplicity and accepted two consequences (his Bronco is
nominally Fernwood's; Bob's contributor sees Bob's equipment record).

⚠️ **Revisiting is fine. Revisiting WITHOUT NOTICING is not** — the standing rule from Mom's surfaces
applies to the schema too: *a change must be intentional, journey-aware, and data-supported where data
exists.* **Recorded here so the reversal, if it comes, is a decision rather than a drift.**

### ⭐ THE DISCRIMINATOR IS SITING, NOT OWNERSHIP `[paul-stated 2026-09-02]`

> *"This is not something we would just change on the fly, and different people have different
> preferences. But thinking about it — if I have Fernwood and then the condo, and then **a car I use
> to drive between the two** versus **a dirt bike that stays at Fernwood** — you can see there may be
> different ways to represent that, where the car that's your main source of transportation is not
> associated to an estate, but a dirt bike is, because it stays there."*

⭐⭐ **This resolves the tension without reversing anything.** The question was never *who owns the
machine* — it is **does the machine LIVE somewhere.** A dirt bike is sited; a car is mobile. Ownership
is the same in both cases.

**So the estate association becomes OPTIONAL AND DECLARED, not removed:**

| | |
|---|---|
| `home: <estateId>` | **sited** — seasonal signals apply, it surfaces under that estate |
| `home: null` | **mobile** — it belongs to the person and surfaces at the person level |

✅ **"A machine belongs to the estate" `[paul-ratified 2026-09-02]` STAYS TRUE for sited machines.**
This refines the ruling rather than overturning it, and it lands exactly in the divergence contract's
middle tier: **a declared absence is not drift.**

### ⛔ AND THE RECORD ALREADY HALF-KNOWS THIS — by accident, in the most fragile way available

**Measured 2026-09-02: not one vehicle carries a `location`, `home`, `stored` or `site` field. Zero.**
Yet `fleet_probe.py`'s SEASON signal correctly fires on **`dr200s-2017` and `drz400s-2001`** — the two
dirt bikes — and not on the road cars.

**How does it know? Because someone wrote *"Fall put-away"* on them as a maintenance item**
(`fleet_probe.py:82`). ⚠️ **The discriminator between "lives at Fernwood" and "moves between places"
is currently whether a human happened to write a task line.** Delete that line and the dirt bike
becomes, as far as every tool can tell, a car — and the fall put-away signal goes quiet with nothing
reporting that it did.

⭐ **Same shape as the module on/off question, one level down:** a machine with **no home** and a
machine **whose home was never recorded** produce the same observation. Only a *declared* `home: null`
tells them apart.

### 🔀 And the split that keeps preference out of the schema

Paul: *"different people have different preferences."* ⭐ **Those are two different things and they
should not share a field:**

- **SITING IS A FACT** — the dirt bike is at Fernwood, and that is true regardless of who is looking.
  **Data. `instance`-class.**
- **SURFACING IS A PREFERENCE** — whether a mobile machine appears at the top level or nested under an
  estate. **`config`-class, per person.**

**So "different people have different preferences" does not have to contaminate the schema at all**,
which is what would otherwise make this feel unresolvable.

### ⚠️ Two collisions on the "finance tab"

1. **A finance surface already exists in the portfolio — twice.** `~/Developer/private-financial-dashboard`
   and `~/Developer/market-digest-pipeline`. A finance tab inside the estate product is either a
   **third** finance surface or a **view onto** one of those, and those are very different builds.
   ⛔ Do not let it arrive as a third by default.
2. **It is the first proposed surface that is NOT about property at all**, which makes it the real
   test of what this product is. ⚠️ Note what the panel found unanimously: the owner-level *monitoring*
   job is unevidenced, while multi-property *navigation* is validated. **A finance tab is neither** —
   it is a third thing, and it should be argued on its own evidence rather than riding in on the
   selector.

### 🧪 "Can we test these?" — measured: no

**There is no journey harness.** `telemetry-walk.js` exists (and is named once in `MOM-CYCLE-MAP.md`)
and the mom-proxy walk is a leg-6 step — but **nothing models or tests a journey end to end**, and the
first journey Paul names (login) does not exist yet to be tested. ⭐ **This is the same pipeline as
C1 + C2** — journeys are what a QA environment would exercise, and *"model the journey"* is the front
half of the feature-development process. **Not a separate workstream; the same one, with a name for
what it tests.**

**Routing** `[paul-suggested: "maybe this is a question for customer researcher"]` — `user-researcher`
owns *what the journeys are*; `practice-steward` owns *how they get tested*. **Queued behind the condo
research already in flight**, deliberately: adding a second charter mid-run dilutes both.

### Also captured

- ⭐ **"Fernwood as a test bed for everything"** — a standing role for the property, additive to
  dev/QA/prod (C1). Worth stating in its own right: it makes Fernwood the place where a mechanism is
  proven before it reaches a second estate, which is a *different* job from being instance 1.
- **Paul: *"we can do another backlog rationalization the right way to do this."*** The 2026-09-02
  proposal is unapplied and already carries the engine/config/instance axis this work needs.

---

## ⭐⭐ C0 · FERNWOOD AS A PRODUCT — multi-tenancy, hosting, auth, cost `[paul-raised 2026-09-01]`

> **CAPTURE ONLY. Nothing is scoped, nothing is decided, no work has started.** Paul asked for this
> to be written down and left alone: *"that's a whole nother big work stream that will need to
> involve a lot of research probably in all the experts weighing in, but I wanna capture that for a
> backlog for later."* Do not open this without his go — and when it opens, it opens as **research
> and options**, not a build.

**His words, the ask as given (2026-09-01):**

> *"I think this is probably a whole nother workstream. We need to figure out for Fernwood — focus
> on product a little bit more, making it a little more formalized, and figuring out what are the
> costs and path to doing that. So for example, getting a domain, and understanding if we want to
> set this up for someone else — which we're being approached for now with Bob. What's the
> best way to do that? Just give him his own custom domain, and ideally give him a login and
> password, or just a password, or some kind of authentication. And how do we make sure he has his
> own database that's not necessarily hosted on my computer? How do we make it all functional and
> modular — ideally in a way that the big engine components stay the same for Fernwood and for Bob's
> house and don't diverge too much."*

### The six questions inside it, kept separate because they have different answers

| # | Question | Note |
|---|---|---|
| Q1 | **Domain** — a real name for Fernwood, and per-tenant custom domains | Cost is small and known; this is the cheapest question here and could be answered alone |
| Q2 | **Authentication** — full login, shared password, or something lighter | ⚠️ Read against Track A doctrine before deciding: Mom's surface has **no login today, deliberately**. Any auth answer must not become a door she has to open |
| Q3 | **Per-tenant data** — Bob's records isolated, and not on Paul's machine | See "where it actually runs" below — this starts from a better place than it sounds |
| Q4 | **Modularity** — one engine, N properties, without divergence | The hard one. See "what would diverge first" |
| Q5 | **Cost** — to stand up, and per additional tenant | Partly measurable today; `/api/cost-log` already tracks per-day Anthropic spend |
| Q6 | **Whether to do it at all** | Not assumed. An approach is not a commitment, and ⛔ monetization is deferred to ~end-2026 (`[[project_monetization_deferred]]`) — this is a *portfolio and architecture* question right now, not a revenue one |

### ✅ RESOLVED 2026-09-02 — "Bob's house" is PERSONAL, and he has SEVERAL `[paul-stated]`

> *"The high-level result of the discussion with Bob was that he is more interested in this product
> managing his personal house — and he has more than one place, which it could expand to cover within his
> profile. The outcome was that he was more interested in personal use at this point than Tate
> Commons."*

**Three consequences, and the second one reshapes the data model:**

1. **Tate Commons is a DIFFERENT product and is not in this scope.** `~/Developer/tate-commons`
   stays where it is. Do not merge, do not write to it off this entry. It is not dead — it is not
   *this*.
2. ⭐⭐ **The tenancy unit is OWNER → N PROPERTIES, not user → property.** Bob asked for one profile
   covering more than one place — `paul-relayed`, and the only validated multi-property case there is.
   So a property should be a CHILD of an owner rather than the root.

   > ⚠️ **CORRECTED 2026-09-02, hours after it was written, by the user-researcher seat.** This
   > paragraph originally read *"that is the same shape as Paul (Fernwood, plus whatever follows)…
   > present in **both** of the only two users this product has."* **Paul owns one property today.**
   > *"Plus whatever follows"* was the main session's projection, written into a canon file as a
   > present fact and then used to justify the schema. That is this repo's most-repeated failure
   > (*a wrong SSOT row*) committed inside the very entry that resolves a stale row. **The schema
   > recommendation survives on Bob's evidence alone; the "both users" argument does not, and is
   > withdrawn.**

   ⭐ **And the correctness half stands on its own, independent of any feature.** Without property
   scoping, three things break in the direction that *looks like activity*: attribution loses its
   bench/unresolved scope, the ribbon clock is unscoped, and `sessions-quiet` sums two households.
   Those are defects to fix regardless of whether an owner-level surface is ever built. **Scope the
   record now; defer the surface.**
3. ✅ **Bob's house HAS a ground-truth contributor** `[paul-stated 2026-09-02]` — someone there who
   would answer the way Mom does for Fernwood. **So Track A's ask → fold → acknowledge machinery is
   CORE SHARED MACHINERY, not Fernwood-only.** ⚠️ And that makes the personalization boundary the
   sharpest question in the scoping: the *loop* ports, the *person* does not. See the brief.

---

### ~~⚠️ Is "Bob's house" the same ask as Tate Commons? — UNRESOLVED, ask Paul~~ (answered above; kept for the reasoning)

`~/Developer/tate-commons` was stood up 2026-08-30 for **Bob's 2026-08-21 ask**, recorded
there as *Fernwood for the whole **community*** — a standalone at a Tate subdomain. Paul's words
here are *"Bob's house"*, which reads as a **per-household instance of Fernwood**. Those are
different products with different tenancy models, and one of them may have been misread. **Do not
merge them, and do not write to `tate-commons` off this entry.** Settle it with one question to
Paul before either scoping runs.

### Where it actually runs today — the honest starting point (measured 2026-09-01)

**None of this is on Paul's computer already**, which removes Q3's scariest half before it starts:

- **Frontend** — `viewer.html`, **21,170 lines**, one file, all domain data inlined as JS consts by
  `tools/reinline.py`. Served by **GitHub Pages** from this public repo.
- **Backend** — one Cloudflare Worker (`worker/worker.js`, **2,720 lines**, name `tate-tracker`),
  **20 `/api/*` routes**, **one KV namespace** (`OBSERVATIONS`, id `100f2b95e4…`).
- **Auth** — a single `SHARED_TOKEN` secret in a `X-Tate-Token` header, gating `/api/*`. **There is
  no user identity anywhere in the system.** No accounts, no login. Who did a thing is inferred
  *after the fact* from `deviceId`, which `tools/people.json` is emphatic is a **browser bucket, not
  a person**. Q2 is therefore not "add a login screen" — it is introducing the concept of a user to
  a system that has never had one.

### ⭐ What would diverge first — the four couplings that make Q4 hard

Named now so the future session does not rediscover them. Each is a place where "one engine, two
houses" breaks on something real:

1. **The Worker holds Paul's keys.** `OPENAI_API_KEY` and `GITHUB_TOKEN` are Worker secrets. A
   second tenant on this Worker **spends Paul's money and can reach Paul's repo.** This is the
   sharpest constraint in the whole entry and it bounds every cheap answer to Q3.
2. **The write path goes through git into a specific public repo.** `/api/promote-species` commits
   to `plants.json` + `viewer.html` via the **GitHub Contents API**. Bob's confirmations would land
   as commits in *Fernwood's* repo. Canon-in-git is the architecture, not an implementation detail —
   arrivals live in KV, canon lives in the repo, and that hybrid is the centre of Q3/Q4.
3. **The weather card is bound to hardware Paul owns.** `AMBIENT_MAC` defaults to the on-site
   station's MAC. Weather is **the card Mom demonstrably opens most**, and Bob's house has no
   station. A tenant without a sensor gets a different product, not a configured one.
4. **Data is inlined into the served HTML.** 12 domain consts are baked into `viewer.html` and
   `check-data-inline.py` exists to police exactly that. Per-tenant data means either N built
   `viewer.html`s (divergence guaranteed by construction) or breaking the inline model (which the
   whole offline-on-a-mountain premise leans on — `96395b1`: *no cell, Wi-Fi from the house only*).

### ⭐⭐ THE REFRAME — auth is not a cost of the product, it is the thing that UNLOCKS it `[paul-stated 2026-09-01]`

Paul, on the privacy caveats raised against the household/contractor build-out:

> *"I think that ties directly into our question about making this more of a secure product, right?
> And how do we do that — because that then enables us to do some of these things where there's a
> real value in it. For example, being able to access the contact information, see receipts or
> histories and all that online. We need to be able to do that in a trusted way."*

**He is right, and this reorders the whole entry.** C0 was written above as *"how do we serve a
second tenant,"* with privacy as a constraint on it. The truer framing is the reverse: **the system
has no way to hold trusted data at all**, and both the second tenant *and* the household knowledge
Paul wants are downstream consequences of that one gap.

**`.private/` is a capability ceiling, not just a safety measure — measured 2026-09-01:**

- **436 MB** sits in `.private/`, gitignored, **on Paul's laptop and nowhere else.**
- It holds **254 service-record scans** — the receipts and invoices — catalogued by
  `service-records.manifest.json`, which IS committed and IS public.
- So the public record **knows 254 receipts exist and cannot show you one.** The index is
  reachable; the documents are not.

**And the data most locked away is the data most needed in the field.** The contractor's phone
number matters when the furnace quits. The water-heater invoice matters when the warranty claim is
live (that is H4, open right now). The shut-off valve location matters at the moment water is
running. Every one of those is a phone-at-the-property moment, and today that is precisely where
the record cannot reach — no cell service, Wi-Fi from the house only (`96395b1`), and the documents
on a laptop in Atlanta.

**What this changes about the questions above.** Q2 stops being *"do we need a login for Bob"* and
becomes **the load-bearing question of the whole entry**: an authenticated, trusted tier is what
lets the record carry contacts, receipts and histories at all — for Fernwood first, whether or not
a second tenant ever exists. Multi-tenancy then falls out of it nearly free, because a system that
can say *who you are* can already say *whose data this is*.

⚠️ **The one thing that must not be traded away.** Mom's surface has no login **by design**, and
the frictionless door is load-bearing for the only user this project has evidence about. A trusted
tier must be **additive** — a second, gated layer over the open journal — never a gate placed in
front of what she already reaches. If an auth design would make her type anything to see the
weather card, it is the wrong design, regardless of what it unlocks for Paul.

### ⭐⭐ ONE BOX FOR EVERYTHING — the single-entry-point vision, and the ceiling it runs into `[paul-stated 2026-09-01]`

> *"What's the Garden Guru box in Fernwood could be asked about anything, right, in the future — and
> that's kind of the vision. Is now the right time to water my azaleas, or walk through
> troubleshooting for one of the vehicles, or understand where the water shut-off valve is. Anything
> that we would upload to a given state or home is fair game to be questioned… then it becomes one
> single point of entry, it's very clear what's going on. And I want to limit developing multiple
> analysis or interaction points like Track A and Track B, if we can find a good clean way around
> it — which I feel like we can, but that's something we need to put to the experts."*

He also asked whether the A/B split was about **memory constraints and context bloat**, and whether
**RAG** is the answer so the corpus need not be constrained.

**Two corrections first, because they change what the work is.**

**① The A/B split was never a runtime split.** Its own reconciliation note (2026-07-17) says what it
was for: *"Fernwood is two products in one repo — split into Track A / B so the Mom arc reads
clearly and the fleet sub-system isn't interleaved through it."* That is a **backlog-legibility**
decision about this document. It was not motivated by context, and no runtime boundary was ever
built from it.

**② The one box already exists.** Measured 2026-09-01: `GARDEN_GURU_SYSTEM` carries an explicit
REGISTER section — *"You are one voice throughout — the same person who tends this whole place, the
living things and the machines alike"* — with a field-journal voice for the living property, a
shop-hand voice for the machines, a `<!--register:machine-->` marker the client uses to restyle the
reply, and a machine-log fence sharing the plant fence's mechanism *"distinguished only by
noteType."* **Paul's vision is largely the architecture already.** The gap is coverage, not entry
points: household systems, contractors, receipts and shut-off valves are not in the digest, so the
one box cannot answer about them yet.

### ⛔ THE ACTUAL CEILING, and it is closer than anyone has said

Every Guru turn ships the whole property digest as a cached system block. **Measured 2026-09-01:**

| | |
|---|---|
| `worker/digest.json` | **493,137 chars ≈ ~123,000 tokens** |
| model | `claude-haiku-4-5-20251001` (200K context) |
| **share of the context window consumed before the conversation starts** | **~62%** |

Composition: plants **41%**, vehicles **15%**, insects 10%, mammals 6%, birds 5%, snakes 5%,
amphibians 4%, fishing 4%, property 4%, lizards 2.5%, weeds 2%, turf 0.8%, zones 0.3%.

⚠️ **`worker.js`'s own comment beside that block says "the ~57K-token digest."** It is ~123K. **The
digest has more than doubled and the code's description of it never moved** — the constraint is
growing faster than the record of the constraint. (Same shape as
`[[reference_match_payload_not_container]]`: the number beside the mechanism reads plausible and is
wrong.)

**So Paul's instinct is right and the arithmetic is on his side.** Adding household systems,
contractor history, 254 receipts and a shut-off-valve map to a digest already at 62% does not
degrade gracefully — it hits a wall. **And a second property multiplies it**, which ties this
directly to Q3/Q4 above: one box across two houses cannot be one prompt.

### ⚠️ BUT RAG IS NOT FREE HERE — the trade the experts must actually price

The digest is affordable **because it is cached**: `cache_control: ephemeral` on a static block
means a 5-minute window re-reads it at 10% of base rate. **Retrieval makes the block vary per
turn, and a varying block is a cache miss every turn.** A naive swap to RAG can be *more*
expensive than the thing it replaces, not less. Do not let this open with "add RAG" as the premise.

Options worth pricing against each other, none chosen:
- **Tiered prompt** — a small always-cached core (property, zones, live state) + a retrieved tail.
  Keeps most of the cache benefit; the split point is the design question.
- **Domain-scoped digests** — route on the question, ship one domain's slice. Cheap, cache-friendly,
  and **it reintroduces a router**, which is the thing Paul wants to avoid. Name that tension.
- **True retrieval over an embedded corpus** — the only option that scales to receipts, manuals and
  forum notes, and the only one that pays the cache cost in full.
- **Do nothing yet** — plants alone are 41%; pruning or summarizing the digest may buy a year.

⭐ **The falsifier to hold this to:** *if answering "where is the water shut-off valve" requires
choosing which assistant to ask, the design failed.* One box, whatever is behind it.

**Where this sits:** it is Q4 (modularity) and Q5 (cost) of C0, seen from the runtime rather than
the tenancy side — same workstream, same expert panel, same "research and options, not a build."

### ⭐⭐ THE DETAIL-VS-CARD SPLIT — measured, and it is worse than remembered `[paul-raised 2026-09-01]`

> *"There's a question about — at one point we made a decision to kind of split the super-detailed
> records versus what's on the card. But I think in reality this conversation agent would need to be
> able to look at that whole record in detail. And maybe it's not always loaded into context from the
> beginning — in fact we can avoid that — but it accesses that information when it's clear that it
> needs it, and we can build deterministic helpers or lookup tables or who knows what."*
>
> *"It would even be cool to be able to have it pull up pictures from past repairs — if you ask how
> something was done, or what a specific material is. And also just in general, keeping track of
> tools and supplies… a functionality we want to consider."*

**He is remembering a real decision, and it is recorded.** `tools/build-digest.py` carries the whole
history: vehicles were EXCLUDED from the digest 2026-07-17 for two reasons, and Paul reversed it
2026-07-28. The file is explicit that only one reason was ever technical — *"CAPACITY — dropping
vehicles relieved the ~80K digest line. That line turned out to be about COST, not capability, and
it is not enforced anywhere: it sets a status string, nothing more."*

**But re-enabling the vehicles did not re-enable the record.** Measured 2026-09-01:

| domain | source | reaches the Guru | kept |
|---|---|---|---|
| plants | 221,448 | 202,607 | 91.5% |
| property | 19,663 | 17,970 | 91.4% |
| insects | 57,294 | 49,143 | 85.8% |
| **vehicles** | **308,410** | **72,804** | **23.6%** |
| zones | 26,039 | 1,538 | 5.9% |

**`digest_vehicles()` drops these fields ENTIRELY:** `serviceHistory` · `rhythms` · `circuits` ·
`techniques` · `mileage` · `registration` · `restoration` · `photoEvidence` · `referenceLibrary` ·
`openMechanicalItems` · `vin` / `vinDecode` · `acquired`.

**⛔ The three that matter most, stated plainly:**

1. **All 61 service-history rows are gone. Every one.** The assistant that is supposed to be a
   troubleshooting and maintenance partner **cannot see a single thing that was ever done to a
   machine.** It knows specs, current maintenance values, open needs, notes and who to call — and
   nothing about what happened. Ask it *"when did we last do the Bronco's brakes"* and it cannot
   answer from a record that holds the answer.
2. **`circuits` and `rhythms` shipped on 2026-08-31 and are invisible to the assistant.** The
   30-row breaker directory and the recurring-chore ladder were built the day before this was
   measured, and the Guru cannot read either. *"Which breaker runs the patio outlets"* is in the
   record and unreachable through the one box — which is precisely Paul's falsifier from the section
   above, already failing today.
3. **`photoEvidence` is dropped too**, so the "pull up pictures from past repairs" idea is blocked
   by the same mechanism rather than by a missing capability.

⚠️ **AND THE DIGEST IS ALREADY PAST ITS OWN STATED CEILING.** `build-digest.py` sets a *"soft target
~50K tokens, actual Haiku ceiling ~100K before retrieval degradation becomes a concern."* It is at
**~123K**. It is **23% past the limit this file wrote for itself**, the limit is **enforced
nowhere** (it sets a status string), and the comment beside the API call still says ~57K. So adding
the dropped fields back into the digest is not available: the thing being asked for **cannot** be
solved by putting more in the prompt.

### ⭐ WHY HIS INSTINCT IS THE RIGHT ONE — and why it is NOT the same as "add RAG"

His own framing — *"not always loaded into context… it accesses that information when it's clear it
needs it… deterministic helpers or lookup tables"* — describes **tool-use / function-calling over
deterministic lookups**, not embedding-based retrieval. That distinction is worth protecting through
the whole workstream, because the two have opposite properties here:

|  | embedding RAG | deterministic lookup tools |
|---|---|---|
| cache | breaks it (variable block each turn) | **preserves it** — the cached digest never changes |
| answer for *"last brake job on bronco-1989"* | nearest-neighbour, may miss | **exact, every time** |
| new failure mode | silent wrong-chunk retrieval | a tool call that errors **loudly** |
| fits the repo's doctrine | weakly | ⭐ directly — a closed set of legal queries |

⭐ **This also satisfies the "deterministic things need a non-AI door" rule.** A lookup like
`service_history(vehicle_id)` or `circuit_for(room)` is a function a human can call from the
terminal AND the model can call as a tool — one implementation, two doors, and the AI-free path
exists by construction rather than as a second build.

⚠️ **The known trap, named now:** `[[reference_match_payload_not_container]]`. A lookup helper that
returns `[]` for a mistyped vehicle id looks identical to one that correctly reports no service
history. Every helper needs a **closed set of legal inputs** and must **raise** on anything outside
it, never return empty.

### 🧰 TOOLS & SUPPLIES — the record already exists; what is missing is REACH

Paul asks for tool/supply tracking as new functionality. **It is already built:**
`.private/service-records/TOOLS.md` (12.7 KB, last updated 2026-08-31) and `AMAZON-PARTS.md`, with
the tool/part distinction already drawn — *"a **part** is consumed into one vehicle; a **tool** is
durable and serves the whole fleet."* It exists because of three misses in one 2026-08-28 session
that each nearly bought a duplicate, including an entire plastic-welding kit *"in no record at
all."*

**So the gap is not the register — it is that the register is in `.private/`, gitignored, on the
laptop, and absent from the digest.** It is the same finding as the 254 receipts one section up, and
the same shape: **the data most useful standing in a hardware-store aisle is the data structurally
guaranteed not to be there.** ⛔ Do not open this as "build a tools tracker." Open it as *make the
tools register reachable* — which is the auth question (Q2) and the retrieval question, not a new
domain.

⚠️ `TOOLS.md` opens with its own **COVERAGE** warning: the parts record has been measured wrong in
BOTH directions. Absence is not evidence, and a stated order clears only with an ORDER NUMBER
(`[[reference_parts_record_under_reports]]`). Any lookup built over it must carry that, not flatten
it into a clean-looking inventory.

### 🎯 HOW C0 OPENS — a user-researcher INTERVIEW first, then agile artifacts `[paul-stated 2026-09-01]`

> *"It's worth at some point having the customer researcher come in and kind of interview me, to be
> sure that my intentions are clear and also establish a vision here for what we're trying to build.
> Fernwood is kind of the first example of it, but there's an overarching **product engine
> capability** that I'm trying to steer us towards — and ensure we're on a good path to not have a
> bunch of diverging issues, and we will have flexibility so that we can approach other people and,
> to oversimplify, pull in all their data and preferences and what they're interested in and want to
> see, and then just populate it."*
>
> *"I want to try to have some of the classic agile product-management artifacts to keep us on the
> right track — because if we get off, this could get real confusing really fast."*

**⭐ THIS REORDERS THE ENTRY. C0 above reads as an architecture question; it is not one yet.** Every
option in it — tiered prompt, domain-scoped digests, retrieval, lookup tools, per-tenant data — is
downstream of a product decision nobody has written down. **Beat 0 of this workstream is the
interview, not a design.** Do not open C0 with engineering.

**Why user-researcher is the right seat and not a formality:** Bob is a **real prospective
user who can be asked rather than assumed**, and that agent's charter forbids replacing real users
with synthetic ones without an explicit OK. Paul is both product owner *and* a real Track B user.
Mom is the only user with months of behavioural evidence behind her. Three genuine research
subjects, none of them hypothetical.

#### ⭐ THE MINED HISTORY IS RESEARCH INPUT, NOT JUST A RECORD GAP-CHECK `[paul-stated 2026-09-01]`

> *"All of this maybe is worth mining kind of with the customer researcher, to help design the cycle
> or loop requirements."*

**This changes what the conversation mines are for.** They were commissioned as record-completeness
checks. Paul is pointing out that the same corpus is **behavioural evidence about how he actually
works** — and that is exactly the input a loop's requirements should be derived from, rather than
designed from an armchair.

⭐ **And it is not hypothetical: the first mine already produced a finding of exactly this kind**,
without being asked for one. `.plans/2026-09-01-vehicle-conversation-mine.md` §4, cross-cutting:

> *"Roughly four in five of these openings are voice-dictated run-ons that (a) name the machine by
> nickname, (b) state a symptom or a scope, and (c) **carry a separate instruction about the
> record** — 'let's record all this', 'go ahead and fold today's findings into the record', 'Please
> log all this'. **He is running two loops per session: fix the thing, and make the record carry
> it.** The second instruction is almost never merged into the first, and it is almost never
> omitted."*

**That is a jobs-to-be-done statement, fully evidenced, sitting in a file.** A `user-researcher`
session would otherwise have to elicit it from scratch — and would get a *reported* version rather
than an *observed* one, which is strictly weaker evidence.

**What this implies for sequencing, and it is a real change:** C0 beat 0 was written above as *the
interview first*. It is better as **mine → interview**. The mines are already running; their §4-style
findings become the researcher's evidence base, so the interview spends its time on the questions
only Paul can answer (vision, tenancy, whether categories are per-tenant) instead of re-deriving
behaviour the corpus already shows.

⚠️ **The boundary that must hold:** an observed pattern is evidence about **what he did**, never a
statement about **what he wants**. The `user-researcher` charter already tags every claim
`assumption | inferred | validated` — a mined behaviour enters as **inferred** at best, and only
Paul's answer promotes it. Do not let a corpus finding arrive at the interview pre-promoted.

**Also in scope for the same treatment:** the fleet loop's own requirements. **B0** records that
Track B has **no ask loop and no arrival path for its own user** — a conversational or photo-borne
update from Paul triggers *nothing* (`fleet_probe.py`'s four signals are SEASON · INBOX ·
PROVENANCE · STALE-OPEN, and none of them is *"Paul said something"*). What the corpus shows about
how his updates actually arrive is the direct evidence for designing that path.

### ⚠️ THE PORTFOLIO HAS NO PRODUCT-OWNER FUNCTION — this is that gap arriving

`[[project_backlog_coherence_finding]]` already records it: **there is no product-owner agent.** The
roster has `user-researcher` (proto-personas · JTBD · journey maps — *discovery* artifacts) and
`ux-expert`, `engineering-partner`, `content-steward`, `ai-advisor`. **Nothing owns a product vision,
a roadmap, or acceptance criteria.** Paul is asking for exactly that function. Whether it is a new
seat or a mode on an existing one is itself a decision for `/team-audit`, not something to assume.

**⛔ And this file is NOT the backlog he is asking for.** `BACKLOG.md` is ~1,400 lines and is
excellent at what it actually is — a **decision record**, read for *why*. It is a poor agile backlog:
no estimates, no acceptance criteria, no prioritised increment, shipped and open interleaved by
topic. **Conflating the two is precisely how this "gets real confusing really fast."** Keep the
decision record; put the product artifacts somewhere else and let this file point at them.

**Candidate artifact set — to be chosen WITH him at the interview, not imposed:**
product vision statement (one page, falsifiable) · proto-personas for Mom / Paul / Bob ·
jobs-to-be-done for the one-box assistant · a now/next/later roadmap · epics with acceptance
criteria · a definition of done · a decision log (**already exists — this file**) · a risk register.
⚠️ **Pick the few that earn their keep at two users.** A full ceremony set for a two-person app is
its own kind of drift, and this repo's doctrine is `defer-affordances-pending-signal`.

### ⭐ THE NUMBER THE INTERVIEW MOST NEEDS — what "just populate it" costs today

His vision sentence — *"pull in all their data and preferences and what they're interested in and
want to see, and then just populate it"* — implies the **domain set itself is configurable per
tenant**. Fernwood's is not. Measured 2026-09-01, lines naming a specific domain:

| surface | lines naming a domain |
|---|---|
| `viewer.html` | **606** |
| `worker/worker.js` | 85 |
| `tools/build-digest.py` | 50 |
| `tools/check-data-inline.py` | 24 |
| `tools/momlib.py` | 23 |

Plus **68 domain-specific renderers** in `viewer.html` and **10 hand-written digest builders**
(`digest_plants`, `digest_wildlife`, `digest_vehicles`, `digest_zones`, `digest_turf`,
`digest_fishing`, `digest_weeds`, `digest_property`, …).

**So per-tenant DATA and per-tenant DOMAINS are different orders of work, and the vision sentence
quietly asks for the second.** A second property with plants, vehicles and a house is close to free.
A tenant who wants beehives, or a boat, or no garden at all, is ~790 lines and 78 functions.
⚠️ **`momlib.DOMAINS` is a real declared manifest and `check-domains.py` enforces conformance against
it — that is a genuine spine and the best evidence the engine idea is sound.** The divergence risk is
everything *downstream* of it that never learned to read it.

**Ask him at the interview, in his words, not ours:** *when you say pull in their data and populate
it — are the categories the same as Fernwood's, or does each place get to name its own?* The answer
sets the whole engineering scope and nothing else in C0 can be sized without it.

### What it will need when it opens

Paul named it: **research plus all the expert seats.** At minimum `engineering-partner` (path
evaluation, before code), `ai-advisor` (where AI sits per-tenant, and whose key pays), `ux-expert`
+ `content-steward` (Q2 — an auth story that does not cost Mom her frictionless door), and
`user-researcher` (Bob is a real prospective user who can be asked rather than assumed).

**Do not wrap this in loop machinery.** Per `[[feedback_cyclical_vs_finite_projects]]` this is
**finite** — a research-and-decide arc with an end — not a cycle. Burn it down; don't give it beats.

| Item | What it is | Gate |
|---|---|---|
| **Worker deploy automation — arm the secret** | GitHub Action `.github/workflows/deploy-worker.yml` is built + runs green, skipping the deploy until armed. **One-time: add repo secret `CLOUDFLARE_API_TOKEN`** (Cloudflare → API Tokens → "Edit Cloudflare Workers"; GitHub → repo Settings → Secrets → Actions). After that, Worker changes self-deploy on push. | **⚡ NOT A GATE ON ANYTHING — proven by command 2026-07-28, not by prose.** `test -x tools/deploy-worker.sh` succeeds: `19aa3aa` made deploys **agent-runnable without the token** (run it with the Bash sandbox disabled — see `CLAUDE.md`). Arming the secret is a convenience that moves deploys onto push; it is Paul's (external account) and **optional**. Anything previously recorded as "blocked on the Cloudflare token" was blocked on nothing. |
| **🔑 Rotate the Ambient Weather API key** (found 2026-07-25) | The Ambient `applicationKey` + `apiKey` are hardcoded as fallbacks in `tools/record-daily-rollup.mjs` AND embedded in `viewer.html` — served world-readable on the public Pages site (confirmed raw-fetch 200). Moderate blast radius (read access to the station + rate-limit burn, nothing financial). **Rotate at ambientweather.net;** then Claude will move the new key to a GitHub Actions secret + strip the hardcoded fallbacks from both files (one pass). The rain backfill ran on the current (exposed) key at Paul's direction 2026-07-25. | **WAITING ON PAUL** (secret) — say "rotated" → Claude does the de-embed cleanup. **🔴 RE-VERIFIED STILL LIVE 2026-07-28** against the *public* raw file: both 64-char hex literals are retrievable from `raw.githubusercontent.com` right now. ⚠️ **Pointer corrected — they sit at `viewer.html:6451-6452`, NOT 6389-6390**; that day's edits shifted them, and a stale line number on a security item is exactly how it gets read as already handled. Also present in `tools/record-daily-rollup.mjs` and `.github/workflows/record-weather.yml`. Exposed since `99f0f07` (2026-05-05) = **84 days**. Blast radius stays small (read access to one weather station), which is why deferring is still reasonable — but this is **deferred, not done**. **Unpark trigger (Paul's call 2026-07-27):** *"we'll do the ambient de-embed as part of a Fernwood working session"* — not as a standalone fix. |
| **✅ ONE shared entity-resolution map — "assumed plants" hit THREE times in one day** (filed 2026-07-26 · **SHIPPED 2026-07-27**) | Every place that resolved a card's `entityRef` to a record re-implemented the lookup, and each was written assuming plants — all three shipped broken and none failed loudly: `fold-answer.py` degraded weed cards to *"entity not found in plants.json"*; `read-mom-feedback.py`'s probe did the same; and `buildCard` gated on `eref.type === "plant"`, so **`q-weed-stiltgrass` was served for six days with a photo Mom took rendering nothing**. **Now collapsed:** `momlib.ENTITY_SOURCES` is the ONE declaration (carrying file + list key + viewer const); `fold-answer.py` binds straight to it and `check-cards.py` **reads** `buildCard`'s binding via `momlib.viewer_entity_map()` instead of re-typing a `RENDERABLE` set. JavaScript cannot look a `const` up by name, so `buildCard`'s `ENTITY_DATA` is the one irreducible copy — but it is no longer agreed by hand: `momlib.entity_map_divergence()` derives the comparison, `check-cards.py` reports it once up front, and `test-feedback-cycle.py` has a RESOLVE leg that fails on a missing type, a wrong const, and an unreadable binding. Behaviour proved unchanged: a 16-card snapshot (state · entity hit · photo · probe target · the exact fold edit) is byte-identical pre/post. | **Adding a domain = `momlib.ENTITY_SOURCES` + `buildCard`, nothing else** — the test names exactly what is missing. ⚠️ Still open and **Paul's call, deliberately not touched:** `harvest-questions.py` is the one remaining plants-only site, and it is a *producer*, not a resolver — it reads `plants.json` only and knows only the `variety`/`bloom` marker shapes, not the weeds' top-level `confidence`. Handed the weed records it drafts **zero** candidates, so `crabgrass`, `virginia-creeper` and `wild-violet` (all `confidence: inferred` + `status: needs-confirmation`) can never be harvested while `japanese-stiltgrass` and `beggars-lice` got hand-authored cards. Wiring it to the shared map would put **new cards in front of Mom** — a Mom-facing behaviour change, not a refactor. |
| **⭐ How should the record be ORGANIZED, holistically? (Paul, 2026-07-28)** | Raised off the `harvest-questions.py` weed gap above, and it reframes that item: *"technically, weeds are plants, right? I think we need a holistic view of how to organize all the information."* The gap is a **symptom of an unanswered taxonomy question**, not a wiring bug — every domain so far was added by accretion (plants → wildlife → weeds → vehicles → equipment → household systems B6), each with its own JSON file, its own card, and its own implicit shape, and `ENTITY_SOURCES` now makes that list explicit **without ever deciding what the list should be**. Live tensions already on the board: weeds carry a top-level `confidence`/`status` while plants carry `variety`/`bloom` markers (the exact mismatch that makes weeds unharvestable); Mom herself derived the vehicles/equipment/household-systems split unprompted (B6) — evidence the *domains* are right even if the *schema* isn't; and the field-journal framing may want "things I tend / things I fight / things that visit / things that run the place" where the data model wants shared fields. **Two ways to answer it and they're not exclusive:** ask the **team** (engineering-partner on the data model + ux-expert on whether the domain split is how Mom navigates, and user-researcher on whether her mental model matches the file layout), and/or **ask Mom** — she has already proven she'll propose structure unprompted, and this is the one kind of question that asks no verdict of her about a plant she might get wrong. **Do not answer this by refactoring first** — the answer decides whether `harvest-questions.py` gets wired to the shared map or the shape underneath it changes. | **📄 ANSWERED 2026-08-02 — recommendation on the table, Paul's call.** Full analysis: `.engineering/2026-08-02-record-organization.md` (field inventory of all 11 domain files, measured not recalled). **Finding: the domains are already right and a reorganization is the expensive wrong move.** A universal spine already exists unplanned (`id`/`name`/`scientificName`/`emoji`/`photo`/`attribution`/`notes` in every domain); the five wildlife files are one schema wearing five filenames; the ONLY axis that actually diverges is **honesty** — weeds carry top-level `confidence`+`status`+observation provenance (the best design in the repo), plants carry it nested and partial (3/36 variety, 24/36 bloom, 8/36 `_provenance`, 0/178 seasonNotes), **wildlife carries none at all — 0 of 64 records**, and vehicles use a fifth shape. **And the harvester is worse than 'plants-only': it hardcodes the `variety` and `bloom` FIELD SHAPES**, so repointing it at `weeds.json` would find zero candidates — the weeds are marked askable in their own vocabulary, which it cannot read. **Answer to 'weeds are plants': biologically yes, but this record's split has never been biological — it is what you DO (tend vs fight), which is the axis Mom derived herself with vehicles/equipment/household-systems. Biology is a PROPERTY, not a folder.** Recommended, dependency-ordered: **M1** one uncertainty contract in every domain + a marker-agnostic harvester (the whole unblock) · **M2** a `momlib` temporal accessor, NOT a rename of 64+ records · **M3** declare the action group in each `_meta`. ⚠️ **The risk is supply, not schema:** a harvester that can see four domains puts new cards in front of Mom, and the 5-slot cap binds immediately with 8 already on the bench. |
| **Citizen-science scaffolding** | Dormant code in viewer.html. | Paul's call: re-enable / drop / leave dormant. |
| **Batch document-mining playbook** | Generalize the triage→characterize→verify→fold receipt-mining pattern cross-project. | Until a 2nd project needs it. |
| **Expert-proposed principles (candidates)** | "reuse the mechanism, not the semantics"; "match structure to the reader's unit of meaning"; "widen the ask → implied the log". | Paul demote/keep call. |

---

# SHARED REFERENCE