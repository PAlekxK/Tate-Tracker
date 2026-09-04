# The product name, re-run narrow — rendered vs spoken, and the family label's form

**Date:** 2026-09-03 · **Lens:** content-steward · **Mode:** draft (naming), **deliberately narrow**
**Charters applied:** `cross-project/voice-and-stance.md` (could-be-anyone · credit-don't-thank ·
register-follows-audience) → `fernwood.md` (*anchored naming beats field-journal-fluent naming*;
door-layer per §4a) → `VOCABULARY.md` §2 / §3b / §4.
**Ruled context cited, not edited:** `.plans/2026-09-03-product-name-PLAN.md` (Q1–Q4, the
reversibility ladder, the Files-touched sweep).
**Audience:** Paul (ruling) · Mom (the only person who meets a rendered surface daily) · a stranger
who types the apex · Bob's family, later. **Surfaces:** the apex page · a family door · the instance
shell · four hand-edit sites · what is said out loud.
**Register:** *(how the voice flexes to the reader's state)* plain and unceremonious — a door is
opened, not announced.

> **GATE. Nothing decided, no canon touched.** No edit to `VOCABULARY.md`, `CLAUDE.md`,
> `BACKLOG.md`, any `*-PLAN.md`, `viewer.html`, or my own earlier trail. Everything below is a
> recommendation ending at Paul's gate.

> ## ⭐ AMENDMENT, same day — **§2 is REWRITTEN. §1 and §3 are unchanged.**
>
> Paul stress-tested the label spec with a case neither the plan nor I had put to it: *"Let's say
> some of Bob's relatives want to adopt this. They have multiple homes as well and they all use the
> same last name — Rolader. Would that mean we back ourselves into Rolader-one?"*
>
> **He is right, and the defect is mine.** §2's namespace was **surnames**; the thing being named is
> **households** — and surnames are least distinguishing exactly where this product spreads, because
> it spreads through relatives and neighbours. Several related households sharing a surname is the
> middle of the distribution, not the tail.
>
> ⛔ **And my own no-derived-suffix argument turned against my own rule.** I refused an auto-suffix
> because *"it tells the second family they are the duplicate."* Among strangers that is mild. **Among
> siblings it is a status assignment inside one family** — one brother is *the Roladers* and the other
> is not. My manual escape hatch is no better: *"the second household chooses a distinguishing
> label"* becomes *"your brother already has your last name."* **The rule produced the exact harm it
> was written to prevent.**
>
> **Amended rule: the household chooses its own label; the surname is OFFERED as a default, never
> derived as the rule.** Tested in § 2e, not assumed. §2a–§2d below are the amended text; the
> superseded surname-first version is in git history and is not restated here.
>
> ⚠️ **§1's verdicts do not move** — they govern *where a label is rendered*, not *what it says*. One
> of them turns out to be load-bearing for this amendment (§2e.3).

---

## 0 · What this supersedes in the 09-03 trail, and what carries forward

**These two files are not peers.** Where they disagree, this one is current.

⛔ **VOID in `.content-reviews/2026-09-03-product-door-naming.md`:**

| section | status |
|---|---|
| **§4 · the pick** — *Porchlight* / `porchlight.place` | ⛔ **VOID.** The domain is registered (RDAP 2026-08-10, recorded by this seat in the greeting note), and the apex is ruled **`myhome.place`** `[paul-ruled 2026-09-03]`. The trail contains zero mentions of `myhome`. |
| **§2 · candidates A–E as a choice set** | ⛔ **VOID.** All five were scored as *the one door's* name. There are now three levels. |
| ⭐ **§2a · "every surname candidate breaks at Bob"** | ⛔ **INVERTED, not merely stale.** It was correct against a one-door model. At the **family** level the objection dissolves by construction: `<surname>.myhome.place` makes no claim on Bob, because Bob's family gets its own label. **The bare surname §2a retired is now the ruled answer one level down.** A reader trusting §2a today reaches the opposite of the truth. |
| **§5.6 ·** `.place` vs `.house` vs `.com` | ⛔ moot — ruled `.place`. |

✅ **CARRIES FORWARD as input, not re-derived here:** §4a (door vs room — and note the ruled apex is
**evidence for** it: `myhome.place` is maximally warm-generic, exactly what §4a predicts a door
should be) · §2d (*portfolio* triple-booked and the twice-named anti-persona; *estates* reads as
property management) · §2e (the three recorded kills: Keyring/Keychain · cherry/orchard ·
Guide/Fieldbook/Journal) · §2b.1 (the retraction — **sayable, not typeable**) · §5.1 (the identity
cost, **escalated and still open**) · and the constraint that bears hardest here, from
`.content-reviews/2026-09-03-myhome-place-greeting.md` § c:

> *"`my` appears exactly once in the whole system — in the address — and nowhere in the shell's
> chrome. A second `my` turns a name into a pattern, and the pattern it becomes is the portal."*

⛔ **Out of scope, settled, not re-opened:** Fernwood's `<h1>` stays *Fernwood* and its authored
subtitle stays anchored (§4a). Q2's ruling (`bare-surname-lowercased`), Q3's ruling (*My Home*,
provisional), Q4 (the brother's door, **parked**).

---

## 1 · Question A — the rendered / spoken seam

### 1a · The constraint cuts across the option set. Here are its two readings, separated.

Paul ruled the **name**. He did not rule **where it appears**, and the `my`-count discipline does not
choose within the options — it splits them. Read it two ways and you get two different answers, so
the honest move is to say which reading is load-bearing and why.

**Reading 1 — strict token count.** *The literal string `my` may occur once, in the address.* Under
this reading, any rendered *My Home* anywhere is a second occurrence and the discipline is broken.
Clean, checkable, and **slightly over-firing**: the note's own mechanism is that repetition turns a
name into a **pattern**, and a pattern needs *variation on a template* — `my account`, `my settings`,
`my dashboard`. One name appearing twice is a name appearing twice, not a template.

**Reading 2 — what the note is actually protecting.** *A possessive attached to a **system noun** is
what reads as an account.* `my home` attaches to a **place**, which is the one thing here the reader
genuinely owns — that is why the apex ruling holds at all. Under this reading, a rendered *My Home*
is not automatically fatal.

⭐ **The tie-breaker is not a taste call, and it is measured.** Reading 1 is worth keeping even though
it over-fires, because **it is the only version of the rule that is a check rather than a judgment.**
The plan's F5 tripwire is `grep -rn '\bMy\b'` over `engine/viewer.template.html` and the apex page.
**Measured just now: 0 occurrences.** That zero is what makes F5 a *deterministic door* — any hit is
a defect, no reader has to adjudicate. Render *My Home* into chrome and the check returns legitimate
hits forever; the next `My settings` then hides among them, and a check that requires judgment on
every run is a check nobody runs. This project has already paid for that exact shape three times
(`CLAUDE.md`: *"a flag nobody reads is the same as no flag"*).

**So: reading 2 explains why the NAME is fine. Reading 1 decides where it may be WRITTEN.** Those are
not in conflict — they govern different acts, which is precisely the separation the re-run was asked
to make.

### 1b · Verdict, per surface

**Rendered** = written where a reader sees it. **Spoken** = said aloud and lives in the address.
**Absent** = the product name does not appear.

| # | surface | who reads it | verdict | why |
|---|---|---|---|---|
| 1 | **The address** — `myhome.place`, `<surname>.myhome.place` | everyone who opens it | ✅ **RENDERED — and this is the one sanctioned `my`** | Not a choice; ruled and registered. The name *is* the address, which is the elegant part of Paul's ruling: nothing extra to remember, teach or spell. |
| 2 | **Said aloud** — *"open my home dot place"* | Paul → his brother, Bob, anyone he onboards | ✅ **SPOKEN — the name's home, and the reason to have one** | Four syllables of ordinary words, zero spelling, and it is self-identical to the address. This satisfies researcher §1.1 (*sayable, not typeable*) better than any candidate in the A–E set did. |
| 3 | **Apex page body copy** (`myhome.place`, C4 2a′) | a stranger who typed the domain. **Nobody in the family** | ⛔ **ABSENT** | The drafted copy (greeting note § a) names nothing but Paul and describes what the thing does. A wordmark over its own URL is the portal shape — the page reading its address back at you. And it turns on a fact no agent has: **branded product, or a thing Paul builds for people he knows** (PRODUCT-ENGINE Q6, still open). **Absence is the only option that stays true under either answer**, and adding a wordmark later is one line while un-branding is not. |
| 4 | **Apex `<title>` / tab / bookmark** | Paul; anyone who bookmarks it | ✅ **RENDERED — as the address, not as a wordmark.** Recommend `myhome.place` | A title is a machine slot that must contain *something*; empty renders the URL anyway, and a bookmark and a home-screen icon both inherit it. Using the host keeps the token count at one, and a bookmark reading `myhome.place` is **the thing you would say out loud** — bookmark and spoken line converge. *Alternate: `My Home` — warmer in a tab strip, and it is the first place the tripwire goes soft.* |
| 5 | **An apex home-screen icon** | nobody today | ⛔ **ABSENT** | Nobody in the family reaches the apex; Mom never meets it (greeting note scope note). A slot with no reader is not a naming decision. |
| 6 | **Family door body copy** (`<surname>.myhome.place`) — the greeting + the chooser | Paul, Mom at two grants, later Bob's family | ⛔ **ABSENT** ⭐ **strongest absence in the table** | The ruled greeting is **Your home(s)** `[paul-stated, provisional]`. A product name above it puts **My** and **Your** in one eyeful, inches apart — which is falsifier b.2 written as a layout (*"is that your home or mine?"*). §4a's door-must-not-compete rule bites hardest here, because this is the surface immediately upstream of the room. |
| 7 | **Family door `<title>`** | Paul (who will hold several); Mom's bookmark at two grants | ✅ **RENDERED — as the host** (`kirschenbauer.myhome.place`); product name ⛔ **ABSENT** | It must disambiguate: Paul is administrator across families and *"Your homes"* in two tabs collides. The host disambiguates, makes **no identity claim** (see §2d — a bare surname as a page-level heading reads as a username; as an address it does not), and needs no second string maintained. *Alternate: the family label alone (`Kirschenbauer`).* |
| 8 | **Instance chrome** — `<h1>`, header subtitle | Mom, daily | ⛔ **ABSENT — settled, out of scope** | Stated once as the boundary: *Fernwood* and its anchored subtitle do not move. |
| 9 | **Instance `<title>`** — `{{IDENTITY:title}}` | Mom, daily; **and her icon derives from it** | ⛔ **ABSENT — and this one is `critical`** | Appending *· My Home* would (a) put a second rendered `my` on the one surface she actually meets, (b) change the string a re-added home-screen icon inherits, and (c) reverse row 8 through the back door. `{{IDENTITY:title}}` resolves to the **estate** name and must keep doing so. |
| 10 | **Mom's home-screen icon** — *"Fernwood Tracker"* | Mom | ⛔ **ABSENT — hers** | *Adopt their words, never improve them* (`cross-project/voice-and-stance.md` → Credit, don't thank). It exists in no tracked file; nothing here may reach for it. |
| 11 | **Worker prose + the three Guru model prompts** (`worker.js:2, :76, :638, :772, :1262`) | Mom, **through model output** | ⛔ **ABSENT — `critical`** | A product name in a prompt is a second proper noun the model may volunteer to her unprompted, on the one channel where the wording is not human-authored. That is F1 (*the door competes with the room*) arriving through the least-gated path. `:76` already flags itself as identity-not-canon; leave it naming the place. |
| 12 | **`README.md:1`** — today `# Church Mountain Property Tracker` **(verified)** | strangers on a public repo | ⚠️ **OPEN — Q3 below** | A **third** live product name, stale by two renames, wrong today independent of any ruling. |
| 13 | **`RELEASE_NOTES.md:3`** + the in-app *Recent updates* card | Mom | ⛔ **ABSENT** | *"What's changed at Fernwood lately"* names the **place**, correctly. This is instance voice on an instance surface. |
| 14 | **`index.html:7`** — `<title>Fernwood</title>` **(verified)** | effectively nobody (0 ms redirect stub) | ⛔ **ABSENT** — mirror row 9 | Only reachable by a bookmark made mid-redirect. Keep it equal to the instance title so it cannot drift into a fourth name. |
| 15 | **Paul's outbound** — email, texts, the apex's *Reach Paul ›* reply | whoever he is onboarding | ✅ **SPOKEN register — write the address, not a wordmark** | *"It's myhome.place — I'll open your door and send you the link."* Typing **My Home** as a brand in an email is a branding act he has not decided. Not blocking. |
| 16 | **`VOCABULARY.md` §3b row · plan and trail headers** | agents, Paul | ✅ **RENDERED — canon, not a user surface** | Step 6's three lines. Canon must name the thing to cite it; the cite-never-restate rule (§6) governs the wording. |

### 1c · The one-line verdict

⭐ **Spoken and addressed; rendered nowhere a reader meets it, except as its own address in two
`<title>` slots.** The name is a thing Paul says and a thing you type into a bar — never a wordmark
over anyone's cards.

---

## 2 · Question B — the family label's form ⭐ **AMENDED**

**The household chooses its own label. The surname is offered as a default, never derived as a rule.**
Q2's ruling (`bare-surname-lowercased`) stands as **the default it names**, not as the namespace.

### 2a · The rule, in order

1. ⭐ **AMENDED — start from the word that household chooses for its door.** Not their surname by
   rule, not a legal record, not a form field, not Paul's memory of it. **The offer carries a default
   so nobody meets a blank page** (§2c). *(`cross-project/voice-and-stance.md` → Credit, don't
   thank → **adopt their words, never improve them**.)*
   ⛔ **What I got wrong the first time, stated so it isn't repeated:** I applied that doctrine to the
   **spelling** of the word (*"the surname as that family spells it"*) and not to **the word itself.**
   Half-applying a ratified rule is how this corpus produces forks.
2. **Lowercase.** Stored, written and spoken lowercase everywhere — URL bar, `LIVE_BASE`, the mapping
   file, this spec. DNS is case-insensitive; writing it one way everywhere means no two surfaces can
   appear to disagree. ⭐ A chosen label may not be a proper noun at all, and this is why
   capitalisation never becomes a question: the host is lowercase and the `<title>` mirrors the host.
3. **Fold diacritics to the base ASCII letter** — `ö→o`, `é→e`, `ñ→n`, `ß→ss`. ⚠️ **Generalised from
   the surname version: the household's own written form wins over any fold we derive** (`Müller →
   mueller` if that is how they write it). Ask once; never derive over a stated preference.
4. **A hyphen already in the word survives as a hyphen.** `Smith-Jones` → `smith-jones`.
5. **Everything else that is not `a–z` or `0–9` is removed, not substituted.** `O'Brien` → `obrien`;
   `St. John` → `stjohn`; `Van Dyke` → `vandyke`. Removal beats hyphenation because a hyphen standing
   in for an apostrophe reads as a typo of a hyphenated name.
6. ⭐ **NEW, and the amendment opens it: a multi-word chosen label.** A surname is rarely two words; a
   place name often is. **Default is to close the space** — `Church Mountain` → `churchmountain` —
   because a hyphen has to be *spelled* over the phone (*"church dash mountain"*) and the ratified
   correction is **sayable, not typeable** (§2b.1). **Offer the hyphen if the closed form misreads**;
   it is their word and both forms are sayable. One question, at the same moment as the label itself.
7. **No leading or trailing hyphen** — strip if the fold produces one (invalid in a hostname).
8. **Length: the DNS limit (63) is the only cap.** ⛔ Do **not** import the researcher's *label-short*
   threshold — that governs a **home-screen icon**, which nobody reads on a hostname, and it is
   unmeasured anyway.
9. **The system never appends a digit, an initial, a state, or a year.** See collision.

**Worked:** `Kirschenbauer` → **`kirschenbauer`** · `Fernwood` → **`fernwood`** · `Rolader` →
**`rolader`**. Each 8–14 characters, one pronunciation, no spelling required.

✅ **Confirming the coordinator's point 2 exactly: rules 2–9 are unchanged and survive intact.** They
govern **how a chosen label is written**. Only rule 1's *input* moved, plus rule 6, which exists only
because rule 1 moved.

### 2b · Collision — ⭐ the amendment dissolves the harm, and I will not oversell how far

- **The register is authoritative; assignment is first-come and permanent.** `fernwood-private`'s
  family→subdomain mapping is the record. **The incumbent never moves.** Re-labelling a live
  household costs them an origin move — the single expensive act in this item.
- ⭐ **First-come stops stinging, and here is the mechanism.** *First-come only injures the second
  party when the thing claimed is something they had a claim to.* Under a surname namespace, the
  second Rolader household **had a claim to `rolader`** — it is equally their name — so first-come
  ranked two branches of one family. Under a chosen namespace, the second household is choosing from
  **its own words**, and has no claim on the first household's word at all.
- ⚠️ **The residual, stated honestly rather than dissolved by assertion.** Two households can still
  *want the same word* — two Rolader brothers who would both pick `rolader`. Someone is still second.
  **What changes is what that costs:** it becomes ordinary scarcity (*"that one's taken — what else do
  you call the place?"*) instead of a family ranking rendered in an address they open daily. That is a
  real improvement, not a complete removal, and the difference is the sentence Paul has to say.
- ⛔ **The system never derives a disambiguator.** Never `rolader2`, never `rolader-ga`, never a middle
  initial by rule. **An auto-derived suffix tells a household it is the duplicate, and the address
  says it to them every time they open it** — which, among relatives, is a status assignment inside
  one family.
- **There is no self-serve signup** — the apex says *"the doors here are opened by hand."* A collision
  always reaches **Paul** before it reaches a household, so no automatic rule is needed. ⛔ **He checks
  the register himself and comes back with a door; he never makes anyone contend for a name.**
- **Falsifier:** if a collision is ever resolved by a system-derived suffix, or if a household is ever
  told a word is *"already taken"* by a named relative, this rule failed.

### 2c · What a person is told — ⭐ REWRITTEN, because *"it's your last name"* stops being true

**The offer, at activation. This is the load-bearing string, and it carries the default so nobody
meets a blank page:**

> *"I'll set your door up as rolader dot myhome dot place — or if there's a name you'd rather have on
> it, that works too. Some people use their last name, some use what they call the place."*

⭐ **Why the surname goes first and it is not a preference:** every household **has** a surname; not
every household's place has a name. It leads because it is the option that always exists, and the
sentence offers both shapes without ranking them.

**If they ask what the label is:**

> *"It's whatever you call your place — yours is fernwood dot myhome dot place. That's your family's
> door; everything behind it is yours."*

**Shorter, in passing:**

> *"It's the word you picked, then the address. That's all it is."*

**One soft frame, offered only if they hesitate — never as a rule:**

> *"Something that'll still be true in ten years — that's usually the last name or the place."*

⛔ **What he must never say:** *your subdomain · your tenant · your instance · your account · your
profile · your site · pick a workspace name.* Each converts a door into a portal — `VOCABULARY.md`
§4's durable reason. **`estate` never reaches a user-facing surface**, including this sentence.
⭐ **And new with the amendment: never ask *"is that available?"*** Availability is signup grammar, and
this product opens doors by hand. Paul checks the register and returns with a door.

### 2d · The identity escalation, re-read under the amendment — ⭐ **it PARTLY discharges**

⚠️ **What I escalated on 09-03** (§5.1): a family label lands in Mom's URL bar, in `LIVE_BASE`, and in
the mapping file, so *the rule* forced a real surname into a permanent address. **That was a policy
question about a compulsion. The amendment removes the compulsion**, so the question genuinely
changes shape rather than merely deferring.

**Discharged:**
- ✅ **Nothing forces a surname into any address.** A household that does not want its name in a URL
  simply does not use it. Under `fernwood`, **there is no surname in the hostname, none in
  `LIVE_BASE`, none in either `<title>`.**
- ✅ **The CT half was already measured away** and is unaffected — C4 2a: one wildcard SAN
  (`*.myhome.place, myhome.place`), Total TLS off, `crt.sh` for `%.myhome.place` empty. A first-level
  label never enters a public log by name.
- ✅ **The stakes were lower than either of us was pricing them.** Measured tonight: `worker.js`
  resolves the estate from a **deploy binding**, and C4 ruled the estate is *chosen by grant, never by
  the address.* **The label gates nothing.** Guessing a label buys a login prompt, not data — so its
  cost is **social and expressive, not security.** That is precisely why *whose word is it* is the
  right axis and *what does it leak* is the smaller one.

**NOT discharged, and it is now smaller and different:**
- ⚠️ **A chosen label is not automatically identity-free — it trades *whose family* for *which
  property*.** `fernwood` names the place, and this repo is public, renders the street address 14
  times and carries `credit: "Paul Kirschenbauer"`. **For this household that is a strict improvement
  — it adds nothing that is not already public.** For a household whose place has no public name it is
  neutral. For a household that picks something identifying about itself, it chose knowingly. I will
  not claim a clean win the record does not support.
- ⚠️ **The mapping file still records household → label**, and for households that take the default it
  still records a surname. Unchanged, and it is a private file.
- ⭐ **The question the spine is left holding is much cheaper: not *"may we put a surname in a
  permanent address?"* but *"what does Paul offer as the default, given most households will take
  it?"*** That is a default-selection question, arguably his alone, and it no longer blocks a build
  step — which is a real reduction in what I escalated, not a re-labelling of it.

⭐ **What §1 still contributes, unchanged:** the label is rendered in the hostname and the two
`<title>` slots that mirror it — **and nowhere else in any copy this project authors.** Not as a
heading, not as a greeting, not in the shell, not in a prompt, not in release notes.

### 2e · ⭐ Testing the amendment rather than adopting it — including the one wrinkle put to me

**Verdict up front: I recommend it.** Four tests, and the third answers the coordinator's wrinkle 1.

1. ✅ **The strongest argument is Fernwood, and it is decisive.** This place **already has a name Mom
   uses**, predating all of this. A bare-surname *rule* would have **discarded an existing name in
   favour of a derived one** — which is the precise failure *adopt their words, never improve them*
   was ratified against, after the *"household systems" → "the house's own systems"* incident with the
   one reader whose stated fear is getting words wrong. A naming rule that overwrites a name in use is
   the same act with a different subject.
2. ⚠️ **The real cost is that a chosen label is an ASK, and asks are expensive here.** Measured in this
   repo: every affordance that asks Mom to answer is **0-for-30**; the one that simply moves her is
   5-for-5. **Two things keep it cheap.** It lands in *Paul's onboarding conversation*, not on a
   Mom-facing surface — the door is opened by hand either way. And §2c **carries the default inside
   the offer**, so it is a sentence to agree with, not a blank field. *(Mom is never asked this. She
   is not the household head at either of her places for this purpose, and she never types a URL.)*
3. ⭐ **Wrinkle 1 — a door that spans places. The constraint is real, and §1 already installed it.**
   Paul's door holds Fernwood **and** the condo, so naming it `fernwood` names the door for one of the
   things it asks you to choose between — **which is the exact defect Paul himself caught**
   (`VOCABULARY.md` §3b: *"Paul caught the mock branding it 'Fernwood' — the page was named for one of
   the things it asks you to choose between"*). **But that ruling governs what the page RENDERS, not
   what the host SAYS.** §1 row 6 already fixed the heading at *Your home(s)* and row 7 fixed the
   `<title>` to the host. **An address names a place; a heading claims to be its name.** So a chosen
   label is safe at one estate and at three *because the label never becomes a heading* — and it stops
   being safe the moment one renders. **That is a new falsifier and it is now §5.3.**
   ⚠️ **The honest residual:** an address named for one estate quietly implies a hierarchy (Fernwood is
   the main one; the condo is inside it). Mom has **no record of typing a URL, ever**, and reaches it
   by icon, so she effectively never meets it. But it is a real reason the *offer* leads with the
   neutral option and lets the household override — which is exactly the amendment's shape.
4. ⚠️ **A chosen word can over-claim in a way a surname cannot.** `rolader` asserts only *this is the
   Roladers*. A chosen word can name a place they later sell, or a family nickname one member dislikes.
   Surnames are stable; chosen words are not. **The mitigation is a soft frame, not a rule** — the
   ten-years line in §2c — and the two shapes that reliably satisfy it are the surname and a place they
   own. ⛔ Not a constraint on *choosing*; a sentence offered only if they hesitate.

⭐ **The cleanest proof the amendment is not just a way to avoid surnames: under it, Paul might still
pick his own.** His door spans two places, so `kirschenbauer` is the neutral label and `fernwood`
implies a ranking — while for a one-place household `fernwood`-shaped is obviously right. **A rule
could not have made that call in either direction.** It is Q4.

---

## 3 · Is Paul's Q3 condition satisfiable in copy terms?

> *"We can just go with my home for now, as long as we can save and address it later in a
> deterministic way and propagate that."*

### ✅ Yes — and the reason is §1, not the plumbing.

**Under the verdicts above the rename cost is approximately zero, because the name is rendered
nowhere except as its own address.** Count the slots: the apex `<title>` (which I recommend be the
host string, so it is not even a name slot), `VOCABULARY.md` §3b's row, and plan headers. Nothing
Mom reads. Nothing in the shell. Nothing in a prompt. A later rename is a domain decision plus two
canon lines — **the condition is met by absence, not by good machinery.**

### ⛔ And here is the finding, because it is a finding and not an obstacle

**If Paul chooses to RENDER the name, the condition stops being fully satisfiable — for three
reasons, only the third of which is fixable by building something.**

1. ⛔ **A rendered name is user-visible by definition, so a rename is user-visible by definition.**
   Paul's condition asks for *deterministic and propagatable*. The build chain delivers that:
   `build-viewer.py --check` proves byte-identity, so a one-key change provably reaches every
   surface. **But cheap-to-change is not invisible-to-change.** If *My Home* sits above Mom's cards
   for six months and then becomes something else, she sees a different word in her environment —
   a **fourth** change this quarter after the origin move, the icon, and the label. Determinism
   is achievable; invisibility is not, once rendered. *(This is why row 6 and row 9 are the two
   absences I would hold hardest.)*
2. ⛔ **Rendering disarms F5, and F5 is currently a clean check.** Measured: `\bMy\b` returns **0**
   in `engine/viewer.template.html` today. Render the name and the check returns legitimate hits
   forever. **Release condition if Paul renders it anyway:** F5 is re-specified to *"any `\bMy\b` in
   the template outside the `{{PRODUCT:name}}` token"* — i.e. grep the **template**, never the built
   artifact, so the tripwire keeps a hard zero. Without that re-spec, rendering silently retires the
   only mechanical guard on the portal failure.
3. ✅ **Fixable, and the plan already requires it: ONE engine-class key, one writer.** A new
   `{{PRODUCT:*}}` namespace in `tools/build-viewer.py`'s IDENTITY table plus its template tokens.
   ⛔ Never in `instance/fernwood.json` — that file names the **place**, and a product name there is
   a fork by construction. **The copy-side clause the plan does not state:** the key holds **the name
   only, never a sentence containing the name.** If a slot needs *"Welcome to My Home"*, the key is
   `name` and the sentence is assembled around the token — otherwise a rename means rewriting prose
   in N places.

⭐ **The evidence that clause is load-bearing is already in this repo, measured, and it is the same
failure one level up.** The plan's sweep found **at least seven hardcoded *"the Almanac"* strings
that are template LITERALS, not tokens** (`:6415`, `:14356`, `:19261`, `:19884`, `:19924`, `:20710`,
`:20718`) — instance voice baked into engine-class code, on a `must-not-diverge` item, and
`VOCABULARY.md` §4 bars *"Almanac"* as a portable noun. **A name typed into prose does not come back
out.** That is not a hypothetical about *My Home*; it is what already happened to the last warm noun
this project liked.

---

## 4 · Questions for Paul

```
Q1 · assent · Does the product name stay out of every surface a reader meets — spoken, and in the
     address, but never rendered as a wordmark?
   options: spoken-and-address-only | render-on-the-apex-page-only | render-in-the-family-door-chrome
   recommend: spoken-and-address-only — it is the only option that keeps F5 a hard zero (measured 0
     `\bMy\b` in the template today), the only one that stays true whether or not this becomes a
     branded product (PRODUCT-ENGINE Q6, still open), and the only one under which your own Q3
     condition is fully satisfiable — a name rendered nowhere costs nothing to change. Rendering it
     on the family door is the one I would refuse outright: it puts "My" and "Your home(s)" in one
     eyeful, which is falsifier b.2 drawn as a layout.
   caveat: if you render it anyway, two things ride with the ruling — F5 must be re-specified to grep
     the TEMPLATE outside the `{{PRODUCT:name}}` token (or the tripwire retires silently), and the key
     holds the NAME only, never a sentence containing it. The seven hardcoded "the Almanac" literals
     in the engine template are what happens when that clause is missing.
   blocks: plan steps 4, 5 and 6 — all reversible. ⛔ Blocks nothing irreversible. Until you rule: the
     apex page (C4 2a′) is buildable today with no product name at all, and step 8 pays regardless.

Q2 · assent · ⭐ AMENDED — is the label the household's CHOSEN word, with the surname offered as the
     default, and §2a's mechanics governing how it is written?
   options: chosen-with-surname-offered | bare-surname-as-ruled | chosen-with-no-default-offered
   recommend: chosen-with-surname-offered — you found the defect and it is not an edge case: the
     namespace was surnames, the thing named is households, and surnames are least distinguishing
     exactly where this spreads. Two Rolader households each CHOOSE, so neither is the duplicate, and
     first-come stops stinging because the second household never had a claim to the first one's word.
     The argument I weight highest is your own place: Fernwood already has a name Mom uses, and a
     surname RULE would have discarded a name in use in favour of a derived one — the precise failure
     "adopt their words, never improve them" was ratified against. `chosen-with-no-default-offered`
     is the one I would refuse: a blank page is an ask, and every ask-shaped affordance in this repo
     is 0-for-30. The default belongs INSIDE the offer sentence, not in a rule.
   caveat: it does not dissolve collision completely and I will not claim it does — two brothers can
     still both want `rolader`. What changes is the cost: ordinary scarcity ("that one's taken — what
     else do you call the place?") instead of a family ranking rendered in an address they open daily.
     ⭐ And it PARTLY discharges the identity escalation rather than deferring it (§2d): nothing now
     forces a surname into any address, and the label gates nothing — `worker.js` resolves the estate
     from a deploy binding, estate by grant never by address. What remains is smaller and is yours:
     what the DEFAULT should be, given most households will take it.
   blocks: plan step 3, and downstream C4 3c and C4 2d. ⛔ STILL THE IRREVERSIBLE ONE — the label
     lands in her URL bar once. Until you rule: `<family>` stays a placeholder in every tracked file
     and nothing is lost by waiting.

Q4 · framing · What goes on YOUR door — the one that holds Fernwood and the condo?
   options: kirschenbauer | fernwood | something-else-you-call-it
   recommend: kirschenbauer, and for a reason specific to your door rather than a preference for
     surnames — yours SPANS places. `fernwood` over a chooser that also holds the condo names the door
     for one of the things it asks you to choose between, which is the defect you caught yourself on
     the landing-page mock. It is safe here only because §1 keeps the label out of every heading; it
     still quietly implies Fernwood is the main one. For a one-place household `fernwood`-shaped is
     obviously right — which is the cleanest evidence the amendment is not just a way to avoid
     surnames: under it you might still pick yours.
   caveat: this is the one question where I am arguing against the Fernwood precedent that carries the
     amendment. Both can be true — a rule that discards a name in use is wrong, AND the name in use
     names one estate of two. If the condo never lands, `fernwood` is right and this reverses.
   blocks: nothing beyond Q2 — it is the first instance of Q2's rule, not a separate decision. Until
     you rule: Q2 can be ruled without it and `<family>` stays a placeholder either way.

Q3 · framing · `README.md:1` says "Church Mountain Property Tracker" — a third live product name,
     stale by two renames. What should it say?
   options: Fernwood | My Home | leave-until-the-engine-repo-splits
   recommend: Fernwood — the repo serves Fernwood's instance today, and `ENGINE-MANIFEST.md` says the
     engine/instance split is still in progress. Putting a PRODUCT name on this README claims the repo
     IS the product, which is not yet true; naming the instance is true today and stays true after the
     split, when the engine repo gets its own README and its own name.
   caveat: this is a public repo, so `README.md:1` is the one line in §1's table a stranger reads
     without being invited. That is an argument for it being right, not for it being branded.
   blocks: plan step 8 (the four hand-edit sites), which is reversible and pays regardless of Q1.
     Until you rule: all three names stay live in the repo, and `RELEASE_NOTES.md:3` and
     `index.html:7` (both verified today, both naming Fernwood correctly) stay as they are.
```

---

## 5 · Falsifiers this trail adds

Both existing sets stand (`content-steward` §4b, greeting note § b, and the plan's F1–F6). Two here
are new and both attach to §1:

1. ⛔ **A `\bMy\b` appears in `engine/viewer.template.html` that is not the product-name token.** The
   baseline is **0, measured today** — so this is a deterministic door, not a judgment call, exactly
   as long as Q1 rules `spoken-and-address-only`.
2. ⛔ **Paul finds himself typing the product name into an email, a card, a prompt or a heading** to
   explain what a link is. That would mean §1's absences are starving a real surface, and the right
   remedy is to render it in **one** named place — not to let it leak into several.
3. ⭐ **NEW with the amendment — the family label appears as a HEADING anywhere.** A chosen label is
   safe on a door that spans several places *only because it never renders as the page's name*
   (§2e.3). The moment `fernwood` sits above a chooser that also holds the condo, it is the
   landing-page defect Paul caught himself. Measured the same way as F5 — a grep of the family door's
   markup for the label outside `<title>` and the address.
4. ⚠️ **A household is told a word is "already taken," or a label ends in a system-derived suffix.**
   Either means §2b's collision rule failed in the way that costs the most — among relatives, in an
   address they open daily.

*(Not a falsifier: nobody ever saying the name. That is the plan's F3, carried, and it belongs to the
09-02 "call it nothing" position which has still never fired.)*
