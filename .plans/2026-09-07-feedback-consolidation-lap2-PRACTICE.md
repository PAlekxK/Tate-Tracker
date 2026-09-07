# FEEDBACK COLLECTION & CONSOLIDATION — the loop between a CLEAR and the next BEAT 1
`(practice-steward, 2026-09-07, DESIGN with a short audit)`

- kind: design
- ready: agent-proposed — Paul rules
- cites: `cycle/release/CYCLE-MAP.md` · `cycle/release/CYCLE-LOG.md` · `.plans/2026-09-06-release-loop-PRACTICE.md` · `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §6 · `~/.claude/rituals/CYCLE-SPINE.md`

**Method only.** Every claim is graded `measured` (I ran or read it today) · `inferred` · `assumption`
· `proposed`. **Nothing here ranks one finding against another, and nothing here decides what a card
should say.** Where the design needs a content call, it names the gate and stops.

Occasioned by Paul at 11:50 ET: *"I think we are good to green light this as our first full approved
production build"* → *"let's have the process steward check in here to mark how we collect and
consolidate feedback for the next build cycle."* Two later inputs are treated as stated requirements
(§C.3, §C.4, §C.6).

---

## A · THE INVENTORY — every channel that produced feedback today

`measured` unless marked. "Reader" = a deterministic tool that can read it without a model.

| # | channel | producer | store | deterministic reader | who consolidates | derived vs typed | measured today |
|---|---|---|---|---|---|---|---|
| **a** | in-app + onboarding feedback, **production** | Paul in a browser → `POST /api/feedback` (ungated, `worker/worker.js:3168`) | KV `est-e6696a:feedback:YYYY-MM-DD` | ⛔ **NONE.** `GET /api/feedback` exists (`worker.js:3090`) but needs the master token or an administrator grant (`worker.js:3460-3467`); **`.private/fernwood-token-home` does not exist** | a human, by hand, this once | raw records; the log's summary is typed | **10 records**, 2 runs (14:22Z, 15:17Z), 3 record classes |
| **b** | synthetic seat readings | `journey-walk.py` + one fresh agent per run | `.private/synthetic-walks/<seat>/<run>/REPORT.md` | `walk-integrity.py` (countability), `release-gate.py` (per-sha) | ⛔ **nothing** — a human reads 4 files per round | countability derived; **findings are prose, uncounted** | **34 runs** today · 31 REPORT.md · **11 still `WALK-REPORT-UNWRITTEN`** · 3 runs with no report file · corpus 124 runs / 63 countable / 61 refused |
| **c** | Paul's spoken beat-3 findings | Paul, dictated mid-walk | `CYCLE-LOG.md` verbatim, **only there** | ⛔ none | the session that heard him | hand-typed | 4 beat-3 failures, each re-entered beat 2 (`CYCLE-LOG.md:622,646,680,706`) |
| **d** | onboarding metrics | `POST /api/onboarding-metrics` (`worker.js:3296`) | KV `…:onboarding-metrics:<date>` | ⛔ **write-only — no GET handler anywhere in `worker.js`** | nobody | — | every seat's `capture.json` reported it UNREADABLE, 4 of 4 |
| **d2** | app events (the `instrumented` clause) | walker/app → `/api/metrics` | KV, per run id | ✅ `release-gate.py` clause 5 | the gate | **derived** | 4 of 4 seats, 5 events each at `c821051` |
| **e** | Mom's channels on **est-3c9f1a** (frozen) | Mom | legacy Worker | ✅ `read-mom-feedback.py`, `check-arrival-dispositions.py`, `read-mom-engagement.py` | `/mom-cycle` | derived + per-record dispositions (`arrival-dispositions.json`) | **all read `momlib.DEFAULT_WORKER_URL` = the legacy worker (`momlib.py:42`) = `ESTATE_ID est-3c9f1a` (`worker/wrangler.toml:31`)** |
| **e2** | Mom's arrivals on **est-e6696a** (the new product) | Mom, invite texted ~12:05 ET | KV `est-e6696a:*` | ⛔ **NONE — no loop watches this estate** | **nobody** | — | `BACKLOG.md:304` already says it in its own text: *"an estate no existing reader watches"* |
| **f** | BACKLOG rows | a session, by hand | `BACKLOG.md` | `check-backlog-ready.py`, `check-backlog-drift.py` | a session | typed | cites `cycle/release/CYCLE-LOG.md` **1×**; mentions today's 5 certified shas **0×** |

### A.1 · The labelling contract, measured per record class

Paul: *"the challenge will be correctly labelling all feedback so we know what to action on which
page and who was submitting feedback when."* Here is what the store carries today. `measured` from
the KV read.

| field | `onboard-*` (8) | `homes-second-home` (1) | `fb-*` general (1) |
|---|---|---|---|
| `personId` | ✅ | ✅ | ✅ |
| `estateId` / `env` | ✅ / ✅ | ✅ / ✅ | ✅ / ✅ |
| `ts` | ✅ | ✅ | ✅ |
| `sessionId` | ✅ | ⛔ null | ⛔ null |
| `deviceId` | ⛔ null | ⛔ null | ✅ |
| `context.surface` | ⛔ **absent** | ⛔ **absent** | ✅ `app` |
| `context.screen` | ⛔ absent (`step` only) | ✅ `homes` | ✅ `card-property` |
| producing control | inferable from `field` | inferable from `type` | ✅ `questionId` + `section` |
| **id is unique** | ✅ minted | ⛔ **CONSTANT** — `homes/index.html:243` posts `id: "homes-second-home"` | ✅ |

⛔ **The one that is not a labelling gap but a data-loss path, `measured`.** `worker.js:3082-3085`
is idempotent on a **client-supplied** id and returns HTTP 200 `{stored:0, duplicate:true}`;
`homes/index.html:245` reads that as `r.ok` and shows the success ack. **So the second person — or
the same person twice — using "Add a home" on any UTC day is silently dropped while the screen says
it landed.** This is the repo's own *capture must not lie* rule, inverted. → engineering-partner;
I do not design the fix.

---

## B · WHERE THE RECORD DISAGREES WITH THE WORLD

| # | the record says | the world says | grade |
|---|---|---|---|
| **B1** | `CYCLE-LOG.md:868` — *"the general-feedback record carries no `surface`/`screen`/`step` fields in the store as read"* | the `fb-*` record **does** carry `surface: "app"` and `screen: "card-property"`; the records missing `surface` are `homes-second-home` and all eight `onboard-*` | **measured** — the log names the wrong record class. The 9/06 ruling is **satisfied for general-feedback (1 of 1)** and unmet for the two classes it never covered |
| **B2** | `cycle-state.json` `last_lap.outcome: "cleared"` | the spine's closed enum is `closed \| open \| abandoned` (`CYCLE-SPINE.md` S1 amendment) | **measured** — a fifth dialect. S4's predicate reads the enum first, so this loop falls to fail-closed prose matching. One-word fix; **naming which word is Paul's or the spine's, not mine** |
| **B3** | `cycle-state.json` `pre_registered[]` holds **2** items | `CYCLE-LOG.md:826-846` lists **9** pre-registrations for lap 2 | **measured** — the machine-readable half is 2/9. Nothing derives one from the other |
| **B4** | `release-gate.py` docstring: *"it never prints a bare pass while a clause is uncheckable"* | now true of the **exit code** too — 🟡 at `c821051` exits **1** | **measured, and it is a discharge**: U1 of the 09-06 ruling is closed |
| **B5** | the loop's evidence is per-sha and expires when the build moves | **11 of today's 34 runs were never read** — 4 at `ca9161e`, 3 at `e60d691`, 4 at `5727efe`. Their screens largely shipped | **measured** — expiry is correct for the *gate*; it is not a policy for the *evidence*, and today none exists |
| **B6** | `read-onboarding.py` is in the session-start block as the reader of what people said at setup | `--env home` is **UNREADABLE by construction** — `TOKENS["home"]` points at `.private/fernwood-token-home`, which does not exist. It exits 3, never "0 answers" | **measured** — the tool is honest; the door is absent |
| **B7** | `PRODUCT-ENGINE.md` § THE SEQUENCE is the plan of record | flagged 🟡 by the flex-point audit's status grid; its one open row is *"Agile PM artifacts"* — this question | **measured** by that audit (`.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §0) |

⚠️ **B2 and B3 are the same shape as B5:** a value that only exists because a person typed it beside
a tool that could compute it. I report all three; **which one to fix first is not mine.**

---

## C · THE DESIGN — the FEEDBACK LOOP between a clear and the next beat 1

### C.0 · What this loop is, and what it is NOT

The release loop exits at beat 5 and **has no successor.** `measured`: `CYCLE-MAP.md:43-51` ends at
*"PAUL CLEARS IT"*; nothing in the map, the state artifact or the tooling names what happens to the
words a real person left on the way through. Today those ten records were read because Paul asked.

⛔ **It is not a second release loop and it does not decide what gets built** (`CYCLE-MAP.md:145`).
It converts **arrivals into dispositioned rows**, and hands beat 1 a *candidate set*, never a
ranking.

### C.1 · The map — six beats, drawable

```
   ┌───────────────── the release loop (beats 1–5) ──────────────────┐
   │  build → seats → Paul walks → fix → PAUL CLEARS  ───────────────┼──▶ F1
   └─────────────────────────────────────────────────────────────────┘        │
                                                                              ▼
 F1 SWEEP ──▶ F2 LABEL ──▶ F3 DISPOSE ──▶ F4 READ ──▶ F5 CARRY ──▶ F6 ARM ──▶ beat 1
 (machine)     (machine)    (👤 Paul)      (seats)     (citation)   (machine)
```

| # | beat | actor | reads | writes | exit condition |
|---|---|---|---|---|---|
| **F1 · SWEEP** | machine | `feedback-sweep.py --env home --since <cleared_sha date>` → `GET /api/feedback` | `.private/feedback-sweep/<env>-<date>.json` (verbatim stays in `.private`) | every household env answered or **UNREADABLE** (never "0") |
| **F2 · LABEL** | machine | the sweep file + the register | a per-record label row (§C.5) | every record carries the six required keys, or is listed as **unlabelled** |
| **F3 · DISPOSE** | 👤 **Paul** | a one-screen list: who · when · which screen · what they said | `feedback-dispositions.json` (repo root, **no note text**) | **every record has its own disposition** — act · fold · hold · not-a-finding |
| **F4 · READ** | `user-researcher` (+ the carrying seat, §C.6) | only records Paul dispositioned `act` or `fold` | a dated brief in `.user-research/` | the brief exists and cites record ids |
| **F5 · CARRY** | citation-bound seat / main session | the brief + `CYCLE-LOG.md` rulings | BACKLOG rows / plan stage-notes, **each citing a `file:line`** | every `act` record reaches a row or an open question |
| **F6 · ARM** | machine | dispositions + `cycle-state.json` | `state: ARMED`, `pre_registered[]` for lap 2 | **zero undisposed records** → the next beat 1 may open |

**Beats F1, F2 and F6 are deterministic and must be runnable with no model in the loop** — Paul's
non-AI-door rule. F3 is the only human gate. F4 and F5 are where seats belong.

### C.2 · The trigger that fires lap 2's beat 1 `proposed`

**A clear is not a trigger; an undisposed arrival is a blocker.** Two conditions, both computable:

1. **F6 is green** — no record in the sweep window lacks a disposition. *(Fail-closed: an unreadable
   env is not green.)*
2. **HEAD ≠ the served production sha** *or* a `fold`-dispositioned record has reached a row.

⭐ **Why the blocker, not a cadence:** this loop rests, like every other one here. The thing that
must never happen is beat 1 opening over an unread arrival — that is the 2026-07-26 rainfall failure
(*capture is not a loop*) reproduced on a new estate. `proposed`.

⚠️ **What it must NOT do:** it may not compute a lap age, and it may not say a lap is late. Paul's
standing rule.

### C.3 · The deterministic door `[paul-stated 2026-09-07, ~12:10 ET]`

> *"Production store feedback needs to be accessible for backlog seeding, rationalization, quality of
> life improvements."*

**Ruling on method:** the door is a tool, not a seat. `tools/feedback-sweep.py`, modelled on
`read-onboarding.py`'s three honesties — a declared token per env, **exit 3 UNREADABLE when a token
or a store cannot be reached, never "nothing came in"**, and a `--json` for other readers.

`measured` blockers, both real and neither mine to fix:
- **`.private/fernwood-token-home` does not exist.** Until it does, no tool can read production.
- **`GET /api/feedback` resolves the estate from the DEPLOYMENT, not the caller's grant**
  (`worker.js:3479` passes no grant; the handler keys on `scopeOf(env)`, `worker.js:3113`). So a
  sweep is **per-env**, and the day two households share one Worker it will read one of them and
  look complete. → engineering-partner. `inferred` on the second-household consequence.
- ⚠️ **A live administrator credential on production belongs to a verification seat** (`p-vfy`,
  `CYCLE-LOG.md:617`). **The sweep must not be built on it** — a tool whose door is a leftover seat
  token is a tool that dies silently at the first revocation.

### C.4 · The sweep and where dispositions live `[paul-stated 2026-09-07, ~12:15 ET]`

> *"An automatic feedback check for production that sweeps all accounts… like we had for the mom cycle."*

**Copy the mom-cycle shape exactly, because it is the one that has been proven to fail correctly:**

| borrowed from | rule it carries |
|---|---|
| `check-arrival-dispositions.py` | ⭐ **the disposition is keyed by (channel, record id)** — a batch may never be cleared by one of its members (`CLAUDE.md`, the 2026-08-28 ruling) |
| `read-mom-feedback.py` | the watermark is **clamped below the oldest still-actionable record**, so advancing it can never bury one |
| the Mom-check counter | it prints **one line every run, quiet days included** — *"a quiet watcher and a dead one are indistinguishable in a log"* |
| `feedback-log.json` | the register records **where a record went, never what it said** — this repo is public |

**Where they live** `proposed`: `feedback-dispositions.json` at the repo root beside
`arrival-dispositions.json` (tracked, no note text); the verbatim stays in KV, and any local cache in
`.private/`. **Siting reason:** the disposition is a fact about our own conduct and belongs in the
tracked record; the words are the person's and belong where the AI boundary put them.

⛔ **What the sweep may never assert.** It reports `personId` and the register's mapping when one
exists, and **nothing else about who that is.** `measured`: Paul is **three ids** today —
`p-7f3a2c` and `p-paul` in the register, `p-lnxakyzniuwk` and `p-yjnw9lt41nww` minted by two account
creations (`CYCLE-LOG.md:797`; both ids appear in the store). Any tool that collapsed those into "a
person" would be authoring an attribution. It prints the ids and the divergence; a human names the
human. Same clause as *a deviceId is a browser bucket, not a person.*

⛔ **And the AI boundary is unchanged and binds F1–F3.** *"AI never touches an estate's people or
their words… the administrator's eyes sit between the model and the estate's people, both
directions."* So: the sweep is **deterministic** (no model reads the store to decide what matters);
**Paul dispositions before any seat reads**; and no model output derived from a person's words about
themselves leaves `.private/`.

### C.5 · The labelling contract every record must carry to be actionable `proposed`

Six keys. **Stated as a contract on the producing control, not as a validator that grades old data.**

| key | source | today (§A.1) |
|---|---|---|
| `personId` | grant, server-side (`attributeTo`) | ✅ 10/10 |
| `estateId` + `env` | grant / deployment | ✅ 10/10 |
| `ts` | server | ✅ 10/10 |
| `context.surface` | the producing control | **2 of 3 classes missing** |
| `context.screen` (or `step`) | the producing control | ✅ 10/10 in one spelling or the other |
| producing control id | the control | ✅ inferable 10/10; ⛔ **not unique** in one case |

**The check** `proposed`: a **coverage line, counted, never graded** — *"N of M records carry all
six"*, printed by the sweep. ⛔ **Not a gate.** A grade would read red on every record written before
the contract existed, which is the permanently-red alarm Paul forbids. **Falsifier:** if the coverage
line sits at 100% for two laps, delete it — it is measuring a solved problem.

### C.6 · The seats `[paul-stated 2026-09-07, ~12:10 ET]`

> *"Good opportunity for customer researcher and product owner to team up."*

`measured`: **`user-researcher.md` exists** in `~/.claude/agents/`. **No product-owner agent exists**
— the roster is `ai-advisor · business-analyst · career-coach · content-steward ·
engineering-partner · examiner-panel · practice-steward · user-researcher · ux-expert`.

**I am not minting one.** The product-owner half is already designed, by today's other steward run:
`.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §6.4 — a **citation-bound `product-steward` with no
decision authority**, whose falsifier is ≥80% duplication → build a check instead. **R7 is Paul's to
rule; this design defers to whatever he rules.**

| beat | seat | boundary |
|---|---|---|
| F4 · READ | **`user-researcher`** | what the words mean, JTBD, whether "Houseplants!" names a need the product never anticipated. **It reads only what Paul dispositioned.** It does not rank |
| F5 · CARRY | **`product-steward` if Paul rules R7 = C; until then the MAIN SESSION** | writes a row only where it can cite a `file:line`; opens a question where it cannot |

⚠️ **The honest part: until R7 is ruled, F5 has no owner and it is the beat that failed today.**
`measured`: BACKLOG.md cites `CYCLE-LOG.md` once and names **zero** of the five certified shas. So
the design's answer is *the main session holds it*, and F6 makes the residue **visible** — an
`act`-dispositioned record with no citation is an open question, printed, not a silence.

### C.7 · How a finding reaches BACKLOG.md or the next build's candidate set

One path, three destinations, and **the destination is Paul's at F3, never the tool's**:

- `act` → a BACKLOG row or an existing row's stage-note, citing the record id **and** the ruling.
- `fold` → the next build's **candidate set**, recorded in `cycle-state.json` `pre_registered[]` or
  a candidate list — *a set, not an order.* ⛔ **No tool sequences it.** Paul's words from the very
  ruling that started this: he alone has the real-world context.
- `hold` → a named release condition. *"Indefinite" is abandonment with manners.*
- `not-a-finding` → recorded as such, with what attested it. ⭐ **`nobody looked` and `we looked and
  it was fine` must never print the same.**

---

## D · S1–S6 CONFORMANCE OF THIS DESIGN

| | element | how this design satisfies it | residue |
|---|---|---|---|
| **S1** | state schema | it **reuses `cycle/release/cycle-state.json`** — one added key, `feedback: {swept_through, undisposed, unreadable_envs}`. ⛔ **No second state artifact and no fourteenth loop** | B2's `outcome: "cleared"` still off-enum |
| **S2** | ≥1 blocking human gate, machine-visible | **F3 is the gate**, published as `beat.owner: "paul"` — the key the boards render as *stopped ON YOU* | none |
| **S3** | ≥1 deterministic check seen to fail | the sweep's **UNREADABLE exit 3** and the **undisposed-record blocker**. Both must be proven by mutation before use — a missing token, and a record with no disposition. **Siting sentence:** *the check sits at F6 and not at F1, because a sweep that refuses to run tells you nothing about whether anyone looked at what it found.* Coverage, counted, never graded | selftest not built |
| **S4** | a closed lap is MARKED | this loop closes when F6 arms; recorded in the same `last_lap` dict | inherits B2 |
| **S5** | pre-registration | `pre_registered[]` is where `fold` records land — the key already exists and is already under-filled (B3) | 2 of 9 today |
| **S6** | the map parses / a non-AI door | ⚠️ **the beat table above uses `F1 · SWEEP`, which `render.py:832` cannot parse** (it wants `N · NAME` with a bare integer). **Either renumber 6–11 inside the release map, or accept it renders as prose and say so.** ⭐ **The right answer is to put these beats INSIDE `CYCLE-MAP.md` as beats 6–11 of the same loop, not a new map** | Paul's call: one loop with eleven beats, or two loops |

⚠️ **Enactment amendment check.** This design rules **no machinery** — it changes no spine key, no
comms declaration, no propagation mechanism. It is a **domain** change to one loop and adopts on that
loop's own next lap. Nothing to propagate. `measured` against `CYCLE-SPINE.md` § ENACTMENT.

⚠️ **And its own first residue, stated because that amendment's text demands it:** *a standard
travels on the execution path, not the reference path.* **This loop has a map and no skill and no
command.** If these six beats live only in a `.md`, the next session opens at beat 1 exactly as
health-record did. The carrier is `CLAUDE.md`'s session-start block plus the release map — **not this
file.**

---

## E · WHAT THIS DESIGN CANNOT SEE

| class | why |
|---|---|
| **anything on `est-e6696a` that is not `/api/feedback`** | observations, Guru turns, zone audio and the door all have their own KV keys and their own (legacy-only) readers. Mom's channel doctrine names four; this sweep reads one |
| **whether a disposition is TRUE** | `check-arrival-dispositions.py` says so of itself and it is a property of the idea: it checks a disposition **exists** and what attested it |
| **who a `personId` is** | three ids for one human today. The tool prints the divergence; it never resolves it |
| **the second household on a shared Worker** | `GET /api/feedback` keys on the deployment's estate (§C.3). It will read one and look complete |
| **a record the store deduped away** | §A.1's constant id. The sweep cannot count what never landed, and the ack said it did |
| **what a person did NOT say** | the same bound as the synthetic seats: this reads arrivals. Silence in the feedback store is not silence in the app — `read-mom-engagement.py` exists for exactly that on the frozen estate and has **no counterpart on `est-e6696a`** |
| ⭐ **whether the thing Paul wants is what a person needs** | this loop carries words to rows. It cannot tell a preference from a need, and it must not try |

---

## F · THE UN-TRIGGERED CLASS — found today, scheduled by nothing

| # | the thing | → trigger it wants | grade |
|---|---|---|---|
| **F-a** | **11 of 34 walk runs today were never read**; 3 have no report file at all. Their builds are superseded, so the gate will never ask again | a lap-close sweep that **lists unread runs and disposes each** (read · superseded-and-kept · discard). R2 of the 09-06 ruling remains open — it is in `CYCLE-LOG.md:840` as a lap-2 pre-registration | **measured** |
| **F-b** | **Mom's first arrival on `est-e6696a` is now possible and no loop watches it.** Her invite went by text ~12:05 ET; every mom-cycle reader points at the frozen estate | ⚠️ **This is a RULING Paul owes, not a build.** The mom-cycle freeze says *"hold all feedback from Mom… I will say when to lift"* — written for `est-3c9f1a`. Whether it binds the new estate is his word, and **the sweep must not decide it by existing** | **measured** |
| **F-c** | a `paul-ruled` entry lands in a chronicle and no row cites it | the flex-point audit §6.4 trigger 1 — the product-steward's first event | measured there |
| **F-d** | production feedback has **no reader at all**; today's read was a person with `wrangler` | §C.3 | **measured** |
| **F-e** | `pre_registered[]` holds 2 of the chronicle's 9 | the close step writes both, or derives one from the other | **measured** |
| **F-f** | the constant-id capture-lie (§A.1) | engineering-partner; and a positive control: **post the same control twice and assert two records** | **measured** |

⭐ **The shape all six share, and it is this corpus's oldest one:** *a writer with no reader.* The
store filled correctly ten times today; nothing was built to read it. `CLAUDE.md` records the same
shape four times, and `read-onboarding.py`'s own docstring calls it *"this repo's most repeated
defect."* **F-b is the dangerous member**, because when it happens the surface will look calm.

**Falsifier for this whole design:** if lap 2 closes with every arrival dispositioned *without*
anyone running F1 — i.e. a person read the store by hand again and it worked fine — then the sweep is
ceremony and the honest fix is a line in `CLAUDE.md`'s session-start block, not a tool.

---

## TEN LINES FOR PAUL

1. **The release loop has no successor beat.** It ends at your clear; nothing owned the ten records you left behind. Today they were read because you asked.
2. **Six beats close it:** sweep → label → **you dispose** → researcher reads → carry to a row → arm. Only beat 3 is yours; the rest are deterministic.
3. **Production feedback has no deterministic reader** — `GET /api/feedback` exists but `.private/fernwood-token-home` does not, so `read-onboarding.py --env home` is unreadable *by construction*. That token is the whole blocker.
4. **Your labelling worry is measured:** the place-card record carries surface + screen + account correctly (the log's note saying otherwise is wrong); the onboarding and "Add a home" records do not. Coverage line, counted — never a grade.
5. **One real bug underneath it:** "Add a home" posts a constant id, so the second use in any day returns *duplicate* and the screen still says it landed. Capture is lying. → engineering-partner.
6. **The sweep copies the mom-cycle shape** — per-record dispositions keyed by (channel, id), a watermark that cannot bury an unactioned record, a line printed every run including quiet ones.
7. **It may never assert who someone is.** You are three person-ids today; it prints the ids and the divergence and stops. The AI boundary holds: deterministic sweep, your eyes, then a seat.
8. **On your seat pairing:** `user-researcher` exists; **no product-owner agent does.** The carrying half is already designed as the citation-bound `product-steward` in today's other steward file (§6.4, ruling R7). Until you rule it, the main session holds that beat — and it is the beat that failed today: BACKLOG.md names none of the five shas you certified.
9. **What fires lap 2's beat 1:** not a cadence — an arrival left undisposed *blocks* it. No tool computes a lap age; none ever will.
10. **The one thing that needs your word, not a build:** Mom's invite is out, and the freeze that says *hold all her feedback* was written for the frozen estate. Whether it binds her arrivals on the new one is yours to say — and until you do, nothing watches for her.
