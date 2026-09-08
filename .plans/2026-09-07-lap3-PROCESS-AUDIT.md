# LAP 3 · PLAN vs ACTUAL — the divergences so far, and the gaps beats 2 and 6–11 will hit next · AUDIT

- row: process (no BACKLOG row — same posture as the flex-point AUDIT and the lap-boundary PROCESS)
- objective: O5
- class: engine · declared (process machinery; nothing here is a module, a feature, or a ranking)
- kind: audit
- seats: practice-steward — the whole file
        engineering-partner → owed at three places and designed at none: §2 G1's disposal mechanism,
          §2 G8's channel-age parse, §2 G9's check roster. Named, not scoped
        user-researcher → owed at §2 G2 only (beat 7's empty-set report). Waived at authoring
        ux-expert · content-steward · ai-advisor → waived: no surface, no word that reaches a person,
          and no model sits on any path in this file
- depends-on: .plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md
- depends-on: .plans/2026-09-07-lap3-BRIEFING.md
- depends-on: .plans/2026-09-07-lap2-RETRO.md
- depends-on: .plans/2026-09-07-lap3-CONSOLIDATION.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ **NOTHING IN THIS FILE EXECUTES.** Read-only. ⛔ **Nothing is ranked.** Every ordering below
  is dependency and sequence. Where a call needs real-world context — which records count, which of
  three routes to take — this file **lays out the board and stops.**
- stage-note: 2026-09-07 — ⚠️ **this document deliberately carries NO `stage:` key.** R4
  (`check-backlog-ready.py:263-302`) says a `-AUDIT` document declares `kind:` *instead of* `stage:`,
  and a legal stage on a doc-suffix file raises *"is it a document or an item? [R4, unresolved]"*.
  Written at HEAD `3b3e193`; every measurement below was taken between 3b3e193 and this write, and
  each names its file and line. Grades: `measured` · `inferred` · `proposed`.

---

## 0 · THE ONE-LINE ANSWER

> **Lap 3's execution is better than its plan and worse than its record.** Every ruling was applied to
> the document that describes the loop and only some were applied to the code that publishes the same
> fact; every honest shortfall was written into the chronicle and none of it was written into the
> artifact that will be read at close. **The divergences are not scattered — eight of the ten below
> are one shape: a change lands in one of a pair of places that hold the same claim.**

---

## 1 · PLAN vs ACTUAL — ten divergences, each graded, each with a verdict

⚠️ **The plan is not the standard.** Three of the ten are the plan being wrong and the execution being
right, and those are the ones that need writing DOWN, not correcting.

### 1.1 ⛔ D1 · TWO THINGS ARE CALLED "BEAT 1" — and it is the collision found tonight, one file over

`measured`:

| document | what "beat 1" is | line |
|---|---|---|
| `cycle/release/CYCLE-MAP.md` — the RATIFIED map | **a BUILD exists** | `:45` |
| `.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md` §4 | **CONSOLIDATE** | `:201` |
| `cycle/release/CYCLE-LOG.md` — the CHRONICLE, written tonight | **the end-to-end proof** (consolidation) | `:1192` |
| commit `9880e58` subject | *"beat 1 consolidation"* | — |

Under A-1 as ratified, the work the chronicle files as *beat 1* is **beats 6–8** (F3 dispose = beat 6,
DISPOSE, owner **Paul**). So the record already shows beat 6 partially firing while calling it beat 1,
and a reader asking *"has beat 6 run?"* gets **no** from the headings and **yes** from the content.

⭐ **The reusable part:** commit `9880e58` wrote a rule for exactly this — *"a walk is filed under the
sha it walked — a sha is unambiguous across every sequence here, an ordinal is not"* — after
`GATE2-paul-findings.md` hid **both** of Paul's release walks behind its own lap ordinals. The rule was
written and **not applied one file over, the same night, to a second ordinal collision.**

**Verdict: the PLAN is wrong** (its numbering predates A-1 by hours), **and the defect is that nothing
carried the new rule from the file where it was learned to the file where it was needed.**

**Falsifier:** if `release-state.py` or any reader resolves chronicle beat numbers against the map's,
the collision is cosmetic and I am overstating it.

### 1.2 ⛔ D2 · A-1 WAS APPLIED TO THE MAP AND NOT TO THE INSTRUMENT — and the board is publishing it

`measured`, `tools/release-state.py`:

    :102   "beat": {"n": beat, "of": 5, "owner": owner,
    :103    "name": {2: "the synthetic loop", 3: "Paul walks it", 5: "Paul cleared it"}[beat]},

The ratified map has **twelve** beats (0–11). The instrument can publish **three** of them and hard-codes
`of: 5`. Live consequence, `measured` tonight:

- `cycle/release/cycle-state.json` reads `beat {n: 2, of: 5, "the synthetic loop"}` while the loop is
  in the estate-manager beats;
- `operating-layer/config/projects.json:446` records the verified render as
  *"open since 2026-09-07 · beat 2 of 5, owner session"* — so **the portfolio board is now publishing a
  beat number that the ruling made wrong**, and the commit that verified the render (`0f2cd64`) checked
  *that* it rendered and not *what* it rendered.

**Verdict: DEFECT.** A ruling reached the document and not the code that states the same fact.
**Falsifier:** if beats 0 and 6–11 are derivable elsewhere and `release-state.py` is deliberately
scoped to the release sub-loop only, this is a labelling problem and not a wrong value — but then the
label must say `beat 2 of 5 (release beats)`, because `of: 5` against a 12-beat map is a false denominator.

### 1.3 ⛔ D3 · LAP 3'S FIVE PRE-REGISTRATIONS EXIST IN PROSE ONLY

`measured`: `.plans/2026-09-07-lap2-RETRO.md:426-438` pre-registers **P1–P5**.
`cycle/release/cycle-state.json` `pre_registered[]` holds **two** entries — both lap-1's, both now
disposed. P2, P3, P4 and P5 are in **no** artifact.

The mechanism, `measured` at `tools/release-state.py:111`:

    "pre_registered": prior.get("pre_registered") or [ <the two lap-1 seeds, hardcoded> ],

It **carries forward and never adds.** Nothing writes a new lap's questions, and beat 0's exit condition
(`CYCLE-MAP.md:60`) requires *"its pre-registrations are disposed"* — the prior lap's — and says nothing
about **writing this lap's**.

⭐ This is the spine's own named failure, inverted. `~/.claude/rituals/CYCLE-SPINE.md:227-229`: *"that
rule governs WRITING the pre-registration at close N and says nothing about DISCHARGING it at close
N+1, which is exactly why lap 1 was compliant while closing over its own question."* Here discharge is
wired and **writing is not** — so at lap 3's close the loop will discharge lap 1's questions again and
have nothing to read for P2–P5.

**Verdict: the PLAN is wrong** — beat 0's step list is missing a step. **Falsifier:** if a close-time
procedure writes the next lap's pre-registrations, the gap is at close and not at open, and the fix
moves rather than disappears.

### 1.4 D4 · `pre_registered[].disposition` PUBLISHES WORDS OFF THE SPINE'S ENUM

`measured`: the spine's enum is `open | answered | carried | dropped`
(`~/.claude/rituals/CYCLE-SPINE.md:209-211`). The file publishes **`"closed"`** and **`"retired"`**.
`tools/momlib.py:1726` defines `VALID_LAP_OUTCOMES` for the sibling field and **there is no equivalent
constant for this one.**

⚠️ Same class as the defect this loop *fixed* tonight — `last_lap.outcome` publishing `"cleared"`, a
word off the enum (`24d17f5`, and the chronicle records it at `CYCLE-LOG.md:922`). It was corrected in
one field and re-created in the neighbouring field **in the same commit**.

**Verdict: DEFECT**, and a one-constant one.

### 1.5 D5 · C-1 IS ~60% APPLIED, AND WHAT IS LEFT IS THE MAP'S OWN SELF-CONFORMANCE TABLE

The retro named **seven** documents (§4.4). `measured` tonight:

| document | retro said | state now |
|---|---|---|
| `CYCLE-MAP.md` § The beats | no beat for the feedback | ✅ amended (`24d17f5`, +47) |
| `CYCLE-MAP.md` § **Conformance** | S1 and S6 are built; S4 genuinely unmet | ⛔ **UNTOUCHED** — `:181-186` still reads `S1 ⬜ to build · S4 ⬜ to record · S5 ⬜ · S6 ⬜ to build` |
| `CYCLE-MAP.md` § TWO CLASSES OF WALKER | *"should say the flag exists and the journey behind it does not"* | ⚠️ **see below — the retro row is itself wrong** |
| `CYCLE-LOG.md` lap-2 section | omits the three unmapped repairs; names 8 shas where 11 were walked | ⛔ not amended in lap 3's commits |
| `CYCLE-LOG.md` lap headings | do not parse | ✅ `590a551` |
| `cycle/release/cycle-state.json` | frozen, off-enum outcome | ✅ `24d17f5` |
| `GATE2-paul-findings.md` | both walks missing | ✅ `9880e58` |

⭐ **The conformance row is the sharp one.** S1 (`cycle/release/cycle-state.json`) exists and is rewritten
on every commit by a hook; S4 was **ruled** tonight (A-5, the two-half closing condition) and `--cleared
1e2748d` was **run**; S5's `pre_registered[]` is populated; S6 (`release-gate.py` prints one screen) is
built. The table under-reports in the *pessimistic* direction — the rarer, and still wrong. **`24d17f5`
edited that file and left the table 130 lines below untouched.**

⚠️ **A CONTRADICTION I AM REPORTING, NOT RESOLVING.** The retro asks the walker section to say *"the flag
exists and the journey behind it does not."* `measured`: **neither exists** — `tools/journey-view.py:64`
hardcodes `viewport: { width: 414, height: 848 }`, and `grep -n 'carry-state\|carry_state'` over that
file returns **zero**. So the map's current text (*"none of it built yet"*) is TRUE and the retro's
instruction to change it was wrong. Which document to amend is a call about what C-2's scope now is.

### 1.6 D6 · AN ARTIFACT WENT STALE INSIDE ITS OWN LAP, IN UNDER AN HOUR

`measured`: `.plans/2026-09-07-lap3-CONSOLIDATION.md:140` states *"The end-to-end proof (F1→F6) **has not
run**."* The **very next commit**, `3b3e193`, ran it — and touched only `cycle/release/CYCLE-LOG.md` and
`feedback-dispositions.json`. The plan file was not amended and carries no stage-note.

**Verdict: DEFECT**, and it is the counterfactual-gap shape at its shortest observed interval: the
chronicle got the update, the `.plans/` file that stated the opposite did not.

⚠️ **AND THAT FILE IS GRADED BY NOTHING.** `measured`: `-CONSOLIDATION` is not in `DOC_SUFFIXES`
(`check-backlog-ready.py:72-73`) and the file is neither a `-PLAN` nor a `-PROPOSAL`
(`:254-255`), so it falls through both loops — `python3 tools/check-backlog-ready.py | grep -c
CONSOLIDATION` returns **0**. It carries a full header block including `stage: draft` that nothing
reads. **Beat 1's entire output — the four-channel census, rows T1 and T2, and the single-disk finding
about the register — sits in a file no instrument can see and no BACKLOG row points at.**

### 1.7 D7 · BEAT 1 MET ONE OF ITS THREE EXIT CLAUSES, AND NOTHING CARRIES THE OTHER TWO

Procedure §4 beat 1 exit: *"one record has made the full F1→F6 trip · the captures are one document ·
the walk is in the findings register with its third column answered."* `measured`:

| clause | state |
|---|---|
| the full F1→F6 trip | ⛔ **four of six.** F4 and F5 never exercised — the chronicle says so plainly and `3b3e193` says so in its own message |
| the captures are one document | ⛔ **not done.** `.plans/2026-09-07-lap3-paul-feedback-CAPTURE.md` and `-CAPTURE-2.md` both still exist; `grep -in merge` over the CONSOLIDATION returns **zero** |
| third column answered | 🟡 **partial.** Filed, with F7/F8/F9 left honestly UNANSWERED |
| retro **C-7** (count the repeat ask — one column) | ⛔ **not applied.** `grep -n "asked before\|repeat"` over `GATE2-paul-findings.md` returns **zero** |

⛔ **And beat 1 has no closure table.** Beat 0 got a six-row `Beat 0 · CLOSED` table naming step 4 as
UNCHECKABLE. Beat 1 has none, so its two unmet clauses exist only as prose inside sections about other
things. **This is the loop's own argument against itself** — its words at beat 0 step 4: *"an
undischargeable step teaches the loop that steps need not be discharged."*

**Verdict: plan fine, execution incomplete, and the incompleteness is unrecorded in the place a close
would read.**

### 1.8 D8 · NINE RULINGS, ZERO REGISTER ROWS

`measured`: `grep -rn "J-d" .plans cycle BACKLOG.md PRODUCT-ENGINE.md CLAUDE.md` → four hits, three in
`.plans/` and one at `CYCLE-LOG.md:1053`, whose *"where it landed"* column reads literally
**`*pending: reading confirmed with Paul*`**. `BACKLOG.md` contains **no** reference to A-1, A-2, A-3,
A-5, A-6, J-c or J-d.

Where each ruling actually landed: A-1/A-5/A-6 → `CYCLE-MAP.md`; A-2/A-3 → `check-backlog-ready.py:60`
and `:85`; J-c → `release-state.py` + `momlib`; charters → `product-steward-CHARTER.md`; **J-d →
nowhere**. Every one of them is *also* recorded in the chronicle, which is right. **None is in a
register a reader who is not reading this chronicle would find.**

⭐ This is the standing measured finding firing again at nine-times scale in one evening
(`[[project_backlog_coherence_finding]]` — *"09-07 re-measured: drop rate 1.5%, ruling→register is the
gap"*). **In my lane, and this is the whole of the claim:** the staged pipeline advances items on
rulings; an item cannot be advanced on a ruling the pipeline cannot see. J-d is the worked example —
the briefing says it blocks **C5**, and C5's plan of record (`PRODUCT-ENGINE.md` § THE SEQUENCE) does
not know it was ruled.

### 1.9 D9 · THE TWO THINGS THE BRIEFING SAID LEAD THE LAP HAVE NO CARRIER

`measured`: **GAP 1** and **GAP 2** appear in `.plans/2026-09-07-lap3-BRIEFING.md` §2 and are referenced
three times in `CYCLE-LOG.md` lap 3. There is **no BACKLOG row, no `.user-research/` artifact, and no
`pre_registered[]` entry** for either.

They are also the only lap-3 work with an **external dependency** — a house visit, riding on a visit
already ruled to happen. `inferred`: work whose trigger is outside the repo and whose record is inside
one prose file is the class that gets discovered after the window closes. Nothing structural will
surface them at beat 10.

### 1.10 ⭐ D10 · THREE PLACES THE PLAN WAS WRONG AND THE EXECUTION WAS RIGHT — write these DOWN, do not correct them

1. **A-4 was refused as stale.** The procedure asked whether the FOCUS FREEZE binds Mom's arrivals on
   `est-e6696a`; J-a had answered it the same evening. The execution declined to re-ask. ✅
2. **Beat 0 step 4 was recorded UNCHECKABLE rather than clean.** The procedure's step list has **no
   UNCHECKABLE state** — the execution invented one, correctly, and refused the `0 gates — clean` that
   would have been lap 2's own finding #2 committed inside the lap that recorded it.
3. **A finding was retracted with the wrong claim left in history.** The procedure has no retraction
   step. The execution created one and preserved the error deliberately.

⛔ **All three are amendments the map should absorb**, or the next lap will re-derive them under
pressure. Beat 0's exit condition currently admits only *done*; it needs to admit **UNCHECKABLE with a
named reason**, and the map needs a line saying a finding is retracted in place, never amended away.

---

## 2 · ⭐ GETTING AHEAD OF IT — what beats 2 and 6–11 will hit, and the cheap thing now

**The predictive basis, stated so it can be checked:** eight of the ten divergences above are one shape —
*a claim lives in two places and the change reached one of them.* The other two are *an ordinal
sequence collided with another ordinal sequence.* Everything below is those two shapes projected onto
beats that have not run.

### ⛔⛔ G1 · BEAT 11'S EXIT CONDITION IS STRUCTURALLY UNREACHABLE — this is the one to look at first

`measured`, `python3 tools/watch-feedback.py` run 2026-09-07 at HEAD `3b3e193`:

| env | estate | records | awaiting |
|---|---|---|---|
| qa | `est-qa0001` | 431 | **431** |
| lab | `est-lab0001` | 38 | **38** |
| home | `est-e6696a` | 10 | **7** |
| prod (frozen) | `est-3c9f1a` | 1 | **1** |
| bob · paul | — | 0 | 0 |
| | | | **477** |

The map's **beat 11** exit (`CYCLE-MAP.md:66`) is *"zero records undisposed; the next beat 0 may open."*
The map's **beat 10** gate (`:75`) is *"the board may not be laid out while records nobody has read are
sitting in the store."*

`measured` on the mechanism: `--dispose-all` does not exist and no pattern match is possible
(`3b3e193`'s own message); the tool's closing line prints only the single-key form
`--dispose '<key>' --as … --why "…"`. Disposal is **one hand-written reason per record**, and **F3 is
Paul's beat** by ruling.

⭐ **A provenance fact, not a value fact:** 431 of the 477 carry ids the loop's own synthetic walkers
wrote — `fb-qaprobe-*`, `onboard-name-*`, `onboard-address-*`, `probe-*`, `p-qa-synth-1` — visible in
the sweep's own output.

**What I am claiming, and it is entirely inside my lane:** *an exit condition that no available
mechanism can produce is not an exit condition.* As written, beat 11 can never arm, so lap 4's beat 0
can never legitimately open, and beat 10's gate is unmet for the same reason. **Two ratified
conditions currently deadlock the lap**, and leaving it teaches the loop that beats need not close —
the loop's own argument for retiring `second-viewport` tonight.

⛔ **What I am NOT claiming:** that production records matter more than QA probes. **Three routes,
unranked, dependency stated. Paul rules:**

| | route | what it depends on |
|---|---|---|
| **a** | beat 11 counts only records the loop did not author; machine-authored ones are disposed **by class at the moment the walker writes them** | a provenance field the walker sets — engineering-partner |
| **b** | a bulk disposition over a **named provenance class**, one command, one reason | a `--dispose-class` — engineering-partner |
| **c** | accept 477, leave beat 11 unmet, and record the shortfall under closing-condition **half (b)** | nothing; it is free and honest, and it makes the beat permanently open |

**Falsifier for the reachability claim:** if a disposal call already exists that closes a class in one
invocation, or if Paul disposes 477 in one sitting, I am wrong and the beat is fine as written.

### G2 · BEAT 7 WILL FIRE ON AN EMPTY SET AND IT WILL LOOK LIKE IT WORKED

`measured`: beat 7 reads only `act`/`fold`. The only dispositions in existence are **three
`not-a-finding`**, which beat 7 excludes by design, so **F4 and F5 have still never carried anything.**

`inferred`, and it is the shape the loop caught twice tonight: *a zero from a beat that was never fed
reads identically to a zero from a beat with nothing due.* Beat 0 step 4 refused exactly this; beat 7
has no such refusal built.

**Cheap now:** beat 7's record prints the count of `act`/`fold` records it read and reports
**UNEXERCISED** at zero — never *done*, never *clean*. One line, same idiom the chronicle already used
for step 4. **Falsifier:** if a beat-7 run at zero already refuses somewhere I did not find, drop this.

### G3 · BEAT 8'S ESCAPE CLAUSE HAS NO NAMED DESTINATION

Beat 8's exit: *"each finding reaches a row it can **cite**, or **opens a question** where it cannot."*
`measured`: **the second half has no file.** Tonight's evidence for what happens to an unhoused ruling
is D8 (nine rulings, zero register rows) and D6 (rows T1 and T2 sitting in a file no checker grades).

**Cheap now, and it is a naming decision, not a build:** name the destination for both halves before
beat 8 runs — the row's file for a carried finding, and one named file for an opened question. If the
answer is `BACKLOG.md` for both, say so; the failure mode is that it is decided per-finding, at speed,
by whoever is writing.

### G4 · THE BOARD WILL BE ASSEMBLED FROM FIVE REGISTERS THAT DO NOT SHARE AN ID SPACE

`measured` inputs that exist today: the **47-row census** (RESEARCH-BRIEF §4, ids A1…J7), **477
feedback records** (ids `env|estate|channel|id`), **F1–F15** in `GATE2-paul-findings.md`, **T1/T2** in
the CONSOLIDATION, **GAP 1/GAP 2** in the briefing, the **nine rulings** (A-1…J-d), and BACKLOG's own
tiers. At least three of those use bare ordinals, and **two of them already use `F<n>`.**

`inferred` from D1 and from tonight's GATE2 collision: two independent sequences that each read current
is this corpus's most repeated register failure, and it has now happened twice in twelve hours.

**Cheap now:** **a board row is identified by `register:id`, never by an ordinal** — `census:F4`,
`gate2:F14`, `feedback:home|est-e6696a|feedback|…`. This is the generalisation of the rule `9880e58`
already wrote for walks. One column. **Falsifier:** if the board is built and no two rows collide, it
cost a column and nothing else.

### G5 · BEAT 10'S BOARD LENGTH IS PREDICTABLE NOW — and there is a non-ranking way to shorten it

A-6's own falsifier is *"if the board is consistently so long that picking from it is the bottleneck."*
That is currently readable only by argument at close.

⛔ **Not a value call, and this is the only lever I am allowed to offer:** require every board row to
carry **`blocked-on:`** and **`target rung:`**. A row blocked on something not in hand this lap is **not
reachable this lap** — dependency, not importance — and the board collapses by reachability without
anyone ranking anything. It also makes closing-condition **half (b)** ("at or past its target rung, or
the shortfall recorded") checkable instead of narrative, which is the half A-5 exists to protect.

### G6 · P2 IS UNREACHABLE UNLESS C-2 LANDS FIRST, AND NOTHING SAYS SO

`measured`: P2 asks for one **non-`--fresh`** run at lap 3's cleared sha with < 5 failed actions.
`tools/journey-view.py:64` hardcodes `viewport: { width: 414, height: 848 }`; `carry-state` /
`carry_state` appear **zero** times in that file; **0 of 39** lap-2 walks were non-`--fresh`. Beat 2
cannot produce a returning walk with the harness it has.

**Sequence claim:** C-2 (engineering-partner) is a **prerequisite** of P2. When P2 is written into
`pre_registered[]` (per D3), it should carry that blocker by name so it discharges as **`carried` with a
reason** rather than reading as a miss at close. ⛔ Whether C-2 gets built this lap is Paul's.

### G7 · GATE ①'s UX CLAUSE IS A PERMANENTLY-AMBER CONTROL

`measured`: `tools/release-gate.py:260` prints *"UX sweep for this build — UNCHECKABLE: no artifact
convention exists yet"* and `:263` converts every all-seats-pass into *"🟡 … this is **NOT** a bare
pass."* **No lap's behaviour can change that state.** Only defining what a UX-sweep artifact for a build
looks like clears it.

Per Paul's own standing rule — never install a control whose alarm is permanently on — this one has
been on since it was written. It is *honest* (it fails closed, which is right), but a clause that
cannot change state carries no information about any build. **What clears it is a convention, and
`tools/check-ux-sweep.py` already exists with its own clock.** ⛔ Defining the convention is content
and is not mine.

### G8 · AN INSTRUMENT IN THE BEAT-0 SWEEP IS PRINTING A PLAUSIBLE WRONG NUMBER

`measured`, from tonight's `watch-feedback.py` run:

    📦 channel `library` holds 8114 day(s) and NO TOOL READS IT

8,114 days is ~22 years. The age is being computed off something that is not a timestamp. It will print
in **every** beat-0 and beat-6 sweep from here. `[[reference_match_payload_not_container]]` — the
wrapper check returns a plausible number, never an error. **Cheap:** the channel-age line refuses to
print an age it cannot parse. → engineering-partner.

### G9 · NO DOCS-vs-CODE CHECK COVERS THE RELEASE LOOP — and D2 is exactly what such a check catches

`measured`: `tools/check-loop-docs.py:52` — `SOURCE = REPO / "tools" / "mom-cycle-status.py"`; its
`SURFACES` are `CLAUDE.md`, `MOM-CYCLE-MAP.md` and the mom-cycle skill. Its run tonight reports **3/3
green** and says **nothing** about `cycle/release/`.

So the one class of divergence this repo built a check for — *do the loop's docs still describe the
loop's code?* — occurred tonight in the one loop the check does not cover (D2: map 12 beats, code 5).
**The check exists; only its roster is narrow.** ⚠️ **Falsifier, and it decides the recommendation:** if
extending it produces a line that is red on day one and stays red, do **not** extend it. The beat
count is the one thing comparable today, and today it is comparable — so the extension can be green
the moment D2 is fixed and is not a permanent alarm.

---

## 3 · IS ITEM 7 A PATTERN? — yes, and a checklist would NOT have caught it

**The two instances, `measured`:**

| | instrument | question it answers | question it was asked | conclusion drawn |
|---|---|---|---|---|
| **i** | `watch-accounts.py --all` | *what credentials are in the store now* | *did this credential ever exist* | "the credential vanished" — **false** |
| **ii** | `cycle_registry()` | *does this loop CLAIM a project's rows* (coverage) | *does this loop render* | "it does not render" — **false** |

**It is a pattern, and the evidence is not two.** In this repo's own current text: `check-estate-neutral`
green means *names*, and a gauge leak of numbers and possessive pronouns passed it (CLAUDE.md, the
pickup block, measured 09-07); `build-viewer.py --check` green means *reproducible*, never *runs*, and
four seats walked a corpse on 09-06; gate ① printed **4 of 4** while its intersection was **empty**
(briefing §5.2); `wide-eyed`'s unreached purpose was **scored as passed** (retro §2.3). And the corpus
already carries the ratified general form — `[[reference_match_payload_not_container]]`, *"read before
any signal, gate, parser, probe or status value."*

**Would a checklist have caught it? No, and I will not propose one.** A rule that says *verify by a
second method* applies to every read in the session, costs attention on all of them, and is therefore
ignored on the one that matters — which is the definition of a control nobody reads. Both errors were
also made by someone who **knew the rule**, in a session that **cited it**.

**What actually worked, twice, in under three hours:** both were caught. (i) by grepping the chronicle;
(ii) by running the render. **The loop's self-correction is functioning.** The two things worth adding
are narrow and trigger-scoped, not standing:

1. ⭐ **The chronicle-first probe, and it is already written in the chronicle's own words:**
   `grep -n '<the id>' cycle/release/CYCLE-LOG.md` **before writing a finding about anything a store
   cannot explain.** It has a **trigger** ("a store returned nothing and I am about to say why"), not
   an always. It costs one command. It would have caught (i) outright.
2. **A tool's negative result carries its own predicate in the printed line.** `watch-accounts.py`
   already did this — it printed *"a personId the local **register** does not know"*, a claim about the
   register, and the reader upgraded it. `cycle_registry()` printed no predicate at all. This is the
   same discipline as *a count carries its predicate*, applied to zeroes.

⛔ **What I am not proposing:** a pre-flight, a gate, or a step. The failure was in the reader, and one
of the two tools said the right thing already.

---

## 4 · WHAT SHOULD BE DOCUMENTED, AND WHERE

⚠️ **Flagged first: what lives only in a commit message.**

| # | the thing | where it is now | where it should go | if left |
|---|---|---|---|---|
| **W1** | ⭐ *"an instrument answered the question it was built for and I took the answer for a broader one"* — the **general** form of tonight's two errors | **commit `0f2cd64` only.** The instance-specific half IS durably written into `operating-layer/config/projects.json:446` (*"`cycle_registry()` is the WRONG INSTRUMENT for the question 'does it render'… do not conflate them again"*), and the general half is not | `~/.claude/practice-principles/` — a second file beside `reading-the-world.md`, provenance-stamped, with **both** incidents | the corpus re-derives it a seventh way |
| **W2** | *"Absence in a store is not an event — the store answers what is here now, the chronicle answers what happened"* | `CYCLE-LOG.md` lap 3 § HOW IT WENT WRONG + commit `e84ac16` | same principle file as W1; it is the same rule seen from the data side | reachable only by reading one project's chronicle |
| **W3** | *"A walk is filed under the sha it walked — a sha is unambiguous across every sequence, an ordinal is not"* | **commit `9880e58`** + a warning header inside an **untracked** private file | `cycle/release/CYCLE-MAP.md` as a naming rule, and it is a spine candidate | it was violated one file over, the same night (D1) |
| **W4** | The **nine rulings** (A-1,2,3,5,6 · J-c · J-d · charters · second-viewport) | `CYCLE-LOG.md` lap 3 table only | `BACKLOG.md`; **J-d specifically → `PRODUCT-ENGINE.md` § THE SEQUENCE**, because the briefing says it blocks C5 and C5's plan of record does not know it was ruled | D8 |
| **W5** | Lap 3's **P1–P5** | `.plans/…lap2-RETRO.md:426-438` prose only | `cycle/release/cycle-state.json` `pre_registered[]`, with P2 carrying C-2 as a named blocker (G6) | D3 — nothing to discharge at close |
| **W6** | **Beat 0's two invented states** — a step may close UNCHECKABLE; a finding is retracted in place, never amended away | the chronicle's narrative | `cycle/release/CYCLE-MAP.md` beat-0 exit condition, as two clauses | D10 — re-derived under pressure next lap |
| **W7** | **Beat 1's two unmet exit clauses** (captures unmerged; C-7's repeat column not applied) | prose inside sections about other things | a `### Beat 1 · CLOSED` table in `CYCLE-LOG.md`, mirroring beat 0's | D7 |
| **W8** | **GAP 1 / GAP 2** | `.plans/…BRIEFING.md` §2 | a BACKLOG row each, or `pre_registered[]` — they have an **external trigger** and a written protocol already | D9 |
| **W9** | The **single-disk risk** on `GATE2-paul-findings.md`, and its three routes | `.plans/…CONSOLIDATION.md` §5 — **a file no checker grades and no row points at** (D6) | a BACKLOG row; the file itself needs a graded suffix or a pointer | the loop's best instrument stays on one disk with the decision unmade |
| **W10** | Lap 2's **three findings that should survive** — one assumption found five times · a green gate can be structurally meaningless · a defect that suppresses its own telemetry | `.plans/…BRIEFING.md` §5 | ⭐ these are **cross-project** and belong in `~/.claude/practice-principles/` or the design/engineering libraries — they are not Fernwood facts | they retire with the briefing |

⚠️ **One structural note on the destination question.** `.plans/2026-09-07-lap3-CONSOLIDATION.md` is
graded by nothing (D6), and `.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md` and this file are orphans by
declaration. That is three of lap 3's own process artifacts outside every instrument. **It is fine for
one; at three it is the register the loop is actually run from.** Whether `-CONSOLIDATION` and
`-BRIEFING` join `DOC_SUFFIXES` is a one-line call for whoever owns that tool. **Reported, not
resolved.**

---

## 5 · DOES THE PROCEDURE PROPOSAL NEED A STATUS PASS? — yes, and its `gate:` line is now FALSE

`measured`, `.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md`:

- `:21` `stage: draft` · `:20` `ready: agent-proposed 2026-09-07 — **Paul rules**`
- `:24` **`gate: ⛔ THIS IS A PROPOSAL AND NOTHING IN IT STARTS. No step below runs until §7 is ruled.`**
  — §7 **was** ruled (A-1, A-2, A-3, A-5, A-6; A-4 moot), and **beats 0 and 1 have run against this
  document.** The gate line states the opposite of what happened.
- `:323` **A-4 is stale** — the chronicle records it as answered-before-asked.
- `:201-232` its **beat numbers now conflict with the ratified map** (D1).
- `:182-197` its beat-0 step list **omits writing this lap's pre-registrations** (D3).
- `:110-113` its `13 in flight` measurement — `measured` again tonight: still **13**
  (`design 0/2 · build 1/1 (+3 excepted) · concept 9 uncapped`). Its own falsifier (*"if lap 3 closes
  with the in-flight count unchanged at 13 and nothing was blocked, the limit is wrong"*) is **live and
  currently on track to fire**; so is A-2's (*"if no lap-3 item ever sits at `design` or `journey`"* —
  measured **0** at either rung tonight). ⛔ Not a verdict. **Read them at close, not now.**
- `:23` its own stage-note reports the `draft`-stamp contradiction, which was **ruled and fixed**
  tonight (`e84ac16`, `check-backlog-ready.py`) — so half of that note is discharged history.

**Recommendation, and it is method only:** keep `stage: draft` — it is correct and opens no WIP — and
make **two edits**: (1) **replace the `gate:` line**, which is false, with one that says the six
questions were ruled on 2026-09-07 and the **document of record for what was ruled is
`cycle/release/CYCLE-MAP.md`**; (2) add **one stage-note** disposing each of its parts —
*ruled* (A-1,2,3,5,6) · *moot* (A-4) · *superseded by the map* (the beat numbering) · *never ruled*
(§2.1's warning that `design`/`journey` are not sequential; §2.2's WIP numbers as first-cut).

⛔ **I am not proposing a new stage word.** `superseded` is not in `STAGES` and adding an enum value to
retire one document would be the ceremony this ladder was built to avoid.

**Falsifier:** if a reader can open that file tomorrow and correctly tell which of its instructions are
live, no pass is needed and I am adding bookkeeping.

---

## 6 · WHAT I DID NOT MEASURE — stated so this does not read as coverage

- **I did not read the four lap-2 seat walk REPORTs**, so I cannot say whether beat 1's third-column
  cells F7/F8/F9 are answerable. The chronicle's claim that only those reports can answer them stands
  un-rechecked by me.
- **I did not open any record in `.private/feedback-sweep`.** My 477 breakdown is from the sweep's own
  per-env counts and its printed ids; I made **no** claim about what any record says.
- **I did not verify that the 431 QA records are synthetic** beyond their id shapes and
  `p-qa-synth-1` in the sweep output. It is `inferred` from naming, not from a provenance field —
  which is itself the reason G1 route (a) needs one.
- **I did not run `release-gate.py`, `walk-integrity.py` or any browser walk.** Every gate-① statement
  above is read from source, not from a run.
- **I did not check whether `operating-layer/cycles.py` re-derives the beat** rather than echoing the
  state file; D2's board consequence is `measured` from the config field's own recorded verification
  string, not from a fresh render.
