---
type: journey
project: tate-tracker
journey_id: places-and-settings
last_updated: 2026-09-06
evidence_level: assumption — with four `validated` anchors from a real person (Paul's own production walk, GATE2 lap 2) and one `validated (second-hand)` anchor from Bob
performer: .user-research/persona-mom.md · Paul-as-cold-start (GATE2) · tate-commons/research/bob-rolader-proto-persona.md (seat B)
sources:
  - BACKLOG.md rows 19, 19b, 19c, 20 (2026-09-06 — Paul's rulings on shape, naming and settings)
  - .design-options/2026-09-02-journey/README.md + door/ + selector/ (R1-B, R1-SA)
  - VOCABULARY.md §3b SURFACES AND DOORS · §3e AUTHORITY · §3f TWO ADMINISTRATORS · §4 REJECTED WORDS
  - estate/index.html (the arrival surface, source-read 2026-09-06)
  - .private/synthetic-walks/GATE2-paul-findings.md (lap 1 + lap 2 — a real person)
  - .private/walk-answers/README.md (the four seats, and §3 on what they cannot discover)
  - .user-research/persona-mom.md (Paul-direct tier only; the telemetry tier is invalidated)
  - ~/Developer/tate-commons/research/bob-rolader-proto-persona.md (read, not written)
  - CLAUDE.md § site physical premise · § affordances that ask vs affordances that move
---

# One journey, five acts — your places, and the two settings pages

**What this document is for.** Row 20 asked for *one document a reader can follow from cold open to
arrival without opening another*. This is the reader-side half of that: what a person is trying to do
at each of the five acts, what would make them stop, and what each surface must not do. It does not
re-litigate anything Paul ruled on 2026-09-06 — the shape (login → your places → tap in → a quiet
control back), the naming (**place**, never *property*; the shell is called nothing), settings on both
parents, and the cold start are treated as settled and are the frame, not the subject.

> ### ⛔ THREE CORRECTIONS TO THE BRIEF, MADE BEFORE ANY DESIGN CLAIM
>
> **1 · The four synthetic walk reports do not exist.** All seven runs under
> `.private/synthetic-walks/*/2026-09-06T13*/REPORT.md` — `mom`, `strict`, `wide-eyed`, and four
> `owner` runs — still carry the `WALK-REPORT-UNWRITTEN` marker verbatim. `walk-integrity.py`'s own
> rule refuses to count a seat in that state, so **nothing in this document is sourced to them.**
> `[measured 2026-09-06 — file read]` The first-person material about the current build that *does*
> exist is `GATE2-paul-findings.md`, which is a real person, and `.private/walk-answers/README.md`,
> which is a test instrument describing itself.
>
> **2 · R1-SA is not merely superseded — its central rule inverts.** `selector/` ruled that at one
> grant a switcher should be **absent rather than disabled**. That was right for a *switcher*. It is
> wrong for a *list that carries the `+`*: the moment founding lives on the list, the way back to the
> list is the only route to founding, so **the return control must be present at one place, not
> absent.** Founding makes the list unconditionally necessary. `inferred` — from Paul's 19b shape
> ruling read against the 09-02 recommendation.
>
> **3 · Act ⑤ cannot be honestly shipped in this round, and the reason is this project's own rule.**
> A credential knows exactly one place, so a `+` that founds a second place hands someone a place they
> can then never reach. *Capture must not lie* is the rule this repo has broken twice; a founding
> affordance that produces an unreachable place is the same failure one screen earlier. Sequencing
> recommendation at the bottom.

---

## 0 · The performers, and why there are three

| performer | what they bring to THIS journey | evidence |
|---|---|---|
| **Mom** | The adoption floor. Depth-1 reading, 414 × 848 at A+, and the measured split that every affordance which *asks* her scored 0 while the one that *moves* her scored 5/5. Her second place is a condo with no garden. | `validated` (Paul-direct tier) for the constraints; `assumption` for anything about the condo — the persona file carries no detail about it |
| **Paul, as a cold-start stranger** | The only person who has actually walked the current build end to end. He named an Atlanta place, tapped *Open Grant Park Oasis*, and landed on Fernwood. He also asked, unprompted, for a **profile** colour separate from a **place** colour. | `validated` — GATE2 lap 2, 2026-09-05, a real person |
| **Bob (seat B)** | The only person in the corpus who genuinely holds two places. Succession is his job: two houses, a daughter each, each daughter seeing only her own. He raised the access boundary himself, unprompted. | `validated (second-hand)` — recounted by Paul from one conversation; nothing first-hand |

⚠️ **They are not averaged.** Mom sets the floor for friction; Paul is the only source of walked
evidence; Bob is the only source of two-place evidence. Where they disagree, §2 says which one the
design should follow and why.

---

## 1 · The five acts as jobs

Each act is written as a job statement — *when \<situation\>, I want to \<motivation\>, so I can
\<outcome\>* — because that is the format Paul's other artifacts use and it forces the outcome to be
named rather than assumed.

### ① Set up an account

> **When someone I trust sends me a link, I want to become someone this thing recognises — without
> handing over more than it has yet earned — so I can get to the thing they were excited about.**
> `inferred` — from GATE2's ruling that production starts from nothing but a text, plus §3e's rule
> that a person's estates are exactly the grants minted for them.

- **What they are actually doing:** paying an entry cost for a promise made by a human being, not by
  the product. The link came from Paul. That borrowed trust is the entire budget this act spends.
  `assumption`.
- **What makes them abandon it:** a field whose *use* is not stated (the standing rule: every ask says
  use · not-use · who sees it · reversibility); a question that wraps to two lines and therefore reads
  as two questions `validated` — Paul named that as a principle himself (P17); ceremony around the
  password with no live feedback `validated` (P14, P15, and item 1/6/7 of lap 1 — he hit the missing
  reveal control twice, in ninety seconds, on a page where it existed); and being asked to choose
  something they cannot interpret. *"Pick a colour"* is that ask today `validated` (P19).
- **Emotional shape:** starts at **0** (obliging a family member), dips to **−1** at the password
  block, recovers to **+1** only if something confirms in real time that they got it right.

### ② Edit account settings

> **When something about me is wrong, or I want to see what you actually have on me, I want to find
> exactly that one thing and change it, so I can stop thinking about it.** `assumption` — no one has
> been observed opening a settings page in this product; it does not exist.

- **Three real reasons people open a settings page, and only one is configuration:** *repair* (this is
  wrong, fix it), *audit* (what do you have?), and *ownership* (make it look like mine). `assumption`,
  standard practice, and worth stating because a page built for the third serves neither of the first
  two. Bob's is the audit motive with feeling behind it — *the data is his* is the one thing he named
  with emotion `validated (second-hand)`, so *"what do you hold about me"* is a real job here, not a
  compliance chore.
- **What makes them abandon it:** the page opens as a set of empty controls rather than as their own
  current answers; the thing they came for is not visible without scrolling at 414 × A+; and — the
  one that will actually bite — **"back" goes somewhere they did not come from.** 19c already names
  that as a state requirement; it is also the abandonment trigger.
- **Emotional shape:** **0 → −1 → 0.** Nobody arrives here happy and nobody leaves here delighted.
  Success is returning to zero, quietly, in under thirty seconds. Any design that tries to make this
  page *rewarding* is solving the wrong problem.

### ③ Set up a place

> **When I've just made an account, I want to tell it about my place in my own words, so that what
> comes back is recognisably mine.** `validated` — this is P30/P31/P32 in Paul's own voice: land
> somewhere *his*, carrying initial data and a confirmation pairing, and *"what can we pull together
> for them at that level of data provision?"*

- ⚠️ **Today acts ① and ③ are welded.** The onboarding flow does both in one pass — credential, name,
  address, ranking, handoff — and the estate comes from the deployment binding. `[source-read
  2026-09-06]` That weld is invisible and harmless at one place. **At act ⑤ it must come apart,
  because founding-a-place has to run without founding-a-person.** The cheapest way to be ready for
  that is to build ③ as a segment that can run on its own from day one, even while it is only ever
  entered from ①.
- **What they are actually doing:** authoring. The name is the single thing in this whole journey the
  person invents rather than reports. Everything else — address, contact, ranking — is disclosure.
  `inferred`. That asymmetry is why the name belongs first in place settings (Paul ruled it there
  anyway) and why renaming must be cheap.
- **What makes them abandon it:** an ask the address cannot honour and nothing says so (the mail-drop
  case, already handled on the arrival page); an explanation of something the next tap would show
  `validated` (P24 — *"delete 'There's nothing in it yet'"*); and arriving somewhere that is not
  theirs `validated` (P29 — the single most important finding in the corpus).
- **Emotional shape:** **+1 → +2 at the naming → 0 at the address → +1 or −2 at the handoff.** There
  is no middle outcome at the handoff. Landing in your own place is the payoff for the whole act;
  landing in somebody else's is the end of the relationship.

### ④ Edit that place's settings

> **When the name or the look of my place isn't right, I want to change it where I'm standing, so the
> place goes on feeling like mine rather than like a record someone else filed.** `inferred` — from
> Paul's 19c ruling (name + colour first) read against the standing *everything is changeable* rule.

- **What they are actually doing:** repairing authorship. This is the same emotional register as ③,
  not as ②. A person renaming their place is finishing the naming act, sometimes weeks later.
  `assumption`.
- ⭐ **This is where the arrival page's two dead links go.** `estate/index.html` currently routes
  *"That's not right ›"* and *"Change the order ›"* into a note box, because re-entering onboarding's
  `step()` would walk the reader forward through the confirm and the ranking again. `[source-read]`
  Place settings is the destination those links were always waiting for, and the day it exists they
  stop being a message to Paul and become an edit. That conversion is also a **promise being kept**:
  the page currently tells someone their correction goes to a human, which P26 says must not survive
  to maturity.
- **What makes them abandon it:** a picker that opens showing a colour different from the one on the
  masthead they just tapped from (live risk — see §3); a rename that feels consequential (*will this
  break something?*); and a page that also carries account-level things, which makes the person
  re-read every row to work out which ones are about *this* place.
- **Emotional shape:** **0 → +1.** Small and positive. The one act in this journey where the person
  is putting their own stamp on something and it costs them nothing.

### ⑤ Set up a second place

> **When I have a second place that matters to me, I want to found it beside the first without
> disturbing the first, so both are held in one record I control.** `inferred` from two `validated`
> statements — Bob's *"two houses, one to each daughter"* and Paul's relay of Mom's condo.

- **What is genuinely new at ⑤ and is present at neither ① nor ③:** the person now has something to
  lose. Every anxiety at ⑤ is about the *first* place, not the second. `inferred` — this is the
  standard shape of a second-instance act; it is not evidenced here and nobody has been watched doing
  it.
- **What makes them abandon it:** any suggestion that the two places will mix; being made to repeat
  the full founding ceremony (they now know how long it takes, which is an anxiety they did not have
  the first time); and, for Mom specifically, being asked at founding time a question that only makes
  sense for Bob (see §2).
- **Emotional shape:** **0 at the list → −1 at the tap** (*am I about to make a mess?*) **→ 0 through
  the founding → +2 at the list with two on it.** The payoff moment of act ⑤ is not the new place —
  it is **seeing both, side by side, told apart at a glance.** That is what the second place is *for*,
  and it is the single strongest argument for a per-place colour.

### The two transitions, named

**Entering a place — the door, not the load.** R1-B, *"the room"*, was chosen at the login door for a
reason that transfers exactly: *it never puts anything between her and the weather card, which is both
of her card opens since lap 4.* The list → place transition inherits that. Emotionally it is a shift of
person: the list is **custodial and third-person** (*things I hold*), the place is **first-person and
present-tense** (*I am at Fernwood*). The top bar carries the shift — §3b already rules that it always
answers *where am I* — and colour carries it faster than words do. `inferred`.

**Leaving a place — the hallway, not the exit.** The failure mode is that a control at the top of a
full page reads as *close*, *undo*, or *sign out*, and the person who taps it feels dislocated rather
than relocated. `assumption` — but note GATE2 row 6 is direct evidence that Paul's chosen shape (small,
quiet, near the top) is exactly the shape that goes unfound. Three constraints follow:
1. It is **a destination, not a verb.** Never *Switch*, never *Back* (there is no page behind), never
   *Exit*. It points at the shelf.
2. It is **present at one place**, per the correction at the head of this document.
3. It is **outside the reading path** — it may not sit between the reader and the first card, which is
   the same rule that produced R1-B.

Emotional target: **+2 → 0**, never negative. Leaving a place should feel like stepping into a hallway
with the door still open behind you.

---

## 2 · Act ⑤ — the same act, two reasons

|  | **Bob** | **Mom** |
|---|---|---|
| **Why a second place** | Succession. Two houses, a daughter each. `validated (second-hand)` | A second place of her own beside Fernwood — a condo. `assumption`; the persona file carries no detail |
| **Mental model** | Two houses that will be **split**. The set has a plan over it. `inferred` | Two places she **holds**. Peers, one big and one small. `assumption` |
| **The anxiety at the tap** | *Will house B's people be able to see house A?* He raised this himself, unprompted. `validated (second-hand)` | *Will this disturb Fernwood?* `assumption` |
| **What "done" looks like** | Both houses exist; the boundary between them is provable. `inferred` | The condo exists and is obviously not Fernwood. `assumption` |
| **The sharpest risk** | The first open is empty. He was converted by a **populated** phone. `inferred` from a `validated` observation | Being asked to do a setup again at all. `inferred` from the ask-vs-move split |

### Where one design serves both

**The founding act itself is genuinely shared.** `+` on the list → name → address → arrival. Both
performers want the same three things from it and neither wants anything the other doesn't:

- **it must not disturb the first place** — nothing about founding may change what the existing place
  renders, and the person should be able to see that it didn't (the list, with both on it, is that
  proof);
- **it must be visibly undoable** — the standing *everything is changeable* rule, applied to the
  heaviest-feeling act in the product;
- **the new place must be distinguishable from the first at a glance** — which is the per-place colour
  doing real work rather than decorative work.

### Where the design must choose — four seams

**Seam 1 · What happens the instant founding completes.** Bob's next question is *who can see this*.
Mom's next question is *what is this place for*. Putting an access step on the founding path taxes Mom
with a question she has no answer to — nobody will ever share her condo — and omitting it leaves Bob's
entire job unstarted.
**→ Recommendation: founding ends at the place. Access is a place setting, named once on the arrival
screen and never on the founding path.** That holds Mom's floor (founding stays four taps) and gives
Bob a real destination. `inferred`. ⚠️ It also matches §3e's invariant: a grant is minted, never
derived from who someone is related to — so sharing is deliberately a separate, later act.

**Seam 2 · Peers, or a portfolio?** Mom's two are peers. Bob's two are a set with an assignment over
them. A peer list under-serves Bob slightly; a portfolio layer is actively wrong for Mom — it names her
as an operator of her own life, which §4 rejects by name.
**→ Recommendation: peers. Succession lives as a fact *inside* a place (who this one goes to), never
as a structure *across* places.** `inferred` — and flagged as a hypothesis about Bob: he asked for
per-heir access, he never asked for a portfolio view, and nothing in the corpus says he wants one.

**Seam 3 · The order of the list.** Both performers have an obvious primary and a deliberate second —
Bob explicitly deferred one house and started with the mapped one. `validated (second-hand)`. Neither
has said how they'd want them ordered.
**→ Recommendation: the order is the person's, set once and stable. Do not sort by recency** (which
would put the newest, emptiest place first, and permanently demote Fernwood the moment Mom adds a
condo) **and do not sort alphabetically** (which is a filing metaphor for a shelf of homes). ⚠️ This is
`assumption`; it is a good candidate question for both of them.

**Seam 4 · What an empty second place is allowed to look like.** At ⑤ the person founds an empty place
while looking at a populated one. Bob's stated conversion was a *populated* phone, so the contrast is
sharpest for him. Mom's cold start is ruled, so both her places start bare.
**→ Recommendation: the arrival banner's mechanism line — *"Everything here gets built from what you
tell me"* — must survive into the second place unchanged, and must decay on **state** (the first card
built), never on a visit count.** That is already the rule written into `estate/index.html`; act ⑤ is
the case that proves why it was written that way. `inferred`.

### What act ⑤ IS today, honestly

A credential resolves to one estate (`scopeFor` has zero callers; `scopeOf(env)` has 51 call sites).
`[verified in row 19, 2026-09-06]` So the truthful inventory is:

| piece of act ⑤ | can it be honest today? |
|---|---|
| the list, showing one place | ✅ yes — a list of one is a true statement |
| the quiet control from a place back to the list | ✅ yes, and it is needed even at one, per the correction above |
| settings entered from either parent, returning to its origin | ✅ yes — this is the whole of 19c and it is testable at one place |
| `+ add a place` → a second place that appears on the list | ⛔ no. The place would be founded and then unreachable |

**→ Sequencing recommendation: build ①②③④ and the list-of-one now; hold the `+` until per-request
scope lands.** A `+` that produces a place you cannot open is *capture must not lie*, moved one screen
earlier. And there is a hard consequence for the walk that follows: **not even Paul can walk act ⑤
until scope lands**, because he cannot hold two grants either. Anything that claims to have tested
act ⑤ before then has tested a mock.

### What an honest list of one looks like

- **One card. The `+`. A settings control. Nothing else.** `inferred` from Paul's 19b shape.
- **No count.** *"You have 1 place"* is a status line about emptiness; it draws attention to the thing
  the person hasn't got. `inferred`.
- **No ghost card, no empty slot, no disabled second tile.** The 09-02 absent-rather-than-disabled
  instinct was right about *this*; it was only wrong about the return control.
- **No title.** §4 rules that the shell is called nothing to a user, and *"your homes"* is plural-only
  and reads oddly over a single card — §3b flags this itself. Let the cards be the content.
  `inferred`, with the citation; Paul's to overrule.
- **It renders offline, from cache.** The site has no cell reception and Wi-Fi only near the house. A
  list that needs the network to tell you which places are yours is a door that closes when you walk
  away from the house. `inferred` from the site's stated physical premise.
- **It carries no place *content*** — no reading, no count of things needing attention. See §4.

---

## 3 · The two settings pages — what a person expects where

The test applied throughout: **is this true of the PERSON, or true of the PLACE?** A person can answer
that question about almost any row without being taught the model, which is why it is the right split.
`assumption` — standard practice, but it is also the split Paul reached independently at P19.

### Account level — true of me, everywhere

| row | why here | evidence |
|---|---|---|
| **username** | display-only; it is how you sign in and the only part of an account other people see | §3b `paul-stated 2026-09-05` |
| **password** | with the reveal and the live match check Paul asked for twice | `validated` — GATE2 items 1, 6, 7; P14, P15 |
| **how to reach you** (+ email / phone) | a fact about the person; also the one row where a *decline* was recorded and must be visible as having taken | `inferred`; the arrival page already renders it this way |
| **profile colour** | *"Pick a **profile** colour — and it must be separate from the PLACE colour; each place gets its own"* | ⭐ `validated` — P19, Paul's own words, 2026-09-05 |
| **text size** | it is about the reader's eyes, not about any place. A+ is the standard | `validated` — measured, `text_size_served` lg in 8 of 8 |
| **sign out** | the only genuinely account-scoped exit | `assumption` |
| *(later)* **get my data / delete my account** | Bob named data-is-mine with feeling; it is the thing whose absence he would notice | `validated (second-hand)` |

### Place level — true of this place only

| row | why here | evidence |
|---|---|---|
| **the name** | the one thing the person authored. Paul ruled it first | `paul-stated 2026-09-06` (19c) |
| **the place's colour** | Paul ruled it second | `paul-stated 2026-09-06` (19c) |
| **where it is** | the arrival page's *"That's not right ›"* has been waiting for this destination | `[source-read]` |
| **what I'll build first** (the ranking) | ditto, *"Change the order ›"* | `[source-read]` |
| *(later)* **who else can see this place** | Bob's unprompted requirement; deliberately off the founding path per seam 1 | `validated (second-hand)` |
| *(later)* **what this place contains** (e.g. garden on/off) | the condo's no-garden falsifier is a per-place fact | `paul-approved 2026-09-03`, C7 |

### ⛔ The colour collision — what a person expects, and where the seam actually is

**Live state:** an account-level `accent` chosen at signup, stored `fw-accent`, sent on the account row,
and painting the masthead of `estate/index.html` today `[source-read 2026-09-06]`; and a per-estate
`identity.theme.main` declared in `instance/*.json` — Fernwood green, the condo dark blue, `paul-stated
2026-09-04` — that **nothing reads**.

**The expectation is not in doubt, and it did not come from me.** Paul, walking production as a
stranger, asked for exactly this split unprompted `validated — P19`. So the question is not *which one
wins* but *what each one is for* — and once that is named, **they stop competing, because they paint
different surfaces**:

- **The profile colour answers *whose account is this*.** It belongs on the surfaces that are about the
  person and about no single place: the places list, both settings pages, the signed-in-as line.
- **The place colour answers *where am I*.** It belongs on everything inside a place — the masthead
  above all, because §3b already rules that the top bar's standing job is to answer that question, and
  colour answers it faster than a word does. `inferred`.

**→ The expectation, stated as one rule: inside a place, the place's colour wins, always. Outside a
place, the profile colour paints. The one seam is a place's card on the list — and the card should wear
its own place's colour, on a surface painted in the person's.** That is what makes a list of two
scannable, which is the payoff moment of act ⑤. `inferred`. ⚠️ Precedence is Paul's ruling to make;
this is the expectation, which is mine.

**Three consequences the build has to absorb, whichever way he rules:**

1. ⚠️ **`fw-accent` is ambiguous evidence about intent and must not be silently assigned to one side.**
   It was chosen at a moment when the person had exactly one place and could not tell which thing they
   were colouring — that is precisely what Paul objected to in P19. Reading it as a *profile* colour or
   as a *place* colour are both inventions. The honest move at the split is to ask once, cheaply, in
   place. `inferred`.
2. ⛔ **Place settings must open showing the colour the masthead is currently rendering.** Today the
   instance declares one colour and the page paints another; if settings opens on the declared value,
   the first thing the page does is contradict the screen it was opened from — on the surface whose
   entire job is to be trusted.
3. ⛔ **Do not build two colour pickers before the ruling.** 19c says this and it is right; two pickers
   shipped ahead of a rule is how one concept becomes two forever.

### The return-path requirement, restated as a reader problem

19c calls it a state requirement. For the reader it is simpler: **a settings page is not a place, so
"back" is not a direction — it is a memory.** One page, two parents, and the page must remember which
door it came through. `inferred`. The reader-visible falsifier: enter from the list and from a place;
each returns to where it came from; and if the person changed the place's name, **the parent they land
back on shows the new name immediately** — otherwise the edit reads as not having taken, which is the
one thing settings must never do.

---

## 4 · What each surface must NOT do

**The places list must not:**
- name itself — *Account*, *Dashboard*, *Hub*, *Portal*, *Home base*. §4 rules the shell is called
  nothing to a user, and every one of those names describes a management function over someone's home.
- count. No *"1 place"*, no *"2 of 2"*.
- show any place's **content** — a temperature, a *3 things need attention*, a last-updated stamp. That
  turns a shelf into a dashboard, re-imports the task-manager register the tone rule forbids, and
  cannot be honest offline. `inferred`, and it is the strongest single "must not" on this surface.
- sort itself by recency or alphabet (seam 3).
- use the verb **switch**. Switching is a mode; entering is a place.
- require the network to render.

**The estate page must not:**
- put the return control in the reading path. R1-B was chosen because it never puts anything between
  her and the weather card; the return control inherits that constraint exactly.
- let the top bar answer anything other than *where am I*.
- carry account-level settings.
- change what it renders because a second place exists.

**A settings page must not:**
- hard-code its exit.
- open as a form of empty controls. It opens as **the person's current answers**, editable in place —
  the receipts grammar `estate/index.html` already established, which is the grammar Mom's surfaces
  run on.
- re-ask anything already settled. The arrival page's own comment says it: there is no second confirm
  pair, because asking again thirty seconds later in a different vocabulary is a new question, not a
  confirmation.
- explain itself. P24: *explain nothing the next tap will show.*

### ⭐ Which acts must complete without ever opening a settings page

**All three creation acts: ① account, ③ first place, ⑤ second place.** Plus both transitions —
entering a place and leaving it. `inferred`, and it follows directly from the ask-vs-move split: a
settings page is the most asking-shaped surface in the product, and the measured record is that every
affordance which asks scored zero.

Acts ② and ④ **are** the settings pages; they are the only two that may require one.

**The falsifier, stated so it can be run:** unplug both settings pages entirely. A person can still make
an account, found a place, enter it, leave it, and found a second — and each of those ends in a usable
result, not a half-configured one. Two corollaries the build should hold itself to:
- **nothing founding needs may live only in settings** (if founding requires it, founding asks for it);
- **nothing settings offers may be a prerequisite for founding** (including the colour — a place
  founded without ever choosing a colour must render correctly).

And one thing settings **must** be able to do: repair any mistake made during founding. A mistake must
be fixable afterwards without ever having been able to block the act. `inferred` — this is the *everything
is changeable* rule applied to the one flow where the person has the least information.

---

## 5 · ⛔ What a synthetic seat cannot settle here

Read this before commissioning any walk against this journey. `.private/walk-answers/README.md` §3
already states the general case; this is the part specific to these five acts.

**Structurally unreachable — no number of seats, answers or runs closes these:**

1. **The whole subject.** Every seat holds one grant. *Having two places, and moving between them,* is
   outside every seat's experience by construction. GATE2 names this at P19: a model distinction like
   profile-colour-vs-place-colour *"requires holding two places at once; a seat holds one grant and
   cannot feel the collision."*
2. **Whether the return control is findable.** ⭐ GATE2 row 6 is the strongest evidence in the corpus
   and it is about exactly this shape of control: it existed, was correctly labelled, read perfectly in
   every text extraction, sat in the wrong place — *"and for the reader that is identical to not
   existing."* Paul's ruling is *small, quiet, near the top*, which is the exact profile of the thing
   that goes unfound. **No DOM-reading or source-reading seat can check this. It needs eyes on pixels
   with an expectation of where a control belongs.**
3. **Whether founding a second place feels safe.** The anxiety at ⑤ is entirely about the *first*
   place. A seat has no first place it cares about, so it cannot feel the thing the act is about.
4. **Whether the colour split is legible.** Needs two places rendering differently, on one screen,
   read by one person.
5. **Abandonment, at any of the five acts.** No seat can stop; compliance is the harness's control
   flow, not a behaviour a seat emits. So no battery can tell you where anyone gives up.
6. **Naming.** No seat can tell you whether *add a place* reads as founding or as filing, or whether
   an untitled list reads as clean or as broken.
7. **Whether a settings page holds what someone came for.** A seat has no grievance, so it has no
   reason to open settings and nothing it is looking for when it gets there.
8. **The class GATE2 names outright:** *"No synthetic seat has ever asked what the product should DO.
   They review what it does."* Acts ② ④ ⑤ are all mostly *should-do* questions.

**What a seat genuinely CAN settle here — worth commissioning, and worth scoping to exactly this:**
- the 19c return-path assertion — enter settings from both parents, assert each exit, mechanically;
- the list of one renders honestly at 414 × 848 A+ with a long place name and a curly apostrophe;
- a place founded with no colour chosen still renders;
- both settings pages unplugged, and all three creation acts still complete (the §4 falsifier).

**And the one thing to say plainly:** ⛔ **act ⑤ cannot be walked by anyone — synthetic or real —
until per-request scope lands**, because no credential can hold two places. Any pre-scope result about
act ⑤ is a result about a mock. The instrument this journey actually needs is a **gate 2.5**: one real
person who owns two places, watched, silently, once. **Bob is literally that person and is the only one
in the corpus** — and he is gate 4 in the cascade, behind a release gate whose isolation assertion is a
known fail by design. That tension is real and it is Paul's to resolve, not mine.

---

## 6 · Five questions worth asking, if a real conversation happens

Written to Mom Test rules — past behaviour, their life, not the idea. Two are for Mom (relayed by Paul
through the app or in person, never fetched), three for Bob at the follow-up.

**Mom** — 1. *"When you think about the condo and Fernwood, do they feel like two of the same thing, or
like the big one and a little one?"* (tests seam 2 and seam 3 without naming a design.)
2. *"Last time something in the app said the wrong thing about the place — what did you do?"* (tests
whether the repair motive exists at all before a settings page is built for it.)

**Bob** — 3. *"Walk me through what you did the last time you tried to write down how the houses work.
Where did that get to?"* (the prior attempt is unexamined and is the biggest gap on his side.)
4. *"When you picture your daughter opening this — what's the first screen you'd want her to hit?"*
(tests seams 1 and 2 from the direction he cares about.)
5. *"Which of the two houses would you set up second, and why that one?"* (his deferral is `validated`;
his reason is not.)

---

## Pain points

- `validated` — a control that exists, reads correctly, and sits in the wrong place is identical to one
  that does not exist (GATE2 row 6). This is the standing risk on the return control.
- `validated` — landing in a place that is not yours ends the relationship (P29).
- `validated` — a question that wraps reads as two questions (P17, named as a principle by Paul).
- `validated` — an ask with no live confirmation makes the person doubt they got it right (P14/P15,
  and lap 1 items 1/6/7).
- `validated` — asking her costs everything; moving her costs nothing. Every asking affordance scored
  0 offered→taken; the one moving affordance scored 5/5.
- `inferred` — a settings page that opens as controls rather than as answers forces a re-read.
- `assumption` — the anxiety at act ⑤ is about the first place, not the second.

## Opportunities

- `inferred` — the per-place colour is the cheapest thing in the product that makes a list of two
  legible at a glance, which is the payoff moment of the entire second-place act.
- `inferred` — place settings converts two live "tell Paul" links into real edits, keeping a promise
  P26 says must not survive to maturity.
- `validated` — an address alone should buy the person *something* (P32). The list of places is where
  a person will notice whether it did, because at two they can compare.
- `inferred` — building act ③ as a segment that can run without act ① costs nothing today and is the
  whole of what act ⑤ needs later.

## Evidence log

- `2026-09-06: [measured] — .private/synthetic-walks/*/2026-09-06T13*/REPORT.md — all seven runs carry WALK-REPORT-UNWRITTEN. No first-person synthetic account of the current build exists; none is cited here.`
- `2026-09-06: [source-read] — estate/index.html — "That's not right ›" and "Change the order ›" open a note box, not an edit (F12); fw-accent paints the masthead; the reconcile path treats the server as truth and stays silent offline; three distinct empty states.`
- `2026-09-06: [paul-stated — BACKLOG.md 19b/19c] — the shape (login → places list → tap in → quiet control back → + founds), settings on both parents, estate settings starts with name + colour, and every settings page returns to its origin.`
- `2026-09-06: [paul-ruled — VOCABULARY.md §3f] — application administrator vs estate owner; no profile outranks another inside the app; an estate owner cannot found a second estate today.`
- `2026-09-05: [validated — GATE2 lap 2, a real person] — P19: "Pick a profile colour", separate from the place colour, each place gets its own. The single strongest piece of evidence for §3.`
- `2026-09-05: [validated — GATE2 lap 2] — P29: named an Atlanta place, tapped "Open Grant Park Oasis", landed on Fernwood. P30/P31/P32: land somewhere recognisably yours, carrying initial data; an address alone should yield something.`
- `2026-09-05: [validated — GATE2 lap 1] — the reveal control existed, was correctly labelled, and was unfindable. A walk that reads a DOM cannot review a layout.`
- `2026-09-05: [validated — GATE2 lap 1 rulings] — production starts from nothing but a text; everything is changeable after account creation; an invited reader routes through account creation.`
- `2026-09-04: [paul-stated] — the condo's main colour is dark blue, Fernwood's is its green (instance/*.json identity.theme.main). Nothing reads them.`
- `2026-09-03: [paul-approved — BACKLOG §C7] — the condo paper model: she owns it, garden off. The no-garden case is the falsifier act ⑤ will meet first.`
- `2026-09-02: [design-options README] — R1-B "the room" and R1-SA "the masthead is the control"; frames 2 and 3 do not exist in code. R1-SA's absent-at-one-grant rule is superseded by founding, per the correction at the head of this file.`
- `2026-09-01 (lap 8 window): [measured] — jump strip 5 offered → 5 tapped; Perspective queue 10 → 0; ack ribbon 10 → 0; front-door launcher 10 → 0; look-for prompt 5 → 0. The ask-vs-move split behind §4's settings rule.`
- `2026-08-31: [validated (second-hand), via tate-commons] — Bob: two houses, a daughter each, each seeing only her own; excited the data would be his; converted by a populated phone; agreed to start with the mapped house. One conversation, recounted from memory, no recording.`
- `2026-08-24 / 2026-09-03: [measured] — her conditions are 414 × 848 at A+ (text_size_served lg in 8 of 8 reports over 60 days).`
- `2026-08-01: [contested → Paul-direct tier only] — persona-mom.md: depth-1 reading, low-attention posture, fear of getting it wrong, a simple memorable password is acceptable. The telemetry tier is invalidated and is not used here.`
