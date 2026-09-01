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
| **1** | **Fleet lap 1** (`cycle/fleet/CYCLE-MAP.md`) | nothing | 🔴 **READY** — FIRED on INBOX · PROVENANCE · STALE-OPEN, `lap_count: 0`, never run |
| **2** | Review the two conversation mines | agent (running 2026-09-01) | ⏳ |
| **3** | **`user-researcher` interview** — beat 0 | step 2 | ⏸ |
| **4** | Agile PM artifacts — vision · personas · JTBD · now/next/later | step 3 | ⏸ |
| **5** | Architecture options, priced | step 4 | ⛔ **do not start here** |

**Parked on Paul, correctly:**
- **Mom-cycle lap 7 is OPEN at leg 6** — the ack ribbon is held until he does more zone work.
  `MOM-CYCLE-LOG.md` § Lap 7. A later run must not read `R1 ack staleness 🔴` as neglect.
- **Is "Bob's house" the Tate Commons ask, or a second one?** One sentence unblocks scoping. See
  the UNRESOLVED block below.

**Independent, take when there is room:**
- **UX sweep** — owed, all three thresholds blown (29d/21 · 65 viewer commits/20 · 6 laps/3).
- **Contractor normalization** — the 32-string cleanup does **not** need the auth decision; only
  *publishing contact details* does. See `BACKLOG.md` § CONTRACTORS & TRUSTED PEOPLE.
- **D4 pre-glance stack ledger** (1,712px at 414×A+) — owed since 2026-08-31, never run.

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
| `corpus_search --sessions` ignores its query | `~/Developer/operating-layer/BACKLOG.md` |

⚠️ **A lot of this session's reasoning lives only in COMMIT MESSAGES** (2026-09-01, `7071162`
onward). If a claim here looks unsupported, `git log` before assuming it was invented.

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
> set this up for someone else — which we're being approached for now with Bob Rolader. What's the
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

### ⚠️ Is "Bob's house" the same ask as Tate Commons? — UNRESOLVED, ask Paul

`~/Developer/tate-commons` was stood up 2026-08-30 for **Bob Rolader's 2026-08-21 ask**, recorded
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

**Why user-researcher is the right seat and not a formality:** Bob Rolader is a **real prospective
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