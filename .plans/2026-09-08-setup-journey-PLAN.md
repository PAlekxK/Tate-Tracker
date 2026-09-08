# setup-journey · the clean journey, and the plan to build it

- row: `BACKLOG.md` § TIER 2 (row to add) · this scopes **the way in** end to end — arrive · account · place · return · repair · recover
- objective: O3 · class: **engine · declared** (one door, every household; whether a door is *demanded* stays `config`)
- seats: user-researcher → `.user-research/2026-09-08-setup-journey-map.md` (the SHOULD · the IS · the diff, every claim tagged)
  - content-steward → **owed, not waived.** Every screen in Act I is read by someone who thinks they have been locked out. This file specifies slots and constraints; it words nothing.
  - ux-expert → owed for B3/B4 (where the door stands, what the shelf looks like). ⚠️ Its F1a — *the glance renders with zero authorization round-trips* — binds every step below.
  - privacy-security → **owed before B2 ships**, on a premise that moved: `.plans/2026-09-07-sign-in-door-PROPOSAL.md` §4.3 P1 (`ACAO: *` on a credential-returning route) and P2 (no rate limit on `/api/session` or `/api/account`).
  - ai-advisor → waived. No model is on this path, and ⛔ a model may never generate a credential.
- depends-on: `.plans/2026-09-07-sign-in-door-PROPOSAL.md` · `.plans/2026-09-05-onboarding-PLAN.md` · `.user-research/2026-09-06-places-and-settings-journey.md`
- ready: **agent-proposed 2026-09-08 — Paul rules.** ⛔ NOTHING IN § Sequence STARTS.
- stage: concept
- stage-note: 2026-09-08 — written read-only against the working tree while the build is **frozen at `13b98a4`** for a walk. ⛔ No tracked file outside `.plans/` and `.user-research/` was edited; nothing deployed; no production call. **Any commit expires the gate ① evidence** — this file exists so the work is ready the moment the freeze lifts, not so it starts under it.

> ### ⭐ THE ONE PARAGRAPH
> Paul could not get into his own home today, and **no screen was broken.** A rejected credential
> returns a deliberately opaque 404; every client reads "not 200" as `null` and returns early; the
> screen keeps the empty state it painted first. **So "I couldn't check" renders as "you have no
> homes."** The clean journey below is built around that: a person is never told a thing is absent
> unless the product has *verified* it is absent, and there is always exactly one way back in.

---

## 1 · THE CLEAN JOURNEY — four acts, sixteen stages, and every stage has a failure exit

Full stage-by-stage detail, evidence and tags: `.user-research/2026-09-08-setup-journey-map.md` §1.
This is the shape a build follows.

```
              ┌──────────────────────────── ACT I · GETTING IN ────────────────────────────┐
  /  (origin) ─►  THE DOOR  ──── "I'm new"  ──►  account  ─►  name  ─►  where  ─►  confirm  ─►  what matters
       │            │  ▲                                                                          │
       │            │  └─ wrong password / no such pair → ONE generic message, no red, no alarm    │
       │            └── "I've been here" ─► sign in ─► ─────────────────────────────────────┐     │
       │                                                                                     ▼     ▼
  /?g=<link> ──► same door, recognised ──────────────────────────────────────────────►  ┌─ YOUR HOMES ─┐
                                                                                        │  a row = the │
              ┌──────────── ACT III · LIVING IN IT ────────────┐                         │  place, one  │
              │  the app  ◄──────────────────────────────────────────────────────────────┤  tap, always │
              │    ├─ what you told me   (the receipts, carried IN)                      └──────┬──────┘
              │    ├─ settings · this place                                                     │
              │    └─ settings · your account ──────────────────────────────────────────────────┘
              └────────────────────────────────────────────────┘        ACT IV · KEEPING IT
                                                                        repair · recover · add · sign out
```

**Five rules the shape encodes. Each is a constraint on the build, not a description.**

1. ⭐ **One door, two answers.** *"I've been here"* and *"I'm new"* meet the same surface. The
   product never guesses which one a person is from a device-local key — it **asks**, because a
   localStorage key cannot answer *"do you already have an account?"*
2. ⛔ **Never assert absence you have not verified.** Three states, always: `ok` · `empty` ·
   `unknown`. *"I couldn't check"* is a first-class screen state and never wears `empty`'s words.
3. ⭐ **The shelf is the way in** `[paul-ruled 2026-09-08]`. A row opens **the place** — the app — in
   one tap. Nothing is interposed.
4. ⭐ **Receipts travel with the person, not with the setup.** What they told us is reachable from
   where they live, not from a screen they passed through once. **Transfer, not deletion** (§4 of the
   research map).
5. ⛔ **Every failure names its own system.** A credential failure must never wear a save failure's
   words. Paul could not tell the two apart today, and he wrote the flow.

---

## 2 · ⛔ WHAT ONLY PAUL CAN RULE — six, largest first

> ## ✅ ALL SIX RULED — 2026-09-08, in conversation. The table below is kept as the framing; these are the answers.
>
> | | ruling | what it now requires |
> |---|---|---|
> | **D1** | ⭐ **A — the ADMINISTRATOR is the reset path.** | The only option that serves someone who answered *"Please don't"*. ⛔ **It makes "the administrator can read anything behind anyone's door" a stated PRODUCT PROPERTY, not an implementation detail** — so any copy implying privacy-from-the-administrator is now false and must be found and fixed. It also means the product cannot onboard a household faster than one person can answer a phone. Half-built already: `grant-mint.py --rotate`. |
> | **D2** | ⭐ **(iii) A FRONT DOOR FOR EVERYONE** at the bare origin. | ⚠️ **Chosen against the recommendation, knowingly, after being told it was flagged.** It contradicts ux **F1a** — *the glance renders with zero authorization round-trips* — **if the door is reached before first paint**. ⛔ The plan's own words: this *"needs rejecting in writing, not by silence"*, and the same is true of adopting it. **The reconciliation is owed before B3 is built:** the likely shape is that a credentialed device passes straight through and only an un-credentialed visitor meets the door, which honours both — but that is `proposed`, not ruled, and F1a's owner has not agreed it. |
> | **D3** | ✅ **TRANSFER the receipts, then retire `/estate/`.** | Address, contact choice and ranking move into *"What you told me"* inside the app **first**; the screen retires after. Same shape as TIER 2 · 10's warning about the tile row: the fix is a transfer, never a deletion. This is what answers the `mom` seat's *"recognised on the way in, left behind on the doorstep."* |
> | **D4** | ✅ **ONE vocabulary question to content-steward.** | The top-left label, the shelf's name, *"What you told me"*, and *"Your colour" → "Your account colour"* go as a single brief, so the answers agree with each other and with `VOCABULARY.md`. ⛔ Four separate string fixes is how this corpus grows a fifth noun. |
> | **D5** | ⭐ **NO — multiple homes per account, THIS LAP.** | ⚠️ **Chosen against the recommendation, knowingly.** ⛔ **This is engine scope, not a screen change.** `whoami` resolves to exactly one estate by construction and **there is no person→estates index** — the Worker's own comment says so. B4 changes shape, and the dead end Paul walked into today (no home shown AND no way to add one) is removed at the root rather than papered over. |
> | **D6** | ✅ **Email and phone DISPLAYED AND EDITABLE.** | Unblocked by D1: with the administrator as the reset path, the email is no longer load-bearing for recovery, so editing it is a build rather than a security surface. Two seats independently found they could choose *"by email"* and never see or change which email. |
>
> ⭐ **D2 and D5 both went against the recommendation and both were taken with the objection stated.** That is recorded here so a later reader does not "correct" them back, and so the two things they now owe — F1a's reconciliation, and a person→estates index — are visible as consequences of a decision rather than as surprises.


Nothing below B1 starts without the ruling that gates it. A ruling that is not in the register is not
in force: whichever way each goes, it is written into the citing file before anything is built on it.

| | the question | why it is his | gates |
|---|---|---|---|
| **D1** | ⭐⭐ **RECOVERY — who resets a forgotten password?** Options, costs and precedents are already laid out in `.plans/2026-09-07-sign-in-door-PROPOSAL.md` §5 (R1) and are **not re-opened here.** Choosing *"the administrator"* means the product cannot onboard a household faster than one person can answer a phone, **and** that the administrator can read anything behind anyone's door | It is an operating-model decision wearing a UI question's clothes | **B10**, and the *copy* of B2 |
| **D2** | ⭐ **What is at `/`?** Today it redirects to the app (`index.html:6`). Three readings, all consistent with something already ruled: **(i)** the app, with the door reachable from its empty states · **(ii)** the shelf · **(iii)** a front door for everyone. ⛔ (iii) contradicts ux F1a (*the glance renders with zero authorization round-trips*) if it is ever reached before first paint, and it is what an implementer builds by default — so it needs rejecting in writing, not by silence | Naming and shape are his | **B3** |
| **D3** | ⭐ **What happens to `/estate/`?** His ruling says the handoff screen is a leftover and the homes list is the way in. ⚠️ **It is also the only surface carrying the receipts** — address, contact choice, ranking (`estate/index.html:346–420`). Delete the screen and the ranking has no home. Recommend: **transfer** the receipts to *"What you told me"* inside the app, then retire the screen | It is a scope call and a naming call | **B4, B5** |
| **D4** | **What is the top-left called?** *"is 'My Home' the right thing there or is it kind of account menus."* Same question as *"What you told me"* (F7). ⛔ **Route it to content-steward as one question about the whole navigation vocabulary**, not four separate string fixes — that is how this corpus grows a fifth noun | Naming is his | **B4, B5, B6** |
| **D5** | **Does one-account-one-home stay true this lap?** `＋ Add a home` is honest today and it answers *no* on a page that may be showing nothing. If it stays, the shelf's empty state has to be right first (B4). If it goes, B4 changes shape | Scope | **B4** |
| **D6** | **Email and phone: displayed, or displayed *and* editable?** He asked for both. Display is a build (B6); **editable** touches the recovery route and therefore waits on D1 | The recovery half is his | **B6** |

---

## 3 · THE BUILD PLAN — ten steps, each shippable alone, each with a falsifier

⛔ **Nothing here starts.** Order is chosen so that **the step that makes every later failure legible
lands first**, and so that instrumentation lands in the same commit as the route it watches.

### B1 · One resolver for *"can I check?"* — the class fix
- **What ships.** One shared helper returning `ok · empty · unknown`, adopted by `/homes/`,
  `/settings/account/` and `/estate/`. `estate/index.html:457–468` has already solved this correctly
  with three empty states; **this generalises that fix rather than inventing one.** ⛔ Not a new
  resolver for trust state — ux F7 stands; this resolves *"did the request answer"*, nothing more.
- **Who / reversible.** Agent · fully reversible · touches three files, no Worker change.
- **Why first.** It is the only step that costs nothing and removes the lie **before** the door
  exists. It also makes B2's failures readable while B2 is being built.
- ⛔ **Falsifier.** With `/api/*` blocked in devtools, load `/homes/`, `/estate/`, `/settings/account/`
  and `/settings/place/`. **Every one says *I couldn't check*; not one says *you have nothing*.**
  If any surface still renders an unverified absence, B1 did not land.

### B2 · Route the sign-in door so a clean device can reach it
- **What ships.** The routing test at `onboarding/index.html:1889` stops being device-local. A device
  with no `fw-username` and no working grant meets a screen offering **both** *sign in* and *set up* —
  ⛔ not a guess about which one they are. The door itself (`s-nolink`, `:325–344`, wired `:981–1030`)
  already exists and is unchanged.
- **Who / reversible.** Agent builds, **Paul walks** · reversible · one routing condition, one view.
- **Constraints, all already ruled and not re-decided here.** One generic failure message
  (`/api/session` returns one shape on purpose — a distinguishable pair is a username oracle) ·
  `autocomplete="current-password"` on the sign-in form, `new-password` only on create ·
  ⛔ **it must not be reachable before first paint** (ux F1a) · ⛔ **exactly one account-creation
  surface** — link to `onboarding/`, never a second form.
- ⛔ **Falsifier.** Create an account. Clear all site data. Open the origin in a clean context. **Sign
  in and land in your place, with its name, its address and its ranking, without a link and without
  asking anyone.** That is `.plans/2026-09-07-sign-in-door-PROPOSAL.md` §1.4's promise, tested rather
  than asserted. If it needs a link, B2 did not land.

### B2i · The failure record, in the same commit as B2 — ⛔ not after
- **What ships.** A `door_failed` write on a failed **sign-in**, and a reader that separates *locked
  out* from *never wanted in*. The machinery exists (`storeDoorRecord`, its own rate bucket,
  `ctx.waitUntil`); `watch-door.py` is the reader pattern and its rule is the constraint —
  **it reports what happened at a door, never who was standing at it.**
- **Why the same commit.** `relayed-measured`: 20 reached, 0 through, and nothing distinguishes the
  two outcomes because `personId` and `deviceId` are null by construction. Ship the route without the
  reader and the lockout is invisible again, which is the shape this project has now recorded four
  times. ⭐ **An event with no reader is not instrumentation** (`CLAUDE.md`, TIER 2 · 13).
- ⛔ **Falsifier.** A wrong password on QA leaves a `door:<date>` row with a reason, a right one does
  not, **no `personId` is stamped on a failure**, and the reader prints the two classes apart. If the
  reader prints `0` where the route did not exist, that is `UNREADABLE`, not zero.

### B3 · A front door at the origin — ⛔ gated on D2
- **What ships.** Whatever D2 rules. If (i): the app's empty states carry the way in and `index.html`
  is untouched. If (ii): `/` serves the shelf. If (iii): a door page, **and F1a is explicitly
  re-ruled in writing.**
- ⛔ **Falsifier.** A clean browser at the bare origin. **The first screen tells a person who has been
  here how to get in, and a person who has not what this is** — without either of them typing a path.

### B4 · The shelf becomes the way in — ⛔ gated on D3, D5
- **What ships.** (a) A row opens **the app**, one tap (`homes/index.html:201` today opens `/estate/`).
  (b) The empty state is only rendered on a **verified** empty — B1 is a hard prerequisite.
  (c) The no-grant empty state names the door instead of an invitation link.
  (d) ⛔ The page never says *"Signed in as X"* over *"open your invitation link"* again.
- **Constraints already ruled, carried unchanged.** A row does **one** thing, enter the home (that is
  what keeps "back" a word rather than a stored origin) · never the full street address · no counts,
  no badges, no content on the shelf.
- ⛔ **Falsifier.** Signed in with one home: **one tap from the shelf to the app.** Signed in with a
  rejected credential: the shelf says it could not check and offers the door. Never both messages at
  once.

### B5 · Retire the place page — as a **transfer** ⛔ gated on D3, D4
- **What ships.** The receipts (`Where it is` · `How to reach you` · `What I'll build first`) move to a
  surface reachable from inside the app; `/estate/` stops being a stop on anyone's path. ⚠️ Its
  utility row is currently the **only** route to `/homes/` and `/settings/place/` for a person in the
  app who does not know the URLs — the app's own row (`viewer.html:19835`) must carry them before the
  screen goes.
- ⛔ **Falsifier.** From the app, without typing a URL: see your address, your contact choice and your
  ranking; reach both settings pages; reach the shelf. Then delete `/estate/` and repeat. Nothing
  becomes unreachable.

### B6 · Account settings tells the truth and can be edited — ⛔ partly gated on D6, D4
- **What ships.** (a) Email and phone **shown**, and shown as *unknown* rather than absent when the
  record could not be read — B1 covers this (`settings/account/index.html:203–212` hides them today
  behind `if (!d) return`). (b) Editable in place, if D6 says so. (c) *"Your colour"* → whatever D4
  rules (Paul suggested *"Your account colour"*). (d) ⭐ **The save failure names its system:** a
  rejected credential says *sign in again*; a transport failure says *your changes are still here*.
  Today both read *"That didn't go through"* (`:236–239`).
- ⛔ **Falsifier.** With a revoked grant, tap Save. **The message sends you to the door, not back to
  the form.** With the network off, tap Save. The message keeps your changes and says so.

### B7 · Sign out
- **What ships.** One control, on the account page. Clears the grant and the cached answers — ⛔ using
  the **same** clear list as `clearAnswers()`, plus `fw-onboard-coords` (see B8).
- **Why it is not cosmetic.** Asked twice in one evening (lap-3 capture F12), and it is the only way a
  person can *deliberately* reach the door — which makes it the cheapest test of B2.
- ⛔ **Falsifier.** Sign out, then sign back in, and land in your place. Sign out and check
  `check-storage-keys.py`: **no rostered key survives that should not.**

### B8 · The stale-coordinate hole behind the contradicting card
- **What ships.** `clearAnswers()` (`onboarding/index.html:1063–1065`) adds `K_COORDS`, and the
  `estate` card renders from the reconcile rather than ahead of it. **`measured` from source:** the
  clear list omits `fw-onboard-coords` while `:1069` advances the owner stamp — so after a credential
  change `mine` is true, `placed` is true from the **previous** grant's coordinates, and every
  receipts row is empty. That is Paul's *"your place is set up… nothing here yet… the rest fills in"*,
  in the page's own reading order.
- ⚠️ The file already names three defects in this block and calls the third *"still open"*
  (`estate/index.html:291–299`). **This is a fourth, and it is not in that list.**
- ⛔ **Falsifier.** Set up place A; sign in as B on the same browser; **B's card never says "your place
  is set up"** and never shows A's rows. Run it both ways round.

### B9 · The two copy moves that cost nothing and were earned on this build
- **What ships.** (a) **The PO-box sentence moves to the moment of asking.** It is written, it is the
  best thing in the product, and it currently arrives *after* the confirm — *"the app knew my address
  wasn't a location, and waited until I had committed to say so"* (`strict` seat, `assumption`).
  (b) **`Does that look right?` gets a subject**, by reusing `WHERE IT IS` from the very next screen —
  *"the app already knows how to say this. It says it one screen too late"* (`owner` seat,
  `assumption`).
- ⚠️ **Both are content-steward's words, not an agent's.** This step is *where and what*, never *how it
  reads*.
- ⛔ **Falsifier.** A seat entering a PO box meets the caveat **before** it taps confirm, and a seat
  reading the confirm card can say in one sentence what it is confirming.

### B10 · Recovery — ⛔ gated on D1
- **What ships.** Whatever D1 rules. The affordance is a slot with one rule: **it must name the real
  route.** ⛔ No *"Forgot password?"* with nothing behind it.
- ⛔ **Falsifier.** A walk seat that chooses *"Please don't"*, loses its password, and gets back in. If
  it cannot, D1's ruling did not cover the branch the product ships. `relayed-measured`: that branch
  is **unexercised by anyone, synthetic or real** — `read-onboarding.py` reports zero
  `onboard-contact` answers in every environment.

### Ordering, stated once

**B1 → B2 (+B2i) → B7** is the smallest sequence that closes the finding Paul hit, and every one of the
three is independently shippable. **B8** can land any time and is a two-line change with a real
falsifier. **B3, B4, B5, B6, B10** each wait on a ruling in §2. **B9** waits on content-steward.

---

## 4 · Files touched

⛔ **NOTHING IS TOUCHED BY THIS DOCUMENT.** This declares what a build would touch, so the blast radius
is visible before it is authorised. Every row is gated on §2 or §3.

- `homes/index.html` — B1 (three states), B4 (row destination, empty states)
- `onboarding/index.html` — B2 (the routing test at `:1889`), B8 (`clearAnswers`), B9 (copy placement)
- `estate/index.html` — B1 (already correct; the pattern source), B5 (retire), B8 (render from reconcile)
- `settings/account/index.html` — B1, B6, B7
- `viewer.html` **and** `engine/viewer.template.html` — B5 only, and **both or neither**
  (⚠️ `build-viewer.py --check` is a byte comparison and does not parse JS; `check-data-inline.py --fix`
  writes instance values over engine placeholders — `CLAUDE.md`'s own two traps)
- `worker/worker.js` — B2i (a `door_failed` write on a failed sign-in); **and, only after the privacy
  seat re-runs**, the rate-limit bucket and Origin-scoped ACAO on `/api/session` and `/api/account`
- `tools/journey-walk.py` — a seat that arrives with a **revoked** token, and one that refuses contact
- `tools/watch-door.py` — the reader for B2i
- `tools/check-storage-keys.py` — any key B7 clears or B2 writes must be rostered
- `RELEASE_NOTES.md` — B2, B4, B6, B7 are all user-facing
- ⛔ **NOT touched, by rule:** `BACKLOG.md`, `PRODUCT-ENGINE.md`, `VOCABULARY.md` — a ruling goes in the
  register **by Paul**, and §2 is exactly that.

---

## 5 · Falsifier — for the design as a whole

Each is an observation and how it is measured. A build that cannot fail these has not been tested.

- **A person is told something is absent that the product never checked.** Measured: `/api/*` blocked,
  every surface loaded. If any renders `empty`'s words on an `unknown`, the whole premise of B1 failed
  and nothing downstream is trustworthy.
- **A returning person on a clean device cannot reach their place without a link or a person.**
  Measured: the B2 falsifier, run cold. This is the single finding the lap turns on.
- **A locked-out person is invisible to the record.** Measured: a wrong credential on QA produces no
  `door_failed`, or the reader cannot separate it from a decline.
- **Two account-creation surfaces exist.** Measured: `grep -c 'new-password'` returns a form outside
  `onboarding/`. If true, B2 was built as a copy and the divergence has started.
- **The receipts died with the screen.** Measured: after B5, a person in the app cannot see their own
  ranking. If true, the transfer was a deletion.
- **The door reached the glance.** Measured: `check-glance-ungated.py` (⛔ **declared in C6 and does not
  exist** — building it is part of B3, not an assumption) logs any Worker request before the
  first-paint marker, signed in or out.
- **This document is ceremony.** Discharged in a `## Retro`: the parts that exist only because
  something was executed rather than recalled — today the `:1889` routing test, the four
  `show("s-nolink")` sites, `clearAnswers`'s omission of `K_COORDS`, and the absence of any harness
  stop for a rejected credential. **Zero at retro is a valid, informative answer.**

---

## 6 · QA

**An agent may exercise, and where.** Nothing in this document was exercised: every claim is a read of
the working tree, cited to file and line in `.user-research/2026-09-08-setup-journey-map.md`'s evidence
log. ⛔ **The build is frozen at `13b98a4` for a walk and any commit expires the gate ① evidence** —
no step in §3 opens until the freeze lifts. When it does: QA Worker and QA origin only, at
**414 × 848 × A+** (`herConditions()`), never `main`. On production, permanent: read-only.

**Agent may NOT:** mint or hold a credential outside `/secrets`; word any screen a person reads; choose
the recovery option; write a `- ready:` stamp; write a ruling into the register.

**Paul verifies:** D1–D6 before the steps they gate; the B2 falsifier on his own device, cold, with a
cleared browser; the B4 one-tap claim; and `check-live.py --wait 180` after any shipped surface.

**Presence of a person.** ⭐ **One, and it is the reason this file exists.** Paul's own walk on
2026-09-08 is the only real-person evidence in this plan, and it covers stages 2, 3, 12 and 13 of the
journey. Stages 14–16 have never been walked by anyone, synthetic or real. ⛔ Everything else is a
synthetic seat, which is `assumption` permanently and cannot be promoted by adding runs.
