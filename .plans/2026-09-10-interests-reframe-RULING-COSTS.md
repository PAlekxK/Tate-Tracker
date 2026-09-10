# What each branch costs — so the interests ruling takes a minute, not an hour

- row: companion to `.plans/2026-09-10-interests-as-activities-PROPOSAL.md` (committed at `4439010`)
- objective: O3
- class: engine · declared
- seats: engineering-partner → **owed, not judged**: §3's migration hazard is a real defect this file only enumerates — the fix belongs to whoever owns `viewer.html`, and that owner does not currently exist
        content-steward → waived: no new copy is drafted here, only the already-staged wording is costed
        ux-expert → waived: nothing is proposed that moves a surface
        user-researcher → waived: this file costs a decision, it does not make a claim about a person
        ai-advisor → waived: no model on the path
- ready: agent-proposed 2026-09-10 — Paul rules
- stage: concept
- wip-exception: enumerates consequences and builds nothing. No file outside this note was touched.

⛔ **`viewer.html` was NOT edited.** It has no owner this lap. Every line below is a *proposed* change-set
with its current text quoted, not an applied one.

---

## 1 · ⭐ THE THREE QUESTIONS ARE NOT ONE BUNDLE — two of them are free

This is the part worth reading. **The label reframe is the only thing that touches a product boundary, and
nothing else depends on it.**

| what shipped in `4439010` | depends on the labels? | can ship alone? |
|---|---|---|
| **The address sentence** (adds the missing NOT-use clause, s2) | **No** — different screen, different flow, no shared identifier | ✅ **yes** |
| **The four-field contract lines** (s5 use · not-use · who-sees · reversibility) | **No** — chrome above the list; reads identically over old labels or new | ✅ **yes** |
| **The question wording** ("What would you like to spend time on at your place?") | **No** — "Gardening", "Vehicles" and "Wildlife" are all things one spends time on; the sentence is true over either list | ✅ **yes** |
| **The 9 label changes** | — | ⚠️ **this is the only one with a cost** |

**So the safe three-quarters can ship now.** The address fix closes a ruled contract gap on the
highest-leverage field in the product; the contract lines close the same gap on the interests screen. Neither
one waits on a product decision about houseplants.

⭐ **And that reframes the ruling itself.** It is not *"approve this change"* — it is:

> **Ship the contract fixes now, and decide about "Growing things" separately, whenever you like.**

## 2 · Branch A — "ratify the reframe": the exact `viewer.html` change-set

Five label strings, all inside `EMPTY_CARD_COPY` (`viewer.html:18346-18370`):

| line | current | would become |
|---|---|---|
| `18348` | `label: "Gardening",` | `label: "Growing things",` |
| `18352` | `label: "Wildlife",` | `label: "Watching what comes around",` |
| `18357` | `label: "Vehicles",` | `label: "Looking after a vehicle",` |
| `18361` | `label: "Equipment and tools",` | `label: "Working with tools",` |
| `18367` | `label: "Household systems",` | `label: "Keeping the household systems running",` |

⚠️ `18356` carries a comment that would go stale — *"the reader-facing word is VEHICLES, which is what they
ranked"*. Under branch A the reader-facing word is no longer Vehicles, and a comment asserting otherwise is
the class of stale claim this repo pays for most.

**Six downstream sites read those labels. Five need no edit; one is a defect.**

| site | what it does | under branch A |
|---|---|---|
| `18412` `byLabel` | maps label → module id, the fallback for records stored without an id | ⛔ **BREAKS — see §3** |
| `18476` "something else" | suppresses that idea card by exact lowercased match | ✅ no change — that string lives in `INTERESTS`, which is why it was frozen |
| `18532` ask-next chip | writes `EMPTY_CARD_COPY[m].label` into `fw-onboard-interests` | ✅ follows automatically — this is what *creates* the two-vocabularies bug today, and changing the source fixes it |
| `18539` ask-next feedback | posts the label as the note body | ✅ follows automatically |
| `18606` card title | overrides `.main-card-title` with the label | ✅ follows automatically |
| `estate/index.html:427` | replays `r.label` from the stored record, verbatim | ✅ **no change, and must not change** — it repeats back what the person was actually shown, which stays correct even after a rename |

## 3 · ⛔ THE ONE THING THAT MAKES BRANCH A MORE THAN A FIND-AND-REPLACE

**`byLabel` is built FROM the labels being changed, and it is the resolver for older records.**

```
18411   const byLabel = {};
18412   Object.keys(EMPTY_CARD_COPY).forEach(k => { byLabel[EMPTY_CARD_COPY[k].label.toLowerCase()] = k; });
18413   … { id: x.id || byLabel[String(x.label || "").toLowerCase()] || null, … }
```

`viewer.html:18408`'s own comment says why it exists: *"ONBOARDING STORES OBJECTS, NOT IDS — {label, soon},
and from tonight {id, label, soon}."* **Records written before that change carry a label and no id**, and
`byLabel` is the only thing that resolves them.

**Rename the labels and `byLabel` stops recognising the old ones.** A stored `{label: "Gardening"}` resolves
to `id: null`, and then:

1. `18414-18419` — `READER_RANKING` does `.filter(Boolean)`, so **the pick silently disappears** from card
   ordering (`18433`), from the top-card highlight (`18564`), and from the ask-next exclusion list (`18517`)
   — meaning the app would then *offer them a module they had already ranked*.
2. `18475` — the idea-card guard is `if (it.id && known.has(it.id)) return;`. With a null id it does **not**
   return, so a **built module renders as an unbuilt "idea card"** titled "Gardening".

**That is the same failure class this lane already fixed twice today**: a control correct about its contract
and wrong about the world. And it would land on the surface whose entire job is showing someone we heard them.

⚠️ **Blast radius is wider than one browser.** `onboarding/index.html:1195` and `estate/index.html:529` both
hydrate `fw-onboard-interests` from the server's `d.ranked`, and `worker/worker.js:3877` stores whatever the
client sent (`acct.ranked = b.ranked.slice(0, 20)`). So a pre-id **account** record propagates its old labels
to every device that person signs in on. It is not self-healing.

✅ **The fix is small and must ship in the same commit** — teach `byLabel` both vocabularies:

```js
const LEGACY_LABELS = { "gardening": "garden", "wildlife": "wildlife", "vehicles": "motor-pool",
                        "equipment and tools": "equipment", "household systems": "house-systems" };
const byLabel = Object.assign({}, LEGACY_LABELS);
Object.keys(EMPTY_CARD_COPY).forEach(k => { byLabel[EMPTY_CARD_COPY[k].label.toLowerCase()] = k; });
```

⭐ **This is a permanent alias table, not a migration step** — it can never be deleted, because a record
written under the old vocabulary may be read at any future point. Whoever applies branch A should say so in a
comment beside it, or the next tidy-up removes it.

**Estimated branch A: 5 string edits, 1 stale comment, 1 alias table (~6 lines). One file.**

## 4 · Branch B — "keep Gardening": what still ships

> ### 🔴 CORRECTION, 2026-09-10 — the "Houseplants!" evidence is PAUL'S OWN, and this file said otherwise
>
> This file described that answer as **"a person telling us the old label had shut them out."** That is
> **false**. `onboard-interests-other-atz6kh` carries personId `p-yjnw9lt41nww` = `pkirsch`, place *Grant Park
> Condo* — **Paul's own production account**, and `.user-research/2026-09-08-localized-feed-and-property-type.md:401`
> already said so in plain words: *"**Paul's** twelfth interest."*
>
> ⛔ **The 09-08 artifact was careful about attribution and this file re-narrated it anonymously** — while the
> personId was in a dump this window had run itself and did not resolve. That is the exact failure this thread
> recorded nine times today, committed here. Caught by `content-steward`'s seat.
>
> **What survives:** it is still a real answer, given at the real ask, by someone at a condo who reached for
> "Something else" rather than "Gardening". **What does not:** it is not a stranger at the door, and *that was
> the whole rhetorical force* of the argument for widening the label. n=1, and the 1 is the author.

**Zero changes to `viewer.html`.** The divergence in §2 exists *only* because the labels moved; leave them and
there is nothing to reconcile.

In `onboarding/index.html`, reverting only the 9 labels while keeping everything else would need the label
strings put back and the two ⭐ comment blocks explaining the reframe trimmed to match. **The address
sentence, the four contract lines and the question wording all stay** — none of them references a label (§1).

⚠️ **One thing would be lost that is worth naming:** "Gardening" is the label the only piece of free text
anyone has ever volunteered was working around. **"Houseplants!"** arrived through the "Something else" door —
someone telling us, in the one place the product asks, that the list did not have a row for them. Branch B
keeps that gap open. That is a legitimate choice; it should just be a *chosen* one.

## 5 · A finding from this enumeration, which strengthens the reversibility line

`estate/index.html:431` offers **"Change the order ›"** on the replayed ranking — and `:450-457`'s comment
says exactly what it is:

> *"THE EDIT ROUTE IS A NOTE, NOT A TRIP BACK THROUGH THE FLOW — F12. Re-entering onboarding's step()/K_STEP
> walks the reader forward through the confirm and the ranking again… correcting a value tells Paul what it
> should say; the loop closes on his side."*

So the shipped line — *"Reorder and save again as often as you like"* — is **true and slightly understated**.
There is also a post-hoc route: from their own place, someone can say the order is wrong and it reaches Paul.

⚠️ **It is not self-serve, so the wording must not imply that it is.** But if Paul wants the reversibility
promise to reach further, *"or tell me later from your place"* would be TRUE today — unlike *"change it any
time"*, which was not. **Offered as an option, not applied**: it is more words on the screen already carrying
the most reading, and that is a content-steward call.

---

## What this asks of Paul

1. ⭐ **Ship the contract fixes now?** The address NOT-use clause and the s5 four-field lines are independent
   of every open question (§1). They close a ruled gap and wait on nothing.
2. **Then, separately: "Growing things" or "Gardening"?** (§4 names what each costs.)
3. **If branch A: the alias table in §3 is not optional** — without it, older records lose their picks and
   render built modules as unbuilt ideas, across every device the person signs in on.

---

## 6 · `content-steward`'s seat, verified in this lane — two claims stand, one needs a refinement

The seat's findings are about files this window owns, made by a seat that does not. Verified here rather than
accepted, per the rule that has caught nine relayed claims today — **including one of this file's own (§4).**

### ② "the nouns→activities frame is false for four of ten rows" — ✅ CONFIRMED, and it voids this file's argument

Read at `onboarding/index.html:908-946` as it stood before the change. Of the ten real rows (excluding
*Something else*), **six were nouns and four were already activity phrases**: `Gardening` · `Marking spots on
the map` · `Asking questions about your place` · `Handing it all over`.

⛔ **`garden` was never on the noun side.** So "the list names activities now" is true of six rows and does not
reach the seventh. **"Growing things" is a standalone scope decision wearing a set's clothes**, exactly as the
seat puts it — and with §4's correction removing the Houseplants argument, **there is now no evidence-backed
case for it in this file.** The seat's recommendation to keep `Gardening` is the better-supported position.

### ③ "a seventh downstream site, and it fires immediately" — ✅ CONFIRMED, ⚠️ with a refinement that changes the remedy

`viewer.html:18481` lowercases a label's first letter **only** when it matches `/^(A|An|The) /`. Measured
against all five `soon` rows, old labels and new:

| row | today | after the reframe |
|---|---|---|
| `papers` | ⛔ "You put **P**apers and documents first." | ⛔ still broken |
| `map-points` | ⛔ "You put **M**arking spots on the map first." | ⛔ still broken |
| `ask` | ⛔ "You put **A**sking questions about your place first." | ⛔ unchanged label, still broken |
| `handover` | ⛔ "You put **H**anding it all over first." | ⛔ still broken |
| `map-zones` | ✅ "You put a map you draw yourself first." | ⛔ **breaks** |

⭐ **The defect is already live on four of five seed rows in production.** The regex only ever matched **one**
label. So the reframe does not create this — it removes the single case that worked, taking it from 4/5 broken
to 5/5.

⛔ **Which means reverting the labels does not fix it, and never would have.** `wide-eyed`'s round-9 fix was an
instance fix that never generalised — the same pattern `homes/index.html:212` records against itself in as many
words (*"the fix did not generalise, because I fixed the instance"*). **The real remedy is to sentence-case
properly at the slot**, and it is owed whichever way Paul rules. `:18447` is the same shape for built modules.

### ④ the `ask` / `name` split — ✅ BACKED, and it voids §3

Two fields per row: `ask` (the verb phrase the question offers) and `name` (the noun the app calls the thing).

⭐ **It removes this file's largest cost.** `byLabel` is built from `EMPTY_CARD_COPY` **names**; if names never
move, the resolver never stops recognising an older record — **so §3's "not optional" permanent
`LEGACY_LABELS` table is not needed at all.** The seat's citation against it is fair and specific:
`momlib.py:367` — `MODULE_ALIASES = {}  # kept as a hook; empty by ruling`, over *"No aliases: one
vocabulary."* **That shape has been ruled against in this repo once already**, and §3 proposed it without
noticing.

⚠️ **One caveat the split does not remove, only relocates.** `estate/index.html:427` replays the **stored**
label under *"What I'll build first"*, so a reader would meet the *ask* phrase there and the *name* on the card
title. That is **softer than today's bug** — which puts both vocabularies inside the *same* list, via the
ask-next chip — but it is not zero, and it should be a decision rather than a surprise.

**Net: §3 above is superseded. Branch A under the split is ~5 rows gaining a field, one line at `:18532`, and
no alias table.**

### ⑤ "Watching what comes around" — ✅ conceded

It names only the half that arrives, and `VOCABULARY.md` §4 rejects `resident` for precisely that reason: the
chickadees that never leave are the ones the phrase excludes. **"Watching what's around"** — which is what the
description already said — is correct.
