---
type: jtbd
project: fernwood / bug lane — cross-device sign-in
job_ids: [capture-from-the-device-in-my-hand, share-it-onward, get-in-from-a-new-device, administer-without-impersonating]
last_updated: 2026-09-10
sha: 5ffe811
seat: user-researcher
evidence_level: mixed — per-claim tags throughout. Nothing here is validated on more than one person.
sources:
  - "Paul verbatim, 2026-09-10 evening — the four attempts, the 'devices synced' ask, the landing-page direction, 'pkirsch should be production only'"
  - "handoff/handoff-cross-device-signin.md §1–§2 — the lane's measured account of what happened"
  - ".plans/2026-09-10-mom-onboarding-answers-FINDINGS.md — Mom's four records at `home`, 12:24:41→12:26:12 ET"
  - ".plans/2026-09-10-account-estate-model-SCOPE.md §2.2, §2.3, §5.1, §5.3 — one account many estates; zero estates is legal"
  - ".plans/2026-09-10-multi-tenancy-PLAN.md § HOW PAUL GETS IN, IN PRODUCTION [paul-ruled]"
  - ".plans/2026-09-07-sign-in-door-PROPOSAL.md §1.3, §1.4, §3.3, §5 — the portability promise, the door's three homes, recovery"
  - ".plans/2026-09-10-empty-shelf-and-founding-DESIGN.md §2 — the reached-and-empty branch"
  - ".user-research/2026-09-03-product-door-naming.md §1.1 — she has never typed a URL, ever"
  - ".user-research/2026-09-08-localized-feed-and-property-type.md §5 — an instrument property read as a customer property"
  - "🔬 read at 5ffe811: onboarding/index.html:331-332, :357, :374-384, :1138, :1181-1182, :1204-1215, :2207-2208 · estate/index.html:472-490 · homes/index.html:126, :202, :217 · viewer.html:7407-7432, :12244 · worker/wrangler.toml"
  - "~/.claude/user-research/fernwood.md — Builder-user structural bias; fact-of-household vs preference"
gate: >
  ⛔ Nothing here executes. No feature is pitched, no copy is authored, no ruling is made.
  Criticality is stated once, inside the customer lane, with a falsifier (§5).
privacy: >
  Public tracked file. No address, no first names, no credential value. Mom's records are cited by
  id. Paul's condo is named only as "the condo" except where a deployment name is load-bearing.
---

# Four jobs behind "I can't sign in to my own place from my phone"

> ## THE TEN LINES — liftable into a FINDINGS doc
>
> 1. `validated` **The product told a person his credential was wrong when his credential was fine.** `onboarding/index.html:1181` says *"That username and password don't go together… or ask Paul for a fresh link."* Both clauses were false for him: the pair does go together, and a fresh link would not have helped. The sentence cannot say *wrong house* by design (oracle defence) — so **the door's ownership, not the door's copy, is the defect.**
> 2. `inferred` **Paul did not go to the wrong door. He went to the door he had open** — a week of administering Mom's household. That is not a mistake a landing page prevents; it is two jobs colliding on one browser.
> 3. `validated` **Four jobs are tangled in this one report** and only one of them is about signing in: capture from the device in my hand · share it onward · get in from a new device · administer someone else's household without being one of its members.
> 4. `validated` **Job (c) — get in from a new device — is Paul's alone today.** Mom has never typed a URL, ever; her one origin move was Paul's act, in person. She is a **one device, one place** user and the door is invisible to her. Designing the door on her behalf has no evidence behind it.
> 5. `validated` **Job (d) is administrator-only and must NOT generalise.** `[paul-ruled 2026-09-10]` in production he holds `capability: administrator` and **no relationship at her household until she invites him**. A generalised "work at another household" affordance is the consent seam wearing a convenience feature's clothes.
> 6. `validated` **The laptop was the worst of the four attempts and produced no visible signal at all** — a cached shell of a place while every server request was refused (14 in ten minutes). A device rendering a place it can no longer reach is **silent to the person and silent to the record.**
> 7. `inferred` **"Synced automatically" is three different things and only one of them shipped.** The **place's facts** follow the person (`onboarding/index.html:1204-1215`, since 09-08). The **credential** does not (accounts are per-deployment). **Capture drafts** do not and have never been designed to — the outbox is *this device's disk* (`viewer.html:12244`).
> 8. `inferred` **Paul's binding constraint is identity; Mom's is connectivity.** Same job statement — *capture from the device in my hand* — different force. Fixing sign-in does nothing for the person standing where the Wi-Fi ends, and the site premise says that is permanent.
> 9. `inferred` **A house-independent door dissolves the unsayable sentence.** You cannot say *wrong house* at a house's door without building an oracle. At **the** door, "which house" stops being a secret worth protecting and becomes the thing the door is for.
> 10. ⭐ `inferred` **CRITICALITY (§5): the only reason this was diagnosable is that the person it happened to owns the KV store.** Every surface he met either blamed him or said nothing. Falsifier inside.

---

## 0 · A note on the framework, since it is the first JTBD card in this lane

**Jobs-to-be-Done** describes what a person hired the product to do — the *progress* they wanted — rather than what they clicked. Each card states the job as **when \<situation\>, I want to \<motivation\>, so I can \<outcome\>**, then the **four forces** that decide whether they switch to the new way: **push** (pain in the current state), **pull** (attraction of the new), **anxiety** (fear of the new), **habit** (inertia of the old). The forces matter here because three of these four jobs currently fail on **anxiety and habit**, not on capability — the mechanism mostly exists.

⚠️ **n = 1 on every card, and he built it.** `[[Builder-user structural bias]]` applies at full strength. Per `[[A fact-of-household report survives the builder-user bias]]`, I split each card: **what the product did** (fact, survives) from **what he wants** (preference, n=1).

---

# 1 · THE FOUR CARDS

## JOB A — *Capture something at my place from whatever device is in my hand*

> **When I'm standing in my own place and see something worth recording, I want to use the device already in my hand, so I can get it down without the moment becoming an errand.**

| force | reading | tag |
|---|---|---|
| **Push** | *"I can't just pick up my phone and take pictures of stuff in my condo"* — his words. The phone is the only device that is *with him at the thing.* | `validated` — his verbatim, 2026-09-10 |
| **Pull** | The laptop works. So the product is not unproven to him — it is **proven and unreachable**, which is a sharper push than never having worked. | `validated` — *"Using that link I'm auto-logged in on my computer."* |
| **Anxiety** | *Are my credentials wrong? Did I break something?* The product supplied this anxiety itself (§3.1). | `inferred` — from the copy he met, not from a statement he made |
| **Habit** | The camera roll. Nothing was blocked from his life — he can still photograph the thing and it lands nowhere the product can see. ⭐ **The competitor is not another app; it is the photo he takes and never files.** | `inferred` |

**Friction measured.**
- `validated` [lane] Accounts are written into the KV namespace of the deployment that created them (`worker/wrangler.toml` — `home`, `paul`, `bob`, `qa`, `lab`, each with its own namespace id). `pkirsch` exists at `paul`, not at `home`. **His username does not exist at the origin he opened.**
- `validated` [🔬 `viewer.html:12244`] The feedback outbox is *"durable on disk"* on the device that wrote it. A draft is a **device fact**, not a person fact — by design, and correctly so for the offline premise.
- `validated` [🔬 `viewer.html:7407-7432`] The whole `STORAGE_KEYS` roster is device-local: observations, outboxes, queue state, zones cache. Nothing in it is keyed to a person.

**What counts as done.**
> A photo taken on a phone that has never been to this place appears in the record of the place the person chose, **without a link, without asking a human, and without the person having to know which origin their place lives at.**

⛔ **What does NOT count as done:** signing in works. Signing in is the precondition; the job is the photo landing.

**Performers.** Paul at the condo `validated`. Mom at Fernwood `assumption` — **and the constraint is different for her** (see §4).

**Falsifier.** If, over the next four weeks, Paul signs in successfully on his phone and **still** files no captures from it, the blocker was never the door and this card is about a want he does not act on. Measured by: any `observations`/`feedback`/audio record from a second device at `est-d93508`.

---

## JOB B — *Share what I captured with the Guru, or with the administrator*

> **When I've recorded something at my place, I want it to reach the person or the assistant who can do something with it, so I can stop being the only copy.**

| force | reading | tag |
|---|---|---|
| **Push** | *"…to share with you, or with the Guru."* Two recipients named in one breath, unprompted. | `validated` — his verbatim |
| **Pull** | Both channels exist and both are good: Guru answers, and the administrator reads. | `validated` — shipped surfaces |
| **Anxiety** | ⭐ **The one this product has to watch.** *"share with you"* is frictionless when the administrator is your son. At Bob's house the same sentence means *a person outside the household reads my record* — the duty the 2026-09-02 AI-boundary amendment attaches and `.plans/2026-09-02-data-model-design.md` §7 gates. | `inferred` |
| **Habit** | Text the photo to Paul. **This is the real incumbent and it is explicitly out of bounds** — CLAUDE.md's standing rule is that text is not a feedback channel, because a parallel channel that works removes the reason to use the app. | `validated — standing doctrine` |

**Friction measured.**
- `validated` [🔬 `onboarding/index.html:1191-1199`, code comment recording a 09-08 measurement] The place's facts *were* being returned by the server and thrown away by the client — a person could sign in cold and land in a place called *"My Home"* while the record held the right name, address, coordinates and rankings. Fixed 09-08; **the fix is younger than the report.**
- `validated` [`.plans/…mom-onboarding-answers-FINDINGS.md` row 1] `est-e6696a` now holds **two published places** — Mom's Fernwood record and Paul's Grant Park records, from the 09-07 session at her origin. ⭐ **That is Job B's failure mode already realised**: material he captured "to share" landed in *her* household's record, not in a shared surface.

**What counts as done.**
> The thing I captured is readable by exactly the people I meant, and **I can tell, on the screen, which household it landed in** before I let go of it.

**Performers.** Paul `validated`. The Guru half is `validated` as a want and **unexercised** — no cross-device Guru turn exists for the condo.

**Falsifier.** If a capture-from-phone path ships and nobody ever names a recipient (every capture goes to the default household), then "share with you or the Guru" was a description of the current workaround, not a job — and this card collapses into Job A.

---

## JOB C — *Get into my place from a device that has never been there*

> **When I'm holding a device that knows nothing about me, I want to reach my own place, so I can use it where I actually am rather than where I set it up.**

| force | reading | tag |
|---|---|---|
| **Push** | Four failed attempts in one evening; *"this is a big usability issue for me right now."* | `validated` |
| **Pull** | ⭐ **The promise is already made.** The setup flow tells a person their place is theirs *on any phone, not just this one* (`.plans/2026-09-07-sign-in-door-PROPOSAL.md` §1.4). | `validated` |
| **Anxiety** | *I might be locked out of my own record.* And the product's own answer to that is **ask a human** — `onboarding/index.html:357`: *"Can't remember your password? Ask Paul — he can reset it."* | `validated` [🔬 read] |
| **Habit** | Use the laptop, where it already works. **Habit won on 09-10** — and the laptop's success is what made the phone's failure read as *my credentials are broken* rather than *this is a different house.* | `inferred` |

**Friction measured — the four attempts, by what the person could see.**

| # | device · surface | what he saw | what it meant | tag |
|---|---|---|---|---|
| 1 | phone · `/onboarding` at Mom's origin | *"That username and password don't go together."* | your account is not in this namespace | `validated` 🔬 `:1181` |
| 2 | laptop · `/onboarding` at Mom's origin | same sentence | same | `validated` [lane] |
| 3 | ⭐ laptop · `/estate/` at Mom's origin | **a place, rendered** | a cached shell; 14 server refusals in ten minutes, none visible | `validated` [lane] |
| 4 | phone · `/estate/` at Mom's origin | the bare door — *"Open your invitation link and your place will be here."* `estate/index.html:473` | correct for *no credential*; **false for a person holding a working one at another origin** | `validated` 🔬 |
| 5 | phone · his own origin, updated link | signed in; **filed feedback from the phone the same evening** | the job is reachable once the origin is right | `validated` — his verbatim |

⭐ **Row 3 is the dangerous one and it is the one that looks fine.** A device that paints a place it can no longer reach is the project's recorded **invisible-failure shape** — *"an empty answer record is not a quiet user"*, *"an event with no reader is not instrumentation"* — arriving a fourth time, this time in the person's own eyes rather than in an instrument.

⚠️ **And row 4 is a true sentence pointed at the wrong reader.** `estate/index.html:472-490` resolves four states honestly; **"holds a credential that is valid somewhere else" is not one of them**, and it cannot be, because the origin has no way to know.

**What counts as done.**
> On a device with no history, a person reaches their own place with **a username and a password and nothing else** — no link, no re-setup, no human — and if they fail, the sentence they read is **true about their situation** and names a next move they can take alone.

**Performers.** Paul `validated`, twice (09-08 cold sign-in, 09-10 phone). ⛔ **Mom: never.** She has no record of ever typing a URL (`2026-09-03-product-door-naming.md` §1.1, validated as an absence), her one origin move was Paul in person, and her four setup records are 91 seconds on **one** device. **This job has one performer on the record.**

**Falsifier.** If a second device ever appears for Mom without Paul physically present, she is a performer and the card's scope doubles. Measured by: two distinct `deviceId`s in her engagement record — ⚠️ a deviceId is a browser bucket, so this is evidence of a second *browser*, not of a second *person*.

---

## JOB D — *Work at a family member's household without pretending to be them*

> **When I'm looking after someone else's place on their behalf, I want to act as myself with the standing they gave me, so I can help without their record recording me as them.**

| force | reading | tag |
|---|---|---|
| **Push** | ⭐ **He had Mom's origin open because he had been working there for a week.** The collision was not confusion; it was two legitimate jobs sharing one browser. | `inferred` — from the brief's own note, not from a statement of his |
| **Pull** | `[paul-ruled 2026-09-10]` *"in production… Mom [sets] up an account, [sets] up an estate, and then [invites] me"* — he has already described the shape he wants. | `validated` |
| **Anxiety** | ⭐ The consent duty: an administrator who is not a household member reads that household's notes, voice and Guru turns. At Fernwood that is family; elsewhere it is a stranger. | `validated — standing doctrine` |
| **Habit** | ⛔ **The back door.** A hand-minted grant at her estate is one command away and would have "fixed" 09-10 in a minute. The ruling closes it by name. | `validated` |

**Friction measured.**
- `validated` [lane, inferred source] The laptop's stored credential at her origin resolved to *something* — his auto-login. The product has **no way to express "I am here as the administrator, not as a resident"**, so administering her household and being in her household are the same act on one screen.
- `validated` His own instruction — ***"pkirsch should be production only"*** — is this job asking for a boundary: **one identity, one home namespace**, and a duplicate of himself in QA is an identity the record can confuse with him.
- `validated` [FINDINGS row 1] The cost of having no such expression is already on the record: her estate holds his place's data.

**What counts as done.**
> The administrator can do administrator work at a household **and the household's record can tell the difference** — his acts attributed to him, her record unchanged by his presence, and **his own place never a row inside hers.**

⛔ **And the half that is done by NOT building:** no product surface offers "switch to another household." If that affordance ever exists for a non-administrator, this job has generalised and the consent gate has become decorative.

**Performers.** ⭐ **Paul, alone, permanently by design.** Not a persona — a **capability**, per the 2026-09-02 amendment (the gate is a role, not a person).

**Falsifier.** If a second person ever legitimately needs to act at a household they hold no relationship at — a co-administrator, a handover, a bereavement — this is no longer administrator-only and needs a real model rather than a rule. ⚠️ The `handover` seat in the reading roster is the standing probe for exactly this.

---

# 2 · WHOSE JOB IS WHOSE — the generalisation table

| job | Paul | Mom `validated` | Bob / Nigel / Aida | generalise? |
|---|---|---|---|---|
| **A · capture from the device in my hand** | `validated` want, blocked by identity | `assumption` want, blocked by **network** (§4) | `assumption` — nobody has been asked | ✅ **yes — every account-holder's**, but the *binding constraint differs per place* |
| **B · share it onward** | `validated` | `inferred` — she authors freely (4 notes, 4 composer opens, 4 Guru turns in one lap window) and has never chosen a recipient | `assumption`, and the **anxiety force flips** outside family | ⚠️ **yes, with the consent duty attached** — it is not the same job at a household the administrator is not in |
| **C · get in from a new device** | `validated`, twice | ⛔ **never performed; no evidence at all** | `assumption` — every one of them arrives on a new device by definition | ✅ **yes — and it is the ONLY door a new owner can use**, since their estates must now be founded through the product |
| **D · administer without impersonating** | `validated` | ⛔ not hers | ⛔ not theirs | 🚫 **NO. Administrator-only, and the product should not grow a surface for it.** |

⭐ **The asymmetry that matters for the roadmap:** job C is **least evidenced on the make-or-break user and most binding on every new one.** Mom is already in; Nigel and Aida have had their pre-provisioned environments deleted and must found through `POST /api/estate`, which does not exist yet. **A door they cannot use is a door with a zero at both ends** — nobody has walked it and nobody could.

⚠️ **What I will not do with that:** turn it into a priority claim. Ranking lanes is not mine.

---

# 3 · THE ONE LANDING PAGE — from the person's side

## 3.1 The sentence that cannot be said, and why the door's owner is the defect

`validated` 🔬 The failure copy is deliberately one message for both failures, mirroring a Worker that answers *unknown username* and *wrong password* with a byte-identical 404 — *"a distinguishable pair is a username oracle"* (`:1176-1178`). **That care is right and should not be undone.**

> ⭐ **But at a HOUSE's door there is a third failure it also cannot name — *right credential, wrong house* — and that one is not a secret.** Merging it into the other two is what produced a sentence that was false about the person reading it.
>
> **At THE door, that failure stops existing.** A person-scoped credential presented at a house-independent door either resolves to a person or does not; "which houses are yours" is answered *after* they are known, from their own grants. **Paul's direction removes the unsayable case rather than wording around it.**

`inferred`, and it is the strongest product argument in this file — and it is a *person-side* argument, not an engineering one: the reader's model of what went wrong finally matches the system's.

⚠️ **Three ledes, one door, at HEAD** (`:331`, `:1138`, `:2207`) — *"This link isn't working." · "Sign in to your place." · "Welcome back."* — chosen by the route that brought you. That machinery already understands that **the same screen means different things to different arrivals.** A landing page inherits that requirement, it does not retire it.

## 3.2 What a house-independent door must say to four readers

⛔ **Slots and constraints only. Wording is content-steward's; nothing below is copy.**

| the reader | what they must be able to do | what it must never do | tag |
|---|---|---|---|
| **one place** (Mom) | ⭐ **never meet this page.** Her icon opens her place. If the landing page is on her path, the migration has made a visible change to the one user whose target was *no visible change*. | become a step | `validated` — her icon is her only route |
| **two places** (Paul, after the condo and any invite) | see both, named as **places**, and pick | make him pick every time he opens it if he has one habitual place — position is priority and she taught us that | `inferred` |
| **zero places** (every new owner after signup) | be told the account worked and that founding is next, at a stated price | ⛔ **mention a link.** `homes/index.html:202` already carries the note: they *already opened it* — that is how they have an account | `validated` 🔬 + `.plans/…empty-shelf…DESIGN.md` §2 |
| ⭐ **stale credential** (the 09-10 laptop) | **be told, visibly, that this device is no longer connected** — and be offered the one act that fixes it | ⛔ **render a place it cannot reach.** This is the state with no sentence at all today | `validated` — 14 silent refusals |

⭐ **The fourth row is the new one.** Three of these four states are already resolved somewhere in the product; the stale-credential state is resolved nowhere, and it is the state this report was written about.

## 3.3 The stranger at the door — reconciling two ratified positions

Two things are both true and they have been pointing in opposite directions since 09-05:

- `validated` **Enrolment is no longer closed.** *"NOBODY SIGNS UP" IS RETIRED* `[paul-ruled 2026-09-05]` — people set up their own accounts. Mom did exactly that on 09-10, in 91 seconds, four records, no abandonment.
- `validated` **The product apex never says "sign up" to Mom**, because *she never meets the domain* (`2026-09-03-product-door-naming.md` §1) and because account-shaped naming is a barred register on her surfaces.

> ⭐ **They reconcile cleanly once the door is house-independent: the landing page is a surface for everyone EXCEPT the make-or-break user.**
>
> Two consequences, and both are research constraints rather than design opinions:
> 1. ⛔ **It cannot be validated by her behaviour and must not be justified by it.** No Mom telemetry can speak to a page she will never load. Anyone reaching for her funnel numbers to rank this work is reading the wrong instrument — the §5 error of the localized-feed pass, repeated.
> 2. ⭐ **Its only real reader today is a returning person on a cold device, and the product has n=1 of those.** Which of *sign in* or *create* leads is still what the door proposal called it: *"an evidence question, not an argument"*, with **0 real onboarding answers in every environment** at the time it was written and **four** now — all Mom's, all through an invite, none through a landing page.

⚠️ **And the honest cost of Paul's direction, stated once:** deployment separation is currently *the only thing holding the 2026-09-10 isolation rule up* (`multi-tenancy-PLAN` § Falsifier). One production origin is the right product answer and it **spends that protection** — which is why the plan binds the grant-key change and `POST /api/estate` to ship together. **That is not my call and I am not making it; I am noting that the person-side argument and the isolation argument point opposite ways and the first must not be used to quiet the second.**

---

# 4 · "DEVICES SYNCED AUTOMATICALLY WITH THE ACCOUNTS" — three things, three verdicts

He said one phrase. The record says it decomposes into three independent layers, and they are in three different states.

| # | layer | does it follow the person today? | evidence | tag |
|---|---|---|---|---|
| **1** | **The credential** — *my username works wherever my places are* | ⛔ **No.** Accounts are per-deployment namespace; `pkirsch` at `home` cannot resolve | `wrangler.toml`; lane sweep (`home` held one account, `paul` held `pkirsch`) | `validated` |
| **2** | **The place's facts** — name, accent, address, coordinates, rankings, contact preference, journal name | ✅ **Yes — since 2026-09-08, two days before the report** | 🔬 `onboarding/index.html:1204-1215`; the Worker returns them on `/api/session` and the client now stores them | `validated` |
| **3** | **Capture drafts and device state** — the outbox, observations, queue answers, zones cache, text size | ⛔ **No, and by design.** Every `STORAGE_KEYS` entry is device-local; the outbox is *"durable on disk"* until a 2xx | 🔬 `viewer.html:7407-7432`, `:12244` | `validated` |

> ### ⭐ What he almost certainly means is (1), and the record supports that reading
> His sentence names the *symptom* — *"can't pick up my phone"* — and (1) is the only layer that produced it. (2) had already been fixed. (3) never blocked him: he lost no draft, because he never got far enough to write one.
> `inferred`. ⚠️ **I did not ask him**, and the phrase is ambiguous on its face — it is also a fair description of (3). **One sentence from Paul settles it and I am flagging it rather than assuming it** (§6 Q1).

### 4.1 ⛔ Do not let (1)'s fix get read as a promise about (3)

`inferred`, and this is the finding I would most want carried forward:

**Layer 3 must stay device-local, and the site premise is why.** No cell signal; Wi-Fi fades with distance from the house; heavy canopy. *"Capture must be entirely local, with sync deferred."* A design that made drafts "follow the person" through the server would put a network call on the capture path at the exact moment there is no network — and *"capture must not lie"* is the one rule her surfaces are built on.

> ### ⭐ So the same job statement has two different binding constraints, and they want opposite fixes.
>
> | | Paul, at the condo | Mom, at the far end of the property |
> |---|---|---|
> | blocked by | **identity** — the door refused him | **connectivity** — the door is irrelevant, the network is gone |
> | fixed by | a person-scoped credential | a local-first capture path that syncs later |
> | current state | ⛔ broken | ⚠️ `assumption` — **never measured with her, standing out there** |
>
> `inferred` for the left column (his four attempts), `assumption` for the right. ⛔ **Nobody has ever observed a capture attempt out of range**, and the zone-audio surface posts to the Worker — the open hazard CLAUDE.md names by hand. **Fixing sign-in will not move that square inch.**

---

# 5 · ⭐ CRITICALITY — one claim, inside the customer lane, with a falsifier

> ### The only reason this failure was diagnosable is that the person it happened to owns the KV store.

**Why, each tagged:**

1. `validated` 🔬 **Every surface he met either blamed him or said nothing.** The door said the pair don't go together (false about him). The bare page said open an invitation link (false about him — he holds a working credential). The laptop said nothing at all and drew a place. **None of the three states he met had a sentence that was true about his situation.**
2. `validated` 🔬 **The product's stated recovery route for him is himself** — *"Ask Paul — he can reset it"* (`:357`) and *"or ask Paul for a fresh link"* (`:1182`). For the administrator, the escalation path is a closed loop. For Mom, *"ask Paul"* is precisely the escalation the sign-in door was built to avoid (the door's own comment says so).
3. `inferred` **A non-administrator in the same position has no route at all.** They would have concluded their password was wrong, tried again, and asked a human — and the human's answer would be *"you're at the wrong address"*, which nothing on any screen could have told them.
4. `inferred` **The lane's method is not repeatable by the people it is for.** The four attempts were resolved by reading namespaces and refusal logs. **The person-facing record produced nothing that would have resolved them.**

**My falsifier, pre-registered.** Name the sentence a non-administrator would have read on one of those three screens that lets them recover **without contacting a human**. If such a sentence exists at HEAD, this claim did not fire. I could not find one.

**Second falsifier, measurable.** If a failed sign-in at a foreign origin writes a record a person can act on — and someone other than Paul recovers from it unaided — the claim is retired. ⚠️ `door_failed` instrumentation is *specified* (`sign-in-door-PROPOSAL` §5, last constraint) and I did not verify it fires on this path. **Do not treat that as either present or absent on my word.**

⛔ **What I am not saying.** Not that this outranks the multi-tenancy work, the founding endpoint, or any engineering row. Inside the customer lane: this is the claim about a person most likely to be acted on and most likely to be mis-stated as *"we need a login page."*

## 5.1 ⭐ Critical in my own lane: no seat in the battery could have found this

`inferred`, and it is a coverage hole rather than a defect.

Every synthetic walk is provisioned **per seat per env** — a seat's fixture belongs to one environment, and `walk-fixtures.py` reports arrival and procedure within one. **No walk in this harness has ever held one credential and presented it at two origins**, which is the entire shape of the 09-10 report. `seat-portfolio.py`'s first run already said the portfolio cannot be assessed yet and named `other` as the best uncovered cell — *"somebody whose want is not on the list."* **This is a second uncovered cell with a name: the person who belongs to more than one place.**

⚠️ **Not a request to build a seat.** A seat is a shape, and I am naming the shape: **multi-household person, cold device.** Whether it earns a seat is not mine.

---

# 6 · WHAT I NEED FROM PAUL — four questions, one line each

1. ⭐ **By "devices synced automatically," did you mean your credential should work anywhere (layer 1), or that things you start on one device should show up on another (layer 3)?** §4 reads it as layer 1; the whole cross-device design forks on the answer and I will not guess it.
2. **When you went to Mom's origin on your phone — were you trying to get into *her* place or into *yours*?** It reads as *yours* (the condo photos), but that makes the trip an accident of a bookmark, and if you were trying to reach hers, job D is the primary job in this report and A is secondary.
3. **Was Mom alone when she set up on 09-10?** Already the highest-value missing fact in the onboarding findings, and it now also decides whether her *never performed job C* is a fact about her or about the fact you were there.
4. **Does "pkirsch should be production only" mean one identity per person across all environments, or one *production* identity plus disposable QA ones?** They are different rules for the fixture hygiene work and only the first is a claim about identity.

⛔ **A Mom-Test-legal question for the only person who can answer one** — past behaviour, about his life, not about the idea:
> *"Walk me through the last time you were somewhere at the condo and wanted to record something — what device was in your hand, what did you actually do with it, and where did it end up?"*

⭐ The value is in **what he used instead.** If the answer is the camera roll, the product is competing with a photo that is already taken; if it's a note to himself, it is competing with a list. ⛔ **Do not ask whether he would like to capture from his phone** — he has said so; a second yes measures nothing.

---

# 7 · WHAT I DECLINED

- ⛔ **To design the landing page.** §3.2 states what four readers must be able to do. No layout, no copy, no ordering of *sign in* vs *create* — that last one is explicitly an evidence question and the evidence is n=1.
- ⛔ **To rule the isolation trade.** §3.3 names that the person-side argument and the deployment-isolation argument point opposite ways. Paul's, with the engineering seat.
- ⛔ **To write a persona for "the multi-household person."** One observation, and he is the builder. §5.1 names the shape; it is not a person yet.
- ⛔ **To treat "share with you or the Guru" as validated for anyone but Paul.** Mom has never chosen a recipient.
- ⛔ **To claim `door_failed` is or is not firing on this path.** I did not measure it (§5).
- ⛔ **To promote Mom's 09-10 setup into evidence about job C.** She performed founding, on one device, possibly assisted. Those are different journeys.
- ⛔ **To re-derive the lane's namespace measurements.** Cited, not re-run.

---

## Evidence log

- `2026-09-10: [validated] — Paul verbatim, evening: four attempts; "I can't just pick up my phone and take pictures of stuff in my condo to share with you, or with the Guru"; "Using that link I'm auto-logged in on my computer"; later "With the updated link I can log in successfully on my phone. I submitted some feedback via my phone."`
- `2026-09-10: [validated] — Paul verbatim: "Does that mean that we don't have a single sign-in door?… We should have a landing page, just in the production environment, and everyone can access by logging in to their own estates." And: "pkirsch should be production only."`
- `2026-09-10: [validated — lane-measured, cited not re-run] — accounts live per deployment namespace; `home` held one account (Mom's), `paul` held pkirsch with 3 routed grants. pkirsch cannot resolve at fernwood-home. The laptop showed a cached shell while 14 server requests were refused in ten minutes. The phone at /estate/ with nothing stored showed the bare door.`
- `2026-09-10: [validated — 🔬 onboarding/index.html:1176-1182 @5ffe811] — one failure message for both failures, mirroring a byte-identical 404, because "a distinguishable pair is a username oracle": "That username and password don't go together. Have another look — or ask Paul for a fresh link." ⭐ It also cannot say RIGHT CREDENTIAL, WRONG HOUSE — and that third case is not a secret.`
- `2026-09-10: [validated — 🔬 onboarding/index.html:331, :1138, :2207] — three ledes for one door, chosen by arrival route: "This link isn't working." / "Sign in to your place." / "Welcome back." The door already knows the same screen means different things to different arrivals.`
- `2026-09-10: [validated — 🔬 onboarding/index.html:357] — "Can't remember your password? Ask Paul — he can reset it, and it only takes him a second." For the administrator this is a closed loop; for Mom it is the escalation the door exists to avoid (the file's own comment).`
- `2026-09-08: [validated — 🔬 onboarding/index.html:1191-1215, code comment recording the measurement] — sign-in stored the token and threw the place's facts away; a cold sign-in landed in "My Home" while whoami returned the real place. Fixed 09-08: name, accent, address, addressParts, ranked, contactPref, coordinates and the journal name now cached from the session response. LAYER 2 OF "SYNCED" ALREADY SHIPPED.`
- `2026-09-10: [validated — 🔬 viewer.html:7407-7432] — every STORAGE_KEYS entry is device-local (deviceId is "the browser bucket — NEVER a person"); four are additionally per-estate-segmented. Nothing in the roster is keyed to a person.`
- `2026-09-10: [validated — 🔬 viewer.html:12244] — the feedback outbox is "durable on disk", held until a 2xx: her words survive a dead network, a closed tab and an unpaired device — but not a different device. Layer 3 does not follow the person, by design.`
- `2026-09-10: [validated — 🔬 estate/index.html:472-490] — four empty states: no grant / fetching / unreachable / reached-and-empty (split further by placed). ⛔ "holds a credential that is valid at another origin" is not one of them and cannot be, at a house's door.`
- `2026-09-10: [validated — 🔬 homes/index.html:126, :202, :217] — the shelf says "One account, one home — for now"; its reached-and-empty branch tells a person to open an invitation link they already spent. Named as the defect in .plans/2026-09-10-empty-shelf-and-founding-DESIGN.md §2; copy is DRAFT, unratified.`
- `2026-09-10: [validated — 🔬 worker/wrangler.toml] — envs qa · lab · home · bob · paul, each with its own KV namespace id; pages projects myhome-bob, myhome-paul. Per-deployment accounts are the design as built.`
- `2026-09-10: [paul-ruled — .plans/2026-09-10-multi-tenancy-PLAN.md §HOW PAUL GETS IN] — in production Mom creates her account and estate and invites him; he holds capability: administrator and NO relationship at her household until granted. Minting himself a grant is the back door this closes.`
- `2026-09-10: [validated — .plans/…account-estate-model-SCOPE.md §2.2, §5.1] — one account, many estates; zero estates is a legal, normal state ("the empty shelf"). §5.3: an account with no estate cannot be attributed today — a person's first words come back personId:null.`
- `2026-09-10: [validated — .plans/…mom-onboarding-answers-FINDINGS.md] — Mom set up at `home` 12:24:41→12:26:12 ET: four records, 91 seconds, no abandonment, one device. Row 1: est-e6696a now holds TWO published places — hers and Paul's Grant Park records.`
- `2026-09-03: [validated as an absence — .user-research/2026-09-03-product-door-naming.md §1.1] — no record of Mom ever typing a URL; her one origin move is Paul's act, in person. She is the reader for whom the landing page must be invisible.`
- `2026-09-07: [validated — .plans/2026-09-07-sign-in-door-PROPOSAL.md §1.4] — the setup flow promises a person their place is theirs "on any phone, not just this one", and there was no route that kept it. THE PROMISE PREDATES THE COMPLAINT.`
- `2026-09-08: [validated as a record, not re-run — onboarding/index.html:374-384] — "20 people reached the QA door that day and 0 got through"; a clean browser was routed to CREATE AN ACCOUNT under a username already taken. The fix was to stop guessing and offer both answers.`
- `[validated — standing doctrine, CLAUDE.md] — the app is the feedback channel and text is not; capture must be local-first (no cell, Wi-Fi fades with distance, heavy canopy); the AI-boundary gate is a ROLE, and an administrator outside the household needs explicit up-front agreement before the first contributor input.`
- `[inferred] — Paul's binding constraint is identity; Mom's is connectivity. Same job statement, opposite fixes. ⛔ Nobody has ever observed a capture attempt out of Wi-Fi range at Fernwood — the right-hand column is assumption.`
- `[inferred] — no synthetic seat could have produced this finding: walks are provisioned per seat per env, and none has ever presented one credential at two origins. Uncovered shape: multi-household person, cold device.`
- `[assumption] — that "devices synced automatically" means layer 1 (the credential) rather than layer 3 (drafts). Read from the symptom he reported, NOT from anything he said about the mechanism. §6 Q1.`
- `Open, unobserved: whether he was going to her place or his · whether Mom was alone at setup · whether door_failed fires on a foreign-origin sign-in · what anyone other than Paul would do at the three screens he met · whether a capture succeeds out of range at Fernwood · whether Bob, Nigel or Aida want any of jobs A–C (none has been asked).`
