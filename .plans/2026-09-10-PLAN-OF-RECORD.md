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
| **Lane 3 · walk harness** | `journey-*.py` · `release-gate.py` · `walk-*.py` · `elicitation-lens.py` · `check-canon-scope.py` · `seat-portfolio.py` · `household-fixtures.py` · `.decisions/fernwood-15..22` | ✅ **merge LANDED** (`6b0785a`, 9/9 selftests). Now: QA deployed, gate ① diagnosis, J0 |
| **`paulkirschenbauer-b8`** | `.plans/*zones*` · `.engineering/zones-derivability/` — worktree `zones-assess` | **running.** Zones automation ASSESSMENT, design-side only |
| **`paulkirschenbauer-3b`** | `~/.claude/**` only — no Fernwood writes | **running.** Meta-stack: standing up a security seat |
| **B3 design consult** | nothing — advisory | ✅ **delivered.** Founding write-set; premise corrected mid-flight |
| **Backlog registrar** | ⭐ proposed **SOLE WRITER of `BACKLOG.md`, as SCRIBE not author** | ✅ first report delivered; **authorised to write** |

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

## ⑥f 🔴 THE INSTRUMENT WAS LYING, AND THE CALM AND THE ALARM WERE SWAPPED — `2026-09-10 ~5:10 PM`

**`publish-digest.py`'s `household_property()` wrapped its `kv_get` in `except Exception: return None`.**
So a wrangler failure and a missing key were indistinguishable, and `--check` printed
*"no estate-level place record — **Correct, not a fault**"* **with the network down.** The outer `except`
in `main()` that prints `⛔ UNREADABLE` was dead code for that path; the inner swallow won.

⭐⭐ **THE INVERSION, and it is the lesson:** the six *"Correct, not a fault"* lines were the readings that
**could not be trusted**, and the one `home` **UNREADABLE** was the reading that was **TRUE** — it raised.
Exactly backwards from how it looked to every reader, the coordinator included. **Green-by-absence with
the calm and the alarm swapped.** A tool that fails loud on one estate and falsely calm on six teaches
its reader to worry about the wrong one.

✅ **Fixed and proven by mutation** (`tate-tracker-ec`, own file): the discriminator is the message —
wrangler reports a missing key as **404**; anything else is a failure to *look*, **and a failure to look
is not a fact about the world.** Four cases proven: 404 → absent · no network → raises · bad credentials
→ raises · wrangler missing → raises.

⛔ **WHAT THIS DOES AND DOES NOT CHANGE.** A1-depends-on-B3 **STANDS** — it was carried by the **grep**
(`:place` occurs in one file as a `kv_get` plus two message strings; nothing writes it), which is
independent of the tool. ✅ **RE-RUN LANDED — the first honest seven-estate reading this project has had.** All six raised a
**clean 404**, which under the fixed discriminator means *genuinely absent*, not *could not look*.
`fernwood` builds from strict repo-root canon, which is not a place record. **So the six-red conclusion
was right, and is now supported by the tool rather than only by the grep.**
⚠️ **And `home` no longer reads UNREADABLE — it 404s cleanly. That was transient**, which *sharpens* the
inversion rather than softening it: at the moment it was reported, `home` was the one estate whose
reading was **honest**, and it was honest about a **network failure**, not about Mom's estate.
⭐ **The reading was true and what was inferred from it was not.** Two different failures, and only the
second one was ours.

⭐ **The generalizable form, and note whose it is:** it was caught in that lane's own file **an hour after
that lane flagged the identical shape in three other tools.** The honest version of the day's rule, not
the flattering one — *a control can be entirely correct and still not cover the thing you rely on it for*
applies hardest to the control you just built.

**⭐ ONE ROUTE, TWO VERBS — one-function-two-callers is WITHDRAWN by its own proposer.** Founding runs in
`worker.js` (JS, in a request); any migration runs in Python on a laptop. One function cannot span those
runtimes, and `derive-property.py` already ruled this way for the geocoder — *"one SERVICE, two readers."*
So `POST /api/estate` carries **`found`** and **`adopt`**; the migration is an HTTP **client** of founding,
never a second implementation. ⛔ **Share the endpoint, not the function.**

**⛔ AND THE BINDING CONDITION ON THE INLINE COMPOSER, adopted from `tate-tracker-ec`:** composing the
digest in the Worker re-implements a place-facts derivation that already exists in selftested Python —
**two writers of one fact, the shape three of today's five defects had.** `measured`: an all-absent
instance composes to **1,780 bytes / 345 core tokens**, all 13 domains correctly omitted — so it is the
small end of plausible, **not** ~30 lines. Therefore `publish-digest.py --check` as drift-lint is **not
bookkeeping — it is the only thing that would catch the two implementations diverging, and it must
compare the DERIVED output FIELD BY FIELD, never as a blob.** Two implementations agreeing on
byte-length and disagreeing on `countyFips` is exactly the failure a coarse comparison survives — and
`countyFips` is a tier-1 field that `paulkirschenbauer-b8`'s parcel step keys on, so a coarse lint would
break a lane that does not own it.

**⛔ TWO RULINGS ARE PAUL'S AND BOTH ARE OPEN — no lane may build past them:**
1. 🔴 **The `X-Estate` collision.** ⑤ lists it *"deferred, ruled not-now"*; `SCOPE` §2.4's fallback is
   *absent header + several grants → **400**, never a guess.* **The moment anyone holds two grants,
   every request they make 400s.** Both rulings cannot stand once B3 ships. Recommendation on the table:
   B3 **refuses a second estate per person by a named error** until `X-Estate` lands — a visible refusal
   beats an unpredicted 400.
2. **B3's scope GROWTH** — Q6 wants Guru at first light, which puts the digest compose inside the Worker.
   He has not seen that.
⛔ **And the acceptance test is NOT the condo.** The condo is Paul's **second** estate, so it either trips
the refusal or forces `X-Estate` off the deferred list; it is an irreversible cross-namespace copy on
production; and it is `adopt`, so **it cannot exercise the one thing the milestone exists to prove — the
product creating an estate.** Gate on **J0 walked twice on lab by two synthetic seats** instead.

**B3 STATUS: `found` verb building ON LAB ONLY.** ⛔ `adopt`, the second-estate refusal, the inline
composer, production, `home`, the condo and the nigel/aida deletion all remain closed. **The deletion
goes to Paul directly, never on a relay.**

> ### ⛔⛔ PAUL: THIS ONE NEEDS YOUR EXPLICIT CONFIRMATION — IT IS AN INTERPRETATION, NOT YOUR WORD
>
> Every standing instruction says **B3 opens on Paul's word specifically**, *"not because a queue
> advanced."* What opened it was the **coordinator reading** *"go ahead and get them through G1"* as
> covering it, on the ground that G1 cannot complete without founding through the product.
>
> ⭐ **`tate-tracker-ec` flagged this rather than taking it**, and it is right to: *"it is an
> interpretation, not his word on B3, and I'd rather say so plainly than have it become 'the build
> started because a queue rolled forward' — which is the exact failure mode we've both been guarding
> against all day."* **That is the guardrail working on the coordinator, which is what it is for.**
>
> **The exposure is bounded and stated:** lab only, nothing deployed beyond lab, all reversible, behind
> a falsifier. **If Paul meant something narrower it costs one revert.** ⛔ It must not ride silently.

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

**✅ `qa/est-qa0001` READING DARK IS INTENTIONAL — question closed.** `tate-tracker-ec` deleted
`est-qa0001:digest` deliberately: it was the record composed by the **election** bug and it held **Paul's
real home address** (`Grant Park Condo`, 33.7275/-84.3661), because his live accounts sit in that test
estate beside 174 synthetic ones. QA's Guru was answering *"clear skies over Mead Street"* from it.
Removing it restored the honest `canon-not-this-estate`. **Nothing republished or moved it.** ⚠️ The
remaining question — *why his home address is in a QA estate at all* — is one of Paul's four in ⑦.

## ⑥g 🔴 A `viewer.html` TRAP, IN THE FILE THAT HAS NO OWNER — `2026-09-10 ~5:30 PM`

**Found by `onboarding-ask-b3`; recorded here because `viewer.html` has no lane and a finding about an
unowned file has nowhere else to live.** Full change-set: `.plans/2026-09-10-interests-reframe-RULING-COSTS.md`
on `onboarding-ask` @ `f27634e`.

⛔ **RENAMING THE INTEREST LABELS IS NOT A FIND-AND-REPLACE.** `byLabel` (`viewer.html:18412`) is **built
from the five labels being renamed**, and `:18408`'s own comment says it is the **only resolver for
records stored before ids existed**. Rename them and a stored `{label:"Gardening"}` resolves to `id
null`, which then:
1. drops out of `READER_RANKING` via `.filter(Boolean)` — the pick vanishes from card ordering (`:18433`),
   the top-card highlight (`:18564`) and the ask-next exclusion (`:18517`), **so the app re-offers a
   module the person already ranked**; and
2. fails the idea-card guard at `:18475` — **so a BUILT module renders as an unbuilt "idea card"**.

⭐ **On the surface whose whole job is showing someone we heard them.** Third instance today of the same
class this lane keeps catching.

⚠️ **And it is wider than one browser:** `onboarding:1195` and `estate:529` both hydrate the ranking from
the server's `d.ranked`, and `worker.js:3877` stores whatever the client sent — so a pre-id **account**
record propagates old labels to **every device that person signs in on. Not self-healing.**

✅ **Fix is ~6 lines** (a legacy alias table merged into `byLabel`) and **must ship in the SAME commit as
any rename.** ⛔ It is **permanent, not a migration step** — a record written under the old vocabulary can
be read at any future point — so it needs a comment saying so, or the next tidy-up deletes it.
⛔ `estate/index.html:427` replays the stored label verbatim and **must NOT change**: it repeats back what
the person was actually shown, which stays correct after a rename.

**⭐ AND THE DECOMPOSITION THAT MAKES PAUL'S RULING CHEAP — the three questions are NOT one bundle:**

| ships alone, waits on nothing | needs the product call |
|---|---|
| the address **NOT-use** clause (different screen, different flow) · the four **contract lines** (chrome above the list, reads identically over either vocabulary) · the **reframed question wording** (true over either list) | **"Growing things" vs "Gardening"** — it widens gardening to a windowsill and quietly absorbs the Houseplants record that `feedback-dispositions.json:102` ruled a twelfth interest, **not** a module request |

⭐ **So the ask is not "approve this change." It is: ship the two contract fixes now, decide about
"Growing things" whenever.** Both fixes close a **ruled** contract gap. **Branch B costs zero
`viewer.html` changes.**

⚠️ **A self-correction from that lane, worth keeping because it runs the other way:** its shipped
reversibility line is **understated**, not wrong — `estate/index.html:431` offers *"Change the order ›"*,
so a post-hoc route does exist and *"or tell me later from your place"* would be TRUE today (unlike
*"change it any time"*, which was not). Offered as an option, **not applied** — more words on the screen
already carrying the most reading is a content-steward call.

## ⑥h THE BOARD WAS STALE AND THE REGISTRAR CAUGHT IT — `2026-09-10 ~5:45 PM`

⭐ **⑥c is a live document and it went stale in FOUR HOURS, in the over-reporting direction** — exactly
the direction `CLAUDE.md` says these documents fail in. The registrar measured it on its first pass.
**The coordinator's own board is not exempt from the rule the coordinator enforces.**

⭐⭐ **AND ITS MEASUREMENT WAS RIGHT WHILE ITS INFERENCE WAS WRONG — the third instance today.**
It measured `main..testing-arch` = 0 and `testing-arch..main` = 0 at 16:25 and concluded *"no merge
commit; Lane 3 has been landing on `main` directly."* ⛔ **The merge commit `6b0785a` exists and is in
`main`'s history.** What actually happened: the merge landed, then the `testing-arch` **branch pointer
was advanced** to follow `main`, so at that instant the two were the same commit. **The reading was true
and what was inferred from it was not** — the identical shape as `home`-UNREADABLE and as
*"A2 is partial."* ⭐ **Three different lanes, one failure mode, one day. Grep, then read the line;
measure, then check what else explains it.**

✅ **`publish-digest.py`'s 16:25 commit is NOT a one-writer violation** — it is `tate-tracker-ec`
committing the swallow fix in its own file, at the coordinator's request. The registrar was right to
**route rather than arbitrate**.

**RULINGS ON THE REGISTRAR'S THREE QUESTIONS:**
1. ✅ **SCRIBE, not author — CONFIRMED.** It transcribes a lane's forwarded row **verbatim, attributed to
   that lane and its sha**; it flags and proposes separately in its own marked voice. ⭐ **Every status is
   then attributable to the lane that measured it** — strictly stronger than today, where a status is
   attributable to whichever session last had the file open.
   ⚠️ **Unresolved and real:** `BACKLOG.md` is written by two loops (mom + fleet). A registrar is a
   **third** writer unless those loops forward too. **One door, or it is not a door.**
2. ✅ **ONE packet to Paul**, not several — its §2, §3 and §4 share one root cause.
3. ✅ **Authorised to write.**

**⭐ ITS THREE HIGHEST-LEVERAGE FINDINGS, all of which outrank the count they came from:**
- 🔴 **The register has learned to explain away its own alarm.** Three plans say *in their own headers*
  that *"the orphan flag is expected and is not a defect to repair."* `check-backlog-ready.py:398-402` is
  this repo's own ruling that **a control red on every signal from day one is one nobody reads** — and 10
  permanently-red rows are training exactly that. **Proposal: `row: process` becomes a third state
  (`awaiting-ruling`), not an orphan.**
- ⭐ **"29 orphaned plans" is the wrong problem statement.** The tool says **28**, and **18 declare a
  `row:` in their own header** — `POINTER_PAT` is **one-directional**, so a plan that correctly names its
  row is still "orphaned" because the BACKLOG side never got the back-pointer. Real populations: **4**
  need one back-pointer line each (**one write, not four items — the cheapest closable thing on the
  board**) · **4** need a row minted · **10** need a Paul ruling.
- ⭐⭐ **THE HIGHEST-LEVERAGE SINGLE RULING ON THE REGISTER, and it is Paul's:** *is a `-PROPOSAL` a
  **DOCUMENT** or an **ITEM**?* Ruling it once discharges **10 orphans, most of the 22-suffix ambiguity,
  and the expected-orphan habit** together.

**⛔ CADENCE — DO NOT BUILD A SECOND DOOR.** `cycle/requests.jsonl` **already exists** (52 lines, readers
in `fleet_probe.py` and `check-public-build.py`). Its two known defects — Track-B-scoped, and *"nothing
sweeps that door on a cadence"* — are **exactly what a registrar fixes**.
⭐ **The trigger is the COMMIT, not a clock** — a cadence in hours is a thing to remember; a cadence in
commits fires when there is something to say. ⭐ **`row: none` is legal and is the highest-value line in
the system**: *"I built X and it has no row"* is precisely what `onboarding-ask-b3` reported and nothing
captured. ⭐ **Pilot the cheapest form first — a `Register:` commit trailer**, swept with `git log --grep`.
**A discipline that needs a second tool open is the one nobody follows.**

**⚠️ PRODUCT-STEWARD TRIAL — the verdict is that it cannot settle itself.** First falsifier not tripped
(redundancy 49% vs 80%); **second IS tripped** (20 questions opened vs 19 carried — *"a bottleneck
wearing a helper's name"*). Both rounds **confounded**. Its settling condition needs a **clean** round,
which requires the unread rationalization applied **and** walk reports written — **neither is the
steward's to produce.** ⛔ **Renewing for a round that cannot settle it is how a trial becomes
permanent.** Recommend: renew **conditional on one clean round being scheduled**; if the reports are
unwritten again, **kill it** rather than record a third confounded row.
⚠️ And two of its three triggers are **majority-UNCHECKABLE by their own predicate** — T1 sees 20 of 29
ruling lines, T3 sees 2 of 10 plans. **Those are floors reported as counts.**

**⚠️ TWO LANES HAVE PRODUCED NOTHING DURABLE, and the shape is the same:** `zones-assess` is **0 ahead,
0 uncommitted** — that lane's whole output lives only in its session context. And
`.plans/2026-09-10-interests-reframe-VERIFY-82.md` is still uncommitted and orphaned in the
`onboarding-ask` worktree, belonging to a window that has closed.
