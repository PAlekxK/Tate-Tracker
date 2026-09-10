# The interests ask, reframed as ACTIVITIES — what you'd like to DO, not a domain to rank

- row: `onboarding/index.html` § `INTERESTS` (`:908`) and § s5 (`:728`) · commissioned `[paul-stated 2026-09-10]`
- objective: O3
- class: engine · declared
- seats: content-steward → **owed, not run**: every label and sentence here is authored content that reaches a person, and this file drafts and stages rather than ratifies — the repo's standing rule is that copy reaching a reader is human-confirmed before it ships
        ux-expert → owed, not judged: no layout moved, but the chrome above the list grew 130px to 243px (§6) and that shape is the seat's call, not this file's
        user-researcher → owed, not judged: §7's "Growing things" question is a product call about absorbing "Houseplants!" into the garden module, not a copy call
        engineering-partner → waived: no tool was built and the machinery is byte-identical to HEAD (§3, §9)
        ai-advisor → waived: no model is on this path — capture stays deterministic and the free-text answer is stored verbatim
- ready: agent-proposed 2026-09-10 — Paul rules
- stage: concept
- wip-exception: builds nothing and opens no item between concept and QA. It re-authors words on an existing
  screen; the machinery underneath is byte-identical (§3) and no tool's contract moved.

---

## 1 · What Paul asked for, and what was actually changed

> *"I'm also open to just removing or replacing that question about the modules. We bring it one step closer
> to the customer by just asking what they'd like to do."* · *"what are some of the things you'd like to do on
> this property? Gardening, working in the garage or shop."* `[paul-stated 2026-09-10]`

**The ASK was re-authored. The ANSWER was not touched.** Nine of eleven labels and eight of eleven
descriptions now name a verb the reader could do this afternoon. Ids, order, `builds` and `soon` are
unchanged, verified by parsing both versions and comparing (§3).

| id | was | now |
|---|---|---|
| `house-systems` | Household systems | **Keeping the household systems running** |
| `papers` | Papers and documents | **Keeping the paperwork straight** |
| `equipment` | Equipment and tools | **Working with tools** |
| `garden` | Gardening | **Growing things** |
| `motor-pool` | Vehicles | **Looking after a vehicle** |
| `wildlife` | Wildlife | **Watching what comes around** |
| `map-points` | Marking spots on the map | **Marking where things are** |
| `map-zones` | A map you draw yourself | **Drawing your own map** |
| `handover` | Handing it all over | **Getting it ready to hand over** |
| `ask` | Asking questions about your place | *unchanged — already a verb* |
| `other` | Something else | *unchanged — **and it must stay**, see §4* |

The question itself: *"What matters most at your place?"* → **"What would you like to spend time on at your
place?"** The first asked for a verdict on a taxonomy; the second asks about an afternoon.

## 2 · ⭐ The rule that stops an activity presuming a place

The brief's hazard was correct and is the hardest constraint here: **an activity presumes a place harder than
a subject does.** "Working in the shop" assumes a shop the way "Gardening" assumed a yard, so the 09-06
ruling applies with *more* force, not less.

> **The presumption lives in the NOUN, never in the VERB.**

So every label names a verb plus *the reader's own belongings*, and **not one names a building, a facility, an
acreage or a tenure.** Paul's own example was "working in the garage or shop" — and *shop* is exactly the noun
that could not survive; "Working with tools" keeps the verb and drops the room. `papers` lost "deeds", which
presumed an OWNER: a renter has a lease, an heir has a folder nobody has opened.

### The condo-reader test, run row by row

Ten of eleven read clean for someone in a condo — they meet the verb and their own belongings, never a
building they do not have. **One residual, reported rather than papered over:**

⚠️ **`map-zones` — "Trace your own areas onto a picture of your place."** A condo's picture of its place is a
floor plan; the feature is aerial-basemap tracing. This is the one row where condo-neutrality and honesty
about what the feature *is* genuinely pull apart, and I chose honesty, because the seed rule forbids
describing an unbuilt thing as friendlier than it is. It is a **property of the feature, not of the wording** —
it cannot be fixed in copy.

## 3 · What did NOT change, and why each was frozen

Verified by parsing `INTERESTS` out of both `HEAD` and the working tree with node and comparing structurally:
**`ids/order/builds/soon identical: True`.**

- **The ids** are the join. They are what `postAnswer` and `saveProfile` actually transmit — the label travels
  only as a display copy — and five of the eleven are literally module names in `momlib.MODULES`. Freezing ids
  while re-authoring words is what makes this a reframe rather than a migration.
- **The order** encodes universality `[paul-ruled 2026-09-06]`. Re-tested under the new wording (§2) and it
  survives. It also **must not** be reshuffled: every rank event records the POSITION an item sat in, so a
  reorder would break the one series that can tell a real preference from an artifact of being near the top.
  Freezing it keeps rank data recorded before and after this change directly comparable.
- **`soon`** still marks the seeds, and the marker still travels into storage.

### ⛔ Two claims in the commissioning brief that FAILED verification

1. **"Five tools read `builds`" is FALSE.** `grep -rn "builds"` across the repo finds **zero** consumers
   outside `onboarding/index.html`. `builds` is never transmitted — `postAnswer` sends `ranked` (ids),
   `saveProfile` sends `{id,label,soon}`. Those five tools read the module/domain *vocabulary* that `builds`
   names, via `momlib.MODULES` and `estate.json`. The brief's conclusion (keep the ranking) is right; its
   stated reason is not. **`builds` is presently a declaration with no reader** — the class CLAUDE.md rules
   against ("an event with no reader is not instrumentation"). Flagged, not fixed: wiring a ranking to a
   module switch is a product decision, not a copy change.
2. **"Mom has already answered the current question" is unsupported.** `legacy` (est-3c9f1a, her Fernwood) has
   **zero** `onboard-interests` records. All three that exist are on `home`/est-e6696a and are walk records.

## 4 · What happens to answers already recorded — nothing orphans

Three `onboard-interests` records exist, all on `home`/est-e6696a:

| when | ranked |
|---|---|
| 2026-09-07 14:23Z | `house-systems > papers > motor-pool > equipment > wildlife > other` |
| 2026-09-07 15:17Z | `onboard-interests-other`: **"Houseplants!"** |
| 2026-09-10 16:26Z | `garden > motor-pool > house-systems > equipment > wildlife > papers` |

**All store ids, not labels.** Re-authoring labels cannot misread them. `read-onboarding.py` parses ids
(selftest 0 failures). A reader's own stored record is a snapshot in their localStorage, so
`estate/index.html` still replays the words they actually chose under — which is correct: they should see
what they were shown, not what we renamed it to afterwards.

⛔ **`"Something else"` is a JOIN KEY, not just copy** — and this is the reason it is the one label left alone.
`viewer.html:18476` suppresses that idea card by lower-cased string equality, so renaming it would make
"Something else" render in the app as an idea card of its own. Recorded here so nobody tidies it later.

## 5 · ⛔ TWO PROTECTIONS THIS WORK NEARLY BROKE, both caught before shipping

**(a) "Household systems" is Mom's coined phrase and is protected.** The first draft said *"Keeping things
running"* and quietly retired her word — which `viewer.html`'s `EMPTY_CARD_COPY` forbids in as many words
(*"Mom's own coined phrase and is protected — do not normalise it"*) and which CLAUDE.md's ribbon rule forbids
in general: *"adopt her words, never improve them… if she names a thing, that is its name."* She coined it,
hedged that it might be the wrong term, and was right. The shipped form puts a **verb in front of her noun**;
the reframe does not get to replace the noun. *(Caught by the duplicate window `onboarding-ask-82`, verified
here against `viewer.html:18364`.)*

**(b) The reversibility line nearly re-shipped a measured defect.** The first draft of the interests
disclosure said *"you can change it any time"* — **the exact sentence the address screen was already burned
by**: the gate-1 walker *"was promised 'you can change it any time' on the screen where she typed, and could
find no route back afterwards."* Measured here before repeating it: a returning reader whose record holds a
name and an address is redirected to `/estate/` at `:2168` and **cannot reach the interests screen again.**
"Any time" would have been false for everyone except the person still standing on it. The shipped line
promises only what the Save button actually does — `go5` deliberately does not hide on success, it re-labels
to "Update these" and re-tapping re-sends.

## 6 · The four-field contract, now on the screen

`[paul-ruled]` **every ASK states USE · NOT-use · WHO SEES IT · reversibility.** This screen stated only USE.

| field | the line |
|---|---|
| USE | *"Your order tells me what to build next"* |
| NOT-use | *"— nothing is switched off or hidden because you left it out"* |
| WHO SEES IT | *"Only Paul sees it."* |
| reversibility | *"Reorder and save again as often as you like."* |

⚠️ **The NOT-use clause is TRUE TODAY BY MEASUREMENT and will become a lie the day the ranking is wired to a
module switch.** Nothing currently reads the ranking to switch a module (§3). If that path is ever built, this
sentence changes with it — flagged beside the sentence in the file itself.

⚠️ **The cost, measured, not asserted** (414 × 848, A+): chrome above the list goes **25 words / 3 paragraphs /
130px → 56 words / 4 paragraphs / 243px.** That is +113px on the screen content-steward already flagged as
carrying the most reading in the journey. The contract is owed and I paid it; **whether four paragraphs is the
right shape is a content-steward call**, and this is the number that seat needs.

## 7 · ⚠️ ONE PRODUCT QUESTION FOR PAUL, not a copy question

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

**"Growing things" (was "Gardening") is the one label whose universality genuinely rose** — it now reaches a
windowsill. That is directly responsive to the only free text anyone has ever typed into "Something else":
**"Houseplants!"** — a person telling us the old label had shut them out.

⛔ **But `feedback-dispositions.json:102` ruled that record a *twelfth interest, NOT a module request*, and
"whether to build anything for it stays Paul."** Widening the label to reach a windowsill quietly absorbs it
into the `garden` module (`plant · weed · zone · care-calendar`) ahead of that ruling. **Raised for his call
rather than landed silently.** The conservative alternative is to keep "Gardening".

*(It is deliberately NOT moved up the list. Moving it would re-lead with gardening, which is exactly what the
`mom` seat objected to. The wording earns the reach; the position stays honest.)*

## 8 · The routed address-screen finding — **two thirds of it was noise**

The elicitation lens reported that the address screen *"says nothing about what the address is used for, what
it is NOT used for, or that it can be changed."* **Verified against the rendered screen** (headless, 414×848),
per the lens's own rule that 13 of its first 16 findings were noise:

| sub-claim | verdict |
|---|---|
| no USE stated | ❌ **false** — *"We work out your weather and what grows there from this address"* |
| no WHO-SEES stated | ❌ **false** *(not claimed, but worth recording)* — *"Paul — who built this — is the only other person who sees it"* |
| not-use absent | ✅ **CONFIRMED** — the one genuine gap |
| can't be changed | ⚠️ **partly** — it said *"You can fix it before saving"*, which is pre-commit only |

⛔ **And "before saving" is the hard-won correction, not an oversight** — see §5(b). Do not re-add the stronger
promise until a self-serve edit exists.

**Amended in place, words traded not added:** the not-use clause is paid for by folding who-sees into the same
breath, and the sentence now points at the s4 check by name instead of going quiet about what happens after.

> *"We work out your weather and what grows there from this address — nothing else, and it goes no further
> than Paul, who built this. You can fix it before saving, and check it on the next screen."*

⭐ **Measured:** 32 → 38 words, and the paragraph's rendered box is **UNCHANGED at y=561–653** with the button
at 671. The added words wrap into lines that already existed, so the disclosure costs **no vertical space** and
stays entirely above the commit control — which matters, because its position above the button was itself a
2026-09-05 measurement.

🟠 **The account-screen reversibility finding is CONFIRMED and is NOT fixed here.** It needs the same
verify-what-exists-first treatment §5(b) demanded, and the reframe was the commissioned work.

## 9 · Verification run

| check | result |
|---|---|
| `INTERESTS` ids / order / `builds` / `soon` vs HEAD | ✅ identical (parsed + structurally compared) |
| page's single inline script | ✅ `node --check` clean |
| s5 rendered at 414 × 848 × A+ | ✅ renders, ranking paints 1·2, seed markers travel, "what's missing" box opens |
| s2 rendered | ✅ renders; disclosure above the button |
| page errors across both screens | ✅ **zero** |
| `read-onboarding.py --selftest` | ✅ 0 failures |
| `check-estate-neutral.py --page onboarding/index.html` | ✅ (pre-existing comment-only 'Fernwood' at `:16`) |
| `check-storage-keys.py` | ✅ every literal rostered |

⚠️ **A syntax check is not a working screen** — both screens were loaded headless and driven, per this repo's
own rule that a green byte-check has shipped a corpse before.

## 10 · ⚠️ Known divergence, deliberately NOT repaired from here

`viewer.html`'s `EMPTY_CARD_COPY` still carries the OLD noun for all five built modules (Gardening · Wildlife ·
Vehicles · Equipment and tools · Household systems). So a reader can rank **"Growing things"** and then meet a
card titled **"Gardening"**; and `viewer.html:18532`'s ask-next chip writes `EMPTY_CARD_COPY`'s label into the
**same** `fw-onboard-interests` store that `estate/index.html` replays as *"What I'll build first"* — which can
put **two vocabularies in one reader's own list**, on the surface whose whole job is showing we heard them.

⛔ **`viewer.html` is owned by another window in this lap, so it was not touched.** This is recorded as a
divergence for Paul's gate, and in the file itself, rather than repaired silently across a one-writer boundary.
**If the reframe is ratified, `EMPTY_CARD_COPY` must move with it** — that is the follow-on, and it is not
optional, because the divergence is visible to a reader.

---

## What is being asked of Paul

1. **Ratify or edit the wording** (§1 table, §6 contract lines, §8 address sentence). None of it has been
   through content-steward; all of it reaches a person.
2. **Rule on "Growing things"** (§7) — it absorbs "Houseplants!" into the garden module ahead of your own
   ruling that whether to build for it stays yours.
3. **Note the follow-on** (§10): ratifying this obliges a matching `EMPTY_CARD_COPY` change in `viewer.html`.
