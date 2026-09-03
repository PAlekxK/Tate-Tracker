# C4 · THE RELEASE PROCESS — what a release is, where QA sits, what an agent may test · PROPOSAL (2026-09-03)

> ## ⛔ STATUS: **PROPOSAL. Ends at Paul's gate. No canon changed to write it.**
> Seat: `practice-steward`, the PROCESS half of `BACKLOG.md` § C4. `engineering-partner` is drafting
> the TOPOLOGY half concurrently — branches vs a second Pages site, Worker environments, namespace
> separation, the public/private split, rename mechanics. **This file designs no topology.** Where the
> process needs something from it, the requirement is stated and handed over, marked ➡️ **TOPOLOGY**.
>
> **Method, never content. This file ranks nothing.** Every measurement in C4's own tables is carried,
> not re-measured, per the brief.
>
> **Falsifier for the whole proposal:** if the first release through this produces zero findings at the
> `qa` stage that leg 7-QA would not also have caught, then under this topology the stage is ceremony
> and should be **deleted rather than tuned** — see §8.

---

## 1 · WHAT A RELEASE IS

> **A release is one plan file's change set, pushed as one act and verified as one act.**
> **The plan file is the release's identity.** No plan file → no release.

Why the plan file and not a commit or a lap. A commit is too small: C4's table measures **43 unpushed
commits** here, and `~/.claude/CLAUDE.md` ungates git precisely because a commit is reversible. A lap is
the wrong shape: the mom-cycle is a **loop** fired by her input or behaviour (`MOM-CYCLE-MAP.md:67`,
amended `:80`), while this is a **procedure** — invoked, run, ended, and it **cannot be owed**
(`VOCABULARY.md` §3c). The plan file already exists per item and already crosses the READY seam
(`.plans/2026-09-03-backlog-readiness-PROPOSAL.md` §1.3, §2), so nothing is minted.

⭐ **This predicate also separates a release from a push, which today are conflated.** C4's table:
`main` only, Pages serves `viewer.html` from it, **a push is a production deploy** — *and* the weather
bot pushes **~4×/day**. `weather-history.json` and `weather-bias.json` are both inside
`check-live.py`'s `TRACKED_FILES` (`tools/check-live.py:99-105`), so **the bot changes a live asset on
her phone four times a day with no plan file and no gate.** Under this design those are not releases.
⚠️ **Reported, not resolved:** that is either a declared exception or a hole in "anything that reaches
her phone is Paul's gate," and which one it is is his call (§9 Q4).

**What "done" means at each stage — existing checks first, and what each cannot prove.**

| transition | deterministic evidence | ⛔ cannot prove |
|---|---|---|
| `ready → concept` | an exhibit set exists **and** the run is appended to `/design-options`' own **Refinement log** — the authoritative record by the skill's design (`~/.claude/skills/design-options/SKILL.md` head; C4/C2 corrected a count taken from directories instead) | that the option set was the right set |
| `concept → build` | the plan file names the **winning exhibit id** Paul ruled on (round-stamped, `SKILL.md` exhibit rule 5) | that the ruling will survive contact with code |
| `build → qa` | **12** tools in `tools/` carry `--selftest` (predicate: files matching the literal `--selftest`, measured 2026-09-03; C1 reported **11** on 2026-09-02 — the delta is `check-backlog-ready.py`, committed 11:18 today) · `check-data-inline.py` exit 0 · `check-digest-fresh.py` exit 0 · `check-vocabulary.py` where any name moved | **that it renders.** Every one of these reads the repo, never the screen |
| `qa → shipped` | ⭐ the whole gate — see §5. `guard-concurrent.py before-push` · `check-live.py` exit 0 (five same-origin assets byte-identical to HEAD, its drift guard re-deriving the list from `viewer.html`) · `deploy-worker.sh` `/health` if the Worker moved (`tools/deploy-worker.sh:44-49`) · `measureNestingWidth.herConditions()` `clean:true` or every HIGH dispositioned · the scoped live review = **leg 7-QA** | that a phone is not still serving a cached copy (`CLAUDE.md:555`) |
| `shipped → retro` | `## Retro` present in the plan file — already enforced at `tools/check-backlog-ready.py:149` | that the retro is honest |

⚠️ **A contradiction to carry, not fix:** her-conditions is named at **two** positions — leg 6e
(pre-push, local, `CLAUDE.md:524`) and leg 7-QA step 1 (post-push, live) — and was **not runnable live
at all until `a43812d`**, the harness having scored GitHub's 404 page (`MOM-CYCLE-MAP.md:524-530`).

---

## 2 · WHERE QA SITS — **two acts, not one at two altitudes**

Today they are one act only because there is nowhere else to run the first. They separate cleanly on
**what would falsify each**:

- **the `qa` stage** — falsified by *the change being wrong*. Subject: the diff.
- **leg 7-QA** — falsified by *the change being right and not arriving intact*. Subject: production.
  Pages rebuilds asynchronously (~2 min measured, `CLAUDE.md:543`), the Worker deploys separately, a
  phone caches. **No QA environment can host this act; its subject is the thing a QA environment is
  not.**

⭐ **The corpus already runs one measurement at two altitudes and treats the results as two claims** —
her-conditions at 6e and again at 7-QA (§1). That is the precedent, and it is why this is a split
rather than a move.

**Three constraints that follow:**

1. ⛔ **Leg 7-QA is not renamed and does not become a pipeline stage.** `MOM-CYCLE-MAP.md:33`:
   *"renaming established legs would fork the doctrine."* It enters the pipeline vocabulary only as
   **evidence for the `qa → shipped` transition**, so there is exactly one *stage* called `qa`.
2. **The `qa` stage must not reset the `/ux-sweep` clock.** The existing rule already protects this for
   leg 7-QA (*"a single-seat scoped review does not reset the sweep clock"*, `MOM-CYCLE-MAP.md:508`);
   a procedure that silently reset an accumulation trigger would be the same defect one altitude up.
3. **A release does not fire a lap and does not close one.** The loop's trigger is hers
   (`MOM-CYCLE-MAP.md:67`+). ⭐ **And there must be exactly one path to production:** when a release
   ships *inside* a lap, `qa → shipped` **is** legs 6 → 6e → 7-QA, not a second gate beside them; when
   it ships outside any lap (Track B, engine work, C4 itself), the pipeline supplies the gate the loop
   would have, with 6c PROXY and 6e **waived with a reason** if no Mom surface moved. The predicate is
   mechanical: *does the release touch a file in `check-live.py`'s `TRACKED_FILES`, or the Worker?*

---

## 3 · WHAT AN AGENT MAY TEST — the fence, and what dissolves it

**Today, unchanged: metrics-safe paths only.** The mechanism is a synthetic `deviceId` with
`excludeFromEngagement` + `isTestHarness` (`tools/people.json:34`, added 2026-08-08, Paul-approved).
Its reasoning is load-bearing and must survive any redesign: `tateTracker.metricsExclude` makes
`MetricsCollector.track()` a no-op (`viewer.html:16688`), so **it can prove nothing** — *the test must
RECORD to be a test and be SEGREGATED to be safe.* And the fence itself: *"Paths that POST to
`/api/feedback` … are NOT safe to walk — they write into Mom's answer record, which no metrics
exclusion covers."*

**The fence stands until a QA environment exists.** ➡️ **TOPOLOGY — five requirements the process has
of it. Requirements, not a design:**

| # | requirement | why, in evidence |
|---|---|---|
| **R1** | An agent-issued `POST /api/feedback` in QA must be **unreadable by every tool that reads her record** — demonstrated by *driving it*, not by reviewing config | C4: **one** KV namespace holds her verbatim answers, **zero `[env.*]`** |
| **R2** | Every record must carry the environment that wrote it, and every reader of her answers must **fail closed on an absent value** | `excludeFromEngagement` works because it is an allowlist every analysis tool drops; an absent field must never read as production-clean. *Cannot-tell must never render as clean* (`CYCLE-SPINE.md` S4) |
| **R3** | Both a **positive and a negative control**: a QA write seen present in QA *and* seen absent from production, both by command | the leg 7-QA 404 incident — a harness must assert it loaded the right document and **throw** when it did not (`MOM-CYCLE-MAP.md:527-530`) |
| **R4** | QA must be reachable **without a model** — a URL and a `curl`, not "ask Claude whether QA is up" | `~/.claude/CLAUDE.md` § deterministic things need a non-AI door |
| **R5** | Declare what QA **cannot** exercise. Storage is **per origin** (C4 table), so a QA origin has its own 12 `tateTracker.*` keys — **the rename's old-key → new-key migration is not testable in QA**, and done wrong it is M3 for real | C4 rename table, browser-storage row |

⛔ **Only the broad half of the fence dissolves.** Even with QA, an agent may never write to her live
record and never drive her device. That half is permanent.

---

## 4 · THE STAGE VOCABULARY — ratified, with one rename

Recorded as `- stage:` in `.plans/YYYY-MM-DD-<slug>-PLAN.md` (readiness §1.3), read by
`tools/check-backlog-ready.py:38`.

| placeholder | ruling | reason |
|---|---|---|
| `ready` | ✅ **ratify** | Paul's word, `paul-approved 2026-09-03`, already applied |
| `concept` | ✅ **ratify** | his own word — *"not UX review, **concept review**"* (C2 quote); `/design-options` is its tool |
| `build` | ✅ **ratify** | no competitor in the corpus |
| `qa` | ✅ **ratify the word**, ⚠️ **with a declared collision** | it double-books "QA" against leg 7-QA — one name, two meanings, one repo, which is exactly `check-vocabulary.py`'s **V3** class (`tools/check-vocabulary.py:20-23`). §2's constraint 1 keeps them structurally distinct; the residual risk is prose, and prose is not a mechanism. **Falsifier:** if a session writes *"QA passed"* and a reader cannot tell which act, rename the **stage**, never the leg |
| `live` | ⛔ **RENAME → `shipped`** | `live` names a **deployment fact**; the transition it guards is a **verification**. With `live`, a push that was never verified and one verified clean read the same — that is the 08-14 radar incident's exact shape (`CLAUDE.md:545-549`). **`shipped` already means verified-at-the-live-URL in this repo** — *"A COMMIT IS NOT A SHIP — AND NEITHER IS A PUSH"* (`CLAUDE.md:539`) and leg 7's *"until it does, the lap shipped nothing, whatever git says"* (`MOM-CYCLE-MAP.md:49`) — and `SHIPPED` is already in `BACKLOG.md`'s status taxonomy. **Reuse, not a new word** (`feedback_reuse_vocabulary_before_adding_state`) |
| `retro` | ✅ **ratify** | `feedback_retro_improvement_closes_a_cycle` |

**`ready → concept → build → qa → shipped → retro`.** Six words, one rename, nothing added.

**Who advances it, on what evidence.** The agent doing the work advances `ready → concept → build →
qa` — all reversible, nothing has left the machine (§5). **Only Paul's stamp permits `qa → shipped`.**
`shipped → retro` is the agent's, on §1's evidence.

**How the WIP default reads.** `check-backlog-ready.py:39` — `IN_FLIGHT = {"concept","build","qa"}`;
more than one without `wip-exception:` is flagged (`:157`). ⭐ **Under the rename this gets *more*
honest, not less:** the push-to-verified window now sits **inside `qa`**, so a release that is in
production but unverified is still counted in flight — which is the one window this corpus has been
wrong in before.

⚠️ **The rename touches enforcement, not just words:** `check-backlog-ready.py:38` `STAGES`, `:149`
(`stage in ("live","retro")` → `## Retro` required) and three selftest strings. **One-line class of
change, `engineering-partner`'s to make, and it is not canon.**

---

## 5 · THE TWO GATES

**Paul's — irreversible.**

- **`qa → shipped`, whenever the release touches a file in `check-live.py`'s `TRACKED_FILES` or the
  Worker.** Reversibility argument: a revert is *another* asynchronous push, so the un-reversible part
  is that **she may already have loaded it** and her phone may cache it long after the origin is
  correct (`CLAUDE.md:555`); a build that writes `/api/feedback` cannot be un-written; and a botched
  per-origin storage migration loses her `textSize` on her own device, which no push restores (C4
  rename table + M3).
- **Anything that reaches her phone at all** — this is leg 6 / 6c / 6d, existing, unchanged.
- **The C4 push itself is a live instance of this gate**, already held on the topology ruling (C4).

**An agent's — reversible.** `ready → concept`, `concept → build`, `build → qa`, and `shipped →
retro`. Nothing has left the machine; a bad step is undone by an edit or a revert. Per
`~/.claude/CLAUDE.md`: *"an agent may commit a hundred times in a lap and may not send one email,"*
and git is explicitly ungated.

⭐ **The boundary that is NOT reversibility, and it is the process's one ask of topology on the gate
side.** Under today's topology — `main` only, Pages from `main` — **there is no such thing as a
non-production push of a tracked asset**, so the gate has been forced onto the git verb. ➡️
**TOPOLOGY: make "push to QA" and "push to production" two distinguishable acts.** Then the QA push
becomes an agent's act and Paul's gate moves off the verb and onto the **promotion**, which is where it
belongs — the gate sits on the irreversible act, never on work.

---

## 6 · IF THE ENGINE / INSTANCE SPLIT HAPPENS — where each piece of the process lives

Paul, 2026-09-03: an ENGINE repo with per-estate INSTANCE repos rather than the reverse. **Process
implication only; the layout is `engineering-partner`'s.** The governing rule is already ratified as a
data rule and generalises exactly: ⛔ **a per-instance DECLARATION is not per-instance CODE** —
*"Bob's house declares `SEASON: unobserved`; it does not get a second probe. Two probes are how two
definitions of 'a lap is owed' are born"* (`.plans/2026-09-02-data-model-design.md:262`).

| piece | lives where | class, and why |
|---|---|---|
| the readiness **mechanism** (the five fields, the `- key: value` format, the stage list) | **ENGINE**, one definition | `engine` — a second definition of READY is a second definition of *done* |
| `tools/check-backlog-ready.py` and every `check-*` that reads a **contract** | **ENGINE**, one copy, run against an instance by path | check/probe contracts are already ⛔ **MUST NOT DIVERGE** (`PRODUCT-ENGINE.md:375`) |
| **plan files** | **INSTANCE** — they describe this estate's change set | `instance`. An engine-class change gets its plan file in the **engine** repo, under the same mechanism |
| `OBJECTIVES.md` | ⭐ **both, and they are different documents.** Instance objectives (O1, O2, O4) stay per estate; **O3 and O5 are engine objectives and belong to the engine** | `config` for the citation, `engine` for the *format*. A row cites **one** id; ids must therefore be unambiguous across the seam — ➡️ engine ids need a distinguishable form (e.g. `E1`), or one id resolves to two objectives |
| the **feature pipeline's stages** | **ENGINE** — the vocabulary and the transitions | `engine`. Per-instance stage words are how *"qa"* comes to mean two things in two repos |
| the **mom-cycle** (map, log, trigger, state artifact) | **INSTANCE** | it is fired by *one person's* input on *one* estate. The condo has no Mom |
| the mom-cycle's **beat mechanics** — the watermark clamp, the fold, the guard, `mom-cycle-status.py` | **ENGINE**, invoked per instance | already ⛔ MUST NOT DIVERGE (`PRODUCT-ENGINE.md:375`); the clamp's divergence is *silent data loss* |

**The requirement the process places on the split, stated as one testable thing:**

> ⛔ **Every procedure, check and stage word has exactly ONE definition in the engine. An instance may
> only DECLARE — a value, an absence with a reason, a threshold. An instance that carries a *copy* of a
> procedure is a defect, not a customisation.**

**The leak is already measurable in this repo, which is why this is a requirement and not a worry:**
`fleet_probe.py:50` re-types `FROST_MONTH, FROST_DAY = 10, 17` from canon — a value that has already
moved once (Oct 20 → Oct 17), so the probe is *correct by timing, not by derivation*
(`.plans/2026-09-02-data-model-design.md:266-269`). One repo, one estate, and a config value had
already forked. ➡️ **TOPOLOGY: the split must make a per-instance copy of engine code *harder* than a
declaration, or this leak becomes per-estate.**

**Falsifier for this section:** if the second estate needs a second `check-backlog-ready.py`, a second
stage list, or a second definition of READY, then the mechanism was instance-shaped all along and this
table is wrong — record it, do not fork the tool and call it configuration.

---

## 7 · WHAT THIS DOES NOT DO

- **Designs no topology.** §3 R1–R5 and the two ➡️ asks in §5 and §6 are requirements handed over.
- **Ranks nothing.** No item, no stage, no estate is more important than another here.
- **Retrofits nothing.** No lap, leg, or already-shipped item is re-labelled. `MOM-CYCLE-MAP.md` is
  untouched, and leg 7-QA is not renamed.
- **Adds no loop, lap, trigger or state artifact.** This is a **procedure**; it cannot be owed, so
  `CYCLE-SPINE.md` S1–S6 do not apply to it and nothing may ever report it as behind.
- **Builds no check.** `check-backlog-ready.py` already exists; §4 names a one-line class of change.
- **Does not resolve** the weather-bot contradiction, the two-altitude her-conditions contradiction
  (both §1), or whether the mom-cycle's own shipping now gets plan files (§9 Q3); and **verifies no
  quality** at any stage — only that the evidence exists and points somewhere.

---

## 8 · PRE-REGISTERED FOR THE FIRST RELEASE — two-sided

**The question:** *did the `qa` stage catch anything leg 7-QA would not have caught?* Measured as a
count of findings dispositioned at `qa` that were (a) about the change itself and (b) would otherwise
have reached production. ⭐ **Zero is a valid and informative answer** — it says that under this
topology the stage is ceremony, and the honest response is to delete it rather than tune it. *"None —
pre-registered metric unmoved"* is a recorded outcome, not a failure.

**Where it discharges:** the first plan file's `## Retro`, alongside readiness §5's own two questions.
Already enforced — `check-backlog-ready.py:149` flags a `retro`-or-later stage with no `## Retro`
section. ⚠️ **That line reads `("live","retro")` today and must move with the §4 rename or the
enforcement goes silent.**

**The second side, which is the half that failed on fleet lap 1:** at the **next** release's
`ready → concept`, state this question's disposition **out loud before doing anything** — answered,
carried, or void. **Silent ≠ carried** (`feedback_retro_improvement_closes_a_cycle`, two-sided
2026-09-01).

---

## 9 · OPEN QUESTIONS FOR PAUL — one sentence each

1. **`live` → `shipped`** (§4): rename, or keep `live` and accept that pushed-unverified and
   verified-clean wear the same word?
2. **The `qa` name collision** with leg 7-QA (§4): rename the stage, or declare the collision and let
   `check-vocabulary.py`'s V3 class carry it?
3. **Do the mom-cycle's own releases get plan files** (§2 constraint 3), or do loop-fired releases ship
   outside the pipeline and only engine/Track-B work go through it?
4. **The weather bot** pushes a live asset ~4×/day with no plan file and no gate (§1) — declared
   exception, or a hole in the "reaches her phone" gate?
5. **Is leg 6c PROXY absolute** on any release touching a Mom surface, or waivable with a reason like
   the other seats?
6. **Engine-objective ids** (§6): do `O3`/`O5` move to the engine's own `OBJECTIVES.md` with a distinct
   id form, or does every estate cite the same flat `O`-space?
