# Fernwood — the second rationalization, PROPOSED 2026-09-02 · **APPLIED 2026-09-03**

> ## ✅ STATUS: **APPLIED 2026-09-03 in `9f17419`** `[paul-approved 2026-09-03]`
> `BACKLOG.md`'s head marker now reads `(rationalized 2026-09-03)` — the application date, since the
> clock measures time since a rationalization was *applied*, not drafted. `check-backlog-drift.py`
> reads **rested · 110 lines head→list · 5 sections above the tracks**. §1's moves were applied by a
> script that asserts every original line survives; **every move was a MOVE.** One declared
> deviation: THE FOLD and the household build-out were moved **whole** rather than split into riders
> and narrative — a split is a judgment edit, not a move. §2's four wrong rows and §3's eleven cards
> remain **surfaced, not fixed / not ruled**; §6's pre-registered question is still open and
> discharges at the next OWED run that is acted on.

**Trigger:** `python3 tools/check-backlog-drift.py` → **OWED**, 2 of 3 signals fired.
**Scope:** the reading order of `BACKLOG.md`'s live region. **Not** the tracks, which are the
decision record and are correct as-is.

---

## 0 · The finding: the collision the last rationalization killed has re-grown

The 07-29 run was commissioned to end **"the two colliding `▶️ NEXT` tables."** It did, and its head
declared the contract: *"This is a POINTER list, not a second tracker… read this for what now."*

**Measured 2026-09-02:**

| | 2026-07-29 | today | |
|---|---|---|---|
| `BACKLOG.md` | 575 lines | **2,421** | 4.2×, 134 commits |
| pointer head → its own TIER 1 table | adjacent | **734 lines apart** (19 → 753) | ⚡ fired |
| days since a rationalization | 0 | **35** | ⚡ fired |
| sections wedged above the tracks | — | **18** (11 added since) | · quiet, 11 of 12 |
| of those, already finished | — | **5** | fact, not a signal |

⭐ **The defect is not size, and this matters for what gets proposed below.** A long decision record
is correct and wanted — that is what the tracks are *for*. The defect is that **the ranked list is no
longer what you read after the head.** A reader obeying the head's own instruction now crosses 710
lines of session dumps, routed intake and shipped records before reaching what-now. The collision did
not come back as a second table; it came back as **distance**, which no one was watching.

**Today's reading order** (the problem, stated as a list):

```
  19   ▶️ NEXT — "read this for what now"
  43 ┐ pond azalea · basemap session · ux-sweep walkthrough · THE FOLD ·
     │ household build-out · contractors · 4× INBOUND from photo-organizer ·
 752 ┘ orienting principle · engagement warning · 2× SHIPPED records      ← 710 lines
 753   🔥 TIER 1 · FIX NOW          ← what-now, finally
 791   🧭 TIER 3 · STEER
 828 ┐ the shape system (SHIPPED 08-02, 168 lines) ·
1030 ┘ two-pass review (RAN 08-03, FROZEN)                                 ← 203 lines
1031   ⚖️ TRACK A vs TRACK B
1047   👤 WAITING ON PAUL                                                  ← 1,028 lines down
1083   # TRACK A …                                                          the decision record
```

**`👤 WAITING ON PAUL` is 1,028 lines below the head.** It is the shortest path to the only work
Paul can unblock, and it is the last thing anyone reaches.

---

## 1 · Proposed reading order — the diff, as section moves

No row is deleted and no row's status is changed. **Every move is a MOVE.** The live region becomes
only what a reader needs to decide what to do next; everything else goes to the track that owns it or
to the archive that already exists at the bottom of the file.

```diff
  # ▶️ NEXT — the one true list (rationalized 2026-09-02)
+ ## 👤 WAITING ON PAUL — and nothing else is          (was L1047, ↑ 1,028 lines)
+ ## 🗳 DECISION CARDS OPEN — 11 of 12                  (new pointer block; see §3)
  ## 🔥 TIER 1 · FIX NOW — remaining                    (was L753, now adjacent to the head)
  ## ✅ TIER 2 · CONFIRMED — she already answered
  ## 🧭 TIER 3 · STEER
  ## ⭐⭐ THE ORIENTING PRINCIPLE                        (was L580 — a lens; keep, below the list)
  ## 🚨 READ THIS BEFORE CITING ANY ENGAGEMENT NUMBER   (was L599 — a lens; keep, below the list)
  ## ⚖️ TRACK A vs TRACK B — the ranking                (was L1031 — a lens; keep, below the list)
  # TRACK A — Mom's field journal
- ## 🌸 THE POND AZALEA WANTS MOVING            → Track A (A2, the record about her place)
- ## 🛰 BASEMAP & LAND-DATA SESSION (104L)      → Track A (A2) — session dump, keep whole
- ## 📐 From the 2026-08-31 production ux-sweep → Track A (A4) — Paul's walkthrough, open items only
- ## 🗺 THE FOLD — SHIPPED 08-31                → riders to Track A; narrative to the archive
- ## 🗺 INBOUND: photo→zone join has a floor    → Track A (A2)
- ## 🌿 INBOUND: species at fairway-border      → Track A (A2)
- ## 📷 INBOUND from photo-organizer 08-28      → Track A (A2)
  # TRACK B — Fleet & equipment
- ## 🏠 Household systems build-out — SHIPPED   → riders to B6; narrative to the archive
- ## 🧑‍🔧 CONTRACTORS & TRUSTED PEOPLE (69L)     → Track B (new B8) — it is a Paul-facing register
- ## 🔧 INBOUND: mower blade sharpening dated   → Track B (B2, the record) — already labelled Track B
  ## Recently shipped / SHIPPED / KILLED  ← the archive that already exists
- ## ✅ SHIPPED 2026-07-29 — Tier-1 correctness pass        → archive
- ## ✅ SHIPPED 2026-07-29 (evening) — agent-drivable sweep → archive
- ## 🎨 The shape system — SHIPPED 2026-08-02 (168L)        → archive  ← the single biggest block
- ## 🔭 Two-pass fresh-eyes review — RAN 08-03, FROZEN      → archive
```

**Result:** live region **1,064 → ~230 lines**; head-to-TIER-1 gap **734 → ~40**; the four
already-finished narratives (261 lines) leave the region a reader crosses to find open work.

### Why these three stay in the live region when the rest leave

`THE ORIENTING PRINCIPLE`, `READ THIS BEFORE CITING ANY ENGAGEMENT NUMBER` and `TRACK A vs TRACK B`
are not rows — they are **lenses that govern how the ranked list is read**, and the engagement one is
a standing correctness guard against citing a number wrong. They belong *with* the list, just not
*above* it.

---

## 1b · ⭐ THE SECOND AXIS — engine · config · instance `[paul-ratified 2026-09-02]`

Paul, after the estate-manager scoping: *"Some of the backlog rationalization discussion with this
framing will be helpful."* Asked directly whether to re-cut before he reviews: **yes — add engine vs
instance as an axis.**

**Why it belongs here and is not a second tracker.** The 07-29 tiers answer *what unblocks a row*.
This answers a question that did not exist this morning: **does this row pay once, or every time?**
Fernwood is now one instance of a product with a second and third property on the roadmap, so a row
that improves shared machinery is an investment and a row that enriches Fernwood's own record is not
— they are both worth doing and they are **not the same kind of thing**.

| class | means | in the backlog |
|---|---|---|
| **⚙️ engine** | shared machinery; serves every property; a divergence here is a **defect** | the loop · the fold path · the watermark clamp · the Guru's register system · capture infra · auth · the probes' mechanisms |
| **🎛 config** | per-property **declaration as data**, never a fork | frost dates · station MAC · coordinates · elevation · a property's declared signal set |
| **🏡 instance** | Fernwood's own record and content | plants · weeds · insects · zones · the fleet record · her zone names · season notes |

**First-cut classification at the section level** (row-level labelling is mechanical follow-on, not
done here):

| | sections |
|---|---|
| ⚙️ **engine** | A3 the loop · A5 privacy→auth · A6 Guru & capture infra · **B0 the ask loop** · L1/L2 lap machinery · M1 the feedback reader · G1 the Guru fence · A-ASK the ask design · W1 `viewer.html` ownership |
| 🎛 **config** | the physical constants inside A2 · the frost/station/coords values Track B's probe re-types |
| 🏡 **instance** | A2 the record about her place · A7 weeds · A9 insects · A8 the mine · B1–B4 the fleet record · B6 household · Z-ACK her zone names · V-SERIES |

### ⚠️ Three guards, because this axis is easy to misuse

1. ⛔ **"Engine" must not become a synonym for "important."** Mom's adoption is the open question this
   whole project rests on, and it is answered by **instance** work. A backlog that sorts engine-first
   would quietly deprioritize the only user with real evidence.
2. ⭐ **Most of Mom's machinery IS the engine — that was the panel's finding, not a hope.** Track A's
   ask → fold → acknowledge path is shared machinery now that Bob's house has a contributor. So the
   axis does **not** cut cleanly along Track A / Track B, and anyone who assumes it does will mis-file
   half the list.
3. **This axis RANKS NOTHING on its own.** It is a label that makes a tier decision better informed —
   *this Tier-3 row happens to pay three times* — never a competing sort. The tiers remain the sort.

**What it changes about §1's reordering: nothing structural.** The moves stand. Each moved section
additionally carries its class, so the migration can find its own rows without a second pass.

---

## 2 · Rows this pass found wrong against reality — surfaced, not fixed

The standing rule is *verify a row against the app before acting on it, and correct the row rather
than quietly fixing past it.* Four came up. **None is fixed here.**

| # | row / card | what the record says | what reality says |
|---|---|---|---|
| R1 | `.plans/2026-07-29-…-PROPOSAL.md` | *"Nothing here has been applied"* | applied 07-29 as `a6c89a8`. **✅ FIXED this session** — the only thing I changed, because it is the pointer `BACKLOG.md` sends readers to |
| R2 | card `fernwood-6` | *"check-cards exits 1 on one amber… criterion 3 is not met"* | **`check-cards.py` exits 0 today.** The card's stated premise is false; `q-fairway-grass-seedheads` is still active. **Re-verify before answering it** — do not answer it as written |
| R3 | card `fernwood-5` | *"how lap 2 is timed"* | laps 3–8 have since run and closed. The question as posed has been overtaken by events; what survives is the general cadence question, if anything |
| R4 | `THE FOLD` section | *"18 zones"* | `zones.json` holds **23** (+6 `_deleted`). Almost certainly normal growth since 08-31, **not** a defect — but the row reads as a current count and is not one |

---

## 3 · 🗳 Eleven decision cards are open — Paul's, not mine to rule

**Correction to the framing this pass was given:** it is **11 unanswered, not 8.** `data/decisions.jsonl`
holds exactly one Fernwood answer — `fernwood-10` (pagination dots, ruled 08-27: *"if we have the
shuffle in place, we don't need the pagination dots"*). Every other card is open.

**Nine are 25 days old** (minted in the 2026-08-08 Phase-3a migration); two are one day old.

| card | loop | question |
|---|---|---|
| `fernwood-1` | tate-tracker | Does the Almanac get a lifecycle, knowing only you can drain the queue? |
| `fernwood-2` | fernwood-fleet | Bolores paint — carpet + trim as ONE decision against factory Chestnut |
| `fernwood-3` | fernwood-fleet | Bolores corpus — confirm or reject *snapshot-at-ingest becomes the contract* |
| `fernwood-4` | tate-tracker | Control-center page — your review verdict *(open the page, not the code)* |
| `fernwood-5` | tate-tracker | After the 8/10 window — how lap 2 is timed ⚠️ **overtaken, see R3** |
| `fernwood-6` | tate-tracker | The carried amber — fairway-meadow has no photo ⚠️ **premise false, see R2** |
| `fernwood-7` | claude-meta-stack | *"Bring our fleet into…"* — which fleet, and into what |
| `fernwood-8` | tate-tracker | W13 — should Gardening be ONE card? |
| `fernwood-9` | tate-tracker | `momack_unfolded` — re-wire the dead metric or retire it |
| `fernwood-11` | tate-tracker | The ask design — is the confirm queue the wrong instrument, or the right one asked wrong? |
| `fernwood-12` | tate-tracker | Does a non-plant `suggest-add` fence get built, or does the Guru refuse gracefully? |

⛔ **Not ruled here.** Two (R2, R3) should be **re-verified or re-minted** rather than answered as
written — answering a card whose premise reality has already changed is the same failure as the
stale PROPOSAL header.

---

## 4 · Track B — the brief's premise is out of date, and the open question has moved

**This pass was told Track B "has NO loop by declared decision" and that `cycle/requests.jsonl` is
"an inbound door nothing reads on a cadence." Both were true on 2026-08-28. Neither is true now.**

Verified 2026-09-02:

- **Track B has a loop.** `cycle/fleet/CYCLE-MAP.md` + `cycle-state.json`, `lap_count: 2`, laps 1 and
  2 both **closed 2026-09-01**, seven beats, two human gates, CYCLE-SPINE S1 two-axis keys adopted.
- **The door IS swept, deterministically.** `fleet_probe.py`'s `S2 · INBOX` signal reads
  `cycle/requests.jsonl` directly (`observed_via: detector:s2_inbox`).

🔴 **But it is FIRED right now, and its published artifact says otherwise.** Live probe:

```
⚡ SEASON   45d to first frost · fall put-away open on dr200s-2017, drz400s-2001
⚡ INBOX    4 unread fleet correction(s) filed
FIRED — SEASON, INBOX
```

`cycle/fleet/cycle-state.json` still reads **`"state": "RESTING"` · `"inbox clear (6 filed, all
handled)"`**, stamped `2026-09-01T16:16:08Z` — **before** four more requests were appended at
`23:54Z` the same day. **This is the exact hazard `CLAUDE.md` already documents for the mom cycle**
(*"the state artifact is only as fresh as its last `--write-state`, and nothing runs it on a
cadence"*), now demonstrated a second time in a second loop. It is a **portfolio-shaped** finding, not
a fleet one.

**So the open question is no longer "does Track B earn a loop."** It has one. What is still open —
and is **Paul's to rule, surfaced not decided** — is `BACKLOG.md` **B0 · TRACK B HAS NO ASK LOOP**:
Track B is *"one person talking to himself,"* Paul both asker and answerer. That is a different
question from whether the loop exists, and this pass does not touch it.

---

## 5 · What this pass deliberately did NOT do

- **Did not apply the reordering.** `BACKLOG.md` is canonical; §1 is a diff for review.
- **Did not rule any decision card**, and flagged two as needing re-verification instead.
- **Did not decide the Track B ask-loop question** (B0), or re-run `--write-state` on the fleet
  artifact — a stale artifact is a finding for its own loop's next lap, and rewriting it from here
  would quietly close a lap that is legitimately FIRED.
- **Did not convene expert seats.** The 07-29 run used five. This pass is a **structural** reordering
  driven by a measurement, not a re-prioritization of what matters — and per the CYCLE-SPINE, seats
  are declared-optional with a stated reason. If Paul wants the priorities themselves re-argued
  rather than the file re-ordered, that is a different and larger run, and it should be commissioned
  as one.

---

## 6 · 📌 PRE-REGISTERED — and where it discharges

⚠️ **This pass is not a lap, so it cannot close one.** Pre-registering a question that no beat will
ever read is how a self-improvement note becomes decoration — so the discharge point is named here
rather than assumed.

**The question, registered 2026-09-02:** *were the three thresholds right?* Specifically —
`LIMIT_HEAD_GAP = 400` fired at 734 and is the signal that found the real defect; `LIMIT_DAYS = 30`
fired at 35 and may be **redundant with it** (does a time signal ever fire alone on a healthy file,
or is it just noise ahead of the structural one?); `LIMIT_SECTIONS = 12` did **not** fire at 11 and
has never been seen to fire at all.

**Discharge:** at the **next** run of `check-backlog-drift.py` that reports OWED and is acted on —
record in `MOM-CYCLE-LOG.md` (the convention `check-ux-sweep.py`'s thresholds already use) which
signals fired, whether `days` fired alone, and whether `sections` has ever fired. **If `days` has
fired alone twice with no structural drift behind it, it is measuring the calendar, not the file, and
should be dropped** — this loop's whole doctrine is that cadence is not a trigger.

**Falsifier for the design itself:** if a rationalization is ever commissioned by Paul by hand again
while this check read *rested*, the check is sited on the wrong thing.
