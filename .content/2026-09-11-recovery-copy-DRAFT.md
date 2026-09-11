# Recovery copy — the one constant receipt, and the ask above it — DRAFT

> ⛔ **AUTHORED CONTENT UNDER THE AI BOUNDARY.** Every line below reaches a person, and this one
> reaches them at the moment they cannot get in. **Nothing here is approved. Nothing ships until Paul
> confirms the words.** Nothing has been edited into a tracked surface file.

| | |
|---|---|
| **Draft** | `content-2026-09-11-recovery-copy` · lap 7 row B · B6 · design closure rows 28/29/31 · taps L11–L13 |
| **Commissioned by** | `[paul-ruled 2026-09-11 ~12:45 AM ET]` — *one honest constant sentence naming a person*, replacing *"if that address is on file, it has been sent"* |
| **Audience** | A person who cannot get into their own place, on a phone, with no sign-in and no policy page. Behind it: **Mom at the condo** — reads with difficulty, served A+, whose documented fear is getting it wrong. She is the reader this string is priced against. |
| **Surface** | `onboarding/index.html` `#s-nolink` — the recovery block revealed by `Can't get in?` (row 28), below `#si-trouble` and above `Never set one up?`. Same block serves **username and password** (row 28). |
| **Charters applied** | `~/.claude/content-principles/fernwood.md` · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · credit-don't-thank · register-follows-audience) · `.content/2026-09-10-founding-flow-copy-REVIEW.md` §A4 (one narrator) · CLAUDE.md tone + rule 5 · `VOCABULARY.md` §3e·R, §3f |
| **Tone register** | **Steady.** Not apologetic (nothing went wrong), not reassuring-for-its-own-sake (the charter's Avoid list), not brisk. The person is stuck and anxious; the voice does not move, the tone acknowledges the shared work — *fernwood.md* → "Acknowledge the shared work — for uncertain readers." |
| **could_be_anyone** | **PASS** — the recommended string names a real person, his own email address, and a by-hand mechanism. No stranger could have written it. |
| **anchor_check** | **n/a by design.** This is an **engine** surface serving every household; it must name no place (`check-estate-neutral.py`; `VOCABULARY.md` §3f). See *Principle to propose #1* — on an engine surface the anchor is **the person**, not the place. |
| **Conditions** | 414 × 848 × A+ |

---

## 0 · The six constraints, and where each one landed

Security's `③ LEGIBILITY L3` list is binding. Mapped to the drafts so a reviewer can check them off:

| # | constraint (`.engineering/2026-09-10-recovery-route-SECURITY.md` L3) | where it is satisfied |
|---|---|---|
| 1 | one string, byte-identical for every outcome, from a single branch; no second round trip | the receipt contains **nothing derived from the submitted address** — no name, no domain, no "we'll write to *you@…*". There is only one string to render, so there is only one branch to write |
| 2 | may not assert an act the system does not perform | *"written down"* is the act the Worker performs (a KV row). **No send verb, no past-tense delivery, no check.** The only delivery verb — *"email him"* — describes what **the reader** does |
| 3 | must name that **a person** reads it, and set an honest expectation of **when** | *"only Paul can read it"* · *"he answers these by hand"* · the when is expressed as **the reader's own trigger to escalate**, not as our promise — see §3 |
| 4 | readable holding only a phone and a link — no policy page, no sign-in | every fact is in the two blocks on that screen. ⚠️ **It may not lean on the s0 introduction** (*"I'm Paul. I built this…"*, review A4 edit 1) — a locked-out person never sees s0. So **the ask introduces him**; see §2 |
| 5 | must not contradict the refused/unreachable split (RR-5) | the receipt renders **only on a 200**. A failed POST keeps the shipped sentence *"That didn't go through — your note is still here, tap Send once more."* (`estate:662` and four siblings). ⛔ See §6 finding 3 |
| 6 | must leave a second door that does not depend on this route | sentence 2 **is** the second door: `paul.kirschenbauer@gmail.com`, already on the screen at `onboarding:488` and already ruled KEEP `[paul-stated 2026-09-05]` |

And the ruling it implements, `VOCABULARY.md` §3e·R: **the credential goes to the address on the
account row, never the request's.** That rule has a copy consequence nobody has written down —
*a person who types an address that is not the one on their account will hear nothing, at an address
they are watching.* The **ask** carries it (§2), because saying it in the receipt is too late.

---

## 1 · RECOMMENDED — the constant receipt

> ### DRAFT — recommended
>
> **That's written down where only Paul can read it, and he answers these by hand.
> If nothing's come back by tomorrow evening, email him at paul.kirschenbauer@gmail.com.**

*Two sentences, one string, 30 words. Renders in place of the field + `✓ Send`, on a 200, and is
identical for every address typed.*

**Word by word, and why each one is there:**

| clause | why |
|---|---|
| **`That's written down`** | The act the system actually performs — B6 writes one KV row, unconditionally, with no lookup (`[paul-ruled 2026-09-11]`, B6 lookup: *none this lap*). It is the honest past tense; *"has been sent"* was not. It also does what `capture must not lie` asks of every other capture surface in this product: say what was kept |
| **`where only Paul can read it`** | The **ruled destination** in the reader's words — B6 lands on its own admin-only key, members never read it, it never enters the mom cycle's arrival record. ⭐ This is L3's own instruction: *the mechanism must be legible as a deliberate protection of them.* It is the one line here that converts paid-for security into trust the reader can feel |
| **`Paul`** | Security L2: *"the route that most looks like stonewalling is the one where naming the human is both honest and the strongest thing the product can say."* Also the only available trust vocabulary — staff-blindness is not available to this product, accountability is. **See open question 1** |
| **`he answers these by hand`** | Sets **when**, truthfully, without a clock: a human on human time. It pre-explains the wait instead of apologising for it afterwards. ⛔ It replaces the shipped *"it only takes him a second"* (`onboarding:357`), which is a time claim this route cannot keep — see §6 finding 1 |
| **`If nothing's come back by tomorrow evening`** | ⭐ **The time expectation is expressed as the reader's trigger, not as our promise.** Nothing here can become false if Paul is slow; the reader simply escalates. It also silently covers §3e·R's real failure mode — a reply sent to a different address on the account row looks exactly like silence, and this tells them what to do about it |
| **`email him at paul.kirschenbauer@gmail.com`** | Constraint 6. It does not depend on this route, on the Worker, or on Paul's sweep; and the reader can **verify it left**, which is the one thing nothing else on this screen gives them (*"on this route nothing is verifiable by them"*) |

**What it deliberately does NOT say, and why:**

- ⛔ **No "if that address is on file."** There is no lookup. The clause asserted a check that does not happen (L1(3)).
- ⛔ **No "has been sent."** Nothing sends; the Worker has no outbound email capability of any kind (L1(1), searched-negative).
- ⛔ **No "we".** One narrator `[paul-ruled 2026-09-05]`; review A4 retires the corporate *we*.
- ⛔ **No apology, no "sorry you're locked out", no "don't worry".** *fernwood.md* → "Acknowledge the shared work" **Avoid**: reassurance-for-its-own-sake is Duolingo-mentor, not Leopold-mentor. Nothing went wrong; a person forgot a password.
- ⛔ **No ✓ glyph on this string.** The affirmative grammar is spent on the `✓ Send` she just tapped (CLAUDE.md standing rule 1). A receipt is not a second affirmative.

---

## 2 · The ask above the field — revised so the receipt agrees with it

Today the block does not exist; what stands in its place on that screen is
`onboarding:357` — *"Can't remember your password? Ask Paul — he can reset it, and it only takes him
a second."* Row 28 replaces it with one entry point covering **both** username and password.

> ### DRAFT — recommended (the revealed block)
>
> **Forgotten username or password**
>
> **Type the email address you set up with. Paul built this, and he does the resetting himself — he
> writes to the address your account already has. This page won't say whether it's on file, because
> that would tell anyone who typed it.**
>
> `[ Your email address ]`
> `[ ✓ Send ]`

*Three sentences, 42 words, one job each.*

| sentence | job | citation |
|---|---|---|
| *"Type the email address you set up with."* | the ask, in plain words, no *"please enter"*, no validator register | `estate:362–365` — *"NOT A VALIDATOR… a form that rejects her address scolds the one reader least willing to be told she is wrong"* |
| *"Paul built this, and he does the resetting himself"* | ⭐ **the introduction, here, because s0's introduction is unreachable from this screen.** A locked-out person meets a stranger's first name otherwise — exactly the defect review A4 found at `:420` and mom read as *"Who is 'me'?"* | review A4; constraint 4 |
| *"he writes to the address your account already has"* | **`VOCABULARY.md` §3e·R, in the reader's words.** It is the only place this fact can be useful — told after the tap it is an explanation for silence; told before it is information they can act on | §3e·R; D1 (the administrator is the reset path) |
| *"This page won't say whether it's on file, because that would tell anyone who typed it."* | ⭐ L3 exactly: *copy that enumerates the possibilities is not disclosure; only copy that varies with the truth is.* The **because** is load-bearing — without it the constant reads as an unhelpful machine; with it, it reads as a protection of them | L3; security L2 |

**Why the split is the design, not a convenience.** The receipt can be two sentences *because* the ask
is carrying who-he-is, where-the-reply-goes, and why-we-won't-confirm. Put those in the receipt and it
becomes a five-sentence wall arriving at the worst possible moment; put them in the ask and the person
reads them **before** spending a tap. The two agree by construction, which is what the brief asks for.

⚠️ **The entry-point label `Can't get in?` is ruled (row 28) and is not re-opened here.** It is the
right words: a locked-out person usually cannot say *which* thing they have forgotten, and D1 makes
both the same act.

---

## 3 · Two alternates, with the trade named

> ### ALTERNATE A — no clock at all
>
> **That's written down where only Paul can read it, and he answers these by hand.
> If nothing's come back, email him at paul.kirschenbauer@gmail.com.**

**The trade.** It is the only draft that cannot age into a false statement under any behaviour by
anyone — there is no window to miss. **What it costs is constraint 3's second half**: *"sets an honest
expectation of WHEN"* is satisfied only by *"by hand"*, and *"if nothing's come back"* gives the reader
no point at which to stop waiting. ⚠️ **Mom is the reader most likely to wait indefinitely** and least
likely to chase — her documented posture is not wanting to be a bother. Choose this only if Paul will
not commit to any window at all.

> ### ALTERNATE B — the window as a promise
>
> **That's with Paul now — he'll have you back in within a day or two.
> He writes to the address your account already has.**

**The trade.** Warmest, shortest, and by far the clearest to a worried reader — and it is **the only
one of the three that can become false without anyone noticing.** Three costs, stated plainly:
(1) *"with Paul now"* asserts a delivery the system does not perform — there is no notification; the
row sits in KV until he runs the pickup block, so this is the *"has been sent"* failure returning in
softer clothes; (2) it spends the reader's next move on **waiting** and drops the second door, which
is constraint 6; (3) a missed window is a broken promise to the one reader who has no other way in —
**the highest-cost place in the product to break one.** ⛔ Do not ship this unless Paul is committing
to the window personally and accepts (2).

---

## 4 · Falsifier per sentence — the fact asserted, and where it would be false

The brief's own instrument. Every clause that makes a claim about the world, with the condition that
would falsify it.

| # | clause | fact it asserts | where it would be FALSE | check |
|---|---|---|---|---|
| F1 | *"That's written down"* | a durable record was created by this submission | the POST failed, or the handler 400s. ⚠️ **`handleFeedback` rejects a record with neither sentiment nor note** (`worker.js:3962`) — a genuinely outcome-only record fails that validation, so B6 must write its own KV row. **If it does not, this sentence is false on the route's first request** | `python3 tools/watch-feedback.py --env qa` shows the `account-recovery` row on its own admin key after a submit; a 4xx/5xx must render §6 finding 3's sentence instead |
| F2 | *"where only Paul can read it"* | the record is not readable by a household member | the record lands on the estate feedback key (`feedbackDestination` rule 1) instead of its own admin-only key. **This was the specified behaviour until the 09-11 ruling** — it is the single likeliest way this sentence ships false | `grep -n '"/api/feedback"' worker/worker.js` — the recovery key's route must be in `ADMIN_ONLY`, never `MEMBER_OK`; and `read-mom-feedback.py --pickup` must **not** show a recovery request as an arrival |
| F3 | *"only Paul"* | one named person, and no other reader | a second application-administrator credential exists, or the master token is held by anyone else (`VOCABULARY.md` §3f — the application administrator is a **seat**, and today it is him) | true today by Paul's own statement; **re-check the day anyone else holds `X-Tate-Token`.** If that ever happens this sentence must change to a role, and the trust it buys is gone |
| F4 | *"he answers these by hand"* | a human, not an automation, performs the reset | a send path or an automated reset is built (lap 8, V8). ⭐ Then this sentence is **stale in the good direction** — but still stale, and this is the one clause that a future improvement makes false | any commit adding an outbound mail capability re-opens this file |
| F5 | *"If nothing's come back by tomorrow evening"* | a reply is a thing that can come back at all | the account has **no** contact value on its row, in which case nothing can ever come back and the reader waits for something impossible. ⚠️ **UNRESOLVED — see open question 4** | `/api/profile`'s email field is optional and `#contactnone` ("Please don't") is a real choice at signup |
| F6 | *"email him at paul.kirschenbauer@gmail.com"* | that address reaches him | the address changes, or it stops being one he reads. It is already shipped at `onboarding:488` and ruled KEEP, so this adds no new exposure — **but it is now load-bearing in two places** | it is a literal in two files; a change must move both |
| F7 | ASK · *"he writes to the address your account already has"* | the reply goes to the account row's value | a reset is ever sent to the address in the **request**. That is the §3e·R falsifier verbatim: *a credential sent to an address that appears in a recovery request and not on the account row* | §3e·R; it is a rule about **Paul's own act**, and no code enforces it |
| F8 | ASK · *"This page won't say whether it's on file"* | the response does not vary with the truth | any second round trip, any field-state change, any timing difference. ⚠️ **L12's timing half is marked UNCHECKED in the walk** and the transport measurement has never been run by anyone, three artifacts running | byte-identity is checkable in the Chrome walk; the timing half needs `curl -w %{time_total}` distributions, once, ever |
| F9 | ASK · *"because that would tell anyone who typed it"* | the product does not publish existence | ⛔ **narrow and deliberate — it claims only that THIS PAGE does not confirm an EMAIL address.** `/api/account/available` publishes **username** existence unauthenticated, by design and knowingly. The forbidden inverse, which must never be said by the product, a release note, or Paul to a neighbour: *"we never reveal whether an account exists."* | security L1's honest-posture box. **The draft says *this page*, never *we never* — that word choice is the finding** |

---

## 5 · Where each string goes

| slot | string | note |
|---|---|---|
| `#si-trouble` (`onboarding:343`) | **unchanged** — the one constant sign-in refusal (row 31) | ⛔ **Do not render the receipt into `#si-trouble`.** Two different constants with two different jobs; sharing the slot means a recovery receipt can overwrite a refusal the reader has not read, and vice versa. The recovery block needs its own `#rec-said` element |
| `Can't get in?` | **unchanged**, ruled (row 28) | below `#si-trouble`, above `Never set one up?` |
| the revealed block | §2's ask + one field + `✓ Send` | one field only (row 29) |
| on 200 | §1's receipt, in place of the field and the button | one branch, one string |
| on a failed POST | *"That didn't go through — your note is still here, tap Send once more."* | already shipped in five files; **do not mint a sixth wording** |
| `onboarding:357` | ⛔ **cut** — see §6 finding 1 | its job is taken by `Can't get in?` |
| `/settings/account/` row 30 (signed-in twin) | ⛔ **do not reuse this string** | different reader — they are **not** locked out, the account row's address is known to the product, and the constant-response constraint does not apply to them. That card's copy is a separate draft; it currently reads *"Paul can reset your password — one tap sends him your username, never your password."* and is fine |

---

## 6 · Three findings the drafting turned up

**1 · `onboarding:357` contradicts the receipt, and is itself an unkeepable time claim.**
*"Ask Paul — he can reset it, and it only takes him a second."* The **doing** takes a second; the
**noticing** takes until he next runs the pickup block. Ship the receipt beside this line and the
screen tells the reader two different things about time, one of which is the reason the other exists.
⛔ **Cut it when the recovery block lands** — do not soften it, because `Can't get in?` now does its
whole job and a second route to the same act re-creates row 28's *"don't make the reader diagnose
their own failure."*

**2 · The introduction problem is structural, not a wording choice.** Review A4 places the narrator's
introduction on **s0**. A locked-out person reaches `#s-nolink` **without passing s0** — from a dead
link, from the sunset banner, from `?from=signout`, or from the bare origin's door. So *every*
sentence on this screen that says "Paul" is speaking to someone who may never have been told who he
is. The ask carries the introduction for that reason, and it is **not redundant with A4's edit 1**;
they cover two disjoint sets of readers.

**3 · The constant renders on a 200 only — and that is a security property, not a nicety.** If a
failed POST also rendered the constant, the product would be claiming a record it does not hold —
`capture must not lie` — **and** it would make the route's response *stop* being constant in the only
way that matters (a reader could learn something from which sentence they got). Both halves point the
same way: 200 → the receipt, anything else → the shipped send-failure sentence.

---

## 7 · Questions Paul must answer before these words ship

1. ⭐ **May the screen use your name?** The drafts say **Paul**, four times across the two blocks, plus
   your personal email address. The case for: `VOCABULARY.md` §3f makes you the **application
   administrator** at every household today, so it is true everywhere; security L2 says naming the
   human is the strongest honest thing this route can say; and your name and that address are
   **already on this flow** at `:357`, `:420`, `:488`, `:604` `[paul-stated 2026-09-05]`. The case
   against: it is a personal name on an engine surface that will one day serve households you do not
   administer — and on that day **F3 fires and every one of these sentences has to change.** If you
   want it future-proofed now, say so and I will draft the role-named variant; it is materially
   colder and I do not recommend it today.

2. ⭐ **The time promise — which of the three shapes?**
   (a) **recommended** — no promise; *"he answers these by hand"* plus *"if nothing's come back by
   tomorrow evening, email him"*. Nothing can become false; the reader always has a next move.
   (b) **Alternate A** — no clock at all. Safest, and it leaves Mom with no point at which to stop
   waiting.
   (c) **Alternate B** — *"within a day or two"* as a commitment you are making personally.
   ⚠️ If you pick (a), I still need you to confirm **"tomorrow evening"** is the right bound — it is
   the number I invented, and the only thing behind it is that the pickup block's own Mom-check
   counter warns at seven days, which is far too long to leave someone locked out.

3. ⭐ **The second door — is `paul.kirschenbauer@gmail.com` the right one, and is it right for Mom?**
   It is the door I used because it is already on the screen, already ruled KEEP, and the reader can
   verify it left. But **Mom's real second door is almost certainly her phone**, not email — and I
   will not put *"text or call him"* on a shipped surface on my own read, both because it is your
   personal availability being promised to strangers at other households and because this repo's
   channel doctrine deliberately keeps text out of the product. **Your call, and it may differ per
   deployment.**

4. ⚠️ **What does this say to someone whose account has no email on it?** *"Please don't"*
   (`#contactnone`) is a real choice at signup, and review B9 already found that its cost — *this
   closes the only reset route* — is stated **nowhere at the moment of choosing**. For that person,
   F5 fires: the receipt tells them to wait for a reply that cannot come. **This is not a wording
   problem and I am not solving it in this string.** Two honest exits, both yours: say the cost at
   the moment of choosing (review B9's draft line), or let the second door carry them. **Flagged to
   `ux-expert` / the build lane** as the one reader this route cannot serve.

---

## 8 · Principles to propose

*(Not written into the library. Proposed for ratification.)*

1. **`cross-project/voice-and-stance` — "On a surface that must name no place, the anchor is the
   person."** `[candidate — 1 occurrence]`
   *Statement:* Where estate-neutrality or multi-tenancy forbids the copy from naming the place, the
   could-be-anyone test is not satisfied by voice alone — it is satisfied by naming **the accountable
   human and the actual mechanism**. Specificity has to come from somewhere; if it cannot come from
   the place, it comes from the person.
   *Why:* This string. Every other Fernwood surface passes the anchor test on *the laurels by the
   porch*; an engine surface cannot, so the same test would have to be waived — and waiving it is how
   engine copy drifts to bland-everywhere. Naming Paul, his own address, and *"by hand"* makes the
   sentence unwriteable by a stranger without naming a single place.

2. **`Fernwood` — "Express an unkeepable window as the reader's trigger, not as our promise."**
   `[candidate — 1 occurrence]`
   *Statement:* When a latency depends on a human's attention rather than on a system, do not promise
   a window. Name the point at which the reader should do something else. A promise can be broken
   silently; a trigger cannot.
   *Why:* The recovery route's latency is *"whenever Paul next runs the pickup block."* *"Within a day
   or two"* is a promise nothing enforces; *"if nothing's come back by tomorrow evening, email him"*
   carries the same information, cannot become false, and leaves the reader holding the next move.
   Generalises to any queue a human drains — feedback replies, a reset, an invite.

3. **`Fernwood` — "Say what a record is protected FROM, not just that it is safe."**
   `[candidate — 1 occurrence]`
   *Statement:* A privacy property the reader cannot see buys no trust. State it as the concrete
   boundary — *"where only Paul can read it"* — rather than as a reassurance (*"it's private"*,
   *"kept secure"*).
   *Why:* Security L3: the 404 discipline, the dummy derive, the personId-null guard and the
   member/admin split are *"real, paid for, and unreadable from the person's seat."* One clause of
   six words converts the most expensive protection in the route into something the reader can feel.
   Sibling of the shipped *"Nothing goes to Google unless you tap."*, which is the same move and is
   the line every seat named unprompted.
