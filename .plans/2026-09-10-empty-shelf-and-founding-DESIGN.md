# The empty shelf, and the founding step that is already built

- row: `homes/index.html` § the empty-state resolver (`:175-199`) and § `addcard` (`:106-121`) · commissioned by the coordinating window after `[paul-ruled 2026-09-10]` that signup stops granting an estate
- objective: O3
- class: engine · declared
- seats: content-steward → **owed, not run**: every string below reaches a real reader on the first screen after signup, and none of it is ratified
        ux-expert → **owed, not judged**: §2 changes what an empty state offers, which is the seat's call on the surface a person meets first
        engineering-partner → owed, not judged: §4's precondition is a claim about `whoami`'s resolver that `tate-tracker-ec` owns and should confirm
        user-researcher → waived: no claim about a person is made or relied on
        ai-advisor → waived: no model on this path
- ready: agent-proposed 2026-09-10 — Paul rules
- stage: concept
- wip-exception: designs and stages; nothing was edited. `homes/index.html` is not in this window's declared lane and was read only.

⛔ **NOTHING WAS SHIPPED OR EDITED.** No file outside this note was touched.

---

## 1 · ⭐ THE HOLE IS NARROWER THAN IT LOOKS — the founding flow already exists

The brief for this work described a screen that does not exist. **It largely does.** Onboarding already
collects exactly what founding a home needs, in the right order, with a resume path:

| onboarding screen | collects | is |
|---|---|---|
| `s0` | username · password · contact · colour | **the account** |
| `s1` | *"What do you call it?"* | **the home's name** |
| `s2` | street · unit · city · state · ZIP | **the home's address** |
| `s4` | shows the address back, "Does that look right?" | **the founding confirm** |

And `onboarding/index.html:2168-2171` already routes it:

```
if (who && who.name && who.address) { location.href = "/estate/"; return; }
var at = read(K_STEP);
step(at === "4" ? 4 : at === "3" ? 4 : at === "2" ? 2 : 1);
```

**An account with no name and no address resumes at step 1 — the naming screen.** That is the founding step,
and it is built, walked and instrumented.

⭐ **This also satisfies "never ask twice" structurally rather than by discipline.** There is no second place
that asks for an address, so there is no opportunity to ask again. Any *new* founding screen would create one.

> ### The design conclusion
> **Do not build a founding screen. Route to the one that exists.** What is genuinely missing is two strings
> and one button's destination.

## 2 · ⛔ THE ACTUAL DEFECT: the empty shelf tells a person to reopen a link they already used

`homes/index.html:190-193` resolves four states. Three are correct — they are B1's fix, and they are why
*"I could not check"* no longer prints as *"you have nothing"*. **The fourth is the hole:**

| state | current string | verdict |
|---|---|---|
| no grant | "Open your invitation link and your homes will be here." | ✅ true — they hold no credential |
| `unknown` | "We couldn't reach your homes just now — nothing is lost. Try again in a moment." | ✅ B1's fix, correct |
| `fetching` | "Looking for your homes…" | ✅ correct |
| **reached, and empty** | **"Open your invitation link to set up your first home."** | ⛔ **wrong, and about to become the normal case** |

**They already opened it — that is how they have an account.** The sentence sends a person who did everything
right back to a credential that is spent, on the first screen after signup.

⭐ **This is the third instance today of one failure shape this repo has already recorded twice by name:**
`onboarding/index.html:980` — *"A LINK MUST NOT REPLACE A CREDENTIAL THAT WORKS"* — and `:1002` — *"A PERSON
WHO BROUGHT NO LINK CANNOT BE TOLD THEIR LINK IS BROKEN."* Both were Paul walking it and quoting the sentence
back. This is the same defect from a third side: **telling someone to re-present a credential that already
worked.**

⚠️ **Today it is rare** (an account whose estate is absent — Paul's own B1 incident). **Under the new ruling it
is what every new signup sees**, because an account will no longer come with a home.

### Proposed — the reached-and-empty branch only

> **"Your account is set up. Your first home is next — it takes a name and an address, and I build the rest
> from there."**
>
> **[ ✓ Set up my first home ]** → `/onboarding/`

Why each half:
- **"Your account is set up"** names a thing achieved. The state is a beginning, and the first clause has to
  say so before anything else — an empty surface that opens by describing an absence reads as a fault however
  the next sentence softens it.
- **"it takes a name and an address"** sets the price honestly and low. The measured killer at this stage is
  *"a form with more than one typed field"*, and naming the cost is what keeps someone walking.
- **"I build the rest from there"** is the product's actual promise and it is true: one address yields
  coordinates, elevation, hardiness zone, frost dates, watershed.
- **No mention of a link, in any branch that has a working credential.**

⚠️ The button is a **route to `/onboarding/`, not a new flow.** `K_STEP`'s resume logic (§1) lands them on the
naming screen by itself.

## 3 · What founding should show back — and why it is the cheapest Perspective seed we will ever get

The address confirm at `s4` already shows the address back and asks *"Does that look right?"*. **What it does
not show is what was derived from it** — which is the one moment the product can demonstrate its own premise
instead of asserting it.

⭐ **And those derived facts are `inferred` by construction**, which makes them exactly the shape
`harvest-questions.py` already harvests: a value we guessed, marked askable, that someone standing on the
property can settle. *"I think you're at about 1,420 ft — is that right?"* is a variety-confirm card in
everything but subject.

⚠️ **Two constraints, and the first is load-bearing:**
1. ⛔ **A derived value must render as an estimate at founding, not as a fact.** `CLAUDE.md`'s governing rule
   is that measured and modelled signals stay visually distinct at every altitude — and this repo's most
   expensive elevation error (2,959 ft, stamped `confirmed`, from a ~90 m global model that reads 86 ft high
   on this spur) is exactly what a confidently-rendered derived number produces.
2. **It is display-only at founding.** Promoting any of it to canon happens through the existing fold path,
   at the administrator's gate — never as a side effect of someone finishing setup.

**Scoped out of this note deliberately:** which facts to show, and their wording. That is a content-steward and
`user-researcher` question, and §2 is the part that is broken today.

## 4 · ⛔ THE `＋ Add a home` CARD IS A DIFFERENT PROBLEM WITH A HARDER PRECONDITION

`homes/index.html:106-121` already carries a founding affordance, and it is deliberately inert:

> *"The `+` IS PRESENT AND HONEST. It cannot found a home yet: a credential resolves to exactly one estate
> (`grantFor` rejects any other), **so a home founded today would be one its owner could never reach.**"*
>
> Its card reads: **"One account, one home — for now."**

**Do not promote this card in the same change as §2.** They look alike and are not:

| | **first** home (§2) | **second** home (this section) |
|---|---|---|
| person holds | zero homes | one already |
| needs a person→estates index? | **no** — a one-estate resolver is sufficient | **yes** |
| safe today? | ✅ | ⛔ **not until the resolver changes** |

⚠️ **`homes/index.html:262` states the blocker as current fact** — *"A credential resolves to exactly one
estate today; there is no person→estates index."* If that is still true, promoting `＋ Add a home` would
manufacture a home its owner cannot open — **the precise failure the card's own comment exists to prevent**,
and a control reporting a success it did not achieve, which this project has broken twice.

⛔ **`tate-tracker-ec` owns that endpoint and should confirm the resolver's state before anyone touches this
card.** I did not verify it beyond reading this file's own claim, and a file's claim about another file is
exactly the class that has failed verification eight times in this thread today.

**Meanwhile "One account, one home — for now" stays TRUE and stays put.**

## 5 · Ownership, stated plainly

⚠️ `homes/index.html` is **not** in this window's declared lane (`onboarding/index.html`, and `viewer.html` as
of this afternoon). It was read, never written. §2 is a two-string change plus one button destination, and it
is ready to apply the moment someone says the lane covers it.

---

## What this asks for

1. ⭐ **Confirm §1** — that founding routes to onboarding's existing `s1`/`s2` rather than getting a new
   screen. It is the difference between two strings and a new flow, and it is what makes "never ask twice"
   structural.
2. **Ratify the §2 copy** (content-steward has not seen it; it reaches a real reader on the first screen after
   signup).
3. **Confirm the lane covers `homes/index.html`** before §2 is applied.
4. ⛔ **Get `tate-tracker-ec` to confirm §4's resolver state** before anyone promotes `＋ Add a home`.
