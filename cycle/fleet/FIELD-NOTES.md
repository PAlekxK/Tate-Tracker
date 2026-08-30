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

*(none yet — the store was created 2026-08-30, before its first sweep.)*
