# FIELD NOTES — the quarantine

**Third-party reports about our machines: forums, owner accounts, videos, vendor listings,
model-generated summaries. `paul-stated 2026-08-30`:** *"I think it's important to also get
kind of third-party forum takes, which can be kind of dangerous… that information may need to
be sequestered and treated differently than the user's manual."*

Agreed, and this file is the sequestration. **Nothing in here is a fact about a machine.**

Tiers are NOT redefined here — they are `A / B / C` from
`.private/service-records/bronco-1989/SOURCES.md`, promoted from one vehicle's private file to
the fleet standard. **Everything in this file is tier C by construction.** The rule that
governs it is already written there and is the whole point: **a C never silently becomes an A.**

---

## ⭐ THE RULE THAT MAKES THIS SAFE: never take a NUMBER from a forum. Take a QUESTION.

The tiers say how *good* a source is. They do not say what a forum is *good at*, and that is
the missing half:

| source | authoritative for | never |
|---|---|---|
| **the manual** | values — capacity, torque, clearance, spec bands | what actually breaks |
| **the field** (this file) | **failure modes, symptoms, what to check first** | any value, ever |
| **the machine** | settles both | — |

A factory manual will never tell you *"the regulator/rectifier cooks on these and takes the
battery with it."* Only owners know that, and it is genuinely valuable — it is the difference
between testing four things and testing the right one first.

But its legitimate output is **a hypothesis with a test attached**, not a number. That is
exactly why quarantine works rather than merely being tidy: **a hypothesis cannot launder into
the record, because the record only accepts a measurement.** A forum may send you to T3. It may
never tell you what T3's pass band is.

## Why sequestration has to be STRUCTURAL, not a habit

**The danger is migration, not error.** This portfolio has already measured it: the Bronco card
carries a `_chatgptProvenanceWarning` recording **four wrong card values** traced to two
ChatGPT threads — one of them wearing a *false* "read off the actual sidewalls" provenance. The
claim did not arrive labelled as junk. It arrived, got summarised into a note, and three weeks
later sat in `vehicles.json` looking exactly like a manual-sourced value.

A forum claim is the same mechanism with a different source. So:

- **This file is never read as a source by any tool.** `vehicles.json` is the record; this is not.
- **A card value's `source` may never be a URL.** Tier A means *"the file is in `_assets/` and
  anyone can check it without asking us."* A link is not a held document. **Checked mechanically
  by `vehicle-brief.py --check`** — 0 findings on the day it was installed, which is the point:
  a guard fitted before the problem, not after.
- **Promotion is an event with a name.** A note leaves this file only when a non-field source
  or a physical read confirms it — and the entry says which, and stays here marked `promoted`.
  It is never deleted, because a promotion nobody can audit is a laundering with better manners.

## Retrieval decays, and it has been measured here

Of 27 Bronco bookmarks, 11 were once unretrievable — 7 behind a tollbit paywall handshake, 3
host 403s, 1 dead. ⚠️ And the correction that came with it: **`curl` returning 403 is a fact
about the client, not the page** — several loaded fine in Chrome. So:

- **Archive at read time.** A thread you did not archive is a citation you cannot check later.
  Precedent and destination: `_assets/forum-threads-archived-<date>.md`.
- Record the date the source **speaks to**, not only the date we fetched it —
  `[[feedback_ingestion_time_is_not_evidence_time]]`. Ingestion order confers no recency.

## Corroboration: three, from independent AUTHORS

Where a field claim cannot be checked against a document or the machine, it wants **three
independent authors** — not three links, which can all be one person quoted onward, and not
three posts in one thread. `[[feedback_show_three_when_one_cannot_be_checked]]`. One author
repeated by two others is one source wearing a crowd.

---

## Entry schema

```
### <machine id> — <the claim, in one line>
- tier:        C (always, in this file)
- kind:        failure-mode | symptom | procedure | part-fitment | opinion
- authors:     N independent · <who/where>
- speaks to:   <what year/model/mileage the claim is about>  (unknown is a valid answer)
- fetched:     <date> · archived: <path or NOT ARCHIVED>
- test:        <the measurement or physical check that would settle it>   ← REQUIRED
- status:      open | corroborated | falsified | promoted → <what confirmed it>
```

**`test:` is required and a note without one is not accepted.** A field claim with no way to
settle it is an opinion, and opinions do not get a row in a machine's file.

---

## Notes

### SWEEP 1 — 2026-08-30 · dr200s-2017 · charging / battery drain

**Scope, per `paul-stated` the same day: *"they should all be very specific to the two hundred."***
Generic Suzuki charging advice was found in quantity and **deliberately not recorded** — the first
search returned DL650, GSX-R and GSXR threads and nothing on a DR200. Folding those would be exactly
the laundering this file exists to prevent.

⚠️ **THE MODEL BOUNDARY BIT IMMEDIATELY, and it is the same boundary that produced the kickstarter
error.** Every DR200 thread found is **DR200SE-generation (1998 / 2003 / 2007)**, not the 2017
DR200S. Forums use "DR200" for both. Every note below records what it speaks to, and none of them
speaks to this bike.

---

### dr200s-2017 — a dead charging system on a DR200 reads ~12.9–13.0 V running AND stopped
- tier:        C — and **weaker than C: a search-result summary of a post I did not read.**
- kind:        failure-mode
- authors:     1 · Steve Sturdevant, ThumperTalk, 2008-09-10. ⬆️ **UPGRADED — thread READ IN FULL
               via Chrome**, not a search summary. Verbatim: *"When not running I get 12.9 volts at
               the battery, when running I get 12.9-13.0."*
- speaks to:   1998 DR200 (SE generation) — **NOT the 2017 DR200S**
- fetched:     2026-08-30 via Chrome · archived: NOT ARCHIVED
- ⚠️ his own method looks wrong, and that is the point: he measured the alternator's three wires
               **each to GROUND** and read 0.0 V, then concluded two alternators were bad. Stator
               windings are normally isolated from ground, so phase-to-**ground** reads ~0 on a
               HEALTHY unit — the test is phase-to-**phase**. *(My inference, not his and not a
               document's — flagged as such.)* **A forum post can be a real symptom wrapped in a
               wrong diagnosis, and the symptom is still worth having.**
- test:        **T3.** Meter across the battery, engine warm, hold ~5 000 r/min. A charging system
               that is working climbs to 13.5–14.5 V; one that is dead sits at the resting figure
               and does not move with revs. ⭐ **The useful half is the SHAPE, not the number: read
               it stopped AND running and compare.** A single running reading of 12.9 V could be a
               flat battery being charged; the same figure at rest AND at 5 000 r/min cannot.
- status:      open — a hypothesis with a test attached, which is the only thing this file may hold

### dr200s-2017 — DR200 owners report batteries that die repeatedly, one per season
- tier:        C (search-result summary, threads not read)
- kind:        symptom
- authors:     3 · owners of a 2003, a 2007 and one undated DR200 (2003 thread READ IN FULL)
- speaks to:   DR200SE generation, 1998–2007
- fetched:     2026-08-30 via Chrome · archived: NOT ARCHIVED
- test:        T4 overnight hold, then **T5 as an A/B** (charger attached-unpowered vs removed).
               A repeatedly-dying battery is the SYMPTOM these owners share; none of the summaries
               names a confirmed cause, so this note buys a *prior*, not an answer.
- status:      open
- ⚠️           **Do not read this as "these bikes have a known battery problem."** Owners with a
               working bike do not post. A forum is a census of complaints, never of machines.

### ⭐ dr200s-2017 — THE KEY SWITCH POSITION can hold a circuit live and flatten it while parked
- tier:        C · **thread read in full via Chrome**, 2 responders on a 2003 DR200 (ThumperTalk,
               2007). One raised key-switch position; a second gave the isolation method below.
- kind:        failure-mode
- speaks to:   2003 DR200 (SE generation) — **NOT the 2017 DR200S; the key positions may differ**
- test:        **Free, today, no meter.** Look at what the key can be turned to on THIS bike — if
               there is a park / accessory detent past OFF that holds the tail light on, check
               where Mom leaves it. Then the responder's own draw test, which is T5 without a
               meter: pull the negative cable, **tap it against the post — a spark means something
               is live**. Isolate by unplugging one connector at a time and re-tapping.
- status:      open — ⭐ **the best thing this sweep produced.** It is a candidate cause for the
               *"left it sitting and it lost charge"* episode that costs nothing to check, it is
               checkable BEFORE the battery finishes charging, and it is the kind of thing a
               factory manual will never tell you.
- ⚠️           Records a POSITION to look at, never a claim about this bike's switch. Confirm at
               the machine.

### SEARCHED-NEGATIVE — the accessible DR200 threads carry no diagnosis
- `suzukiforum.com` 2007 DR200 starting-issues thread: **fetched and read in full — one post, zero
  replies, no measurements, no cause.** A dead end, recorded so nobody spends the search again.
- `thumpertalk.com` and `suzuki-forums.net` both return **307 → tollbit.<host>** to an agent. The
  two threads most likely to carry real measurements (*"DR 200 Charging system Alternator"*,
  *"DR 200 Drains Battery"*) are behind that handshake.
- ✅ **RESOLVED THE SAME SESSION — `paul-stated`: *"What about accessing via Chrome"*.** Both
  threads loaded **first try** in his logged-in Chrome and were read in full. **The 307 was a fact
  about the client, exactly as the Bronco bookmark sweep concluded** — this is the second
  independent confirmation of that correction, and it should now be the default move rather than
  an afterthought: *agent blocked ≠ page gone.*

### VERDICT ON THIS SWEEP — one usable hypothesis, and a lot of nothing
Recorded plainly because lap 1 pre-registered the question *"does the FIELD beat earn its place, or
produce only noise?"* ⬆️ **REVISED after the Chrome pass: it earned its place.** The first answer —
*"a thin margin"* — was written while two of three threads were unreadable, and **it was a verdict
on the retrieval, not on the beat.** With Chrome it produced three things, all of them procedures
or positions to check and none of them a value:

1. **read the charging voltage stopped AND running** and compare — a single running figure of
   12.9 V is ambiguous, the same figure at rest and at 5 000 r/min is not;
2. ⭐ **the key-switch position**, a free check available before the battery even finishes charging;
3. **the negative-cable spark test** — T5's question answered without a meter, then isolated by
   unplugging one connector at a time.

⚠️ **And it produced one clear illustration of why the quarantine exists:** the 1998 owner's
measurements are real and his diagnosis is probably wrong. **A field note is worth having and is
still not a fact.**
