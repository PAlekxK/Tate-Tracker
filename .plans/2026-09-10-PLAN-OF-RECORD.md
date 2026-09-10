# Plan of record — the road to five founded households

- row: `OBJECTIVES.md` G1 (proposed this file; Paul to ratify the row itself)
- objective: O3
- class: engine
- stage: concept
- seats: engineering-partner · practice-steward · account-model scope · testing-architecture scope — all four ran 2026-09-10
- depends-on: `.plans/2026-09-10-account-estate-model-SCOPE.md` ⚠️ **its migration table's M1 was
  KILLED 2026-09-10** (it proposed deleting `nigel`/`aida`, beta owners 3 and 4). Annotated in place;
  the migration starts at M2. Do not follow that table from an unannotated copy.
- depends-on: `.plans/2026-09-10-testing-architecture-PLAN.md`
- depends-on: `.plans/2026-09-10-WORK-QUEUE.md`

⭐ **This is a POINTER document.** Every claim cites where it actually lives. Nothing here is the
source of truth for anything; it exists so three build windows and Paul steer by one page instead of
thirteen cards and four plans. **When it disagrees with a cited source, the source wins.**

---

## ① THE MILESTONE — **READY TO INVITE** `[paul-stated 2026-09-10]`

> *"When are we ready to send Aida and Nigel their invites — fully set up and tested, with all the new
> environments and everything we built today? That's probably our next milestone. Basically saying
> we're ready to send to Aida and Nigel because **we've done all the plumbing and infrastructure work
> we know of at this point**, and now we're ready to start working on **user-facing features**."*

⭐ **This is G1 reframed as an EVENT rather than a state, and the event is better.** A state invites
argument about whether a clause is met; an event has a trigger, a date, and a person who pulls it.
**The milestone is the moment Paul sends two invites.** Everything below is what must be true first.

**What it means that G1-as-a-state did not:**
- **"All the plumbing we know of"** — the bar is *our current knowledge*, not perfection. Work we
  have not yet discovered does not hold the milestone; work we HAVE named does.
- **"Fully set up and tested"** — tested means **walked**, not "the deploy succeeded." A walk of the
  founding path, not an assertion about it.
- ⭐ **It is also the gate that OPENS feature work.** Plants, vehicles and zones are out of scope
  until this fires — and in scope the moment it does. That makes it the single most useful line on
  the board: it says what we are not doing *and* when we start.

⛔ **The founding path must be exercised, not bypassed.** `nigel` and `aida`'s pre-provisioned envs
are being deleted `[paul-stated 2026-09-10]` — partly for a clean base, and partly because leaving
them would let the beta launch **without the product ever creating an estate.** Their estates are
created through `POST /api/estate` or the milestone has not been met.

---

## ①b THE STATE IT REQUIRES — G1 `[paul-stated 2026-09-10]`

> **G1 — Five owners, each with a working, personalized household.** `paul · mom · bob · aida ·
> nigel` are each a **user and an owner**. For each: they hold an owner grant; they signed up through
> the link path; **their household is centered on their own address** — place derived, canon their
> own, model routes answering from their record; their record captures what they enter; and their
> feedback reaches a loop that reads it. Across all five: **the user journeys are documented, and one
> testing procedure walks them.**
>
> ⛔ **Features — plants, vehicles, zones — are out of scope until G1 is met.**

**Two clauses Paul ruled explicitly, against a recommendation to defer them:**
- **Personalization is INSIDE G1**, not after it — *"we are already producing a personalized product
  by having it centered around their address. Personalization is critical at every step."*
- **The unit is the USER, not the estate**, and Paul counts himself — *"my user account, like Mom,
  Bob, Aida, Nigel, are all users and owners."* `excludeFromEngagement` is a telemetry flag, not a
  roster exclusion.

⚠️ **This row existed in no file until today.** Three independent seats found that separately
(engineering, practice-steward, testing-architecture `fernwood-20`). Ratify it into `OBJECTIVES.md`
— **not a fifth surface**; that file has held at 15 lines for a week while `BACKLOG.md` grew to 4,327.

---

## ①c THE STANDING LENS — elicitation & derivation `[paul-stated 2026-09-10]`

> *"At each step, are we requesting all the information that makes sense to give us enough data to
> populate and triangulate what we need for that estate? And every time we ask for information,
> ideally we're confirming that information and making it clear what's linked to it and what's being
> added… Are we asking the right questions to really drive personalization for each account and
> estate at each step? That's something we want built into the review cycle and the testing cycle
> overall — especially as we get a growing user base with more and more divergent profiles."*

**A permanent reading posture on every walk, not a one-off review.** Three questions per stop:
**ASK** (does this step request what it should?) · **CONFIRM & SHOW** (is the value confirmed, and is
it visible what was *derived* from it and what was *added*?) · **PERSONALIZE** (are these the right
questions for this estate?).

⭐ **It is NOT "ask more questions."** `feedback_check_standards_before_building` ruled that fewer
fields is the standard. The reconciliation is Paul's own address example — **one field, many derived
facts**: coordinates, elevation, USDA zone, frost dates, watershed, area history. **The metric is
derived-facts-per-asked-field**, and a step asking for something it could derive is a finding.

⭐ **It is the exact inverse of the neutrality probe.** Neutrality asks *"are we showing them anything
that isn't theirs?"* This asks *"are we capturing enough of what IS theirs?"* A household can pass one
and fail the other: a young estate can be perfectly neutral and completely hollow.

**Composes with, does not replace:** `[paul-ruled]` every ASK states USE · NOT-use · WHO SEES IT ·
reversibility. And capture stays deterministic — deriving elevation and zone is deterministic;
anything generative (*"the history of the area"*) lands on the ask path, marked `inferred`, never
written to canon as fact.

⛔ **It applies hardest to J0**, the founding journey — where an estate is populated from nothing, and
which is currently declared-but-unbuilt pending `POST /api/estate`.

## ② THE READINESS BAR, AND THE HOLDS `[paul-stated 2026-09-10]`

> *"Let's set as our long-term goal that Guru is working for all households that launch. Right now we
> have Bob's and Mom's invites out. Neither of them has really set up an estate. We can hold on Aida
> and Nigel until we catch up to our readiness definition."*

- **A household that LAUNCHES has Guru working.** No launching on the deterministic app alone.
- **Aida and Nigel are HELD** — release condition: *the readiness definition is met*. A hold naming
  the work, not the mechanism.
- **Bob's invite is out and unspent; Mom's is spent.** Neither has founded an estate. We send no
  further invites until ready.

⛔ **Consequence: A1 → A2 is the beta-gating work.** Not a quality improvement — the thing standing
between today and anyone new arriving.

---

## ③ WHERE THE FIVE ACTUALLY STAND — measured 2026-09-10, not asserted

| owner | person | estate | state |
|---|---|---|---|
| **paul** | `p-7f3a2c` / `pkirsch` | `est-d93508` | Grant Park Condo, established in production. ⚠️ moved off production onto its own estate today (`fernwood-private@ac1d414`); Paul expects it back — see ⑦ |
| **mom** | `p-b91e4d` / `marguerite` | `est-e6696a` | **account created 12:24 PM ET** at a pre-provisioned estate. Authored 4 feedback records in the 2 minutes after |
| **bob** | `p-2f4735` | `est-9a74df` | grant minted, **invite UNSPENT** |
| **aida** | ⛔ none | `est-92e588` | estate provisioned `c1ae9bb`; **held** |
| **nigel** | `p-5cf094` | `est-76012d` | estate provisioned `c1ae9bb`; **held** |

⭐ **Nobody has ever founded an estate through the product.** `POST /api/estate` does not exist; every
estate was minted by hand in `wrangler.toml`. Mom signed up *at* an estate; she did not create one.

🔴 **Zero of five "come up whole" today.** `worker/digest.json` is one global file stamped
`est-3c9f1a`, so every real household's model routes answer **503 `canon-not-this-estate`** — Mom's
included. No household has a derived place.

---

## ④ THE RULED MODEL — full detail in `.plans/2026-09-10-account-estate-model-SCOPE.md`

| | ruled |
|---|---|
| **credential** | resolves to a **PERSON** who has estates, not to an estate `[fernwood-14, paul-ruled]` |
| **account key** | `account:<personId>` deployment-scoped, `username:<lowercased>` → `{personId}` as index |
| **usernames** | **unique per deployment** — already enforced by `/api/account/available` |
| **grant** | the person↔estate **edge**. No estate-less grant; a person with no household holds **zero** grants and `estates: []` |
| **identity vs authority** | **two lookups.** `route:<hash> → {personId}` names the person with no grant involved; `grantsFor(personId)` answers what they may do |
| **which estate a request means** | **`X-Estate`**, a *disambiguator among estates the credential already proves* — never an input to scope resolution. Not in the set → **404** |
| **feedback scope** | `account:<personId>:feedback:<date>` travels with the person · `<estateId>:feedback:<date>` stays with the place. **Server decides**, client's `surface` never chooses the namespace |
| **view-only** | a third `capability` value, `reader`, failing toward less |
| **door records** | deployment-scoped |
| **credential class** | stamp `via: master \| grant` on every write |
| **grant-key + `POST /api/estate`** | **ONE ruling, bound.** The day a person can hold two estates, enumeration must already exist |

⚠️ **`X-Estate` refines a ratified rule and cost a control.** The 09-02 rule — *"tenant is derived
from the CREDENTIAL, never from the path"* (`~/Developer/fernwood-private`, §2b) — did not
contemplate a credential legitimately spanning several estates. `falsifier-tenancy.py` **C2 is
retired by name** and replaced with the grant-checked form. Paul ratified knowing the cost. ⛔ The
replacement must land **in the same change that first reads the header**.

---

## ⑤ THE SEQUENCE — what gates what

**1 · A1 — publish `<estateId>:digest` per estate.** `tools/publish-digest.py` exists with `--check`
and **has never been run**. Tools + KV only.
**2 · A2 — `canonFor(env, scope)` fail-closed; retire `canonIsThisEstate`; delete `CANON_FOREIGN_OK`.**
⚠️ Deleting that flag takes `qa`'s and `lab`'s Guru with it **unless the digests publish first** — so
A1 is A2's green light. Prove on lab with two estates first.
⭐ **A1 + A2 together are the readiness bar.** Everything below is real and none of it gates the beta.

⚠️ **Three documents give three answers to "what gates the beta" — they are not in conflict, they
name different blockers.** Reconciled once, here: **A1 + A2 gate the READINESS BAR** (a household
comes up whole, Guru answers from its own record — the thing holding Aida and Nigel). **A2 + B0
gate ISOLATION IN PRODUCTION** (many households safely on one deployment — the thing holding the
condo's return and `POST /api/estate`). **A5** is the model-route path *inside* A1+A2, not a fourth
answer. Cite this line rather than re-deriving it.

**3 · `personFor(request, env)`** — token → `route:` → `{personId}`, no grant. Without it Q3's rule 1
and `attributeToPerson` are both **shipped and dormant**.
**4 · B0** — `scopeOf(env)` conversion, read-only handlers first. ⚠️ **Exception:** the four handlers
that already resolve a grant convert FIRST, because routing arms them.
**5 · Durability** — fix `household-export.py` ✅ done (`eedd456`), then **write `household-import.py`**.
⛔ **Nothing in Phase C runs before both exist and have been exercised on lab.**
**6 · B3 `POST /api/estate`** + the grant re-key, together. The only completely unexercised step.
**7 · Testing** — P0 per-run unspent invite, P2 named server-record fixture → **J3 returning-finished**,
which no walk in this project's history has ever entered.
**Deferred, ruled not-now:** `X-Estate` · `reader` · `via:` · A4 place literals · B2 · B4.
**Killed:** C4 `ENV_NAME` → production · deleting `nigel`/`aida`.

---

## ⑥ WINDOW OWNERSHIP — one writer per file

| window | owns |
|---|---|
| **`tate-tracker-ec`** | ⭐ **`worker/worker.js` — sole writer.** Credential + account path, feedback write path, `falsifier-tenancy.py` |
| **A1 window** | `tools/publish-digest.py`, `build-digest.py`, KV digest publication. **Does not touch `worker.js`** |
| **`testing-arch-e2`** | the walk harness — `journey-walk.py`, `release-gate.py`, `synthetic-identity.py`, `walk-*.py`, `.private/synthetic-walks/`, cards 15–22 |
| **coordination** | `paulkirschenbauer-5d`. Cross-lane requests route through it; no window reaches into another's files |

⚠️ **Measured today:** four relayed claims failed verification, and every one was caught by the
receiving window checking rather than accepting. **A relayed claim is a hypothesis.**

---

## ⑥b COORDINATION STATE — what a successor session needs `[live, keep current]`

⭐ **Read this before touching any window.** The coordinating session holds no authority the windows
don't; it holds the *boundary*, and the boundary is the only thing here that lives nowhere else.

**AUTHORITY — a window may do these without asking:** build · commit on its own branch · deploy to
**lab** and **qa** · read-only probes of lab/qa/`paul` · plan and register writes in its own lane.

⛔ **THESE WAIT FOR PAUL, no exceptions:**
| gate | why |
|---|---|
| `git push origin main` | Mom's frozen production, 681/22 divergent. Never, for any reason |
| **sending any invite** | outbound, and it IS the milestone |
| deploy to **`home`** | Mom's estate, her record. `paul` is authorized; `home` is not |
| **`POST /api/estate` (B3)** | bound to the grant-key ruling; opens on his word, not because a queue advanced |
| any new irreversible act or live-data migration | the condo placement fix was authorized; a *new* one is not |

**ONE WRITER PER FILE.** `tate-tracker-ec` → `worker/worker.js` **sole writer**, credential/account
path, `publish-digest.py`, `falsifier-tenancy.py`. `testing-arch-e2` → the walk harness
(`journey-*.py`, `release-gate.py`, `synthetic-identity.py`, `walk-*.py`, `.decisions/fernwood-15..22`).
`onboarding-ask-b3` → `onboarding/index.html`. `backlog-rat-3a` → its proposal only, applies nothing.
**Cross-lane requests route through the coordinator; no window reaches into another's files.**

⚠️ **THE STANDING HAZARD, measured today: SIX relayed claims failed verification, three of them the
coordinator's.** Every one was caught by the *receiving* window measuring rather than accepting. The
worst — *"no walk has ever entered J3"* — was relayed three times and verified zero. ⭐ **A relayed
claim is a hypothesis. Label it or measure it; never pass it on as fact.**

⚠️ **And two instruments the coordinator built were themselves wrong** — a watchdog that watched two
branches of four (so the one quiet window was invisible), and a milestone clause grepping a flag name
that survives in the comments explaining its deletion. **Matching the string rather than the thing.**

**WHAT A STALL LOOKS LIKE, and the first question to ask:** a closed window and a window blocked on a
permission prompt are indistinguishable from outside. Ask Paul *"did you close it?"* first, not last.

## ⑥c THE LIVE BOARD — `2026-09-10 ~4:45 PM ET`, coordinator `tate-tracker-af` `[live, keep current]`

⭐ **Six lanes running. This table is the one-writer register; ⑥ and ⑥b are the rules, this is the state.**

| lane | owns | state |
|---|---|---|
| **`tate-tracker-ec`** | `worker/worker.js` · `publish-digest.py` · `grant-mint.py` · `grant-route-backfill.py` · `falsifier-tenancy.py` · account/credential path | **parked, clean, holding.** Awaiting the B3 design + Paul's word to open B3 |
| **`onboarding-ask-b3`** | `onboarding/index.html` | **parked at `4439010`** (1 ahead of `cb5e46a`). Copy staged for Paul; three product rulings owed |
| **Lane 3 · walk harness** | `journey-*.py` · `release-gate.py` · `walk-*.py` · `elicitation-lens.py` · `check-canon-scope.py` · `seat-portfolio.py` · `household-fixtures.py` · `.decisions/fernwood-15..22` | **running.** Preparing the `testing-arch`→`main` merge, then J0 |
| **`paulkirschenbauer-b8`** | `.plans/*zones*` · `.engineering/zones-derivability/` — worktree `zones-assess` | **running.** Zones automation ASSESSMENT, design-side only |
| **`paulkirschenbauer-3b`** | `~/.claude/**` only — no Fernwood writes | **running.** Meta-stack: standing up a security seat |
| **B3 design consult** | nothing — advisory | **running.** Founding write-set; premise corrected mid-flight |

🔴 **`viewer.html` HAS NO OWNER.** 380 zone mentions, ~17,900 lines, and it is Mom's live app — the most
collision-prone file in the repo and no lane holds it. **Ask the coordinator before writing it.** This is
a gap, not permission. `onboarding-ask-b3` correctly recorded a divergence into it rather than crossing.

## ⑥d WHAT LANDED SINCE ⑥b — rulings and measurements, cited

**⭐ THE ESTATE'S PLACE IS WRITTEN ONCE AT FOUNDING** `[paul-ruled 2026-09-10]`: *"let's take the most
durable approach and invest now so we don't have to change it later."* Ruled against a cheaper interim.
⛔ **Consequence: A1 (step 1) depends on B3 (step 6)** — see ⑤. And the population splits:
**TWO by migration** (`home`, `paul` — owner-supplied addresses on file) · **THREE by founding**
(`bob` has zero addressed accounts; `nigel`/`aida` have empty namespaces).
⚠️ `qa` holds **174 addressed accounts** — declaring a place there is the election with a human ranking.
It needs an **invented fixture place, marked as such**, never one of the 174.

**⛔ `nigel` AND `aida` SHOULD NOT HAVE ESTATES** `[paul-restated 2026-09-10]`: *"we should not have an
estate for Nigel cause he's not even set up his account. He hasn't even gotten an invite right."*
Correct on the facts — both namespaces empty, both pre-provisioned by hand in `wrangler.toml`
(`c1ae9bb`), neither invited, aida has no person record. **The delete was ruled and is NOT executed** —
it goes to Paul directly, never on a relay. Estate ids are **RETIRED, NOT REUSED**.
⭐ The argument that carries it: those envs are the only way to provision an estate today, so leaving
them lets the beta launch **without the product ever creating one**. The delete protects the test.

**⚠️ `home` READ UNREADABLE** in `tate-tracker-ec`'s last sweep — a wrangler failure, **not** an empty
result. ⛔ Nothing is written to Mom's estate until it re-reads clean. Green-by-absence.

**⭐ THE SHARED WRITE UNIT MUST TAKE A PLACE, NOT FIND ONE** — `tate-tracker-ec`'s caveat, adopted:
roughly `writeEstatePlace(env, estateId, place, declaredBy)`. If the unit *discovers* the place, the
migration caller re-derives the election **inside** the shared function and the bug becomes durable
instead of the fix. **Share the write, never the discovery.** And `<estate>:place` carries its own
provenance — who declared it, when, founding vs migration.

**🔴 `builds` IS A DECLARATION WITH NO READER** — `measured` by `onboarding-ask-b3`: the brief's *"five
tools read `builds`"* is **false**, zero consumers repo-wide; those tools read the module vocabulary it
names. The brief's conclusion was right for the wrong reason. **Exactly the class `CLAUDE.md` rules
against.** Flagged, not fixed — wiring it is a product decision.
Also falsified: *"Mom has already answered the current question"* — `legacy` (`est-3c9f1a`) holds **zero**
onboard-interests records.

**⚠️ THE SECURITY SEAT WAS A BLOCKING PREREQUISITE ON THE AUTH BUILD, AND NOTHING NOTICED IT FIRE.**
Ratified `[paul 2026-09-02]` — *"queue it, stand up before auth work"* — recorded in
`~/.claude/agents/backlog.md` against step 6 of `fernwood-private/.plans/2026-09-02-data-model-design.md`.
**Auth has since shipped**; Mom's account was created today; `security` appears **zero** times in this
file and in `WORK-QUEUE.md`; three 🔴 cross-record incidents landed today. ⛔ **Not a stop and not the
coordinator's to rule** — but if READY-TO-INVITE means real people other than Mom get credentials, the
prerequisite Paul set for that build is still open, and `PRIVACY-POSTURE.md`'s four gaps are unowned.
**Surfaced before the invite rather than after.** *(Raised by `paulkirschenbauer-3b`; the fifth instance
of a capability the loop cannot reach by running its own procedure.)*

**⚠️ RELAYED CLAIMS THAT FAILED VERIFICATION TODAY: EIGHT.** Three of the coordinator's; **three from
one brief**. Every one caught by the *receiving* lane measuring rather than accepting.
⭐ **The mechanical form of the rule, which is the checkable one** (`onboarding-ask-b3`'s own
sharpening — the abstract version is not testable): **verify a reversibility promise against the actual
route back before writing it.** *"You can change it any time"* had already shipped and been removed
because the gate-1 walker was promised it and could find no route back. A checklist would have restored
a measured defect.
⭐ **And: GREP, THEN READ THE LINE.** A count locates; it does not establish.

**Credit correction:** the coined-phrase catch (`Household systems` — Mom's own words, which must not be
"improved") was **`onboarding-ask-82`'s**, verified by `b3`. That window has closed and cannot claim it.
⚠️ Its `.plans/2026-09-10-interests-reframe-VERIFY-82.md` is **uncommitted and orphaned** in the
`onboarding-ask` worktree — it belongs to nobody and needs a disposition.

## ⑥e OPEN PROPOSAL — a standing BACKLOG REGISTRAR seat `[paul-raised 2026-09-10]`

> *"a backlog rationalization and maintenance session… a standing expert that's helping keep track of
> everything and that they can all forward their updates to in questions and so on and help identify how
> we can package work together."*

**Not yet designed, not yet staffed.** Recorded here so it is not lost. The distinction it must hold:
**the coordinator holds the BOUNDARY** (who writes what, what is gated, concurrency); a registrar would
hold the **REGISTER** (what work exists, what is decided, how it packages). Different jobs; both real.
⚠️ It wants a **persistent addressable lane**, not a subagent — lanes forward to it, so it must outlive a
task. ⛔ `practice-steward` rules on METHOD and explicitly **does not prioritize**, so *"package work
together"* is outside it as chartered.
**The debt it would inherit, measured:** `BACKLOG.md` at **4,327 lines** written by two loops · **29
orphaned plans** repo-wide · a committed **rationalization PROPOSAL Paul has not read** (on `backlog-rat`;
its own §7.2 is stale) · `check-backlog-drift.py` exists but **does not fire a lap** by design.

## ⑦ OPEN — Paul's, not scheduled

- **The Grant Park Condo's return to production.** Precondition named (`POST /api/estate` + call-site
  conversion); **nothing schedules it.** Recommend attaching it to B3 as its acceptance test.
- **No path exists to change a person's access level**, and a locked-out person is invisible to the
  record `[paul-stated: backlog it]`. Under person-scoping, an account with no grants is
  indistinguishable from a stranger. Evidence: scope doc §4.4.
- **Lap 5** — candidate `8d17e4e`, now far behind HEAD, gate ① 0/4, evidence per-sha by design. Either
  nominate a fresh candidate or close it; `fernwood-16` makes it evaluable again.
- Scope doc §9 residue: Q2 Angel's consent (narrow first, then author) · Q6 Guru-at-first-light
  **now ruled by ②**.

---

## Files touched
None by this document. It is a pointer.

## Falsifier
If a window can state today's plan and the order of work **without reading this file**, it is
redundant and should be deleted. If two windows give different answers to *"what gates the beta?"*,
it has failed and needs to be shorter, not longer.

## QA
`git -C ~/Developer/Tate-Tracker log --oneline -15` · `grep -c canonFor worker/worker.js` (0 until A2)
· `python3 tools/publish-digest.py --check` · `ls .decisions/ | wc -l` (22)
