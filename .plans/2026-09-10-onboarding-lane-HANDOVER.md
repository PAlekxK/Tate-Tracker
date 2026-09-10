# Onboarding lane — what a fresh window does not know

- row: close-out for lane `onboarding-ask-b3`, merged to local main at `ea5f838`
- objective: O3
- class: engine · declared
- seats: content-steward → **owed, not run**: every string this lane touched reaches a real reader and NONE of it is ratified — that is the first thing a successor must not assume away
        ux-expert → owed, not judged: the shelf's empty state and the founding route are a surface decision the seat has not seen
        engineering-partner → waived: no tool built; §1's limitation is stated rather than engineered around
        user-researcher → waived: no claim about a person is made here
        ai-advisor → waived: no model on this path
- ready: agent-proposed 2026-09-10 — Paul rules
- stage: concept
- wip-exception: a handover record. Builds nothing, opens nothing.

**Written against the stated next target** `[paul-stated 2026-09-10]`: *"QA deploy with synthetics walking in
and then walking. It is a big test, and that's where I want to go before we start onboarding folks more and
sending them out links."* **The screens this lane owns are the middle of that walk** — the shelf a person lands
on, and the founding path out of it. Everything below is ordered by what would waste a successor's day.

---

## 1 · ⛔ READ THIS FIRST: MY EVIDENCE IS ROUTE-MOCKED, NOT A WALK

Every verification in this lane was **headless Chromium with `/api/grant/whoami` intercepted and fulfilled
from a literal**. That is strong evidence about *rendering logic* and **zero evidence about integration.**

**Not once did I walk sign-up → found → shelf against a live Worker.** So:

- ⛔ **`release-gate.py` has not been satisfied by anything I did.** It requires every seat to walk the actual
  sha in Chrome. My runs are not walks and must not be counted as any.
- ⚠️ **The first synthetic through these screens is the first real integration test of them.** Expect to find
  something. That is the instrument working, not a regression.

## 2 · ⚠️ THE TRAP THAT WILL EAT A DAY AT QA: the shelf's answer depends on the WORKER, not the page

`homes/index.html` decides "does this person have a home" like this:

```js
var told = Array.isArray(d.estates);
var empty = told ? d.estates.length === 0 : !(merged.name || merged.addressParts);
```

**Two code paths, and which one runs is a property of the deployed Worker.**

| the Worker at that origin | what happens |
|---|---|
| carries `6414435` (returns `estates`) | reads the record's own answer — correct |
| **older** (no `estates` field) | silently falls back to **inferring** from an absent name and address |

⭐ **So if a synthetic on an estate-less account does NOT see the founding button, suspect the Worker before
the page.** The deploy hook was reporting qa several commits behind HEAD all through this lane's work, so a
stale QA Worker is the *likely* state, not a corner case.

⛔ **And do not "fix" the fallback away.** It exists because **absence of the field is a fact about the
Worker, never about whether someone has a home** — and this repo has a live QA/production build-path split.
Deleting it would make an old Worker's silence read as "you have nothing."

### The specific field trap, registered but worth repeating

**Gate on `estates`, never on `hasEstate`.** `hasEstate` is set on the two ZERO-estate branches only
(`worker.js:4400`, `:4523`); the grant-resolved `whoami` at `:1008` **omits it**. So `!d.hasEstate` is `true`
for a person who *has* a home, and any client gating on it **offers "Set up my first home" to every
household in the product.** `estates` is on both branches — `[]` or `[{…}]`. *(Registered on `b5a4247`'s
trailer. I was pushed at `hasEstate` by name and only avoided it by reading the payload.)*

## 3 · What this lane actually changed, and what it is evidence of

| change | verified how | ⚠️ |
|---|---|---|
| `homes/index.html` empty shelf — stopped saying *"Open your invitation link"* to someone who already opened it | **4 states driven headless** at 414×848: no-grant · unreachable (incl. its "Sign in again" door) · a real home (1 row, NO button) · estate-less (0 rows, button → `/onboarding/`). Zero page errors in each | copy is **DRAFT** |
| the **phantom home** — `:310` rendered a home row unconditionally, so an estate-less account met a place called "My Home" that opens nothing | same run; found only because I checked whether my own fix could fire — **it could not** | — |
| `estates` predicate replacing the inference | **7 payload shapes**, incl. the trap: `estates:[{…}]` with a null name, where the old inference showed the founding button to someone who already has a home | — |
| `onboarding/index.html` address disclosure — added the missing NOT-use clause | rendered; **32→38 words with the box UNCHANGED at y=561–653**, button at 671 | copy is **DRAFT** |
| the interests reframe (9 labels, the question, 4 contract lines) | ids/order/`builds`/`soon` byte-identical; both screens rendered, zero errors | ⛔ **UNRULED — see §5** |

## 4 · ⛔ FOUR THINGS THAT LOOK LIKE TIDY-UPS AND ARE NOT

**(a) A label rename is not a find-and-replace.** `viewer.html:18412` builds `byLabel` **from**
`EMPTY_CARD_COPY`'s labels, and it is the only resolver for records stored before ids existed (`:18408` says
so). Rename those labels and a stored `{label:"Gardening"}` resolves to `id: null` — the pick then vanishes
from `READER_RANKING` via `.filter(Boolean)` (so the app **re-offers a module already ranked**) and fails the
idea-card guard at `:18475`, rendering a **built module as an unbuilt idea card**. Blast radius is not one
browser: `onboarding:1195` and `estate:529` hydrate from the server's `d.ranked`, and `worker.js:3877` stores
what the client sent. **The `ask`/`name` split (§5) avoids all of this by never moving the names.**

**(b) `"Something else"` is a join key, not copy.** `viewer.html:18476` suppresses that idea card by
`label.toLowerCase() === "something else"`. Rename it and it renders in the app as an idea card of its own.
**Nothing checks this.**

**(c) ⛔⛔ NEVER RE-ADD *"you can change it any time"* to the address screen.** It shipped, and was removed
because the gate-1 walker *"was promised 'you can change it any time' on the screen where she typed, and could
find no route back afterwards"* (`onboarding/index.html`, s4 confirm block). *"You can fix it before saving"*
is the **hard-won correction, not an oversight.** I nearly re-shipped it on the interests screen and caught it
only by checking: `:2168` redirects a returning reader with a name and address to `/estate/`, so they cannot
reach that screen again. ⭐ **The rule, and it is cheap: verify a reversibility promise against the actual
route back before writing it.**

**(d) `＋ Add a home` stays inert.** Walked by `tate-tracker-ec`: a second estate returns `409
already-has-an-estate`, the person then holds two grants, and `whoami` still answers with one, because it
resolves from the **route row** — the grant is not the bottleneck. Promoting the card would manufacture a home
its owner could never open. It unblocks **last** in the chain `route → grantsFor(personId) → whoami returns an
array → X-Estate → the card`. *"One account, one home — for now"* stays true.

## 5 · ⛔ THE ONE THING PAUL OWES, AND WHY I DID NOT GUESS

The relay said *"Paul ruled the wording: keep `Gardening`."* **That settles one label of nine and says nothing
about the question sentence.** Three readings produce three different diffs — revert `garden` only · revert all
nine · revert nine and the sentence. **The branch holds all nine and is merge-clean either way.** `af` has
taken the gap back to him; it is a small commit once answered.

⭐ **And my own argument for the change is void**, which a successor should know before defending it:
- The *"Houseplants!"* evidence is **Paul's own account** (`p-yjnw9lt41nww` = `pkirsch`, Grant Park Condo).
  `.user-research/2026-09-08…:401` already said *"Paul's twelfth interest"*; my two plan docs re-narrated it
  anonymously as a stranger shut out by the label. **That was the whole case.** Corrected on `54813e0`.
- **Four of ten rows were already activity phrases** (`Gardening` · `Marking spots on the map` · `Asking
  questions about your place` · `Handing it all over`). `garden` was never on the noun side, so the set
  argument never reached it.

**My recommendation is `content-steward`'s: keep `Gardening`, and take the `ask`/`name` split** (two fields per
row — the verb the question offers, the noun the app uses). ⚠️ **Its caveat must travel with it:** the split
*relocates* the divergence rather than removing it — `estate/index.html:427` replays the stored *ask* phrase
against the card's *name*. Softer than today's bug, not zero.

## 6 · 🔴 A LIVE DEFECT THAT IS NOT MINE AND OUTLIVES EVERY RULING ABOVE

**`viewer.html:18481`'s sentence-case regex matches 1 of 5 `soon` labels — and `viewer.html` is unchanged from
`origin/main`, so this renders in production today:**

> *"You put **P**apers and documents first."* · *"You put **M**arking spots on the map first."* · *"You put
> **A**sking questions about your place first."* · *"You put **H**anding it all over first."*

The regex is `/^(A|An|The) /` — written for the `wide-eyed` seat's round-9 finding about *"A map you draw
yourself"*, the **only** label it ever matched. `:18447` is the same shape for built modules. ⛔ **Reverting
the interests labels does not fix it** — it restores 4/5 broken, not 0/5. **The remedy is to sentence-case at
the slot, and it is owed whichever way Paul rules.** Already `BACKLOG.md` **TIER 2 · 25**.

## 7 · Housekeeping

- **Branch `onboarding-ask` is merged** (`ea5f838`) and 0 ahead of local main as of this note.
- ⚠️ **"main" names two things here and one is protected.** `origin/main` is Mom's frozen production
  (divergent history; my first merge-check ran against it and reported 689 ahead with conflicts).
  `local main` tracks `origin/staging` and is the integration line. **Say which one, every time.**
- `cycle/release/cycle-state.json` is modified in the tree by the post-commit hook, not by this lane.
- `.plans/2026-09-10-interests-reframe-VERIFY-82.md` — **committed verbatim by this lane**, see §8.

## 8 · The closed window's file

`onboarding-ask-82` was a duplicate window launched on the same brief. It read my working tree, wrote nothing,
sent me six findings and closed before I could reply. **Two of them were load-bearing and I acted on both:**
it caught that my draft retired *"Household systems"* — Mom's coined phrase, protected by name in
`viewer.html:18364` — and it independently found the `"Something else"` join-key dependency.

**Committed verbatim, unedited.** It also carries one finding I never recorded elsewhere: `onboarding
/index.html:398`'s comment **asserts a reversibility clause the rendered markup does not contain**. That is
this repo's most-repeated failure shape — a comment claiming copy that isn't there — and it is still open.
