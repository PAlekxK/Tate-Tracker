# Content read — build `87c7aae`, lap 7 gate ① content clause

content-steward, 2026-09-11. Fifteen counted runs at `87c7aae` (QA origin), three each for
**mom · owner · strict · wide-eyed · handover** (J0 founding · J3 returning · J8 lifecycle).
Read: every counted `REPORT.md`, the fold frames for the screens named below, and the source
copy in `onboarding/index.html`, `settings/account/index.html`, `estate/index.html`,
`viewer.html`. Charter: `~/.claude/content-principles/fernwood.md`,
`cross-project/voice-and-stance.md`. `VOCABULARY.md` §2 and §3i bind.

## Verdict

**Something here stops the release on content.**

One thing, narrowly: **the receipt renders a schema id as if it were the person's own words.**
On the owner seat's J3 and J8 walks — the first screen a returning person lands on, and the last
screen they open — *WHAT I'LL BUILD FIRST* reads **`1. garden  2. motor-pool  3. equipment`**
(verified myself, `owner/2026-09-11T083409/R01-arrive.fold.png`). That person tapped *Gardening*,
*Looking after a vehicle*, *Working with tools*.

Two grounds, both already written down in this repo:
- `VOCABULARY.md` §2 — schema words never reach a person's screen. `viewer.html:18384` says it of
  this exact key: *"the reader-facing word is VEHICLES … `motor-pool` is schema only."*
- **Credit, don't thank** (`cross-project/voice-and-stance.md`, paul-ratified 2026-07-26) —
  *adopt their words, never improve them.* The card is titled **What you told me**. It is the one
  surface in the product where showing words the reader did not say is not a blemish but a failure
  of the thing itself.

Why a stop and not a note: `estate/index.html:430` does `var label = (r && r.label) || r;` — an
unguarded fallback that prints whatever string is stored. The storage holding the *words* is
browser-local; the record holds ids (`transcript.json entryState.ranked: ["garden","motor-pool",
"equipment"]`). The sign-out screen promises, in its own words, *"sign back in whenever you like,
from any phone"* — which is precisely the condition in which the words are gone and the ids remain.
The guard is absent, not merely untested. **Scope, stated honestly:** measured on a QA fixture
account; I cannot prove from these walks that a production account is in that state today.

Everything else below is a slot, not a stop.

## Slots

All DRAFT for Paul. Nothing here reaches a person without his confirmation. The recovery block's
two sentences (Paul-confirmed 2026-09-11) are untouched.

1. **⛔ THE STOP — `estate/index.html:429–433`, place page + app receipt.**
   Now: `1. garden` / `2. motor-pool` / `3. equipment`.
   Proposed: never print a bare stored string on this row. Resolve the id to its label; where no
   label is known, **omit the row** — the file's own rule for an empty ranking already says silence
   beats printing at her.
2. **`settings/account/index.html:125–126` — Your account, USERNAME.** All five seats.
   Now: `—` / `How you sign in. Anyone who shares a home sees it.`
   Proposed, when the phone doesn't hold it: value `Not saved on this phone.` · caption
   `How you sign in. Ask below and Paul will send it.` A dash rendered where a value belongs reads
   as *the value is a dash*; and the page's own next card already does that job.
3. **`onboarding/index.html:459` — account form, Paul's first mention.** Four of five seats.
   Now: `Eight characters or more. Nobody sees this, not even Paul — if you lose it, email him.`
   Proposed: `…not even Paul, who built this — if you lose it, email him.`
   He is named up to nine times before line 659 introduces him.
4. **`onboarding/index.html:659` — address form, present tense.** Four seats.
   Now: `We work out your weather and what grows there from this address…`
   Proposed: `We work out your weather from this address, and what grows there as your place fills
   in…` The app delivers weather and sky on day one and nothing about what grows there.
5. **`onboarding/index.html:2227` — the box refusal.** strict.
   Now: `…Add where the place itself is.`
   Proposed: `…Add where the place itself is — the road and the town are enough if there's no
   delivery there.` ⚠️ Only if Paul keeps *refusing*; the app elsewhere **holds** a boxed place
   (*"Add where it is when you can, and it lands here"*). Which door is right is his ruling.
6. **Same screen, the sentence four lines above the refusal.** strict.
   Now: `You can fix it before saving, and check it on the next screen.` — there was no next screen.
   Proposed: keep the sentence; when the refusal is showing, swap it for `Nothing's been saved yet.`
7. **One speaker.** strict + wide-eyed, independently.
   Now, on adjacent screens: `We work out your weather` · `that's my job` · `Everything here gets
   built from what you tell me` · `so I can't work out your weather` · `Paul does the resetting
   himself`. Proposed: **`I`** wherever the product speaks about its own work; **`Paul`** only where
   a human act is named; retire `we` (line 659 is its only appearance on the setup path).
8. **`tools/build-viewer.py:125` — the composer button default for every non-Fernwood household.**
   handover.
   Now: `Save & ask the Journal`, over a caption reading `Stays on this phone for now — nobody else
   sees it.` One of those two is untrue. Proposed, if nothing answers yet:
   `Save it to the Journal`. If something does answer, the caption is the half to fix.
   (Fernwood's own instance says `Save & consult the Almanac` — that split is correct and ruled.)
9. **`estate/index.html:397` — How to reach you, provenance line.** mom, J8.
   Now: `By email.` / `The default — change it whenever you like.` — shown after signing back in on
   an account that had the preference on file the whole time, because the *did-they-choose* flag is
   a local key sign-out clears. Proposed: show the provenance line only when that flag is readable;
   otherwise `By email.` alone with `Change that ›`.
10. **Card shells.** strict, twice. An expanded module card reads `Open ▲`; the expanded *What you
    told me* card reads `Close ▲`. Proposed: `Close ▲` on every open card.
11. **`onboarding/index.html` — the account receipt.** strict.
    Now: `✓Your account's set up. Now your place.` Proposed: a space after the tick, as every other
    ✓ on the walk has.
12. **One sentence, two nouns, one field.** `onboarding/index.html:442`
    `Anyone who shares a place with you sees this.` vs `settings/account/index.html:126`
    `Anyone who shares a home sees it.` Proposed: `Anyone who shares a home with you sees this.`
    in both.

## mom

**J0** — bare door → account → *What do you call it?* → **the condo** → *38 Hill St Apt 3B,
Roswell* → read-back → ranked **household systems** first, **paperwork** second → the app.
**J3** — carried straight to her place, typed nothing. **J8** — sign-out, cold door, a wrong
password, a made-up name, recovery, sign back in.

*Consistent naming?* No, in one place: her two picks read **Keeping the household systems running**
/ **Keeping the paperwork straight** on founding and **Household systems** / **Papers and
documents** on both later walks. These are real words she once tapped, from an earlier wording —
so it is a **consistency** finding, not the accuracy one above. It still matters for her
specifically: *household systems* is her own coined phrase, protected by name in `viewer.html:18393`
and in CLAUDE.md's ribbon rule, and two vintages of it on one account is how a protected word starts
drifting. Almanac→Journal is correct and ruled: her app says **the condo Journal**, Fernwood keeps
the Almanac.

*True of what the record did?* Yes, with three exceptions. The read-back offered
**Add an apartment or unit number ›** directly under an address that already carried `Apt 3B` — read
as a person, the app telling her she missed a box. On J8 the *How to reach you* row **appeared after
she signed back in** and had not been there before, on the same account with the same preference on
file (slot 9). And *USERNAME —* is the page she'd come to on the one walk where she needed it
(slot 2). The sign-out copy — *"Signing out forgets you on this phone only"* — was checked against
the record and was exactly true. She stopped, by her own account, at the sign-in refusal.

## owner

**J0** — founded **Hollow Creek Road**, Dahlonega; ranked *Gardening · Looking after a vehicle ·
Working with tools*. **J3** — returned, typed nothing. **J8** — full lifecycle, clean.

*Consistent naming?* **No — this is the stop.** Founding rendered his three labels; returning and
lifecycle rendered `garden / motor-pool / equipment`, twice each, with an **Edit** link under them.
Same build, same account, one hour apart.

*True?* Everything else was. He asked on 09-10 for the address confirm to become a gate; at this
build it is — *"You can fix it before saving, and check it on the next screen"* is now true in
letter and in order (`#ok1` → `Saving…`). Sign-out, the cold door, the one constant refusal and the
recovery receipt each did what their sentences said. Two standing untruths of tense: *"what grows
there"* (slot 4), and **A+ was already selected on a brand-new account** — a preference shown as
chosen that nobody chose.

## strict

**J0** — refused at the address gate with `PO Box 417`, nothing founded. **J3** and **J8** on the
boxed durable record.

*Consistent naming?* His own words came back verbatim, `ga` lower-case included — right posture.
The voice did not: `We` / `my job` / `I` / `Paul` across four adjacent screens (slot 7). Two labels
for one card state (slot 10). And the same explanation for an unplaced household appears twice on
one screen, impersonal in one card and first-person in the other.

*True?* The refusal is fair, names what he typed, and says why — the cream box, not red, is the
right register (**Caution as noticing, not warning**). Two sentences around it are not: *"check it
on the next screen"* over a screen that never came (slot 6), and a refusal that assumes he has a
street line to give (slot 5). *"Early days — Nothing's been built on it yet"* closed by
**"Empty so far."** under a button — three readings, none resolvable. `USERNAME —` again.

## wide-eyed

**J0** — founded *The Old Miller's Place on the Bend*, Bangor ME, ranked four. **J3** — returning
(weather throttled by a third party; not read as typical). **J8** — lifecycle.

*Consistent naming?* Her four came back as **Wildlife** and **A map you draw yourself** where she
tapped **Watching what's around** and **Drawing your own map** — the vintage split again.

*True?* One finding is sharper than any other seat's: **she signed in successfully while the screen
still said Paul was resetting her password by hand**, with the receipt's *"if nothing's come back by
tomorrow evening"* still on the page below the sign-in she had just completed. Nothing told her the
request was moot. That is a live claim about the future that the same screen had already falsified —
and it sits under Paul-confirmed sentences, so the slot is not in those words but in *when the block
is still shown*. Flagged for Paul as an open question, not drafted over. Also: *"Gardening"* and
*"Watching what's around"* carried **no** *an idea — not built yet* tag on the ranking screen, so she
read them as existing; neither exists. The green in-line confirmations on the account form
(*"is free"*, *"That's long enough"*, *"These match"*) are the best copy on the walk and the habit
stops there.

## handover

**J0** — founded *The Home Place*, Marshall NC, ranked *Getting it ready to hand over* first.
**J3** and **J8** on the durable record.

*Consistent naming?* Same vintage split: **Handing it all over · Papers and documents · Household
systems · Equipment and tools** on return against the four activity phrases at founding.

*True?* Yes of the record — and one sentence is true of nothing yet. The only mention anywhere that
a second person can exist is the username caption *"Anyone who shares a place with you sees this"*,
and across thirteen screens there is **no share, invite, or add-a-person control**. For this seat
that is the whole of the visit: the account page is the one he would screenshot for the next owner,
and it shows a dash where his username belongs. Two of his four picks carried no *not built yet* tag
and neither is in the app. He could not tell what **Save & ask the Journal** asks (slot 8).

---

*Fifteen runs read. Findings cite the frame or the source line. Nothing in this file has been
shown to a person.*
