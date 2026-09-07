# Handoff: fernwood-release-lap3
<!-- generated 2026-09-07 ~23:55 ET · sources: ~/Developer/Tate-Tracker@53c3446 (main, clean) · ~/.claude@a98ea89 · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1 · Mission
Open and run **lap 3** of Fernwood's release loop, on the revised process — starting from the
consolidated briefing, not from a re-derivation.

## 2 · Read first
1. **`.plans/2026-09-07-lap3-BRIEFING.md`** — the entry document. §1 rulings owed · §2 the two gap
   questions · §4 the 47-row census · §7 Paul's five rulings · §8 the v1 rule. Everything else is
   pointed at from here; do not re-read the panel files unless a step needs one.
2. **`.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md`** — how lap 3 should run. ⛔ `agent-proposed`,
   Paul has NOT ruled it. Treat as a proposal to put to him, not a procedure to execute.
3. **`cycle/release/CYCLE-MAP.md`** + **`CYCLE-LOG.md`** — the map and the chronicle. Lap 2's
   closing entry is the last `## Lap 2` heading.

## 3 · Next steps (ordered)
1. **Put the lap-3 procedure to Paul** (`PROCEDURE-PROPOSAL.md`). It reconciles the estate-manager
   loop, the staged pipeline, where the three sweeps fire, and his stated order. He rules it before
   the lap runs — his own standing rule is that a cadence is designed before it runs.
2. **Get J-c and J-d** — the last two open rulings. J-c: ratify or reverse the lap-state shape
   applied in `590a551` (the chronicle is now the source; `release-state.py:49` still hardcodes the
   old assumption). J-d: colour precedence, account accent vs estate theme.
3. **Reconcile the three charters** before any seat is asked to weigh in — see Guardrails. One edit:
   *criticality WITHIN a lane, with evidence, is advice; ranking ACROSS lanes is Paul's; no seat decides.*
4. **Build + prove the three deterministic sweeps.** `tools/watch-accounts.py` and
   `tools/watch-feedback.py` exist; the CONSOLIDATION half is designed and unbuilt
   (`.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md`); health is
   `~/.claude/tools/health-probe.py --only fernwood`. ⭐ **E1 (feedback plumbing) is the precondition
   for the census being complete** — until it runs, the census cannot know what it is missing.
5. **The maturity grading.** `practice-steward` owns the rubric (stage-entry criteria = method);
   `product-steward` applies it per row. ⭐ Grade the **V1**, not the whole feature (§8), and a
   `v1-ready` row must NAME WHAT IT DEFERS.
6. **The zone scoping session** — its own focused session. Scope zone work AS A FEATURE: what it is,
   concepts, journeys, how it evolves. ⛔ Produces concept → design → journey and **NO production
   release**; it is the named test case for whether a lap can advance a stage and ship nothing.
   Start from `.plans/2026-09-06-maps-and-zones-PROPOSAL.md` (812 lines, **unread by anyone**).
7. **Mom's guided visit** — GAP 2 first (~5 min, before any UI is opened), then GAP 1 (~20 min, on
   HER phone). Exact protocol in briefing §2. Unblocked: Paul ruled the freeze does not follow her.
8. **The safe process changes** from the retro, not yet applied: a real step list for the returning
   journey · gate ① printing its coverage intersection (counted, never graded) · `product-steward`
   re-deriving `measured` numbers before they are written.

## 4 · State & pointers
- Repo `~/Developer/Tate-Tracker` @ `53c3446`, **main, clean — no uncommitted work.**
- Production `fernwood-home.pages.dev` serves **`1e2748d`**; QA serves `fbd5072` and is **8 commits
  behind HEAD** (no app surface changed). Verify with `journey-walk.served_sha`, never by assumption.
- Lap 2 **CLOSED**. `momlib.lap_outcomes('cycle/release/CYCLE-LOG.md')` now returns **2** (was 0);
  siblings unchanged at mom 8 / fleet 3.
- Production accounts: **one** — `pkirsch` / `p-yjnw9lt41nww`, place *Grant Park Condo*, estate
  `est-e6696a`. Mom's invite `p-b91e4d` **minted, sent, still unspent.**
- The seven panel files are listed in briefing §6. Raw input: `2026-09-07-lap2-CLOSE-HANDOVER.md`
  and the two `lap3-paul-feedback-CAPTURE*.md` files.

## 5 · Guardrails
- ⛔ **Three charters currently forbid what Paul asked for in J-b.** `user-researcher` (does not
  pitch features), `practice-steward` ("may never say one item matters more than another"),
  `product-steward` ("may not RANK anything"). **Do step 3 before asking any seat to weigh in on
  criticality**, or you are asking a seat to break its own foundation.
- ⛔ **Do not build any acknowledgment mechanism for Mom's 23 zones.** Z-ACK is closed — Paul
  discharges it in person. No ribbon, no card, no surface. Do not let a sweep re-raise it.
- ⛔ **Nothing is pre-filled into Mom's account.** She starts blank; that is what preserves the 23
  hand-traced zones as the answer key. Irreversible if broken.
- ⚠️ **A green gate can be structurally meaningless.** Lap 2's gate ① printed 4 of 4 while the
  intersection of "can test a placed household" and "had undegraded data" was EMPTY. Read the
  coverage, not the verdict.
- ⚠️ **39 of 39 lap-2 walks ran `--fresh`** — no seat has ever arrived as a person who already
  exists, which is why the lap's worst defect was invisible to the harness.
- ⚠️ Walks need `--fresh --watch`; wait ~25 s after a QA deploy before walking.
- ⚠️ `cycle/release/cycle-state.json` is rewritten by the post-commit hook every commit — **restore
  it, never commit it.** Scope commits: `git commit -- <paths>`.

## 6 · Done when
Lap 3's procedure is ruled by Paul; the three sweeps run and are proven; the maturity grading has
assigned every census row a stage; the zone scoping session has produced concept → design → journey
with no production release; and — at the commitment point, **not before** — the options list is built
extensively from a census whose gaps have been filled. Paul's words: *"the options list we should
build more extensively once we are in lap three and have collected all the feedback and input and
data that's out there."*

## 7 · Un-sealed judgment
- **The mint band.** Paul saw a mint band and stale-looking chrome at the top of his walk. Mechanism
  is CONFIRMED in source (`viewer.html:6421` gates `__HOUSEHOLD_NAME`, which eleven places use as
  "is this a household at all"; a stale owner stamp drops it and restores the pre-ruling surface).
  The specific link to the mint band is **strong inference, not measured** — falsifiable in ~1 min
  by re-creating a mismatched `fw-onboard-owner` and reloading.
- **`coordinates` absent on Paul's account.** Explanation — his account was created 11:16 ET on
  `c821051`, W0 geocoding reached production 17:15 ET on `1e2748d` — is `inferred`, **UNTESTED**.
  Predicts that re-saving his address populates it. Note `viewer.html:7312` also gates
  `adoptHouseholdCoordinates()` on the same owner stamp, so this has **two independent causes**.
- **My own count of `.expanded` writers was wrong twice.** Do not quote a count here without stating
  the predicate; three independent counts disagreed tonight.

## 8 · Trust status (per open item)
**Human-cleared by Paul (2026-09-07):** the lap-2 clear itself · J-a (no freeze follows Mom) ·
J-b (Paul ranks; seats advise in lane) · J-e (closed until something filters) · J-f (keep for
reference, Mom starts blank) · J-g (the session scopes breadth) · Z-ACK (in person) · the v1 rule ·
that zone work is a lap-3 priority · Open-Meteo proxy approved.

⛔ **Model-flagged, NOT cleared — do not treat as fact or as decided:** every finding in the seven
panel files, including the whole engineering path-eval A–F (A2, D1 etc. are RECOMMENDATIONS);
all 15 UX findings and the proposed synthesis line; every drafted copy line; the AI boundary table
and its order-not-membership rule; the retro's ranked process changes; the entire 47-row census and
its concept/defined split. All carry `ready: agent-proposed — Paul rules`.

⚠️ **Also uncleared:** the two knowingly-shipped defects fixed in `4a3a61b` are on main and **have
never been walked** — the gate is per-sha, so that commit needs a round to certify.
⚠️ `second-viewport` **cannot be discharged** — viewport is hardcoded at `journey-view.py:64` with
no flag, so it would read open forever regardless of how many laps run.
