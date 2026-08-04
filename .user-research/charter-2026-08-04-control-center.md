---
type: charter
project: fernwood
artifact_id: control-center
last_updated: 2026-08-04
evidence_level: inferred
performer: .user-research/persona-paul-co-steward.md
sources:
  - "Paul's commission, 2026-08-04 (relayed): 'all these checks and balances and Mom's last feedback, Mom's last visit, funnel metrics, open items, a link to the page itself.'"
  - tools/build-control.py (the prototype generator — read in full; NOT run, see Method note)
  - tools/mom-cycle-status.py, tools/check-telemetry.py, tools/read-mom-funnel.py (read in full)
  - MOM-CYCLE-MAP.md, MOM-CYCLE-LOG.md (Lap 1), BACKLOG.md (head), CLAUDE.md
  - ~/.claude/ai-playbook/cross-cutting/definable-loops.md (via CLAUDE.md design-time default)
  - ~/.claude/user-research/fernwood.md (Fernwood audience patterns)
privacy: >
  This file is TRACKED in a PUBLIC repo. It carries no deviceId, no verbatim words
  of Mom's, and nothing about her account of herself. That is deliberate and is
  itself a charter rule (§3).
---

# CHARTER — Fernwood Control Center

**Seat 1 of 3 (user-researcher). This is the brief seats 2 (ux-expert) and 3 (content-steward) work against.** It contains no layout, no HTML, no visual design, and no copy — by design.

**Method note, stated because an unstated boundary reads as full coverage:** I read `tools/build-control.py` in full but could **not execute it** — this seat runs without a shell. Every prototype finding in §6 is derived from the generator's source, not from a rendered instance. Findings marked ⚠️SOURCE-ONLY would be confirmed or killed by one run of `python3 tools/build-control.py` and a read of the HTML. None of them depend on runtime data to be true, but a reader should know which eye saw them.

---

## 1 · WHO, and WHAT JOB — the moment of use

**The user is Paul, alone.** `[validated — Paul's commission, 2026-08-04: "HIS surface, not Mom's"]` Not Mom, not a future collaborator, not a portfolio audience. The existing persona `persona-paul-co-steward.md` is the performer, but this page serves only one of his two halves — **Paul-the-operator-of-a-loop**, never Paul-the-steward-of-a-property. The property lives in `viewer.html`; this page is about the *machinery*.

### The moment — ranked, and the rejected ones are the load-bearing part

**PRIMARY · Re-entry after a gap.** `[inferred — CLAUDE.md session-start block; the Mom-check counter's 7-day ⚠️; MOM-CYCLE-LOG Lap 1's trigger was Paul returning and asking to "take care of the things waiting on me"]`
Paul does not live in this repo. He arrives after days, opens a session, and the first real question is *what happened while I was gone, and is any of it mine?* Today that question is answered by an agent running eight tools and narrating the output — which is precisely the failure the definable-loop standard names (*"Paul aware and in control, never parsing an AI stream"*). The gap-crossing case is also where the repo's documented failures actually happened: the ribbon sat 8 days stale, a card was served a day after she answered it, a channel went unread while a stamp read green. **Design for the 9-day gap, not the 9-minute one.**

**SECONDARY · The pre-push gate (leg 6).** `[validated — MOM-CYCLE-MAP.md § Leg 6, paul-stated 2026-08-04]`
Before anything reaches Mom, Paul needs one place that says: preview served, telemetry clean or its gaps named, nothing served that she already answered, and the thing about to ship is the thing he read. This is a *different* moment with a *different* question ("am I clear to push?"), and it is the second-most valuable because it is a gate that already exists and currently has no surface.

**TERTIARY · Post-push confirmation.** `[inferred — Lap 1 verified the ship by unauthenticated fetch; "a commit is not a ship"]` Thirty seconds after a push: did it actually land, and is the Worker healthy.

### Rejected moments — and why the rejection matters downstream

- ❌ **Continuous "is anything on fire" monitor.** `[inferred]` Fernwood has no continuous-risk surface. Its slowest-moving signal (Mom's input) arrives every few days; its fastest (git state) is already visible in the terminal. Designing for an always-on watch would drive alarm affordances that fire on nothing, and a red that never means anything trains the reader to ignore red — the exact pathology Lap 1 caught in `test-feedback-cycle.py`. **Consequence for seat 2: no auto-refresh, no polling, no persistent alert chrome.**
- ❌ **Weekly review artifact.** `[inferred]` There is no weekly cadence, and — decisively — **no history store**. One lap exists. Any trend, sparkline, or week-over-week delta would be a shape that implies data that does not exist.
- ❌ **Portfolio / demo artifact.** `[inferred, and I want Paul's read on this]` Doctrine says the governed loop IS his portfolio artifact — but the *loop's* portfolio face is `MOM-CYCLE-MAP.md`, which is public-safe. This page carries her engagement counts and open work and lives in `.private/`. **Do not design it to be shown to anyone.** If Paul wants a showable version, that is a separate, redacted artifact and a separate brief.
- ❌ **A place to do work.** See §3 — read-only is a hard constraint, not a phase-1 scope cut.

### The job statement

> **When I come back to Fernwood after a gap, I want to read the state of my own project off the record instead of off an agent's account of it, so I can decide in under a minute whether anything is mine — and start the session knowing rather than asking.**

### Four forces (JTBD — the pressures for and against him adopting this page)

*Brief framing for the seats downstream: "push" = pain in today's way of working; "pull" = what draws him to the new thing; "anxiety" = what would make him distrust it; "habit" = what makes the old way sticky. A page that answers push and pull but ignores anxiety and habit gets built and never opened.*

- **PUSH** `[validated — CLAUDE.md design-time default, paul-stated 2026-08-03; mom-cycle-status.py's own docstring]` — *"Five green exit codes do not answer 'is anything waiting on me.'"* Eight terminal tools produce eight verdicts and no position. And the alternative to reading tools is reading an agent's summary, which this repo has caught being flatteringly wrong five times on a single day (`[[feedback_hand_maintained_facts_drift]]`).
- **PULL** `[inferred]` — one surface, every number carrying where it came from and how old it is, reachable without invoking a model. The definable-loop standard's missing fifth part, made real.
- **ANXIETY** `[inferred — this is the strongest force and the one the design must answer]` — *that the page becomes another confident summary that goes quietly stale.* Paul's stack has paid for this repeatedly: a CLAUDE.md line that claimed automation for 18 days, an architecture note that said 4,600 lines when the file was 17,878, three phantom backlog rows that propagated into four documents. **A control page is the highest-leverage possible place for that failure.** If it can't prove its own freshness, he should not use it and he will be right not to.
- **HABIT** `[inferred]` — the terminal block works today. If reading this page costs more than running the block, the block wins. **The page must be cheaper than the habit it replaces**, which is a design constraint on the *invocation*, not just the layout.

### Anti-persona — who this page is NOT for

`[inferred]` **The operator watching a fleet of systems.** Paul has that reflex from consulting: uptime boards, RAG status, composite health scores. This page has one system, one other human in it, and n=1 laps. Anything that would look at home on an ops wall — a health percentage, a trend line, an SLA, a queue depth — is wrong here and should be read as a smell.

Also anti: **the agent.** Nothing on this page exists so that a future Claude can read state. Agents read the tools. The page is a human surface, and if a design choice only makes sense to a machine reader it does not belong.

---

## 2 · DECISIONS the page must enable, ranked

Each row states what Paul does differently having read it. **A panel that maps to no row below is decoration and seat 2 should cut it.**

| # | The question he arrives with | What he does differently | Why ranked here |
|---|---|---|---|
| **D1** | **Do I owe Mom a reply, and is it mine to write right now?** | He writes the ribbon words — the one act no tool and no model may perform (`check-mom-ack` computes *that* she is owed a line and never the words). Or he closes the tab knowing he doesn't. | `[validated — CLAUDE.md; MOM-CYCLE-MAP § checks]` Highest because it is **the only leg whose absence is invisible to both parties**. It sat 8 days stale during her best contributing week. Everything else on this page can wait a day; this cannot. |
| **D2** | **Is she being shown something wrong right now?** | He runs `read-mom-feedback.py --retire <id> --because "…"` before a fresh device re-asks her a question she already answered. | `[validated — Lap 1, leg 7; `q-top-categories` answered 08-03, still served 08-04]` It costs her attention, the project's scarcest resource, and it silently pins the watermark. |
| **D3** | **Is my last work actually in front of her, or sitting on my laptop?** | He pushes. Or deploys the Worker. | `[validated — CLAUDE.md: "shipping means a push"; MOM-CYCLE-MAP: "a ribbon Paul wrote and didn't push is exactly as stale to Mom as one he never wrote"]` A near-miss with a documented precedent and a one-keystroke fix. |
| **D4** | **Is a lap open, and where is it standing?** | He either runs `/mom-cycle` to continue a lap, or does meta/other work knowing no lap is hanging. | `[inferred — MOM-CYCLE-MAP § meta-work vs lap-work split]` This is the "what kind of session is this" decision, and it changes the whole session, not one action. |
| **D5** | **Can I trust the number I am about to reason from?** | He goes and triggers the path himself once before reading a zero — or he refuses to draw the conclusion. | `[validated — check-telemetry.py docstring; 23 events have never fired; a "0 taps" reading was written into the backlog and the cycle log as a finding and was not one]` This is a **negative** decision the page must enable, and this stack has shipped its opposite twice. |
| **D6** | **Has she gone quiet, and is that mine to act on?** | He picks up the phone or raises it on a visit — an action **outside the app entirely**. | `[inferred]` Ranked below D1–D5 because **the page cannot answer it** (see §5.7). What it can do is prompt the question honestly and refuse to answer it. |
| **D7** | **What should I work on next?** | Nothing — he opens `BACKLOG.md`. | `[inferred]` **Deliberately last, and I recommend demoting it to a pointer.** See §3 exclusions. |

**The falsifier for the whole page:** if Paul reads it end to end and takes no different action than he would have without it, it is decoration. D1–D3 are the ones that must survive any scope cut.

---

## 3 · WHAT IT MUST CARRY — and what it must NOT

### Must carry

Every item below carries **a named source and an age**, per the standing constraint. Ages are per-panel, not per-page (see §4).

1. **One verdict line, at the top: is anything yours?** `[inferred — mirrors mom-cycle-status.py's 🔴 NEEDS YOU]` Binary, and it must be readable without reading anything else. This is the whole page for the 80% of visits where the answer is no.
2. **The return leg — its own panel, not a row.** `[inferred — serves D1, the top-ranked decision]` What she gave · which channel · how old · does the ribbon cover it · did it ship (pushed, not committed) · the one command that shows the evidence. In the prototype this is a boolean inside a banner; the highest-value decision deserves the most surface.
3. **The served queue.** `[inferred — D2]` Is anything being shown that she has already answered, and the retire command.
4. **Loop position — read from the chronicle AND from the detectors, shown as two things.** `[inferred — D4; see §5.6 for why they are not the same claim]`
5. **The checks, with their exit codes, what each asks, and — when red — the actual failing line.** `[inferred]` A red with no detail sends him back to the terminal, which defeats the page in exactly the case that matters most.
6. **Shipping + liveness.** `[inferred — D3]` HEAD · dirty · unpushed · Worker version and `/health` · and, ideally, an unauthenticated fetch of the live `viewer.html` confirming what she'd actually load. (Lap 1 verified its ship that way; the page should make that free.)
7. **Her engagement — with the UNMEASURED discipline applied ruthlessly** `[validated — check-telemetry.py; read-mom-funnel.py]`: last visit (age), sessions in a **labelled, non-spanning window**, the exclusion denominator, and the word UNMEASURED — not a numeral — for any event with no first-fire.
8. **Doors.** `[validated — Paul's commission: "a link to the page itself"]` The live app; the preview command; and the four files that make this navigable (`MOM-CYCLE-MAP.md`, `MOM-CYCLE-LOG.md`, `BACKLOG.md`, `/mom-cycle`).
9. **Its own generation time and its own staleness, self-declared.** See §4.
10. **The privacy banner.** `[validated — the 2026-08-04 devices.json lesson]` The prototype has this and it is right; keep it.

### Must NOT carry — the exclusions, argued

- ⛔ **Her verbatim words. Any of them, on any panel.** `[validated — CLAUDE.md AI-boundary amendment, quarantine clause; her words live in the Worker and `.private/`, and `feedback-log.json` records *where a note went*, never what it said]` Two arguments beyond the doctrinal one: (a) the page's job is **state**, not content — a page carrying her sentences invites reading the page instead of reading her; (b) it would make the page a second copy of a record that already has a home, which is `[[feedback_single_source_of_truth]]`. **Carry that a note exists, its channel, its age, and where to read it. Never the text.**
- ⛔ **Her deviceId on the page's face.** `[inferred]` The generator needs an identifier to filter by; the *reader* never needs to see it. It is exactly the field that leaked for 15 days. Render "her device (builder devices excluded)" — never the string. *(And see §6-d: the identifier's presence in a **tracked** generator is a separate finding.)*
- ⛔ **A scraped BACKLOG dump.** `[validated — [[feedback_unchecked_box_is_not_open_work]], paul-stated 2026-07-31]` The prototype prints 14 rows whose status *cell* says open. That doctrine says these documents go stale in the safe-looking direction: they **over-report open work, never under**. So the panel is systematically wrong in the direction that makes Paul act on something already handled. `BACKLOG.md` is the SSOT and carries the argument; a status-cell scrape is a second tracker with none of it. **Recommendation: a count, a pointer, and at most the rows the loop is currently standing on.** Paul asked for "open items" — I am proposing this narrower reading and flagging it as a decision for him, not quietly dropping it.
- ⛔ **Any control that writes.** `[inferred]` Not a retire button, not a "mark read," not an acknowledge. Two reasons: the attestations must be clearable **only by the act they detect the absence of** (a button on a dashboard is a stamp, and stamping is what already produced an all-green ribbon while five recordings sat unlistened); and `--because` is a human judgement typed by a person. **The page's affordances are commands to copy, never actions to click.**
- ⛔ **Trends, sparklines, deltas, history.** `[inferred]` n=1 lap, single-digit sessions, and two boundaries across which the data is explicitly not poolable. A trend line is a lie told by shape. Revisit at ≥5 laps.
- ⛔ **A composite health score / percentage / RAG roll-up.** `[validated — [[feedback_chain_stage_granularity]]: "a single number is a smell"]` A composite hides which leg is red, which is the only thing he needs.
- ⛔ **Anything a model produces, or any interpretation typed by hand and rendered beside a derived number.** `[validated — the non-AI-door constraint; and see §6-e for a live instance of the second failure in the prototype]`
- ⛔ **Percentages or rates at n<10.** `[inferred]` "50% completion" over two events is a number that will be quoted later.
- ⛔ **Sentiment.** `[inferred]` A tap is a tap. Rendering an emotional word next to a button value is the model-free version of AI re-interpreting her input, which is forbidden creep-mode (4).
- ⚠️ **Scope, and I want Paul's call:** this page as specced is the **Mom-loop's** control center. Track B (fleet & equipment) is a different user, tone, cadence, and has no loop and no live deadline. **Recommendation: name the page for the Mom loop, and give Track B one honest line** ("no loop; next hard date 2027-06-03 — see BACKLOG Track B") so its absence is a recorded decision rather than an omission.

---

## 4 · THE CYCLE around the page

**The page is a snapshot generator that runs live tools.** Its numbers are exactly as fresh as its last generation, and its single most dangerous failure is Paul opening yesterday's file and reading it as today's.

**Regeneration — by trigger, never by schedule.**

| trigger | why |
|---|---|
| **Session start on Fernwood** — the first line of the `CLAUDE.md` session-start block | `[inferred]` The block already runs these tools. Today their output lands in an agent's stream; this routes it to a surface Paul reads. Same cost, different destination. |
| **Leg 6, before the push** | `[validated — MOM-CYCLE-MAP § Leg 6b]` The gate moment; state changes materially here. |
| **Leg 7, at close** | `[inferred]` So the last generation of a lap is the one that scores it. |
| **On demand, any time** | It is one command and has no side effects. |

⛔ **No launchd, no cron, no watcher.** `[inferred, and this is a real recommendation against an obvious idea]` A scheduled regenerator produces a page that is *fresh and unread* — the "mechanism that inspects as present and has never actually run" pathology this repo names explicitly. **Regeneration should be evidence that a human arrived.** (`read-mom-funnel.py --notify` exists for the one genuinely push-shaped signal; that is the right home for it, not this.)

**How he knows it is stale — three requirements, all non-negotiable:**

1. **The page declares its own age at view time, not at build time.** `[inferred]` Bake the generation instant into the HTML and let a trivial inline script compute elapsed time when the file is opened. *(Inline JS is deterministic and is not a model — this does not violate the non-AI door.)* This is what stops "silently shows yesterday" with no daemon.
2. **It self-degrades past a threshold** rather than continuing to display numbers confidently. Proposed: **30 minutes** for tool-derived rows (they cost seconds to re-derive, so there is no reason to trust an old one) and a visible "REGENERATE — this page is N hours old" state past that. Seat 2 owns how that reads; the charter owns that it must happen. **Threshold is a proposal for Paul, not a finding.**
3. **Ages are per-panel and per-clock.** `[inferred]` Check exit codes age from generation. Her last visit ages from the **event**. Worker health ages from the probe. Git ages from the commit. Collapsing these into one "generated at" is the same error as three unlabelled "week" figures on the rainfall card — a reader with no way to tell which clock a number is on reads a contradiction and concludes the page is broken.

**And the failure mode that must be designed in, not bolted on:** when a tool times out, the Worker is unreachable, or the token is missing, the panel says **UNAVAILABLE** and names which. It never renders 0. (§6-b — the prototype currently fails this.)

---

## 5 · HONESTY REQUIREMENTS — the numbers that can lie

This stack has already shipped an unmeasured zero as a finding twice. Each item names a specific number and the specific way it deceives.

1. **Any count for an event that has never fired.** `[validated — check-telemetry.py: 23 such events as of 2026-08-04]` A zero here means UNMEASURED. **Requirement: do not render a numeral at all.** A greyed "0" is still a zero to a tired reader at 11pm; the word is the guard. The prototype's `strip_row()` gets this right for two events and must be generalized to every event on the page.
2. **Her session and answer counts depend on device attribution.** `[validated — read-mom-funnel.py; people.json `_meta`: the mapping was BACKWARDS for 26 days and Paul's own dogfooding was counted as her engagement]` **Requirement: print the denominator on every run** — how many builder devices were excluded, how many events dropped, and loudly, any **unmapped** device (which is silently counted as hers). A tool that quietly excludes nothing reads identically to one that correctly excluded everything.
3. **Windows that span a methodology change are not poolable, and the page will span them by default.** `[validated — read-mom-funnel.py names two boundaries: 2026-07-28 (attribution fix) and 2026-08-04 (jump-strip rebuilt around her categories with real 44px targets)]` A rolling 30- or 60-day window on 2026-08-04 crosses **both**. **Requirement: windows are anchored and labelled** (`TIMEBOX_START = 2026-07-13`, her first confirm), and any figure crossing a boundary is either split or flagged on its face.
4. **Every window label must equal the window queried.** `[inferred]` "Answers, all time" over a 60-day query is a plain false statement, and it is the kind that gets quoted into a backlog row three weeks later.
5. **A green check means "this detector found nothing," never "this is right."** `[validated — each tool's own stated limits: check-telemetry cannot prove correct wiring; check-cycle-map verifies no undocumented tool and "cannot verify a sentence"; the preview "cannot catch anything that only breaks on Pages"]` **Requirement: each check's scope travels with its green.** Seven greens must not compose into "everything is fine."
6. **"Where the loop is standing" is an inference from exit codes, not a reading of a lap.** `[inferred — build-control.py derives position from 2 exit codes; mom-cycle-status.py from 3; neither reads MOM-CYCLE-LOG.md]` A lap genuinely paused at leg 4 with all detectors green renders as "leg 7 · CLOSE." **Requirement: show two claims, separately labelled — what the *chronicle* says (is the newest lap CLOSED?) and what the *detectors* say (is anything red?).** Today the page asserts the first while measuring only the second.
7. **Silence is the one thing this page structurally cannot interpret.** `[validated — MOM-CYCLE-MAP: "clean never means she felt heard"; the honest-limits constraint]` "No new input in 9 days" is *quiet*, *neglected*, or *the capture path is broken*, and nothing on this page can tell them apart. **Two requirements:** (a) say so on the face, once, plainly; (b) add the one signal that *does* discriminate — **days since anything at all fired, from any device**. Her silence next to a live pipe is a different fact from her silence next to a dead one, and that pairing costs nothing and does not exist today.
8. **`acknowledgedThrough` is a stamp; a stamp is not an act of reading.** `[validated — check-mom-ack reported ALL GREEN on 2026-07-26 while five zone recordings sat unlistened and fourteen Guru conversations unread; the fix was attestation]` **Requirement: the ribbon row must never imply anyone read anything. The attestation state (R2b) is the honest signal and belongs beside it.**
9. **`momack_shown` counts exposure, not receipt.** `[validated — MOM-CYCLE-MAP § clean lap]` There is **no outcome measure for the return leg**, that gap is named in the map, and a page that displays process greens without that line will be read as the loop's scorecard. **Requirement: it appears on the page.**
10. **Open-item counts over-report.** `[validated — [[feedback_unchecked_box_is_not_open_work]]]` If any open-work figure survives §3, it is labelled *"rows whose status cell says open — not verified against the world."*
11. **A tap is not a preference and not a sentiment.** `[inferred]` No interpretive word may sit beside a count unless a tool derived it.
12. **Timestamp arithmetic is itself a claim.** `[inferred — build-control.py hardcodes UTC-4]` Correct today, wrong from 2026-11-01. On a page whose entire premise is *age*, an hour-wrong clock is a lie in the load-bearing dimension. Derive the zone; label it ET.

---

## 6 · THE PROTOTYPE, against this charter

Read as a straw man, as instructed. **What it gets right and must survive:** per-panel source-and-age notes; the private banner and its reasoning; the `strip_row()` UNMEASURED treatment; "PREVIEW ≠ SHIPPED"; "a commit is not a ship"; the doors. Those are the charter, already implemented.

### Blocking

**a · Silent failure renders as a confident zero.** `⚠️SOURCE-ONLY` `gather()` catches metrics and feedback exceptions into `g["metrics_error"]` / `g["feedback_error"]` — and **`render()` never reads either key**. Worker down, token missing, or network off, and the page prints *"Sessions (30d): 0 · Answers, all time: 0 · Last visit: —"* with no indication anything failed. **This is the unmeasured-zero failure, shipped again, inside the page built to prevent it.** Highest severity in this list.

**b · A hand-typed conclusion is rendered as if it were derived.** Line 226 places *"she reads the glance; she rarely drills"* in the `.ago` slot beside the card-expansion count — the same visual position used everywhere else for derived metadata. This is a persona-level claim with no source, no date, and no tag, on a page whose thesis is *"a number with neither is a rumour"* — and it is the same class of claim the repo **struck everywhere on 2026-08-01** when the persona's telemetry tier turned out to describe Paul's own dogfooding. **Delete it. Nothing interpretive gets rendered beside a number.**

**c · Windows are wrong and mislabelled.** Metrics query = 30 days, feedback = 60 days, and the row reads *"Answers, all time."* Both windows cross the 2026-07-28 attribution correction **and** the 2026-08-04 jump-strip rebuild, which the repo's own tooling says are not poolable. Three separate violations of §5.3 and §5.4 in one panel.

**d · The exclusion denominator is entirely absent, and Mom's deviceId is hardcoded in a tracked file.** The generator filters to one literal deviceId constant (line 49). Two consequences: (i) it can never surface an **unmapped** device, which is the specific mechanism that produced 26 days of wrong numbers — `read-mom-funnel.py` prints both the exclusion count and unmapped devices, and this page prints neither; (ii) `tools/build-control.py` is **tracked in a public repo** and now contains that identifier verbatim. The rendered page is safely `.private/`; the *generator* is not. **That is the devices.json lesson exactly — the unexamined tracked file is the exposed one.** ⚠️ *This one is outside my seat: it is a privacy/engineering finding, it likely also implicates `tools/people.json`, and I have not verified that file's tracked status. Route it to Paul directly and to `engineering-partner`. The charter's binding rule for seats 2 and 3 is narrower: **introduce no new copy of that identifier.***

**e · The return leg — the top-ranked decision — has no panel.** It exists as one boolean in the banner and one row in the checks table. What she gave, through which channel, how old, whether the ribbon covers it, whether it shipped: none of it is on the page. D1 currently has less surface than the 14-row backlog scrape.

**f · A red check shows no detail.** `run(tool)[0]` discards stdout entirely for the checks table, so a red says *something is wrong* and nothing more. `mom-cycle-status.py` already captures the 🔴/🟡 lines and prints them. The one case where the page has the most value is the one case it sends him back to the terminal.

**g · Loop position is re-derived, a second time, from a different rule.** `render()` computes `at` from two exit codes; `mom-cycle-status.py` computes it from three. **Two surfaces, two definitions of "where the loop is."** `[[feedback_single_source_of_truth]]` — and this repo has already paid for exactly this with three copies of `_load()` and three definitions of "pending." **The control page must call `mom-cycle-status.py --json` and render it, never re-derive it.** Same for the `LEGS` table hardcoded at line 61: it is a hand copy of the map's eight legs with its own gate flags, and `check-cycle-map.py` does not guard it.

**h · No self-staleness.** "Generated <time>" sits in small grey sub-text and nothing degrades. Opened three days later the page reads exactly as it reads now. §4's whole point is unmet.

### Should-fix

**i · No liveness.** No Worker version, no `/health`, no unauthenticated fetch of the live `viewer.html`. "Is the thing she'd load right now the thing I pushed" is the most non-AI-door question there is, it has a Lap 1 precedent, and it is absent.

**j · The open-items panel is the largest thing on the page and the weakest decision.** Fourteen scraped rows, unverified against the world, systematically over-reporting. See §3.

**k · No liveness-vs-quiet discrimination.** Nothing distinguishes *she is quiet* from *the pipe is dead* (§5.7).

**l · No pointer to the map, chronicle, backlog, or the `/mom-cycle` procedure.** "Doors" carries the live app and localhost only. The reading-order files are what make this navigable to someone arriving cold — which, after a nine-day gap, Paul partly is.

**m · `et()` hardcodes UTC-4.** Correct through 2026-10-31 (§5.12).

**n · The "Mom" panel's framing.** It is titled with a person's name and reads as a portrait of her. Retitle around the *relationship state* — what the record owes her and what it has heard — so the page cannot drift into being a dashboard about a person.

---

## Open questions for Paul — answers change the brief

1. **Do you actually open a page at session start, or is the terminal block still your front door?** If the block stays, this page *supplements* and should be optimized for the leg-6 gate instead of re-entry — a different primary moment and a different §1.
2. **Whole repo, or the Mom loop?** I have scoped it to the Mom loop with a one-line Track B stub (§3). Your "open items" phrasing may have meant the whole backlog.
3. **The open-items panel — count-and-pointer, or do you want rows?** I have argued for demotion against your original ask; overrule me if reading rows there is genuinely how you use it.
4. **Is 30 minutes the right staleness threshold**, or would you rather the page simply refuse to open stale — i.e. always regenerate, never read the file directly?
5. **Will you ever want to show this to anyone?** I have designed on the assumption of never (§1). A yes means a separate redacted artifact, not a mode on this one.

---

## Evidence log

- `2026-08-04: [validated] — Paul's commission (relayed) — the page is Paul's surface, not Mom's; contents named: checks and balances, Mom's last feedback, Mom's last visit, funnel metrics, open items, a link to the page.`
- `2026-08-03: [validated] — CLAUDE.md design-time default, paul-stated — every recurring AI workstream gets a definable loop, one part of which is a glanceable awareness surface: "Paul aware and in control, never parsing an AI stream."`
- `2026-08-02: [validated] — CLAUDE.md, paul-stated — deterministic things need a non-AI door; falsifier: if the only way to learn whether a site is up is to ask Claude, this is broken.`
- `2026-08-04: [validated] — check-telemetry.py first run — 23 instrumented events have never fired; a "0 taps" reading had already been written into BACKLOG.md and MOM-CYCLE-LOG.md as a finding and was not one.`
- `2026-07-28: [validated] — tools/people.json _meta + read-mom-funnel.py — the device mapping was backwards for 26 days; no pre-2026-07-28 funnel verdict may be cited without re-derivation.`
- `2026-07-26: [validated] — CLAUDE.md — check-mom-ack reported ALL GREEN while five zone recordings sat unlistened and fourteen Guru conversations unread; a detection mechanism must be clearable only by the action it detects the absence of.`
- `2026-07-26: [validated] — CLAUDE.md — the acknowledgment ribbon sat 8 days stale during Mom's best contributing week.`
- `2026-07-31: [validated] — [[feedback_unchecked_box_is_not_open_work]], paul-stated — status docs go stale in the safe-looking direction; they over-report open work.`
- `2026-08-04: [inferred] — build-control.py source read — findings §6-a through §6-n derived from the generator, not from a rendered instance; this seat could not execute it.`
- `2026-08-04: [assumption] — the ranking of decisions D1–D7 and the primary moment-of-use are my read of how Paul works on this repo, built from the loop's documented failures rather than from watching him use anything. Open question 1 is the cheap way to falsify it.`
