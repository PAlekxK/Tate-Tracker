# Backlog rationalization against the 2026-09-10 rulings — what they CLOSE, what they INVALIDATE

- row: `BACKLOG.md` § ▶️ NEXT (the rationalization trail; this file is the third run, after 07-29 and 09-02)
- objective: O5
- class: engine · declared
- class-note: the backlog's reading order is shared machinery every estate's work is planned through, but nothing renders from it — a divergence here is a legibility cost, not a defect
- kind: process
- stage: draft
- seats: practice-steward → **waived with a reason**: this is a reading-order and staleness proposal over an existing record, and the two precedent runs (`.plans/2026-07-29-rationalized-backlog-PROPOSAL.md`, `.plans/2026-09-02-rationalization-PROPOSAL.md`) both ran without one · engineering-partner → waived: no code is proposed, and every engine claim below is cited to a file:line read at `fdece26` · ux-expert · content-steward · ai-advisor → waived: nothing here reaches a person and no authored content is drafted
- depends-on: `.plans/2026-09-10-PLAN-OF-RECORD.md`
- depends-on: `.plans/2026-09-10-account-estate-model-SCOPE.md`
- depends-on: `.plans/2026-09-10-WORK-QUEUE.md`
- depends-on: `.plans/2026-09-10-testing-architecture-PLAN.md`
- ready: **agent-proposed 2026-09-10 — Paul rules.** ⛔ Nothing here is applied.
- commissioned: `~/.claude/handoff/brief-backlog-rationalization.md`, Paul 2026-09-10
- stage-note: 2026-09-10 — written **read-only** in the `backlog-rat` worktree at `fdece26`, while `tate-tracker-ec` works `worker/worker.js` in the main tree (measured: `property.json`, `worker/digest.json`, `worker/worker.js` all modified-uncommitted there). No file outside this one was written. No network call, no deploy, no tool edited.

> ⛔ **PROPOSE, DON'T APPLY.** Every move below is a proposal for Paul. Nothing is applied — the repo's
> own standing rule for rationalizations (`BACKLOG.md:20-34`), honoured by both prior runs.

> ⛔ **I DO NOT OWN THE RULING REGISTER.** `tate-tracker-ec` is writing today's rulings into
> `BACKLOG.md` § 📜. ⚠️ `measured` at `fdece26`: **`BACKLOG.md` contains zero occurrences of the string
> `2026-09-10`**, and its last commit is `eafcdfe` (2026-09-08). So at the moment this was written the
> register does not yet carry today. Everything below is written to **compose with** that write, not to
> race it: §1 and §2 name rows to change, never register text to author.

---

# 0 · WHY NOW, WHEN THE DETECTOR SAYS RESTED — and it should say so on the board

`measured 2026-09-10`: `python3 tools/check-backlog-drift.py` →

```
📋 Backlog rationalization — rested. Last 2026-09-08 (2d) · 10 sections above the tracks
   · ranked list 186 lines below its head.
```

**All three signals are green and all three are honest.** The detector measures *structural* drift —
head-to-list distance, section accretion, days since the last run. It is right that nothing has
accreted since 09-08.

⛔ **Today's drift is SEMANTIC and the detector is blind to it by construction.** Thirteen rulings, a
new goal, a readiness bar, two holds, two kills and a ruled model landed on 2026-09-10, and **not one
of them moves a line in `BACKLOG.md`.** They change what existing lines *mean*. A row can be fully
invalidated without growing the file by one byte, and the file's own drift check will read rested
while it happens.

⭐ **THE SAME BLIND SPOT ALREADY PRODUCED A LIVE FAILURE, AND IT IS STILL LIVE AS I WRITE.**
`BACKLOG.md` § FOCUS FREEZE (`:114`, `:121`) states that Mom's arrivals are HELD unread and that the
release condition is Paul's word. `BACKLOG.md` § 📜 THE RULING REGISTER (`:882`) — **741 lines below
it, in the same file** — records *"THE HOLD ON MOM'S FEEDBACK IS LIFTED — FULLY `[paul-stated
2026-09-06]`"*. **Four days. The detector read clean the entire time.** A session read the head block
and relayed it as current, which is the failure mode: the head is what gets read.

### ⭐ RECOMMENDATION F-1 · give `check-backlog-drift.py` a SEMANTIC trigger — as a finding, not a build

**Shape, proposed not designed:** a fourth signal, `rulingsSince` — the count of dated
`[paul-ruled|paul-stated|paul-approved <date>]` stamps in `.plans/`, `.decisions/` and `BACKLOG.md`
itself whose date is newer than the rationalization marker the tool already reads. Above a threshold,
the tool reports **`⚡ rulings landed since the last rationalization`** and names them.

⚠️ **Three constraints that make it a real check rather than a second nag**, each earned by something
this repo already paid for:

1. **It reads EVIDENCE, never a hand-typed line.** Same rule the existing clock runs on
   (`BACKLOG.md`'s `(rationalized <date>)` head marker plus `.plans/` artifacts, newest wins) — *a
   count typed beside a tool that computes the same count* is the CYCLE-SPINE enactment amendment's
   own recorded failure mode.
2. ⛔ **It must NOT fire on every ruling.** The ratified narrowing is *a **load-bearing** ruling that is
   not in the register is not in force* (`BACKLOG.md:760-765`) — **load-bearing = it changes what gets
   built, what may not be done, or what a later reader would otherwise get wrong.** A trigger that
   counts all rulings is red permanently, and this repo has ruled against controls whose alarm never
   clears (`check-backlog-ready.py:398-402`, on exactly this).
3. ⛔ **It flags; it never reorders.** Same as the structural half.

**Threshold: a first cut, not ratified** — suggest ≥5 load-bearing rulings, or ≥1 ruling that KILLS
something. ⭐ **Today's run is its own worked example and its own selftest fixture: 13 rulings + 2 kills
against a green board.** ⚠️ And it inherits the parent's constraint verbatim: **it does not fire a lap**
(`MOM-CYCLE-MAP.md` — *"The loop rests. HER INPUT is what fires it"*); it is a pickup-time trigger
disposed at the gate sweep.

---

# 1 · ⭐⭐ WHAT THE DAY'S RULINGS CLOSE OR INVALIDATE — the highest-value output

**Method.** Every row below was read at `fdece26` and checked against the world, not against its own
checkbox (`~/.claude/CLAUDE.md` § *an unchecked box is not open work*). `measured` = I ran the command
or read the file:line. `inferred` = I reasoned from two cited sources. Nothing here is relayed.

## 1.1 · 🔴 THE HEADLINE — THREE LIVE ARTIFACTS STILL CARRY A PROPOSAL PAUL KILLED TODAY, AND ONE OF THEM IS STEP 1 OF THE MIGRATION

**The ruling** (`.plans/2026-09-10-WORK-QUEUE.md:67`):

> ~~**Delete `nigel` and `aida`**~~ · ⛔ **KILLED 2026-09-10 — DO NOT RE-PROPOSE.** The justification
> (*"namespaces empty, never used"*) was **wrong**… Their namespaces are empty because **they have not
> been invited yet**, not because they are dead.

**`measured` — the killed proposal is still live in three places, two of them written the same day:**

| file:line | what it still says |
|---|---|
| `.plans/2026-09-10-account-estate-model-SCOPE.md:633` | **`M1 · delete nigel + aida — zero keys · ⛔ irreversible, and free`** — **step 1 of the six-step migration table** |
| `.plans/2026-09-10-account-estate-model-SCOPE.md:620` | *"Two of the five are not people yet… **They are not a migration; they are a deletion**, and doing it first is free and proves the direction (C1)."* |
| `.plans/2026-09-10-migration-shape-REASSESS.md:118` | *"**C1 delete `nigel` and `aida`** — zero keys, never used. **Free, and do it first**"* |
| `.plans/2026-09-10-migration-shape-REASSESS.md:148` | *"**Delete `nigel` and `aida` now?** Recommend yes — zero keys, zero risk."* |

⛔ **`account-estate-model-SCOPE.md` is a declared `depends-on:` of `.plans/2026-09-10-PLAN-OF-RECORD.md`.**
So the plan of record points, one hop away, at a migration whose first step is the act Paul killed —
and the kill is recorded **only** in `WORK-QUEUE.md:67` and in `PLAN-OF-RECORD.md` ⑤'s one-line
*"Killed:"*, neither of which the SCOPE doc cites.

⭐ **And the reason the kill matters is not tidiness — it is the ROSTER.** `nigel` and `aida` are two
of the five owners in **G1**. Deleting their estates deletes 40% of the goal's denominator. The exact
stale reading the kill names (*"empty because never used"*) is **still sitting in the document that
scopes the migration**, and it survived because nothing re-read it after the ruling.

**Proposed:** ① the SCOPE doc's §6/§6.1 M1 rows carry a struck-through KILLED line citing
`WORK-QUEUE.md:67` — *recorded visibly rather than deleted*, exactly as the work queue did, so the
stale reading cannot mint the row a third time; ② the same at `REASSESS.md:118` and `:148`; ③ the
migration table renumbers M2→M1 or keeps M1 struck. ⛔ **I have not applied any of these** — those two
files belong to the lanes that wrote them.

## 1.2 · ⭐ CLOSED BY WORK THAT LANDED AFTER THE PLAN OF RECORD WAS WRITTEN — four items reported open that are done

⚠️ **`.plans/2026-09-10-PLAN-OF-RECORD.md` was copied into this worktree from the main tree as
untracked** (the brief said so). `measured`: four of its open items closed in commits timestamped
**14:32–14:46 ET today**, on this branch's own history.

| plan-of-record claim | `measured` at `fdece26` | verdict |
|---|---|---|
| ⑤ **3 · `personFor(request, env)`** — *"Without it Q3's rule 1 and `attributeToPerson` are both **shipped and dormant**"* | `fdece26` — *"personFor: identity and authority are two lookups — and route rows now name their person"*. Its own message: *"this is the resolver they were waiting on"* | ✅ **CLOSED** |
| SCOPE ⑨ Sequence **2 · §5.3's attribution fix** — *"a live data-loss defect on the path Mom is on **today**"* | `455c01e` — *"a person with an account and no household lost the authorship of her own words"* | ✅ **CLOSED** |
| SCOPE ⑨ Sequence **3 · M2/M3** (additive account + route rows) | `2a552f2` — *"Q1: an account belongs to a PERSON, not a household — dual-write, non-breaking"* | ✅ **CLOSED** |
| SCOPE ⑨ Sequence **4 · §3.2's feedback destination rule** | `2b62fb5` — *"Q3: a record about a PERSON travels with her; a record about a PLACE stays"* | ✅ **CLOSED** |
| WORK-QUEUE Lane A **A0** — derive a property from an onboarding address | `3de2d62` — *"A0: derive a household's starting place"* | ✅ **CLOSED** |
| WORK-QUEUE Lane C **C3** — teach `grant-mint.py` to write the router row at mint | `5a84d0a` — *"grant-mint writes the router row at the mint"* | ✅ **CLOSED** |
| SCOPE ⑨ **F1 · `-SCOPE` is graded by nothing** — *"two lines: add `-SCOPE` to `DOC_SUFFIXES`"* | `f590082` — *"the suffix allowlist fails open — 21 ungraded suffixes, not 4"*. `measured`: the tool now **NAMES all 22 ungraded suffixes** including `-SCOPE` rather than allowlisting one | ✅ **CLOSED BY A BETTER FIX** — F1 as written is superseded; the allowlist was the wrong instrument |
| SCOPE ⑨ **F3 · `.decisions/fernwood-14.md` is now stale** | `f590082` — *"and fernwood-14 is ruled"*; the card now carries **⛔ RULED — person-scoped `[paul-ruled 2026-09-10]`** | ⚠️ **HALF-CLOSED — see 2.6** |

⭐ **This is the "unchecked box" rule firing on a four-hour-old document.** The plan of record is
correct about everything it measured and stale about four things that closed *while it was being
read*. **That is not a criticism of the file** — it is the argument for §5's assessment and for F-1
above: a pointer document accrues staleness at the speed of the build, and the build today is running
three windows.

**Proposed:** the plan-of-record's ⑤ becomes a 4-row sequence (A1 · A2 · B0 · durability), with
`personFor` struck and dated, and a line saying which commit closed each — so the next reader does not
re-derive it.

## 1.3 · ⭐ CLOSED BY RULING ② — `SCOPE` §9·Q6, still labelled *"the single highest-leverage question on the board"*

**The ruling** (`PLAN-OF-RECORD.md` ②, `[paul-stated 2026-09-10]`):

> *"Let's set as our long-term goal that Guru is working for all households that launch."*

**`measured` — the question it answers is still open in two files, one of them today's:**

- `.plans/2026-09-10-account-estate-model-SCOPE.md:739` — **`## Q6 · Does Guru have to work at first
  light for a new household?`** … *"⭐ Carried forward… because it is **the single highest-leverage
  question on the board** and it gates §6's long pole. If a household can launch with the deterministic
  app and no model routes, **A5 stops blocking B1** and Nigel and Aida can be invited much sooner."*
- `.plans/2026-09-10-migration-shape-REASSESS.md:143-146` — the same question, same framing, **"⭐ This
  is the single highest-leverage question on the board."**

⛔ **`PLAN-OF-RECORD.md` ⑦ already knows this** — *"Q6 Guru-at-first-light **now ruled by ②**"* — and it
is the only place that says so. Neither cited file was updated.

⚠️ **The ruling goes the harder way, and that is the load-bearing part.** Q6's own text says a *no*
answer would let *"Nigel and Aida be invited much sooner."* Paul answered **yes** (a launching
household has Guru working) **and** held Nigel and Aida. **So the cheap escape hatch both files still
offer is closed**, and A5/A2 stays the long pole — which is precisely why `PLAN-OF-RECORD.md` ⑤ can say
*"A1 + A2 together are the readiness bar."* A reader who finds Q6 open will reach the opposite
conclusion about what gates the beta.

**Proposed:** both Q6 blocks are struck with `✅ RULED 2026-09-10 by the readiness bar` and a pointer.

## 1.4 · 🔴 INVALIDATED — `BACKLOG.md` § C4's ratified **THREE LEVELS** domain shape

`BACKLOG.md:2815` carries, `[paul-stated 2026-09-03]` and stamped into the C4 ruling table:

> ⭐⭐ **REFINED: THREE LEVELS.** The PRODUCT apex (`<product>.place`) · **the FAMILY door
> (`<family>.<product>.place` — the *your homes* greeting and that family's estates; two example
> families: Paul's and Bob's)** · the INSTANCE, chosen behind the family door by grant.

**Three of today's rulings cut against the middle level, and none of them mentions it:**

| ruling | source | consequence for the family door |
|---|---|---|
| **R32 · an estate is a ROW, not a deployment** | `SCOPE` §1.9, `[paul-ruled 2026-09-10]` | a per-family origin is a per-family deployment in everything but name |
| **R33 · ONE production environment** — *"we should just have one production environment"* | `SCOPE` §1.9, `[paul-ruled 2026-09-10]` | there is no second environment for a second family to be |
| **R25 · nothing on the open web** + `SCOPE` ⑦ row 9 | `[paul-ruled 2026-09-10]` | ⛔ *"`myhome-bob.pages.dev` tells a stranger a household exists for someone called Bob. **One origin for everyone names nobody**."* A family subdomain is **public in certificate logs the moment it serves HTTPS** — `BACKLOG.md:2815` says so itself, as a caveat, and R25 turns that caveat into a violation |

⭐ **The C4 row's own words are the argument against it now:** it justifies the family door as *"a
subdomain is ROUTING, never access — the Worker derives every grant from the credential."* Today's
model makes that true **without the subdomain** — `route:<hash> → {personId}` + `grantsFor(personId)`
is the whole chooser, and `X-Estate` is the disambiguator. **The middle level buys nothing the
credential does not already buy, and costs a name in a public log.**

⚠️ **It is not obviously dead — it is unreconciled, and that is the finding.** A family door might
still be wanted as *branding* rather than tenancy. But it is a **ratified `[paul-stated]` design that
today's rulings retire the mechanism for**, and `BACKLOG.md` says nothing. This is the class the
register exists to catch.

**Proposed:** C4's THREE LEVELS block gains a dated ⚠️ rider naming R25 · R32 · R33 and asking the one
question — *does the family door survive as branding, or does it go?* ⛔ **A question, not an answer.**

## 1.5 · 🔴 INVALIDATED — `BACKLOG.md` § 🎟 C9's release condition has ALREADY FIRED, and its ⏸ is wrong

`BACKLOG.md:3168` — C9 · THE INVITE FLOW — carries **⏸ *"Not critical now — raised to be findable, not
to be scheduled."*** Its release condition (`:3204`):

> ⚠️ **RELEASE CONDITION, and it is a fact rather than a date:** (A) is safe **only while Fernwood is
> the only estate with people in it**. It must be re-ruled **before instance 2 activates any person who
> is not Paul's family.**

**`measured`, from `PLAN-OF-RECORD.md` ③ (itself measured today, not asserted):** `est-e6696a` (Mom,
account created 12:24 PM ET) and `est-d93508` (Paul, Grant Park Condo) are **two estates with people
in them**. Bob's invite is out and unspent. **Fernwood is no longer the only estate with people in
it** — the condition's own predicate is false.

⛔ **And R14 changes C9's class outright.** `[paul-ruled 2026-09-10]`: *"in production, I would expect
Mom to have to go through the process of setting up an account, setting up an estate, and then
**inviting me** to the estate to see it."* `SCOPE` ⑦ row 10 states the consequence in one line: the
invite path is ***"Paul's own production access route, not a down-the-road nicety."***

⭐ **So C9 item 2 — *"the owner-facing surface — does not exist"* — is now the only way Paul gets into
Mom's household in production.** A row marked *"not to be scheduled"* is on the path.

**Proposed:** C9's ⏸ is lifted to a dated status line citing R14 and the fired release condition. ⛔
**Its TIER placement is Paul's** — I am recording that the gate opened, not ranking it.

## 1.6 · 🔴 INVALIDATED — `BACKLOG.md` TIER 1 · 19's build instruction, and two of its measurements

`BACKLOG.md:231` (TIER 1 · 19, *A PERSON CANNOT FOUND A SECOND PLACE*) is the closest existing row to
today's model. Three of its claims no longer hold:

| the row says | `measured` at `fdece26` | verdict |
|---|---|---|
| *"`scopeFor(request, env, grant)` … has **ZERO callers**, while `scopeOf(env)` sits at **51 call sites**"* | `grep -c "scopeOf("` → **64** · `grep -c "scopeFor("` → **3** | ⚠️ **STALE, and in the understating direction** — the conversion surface grew 25% while the row sat |
| ⭐ *"**Build ① against Bob's household, not against `home`** — it is the first real case of two estates, three people, one person spanning both"* | **R32** — an estate is a ROW, not a deployment; **R33** — one production environment; `WORK-QUEUE.md §1 B0` — *"finish the `scopeOf(env)` classification… convert **read-only handlers first, writers last**"*, and A2 is proven *"on **lab** with two estates first"* | 🔴 **INVALIDATED.** Bob's household is a separate *deployment*; today's model retires deployment-per-household. **Lab with two estates is the proving ground, and it is already ruled.** ⚠️ Bob's invite is also **unspent** — building against it would gate engine work on an outbound act that is Paul's |
| *"② a **found-a-new-estate flow**, which does not exist even after ①"* | ✅ **now named and bound**: `POST /api/estate` (B3), ⛔ **ruled to ship in the same change as the `grant:<personId>:<estateId>` re-key** (`SCOPE` §2.5, `[paul-ruled 2026-09-10]`) | ✅ **ANSWERED** — the row's open half has a name, an owner and a binding constraint |

⭐ **The row's falsifier survives intact and is worth preserving verbatim** — *"one person, one
credential, two estates, one deployment — write under each and prove neither read sees the other,
**asserting on the RAW KV KEYS**."* That is `falsifier-tenancy.py`'s job and today's rulings sharpen
rather than replace it.

⚠️ **AND A CONTROL IS RETIRED UNDER IT, which the row does not know.** `falsifier-tenancy.py` **C2**
(`tools/falsifier-tenancy.py:189` — *"no request input may make A's credential answer as B"*) is
**retired by name** and replaced with the grant-checked form, ⛔ **in the same change that first reads
`X-Estate`** (`SCOPE` §2.4, ratified with its cost stated). `measured`: `grep -c "X-Estate"
worker/worker.js` → **0**, so nothing reads it yet and C2 still passes honestly today.

## 1.7 · ⚠️ RE-SCOPED BY G1's ⛔ CLAUSE — two READY rows and one ordering

**The clause** (`PLAN-OF-RECORD.md` ①, `[paul-stated 2026-09-10]`):

> ⛔ **Features — plants, vehicles, zones — are out of scope until G1 is met.**

| row | today |
|---|---|
| **TIER 2 · 7** (`BACKLOG.md:248`) — ⭐ **ZONES AS A FEATURE, the epic**, `→ READY · .plans/2026-09-07-zones-PLAN.md`, ten rulings Z-1…Z-10 | 🔴 **named explicitly by the clause.** A READY row with a stamped plan is now behind G1 and **nothing on the row says so** |
| **TIER 2 · 8** (`:249`) — the per-estate capture write path, LEG 0, `→ READY` | ⚠️ **AMBIGUOUS AND IT NEEDS A RULING, not my guess.** It is the co-requisite of row 7 (zones ⇒ out) *and* it is engine capture plumbing G1's *"their record captures what they enter"* clause arguably requires. **Paul's** |
| **TIER 2 · 12** (`:253`) — the per-estate canon store, status field **`after zones`** | 🔴 **the ordering is inverted.** `PLAN-OF-RECORD.md` ⑤ makes **A1 — publish `<estateId>:digest` per estate — step 1 of the whole sequence**, and A1 *is* this row's first consumer. The row waits on a thing that today's sequence puts behind it |
| **TIER 2 · 15** (`:256`) — the model routes are not modular, 60 place literals, status **⛔ unscoped — size before a lap** | ⚠️ **now has a status it does not carry**: `PLAN-OF-RECORD.md` ⑤ — *"Deferred, ruled not-now: … **A4 place literals**"* |

⛔ **I am not re-tiering anything.** Tier is priority and priority is Paul's; these are status facts the
rows do not currently carry.

## 1.8 · ⚠️ THE TWO KILLS ARE RECORDED IN NO RANKED ROW AND NO REGISTER

`PLAN-OF-RECORD.md` ⑤ ends: **`Killed: C4 ENV_NAME → production · deleting nigel/aida.`**

`measured`: `grep -n "ENV_NAME" BACKLOG.md PRODUCT-ENGINE.md` → **zero hits in both.** The `ENV_NAME`
relabel lives in `.plans/2026-09-03-c4-environments-PLAN.md` and in `SCOPE` §6.2, and the kill exists in
exactly one line of one untracked pointer document.

⚠️ **And the kill is narrower than the sentence reads — state it precisely or it will be over-applied.**
`SCOPE` §6.2: *"⛔ **`ENV_NAME`** — a runtime value stamped on every feedback and zone-audio record and
matched against `env-canary`. *'That is a migration, not a rename.'* Recommend **collapse first, rename
last or never**."* Against **R33** — *"one production environment… I think we relabel to production from
home"*. ⭐ **So: the COLLAPSE to one production environment is RULED; the RELABEL of the stored
`ENV_NAME` value is KILLED.** Those are different acts on the same word, and a reader who collapses
them will either orphan `feedback-dispositions.json` (keyed `env|estate|kind|id` — `SCOPE` §6.2's own
warning) or refuse a collapse that was ruled.

**Proposed:** both kills get a register line with that distinction spelled out.

---

# 2 · CONTRADICTIONS IN EITHER DIRECTION

## 2.1 · 🔴 § FOCUS FREEZE — the known collision, plus five more the brief did not name

`BACKLOG.md:74-141` is **68 lines at the top of the reading order**, declared by `:34` to be *"the scope
gate for everything below it."* Every claim below is contradicted by something later in the same file
or by today.

| line | what the head says | contradicted by | gap |
|---|---|---|---|
| `:114` | *"An arrival from Mom during the freeze is **HELD, not read**"* | `:882` — **rule 4, THE HOLD IS LIFTED — FULLY** `[paul-stated 2026-09-06]`; *"Read, disposition and act are all released"* | **768 lines** ✅ *known, brief-flagged* |
| `:121` | *"**Release condition is PAUL'S WORD**, and only that"* | `:882` — the named human act **already happened** | 761 lines |
| `:81` | Track B fleet laps frozen; *"lap 3 is FIRED… and **stays unrun on purpose**"* | `:811` — **rule 2, PARTIAL UNFREEZE — Track B vehicles & equipment**, *"Track B → **WORK: LIFTED** · PUSH: FROZEN"* | 730 lines |
| `:82` | *"`OBJECTIVES.md` **O1 · O2 · O4** rest"* | `:257` — **TIER 2 · 16**, the ask surface, *"**objective: O1**"*, `[paul-ruled 2026-09-08]`, status **🟢 standing** | 175 lines |
| `:78` | freezes *"the decision cards fernwood-1 · 4 · 5 · **6** · 8 · 9 · 11 · 12"* | `:193`, `:194` — **fernwood-5 and fernwood-6 were RETIRED 2026-09-08** | 115 lines |
| `:96` | *"**Plan of record**: `PRODUCT-ENGINE.md` § THE SEQUENCE › *The migration path*"* | `.plans/2026-09-10-PLAN-OF-RECORD.md`, which names itself the plan of record and states a **different sequence** (A1 · A2 · personFor · B0 · durability · B3 · testing) against PRODUCT-ENGINE's **C4 · C5 · C6 · C7 · Guru · vocabulary · onboarding** | **two live plans of record** |
| `:137` | *"**FEATURES HOLD LIFTED** — on QA only"* `[paul-stated 2026-09-04]` | `PLAN-OF-RECORD.md` ① — ⛔ *"**Features … are out of scope until G1 is met**"* `[paul-stated 2026-09-10]` | **the same word, opposite rulings, six days apart, both live** |
| `:135` | *"the held feedback is **poured into that instance** at transfer time"* | `:897` **rule 5** (the map arrives empty) + **R36 · R37** today — ***"Fernwood is re-founded, not migrated"***; *"she knows it's empty and she has to rebuild it"* | nothing is poured in |
| `:139` | *"**the CONDO is the trial estate** for onboarding"* | `PLAN-OF-RECORD.md` ③ — the condo moved to its **own estate** `est-d93508` today; **Mom signed up at `est-e6696a`** at 12:24 PM ET and *"authored 4 feedback records in the 2 minutes after"* | the trial already happened, on a different estate |

⭐ **AND THE SAME BANNER WAS ALREADY REPAIRED ONCE, IN THE OTHER FILE, AND THE FIX DID NOT REACH HERE.**
`PRODUCT-ENGINE.md:118-124`, lane D, 2026-09-07:

> ⚠️ *"This banner said **'this workstream is the ONLY active Fernwood work'** and that has been false
> since 2026-09-04 — reported as 🔴 STALE on 09-04… and **unfixed for three days**, which mattered
> because it was the first sentence a reader met in the plan of record."*

**`BACKLOG.md:74`'s heading is that exact claim, still standing:** *"🧊 FOCUS FREEZE — the instance
rests; **the migration is the only active work**."* ⭐ **The correction was written into the file that
was corrected and never into the file that is read first.** That is the whole argument for §3's move.

## 2.2 · ⚠️ ONE RELAYED CLAIM IN MY OWN BRIEF FAILS VERIFICATION

The brief (`~/.claude/handoff/brief-backlog-rationalization.md:56`) asks me to check whether the freeze
block *"still misdescribes the CHANNEL hold (**lifted 09-06**) and Track B WORK (**lifted 09-05**)."*

- **CHANNEL hold — 09-06: ✅ VERIFIED.** `BACKLOG.md:882`, rule 4, `[paul-stated 2026-09-06]`.
- **Track B WORK — 09-05: 🔴 FAILS.** `measured`: `grep -n "PARTIAL UNFREEZE" BACKLOG.md` → **`:811`,
  `[paul-stated 2026-09-06]`**. `PRODUCT-ENGINE.md:122` independently dates it **2026-09-06**. There is
  **no 09-05 Track B statement anywhere in `BACKLOG.md`.** The nearest 09-05 quote in that block
  (`:815`) is *"this note released the loop, not the deploy"* — about the **release loop**, not Track B.

⭐ **Recording it because the brief's own last line asks for it** — *a relayed claim is a hypothesis;
four failed verification today.* This is the fifth. Both dates were relayed in one sentence; one held
and one did not, which is why the rule is *check each*, not *check the source*.

## 2.3 · ⚠️ § 🗳 DECISION CARDS OPEN says **"11 of 12"** and `.decisions/` holds **22**

`BACKLOG.md:181` heads a twelve-row table. `measured`: `ls .decisions/*.md | wc -l` → **22**. Cards
**13–22** — nine of them minted today (`ab733df`, *"mint the testing plan's eight rulings as decision
cards — it had already stalled once"*) — are reachable from **no row in `BACKLOG.md`**.

⛔ **Two of the ten are live consequences, not paperwork:**
- **`fernwood-16`** (*does gate ① change its unit from `seat` to `(journey, lens)`*) — *"⚡⚡ THIS IS THE
  ONE WITH A LIVE CONSEQUENCE. Lap 5's gate ① has sat **0/4 with no reachable close**."*
  `PLAN-OF-RECORD.md` ⑦ confirms: *"`fernwood-16` makes it evaluable again."*
- **`fernwood-20`** (*the productionalization goal is in NO file*) — ⛔ *"**NOT A TESTING QUESTION.** This
  is a G1 / `OBJECTIVES.md` question… the **third seat** to report that the finish line is written down
  nowhere."* **That card is the origin of §4 below.**

⚠️ **The header's own instruction already forbids what it does** — `:184`: *"**read the count from
there, never from this line**."* The line then states a count. **Proposed:** the count is deleted (not
corrected — a count typed beside the thing that computes it is the failure mode), and the table gains
rows 13–22. ⛔ **`tate-tracker-ec` owns the register; this row is adjacent to it, so I flag rather than
draft.**

## 2.4 · ⚠️ TWO OF TODAY'S OWN ARTIFACTS DISAGREE ABOUT WHETHER `route:` IS RULED

- `SCOPE` §2.3, carried verbatim into `PLAN-OF-RECORD.md` ④: *"credential router · `route:<sha256(token)>`
  → `{personId}` · **the noun `route:` is fixed**; only its value shape moved."*
- `WORK-QUEUE.md:70`, under ⛔ **WHAT I CANNOT CLOSE ALONE**: *"**Ratify the `route:` key noun** — I
  chose it over the plan's `credential:` to avoid a double-booking, and **you have not ruled**. Cheap to
  change now, **expensive after A1**."*

⭐ **And the cheapness window is closing while both lines stand.** `fdece26` shipped *"route rows now
name their person"* — the rows are written; A1 has not run (`measured`: `tools/publish-digest.py` exists,
committed at `74bc7a1`; `grep -c canonFor worker/worker.js` → **0**, so A2 has not started). **Paul's,
and it is one word.**

## 2.5 · ⚠️ `PLAN-OF-RECORD.md` USES "RULED" IN TWO SENSES ON ONE PAGE

④ THE RULED MODEL lists **`X-Estate`**, the **`reader`** capability and the **`via: master|grant`** stamp
as ruled. ⑤ THE SEQUENCE ends: *"**Deferred, ruled not-now:** `X-Estate` · `reader` · `via:` · A4 place
literals · B2 · B4."*

**Both are true** — the *shape* is ruled, the *build* is deferred — and a reader in a hurry will take ④
as a work item. ⛔ **It matters for one of the three:** `X-Estate`'s ruling carries a bound obligation —
`falsifier-tenancy.py` C2 must be retired and replaced **in the same change that first reads the
header**, never after. A deferred build with a same-change control obligation is exactly the thing that
gets half-done. **Proposed:** ④ gains a `build:` column, or ⑤'s line reads *"shape ruled, build
deferred."*

## 2.6 · ⚠️ `.decisions/fernwood-14.md` records the ruling and its **Recommendation** still says the opposite

`SCOPE` §9·F3 flagged the card as stale; `f590082` discharged half of it. `measured` at `fdece26`: the
card carries **⛔ RULED — person-scoped `[paul-ruled 2026-09-10]`** — and eleven lines below, under
**`### Recommendation`**, it still reads:

> **Ship (a), design so (b) is reachable — and decide (b) before `POST /api/estate` ships, not after.**

⭐ **The card also carries the correction that makes this worth fixing rather than tidying** — *"Earlier
the same day I told another session that Paul 'has effectively ruled person-scoped', and that was
**overstated**… It was never a standing ruling and must not be cited as one."* A card that took that
much care over provenance should not leave the superseded recommendation reading as current.

**Proposed:** the Recommendation block is struck and dated, not deleted. `.decisions/` is the operating
layer's intake and a card is a document — ⛔ **never edit status into it**; the strike is a document
edit, which is legal.

## 2.7 · ⚠️ `CLAUDE.md`'s data-model-design citation is dangling — `SCOPE` §9·F2, unfixed

`measured`: `CLAUDE.md:534` cites **`.plans/2026-09-02-data-model-design.md` §7** with no repo. The file
lives in `~/Developer/fernwood-private`. **`BACKLOG.md` cites the same file correctly three times** —
`:2766`, `:2849`, `:3460`, all as `../fernwood-private/.plans/…`. So within one repo the same
load-bearing document is cited two ways and **only the globally-loaded one is broken.**

⚠️ **And the section number is also wrong** — the consent prerequisite is **§2b**, not §7 (§7 is Mom's
door). `SCOPE` §9·F2 records that at least one session hit the dead end and concluded the file did not
exist. **Two lines, and it is `~/.claude`'s owner's, not this repo's.**

## 2.8 · ⚠️ R25 UNPARKS `BACKLOG.md` § C4's REPO-VISIBILITY item — and turns curiosity into a requirement

`BACKLOG.md:2746` — **⏸ REPO VISIBILITY** — `[paul-parked 2026-09-03: "let's not worry about this right
now. **I was curious, though.**"]`. Its own body already contains the finding: *"**GitHub Pages does not
publish from a private repo on a free plan, and a Pages site is world-readable on any plan**."*

**R25, today:** *"ideally everything is private… **You should have to log in**, so that users have
confidence their information is not posted on the web. **That's a clear requirement.**"*

⭐ **`.plans/2026-09-10-PRIVACY-POSTURE.md` measured the gap the same hour and it is the parked item's
own subject:** *"Fernwood's entire record is public, with no login —
`https://palekxk.github.io/Tate-Tracker/viewer.html`, **HTTP 200, 2,062,839 bytes**… It carries the
address, the plants, the zones, the vehicles, the property file."*

⚠️ **The posture doc is careful and I am not overriding it** — *"This is Paul's own record and he
published it deliberately, long before the requirement existed. **It is a decision to revisit, not a
bug to fix quietly.**"* ⛔ **So the proposal is only that the ⏸ comes off and the release condition is
rewritten from *"decide at the C4 step 5 repo split"* to R25.** The decision stays Paul's.

---

# 3 · READING ORDER — ONE move, and an argued case for no second

**Discipline, unchanged from the 09-02 run** (`BACKLOG.md:26-33`): every move is a **MOVE** — no row
deleted, no status changed, each moved section carrying a provenance line. ⛔ **Splitting a section is a
judgment edit, not a move**; the 09-02 run correctly moved four whole rather than splitting them, and I
propose no split.

## ⭐ MOVE 1 — § 🧊 FOCUS FREEZE (`:74–141`, 68 lines) → into § 📜 THE RULING REGISTER, immediately above the 2026-09-06 four-rulings block

**Why it is a move and not an edit.** Every one of its five sub-blocks is a **dated ruling record**
(`[paul-stated 2026-09-03]` · `09-03 9:45 PM` · `09-04 ~10:45 AM` · `09-04 ~11:50 AM` · `09-04
~11:55 AM`). It is *already* a register; it is simply sited 642 lines above the register. **Nothing is
rewritten by moving it** — §2.1's eight contradictions all survive the move and are then adjacent to
the rulings that supersede them, which is where a reader can resolve them.

**Why it must leave the head.** The head region is declared to be *"for pointers"* (`BACKLOG.md:34`,
the rule ratified `[paul-approved 2026-09-08]`). A 68-line block of superseded rulings is the opposite
of a pointer, and it is **the first thing a session reads** — which is how a four-day-stale claim got
relayed as current.

**What replaces it — three lines, a pointer, not a second gate:**

```markdown
## 🧭 THE SCOPE GATE → `OBJECTIVES.md` § G1
The current goal and what it puts out of scope live in `OBJECTIVES.md` (§4 of this proposal).
Freeze history — the 09-03/09-04 rulings and their supersessions — moved to § 📜 THE RULING
REGISTER on 2026-09-10; read it there, not here.
```

**Provenance line the moved section carries** (matching the 09-02 run's own wording at `:477`, `:558`):

> *(Moved here from the pointer-head region at the 2026-09-10 rationalization — reading order only; no
> row deleted, no status changed. Proposal: `.plans/2026-09-10-rationalization-PROPOSAL.md` §3 · MOVE 1.)*

⚠️ **One dependent pointer follows it:** `BACKLOG.md:3958` (in § 🌱 SEEDS) reads *"🧊 **FOCUS FREEZE
APPLIES.** 21 of the 27 sit under O1 · O2 · O4, which rest."* It must be re-pointed **and** re-checked
against §2.1 row 4 — *O1 does not rest* (TIER 2 · 16 is `objective: O1` and 🟢 standing). That is a
one-line edit riding with the move.

## ⛔ NO SECOND MOVE — and the reason is the "everything is changeable" caveat

Two candidates were considered and both are **declined**:

| candidate | why not |
|---|---|
| Promote § 📜 THE RULING REGISTER (`:716`) above the four lenses and the two THEMES | The reading order was **ratified two days ago** `[paul-approved 2026-09-08]` after R1 moved 491 lines. `~/.claude/CLAUDE.md`'s ratified caveat: a change must be **journey-aware** — *"we generally wanna change things in a way that makes sense… so the app oscillates and she can never learn it."* ⭐ **Reversing a two-day-old ratified order on one lap's evidence is the oscillation, not the fix.** MOVE 1 reduces the head by 68 lines without touching the ratified sequence of what remains |
| Re-tier TIER 1 · 19 / 19b / 19c / 20 out of *FIX NOW* (whose definition is *"Nothing blocks these. All agent-drivable"* — false of all four: 19 is *"journey first"*, 19c is *"colour precedence is Paul's"*, 20 is *"then Paul rules what survives"*) | ⛔ **A re-tier is a STATUS CHANGE**, which the rationalization discipline forbids outright. Recorded here as an observation for Paul; not proposed as a move |

---

# 4 · WHERE G1 LIVES — `OBJECTIVES.md`, as a BAND above the table, not as a sixth row

**Recommendation: `OBJECTIVES.md`.** ⭐ **It has held at 15 lines for a week while `BACKLOG.md` grew to
4,327** — the brief's own reason, and it survives checking: `measured`, five objectives, one table, one
contract paragraph.

⛔ **But NOT as `O6`, and the reason is the file's own contract.** `OBJECTIVES.md:3-4`: *"A backlog item
that claims READY **cites exactly one of these by id**."* G1 is not a thing a row cites — **it is a gate
over every row**, and half its content (personalization, the five-owner roster) is delivered *through*
O3 and O1. Minting it as O6 creates a sixth id that competes with O3 for the same rows and gives
`check-backlog-ready.py` a second legal answer to *"which objective is this?"* — a second grouping axis
competing with the first, which `.plans/2026-09-07-epic-tracking-DESIGN.md` §1.4 already forbids by name
(*"two registers each reading current, this corpus's most-repeated register failure"*).

**Proposed shape — a band ABOVE the table, ~9 lines, ids untouched:**

```markdown
## ⛔ THE CURRENT GOAL — G1 `[paul-stated 2026-09-10]`

> **G1 — Five owners, each with a working, personalized household.** `paul · mom · bob · aida · nigel`
> are each a **user and an owner**. For each: they hold an owner grant; they signed up through the link
> path; **their household is centered on their own address**; their record captures what they enter;
> and their feedback reaches a loop that reads it. Across all five: **the user journeys are documented,
> and one testing procedure walks them.**
>
> ⛔ **Features — plants, vehicles, zones — are out of scope until G1 is met.**

G1 is a **gate over the objectives below, not a sixth objective** — it draws on **O3** (the engine
transfers), **O1 · O2** (personalization is inside it, `[paul-ruled]`) and **O5** (one testing
procedure). ⛔ **A row still cites exactly one `O*` id.** Readiness bar and holds:
`.plans/2026-09-10-PLAN-OF-RECORD.md` ②. Roster question: `.decisions/fernwood-20.md`.
```

## What it displaces — and something real does

**In `OBJECTIVES.md`: nothing.** No id changes, no row is struck, the contract paragraph is untouched.
9 lines onto 15.

⛔ **In `BACKLOG.md`: it displaces § FOCUS FREEZE as the scope gate**, and that is the point rather than
a side effect. Today **two blocks both claim to gate scope and they say opposite things** (§2.1, last
row: *"FEATURES HOLD LIFTED — on QA only"* vs ⛔ *"Features … are out of scope until G1 is met"*). Two
scope gates disagreeing is worse than either alone. **MOVE 1 and this band are one change**: the gate
becomes G1, and the freeze becomes history filed where history goes.

⚠️ **THE ROSTER IS NOT MINE TO SETTLE AND I AM NOT SETTLING IT.** `.decisions/fernwood-20.md` puts the
same question to Paul — *five-owners-including-paul | four-owners | leave-it-spoken* — and
`WORK-QUEUE.md` §2b already recorded its own correction from four to five in his words (*"my user
account, like Mom, Bob, Aida, Nigel, are all users and owners"*). ⭐ **The wording above is the
five-owner form because that is what Paul said**; if he rules otherwise on the card, one line changes.
⛔ **Ratifying the row itself is his** — the plan of record says so on its own face.

---

# 5 · DOES `.plans/2026-09-10-PLAN-OF-RECORD.md` EARN ITS PLACE? — ✅ YES, and its own falsifier has already tripped once

**Its falsifier, in its own words:**

> If a window can state today's plan and the order of work **without reading this file**, it is
> redundant. If two windows give different answers to *"what gates the beta?"*, it has failed and needs
> to be shorter, not longer.

## Clause 1 — redundancy: ✅ **PASSES. It carries four things no other file holds.**

`measured` against every candidate source:

| what only this file holds | nearest alternative | verdict |
|---|---|---|
| **① G1**, stated and stamped | `.decisions/fernwood-20.md` asks the *question*; `WORK-QUEUE.md` §2b corrects the roster. **`grep` for the goal returns zero across `OBJECTIVES.md`, `BACKLOG.md`, `PRODUCT-ENGINE.md`** | ⭐ unique |
| **② the readiness bar + the Aida/Nigel hold** | nowhere else at all | ⭐ unique |
| **③ where the five actually stand**, measured, with 🔴 *"Zero of five come up whole today"* | `WORK-QUEUE.md` §2b has the roster table; it does **not** carry the digest finding | ⭐ unique |
| **⑥ window ownership** — one writer per file | nowhere else. ⛔ **This is what stopped three windows colliding in `worker.js` today** | ⭐ unique |

⚠️ **And the sequence is NOT redundant either, because the two candidate sources disagree with each
other:** `WORK-QUEUE.md` §3 says *"**A0 → A1 → B0**"*; `PLAN-OF-RECORD.md` ⑤ starts at **A1** — because
A0 shipped at `3de2d62`. **A reader with only the work queue would start on finished work.**

## Clause 2 — *"two windows give different answers to what gates the beta"*: 🔴 **TRIPPED, inside its own dependency set**

| source | what gates the beta |
|---|---|
| `PLAN-OF-RECORD.md:109` | ⭐ *"**A1 + A2 together are the readiness bar.** Everything below is real and none of it gates the beta."* |
| `WORK-QUEUE.md` §4 (THE STANDING RISK) | *"Nothing in this queue changes that until **A2 + B0** ship together — and until they do, the falsifier's pass is a statement about lab, not about production."* |
| `SCOPE` §6.1 | *"⛔ **The blocker is not any of these.** It is **A5** — a per-estate digest resolved per request… **It is the long pole and nobody has started it.**"* |

⭐ **All three are honest and two of them are the same thing under two names** (`A5` in the SCOPE doc's
numbering is `A2` in the work queue's). **`B0` is the genuine disagreement**: the plan of record puts it
at ⑤·4, *below* the bar; the work queue calls it co-required for isolation to be real in production.

⛔ **Both can be true and the file does not say how.** The reconciliation, as far as I can read it: **A1
+ A2 gate GURU working for a launching household** (the readiness bar, ②), while **A2 + B0 gate
ISOLATION being enforced by software rather than by separate hardware** (the standing risk). Those are
two different beta-blockers wearing one phrase.

**Proposed — one line in ⑤, and the falsifier stops tripping:**

> **A1 + A2 gate the READINESS BAR (Guru at a launching household). A2 + B0 gate ISOLATION IN
> PRODUCTION** — today it is still enforced by separate hardware (`WORK-QUEUE.md` §4). Both are
> beta-blockers; they block different things.

## ⚠️ AND THE HONEST COST OF THE FORM — it went stale in four hours

§1.2 measured **four of its sequence items closed between 14:32 and 14:46 ET today**, and §1.3 measured
one of its own dependencies still carrying a question ⑦ says is ruled. ⛔ **That is not an argument
against the file — it is the argument for the falsifier's second sentence: *"needs to be shorter, not
longer."*** Its ③ and ⑤ are the fast-decaying halves.

**Recommendation: KEEP IT, and keep it under two screens.** Add nothing; strike what closes, with the
commit that closed it. ⭐ **And commit it** — it is untracked in the main tree, which means the one
document three windows steer by exists on one disk with no history. `measured`: `git status` in
`~/Developer/Tate-Tracker` lists it as `?? .plans/2026-09-10-PLAN-OF-RECORD.md`.

---

# 6 · WHAT I DID NOT DO — the boundaries, stated

- ⛔ **No file outside this one was written**, in this worktree or anywhere else. No tool, no
  `worker.js`, no `BACKLOG.md`, no `.decisions/` card, no `OBJECTIVES.md`.
- ⛔ **I did not write the ruling register.** `tate-tracker-ec` owns it. §1 and §2 name rows; they draft
  no register text.
- ⛔ **No row re-tiered, no status changed, no row deleted, no section split.** MOVE 1 is one whole
  section with a provenance line.
- ⛔ **The roster question (four owners or five) is not settled here** — `.decisions/fernwood-20.md` is
  Paul's.
- ⚠️ **`check-backlog-ready.py` will flag this file as an ORPHAN** (*"no `BACKLOG.md` row points at this
  plan"*). **That is correct and deliberate.** `POINTER_PAT` (`:114`) requires the literal `→ READY ·`,
  which is a **readiness claim**, and this proposal is `stage: draft` awaiting Paul. Adding one to
  silence a checker is precisely what `.decisions/fernwood-22.md` was minted to refuse. ⭐ **Both
  precedent rationalization proposals are orphans for the same reason** — `.plans/2026-07-29-rationalized-backlog-PROPOSAL.md`
  and `.plans/2026-09-02-rationalization-PROPOSAL.md`, and unlike them this one carries a full header,
  so it clears the other five flags they each carry.

---

# 7 · ⏱ ADDENDUM — what moved between measuring and committing (2026-09-10, later the same day)

⛔ **Nothing above is rewritten.** This corpus's own discipline, stated in `cb5e46a`: *"A decision that
flipped twice in one day must not be smoothed over."* The findings stay as measured at `fdece26`; this
section says what happened to each. Every row `measured` at `cb5e46a` and at `main` = `ea84315`.

## 7.1 · 🔄 §1.1's KILL WAS ITSELF REVERSED — the finding stands, its conclusion was overtaken

`cb5e46a` — *"A1 composes from the household's own record — **and the nigel/aida reversal, both events
kept**"*. `[paul-ruled 2026-09-10, reversing a kill made earlier the same day]`: *"I'm fine with
deleting Nigel and Aida for the time being. We can always re-mint their invite since we have a cleaner
base if deleting helps."*

⭐ **The reasoning is NOT the inference §1.1 correctly refused.** The commit says so in its own words —
*"The reason is NOT 'zero keys, never used' — that inference was wrong when first made. It is the
retirement of two environments built under the **deployment-per-household model R32/R33 supersede**."*
And the argument that carried it is one nothing in §1 had: ⭐ **the delete PROTECTS THE TEST** — those
envs are currently the only way to provision an estate, so leaving them would let the beta launch
**without the product ever creating one**.

**So the correct reading of §1.1, and it should not be read as the record contradicting itself:**

| | |
|---|---|
| **what §1.1 got right and still stands** | four live sites proposed an act on a **justification that was false**, one of them as step 1 of a six-step migration, and nothing reconciled them |
| **what was overtaken** | the *conclusion* (annotate as killed). Paul re-ruled **delete**, on a different and better argument |
| **what neither version licenses** | ⛔ the act. `cb5e46a`: *"**THE DELETION ITSELF IS NOT DONE.** Namespaces verified empty **BY ENUMERATION** (0 keys each, not inferred from activity), but destroying Cloudflare resources on a decision that has already reversed once today goes to **Paul directly, not on a relay**."* |

⭐ **And a ruling rode in with it that §1 did not anticipate:** ⛔ **ESTATE IDS ARE RETIRED, NOT
RESERVED** — `est-76012d` and `est-92e588` must never be re-used, *"an id is minted per estate;
re-using one makes two households indistinguishable in every historical record that already names it."*

`measured`: both events are on the page at **all four sites** — `SCOPE:624-625`, `:652`;
`REASSESS:118`, `:121-122`, `:169`. **§1.1's proposed remedy is therefore discharged**, by a route
better than the one it proposed.

## 7.2 · ⚠️ §1.3's Q6 IS HALF-DISCHARGED — `REASSESS` was fixed, `SCOPE` was not

`measured` at `main` = `ea84315`:

- ✅ `.plans/2026-09-10-migration-shape-REASSESS.md:167` now records the ruling — *"launch on the
  deterministic app alone, and Aida and Nigel are **held** rather than invited sooner."*
- 🔴 `.plans/2026-09-10-account-estate-model-SCOPE.md:758-762` is **byte-unchanged**: *"`## Q6 · Does
  Guru have to work at first light for a new household?` ⭐ …**the single highest-leverage question on
  the board**… If a household can launch with the deterministic app and no model routes, **A5 stops
  blocking B1** and Nigel and Aida can be invited much sooner."*

⛔ **That is the more consequential half and it is still open.** `SCOPE` is the file the plan of record
declares as a `depends-on:`; `REASSESS` is not. **§1.3's second strike is still owed.**

## 7.3 · ✅ §5's TWO FINDINGS ARE BOTH DISCHARGED

- **The falsifier's tripped clause is repaired.** `PLAN-OF-RECORD.md:140` now reads *"Three documents
  give three answers to 'what gates the beta' — they are not in conflict…"*, which is the reconciling
  line §5 asked for.
- **It is no longer untracked** — `git ls-tree main` resolves it. It has also grown and re-framed: ①
  is now **THE MILESTONE — READY TO INVITE**, ⭐ an **event rather than a state**, which is a better
  shape than the G1 wording §4 was written against.

⚠️ **§4's recommendation is unaffected and I am not revising it:** *where* the milestone lives and
*whether it is a sixth objective id* are the same questions under the new name, and the answer — a band
above the table, not `O6`, because a row cites exactly one id — turns on `OBJECTIVES.md`'s contract, not
on the milestone's wording. ⛔ **Ratifying the row is still Paul's**, and `.decisions/fernwood-20.md`
still holds the roster question.

## 7.4 · ⚠️ THE MEASUREMENT BASE MOVED — re-measure §1.6 before acting on it

`main` advanced `fdece26` → `ea84315` while this was written. Notably **A2 shipped**
(`a263ed3` — *"canon is resolved per REQUEST"*; `measured`: `grep -c canonFor worker/worker.js` → **7**,
against **0** at `fdece26`), plus two 🔴 fixes — *an estate's canon was ELECTED from whichever member had
an address* and *a household's setup was written to whichever record the CLIENT happened to name*.

⛔ **So §1.6's `scopeOf` 64 / `scopeFor` 3 / `X-Estate` 0 / `canonFor` 0 are stamped to `fdece26` and
at least one is already false.** They are labelled with their sha in §1.6 and in the QA table; **re-run
the greps before citing them.** ⭐ That is §0's own argument arriving on this document: a record goes
stale in the direction of over-reporting open work, and a rationalization is not exempt from the rule
it is written to enforce.

---

## Files touched

⛔ **None.** This file only. Everything below is **proposed** for Paul:

| file | proposed change | § |
|---|---|---|
| `OBJECTIVES.md` | the **G1 band** above the table — 9 lines, no id changes | 4 |
| `BACKLOG.md` | **MOVE 1**: § FOCUS FREEZE `:74–141` → § 📜 RULING REGISTER, with a provenance line + a 3-line pointer in its place; re-point `:3958` | 3 |
| `BACKLOG.md` | dated riders on **C4's THREE LEVELS** (`:2815`), **C9's ⏸** (`:3168`), **TIER 1 · 19** (`:231`), **TIER 2 · 7 · 8 · 12 · 15** (`:248–256`), **§ REPO VISIBILITY** (`:2746`) | 1.4–1.7, 2.8 |
| `BACKLOG.md` | § 🗳 DECISION CARDS: delete the *"11 of 12"* count; add rows 13–22 | 2.3 |
| `.plans/2026-09-10-account-estate-model-SCOPE.md` | ✅ M1 **done** by `cb5e46a` (§7.1) · 🔴 **Q6 (`:758-762`) STILL OWED** — the only remaining strike from §1 | 1.1, 1.3, **7.1, 7.2** |
| `.plans/2026-09-10-migration-shape-REASSESS.md` | ✅ **done** by `cb5e46a` — both the C1 sites and Q6 (`:167`) | 1.1, 1.3, **7.1, 7.2** |
| `.plans/2026-09-10-PLAN-OF-RECORD.md` | ✅ committed, and the beta-gate reconciliation landed (`:140`) · ⬜ still owed: strike the four closed sequence items with their commits; a `build:` sense in ④ | 1.2, 2.5, 5, **7.3** |
| `.decisions/fernwood-14.md` | strike the superseded **Recommendation** block (dated, not deleted) | 2.6 |
| `~/.claude/CLAUDE.md` | name the repo on the data-model-design citation (`:534`); §7 → §2b | 2.7 |
| `tools/check-backlog-drift.py` | ⭐ a `rulingsSince` **semantic** signal — a finding, not a build | 0 · F-1 |

## Sequence

1. **§4's G1 band + §3's MOVE 1 together.** They are one change — the gate becomes G1 and the freeze
   becomes history. Splitting them leaves two scope gates for a window.
2. **§1.1's three strikes** (the killed deletion). ⛔ Highest urgency of anything here: it sits at step 1
   of the migration table in a document the plan of record depends on.
3. **§1.3's Q6 strikes**, same shape, same files.
4. **§1.2's plan-of-record strikes** — ⚠️ re-measure before applying; the build windows are live and
   more will have closed.
5. **§1.4–1.7's riders** on `BACKLOG.md` rows — ⛔ **after `tate-tracker-ec` lands the register**, so the
   riders can cite it instead of duplicating it.
6. **§2.3, §2.6, §2.7** — independent, cheap, any order.
7. **F-1** — a finding for whoever owns `check-backlog-drift.py`. Not scheduled here.

## Falsifier

> ⭐ **A window that reads only `OBJECTIVES.md` § G1 and `BACKLOG.md`'s head region can state (a) what
> the goal is, (b) what is out of scope, and (c) what gates the beta — and gets the same three answers
> as a window that read the plan of record.**

Today it cannot: the head says *features hold lifted* and the plan of record says *features out of
scope*; the head names `PRODUCT-ENGINE.md` as the plan of record and a different plan of record exists;
and *"what gates the beta"* has three answers across three files (§5).

**And three narrower ones, each a single command:**
- `grep -rn "delete \`nigel\`\|delete nigel + aida" .plans/` returns **only lines carrying BOTH events**.
  At `fdece26`: 4 live and unannotated. ✅ **Green at `cb5e46a`** (§7.1).
- `grep -n "Q6 · Does Guru" .plans/*.md` returns **only headings carrying the ruling**. At `fdece26`:
  2 live. ⚠️ **Still red at `ea84315` — `SCOPE:758` is unchanged** (§7.2).
- `python3 tools/check-backlog-drift.py` reports **`⚡ N rulings landed since the last rationalization`**
  on a day like today, and stays quiet on a day with none. Today it says `rested` against 13 rulings and
  2 kills.

⛔ **The falsifier for this proposal as a whole:** if applying every move above leaves any reader able to
find, in a file the reading order sends them to, a statement that Mom's feedback is held, that Track B
is frozen, that nigel and aida should be deleted, or that Guru-at-first-light is open — then the
rationalization has moved lines and not meaning, and it has failed on its own terms.

## QA

**This document ships no code.** Every `measured` claim was read at **`fdece26`** in
`~/Developer/.tt-worktrees/backlog-rat` and is re-checkable:

| claim | how to re-check |
|---|---|
| `BACKLOG.md` carries nothing from today | `grep -c "2026-09-10" BACKLOG.md` → **0**; `git log --oneline -1 -- BACKLOG.md` → `eafcdfe` |
| the four closed sequence items | `git log --oneline -6` → `fdece26` · `2b62fb5` · `455c01e` · `2a552f2`; `git show --stat <sha>` |
| the killed deletion is still live in 4 places | `grep -n "nigel" .plans/2026-09-10-account-estate-model-SCOPE.md .plans/2026-09-10-migration-shape-REASSESS.md` |
| Q6 is still open in 2 places | `grep -n "Q6 · Does Guru\|highest-leverage question" .plans/2026-09-10-*.md` |
| `scopeOf` 64 / `scopeFor` 3 / `X-Estate` 0 / `canonFor` 0 | `grep -c "scopeOf(" worker/worker.js` etc. |
| `POST /api/estate` does not exist | `grep -n "api/estate" worker/worker.js` → **0 hits** |
| 22 decision cards, backlog says 12 | `ls .decisions/*.md \| wc -l` → **22**; `BACKLOG.md:181` |
| Track B lifted **09-06**, not 09-05 | `grep -n "PARTIAL UNFREEZE" BACKLOG.md` → `:811` `[paul-stated 2026-09-06]` |
| the drift detector reads rested | `python3 tools/check-backlog-drift.py` |
| `-PROPOSAL` owes a header, not sections | `tools/check-backlog-ready.py:398-406` |
| the plan of record is untracked | `git -C ~/Developer/Tate-Tracker status --short` → `?? .plans/2026-09-10-PLAN-OF-RECORD.md` |

⚠️ **What this document does NOT verify:** anything in live KV, any origin, or any deployment. It made
no network call. ⭐ **The five-owner state in `PLAN-OF-RECORD.md` ③ is cited as *its* measurement, not
re-measured here** — and by this repo's own rule that is a **relayed claim and therefore a hypothesis**
until someone reads the store. §1.5 depends on it (two estates now hold people); if that reading is
wrong, C9's release condition has not fired and §1.5 falls.
