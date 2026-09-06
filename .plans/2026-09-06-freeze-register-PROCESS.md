# THE FREEZE REGISTER — one place that says what is frozen, and the process that keeps it true

**Author:** practice-steward · **Date:** 2026-09-06 · **Mode:** design (§1–§4) over audit (§5–§7)
**Commissioned by Paul, 2026-09-06:** *"we just need very clear documentation to process to manage and
ensure we're correctly not confusing ourselves with this data freeze. And then we've got a partial
unfreeze on the vehicles, but we've still not looked at any of her feedback, etcetera. All of that
needs to be considered at a granular level and tracked."*

⚠️ **This file carries no `stage:` key on purpose.** `tools/check-backlog-ready.py`'s stage enum has
now been unable to name five files that needed a word (`.plans/2026-09-04-process-wiring-AUDIT.md:7`,
`.plans/2026-09-05-state-of-the-work-PROPOSAL.md:13`, `.plans/2026-09-06-cascade-and-release-state-AUDIT.md:15`,
plus two `stage: draft` proposals) and the enum question is unruled. Adding a sixth illegal word would
be a sixth instance. **Proposed, not designed:** this file is a PROCESS artifact, not a plan; if the
register is adopted, §2 moves into `BACKLOG.md` and this file becomes its rationale.

⛔ **Nothing here is a priority call.** Every state below is copied from a ruling of Paul's, cited to
the file that holds it. Where two rulings disagree, §5 reports the disagreement and does not settle it.

---

## 0 · THE ONE RULE THAT MAKES A REGISTER WORK — Paul's to ratify

> ### A ruling that is not in the register is not in force.

Everything else in this document is bookkeeping. This is the only line that changes behaviour, and it
is a governance choice, not a mechanism — **no check can catch a ruling that was spoken and never
written.** The register's answer to a verbal ruling is not a detector; it is this rule, plus a habit:
the session that hears a freeze ruling writes the register line before it does anything else.

**Why this is not ceremony — measured tonight `[measured]`:**

| register | what it holds | last updated |
|---|---|---|
| `BACKLOG.md` § FOCUS FREEZE (:69–:127) | 11 rulings, 09-03 → 09-04 | **2026-09-04 11:16 ET** (`d41b2e7`) |
| `cycle/fleet/CYCLE-LOG.md` :18–:27 | the fleet loop's freeze **and its release** | 2026-09-05 (`69dfc14`) |
| `MOM-CYCLE-LOG.md` :22–:28 | her channels HELD | 2026-09-03 |
| `tools/pages-deploy.py` :40, :55 | *"The production home is her blank slate"* `[paul-ruled 09-06]` | 2026-09-06 18:09 (`9cb468d`) |
| `tools/archive-frozen-estate.py` :8–:11 | *"none of that should get lost"* `[paul-stated 09-05]` | 2026-09-06 00:12 (`2ccb896`) |
| session context only | the sunset intent stated tonight | never written |

Six registers, four of them files nobody would open to ask *"what is frozen?"* — two are **Python
docstrings**. `git grep 'FOCUS FREEZE' -- '*.py'` returns **zero**: no tool in this repo reads the
freeze block, so **every one of the 33 commands in `CLAUDE.md`'s session-start block is freeze-blind**
`[measured]`. The § FOCUS FREEZE text itself tells the reader to correct for this by hand — *"read its
FIRED against this note"* — three times.

---

## 1 · A FREEZE HAS THREE AXES — and every confusion so far has been an axis collapse

**Do not read this as a new model.** Paul has drawn this distinction himself, in his own words, three
times on three different days. The register's shape is derived from those three sentences.

| # | axis | the question it answers | Paul's own line drawing it |
|---|---|---|---|
| **W** | **WORK** | may we *work* on this? | *"we're freezing kind of the Fernwood-specific data and feedback cycle stages… I wanna focus at this point just on the large migration"* — `BACKLOG.md:71` |
| **P** | **PUSH** | may it *reach her*? | *"this note released the loop, not the deploy"* — `cycle/fleet/CYCLE-LOG.md:26` (the fleet release, 09-05) |
| **C** | **CHANNEL** | may we *read what she sent*? | *"this lifts the FEATURES hold, not the freeze on her channels"* — `BACKLOG.md:103`, recording `[paul-stated 2026-09-04 ~11:50]` |

⭐ **"Partial unfreeze" needs no new state word — it is one axis LIFTED while another stays FROZEN on
the same domain.** Paul's standing rule is to reuse the vocabulary before adding a state, on
demonstrated need. Checked before proposing `[measured]`:

- `VOCABULARY.md` has **no freeze vocabulary at all** — 15 ratified sections, none about hold state.
- `BACKLOG.md` § FOCUS FREEZE already uses **FROZEN · ACTIVE · HELD · LIFTED**, and `cycle/fleet/CYCLE-LOG.md:24` adds **RELEASED** as the *act* that produces LIFTED.
- Arrival state already has its own four-word vocabulary in `arrival-dispositions.json` / `momlib.py:1710-1714`: **undispositioned · bench-unheard · baselined · dispositioned**.

**So the register uses four words and invents none:**

| word | means | who may write it |
|---|---|---|
| **FROZEN** | the axis is shut. Work/pushes/reads on it do not happen | Paul |
| **HELD** | arrivals accumulate deliberately and are **not read**. Distinct from FROZEN: the channel is *open*, the *reading* is shut | Paul |
| **LIFTED** | was FROZEN or HELD; Paul released it. Carries the release act's date and words | Paul |
| **ACTIVE** | never frozen, or lifted and now being worked | Paul, or a session recording his instruction |

⚠️ **`RESTING · ARMED · FIRED` are the probes' words and stay theirs.** `fleet_probe.py` and
`mom-cycle-status.py` publish loop *readiness*, which is a different fact from permission. Neither
publishes a HELD phase and the § FOCUS FREEZE block says so — that is correct and should not be
"fixed" by teaching a probe the register's vocabulary. See §4(e).

---

## 2 · THE REGISTER — 2026-09-06, reconciled against HEAD `6d94a9a`

Four domains × three axes. **A cell with no ruling behind it reads `UNDECLARED`, never green.**

### Track A — Mom's field journal (`OBJECTIVES.md` O1 · O2)

| axis | state | who / when / whose words | release condition | queued behind it |
|---|---|---|---|---|
| **W** work | 🧊 **FROZEN** | `paul-stated 2026-09-03 14:11:59 ET`, `475872f`, text at `BACKLOG.md:71` | Paul's word | the frozen decision cards fernwood-1·4·5·6·8·9·11·12; the zone hold; ⚠️ **and see §5·C1 — tonight's onboarding goal is O1 work** |
| **P** push | 🧊 **FROZEN** to human commits | last human commit to `origin/main` = `315419c`, **2026-09-04 10:30:25 ET** `[measured]`. Branch consequence recorded `BACKLOG.md:96` | Paul's own `git push`; an agent push to `main` is classifier-blocked | **247 commits** on `origin/staging` she does not have; 17 SURFACE, **11 named by no plan stage-note** `[measured, qa-divergence.py --check, exit 1]` |
| **C** channel | ⏸ **HELD** (unread) | `paul-ruled 2026-09-03 16:43:04 ET`, `4e3c958`: *"Let's hold all feedback from mom. Let's not ingest it or action anything… I will say when to lift the freeze"* | **Paul's word alone.** Shipping C4/C5 was explicitly rejected as a condition | §3 |

### Track B — Fleet & equipment (O4)

| axis | state | who / when / whose words | release condition | queued behind it |
|---|---|---|---|---|
| **W** work | ✅ **LIFTED 2026-09-05** — *this is the "partial unfreeze on the vehicles"* | Paul opened lap 3 himself — *"launch a fleet cycle… focusing on the 200"* — recorded `cycle/fleet/CYCLE-LOG.md:24-27`. Lap 3 opened and **closed** the same day | n/a (lifted) | ⛔ **`BACKLOG.md:74` still reads *"lap 3 is FIRED on SEASON + INBOX and stays unrun on purpose"*** — false since 09-05 `[measured]`. §5·D1 |
| **P** push | 🧊 **FROZEN** | same branch as Track A · P. The door row of 09-05 states it: *"the freeze does NOT block writing to this repo… What is actually held is the PUSH"* (`cycle/requests.jsonl:52`) | Paul's word on the prod push | lap 3's residue: 3 named local commits + `TOOLS.md`/`vehicles.json`/guide edits, unpushed |
| **C** channel | 🟢 **ACTIVE — never frozen, and nothing drains it** | door declared 2026-08-28, `BACKLOG.md:5`: *"⚠️ Nothing sweeps that door on a cadence"* | n/a | **15 rows filed; the door reports 9** `[measured]` — §5·D3 |

### Track C — Engine / the migration (O3)

| axis | state | who / when / whose words | release condition | queued behind it |
|---|---|---|---|---|
| **W** work | 🟢 **ACTIVE — the only active Fernwood work** | `paul-stated 2026-09-03`, `BACKLOG.md:77` | n/a | C4 in pipeline; C5·C6·C7·Guru at Paul's stamp gate |
| **P** push | 🟢 **ACTIVE** — bare `git push` reaches QA | `paul-stated 2026-09-04 ~11:50`, mechanics at `BACKLOG.md:103`; local `main` tracks `origin/staging` | n/a | **8 local commits unpushed right now** `[measured]`, incl. tonight's `9cb468d` |
| **C** channel | 🟢 **ACTIVE** | peer-project asks arrive at `cycle/requests.jsonl` (Track B's door) and `cycle/mom/requests.jsonl` | n/a | — |

### Production — the new instance (`home` / `est-e6696a`) (O3 → O1)

| axis | state | who / when / whose words | release condition | queued behind it |
|---|---|---|---|---|
| **W** work | 🟢 **ACTIVE** | promoted + verified @ `bce212a`, 2026-09-05 ~23:00 (`.plans/2026-09-05-production-promotion-PLAN.md` stage-note) | n/a | that plan's own ⛔: *"synthetics have not given experiential feedback on production; Paul has not walked it; Mom has not been invited"* |
| **P** push | 🟢 **ACTIVE** — and **changed 20 minutes before this register was written** | `9cb468d`, 2026-09-06 18:09:36 ET: `home` joins the household allow-list and stops shipping `viewer.html` `[paul-ruled]` | n/a | unpushed; the ruling lives only in a commit message + `tools/pages-deploy.py:40,55` |
| **C** channel | 🟢 **ACTIVE, synthetic only** | `tools/read-onboarding.py --env home` | n/a | no real arrival has ever landed here `[inferred from the promotion plan's stage-note]` |

### The frozen instance as a DATA CONTROL — a fifth thing, and it is not an axis

| fact | evidence | grade |
|---|---|---|
| Her estate is `est-3c9f1a`, bound to the **top-level** Worker (`worker/wrangler.toml:31`) — not `[env.home]`, not `[env.qa]` | parsed | measured |
| It holds **175 KV keys, 2026-05-20 → 2026-09-05**; **171 of them are LEGACY unprefixed**, only 4 carry the `est-` prefix | key names only, from `.private/frozen-fernwood-archive/frozen-2026-09-06T000836.json` | measured |
| A **complete archive exists**: 175/175 keys, taken **2026-09-06 00:08:36**, mode 600, gitignored | same file's `keyCount` / `unreadable: []` | measured |
| The **first** archive run 5 minutes earlier missed `metrics:2026-05-29` (174/175) and **said so** | `frozen-2026-09-06T000342.json` `unreadable` | measured — the tool's positive control fired |
| **Nothing re-takes or verifies the archive.** `--verify` has no caller and no cadence; `git grep` finds the tool named in 1 plan + 1 sibling docstring | grep | measured |
| **The control is not static.** `origin/main` has taken **12 commits since the last human one** — 11 `weather-recorder[bot]`, 1 `fernwood-deployer[bot]` — on a 6-hourly cron | `git log origin/main`, `record-weather.yml:6` | measured |

---

## 3 · HER HELD ARRIVALS — tracked granularly, as a QUERY, never as a copied list

⛔ **Nothing in this section reads her words, and the register must never hold them.** The
`arrival-dispositions.json` `_meta.purpose` already states the rule for this repo: *"PUBLIC repo:
never her words and never a transcript, only where the record went."*

**Item-level tracking is possible without opening content, and the mechanism already exists**
`[measured]`:

- `momlib.undispositioned_arrivals()` (`tools/momlib.py:1656-1718`) returns, per arrival:
  `{channel, id, ts, deviceId, origin, state, owed_to_mom}` — **no note text, no transcript.**
- `tools/check-arrival-dispositions.py:49-54` prints exactly `tag · channel · id · timestamp`. Its
  per-item renderer is content-free **by construction**, not by care.
- Channels covered: `feedback · observations · zone-audio · guru` (`momlib.py:1530`). `pending-species`
  is deliberately outside the authored set.

**So the register stores no list.** It stores the query, the last reconciliation, and the count's
predicate — the same doctrine this repo already ratified for the trace (`BACKLOG.md` § C3: *"THE TRACE
IS A QUERY, NOT A FILE"*). A copied list of held arrivals would rot in the safe-looking direction
within a day; a query cannot.

```
python3 tools/check-arrival-dispositions.py          # item level, content-free: channel · id · ts
python3 tools/check-arrival-dispositions.py --json    # same, machine-readable
```

**Three limits that must travel with any count from it — a count without its predicate is not a fact:**

1. ⛔ **It cannot speak before 2026-08-28T00:00:00Z.** That is the declared `baseline`
   (`arrival-dispositions.json` `_meta.baseline`); 68 of the 69 arrivals found at first run sit behind
   it and are `baselined` — *governed by the channel watermark, never individually attested*. The
   baseline's own text says: **"Do NOT extend this date to quiet a finding."**
2. ⛔ **An arrival with no `id` is invisible to item-level tracking** (`momlib.py:1698-1699` skips it;
   the channel watermark still covers it). How many such records exist is **unmeasured** — it needs one
   read of each channel's records, which is a network fetch, and I did not make one.
3. ⚠️ **A channel it could not reach prints UNMEASURED, never 0** — correct behaviour, and it means a
   green line is not the same claim as a clean one.

### ⛔⛔ THE FREEZE'S OWN SANCTIONED TOOL BREAKS THE FREEZE — the finding that most needs Paul

`BACKLOG.md:88-90` permits exactly one thing during the hold:

> *"`read-mom-feedback.py --pickup` still fires at session start because it is the arrival detector;
> its output is a COUNT that says 'something is waiting behind the freeze' and nothing more. Do not
> open it, do not `--address` it, do not draft an ack."*

**That is false of the tool** `[measured, from source, not from a run]`:

- `tools/read-mom-feedback.py:556` prints her note verbatim beside each new answer —
  `print(f"  • [{verdict}] {subj}" + (f'  —  "{note}"' if note else ""))`
- `:578-580` prints up to 110 characters of every unanswered note, under the heading
  *"She told us N thing(s) nothing has answered yet."*

`render_counter` (`:166-206`) and `render_channels` (`:217-271`) **are** count-only and honour the
ruling exactly. `render_pickup` is not. So the session-start ritual mandated by `CLAUDE.md:23` will
print Mom's words into any session that picks up Fernwood while the hold is on.

⛔ **I did not run it, and I did not run the item-level census either** — the peer seat owns that
inventory. **This is a contradiction between a ruling and a mechanism, and resolving it is Paul's:**
either the ruling names a different tool, or the tool gains a content-free mode. Both are one-line
changes and I am not choosing between them.

---

## 4 · WHAT KEEPS THE REGISTER TRUE — mechanism where possible, discipline named where not

A freeze register is exactly the artifact class this repo has been burned by: it goes stale in the
**safe-looking** direction (it keeps saying *frozen* after a release), and `BACKLOG.md:74` is already
an instance, 26 hours old. So the mechanism is specified as three machine-checkable assertions, one
governance rule, and an honest statement of what no check can reach.

### (a) Canonical form: `freeze.json` + a GENERATED block in `BACKLOG.md`

`BACKLOG.md`'s own opening says it is *"Single source of truth for Fernwood backlog statuses. When any
other doc disagrees, this file wins."* A separate register file would be a second tracker — the exact
thing its § NEXT list warns against. So:

- **`freeze.json`** (repo root, tracked) is canonical and machine-readable: one object per
  `domain × axis`, each with `state` (the four words) · `ruledBy` · `ruledAt` (ISO, ET) · `words`
  (verbatim) · `evidence` (file:line or sha) · `releaseCondition` · `queuedBehind` · `permittedWriters`.
- **`tools/freeze.py --render`** writes the §2 table into `BACKLOG.md` between
  `<!-- freeze-register:start -->` / `<!-- freeze-register:end -->` markers.
- **`tools/freeze.py --check`** asserts (b)–(d) and **fails closed** when `freeze.json` is absent.
- The local precedent to copy is `tools/instance-recipe.py --check` (generated doc, hand-kept log) and
  `tools/pages-deploy.py` (a check **wired into the act it guards**, not merely named).

### (b) Assertion 1 — the register is BEHIND A WRITTEN RULING (deterministic)

Scan every tracked file for `[paul-stated|paul-ruled|paul-decided|paul-approved|paul-did] YYYY-MM-DD`
stamps. **RED when the newest such date anywhere in the repo is later than `freeze.json`'s newest
`ruledAt`,** listing the files that carry it.

This is the detector for tonight's actual failure: `9cb468d` put a `[paul-ruled 2026-09-06]` freeze
ruling into `tools/pages-deploy.py:55` and no register learned of it. **The check would have been red
at 18:09.** It is cheap, has no network dependency, and cannot be permanently red — writing the line
clears it.

⚠️ **Its blind spot, stated rather than hidden:** it catches *written-somewhere-but-not-here*. A ruling
that was spoken and never written is invisible to it, and §0 is the only answer to that.

### (c) Assertion 2 — a FROZEN push axis is checked against the world (deterministic)

For each domain whose **P** cell reads FROZEN: `git log <ref> --since <ruledAt>` must contain **no
commit from an author outside `permittedWriters`.** Red on the first human commit to a frozen branch.

⭐ `permittedWriters` is a required field precisely because the honest answer today is
`["weather-recorder[bot]", "fernwood-deployer[bot]"]` — a silent exclusion would make the check green
over a mutating control, and an unlisted bot would make it red every six hours. **Neither is
acceptable and the field forces the choice to be declared.**

**Falsifier for the check itself:** cherry-pick any human commit onto a scratch ref that the register
declares FROZEN; the check must go red. If it does not, it is measuring the register, not the world.

### (d) Assertion 3 — axis coverage, and UNCHECKABLE is not green

Every domain in `freeze.json` carries all three axes. A missing cell prints `UNDECLARED` and exits
non-zero. Following the control shape ratified in `.plans/2026-09-06-one-environment-DECISIONS.md`
§F2 — *"an instrument's scope must be DERIVED from whatever declares reality, and a derivation that
finds nothing must read UNCHECKABLE — never green"* — the domain roster derives from
`worker/wrangler.toml`'s declared environments plus the two tracks named in `BACKLOG.md`'s header,
**not** from a typed list in `freeze.py`.

### (e) Where the check is SITED — and it is not the session-start block alone

| siting | what it can actually stop | recommendation |
|---|---|---|
| `CLAUDE.md` session-start block | nothing; it is an index | add it — as the reader's index, per that block's own doctrine |
| **`.git/hooks/pre-push`** | ⭐ **a push to a FROZEN branch** | **wire it here.** The hook already runs `check-public-build.py` + `check-qa-fixtures.py` and already special-cases `main` |
| `build-viewer.yml` CI | a merge | optional; the pre-push hook is the real gate |

**This is the whole reason to prefer (c) over prose:** the PUSH axis is the only axis with an
irreversible act behind it, and Paul's own rule is that the gate sits on irreversible acts.

### (f) What NO check can reach — say it plainly rather than proposing a check nobody will run

1. **The WORK axis is an attestation, not a measurement.** "Did anyone work on frozen Track A content?"
   has no deterministic answer — a commit touching `plants.json` may be engine work, instance work, or
   a defect fix. Any detector here would be permanently amber and would teach its reader to ignore it.
   **Leave it as an attestation and label it one.**
2. **The CHANNEL axis cannot prove nobody read.** `.private/channel-read-state.json` records
   `readThrough` with `by: "human attestation"` for three of four channels — an attestation by
   construction. A `--mark-read` stamp is not a read; this portfolio has already ratified that.
3. **A verbal ruling.** §0.

**So the honest summary is: one axis of three is machine-checkable, the other two are disciplined
bookkeeping, and the register's value is that it says which is which on its own face.** A register
that implied uniform rigor would be worse than none.

### (g) Reconciliation, and the thing that most often goes wrong

`freeze.json` carries `reconciledAt` + `reconciledAgainst: <sha>`, and `--check` prints both on every
run. **The register is not claiming to be true; it is claiming when it was last checked** — the same
move as the Mom-check counter (`read-mom-feedback.py:166-206`), which exists because *"a quiet watcher
and a dead one look IDENTICAL in a log."*

⚠️ **Do not compute a staleness age and nag on it.** A lap that has not run is not late, and a
register reconciled two days ago is not wrong. Print the date; let the reader judge.

---

## 5 · CONTRADICTIONS THE REGISTER MUST CARRY AND MUST NOT RESOLVE

These are for Paul. Each is two rulings or a ruling and a record that cannot both be true. I state the
evidence and the direction of error, and stop.

### C1 · The freeze rests O1; tonight's goal is O1 work
`BACKLOG.md:77` — *"`OBJECTIVES.md` **O1 · O2 · O4** rest"*; O1 is *"Mom uses Fernwood as her field
journal, on her own initiative"* (`OBJECTIVES.md`). Moving Mom onto production and onboarding her is
O1 work by that definition. Either O1 is no longer resting, or "the migration" now includes it. **The
register cannot state Track A · W without this answer.**

### C2 · "Pour her input into the new instance" vs. "her blank slate"
- `[paul-stated 2026-09-04 ~10:45]`, `BACKLOG.md:99`: the held feedback *"is poured into that instance
  at transfer time."* The 09-04 development goal adds *"her data reaching the new estate server-side
  (notes, observations, `momQueue.*`)."*
- `[paul-stated 2026-09-05]`, `tools/archive-frozen-estate.py:8-11`: she *"will rebuild Fernwood from
  scratch,"* the frozen version *"becomes a data control,"* and *"all the input that she's provided
  over time since we froze it — none of that should get lost."*
- `[paul-ruled 2026-09-06]`, `tools/pages-deploy.py:55`: *"The production home is her blank slate."*

⭐ **These probably reconcile as PRESERVED-not-MIGRATED, and the tool built on 09-06 00:12 reads that
way** — but that is a supersession of a ruling that still stands in `BACKLOG.md`, and **only Paul can
confirm a supersession.** ⚠️ It is load-bearing for the sunset: *pour in* requires an import path that
does not exist; *archive* requires only that the archive be current.
(A peer seat has flagged the same collision from the other side —
`.plans/2026-09-06-conversion-method-DESIGN.md:783` §B1.)

### C3 · The data control and the lock-out are compatible — but only in one of two shapes
Not rhetorical, and the answer is structural rather than a judgment:

| shape | what "locked out" means | does the control survive? |
|---|---|---|
| **A — control as ARTIFACT** | unpublish / gate the Pages origin; her live app stops loading | ✅ yes — the 175-key archive + the git sha are the control. **Both already exist.** |
| **B — control as LIVE SITE** | her access must be *gated*, not removed, because the site must stay loadable for comparison | ⚠️ needs a build: her origin has **no access control to revoke** (public GitHub Pages), so gating it is new work of the kind QA already has (Cloudflare Access) |

They are in tension **only under shape B.** Under shape A they are fully compatible, and shape A is
what the tooling built on 09-06 already assumes. ⛔ **Which shape is Paul's call, not mine** — it turns
on whether the comparison he wants is against a *snapshot* or against a *running app*.

### C4 · The archive is complete as of 00:08 today; her instance is still live
The complete archive was taken **2026-09-06 00:08:36**. Her Worker still accepts writes on four
channels and the weather bot still commits to her branch every six hours. **Any input since 00:08 is
outside the archive** — 18h 30m as of this file. Nothing schedules a re-take. This is not an error; it
is an ordering constraint the sunset must respect (§ audit file, Q4).

### D1 · `BACKLOG.md:74` is FALSE and errs toward *more frozen*
It reads *"Track B fleet laps (lap 3 is FIRED on SEASON + INBOX and **stays unrun on purpose**)."*
Lap 3 ran and **closed** on 2026-09-05 (`cycle/fleet/CYCLE-LOG.md:45`, `cycle-state.json` `lap_count: 3`,
`last_lap.outcome: "closed"`). ⭐ **The fleet chronicle recorded the release correctly and kept the old
note beside it** — *"Kept rather than deleted so the two are not read as one."* The defect is that the
canonical file was never updated. **Direction of error: it would have stopped someone from doing work
Paul had already released.** That is the "partial unfreeze" being invisible in the one place a reader
looks — and it is why he asked for this register.

### D2 · `data/cycle-state.json` says nothing is waiting
`state: ARMED`, `unresolved_arrivals: 0`, `generated_at: 2026-09-01T23:24`. Five days old, and written
before the hold existed. **Direction of error: it says the mom loop owes nothing while arrivals are
being held.** Any board reading it would render Track A as clean.

### D3 · Both directions of error in one file — `cycle/requests.jsonl`
15 data rows. `fleet_probe.py:112` counts a row only when `(r.get("status") or "open") == "open"` → **9**;
the other **6** are invisible, and the probe's own zero-branch prints *"inbox clear (N filed, all
handled)"*. Meanwhile row 41's disposition still reads *"ROUTED, NOT RESOLVED"* while `BACKLOG.md:1322`
reads *"✅ P7 RESOLVED."* **The door under-reports open work on 4 rows and over-reports it on 1, in the
same file.** Full reconciliation in the audit file, Q2.

---

## 6 · FALSIFIERS — what would show this design wrong

| claim | falsifier |
|---|---|
| Three axes are enough | a ruling Paul makes that cannot be written as one cell of (domain × W/P/C) without losing meaning |
| No new state word is needed | Paul says a domain is in a state that FROZEN · HELD · LIFTED · ACTIVE cannot express |
| §4(b) catches the real failure | a written `[paul-*]` freeze ruling lands and the check stays green |
| §4(c) measures the world | a human commit reaches a FROZEN branch and the check stays green |
| The register is worth its upkeep | at its first reconciliation, zero lines have drifted — then prose was sufficient and this is ceremony |
| Item-level arrival tracking needs no content | any granular question Paul asks that `channel · id · ts` cannot answer |

## 7 · RECONCILIATION RECORD

| reconciled at | against | by | drifted lines found |
|---|---|---|---|
| 2026-09-06 ~18:45 ET | HEAD `6d94a9a` · `origin/main` `294c0b4` · `origin/staging` | practice-steward (proposal; **not adopted**) | **§5 · D1 · D2 · D3 · C2** — 4 registers disagreeing, 2 rulings on disk only in Python docstrings, 1 verbal |

⛔ **Nothing in this file has been adopted.** No tracked file was edited to produce it, `freeze.json`
does not exist, and `tools/freeze.py` does not exist. If Paul says go, the build order is:
`freeze.json` (hand-written from §2) → `--check` (b/c/d) with its mutation falsifiers → pre-push wiring
→ `--render` into `BACKLOG.md` last, so the generated block never precedes a working check.
