# Lap 5 tracker — everything raised 2026-08-24

**Why this file exists.** Paul, late in the session: *"I know I've thrown a lot of detailed feedback
at you now, so make sure you review the thread and set up a tracker, or make sure there are agents
distributed to look at everything — or a tracker if it's good to do this in sequence rather than
parallel."*

**Sequence vs parallel — the answer.** Mostly **sequence**, and the reason is that one item gates
almost everything else: **nothing pushes until the ribbon is right**, because a push is what reaches
Mom. The two genuinely independent workstreams (the ribbon copy, and the confirm-card UX grammar)
ran in parallel because they touch different artifacts. Everything downstream of them is a single
chain.

**Status vocabulary.** `SHIPPED` = in the working tree, verified, **not pushed**.
`AWAITING PAUL` = needs his word before anyone can act. `HELD` = deliberately not done, with a
reason. Nothing in this lap has reached Mom.

---

## ✅ CRITICAL PATH — CLOSED 2026-08-24, SHIPPED AND LIVE

`9c05c81` + `50126ab` · **`check-live.py` ✅ LIVE MATCHES HEAD** (sha `2bcf844f…`, 03:12 GMT).
Loop state: **🟢 ARMED at leg 7** — the healthy resting state. Her arrival
`fb-0wk7w59c-mt1k6tll` is dispositioned and acknowledged; watermark advanced.

The ribbon that shipped:

> ✓ **Thursday, August 20 — what you wrote back settled:**
> • "Fabulous" — so the radar stays right where it is, first thing in the Weather card.
> *Everything else new is in Recent updates ›*

Also shipped: the release note the bridge's completeness claim depends on · the
stepper's orphaning `border-top` deleted (fix C) · the bridge styled italic ·
`.gitattributes` + `tools/git-merge-generated.py` so the weather bot's commits stop
costing a hand-merge.

### ⏭ PICK UP HERE — the only things still owed

| # | item | why it is not done |
|---|---|---|
| 1 | **Confirm-card fixes B and A** | B = generalize `correctionPrompt` (mechanism exists). A = dismissal → one word in the corner, ⛔ **not an ×**. **A is the dangerous one** — it must keep carrying `getNote()` or her typed-but-unsent words die, and that wants a real test, not a midnight edit. **Paul still owes the word** for the corner label. |
| 2 | **`closing` renders only when `changes[]` is non-empty** | The model cannot express *"she gave approval; nothing changed."* Did not bite this lap (there was a bullet). Restructuring live render code at midnight for a case that does not occur was the wrong trade. |
| 3 | **`/ux-sweep` is OWED** | 21d, 38 viewer commits, 5 laps. `check-ux-sweep.py` now fires it at every pickup, so it cannot be forgotten again. Two agents + a full browse — start it fresh. |
| 4 | **Type + colour system** | 24 sizes, **165 text colours**, 55 used once. Proposals written, none ratified — needs Paul's word on the ~7 bands, "collapse to most-used", and the merge test. |
| 5 | **`.card-later-link` is an opener AND a dismisser** | One class, two opposite meanings. Needs its own class. |
| 6 | **`vehicle-specs-toggle` 55×19** | Smallest real control, on Paul's own surface. |

---

## 🔴 THE ORIGINAL CRITICAL PATH — kept for the record

| # | item | state | note |
|---|---|---|---|
| 1 | **Ribbon redraft** | ⏳ drafted, needs Paul | Steward fixed it with one word: heading `changed` → **`settled`**. Insects line removed entirely; replaced by Paul's **bridge to Recent updates**. Text below. |
| 2 | **Release note for the chorus + width fixes** | 🔴 **REQUIRED BY 1** | The bridge says *"everything else new is in Recent updates"* — a **completeness claim**. Ship the card without the note and the bridge lies on day one. |
| 3 | `closing` renders only when `changes[]` is non-empty | 🔴 code fix owed | The model **cannot express "she gave approval; nothing changed"** — the shape most likely to recur. Steward specified the target model (4 independent slots). |
| 4 | Commit → push → `check-live.py` | ⛔ **HELD** | Gated on 1–3. |
| 5 | Leg 7 close: disposition `fb-0wk7w59c-mt1k6tll`, retire, watermark | ⛔ blocked by 4 | Mechanical once pushed. |

### The ribbon as it now stands (Paul has NOT approved this revision)

> ✓ **Thursday, August 20 — what you wrote back settled:**  `Look back ›`
> • "Fabulous" — so the radar stays right where it is, first thing in the Weather card.
> *Everything else new is in Recent updates ›*

"Settled" and "stays" agree; "changed" and "stays" never could. The bullet is unchanged from the
version Paul already accepted.

---

## ✅ SHIPPED THIS LAP — in the working tree, verified, unpushed

| item | evidence |
|---|---|
| Chorus row stacked | 5 left edges → **1**; text track 174px → **296px**; 16 line boxes → **9** |
| Vehicle icon out of the content column | Vehicles/Equipment/Household: **32 extra rows → 15** |
| `table-layout: fixed` on the specs table | prevention — bites when Household populates |
| `expandCard(id, source, subtab)` | verified: closing link lands on **Insect Sounds**, chorus rendered |
| `titlePhrase` on the ribbon | heading is now authorable + human-gated; derivation kept as fallback |
| `ack-reply` branch in `changedPhrase` | 3rd lap running to add a branch — she keeps finding new doors |
| `subtab_switched` dead branch | read `parent`/`target`; viewer only ever emitted `{card, subtab}`. Dead since 2026-05-21 |
| `detail_opened` surfaced | was read by **zero** tools; now a HOW DEEP block in `read-mom-engagement.py` |
| `check-cycle-map.py` globs `*.js` | `telemetry-walk.js` served the loop **16 days** unnamed |
| Guru digest rebuilt | was stale on vehicles |
| 2026-08-18 weather | re-record returned identical 192 records → acked **with that evidence** |
| `health-probe.py --only` | one source, N readers — no second weather check |
| **Leg 6e — `herConditions()` 414×A+** | **0 HIGH**, 20 MED (row tax), 4 tap targets <44px |
| Weather check → Leg 1 block | `[paul-approved]` |
| `check-ux-sweep.py` | new; fires today on all three signals |
| Principles library | ux seat: `design-principles/fernwood.md` + 2 cross-project files. Steward: `content-principles/fernwood.md`. **All `[candidate]`, none ratified** |

---

## 🟡 AWAITING PAUL — nothing moves on these until he answers

| # | question | who asked | why it needs him |
|---|---|---|---|
| A | **Ribbon revision** above — yes, or changes? | steward | reaches Mom verbatim |
| B | **Are the ~7 type bands the right cut?** | ux seat | 24 distinct sizes today, 10 of them half-pixel |
| C | **Is "collapse each band to its most-used member" the rule?** | ux seat | never the average — most-used is already tuned and already seen |
| D | **Do the row-tax thresholds (1.25 / 15%) survive a second run?** | ux seat | declared a first cut, 25 breaches today |
| E | **Colour system** — name the top 8–10, merge within 5 RGB units, leave the tail | ux seat | **165 distinct text colours**, 55 used exactly once |
| F | **`vehicle-specs-toggle` is 55×19** | herConditions | smallest real control on his own surface |
| G | **`/ux-sweep` is OWED** — 21d, 38 viewer commits, 5 laps | check | two agents + a full browse; his call when |

---

## ✅ CONFIRM-CARD GRAMMAR — delivered, awaiting Paul

**The grammar: four tiers, and a control may not borrow another tier's clothes.**

| tier | form | where |
|---|---|---|
| **ANSWER** | filled green ✓ / outlined × · boxed | in the flow — the **only** boxed controls |
| **SAY MORE** | disclosed text field | **after** an answer, never beside one |
| **NOT NOW** | one quiet word-led control | the card's **corner** — chrome, not content |
| **SOMETHING ELSE** | one quiet word-led link | the card's **footer**, bound to it |

ANSWER is already ratified (rule 1, 07-29) and needs nothing. The other three have drifted.

| # | fix | state | verified? |
|---|---|---|---|
| **C** | **Delete `.mom-queue-nav`'s `border-top`.** The stepper is flanked by two hairlines — `#ece2c2` and `#e4dcc4`, 8/6/2 RGB units apart — so it reads as a band belonging to neither. One line, −6px. | recommended first | ✅ `border-top: 1px solid #ece2c2` confirmed at `:4969`; computed `rgb(236,226,194)` |
| **B** | **Generalize `correctionPrompt`.** It already opens the note, replaces the action row with one "Send", and hides the add-note link — gated to one branch of one card type. Invent nothing. | highest value | ✅ mechanism exists |
| **A** | **Dismissal → one word, in the corner.** ⛔ **But NOT an ×** | needs Paul's word | ✅ `.gg-suggest-btn-no::before { content: "×" }` — × already means *"No, that's wrong"* 12px away |
| **D** | **Carousel dots: no.** | closed | ✅ `render()` wraps `idx` — the set cycles, so there is **no position to show**; and 5 dots at the 44px floor is ~220px added to the card he says is too tall |

⭐ **Paul's own next sentence supplied the fix his × proposal couldn't:** *"when you click that it
says 'Card snoozed'."* Move the reassurance from decide-time to confirm-time — `showAck()` already
exists at `:12017` — and the label gets short enough for a corner. ⚠️ Two regression paths: the
corner control **must still carry `getNote()`** (moving it away from the textarea is how typed-but-
unsent words die), and it writes `SNOOZED_KEY` only — **a snoozed card is not an answered card.**

⚠️ **`.card-later-link` is used as an OPENER on the household card** (`Is there something else the
house runs on? Tell the Almanac ›`) — one class, two opposite meanings, for a reader who learns by
shape. Needs its own class.

### 📏 THE HEIGHT — measured, and the finding is POSITION, not height

The seat labelled its own ≈638px an **arithmetic estimate, not a measurement** (it has no Bash).
Measured here at 414 × A+:

> **The first answer button sits at y = 862px in an 848px viewport.**

**The answer buttons are entirely below the fold.** She cannot answer without scrolling — on 28–127
second sessions. That confirms the seat's conclusion and is *worse* than its estimate (it predicted
~470px in). A 75%-of-screen card is fine **first** and wrong **third**, and this one is third.

The seat's per-element ledger is **not** independently verified — my selectors caught a different
card. Do not quote the 638 or its parts; quote the 862.

**Recommended order: C → B → A → re-measure.** The prose is innocent (~12%); photo + control stack
are ~51%. Any fix starting with copy is aimed at the wrong twelfth.

---

## ⏸ HELD — deliberately not done, with the reason

| item | why held |
|---|---|
| Sticky card header (wayfinding) | ⛔ **`.main-card { overflow: hidden }` makes `position: sticky` inoperable.** Not a taste question — a capability one. And Paul has not seen it rendered. |
| `.bio-section` padding pass | Mom-facing; gated |
| Colour + type cleanup | needs B/C/E answered first — a system, not a sweep |
| `today-glance-item`, specs value column | **measured and cleared** — 2 distinct left edges across 4 and 270 cells. Real columns. Nearly "fixed" two non-defects |
| The A+ archaeology (who pressed it) | likely unrecoverable; the actionable half needs no answer. Paul will check her phone when he sees her |
| `titlePhrase` ↔ body agreement check | steward proposes a crude gate in `check-mom-ack.py`; not built |

---

## ⭐ THE PATTERN OF THE NIGHT — worth carrying into the next lap

**Three instruments were dead and one control was blind, all found in one evening:**
`subtab_switched` reading fields the viewer never emitted · `detail_opened` read by nothing ·
`check-cycle-map.py` seeing only `.py` · weather completeness living outside the loop · `/ux-sweep`
reachable only from memory.

> **A capability the loop cannot reach by running its own procedure is not a capability the loop
> has.**

**And the harness was wrong four times, each time returning a plausible number rather than an error:**
`clientWidth` = 0 for inlines · the A/A+ split contaminated by localStorage · the pair detector
reading computed `display` when flex items are blockified · `herConditions` reporting **235 HIGH
findings** that were side-scrollers, collapsed cards, and `::after` hit areas it could not see.

> **A harness earns belief by reproducing a case you already know.** Pick that case *before* the
> first run. If a check returns a big number, suspect the check first.
