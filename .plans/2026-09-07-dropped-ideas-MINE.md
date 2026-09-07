# Dropped-ideas MINE — what Paul asked for about Fernwood / the estate manager that never landed `[commissioned 2026-09-07]`

> **Status: PROPOSAL. Nothing here is canon.** Paul rules on every row. This file was written by a mining
> agent on 2026-09-07 (~11:00–13:00 ET); it is the ONLY file that session wrote. It edits no tracked file
> and commits nothing.
>
> ⚠️ **A prior mine of the same corpus already exists** — `BACKLOG.md` § 🌱 SEEDS (2026-09-04, 27 rows
> `P-01`…`P-27`) and `PRODUCT-ENGINE.md` § 🎙 RECOVERED FROM VOICE MEMOS. Where a candidate here is one of
> those rows it is graded LANDED with the row named — a seed is a durable surface, even though a seed is
> *filed, not scheduled*. This mine re-derived the candidates independently from Paul's own turns and then
> checked each against the repo; it did not start from the seeds list.

---

## What was searched

| | |
|---|---|
| Instrument | `~/Developer/operating-layer/tools/corpus_index.py` rebuilt first (2,089 transcripts · 65,856 messages · 66.0 MB) → `~/LocalProjects/conversation-corpus/corpus.sqlite`, queried directly with SQL (message mode only; `--sessions` mode ignores its query, known bug) |
| Project tag verified | `SELECT project, count(*) FROM messages GROUP BY project` — the tag is **`Tate-Tracker`** (14,573 messages); `fernwood-private` (63) and `tate-commons` (85) exist as separate tags; no tag `fernwood` |
| Corpus span | 2026-07-03 12:50 UTC → 2026-09-07 14:58 UTC (the corpus starts 07-03; May–June has no conversation record — see § 4) |
| Session set | **335 top-level sessions** (`kind='session'`, subagents excluded): 188 carrying any `Tate-Tracker` message + 147 sessions from other roots (`~/.claude`, operating-layer, photo-organizer, tate-commons, …) in which a user turn names Fernwood / Tate-Tracker / estate manager / Tate Mountain / field journal |
| Paul's turns | 6,134 `role='user'` turns in those sessions → **4,227 are his words** after excluding image-only turns, `<system-reminder>` bodies, skill preloads, tool results, `<task-notification>`, cross-session messages, continuation summaries and turns under 15 characters (333 sessions) |
| Intent turns | **762 turns across 240 sessions** matched ask-shaped phrases (*we should · I want · I'd like · let's make sure · be sure · don't forget · at some point · eventually · one thing I · also, · another thing · would be nice · remind me · add to the backlog · capture that · note that · we need · idea · what if · could we · down the road · long-term …*); for the 147 non-Tate-Tracker sessions the turn itself also had to name a Fernwood concept |
| Reading | All 762 turns were read in full by the agent (647 KB), not sampled. Voice-dictated; asks were extracted for meaning, per turn, and stitched into arcs where the same ask recurs |
| Exclusions | pure one-off debugging instructions · vehicle-repair research questions (coolant type, door-panel solvents, headliner listings, amp/subwoofer — Fernwood *content*, not product asks) · asks that belong to another project (operating-layer renderer, photo-organizer, local-ai-exploration, market-digest, health, Bolo) · frozen-instance items gated by `BACKLOG.md` § FOCUS FREEZE / the 09-06 rulings |
| Landing check | per arc, 2–3 distinctive keyword regexes each, over `BACKLOG.md` · `OBJECTIVES.md` · `PRODUCT-ENGINE.md` · `VOCABULARY.md` · `CLAUDE.md` · `MOM-CYCLE-LOG.md` · `MOM-CYCLE-MAP.md` · `RELEASE_NOTES.md` · `INSTANCE-RECIPE.md` · `.plans/*.md` · `.decisions/*.md` · `.user-research/*.md` · `.ux-reviews/*.md` · `cycle/*/CYCLE-LOG.md` + `CYCLE-MAP.md` · `onboarding/*` · `handoff/*` · `~/.claude/projects/-Users-paulkirschenbauer/memory/*.md` · `~/.claude/design-principles/fernwood.md` · `git log --all -i --grep` (2,063 commits). **Every hit was read, not counted** — a keyword hit alone was never graded as landing. Where the surface was code (`tools/area-trace.html`, `onboarding/index.html`, `tools/walk-brief.py`) the code was grepped too |
| Attribution | from the content of Paul's turn only — never from a keyword or a nearby date |

**Grades.** LANDED = the ask is in a durable surface with a pointer (a row, a plan, a shipped commit, a seed, a ruling, a memory) · PARTIAL = a named half landed and a named half did not · DROPPED = searched every surface above, zero · SUPERSEDED = a later ruling of Paul's replaced it (cited).

**Surface tag** (added at the coordinator's request, for the freeze lift): `frozen-control` (Mom's old page, now a data control — nothing lands there) · `new-production` (the household she will be onboarded into) · `engine` (shared across estates) · `process` (how the work is run). Tag only; no ranking, no placement relative to gate G0.

---

## 0 · THE NUMBERS

| grade | count | predicate |
|---|---|---|
| **candidates found** | **131** | distinct Fernwood / estate-manager product-or-process asks in Paul's own words, 2026-07-03 → 2026-09-07, after the exclusions above; each is one row in § 1–3 or Appendix A. Recurrences of one ask are one arc, not several |
| **LANDED** | **114** | a durable surface names the ask with a pointer (row · plan · shipped commit · seed · ruling · memory) — Appendix A, one line each |
| **PARTIAL** | **5** | a named half landed and a named half is in no surface — § 2 |
| **DROPPED** | **2** | zero hits across every surface listed above — § 1. One of the two is a weak signal (said once, as a *maybe*) and is flagged as such |
| **SUPERSEDED** | **10** | Paul's own later ruling replaced the ask — § 3 |

**Measured drop rate: 2 of 131 (1.5%) DROPPED · 7 of 131 (5.3%) DROPPED-or-PARTIAL.** Conservative by construction: a seed counts as landed, a source-code comment counts as landed for the half it names, and a one-off *maybe* is flagged rather than dropped silently. ⚠️ Read against § 4: this cannot see May–June, cannot see images, and the 09-04 mine already swept most of what a July–August pass would have found — so the rate measures *what the register holds today*, not what would have been dropped without that earlier mine (that mine found 27 seeds, none of which were in the backlog before 09-04).

---

## 1 · DROPPED

### engine

**D-1 · A FORWARDED GRANT LINK MUST NOT GRANT ACCESS — the requirement, and its own deferral, are in no register**
*surface: `engine` · confidence: real drop*

> *"I think, generally, the grant link will route through account creation unless the account already exists. And then it's just in addition to kind of the estates they have access to. Right? **Ideally, a forwarded grant does not grant access. It should only be the person identified**, but we have to kinda figure that out how exactly that works for the immediate term."* — 2026-09-05 20:11 ET
> *"OK, yeah **let's not worry about this Forwarded Grant thing for the immediate term**. Let's just focus on getting people in the loop and I think we can assume I will not forward anything. Mom will not forward anything. Bob will not forward anything so **let's deprioritize that**."* — 2026-09-05 20:21 ET

- session `c4f82e9a-266e-4821-9a30-dcffc90eb6fe` · first 2026-09-05 20:11 ET · last 2026-09-05 20:21 ET
- **What landing would look like:** a row (C9 · THE INVITE FLOW is the natural home, `BACKLOG.md:2438`) or a line in `.plans/2026-09-04-roles-and-access-REQUIREMENT.md` stating the requirement *a grant is bound to the person it was issued to* **and** its disposition *deferred by Paul 09-05, released when a second real person exists outside the three named*. A deferral is a ruling; the rule the repo already holds is that a ruling not in the register is not in force (`BACKLOG.md:134`).
- **Where I looked, zero:** `forward(ed)? grant` across BACKLOG · PRODUCT-ENGINE · VOCABULARY · C9 · roles-and-access-REQUIREMENT · onboarding-PLAN · release CYCLE-LOG · memory · git log. The only adjacent thing is the 09-07 finding that a grant link does not clear `K_USER` (`cycle/release/CYCLE-LOG.md:626`) — a different defect. The first half of the same turn (*route through account creation unless the account already exists*) DID land there.
- **Why it matters for the freeze lift:** the same week Bob was ruled to get a link (tate-commons, 09-06), which is exactly the grant-bearing message the requirement is about. The requirement is security-shaped and currently exists only as the assumption *"nobody will forward anything."*

### frozen-control

**D-2 · THE FROZEN GITHUB FERNWOOD "MAYBE BECOMES AN ANONYMOUS PORTFOLIO VERSION"**
*surface: `frozen-control` · confidence: **weak** — said once, as a maybe, mid-sentence; listed because it touches the sunset order and nothing records it either way*

> *"the GitHub Fernwood will eventually be replaced by the production Fernwood… the GitHub Fernwood will eventually be sunset, but that will be after we sync all of them with her latest feedback from the frozen version **and then maybe that hub frozen version becomes an anonymous portfolio version**."* — 2026-09-04 18:53 ET

- session `4126aa5c-ab54-40ca-bd35-99601ad12fb2` · first and only 2026-09-04 18:53 ET
- **What landing would look like:** one line in the 09-06 rule-3 sunset order (`BACKLOG.md:159-174`) saying whether the frozen artifact has a second life as an anonymised portfolio page, or that it does not. The sunset order as written ends at *disable Pages · stop the bots*; the career memory (`project_career_ai_capability_evidence.md:16`) wants *"a portfolio-grade demonstration — not the raw private repos"*, which is the same idea from the other side, and neither file points at the other.
- **Where I looked, zero:** `anonymous|portfolio version` across every surface above, plus the two Fernwood memories (`project_fernwood_qa_parallel_and_onboarding_goal`, `project_fernwood_release_loop`).
- **Tension to note, not resolve:** rule 3 says the control is *an artifact, not a live site* and the sunset disables Pages. An anonymous public version would be a *new* surface built from the archive, not the live control kept up — so this is not in conflict with rule 3, but it is not in it either.

---

## 2 · PARTIAL

### process

**P-1 · THE USER-RESEARCHER INTERVIEW OF PAUL — captured as beat 0, never run, no row owes it**
*surface: `process`*

> *"I think it's worth at some point having the customer researcher come in and kind of interview me to be sure that kind of my intentions are clear and also establish kind of a vision here for what we're trying to build… there's an overarching kind of product engine capability that I'm trying to steer us towards."* — 2026-09-01 08:39 ET

- session `f4b54a64-a52a-4795-bdc8-07bd1bd1b37d` · first 2026-09-01 08:39 ET · restated 2026-09-02 14:27 ET (`f0499534-86b7-4422-b040-c54f8d132b92`, *"clear vision of what we're working towards at all times… I need help standardizing it"*)
- **Landed:** `PRODUCT-ENGINE.md:1147-1163` (§ HOW C0 OPENS — *"Beat 0 of this workstream is the interview, not a design. Do not open C0 with engineering."*) and the ordered path at `BACKLOG.md:2757` (*fleet lap 1 → review the mines → user-researcher interview → agile artifacts → then…*).
- **Not landed:** the interview. No `.user-research/` artifact after 09-01 is an interview of Paul (`2026-09-03-setup-journey`, `2026-09-04-fictive-test-user`, `2026-09-06-*` are journeys, personas and research); no BACKLOG row carries it as owed with a gate; and C4–C7 plus the Guru plan were all opened 09-03 (`.plans/2026-09-03-*-PLAN.md`) — the engineering the same paragraph says not to open first. The *"mine → interview"* reordering (`:1195`) is honoured on the mine half only.
- **What landing would look like:** either a dated row that owes the interview to a named lap, or a ruling that the 09-02 practice-steward derivation (`~/.claude/agents/audits/2026-09-02-operating-style-derivation.md`) and the 09-06 places-and-settings journey discharged it.

**P-2 · A RUNNING LIST OF WHERE A LOCAL MODEL COULD SIT IN FERNWOOD — and the "AI drafts the harder cards" idea**
*surface: `process`*

> *"we can kinda just come up with ideas as well for local model implementation and keep that as a running backlog."* — 2026-07-20 21:54 ET
> *"this is where I wonder if we can start to consider developing a very specific agent or local model that can get some of the less deterministic cards and kind of draft them… I hope we're accumulating at least these ideas of where we can implement local models. I'm totally good with you pushing back here, but **let's not lose track of all the ideas we proposed so that we can go back and test them when we get more confident**."* — 2026-08-01 23:10 / 23:13 ET

- sessions `cf0ab802-bbcc-4214-886f-335564915952` (07-20) · `e1cac6d4-2402-498a-8a43-8eb91772be96` (08-01) · restated from the process side 2026-09-02 14:27 ET (`f0499534…`, *"testing local models and trying to identify further opportunities for automation and how to build trust in that"*)
- **Landed:** the nearest thing is the 07-14 ai-advisor deferral in `CLAUDE.md:451` — *"Also deferred: … AI-assisted card phrasing"* and *"revisit AI-draft-behind-the-gate only if the loop proves durable — >10 answered across reseed cycles"* — which predates the ask and is the rule the agent pushed back with.
- **Not landed:** the list itself. `local model|local-model|small model` returns zero in every Tate-Tracker surface; the memory `project_local_ai_exploration.md` (the sibling project) carries no Fernwood entry, no card-drafting entry, nothing about Mom. Three separate asks to *accumulate* these ideas (07-20, 08-01 ×2) produced no register.
- **What landing would look like:** one row (or one `PRODUCT-ENGINE.md` table) titled *where a constrained local model could sit* with the two he named — drafting the less-deterministic cards behind the administrator gate, and whatever the 07-20 session proposed — each with the gate that would release it. ⚠️ Any such row must carry the AI-boundary rule: authored content is *human-confirmed before it reaches Mom*, and a local model is still a model.

**P-3 · UPDATE CADENCE TO BETA HOUSEHOLDS — "under-promise, every three days an update"**
*surface: `process`*

> *"can we set it reasonably to start it be like under promise overdeliver every three days there's an update or something like that. This also ties into the business model discussion down the road… treat them as beta users or whatever and give them full access, kinda to everything without putting anything behind a paywall for the time being."* — 2026-09-04 20:30 ET

- session `4126aa5c-ab54-40ca-bd35-99601ad12fb2` · first and only 2026-09-04 20:30 ET
- **Landed:** the second half — beta users, full access, nothing behind a paywall — is a standing rule (`memory/project_monetization_deferred.md:118-128`, amendment 09-04, quoting this turn); and the *axis* — *"the SLA in terms of how long are they supposed to…"* — is in `fernwood-private/.business/2026-09-05-segment-JOINT-BRIEF.md:370` and `PRODUCT-ENGINE.md:1368` (*"the SLA on feedback turnaround"*).
- **Not landed:** the concrete proposal — a stated update cadence to beta households, starting at roughly every three days, under-promised. No surface holds a number or a promise shape.
- **What landing would look like:** one line in the joint brief or `PRODUCT-ENGINE.md` § ⑥ Commercial: *proposed starting cadence: an update every ~3 days, under-promised — Paul, 09-04; not ratified*.

### engine

**P-4 · CONTACT FIELDS ON ACCOUNT SETUP — format checks and the "at least one" rule**
*surface: `engine` (the onboarding surface is shared across estates)*

> *"…just say you know email address and then they can fill that in and the phone number and they can fill that in and pick a color should be like pick a profile color… we asked that you provide at least one way to get in touch and have the email on the phone number field below and let structure those intelligently so they kind of do the basic as if all email format check or does it follow a common phone number check with formatting and all that and then there's also a logic that at least one of those is filled out and formed correctly."* — 2026-09-05 23:36 ET (his own walk of production, *"not to be actioned but to be rolled with everyone else's"*)

- session `c4f82e9a-266e-4821-9a30-dcffc90eb6fe` · 2026-09-05 23:36 ET (dictated twice, 23:36 and 23:37)
- **Landed:** the profile colour as a separate thing from the place colour (`VOCABULARY.md:296-305`; `.user-research/2026-09-06-places-and-settings-journey.md:309`, tagged `validated` — P19, Paul's own); the one-line phrasing cuts (release CYCLE-LOG rounds 5–9); the live password-match check (`…places-and-settings-journey.md:307`); `type="email"` on the field (`onboarding/index.html:414`).
- **Not landed as a row:** email / phone **format validation**. It is recorded only as a comment in the source — `onboarding/index.html:349`: *"Email and phone still carry NO such [check]"* — and appears in no BACKLOG row, plan or cycle log. A comment in a 1,800-line HTML file is not a place the loop reads.
- **Superseded, and worth stating:** the *"at least one of email or phone"* logic was overtaken the same night by Paul's own later ruling — `onboarding/index.html:385-393` `[paul-stated 2026-09-05]`: *"capture their email address as well and make their phone number optional"* → required email, optional phone. So only the format-validation half is open.

**P-5 · THE SYNTHETIC WALK ENDS BY PLAYING THEIR INPUT BACK (editable) UNDER A "YOUR FEEDBACK IS CRITICAL" BANNER**
*surface: `engine` (arrival / first-screen surface)*

> *"that will be a key part of the synthetic walk-throughs is not just breeze through it and fill it out, but read everything… at the very end they should be able to look at the instance and ask the question OK does this seem personalized to me? Does the buildout make sense based on what information I provided? … **this is where we integrate our feedback portion — we could play back any of the information they provided with the option to edit it if they want, but somewhere we should also just have a banner across the top that emphasizes your feedback is critical to making this digital home helpful to you.**"* — 2026-09-06 10:42 ET

- session `f7791786-6548-42ad-8aec-9f06aa799793` · first and only 2026-09-06 10:42 ET
- **Landed:** the reading brief — `tools/walk-brief.py:14-16` carries the *"READ everything… Does this seem personalized to me? Does the buildout make sense…"* questions verbatim, and `tools/journey-walk.py:174` makes the seat actually rank (*"not just breeze through it"*, `[paul-stated 2026-09-06]`). The 09-07 first-screen rulings (`cycle/release/CYCLE-LOG.md:705ff`) cover *what the place card says*.
- **Not landed:** the two product halves of the same sentence — (i) a **playback of everything the person provided, editable**, at the end of setup / on first arrival; (ii) a **standing banner** that their feedback is what builds the place. `play ?back|feedback is critical|digital home` return zero across BACKLOG · plans · CYCLE-LOG · onboarding · tools. ⚠️ (ii) collides with a rule the repo already holds — the ribbon doctrine's *"the intent is carried by STRUCTURE, not by explaining itself"* (`CLAUDE.md`, ribbon rule 3) and the crisp-register cuts of 09-06 — so landing it may mean recording *why not*, not building it. (i) is close to `read-onboarding.py`'s *what people said while setting up*, but that is Paul-facing, not a surface the person sees.

---

## 3 · SUPERSEDED — one line each, with the ruling that replaced it

| # | the ask (his words, date) | replaced by |
|---|---|---|
| S-1 | *"the feedback cycle with mom… the interview format"* — 07-13 21:08 ET (`dcc19b55-0bb8-4739-bb10-2060949d5b58`) | 07-22 09:31 ET: *"we're not sending mom the interview draft. We're basing everything off of her interactions in the app"* (`31079d65-2c3d-44e5-8f00-97b8eb531012`) → `BACKLOG.md:3075` KILLED row; Mama's Perspective is the replacement |
| S-2 | *"I think we need to be running this [the mom loop] more often than just eight, ten"* — 08-01 20:50 ET (`8be8aea8-ed67-4e58-8592-ce7c63e622fe`) | 08-10 11:32 ET: *"when we get [her feedback], that's a trigger to start a cycle"* (`f800508e-33f3-4e94-8a28-1a1255ca9843`) → `MOM-CYCLE-MAP.md` § What STARTS a lap; `CLAUDE.md` "the loop RESTS; her input fires it" |
| S-3 | *"it was clearer when there were dots as kind of a carousel… a design choice that we definitely need to revisit"* — 08-09 22:13 ET (`be5935ad-9dcb-448d-893b-35c67a8a95e6`) | 08-27: NO pagination dots — Paul's call (commit `39108d6`); `BACKLOG.md:698` W8·e narrows to cosmetic |
| S-4 | *"the transition… is by sending her a message with a link to set up an account and do the full onboarding"* — 09-04 ~11:55 ET (`6ea87de3-44f6-490e-828a-1fb3f0832448`) | 09-06: *"which I'll guide her in person"* → `BACKLOG.md:159` rule 3, THE TRANSITION IS A GUIDED VISIT |
| S-5 | *"we could just go ahead and add her condo in Atlanta… what are free events in the park…"* — 09-02 16:01 / 17:19 ET (`f0499534-86b7-4422-b040-c54f8d132b92`) | 09-04 18:49 ET: *"get rid of it and let mom set up the condo at her own pace"* (`4126aa5c…`) → `BACKLOG.md:2422` C8 DEFERRED; C7 stays a paper model |
| S-6 | *"at least one of [email, phone] is filled out and formed correctly"* — 09-05 23:36 ET (`c4f82e9a…`) | same night, later: *"capture their email address as well and make their phone number optional"* → `onboarding/index.html:385-393` (the format-check half is P-4) |
| S-7 | *"we don't have modules that pop up and are empty"* / 09-06 *"no empty modules, ask instead"* (voice memo 09-04 + release-loop ruling) | 09-07 11:05 ET: *"We shouldn't really show anything that's just empty… the preferences they select… let's not count that"* (`0aeff866-076c-486e-a997-a8bba1852d45`) → `cycle/release/CYCLE-LOG.md:705ff`; commits `e60d691`, `5727efe` |
| S-8 | *"when our usage resets, we need to do an audit… the really extensive scrubbing… we will do a history rewrite across all the repositories"* — 08-04 10:50 ET (`b43008bb-b148-4c24-944f-d33a84eb497d`) | 09-02: *"It doesn't need to appear, but we don't need to do a huge scrub if it showed up at one point"* → `PRODUCT-ENGINE.md:320` **no history rewrite**; the audit half lives on as `.plans/2026-09-03-privacy-scrub-PROPOSAL.md` and the S19 cross-repo item (`BACKLOG.md:1863`) |
| S-9 | *"the Fernwood tracker making that kind of an app you can… people can subscribe to"* — 08-13 15:41 ET (`8a47e801-ba49-4a87-9d88-0c9299dd8e3d`) | same session 15:47: *"I don't wanna do anything to interfere with my disability"* and 09-04 23:37 *"monetization is like down the road and lowest on the priority list"* → `memory/project_monetization_deferred.md` (deferred to ~end-2026; first customers are beta users) |
| S-10 | *"seed in some other ideas that we have to gauge interest, even if we haven't fully developed the features"* — 09-05 16:39 ET (`c4f82e9a…`) | 09-07: *"no idea cards"* → commit `e60d691` (*"a household's first screen is the almanac — no empty modules (ranked or not), no idea cards"*) |

Two **open conflicts** the 09-04 mine already recorded and this pass re-confirmed are NOT listed as superseded, because neither side has been ruled: *she edits and owns the plant table* (07-16) vs *no authorship-level input yet* (08-04) — SEEDS `P-18`, conflict X3; and *no telemetry on her site* (08-03 12:02 ET, `637706fe-c240-43e1-84d6-56b68301ba53`) vs *a clear view of her logins, clicks* (08-15 23:10 ET, `b3d5955e-e0ab-4f47-a4c6-bf742f1923cf`) — SEEDS `P-22`, conflict X4. Both are Paul's to settle and both are written down.

---

## 4 · METHOD LIMITS — what this mine structurally cannot see

1. **Nothing before 2026-07-03.** The Claude corpus starts there; the 30-day `cleanupPeriodDays` default deleted May–June before retention was raised on 08-03 (`31aa229`). Older Fernwood conversations live in a **second corpus** — `~/Developer/openai-data-archive/corpus.sqlite` (2022-12 → 2026-07, with images). **Not mined here, deliberately** — it is a different instrument with a different project tag scheme; the 09-04 mine's finding stands that only 2 of 52 May–June candidates were Paul's words at all. A Phase-D/E/F ask from May would not appear in this file.
2. **Images.** 159 of the 6,134 user turns in scope open with `[Image: …]` and carry no readable text (measured); they were excluded, and a screenshot with under ~60 characters of typed text carries the ask in the picture. Feedback he gave by annotating a screenshot (the 07-17 button screenshot, the 08-04 colour-code graphic, the 09-05 walk) is only here where he also said it.
3. **Voice memos are not in the corpus.** The eight 09-04 memos reached the record only through `PRODUCT-ENGINE.md` § RECOVERED FROM VOICE MEMOS; any memo not transcribed is invisible to this instrument (the repo itself notes the 18:55 memo was never transcribed until 09-05).
4. **Sessions tagged "outside a known root".** 12,440 messages carry an empty project tag (the second-largest bucket). They were included by content match on Paul's words, so a Fernwood ask made in an untagged session that never *named* Fernwood, Tate-Tracker, the estate manager, Tate Mountain or the field journal would be missed.
5. **The phrase filter.** 4,227 turns → 762 by ask-shaped phrases. An ask phrased without any of those markers (a bare imperative, *"do X"*) was not read unless it co-occurred with one. The filter was chosen to over-include (762 read in full; roughly a third were not asks).
6. **Subagent turns were excluded on purpose** (1,210 of 2,089 transcripts). Only his words count as an ask; an agent restating him is not evidence he said it.
7. **Landing was checked by grep-then-read, not by proving behaviour.** A row that says a thing shipped was taken as landed if the pointer exists; whether the shipped thing still works is the release loop's question, not this mine's.
8. **"Distinct arc" is a judgement.** 131 is the count of arcs *this reader* drew; another reader merging or splitting differently would move the denominator by a handful. The DROPPED and PARTIAL rows are stated per ask, so the numerator is less sensitive to that than the denominator.
9. **One prior attribution failure is the reason for the content rule here:** on 09-01 a grouping by keyword put four unrelated conversations under one heading. Every arc above cites the session and the turn it was read from.

---

## Appendix A · LANDED — 114 arcs, one line each (ask · first stated ET · session · where it landed)

Grouped by theme. Session ids are full so `corpus_search.py --session <id> --full` reopens them. `SEEDS P-nn` = `BACKLOG.md` § 🌱 SEEDS (2026-09-04).

### release / process (30)

| # | ask | stated | session | landed |
|---|---|---|---|---|
| L-1 | deploy the Worker yourself / a reusable deploy script | 07-12 17:29 · restated 07-14 10:55, 07-26 08:45 | `b4461624-fffd-4e68-90f0-348036a5c8ae` · `e5d04a9e-900e-4156-a4ff-2be2559279bd` | `CLAUDE.md` "Worker deploy is the agent's job (07-26)"; `tools/deploy-worker.sh` |
| L-2 | automate detect → mark → reseed of Mom's answers; never re-serve an answered card | 07-14 11:08 · 07-14 12:18 | `5ed881fe-fcb0-43af-a799-a5e6c4e53a51` | `read-mom-feedback.py`, `syncServerAnswers`, `harvest-questions.py`; `CLAUDE.md` § Mama's Perspective |
| L-3 | full-team review of the feedback cycle; automated recognise → analyse → reflect → incorporate → steer | 07-26 12:00 · 07-26 13:59 | `e5d04a9e…` · `8fb37ded-27d2-4cc5-b7d5-2da83763ed3c` | `.user-research/2026-07-26-feedback-loop-audit.md`; `/mom-cycle` (07-29); `MOM-CYCLE-MAP.md` |
| L-4 | acknowledgment ribbon covers everything since her last input, each phrase linked | 07-29 22:30 | `277ef96e-14b7-4b2a-9f54-dddb1f55da9d` | `CLAUDE.md` standing rule 2; `MOM_ACK_DATA.links` |
| L-5 | ribbon = *we actioned these because of you*, not a changelog | 08-04 11:02 · 11:45 | `b43008bb-b148-4c24-944f-d33a84eb497d` | `CLAUDE.md` "WHAT THE RIBBON IS FOR: ATTRIBUTION" |
| L-6 | "everything is changeable" messaging while she learns to give feedback | 08-04 10:46 | `b43008bb…` | `CLAUDE.md` standing rule 5; memory `feedback_everything_is_changeable` |
| L-7 | document the loop rigorously; cycle docs updated at close-out | 08-04 09:58 · 10:21 | `b43008bb…` | `MOM-CYCLE-MAP.md`; `~/.claude/tools/cycle-docs-check.py` (close-out C4·cycle) |
| L-8 | fresh-eyes agent reviews the app after bursts of change | 08-03 08:50 | `abe4ea74-f967-4801-9748-0a8395c48c7b` | `/ux-sweep` skill (standardised from the 08-03 pilot) |
| L-9 | ideation/visualisation cycle (side-by-side mocks) standardised | 08-02 22:06 | `f6e8c1b8-51e0-48e2-8e27-da5ab101586c` | `/design-options` skill; `.design-options/` |
| L-10 | telemetry sweep — every instrumented event proven to fire | 08-08 06:56 · 08-09 11:27 "go ahead on the telemetry walk" | `64473669-9e61-4ac7-8c97-0c3eeeb6ae92` · `d8027eed-7609-4627-a6e1-b23476b587ca` | `tools/telemetry-walk.js`, `tools/check-telemetry.py`; `BACKLOG.md:601` W12 (one class closed 08-09, `e63ce1e`) |
| L-11 | her feedback is the TRIGGER; the loop rests otherwise; keep it documented | 08-10 11:32 | `f800508e-33f3-4e94-8a28-1a1255ca9843` | `MOM-CYCLE-MAP.md` § What STARTS a lap; `CLAUDE.md` |
| L-12 | rotate / shuffle cards that get no response; track what gets answered | 08-27 14:02 · 14:18 | `92d69089-c209-405d-aa91-09dc90f4f8d1` | shipped 09-01 `6988816`; `MOM-CYCLE-LOG.md:409`; `.user-research/2026-08-27-card-rotation.md` |
| L-13 | the 08-14 audio clip that slipped — file both cracks, make sure it cannot recur | 08-28 12:39 · 12:44 | `33a7641b-0d3b-4447-ba5d-4c2c4325a032` | `MOM-CYCLE-LOG.md:540ff`; `BACKLOG.md:350-352` rows 12/13/14; `tools/check-arrival-dispositions.py` |
| L-14 | two-pass UX review is part of the natural release cycle | 08-24 22:54 | `1e88df55-35c9-4435-a3f0-775b4a57209d` | `CLAUDE.md` (`check-ux-sweep.py`, added 08-24); `cycle/release/CYCLE-MAP.md` |
| L-15 | check at HER conditions (414 × A+) before every release | 08-24 21:37ff | `1e88df55…` | `CLAUDE.md` § CHECK IT AT HER CONDITIONS; `measure-nesting-width.js` |
| L-16 | full UX review of production, fresh eyes + rules | 08-31 16:53 | `8f98321a-5891-4538-ac9d-33191589d8fd` | `.ux-reviews/2026-08-31-production-full-sweep.md` |
| L-17 | general assessment + rationalisation of Fernwood; a recurring rationalisation step | 09-01 07:57 · 09-02 13:12 | `f4b54a64-a52a-4795-bdc8-07bd1bd1b37d` · `f0499534-86b7-4422-b040-c54f8d132b92` | `.plans/2026-09-02-rationalization-PROPOSAL.md` (applied `29df004`); `tools/check-backlog-drift.py` |
| L-18 | definition of ready for a backlog item; expert review before build | 09-03 10:21 · 10:25 | `2c37c275-018a-4cf3-90e7-ea7a6d7c2987` | `.plans/2026-09-03-backlog-readiness-PROPOSAL.md`; `tools/check-backlog-ready.py`; grooming queue |
| L-19 | formalise concept → design → code → test using the prototyping tools | 09-02 17:11 | `f0499534…` | `BACKLOG.md:2649` C2 · THERE IS NO FEATURE DEVELOPMENT PROCESS |
| L-20 | a vocabulary document before locking names | 09-02 17:04 | `f0499534…` | `VOCABULARY.md` `[paul-ratified 09-02]` |
| L-21 | rename Tate-Tracker → Fernwood tracker in files/paths; consider migrating the stack | 09-03 11:21 · 11:27 | `2c37c275…` | `BACKLOG.md:2264` C4 · THE RENAME; `.plans/2026-09-03-c4-environments-PLAN.md:297` (GitHub Pages → Cloudflare Pages) |
| L-22 | keep a review window open on QA as content lands, with a "QA + last updated" bar | 09-03 19:12 | `525e5c77-c9bf-464d-8100-21d6b1d01c78` | memory `feedback_review_window_when_content_lands`; QA banner |
| L-23 | token-optimisation learnings need a home; seed it to the metacycle | 09-04 05:34 | `525e5c77…` | memory `project_token_optimization` (seeded 09-04) |
| L-24 | mine past conversations for small feature ideas (the first commission of this task) | 09-04 05:48 · 06:08 | `938d7d42-7e80-4315-832b-06a104bf1404` | `BACKLOG.md:3193` § SEEDS (27 rows; trail in `.private/idea-mine-2026-09-04/`) |
| L-25 | parallel terminal sessions with strict contracts and cross-session awareness | 09-04 14:25 | `4126aa5c-ab54-40ca-bd35-99601ad12fb2` | `.plans/contracts/_PREAMBLE.md`; the lane ledger |
| L-26 | the voice memos from 09-04 fully captured and processed | 09-05 09:53 | `c4f82e9a-266e-4821-9a30-dcffc90eb6fe` | `PRODUCT-ENGINE.md:1288` § RECOVERED FROM VOICE MEMOS; `tools/ingest-voice-memos.py` |
| L-27 | a failed synthetic run must not be kept; only the final successful run's data supersedes | 09-06 12:34 | `f7791786-6548-42ad-8aec-9f06aa799793` | commit `bb21863` run identity (current / pending / superseded); `cycle/release/CYCLE-LOG.md` |
| L-28 | QA = production + the feature under test; dev is the playground; a second QA / lab for Paul | 09-04 18:01 · 09-06 18:44 · 19:03 · 09-07 10:55 | `4126aa5c…` · `f7791786…` · `815b42ae-e4bb-47f8-8a75-0570cd7878a4` | `.plans/2026-09-04-three-environments-PLAN.md` (lab); `.plans/2026-09-06-one-environment-DECISIONS.md` § 8 |
| L-29 | run synthetics until it stops failing → Paul → Mom → Bob; process steward researches agile best practice | 09-05 23:08–23:40 · 09-06 10:34 · 18:42 | `c4f82e9a…` · `f7791786…` | `cycle/release/CYCLE-MAP.md`; `.plans/2026-09-06-release-loop-PRACTICE.md`; memory `feedback_release_cascade_persona_paul_mom` |
| L-30 | catch the frozen Fernwood up, gated on her production link; scope it with the other window | 09-07 09:50 | `443cb86a-ec16-499a-8598-d37892e89f5f` | `BACKLOG.md:244` rule 6; `.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md` |

### onboarding / journey / engine (36)

| # | ask | stated | session | landed |
|---|---|---|---|---|
| L-31 | a product engine: own domain, login, own database per household, modular so instances do not diverge | 09-01 08:09 | `f4b54a64…` | `PRODUCT-ENGINE.md` (stood up 09-01) |
| L-32 | one box for everything; do not build two interaction points (Track A / Track B) | 09-01 (voice) · 09-02 13:26 | `f4b54a64…` · `f0499534…` | `PRODUCT-ENGINE.md:972` § ONE BOX FOR EVERYTHING; `:255` Track A/B |
| L-33 | estate manager as the overarching cycle; Fernwood one instance; Bob's house another | 09-02 13:26 | `f0499534…` | `PRODUCT-ENGINE.md` § THE SEQUENCE; `OBJECTIVES.md` O3 |
| L-34 | all data separated by user; log in, select a house, then dive in | 09-02 13:49 · 18:25 | `f0499534…` | `PRODUCT-ENGINE.md:117` (reverses the no-login rule, deliberately); `BACKLOG.md:360` row 20 |
| L-35 | Fernwood as test bed; migrate data; Margaret's profile; then her condo | 09-02 16:01 | `f0499534…` | `PRODUCT-ENGINE.md:288` sequence table; C5/C6 plans |
| L-36 | define what may deviate between profiles (fonts) vs what must not | 09-02 16:04 | `f0499534…` | `PRODUCT-ENGINE.md:442`; commit `5ca9684` the divergence contract |
| L-37 | condo features (park events, restaurants, local news); why a condo dweller would use it | 09-02 17:19 · 09-04 06:17 | `f0499534…` · `525e5c77…` | `BACKLOG.md:2396` C7 paper model (C7-R1…R5); `.user-research/2026-09-04-condo-dweller.md` |
| L-38 | customer journeys to model: login, two estates, a finance tab, vehicles promoted to top level | 09-02 17:22 · 09-04 22:23 | `f0499534…` · `8ce54acf-3bd7-4667-a8c2-485ebd2670c3` | `PRODUCT-ENGINE.md:699/:785`; SEEDS `P-24`; `VOCABULARY.md:171` |
| L-39 | design concepts for open → login → select → arrive | 09-02 18:01 · 18:19 | `f0499534…` | `.design-options/2026-09-02-journey/` (door · selector, recommendations made) |
| L-40 | a coherent view of that journey and a full review of prior work | 09-06 13:50 | `f7791786…` | `BACKLOG.md:360` row 20 (six artifacts inventoried) |
| L-41 | product name vs the family's own domain; one link per family? | 09-03 12:01 · 12:24 | `2c37c275…` | `.plans/2026-09-03-product-name-PLAN.md`; `.user-research/2026-09-03-product-door-naming.md`; `VOCABULARY.md:176` |
| L-42 | people set their own name; name enters the Guru's lexicon; drop "Church Mountain property tracker" | 09-03 14:19 · 22:28 | `e1df7583-b538-4392-9c9f-6cbc2584dbfb` · `0e6305f9-3c1f-4f05-8537-4282e9ff413b` | `PRODUCT-ENGINE.md:529-536`; SEEDS `P-25`; commit `b93ace8` |
| L-43 | streamline device sync into the account (replace the pasted token) | 09-03 14:19 | `e1df7583…` | `PRODUCT-ENGINE.md:531/:536` ④ devices join the account |
| L-44 | administrator / owner / member in the vocabulary; owners invite additional people | 09-03 23:10 · 23:17 | `0e6305f9…` | `VOCABULARY.md`; `BACKLOG.md:2438` C9 · THE INVITE FLOW |
| L-45 | the Guru may hold private information behind a login | 09-03 (session ruling) | `525e5c77…` | `PRODUCT-ENGINE.md:184`; C6 door plan |
| L-46 | people can name things themselves; nicknames recorded against the internal name | 09-04 11:17 | `6ea87de3-44f6-490e-828a-1fb3f0832448` | `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` |
| L-47 | onboarding from first contact: draft the journey, copy, settings, buttons; design options per step | 09-04 17:45 · 17:54 | `4126aa5c…` | `.plans/2026-09-05-onboarding-PLAN.md`; `.user-research/2026-09-03-setup-journey.md` |
| L-48 | forced ranking of modules; batch the questions; unlock more as she confirms | 09-04 17:54 · 17:58 (+ voice memo) | `4126aa5c…` | `PRODUCT-ENGINE.md:1322-1357` (population order; *gamify* open, his); the ranking screen in `onboarding/index.html` |
| L-49 | a view-only role; a read-only invitee who can still found her own estates | 09-04 20:36 | `4126aa5c…` | `.plans/2026-09-04-roles-and-access-REQUIREMENT.md` |
| L-50 | naming as part of the vocabulary as ownership/family models expand | 09-04 20:54 | `4126aa5c…` | `VOCABULARY.md` § 4 + `:155-170` (what an estate IS vs CONTAINS); nicknames plan |
| L-51 | address validation: an automated step later; Paul performs it meanwhile | 09-04 22:05 | `8ce54acf…` | `BACKLOG.md:304` |
| L-52 | Mom is the first account → first property; force the synthetic → me → Mom test | 09-04 22:10 | `8ce54acf…` | `cycle/release/CYCLE-MAP.md`; three-environments plan |
| L-53 | flexible hierarchy: a car, a condo, or a single appliance can be a root; per-login trees | 09-04 22:23 | `8ce54acf…` | `.plans/2026-09-04-roles-and-access-REQUIREMENT.md:132-143`; commit `42d06ab`; SEEDS `P-24` |
| L-54 | size customer segments so there is a commercial pull on the backlog | 09-04 22:40 | `8ce54acf…` | `fernwood-private/.business/2026-09-05-segment-JOINT-BRIEF.md`; business-analyst seat |
| L-55 | confirm the address with a Google Maps link, not an embed | 09-04 22:43 · 09-05 09:27 | `8ce54acf…` · `c4f82e9a…` | commit `a2b7b68`; `PRODUCT-ENGINE.md:71` ("if the pin looks wrong, tell Paul") |
| L-56 | beta users get full access; nothing behind a paywall | 09-04 20:30 | `4126aa5c…` | memory `project_monetization_deferred.md:118` amendment |
| L-57 | feedback traced to an individual AND a home; one account, many households, shareable | 09-05 14:56 | `c4f82e9a…` | C9; `VOCABULARY.md`; tenancy work (`scopeFor`) |
| L-58 | estates per environment — walk a from-scratch Fernwood in QA and prod and compare | 09-05 16:10 | `c4f82e9a…` | `.plans/2026-09-04-three-environments-PLAN.md:123` table; `.plans/2026-09-06-conversion-method-DESIGN.md` |
| L-59 | grant link routes through account creation unless the account exists | 09-05 20:11 | `c4f82e9a…` | `cycle/release/CYCLE-LOG.md:626` (the `K_USER` finding, 09-07) |
| L-60 | password-match check · username changeable · everything changeable after creation · estate page reachable at end of account creation · onboarding questions = feedback lap 1 | 09-05 20:40–20:54 | `c4f82e9a…` | `.user-research/2026-09-06-places-and-settings-journey.md:307`; commit `51dca6a`; memory `feedback_onboarding_is_lap_one_of_the_cycle` |
| L-61 | his own walk: username ✓ live, password best-practice research, one-line phrasing, profile colour separate from place colour | 09-05 23:36 | `c4f82e9a…` | `cycle/release/CYCLE-LOG.md` rounds 5–9; `VOCABULARY.md:296-305`; memory `feedback_check_standards_before_building` |
| L-62 | founding owner is the household's administrator; Bob sets up both houses himself | 09-06 13:45 | `f7791786…` | roles REQUIREMENT; `tate-commons/process/2026-09-06-first-external-user-gate.md` |
| L-63 | settings on both the account menu and the estate page (colour, estate name, back navigation) | 09-06 14:06 | `f7791786…` | `BACKLOG.md:359` 19c; commit `382b1d0` |
| L-64 | production from scratch — carry nothing of his own property over | 09-06 14:08 | `f7791786…` | `tools/reset-production-estate.py`; `BACKLOG.md:138` rule 1 |
| L-65 | the jump strip still shows modules not turned on — control what is displayed | 09-06 19:59 | `f7791786…` | commits `e60d691`, `b0ce794` (09-07 "the emptied tile strip") |
| L-66 | colour is a SCHEME, not a header; research schemes incl. accessible; almanac's yellow joins the theme | 09-06 21:37 · 21:38 · 22:43 | `a4c82ab4-e8f4-4289-b461-e5263a36bf62` · `e102b8f3-261d-46ec-a735-e1eb9dc3cd81` | `.ux-reviews/2026-09-06-colour-scheme.md` + `-RESEARCH.md`; `cycle/release/CYCLE-LOG.md:318ff` |

### Mom's surfaces and the record (33)

| # | ask | stated | session | landed |
|---|---|---|---|---|
| L-67 | each plant: her own picture, description, zone; a table she can edit and own; add/edit-a-plant button; same plant in several zones | 07-16 09:21 · 09:57 · 10:20 | `db37b1c1-fdc3-4aab-8e45-adce27d21f2a` | `BACKLOG.md:591` W6 (photo = identity key), `:585` A2 intent; `.plans/2026-07-16-mental-model-elicitation-brief.md`; SEEDS `P-18` (conflict X3 open) |
| L-68 | reference photos on question cards with source; option to add her own picture | 07-20 17:12 · 19:27 | `bba2f793-1824-4273-b38d-52d0301f40be` | `BACKLOG.md:592` W4(a) shipped 07-20; `:593` add-a-photo IDEATION |
| L-69 | a weeds section; reminders before a weed goes to seed | 07-20 18:51 | `bba2f793…` | A7 shipped 07-20 (`:818`); `:826` "before it seeds" IDEATION |
| L-70 | a zone as a rich container (the pond: koi, pump, filter, plants) | 07-25 15:46 | `d3499a49-adae-4b87-85bd-fa2a79473061` | `BACKLOG.md:599` (explore later, his steer); `:848` |
| L-71 | curate a real reference corpus (pond water) → the RAG use case | 07-26 12:20 | `e5d04a9e…` | `BACKLOG.md:809`; `:648` (RAG correction); guru-retrieval plan |
| L-72 | convert her voice recordings to usable text | 07-18 00:14 | `52925802-41ed-4b57-ab4a-2d1303caef8a` | `BACKLOG.md:808` built 07-25 `tools/transcribe-mom-zone-audio.py` |
| L-73 | "not sure / ask me later" option; cards 3 → 5 | 07-14 12:57 · 13:03 | `5ed881fe…` | `MAX_VISIBLE=5` (CLAUDE.md); Snooze label; SEEDS `P-20` |
| L-74 | one dismiss gesture (an X, "card snoozed"); a cleaner "write me back" journey | 08-02 21:43 · 22:40 · 08-24 22:51 | `f6e8c1b8…` · `1e88df55…` | SEEDS `P-20`; `RELEASE_NOTES.md:222/:278` one "Write me back" (`05db30a`) |
| L-75 | Mama's Perspective as a master card; a condensed acknowledgment strip that stays visible | 08-02 22:23 · 22:44 | `f6e8c1b8…` | commits `a7f1dc1`, `05db30a` (folded receipt + one-question view, 08-03) |
| L-76 | unify the mismatched submit buttons; build an accretive rule set from these reviews | 08-02 18:07 · 18:09 · 21:19 | `6e03a78e-6cea-41da-b172-59ac88ff82e5` · `f6e8c1b8…` | `BACKLOG.md:2857` the shape system; `~/.claude/design-principles/fernwood.md` |
| L-77 | nesting / "chorus stacking" — rules, not a new rule per case | 08-24 21:44 | `1e88df55…` | `.plans/2026-08-24-nesting-width-measurement.md`; `BACKLOG.md:2915`; SEEDS `P-21` |
| L-78 | insect card: scrolling breaks going down the cicadas | 08-15 12:44 | `f01ff57b-0c81-4680-9b53-8fb9a73acb84` | `RELEASE_NOTES.md:113`; commit `d3b6460` |
| L-79 | household systems view — appliances, breaker box, what is worth knowing | 08-31 15:50 (+ 07-26, 08-04 seeding) | `c6bd08db-262d-4f42-9565-eb978d3c8e13` · `b43008bb…` | `BACKLOG.md:2102` SHIPPED 08-31; B6 `:2043`; commit `933efb4` |
| L-80 | the schema should match her model, not just the labels | 08-04 10:46 | `b43008bb…` | `BACKLOG.md:604` M2 (gated on data) |
| L-81 | plants + weeds + gardening as one card? | 08-04 11:40 | `b43008bb…` | `BACKLOG.md:603` W13; decision card `fernwood-8` |
| L-82 | emissions & registration reminders keyed to the owner's birthday | 07-11 16:27 | `b4e81051-e041-4e48-bba8-b43c36241b45` | SEEDS `P-01` THE REMINDER ENGINE; `BACKLOG.md:1955` |
| L-83 | both bikes: full oil change + carb cleaning next spring | 07-27 13:23 | `eb42c4bb-1da4-43f6-8b54-46b9f9fcb379` | commits `2150d78`, `5a6ef74`; `RELEASE_NOTES.md:496` |
| L-84 | the generator: sweep the manual, recommission before cold | 08-04 18:16 | `e77eed64-6ed0-48cc-a4f1-97265b87e97f` | `BACKLOG.md:1976`; decision card `it-ed637d5041ba` |
| L-85 | an LMC order bank | 08-18 17:34 | `d72bad07-082b-4279-975c-787aae204aad` | SEEDS `P-10` |
| L-86 | reference materials for every machine, queryable through the Guru | 07-08 17:18 | `e082d006-ffbb-4812-b582-c118be98607d` | `RELEASE_NOTES.md:811` "A manual for every machine"; `manuals/LINKS.md`; `.plans/2026-09-03-guru-retrieval-PLAN.md` (`search_library`) |
| L-87 | the Guru vision: one input box for everyone; evolving its capability is its own item | 07-28 14:10 · 14:13 · 07-07 13:11 | `5f68c0bf-ec82-42ca-ba0c-b481b2f58d38` · `5c848889-a482-4bf4-a495-3b581339381b` | `BACKLOG.md:800/:802` (plan stamped 09-03) |
| L-88 | a narrative book you can flip through of the vehicle work | 07-09 22:09 | `6e32e5cc-f433-4775-86ec-6a33896801ff` | SEEDS `P-04` the project arc; memory `project_vehicle_service_records` |
| L-89 | a clickable 3D vehicle showing repairs — file as an idea, feasibility first | 08-02 23:28 · 08-03 08:00 | `0559c5db-60ad-44be-a69c-5862e5cdb71a` · `a8a12ced-7022-4e62-a20a-648cda177e6f` | `BACKLOG.md:2057` B7 |
| L-90 | plant photos by zone from photo-organizer; projects within zones to the backlog | 09-01 20:02 · 20:52 | `6706db9a-e740-434e-8b69-4830e49bb3a4` | `BACKLOG.md:1068`, `:1142`, `:1225` INBOUND rows |
| L-91 | a higher-quality, zoomable map; property-line overlay; the Google Earth 2018 frame as a layer | 08-31 07:56 · 09-01 22:33 | `0c3df663-2099-4a41-9c2e-74714a5ccb33` · `d4c6f755-137d-48fa-84e9-702b7f38e413` | `BACKLOG.md:615/:617/:619`, `:910` basemap session; `.plans/2026-09-06-map-design-research.md` |
| L-92 | tracing tool: navigation buttons; hide / shrink zone labels so they do not cover adjacent zones | 08-31 07:39 · 07:49 | `0c3df663…` | `tools/area-trace.html:214-222` (pan/zoom buttons), `:372` `LABEL_MODES` Normal/Small/Off, `:423` no-overspill rule |
| L-93 | is "events and maps" the right solution overall — research before committing | 08-31 11:25 | `0c3df663…` | `.plans/2026-09-06-map-design-research.md`; `.plans/2026-09-06-maps-and-zones-PROPOSAL.md` |
| L-94 | a clearer schematic of the house and grounds; upgrade zone definition | 08-16 22:31 · 08-30 21:31 | `3e14f4b2-b175-4a94-8d34-cddb1aad74ba` · `0c3df663…` | the 08-30/31 tracing session with Mom; `BACKLOG.md:1042` THE FOLD; `.plans/2026-08-31-zones-traced-with-mom.json` |
| L-95 | landmarks / barriers first, not vertices; propose landmarks from imagery for new onboardings | 09-04 (relayed verbatim) · 09-06 09:36 | `15167b46-3fd9-4eef-ab18-1021175a3e12` · `3d29f0cb-35df-4da0-8af6-742cb51844b8` | commit `133fd01`; `.plans/2026-09-06-ai-mapping-capability-SCAN.md`; `BACKLOG.md:618` |
| L-96 | see whether she is logging in even when not answering cards | 08-14 10:16 · 08-15 23:10 · 08-16 19:09 | `4e5d404f-c709-4c9c-86d4-df7678981401` · `b3d5955e…` · `6d181dec-5aa5-4e06-bcc8-abe6be96d8a1` | `tools/read-mom-engagement.py --pickup` (in the session-start block); SEEDS `P-22` (X4 open) |
| L-97 | the glance vs the repository — a project principle | 07-06 15:56 | `770af494-955f-4c0e-8959-0b39eca9c274` | `CLAUDE.md` § Governing design principle (2026-07-06) |
| L-98 | name the station "Fernwood Weather Vane"; one source tag | 07-14 05:32 | `07c26e4e-0863-4b1a-b44e-e0768094cd3e` | `RELEASE_NOTES.md:703`; `INSTANCE-RECIPE.md:30` |
| L-99 | reinforce cards as doors; ask her which major categories she comes for | 07-29 15:13 | `4a88cf71-7f16-4192-8129-b952b11376bf` | `q-top-categories` — answered 08-03, retired 08-04 (`BACKLOG.md:384`) |

### data / instrumentation / other (15)

| # | ask | stated | session | landed |
|---|---|---|---|---|
| L-100 | a top card inviting her to talk through the zones; a trackable journey with hypotheses | 07-17 22:27 | `52925802…` | `BACKLOG.md:580` zone-journey front door v1 (07-17); `.user-research/2026-07-17-zone-journey-panel-synthesis.md` |
| L-101 | an MVP zone map on a leaf-off image, agreed with Mom | 07-16 21:58 | `c569ab1e-da1e-4015-9165-ae9dc1274628` | `BACKLOG.md:596` W0 done 07-16; area-trace 08-31 |
| L-102 | soil sampling by zone | 07-25 11:52 | `d3499a49…` | `.plans/2026-07-25-soil-sampling-plan.md`; W9 `:595` |
| L-103 | always offer free text; let her use the microphone | 07-13 22:15 · 07-16 10:05 | `dcc19b55…` · `db37b1c1…` | `.user-research/2026-08-02-free-text-journeys.md`; SEEDS conflict X2 (recorded, open); W3 voice |
| L-104 | her texts are not an official feedback channel | 07-26 13:01 | `e5d04a9e…` | `CLAUDE.md` "THE APP IS THE FEEDBACK CHANNEL. TEXT IS NOT" |
| L-105 | keep everything about Mom out of public reach; no new PII; hard to find, no password | 07-16 10:20 · 07-17 23:18 | `db37b1c1…` · `52925802…` | `BACKLOG.md:783` A5; `CLAUDE.md` QUARANTINE clause |
| L-106 | cross-repo privacy audit when usage resets (the scrub half) | 08-04 10:50 | `b43008bb…` | `.plans/2026-09-03-privacy-scrub-PROPOSAL.md`; `BACKLOG.md:1863` S19 (rewrite half → S-8) |
| L-107 | bookmarks and small-engine links swept into the reference corpus; keep copies of catalogs | 08-04 18:12 · 18:20 | `e77eed64…` · `ec96b26c-68be-4c93-8d8c-a890f908481e` | `manuals/LINKS.md` (commit `0393d64`); `BACKLOG.md:1977` manuals-corpus queue |
| L-108 | a start-up mnemonic for Mom on the 200 | 08-30 (session) | `7353af46-3abf-4993-b0d1-abc313dc99fb` | SEEDS `P-16` |
| L-109 | forum takes sequestered from the manual until verified | 08-30 16:11 · 09-01 08:49 | `7353af46…` · `f4b54a64…` | SEEDS `P-17`; memory `project_fernwood_fleet_cycle` |
| L-110 | pull every vehicle image into a massive archive; multi-session arcs like the coolant change captured | 09-01 08:53 · 08:55 | `f4b54a64…` | `.plans/2026-09-01-chatgpt-fleet-image-manifest.json`; SEEDS `P-04` |
| L-111 | a deterministic "is the site online" door for Fernwood | 07-31 16:02 | `394ced0d-bef3-4e8a-ba60-d23925a61e01` | SEEDS `P-14` |
| L-112 | read and answer cards offline; voice-dictate answers | 08-06 10:59 · 16:52 | `52f7015d-0e80-4c0d-b42a-c900083de0c5` | SEEDS `P-13` |
| L-113 | a larger-than-A+ text option for older readers | 09-03 (ruling C6 Q1) | `525e5c77…` | `BACKLOG.md:240` frozen question |
| L-114 | the weather card as one cohesive view; burn ban to the bottom; fishing read top-down by decision | 07-14 04:48 · 07-06 15:47 | `07c26e4e…` · `770af494…` | `RELEASE_NOTES.md:703-704`, `:840`; `.user-research/2026-07-14-weather-card-reader-jobs.md`, `2026-07-06-fishing-decision-journey-and-patterns.md` |

*Counting note:* L-1…L-114 = 114 rows; the S-1 interview, S-3 carousel and S-8 history-rewrite arcs were moved out of this list into § 3 so nothing is counted twice.
