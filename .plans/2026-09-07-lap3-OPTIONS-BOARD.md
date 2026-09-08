# WHAT WE COULD DO NEXT — lap 3's options, in plain words

- row: process · kind: queue · class: engine · declared · objective: O5
- seats: user-researcher · practice-steward · product-steward (layout). ⛔ **engineering-partner has
  NOT run this lap** — see "What this list is missing" at the bottom. Not waived; owed.
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ **Nothing here is ranked and nothing here starts.** Grouped by *what's stopping it*.
- stage-note: 2026-09-07 — rewritten in plain language at Paul's request. The first version used the
  loop's internal shorthand and he could not read it, which meant it failed at the one job it had.
  ⭐ **A decision surface the decider cannot read is not a decision surface.**

---

## Where things stand right now

**Production is stable and untouched.** It serves the build you cleared (`1e2748d`). Nothing has
shipped to it tonight, on purpose.

**Mom has the link.** It was texted, it has not been used, and she can open it at any moment.

**One thing changed tonight that you should know:** production now **refuses** to deploy anything
except the build you've cleared. That's new and deliberate. To release something, you clear it first.

---

## 1 · WAITING ON YOU — building can't unstick these

### 1a. Move your review from production to QA — **you said go**
Rename the environments so they mean what they say, finish making QA a real copy of production, and
keep the new post-deploy check.
- **Changes for a person:** nothing.
- **Cost:** touches 9 files. ⚠️ *You asked about the "no drift control" worry — that's fixable and
  I'm doing it as part of this.* It means: today, nothing checks whether the release loop's
  instructions still match the release loop's code. Two such checkers exist but both only look at
  Mom's cycle, not this one.

### 1b. Cloudflare Access on QA — keep it or drop it? **You asked for a full recommendation.**
QA currently sits behind a login wall; production doesn't. That's the single biggest way QA *isn't*
a copy of production. Recommendation coming separately, in the context of the whole stack.

### 1c. Synthetic testers and your household — **you ruled: no**
They may not touch your real household. You're open to them **cloning** it and walking the copy.
That's now written down; building the clone is a separate question nobody has costed.

### 1d. Naming the Almanac — **you reframed this into a real feature (see 3a)**
~~Was: "Mom said Journal, the build says Almanac."~~ **Withdrawn — that was my error.** You ruled the
rename yourself on 2026-07-30 as a deliberate consolidation. Your reframing replaces it.

---

## 2 · I CAN DO THESE NOW — and none of them changes anything anyone sees

⭐ **This is the group your "let's do things without her where we can" points at.** No Mom, no you,
no deploy to her.

### 2a. Learn whether someone opened the invite and gave up
Right now, if Mom opens her link and can't get in, **we would never know.** She doesn't complain —
she stops. There's a record of arrivals sitting on the server and **nothing reads it**.
- **Why it matters:** the research seat called this the most serious risk to the customer — her first
  screen showing someone else's name over an empty place. It called it *"irreversible and invisible
  at once."* Since there's no visit any more, this is the only way we'd ever find out.
- **Cost:** small. The route already exists; nothing calls it.
- **First version:** how many arrived, per day, and which ones never became an account.
  **Leaves for later:** tying a specific arrival to the account it later became.

### 2b. Make the onboarding measurements readable at all
The app records what people do during setup. **There is no way to read it back** — it can be written
and never fetched. Every setup signal from both laps is currently invisible.
- **Cost:** small — a read route, mirroring one that already exists for feedback.
- **First version:** read it back over a date range. **Leaves for later:** any analysis on top.

### 2c. When we don't know who wrote something, record *why* we don't know
Today a record either names its author or is blank — and blank means three different things at once:
nobody was signed in · we couldn't verify them · this path predates the feature.
- **Why it matters:** you asked for this directly — *"be sure that for everything we know who wrote
  it."*
- **Leaves for later:** ⛔ **older records stay blank forever.** Guessing an author after the fact is
  exactly the mistake this prevents.

### 2d. Build QA the same way we build production
QA and production are built by **different halves of the same script**. That is *why* a real
production bug was invisible in the environment meant to mirror it.
- **Cost:** about one line, but it changes what QA serves, so it needs care.

### 2e. File the 20 decisions that nothing has acted on
Twenty things you've ruled are recorded in the log and **carried into no working list**.
- **Cost:** one pass through them.

### 2f. Let a test walk the app as someone who already has an account
Every test we run pretends to be a brand-new person. **Nobody has ever tested "come back tomorrow."**
That's the exact situation the worst current bug lives in.
- **Cost:** a real build. Blocks 4a below.

---

## 3 · CHANGES SOMETHING PEOPLE SEE

### 3a. Let each household name its own Almanac — **your idea tonight**
> *"Everyone may have a different take on what makes sense or feels the most natural. So that would
> be a way of systematically replacing the name in the displays, but keeping that module still have
> an internal name that's consistent."*

⭐ **This settles an old argument instead of re-fighting it.** The 2026-07-30 consolidation was right
because scattered names confused her — that's about the name *the code uses*. Her answer "Journal" was
right because it was her word — that's about the name *on screen*. They only ever collided because one
string did both jobs.

⭐ **And it's the right shape for many households:** with more than one home, "the most natural name"
isn't one answer, so a fixed name is wrong no matter which word wins. It also turns your open question
— *does "Almanac" land for her?* — into something she can just change herself, which is what you asked
for: have her do it in the app.
- **First version:** the Almanac only, one name, set in settings.
  **Leaves for later:** every other module's name, and whether the name belongs to the place or the person.

---

## 4 · CAN'T START YET — something else has to land first

### 4a. The front-door problem — the biggest single thing on this list
Getting in, staying in, and the app knowing it's you. **Fifteen separate items collapse into this
one.** In one sentence: an account's *facts* and its *credential* are two different records, and the
one path that reconciles them has no door.
- ⛔ **Blocked by 2f.** Not for lack of will: the bug only happens to someone who already exists, and
  no test can currently be that person — so we can't prove a fix worked.

### 4b. Ship the bug fix I made tonight
Production was serving placeholder files for four things the app reads, and answering "success" while
doing it. Fixed and committed, **not deployed** — it's waiting behind the new rule that production
only takes builds you've cleared.

### 4c. A build with two known bugs fixed has never been tested
It's sitting on the main branch, unwalked.

---

## 5 · DESIGN ONLY — ships nothing, and that's the point

### 5a. Zones — **you ruled: not being implemented**
Concept and design work only, running in its own session. It has reached the design stage with a
journey written.
⭐ **This is the deliberate test of whether we can move something forward and ship nothing without
that reading as a wasted lap.**

### 5b. What actually fills a place card
Your finding: the card should be about the **property** — local events, festivals — not the weather.

---

## 6 · NOT ON THIS LIST, AND WHY

| | |
|---|---|
| **"Can a real person get in the door?"** | Not blocked — **we just can't watch any more.** 2a and 2b replace it |
| **"Is 'add a place' founding or switching?"** | ⚠️ **Probably already spent.** Only answerable before she'd seen the app, and she has the link |
| **"Does she know where her writing went?"** | Only if it comes up naturally |
| **Bob's two houses** | Nobody has asked him anything. Every claim is a guess |
| **Thanking Mom for the 23 zones** | ✅ Closed — you do it as a person, whenever |
| **The colour question** | ✅ You ruled it 2026-09-06. I re-raised it in error |

---

## ⚠️ What this list is missing

**No engineering view.** The engineering seat hasn't run this lap, so **nothing here reflects what a
builder would call urgent** — and your own rule is that a critical build problem gets raised
unprompted. A whole perspective is silent. That's a hole in this list, not evidence there's nothing in it.

**Nearly all the evidence is yours.** You're one person, and the builder. The person this has to work
for has **never used it**.

**Sorting by "asked most often" would be wrong.** How many times something's been raised measures how
long it's been stuck, not how much anyone needs it.
