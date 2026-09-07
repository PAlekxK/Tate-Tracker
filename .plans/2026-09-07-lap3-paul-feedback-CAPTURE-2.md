# Paul's lap-3 feedback, part 2 — the production walk after sign-in

- row: process · kind: record · objective: O5
- ready: record 2026-09-07 — no ruling requested by this file
- gate: ⛔ NOTHING HERE EXECUTES. Verbatim-in-substance capture, taken live while Paul walked.
- ⚠️ WHY THIS IS A SECOND FILE: `.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md` (F1-F6) was
  being read by five subagents when these arrived. Appending mid-read would have given some seats
  one version and some another — the class of inconsistency that manufactures false findings.
  Merge the two after the panel reports.

---

## ⭐ THE RELEASE EVENT — Paul CLEARED lap 2 in production, 2026-09-07 evening

`paul-stated`: *"at this point, you know, I guess I've set up my property. It seems to have taken my
address, and we've highlighted a lot of different changes we could make… so I guess I'm gonna pass
this build, and say let's go ahead and conduct a full audit of how this lap went, including my most
recent feedback, and close the lap with that."*

⚠️ **HE PASSED IT WITH KNOWN FINDINGS CARRIED FORWARD — this is not a defect-free build**, and the
record must not later read as though it were. Cleared at `1e2748d` on `fernwood-home.pages.dev`,
estate `est-e6696a`, account `pkirsch`. The gate ① UX clause — uncheckable by machine, exits beat 2
only on a human's confirmation — is discharged by this walk.

⚠️ **And it took three out-of-band repairs to make the walk possible at all** (F4): a fresh grant, a
new `hydrate` path, and a hand re-stamp of `fw-onboard-owner`. A future reader must not conclude the
product let him in on its own. It did not.

## F7 · Settings and "what you told me" read bare-bones
`paul-stated`: *"It says your home is what you told me, settings — those are pretty bare bones…
It would be good for the UX team to look at best practices, how we can make those look a little
more clean. And also, is 'what you told me' the right way to say that?"*
→ ux-expert (layout) + content-steward (the phrase). Both running.

## F8 · 🔴 "Stays on this phone for now. Nobody else sees it." — he could not tell what it meant
`paul-stated`: *"so does that mean it's not syncing, or what exactly does that mean?"*
**ANSWERED, measured:** it genuinely does not sync. `viewer.html:20723` carries a sync mode
`household-local` whose pill reads *"On this phone"*, tagged in source as *"a limitation, not an
error (four seats, round 4)"* — and the very next line renders **no sync button at all** for that
mode: *"no button to a door a household cannot open."* So a household's notes live in one browser
and nowhere else. The copy is TRUE and NOT LEGIBLE, which is the worst combination: it discloses
without informing. ⚠️ It also sits against s0's standing promise, *"yours on any phone, not just
this one."* → engineering-partner §D (architecture) + content-steward Q3 (the line).

## F9 · The ask path and the save path share one error surface
`paul-stated`: *"I put a comment into the Grant Park condo almanac and it says the Almanac can't
reach the network just now, try again in a moment"* — then, later: *"I do see that my entry did get
saved into the almanac at the bottom, and it says on this phone."*
**Measured:** `viewer.html:21360` is the catch on the **ask** path (a question to the Almanac); the
**note** saved through a separate local path. Two systems, one error surface, and nothing on screen
says they are different. A reader cannot tell "my writing was lost" from "the assistant is away."

## F10 · The place card is about the PROPERTY, not the weather
`paul-stated`: *"where it says Grant Park Condo — what is actually gonna go in this card? Not
necessarily weather and what grows, but I think this card is really about the property, right? So
anything we can inference about the property from the address would go in there… local events,
festivals, etc., especially since it's a condo in the city."*
⛔ Blocked on the AI-boundary ruling (BACKLOG C7 Q4). → ai-advisor, running.

## F11 · Reuse Mom's ribbon + feedback box to carry the weather promise
`paul-stated`: *"what would be good is if we have the feedback box, the acknowledgment box and
ribbon that we introduced in the old Fernwood for Mom, but have that message that says we're
working out your weather and what grows here from the address that you provided… and I can just say
OK sounds good."* Ties to the onboarding-promise reframe Paul HELD to this lap for content-steward.
⭐ F10 + F11 read as ONE idea: the card stops promising weather it cannot deliver and becomes a
property card; the weather promise moves into a ribbon that ASKS rather than ASSERTS.

## F12 · Logout — second time asked
`paul-stated`: *"we need a logout button down the road."* Already captured pre-walk; **asking twice
in one evening is the signal.** → C6, with the sign-in door.

## F13 · Let the household rename the almanac
`paul-stated`: *"I'd like to have the opportunity to customize what we call kind of the almanac, but
that's low priority."* His own priority label, recorded as given.

## F14 · Settings shows your ROLE and lets you INVITE — second time asked
`paul-stated`: *"in the settings, what we'll also want to have eventually is a way to also invite
people to the household. It'll show your role as owner and you can invite people to the household."*
⭐ **NOT NEW — this is rows 19/19b, and he asked for it at 11:17 ET this morning too**, in the
production store: *"We want to show roles on this page — I am the owner for Grant Park and you can
see Home members. Down the road I will want to invite mom to have access to my condo and she will
invite me to the house that she sets up."* Twice in one day, unprompted both times.

## F15 · ⭐ THE NEXT QUESTION HE WANTS OPENED — weather as discovery, not as an API
`paul-stated`: *"my immediate next question is the weather, and how we populate that, and how it
makes sense from a user discovery and data endpoint point of view."*
⚠️ Read this as scoped: it is NOT "which weather API". It is how a household that has just handed
over an address discovers what the product can tell it, and where that data comes from. → ai-advisor
§4, alongside the Open-Meteo proxy Paul already approved (one client instead of N).
