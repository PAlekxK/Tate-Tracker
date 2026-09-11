# The STARTING name — one recommendation, against tonight's two rulings

- row: `.plans/2026-09-03-product-name-PLAN.md` Q3
- stage: draft
- ready: agent-proposed 2026-09-11 — Paul rules

**Lens** content-steward · **Mode** draft (naming) · **Charters** `cross-project/voice-and-stance.md`
(could-be-anyone · credit-don't-thank · register-follows-audience) → `fernwood.md` (door-vs-room, §4a)
→ `VOCABULARY.md` §1 · §2 · §3b · §3f · §4 → `CLAUDE.md` § "Project purpose & tone".
**Audience** Paul (ruling) · Mom and every later founder (the only people who meet a rendered surface)
· a stranger who types the apex · the application administrator (a different reader, and that turns
out to be the hinge). **Register** plain and unceremonious — a door is opened, not announced.

> **GATE.** Nothing decided, no canon touched. No edit to `VOCABULARY.md`, `BACKLOG.md`,
> `onboarding/index.html`, any `*-PLAN.md`, or any built artifact. Everything here ends at Paul's gate.

---

## 0 · The finding that reframes the question, and it is measured, not argued

**The product already has a name, it is `My Home`, and it is rendered on shipped pages tonight.**

| site | string | class |
|---|---|---|
| `onboarding/index.html:7` | `<title>My Home</title>` | shipped |
| `onboarding/index.html:304` | `<h1 id="head">My Home</h1>` | shipped |
| `estate/index.html:7` | `<title>My Home</title>` | shipped |
| `estate/index.html:172` | `<h1 id="place">My Home</h1>` | shipped |
| `homes/index.html:270` | `h.name \|\| "My Home"` — a row's fallback name | shipped |
| `VOCABULARY.md` §3b, the top-bar row | *estate > person > **"My Home"**, the product itself* | `paul-stated 2026-09-05` |

And it has been **met on screen by a reading seat and by Paul's own walks**, in tracked files:

- `.ux-reviews/2026-09-10-founding-flow.md` row 1 (`/` → `/estate/`, *title "My Home"*), row 4
  (*"a complete 'My Home' almanac for nobody"* · *"My Home Almanac appears four times on one screen"*),
  row 7 (*"Header still 'My Home'"* mid-flow), F8, and — the one that matters most — § What genuinely
  works #1: **"The header becomes the place's name the moment you name it ('My Home' → 'Bramble
  Hill')… the product visibly taking what you told it."**
- `.content/2026-09-10-founding-flow-copy-REVIEW.md` #10, same observation from the copy side, and its
  flag on `onboarding:865` *"Called 'My Home' until you name it"* as a now-unreachable string.

⭐ **So Q3 is not an open naming question. It is a confirm-or-reverse.** Paul ruled it three times and
the build followed: Q3 *"we can just go with my home for now"* `[2026-09-03]`; the top-bar fallback
`[2026-09-05]`; *"My Home would be the name that they provide, and then add the address to the top
under My Home"* `[2026-09-05]`. Tonight's proposal would **reverse a name he ruled twelve days ago and
that is live in two `<title>`s and two `<h1>`s**, on two production deployments and QA.

⚠️ **And a control is green about the wrong question — the repo's own named failure shape**
(`CLAUDE.md` § *"A control can be entirely correct and still not cover the thing you rely on it for"*).
The plan's **F5** tripwire greps `engine/viewer.template.html` + the apex page for `\bMy\b` and read
**0** on 09-03. Measured tonight: still 0 in the template's rendered chrome (its four `My Home` hits
are all `//` comments) — **and the string renders four times on two shipped pages F5 never looks at.**
F5 is honest about the template and is being relied on for the product. Re-spec is in §4.

---

## 1 · The proposal, read for what it is reaching for

> *"can we just start by calling it either a state manager or my home place estate manager"*
> `[paul-stated 2026-09-11, voice-dictated — a proposal, not a ruling]`

Two things are in that sentence and they are not the same thing.

1. ⭐ **"can we just START BY calling it"** — the ask is to **stop the name being open** so lap 8 · B
   can move. That is legitimate and it is answerable tonight: the answer is *it already is, and here
   is the string*.
2. ⭐ **"estate manager"** — a **descriptor**, not a name. It answers *what is this thing*, not *what
   is it called*. Every word of it is functional: the reader is told what job the software performs.

**The diagnosis: what is missing is not a name, it is a sentence.** `myhome.place` says what it is
called and nothing about what it does, so when Paul says it aloud he reaches for a descriptor to
finish the sentence — and the only descriptor in the record is the one §4 rejected. That is a copy
gap with a copy fix (§3, the apex line), not a naming gap.

---

## 2 · The collision, reasoned through

### 2a · Does §4's "estate manager" rejection yield? **No — and it does not have to, because the
proposal has a legitimate home and it is not the one he named.**

§4's row is two rules stacked:

> *"Manager" is the task-board vocabulary the tone rule forbids.* ⭐ *And the durable reason, which
> kills the synonyms too: a name that describes a management function over someone's home names the
> reader as an operator of their own life.* `[paul-ratified 2026-09-02]`

- **The first half is `CLAUDE.md`'s founding tone rule wearing a different hat** — *"a field journal,
  not a task manager… Tone is everything here."* It is the oldest ratified sentence in the project and
  it is not a style preference; it is the reason Mom opens the thing.
- ⭐ **The second half is the one that decides tonight, and it is audience-scoped, not universal.** It
  names a harm to **the person whose home is being managed**. It says nothing about a reader who is
  managing a *service* — because that reader genuinely is an operator, of a system, not of their own
  life. **Applying the rule past its own reason would be citing it past its reason**, which this seat
  has already been corrected for once (`2026-09-03-product-door-naming.md` §2c).

**And §3f has already made exactly that split, in Paul's own words** `[paul-ruled 2026-09-06]`:
*"There needs to be an overall application administrator, and that's **the estate manager master loop**
and overall back end everything. And then there's a per-estate administrator in the app."*

⭐ **So "Estate Manager" is already this project's word for the back end, ruled by Paul, and §4 never
touched it.** §4 governs what a household member reads. The two rulings have never been in conflict;
the proposal put them in one sentence for the first time.

### 2b · What each option costs, and what it costs the reader the rule was written for

| option | verdict |
|---|---|
| **(c) his proposal as given — *Estate Manager* / *My Home Place Estate Manager* as THE product name** | ⛔ **Refuse, and say why plainly.** *My Home Place Estate Manager* is 6 words / 9 syllables and **fails the one criterion the record has validated** — *sayable, not typeable* (`2026-09-03-product-door-naming.md` §2b.1). It also puts **my**, **place**, **estate** and **manager** in one string: it breaks §1 (`estate` never reaches a user-facing surface) on the surface most people meet, and it re-asserts the possessive-plus-system-noun construction the greeting note identified as **the portal shape**. Bare *Estate Manager* fails §4 head-on and is **already taken by §3f for a different referent** — two things called *Estate Manager* in one repo is §5's live defect (`group`) minted a second time, deliberately, in the week production becomes one origin. |
| **(a) the address as the name — *My Home* / `myhome.place`** | ✅ **Recommended.** Shipped, ruled three times, spoken already, and §4-clean by construction: *home* names **a place**, not a function over a life — which is the greeting note's §c argument, and it is the reason his own apex ruling holds at all. |
| **(b) *Estate Manager* as the ADMINISTRATOR's surface only** | ✅ **Recommended alongside (a).** Adopt it — it is §3f's own phrase, it never reaches a household member, and it gives him the plain descriptive handle he asked for, in the one place where it is true. |
| **(d) a distinct word** | ⛔ **Not now.** *Porchlight* is registered (RDAP 2026-08-10) and a fresh candidate round would re-open a decision three rulings have closed, in the week it blocks Mom's migration. It also turns on `PRODUCT-ENGINE` **Q6** — branded product, or a thing Paul builds for people he knows — which is still open and is his. **A starting name must not require Q6 to be answered first.** |

### 2c · The one rule I would sharpen rather than let stand loose

`My Home` is doing **two jobs on shipped screens** — the product's name (tab, top-bar fallback) and the
placeholder for a place nobody has named yet (`read(K_NAME) || "My Home"`, `onboarding:1469`).

⚠️ **That double-booking is deliberate and it is Paul's** — *"'your place' is the initial starter
filler; it should say like 'my own place'… let's make the bridge very clear, up until they customize
it"* `[paul-stated 2026-09-05]`. **Do not undo it.** It is what makes §4a's door-vs-room rule hold
without any extra machinery: the door's name is visible **only while there is no room to compete
with**, and it disappears the instant the reader supplies a word. That is the best thing in the
founding flow by two independent seats' reading.

⭐ **The rule that keeps it honest, and it is one line:**

> **`My Home` renders only where the reader has not yet named their place. Their word always wins, and
> the two never appear on the same screen.**

Falsifier: `My Home` and a place's own name rendered together. That is F1 (*the door competes with the
room*) arriving as a layout, and it is grep-able.

---

## 3 · The verbatim strings, per surface

| surface | string | note |
|---|---|---|
| **Apex `<title>` / browser tab** (`myhome.place`) | `My Home` | ⭐ **Changed from my 09-03 recommendation** (`myhome.place`, the host). Two shipped pages already title `My Home`; an apex that titles itself differently from its own children teaches two names in one bookmark bar. *Alternate: `myhome.place` — keeps bookmark and spoken line identical; I now weight sibling consistency higher.* |
| **Apex `<h1>`** | `My Home` | A stranger who typed the address is owed the address said back in words. |
| **Apex body — the descriptor, and this is the part his proposal was actually asking for** | `A private record of the places a family looks after — one household at a time.` <br> `Built by Paul Kirschenbauer. Nothing to sign up for; the doors here are opened by hand.` <br> `Reach Paul ›` | Carried from `.content-reviews/2026-09-03-myhome-place-greeting.md` § a, re-broken into two lines so the descriptor stands alone. ⛔ **No wordmark beyond the `<h1>`; no "estate", no "manager", no "platform".** |
| **The sign-in door — heading** | `My Home` | The apex IS the door `[paul-ruled 2026-09-11]`. Matches `estate/index.html:172` today. |
| **The sign-in door — the line under it** | `Sign in — everything you look after is behind this door.` | ⭐ **Deliberately number-free.** §3b's *your homes* is plural-only and the door cannot know the grant count before sign-in; *look after* is the apex's own verb, so door and page say one thing. |
| **Said aloud** | `my home dot place` | Unchanged. Four syllables, ordinary words, zero spelling, self-identical to the address — and it is already how Paul says it. |
| **In-app top bar, product-level fallback** | `My Home` | Unchanged — `VOCABULARY.md` §3b, `paul-stated 2026-09-05`. |
| **A place's header once named** | her word, verbatim | `Bramble Hill`, `Fernwood`. Nothing appended, nothing case-corrected. |
| **The administrator's back end** | `Estate Manager` | ⭐ **His proposal, adopted where it is already true.** §3f's *"the estate manager master loop"*, shortened to the surface's name. In prose: `the Estate Manager — the application administrator's back end, across estates`. ⛔ Never rendered to a household member; never in a model prompt; never in `RELEASE_NOTES.md`. |
| ⛔ **Never** | `My Home Place Estate Manager` · `Estate Manager` as the product's name · *my account / my settings / my dashboard* anywhere | §2b. The last group is the greeting note's § c tripwire and is unchanged. |

**One string Paul will need in his own mouth, since the descriptor is the real gap** (operator
register, `paul-operator.md`):

> *"It's myhome.place — a private record of the places you look after. I'll open your door and send
> you the link."*

⭐ That sentence is what *"estate manager"* was reaching for, and it does the job without naming
anybody the operator of their own home.

---

## 4 · What this asks of the checks (flagged, not done — this seat writes no code)

1. **F5 is re-specified to the shipped pages, not the template.** Today it greps
   `engine/viewer.template.html` + the apex and reads 0, while `My Home` renders four times on
   `onboarding/index.html` and `estate/index.html`. New form: *`\bMy\b` outside the four sanctioned
   fallback sites, over all five shipped pages plus the template.* Without this, F5 stays green and
   the next `My settings` lands unseen.
2. **The §2c rule gets a check of its own:** `My Home` and a non-empty place name rendered on one
   screen. That is the only mechanical read of *the door competing with the room*.
3. **`VOCABULARY.md` §3b gains the name row and §4 gains the rejected shape** — plan step 6, three
   lines, ⛔ **Paul's or the main session's to write, not this seat's**, and the cite-never-restate
   rule (§6) binds the wording.

---

## 5 · Falsifier — what would show the STARTING name is wrong

| # | observation | how it is read |
|---|---|---|
| **S1** | ⭐ **Paul appends a descriptor every time he says it** — *"myhome.place, the estate-manager thing"* | ⛔ **The sharpest one, because it separates the two failures.** It would mean the NAME is fine and the SENTENCE is missing, and the remedy is §3's apex line, **not** a new name. If it persists after the apex ships with the descriptor, then the name genuinely under-says and (d) re-opens. |
| **S2** | Someone he onboards asks **how to sign up / get an account**, or says the name back as a question | `my` was read as a portal — the greeting note's § b.1, unchanged and still the only failure that costs anything. |
| **S3** | `My Home` appears on a screen beside a place's own name | §2c's rule broken; the door is competing with the room (plan F1). Grep-able. |
| **S4** | A founder names their place **`My Home`** | The placeholder taught them the answer. It would mean the bridge became an instruction, and the fallback needs to stop being a word a person could plausibly type. |
| **S5** | `Estate Manager` appears on any household-facing surface, prompt or release note | The §2a split failed in the direction §4 was written to prevent. |
| **S6** | ⚠️ *Nobody ever says the name* | ⛔ **Not a falsifier of this recommendation** — it is the plan's **F3**, which belongs to the 09-02 *call it nothing* position and has still never fired. Recorded so it is not double-counted. |

**Planned revisit — the name is a starting name and this is when it is re-read:** at whichever comes
first — (i) `PRODUCT-ENGINE` **Q6** is ruled (branded product vs. a thing he builds for people he
know), or (ii) the first household outside the family founds a place. Both change the weight on §4a's
door-vs-room reasoning; neither is due this lap. ⭐ **Cost of being wrong is unchanged and low**: the
plan's own ladder puts the name on the reversible rung — the irreversible half was spent when
`myhome.place` was registered, and tonight's apex ruling spent the rest of it.

---

## 6 · What I did not decide

1. **Whether this is a branded product** — `PRODUCT-ENGINE` Q6, his, and the recommendation is
   deliberately stable under either answer.
2. **Mom's home-screen icon** — *Fernwood Tracker*, her word, in no tracked file. Untouched.
3. **`README.md:1`** — still `# Church Mountain Property Tracker`, a third live product name, wrong
   today independent of any ruling. My 09-03 recommendation (`Fernwood`) stands; plan step 8.
4. **Whether the apex `<title>` is `My Home` or `myhome.place`** — I recommend the first and named the
   alternate; it is one line either way.
