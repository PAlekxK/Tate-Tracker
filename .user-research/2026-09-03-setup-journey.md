# The setup journey — invite → account → profile → devices joined

- row: `PRODUCT-ENGINE.md` § THE SETUP JOURNEY · `.plans/2026-09-03-grooming-queue.md` item 5
- objective: O3
- class: engine · declared
- seat: user-researcher (the four journeys, re-read against a setup phase)
- date: 2026-09-03 (ET)
- mode: research · **no build, no mechanism, no canon touched.** Ends at Paul's gate
- parallel seat: `engineering-partner` → `.engineering/2026-09-03-setup-journey.md` (account record, device
  binding, the sync path). Overlaps are cited in §7 and left to the main session
- builds_on: `../fernwood-private/.user-research/2026-09-02-activation-journeys.md` (J1–J4, §1 the minimum,
  §1.3 the backwards hazard, §4 the credential branches, §5.1 the new phone) ·
  `../fernwood-private/.user-research/2026-09-02-estate-manager-scoping.md` (§1.4, R.3, R.4 C-person/C-edge) ·
  `.engineering/2026-09-03-c6-privacy-seat-review.md` (Q5 · F10 · F14) ·
  `.engineering/2026-09-03-c6-door-for-paul.md` (§0 #2/#4, §1 M3) · `VOCABULARY.md` §3b · §4 ·
  `CLAUDE.md` § THE SITE'S PHYSICAL PREMISE · `BACKLOG.md` § FOCUS FREEZE · § M3
- evidence_level: mixed — per-claim tags below. ⛔ **Nobody has been asked anything about a setup phase.**

> ⛔ **PRIVACY.** Tracked, public file. "Mom", "Bob", "a contributor". No names, no addresses.

---

## 0 · What tonight settled, and what it leaves live

`[validated — .engineering/2026-09-03-c6-privacy-seat-review.md, Q5]` **The presented credential is an
opaque minted token for every grant, including hers.** No memorable word; a device-local unlock is the
named successor. ⭐ **So the credential half of ② is out of scope, and out of it in the direction that
helps:** there is now no version of a setup phase in which Mom types a secret. What is left of ② for her
is exactly one thing — **a name** — and that is the whole live question.

`[validated — BACKLOG.md § FOCUS FREEZE, paul-stated 2026-09-03]` *"I will worry about managing the
migration with Mom."* **Her transition is already declared to be an in-person event Paul runs.** That
narrows the Mom question further and changes its shape: it is no longer *"does she meet a setup screen"*
— it is *"at an event Paul is already sitting through with her, does she supply her own name."* Those are
different questions and the second is much closer.

⚠️ **And one thing I got wrong on 09-02 that I am retracting here, because the ratified vocabulary moved
under it.** I wrote that a display name is *"habit, and at Fernwood actively harmful,"* and I gave two
reasons: no surface addresses her, **and** a name field puts her name in the UI and in public git *by
construction*. `[validated — VOCABULARY.md §3b, 2026-09-02]` the second reason is dead:

> *"Personalising the landing page with a person's NAME is available and does not breach the name rule —
> that rule governs tracked files… A name a person supplies at activation and sees rendered back is hers,
> held in her instance's data and never in the engine."*

**One of my two legs was removed by a ruling, and the finding should be weaker than I left it.** What
survives is only the first leg — no surface addresses her today, and an ask has a measured 0-for-35 —
and that is a *cost* argument, not a *harm* argument. `[inferred]`

---

## 1 · The four journeys, re-read against a setup phase

`[inferred]` A **setup phase** is the mechanism that converts *an act the administrator performs on a
person's behalf* into *an act the person performs themselves.* Read that way, the question "who needs
one" answers itself against the cross-journey finding.

| # | journey | needs a setup phase? | harmed by one? |
|---|---|---|---|
| **J1** | administrator stands up an estate | ⛔ **no — it is where the invite is AUTHORED, not where anyone sets up.** Nobody is activated in J1 | no |
| **J2** | **Mom's retrofit** | ⛔ **no need exists.** The grant precedes the person; the credential is minted (Q5); she has used the app since May | ⚠️ **the seam. Depends entirely on whether the name is a screen or a conversation** — §2 |
| **J3** | Bob activates his own estate | ✅ **yes — and it fixes a governance defect.** An owner whose own name and credential are authored by Paul is *"a governance defect, not a convenience"* (my 09-02 §4) | no — he asked for this unprompted, friction is affordable, and this is the one place a text input plausibly belongs |
| **J4** | a contributor at **someone else's** estate | ✅✅ **the strongest case in the item** | no |

### 1.1 ⭐⭐ The cross-journey finding, carried forward and sharpened

`[inferred — 2026-09-02, unchanged and now load-bearing in the other direction]`

> **The shortcut that makes J2 kind is the exact act J4 forbids.** Paul binding her phone in person is the
> best available design at Fernwood and an **unconsented act** at Bob's — because he holds **capability**
> there and **no relationship**.

**A setup phase is precisely the machinery that removes that act.** So:

> ⭐ **The setup phase's strongest justification is J4 — the journey with the least evidence — and its
> only real cost lands on J2, the journey with all of it.**

`[validated]` The record on Mom: 11 sessions / 6 active days / 20-day window; 414 × A+; reading is
difficult; documented fear is getting things wrong; **0 of 10 · 0 of 10 · 0 of 10 · 0 of 5** on every
affordance that asks her, **5 of 5** on the one that moves her. `[validated — Paul relay 2026-09-02]` The
record on Bob's contributor, in full: **the person exists.** That is the entire validated content of the
role, and I declined to write a persona for it on 09-02 for the same reason I decline again here.

⛔ **That asymmetry is itself the finding, and it should be said out loud rather than smoothed:** the
design pressure for ② comes from a household nobody has measured, and the design cost lands on the one
person this project has four months of behaviour for. **Three of four journeys want a setup phase. The one
that does not is the one we actually know something about.** Any resolution that reads "three out of four,
so build it" has quietly traded evidence for arithmetic.

### 1.2 What survives both readings, so it is not re-litigated

`[inferred — restating PRODUCT-ENGINE's own reconciliation, verified against my source findings]`

- ① **The invite is the grant, authored by someone with a relationship at the estate.** This is my own
  09-02 rule wearing Paul's word for it. No conflict. ⭐ *An invitation may only be authored by someone
  holding a RELATIONSHIP, never only a CAPABILITY.*
- ② **The id stays minted and opaque; the name is data in the account record.** Under VOCABULARY §3b the
  public-git objection dissolves (§0). What is left is a cost question, not a rule violation.
- ③ **Account-keyed attribution is my own *"a binding is a declaration"*.** No conflict — see §3.
- ④ **Devices join the account** rather than each holding the master token. No conflict, and §4 argues it
  is overdue independently of any of this.

⚠️ **`profile` is not a noun here.** `[validated — VOCABULARY.md §4]` It was rejected: *"it is exactly
`person` + their `grants`, and a third word for a thing that already has two is how a fork starts."*
Paul's capture uses the word naturally, which is fine in speech; **it must not become a schema key or a
surface name.** `[validated — VOCABULARY.md §3b]` The ratified word for ①+② together already exists:
**activation** — *"a person becoming a person with a grant — first credential, first presence."*

---

## 2 · The name question, framed for Paul's ruling

### 2.1 What a self-supplied name buys

| # | what it buys | where | tag |
|---|---|---|---|
| 1 | ⭐ **At J4, it is the difference between self-description and a third party asserting a fact about a stranger.** If Paul types the name of someone in Bob's household, that is the relationship/capability violation arriving as a data-entry convenience | J4 | `inferred` |
| 2 | **An administrator can tell two people apart at one estate.** This was my own §1 falsifier on 09-02 — *"the most likely candidate [for a real job for a name] is a second contributor at one estate"* — and it is **still unasked.** One question to Bob settles it | J4 | `gap` |
| 3 | **An owner controls his own record.** J3's parallel to the credential ruling: an owner whose name was typed for him is the same defect one field over | J3 | `inferred` |
| 4 | ⚠️ **A person sees themselves recognised rather than a device greeted** — now *available* under VOCABULARY §3b, on a landing page that may say *"your homes"* | all | `assumption` — nobody has been asked, and the funnel cuts the other way |
| 5 | ⛔ **At Fernwood today: nothing a minted `personId` does not already do.** Two people, one contributor, and Paul authored the grant so he knows whose it is | J2 | `inferred` |

### 2.2 What it costs

1. ⛔ **A field with no job at its only live instance is a dead field, and this repo has a measured
   template for what that does.** `[validated — PRODUCT-ENGINE.md]` `location` exists 7× in
   `vehicles.json` meaning *where the paint-code sticker is*, and a session nearly minted it for siting —
   *"the sentence was the dangerous kind: a future agent would trust it and mint `location` for siting,
   straight into an existing meaning."* A `name` that is empty for both real people invites a fill.
2. ⚠️ **Asking is the class she is 0-for-35 on.** `[validated — CLAUDE.md lap 8 funnel]` Every affordance
   that asks her: zero. ⚠️ **But the sample is all cards.** `[inferred — my 09-02 §4]` *the trap is
   conflating choosing with typing; only the second is friction* — and she has demonstrably answered
   questions asked in conversation, deriving *vehicles / equipment / household systems* unprompted. **The
   funnel is evidence about cards, and it has been over-generalised (by me) to all asks.**
3. ⚠️ **A first-run on an app used four months is the product forgetting her.** Unchanged from J2.
   ⭐ **But Paul's in-person migration ruling means her setup need not look like a first-run at all** —
   there is a human in the room, which is the shape my own §4 recommended for the credential.

### 2.3 ⭐ Can it be optional without becoming a dead field? Yes — under two conditions

`[inferred]` **Optional is fine. Blank is not.**

1. ⛔ **`null`, never `""`.** An optional field that stores an empty string when skipped is
   indistinguishable from one nobody has filled — and that exact confusion is this repo's single most
   repeated failure class, recorded at least four times: a module **off** vs **on-but-empty**; a machine
   with **no home** vs **whose home was never recorded**; an **un-activated grant** vs **a quiet
   contributor**; and `read-mom-engagement.py` publishing `"?"` rather than `0`. **A declared absence is
   not a gap.** `[validated — PRODUCT-ENGINE.md; CLAUDE.md]`
2. ⛔ **Nothing may require it.** The moment a surface renders *"Hi, {name}"*, the field is required in
   practice and a fallback string is the admission. A surface that reads correctly with the field `null`
   is the only test that keeps it genuinely optional. `[inferred]`

### 2.4 ⭐⭐ What happens for Mom — three shapes, and the seam I have not tested

**She has used the app since May, and my J2 ruling stands unamended: `[inferred, high confidence]` the
correct retrofit produces no visible change. Falsifier: if she can tell anything happened, it was designed
wrong.** Against that, three shapes:

| | **(a) she never sets up** | **(b) she runs the full setup** | ⭐ **(c) she CHOOSES, Paul ENTERS** |
|---|---|---|---|
| what she does | nothing | types a name at the migration event | answers a question in a conversation |
| fields she supplies | 0 | 1 | **0** |
| a moment she can get it *wrong* | none | ✅ yes — a typo, *"is that right?"* | none |
| is the name genuinely hers | ⛔ no — Paul's, or absent | ✅ yes | ✅ yes |
| J2 falsifier (*she can tell*) | held | ⚠️ **breached by construction** | held |
| consistent with the Q5 credential ruling | — | — | ⭐ **identical shape** — the word she chooses, Paul enters |
| ⚠️ readable in the record | — | — | ⛔ **indistinguishable from (a) unless a `nameSource` exists** — see Q3 |

⛔ **I am not recommending among these, and the reason is not diplomacy.** PRODUCT-ENGINE assigns the
ruling to Paul, and it turns on a fact I do not have: **whether she experiences *"what should the app call
you?"* as an ask (the funnel says she declines asks) or as a conversation (my own §4 says choosing and
typing are different acts).** I have never tested that seam, and nobody has asked her. Manufacturing a
recommendation across it would be the same move that produced the 09-01 no-login drift — a plausible
inference hardening into doctrine because it was the newest thing written down.

⭐ **What I will say:** (c) is the shape most *consistent* with everything already ruled — and "most
consistent with prior rulings" is not the same as "right." It is also the shape that most needs Q3,
because on the record it looks exactly like (a).

⚠️ **And one honest note about (b), which is stronger than it looks.** `[validated — FOCUS FREEZE]` Paul
already owns her migration as an in-person event. A name typed once, with him sitting beside her, is not
an unattended first-run screen — it is closer to (c) than to a form. **The J2 falsifier fires on *"she can
tell something happened,"* and at an event she is already attending with him, something has visibly
happened regardless.** That may make the falsifier the wrong instrument for that day, which is Paul's
read to make, not mine.

---

## 3 · Attribution keyed to an account rather than `deviceId` — what changes for the person

**The standing constraint, and this repo has been burned by it repeatedly:** `[validated —
tools/people.json; CLAUDE.md]` **a `deviceId` is a browser bucket, not a person.** The 2026-08-01
retraction cost nine weeks — an unconfirmed identification promoted to validated, then reasoned from.
Every board in the loop says it asserts nothing about her.

**What ③ changes, from the person's side rather than the schema's:**

1. ⭐ **Her words stop being attributed by inference and start being attributed by an act she was present
   for.** `[inferred — my 09-02 §1.2]` *"today's attribution is an INFERENCE and a person record makes it
   a DECLARATION."* **That is the entire value proposition of identity here, and it is worth more than the
   access control.**
2. ⛔ **For her, nothing visible changes — and that is the correct outcome.** `[inferred]` There is no
   byline, no author chip, no *"posted by"* anywhere in the app, and nothing in the record suggests she
   wants one. **The change lands entirely on the reading side — on the boards Paul reads.**
3. ⛔⛔ **The archive hazard, and ② makes it worse, not better.** `[inferred — my 09-02 §1.3, restated
   because it is now closer]` The day identity exists, someone will retro-attribute four months of notes,
   voice and Guru turns. ⭐ **A *name* makes that feel not merely possible but tidy.** It must not happen:
   **records written before the person record existed stay `null`, permanently, and `null` rather than
   absent.** The cost is not a data error — it is a claim about who said something, made about the person
   whose documented fear is getting things wrong.
4. ⭐ **Two writers now write the same field, and only one of them is the person.** `[validated —
   privacy seat F10]` The grant is a **claim**; the `deviceId` resolver is a **guess** on an
   unauthenticated, client-supplied value. The seat proposes `personSource: grant | device-inference |
   null`. **Read from the person's side that field is the difference between *"she said this"* and *"a
   browser that is usually hers said this"* — two different sentences to put in front of Paul, and only
   one of them should ever be quoted back to her.** I endorse it on user-research grounds, independently
   of the security grounds. **Same idea as `via: master|grant`; adopt one shape, not two.**
5. ⚠️ **A bound device is still not a person.** `[inferred]` The binding says the device is *entitled*,
   not that she is *holding it* — a shared phone, a visitor, Paul on her phone. **Account-keyed
   attribution is better evidence, not conclusive evidence.** The disclaimer changes wording; it does not
   retire. ⛔ Anyone who reads ③ as retiring the caveat has upgraded an inference one notch and spent it
   as two — which is the 08-01 failure with a stronger-looking warrant.

---

## 4 · Device join — what it is today, and what a person should experience

### 4.1 Today, measured

`[validated — viewer.html:6889–6910, 19476–19544, read 2026-09-03]` The device-join surface is the **Sync
settings** modal: two text inputs — a **Worker URL** (`https://…workers.dev`) and a **Shared token**
(password field, placeholder *"paste the SHARED_TOKEN value"*). Its intro copy reads:

> *"Connect this device to your <estate> Worker so entries follow you between phone, tablet, and laptop.
> One-time setup per device — paste the same Worker URL and shared token everywhere you want to sync.
> **Deploy instructions live in the repo's `worker/README.md`.**"*

⭐ **The device-join surface points a person at a git repository's README.** It is a developer's pairing
screen wearing the app's stylesheet, and it asks for the two highest-friction inputs that exist — a URL
and a secret. `[validated — .engineering/2026-09-03-c6-door-for-paul.md §0 #2]` **And the secret it asks
for is the master token**, which gates her verbatim words, model spend, and writes to public canon.

`[validated — BACKLOG.md § M3]` **M3 is the same wound.** `tateTracker.textSize` is localStorage-only and
syncs nowhere; the Worker contains zero occurrences of it. **A new phone makes her words smaller, on the
one constraint she cannot work around** — and `[validated]` the toggle has 0 of 37 firings on her device,
so *she is not equipped to undo it.* ⭐ Nothing follows her across devices **because there is nothing that
IS her across devices.** That is ④ and M3 stated as one sentence.

### 4.2 The site's premise rules out the two most common join mechanisms in the world

`[validated — CLAUDE.md § THE SITE'S PHYSICAL PREMISE, paul-stated 2026-08-31]` No cell reception; Wi-Fi
from the house only; coverage falls off with distance; heavy canopy. **Never propose a design whose
mitigation is "improve the signal."**

> ⭐ **An SMS code is unreceivable at this property. An email link needs the house Wi-Fi she may not be
> on.** `[inferred]` So the physical premise independently rules out phone and email as join mechanisms —
> **a second, entirely separate road to the same conclusion my 09-02 field audit reached on doctrine
> grounds** (*"email has no job"* · *"the app is the channel, text is not"*). Two independent paths to the
> same rule is much stronger than one, and it means the rule survives even if the doctrine is ever revised.

**Three constraints on any join design, all falling out of the premise rather than out of taste:**

1. ⛔ **Joining happens in the house, once, and the device never needs the network again to stay joined.**
2. ⛔ **No join step may become a precondition for capture in the field.** `[validated — the 07-15 loss;
   ux F1b#5]` *a capture that can fail because a session lapsed is a capture that lies.* The ungated write
   path stays ungated; joining must not quietly re-couple them.
3. ⚠️ **A second device at the moment of joining is fine only if both are in the house.** A code shown on
   a laptop in the kitchen is fine; anything assuming the other device is reachable is not.

### 4.3 What a person should experience

| journey | what joining should feel like | tag |
|---|---|---|
| **Mom, new phone** | ⭐ **she should not experience it at all.** It is Paul, in person, in the house — the same mechanism as recovery, and the honest one at n=1. ⭐ **The test is not "the device is joined." The test is: the words are the same size.** | `inferred` |
| **Paul, his own devices** | one act in the house. No README, no URL, no master secret on a phone | `inferred` |
| **Bob** | ⭐ **he joins his own, and this is where a real join surface earns its text input.** J3 is the only journey where friction is affordable | `inferred` |
| **Bob's contributor** | Bob authors; **they** join. The join act is what makes ④ the mechanism that discharges §1.1 rather than working around it | `inferred` |

> ⭐ **The user-facing success criterion for ④, stated so an engineer can aim at it:**
> **a person who gets a new phone opens the app and everything looks the way it did on the old one —
> including the text size — and nobody has to explain anything.** M3 is the failing half of exactly that,
> live today, with no auth involved.

⚠️ **Two honest limits, stated rather than designed around.**

- `[validated — ux F3, via .engineering/2026-09-03-c6-door-for-paul.md §1]` **The device stays
  authoritative; the account is only a backup for the *next* device.** So the promise is *"the next device
  starts where the last one was,"* not *"settings follow you live."* Those differ when someone uses two
  devices at once, and a mirror that writes back could reset a device somebody set deliberately.
- ⭐ **A partially-joined device is worse than an unjoined one, because it works.** `[validated — privacy
  seat F14]` six of seven `X-Tate-Token` call sites read `sync.v1` directly. If a device is "joined" while
  most paths still present the master, the person-visible symptom is **some things sync and some don't** —
  the worst diagnostic shape available for a reader with difficulty, and invisible to every board. The fix
  is F14's and it is engineering's; **the user-side consequence belongs on this record.**

---

## 5 · Falsifiers

| claim | what would show it wrong | how it is measured |
|---|---|---|
| ⭐⭐ **A setup phase belongs in the engine at all** | It ships, and Mom's migration still runs as *"Paul does it in person on her phone"* — the make-or-break user routes around the mechanism | **Observed at the migration event Paul has already said he owns.** If it fires, the setup phase is J3/J4 machinery and should be **declared per grant**, not built as a journey everyone passes through |
| **② has a performer** | Bob's household has exactly one contributor, Bob authors that grant himself, and no surface ever addresses anyone by name. Then ① plus a minted id does everything ② was for | **One question to Bob.** Open since 2026-09-02, unasked |
| **A name field can stay optional** | Six months on, `name` is `null` at every grant at every estate and no surface has ever rendered one | Count non-null names across grants; count surfaces that read one. Both `grep`-able |
| ⭐ **Mom's retrofit should be invisible** | She notices and it goes **well** — asks about it with interest, or volunteers a name unprompted. **Her initiations outrank my caution the moment one happens** (standing doctrine) | Her own words, relayed by Paul. ⛔ Never fetched |
| ⭐ **"A name is an ask, and she declines asks"** | She is asked in conversation what the app should call her and answers easily. Then the 0-for-35 was about **cards**, not about **questions**, and I over-generalised | **One conversation.** ⚠️ It is the same conversation that settles the credential branch — one ask, two answers |
| **Device join is a real improvement** | A joined new phone is set up and someone still has to explain something for it to work — or a partially-joined device ships | The M3 test: a fresh profile joined by the new path renders at her size **on first paint**, with no explanation |
| **`personSource` is worth a field** | Every record after ③ carries `grant` and none carries `device-inference` — i.e. the resolver stopped writing people entirely. Then one field would have done | Count by source over the first month of real records |

---

## 6 · Questions for Paul

```
Q1 · framing · Does Mom go through the setup phase, or is her retrofit the exception?
   options: a) she does not — Paul sets the name or leaves it null; the retrofit stays invisible
          | b) she runs the full setup at the in-person migration event he already owns
          | c) she CHOOSES in conversation, Paul ENTERS — the Q5 credential split, applied to the name
   no-recommendation: PRODUCT-ENGINE assigns this ruling to him, and it turns on a seam I have never
     tested — whether she experiences "what should the app call you?" as an ask (funnel: 0 of 35) or as
     a conversation (my own finding that choosing and typing are different acts). Manufacturing a
     recommendation across an untested seam is the move that produced the 09-01 no-login drift.
   caveat: (c) is indistinguishable from (a) in the record unless Q3 lands — and (b) is closer to (c)
     than it looks, because he is already in the room.
   blocks: the person record's shape for HER grant only. J3/J4 need the field regardless, so nothing
     else in the item waits. Until he rules, the standing position is: no name is stored for her.

Q2 · assent · Does the `name` field exist at all, carried nullable everywhere including Fernwood?
   options: a) yes — nullable, null at Fernwood until Q1 | b) no — minted id only, until a real
     performer appears | c) yes, required at owner grants, absent at contributor grants
   recommend: (a). J3 and J4 have a real job for it — a name Paul types at Bob's estate is a third
     party asserting a fact about someone he has never met, which is the act the relationship rule
     forbids. Carrying it unset costs nothing; retrofitting a field into a live identity store costs a
     migration.
   caveat: optional is fine, blank is not — `null`, never `""`, or it becomes indistinguishable from
     unfilled, which is this repo's most repeated failure shape (module off/empty, home null/unrecorded).
   blocks: none.

Q3 · assent · Does the name carry a SOURCE, the way the privacy seat's `personSource` does?
   options: a) yes — self | relayed | administrator | b) no — a name is a name
   recommend: (a), for the same reason F10 gives for personSource: after ② there are two possible
     authors of a fact about a person and only one of them is the person. "She chose this" and "Paul
     typed this" are different sentences to put in front of anyone — and Q1(c) is unreadable without it.
   caveat: same shape as `via: master|grant` and `personSource` — adopt one idea in three places, not
     three ideas.
   blocks: none.

Q4 · framing · Is the setup phase ENGINE (every grant passes through it) or CONFIG (declared per grant)?
   options: a) engine — one journey, everyone | b) config — declared per grant
   recommend: (b), and it is the same answer I gave on 09-02 for activation, on the same evidence: the
     shortcut that makes her retrofit kind is the exact act a stranger's household forbids, so no single
     journey can be right for both. Declaring it per grant is what lets Q1's answer be "she doesn't"
     without that being an exception anyone has to remember.
   caveat: consistent with the item's own `class: engine · declared` — the MECHANISM is engine, the SET
     OF STEPS a given grant runs is declared. Conflating those is how a fork starts.
   blocks: nothing today, but it changes what the engineering seat designs — answer before build.

Q5 · assent · May Paul ask Bob whether his household has one contributor or two?
   options: a) ask it now | b) hold it until the migration lands | c) don't ask
   recommend: (a). It is the falsifier for the whole name question — a name has an unarguable job the
     moment an administrator must tell two people apart, and no job I can name if he does not. It has
     been open since 2026-09-02 and it is one sentence.
   blocks: none — but it is the cheapest thing on this page, and §2.1 row 2 stays `gap` until it is asked.

Q6 · assent · Is "the words are the same size" the acceptance test for device join?
   options: a) yes — a joined new phone renders at her size on first paint, with nobody explaining
     anything | b) no — joining is about data sync; text size is M3's separate problem
   recommend: (a). M3 and ④ are the same wound and his own capture says so ("that's kind of manual now").
     A join that syncs notes and resets the text size has solved the engineer's problem and not the
     person's — and the symptom lands on the one constraint she cannot work around.
   caveat: ux F3 holds the device authoritative and the account a backup for the NEXT device, so the
     test is "the next device starts where the last one was," never "settings follow you live."
   blocks: none.
```

---

## 7 · Overlaps I am NOT deciding — cited and left to the main session

1. **The account record's shape, the binding mechanism, and the `sync.v1` replacement path** →
   `engineering-partner`, running in parallel on this same item.
2. **`personSource` / `nameSource` as fields** → the privacy seat proposed the first (F10); I endorse it
   on user-research grounds and propose the second by the same argument. **The field designs are not
   mine.**
3. **F14 (seven `X-Tate-Token` call sites, one credential)** → privacy seat + C6. I have recorded only the
   user-side consequence: a partially-joined device is worse than an unjoined one.
4. **Whether the invite becomes a governed act** → `practice-steward`, flagged in the grooming queue.
   Nothing here needs it to be one.
5. **The words on any surface** → `content-steward`. ⛔ I specify constraints, never copy — and any
   invitation, welcome or activation message is **authored content**: human-confirmed before it reaches a
   person, or it does not exist.

## 8 · What I could not verify

- `[gap]` **Whether Bob's house has one contributor or two.** Open since 2026-09-02. Q5.
- `[gap]` **Whether she experiences a name request as an ask or as a conversation.** The seam Q1 turns
  on. Never tested. One conversation, which also settles the credential question.
- `[gap]` **Everything about Bob's contributor beyond existence.** ⛔ Bob's to ask, not Paul's, and not an
  agent's.
- `[gap]` **Whether any surface will ever render a name.** VOCABULARY §3b says it is *available*; nothing
  says it is *wanted*. The landing page's greeting is provisional (*"for now"*).
- `[gap]` **Her role at the condo** — open since 2026-09-02. It decides whether her setup happens once or
  twice, and whether she is ever the person a name would be rendered *to* rather than *about*.
