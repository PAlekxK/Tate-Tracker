# THE `product-steward` ABSORPTION — ratify or reverse · RULING PROPOSAL

- row: proposed
- objective: O5
- class: engine
- stage: draft
- ready: agent-proposed 2026-09-11 — Paul rules
- seats: practice-steward → this file

**Question:** board ①·4 of `.plans/2026-09-10-OPEN-ITEMS.md:53`. The seat was chartered as a ONE-LAP
TRIAL (`.plans/2026-09-07-product-steward-CHARTER.md` §7) and then granted beats 4 and 5 of the
standing release loop with no expiry (`cycle/release/CYCLE-MAP.md:83-84`, at `71119d6`;
`grep -c 'trial' cycle/release/CYCLE-MAP.md` → **0**). Nobody ruled it. Predecessor framing and the
option costs: `.plans/2026-09-10-backlog-management-AUDIT.md` §1·A–C — **not restated here.**

⛔ **Method only.** Whether the seat's output is *worth* two beats is a value call and is Paul's.
Everything below is reachability, enactment and what each option costs the loop's structure.

---

## 1 · Did the trial's pre-registered falsifiers get answered? **NO — and its own instrument says so**

`python3 tools/product-steward.py` (read-only, run 2026-09-11), verbatim:

```
TRIAL STATE: INCONCLUSIVE  (2 rounds recorded)
What would settle it, and nothing else will:
   · a round that starts CLEAN: every recorded round so far is confounded
   · a THIRD round — two points give a direction, not a rate
⛔ Until then the redundancy figure is DIRECTIONAL, not a verdict, and neither
   falsifier may be reported as having passed or failed the trial.
```

- **R7 (redundancy ≥80% ⇒ redundant):** 18 of 37 rows = **49%** — below threshold, **not falsified**,
  and both rounds carry a recorded `--confounded` string (`.private/product-steward-ledger.json`).
- **Second falsifier (questions > writes):** **20 questions against 19 carried → 🔴 fires today** —
  and by the charter's own clause above it *may not be reported as having fired the trial* at n=2
  confounded rounds.

⭐ **So neither option can be argued from the ledger.** A ruling today is made on **structure**, not
on the trial's numbers, and should say so in its own text rather than borrow the 49% as support.

⚠️ **One premise of the 09-10 audit is now FALSE, measured after it was written.** §1·B held the
settling condition structurally unreachable because *"100% of the newest run at every seat is refused
for `report-unwritten`."* At lap 6's candidate `318416a` (`cycle/release/CYCLE-LOG.md:2317` ff.)
**all five seats wrote readable reports and `walk-integrity` counted every newest run** — the tool's
round block prints `reports the seat can READ: 5 · ✅ every seat at this build wrote its report.`
**A clean third round became available on 2026-09-10.** The blocker that made "renew conditionally"
an unowned condition has cleared.

## 2 · Is the seat structurally reachable at beats 4+5, or a checklist line? ⭐ **MEASURED: it was skipped at the first lap where its input was clean, and the lap closed green**

**Laps run since the grant (`71119d6`, 2026-09-08): two.**

| lap | candidate | beat 4 CARRY | trace |
|---|---|---|---|
| **5** | `bfa3f23` | ✅ **enacted** | `.private/synthetic-walks/CONSOLIDATION-bfa3f23.md` (09-08 17:16) + ledger row *"lap 5 beat 4 (CARRY). 12 writes … ZERO rows created"*; chronicle cites it three times (`CYCLE-LOG.md:1995`, `:2063`, `:2132`) |
| **6** | `318416a` | 🔴 **never ran** | **no** `CONSOLIDATION-318416a.md` (`ls .private/synthetic-walks/` → two files only, both older); **no ledger row**; the lap 6 entry (`:2317-2461`) carries headings for beats 1, 6, 10, 8, 11, 12 and **none for 3, 4 or 5** |

⭐⭐ **The lap 6 sweep table forward-references the beat that then did not happen** — *"its findings
enter at CARRY (4) / GROOM (5)"* (`CYCLE-LOG.md:2331`, the owed UX sweep) — and the lap closed
✅ CLOSED with production deployed at both real households. **That is the definition of a checklist
line: a named owner, a forward reference, no artifact, no consequence.**

**Why nothing caught it, verified by a second method:**

- `tools/release-state.py:115` can name only beats **8, 9, 11** (*"beats 0, 1 and 6-11 are human or
  session beats this tool cannot observe"*). Beats 4 and 5 are observable by **no** instrument.
- `python3 tools/check-release-docs.py` → ✅ *"the map and the code agree"* — it checks beat **count**
  and the three derivable beats; a skipped beat is outside its question. *(CLAUDE.md's own rule: a
  control can be entirely correct and not cover the thing you rely on it for.)*
- Beat 12's exit condition (`CYCLE-MAP.md:91`) is *zero records undisposed on a real estate*. **A
  lap can close with beat 4 unrun and beat 12 is still honestly green.**
- `OPEN-ITEMS ⑤·4` already names the half of this the seat's own tool cannot see: *"a round that ran
  and failed leaves the same trace as one that never ran."* **Lap 6 shows the other half — a round
  that was never attempted leaves that same trace too.** X and not-X, the corpus's most-repeated
  shape, now on the beat rather than on the ledger.

> ### ⭐ CRITICALITY, stated in this seat's own lane, with its evidence
> **The unenacted beat is the critical item here, not the ratify/reverse choice.** Beats 4 and 5 are
> the only beats in the loop owned by a seat that is neither Paul nor the main session, and they are
> the only two whose omission no instrument and no exit condition can detect. **True at zero business
> value:** it is a statement about which beats have a detector, and it stays true if every row the
> seat would ever carry is worthless. ⛔ It is not a claim that CARRY matters more than any other
> beat — that ranking is Paul's.

## 3 · What each option costs the loop

| | ratify the absorption | reverse it |
|---|---|---|
| **groom** | keeps the owning beat it gained 09-08 (`CYCLE-MAP.md:98`) | returns to **no owning beat** — the measured hole `LAP3-AUDIT.md:176` opened and `CLAUDE.md:583-587` still describes. The 09-07 grooming ran as a hand-commissioned SCAN and *"nothing made it recur"* |
| **the R7 falsifiers** | keep computing for as long as the seat exists, instead of expiring with a trial that never settled | stop computing; the trial closes **unsettled**, with the corpus recording a disposal made on an INCONCLUSIVE ledger |
| **the cheap kill** | given up — unless the grant is written to carry its own falsifier (§4) | preserved; `tools/product-steward.py` survives as a check, which CHARTER §7 already specifies |
| **reachability** | ⛔ **unchanged by ratification alone.** Lap 6 proves a ratified beat with no detector is still skippable | ⛔ **also unchanged** — beats 4/5 revert to the main session, which is exactly who ran lap 6 without them |
| **the register** | one edit makes map, charter and `BACKLOG.md:3376` (*"a one-lap trial as of today"*) agree | same edit needed in the other direction; the charter's §7 expiry becomes live again |

⭐ **Neither option, by itself, changes what lap 6 measured.** That is the finding: the ratify/reverse
axis and the enactment axis are orthogonal, and only the second one has evidence behind it.

## 4 · ⭐ RECOMMENDATION — **RATIFY, and make the grant self-bounding in the same edit**

**Ratify the absorption: beats 4 and 5 are `product-steward`'s, standing.** Grounds, all structural:

1. **Reversal is a disposal on an inconclusive ledger.** The charter's own clause forbids reading
   either falsifier as fired at n=2 confounded rounds; reversing on it would do exactly that.
2. **Reversal re-opens a measured hole to close an unmeasured one.** `groom` loses its owner again —
   the one thing `LAP3-AUDIT` §3 found missing — while the defect lap 6 actually exhibited (an
   undetectable beat) is untouched by the reversal.
3. **The condition that made "conditional renewal" dishonest has cleared** (§1). A third, clean round
   is now producible inside the next lap, by the lap that runs it, at that lap's close — an owner and
   a date, which is what `.plans/2026-09-10-backlog-management-AUDIT.md` §1·C required and could not
   have on 09-10 at 17:04.
4. **Ratifying where the authority already lives ends the X/not-X.** Today a reader cannot tell a
   renewed seat from a lapsed trial whose duties were inherited. One edit to the map does.

⛔ **And ratification is only honest if the grant carries its own bound**, because a permanent grant
with no detector is what lap 6 already ran. The bound is deliberately **an artifact floor, not a
ratio**: *the round was recorded, or the skip was recorded.* ⚠️ The R7 ratios stay in
`--ledger` as a **review read at lap close, never a gate** — beat 4's questions-vs-writes is 🔴
today and confounded, and a beat whose exit condition is red from day one is one nobody runs. (Paul's
own rule; it is why spine conformance is counted and never graded.)

### The exact `cycle/release/CYCLE-MAP.md` edit — quoted, NOT made

**(a) Beat 4's exit condition, line 83.** Replace:

```
| **4** | CARRY | product-steward | each finding reaches a row it can **cite**, or opens a question where it cannot |
```

with:

```
| **4** | CARRY | product-steward | each finding reaches a row it can **cite**, or opens a question where it cannot — **and the round is RECORDED**: `.private/synthetic-walks/CONSOLIDATION-<candidate>.md` exists and `product-steward.py --record` wrote its ledger row, **or** the chronicle names the beat SKIPPED with the reason. ⛔ Lap 6 ran with all five reports readable and produced neither (`CYCLE-LOG.md:2317`), and every instrument stayed green: `release-state.py` can observe only beats 8/9/11 and beat 12's exit reads undisposed records. **A round that never ran, one that ran and failed, and one that ran clean must not leave the same trace** (`OPEN-ITEMS ⑤·4`) |
```

**(b) One new block immediately after the beats table** (before *"**COMMIT (6) gates BUILD (7).**"*,
`:93`), so the file that grants the duty also holds its expiry:

```
### ⛔ BEATS 4 AND 5 ARE `product-steward`'s — STANDING, AND THE GRANT CARRIES ITS OWN FALSIFIER `[paul-ruled 2026-09-11]`

`.plans/2026-09-07-product-steward-CHARTER.md` §7 ruled a **ONE-LAP TRIAL**. The 2026-09-08
renumbering (`71119d6`) granted the seat two beats with no expiry, no review date and no renewal
owner, and the word "trial" appears in this file **zero** times — so the trial was **ABSORBED, not
renewed**, and could not expire, because the file granting the authority did not know an expiry
existed. **This line ratifies the grant and moves the expiry to where the authority lives.**

⛔ **The two R7 falsifiers do not expire with the trial — they become the seat's standing review**,
computed by `product-steward.py --ledger`, **read at every lap close and recorded in the chronicle.**
⚠️ They are a REVIEW, never a gate: at 2 confounded rounds the ledger reads INCONCLUSIVE and its own
text forbids calling either one fired, and a beat whose exit condition is red from day one is one
nobody runs.

⭐ **Falsifier for this grant:** if **two consecutive laps** close with every seat's report readable at
the candidate and **no `CONSOLIDATION-<sha>.md` and no recorded skip**, the ownership is decorative —
beats 4 and 5 return to the main session and the seat is a check, exactly as CHARTER §7 specifies.
**Lap 6 is the first of those two.**
```

⚠️ **Neither edit changes the beat count, the numbering, the owners column or any derivable beat**, so
`python3 tools/check-release-docs.py` (✅ *12 beats declared · named beats [8, 9, 11]*) stays green.
Re-run it after the edit; a green there is evidence about the count and about nothing else.

### What the ruling implies elsewhere — reported, not resolved, and NOT edited here

1. `.plans/2026-09-07-product-steward-CHARTER.md` §7 (*"R7 ruled a TRIAL FOR ONE LAP, not a team
   member"*) **contradicts the ratified map** the moment (b) lands. The proposed block names the map
   as the authority; the charter still needs a `stage-note` saying so. **Whose act: Paul's or the
   seat's, not this one's.**
2. `BACKLOG.md:3376` still reads *"a one-lap trial as of today"*. Same contradiction, second file.
3. `CLAUDE.md:583-587` is stale on three counts already measured by the 09-10 audit (*eleven* beats ·
   *"`groom` has NO owning beat"* · the `LAP3-AUDIT` §5 pointer, which is §3 at `:169`). ⭐ The
   ratification makes the `groom` line wrong in a **second** way, so it wants correcting whichever
   option Paul picks. `check-release-docs.py` cannot see it — it never reads `CLAUDE.md`
   (`OPEN-ITEMS ⑤·5`).

## 5 · Falsifiers for this proposal

- ⭐ **The recommendation is wrong if** beats 4 and 5 are enacted at the next two lap candidates and
  the ledger reaches three rounds with one clean, and the R7 ratios then read ≥80% redundancy or a
  sustained questions>writes — in which case the seat was redundant and REVERSE was right all along,
  on evidence instead of on structure. **The proposed edit is what makes that readable.**
- **The reachability finding is wrong if** a `CONSOLIDATION-318416a.md` exists outside
  `.private/synthetic-walks/`, or lap 6's CARRY ran and was recorded somewhere this file did not
  look. Checked two ways: `ls .private/synthetic-walks/CONSOLIDATION-*` (2 files, `c821051` and
  `bfa3f23`) and the tool's own line — 🔴 *no consolidation for this round* — plus the ledger's two
  rows. A third method available to Paul: `grep -n 'CARRY\|GROOM' ` over the lap 6 section.
- **The "premise now false" claim in §1 is wrong if** the five readable reports at `318416a` would
  not have supported a clean round for some reason the charter names — the `--confounded` field is
  where that would have to be recorded, and it is empty because no round was recorded at all.
