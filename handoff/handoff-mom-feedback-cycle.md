# Handoff: mom-feedback-cycle

<!-- generated 2026-07-26 ~2:15 PM ET · sources: Tate-Tracker@3cb30f9 (clean) · ~/.claude@e149907 (⚠ dirty: settings.json, settings.local.json, plans/calm-churning-locket.md — a CONCURRENT SESSION's, not this thread's, do not touch or commit them) · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1. Mission

Execute the remaining Fernwood Mom-feedback-cycle work — **and before executing, rationalize the backlog.** Paul's words: make sure *"we're doing this the most effective, efficient way."* The design decisions are all made and ratified; what's left is build, plus a hard look at whether the backlog is shaped to be built from at all (it is **342 lines / ~98 rows** and grew again today).

**Do the rationalization first. It is not a warm-up — it is the first deliverable.**

## 2. Read first

1. **`BACKLOG.md`** — the whole file, but especially **A1** (retired gate + the replacement metric table), **A2** (moss, the Japanese-practice thread), **A3** (the "FIX THE ASK" row, the replacement-card slate, the loop-closes row), **A6** (corpus→RAG, conversation browse, the Guru bug), **B6** (household systems).
2. **`CLAUDE.md`** → the **"Mama's Perspective"** section end-to-end. It gained four standing rules today: the channel doctrine (app is the feedback mechanism, text is not), the `MOM_ACK_DATA` freshness duty, the ribbon copy rules, and the **AI-boundary amendment** (ingress + quarantine).
3. **`.engineering/2026-07-26-mom-cycle-determinism.md`** — engineering-partner's ranked punch list and the 10-site asserted-vs-derived inventory. **This is the build spec for step 3 below.** Its companions: `.ai-advisor/2026-07-26-feedback-cycle-boundary.md`, `.ux-reviews/2026-07-26-feedback-loop-visibility.json`, `.content/2026-07-26-feedback-loop-voice.md`.
4. **`.private/2026-07-26-mom-feedback-synthesis.md`** + **`.private/2026-07-26-mom-feedback-return-leg.md`** — user-researcher. **Gitignored and must stay that way** (see Guardrails).

## 3. Next steps (ordered)

1. **RATIONALIZE THE BACKLOG (do this first, report before building).** It's ~98 rows across three tracks and Paul has asked twice today for better tracking. Specifically: fold the duplicate/adjacent rows (the bloom items in A3 overlap the replacement-card slate; W9/soilNotes appear twice); mark what today's decisions **closed** rather than leaving them readable as open; and surface the handful of rows that are actually *next* versus the long tail that is a reference archive. **Do not delete history — reshape for legibility.** Then say plainly whether the ordering below is still the efficient one, and change it if not.
2. **Derive the punch-list from canon** (~1h) — `tools/read-mom-feedback.py`. Three buckets: *Ready to fold* / *Already settled* / *Can't verify automatically*. Probe must resolve `entityRef.type` → file (three live cards point at **weeds**, not plants). Where no probe exists (the 'Annabelle' roster fold), print the assertion **labelled as an assertion** rather than faking a probe. **This is the bug that produced a wrong claim in four artifacts today** — and the principle promoted for it (`~/.claude/ai-playbook/cross-cutting/provenance-and-gates.md`, "Derive the to-do from the record") now binds on exactly this fix.
3. **Scope the watermark to what was actually folded** (~30m) — `tools/fold-answer.py:198` calls a bare `--mark-reviewed`, which stamps the max ts across **every record in view**. Fold one card and an unrelated, unfolded answer stops being "new" **permanently**. Only data-loss-shaped path in the cycle. Fix before anything else touches that tool.
4. **`tools/check-mom-ack.py` + an `acknowledgedThrough` field** (~2h) — makes ack staleness computable. Thresholds (user-researcher): **R1** `today − answeredOn`, 🟢≤3d 🟡4–7d 🔴>7d, **ping on amber**; **R2** unacknowledged arrivals, any ≥1 surfaces, oldest >72h red; **R3** specificity boolean. Reads `/api/feedback` + `/api/observations` + `/api/zone-audio` — **there is no text ledger and none is planned.** Also exit 1 when `viewer.html` is committed-but-not-pushed (CLAUDE.md says shipping means a push; four lines). Offline → run the local half, exit 0.
5. **Widen `tools/mom-queue-watch.py`** to "unacknowledged input" (~30m) — it was silent on 7/26 because it watches *folds*, and she gave input through three non-fold channels.
6. **`tools/momlib.py`** (~1.5h) — rule-of-three has fired: three copies of the `_load()` hyphen workaround, three definitions of "pending". Do it *while* doing 2–5 so they land on one definition instead of adding a fourth.
7. **Reframe the bloom cards** — fix the template **once** in `tools/harvest-questions.py`; it corrects 8 live/staged cards. Shape (content-steward): *"The **X** — we have it down to flower around now, though we've never actually watched it here. **Is it in flower yet?**"* Plant is the subject; the hedge is *the record's gap*, not a request for her verdict; "yet" makes "Not yet" a fact about the season.
8. **Raise the moss confirm card** — observation-shaped only (*what does it look like*, never *which species*). Moss is the best first card: she planted it, she's the expert, the app is the novice.
9. **Research threads, lower priority** — pond water + Japanese moss/niwaki into `research-resources.md` as curated depth (A6/A2). Note the strategic tie: this is the RAG substrate, and the tool-use migration is what makes it payable.

## 4. State & pointers

- **Repo:** `/Users/paulkirschenbauer/Developer/Tate-Tracker` @ `3cb30f9`, **clean, pushed**. 17 commits this session.
- **Live surfaces already changed today** (all verified live, not assumed): Worker `3d230628`→ later deploys; Pages serving the new ribbon, the `Machines` card, `"I haven't looked"`, the chip byline. **Worker deploy is now the agent's job** — `bash tools/deploy-worker.sh` **with the Bash sandbox disabled**; done when `/health` passes.
- **Pages lags a push by ~1 minute.** Poll `https://palekxk.github.io/Tate-Tracker/viewer.html` for your string before claiming anything shipped.
- **Task tracker** is live in this session's task list (14 items). It does **not** survive the window — the backlog is the durable copy, which is part of why step 1 matters.
- **`~/.claude` @ `e149907`** holds the three promoted principles. Its dirty files belong to a concurrent session.

## 5. Guardrails

- **This repo is PUBLIC.** Mom's verbatim words about *herself* live only in `.private/` (gitignored). Her feedback about the *app* may be quoted. **Scan before committing anything that quotes her** — this was nearly published once today and caught pre-push.
- **AI boundary (amended today):** ingress — *Paul relays, the model does not fetch*; no automatic read of her messages, ever. Quarantine — model output derived from her words about herself never leaves `.private/` and never reaches her.
- **Anything whose wording reaches Mom is Paul-confirmed before it ships** — card prompts, button labels, ribbon text, Almanac entries. Propose; don't finalize. Shipping = a push (Pages), not a commit.
- **Canon promotion from her words stays Paul's call.**
- **Never run `check-data-inline.py --fix` blind.** It will land an **un-landed draft `house` zone** that is deliberately still showing as drift awaiting Paul. Use `tools/reinline.py` for a single const instead.
- **`vehicles.json` filename is deliberately NOT renamed** despite holding three groups — same call CLAUDE.md made for `tate-tracker`. Don't "fix" it.
- **Ribbon:** never repeat the same closing phrase two refreshes running; adopt her words, never improve them.

## 6. Done when

Steps 2–6 are shipped, tested against real data, committed and pushed; `check-mom-ack.py` runs at session start and correctly reports 🟢/🟡/🔴; `read-mom-feedback.py` can no longer list an already-folded item as pending; and **the backlog has been rationalized with the result reported to Paul.** Steps 7–9 may remain open.

## 7. Un-sealed judgment

- **The efficiency question Paul actually asked is not answered yet.** My read: the backlog has become a *record* rather than a *worklist*, and today added to it faster than it closed. The honest move may be splitting it — a short "next" surface and a long archive — but that risks a third tracker, which the State Contract warns against. **Worth thinking about properly rather than inheriting my instinct.**
- I'd sequence **3 before 2** (data-loss before wrong-list) even though engineering-partner ranked 2 first as the cheapest.
- **ux-expert's F6 is unresolved and I think it's right:** the queue already says *"No wrong answers, and no rush"*, and it is the faintest text on the surface while the buttons below structurally contradict it. Don't answer that with better copy.
- The **free A/B is now live and clean** (`q-clematis-variety` identification-shaped vs `q-weed-stiltgrass` observation-shaped, one variable apart). **Don't touch either card** until she answers one — it's the cheapest evidence available.

## 8. Trust status (per open item)

- ✅ **Human-cleared:** the A1 gate history (I verified line 138 vs line 142 in the 7/13 source myself) · all three of Mom's confirms already folded (checked against canon) · the `renderVehicles` negative-filter bug (read the code) · Guru's elevation error (scanned all 25 assistant turns; 2,959 correct ×2, 2,800 wrong ×2) · the pond-filter and moss-slurry horticulture (web-verified before it entered canon) · attribution of the Guru questions to Mom (Paul stated it; her 8:59 AM text corroborates).
- 🟡 **Model-flagged, NOT cleared:** every metric threshold (R1/R2/R3) is an agent's proposal Paul has not sat with · the claim that the insecurity is *situational not dispositional* is one morning's evidence, n=1 · the moss `variety` is `inferred` and **askable** by design · content-steward's three unpromoted principles are proposals, not doctrine.
- ⚠️ **Do not treat as fact:** anything in `.private/` describing Mom's state of mind is *her words in one conversation*, not a validated user model.
