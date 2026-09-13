# A11 · THE SINGLE SIGN-IN DOOR — shippable copy

> ⭐ **PAUL'S EXCEPTION, 2026-09-12:** *"I don't think a copy gate is worth holding up a big build on.
> Ask the content steward for their best input and then go with that this time as an exception."*
> **These strings ship as written.** No options, no recommendation-plus-alternatives. Where I am
> uncertain it says so on the line, in this file, so the record carries it.
> ⛔ **EXCEPTION FOR THIS LAP ONLY.** The standing rule is unchanged: copy reaching a person is
> human-confirmed before it ships.

| | |
|---|---|
| **Item** | lap 9 · ROW A · **A11** — the single sign-in page, one door for the account |
| **Surface** | `onboarding/index.html` — `#s-door` (the chooser) · `#s-nolink` (the form, `#si-*`) · `#recover` |
| **Audience** | An adult signing in to **their own** estate at the one production origin — a place they founded or were invited to. Behind it, as the hardest reader: **Mom at 414 × 848 × A+, reads with difficulty, documented fear is getting it wrong.** ⛔ She is a TEST SUBJECT, not the persona — nothing below is written down to her |
| **Charters applied** | `content-principles/fernwood.md` · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · register-follows-audience) · `.content/2026-09-11-recovery-copy-DRAFT.md` (Paul-confirmed) · `VOCABULARY.md` §3b, §3e·R, §3f · `.engineering/2026-09-12-signin-door-disclosure-RULING.md` |
| **Tone register** | **Steady.** Not apologetic (nothing went wrong), not reassuring-for-its-own-sake, not brisk. Voice does not move; the tone acknowledges the shared work |
| **could-be-anyone** | **PASS** — by naming the accountable human and the real mechanism, not by naming a place. On an engine surface the anchor is **the person** (candidate principle, `.content/2026-09-11-recovery-copy-DRAFT.md` §8·1) |
| **anchor check** | **n/a by design** — engine surface, serves every household, names no place (`check-estate-neutral.py`; §3f). ⚠️ **See finding 5·3: one shipped string breaks this and nothing measures it** |

---

## 0 · The posture, stated once — most of this is a RATIFICATION, not a re-mint

**Four of the five deliverables below are the strings already at HEAD.** That is the answer, not a
dodge. The disclosure ruling's own finding is that A11's temptation is *re-minting live copy*, and
that **two sentences for one fact is how a claim drifts out of true while both copies look
confirmed** (`.engineering/2026-09-12-signin-door-disclosure-RULING.md` §4). The same logic that
forbids a second disclosure sentence forbids a second refusal string and a second recovery block.

So what this file does: **puts each shipped string to the tests it now has to survive at ONE ORIGIN,
records the defense so the `⚠️ DRAFT slot, content-steward's` markers in the build plan can be
struck, and changes the three things that are actually wrong.**

---

## 1 · The door's heading and supporting line

### 1a · The heading — ⛔ CHANGED. The page says "My Home"; the ruled wordmark is **My Home Place**

```html
<title>My Home Place</title>
```
```html
<h1 id="head">My <b>Home</b> Place</h1>
```

**Why those words:** they are not mine — they are Paul's, `[paul-ruled 2026-09-11 ~2:55 AM ET]`,
quoted in `VOCABULARY.md` §3b: *"let's just go with my home place for now and bold home in between
my and place… that'll make everything coherent when we move to my home dot place."* **Measured
2026-09-12: `My Home Place` appears in ZERO `.html` files.** The ruling never landed. §3b also makes
the top bar load-bearing rather than decorative — it *always answers "where am I"*, most specific
wins: **estate > person > the product**. At the sign-in door nobody is signed in, so the product's
own name is the only true answer, and at one origin this is the one line that tells a stranger what
they have arrived at.

**Two build notes, because the bold is not free:**
- `:1513` is `el.head.textContent = read(K_NAME) || "My Home";`. **The product state now needs
  markup and a person's place name must NOT get it** — a place name is user-supplied and
  `innerHTML` on it is an injection path. Branch: `if (named) head.textContent = named; else
  head.innerHTML = 'My <b>Home</b> Place';`
- ⚠️ **UNRESOLVED COLLISION, flagged not fixed.** `:888` renders *"Called "My Home" until you name
  it."* — **"My Home" is also the placeholder name for an unnamed estate.** Under the new wordmark
  the product is *My Home Place* and an unnamed place is *My Home*: two near-identical strings, one
  414px screen. I am not changing the placeholder tonight — it is stored-name-adjacent and outside
  A11 — but **the two cannot both stay.** Paul's, or ux-expert's with Paul.

### 1b · The lede and sub — ⛔ ROUTE-DEPENDENT, and that is correct. One is trimmed

The screen is reached three ways and the lede is already set by route (`:1197`). **Keep the split:**
a deliberate arrival and a dead link are different facts and one sentence cannot be true of both.

**Route A — the default at the one origin (deliberate arrival, no `?g=`; also the legacy banner):**

> **Sign in to your place.**
> **If you haven't set one up yet, you can create your account in a minute — no link needed.**

```js
_L.textContent = "Sign in to your place.";
_S.textContent = "If you haven’t set one up yet, you can create your account in a minute — no link needed.";
```

**Why those words.** The lede is **unchanged from HEAD** (`:1200`). The sub **drops its first
sentence** — shipped, it reads *"If you set your place up before, sign back in here. If you haven't
yet, you can create your account in a minute — no link needed."* Read the lede and the sub aloud as
one block (`fernwood.md` → *Read the whole card aloud*): the lede already says sign in here, so
sentence 1 says it a second time in weaker words. Cutting it leaves each line one job, and buys back
a line of vertical space at A+, where the recovery block and *Never set one up?* both sit below the
fold. **The surviving sentence is byte-identical to the shipped second half** — including *"no link
needed,"* which is doing real work for a word-of-mouth reader who arrived expecting an invitation
`[paul-ruled 2026-09-10]`.

⚠️ **The singular, and its falsifier.** *"your place"* is singular while an account may one day hold
several. I am shipping the singular deliberately: nobody holds two today (`POST /api/estate` still
409s the second, §3i), the plural *"your homes"* is VOCABULARY-flagged as reading oddly at one
grant, and at the moment of signing in a person is going to one place or to their shelf. **Falsifier:
the day a real person who holds two estates reads this line, re-read it.**

**Route B — a `?g=` link that did not resolve. ⛔ UNCHANGED, and it must stay:**

> **This link isn't working.**
> **If you've set your place up before, you can sign back in here.**

**Why unchanged:** when a link WAS presented and failed, *"this link isn't working"* is simply true,
and the narrow-by-construction guard at `:1195` already keeps it off every other route. The blameless
subject is the point — *the link* failed, not the reader.

### 1c · `#s-door`, the chooser — ⛔ UNCHANGED, and A11 must not collapse it into the form

> **Your place, on any phone.**
> **Set it up once, then sign in from wherever you are.**
> `[ ✓ Set up my place ]`  `[ I've been here before ]`

**Why unchanged:** it names what the reader gains, commits to no count, grades nothing, and is the
cross-device promise J9 walks. ⚠️ **And it is the reason a stranger's first screen at the origin is
not a form demanding a username they do not have** — `:2392` shows `#s-door` when no grant is held.
**Read from source at one branch, not walked; verify it in the J0 walk before trusting it.**

---

## 2 · Field labels and the submit control — ⛔ ALL UNCHANGED

| slot | string |
|---|---|
| username label | **Your username** |
| password label | **Your password** |
| submit | **✓ Sign in** (filled green + ✓) |
| busy state | **Signing in…** |
| both-boxes-empty guard | **Both boxes, then tap Sign in.** |

**Why those words.** `username` and `password` are the ruled words — `VOCABULARY.md` §3b, ⛔ *"Use
the WORD — not 'a word only you know', not 'a passphrase'."* The possessive *"Your"* is kept here and
deliberately **not** aligned to `s0`'s bare *"Username" / "Password"*: at `s0` a person is minting a
credential, at the door they are retrieving one they own. Different act, different article. The
`✓ Sign in` button is literally the ratified affirmative component — filled + glyph (CLAUDE.md
standing rule 1) — not a lookalike, so it cannot drift.

⭐ **ONE CLARIFICATION THE BUILD LANE NEEDS, because "one constant string" can be misread.** The
constant in §3 governs **exactly one branch: a non-2xx answer from `/api/session`.** `#si-trouble`
legitimately also holds two other strings, and neither weakens the constraint because **neither
varies with the server's answer about an account**:
- the empty-pair guard (`:1228`) fires **before any request**, on the reader's own input;
- the network-failure line (`:1301`) fires on a thrown fetch — no response at all.

**The test is not "this element holds one string." It is "no string rendered here may differ
according to whether the account exists."** All three pass.

---

## 3 · ⭐ THE ONE REFUSAL STRING — `#si-trouble`. ⛔ UNCHANGED, BYTE-FOR-BYTE

> ### **That didn't get you in. Check both boxes and try once more — or tap Can't get in? below.**

```js
t.textContent = "That didn’t get you in. Check both boxes and try once more — or tap Can’t get in? below.";
```

*Curly apostrophes (U+2019) ×2, em dash (U+2014) ×1. One branch, one assignment, selected from the
single `if (!d || !d.token)` arm at `:1237` — wrong password · unknown username · another
household's credential · a revoked one all arrive here and there is nothing to vary.*

**Why these words, clause by clause — this is the load-bearing item and it is being ratified, not
re-minted:**

| clause | why it survives the test |
|---|---|
| **"That didn't get you in."** | ⭐ **It names the DOOR, never the credential.** The subject is *that* — the attempt — not *you* and not a field. There is no grammatical slot in this sentence where a which-one could be added, which is the property the constraint actually needs: a string that **cannot be specialised** is safer than one that merely happens not to be |
| **"Check both boxes"** | **Both**, always, in every case. A reader is pointed at the pair, never at one. It is also the only honest instruction when the system genuinely does not tell the page which was wrong |
| **"and try once more"** | The cheap remedy first — true for the typo case, which is most of them |
| **"— or tap Can't get in? below."** | ⭐ **The escape for the cases retry can never fix** (unknown name, revoked, another house's). ⛔ Without it the constant would send a locked-out person into an infinite retry, which is how a security-correct string becomes a cruel one. It names the control in the control's own words, so there is nothing to match up |

**The disclosure test, stated the way the ruling states it:** *copy that enumerates the possibilities
is not disclosure; only copy that varies with the truth is.* This string offers **both** of the
reader's moves without claiming which applies to them. That is exactly what a forced constant is
supposed to look like.

⛔ **REJECTED, and recorded so it is not re-proposed:** exhibit 3b's *"that username isn't set up at
this house"* `[paul-ruled 2026-09-10]`. At one origin it would be **worse** than it was at five
deployments — usernames become globally unique, so *is this name taken* converges on *does this named
person have an account here*, which is a **membership disclosure about an individual**
(`.engineering/2026-09-12-signin-door-disclosure-RULING.md` §3).

⛔ **ALSO DELIBERATELY ABSENT: any sentence about usernames, existence, or privacy on this door.**
The security seat's ruling is explicit — the unsaid fact is created when a person **chooses** a name,
not when they **use** one; on the sign-in door it is not actionable, and **"a sentence appearing on
the sign-in door would be flagged NET-HARMFUL"** (§4). ⚠️ **Build lane: do not add one.** The
placement question belongs at signup and is ux-expert's.

⚠️ **What this string cannot do, said plainly:** it makes the **bytes** constant. It does not make
the **timing** constant, and timing has never been measured by anyone (the ruling's §0·4 and §7·3,
both marked unmeasured across three artifacts). **Copy cannot close that hole and should not be read
as having closed it.**

---

## 4 · The recovery affordance — ⛔ ENTIRELY UNCHANGED. CITED, NOT RE-AUTHORED

**Every string below already ships at `onboarding/index.html` `#recover`, Paul-confirmed 2026-09-11,
rationale at `.content/2026-09-11-recovery-copy-DRAFT.md`. A11 reuses them verbatim.**

| slot | string |
|---|---|
| entry link | **Can't get in?** |
| block heading | **Forgotten username or password** |
| ⭐ the ask + **the disclosure sentence** | **Type the email address you set up with. Paul built this, and he does the resetting himself — he writes to the address your account already has. This page won't say whether it's on file, because that would tell anyone who typed it.** |
| field label | **Your email address** |
| submit | **✓ Send** |
| receipt (200 only) | **That's written down where only Paul can read it, and he answers these by hand. If nothing's come back by tomorrow evening, email him at paul.kirschenbauer@gmail.com.** |

⛔⛔ **THE DISCLOSURE SENTENCE IS THE SHIPPED ONE AND A11 WRITES NO SECOND ONE.** *"This page won't
say whether it's on file, because that would tell anyone who typed it."* — the **because** is
load-bearing: without it the constant reads as an unhelpful machine; with it, it reads as a
protection of the reader. And note what it does **not** say: *this page*, never *we never*. The
forbidden generalisation — *"we don't confirm whether you have an account"* — is **false**, three
symbols publish username existence, and the ruling names it as *"the failure a build window will
actually produce"* (§4·5). **If the door needs the idea, it reuses these words. It does not restate
them.**

⛔ **The receipt never renders into `#si-trouble`.** Two constants, two jobs, two elements
(`#rc-done` / `#si-trouble`). A recovery receipt overwriting an unread refusal — or the reverse — is
a reader losing the sentence they were about to act on.

⚠️ **What one origin does NOT change here, verified by reading:** none of these sentences names a
place, a deployment or a household. That is why citing works — they were written engine-neutral and
they stay true. *"Paul built this, and he does the resetting himself"* remains true under §3f (he is
the **application administrator** at every household today). **Falsifier F3 is unchanged: the day
anyone else holds `X-Tate-Token`, every sentence on this list that says "Paul" has to change.**

---

## 5 · What is WRONG on this surface today, and what I would change

### 5·1 — ⛔ **The wordmark ruling never landed.** See §1a. *(changing)*
`My Home Place` is `paul-ruled 2026-09-11` and appears in **zero** `.html` files; `<title>`, the
`<h1>` and the `:1513` fallback all still say *"My Home."* At one origin the door is the product's
front page and this is the line that answers *where am I* for everyone who is not yet signed in.
**Plus the unresolved product-vs-placeholder collision at `:888`, flagged for Paul.**

### 5·2 — ⛔ **The sub line repeats the lede.** See §1b. *(changing)*
One fewer sentence, same facts, a line of A+ vertical space returned to the recovery block below it.

### 5·3 — ⛔⛔ **"back on wi-fi" is Fernwood's physics shipped on an engine surface.** *(changing, and it is the finding I would defend hardest)*

```js
// :1301  (sign-in, network failure)
t.textContent = "No connection right now — try again when you’re back online.";
// :1332  (recovery send, network failure)
rt.textContent = "That didn’t go through — nothing was sent. Try again when you’re back online.";
```
**Also `:1923` and `:2440` in the same file, same tail — change them together or the file forks.**

**Why.** CLAUDE.md records the site's founding premise: *"we're limited to Wi-Fi coming from the
house and don't really get cell reception."* **That is Fernwood's ground, and it is stated as
permanent and place-specific.** The sign-in door is reached by people who are **not at any household
at all** — locked out, anywhere, most plausibly on cellular. Telling a person in a Grant Park condo
to get *back on wi-fi* is one house's physics rendered at every house. ⭐ **This is the leak class
CLAUDE.md already measured and that `check-estate-neutral.py` structurally cannot see** — the 09-07
gauge incident leaked *"OUR GAUGE"* and *"123 days"* into three strangers' houses while the neutrality
check read ✅ 311 needles / rendered=0, because **it tests for NAMES and that leak was numbers and
possessive pronouns.** A connectivity premise is the same shape: no name in it, and it is still
Fernwood's.

⚠️ **I am proposing this against a string Paul confirmed on 2026-09-11** (`:1332`, the recovery
failure line). Recorded rather than done quietly: the confirmation was of a **recovery** decision,
not of the engine/instance seam, which was not in front of him. If he disagrees, the revert is one
word.

⛔ **SCOPE, named so a green here is not mistaken for a clean class.** `wi-fi` appears at **~9 more
sites in `engine/viewer.template.html` + `viewer.html`** (the offline-queue vocabulary: *"still on
your phone — it'll go to the record when you're back on Wi-Fi"*) and once at
`settings/account/index.html:356`. **Those are OUT of A11 and I am not touching them.** The split is
principled, not arbitrary: the queue strings are read by someone standing **inside a place**, where
at Fernwood Wi-Fi genuinely is the only network and the more specific word is the more useful one.
The door's strings are read by someone who is nowhere. **Owed: its own sweep, with Paul, over the
engine's offline vocabulary.**

### 5·4 — ⚠️ **A stale comment that will re-introduce cut copy.** *(flagging; comment only, no reader sees it)*
`:374–386` still reads *"there is no reset, which this project already records as its own
word-of-mouth dependency"* — **false since 2026-09-11**, when `Can't get in?` and `/api/recover`
shipped. The same block then says B12 CUT the *"Ask Paul…"* line, so the comment contradicts itself
two lines later. Under *a correction must sweep the files quoting it*: a build lane reading that
comment could reasonably re-add an ask-Paul line the closure deliberately removed. **Rewrite the
comment when A11 touches this block.**

### 5·5 — ✅ **Not a defect, recorded so it is not "fixed":** `#si-trouble` holding three strings. See §2.

---

## 6 · What I could NOT verify — every one of them

1. ⛔ **I have no Bash in this seat, so `git log -1 --format=%B 2f85f3a3` was not run.** I read the
   ruling's content from `.engineering/2026-09-12-signin-door-disclosure-RULING.md` — the filed
   artifact the brief points at. **I cannot confirm the commit message matches that file.**
2. ⛔ **Nothing was run and no origin was loaded.** Every string, line number and count here is from
   the working tree as read on 2026-09-12. **A source read cannot say what an origin serves.**
3. ⚠️ **`#s-door` as the bare-origin first screen** (§1c) is a read of ONE branch at `:2392`, not a
   walk. If A11 changes the routing, that claim goes with it.
4. ⚠️ **Timing equality of the refusal is unmeasured** and copy cannot fix it (§3).
5. ⚠️ **The wordmark ruling** is taken from `VOCABULARY.md` §3b's quotation of Paul, not from the
   session. The bold-on-*Home* rendering is my reading of *"bold home in between my and place."*
6. ⚠️ **Paul-confirmed status of the `#recover` strings** is taken from the file header of
   `.content/2026-09-11-recovery-copy-DRAFT.md` and the code comment at `:358`. I did not see the
   confirmation itself.

---

## 7 · Principles this would propose *(not written to the library; for a later Mode-3 pass)*

1. **`cross-project/voice-and-stance` — "A constant refusal must carry BOTH moves."**
   Where security forces one string across several causes, it must offer the cheap remedy *and* the
   escape, because it cannot know which reader it has. A constant that offers only retry is correct
   and cruel to the reader retry can never help. *(Origin: this door.)*
2. **`fernwood.md` → promote toward cross-project — "An engine surface may not carry one instance's
   physics."** Estate-neutrality is usually policed for names. A **premise** — the weather, the
   network, the terrain — leaks the same way and no needle list can see it. *(Origin: finding 5·3;
   second instance of the 09-07 gauge class.)*

---
---

# ADDENDUM A — `My Home Place` · the VOCABULARY entry `[paul-ruled 2026-09-12]`

> ⛔ **A PROPOSAL. `VOCABULARY.md` IS NOT EDITED BY THIS FILE.** It is canonical, `check-vocabulary.py`
> enforces structure over it, and a build session is the repo's single live writer. **Exact text
> below; route it to that writer.**

**Paul's words, 2026-09-12:** *"The content steward needs to go into the dictionary and say My Home
Place is the name of the product and the website, and should be the generic entry until people have
their own estate name or account name to display there. I think that we're not going to see someone
call their estate My Home Place, because that's in a way an awkward way of calling your home. So it
kind of reinforces it being a decent product name."*

## A1 · The exact §3b entry — ADD this row

| term | means | why this word |
|---|---|---|
| ⭐ **My Home Place** | **the name of the PRODUCT and of the WEBSITE.** Wordmark **My <b>Home</b> Place**, said *"my home dot place"*, at `myhome.place`. ⭐ **And it is the GENERIC ENTRY in the top bar** — it stands until a person has their own **estate name** or **account name** to show there | `paul-ruled 2026-09-12`. ⭐ **The reason is LOW COLLISION, and it was DERIVED rather than asserted:** *"we're not going to see someone call their estate My Home Place, because that's in a way an awkward way of calling your home. So it kind of reinforces it being a decent product name."* ⭐⭐ **A name nobody would plausibly choose for their OWN home is exactly what makes it safe as everyone's default** — the awkwardness as a personal name IS the evidence it works as a product name. ⛔ Retires the bare **"My Home"** as the generic entry (§4) |

## A2 · The ruled block to sit under the table

> ### ✅ THE PRODUCT'S NAME IS NO LONGER OPEN `[paul-ruled 2026-09-12]`
>
> ⛔ **THIS SUPERSEDES §3b's *"THE PRODUCT'S OWN NAME REMAINS OPEN — a greeting is not a brand"*
> paragraph, which closed *"Open, and `content-steward`'s to settle."*** It is settled, and not by
> `content-steward` — **by Paul, on the collision argument.** Strike the paragraph in place, as this
> file strikes rather than deletes, and point it here.
>
> ⭐ **What makes this different from a brand decision:** it is not a claim that the name is good, it
> is a claim that **the name is SAFE in the generic slot** — nobody's own place will collide with it.
> The rejection of *"estate manager"* (§4) still stands and is untouched: that name was refused for
> naming the reader as an operator of their own life, which this one does not do.
>
> ⛔ **IT DOES NOT RETIRE `your homes`** (§3b). That is the **greeting on the shelf**, a different
> slot with a different job. One names the product; the other addresses the person about what they
> hold. A build lane collapsing them would lose both.

## A3 · The §4 row — ADD, because the rejections are the point

| rejected | why |
|---|---|
| ⛔ **"My Home"** as the generic top-bar entry | **RETIRED 2026-09-12.** It sat one word from the product name — *My Home* for an unnamed place beside *My Home Place* for the product — two near-identical strings on one 414px screen. ⭐ **The ruling removes the collision by making the generic slot the product name itself**, so there is no placeholder left to confuse with it. ⚠️ **NOT a ban on the words**: a person may name their own place anything they like, and *"which name does a PLACE with no name show"* is a **different, still-open question** — see the gaps below |

---

## A4 · THE PRECEDENCE RULE — stated for literal implementation

**Three rungs. Most specific wins. This does not change the 2026-09-05 chain; it replaces only what
sits on the bottom rung.**

| # | state | the bar reads |
|---|---|---|
| 1 | **Inside an estate** | **that estate's name** — her word, verbatim, never title-cased |
| 2 | **Signed in, NOT inside any estate** — the shelf, account settings | **the username** (`paul-confirmed 2026-09-05`: the username, not a display name; there is no display name and none is wanted) |
| 3 | **Nobody signed in** — the door, the chooser, a dead link, the bare origin | ⭐ **My Home Place** |

⭐⭐ **IF BOTH EXIST, THE ESTATE WINS — BUT ONLY WHILE YOU ARE INSIDE IT.** This is the clause a build
lane will get wrong: **holding an estate is not being in one.** On `/homes/` a person may hold three
estates and is inside none of them, so the bar reads **the username**, not any estate's name. The bar
answers *where am I*, not *what do I own*.

---

## A5 · Every site that must change — MEASURED 2026-09-12, `grep -n "My Home"`

⚠️ **Four classes, and only the first is a rename.** Treating this as one find-and-replace would
rename three people's estates and break a test.

### ① THE PRODUCT SLOT — rename *(5 sites)*

| site | today | becomes |
|---|---|---|
| `onboarding/index.html:7` | `<title>My Home</title>` | `<title>My Home Place</title>` |
| `onboarding/index.html:313` | `<h1 id="head">My Home</h1>` | `<h1 id="head">My <b>Home</b> Place</h1>` |
| `onboarding/index.html:1513` | `el.head.textContent = read(K_NAME) \|\| "My Home";` | ⛔ **must branch — see the note below** |
| `onboarding/index.html:1422` | the spec comment naming the three states | ⭐ **it STATES THE RULE and is therefore wrong now** — rewrite to A4's table |
| `tools/pages-deploy.py:298` | `'<title>My Home</title>'` in the generated redirect | `'<title>My Home Place</title>'` |

⛔ **`:1513`'s branch is not cosmetic.** The wordmark needs markup; **a person's own place name must
never be injected as HTML.**
```js
var named = read(K_NAME);
if (named) el.head.textContent = named;                       // hers, verbatim, escaped
else       el.head.innerHTML  = 'My <b>Home</b> Place';       // ours, a literal, never user input
```
⚠️ Use `<b>`, not `<strong>` — a wordmark is a presentational offset, and `<strong>` would have a
screen reader announce emphasis on a product name.

### ② THE PLACE SLOT — ⛔ **DO NOT RENAME. These are a different question** *(4 sites)*

`estate/index.html:7` + `:173` (`<h1 id="place">`) · `settings/place/index.html:90` (the back-link,
A22) · `homes/index.html:277` + `:343` (`h.name || "My Home"`, a shelf row).

**Each of these falls back to "My Home" for a place with NO NAME.** Paul ruled the *product* slot,
not this one. ⛔ **Filling them with "My Home Place" would make a house on the shelf read as the
product**, which is worse than what is there today. **See gap 3.**

### ③ ESTATE NAMES IN CONFIG — ⛔ **DO NOT TOUCH, and this is the finding of this sweep** *(3 sites)*

`instance/home.json:12` · `instance/qa.json:12` · `instance/paul.json:12` — each `"name": "My Home"`.

⭐⭐ **THREE ESTATES ARE LITERALLY NAMED "MY HOME" TODAY, AND ONE OF THEM IS MOM'S PRODUCTION
ESTATE.** Paul's collision argument is that nobody would *choose* this name — **true, and nobody
did**: we wrote it as a default. So the near-collision he reasoned was implausible **already exists
in data**, created by us. ⚠️ **Changing these renames a place**, which is not a copy act. **My
recommendation, and it is Paul's call:** stop defaulting an estate's name to "My Home" — leave it
empty so the chain falls through honestly. **Flagged, not changed.**

### ④ TESTS AND FIXTURES — must move in the SAME commit *(1 blocking, several cosmetic)*

⛔ **`tools/journey-logic.py:185` — `if "<title>My Home</title>" in login_bytes`.** This **pins the
old title** and goes red the moment ① lands. **It is the one site that turns a copy change into a
broken build.**
⚠️ `tools/check-estate-neutral.py:45–52` (the exclusion comment quoting the generated "My Home"
redirect) and `:182 / :186 / :210` (fixtures) reference it; re-read after ①.
⛔ `.plans/walks/2026-09-05-onboarding-gate1.json:17` is a **walk artifact — historical, never edited.**

### ⑤ COMMENTS — the sweep rule, so nobody edits history
**A comment that NARRATES a past failure stays** (`onboarding:553/1259/1265/2474`, `worker.js:1064/1074/4616`,
`grant-mint:505/516`, `build-viewer:146–147`, `journey-walk:899/2172`, `viewer/engine:6454/7509/19993/20100`).
**A comment that STATES THE RULE changes** — `onboarding:1422` (in ① above) and `onboarding:1504/1511`,
which assert *"My Home is the honest placeholder."*

---

## A6 · ⚠️ WHAT THIS RULING DOES NOT SETTLE — four gaps, named so a build lane does not invent answers

**1 · An estate that exists but has no name yet, with a signed-in account.** Read literally, A4 sends
this to rung 2 — **the username** — because the estate has no name to show. But `:888` renders
*"Called "My Home" until you name it,"* which describes rung 3 behaviour, and `:1513` implements
rung 3 by checking only `K_NAME`. **The code and the chain already disagreed; this ruling does not
resolve it.** ⭐ **My recommendation, unruled:** inside the founding flow the bar reads **My Home
Place** and `:888` becomes *"Called My Home Place until you name it"* — a person naming a place wants
to see the thing being named, not their own username echoed back. Everywhere else, A4 as written.

**2 · A long user-supplied name, and the truncation trap.** No truncation rule exists anywhere. ⭐⭐
**And the sharp case is that truncation can MANUFACTURE the collision Paul's argument rules out:** a
place named *"My Home Place on the Lake"* truncates to **"My Home Place…"** — our renderer creating
the one name he reasoned nobody would choose. ⛔ **Rule owed: a truncated place name may never render
as a string equal to the product name.** The shape (ellipsis, wrap, two lines at 414 × A+) is
**ux-expert's, not mine** — copy cannot fix a layout, and I am not rewriting a name to survive one.

**3 · What a place with NO name shows in the PLACE slot** (class ② above — the shelf row, the estate
masthead, the back-link). ⛔ **"My Home Place" is the wrong answer there**, and the old "My Home" is
retired. Genuinely open. *(Two candidates if it helps: the town from the address, or an explicit
"Not named yet" that reads as an invitation rather than a name. Neither is drafted; it needs the
shape question answered first.)*

**4 · Environment decoration.** `dev.myhome.place` and `qa.myhome.place` serve the same product. ⛔
**The name does not become "My Home Place (QA)"** — a walker who needs to know which environment they
are in wants a separate marker, and an environment is not part of a product's name (§3h: *a name a
human reads and a value a machine stores are renamed on two clocks*).

---
---

# ADDENDUM B — the offline strings, REDRAFTED after Paul's pushback

**His words, 2026-09-12:** *"I think that this is just something that needs to work, and the key
point is that it needs to work regardless of whether you're connected to Internet via Wi-Fi or via
cellular or not, because that's just the environment. Some of these people are working outside."*

✅ **The coordinator's read is right and I accept the correction.** My *"back online"* fixed the
wrong half — it removed the connection TYPE and kept the instruction, so it still made the network
the reader's problem to solve. **What changed is the question: not *how do we word the failure*, but
*what does each surface say when the product is built to keep working.***

## B1 · THE CLASSIFICATION — and it does not split the way the brief expected

⛔ **NONE of the four sites is a capture path. All four are identity acts that cannot survive being
offline, and that is a finding rather than a disappointment.**

| site | the act | can it queue? |
|---|---|---|
| `:1301` | `POST /api/session` — **sign in** | ⛔ **No, and it never should.** A password is verified by the server; a queued sign-in would either admit someone unverified or park them outside a door they think they opened |
| `:1923` | `POST /api/account` — **create an account** | ⛔ **No.** A username must be claimed against the record. Queue it and a person uses the product under a name that may already belong to somebody |
| `:1332` | `POST /api/recover` — **ask to be let back in** | ⛔ **No, and queuing it would make the shipped receipt a lie.** *"That's written down where only Paul can read it"* is true because a KV row exists. A queued request is written **on the phone**, where he cannot read it |
| `:2440` | `GET /api/grant/whoami` — **check an arriving link** | ⛔ No — **and it is the odd one out**: the person submitted nothing. Nothing of theirs is at risk; the page simply could not check |

⭐ **So why did these strings sound wrong?** They borrowed the offline vocabulary from **the half of
the product that genuinely queues** — `viewer.html`'s outboxes, *"Saved on your phone — it'll reach
the record next time you're back on Wi-Fi"* — and applied it to a half that cannot. **The queue
wording is right where it is and wrong here.**

## B2 · The strings

**One shape for the three a person just tapped: state the condition (environmental, not theirs) ·
name the thing that survived · leave the retry conditional on the world, never on their diligence.**

```js
// :1301 — sign-in
t.textContent = "There’s no connection just now, so that didn’t reach us. Nothing is lost — try again when there is one.";

// :1923 — create an account
el.trouble0.innerHTML = "There’s no connection just now, so that didn’t reach us. Your answers are still here — try again when there is one.";

// :1332 — recovery send
rt.textContent = "There’s no connection just now, so nothing was sent. Try again when there is one.";

// :2440 — the arriving link (lede + soft, nothing was submitted)
'<p class="lede">No connection just now.</p>' +
'<p class="soft">Your link keeps working — try it again once there is one.</p>'
```

**Why these words:**
- **No connection TYPE anywhere.** Works outdoors, on cellular, on a dead bar, in a condo.
- ⭐ **Each names what SURVIVED** — *nothing is lost* · *your answers are still here* · *nothing was
  sent* · *your link keeps working*. That is the reassurance the reader actually needs, and it is the
  honest substitute for a queue promise we cannot make.
- **`"Your answers are still here"` is not a new wording** — it is the clause already shipped at
  `:1894` on the refusal path. No sixth variant minted.
- **`"nothing was sent"` is preserved verbatim in meaning** because it is load-bearing: the recovery
  receipt renders on a 200 only, and the refused/unreachable split is a security property.
- **`"try again when there is one"`** puts the condition on the world. It is not *go and fix your
  wi-fi*, and it is not a promise that we kept anything.

## B3 · ⛔ WHAT I AM ASSUMING, marked because I cannot run anything

**The safe half, stated first: none of these four strings claims anything was queued, saved or will
sync. I deliberately made no queue promise, because a false "it's saved" on a path that drops the
work is far worse than saying wi-fi.**

**Three claims are still code facts I read and did not execute. Have the build lane verify:**

| string | asserts | how to check |
|---|---|---|
| `:1301` *"Nothing is lost"* | a failed sign-in mutates no stored state | the `["catch"]` at `:1298` re-enables the button and nothing else; every `store()` is in the success path. **Source-read at one branch** |
| `:1923` *"Your answers are still here"* | the six typed fields survive the failure | the catch at `:1921–1925` does not call `clearAnswers()` or `step()`. ⚠️ **Verify in a browser with the network off** — this is the one a reader will catch us on instantly |
| `:2440` *"Your link keeps working"* | the grant is not consumed by a failed check | true by construction (no request reached the server), but **confirm nothing local marks the link spent before the fetch** |

⛔⛔ **AND THE STANDING CONDITION ON ALL FOUR: if the build lane ever makes one of these paths
QUEUE, its string is wrong that same day.** A queuing path must say what it kept; these say nothing
was sent. **Re-draft on change, do not adapt in place.**

## B4 · ⚠️ HIS FRAMING IS A PRODUCT REQUIREMENT AND COPY CANNOT DISCHARGE IT — worth him hearing

**Said plainly: a sign-in cannot be made to work with no connection, ever, and it should not be.**
Verifying a password requires the record. So if the requirement is *"this needs to work outdoors"*,
the honest reading is **not** that the door works offline — it is that **nobody who is already in
should ever be sent back to the door by a network blip.** That is the real requirement, and it is
checkable:

1. ⭐ **A held credential must survive being offline.** `homes/index.html:247` already carries the
   comment for exactly this — *"Wi-Fi range must not be told to sign in again — the credential is
   fine, the network is not"* — and `onboarding:1214` states the matching rule, **fail closed toward
   the session the person already has.** ⛔ **Nobody has walked it with the network off.** A J9 stop
   that kills the connection and reloads would prove or kill it in one action.
2. ⭐ **The app must paint before the network answers.** Already the design (the masthead reads
   localStorage first), and it is what makes "works outside" true for the 99% of openings that are
   not a sign-in.
3. ⚠️ **The genuinely unsolved case is a person signing in on a NEW device while outdoors.** No
   design makes that work. What can be done is make it not matter — a credential that survives on
   the device they already carry.

**That is engineering-partner and ux-expert work, not copy.** I am flagging it rather than papering
over it with a friendlier sentence, which is exactly what the original *"back on wi-fi"* was doing.

---

## C · PLACEHOLDERS FOR §A6's GAPS — ⛔ THE COORDINATOR'S, NOT PAUL'S AND NOT CONTENT-STEWARD'S

**Added by the build window 2026-09-13 ~03:00 ET, verbatim from the coordination channel, because
they existed ONLY there.** `[paul-ruled 2026-09-12]`: *"Just come up with placeholders for the small
gaps and we will be able to review them later in context and find the right answer. Don't let that
hold up our build."* He authorised **that placeholders be minted**; he did not author these, and
neither did the steward whose file this is.

⛔ **ATTRIBUTION MATTERS HERE AND IS THE REASON THIS SECTION EXISTS.** A placeholder that gets
committed and then reads as ruled is the failure mode this lap hit three times in one night. Every
row below is **the coordinator's proposal, pending Paul's in-context review.**

| gap (§A6) | placeholder | whose |
|---|---|---|
| **1 · signed in, estate has no name** | show **the USERNAME** — it falls out of Paul's own ruling (*"until people have their own estate name **or account name** to display there"*), so the chain is estate name → account name → My Home Place and this case lands on the middle rung | coordinator |
| **2 · truncation** | ⛔⛔ **WITHDRAWN BY THE COORDINATOR, 2026-09-12** — struck in place, not deleted, because a withdrawn proposal that vanishes gets re-proposed. ~~if truncating a place name would produce exactly `My Home Place`, truncate **one character shorter**, so *"My Home Place on the Lake"* renders `My Home Plac…` rather than manufacturing a false product name~~. ⛔ **TWO THINGS WRONG WITH IT, found by the build lane 2026-09-12:** (1) **there is no truncation mechanism anywhere to attach it to** — the rule guards a code path that does not exist; and (2) **`estate/index.html:91` deliberately takes the OPPOSITE position** — *"a masthead that ellipsises has edited her word."* So the placeholder would have contradicted a shipped design stance in order to solve a problem that cannot occur. ⭐ The coordinator's own note on it: *"I invented a guard for a mechanism I never checked existed."* ⚠️ **§A6·2's underlying observation is NOT withdrawn** — truncation *could* manufacture the one name the ruling exists to keep unique. It is a live question **if** truncation is ever introduced, and it is ux-expert's shape to design then. ⛔ Nothing to rule on tonight. | coordinator (withdrawn) |
| **3 · the PLACE slot for an unnamed place** (`estate/index.html:7`·`:173` · `settings/place:90` · `homes/index.html:277`·`:343`) | **"Your place"** — it can never collide with the product name (the point of the ruling), it matches the door's existing second-person register (*Your username · Your password · Your email address*), and it reads as a SLOT rather than a name, which is honest because the place genuinely has no name yet. ⛔ Not *My Home Place* (makes a house read as the product) and ⛔ not leaving *My Home* (the near-identical string the ruling exists to remove) | coordinator |

⚠️ **The steward DISAGREES with placeholder 1 in this very file** (§A6·1: inside the founding flow the
bar should read **My Home Place**, because *"a person naming a place wants to see the thing being
named, not their own username echoed back"*). **That disagreement is live and is not resolved here.**
Implement the placeholder, carry the disagreement, let Paul see both in context.

**Release condition for the TWO that stand (#1 and #3 — #2 is withdrawn above), and it is concrete rather than "later":** ⭐ **Paul reads them in
the running app and either confirms or revises.** A hold with no release condition is abandonment
with manners.
