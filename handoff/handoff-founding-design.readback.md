# READBACK — the founding-flow design window · written 2026-09-10, ~8:40 PM ET

- receiver: a fresh window opened on `handoff/handoff-founding-design.md`
- read at: HEAD `05a8a8a` (moved from `4e8eeab` to `05a8a8a` during my read — the refinement window's zones commit). ⚠️ Nothing below is started. This file and nothing else is written.

## 0 · The stamp, verified

The brief says *composed at `a96dfa1` + the register commit that carries it*. That register commit is `c38f04b` (it adds this brief and row 26). Between it and HEAD there are three commits, and I read every one:

| sha | what | touches my scope? |
|---|---|---|
| `c4fc894` | `.plans/2026-09-10-fifth-lens-SWEEP.md`, new (98 lines) | **yes, lightly** — see §6 |
| `4e8eeab` | one line in `BACKLOG.md` TIER 2 · 7 (a surname removed) | no |
| `05a8a8a` | one line in `BACKLOG.md` TIER 2 · 7 (cleaned-23 accepted) | no |

`onboarding/index.html` and `homes/index.html` have **zero commits since `318416a`** (measured `git log 318416a..HEAD -- <both>`). The candidate is intact. `qa-behind` reads *qa serves `318416a` — 29 commits behind HEAD (no app surface changed)*. So the brief's stamp is stale by three commits and none of them moves the thing I am here to design. I trust it.

Working tree: `tools/check-backlog-ready.py` is modified and `handoff/patches/` holds two `row-three-states` patches (17:47). Neither is mine and I will not touch, stage or commit them. `worker/digest.json` dirty as the brief predicts.

## 1 · What I understand the thread to be

Lap 6 of the release loop shipped **J0, the founding journey** — a cold person with no invite signs up, names a place, gives one address, and that address step *founds* an estate (`POST /api/estate`, the build lane's `318416a` on Pages, `d0cec6f` Worker). Five synthetic seats walked it in visible Chrome at qa, each read by its own unprimed reading seat, and gate ① reads **5 of 5 — but the UX clause is UNCHECKABLE**, so it is not a bare pass.

The five reads converged on six things, (A)–(F). Two of them are **design questions with a surface**, and those two are my mission:

1. **The confirm card** (onboarding s4, `#confirm`, *"Does that look right?"* · ✓ Yes, that's it · Not quite). All five seats found, independently, that it **founds before it is answered** — F08 calls `/api/estate` and the place is minted and placed; F09 then asks. **Gate or courtesy is Paul's ruling**, and my exhibit shows him both.
2. **The empty shelf** (`homes/index.html`). Four seats: it is **off a cold founder's path** (signup → naming, never the shelf; the harness reached it by goto) and it carries **two founding-looking controls** — *Set up my first home* (a real route into onboarding s1) and *＋ Add a home* (which, in the code, opens a card saying *"One account, one home — for now"* and captures a sentence, not a home).

Everything else the seats raised — s3 unphotographed (B, build lane's), the Almanac composer as primary control on an unplaced place (D), the profile 404 (E, strict's ruling 4, I carry), the 09-08 repeats (F) — is a **finding I carry into one findings list**, not a second mission.

I produce, in order: the owed two-pass `/ux-sweep` on the candidate at qa · two `/design-options` exhibits (confirm card; shelf) staged for Paul · a plan file `.plans/2026-09-10-founding-flow-design-PLAN.md` (`row: proposed — TIER 1 · 26`, readiness-convention header) holding the decision set with each option's seat reads, falsifier, and **which ruling of Paul's it needs** · rulings forwarded to refinement **in Paul's words**. Copy reaching a person goes through content-steward before it ships.

I am the design window. I do **not** write `BACKLOG.md` (refinement's), `worker/worker.js` (build's), any deploy, any origin, any push. I do not reopen the second-person question (§ 🤝 INVITE & JOIN, *"not this round"*) — I cross-reference it.

## 2 · Current state — what I verified myself vs. what I am relaying

**Verified by me tonight:**
- `release-state.py`: *FIRED · beat 9/12 (Paul walks it) · owner: paul · candidate 318416a · seats pass: True*.
- Chronicle beat 10 (`CYCLE-LOG.md:2364`): Paul's walk is **begun, not recorded as complete or clearing** — it names his throwaway owner `PK` and says *"His walk records as the clearing walk only after gate ① passes."* No line after that records the walk. **So condition 1 is in force: no edit to either surface.**
- `check-ux-sweep.py`: OWED, last two-pass 2026-08-31, **121 commits to viewer.html** (the brief and row 26 say 124 — the tool says 121 tonight; same verdict, a different count, and the tool's number wins).
- `release-gate.py:276–281`: the UX clause is UNCHECKABLE because **"no artifact convention exists yet"** — it is not waiting on my sweep, it is waiting on a convention nobody has defined. Running the sweep does not flip it by itself.
- All five seat runs exist under `.private/synthetic-walks/<seat>/2026-09-10T18…/` with `REPORT.md`, `capture.json`, and F01–F13 frames. I read each report's opening; the verdicts match the register verbatim.
- The confirm card's code: `ok1`/`ok2` POST a feedback answer (`onboard-addr-confirm` / `onboard-addr-dispute`) and open a note box (*"Anything else to add?"* / *"What should it say?"*). **Neither touches the estate record.** A "Not quite" lands as an `address-correction` note for Paul. The confirm is a courtesy *by construction today*, not by accident.
- The founding submit: `founding = SERVER_ESTATES.length === 0` → `fetch /api/estate {verb:"found", address, placeName, addressParts}` → on ok `landed()` → `step(3)`. On 409 `already-has-an-estate` it takes the existing-home path. A refusal shows `#trouble` (*"That didn't go through"*). **A PO box does not refuse founding** — strict's `est-pr9pwl` was founded `placed:false`; the geocoder refuses placement, the estate still exists.
- The shelf's `＋ Add a home` is a message-capture card, not a founding path (`homes/index.html:117–128, 353`).

**Relayed (from the brief, the register, the chronicle) and NOT independently measured by me:** every count in row 19 (13/13, 0 failed, 216/216 grants), the five estates' ids, the `walk-integrity` line, the Worker sha. I did not open a browser, did not hit qa, did not run `release-gate.py` or `walk-integrity.py`.

## 3 · The open decisions — Paul's, as I read them

1. **(A) Gate or courtesy** on *"Does that look right?"* — five seats, unruled. ⚠️ **This is not a copy choice.** *Gate* means the confirm precedes the `/api/estate` call, which reverses the build lane's shipped design (*"the one address step founds"*) and lands on the build lane's own finding that *nothing writes the place row after founding until B3/adopt exists* — so a post-founding "Not quite" has no write path to honour today. *Courtesy* means the card stops dressing as a gate (the seats' phrase) and says what it does. My exhibit has to make that cost visible, not just show two button layouts. The brief names engineering-partner for exactly this ("the found response as a gate") and I read that as the reason.
2. **The PO-box refusal at submit** — ruled `[paul-ruled 2026-09-10]`: *"when they hit submit, if we can check whether it's a PO Box… just say we don't accept PO Box."* Mine to design into the address step, for the **next** candidate. ⚠️ A sub-question the ruling does not settle and the exhibit must: *"we don't accept"* said **before** founding (a client-side check, nothing minted) vs. **after** (the server founds an unplaced house, the page reads `geocodeWhy: refused:…` and says so — the coordinator's "cheapest honest form"). Those produce different records. Paul's words lean to the first; the coordinator's note describes the second. I will show both and not pick.
3. **(C) The shelf** — on-path vs. off-path for a cold founder, and one founding control instead of two. Not ruled.
4. **The button grammar** on one card — three same-styled filled ✓ commits (Yes that's it / Save these / Open <place>). Not ruled; the standing rule *one affirmative grammar* (CLAUDE.md, 2026-07-29) bears on it and I will adjudicate against it, not re-litigate it.
5. **Carried, not mine to rule:** (D) the Almanac composer on an unplaced place and *"stays on this phone for now"* (handover's 2) · (E) the silent-catch profile write (strict's 4, engineering) · the account-exists receipt (strict's 3) · *describe or infer* (§ THE STANDING PRINCIPLE, open by Paul's own words).

## 4 · What has NOT been tested or verified

- **Paul's walk at `318416a` is not recorded.** Nothing I design may be applied until it is, or the coordinator re-candidates.
- **The UX clause has no artifact convention.** Even a clean sweep leaves gate ① at "human confirms." Whether I am expected to *propose* that convention is not in the brief (§6).
- **The "Not quite" path has never been tapped by any seat**, and neither has "Yes, that's it" (all five). What the person sees after either tap at `318416a` is unwalked. I read it from code only.
- **"Open <place>" without "Save these"** — untapped, unknown (wide-eyed, strict).
- **The Almanac composer on a not-composed digest** — no seat tapped it; what happens on tap is unverified (four reads say so).
- **Acceptance clause B** (a second founding is refused by name) — untouched by any walk (mom).
- **The receipt's WHERE IT IS captured empty** in the collapsed card on F12 — a hand check Paul does on his walk (wide-eyed).
- **Every `file:line` in the brief and the register older than an hour** — I re-derived the ones I cite above (`onboarding/index.html:727–729, 2024–2033, 2101–2128, 2130–2160`; `homes/index.html:117–128, 220–235, 353`) at `05a8a8a`.
- **The seat reports' paths** were given by run id; I resolved them to `.private/synthetic-walks/<seat>/<run>/` and all five exist.

## 5 · What I would do next, in order — none of it started

1. Wait for this readback to be graded.
2. **`/ux-sweep`, both passes, on the candidate at qa** (`https://fernwood-qa.pages.dev`, from `pages-deploy.py`'s `ORIGIN`), entering **through the bare door** the way a cold founder does — not at `viewer.html`. Viewport **414 × 848 at A+** (the repo's own measured standard; the skill's 390 default is wrong for this project and its own Refinement log says so). Method note records the served build (`/qa-build.json` says `318416a`) before and after.
3. File the trail to `.ux-reviews/2026-09-10-founding-flow.md`; fold its punch list into one findings list with (A)–(F), one vocabulary, dedup by surface.
4. Read the five `REPORT.md`s in full (I read openings only) and the two neighbouring plans (`interests-as-activities-PROPOSAL`, `setup-journey-PLAN`) so the exhibits cite them rather than redesign them.
5. **`/design-options` exhibit 1 — the confirm card**: gate vs. courtesy (with the write-path cost stated on the exhibit), the button grammar, the PO-box refusal at submit in both forms (§3.2). Serve the tree locally, apply swappable patches, screenshot the same region, compose with `exhibit.py`, stage to `~/Desktop/design-options`. **No edit to the tracked file.**
6. **Exhibit 2 — the shelf**: on-path vs. off-path; one founding control; what `＋ Add a home` becomes.
7. Create `.plans/2026-09-10-founding-flow-design-PLAN.md` with the decision set — per option: the seats' reads, the falsifier, the ruling it needs, the seat that is owed (content-steward on every sentence; engineering-partner on the gate option; ux-expert on the shelf). Tell refinement it exists so the `→ PLAN ·` pointer lands on row 26.
8. Iterate on Paul's reactions; forward his words to refinement verbatim; the **apply** to the two surfaces only after his walk is in the chronicle or the coordinator re-candidates.

## 6 · What the brief left me unsure of, or that looks thin

1. **What the sweep covers.** The sweep is *owed* on a clock measured in commits to `viewer.html`; my mission surfaces are `onboarding/` and `homes/`. The brief says "on the candidate at qa" and no more. My reading: the sweep walks the whole cold-founder path — door → account → naming → address → confirm → the app — because that is the product a founder meets and it reaches `viewer.html` at the end. If the coordinator meant *only* the two design surfaces, or *only* `viewer.html`, say so; they are different sweeps.
2. **The sweep founds a house.** The skill's safety rule is *never tap answer/Yes/No/"Looks right" buttons*. A fresh-eyes pass through the founding flow **must** sign up and give an address, which mints a synthetic estate at qa. That is a seventh house (see 4) and it is teardown material that must be recorded by record. I would have the pass use a fixture address, never a real one, and log the `est-` id in the trail. I also read the safety rule as forbidding the confirm taps and the Almanac composer — which means the sweep cannot see the two most-unverified paths either. Flagging, not deciding.
3. **The UX clause's artifact convention** — `release-gate.py` waits on one that does not exist. The brief does not say whether I propose it. I will not invent one in a tool I do not own; I will file the sweep per the skill and say in the plan what shape a convention *could* read, for the build lane / coordinator to rule.
4. **The handover seat's estate is recorded nowhere.** Its report says it founded **`est-otzfk2`**. The chronicle's beat 8 table has `—` under *founded* for handover, and row 19's teardown list names five (`rihhdp · d7teqw · bzr4gb · pr9pwl · ofd6vk`). `grep est-otzfk2 BACKLOG.md CYCLE-LOG.md` returns nothing. **Six synthetic houses at qa, not five.** The coordinator's own rule is *teardown by record, never by name-guessing* — this one is not on the record. Not mine to fix; theirs to hear.
5. **The count drift**: brief and row 26 say 124 viewer commits; the tool says 121 tonight. Same verdict. Noting it because a typed count beside a tool that computes it is the register's own named failure mode.
6. **The fifth-lens sweep (`c4fc894`) landed after the brief** and touches my ground at two points: **c·3** asks whether bare-door founding or a per-run invite is now the fresh-walk credential (J0 has no invite), and **a·2** says C9's *"the administrator authors the founding grant"* is overtaken by code (the product grants `owner` now). Neither changes my mission, but the confirm-card exhibit sits on the founding write, and if Paul re-rules who authors the grant, "gate" changes meaning. I will cite the sweep, not resolve it.
7. **"Design to a proposal is free"** — I read that as: mocks, exhibits, the plan file, `.ux-reviews/` are all free to write now; the *tracked* `onboarding/index.html` and `homes/index.html` are not, and neither is any file another lane owns. If the coordinator also means "no local branch, no patch file against those two", I would like that said — a `.patch` in `handoff/patches/` is what another lane is doing tonight and I do not want to copy the shape by accident.
8. **Two seats' worth of gaps in the gate-or-courtesy question the brief compresses to one line.** The seats did not only say "it founds before it is answered"; strict said F09 asks *about a box the completed founding cannot use*, and the promise *"fix it before saving, and check it on the next screen"* (F07) is what the order breaks. So the exhibit's honest framing is *what does this card promise, and can the record keep it* — the button pair is downstream of that. If the outgoing window sees it differently, I want to know before I mock.
9. **Paul's PK house** is his, at qa, disposable on his say-so — and the sweep's fresh-eyes agent must not be told about it, or about any seat's report, before pass 1. I will spawn pass 1 unprimed as the skill requires.

---

## 7 · GRADED — coordination window (`paulkirschenbauer-96`), 2026-09-10 evening ET

Verdict: *clean, and it caught one error of mine* (§6.4 — six synthetic houses, not five; chronicle corrected). Answers carried: sweep covers the whole cold-founder path from the bare door through the app at 414×848 A+ · the sweep's founded estate id goes to the coordinator for the teardown list · the UX-clause convention is not mine to invent · c·3 / a·2 are cross-referenced, not resolved · **patches against the two surfaces are free; the apply is not** · the exhibit carries strict's two extra clauses and **both** PO-box forms (detect before `found` vs. a Worker refusal) · pass 1 unprimed · Paul's throwaway owner is **`PAK`**, not `PK`. New from Paul's walk, for the findings list: feedback bubble from the moment an account exists · colour copy says *place* while the record says *account* · unit number — *"eventually ask 'do you want to provide a unit number?' — don't force it"* (rows 28, 29; a third being minted). **CLEARED: steps 2–7. Step 8 waits.**
