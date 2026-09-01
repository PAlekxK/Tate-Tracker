# D4 · The pre-glance stack height ledger — 414×A+

`paul-stated 2026-08-31`: *"Every resident is individually ratified; the SUM never ruled on. Run the
8/24-style height ledger on the stack, let the numbers propose the trim, Paul decides from the
ledger. **Change nothing before the ledger.**"*

⛔ **Nothing was changed.** This is measurement only.

**Method.** `python3 -m http.server 8765`, served bytes md5-verified byte-identical to the working
tree (`64ce8c39…`) before any measurement. Playwright at **414×848** — her measured conditions, not
the 390 exhibit convention. Text size applied through the app's own `#text-size-aplus` control, and
`A` re-measured in the same run for comparison, because **A is what she actually has** (the A+
default was walked back 2026-08-19 and never shipped).
⚠️ **Telemetry suppressed before anything was touched** — `tateTracker.metricsExclude` set,
`MetricsCollector.track` neutered in-page, and every non-GET `fetch` stubbed. This synthetic browser
has no registered deviceId and must not enter her funnel or write to her record.

---

## THE LEDGER

| resident | **A+** | **A** (hers) | share of stack |
|---|---:|---:|---:|
| `.header` | 183 | 170 | 9% |
| `.jump-strip` | 172 | 162 | 9% |
| Almanac card | 223 | 213 | 11% |
| **`#mp-master` — Mama's Perspective** | **1,330** | **1,196** | **68%** |
| gaps / margins | ~50 | ~49 | 3% |
| **STACK ABOVE THE FIRST GLANCE ROW** | **1,958** | **1,790** | |
| in viewports | **2.31** | 2.11 | |
| **first card (Weather) begins at** | **3,196 px** | 2,807 px | |
| in viewports | **3.77** | 3.31 | |

### Inside Mama's Perspective — the 1,330 px

| | px | share of the whole stack |
|---|---:|---:|
| head / "Close ▾" toggle | 32 | 2% |
| **acknowledgment ribbon** (Aug 20, *"Fabulous"*) | **236** | **12%** |
| **the served question card** (`q-fairway-grass-seedheads`) | **706** | **36%** |
| **zone-walk launcher** (*"Exploring and defining Fernwood's zones"*) | **293** | **15%** |

---

## ⭐ WHAT THE NUMBERS PROPOSE — three observations, no recommendation acted on

**① The stack is ONE resident.** Mama's Perspective is **68%** of everything above the glance row.
The header, the jump strip and the Almanac card together are 29%. **Any trim that does not touch
Mama's Perspective is rounding error** — a fact worth having before anyone proposes shaving the
header.

**② The single largest item is one question — and she only ever sees one.**
`q-fairway-grass-seedheads` renders at **706 px, 36% of the stack**, and `read-mom-funnel.py` says
she has been offered a card **33 times, 33 of them at the head slot**, never tapping *"Another
question ›"*. So the queue's depth costs her nothing and the **head card's height costs her
everything**. Card length is a layout decision that has only ever been made as a copy decision.

**③ The held ribbon is not free.** The Aug 20 acknowledgment occupies **236 px — 12% of the
stack** — and `paul-stated 2026-09-01` is holding it *"until I do some more work on the zones."*
That hold is his call and stands. **The ledger's contribution is only this: the hold has a
measurable rent**, and it is being paid above the content on every load.

⚠️ **A fourth thing, flagged rather than measured:** the **293 px zone-walk launcher** — *"You know
these gardens better than I do… I'll take you one spot at a time"* — is live on her surface **while
the zone thread is held**. Not a contradiction (her 8/30 naming already happened; this invites
more), but it is 15% of the stack advertising the exact thread Paul has paused. Worth a ruling, not
a fix.

---

## Against D4's own baseline

D4 recorded **1,712 px**. Measured today: **1,790 at A**, **1,958 at A+**. So the figure is
**78–246 px larger** than the number the ruling was written on. ⚠️ **NOT attributed** — the 8/31
sweep shipped 17 punch items and this morning's rotation changed the head card, either of which
could move it, and D4 did not record which text size it measured. **The delta is real; its cause is
not established, and this ledger does not guess.**

⛔ **A counterfactual was attempted and is NOT reported.** I tried substituting each live prompt into
the served card to price the head-card choice. The isolated prompt element measured **23 px for a
326-character prompt**, which is impossible at A+ — so the substitution hit a text fragment, not the
whole prompt, and every card-height delta it produced is unreliable. **Reporting those numbers would
have been an instrument read I cannot stand behind.** Pricing the head-card choice needs a real
re-render through `MomQueue`, and is the obvious next measurement.

---

## What this ledger does NOT settle

- **Whether 2.31 viewports is wrong.** It is a number, not a verdict. Every resident was
  individually ratified and the sum is Paul's to rule on — that is the whole premise of D4.
- **Whether she experiences it as long.** `read-mom-engagement.py` shows 3 sessions / 2 days since
  lap 6, 3 card opens, **zero depth-2 or depth-3 events**. That is consistent with a long stack and
  equally consistent with her getting what she came for from the jump strip. **The instrument cannot
  separate those**, and this ledger does not pretend to.
