# Lap 7 · ALL THE TESTING THAT WAS DONE — the full analysis, every act on every axis, and what it means for the plan

- row: analysis — process (the input to **lap 9 · row T**; ranks nothing, commits nothing) `[paul-asked 2026-09-11 09:39:15 -0400: "complete your full analysis of all the testing that was done"]`
- objective: O5 (the loop itself)
- class: engine · must-not-diverge
- seats: this window (testing-revamp, tate-tracker-d8) synthesising · practice-steward's audit **cited, never restated** (`.practice/2026-09-11-lap7-testing-cycle-AUDIT.md` §0–§8h) · content-steward's read cited (`.content/walks/87c7aae-walk-read.md`)
- depends-on: the audit · `.plans/2026-09-10-testing-architecture-PLAN.md` · `.plans/2026-09-10-lap7-build-PLAN.md` §5 · `cycle/release/CYCLE-LOG.md` § Lap 7 (2463–3560)
- ready: agent-measured — feeds `.plans/2026-09-11-testing-revamp-PLAN.md`; **Paul rules there, not here**
- stage: analysis
- HEAD: `3a2c589f` · stamped from `date` · lap 7 **cleared by Paul** in this window (`"let's close out that lap"`), so the record below is final
- read-only: every tool run below was run read-only; nothing under `tools/` was edited

> ⛔ **What this file is and is not.** The audit answered *where did the time go and why*. This answers
> *what was every act of testing, what could each act SEE, what did each act FIND, and what could NONE
> of them see* — so the plan is sized against the whole of lap 7's testing and not against the battery
> alone. Where the audit already holds a number it is cited by section; nothing is re-derived.

## 0 · THE ANSWER FIRST

**Lap 7 was tested on five axes. Four of them ran; the fifth ran once, by hand, for seven minutes, and
found more base-level defects than the other four together.**

| axis | the act | ran | what it found | what it structurally could not see |
|---|---|---|---|---|
| **DRIVE** (transcript) | 45 walks, 3 batteries + shake-out | ✅ | F1 · F2 · A · B · J2 (5 of 8 audit findings) | anything rendered *correctly from wrong data*; any state the action list never enters |
| **READ** (the lens) | 15 reports at the final sha | ✅ once, late | the receipt renders schema ids as the person's words (the third product defect); **63** non-blocking bullets | the 30 walks at dead shas; anything at a width, engine or text size no walk had |
| **CONTENT READ** | 1 file, 15 runs | ✅ | the same stop, ruled; 12 draft slots | copy on regions no journey reveals (W5) |
| **GATE** (release-gate · walk-integrity · post-deploy · headless · neutral) | every sha | ✅ | nothing new — it *certified* | 17 of 22 battery-C walks (unit = seat, ties by walk order — audit §3f) |
| **HUMAN** (Paul's walk) | once, ~7 min by git | ✅ | **W1–W6**, incl. one 🔴 (audit §8h) | — it is the only axis with no declared coverage, so *what it did not walk* is unrecorded |

**Yield per axis, in one line each:** the drive found what the app *did*; the read found what the app
*said*; the gate found nothing and hid twelve failures; the human found what the app does *to a device
that has been used before*. **No axis overlapped another's findings.** That is the whole case for
keeping all of them — and the whole case that the battery's "15 of 15 clean" was a statement about one
axis in one state.

## 1 · THE INVENTORY — every act of testing the chronicle records for lap 7

*Sources: `CYCLE-LOG.md` § Lap 7 (grep of tool names, lines 2463–3560), the 45 run directories, the
tools' own read-only output at `87c7aae` this morning.*

| # | act | instrument | times in lap 7 | axis | cost measured? |
|---|---|---|---|---|---|
| 1 | **selftests before the freeze** | `journey-walk.py --selftest` 60/60 → **62/62** at `12912b9` (the F2 clause added) · `release-gate --selftest` · walk-integrity's · **11/11** (a tool's) | every candidate | harness | no — seconds |
| 2 | **shake-out at lab** | 3 walks, pre-freeze (`a3beb8d`) | 1 | drive | ✅ 7.2 min (audit §1b) — **best value per minute of the lap** |
| 3 | **freeze** | a commit | 3 (candidates 1·2·3) | — | ~0 |
| 4 | **deploy chain** | `deploy-worker.sh` → `pages-deploy.py` (with its **headless PAGEERROR load**) → `post-deploy.py` | 3 (chronicle: post-deploy ×8 mentions, headless ×7) | gate | ⛔ **not measurable** — no tool writes a duration (audit §8g) |
| 5 | **estate neutrality at the origin** | `check-estate-neutral --url` — *neutral 311/0* at candidate 3 | 3 | gate | no |
| 6 | **the batteries** | `journey-walk.py --watch` × 5 seats × declared journeys | A: 5 · B: 15 · C: 22 = **42** (+3 shake-out = 45) | drive | ✅ 51.9 min browser (audit §1b) |
| 7 | **integrity** | `walk-integrity.py` — this morning: **289 runs · 141 countable · 148 refused**; every seat's newest run countable | per battery | gate | no |
| 8 | **the reading seats** | 5 lenses × J0/J3/J8 = **15 REPORT.md** at `87c7aae`; **0** at the three dead shas | 1 (deferred to the final sha) | read | ✅ bounded — median **27 min** wall (audit §8b) |
| 9 | **the content read** | content-steward, `.content/walks/87c7aae-walk-read.md` | 1 | content | no |
| 10 | **gate ①** | `release-gate.py --sha 87c7aae` — 5 of 5 seats every clause; content ✅; UX clause **UNCHECKABLE** (no sweep filed at this sha); coverage lines: *414×848 ONLY* · *J2 unwalkable* | 5+ mentions | gate | no |
| 11 | **telemetry readers** | `read-glance-order.py --env qa` (row C's reader, ×5 mentions) · `check-telemetry.py` (EMIT only, no `--env`) · `watch-door.py` (×3) · `walk-capture.py` (capture.json per run → the `instrumented` clause) | per candidate | capture | no |
| 12 | **fixtures** | `household-fixtures.py` (×3: mint/list/teardown of the throwaways) · `walk-fixtures.py` (J1/J2/J3 entry state) | per candidate | arrival | no |
| 13 | **the steward ledger** | `product-steward.py --record --sha 87c7aae --carried 14 --already 0 --questions 3` | 1 | carry | counts only — **no CONSOLIDATION file** (audit §8d) |
| 14 | **Paul's walk** | beat 9, the amended gate kit (one throwaway owner, two tabs) | 1 · **09:23–09:30 by git** | human | ✅ ~7 min |
| 15 | **UX sweep** | `check-ux-sweep.py` reads *rested* (last 09-10, 10 viewer commits); **no two-pass sweep filed at `87c7aae`** | 0 | read | — |
| 16 | **seat portfolio** | `seat-portfolio.py` — 5 seats cover 9 of 11 rankable modules; **map-points** and **other** uncovered; `handover` flagged as a journey on the lens list | read-only, this morning | roster | — |

**Sixteen kinds of act; five carry a measured cost; one (the deploy chain) has none anywhere.**

## 2 · WHAT EACH AXIS FOUND, and what a cheaper instrument would have found instead

### 2a · The drive axis — five findings, two of them the harness testing itself

Audit §2 holds the table. The reduction: **F1** (real, needed one ranked walk at qa, cost ten) · **F2**
(harness; a selftest clause, cost one walk) · **A** (both harness cadence and a real product limit; the
loop could not tell them apart) · **B** (real, pre-existing, **only J8 could reach it — the battery's
clearest earned cost**) · **J2** (found by the entry gate at **zero** walks — *the pattern to
generalise*). The `expect:` timing defect cost **11 of battery C's 22 walks** for one harness fault
whose signature (5 of 5 seats, one identical assertion, zero page errors) nothing reads.

### 2b · The read axis — one stop, three convergent defects, and 63 bullets nobody reads

Read from the 15 counted reports' own findings sections (seat prose; no synthetic's typed text quoted):

| finding | seats that reported it independently | class | visible to the drive? |
|---|---|---|---|
| **USERNAME renders as a dash** on the account page — *on the one walk where the person needs it (J8)* | **5 of 5** (handover, mom, owner-via-content, strict-via-content, wide-eyed) | product | ⛔ no — the DOM is what it is; only a reader says *this is the wrong value* |
| **ranked picks have two names** — activity phrases at founding, module nouns on return (*Household systems* vs *Keeping the household systems running*) | 4 (handover, mom, wide-eyed, owner) | product / vocabulary — and for `mom` it touches her **protected phrase** | ⛔ no |
| ⛔ **the receipt renders schema ids** (`garden · motor-pool · equipment`) as the person's words | owner (J3, J8) → content-steward's **STOP** | product | ⛔ **no — the ids are correct; the render is wrong** (audit §8a) |
| **"an idea — not built yet" labels missing** on some ranked items; the app then shows neither | 3 (handover, wide-eyed, mom) | product | ⛔ no |
| **the recovery block still promises a hand reset after a successful sign-in** | 2 (wide-eyed, mom — *"the reset never appeared on any screen"*) | product | partly — the transcript holds both screens; nobody reads them together |
| **the shelf lost the town** under the place name | 2 (handover, wide-eyed) | product, small | ⛔ no |
| the address read-back offered *add an apartment number* under an address that already had one | 1 (mom) | product, small | ⛔ no |
| two rain figures on one stop; two highs five minutes apart at one address | 2 (mom J0, mom J3) | data-timing — and **the same class as her 07-26 rainfall complaint** | ⛔ no |
| two voices on one journey (*we* / *I* / *Paul*) | 2 (strict, wide-eyed) → content slot 7 | copy | ⛔ no |

⭐ **Every one of these was invisible to the drive axis by construction, and every one is the kind of
thing a real person notices first.** The reading did not run until the final sha, ~27 minutes after
the walks, and found in one pass what three batteries could not. **Convergence is real evidence and it
is also cost:** the username dash was reported five times to learn one thing. Under a (journey, lens)
unit that convergence becomes *computable* (same journey, N lenses, one finding) instead of five
paragraphs a human de-duplicates.

**And the 63 non-blocking bullets** (audit §8d) — asked for, written, and read by nothing but a hand
relay. The bullets above are the ones that happened to be relayed. The count is the finding.

### 2c · The gate axis — certified correctly, and hid twelve failures

Audit §3f: `release-gate` keeps the best-scoring run per **seat**, ties broken by walk order, so the
five J0 walks at `87c7aae` (walked first, all clean) masked **11 failed J8 walks + 1 failed J3**. The
gate's own coverage lines this morning already name what it cannot see: *414×848 ONLY*, *J2
unwalkable*, *UX sweep unfiled*. **A gate that prints its own blind spots is the right shape; a gate
whose unit hides its own inputs is not.** Q2 (ruled) fixes the second. Nothing yet acts on the first.

### 2d · The human axis — six findings in seven minutes, four of them a state no walk was in

Audit §8h holds the table (W1–W6). The reduction, for the plan: **W4 is unfindable by a fresh
profile at any volume**; **W2 and W5 are a zero-browser static check**; **W1 became a ruling**; **W3 is
one post-action assertion**; **W6 is the device noun on a laptop, invisible while every walk emulates
a phone.** Paul's own reading, in this window: *"we're not testing the right things… these sterile
Chromes… not realistic."* Measured: no persistent profile, no saved credentials, no stored text size,
**no WebKit installed** — Mom's Safari has never been walked (`journey-view.py:54-73`).

## 3 · WHAT NO AXIS COULD SEE — the coverage holes, named

| hole | evidence | which axis would have to grow |
|---|---|---|
| **a device that has been used before** (stale local state, a dead grant, a dead place name) | W4; W1's marker; the *How to reach you* row appearing only after re-sign-in (mom J8) | arrival-state property: `profile: returning-device` |
| **a signed-in desktop Chrome** with saved credentials and autofill | Paul's walk vs every walk; W6 | arrival-state property: `profile: signed-in-desktop` |
| **WebKit / Safari** | 0 walks ever; engine not installed | arrival-state property: `engine: webkit` — **a named cell that prints UNWALKED until it runs** |
| **A+ text size** (hers, 8 of 8 reports) | nothing sets it; the harness's own A+ measure (`measureNestingWidth.herConditions()`) is a separate tool | arrival-state property: `text: A+` |
| **any width but 414** | gate's own coverage line | ⚠️ ruled out of the harness by design (`journey-view.py:51-53`); Paul's laptop walk is the only wider reading — a declared human cell, not a harness one |
| **J2 returning-unfinished** | unwalkable since founding replaced granting (audit §2); re-scope vs retire is Paul's | journey library |
| **J7 second-member** | on the critical path under Q6 (five owners); nothing has it | journey library (**BACKLOG B3**, the invite-each-other future) |
| **J1 invited-stranger · J5 bare-door** | built action lists, walked by no seat this lap — as ruled: they print UNWALKED | the declared cell list |
| **the sign-in screen's own create-account link** | W2 — J0 enters via the door's button, J3/J8 arrive signed-up | a static check (M7), then a cell |
| **the modules `map-points` and `other`** | seat-portfolio: no seat ranks them; *other* is the catch-all — **nothing has walked the product as someone whose want is not on the list** | the lens roster (user-researcher's ruling) |
| **the two-pass UX sweep at this candidate** | unfiled; gate reads UNCHECKABLE | L7-P2's artifact convention — and `release-state.py:119` hardcodes the clause (audit §8e) |
| **the 30 walks at dead shas** | 0 reports — seats held to the final sha | lens cadence (T-e) |
| **deploy duration** | no record | one stamp pair in `post-deploy.py` |

## 4 · THE COST SHAPE — cited, not re-derived

Audit §0–§1: **51.9 browser-minutes** across 45 walks · **9 h 20 m elapsed**, of which **8 h 06 m 34 s**
(87 %) is one human hold on a stop rule with no latency term · **38 % of walking was shape** — the
harness under test inside the battery (28 %) and re-driving unmoved bytes (10 %) · **per changed served
line, lap 7 tested at lap 6's rate** (1 per 30.3 vs 1 per 28.2). Added by §8: reading wall time
**median 27 min per report**; reports written for **15 of 45** walks.

**Paul's framing rule holds on the numbers:** the volume was proportionate to an 8× build; a ceiling
would remove thoroughness (F1, B) and leave the shape. **His second rule holds too:** rounds within a
lap need not be the same size — battery C re-drove J0 × 5 for zero possible new information.

## 5 · WHAT THIS MEANS FOR ROW T — the spine handed to the seats

Everything below is **already ruled, already measured, or an open question named as one**. The seats
size it by symbol; nothing here is a step yet.

| # | item | status | source |
|---|---|---|---|
| S1 | gate ① unit → **(journey, lens)**; `instrumented` re-keyed with it (T-f) | ruled Q2 | audit §3f, §8f |
| S2 | lens = **posture only**; fixture data leaves `ROLES` with the journey | ruled Q3 | plan §2c |
| S3 | **declared cell list at beat 6**; the gate prints longest-unwalked; J1 · J5 · J7 (and webkit, returning-device) print UNWALKED | ruled Q7 + Q4 as corrected | §3 above |
| S4 | **per-run unspent invite** for J1 — a property of the arrival | ruled Q1 | plan §3a |
| S5 | **impact-scoped re-runs by ROUTE**, byte proof machine-derived and printed on the gate's face | ruled; T-a, T-b | audit §3c, §4 |
| S6 | **rounds within a lap sized to what moved** — first round full cell list, later rounds impact-scoped down to one run-through; carried cells named or it is a cut | paul-stated 2026-09-11 (brief §1d) | — |
| S7 | ⭐ **arrival-state as a declared property of the journey**: profile (clean · returning-device · signed-in-desktop) · engine (chromium · webkit) · text (default · A+) — picked per cell, not a fixture, not a second harness | paul-stated 2026-09-11 (brief §1e); agreed by coordination | §2d, §3 |
| S8 | **a pilot walk before the four** on any changed journey (M2) | unruled — **question for Paul** | audit §3b, §5 |
| S9 | **a ranked household at lab** loaded headless before any freeze (M1) | unruled — **question for Paul**; sits between row T and the engine manifest | audit §3d, §5 |
| S10 | **the identical-failure read** — N of N lenses, one assertion ⇒ SUSPECT HARNESS, stop (M4) | computable only after S1 | audit §3b |
| S11 | **M7 — every `href="#"` control changes the visible region**: a static check, zero browser | proposed in §8h | W2, W5 |
| S12 | **lens cadence** (T-e): when a lens reads — final sha only, or per candidate | unruled — **question for Paul** | audit §3e; 30 unread walks |
| S13 | **the non-blocking channel** (T-i): a fixed heading; CARRY per candidate; a reader | paul-asked 2026-09-11 | audit §8d; 63 bullets |
| S14 | **MODEL POLICY per act** with the reading-tier falsifier (the receipt's schema ids on `R01-arrive.fold.png`) | required section (brief §1c) | readback §1 |
| S15 | **a refusal journey's own expected-events profile** (zero is the pass) | from strict's permanent 🔴 | audit §3f rider |
| S16 | **the stop rule's two classes and a latency term** (M5) | ⛔ **entirely Paul's** — row T does not touch it; the plan names it as OUT with the reason | audit §3a |
| S17 | **third-party 429 scope** (T-h) — declare in the coverage line rather than caveat per run | unruled; may be *do nothing, declared* | audit §3f |
| S18 | `release-state.py:119` — derive the UX clause from the gate's own function | one line; the build window's, lap 8 | audit §8e |
| S19 | **deploy duration** — one stamp pair in `post-deploy.py` | specified | audit §8g |
| S20 | the lens roster's two uncovered cells (`map-points`, `other`) and `handover` as a journey | user-researcher's ruling | seat-portfolio |

**Out of row T, with the ruling:** the stop rule (S16, Paul's) · a scheduler / selection engine / sampling
budget (plan § Sequence; audit § do-not-build) · a second "fast" harness · removing `--watch` ·
properties beyond 3 (Q5) · the second-member journey's *build* (BACKLOG B3; row T only names its cell).

## 6 · WHAT THIS ANALYSIS DID NOT READ

The 30 unwritten reports (there is nothing to read) · the seats' full REPORT.md prose beyond the
findings sections and the *noticed* counts · `journey-walk.py`'s action-list bodies beyond what the
audit read · the deploy legs' internals · lap 8 (not yet open — its monitoring lands as a stage-note on
the plan when its battery runs). Every number above is the audit's, the tools' own output this morning,
or a count over run directories; none is from the chronicle's authored prose stamps.
