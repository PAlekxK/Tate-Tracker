# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Session-start check — is the dashboard showing all of canon? (run at every Fernwood pickup)

**Run these first thing when picking up Fernwood, before other work:**

```bash
python3 tools/check-domains.py             # does every domain still conform to the ONE manifest?
python3 tools/check-data-inline.py         # viewer.html inlines vs source JSON
python3 tools/check-digest-fresh.py        # Garden Guru's digest vs source JSON
python3 tools/check-mom-ack.py             # is the ack ribbon current, and did it ship?
python3 tools/check-cards.py               # does the SERVED card queue match reality?
python3 tools/rationalize-bench.py         # is anything we're serving OUT OF SEASON, and what's on the bench?
python3 tools/read-mom-feedback.py --pickup # Mama's Perspective — the Mom-check counter (ALWAYS one line) + her NEW answers and anything unanswered
python3 tools/read-feedback-sections.py    # WHICH DOOR she came through — decline vs. misunderstanding
```

**⭐ Mom's feedback is checked FIRST, before current state (Paul, standing, 2026-07-29):** *"every time
that we initialize around the Fernwood tracker, we should check for feedback from [Mom] — that should
be part of our first step, and current state."* That is what the block above is; run it before
anything else, not after picking a thread.

**⭐ The Mom-check counter — one line, every run, quiet days included (Paul, 2026-08-02).** `--pickup`
used to be **silent on the happy path**, which meant *"nothing new"* and *"nobody has looked in nine
days"* printed the same thing: nothing. A quiet watcher and a dead one are indistinguishable in a log.
So it now always prints `🌿 Mom-check — last checked N days ago · her last answer <date>`, with a ⚠️
once the gap reaches 7 days, and stamps `lastCheckedAt` in `.private/mom-feedback-state.json` on every
run — so the number measures **the gap between sessions that actually looked**. Run it in any session
that touches this repo, not only a formal pickup. *This is the deliberate replacement for wiring
`mom-queue-watch.py`'s email path* — Paul's call: *"a counter that tells us when's the last time, a
reminder to nudge us… that's just simpler than trying to do something super automated."* The email
code stays in place, unconfigured, and is **not** to be "fixed" (see the docstring on `notify_email`).

*(Occasionally, and after any change to a feedback channel: `python3 tools/test-feedback-cycle.py` — proves a note can't be captured and then silently lost. `--live` also exercises the real POST path.)*

`check-data-inline.py` compares the source JSON (`plants.json`, `mammals.json`, `birds.json`, …) against the inlined `*_DATA` constants in `viewer.html`. Exit 0 = in sync (say nothing, move on). Exit 1 = **drift** — surface it.

`check-digest-fresh.py` compares `worker/digest.json` (bundled into the Worker at deploy — Garden Guru's context) against a fresh rebuild from the source JSONs. Exit 0 = fresh; exit 1 = **stale digest**, meaning Guru is serving outdated data because a source changed but the digest wasn't rebuilt + redeployed (this happened 2026-07-07: plants + fishing were stale three days). Fix: `python3 tools/build-digest.py && (cd worker && npx wrangler deploy)`. Non-mutating — it restores the on-disk digest after checking.

The drift that matters most is **canon-ahead**: a species present in the JSON but *missing from the inlined data*. That almost always means **Garden Guru added it to canon but the re-inline step didn't land**, so a real, confirmed addition is sitting invisible on the dashboard. This is exactly how **Lizard's Tail** hid unnoticed until 2026-07-05.

When drift shows, don't auto-fix — the point is a **human signal that the addition is legit**:
1. Surface the specific species to Paul, framed as "added to canon (likely via Garden Guru) but not yet on the dashboard — legit?"
2. Get Paul's confirm that it's a real addition (his call, not an automatic one).
3. Only then `python3 tools/check-data-inline.py --fix`, verify clean, add a release note, commit.

(Root-cause fix still open: make Guru's promote flow verify its own re-inline commit landed, so this drift can't open silently in the first place.)

`rationalize-bench.py` (built 2026-07-31) answers **"is anything we are asking her right now out of season?"** and manages the **bench** — the cards drafted but not yet serving. It is in this block rather than run on demand for the reason the block exists at all: **a flag nobody reads is the same as no flag.** `harvest-questions.py` computes "is this bloom window open?" when it *drafts* a card and never again, so a card's freshness was measured once, at birth, and every later reader inherited that verdict as current. On the day it was built it found `q-lizards-tail-bloom` hours from asking Mom *"is it in flower yet?"* about a plant with no window for the next ten months, and `q-clematis-variety` sending her to read a flower colour on a day the vine had none.

Three things to know before acting on its output:
- **Paul's clear gate is the whole design.** `--apply` promotes ONLY cards carrying an `approvedForServe` stamp, and nothing writes that stamp except `--approve <id>`, run by a human. An agent may run the report freely; an agent may not approve a card. Multiple supply streams feed the bench (harvest-created · surfaced from her feedback · hand-slotted) and each will grow its own approval rules — this gate is the floor under all of them.
- **`MAX_VISIBLE` stays 5 and variety is a HARD constraint** (Paul, 2026-07-31). The five are *a sample of what she can influence*, not a workload — so diversity is a **filter** over the ranked list, not a tiebreaker. A pure information-value sort would stack all five slots with bloom cards, which scores well and says exactly the wrong thing.
- **It flags; it does not hide.** Fail-open is deliberate: only a *measured* closed window may say "do not serve," and the bloom-gated-by-wording case (`q-clematis-variety`, whose `_foldTarget` is `variety` but whose observable is the flower) is a **heuristic** reported as REVIEW for a human. Wrongly hiding a card loses an answer silently; wrongly showing one costs a line in a report someone reads.

**Seasonal deactivation and the bench are the same mechanism.** To rest a card whose window has closed, set `active:false` and add a `_seasonHold` note — deliberately *no* `resolvedAt`, which would mean folded-and-retired. It lands on the bench awaiting approval and the season check re-offers it when its window reopens. A card needs no separate hibernating state (`q-lizards-tail-bloom` is the worked example).

`check-mom-ack.py` answers the one question the loop's third leg depends on: **does the acknowledgment ribbon still cover what she's given us, and did it actually reach her?** It compares `MOM_ACK_DATA.acknowledgedThrough` (added 2026-07-26 — the field that makes staleness *computable* instead of unanswerable) against the newest input across every **app** channel: `/api/feedback`, `/api/observations`, `/api/zone-audio` **and `/api/conversations`** (Guru turns — metadata only, never turn content). Exit 0 = silent. Exit 1 = she is owed a line, or `viewer.html` is committed-but-**not pushed** — which matters because CLAUDE.md already says shipping means a push, and a ribbon Paul wrote and didn't push is exactly as stale to Mom as one he never wrote. **It never writes the message and never advances the clock on its own** — it computes *that* she is owed a line and *what evidence* exists; Paul writes the words (the AI boundary; a template can only produce "thanks for your feedback," which is worse than silence at the moment she's doubting herself). Attribution is never asserted — a deviceId is a browser bucket, not a person — so if the uncovered input was Paul's own test tap, `--acknowledged-through <ts>` clears it in one command, stamping the clock only.

*(Documentation note, 2026-07-26: BACKLOG A1·R2 lists three channels and places Guru turns in `/api/observations`. That's wrong on the plumbing — Guru conversations live at `/api/conversations`, observations are the field-note log. The check reads both, because the failure that motivated it — an 8-day-stale ribbon while she asked Guru two real questions — is invisible without conversations. Still **no text ledger**, and none planned.)*

`read-mom-feedback.py --pickup` surfaces the ground-truth Mom has settled in **Mama's Perspective** since Paul last reviewed (it reads the Worker's `/api/feedback`; token from `.private/fernwood-token`). Prints a short "N new answer(s)" block with a drafted **ready-to-fold** canon edit per Yes/No answer, or **nothing at all** when there's nothing new (calm, no-noise — matches the app's tone). It **never writes canon** — promotion into `plants.json` (flip a variety's `confidence` inferred→verified, or correct it to what she said) stays Paul's call. When Paul has folded her answers in, run `python3 tools/read-mom-feedback.py --mark-reviewed` to advance the watermark so they stop showing as new. (Note: the viewer now reconciles answered questions against the Worker on load, so a Yes/No answer stops being served on all of Mom's devices automatically — `active:false` in `questions.json` is now just housekeeping, not required to stop re-asking her.)

## ⭐ Four standing rules from 2026-07-29 (Paul-stated) — read before touching her surfaces

1. **ONE affirmative grammar, everywhere she taps.** *"The cue and affirmative styling, we should make
   it consistent and a consistent signal of we hear you, and we've recorded your information … let's
   make it simple and consistent for mom."* Affirmative = filled green + ✓ (`gg-suggest-btn-yes`);
   secondary = the outlined neutral. (The ratified part is the FILL + GLYPH grammar; the shape around
   it became the v2 one-shape stacked rectangle on 2026-08-02 evening — Paul's call from staged
   exhibits, doctrine at the top of viewer.html's stylesheet.) The ribbon's buttons are **literally those components**, not
   lookalikes, so they cannot drift. **This REVERSED BACKLOG Tier-1 #4**, which wanted "Got it" and
   "That's all of them" made *more* different because they mean different things. They do — and one
   learnable signal still beats two precise ones she has to tell apart. Consistency outranks semantic
   precision on Mom's surfaces. Don't re-differentiate them without asking him.
2. **The ribbon covers EVERYTHING since the last one she gave input on, each phrase linked** to where
   she can see it. `MOM_ACK_DATA.links = [{phrase, card}]` — many, not one. A phrase that is no longer
   in the message is skipped rather than rendered as a dead control.
3. **The card queue is ordered by INFORMATION VALUE TO US**, and position IS priority
   (`outstanding()` does `.slice(0, 5)` on declaration order — card 6 renders to NOBODY). Axis, in
   `questions.json._ordering`: an answer that unblocks a BUILD > one that fills a canon gap > a verdict
   on our own guess. Before pushing a card out of the visible set, **check it is unanswered** — an
   answered unprobeable card pins the feedback watermark.
4. **Check her feedback FIRST at every pickup** — see the session-start block above.

⚠️ **And the standing verification rule this session earned the hard way:** three BACKLOG rows were
checked against the running app and found **wrong** — a card count that ignored `SUPPORTED_KINDS`, a
"no label at all" that was true of the JSON but false on screen (the viewer defaults `later`), and a
"190px" that measured 431. **Verify a row against the app before acting on it, and correct the row
rather than quietly fixing past it.** A wrong SSOT row is this repo's most repeated failure.

## Mama's Perspective — the ground-truth feedback loop (built 2026-07-14)

**⭐ The disposition half now has a ritual: `/mom-cycle`** (`~/.claude/skills/mom-cycle/SKILL.md`, 2026-07-29 — Paul-stated). The tools below detect and protect her input; the Skill decides what happens to it — triage → **resolve ambiguity in the cheapest place (telemetry → Paul → only then Mom)** → one expert seat → ship the non-Mom-facing wins → draft the return leg (a **dated** ribbon + at most ONE clarifying card) for Paul's gate. It never sends. Run it when `read-mom-feedback.py --pickup` surfaces anything. It is deliberately early — every run appends to its Refinement log.

A queue of small confirm-cards at the top of the app asking the ground-truth only someone standing on the property can settle. Full lifecycle + tools:

- **Seed / reseed** — `tools/harvest-questions.py` reads the canon's own honest-uncertainty markers (`variety.confidence != verified` & `askable`; `bloom.confidence == inferred` & in-window-now) and DRAFTS candidate cards. It never serves one: candidates are `active:false` until Paul flips them (his gate). Card types: variety-confirm, bloom-confirm, and hand-authored **reflective** cards (a "would you like…" strategy/preference question answerable from anywhere — `_kind:reflective`, no `_foldTarget`, captured as preference, never folded).
- **Serve** — `MomQueue` in viewer.html. Soft-capped at 5 visible (`MAX_VISIBLE`, Paul's call 2026-07-14); per-question button `labels` (variety "Looks right", bloom "It's out/Not yet", strategy "Yes I'd like that") + `correctionPrompt` gates the "what is it?" follow-up to ID cards only; durable cross-device dismissal via `syncServerAnswers` (reconciles answered ids from `/api/feedback`).
- **Answer** — her tap + optional verbatim note → `POST /api/feedback`. DETERMINISTIC, AI-FREE. `firstOfferedAt` rides along for offer→answer latency (novelty-vs-durable).
- **Read** — `tools/read-mom-feedback.py --pickup` (wired into the session-start check above) surfaces her NEW answers + the punch-list; watermark in `.private/mom-feedback-state.json`; token in `.private/fernwood-token`. **⭐ The punch-list is DERIVED FROM CANON, not from the answer record (fixed 2026-07-26).** It prints four buckets — *Ready to fold* (card live, canon still `inferred`) · *Retire the card* (canon already settled, so the card is asking something we know) · *Already settled* · *Can't verify automatically* — and only the first is a to-do. Where no generic probe can see the fold (the 'Annabelle' answer landed in the hydrangea **roster**), it prints the claim **labelled as an assertion** rather than faking a probe — an honestly-unsure tool beats a confidently-wrong one, the same doctrine the app itself runs on. The probe resolves `entityRef.type` → source file, so a **weed** card reads `weeds.json`; it used to assume plants and silently degrade three live cards. *Why this was load-bearing: the old version listed every answered confirm as "ready to fold" regardless of canon, and on 2026-07-26 reported three of Mom's answers as pending when all three had been folded days earlier — a phantom that propagated into `BACKLOG.md`, a researcher brief and three agent reports before anyone checked. This is `[[Derive a gate's pending-count; don't list it]]`, which had been promoted cross-project on 2026-07-01 and never reached this loop.*
- **⚠️ The watermark never steps over an answer that still needs you (fixed 2026-07-26).** `--mark-reviewed` used to stamp the max timestamp across **every** record in view, and `fold-answer.py` called it after folding *some* — so folding one card made an unrelated, unfolded answer of hers stop being "new" **permanently**. It was the only silent-data-loss path in the cycle. Now the stamp is clamped below the oldest still-actionable answer, and `fold-answer.py` passes `--mark-reviewed-through <max ts of what it actually folded>`. **The one state that can't clear itself is `unprobeable` (2026-07-27)** — a reflective card has no `_foldTarget` *by design*, so canon can never say "handled" and the card holds the ceiling until a human **retires it** (`active:false` + `resolvedAt`). It stays actionable (burying her preference would be the same silent loss), so instead every surface that shows it — the punch-list line, the `--pickup` block, the watermark's own "held back" message — **names the card holding the ceiling and the retire action that releases it**. Guarded by the PIN leg in `test-feedback-cycle.py`.
- **The shared definitions live in `tools/momlib.py`** (extracted 2026-07-26). `question_state()` is **the** answer to "what counts as settled?" — one function to read instead of four tools disagreeing. Three copies of the same `_load()` shim and three definitions of "pending" had already produced divergent behaviour and a real wrong claim. Anything new in this loop imports it rather than re-deriving.
- **⭐ `momlib.ENTITY_SOURCES` is THE entity-resolution map (collapsed 2026-07-27).** `entityRef.type` → (canon file, list key, viewer const). "Assumed plants" shipped broken three times in one day — `fold-answer.py`, `read-mom-feedback.py`'s probe, and `buildCard` — and **none of them failed loudly**; a weed card just resolved to nothing, which is how `q-weed-stiltgrass` was served for six days with a photo Mom took rendering nothing. All the Python now reads that one dict. **JavaScript cannot look a `const` up by name**, so `buildCard`'s `ENTITY_DATA` is the one irreducible copy — but it is no longer agreed by hand: `momlib.viewer_entity_map()` *reads* it, `entity_map_divergence()` derives the comparison, `check-cards.py` reports it once up front, and `test-feedback-cycle.py`'s RESOLVE leg fails on a missing type, a wrong const, or an unreadable binding. **Adding a domain = those two places, nothing else — never a third map.** (Still plants-only by design: `harvest-questions.py`, a *producer*. Wiring it to the shared map would serve new cards to Mom — Paul's call, see BACKLOG Track C.)
- **Fold** — `tools/fold-answer.py`: drafts the canon edit (confidence inferred→verified), Paul approves, it applies + re-inlines `PLANTS_DATA` (`tools/reinline.py`, the side-effect-free path) + retires the card (`active:false` + resolution) + advances the watermark + (`--deploy`) rebuilds digest & deploys. A "Not quite" prints her correction for hand-application (an ID change is a judgment call). **Before folding, check the target's CURRENT canon confidence** — a card can be stale-premised (run 1's was). **The fold step also updates `MOM_ACK_DATA` in viewer.html** — the standing top-of-queue acknowledgment ribbon ("We got your feedback on … — keep it coming!"), never cleared, only REPLACED by the next fold (Paul's design, 2026-07-22).
- **Assess** — every real answer worked through the loop gets a dated run section in `.engineering/2026-07-22-mom-loop-first-run.md` (the running assessment log — Paul's standing instruction, 2026-07-22). Run 1's findings live there: stale-premised cards, pre-automation `_foldTarget` gaps, the variety-specific punch-list template, UTC date display.
- **⭐⭐ THE APP IS THE FEEDBACK CHANNEL. TEXT IS NOT (Paul, 2026-07-26 — standing).** Mom's feedback comes through Fernwood: the confirm queue, the open-standing card, Garden Guru, zone voice. **Her text messages to Paul are NOT an official feedback channel and are not treated as one.** Paul's goal is to bring her into the app, and a parallel channel that quietly works just as well removes the reason to. Two rules follow:
  1. **No automatic check of any kind.** No sweep, no watcher, no scheduled read of her messages. **An agent does not fetch her words — Paul relays them, or they are not in the system.** *(This is the same line ai-advisor independently proposed as the boundary's ingress clause; Paul reached it from the product side and it is now doctrine, not a proposal.)*
  2. **Paul-relayed input is real input** — when he passes something along directly, it counts, gets folded, and gets acknowledged like anything else. What is excluded is the *automatic harvest*, not his judgment.
  - **Consequence for the metrics:** "arrivals, any channel" means **any app channel, plus whatever Paul hands over**. The R2 unacknowledged-arrivals check reads `/api/feedback`, `/api/observations` and `/api/zone-audio` — **there is no text ledger and none is planned**, so nothing in the mechanism may depend on one. *(The 2026-07-26 iMessage read that produced `.private/mom-feedback-2026-07-26.md` was a one-off at Paul's explicit request, not the start of a practice.)*
  - **The honest cost, stated once:** today's richest findings arrived by text. Closing that channel means **the app has to earn that input instead** — which is precisely why the card re-shaping and a ribbon that actually answers her are the load-bearing work, not nice-to-haves.
- **⭐ Keep `MOM_ACK_DATA` FRESH — it is feedback *to her*, not a fold artifact (Paul, 2026-07-26).** The standing ribbon exists to tell Mom **we heard you**, so it must reflect **her latest input, through any channel** — a fold, an answered card, a Guru question, or something she texted Paul. **Refresh it whenever she gives real input; do not wait for a fold.** *(Original 7/22 design tied it to the fold step alone; that left it 8 days stale, still naming the panicle hydrangea, while she was actively contributing moss, a household-systems idea, and two Almanac questions — the exact week she told Paul she doubted whether her answers were any good. Staleness here is the opposite of the intent.)* **Name what she actually gave**, specifically — a generic "thanks for your feedback" does not tell her she was heard. **Adopt her words, never improve them:** she coined "household systems," hedged that it might be wrong, and was right — the ribbon initially said "the house's own systems," which for a reader whose fear is *getting words wrong* silently corrects her. If she names a thing, that is its name. **Vary the close, and never repeat the same closing phrase two refreshes running** (Paul, 2026-07-26): the first refresh kept "Keep it/them coming!" from the previous one, which makes the *ask* the recurring furniture and reads as a quota to someone looking at 33 unanswered cards. The queue sits inches below the ribbon and is already the ask — an acknowledgment does not need one. Gate: it reaches Mom, so **the wording is human-confirmed before it ships**, and shipping means a push (Pages serves `viewer.html`), not just a commit.
- **⭐⭐ CAPTURE IS NOT A LOOP — every channel needs a LIFECYCLE, not just storage (Paul, 2026-07-26 — standing).** Her rainfall report was captured perfectly: POSTed, stored, returned by the API on demand. It still went unanswered, because a free-text note **had no state**. It was shown once while it was newer than the watermark and then aged out silently, forever. A confirm answer has a canon target we can probe; a note has nothing, so *"did we act on this?"* genuinely cannot be derived — and that is the one place an explicit assertion is the honest instrument. `feedback-log.json` records **where each note went** (never her words — this repo is public; the verbatim stays in the Worker). `needs-reply` is **actionable**, so the watermark can never bury an unanswered note, and it tracks *"we fixed it"* **separately from** *"she was told"* — because only the second one is the loop closing. Run `python3 tools/read-mom-feedback.py --address <id> --as "<where it went>"` when you act; add `--acknowledged` only once the ribbon names it. **The test is `tools/test-feedback-cycle.py`** — it asserts every leg (capture → surface → protect → escalate → close → release) plus a regression guard on the watermark bug. *The general rule: whenever a new input channel is added, it does not ship until a note arriving on it can be **surfaced, protected from the watermark, and closed**. Storage is the easy half.*
- **⭐ When she disbelieves a number, SHE is the instrument — and the number is probably wrong.** On 2026-07-26 she wrote that the 7-day rainfall was confusing and she didn't believe it. She was right by **14×**: the app was showing the ERA5 regional grid (0.14") while her own station had recorded **2.01"**, including 1.96" in one storm the ~10–25 km grid cell never saw. She was standing in that rain. Three lessons, all now enforced in code:
  1. **A measured signal must never be silently replaced by a modelled one on the glance.** `weather-bias.json` already said the grid under-reads precip here by ~24%, and `daysSinceMeaningfulRain()` already preferred the station as *"closer to ground truth at the property"* — and the dashboard strip printed the grid figure anyway, unlabelled. **Source-hierarchy is a correctness rule, not a presentation preference.**
  2. **Two numbers on one card that measure different things must say which is which.** The card carried three "week" figures (station `weeklyrainin`, which resets on Sunday; the rolling gauge total; the regional grid) and none of them was labelled. To a reader with difficulty that is not depth, it is a contradiction — and the honest conclusion is *the app is broken.*
  3. **An accumulator that resets is not a duration.** `weeklyrainin` read 0.02" on a Sunday two days after 1.96" fell, which made the headline announce a *"Dry stretch."* Nobody means "since Sunday" when they say week.
  - **Why this matters more than the bug:** *trust is the load-bearing emotion here.* She is the one person who can check the app against the actual sky, and she did. The cost of getting this wrong is not a wrong number — it is teaching the person whose ground-truth the whole project depends on that the record disagrees with her own eyes.
- **Visible close** — the provenance chip on the plant card (`renderVarietyRow`): a guess reads "our read from a photo"; once folded it flips to "confirmed on the ground · <month>". THIS is the loop-close (she sees her read become the truth of the place) — NOT a status tracker. `active:false` on a folded question retires it for EVERY device (questions.json is fetched fresh each load), the universal complement to per-device `syncServerAnswers`.

**Two retire layers:** `syncServerAnswers` (per-Mom, interim — stop asking her once she answers, even before folding) + `active:false` in questions.json (universal, final — gone for everyone once folded; fold-answer.py sets this).

**The AI boundary (ai-advisor, 2026-07-14; amended 2026-07-26 — Paul-ratified) — the one rule:** *AI never touches Mom's surface or Mom's words. It may only draft for Paul's approval on the way in, or analyze the record on the way out — Paul's eyes sit between the model and Mom, both directions.*

> **AMENDMENT, 2026-07-26 (two clauses).** The 7/14 rule constrained **egress** and was silent on **ingress** — it was written for a world where everything she said arrived through the app. That stopped being true, so:
> - **INGRESS — an agent may read only what Mom routed to the project.** *Paul relays; the model does not fetch.* No sweep, no watcher, no scheduled read of her messages or any other channel she did not send to Fernwood. **Paul reached this independently from the product side the same day** (see the channel doctrine above — the app is the feedback mechanism, text is not), so it is doctrine from both directions, not a safety hedge on a live practice.
> - **QUARANTINE — model output derived from her words *about herself* never leaves `.private/` and never reaches her.** Her feedback about the *app* is project material. Her account of her own uncertainty is not: it goes to a gitignored file, is referenced rather than quoted in anything tracked, and is never reflected back to her. *(This is the clause that was actually load-bearing on 2026-07-26 — her "I was insecure about my answers" was committed into a **public** repo before being caught and rewritten out of history pre-push. Nothing published, but only because someone looked.)*
> - Creep modes **(7)** an agent fetching her words from a channel she didn't route here, and **(8)** her self-description surviving into a tracked or Mom-facing artifact, join the six forbidden modes below. A card prompt is neither ask-path nor capture-path but a THIRD category — **authored content** — so the rule is "human-confirmed before it reaches Mom," not "AI-free" (Fernwood already AI-drafts authored content behind Paul's approval, e.g. promote-species). Forbidden AI-creep modes: (1) AI cleaning/classifying her note at capture — store verbatim; (2) AI auto-folding to canon; (3) AI phrasing reaching Mom un-gated / auto-reseed; (4) AI re-interpreting her tap ("Not sure but the note implies yes"); (5) AI generating the uncertainty markers themselves; (6) an "ask the Almanac" button on a confirm card (drags Guru onto the capture surface + affordance-without-signal). Card phrasing today = the deterministic template bank in harvest-questions.py, NOT AI (phrasing was never the bottleneck; revisit AI-draft-behind-the-gate only if the loop proves durable — >10 answered across reseed cycles). The one legitimate AI seat is a future off-device, read-only log-summarizer (build at ~15–20 answers, hypothesis-marked, may suggest-but-not-place seeds).

**Deferred pending signal (only n=2 real answers so far — honor [[feedback_defer_affordances_pending_signal]]):** the full "What you've settled" journal surface (content-steward drafted the copy) — the chip is the visible close for now; a standing settled-tracker risks the star-trap, so it waits for real engagement signal. Also deferred: dwell/note-opened metrics, retire-a-Not-sure-after-3-returns, AI-assisted card phrasing. Full panel trail: `.user-research/`, `.ux-reviews/2026-07-14-mom-perspective-loop-close-visibility.json`, `.engineering/2026-07-14-path-mom-harvest-fold-loop.md`, and the ai-advisor/content-steward returns.

## 📋 Canonical backlog → `BACKLOG.md`

**Live status for every Fernwood thread lives in `BACKLOG.md` (repo root) — read status there, not from the dated "Pickup point" log below (that log is historical, not current status).**

## Cross-project linkage — vehicles ↔ photo-organizer `[paul-stated 2026-08-03, "marrying more threads"]`

`~/Developer/photo-organizer` reads **`vehicles.json` IN PLACE** (never copies) to map repair/
in-process photos to `serviceHistory` entries — the **visual-journeys** thread (Bolores first,
then GTI/golf cart/the fleet). Two contracts follow: (1) every serviceHistory entry carries a
stable `id` (convention in the file's `_comment`; minted 2026-08-03) — external references are
`service:<vehicle-id>:<sr-id>`, so **renaming/removing an id breaks tags in another repo**;
(2) confirmed photo↔entry mappings live in photo-organizer's DB (its confirmations JSONL is the
durable copy), and any future vehicles-card photo display reads FROM there — this file stays
photo-free. Paul's review flow: he curates + describes what a photo shows (his words verbatim,
the primary evidence); the deterministic join proposes, he confirms. Long-horizon: part-level
tags → clickable exploded view; deferred per defer-affordances-pending-signal.

## Backlog fragments — folded into `BACKLOG.md` (2026-07-17)

The Mom-engagement backlog (shipped 2026-07-13 as **Mama's Perspective**) and the 2026-07-05 Concept-A items (Save/Ask split — resolved to one log-first button 7/13; `peakDates` + fishing granularity — shipped 7/06) now live in `BACKLOG.md`. Historical design trail: `.user-research/2026-07-13-mom-engagement-panel-synthesis.md`.

## Session log → `PICKUP-LOG-ARCHIVE.md`

The dated per-session **Pickup point** trail (2026-05-21 → 2026-07-14) is archived to `PICKUP-LOG-ARCHIVE.md` (git holds it regardless). Current status lives in `BACKLOG.md`, not the log.

## Project purpose & tone

Fernwood is a **personal property reference dashboard** for 282 Church Mountain Road, Jasper, GA 30143 — a rural mountain property at 2,959 ft elevation in the Blue Ridge, within Tate Mountain Estates. "Fernwood" is the property's name; "Tate Mountain Estates" is the surrounding 1920s mountain development, separate from the nearby town of Tate. It is hyper-personalized, not a generic app.

**Project rename history:** Originally "Tate Tracker" (named for Col. Sam Tate / Tate Mountain Estates); renamed to "Fernwood" on 2026-05-19 to name the actual property rather than the surrounding development. Repo path, GitHub repo, Worker URL, localStorage keys, and most internal var names retain `tate-tracker` / `tateTracker` for now — those are infrastructure-level identifiers, not user-facing, and renaming them carries data-migration risk (existing observations). Rename them only if a clear reason emerges.

**Tone is everything here.** This is a fun, evocative reference tool — a field journal, not a task manager. Language like "17 actions due" or "3 alerts" is wrong for this project. Prefer "What's happening in May" or "Worth checking this month." The dashboard should feel like looking out at the land, not a to-do list with deadlines.

## Governing design principle — the glance and the repository (2026-07-06)

The single most important structural principle for Fernwood. It came out of the 2026-07-06 fishing-section rework, corroborated independently by a ux-expert audit and a user-researcher journey. Every rich domain (plants, fishing, wildlife, weather, vehicles) must be layered this way, not flattened.

**Three strands:**

1. **The glance (decision layer).** A small, foregrounded, near-horizon read that answers "what's relevant to me *right now*?" — usually decision-shaped, driven by the freshest, most-localized data available. *Worth noticing this week* (plants), *is it a good time to fish today/tomorrow* (fishing). This leads. It is a **curated, time-relevant projection of** the repository, never a competing source.

2. **The repository (reference layer).** The deep, researched backing — care calendars, species phase tables, regs, historical temps, the full body of hyper-local research — held **in the parent card** as an on-demand store. It must exist (it's the credibility, and the depth a keen user drills into) but must **not flood the reader by default.** When a surface feels overwhelming, the answer is **relocate depth, don't delete it**: surface the near-horizon decision, shelve the rest one level down.

3. **The loop (invite + fold back) — the flywheel.** The glance is also the moment to **invite the one input only someone at the property can give.** Pair a fresh localized signal with a calm, timely call-to-action for ground-truth, and **visibly fold that truth back in.** The honest-uncertainty flag is the hook: the place we admit "~65°F, *estimated*" is exactly where we invite "log the real reading." This is the moat — anyone can show a grid forecast; only *this* property's accumulated ground-truth can't be commodity-matched, and it only accrues if the glance keeps inviting it. The virtuous cycle: **fresher local data → better glance → more trust → more input → fresher local data.** (This operationalizes the Phase-G "observations as a knowledge layer" thread with a concrete trigger.)

**Disciplines the loop must respect:** capture stays deterministic / **AI-free** (the invitation is on the ask-path; the logged reading is the user's verbatim ground-truth, see [[feedback_no_ai_on_capture]]); calm, not naggy (a field-journal *"seen it yet?"*, contextual + timely, **never a standing "add data" button** — that's the affordance-without-signal trap, see [[feedback_defer_affordances_pending_signal]]); and **close the loop visibly** (the user must see their reading replace the estimate or move the recommendation, or it feels extractive).

**Two ordering mechanisms** sit underneath this (promoted to `~/.claude/design-principles/cross-project.md`, 2026-07-06): **Freshness sets altitude** (order a surface by how live/local/actionable each signal is; position encodes recency) and **Source-hierarchy drives layout** (rank sources by evidence × freshness × actionability, and let that ranking drive presentation — for Fernwood: on-site station → forecast → season/phase-as-context → invisible research plumbing).

**Trust is the load-bearing emotion** (a confidently-wrong model is worse than an honestly-unsure one): keep *measured* signals visually distinct from *modeled* ones, and estimates legibly estimates at every altitude.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd ~/Developer/Tate-Tracker
python3 -m http.server 8765
# then open http://localhost:8765/viewer.html
```

## Release notes — update every release

**Every user-facing change ships with a release note.** When a release lands something Mom or Paul would notice on the dashboard (a new card, a new affordance, a visible behavior change), add a `## YYYY-MM-DD — Title` entry to `RELEASE_NOTES.md` (newest stays at top, field-journal voice, bullets describe what changed *for the user* — not the engineering), then run `python3 tools/build-release-notes.py` to re-inline `RELEASE_NOTES_DATA` (latest 5) into viewer.html. The "Recent updates" card renders it. Purely behind-the-scenes work (refactors, data plumbing) doesn't need an entry. If a release shipped without a note, backfill it.

## ⭐⭐ The domain manifest — how the record is organized, holistically (Paul, 2026-08-02)

**`momlib.DOMAINS` is THE declaration of every domain, and `tools/check-domains.py` is what stops it
drifting.** Paul's ask: *"a holistic structure that allows all these various files and categories of
content to be somewhat modular across, especially some of the capture surfaces that we're building.
And we want to limit how much they diverge as they continue to be enriched over time."* Full analysis:
`.engineering/2026-08-02-record-organization.md`.

**The finding that shaped it: the domains were already right.** A universal spine already existed
unplanned (`id`/`name`/`scientificName`/`emoji`/`photo`/`attribution`/`notes` in every domain), and the
five wildlife files are one schema wearing five filenames. Records answer four axes — identity, time,
action, honesty — and only **honesty** had diverged: weeds top-level, plants nested and partial,
vehicles per-value, **wildlife nothing at all across 64 records**. So this is a contract, **not a
reorganization**: nothing was merged, nothing renamed, nothing moved.

Three things each domain now declares, and what each is for:

- **`group` — the ACTION axis** (`tend` · `fight` · `visit` · `run` · `place`). **This is the answer to
  "technically, weeds are plants."** Biologically yes — but the split here has never been biological:
  you *tend* a plant and *fight* a weed, and those want different fields, a different voice and a
  different question to Mom. **Biology is a PROPERTY of a record (`scientificName` carries it), not a
  folder.** It is also Mom's own axis — she derived vehicles / equipment / household systems unprompted.
- **`time`** — which keys carry that domain's temporal axis. Declared rather than renamed: a
  `monthsPresent`→`monthsActive` rename across 64+ records buys nothing an accessor doesn't and costs a
  re-inline of every domain.
- **`markers`** — where that domain admits a guess. **`momlib.markers(record, dtype)` normalises all of
  them**, so a producer asks *"does this record admit a guess?"* instead of knowing field names.
  `harvest-questions.py` did not merely read plants.json — it hardcoded the `variety` and `bloom` FIELD
  SHAPES, which is why pointing it at `weeds.json` would have returned **zero**: the three
  unharvestable weeds are explicitly marked askable, in a vocabulary it could not read.

**`cardable` is not "does this domain exist" — it is "is it wired into `buildCard` today."**
`ENTITY_SOURCES` is now DERIVED from it, so `entity_map_divergence()` guards exactly what it guarded
before: adding a domain to canon is free; promoting one to Mom's cards is a two-place change the test
names. Flipping the flag without touching `buildCard` fails loudly.

⚠️ **Remaining M1 work, and `check-domains.py` prints it every run:** amphibian · bird · fish · lizard
· mammal · snake have **no marker path at all**, so they cannot produce a card however good the
harvester gets. Backfilling those is authoring judgement, not a migration. ⚠️ **And the risk when they
land is SUPPLY, not schema** — a harvester that can see four domains puts new cards in front of Mom,
and the 5-slot cap binds immediately with 8 already on the bench and none approved.

*(Occasional, not per-session: `python3 tools/check-season-notes.py` audits all 178 month-keyed
`seasonNotes` against each plant's own bloom and care months — heuristics over prose, so it flags and
never fixes. `--month N` gives the only set that is actually on screen.)*

## Plant taxonomy & organization — the rule (v1, 2026-07-22)

**Why this exists.** Three shapes for organizing plants now coexist in `plants.json` — separate species records, the `variety` field, and the hydrangea hub-and-roster — plus a deferred instance model (BACKLOG **W6**). This is the decision procedure so every addition uses the *same* logic and we can measure which shape earns its keep. It's a **starting point**, deliberately simple; adjust it as evidence comes in — when you change it, bump the version here and note what moved.

**The unit of a plant record = one identity that shares one care calendar.** Not a location, not a single physical plant — an *identity* (a species, or a cultivar distinct enough to need its own care). Where it grows lives in `zoneId`; *which individual* is W6, still deferred.

**Decision procedure — when adding or reorganizing a plant, take the FIRST case that fits:**

1. **Distinct species, or same species but genuinely different care → its own top-level record.** The default, and most common. Two plants a reader thinks of as *different plants*, or that need different care timing, are separate records — **even when they share a spot** (the two pond irises: `iris-blue-flag`, `iris-yellow-flag`). **Never name a record for where it lives** — use the identity (`iris-yellow-flag`), not the location (`iris-pond`). Location isn't identity: a plant can move, and one pond can hold two species. (This was the original iris mistake, corrected 2026-07-22.)

2. **Same species, uncertain or noteworthy cultivar, care is identical → one record + the `variety` field** (schema v6), *not* a split. Use when the only variation is *which cultivar* and it doesn't change care. Carries `{value, confidence, askable, …}`, drives the provenance chip, and is harvested into Mama's Perspective. Precedent: `clematis` ("Nelly Moser or Dr. Ruppel", inferred) · `crocosmia` ("Lucifer", verified).

3. **A genus/group a reader mentally bundles together (~3+ members) → hub-and-roster.** One **hub** record telling the shared genus story with a `roster[]` naming every member. Then, per member: one with **its own care calendar** gets **its own top-level record** *and* a roster line pointing to it (`hydrangea-dreamcloud`, `hydrangea-panicle`, Pop Star); one that **shares the genus care** stays a **roster line only**, no separate card (bigleaf-blue, 'Annabelle'). Below ~3 members, plain separate records are simpler — don't build a hub for two.

4. **Several individuals of the SAME species across different zones → do NOT clone the record or widen `plants.json`.** Keep one species record; put the individual/zone specifics in prose or an observation. This is **W6, deferred** — escalate to a real instance model only when its gate fires (see BACKLOG). The rule's job in this case is to *stop silent schema drift*.

**Every new record carries** (checklist): a stable identity `id` (kebab-case); `name`, `scientificName`, `emoji`, `guide`, `seasonNotes` (month-keyed, 0-indexed — see the authoring rule below; `currentSeasonNote` is the superseded single string, retained only as a net for records added without notes); `soilNotes`, `aspectPreference`, `frostSensitivity`; the six `care` types (empty months are fine); `bloom` if it flowers; `photo` + `attribution`; `zoneId` (`null` until Paul assigns it — zone assignment stays Paul-driven, per W2).

**Season-note authoring rule (v7, Paul 2026-07-26) — the note carries the CHARACTER of the month; `peakDates`/`peakWindow` keep the dates.** `seasonNotes` is a month-keyed object of authored prose (`{"0".."11"}`, 0-indexed to match `_meta.monthIndex`, `currentMonth` in the viewer, and every `care.*.months` array). The card renders the current month's line and **stays silent for months with none** — silence beats a false season. Three constraints, and they are what protect the finer-grained timing work:
1. **Never assert a date, a day-range, or "now / right about now"** for anything that has `peakDates`. A month is coarser than a 1–2 week window, so such a claim is wrong for part of the month it renders in.
2. **Hedges must hold true across the whole month** — "late in the month," "by the time the flowers drop," "from here into September." A month may name *itself* only inside a dated historical record ("Mom confirmed it in flower here in mid-July 2026"), never as a temporal claim.
3. **Nothing parses `seasonNotes`** — display-only prose, same posture as `peakWindow` prose. Because a note never claims a date, finer-grained data can land underneath it without invalidating a line.

**Honesty markers are mandatory, not decorative.** Anything guessed (cultivar, bloom window, an ID read off a photo) is marked `confidence: inferred` (plus `askable: true` where someone standing on the property could settle it). That flag *is* the hook the Mama's-Perspective harvest pulls on — a confidently-wrong record is worse than an honestly-unsure one.

**Photos:** prefer a property photo (attribution `source`/`license` = `"Property record"` → renders "Taken here on the property"); otherwise a licensed stock image, captioned as a reference *not* taken here. Photoless degrades cleanly — a missing photo is fine, a mislabeled one is not.

**Landing checklist after any add/reorg:** `python3 tools/check-data-inline.py` (plain check FIRST — see the drift rule above; `--fix` only after Paul confirms the drift is legit) → `python3 tools/build-digest.py` (refresh Guru's context) → add a `RELEASE_NOTES.md` entry if a card or behavior changed for Mom/Paul → commit → **deploy the Worker**.

**Worker deploy is the agent's job (Paul, 2026-07-26 — supersedes "deploy stays Paul's step").** Run `bash tools/deploy-worker.sh` **with the Bash sandbox disabled** (it needs network for `wrangler`; the sandbox is the only thing that ever blocked this). It rebuilds the digest, checks freshness, deploys, and hits `/health`. Verify the health check passes and report the Worker version — a deploy is only done when `/health` says so.

*Why this changed:* the old rule was a **stale assumption, not a real constraint** — an agent ran the script end-to-end on 2026-07-14 (Worker version `977075b2`, `/health` OK). Keeping a human gate on the last step of a checklist the agent otherwise owns just stranded finished work as undeployed. Same failure class as the market-digest refresh nag: *a stale `owner: paul` tag is indistinguishable from a real constraint, and nobody re-tests it.* If a deploy ever needs a judgment call (a schema break, a Worker-side migration), surface that — the *judgment* is Paul's, the *deploy* is not.

**What we measure (the revisit gate).** Watch where the shapes strain. The known pressure is **W6**: when the "same species, several individuals across zones" case shows up *for real* (not hypothetically), that's the signal to design the instance model and revise this rule to **v2**. Until a case forces it, hold to the four above — consistency now is what makes the eventual measurement legible.

## Architecture

`viewer.html` is a single **~17,900-line** self-contained file (>1 MB): all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework.

⚠️ **Two corrections, 2026-07-29 — this section had drifted badly from the thing it describes:**

1. **It said "~4,600 lines." It is 17,878.** The file has roughly quadrupled since that sentence was written and nothing re-derived it.
2. **"Fetched at page load with the inlined copies as fallback" is true of only 4 of the 21 JSON files.** For the other 17 the inlined `*_DATA` constant **is** what renders — there is no fetch behind it. That is why `check-data-inline.py` is a correctness gate rather than a tidiness check: for most domains, a source file that has not been re-inlined is simply **not in the app**. Treat re-inlining as part of the edit, not a follow-up.

**The 1 MB cliff is a live hazard, not history.** Crossing 1 MB on 2026-07-02 silently broke Guru's entire write-to-canon path for two weeks: the GitHub Contents API returns HTTP 200 with an empty body above 1 MB, so every re-inline "succeeded" against nothing. Fixed via a Blob API fallback (100 MB ceiling), but the file grows every session — **this file has now silently hit two ceilings.**

When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 17 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
- `FISHING_DATA` — Lake Sequoyah species profiles, scoring weights, seasonal notes.
- `BIRDS_DATA` / `AMPHIBIANS_DATA` — Species with `monthsPresent`/`monthsActive`, status (resident/summer/winter/migrant).
- `VEHICLES_DATA` — Fleet registry with status badges.
- `PROPERTY_DATA` — Microclimate, soil series, watershed, elevation notes.

Live data is fetched async at init from three sources: the **on-site Ambient Weather station** (MAC `D8:F1:5B:15:28:B8`, via `api.ambientweather.net`) for current on-property conditions; **Open-Meteo** (`api.open-meteo.com` forecast + `archive-api…` ERA5) for the forecast and the historical grid baseline; and **RainViewer** for radar. The logged daily record (`weather-history.json`, maintained by the `record-weather.yml` GitHub Action + `tools/record-daily-rollup.mjs`) is 100% the on-site station. NOTE: the old Weather Underground PWS `KGAJASPE279` is **no longer used** — only a Wundermap deep-link remains. Don't reintroduce it as a data source.

### CSS conventions

Color utilities are defined per care type and reused throughout:

```css
.c-{type}   /* colored text */
.b-{type}   /* solid background */
.bg-{type}  /* solid background (alias) */
.br-{type}  /* left border color */
.t-{type}   /* combined with .tag for action pills */
```

Care types: `prune`, `propagate`, `fertilize`, `water`, `repot`, `inspect`

**Action pills** (`.tag.t-{type}`) are the unified label element across all four plant views. Use this class — never invent new badge/chip patterns for care actions. The corresponding JS constants:

```js
const CARE_TYPES = { prune: { label, icon }, propagate: ..., ... }
const CARE_COLORS = { prune: "#c0622f", propagate: "#3d8a5e", ... }
```

### Key rendering functions

| Function | What it renders |
|---|---|
| `renderWeather()` | Full weather card with forecast, radar, PWS panel |
| `renderRainfallPanel()` | Rainfall context with rv-badge status chips |
| `renderFishing()` | Fishing tab content (lives inside Wildlife card; writes to `#wildlife-tab-content`) |
| `renderProperty()` | Property profile card |
| `renderPlantList()` | By Species view (calls `renderPlantCard` per plant) |
| `renderThisMonthPlants()` | This Month view grouped by care type |
| `renderTimeline()` | 3 Month view |
| `renderCalendarBody()` + `renderCalendarLegend()` | Full Year heatmap |
| `renderBirds()` / `renderAmphibians()` | Wildlife tabs (Birds, Amphibians) |
| `renderDashboardStrip()` | Top 4-tile teaser strip (Weather, Plants, Wildlife, Vehicles) |

### Plant view tabs

Four tabs share the `#plant-view-tabs` switcher. `switchPlantView(view)` controls visibility. Timeline and Full Year are rendered on demand (not at init). The active filter for By Species is stored in the module-level `activeFilter` variable.

### Card expand/collapse

Cards expand/collapse via `.expanded` class toggled on `.main-card` when its `.main-card-header` is clicked. CSS controls visibility of `.main-card-body` (display none → block). There is currently no animation — cards hard-toggle.

## Design system

**Fonts:** `Crimson Text` (serif) for the header title and plant guide prose. `DM Sans` for all UI chrome, labels, data, and tags.

**Header:** Dark forest green gradient (`#183524 → #2a6040 → #3a8a58`). Decorative circles in `::before`/`::after` at low opacity.

**Body background:** Soft green gradient (`#edf7e6 → #e2f0d8`). Max content width 660px, centered.

**Cards:** White, `border: 1.5px solid #d8eacc`, `border-radius: 18px`. Card icons are 42×42px rounded squares with context-appropriate gradients.

## Elevation calibration

**Property is 2,959 ft, not 1,750 ft.** The original data was written with a stale assumption (1,750 ft, derived from Lake Sequoyah's ~2,800 ft mistakenly attributed to the property). `property.json` is the source of truth: 2,959 ft confirmed via Open-Meteo elevation API at coordinates 34.5496°N, 84.3674°W (May 2026), 1,424 ft above KJZP baseline (1,535 ft).

Cleanup completed 2026-05-13 across `plants.json`, viewer.html's inlined `PLANTS_DATA`, and README.md:
- Numeric `elevation_ft`, "~1,750 ft" prose references, hardiness zone (7a → 6b), and KJZP delta strings all corrected.
- Frost-date `_meta` (`lastFrost_50pct`, `lastFrost_90pctSafe`, `firstFrost_50pct`) shifted from April 30 / May 21 / October 20 → May 3 / May 24 / October 17 to match `property.json` `atPropertyElevation`.
- Schema notes / data sources updated from "+7 days spring / -7 days fall" to "+10 days spring / -10 days fall."
- All `peakWindow` and `currentSeasonNote` dates in the **8 original plants** (white-pine, azalea, hydrangea, dogwood, boxwood, holly, mountain-laurel, japanese-maple) shifted +3 days for Jan–Jul dates / -3 days for Aug–Dec dates. The 5 plants promoted from `plants.draft.json` (pyracomeles, deutzia, clematis, hosta, iris-pond) were authored at 2,959 ft and needed no shift.

**Known imprecisions:** the +3/-3 shift relies on lapse-rate math (7 days per 1,000 ft); Paul's direct phenological observation is more authoritative if anything reads obviously off. Some descriptive prose still uses vague phrases ("mid-May to early June," "early summer") that weren't shifted — those are approximate to begin with and should be tightened only if a specific entry reads wrong on the ground.

## Forward direction (Phases D/E/F/G) → historical

Phases **D** (capture rebuild), **E** (Garden Guru conversational layer), and **F** (image input → auto-promote) all **SHIPPED**. **Phase G** (observations as a knowledge layer) is DEFERRED in `BACKLOG.md` (Track A · A3). The full roadmap prose + the plants-to-consider / property-map direction notes are archived in `PICKUP-LOG-ARCHIVE.md`.

## Outstanding for Paul → `BACKLOG.md` Track B3

The vehicle/equipment data-collection list (mower belt P/N, Homelite model IDs, paint codes, Tiguan sticker, GTI mileage, Marietta dealer name, the annual NASA moon-viz refresh, …) is folded into `BACKLOG.md` under **Track B — Fleet & equipment · B3 Data collection**. Read + update it there.

## Location constants

| Field | Value |
|---|---|
| Address | 282 Church Mountain Road, Jasper, GA 30143 |
| Coordinates | 34.5496°N, 84.3674°W (confirmed via Google Maps + Open-Meteo elevation API, May 2026; previous 34.52, -84.46 pointed near Jasper town center and was wrong) |
| Elevation | 2,959 ft (confirmed; 1,424 ft above KJZP baseline) |
| USDA Zone | 6b (elevation-adjusted); 7b official county |
| Last frost 50% | May 3 |
| Last frost 90% safe | May 24 |
| First frost 50% | October 17 |
| On-site station | Kirschenbauer Ambient Weather station, MAC `D8:F1:5B:15:28:B8` (source of `weather-history.json`) |
| Sky quality | Bortle 3 (rural dark sky) |
