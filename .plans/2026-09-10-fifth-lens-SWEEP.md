# The fifth lens — a read-only sweep of BACKLOG.md

- row: none
- kind: proposal
- objective: O5
- class: engine · declared
- ready: agent-proposed 2026-09-10 — Paul rules
- stage-note: 2026-09-10 — read-only sweep commissioned by Paul in the backlog-refinement window ("it's worth going through the backlog with everything we've said"); BACKLOG.md read at HEAD `e01dd58`

**The lens** (BACKLOG.md § THE FIFTH LENS, Paul verbatim): people found their own estates through the product (J0); we build nothing for a household and pre-fill nothing, *"for the most part"*; Paul's own condo is the working model because he uses it. **The one exception:** Mom's Fernwood in production, when she stands it up — we help pre-fill it, and shortcuts there are allowed because legacy Fernwood (`est-3c9f1a`) is the control.

⛔ **This file proposes; it edits nothing and re-tiers nothing.** Each finding quotes the row, names its location, and classifies it. Where a row conflicts only in how it is worded, it says *wording*, not *conflict*.

## Summary

| class | count | what it means |
|---|---|---|
| **a · CONFLICT** | 4 | proposes provisioning / pre-filling / building for a person other than through their own founding |
| **b · EXCEPTION instance** | 7 | pre-fills Mom's production Fernwood — should carry the exception mark on its row |
| **c · AMBIGUOUS** — Paul's word | 6 | sits inside the *"for the most part"* hedge |
| **wording** | 6 | the act conforms; the sentence does not |
| **conforms** | 12 | already honours the lens (listed so the reader sees the lens is mostly already true) |

**Read first:** a·1 (Bob's pre-provisioned `bob` deployment survived the nigel/aida teardown), a·2 (C9 still says the administrator authors the founding grant), b·7 (rule 5's "do not pre-fill her work" is now the rule *and* is reversed by Z-13, on the same page, unmarked).

## a · CONFLICTS — provisioning or content for someone other than through their own founding

**a·1 — Bob's estate exists before Bob has founded anything.** TIER 1 · 19: *"Build ① against Bob's household, not against `home`… the second lands in that person's EXISTING namespace after ①."* TIER 2 · 14: *"Deployed to all five (qa · lab · home · bob · paul)."* TIER 2 · 23: *"two real households now live (`home`/`est-e6696a` and `bob`/`est-9a74df`)."* § INVITE & JOIN: *"whether Bob's unspent invite at `est-9a74df` joins or founds when spent — UNRULED."* The same row 19 records that `nigel`/`aida` were destroyed at `4f7c04f` *"for this reason"* — yet the `bob` deployment, minted by the same `c1ae9bb` provisioning pattern, still stands and is cited as a live household in three rows. Under the lens Bob founds his own house through J0; a pre-minted `est-9a74df` with an authored invite is exactly *"pre-provisioned estates for other people."* **Paul's to say whether `bob` is a fixture to tear down like nigel/aida, or a deliberate second exception** (his 09-07 auto-wire ruling names Bob by hand — see c·1).

**a·2 — C9 says the administrator authors the founding grant.** § C9: *"The administrator authors the founding owner grant only… (A) owner fills a form → it reaches Paul → Paul sends… (A) is the agreed START."* Row 19's own forwarded state says `POST /api/estate` *"mints a fresh `est-` id and grants `owner` to the founder"* — the product now authors the founding grant, not Paul. Paul excluded grants from the lens (*"not about grants"*), so this is filed as a conflict in the row's ruling text, overtaken by code, and his to re-rule or strike.

**a·3 — The Midtown condo scratch instance is a paper model of a place its owner has not founded, and it is still live instrumentation.** § C4 (uniqueness ledger): *"Fernwood (prod build) vs the condo (scratch)… the condo build must carry zero of the 47… `identity.theme.main`, an agent-picked hex for 'dark blue'… declared in the condo's instance file today."* C7 was set aside 09-10 (*"let's not create anything artificial"*), but the C4 rows still treat the Midtown instance file as the falsifier target and the place-claims ratchet's second estate. Conflict in substance unless Paul rules that the scratch condo is a **fixture** (a test property, per the three-axis testing row) and not Mom's condo — in which case it is *wording* and the rows should say "fixture," never "the condo."

**a·4 — P-26 reads as us populating a stranger's instance.** § SEEDS P-26 *ONBOARDING IS AN IMPORT, NOT A BUILD*: *"approach other people and — to oversimplify — pull in all their data and preferences… and then just populate it."* A seed, not a row, and tagged IDEATION; but as written the actor is us. Conforms only if read as *the person imports their own material after founding*. Paul's word on which reading he meant.

## b · INSTANCES OF THE EXCEPTION — pre-filling Mom's production Fernwood; mark them

**b·1 — Z-13, the cleaned-23 preload.** TIER 2 · 7: *"preload the zones into mom's estate when she sets it up in production and you have her confirm them rather than draw them."* The lens names this as the first instance; the row does not yet carry the mark. Legacy control: the raw 23 trace in git history (R-Z4's comparison target).

**b·2 — The frozen-Fernwood catch-up.** § FOUR RULINGS rule 1: *"a manual process between you and me figuring out how we catch up the other instance."* Rule 6: *"gated on her getting her link to set up in prod"* → `.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md` (`stage: concept`, class instance). Exception by construction — it moves her legacy record into her production estate after she founds it. Mark the plan pointer.

**b·3 — Pouring her held feedback into the new instance.** § FOCUS FREEZE (09-04): *"pour in any of Mom's feedback since we froze it into the new instance when we're ready to do the transfer."* Rule 4: *"every action lands on the NEW instance, never on the control."* Exception instance.

**b·4 — Her data reaching the new estate server-side.** § THE DEVELOPMENT GOAL (ii): *"her data reaching the new estate server-side (notes, observations, `momQueue.*`) rather than through browser storage."* Exception instance; same act as b·2.

**b·5 — Z-ACK's acknowledgment debt.** § FOUR RULINGS rule 5, last paragraph: *"Sixteen of the 23 names are hers… The debt needs another form."* Now discharged by b·1 by construction — showing her the cleaned 23 to confirm *is* the attribution. Worth a one-line link between rule 5's open debt and Z-13.

**b·6 — The migration act Paul runs in person.** § FOCUS FREEZE (09-03): *"one event he manages in person (her device binding, the real grant tokens, the public-repo moves…)."* Grants are outside the lens by his word; the device binding and repo moves are shortcuts for Fernwood-in-production. Exception instance; superseded in mechanism by 3b (she arrives on her own) but not in intent.

**b·7 — Rule 5 is the RULE and the exception on one page, unmarked.** § FOUR RULINGS rule 5: *"WHAT WE KNOW INFORMS THE DESIGN, IT DOES NOT PRE-FILL HER WORK… None of it is content poured into her instance ahead of her."* This is the fifth lens's long-term view stated three days earlier — and Z-13 reversed it *"for zones only, on purpose."* Nothing on rule 5 says so. A reader of rule 5 alone would refuse b·1. Proposed: rule 5 gains one line naming Z-13 as its ruled exception; Z-10 (plants do not travel) stays the rule.

## c · AMBIGUOUS under "for the most part" — needs Paul's word

**c·1 — Auto-wiring Fernwood's weather station to Bob's estate.** § INTEGRATIONS: *"For Mom's account and Bob's account… we should just auto-wire the weather station to them… Other than those two houses, the vane will not be automatically attached."* Attaching a household's instrument to a house its owner has not founded is content conferred ahead of founding; Paul's own forward note says *"in the future we'll change that."* Mom's half is the exception; Bob's half is the hedge.

**c·2 — Paul standardising a person's address by hand.** § WAITING ON PAUL, ADDRESS VALIDATION: *"Paul's to do by hand until the API exists."* Help for households other than Mom's; conforms in spirit (*"SUGGEST, never decide… her typed words stay the record"*) but it is us doing a step for them.

**c·3 — The credential-axis remedy is an invite, and J0 has none.** § THE CREDENTIAL AXIS: *"a fresh walker arrives on an unspent invite, minted per run."* Row 19 (09-10): *"the one address step founds, and J0 walks it from the bare door"*; TIER 1 · 25: Paul signed up *"fresh at the qa door, no invite."* The invite remedy now describes J1, not the founding path. Paul or the harness lane: is a per-run invite still the fresh-walk credential, or is bare-door founding?

**c·4 — The family door.** § C4 custom domain: *"the FAMILY door (`<family>.<product>.place`)… two example families: Paul's and Bob's… Bob's address is created inside his consent conversation, not before."* A door we create per family is a provisioned thing; the ruling already defers it to Bob's consent. Which side of the hedge a subdomain sits on is Paul's.

**c·5 — Mom's condo as the onboarding trial.** § THE DEVELOPMENT GOAL amendment (09-04): *"we can also have Mom set up the condo… prompt her to name and provide the name for herself."* She founds it herself — conforms — but the 09-04 wording had the condo as *the* trial estate and C7 (09-10) says *"at her own time."* Which is the plan of record for her first founding: the condo or Fernwood?

**c·6 — The scratch condo's residue after C7 was set aside.** § C8: *"Until then C7's paper model is all the condo is, on purpose."* § THE NEXT TWO LAPS: *"the `paul` deployment IS that condo."* TIER 2 · 15: Paul's *"Grant Park Condo Almanac"* is `env.home` / `est-e6696a`. Two estate ids, two deployments, one condo — the C7 row already flags *"whether those are one condo or two is Paul's to say."* Until he says, the lens's *"working model"* points at an ambiguous record.

## wording — the act conforms, the sentence does not

- **TIER 1 · 20**: *"a second real household (Bob) exists"* — a deployment exists; a household Bob founded does not (see a·1).
- **TIER 2 · 23**: *"two real households now live"* — same.
- **§ B0**: *"'Bob's house' is a third tuning, not a fork"* — reads as a thing we tune; under the lens it is a house Bob founds on the same engine.
- **§ C0 pointer**: *"a product engine that explicitly transcends Fernwood (Bob's house, per-tenant domains…)"* — same shape.
- **§ C8**: *"Gate: the migration has landed — C4 · C5 · C7 shipped"* — C7 is set aside; the gate names a dead dependency.
- **§ C9 release condition**: *"(A) is safe only while Fernwood is the only estate with people in it… See Bob Q2"* — the premise (Paul routes rosters) is a·2's; the sentence is fine once a·2 is ruled.

## conforms — already honours the lens

- **TIER 1 · 19** — J0 founding built and walked from the bare door; `nigel`/`aida` destroyed, ids retired never reused.
- **TIER 1 · 25** — Paul's gate kit: one throwaway owner *"without generating a bunch of synthetic houses."*
- **§ C7** — set aside 09-10: *"Mom is gonna stand up her own condo at her own time… let's not create anything artificial."*
- **§ INVITE & JOIN** — *"just owners setting up houses"* this round; second estates and joining are scoping, not build.
- **§ SEGMENT HYPOTHESES** — *"once… they've built their own estates"*; hypotheses with falsifiers, *"not personas presented as fact."*
- **§ SPLIT THE JOURNEY FROM THE READER** — properties are declared FIXTURES; *"a seat is a SHAPE, not a person."* Synthetic households are presented as nobody's.
- **§ MODULE ONBOARDING** — many doors in, each the person's own act; ingestion proposes, the person confirms.
- **§ 3b** — *"she arrives on her own, and nothing may be gated on a visit"*; the product carries the load.
- **§ THE FOURTH RULING** — every action lands on the new instance, never on the control (the control is what makes the exception measurable).
- **TIER 2 · 7 Z-10** — the frozen instance's plant↔place data does NOT travel; **TIER 2 · 8 R-Z6(B)** — gate the read so `home` never serves Fernwood's 23 to a house that has not saved one (the leak the rule exists to stop).
- **TIER 2 · 14 / 15** — the digest floor refuses another estate's record; row 15 makes routes answer from a household's own.
- **P-24** — *"my mom might have the option to choose between condo, Tate, and Tiguan"* — the person's own top level.

## What I could not classify

- **Which deployment is "my working model with the condo."** The lens gloss says the `paul` deployment (`est-d93508`); the production evidence rows (TIER 2 · 11, 15) say `home`/`est-e6696a`. I did not read wrangler.toml or the instance files — read-only on BACKLOG.md — so I cannot say which is his, and c·6 stays open.
- **Whether the `bob` deployment was minted with Bob's consent conversation done.** § C4 says Bob's address is created *"inside his consent conversation, not before"*; row 19's `c1ae9bb` provisioning has *"no row in this file."* If consent exists, a·1 softens from conflict to a second exception Paul chose; the backlog cannot tell me.
- **Outside the lens, noticed in passing:** § SEGMENT HYPOTHESES prints a third party's full surname (line 775) in this public tracked file, which the C4 forward rule (*"removed forward… covers any third party by name"*) forbids. Not a lens finding; named so it is not rediscovered.

## Falsifier

This sweep is wrong if Paul reads a row marked *conforms* as a conflict — the likeliest candidates are the testing-architecture fixtures (a synthetic condo with an apartment number in `mom`'s seat file could be read as *a paper model of her place*) and R-Z6(B) (gating the read could be read as *we decide what she sees first*). It is also wrong if a·1 turns out to be a ruled exception recorded somewhere BACKLOG.md does not point at; the check is `git log --all -S'est-9a74df'` for a consent or exception note, which I did not run.
