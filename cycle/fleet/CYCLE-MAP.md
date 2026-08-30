# THE FLEET CYCLE — Track B's loop

**`paul-decided 2026-08-30`.** Fernwood's fleet & equipment record (Track B) has had an
inbound **door** since 2026-08-28 and **no loop** — `BACKLOG.md` says so in its own words:
*"⚠️ Nothing sweeps that door on a cadence."* This map closes that.

**Anchor project:** `Fernwood Fleet` · **repo:** `Tate-Tracker` · **non-AI door:**
`python3 tools/fleet_probe.py`

> ⚠️ **EVERY THRESHOLD HERE IS PROVISIONAL AND LAP 1 RE-CADENCES IT.** They are one
> session's first cut, not measurement. Same posture the Tate Dam loop took, for the same
> reason: a threshold invented before a lap has run has no evidence behind it.

---

## Why this loop exists, and what it is NOT

**It is not a maintenance to-do list.** Track B's open work lives in `BACKLOG.md` and always
will. This loop exists for the work **nothing triggers** — the record decaying quietly while
every individual row looks fine.

⭐ **THE FOUNDING EVIDENCE, and it is one day old.** On 2026-08-30 a session diagnosed Blue
Thunder's starting fault out of `manuals/text/dr200s-2017-service.txt` and told Paul to
kick-start a motorcycle **that has no kickstarter**. The manual's own line 3 names the
**DR200SE** — a different model. `manuals/INDEX.md` had it titled correctly behind a 🟡
marker. Nothing was hidden; it was read past.

**The lesson that shaped every beat below:** that session *was* careful. It cross-checked
spec tables and quoted line numbers. **Careful reading of the wrong document produces
confident wrong answers**, so a beat that says *"familiarise yourself with the machine"*
would have caught nothing. Only a mechanical comparison catches it — which is why **beat 0
is a script, not a discipline**, and why it runs before anything else.

Paul, the same day: *"it's very critical that that's like step zero almost, so that we don't
have issues like this… my loose terminology at the beginning is immediately associated with
a specific vehicle in our fleet and all the history and all the exact details."*

---

## The beats

| # | beat | what it does | door |
|---|---|---|---|
| **0 · BRIEF** | resolve + verify the source | `vehicle-brief.py "<whatever Paul said>"` — resolve loose speech to ONE machine (printing what it rejected, refusing on a tie), then print its record **and check every attached manual's own foreword against the model the card claims**. | `tools/vehicle-brief.py` |
| **1 · SWEEP** | what fired | `fleet_probe.py` — four signals: SEASON · INBOX · PROVENANCE · STALE-OPEN. Read the reason, not just the verdict. | `tools/fleet_probe.py` |
| **2 · INTAKE** | drain the door | Read `cycle/requests.jsonl`. Each row lands on a repo surface — `vehicles.json` for fact, `BACKLOG.md` Track B for open work — or is refused with a reason. ⛔ **A row is never folded on a model read of a photograph.** | `cycle/requests.jsonl` |
| **3 · VERIFY** | close the physical checks | The reads only the machine can answer, batched into one trip with a light. Never a paper answer where a physical one exists. | `openMechanicalItems` |
| **4 · SEASON** | the only real clock | Fall put-away / spring wake-up. Parts lead time is the gate, not the weather. | `restoration` |
| **5 · RECORD** 👤 | fold, and Paul rules | Corrections folded, `serviceHistory` appended, generated views re-inlined. **PAUL'S GATE: nothing that costs money, touches a machine, or contradicts his own read of it is decided here.** | Paul |
| **6 · AMEND** | improve the loop | Pre-registered before the lap runs. *"None — pre-registered metric unmoved"* is a valid outcome. | `CYCLE-LOG.md` |

**S2 · the human gate is beat 5**, and it is machine-visible above (👤). Beat 3 also stops at
Paul by nature — he is the one holding the flashlight — but 5 is the declared blocking gate.

---

## S3 · the deterministic check, and WHERE it is sited

`vehicle-brief.py --check` (the model/foreword comparison) is sited at **beat 0, before any
reading**, and not at beat 1 with the other signals.

**Why here and not there, and the alternative rejected:** beat 1 is where signals are counted
for *scheduling* — it answers "is a lap owed." Provenance is not a scheduling question, it is
a **precondition on every sentence the lap will write**. Sited at beat 1 it would fire
correctly and still arrive *after* a session had opened the wrong manual, which is exactly
the sequence that produced the kickstarter answer: the flag existed in `INDEX.md` the whole
time and was simply downstream of the reading. **A check that fires after the mistake is a
report, not a control.**

**Seen to fail:** `vehicle-brief.py --selftest` pins the DR200SE case as a POSITIVE control
(it must fire, and must name `DR200SE`), the correctly-held DR-Z400S manual as a NEGATIVE
control (it must not fire), and the known-bad Husqvarna as a second positive. `fleet_probe.py
--selftest` proves all four signals **both ways**, including that a dead producer reaches
UNKNOWN rather than RESTING.

⭐ **Three payload bugs were found by running these against reality on day one** — the probe
read the inbox as pure JSONL when it carries a `#` header, guessed `ask` where the schema
says `what` (rendering two real corrections as `"?; ?"`), and `manuals-search.py`'s
confidence regex had no `🔴`, so the corpus's most serious rating parsed as *no rating*. All
three are the same shape as the founding defect. **The checks earned their place before the
loop had run a single lap.**

---

## Triggers — this loop RESTS, and fires on a signal

Not a cadence. `fleet_probe.py` exit **1** means a lap is owed; **0** means rest; **2** means
a source could not be read and is **never** treated as rest.

| signal | fires when | rests when | today |
|---|---|---|---|
| `SEASON` | ≤45d to first frost (~Oct 17) with a fall put-away still open | put-away done, or outside the window | · 48d |
| `INBOX` | an unhandled row in `cycle/requests.jsonl` | drained | ⚡ 2 |
| `PROVENANCE` | a manual names a different model and is unacknowledged | fixed, or acked in `cycle/fleet/provenance-ack.json` | ⚡ 6 |
| `STALE-OPEN` | an `openMechanicalItems` check dated >60d ago | the trip with the light happens | ⚡ 3 |

⭐ **Every signal has a resting state, on purpose.** A signal that could never go quiet is a
to-do list wearing a trigger's clothes — the **N8 · COSTLY CONTROL** shape, *a control whose
alarm is permanently on is a control nobody reads.* PROVENANCE has an ack file for exactly
this reason: reviewing a document and accepting it must be able to silence it.

---

## What this loop deliberately does NOT do

- **It does not touch Track A.** Mom's journal, her feedback, the viewer and the ribbon ride
  `MOM-CYCLE-MAP.md`. Two products, one repo, two loops — that split is `D41`, and the
  anchor project strings (`Fernwood` vs `Fernwood Fleet`) keep it honest.
- **It declares no expert seats.** Fleet work is documentary and physical; there is no
  design or copy surface here for a seat to review. Declared absent, per lap output.
- **It does not order parts, book shops, or spend money.** Beat 5 is Paul's gate.
- **It does not transcribe a photographed document into the record.** A value read off a
  photo is a model read, and the parts record is the one place this portfolio has *measured*
  being wrong in both directions.
