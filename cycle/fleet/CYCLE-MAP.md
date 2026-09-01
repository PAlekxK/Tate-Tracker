# THE FLEET CYCLE — Track B's loop

**`paul-decided 2026-08-30`.** Fernwood's fleet & equipment record (Track B) has had an
inbound **door** since 2026-08-28 and **no loop** — `BACKLOG.md` says so in its own words:
*"⚠️ Nothing sweeps that door on a cadence."* This map closes that.

**Anchor project:** `Fernwood Fleet` · **repo:** `Tate-Tracker` · **non-AI door:**
`python3 tools/fleet_probe.py`

<!-- map-control: python3 tools/fleet_probe.py --selftest && python3 tools/vehicle-brief.py --selftest -->

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
| **1 · FIELD** | what OWNERS know | ⚠️ CONDITIONAL — runs when the record has no answer to a symptom, not every lap. Web/forum search for **failure modes**, landing in `cycle/fleet/FIELD-NOTES.md` — the quarantine — never in `vehicles.json`. Every note carries a `test:` or it is not accepted. | `cycle/fleet/FIELD-NOTES.md` |
| **2 · SWEEP** | what fired | `fleet_probe.py` — four signals: SEASON · INBOX · PROVENANCE · STALE-OPEN. Read the reason, not just the verdict. | `tools/fleet_probe.py` |
| **3 · INTAKE** | drain the door | Read `cycle/requests.jsonl`. Each row lands on a repo surface — `vehicles.json` for fact, `BACKLOG.md` Track B for open work — or is refused with a reason. ⛔ **A row is never folded on a model read of a photograph.** | `cycle/requests.jsonl` |
| **4 · VERIFY** | close the physical checks | The reads only the machine can answer, batched into one trip with a light. Never a paper answer where a physical one exists. | `openMechanicalItems` |
| **5 · SEASON** | the only real clock | Fall put-away / spring wake-up. Parts lead time is the gate, not the weather. | `restoration` |
| **6 · RECORD** 👤 | fold, and Paul rules | Corrections folded, `serviceHistory` appended, generated views re-inlined. **PAUL'S GATE: nothing that costs money, touches a machine, or contradicts his own read of it is decided here.** | Paul |
| **7 · AMEND** | improve the loop | Pre-registered before the lap runs. *"None — pre-registered metric unmoved"* is a valid outcome. | `CYCLE-LOG.md` |

**S2 · the human gate is beat 6**, and it is machine-visible above (👤). Beat 3 also stops at
Paul by nature — he is the one holding the flashlight — but 5 is the declared blocking gate.

---

## Beat 1 · the FIELD half, and why it is quarantined `[paul-stated 2026-08-30]`

*"I think it's important to also get kind of third-party forum takes, which can be kind of
dangerous… that information may need to be sequestered and treated differently than the user's
manual."*

Both halves of that are right, and the second is the load-bearing one. **The store is
`cycle/fleet/FIELD-NOTES.md`; it is tier C by construction; nothing in it is a fact about a
machine.** Tiers are not redefined — they are `A/B/C` from the Bolores `SOURCES.md`, promoted
from one vehicle's private file to the fleet standard, along with its governing rule: **a C
never silently becomes an A.**

⭐ **The rule that makes it safe rather than merely tidy: never take a NUMBER from a forum,
take a QUESTION.** A factory manual will never tell you *the regulator cooks on these and takes
the battery with it* — only owners know that, and it is the difference between testing four
things and testing the right one first. But a forum's legitimate output is **a hypothesis with
a test attached**, and **a hypothesis cannot launder into the record, because the record only
accepts a measurement.** A forum may send you to T3. It may never tell you T3's pass band.

**Why the quarantine is STRUCTURAL and not a habit:** the danger is *migration*, not error. The
Bronco card already carries a `_chatgptProvenanceWarning` recording **four wrong card values**
traced to two ChatGPT threads — one wearing a false *"read off the actual sidewalls"*
provenance. It did not arrive labelled as junk; it got summarised into a note and later sat in
`vehicles.json` looking manual-sourced. So a card value's `source` may never be a URL, and that
is **checked mechanically**, not remembered.

⚠️ **CONDITIONAL, and that is deliberate.** This beat does NOT run every lap. It runs when the
record has no answer to a symptom. Making a network search automatic would make beat 0 slow and
non-deterministic, and beat 0's whole value is that it is a script you can trust to say the same
thing twice.

## S3 · the deterministic check, and WHERE it is sited

`vehicle-brief.py --check` carries TWO checks, both sited at **beat 0, before any reading** —
the model/foreword comparison and the no-URL-as-a-source scan — and not at beat 1 with the other signals.

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


---

## Conformance — this loop answers to the portfolio spine `[added 2026-09-01]`

The standard this loop's **machinery** is measured against is
**`~/.claude/rituals/CYCLE-SPINE.md`** — S1 a legal state schema, S2 at least one
blocking human gate that is machine-visible, S3 a deterministic check that has been
*seen to fail*, S4 a closed lap marked as closed in the chronicle, S6 a map that
parses. Read it at the **start** of a lap, not the end.

**Why this section exists, and what it is not.** The spine's standing rule is that no
loop is retrofitted — each adopts on its own next lap. That rule needs something to
travel on, and until today it had nothing: measured 2026-09-01, **11 of 12 maps
contained no reference to the spine at all**, and **seven loops lapped in the days
after the 2026-08-31 two-axis amendment was ratified without adopting it**. A rule
with no carrier is not a slow mechanism; it is not a mechanism. This section is the
carrier, and nothing more. Its presence proves only that a lap can **see** the
standard — never that this loop conforms. Conformance is measured separately by
`python3 ~/.claude/tools/ecosystem-probe.py`, which counts and never grades.

**Open amendments to dispose at the next lap** (each is *check and rule*, not
*apply silently*):

| amendment | what it asks of this loop |
|---|---|
| two-axis state keys `[paul-ratified 2026-08-31, card claude-6]` | `hold{}` and `beat{}` as dicts; `signals[].status` tri-state (`quiet` / `fired` / `unobserved`) rather than a boolean; `signals[].observed_via` naming what did the observing; `last_lap.outcome` from the closed enum (`closed` / `open` / `abandoned`) |
| GATE-SWEEP `[paul-ratified 2026-08-31]` | a lap **opens** by disposing the gates that have already fired, before it does anything else |

⚠️ A boolean `fired: false` and a tri-state `unobserved` are **not the same claim** —
the first asserts the signal was checked and was quiet, the second admits nothing
looked. Adopting the key without honouring that distinction is worse than not
adopting it, because it launders an unmeasured signal into a measured-quiet one.
