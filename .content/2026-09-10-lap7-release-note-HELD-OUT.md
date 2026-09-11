# Lap 7 — THE RELEASE NOTE, HELD OUT. Draft entry · ribbon line · confirmation checklist

- **kind**: content draft — L4 of `.plans/2026-09-10-build-description-chain-DESIGN.md`
- **shape**: `.content/2026-09-10-release-notes-from-commitment-PROPOSAL.md` (§1 the shape · §1d what a
  note may never claim · §3 the falsifier). Nothing here re-decides that proposal.
- **commitment read**: `cycle/release/CYCLE-LOG.md` § Lap 7 — Beat 6 rows **D C B A E**, the exclusion
  list, the two-answers sub-section and § THE ENVIRONMENT MODEL · `.plans/2026-09-10-lap7-build-PLAN.md`
  §1, §2 (A1–A10), row D (D1–D8), row C (C1–C7), row B (B1–B15), row A (A1–A22), row H, **§6 out of this
  build** · `.ux-reviews/2026-09-10-lap7-design-closure.md` (45 rows, its one **NEEDS-PAUL**) ·
  `RELEASE_NOTES.md`'s 2026-09-10 entry (the sibling) · `tools/build-release-notes.py:35–70` (the parser)
- **charter**: `~/.claude/content-principles/fernwood.md` + `cross-project/voice-and-stance.md`.
  `VOCABULARY.md` §2 and §3i bind: no `estate`, no `environment` / `deployment` / `production`, no `QA`,
  no `legacy`, no `sha`, no `Worker`, no `beat`. The interface names **homes** and **places**.
- **audience**: a household reader on their own account — tonight that is **Paul at his own home**.
  ⛔ **Not Mom.** Her Fernwood is frozen and nothing in lap 7 touches it; this note does not reach her.
- **surface**: `RELEASE_NOTES.md` → `tools/build-release-notes.py` → the *Recent updates* card
- **tone register**: plain-report — someone who has just been let back into their own account and wants
  to know what is true now. Not celebratory; nothing here grades the reader's reaction.

> ⛔⛔ **NOTHING IN THIS FILE IS APPLIED.** `RELEASE_NOTES.md`, `viewer.html` and
> `engine/viewer.template.html` were not edited. The note is **held out by design** — §4's checklist is
> the only thing that moves it, and the last line of that checklist is Paul's.

---

## ✅ APPLIED 2026-09-11 — §4 run against `87c7aae`, CLEARED and DEPLOYED (`paul` · `home`)

`RELEASE_NOTES.md` now carries `## 2026-09-11 — Signing out, signing back in, and changing what you
said at setup`. **That file is the only one edited** — `viewer.html`, `engine/viewer.template.html`
and the ribbon were not touched; coordination rebuilds the viewer. Below, per §4a, what each gate
returned. Evidence: `cycle/release/CYCLE-LOG.md` § GATE ① RUN at `87c7aae` (5/5 seats, 15 of 15
journey-runs zero failed actions, zero pageerrors), § BEAT 11 — PAUL CLEARED, § BEAT 12 — DEPLOYED,
and `.content/walks/87c7aae-walk-read.md`.

- **Bullet 4 — J2 dropped from its gate:** J0 (the cold door) and J3 (the landing) cover the shelf at
  `87c7aae`; **J2 is UNWALKABLE by model** (an unfinished record cannot exist without an estate),
  ruled tonight, and the gate's own coverage line prints it — so the bullet is gated J0 + J3.
- **Bullet 4 — one clause CUT:** *"one home, straight into it; more than one, to the list."* No seat
  holds two homes and the 09-10 entry says a second home on one account is **not in the build**, so
  the branch is unreachable and cannot be described. Shipped as *"Signing in takes you straight to
  your place."*
- **Bullet 5 — one sentence CUT:** *Not quite* is **not a walked stop**. `journey-walk.journey_founding`
  goes `click:#go2 → F08-read-back → click:#ok1 → F09`; nothing clicks *Not quite*. The read-back half
  (F08/F09, four seats founded, strict refused) ships; the restore claim does not.
- **Bullet 6 — reduced to what L15 proves.** L15 asserts the three rows exist and each carries an
  `Edit`; it never follows one. The round-trip sentences (*"where it takes you differs… ends back on
  this card with that line rewritten"*, *"says what moved with it"*) were **cut, not softened**.
- **Bullet 7 (row D) — the DO bullet is CUT; a not-yet replaces it, and here is why the replacement is
  true of the deployed build.** The rescue claim (*"your note went through"*) has no record behind it:
  D7 runs after Paul's next load. What **is** verified is the destination — beat 12 deployed
  `deploy-worker.sh --env paul` (health OK, env=paul) and `myhome-paul` serves `87c7aae` with
  post-deploy covered (served sha · worker /health · worker estate `est-d93508` · payload blob
  matched). D8 traces the flush end to end in source (`flushOutbox` first in `MomQueue.start()`; the
  note's own `ts` stamped before `outboxAdd`; `outboxRemove` only after a verified 2xx). So *"has
  somewhere to send… goes the next time you open the app"* describes the build that is live, and its
  failure mode **keeps the words** rather than losing them. No past-tense claim about his note is made.
- **Bullet 2 — shipped with the timing half unverified, disclosed.** L12's byte-identity half is
  walked; its **timing** half is unchecked by ruling (a browser round trip cannot measure it). The
  bullet makes no timing claim, so the unverified half backs no sentence in it. Flagged, not hidden.
- **Bullet 11 (ranked-but-empty) — §4c resolved to SHIP.** `onboarding/index.html:822–825` shows the
  promise **withdrawn** in this build, which is the branch that says ship as drafted. Re-tensed from
  *"not in this build"* to *"not settled yet"*, which is what it actually is.
- **Added, per the chain act:** the **Almanac → Journal** engine default (ruled 2026-09-11, TIER 2 · 20;
  `build-viewer.py:109–112`), worded so it is **true at Fernwood too** — the note is identical at every
  household, and *"a place that already has a word of its own for it keeps that word"* covers the
  instance that declares `journalTile`. And the **looping *Create your account ›*** link (W2,
  `onboarding/index.html:384–385`), which a person absolutely notices: from the sign-in screen there is
  no path to an account at all. Named with the path that does work.
- **Row C still has no bullet** (§1) and the **ribbon line stays here, out of the note** — `instance/paul.json`
  now declares `ack` **and** `questions` absent (lines 39–40), so the §3b leak is closed and the ribbon
  renders nowhere; the per-household seam is lap 8. ⭐ §3b's *"paul.json does NOT declare ack absent"*
  was true when written and is **no longer true at `87c7aae`** — corrected here rather than left standing.

### ⛔ ONE FINDING FOUND WHILE APPLYING, and it would have shipped to every household

**`renderNoteMarkdown` (`engine/viewer.template.html:15775–15778`) handles `**bold**` and NOTHING
ELSE.** Single-asterisk italics render as **literal asterisks** on the card. The draft in §1 italicised
nine control names — *Can't get in?*, *Set up my place*, *Not quite*, *Where it is* … — every one of
which would have printed with visible `*` characters. All converted to **bold** (the 2026-09-01 entry's
own precedent) or to plain text. **The entry title is `escapeHtml`'d with no markdown at all** — no
emphasis of any kind may appear in a title.

### Counts as shipped

**7 do · 2 no-longer · 4 not-yet = 13 bullets** (the sibling runs 6). If Paul wants it shorter, the two
I would still cut first are the **email-shown-back** bullet and the **one-refusal-sentence** bullet, in
that order — **not** the row-D one, which is the one a reader most needs.

---

## 0 · The one thing the shape asks for that the commitment cannot supply

The proposal's §1a says the **title is derived** — from the committed row's `note:` field — and only the
bullets are authored. **Lap 7's beat-6 table has no `note:` field.** Its columns are `committed` and
`done means`; the same gap the proposal already flagged for lap 5 (*"Ids are blank because lap 5's
committed rows carry none — that is exactly what P1 fixes"*).

So the title below is **AUTHORED, not derived**, and it is marked as such rather than presented as a
derivation that happened. Two consequences a reader of this file must not skip:

1. **The charter's own falsifier (§3c) does not bite yet.** *Read the title and the first bullet as one
   sentence; if they disagree the `note:` field is wrong* presumes a `note:` field. Tonight there is
   nothing to be wrong, so the check degrades to ordinary authorship review — weaker, and it should be
   said out loud rather than performed.
2. **The §3a falsifier still works**, because it asserts an **absence**: a committed row with no passed
   walk must not have its title in `RELEASE_NOTES.md`. That holds with an authored title too.

⭐ **Recommendation, one line:** when P2 lands the `note:` field, backfill it for lap 7's rows from the
title below rather than re-authoring — otherwise the first derived title in the project's history will
disagree with the note that actually shipped.

---

## 1 · THE DRAFT ENTRY

**How to read the tags.** Every bullet carries `[walk: <what must pass> · row <D|C|B|A>]`. The tag is
**working apparatus, not shipping bytes** — ⛔ `build-release-notes.py:53–66` appends every continuation
line to the open bullet, so a tag left in place **renders on the card**. Strip the bracketed tag and
nothing else changes.

**Ordering is do · no-longer · not-yet, as bullet ORDER and never as sub-headings** (§1c — a
sub-heading either vanishes or is swallowed, and the script's bullet count looks right either way).

```markdown
## 2026-09-1x — Signing out, getting back in, and a note that goes through

- **You can sign out of this phone.** A new control at the foot of your account page, with a
  second tap to confirm, because signing back in is not always a thirty-second job. It clears
  who you are on this device and leaves the device otherwise alone — if you read at the larger
  text size, it is still larger when you come back. [walk: J8 · row B]
- **If you cannot get in, there is one door for it.** *Can't get in?* sits under the sign-in
  button, opens where you are standing, and asks for one thing: your email address. It covers a
  forgotten username and a forgotten password together, because from outside a locked door
  those feel the same. Signed in, the same request lives on your account page. [walk: J8 · row B]
- **Your email address is shown back to you.** On your account page, under *How to reach you* —
  the address on file, or that there is none, or that it could not be read just now. It is
  shown there; it is not changed there. [walk: J8 · row B]
- **Opening the app with nobody signed in gives you two named doors** — *Set up my place* and
  *I've been here before* — instead of a screen that assumed you were holding an invitation
  link. Signing in then takes you where your homes are: one home, straight into it; more than
  one, to the list. [walk: J0 + J2 + J3 · row A]
- **The address you type is read back to you before anything is written.** The same card turns
  around and shows you what it heard, and nothing is made until you say that is it. *Not quite*
  puts every word you typed back exactly where it was, because nothing was written to undo.
  [walk: J0 · row A]
- **The three lines of What you told me can be changed.** *Where it is*, *How to reach you* and
  *What I'll build first* each carry an **Edit**. Where it takes you differs — the address goes
  back to the address step, how to reach you to your account page, what you'll build first
  opens on the card itself — but every one of them ends back on this card with that line
  rewritten. Change the address and it says what moved with it. [walk: J8 · row A]
- **What you wrote on this phone had nowhere to send, and the app said it had saved anyway.**
  A note, a question to the Garden Guru, an answer to a card — all of it goes to one place, and
  on this phone that place was not connected. It is now. Nothing was lost while it was not:
  anything waiting goes through the next time you open the app, carrying the hour you wrote it
  rather than the hour it arrived. [walk: none — the record check at the deployed origin · row D]
- **A sign-in that does not work says one thing now.** The same sentence whether the name is
  unknown, the word is wrong, or the credential belongs to a different home: it tells you the
  door did not open, and points at the way back in, instead of asking you to work out which
  half you got wrong. [walk: J8 · row B]
- **A post-office box is turned down at the address step, before a place is made.** It says so
  on the screen you are standing on, with nothing written and your other answers intact — and
  the feedback button on that same screen is there if a box is genuinely the only address the
  place has. [walk: J0 (strict) · row A]
- **Not in this build:** changing your email address here, one sign-in that reaches every home
  you are part of, inviting anyone, or joining a home somebody else set up. None of the four
  are here yet.
- **Also not in this build: a card you left out of your ranking is hidden rather than shown
  empty.** How that should read has not been settled, and it is being decided before it is
  built rather than after.
```

**Counts:** 9 bullets a walk must stand behind (**6 do · 3 no-longer**) + **2 not-yet**. Long against
its sibling (the 2026-09-10 entry runs 6). If Paul wants it shorter, the two I would cut first are the
email-shown bullet (it is the thinnest *do*) and the sign-in-refusal bullet (the person-visible change
is that it says **less**, which is right and hard to make interesting) — **not** the row D bullet,
which is the one a reader most needs.

### Provenance — what each bullet is owed

| # | bullet | commitment source | class | gate |
|---|---|---|---|---|
| 1 | sign out of this phone | row B; plan **B8**, **B13**; closure 25–27 | do | J8 · L04–L07 |
| 2 | one door for *can't get in* | row B; plan **B6**, **B9**, **B12**; closure 28–30 | do | J8 · L11–L12 |
| 3 | email shown back | row B; plan **B10**; closure 19 | do | J8 · L03 |
| 4 | two named doors + the landing | row A; plan **A1**, **A2**, **A3** (⛔ depends on **B1**); closure 1–3 | do | J0/J2 · L08–L09; J3 · L14 |
| 5 | the address read back | row A; plan **A7**, **A10**, **A11**; closure 8, 11, 12 | do | J0 · F08/F09 |
| 6 | the three lines can be changed | row A; plan **A14**, **A15**, **A16**; closure 16–18, 20 | do | J8 · L15 |
| 7 | nowhere to send → somewhere | row **D**; plan **D1**, **D5–D8**; TIER 1 · 45 / instance 42 | no-longer | ⚠️ see §4b |
| 8 | one refusal sentence | row B; plan **B5**, **B11**; closure 31 | no-longer | J8 · L10 |
| 9 | the box turned down at the step | row A; plan **A8** + **B4** (the authority); closure 10, 10a | no-longer | J0 strict + `walk-founding.py` |
| 10 | *not in this build* (four) | beat 6 exclusions + plan §6 — see §2 | not-yet | none — it claims nothing |
| 11 | the ranked-but-empty card | beat 6 exclusion **D6**; closure 43; plan §6 | not-yet | none — ⚠️ see §4c |

### ⛔ Row C has no bullet, and that is the finding, not an omission

G6 telemetry ships in this candidate and **a person cannot see any of it.** Its own *done means* is a
tool — `tools/read-glance-order.py` (plan **C7**) — read by us, not by them. §1d·7 and the *describe,
don't grade* rule both forbid dressing instrumentation as a benefit, and there is no honest sentence
here that is not *we are now watching which cards you open*, which is a different conversation and
**not one a release note may open on its own.** ⭐ Row C belongs in the lap's own record, not on this
card. If Paul wants the watching disclosed to a household reader, that is authored copy with its own
gate, and I will draft it — it is not a bullet.

### Held out of the held-out note — two candidates that would be lies tonight

> *"**One sign-in reaches every home you are part of.**"* — ⛔ **LAP 8**, ruled. It is in the *not in
> this build* bullet instead, where its absence is the claim.

> *"**Your account colour and your place's colour are separate now.**"* — ⛔ **built (plan A17), not
> walked as a person would notice it.** The gate is *"a walk that changes the account colour and
> asserts the place colour does not move"* — an assertion, not a journey stop. It enters the note the
> lap a seat walks it, or the lap Paul says he saw it. A reader cannot follow this bullet into an
> action today, which is exactly §3b's test for what is not a do-bullet.

---

## 2 · THE *NOT IN THIS BUILD* BULLETS — verbatim in intent from the exclusions

⛔ **Nothing here is re-decided.** Each row is the ruling, quoted, then the person's words for it.

| the exclusion, as ruled | in the note as |
|---|---|
| **the single-origin sign-in door — LAP 8** `[paul-ruled: "a single sign-in page that redirects to everywhere it needs to go, not individual sign-in pages"]` (TIER 1 · 41/46) | *"one sign-in that reaches every home you are part of"* |
| **the email EDITOR** — *"display-only this lap (B10); the editor in lap 8. NEEDS-PAUL — the closure's only one. Named 'not in this build' on the release note rather than left unsaid"* | *"changing your email address here"* |
| **§ INVITE & JOIN** — *"groom, not build"* | *"inviting anyone, or joining a home somebody else set up"* |
| **D6 · ranked-but-empty cards** — *"needs Paul's Q1 and a user-researcher read… only if ruled and built in time, else named as NOT in this build on the release note"* | its own bullet (11) |

**Deliberately NOT given a bullet, each with the reason** — §1d·6 forbids padding, and a not-yet a
reader has no word for is furniture:

- **§ ADDRESS VALIDATION** (*groom, not build*) — bullet 9 already tells the reader the only check that
  exists. A second line saying *"and nothing else is checked"* invites a worry the product has not
  earned. ⚠️ If Paul wants it said, the honest wording is *"the address is looked at for a box and
  nothing else"* appended to bullet 9.
- **D9 · the glance consolidation** (*design after G6 lands*) — a reader has no name for it. Naming it
  would be the card describing our roadmap to itself.
- **Zones preload** (*parked until Mom has founded her own Fernwood and is ready*) — parked on a
  person, not on a build. It is not this log's business.
- **The composer's split control** and **`Almanac → Journal`** — both are **copy**, still open
  (closure 42, 44; the copy review's open questions 2 and 4). A noun that has not been ruled cannot be
  announced. ⚠️ **If Paul rules the noun this lap, the note needs a bullet** — a card changing its name
  is the most visible thing in the build and would ship unannounced. See §5.
- **G3 (a close signal)** and **the post-deploy blob compare** — invisible to a person either way.
- **Row E, the teardown** — ours, and it touches nothing a household reader has.

---

## 3 · THE RIBBON LINE — and a blocker that must be cleared before it can ship

**What it traces to.** Row **D** is the only row in the commitment that traces to a person's own input:
**TIER 1 · 42** — the note Paul typed in his own app on 2026-09-10 ~9:05 PM ET, which printed *Saved ✓*
against a door that was not there and has been sitting in that phone's outbox since. Nothing else in
lap 7 was caused by a reader; rows A, B and C are ours, and by the 2026-08-04 doctrine they belong in
*Recent updates* and nowhere else.

### 3a · The line, in the card's own grammar

```jsonc
"titlePhrase": "what your note changed",
"changes": [
  {
    "text": "This phone had nowhere to send what you wrote, so your note sat here saying it had saved. It has somewhere to send now — your note went through dated the night you wrote it, and so did everything else that was waiting.",
    "card": "card-fieldnotes"
  }
],
"links": [ { "phrase": "your note", "card": "card-fieldnotes" } ],
"closing": "",
"closingCard": null,
"arrivedAt": "2026-09-11T01:05:00.000Z",   // ⚠️ the real ts of his note — read it, don't retype it
"arrivalRef": "<the outbox record id, once it lands>",
"acknowledgedThrough": "<a minute past the newest arrival at this household>",
"channels": ["observations"]
```

Rendered, that is: **"Wednesday, September 10 — what your note changed:"** over the one line.

**The four card rules, checked:**

- **Rule 1 — the heading may only promise the verb the body delivers.** Read as one sentence: *what your
  note changed: this phone had nowhere to send what you wrote… it has somewhere to send now.* His note
  **caused** the fix (it is what surfaced TIER 1 · 42), so `changed` is the correct one of the three
  shapes — not `settled`, and not the no-list case.
- **Rule 2 — the boundary.** One bullet, and it traces to him. Everything else in lap 7 is ours and is
  in the note above. ⚠️ **The standing bridge is left EMPTY here on purpose** and this is a judgement
  Paul should overrule if he disagrees: *"Everything else new is in Recent updates ›"* is a completeness
  claim, and on **his** household the *Recent updates* card is the product log — it is true. I have left
  it empty only because the bridge was authored for Mom's card and I have not seen it render at another
  household. **If it renders, restore it** — the card is allowed to be short, and the bridge is what
  makes short honest.
- **Rule 3 — `closing` may never be unrelated.** Nothing else of his is outstanding, so it is empty.
- **Rule 4 — four independent slots.** Only `titlePhrase` + `changes[]` fire.

**And the rules from CLAUDE.md that bite here:** *credit, don't thank* — there is no thank-you, and the
line names **what he gave** (a note) and what it changed. *Adopt their words* — "note" is the app's own
word for the thing and his. The **everything-is-changeable** clause does **not** fire: nothing of his
needs correcting, and attaching it would invent a doubt. The **close is not repeated** — the previous
refresh closed on the bridge; this one does not close at all.

### 3b · ⛔⛔ THE BLOCKER — measured tonight, and it is not this line's fault

**`MOM_ACK_DATA` is a CONCRETE literal in `engine/viewer.template.html:12022–12223`, not an
instance-supplied value.** There is no `{{…}}` seam for it, the way there is for identity and the place
log. The only control is the instance's `absent` list, which `build-viewer.py:136` records was added on
**2026-09-06** for exactly this reason — *"Mom's ack ribbon and her confirm cards rendered on EVERY
household (a stranger read…)"*.

**Measured at HEAD, in the instance files:**

| instance | declares `ack` absent? | consequence |
|---|---|---|
| `instance/home.json:39` | **yes** | no ribbon |
| `instance/qa.json:39` | **yes** | no ribbon |
| `instance/paul.json:22–40` | ⛔ **NO** — and `questions` is missing from the list too | the engine's literal renders — **Mom's refrigerator acknowledgment, addressed to her, on Paul's screen** |

So the ribbon can render at Paul's household today **only because it is carrying somebody else's
attribution.** Two things follow, and both are Paul's to rule:

1. ⛔ **Authoring the line above into the engine template inverts the leak rather than fixing it.** It
   would make *Paul's* attribution the engine default — rendering at any household that does not
   declare `ack` absent. An attribution card whose payload lives in the shared engine can only ever
   hold **one person's** attribution, and it will be whoever wrote last.
2. ⭐ **The fix is a seam, not a wording change:** `ack` becomes an instance-supplied value like
   `identity` and `{{PLACE_LOG}}`, so each household's card holds that household's own. That is
   engineering-partner's and it is **not in lap 7's commitment** — which is why this line is held out
   here rather than handed to the build window.

⚠️ **Separately and immediately:** `instance/paul.json` omitting `ack` looks like an omission rather
than a decision — it carries no `_note`, and its two siblings both declare it. Whatever happens to the
seam, **that omission should be ruled on tonight**, because it is live. It is the 09-07 gauge class
again: another household's record on a stranger's screen with no needle in it to catch.

### 3c · The link target, and the one thing I could not verify

`card-fieldnotes` is the card his notes live on (`viewer.html:7068`) and is the right destination for
*"your note"*. ⛔ **I did not verify that a note sent through the composer renders back on that card at
his household** — if it does not, the phrase links to a promise the card cannot keep, and the honest
move is to drop the `links` entry and leave the change text unlinked rather than to soften the wording.
**Check it on the deployed build before the ribbon ships.** ⚠️ And the card's own name is unsettled
(closure 44) — if the noun moves this lap, this link's phrase does not change, but the card the reader
lands on will be wearing a different name.

---

## 4 · THE CONFIRMATION CHECKLIST — what must pass before each bullet may ship

**The rule, stated once:** a bullet ships when a seat has walked it **at the deployed sha** and the walk
passed. Evidence expires when the build moves (`release-gate.py` is per-sha). A bullet whose walk has
not passed is **cut from the entry**, never softened into a maybe — §1d·1.

### 4a · Per bullet

| # | may ship when | if it does not pass |
|---|---|---|
| 1 | J8 stops **L04–L07** pass: the button is not covered at rest, the inline confirm appears, identity keys are gone, **A+ is still set**, and the lede is the signed-out one | cut the bullet. ⚠️ If only the **lede** half fails, cut the final sentence, not the bullet |
| 2 | J8 **L11** (the block reveals inline) **and L12** (known and unknown email → byte-identical, equally timed) | cut. ⛔ L13 is a human stop by design — it is **not** evidence and the walk must say so |
| 3 | J8 **L03**: the field renders in one of its three states and is **not simply absent** | cut — and if it is cut, the *not in this build* bullet keeps *"changing your email address here"* anyway |
| 4 | **L08** (cold origin paints the door) + **L09** (two named doors) + **L14** (the landing branches on the count) | the two halves are separable: cut the sentence whose stop failed. ⛔ **L14 depends on B1** — if the session response still reports one home for everyone, the landing sentence is false |
| 5 | J0 **F08/F09**: the read-back renders in place, *Not quite* restores every typed value, **no feedback POST fires** | cut |
| 6 | J8 **L15**: each `Edit` returns to the card with that line rewritten | cut. ⚠️ If only the address editor lands, cut the last sentence (*"says what moved with it"*) with it — it is A15's, not A14's |
| 7 | **see 4b — this one has no seat journey** | |
| 8 | J8 **L10**: the two failure kinds produce the byte-identical string, and a `signin_failed` record with **no** personId | cut |
| 9 | a strict-seat PO-box walk refuses at the address step **and `walk-founding.py` shows no new place minted** | cut. ⛔ Do not ship it on the page check alone — B4 is the authority, and a page-only refusal is the thing D1a ruled against |
| 10 | — | it claims nothing; it ships if the entry ships |
| 11 | — | ⚠️ see 4c |

### 4b · ⛔ Bullet 7 is the one bullet no journey covers, and it is the headline

The commitment's own *done means* for row D is **a record check, not a walk**: *"a capture from the
condo's app reaches the condo's Worker and the record shows it."* Plan **D7** is the falsifier and
**D8** states plainly that the flush needs no act from Paul — it happens on his next load.

**So bullet 7 ships when, and only when:**

1. `watch-feedback.py` at his origin shows **his note, carrying its own 2026-09-10 timestamp** (not the
   flush time) — that is the whole claim, and the timestamp is the half that proves the outbox
   preserved it rather than a new note being written; **and**
2. `/estate/` tells *refused* from *unreachable* (plan D3/D4), which is the second half of the row's
   *done means*.

⚠️ **If the note does not appear**, plan D8 names the two live explanations — storage cleared, or the
POST refused — and they are distinguishable. ⛔ **In both cases the bullet is cut, not reworded.** The
sentence *"anything waiting goes through the next time you open the app"* is a promise about **his own
words**, and this repo's oldest rule is that capture must not lie. A bullet that claims a rescue that
did not happen is worse than no note at all.

### 4c · Bullet 11 has a condition that is not a walk

Plan §6 and closure 43: while D6 is unbuilt, `onboarding:777`'s promise (*"nothing is switched off or
hidden because you left it out"*) is **false**, and the ruling is that **the sentence must be
WITHDRAWN, not left standing**. So:

- **If the sentence is withdrawn in this build** → ship bullet 11 as drafted.
- **If it is left standing** → bullet 11 ships **and** the release note is now the only place the app
  admits the contradiction, which is the wrong place for it. ⛔ Raise it, do not paper over it.

### 4d · Entry-level checks, before the whole thing goes in

1. **Read the whole card aloud, top to bottom** (charter, 2026-08-24 — the check that catches what
   line-by-line review cannot). Title and first bullet as one sentence.
2. **The could-be-anyone test, inverted for this log** (§1d·4): the note may **not** name a place. Grep
   the entry for `Fernwood`, `Jasper`, `Church Mountain`, `condo`, `pond`, `laurel` — the anchor here is
   the reader's own record (*your account*, *this phone*, *your homes*), never a property.
3. **The vocabulary check**: no `estate`, `environment`, `deployment`, `production`, `QA`, `legacy`,
   `sha`, `Worker`, `instance`, `beat`.
4. **Strip every `[walk: …]` tag.** The parser will otherwise render them on the card.
5. **Paste into `RELEASE_NOTES.md` above the 2026-09-10 entry, set the real deploy date**, then
   `python3 tools/build-release-notes.py`, then **diff the payload** — not the count. The 2026-08-01
   truncation bug survived because *"a count is not a content check"*.
6. **The §3a falsifier, the absence direction**: for every committed row with no passed walk, its title
   must **not** appear as a `## <date> — <title>` heading. With one title for five rows this lap, the
   operative form is per-**bullet**: a cut bullet leaves no trace in the file.
7. **Ship the note in the same push as the ribbon**, if the ribbon ships — the bridge's completeness
   claim rests on it.

### 4e · ⭐ The one line Paul confirms (chain act 12)

Nothing above moves the note into `RELEASE_NOTES.md`. This does:

> **"I've read the whole card top to bottom. Every line of it is true of the build I just deployed —
> ship it."**

⚠️ If he wants to change a bullet, it comes back here and is re-confirmed. ⛔ A bullet edited to make a
title true is the one move the charter names explicitly and forbids.

---

## 5 · WHAT THE COMMITMENT LEAVES ME UNABLE TO DESCRIBE

Five, and the first two are the ones I would put in front of him tonight.

1. ⛔ **Whether a household-specific ribbon can ship at all** — §3b. `MOM_ACK_DATA` has no per-instance
   seam, so there is exactly one attribution card in the product and it currently holds Mom's
   refrigerator, rendering at Paul's household because `instance/paul.json` does not declare `ack`
   absent. **Until the seam exists, the ribbon line in §3a cannot ship without making Paul's
   attribution the default for everyone.** Not in lap 7's commitment; needs Paul's word on whether it
   joins, and needs the `paul.json` omission ruled on either way.
2. ⚠️ **`Almanac → Journal`** (closure 44, copy review open question 2). It is out of this build as a
   *build* item and unruled as a *copy* item — but if the noun moves, a card the reader uses changes
   its name, which is the single most visible thing in the lap, and **the note above does not mention
   it**. Rule it or defer it explicitly; do not let it ship unannounced.
3. **Row C, disclosed or not** — G6 records which cards a person is served and which they open. I have
   given it no bullet (see §1), which is the correct release-note answer and **not** an answer to
   whether a household reader should be told at all. That is authored copy with its own gate.
4. **The two colours (A17)** — built, and a person can see it, but no walk covers it as a person would
   notice. It is held out above. One seat assertion, or one sentence from Paul that he saw it, and it
   becomes a bullet.
5. **Whether bullet 7's rescue actually happened** — §4b. I have drafted the sentence that describes a
   good outcome; I cannot know tonight whether it is the outcome. This is the bullet most worth writing
   and the one most likely to need cutting.

**Two principles I would propose out of this pass — NOT written to the library, pending Paul's word:**

- **`Fernwood`** — *an attribution surface needs a per-reader seam before it has per-reader copy.* A
  card whose whole job is saying **you caused this** cannot live in a shared build: the first
  household-specific sentence written into it is addressed to one person and shown to everyone. Origin:
  §3b, measured tonight. (Sibling of the 09-06 `absent`-list fix, which treated the same defect as a
  visibility problem rather than a seam problem.)
- **`cross-project` candidate** — *instrumentation is not a feature and never gets a bullet.* If the
  only honest sentence for a shipped item is a description of what the system now watches, it does not
  belong in a changelog; it belongs in a disclosure with its own gate. Origin: row C. **Second-project
  evidence not in hand** — hold as a candidate.
