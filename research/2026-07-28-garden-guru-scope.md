# Garden Guru redesign — scoping artifact

**Date:** 2026-07-28 · **Mode:** investigate, do not build. No Guru code was modified in this run.
**Framing constraints honoured:** RAG is not proposed anywhere below (retrieval solves volume, not
confusability — the disambiguation fix already shipped, see §2). AI stays on the ask path. The
variable under examination is *where property context lives*, not raw model access.

> **Method note.** Every number in §1 comes from running something, not from reading the repo's
> prose about itself. That mattered: the BACKLOG's stated digest size is wrong by ~27K tokens,
> and two of the Guru's own system-prompt facts are false against the digest it actually ships with.

---

## 1 · What the Guru is today (evidence)

### 1.1 The call

One Anthropic Messages call per turn, from the Cloudflare Worker.

| Property | Value | Evidence |
|---|---|---|
| Model | `claude-haiku-4-5-20251001` | `worker/worker.js:1164` |
| Output cap | `max_tokens: 600` | `worker/worker.js:1165` |
| System prompt | three blocks: voice rules (cached) · digest (cached) · live state (uncached) | `worker/worker.js:1166–1170` |
| Cache TTL | `cache_control: {type:"ephemeral"}` = 5 minutes | `worker/worker.js:1167–1168`; TTL/multipliers per [pricing docs](https://platform.claude.com/docs/en/about-claude/pricing) |
| Conversation persisted | KV, per `conversation_id` | `worker/worker.js:1183` |
| Usage logged | every turn → `cost-log:<date>` in KV | `worker/worker.js:1014–1036` |

### 1.2 How property context reaches it — the digest

Property context reaches Guru **one way only**: the whole curated digest is stringified into the
system prompt on every turn.

```js
{ type: "text", text: "PROPERTY DIGEST:\n" + JSON.stringify(propertyDigest),
  cache_control: { type: "ephemeral" } },
```
— `worker/worker.js:1169`, bundled at deploy from `worker/digest.json` (`worker/worker.js:61`).

The digest is built from **exactly eight source files** (`tools/build-digest.py:173–180`):
`plants · birds · mammals · amphibians · snakes · lizards · fishing · property`.

**Measured size** (`python3 tools/build-digest.py --verify`, then `git checkout worker/digest.json`
to restore — the script writes, unlike `check-digest-fresh.py`):

```
Source files total: 485,394 bytes
Digest:             349,079 bytes
Est. token count:   ~87,269 tokens (approaching ceiling)
```

That estimate is `chars // 4` (`tools/build-digest.py:204`) and it **under-reads by ~13%**. The real
tokenizer count is recoverable from the live cost log: the turn at `2026-07-26T12:57` reports
`cache_creation_input_tokens = 98,341`, which is exactly the two cached blocks
(`GARDEN_GURU_SYSTEM`, 28,104 chars + `"PROPERTY DIGEST:\n"` + the digest as deployed at commit
`a7d7725`, 337,018 compact chars). That calibrates to **0.2693 tok/char (3.71 chars/tok)**.

Applying the measured ratio to HEAD:

| Quantity | Tokens |
|---|---|
| Voice-rules block (`GARDEN_GURU_SYSTEM`) | ~7,568 |
| Digest | ~93,197 |
| **Total cached prefix, every turn** | **~100,771** |
| Last *measured* value (2026-07-26 turn) | 98,341 |

**The A6 gate has fired and the BACKLOG does not know it.** `BACKLOG.md:203` records the tool-use
migration as *"De-urgent-ed 2026-07-17 … dropped it ~82K → ~71K tokens, back under the ceiling with
headroom."* The measured prefix is **~100.8K** — 26% above the stated 71K and **~16% above the 80K
gate** (the gate lives at `tools/build-digest.py:212`). It first crossed 80K by 2026-07-13
(`cache_creation = 95,147` at `2026-07-13T21:31`), i.e. **four days *before* the 7/17 de-urgent-ing
was written**, and grew again with the 7/25 pond-plant additions.

Growth trace from the cost log (`cache_creation_input_tokens` per fresh write):

```
2026-05-20  61,931      2026-07-03  65,675
2026-05-28  63,917      2026-07-13  95,147   ← 80K gate crossed
2026-07-02  63,917      2026-07-14  95,292
                        2026-07-26  98,341
```

The second A6 gate has **not** fired: `GET /api/observations?start=2026-01-01&end=2026-07-28`
returns **40** observations, against a gate of >50.

### 1.3 What it costs per turn — measured, not estimated

`GET /api/cost-log?start=2026-05-01&end=2026-07-28` (auth `X-Tate-Token`, `worker/worker.js:83–86`),
**37 logged turns across 14 days, 2026-05-20 → 2026-07-26**:

| | Tokens | Cost @ Haiku 4.5 | Share |
|---|---|---|---|
| Cache **writes** | 1,823,027 | $2.2788 | **92.3%** |
| Cache reads | 771,718 | $0.0772 | 3.1% |
| Base input | 39,385 | $0.0394 | 1.6% |
| Output | 14,606 | $0.0730 | 3.0% |
| **Lifetime total** | | **$2.4684** | |
| **Per turn** | | **$0.0667** | |

Prices: Haiku 4.5 $1/MTok input · $1.25/MTok 5-minute cache write · $0.10/MTok cache read ·
$5/MTok output ([pricing docs](https://platform.claude.com/docs/en/about-claude/pricing)).

**The cache is structurally not working, and that is the whole cost story.** `worker/worker.js:1153–1154`
calls the digest's `cache_control` *"the big cost saver — within a 5-minute window across turns or
sessions, the ~57K-token digest is read at 10% of base rate."* Empirically, **26 of 37 turns (70%)
recorded zero cache reads** — they paid the full 1.25× write on ~100K tokens. Mom's sessions are days
apart; a 5-minute TTL almost never spans them. (The comment's "~57K" is also stale by ~44K.)

Volume, for scale: **24 conversations, 66 stored turns, over 68 days** (`GET /api/conversations`) —
about **0.54 Guru turns per day**.

### 1.4 Where it is capped

| Cap | Value | Evidence |
|---|---|---|
| Reply length | 600 tokens | `worker/worker.js:1165` |
| Conversation length | 1 question + 5 follow-ups, 6th submission closes it | `viewer.html:16064` (`GG_MAX_USER_TURNS = 6`) |
| Server-side turn ceiling | 20 (defence in depth) | `worker/worker.js:1106–1108` |
| Request payload | 5 MB | `worker/worker.js:1092–1094` |
| **Domain scope** | 8 of the repo's data files | `tools/build-digest.py:173–180` |

The domain cap is the one nobody is watching. Guru **cannot see**:

- **`weeds.json` (5 weeds)** — an entire domain that shipped to Mom's dashboard on 2026-07-20
  (`BACKLOG.md` A7). If she photographs the stiltgrass her own app shows her and asks Guru, the
  depth filter's instructed answer is that it isn't one we tend.
- **`vehicles.json` (16 machines)** — removed from the digest 2026-07-17, deliberately
  (`tools/build-digest.py:181–186`).
- `zones.json`, `turf.json`, `candidates.json`, `devices.json`.

### 1.5 Two live contradictions between the system prompt and the digest it ships with

Both found by running counts against the shipped artifacts, not by reading docs.

**(a) "the seventeen plants we tend" is wrong — there are 36.**
`python3 -c "import json;print(len(json.load(open('plants.json'))['plants']))"` → **36**.
The phrase appears **five times** in `GARDEN_GURU_SYSTEM` — `worker/worker.js:461, 486, 547, 548, 567` —
and three of those are the *literal refusal script* Mom reads
(`"Not one of the seventeen we tend."`). This is authored content on Mom's surface asserting a false
count about her own garden. It is not tracked anywhere: `grep -rn "seventeen" BACKLOG.md INQUIRIES.md`
returns nothing. (`CLAUDE.md:171` carries the same stale 17.)

**(b) The machine register instructs Guru about 16 vehicles the digest no longer contains.**
`worker/worker.js:461` still says *"You also know the property's machines — the vehicles and equipment
in the digest … each with its maintenance specs, service history."* The digest has held **zero**
vehicles since 2026-07-17 (`grep -c "DR-Z400\|Desert Storm\|Tiguan\|golf cart" worker/digest.json` → 0).
Roughly **5,015 chars ≈ 1,351 tokens (18% of the voice-rules block)** across `worker.js:487, 492,
495–507, 536, 625–641` governs a subject Guru is now blind to — including a machine log-fence flow
(`:641`) that instructs it to *"use the machine's SPECIFIC name as the digest lists it,"* which the
digest can no longer supply. It degrades safely rather than hallucinating (the instructed fallback at
`:496` is *"not logged — I'd check the manual"*), but the instruction block is dead weight.

### 1.6 Why no live behavioural probe was run

I did not send test turns to `/api/chat` to re-test the 2,800 ft bug. `/api/conversations` is a
registered **Mom-input channel** in the acknowledgment loop (`tools/momlib.py:609`; `CLAUDE.md:32`),
so agent-authored Guru turns would forge a signal that Mom is owed an acknowledgment. Behavioural
verification of Guru is therefore **not agent-safe without a test-conversation exclusion** — which
does not exist today. That is itself a finding about the surface.

---

## 2 · What the disambiguation fix already solved

**Commit `a7d7725` (2026-07-26 12:26 ET)** — *"Guru: pin the property's hard facts, with the
lake/property disambiguation."* Two files, +12/−1 lines. Deployed, version
`3d230628-12f0-4a55-a0c2-b546de203ae7`, `/health` OK (per the commit message).

It added a `HARD FACTS` block **above** `WHAT YOU KNOW`, so it lands before the digest
(`worker/worker.js:449–456`):

```
- Fernwood, the PROPERTY: … elevation 2,959 ft.
- Lake Sequoyah is a DIFFERENT PLACE at 2,800 ft. **2,800 ft is the LAKE, never the property.**
  … When the subject is water, this is exactly where the two get confused …
```

**What it solved, and why the diagnosis is the durable part.** The commit message records the
measurement that killed the RAG framing: 2,959 ft appears 59× in the digest, 2,800 ft only 12× and
all twelve fishing-scoped — *"the correct figure massively dominates and the model still reached for
the lake's number BECAUSE THE QUESTION WAS ABOUT A BODY OF WATER. Topical proximity beat frequency."*
That is a confusability failure between two near-duplicate entities. Adding retrieval over the same
substrate selects on semantic *nearness*, which is precisely the axis that produced the error — it
would surface the lake's fishing content for a pond question more reliably, not less. This is already
recorded as an overturning correction at `BACKLOG.md:177`.

It also records what does **not** work: the system prompt's opening sentence already said "at 2,959
feet," so *restating the fact was never the fix*. The load-bearing element is the **explicit negative
binding** — naming the wrong value, naming what it belongs to, and naming the context where the two
collide.

**What is genuinely unresolved.** The commit closes with *"This is the cheap patch, not the cure. The
real fix is retrieval."* Per the correction at `BACKLOG.md:177`, that closing sentence is the part
that was overturned; the pinned block is the right instrument for this failure class, not a stopgap.

**What remains unverified: whether the fix works.** The evidence base is the pre-fix scan (25
assistant turns / 18 conversations / 5 elevation claims, 2 wrong). Only **three turns have been logged
since** the fix deployed (`2026-07-26` at 12:57, 13:00, 13:17 — all inside conversation
`ms1syuug-qcyxx`). **INSUFFICIENT SOURCE** for a post-fix efficacy claim: n=3, and per §1.6 an agent
cannot generate more without contaminating the ack channel.

**A residual the pinned block does not cover.** It disambiguates elevation. It does not disambiguate
*species*: `fishing.json` contributes ~5,014 tokens of Lake Sequoyah fish profiles into the same
prompt as a pond that holds koi and *Gambusia*, and `BACKLOG.md` A8 records the same lake→pond
conflation arriving twice more from a different source (the amphibian-decline note, killed 2026-07-25;
the beaver entry, corrected 2026-07-25). Same entity pair, same direction, three independent
incidents. Whether that warrants extending the pinned block is a cheap, in-pattern question — and
notably it is a *pinning* question, not a retrieval one.

---

## 3 · The tool-use migration assessed

**The candidate:** Guru stops carrying the whole digest in its prompt and instead calls deterministic
lookups (`get_plant(id)`, `get_species(type, id)`, `get_property()`) against the same canon files.

### 3.1 The case for

**a) It is the only fix for the ceiling that keeps scaling.** The digest has hit a ceiling twice:
`viewer.html` crossing the GitHub Contents API's 1 MB cliff (`BACKLOG.md` A6, root-caused 2026-07-16),
and the 80K digest gate, crossed 2026-07-13 and **still crossed today**. Every remediation so far has
been *subtraction from Mom's assistant* — dropping 16 machines (7/17), never adding the 5 weeds that
shipped 7/20. Tool-use is the shape where adding a domain costs a tool definition, not a permanent
per-turn tax.

**b) The coverage gap in §1.4 is a symptom of the ceiling, and tool-use dissolves it.** The measured
cost of a names-only index over all 103 digest entities is **~1,075 tokens** (`json.dumps` of
id+name pairs × the measured 0.2693 tok/char). Adding weeds, zones and vehicles to *that* is
arithmetic noise. Adding them to the current digest is another ~15–20K tokens on every turn.

**c) The per-turn arithmetic is genuinely favourable.**

| | Today (measured) | Tool-use (estimated) |
|---|---|---|
| Cached prefix | 100,771 tok | ~9,539 tok (7,568 voice + 1,075 index + ~896 tool defs) |
| Round trips | 1 | 2 |
| Cost / turn | **$0.0667** | **~$0.0199** |

**10.6× smaller prefix, ~3.3× cheaper per turn.** Tool-definition overhead is grounded: Haiku 4.5 adds
496 system tokens at `tool_choice: auto` ([pricing docs](https://platform.claude.com/docs/en/about-claude/pricing));
~400 tok for schemas is my estimate, marked low-confidence.

**d) It makes the cache irrelevant instead of broken.** At a ~9.5K prefix, the 70% cache-miss rate
costs ~$0.012/turn instead of ~$0.126. The fix isn't a better TTL — it's a prefix small enough that
missing doesn't matter.

**e) It is doctrinally in bounds.** `/api/chat` is an ask-path surface. Replacing prompt-stuffing with
read-only lookups moves no AI toward capture. The doctrine does not decide this one either way.

### 3.2 What it would NOT fix

**a) Not the 2,800 ft bug.** That was fixed by pinning, and the pinning survives any substrate change
(it lives in the voice-rules block, not the digest). If anything the migration makes the pin *more*
load-bearing, since the model would no longer have 59 correct occurrences of 2,959 ft in context to
fall back on.

**b) Not the closed-world depth filter, without extra design.** Guru's most-repeated contract is a
*negative* claim over all of canon — *"Not one of the seventeen we tend"* (`worker.js:486, 547, 548`).
A per-entity lookup cannot ground a negative: a miss is ambiguous between "not in canon" and "the model
guessed the wrong id." This is **solvable** — that is exactly what the ~1,075-token names index is for —
but it is a required piece of the design, not a free consequence, and the same index is what the log-fence
flows need (`worker.js:621, 641, 681` all require the model to emit *"the plant's name as it appears in
the digest so the client can resolve it"*).

**c) Not the *content* problems.** The stale "seventeen," the dead machine register, the missing weeds
domain — all live in `GARDEN_GURU_SYSTEM` and the build script. None is caused by prompt-stuffing and
none is fixed by tool-use. They are cheap, independent, and currently broken.

**d) Not Mom's actual complaint.** Her one unprompted ask, 2026-07-26, was
*"Is there a way to look back at these, eg in the 'journal'?"* (`BACKLOG.md:113`). That is a
findability failure on stored conversations — `BACKLOG.md` A6 notes the capability already exists.
Tool-use moves nothing on it.

**e) It introduces a new failure mode, on a surface where trust is the load-bearing emotion.**
Today's failure shape is *a wrong number inside a correctly-grounded answer*. Tool-use adds *the model
didn't call the tool and answered from nothing* — the harder failure to detect, on Haiku 4.5, across
6-turn conversations that may also carry image and audio blocks (`worker.js:1111–1150`). Per §1.6 there
is currently **no agent-safe way to regression-test this**, because probing `/api/chat` forges a Mom-input
signal. A migration with no safe test harness is a real risk, and building the harness is part of the cost.

**f) It makes latency worse where latency is already the open question.** Two round trips minimum, three
if a follow-up lookup is needed. `BACKLOG.md` A6 gates streaming on *"if turns feel laggy on LTE"* — a
rural mountain property. Tool-use degrades the exact metric that gate watches, and would likely force
streaming to ship with it rather than after it.

### 3.3 The cost

**Engineering surface.** Not a swap of one call — the digest is load-bearing in four places:

| Site | Evidence | Impact |
|---|---|---|
| Chat handler | `worker.js:1156–1175` | rewritten: tool loop, error paths, partial-failure behaviour |
| Depth filter + voice rules | `worker.js:461, 486, 547–548, 567` | rewritten around a names index |
| Four fence flows (plant log · machine log · add-species · remove-species) | `worker.js:610, 625, 666, 679` | each depends on digest-exact naming |
| Promote-species drafter (separate prompt, same digest) | `worker.js:891–916, 1533–1547` | decide: migrate too, or keep stuffing and hold two substrates |

Plus a test harness that does not exist (§1.6), plus a deploy (`bash tools/deploy-worker.sh`, agent-owned
per `CLAUDE.md:157`).

**Financial payback, at observed volume.** 37 turns / 68 days = **~199 turns/year**.
Saving = 199 × ($0.0667 − $0.0199) = **$9.29/year.**
To save $100/year, Guru would need **~2,139 turns/year ≈ 6 turns/day** — roughly **11× current usage**.

**The migration does not pay for itself on cost. It can only be justified on headroom, coverage, or a
decision to grow Guru's scope.**

---

## 4 · The case for doing nothing

Stated as strongly as the evidence supports, because on the current numbers it is the leading option.

1. **The gate that fired is a proxy for a constraint that is not binding.** The 80K gate exists to
   protect cost and context. Cost is **$2.47 lifetime, $0.067/turn**. Context: the largest prompt ever
   sent was 98,341 tokens and **no `/api/chat` call in 37 turns returned an API error** — no truncation,
   no overflow. The gate is firing; the harm it proxies for is not arriving.

2. **The bug that motivated the redesign is fixed, and by a 12-line change.** `a7d7725` cost almost
   nothing and addressed the actual failure mechanism (confusability), which the migration does not
   address at all.

3. **Every cheaper intervention currently outranks it on evidence.** Ranked by (evidence of harm) ÷ (cost):
   - **The stale "seventeen"** — a false claim about her garden, in Guru's refusal script, on Mom's
     surface, today. One-line fix. Highest ratio in the batch.
   - **The dead machine register** — 1,351 tokens of instruction for a subject Guru cannot see. Deletion.
   - **Weeds absent from the digest** — a shipped domain Guru will disown. ~1–2K tokens to add.
   - **Conversation browse** — the only item in A6 with a real, unprompted user signal
     (`BACKLOG.md:113`); the capability already exists.
   - **Tool-use migration** — no user signal, no cost pressure, largest surface.

4. **Doing nothing is not the same as leaving it broken.** Items 1–3 of that list are content and
   coverage fixes inside the existing architecture. They can all land without touching how context
   reaches Guru.

5. **It does not move Paul's variable.** On the reframing — the question is *where property context
   lives*, a capped Guru she leaves versus a fuller in-Fernwood assistant. Tool-use changes the
   *mechanism* by which property context reaches the model. It changes **nothing** about the caps that
   actually define the experience: 600-token replies (`worker.js:1165`), 6 turns
   (`viewer.html:16064`), garden-only scope. A cheaper Guru that says the same amount about the same
   things is still exactly as leavable. **On the axis Paul named, the tool-use migration is a no-op.**

**The honest counter-argument.** Doing nothing means the digest keeps growing (61.9K → 98.3K in nine
weeks, +59%), and each ceiling event so far has been paid for by *removing capability from Mom's
assistant*. That is the wrong direction for a project whose stated goal is to give her a reason to stay
in Fernwood. Doing nothing is right **only if** Guru's scope stays capped. If Guru is meant to grow,
the migration stops being cost engineering and becomes a prerequisite — because you cannot both widen
Guru's scope and keep stuffing a digest that is already 26% over its own gate.

---

## 5 · Agent-drivable vs. Paul's call

| Work | Who | Why |
|---|---|---|
| Correct "seventeen" → the real count in all 5 sites + `CLAUDE.md:171` | **Agent drafts, Paul confirms one line** | It reaches Mom, so it is *authored content* — human-confirmed per the AI-boundary amendment (`CLAUDE.md:72`). The fix itself is mechanical. |
| Delete the dead machine register (`worker.js:487, 492, 495–507, 536, 625–641`) | **Agent** | Removing instruction for a subject the digest cannot supply. No new claim reaches Mom. Deploy is agent-owned (`CLAUDE.md:157`). |
| Correct the stale comments (`worker.js:1153–1154` "~57K"; `BACKLOG.md:203` "~71K") | **Agent** | Internal accuracy. Nothing user-facing. |
| Re-derive the digest gate from the measured 0.2693 tok/char instead of `//4` (`build-digest.py:204`) | **Agent** | Pure measurement fix; the current estimator under-reads by 13%. |
| Add `weeds.json` to the digest sources | **Paul** | Changes what Guru says to Mom about a live domain — a scope decision, not a drift fix. Same class as the 7/17 vehicles removal, which was Paul's. |
| Build a test-conversation exclusion so `/api/chat` can be probed without forging a Mom-ack signal | **Agent designs, Paul ratifies** | Touches the ack loop's channel definitions (`momlib.py:609`) — the loop where a silent bug already cost real data twice. |
| Extend the pinned block to lake-vs-pond *species* (§2 residual) | **Agent drafts, Paul confirms** | Same instrument, same pattern as `a7d7725`; the wording reaches Mom. |
| Conversation-browse UI | **Paul scopes** | Her ask; a new surface on her dashboard. |
| **Whether to do the tool-use migration at all** | **Paul** | See card. It is not an engineering question — the evidence says it does not pay for itself at current scope, so the answer depends entirely on whether the scope is meant to change. |

---

## CARD FOR DECISION

**Is Garden Guru meant to stay a capped garden assistant, or become the fuller in-Fernwood assistant
that gives Mom a reason not to leave for claude.ai?**

This is the one question, because it is the only thing that decides the tool-use migration — and
everything else in A6 resolves without it.

The evidence forces the fork rather than the answer:

- **If capped stays capped** — 600-token replies, 6 turns, 8 domains — then the migration saves
  **$9.29/year**, fixes none of the four things currently broken (§1.5, §3.2c), makes latency worse,
  adds a failure mode with no safe test harness, and moves nothing on the axis you named. Do the four
  cheap fixes and the conversation-browse UI instead. The 80K gate should then be **re-set on measured
  tokens with a real justification**, or retired as a proxy for a constraint that isn't binding.

- **If Guru is meant to grow** — more domains (weeds, zones, the rich pond zone), longer answers, real
  back-and-forth — then the migration is a **prerequisite, not an optimisation**. The digest is already
  26% over its own gate and has grown 59% in nine weeks, and every ceiling event so far has been paid
  for by *removing capability from her assistant* (16 machines dropped; 5 weeds never added). That is
  the wrong direction for the goal, and it is a direction that gets worse on its own.

What makes this yours and not an agent's: nothing in the code or the numbers says which Guru is the
right one. The numbers say only that the migration is unjustified for the Guru that exists and
mandatory for the Guru that might. Both answers are defensible; they are opposite.

*(Narrower fallback if the big question isn't ready: **may weeds be added to the digest?** — a shipped
domain on Mom's dashboard that Guru will currently disown. Same class of call as your 7/17 vehicles
removal, ~1–2K tokens, independent of everything above.)*

---

## SOURCES / CONFIDENCE LEDGER

| Claim | Source | Confidence |
|---|---|---|
| Guru = 1 Haiku 4.5 call/turn, `max_tokens: 600` | `worker/worker.js:1164–1165` | high |
| Digest injected whole into system prompt, ephemeral-cached | `worker/worker.js:1166–1170`; bundled at `:61` | high |
| Digest built from exactly 8 source files | `tools/build-digest.py:173–180` | high |
| Digest 349,079 bytes; script estimates ~87,269 tok | `python3 tools/build-digest.py --verify` (run; `worker/digest.json` restored via `git checkout`) | high |
| Real cached prefix = 98,341 tok measured 2026-07-26 | `GET /api/cost-log`, turn `2026-07-26T12:57` | high |
| Tokenizer ratio 0.2693 tok/char | 98,341 ÷ (28,104 sys + 17 + 337,018 digest-compact @ `a7d7725`) | high |
| Current prefix ~100,771 tok (digest ~93,197) | ratio × HEAD `worker/digest.json` (346,041 compact chars) | med — extrapolated from one measured point |
| 80K gate crossed 2026-07-13, still crossed | cost log `cache_creation` series; gate at `tools/build-digest.py:212` | high |
| BACKLOG's "~71K, back under the ceiling" is wrong by ~27K | `BACKLOG.md:203` vs. measured 98,341 | high |
| Observations = 40, gate >50 not fired | `GET /api/observations?start=2026-01-01&end=2026-07-28` | high |
| Lifetime $2.4684 / 37 turns / $0.0667 per turn | cost log × pricing docs | high |
| 70% of turns (26/37) recorded zero cache reads | cost log, `cache_read_input_tokens == 0` | high |
| Cache writes = 92.3% of lifetime spend | cost log × multipliers | high |
| Haiku 4.5 $1 in / $1.25 5m-write / $0.10 read / $5 out per MTok; 496 tool-system tok @ `auto` | [platform.claude.com pricing](https://platform.claude.com/docs/en/about-claude/pricing) | high |
| 24 conversations / 66 turns / 68 days = 0.54 turns/day | `GET /api/conversations?start=2026-05-01&end=2026-07-28` | high |
| Caps: 6 user turns · 20 server · 5 MB | `viewer.html:16064`; `worker.js:1106–1108, 1092–1094` | high |
| plants.json holds 36 plants; prompt says "seventeen" 5× | `json.load(open('plants.json'))`; `worker.js:461, 486, 547, 548, 567` | high |
| "seventeen" not tracked in BACKLOG/INQUIRIES | `grep -rn "seventeen" BACKLOG.md INQUIRIES.md` → no output | high |
| Digest holds 0 vehicles; prompt keeps ~1,351 tok of machine instruction | `grep -c` on digest → 0; `tools/build-digest.py:181–186`; spans measured | high |
| weeds.json (5) not a digest source | `tools/build-digest.py:173–180`; `weeds.json` | high |
| 103 digest entities; names-only index ~1,075 tok | computed over `worker/digest.json` × 0.2693 | high |
| `a7d7725` = 12-line pinned HARD FACTS block, deployed | `git show --stat a7d7725`; `worker.js:449–456` | high |
| RAG framing overturned; retrieval solves volume not confusability | `BACKLOG.md:177` (ai-advisor, 2026-07-26); diagnostic in `a7d7725` message | high |
| Only 3 turns logged post-fix → efficacy unproven | cost log, entries after 2026-07-26T12:26 | high (that it's unproven) |
| Lake→pond conflation recurred 3× from independent sources | `a7d7725` msg; `BACKLOG.md` A8 (amphibian note killed; beaver corrected, both 2026-07-25) | med — pattern read across records |
| `/api/conversations` is a Mom-ack channel → agent probes contaminate | `tools/momlib.py:609`; `CLAUDE.md:32` | high |
| Tool-use prefix ~9,539 tok → ~$0.0199/turn | arithmetic on measured ratio; 496 tok cited, ~400 tok schemas estimated | **low–med — the only projected figure here** |
| Saving $9.29/yr; ~6 turns/day needed for $100/yr | 199 turns/yr (measured) × ($0.0667 − $0.0199) | med — inherits the estimate above |
| 4 digest-dependent sites must migrate together | `worker.js:610, 625, 666, 679`; `:891–916, 1533–1547` | high |
| Mom's unprompted ask = conversation browse | `BACKLOG.md:113` | high |
| Doctrine: AI on ask path, capture AI-free; tool-use is in bounds | `CLAUDE.md:67–72, 108`; `/api/chat` is an ask surface | high |
| `check-digest-fresh.py` exit 0 at time of writing | run 2026-07-28 | high |
