# First open — the door, and the unplaced household

> ⛔ **AUTHORED CONTENT UNDER THE AI BOUNDARY. DRAFTED FOR PAUL'S READ — not shipped.**
> Every line below reaches a person. Nothing here goes to a household until Paul has read it.
> The three rulings in §4 are his; nothing in §2 or §3 should ship ahead of ruling (a), which
> flips the person of every sentence.

| | |
|---|---|
| **Audience** | A person who has just finished onboarding. They gave a place name, an address, a ranking and a contact preference, and **no facts about the place**. They are one tap from the estate page ("Early days"). |
| **Surfaces** | `estate/index.html` — the door out of the handoff page. `engine/viewer.template.html` — the masthead and three regional card faces on first load. |
| **Reader conditions** | **414 × 848 × A+**, phone. Every line below was written to that width. |
| **Charter applied** | `~/.claude/content-principles/fernwood.md` (field journal not task manager · describe don't grade · anchored naming beats voice-fluent naming · acknowledge the shared work) + `cross-project/voice-and-stance.md` (could-be-anyone · describe don't grade · credit don't thank) + `VOCABULARY.md` §4. |
| **Tone register** | **Orienting**, same as the empty-card brief. Not celebratory, not instructional. Two of the four seats used the word *broken*; the whole job of this copy is that the reader reads *new* instead. |
| **Builds on** | `.content/2026-09-06-empty-card-copy.md` — the three-line shape, Ask-A/Ask-B, the degradation rule. Not restated. |
| **Evidence** | Four synthetic seats (`mom` · `strict` · `wide-eyed` · `owner`), 2026-09-06, `assumption`-tagged, converged. Not real-reader evidence. |

⚠️ **Person.** Everything below is written in **we**, matching the app, so that ruling (a) has one
consistent draft to rule on. **If Paul rules "I" — which is my recommendation — every sentence in
§2 and §3 flips**, and the flip is mechanical: *we → I*, *us → me*, *our → my*. Nothing else moves.

---

## 1 · The door

### The word "almanac" is wrong here, on three counts

1. **It is a genre promise the household has not earned.** `VOCABULARY.md` §4 rejects *Almanac* as a
   portable noun — cyclical, seasonal, earned at Fernwood by 178 month-keyed season notes. On day one
   at a condo it is false, and it is the first word through the door.
2. **In the app it names ONE CARD, not the app.** The jump-strip tile reads `{name} Almanac` — the
   journal card, one of twelve. A door labelled *"Open the almanac"* points the whole product at one
   of its own cards. `wide-eyed` hunted screens 07–11 for "where the almanac is" and gave up;
   `strict` and `mom` reached the app only by typed URL.
3. **The definite article points at something they have never seen.** *"The"* almanac assumes a prior
   introduction that has not happened. This is the reader's first sight of the word.

### Recommended

```
Open your place ›
```
with a one-line lede directly under it:

> **Ranked something:** There's a card in here for each thing you ranked — all of them empty so far.
>
> **Ranked nothing:** The cards are all in here, empty so far.

**Why this label.** It survives every name shape the seats produced — *the condo* · *Home* ·
*Hollow Creek Road* · *The Old Miller's Place on the Bend* — at 414 × A+, where
`Open The Old Miller's Place on the Bend ›` wraps to three lines in a button. It does not collide
with the handoff button that already reads `Open {place}` and lands on **this** page — two doors
with one label, going to two different places, is exactly the carelessness that teaches a reader not
to trust the surface. And it sidesteps the `owner` seat's finding that `Open Hollow Creek Road` reads
as a map instruction rather than a door, *"like a map instruction rather than a door into my own
thing"* — a real cost for anyone who names their place after the road, which is most people up there.

**Why a lede, and why that lede.** The reason stop 12 read as broken was not emptiness — `owner` was
explicit: *"the emptiness is not the problem"* — it was that screen 07 and screen 12 described two
different products. The door is the cheapest possible place to close that gap, and it costs one line.
The lede is anchored in the one thing we actually know about them (their ranking), makes no date and
no feature promise, and tells them exactly what they are about to see.

**The could-be-anyone read, stated honestly.** *"Open your place"* fails the test on its own — a
stranger could have written it. That is the same trade the B variants take in the empty-card brief:
**at day one the honest response to knowing nothing is not to fake an anchor.** The anchor sits in
the lede, where it is true, and in the h1 above it, which is already their word.

### The alternative, if Paul wants the name on the button

```
Open {place} ›
```
Takes the anchor into the label and reads warmly for most names. It costs two things and both are
real: the handoff button on the confirm screen **must** be re-labelled off `Open {place}` in the same
change (I'd use `See what you told me ›`), and the button must be allowed to wrap to two lines at A+.
If Paul takes this one, `{place}` on the button and `{place}` in the h1 one screen apart is a
recognition win, not a repetition — different screens, one tap.

### ⚠️ For ux-expert, not copy
The door is `class="ubtn tap44"` — the same component as `‹ Your homes` and `Settings` in the utility
row above it. The one control on the page that leaves the page is dressed as a utility link. No copy
fixes that.

---

## 2 · The unplaced household

**State:** we have the address; we have **not** put it on the map. No coordinates, so no weather, no
sky, no ground. Two shapes of address, and they need different second lines.

- **`street`** — a locatable address we simply have not geocoded yet.
- **`box`** — a PO Box. Detected on the estate page already (`estate/index.html`, the `boxy` regex).
  The estate page's line for this reader is the best sentence in the flow, per two seats. **Reuse its
  words rather than writing new ones** — same author, one screen apart, recognisable.

### ⭐ One ask for the whole unplaced condition, and it sits on the place card

The empty-card brief's rule — *the ask appears where there is something to confirm or something to
add, and nowhere else* — extends cleanly here. **Weather and Sky have nothing of the reader's on
them to confirm.** The address is on the place card. So the place card carries the ask for all three,
and Weather and Sky are two lines and quiet.

⛔ **And the ask on the place card must not ship until there is somewhere in the app to fix an
address.** `mom` looked for the `‹ Your homes` link on stop 12 and it was not there; there is no
route from the app back to place settings. An ask whose answer has nowhere to go is
affordance-without-signal, and on this product it is worse than that — it is the one class of thing
her surfaces are built to never do. **Flagged to ux-expert; the copy is drafted and held.**

### Weather

| slot | copy |
|---|---|
| line 1 (both) | `Nothing here yet. This is where the weather at your place will live — what it's doing now, what the week looks like, and what the rain has been doing.` |
| line 2 · `street` | `We have your address; we haven't put it on the map yet, so there's no weather to show you here.` |
| line 2 · `box` | `A box number tells us where your post goes, not where your place is — so the weather is the part we can't work out yet.` |
| ask | *(none — see above)* |

### Sky & Stars

| slot | copy |
|---|---|
| line 1 (both) | `Nothing here yet. This is where the sky over your place will live — the moon, what's up tonight, how dark it gets.` |
| line 2 · `street` | `We have your address; we haven't put it on the map yet, and what's overhead depends on exactly where "here" is.` |
| line 2 · `box` | `A box number tells us where your post goes, not where your place is — so we can't say yet what's overhead at yours.` |
| ask | *(none — see above)* |

### The place card *(titled `{place}`)*

Supersedes the place-card copy in the empty-card brief for the unplaced state; the placed-state copy
there is unchanged.

**`street`**
> So far this holds just what you told us — {place}, at {line1}, {city}.
> The ground, the weather and the seasons here all get built out from that, once we've put it on the map.
> *Have we got this right — and is there more we should know?*  ⟵ held, see the ⛔ above

**`box`**
> So far this holds just what you told us — {place}, at {line1}, {city}.
> A box number tells us where your post goes, not where your place is — so the ground, the weather and the seasons are the parts we can't work out yet.
> *Have we got this right — and is there more we should know?*  ⟵ held, see the ⛔ above

⚠️ `{line1}, {city}` renders **exactly as typed**, or the whole clause is removed. `strict` noticed
`ga` silently uppercased to `GA` two screens after being promised *"nothing here gets tidied up"* —
a small correction that costs the promise. If there is no city, the clause is `{place}, at {line1}`.
No comma with nothing before it, ever.

### The masthead

Today: `{taglinePrefix} {address}` — *"An almanac for"* — over an address line that printed
`, · 0 ft`. The build now renders each whole or not at all, which fixes the fragment. What it does
not yet fix is **what a brand-new household's masthead should say**.

**Recommended subtitle for any household with nothing built yet:**

```
Early days
```

Two words. It is the estate page's own state word, in the same position on the page, one tap later —
so the first thing the reader sees in the app is the sentence they just read outside it. `mom`'s
verdict on the seam was *"if I'd only ever seen 12, I would think I'd been given someone else's
app"*; this is the cheapest available answer to that, it fits at 414 × A+ with room, it makes no
promise, and it names no genre.

**Alternative, if two words reads as a label rather than a state:**
`Early days — everything here gets built from what you tell me.` Longer, echoes the estate banner
verbatim, and wraps to two lines at A+. I prefer the short one; the banner's sentence is doing that
job one screen back and does not need to be said twice in four seconds.

**Address line, same masthead:** the address exactly as typed, or nothing. ⛔ **Never `0 ft`.** A
zero is a claim — `owner` read it as *"wrong by nearly two thousand feet"* and `strict` as *"an
elevation asserted as zero"*. Elevation appears once the place is on the map and not before.

**Decay:** the subtitle goes when the household's own genre noun exists — which is the
each-household-names-its-own ruling, out of scope tonight and flagged in the empty-card brief. It
decays on **state**, never on visit count.

---

## 3 · Ranked-but-unbuilt — the copy, if Paul rules (f) my way

Ready to ship behind that ruling. `soon: true` modules only (Papers and documents · Marking spots ·
A map you draw yourself · Asking questions · Handing it all over).

> **Papers and documents** · an idea, not built yet
> Nothing here yet, and nothing to put here yet either — this one is still an idea.
> You put Papers and documents second, so it's near the front of the list.

- Rank-1 form of line 3: `You put Papers and documents first, so it's the front of the list.`
- Rank-4+ form: `You put Papers and documents on the list, so we know it belongs here.`
- ⛔ **No `Open ▾` control.** A disclosure onto nothing is the affordance trap, and `owner` counted
  it: *"Every card offers Open ▼ onto a dash."*
- ⛔ **No ask.** Nothing to confirm, and nowhere for an answer to go. The journal card's B-variant
  ask (*"what would you want this place to keep track of?"*) already catches the unanticipated need
  and is the right home for it.
- The tag is the ranking screen's own words — **`an idea, not built yet`** — carried through
  unchanged. The estate page already carries it; this is the third screen in the chain and it must
  not be the one that drops it.

---

## 4 · Rulings for Paul

Each is a choice with a recommendation. None is shipped.

### a · Voice person at the seam — **I** or **we**

The ranking screen and the estate page speak as **I** (*"how I decide what to build next"*, *"that
part's my job"*, *"I can't set up a second home for you yet"*); the app speaks as **we**. One reader
crosses that seam in one tap, and `strict` tried to settle who was talking and could not: *"I re-read
to settle whether 'I' is Paul or the app. I never settled it."* **Recommendation: I, everywhere the
builder is the one speaking** — setup, empty cards, invitations, apologies, anything about what will
be built — because the strongest lines in this product are already **I**, and *a builder's promise in
the plural is nobody's promise*. Reserve **we/our** for its one other legitimate job, which the
charter already defines: shared stewardship of a place that has a shared record (*"the laurel we've
learned to leave alone"*) — and a brand-new household has no such record yet, so its whole app is
**I** until it does. The cost is real and I'd rather name it: this flips every line in §2 and §3 and
in the empty-card brief, and it flips Fernwood's own long-standing app copy the day Paul wants
consistency across households.

### b · Ask placement — ranked modules + the place card, or every empty card

**Recommendation: ranked modules + the place card only; unranked modules stay two lines and quiet.**
Ask-B (*"Is there anything like this at your place?"*) is a genuinely good question and it is the one
the condo case has been waiting for — but a first screen carrying five or six questions is a form,
and this product's one measured reader is **0-for-35 on affordances that ask** while being 5-for-5 on
the one that simply moves her. Asks are the cheapest thing in this product to overspend and the
hardest to get answered. Ranked modules are, by definition, the things the person said they cared
about, which is where an answer is likeliest; and the unanticipated-need door is already open on the
journal card's B variant. If Paul wants Ask-B kept for the condo case, the cap I'd accept is
*ranked + place card + the single first unranked module* — but I'd rather ship the clean rule and
measure it.

### c · "Gardening" versus "Plants" / "The Field" / "Weeds"

Three seats independently hit this: `wide-eyed` — *"it is called Gardening in the strip and Plants in
the stack, two names for the thing I ranked first"*; `owner` — *"there are three cards where it should
be and none of them is called what I was asked about."* **Recommendation: the word they ranked wins
on every surface, and for a brand-new household the Gardening module renders as ONE card named
`Gardening`.** *The Field* and *Weeds* are Fernwood's shape — the split earned by 17 plants, a mown
field and a weed roster — not the engine's, and a household with nothing planted is shown three empty
cards for a thing it named once. Split into Plants / The Field / Weeds when a household's own record
justifies a split, exactly as `fernwood.md`'s anchored-naming principle requires: name the *thing* the
card holds, and at day one there is one thing. Structure is ux-expert's call; the copy ruling is that
**a person must never see two names on one screen for the thing they were asked to rank.**

### d · "Add a home", and plural "Your homes" for a one-home person

A button whose only function is to apologise should not be on the screen — but the panel behind it
*does* collect something, so the fix is to label the button for what it actually does rather than to
remove it. **Recommendation: re-label it to what happens** (`Somewhere else you'd add? ›`), open it
straight to the textbox, and **add the line that every other input in the flow carries and this one
does not** — `strict` refused to type in it for exactly that reason: *"Every other input in this flow
carried a line about who reads it. This one carries none. I would not type in it."* That is the
standing *use · not-use · who sees it · reversibility* rule, and this box is the one place in the
product that breaks it. On the plural: **a one-grant account's shelf should be headed with the
place's own name, not `Your homes`** — `VOCABULARY.md` already flags the greeting as provisional and
plural-only, and the top-bar rule there is *most specific wins*. One home, one name.

### e · The confirm screen — four same-weight buttons, and a completion claim over an open question

`mom` re-read the bottom half of that screen twice and never resolved which button finishes:
*"'Yes, that's it' / 'Save these' / 'Open the condo' are all the same dark shape."* And *"That's the
setup done"* is printed above the Open button while *"Does that look right?"* is still unanswered —
the surface is announcing an outcome for a question it has not been given an answer to. **This one is
already settled by doctrine and only needs enacting.** Standing rule 1 (2026-07-29) gives exactly one
affirmative grammar: filled + ✓ for the affirmative, outlined neutral for everything else. So:
`Yes, that's it` is the only filled control; `Not quite` and `Save these` go outlined; **`Open {place}`
does not belong on this screen at all** while a question is open — the reader lands on the estate
page anyway, and that page is where the door belongs. And **`That's the setup done` moves to the
estate page**, where it is true. A screen may not congratulate a reader for finishing something it is
still asking them about.

### f · Ranked-but-unbuilt items — does the app carry the "an idea, not built yet" tag

**Recommendation: yes — as a card, in ranked position, carrying the tag verbatim.** Copy is drafted
in §3. `strict` ranked *Papers and documents* **first** and it appears nowhere in the app;
`mom` ranked it second and searched the full screen for it. The estate page's own code comment
already states the governing rule for this exact material — *"silently dropping part of what someone
told us, on the screen whose entire job is showing that we heard them, is the worst place in the
product to do it. Every pick shows."* The app is the next screen in that chain and it is currently
the one that drops it. The honesty tag is what makes ranking an unbuilt idea safe to ask for in the
first place; carrying the ranking without the tag would be worse than carrying neither.

---

## Open questions

- **Is there a route in the app to fix an address?** Gates the place card's ask (§2). If no, the ask
  is held and the reader's only door is the estate page, one tap back — which they cannot reach,
  because there is no link back. ux-expert.
- **The household's own genre noun** — what replaces *Almanac* in the masthead subtitle and on the
  journal card once a household has a record. Flagged in the empty-card brief, still open, still out
  of scope.
- **Does the door's lede survive when the person ranked nothing?** Drafted (§1), unverified against
  the real render.
- **Ruling (a) reaches further than this file.** If Paul rules **I**, Fernwood's own shipped app copy
  is in **we** today and would need a pass. That is a separate piece of work and should not be
  bundled into tonight's.
