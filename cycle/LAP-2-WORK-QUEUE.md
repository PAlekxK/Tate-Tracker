# LAP 2 — THE WORK QUEUE `[paul-stated 2026-09-07 ~11:40 ET]`

- kind: queue
- objective: O5 (the loop is the artifact) · lanes cite their own
- ready: paul-approved 2026-09-07 — *"Go ahead on all of that. Set up a queue and work through it."*
- gate: ⛔ This file RANKS and TRACKS. It decides nothing. Every row cites the ruling that put it here.

**Occasioned by** Paul opening lap 2 across four parallel windows: *"there's a lot of work streams
coming up so I authorize you to spawn up new sessions and launch new windows to focus on individual
pieces… and obviously have all the windows check in with their peers as we go to keep alignment."*

---

## THE LANES — territory is the contract

Four windows. **The dividing line is app surface / deploy**, because the release loop is serial by
construction (deploy → walks → gate ① → Paul walks `home` → Paul clears) and a deploy mid-walk
contaminates the walk. Everything that touches app surface queues behind **A**.

| lane | window | territory (the ONLY paths it commits) | deploys | tree |
|---|---|---|---|---|
| **A** | main session | `worker/`, `engine/`, `viewer.html`, `estate/`, `homes/`, `instance/`, `onboarding/` | **yes — sole deployer** | `~/Developer/Tate-Tracker` (owner) |
| **B** | tab | `tools/`, `.plans/*` headers, `cycle/release/CYCLE-MAP.md` | no | worktree `lap2-machinery` |
| **C** | tab | `tools/watch-*.py` (new), `.private/` | no | worktree `lap2-watcher` |
| **D** | tab | `PRODUCT-ENGINE.md`, `OBJECTIVES.md`, `BACKLOG.md` §pointers | no | worktree `lap2-planrecord` |

### ⛔ THREE RULES THAT ARE NOT NEGOTIABLE

1. **`git commit -- <paths>` always.** A bare `git commit` in this repo has committed another
   session's work **three times** (8/28, 8/29, 9/06) and *explicit staging did not protect it* —
   the COMMIT must be scoped. Memory: `feedback_git_add_all_in_shared_repo`.
2. **`cycle/release/cycle-state.json` belongs to lane A and to the hook, nobody else.** The
   post-commit hook does `cd "$(git rev-parse --show-toplevel)"`, so it rewrites *each worktree's*
   copy on every commit. B · C · D restore it before every commit:
   `git checkout -- cycle/release/cycle-state.json`. It must never ride back in a merge.
3. **Lane A declares walk windows.** While a walk is running, nobody merges to `main` and nobody
   deploys. `--fresh --watch` on every walk; wait for the edge after a QA deploy.

---

## THE QUEUE — ordered, and the order is Paul's

> **⭐ Paul reordered this himself 2026-09-07:** *"where did we land on the product owner — that may
> be something good to prioritize in the beginning because it'll help guide everything else that we
> do as well."* So B1 and D1 lead. W0 is unchanged as lap 2's first *build*
> (`cycle/release/CYCLE-LOG.md`, *"Go on geocoding as lap 2's first build"*).

| # | lane | item | cites | state |
|---|---|---|---|---|
| **B1** | B | **`product-steward` trial, one lap** — citation-bound carrier: writes a row only where it can cite a ruling by `file:line`; opens a question where it cannot. **Joins every synthetic review** as the reader/consolidator of the four seat reports. | R7→C, `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §0 · §6.4 · Paul 2026-09-07 *"product owner should also be a part of all our synthetic reviews"* | ▶️ next |
| **D1** | D | **Plan-of-record repair.** `BACKLOG.md:120` names § THE SEQUENCE as the plan of record for C4·C5·C6·C7; § THE SEQUENCE (`PRODUCT-ENGINE.md:95-108`) **names none of them** — its rows are fleet laps, conversation mines and an interview, and its one open row is 🟡 since 09-02. | AUDIT §0 status row *"Alignment 🟡 partial"* | ▶️ next |
| **C1** | C | **Account watcher — engine capability, not a Mom script.** `POST /api/account` (`worker.js:3184`) mints its person server-side and never touches `grants.json`, so a local reader sees nothing. Polls the Worker per estate/env. `est-e6696a` has **no reader at all**. | Paul 2026-09-07: *"we should have a watcher for her account set up"* → *"in general we need a watcher for new accounts that get setup"* · `BACKLOG.md:304` · steward design §A row e2 | ▶️ next (credential minting) |
| **A1** | A | **W0 geocoding.** Provider-pluggable, Census first, on `/api/profile` address save; `coordinates` on the grant/account row → whoami → `fw-onboard-coords` → `PROPERTY_DATA.location` before `SITE_PLACED` computes. Every placed consumer degrades on missing canon. | Paul: *"Go on geocoding as lap 2's first build"* · `.plans/2026-09-07-weather-card-PLAN.md` D1 | ▶️ now |
| **A0** | A | ⚠️ **Fixture probe BEFORE any UI.** Census returned **0 matches** for the mom fixture *"1420 Ridgecrest Dr Apt 3B, Roswell, GA 30075"* (measured 12:50 ET). Probe all four `.private/walk-answers/*.json` + Paul's real condo address. **A seat that cannot be placed cannot exercise W0.** | handoff §3.3 | ▶️ now, blocks A1 |
| **B2** | B | **R2 — `home..qa` divergence instrument.** `qa-divergence.py:35` is hardwired to `origin/main..origin/staging`, a different pair. Report the **pair of shas**, not a count. | R2→yes, AUDIT §0 | queued |
| **B3** | B | **`walk-brief.py` cannot see the place card at stop 12** — readers cite the PNG. Wanted *before* lap 2's readings. | handoff §7 | queued (feeds A) |
| **B4** | B | **R5 — bound the readiness header parse** to the block before the first `##`. Count what it would drop before cutting. | R5→yes → engineering-partner | queued |
| **B5** | B | **R4 — `kind:` key for non-item docs + add `draft` to `STAGES`.** | R4→B+`draft` | queued |
| **C2** | C | **Six-beat consolidation loop**: sweep → label → **Paul disposes** → researcher reads → carry to a row → arm. Only beat 3 is Paul's. | `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md` | blocked on C1 |
| **E1** | A *(queued behind A1)* | ⛔ **`homes-second-home` posts a CONSTANT id** (`homes/index.html:243`); `worker.js:3082-3085` returns 200 `{duplicate:true}` and the screen shows success. **The second "Add a home" on any UTC day is silently dropped while capture says it landed.** *Capture must not lie*, inverted. → engineering-partner. | steward design §A.1 | app surface — queues behind A's clear |

### 🧨 SEEDED — an ADVERSARIAL seat `[paul-raised 2026-09-07]`

> *"I do wonder if there's a need for a malicious seat or antagonist… that's just trying to break
> things and in general cause havoc that will help us identify even more bugs that we're not
> expecting. Something to consider overall."*

**Not scheduled. Captured, sharpened, and sequenced after W0** — but it converges with a finding the
instrument already made about itself, so it is stronger than a nice-to-have.

**It is the harness gap the answers README named on its own.** §3.1: *"No seat can decline. No seat
can abandon. No seat can lie… These want a seat brief and a branchable harness, not a JSON file."*
Every current seat types its assigned literal and complies. An antagonist is the first seat whose
**control flow** differs, not just its strings — which is exactly the missing rung.

**It already has a proof case, `measured` today.** Row **E1** — `homes/index.html:243` posts a
CONSTANT id, `worker.js:3082-3085` returns 200 `{duplicate:true}`, and the screen shows success. *A
seat whose job is "do it twice, do it fast, do it wrong" finds that in one move.* Four polite seats
walked past it for days; it took a steward reading KV by hand. That is the class of defect this buys.

⛔ **THREE CONSTRAINTS, and the first one is what makes it safe to build:**

1. **IT MUST NEVER ENTER GATE ①.** `release-gate.py` requires **zero failed actions** per seat. An
   antagonist's *purpose* is to produce failed actions — wire it into the gate and the gate can never
   go green again. It is a **non-gating instrument**: its findings feed the backlog, never the
   release decision. (Same reasoning that keeps the `product-steward` out of the walking roster.)
2. **QA and `lab` origins only. NEVER `home`, never Mom's page.** Rate-bounded. "Cause havoc" is
   scoped to *input space* — malformed, boundary, unicode, overlong, double-submit, back-button,
   rapid repeat, out-of-order steps — **not** load, not the store, not a credential path.
3. ⚠️ **It does NOT close §3.3.** The class no synthetic seat has ever produced — *questions about
   the model* — comes from someone with **stake**, and the README is explicit that it *"does not
   close by adding seats, adding answers, or adding runs."* An antagonist finds what is **wrong**;
   it still cannot find what is **missing**. Do not let it be sold as gate 2.5.

**Where it goes:** after W0 clears. It needs the branchable harness first, so it pairs with whatever
lane B learns building the review consolidator. Paul rules whether it is lap 2 or lap 3.

### 📓 SEEDED — TWO CLASSES OF RELEASE NOTES `[paul-raised 2026-09-07]`

> *"We should have release notes. And there are probably two classes… one is general updates to the
> overall system, and then there are individual updates to households or estates. So there's probably
> multiple release logs — one kind of overall for the estate manager, then release logs for each
> individual estate."*

**MEASURED THE SAME MINUTE, and it turns this from tidiness into a hole being filled:** the household
build (`instance/qa.json`) inlines **0** `RELEASE_NOTES_DATA` entries. There is exactly one log,
`RELEASE_NOTES.md`, and it is Fernwood's — correctly excluded from a household build, which means
**every household today has no changelog at all.**

⛔ **That breaks a load-bearing assumption already written into `CLAUDE.md`.** The acknowledgment
ribbon is ATTRIBUTION, not information, and the reason it is allowed to be is stated outright:
*"The ribbon therefore never has to inform; that job is already taken"* — by the Recent updates card.
For a household, that job is taken by **nothing**. The ribbon's whole design rests on a changelog
that does not exist on the surface the ribbon appears on.

**The split maps onto machinery this repo already has, which is why it is cheap:**

| log | scope | who reads it | what belongs in it |
|---|---|---|---|
| **ENGINE** | the product, all estates | everyone, identical text | the door got faster · you can name your place · a picker that shows your colour |
| **INSTANCE** | one estate | only that household | added the yellow flag iris · Mom confirmed the hydrangea · the Bolores service entry |

⭐ **`ENGINE-MANIFEST.md` already classifies every tracked file `engine` · `config` · `instance`, so
the routing rule already exists** — a change's class decides which log it lands in. This is the same
classifier lane B is being asked to define once for app-surface (R2 / qa-behind), so the two should
almost certainly share it rather than mint a third opinion about what "engine" means.

⚠️ **And the estate-neutral rule is the hard constraint:** an instance log must never reach another
estate's build. Today that holds by construction (0 entries) — but the moment per-estate logs exist,
`check-estate-neutral.py` needs a row for them, or Fernwood's plants end up in Bob's changelog.

**Open, and Paul's:** does a household see BOTH logs (engine + its own, interleaved or separate), or
only its own? Neither is obviously right — a household that never sees engine notes cannot tell an
improvement from a thing that was always there; one that sees all of them reads product-release noise
on a field journal. **Not scheduled; it is not lap-2 work.** Sequenced after the "placed without
canon" design, because both are questions about what a household surface IS.

### Discharge at lap close — pre-registered, from lap 1

| id | question | state |
|---|---|---|
| `instrumented-counted` | at the lap-1 candidate sha, does every seat's `capture.json` show ≥1 app event via grant? | open |
| `second-viewport` | does a laptop-width walk find what 414 hides (Paul found one 2026-09-06)? | open |

---

## ⏳ THE SUNSET CLOCK — frozen, and the acts it obliges `[paul-decided 2026-09-07 12:36 ET]`

> *"Mom and I just discussed and agreed that the current full Fernwood will remain live for her to be
> able to check the weather for 24 hours… a banner at the top of that page with the 24 hour countdown
> running until the site gets shut down, and a reminder to set up her profile in the new production
> environment. That's a frozen decision. We're not going back on it and it helps us with all of our
> sequencing as well."* Then: *"start the clock now, shutdown means redirect to the new origin"* →
> *"redirect to mom's account page, but we keep all the data for reference. So mom loses access, we
> still can access the info."*

**DEADLINE: 2026-09-08 13:00:00 EDT · epoch ms `1788886800000`.** 24h from 12:36, rounded up to the
hour; she loses nothing by the rounding.

| # | act | owner | state |
|---|---|---|---|
| S1 | the banner + self-enforcing redirect on her live page | **lane E** (`prod-sunset` ← `origin/main`) | building |
| S2 | approve the exact copy — **it reaches Mom** | **Paul** | owed |
| S3 | `git push origin prod-sunset:main` — the classifier blocks an agent | **Paul** | owed |
| S4 | ⏰ **RE-SEND HER THE INVITE LINK near the deadline** | **Paul** | owed, **and nothing will remind him but this row** |
| S5 | W0 on production, so a placed household actually has weather | **lane F** → lane A | building |

⭐ **S4 is the one with no mechanism behind it.** Paul ruled the redirect lands on the bare origin —
`https://fernwood-home.pages.dev/` → `estate/`, which says *"Open your invitation link and your place
will be here."* That is honest and cannot dead-end her, but it depends on her having a link. Her
invite `p-b91e4d` was texted ~12:05 ET on 09-07 and is **still unspent**, so at 13:00 on 09-08 she
would be looking for a message a day old. ⛔ The link is a **live single-use credential and must never
appear on the public page**; re-sending it is therefore an outbound act only Paul can do.

⚠️ **The redirect target was MEASURED, not assumed** (lane E, three candidates): `/onboarding/` was
rejected because with no stored grant it renders the full account-creation form and then fails at
`POST /api/account` with `invite-required` 403 — *a form she can complete and be rejected by, at a
deadline*. The bare origin was chosen for that reason.

⛔ **NOTHING IS DELETED.** *"We keep all the data for reference."* Her records stay in the legacy
Worker (`est-3c9f1a`) and in git; the redirect removes her ACCESS, not the record. No surface may
imply erasure, and the frozen page remains the **data control** the 09-06 ruling made it.

## OPEN — PAUL'S, NOT A BUILD

- ✅ **RULED 2026-09-07:** the freeze's *"hold all Mom's feedback"* was written for the **frozen**
  estate; her arrivals on the **new** one (`est-e6696a`) get a watcher. Generalized by Paul the same
  minute to **all new accounts**. → C1.
- ✅ **RULED:** reader credential — option **A**, a dedicated reader seat, mode-600, revoked at lap
  close. (**B** was refused for cause: `grant-mint.py:267` `--rotate` *revokes* the live credential,
  which is Paul's own production session.) **C** — a genuine read-only capability in the engine —
  stays the right long-term shape and is engine work under O3.
- 🔴 **STILL OPEN:** nothing narrower than `administrator` can read (`worker.js:3460-3467`). Until
  the O3 read-only capability exists, every reader is an administrator. That is the standing cost.
