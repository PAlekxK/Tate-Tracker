# LAP 3 · BEAT 1 — CONSOLIDATION: every channel Paul's input arrives on, and which ones we can actually read

- row: process — no BACKLOG row, same posture as the lap-boundary PROCESS and the flex-point AUDIT
- objective: O5 (the loops are the artifact)
- kind: record
- class: engine · declared
- seats: none — this is a census of CHANNELS, not a review. No surface, no copy, no model, no person
  is studied here. Seats enter at beat 7, after Paul disposes.
- depends-on: .plans/2026-09-07-lap3-BRIEFING.md
- depends-on: .plans/2026-09-07-lap3-paul-feedback-CAPTURE.md
- depends-on: .plans/2026-09-07-lap3-paul-feedback-CAPTURE-2.md
- depends-on: .private/synthetic-walks/GATE2-paul-findings.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- stage: draft
- gate: ⛔ NOTHING HERE EXECUTES and nothing is ranked. This is a coverage census.
- stage-note: 2026-09-07 — written because Paul asked three things in sequence: *"be sure we're
  pulling in feedback from both of my laps"*, then *"I also submitted feedback within the website in
  the application, not just talking through it to your terminal — make sure you see that in all my
  telemetry and all that too, as much as that's possible"*, then *"if that's something we don't have
  and we need to add to our work, let's include all that in our consolidation and rationalization."*
  ⭐ **All three were right, and the first one found a live gap.**

---

## 0 · THE ANSWER IN ONE TABLE — four channels, not one

Paul's input does not arrive on one channel. It arrives on four, and **they have different owners,
different retention, and very different readability.**

| # | channel | what it holds | can we read it? |
|---|---|---|---|
| **A** | **He talks through a walk** — to the terminal, live | the reasoning, the rulings, the *why* | ✅ captured by hand into `.plans/…CAPTURE*.md` and the chronicle |
| **B** | **He types into the app** — note boxes, onboarding notes, the feedback box | what he wrote *in the moment, on the surface* | ✅ `tools/watch-feedback.py`, **no watermark by design** |
| **C** | **Behavioural telemetry** — what he did, not what he said | taps, sections viewed, text size served | 🟡 **partly**. See §3 |
| **D** | **The door** — arrivals that never became accounts | who reached the invite and stopped | 🟡 **readable by API, read by NO tool** |

⭐ **A and B are not redundant.** B is *"what he wrote while looking at the thing"*; A is *"what he
meant"*. This lap they happened to agree — but only because he said both out loud. **If he had only
typed them, they would have sat in the store, undisposed, until beat 6.**

---

## 1 · ⛔ THE GAP HIS FIRST QUESTION FOUND — both of his walks were missing from the register

`measured 2026-09-07`: `.private/synthetic-walks/GATE2-paul-findings.md` — the register whose stated
purpose is *"what Paul finds when he walks it"* — contained **neither `c821051` nor `1e2748d`**, the
cleared builds of release laps 1 and 2. Its most recent entry was a **2026-09-05** walk.

**Why it hid:** the file numbers its own laps, and that sequence collides with the release loop's.
Its `Lap 1` and `Lap 2` are both **09-05 walks that predate the release loop's lap 1 entirely**, and
its `## Lap 3 — (open)` heading made the file look current. It was current for a sequence nobody was
running. `[[reference_match_payload_not_container]]` — the container said *lap 3, open*.

✅ **FIXED this beat.** Both walks are now filed, under headings that name the **build** and the
**release lap in full**, plus a collision warning at the top of the file. The new rule: **a walk is
filed under the sha it walked.** A sha is unambiguous across every sequence in this repo; an ordinal
is not.

| | filed |
|---|---|
| **release lap 1** · `c821051` · 09-07 11:45 ET | *"OK I just went through and it looks pretty good!"* — **zero findings**, recorded as a row rather than an absence. ⚠️ Not evidence the build was better; it was taken right after three out-of-band repairs cleared his path |
| **release lap 2** · `1e2748d` · 09-07 evening | **15 findings (F1–F15)**, with the third column answered where the record supports it |

⛔ **Four rows are honestly UNANSWERED** — F7, F8, F9 (and F4's siblings are answered). The third
column asks *did any seat raise it BEFORE Paul?* and the only source that can answer it is the four
seats' walk `REPORT.md` at the lap-2 sha. ⚠️ **Grepping the panel reviews does not answer it** — those
seats were commissioned *after* his walk and were handed his findings, so a hit there is a seat
answering a question, not catching a bug. **That read is cheap and is this beat's second job.**

---

## 2 · CHANNEL B — what he typed into the app, read in full

`measured` — production (`home` · `est-e6696a`) holds **10 records, all awaiting disposition, 1 of 10
fully labelled**. Eight are onboarding field captures. **Two are substantive product feedback:**

> **`homes-second-home`** (11:17 ET): *"We want to show roles on this page - for example I am the
> owner for Grant Park and you can saw Home members non. Down the road I will want to invite mom to
> have access to my condo and she will invite me to the house that she sets up"*

> **`fb-53e7l33b-mtre3ll8`**: *"Let's keep brainstorming and coming up with ideas of how specifically
> to populate each card and say what's in it. Here there's a message of saying we're working on
> building out hte weather and what grows here. I think this card should be more focused on the
> property and things you can glean from it: local events, festivals, etc. especially since it's a
> condo in the city"*

⭐ **Both are already in the walk capture** — as **F14** and **F10** respectively — so nothing was
lost this lap. ⚠️ **But that is luck, not process:** they are there because he *also* said them aloud.
The in-app copies were sitting undisposed in the store the whole time.

⭐ **The `Houseplants!` question is answerable from this channel and has been open since the
briefing.** It arrived as `onboard-interests-other` — the *"something else"* free-text on the
interests step — **not** as a feature request. That is a person naming a twelfth interest in the box
provided for exactly that, and it is evidence about the interest vocabulary (D4), not a module ask.
**Still Paul's call, but the channel it arrived on is now on the record.**

---

## 3 · ⛔ CHANNELS C AND D — the telemetry gaps, which is what he asked to have written down

`measured` in `worker/worker.js`:

| channel | write | read | verdict |
|---|---|---|---|
| `feedback` | `POST /api/feedback` :3189 | ✅ `GET /api/feedback?start=&end=` | ✅ swept, no watermark |
| `metrics` | `POST /api/metrics` :3015 | ✅ `GET /api/metrics?start=&end=` | ✅ read by the gate's `instrumented` clause |
| **`door`** | `POST /api/door` :3548 | ✅ `GET /api/door?start=&end=` exists (:992) | 🟡 **THE ROUTE EXISTS AND NO TOOL CALLS IT.** Holds 2 days on production right now |
| **`onboarding-metrics`** | `POST /api/onboarding-metrics` :3480 | ⛔ **NO GET ROUTE ANYWHERE** | 🔴 **write-only.** Holds 2 days on production. The data is in KV and cannot come out through the app's own API |

⭐ **The distinction matters and the two need different fixes:**
- **`door` is a MISSING READER.** The API answers; nothing asks. A small tool closes it, and it is the
  channel that would show *"someone opened the invite and stopped"* — ⚠️ **which is precisely the
  question GAP 1 is going to the trouble of a house visit to answer, and precisely what Mom's unspent
  invite will generate the moment she taps it.**
- **`onboarding-metrics` is a MISSING ROUTE.** No GET exists, so no tool *can* read it. ⛔ **The data
  is not lost** — it is in KV and `wrangler kv key get` reaches it — but nothing in the loop can see
  it, which means every onboarding behaviour signal from both laps is currently invisible to the
  consolidation.

⚠️ **AND NOTE WHAT THAT COSTS RIGHT NOW:** `onboarding-metrics` is the channel that would have told us
**where the 14:22 ET run actually went** without my having to reason from the feedback store and get
it wrong. The behavioural record existed; nothing could read it.

### → Proposed rows, for Paul's disposition. ⛔ Unranked; both are small.

| | proposed row | v1, and what it defers |
|---|---|---|
| **T1** | a `tools/watch-door.py` that calls the existing `GET /api/door` and reports arrivals that never became accounts | **v1:** print arrivals per day per estate and flag any with no matching account. **Defers:** correlating a door arrival to a later account, which needs an id the door record may not carry |
| **T2** | a `GET /api/onboarding-metrics?start=&end=`, mirroring `/api/feedback`'s shape exactly | **v1:** read-only range query, same auth posture as `/api/metrics`. **Defers:** any analysis on top of it — this row buys legibility, nothing more |

⭐ **Both are `concept` and the design band has room** (`design 0/2`). Neither is on the critical path
of anything shipping; both change what the *next* lap can see.

---

## 4 · WHAT THIS BEAT DID NOT DO

- ⛔ **Nothing was disposed.** Beat 6 is Paul's and the 480 records still await him. This beat found
  and read the channels; it did not rule on a single record.
- ⛔ **The end-to-end proof (F1→F6) has not run.** Its first record is chosen — the three orphaned
  production rows, `not-a-finding`, citing the 11:05 ET deletion — but **F3 is Paul's beat** and it
  cannot fire without him.
- ⛔ **The four lap-2 seat REPORTs have not been read**, so three third-column cells stay UNANSWERED.
- ⛔ **No options board.** That is beat 2, at the commitment point, and building it now is exactly
  what Paul said not to do.

---

## 5 · ⚠️ ONE MORE THING, FOUND WHILE FILING — the findings register is NOT in git

`measured`: `.gitignore:5` ignores `.private/`, and `GATE2-paul-findings.md` lives at
`.private/synthetic-walks/GATE2-paul-findings.md`.

So the file whose own header says —

> *"**This file is the point of the exercise, not a side effect.** … Unlike the walk reports, this is
> a real person's observations. … **One Paul finding outranks any number of agreeing fixtures.**"*

— has **no version history and no backup.** Every walk he has ever done exists in exactly one place,
on one disk. Tonight's additions included.

⛔ **I am not moving it, and the reason is a real one.** `.private/` is ignored because this repo has a
public surface (`tools/check-public-build.py`, the neutral export), and the register carries his
verbatim words and material adjacent to his home address. **Privacy is the right default and the
ignore is not a mistake.** The fix is therefore *not* "commit it".

**Three legitimate shapes, and the choice is Paul's:**

| | what it does | cost |
|---|---|---|
| **a** | a private sibling repo for `.private/`, the shape `Bolo Boys - Private` already uses in this portfolio | a second repo to keep in step |
| **b** | fold it into the encrypted-backup path (`/encrypted-backup`) that already exists for never-public material | no history, but a real backup — **the cheapest thing that ends the single-disk problem** |
| **c** | leave it, deliberately, and write down that it is accepted risk | free, and honest, but only if it is a decision rather than an oversight |

⭐ **My recommendation is (b) now and (a) later if the register keeps growing** — it removes the
irreversible failure tonight, needs no new repo, and does not touch the privacy posture. But it is his
call, and a fourth option is that the register was never meant to be durable, in which case that is
worth saying out loud once.
