# Guru capability architecture — the worked design

**Seat:** ai-advisor · **Run:** Fernwood backlog rationalization, 2026-07-29 · **Mode:** consult
**Commission:** BACKLOG A6, *"How to evolve Guru's capability — the worked question"* (Paul, 2026-07-28).
**Instruction honoured:** do NOT answer this by building. Nothing was built. No Guru code, `BACKLOG.md`,
or Mom-facing file was touched. `/api/chat` was **not** probed (it forges a Mom-input signal — that
constraint is itself Finding A-1 below).

> **Method note.** The scoping artifact `research/2026-07-28-garden-guru-scope.md` was verified, not
> re-derived. Two of its findings have since been fixed and are marked so. Three of its numbers, and
> two of `BACKLOG.md`'s, are **wrong in a direction that matters** — every token figure below comes from
> measuring the artifact on disk at HEAD, not from reading the repo's prose about itself.

---

## 0 · THE DESIGN

### 0.1 The reframe — the constraint is distractor density, not token count

A6 names the honest constraint as **retrieval degradation**. That is right, and the 2025–26 literature
lets us say something sharper about *what drives it here*, which changes what to build.

Chroma's *Context Rot* study (July 2025, 18 frontier models, 10K–500K tokens) isolates the mechanism.
Three findings map onto Fernwood one-to-one:

1. **Distractors — topically related but incorrect information — compound with context length.** Even a
   single distractor degrades performance below baseline, and the effect grows with input length.
2. **Models do *worse* on logically coherent haystacks than on shuffled ones.** Local coherence creates
   competing plausible continuations.
3. **When a correct value and a plausible wrong value both sit in context, models select the wrong one
   at rates that rise with length** — though Claude models abstain more and confabulate least.

The 2,800 ft bug is that experiment run on Fernwood's own data. The commit message for `a7d7725`
already recorded the finding empirically — *"2,959 ft appears 59×, 2,800 ft only 12×… the model
reached for the lake's number BECAUSE THE QUESTION WAS ABOUT A BODY OF WATER. Topical proximity beat
frequency."* That is finding (1) and (3), measured locally, before the literature was consulted. It is
the strongest evidence in this report and it is Fernwood's own.

So the operative variable is not how many tokens the digest holds. It is **how many near-duplicate
entities sit in one flat context**. And that is measurable:

| Digest block | Tokens @ HEAD | Shape |
|---|---:|---|
| `plants.care` (36 plants × 12 months × 6 care types) | **27,884** | 36 near-identical structures |
| plants (rest — guide, seasonNotes, soil, aspect, frost, bloom) | 21,604 | 36 near-identical structures |
| wildlife (birds · mammals · amphibians · snakes · lizards) | 29,508 | ~N near-identical species records |
| vehicles (`maintenance` 5,095 · `needs` 3,648 · `specs` 1,910 …) | 13,368 | 16 near-identical spec tables |
| fishing (Lake Sequoyah) | 5,046 | the known confusability source |
| property | 4,513 | the one block that must always be loaded |
| weeds | 2,523 | 5 near-identical records |
| **Total digest** | **~106,016** | |
| Voice-rules block (`GARDEN_GURU_SYSTEM`, 28,279 chars) | 7,616 | |
| **Cached prefix, every turn** | **~113,632** | |

**~93% of the digest is N-instances-of-one-schema.** That is the precise shape where the two candidate
architectures diverge hardest:

- **Similarity retrieval selects by nearness — which *maximises* distractor density.** Every instance of
  a schema is a near-neighbour of every other by construction. Asking a vector index for "the pond's
  water" returns the lake's fishing profile *because it is doing its job*. This is why RAG was rejected
  as the 2,800 ft fix (`BACKLOG.md:267`) and the reason generalises well beyond that one bug.
- **Identity lookup selects by id — which *minimises* it.** `get_vehicle("dr200")` returns one spec
  table, and the DR-Z400's conflicting oil capacity is **not in the context to be confused with**.

That is the argument for tool-use, and it is not the argument the backlog currently makes. The backlog
makes the headroom-and-cost argument, which the scoping artifact already demolished ($9.29/yr).
**Tool-use is a distractor-elimination instrument, not a cost instrument.** Reframed that way it
survives its own cost analysis, and the substrate split stops being a stipulation and becomes a rule
you can apply to a new domain without asking:

> **The substrate rule.** Content with **stable ids and near-duplicate siblings** → identity lookup
> (tool-use). Content that is **prose, un-idded, and topically queried** → retrieval. The digest is the
> first kind; the ~85-resource research library is the second. Nothing goes in both.

### 0.2 The unmitigated risk nobody has named

The 7/28 vision restored 16 machines to the digest (`a73afbd`). That did not just add 13.4K tokens — it
added **the densest near-duplicate cluster in the whole corpus**, and it is entirely unpinned.

DR200 vs DR-Z400 oil capacity is *the same failure shape as pond vs lake elevation*, and the fleet
record has already been bitten by it once: the maintenance-values audit (B2) found the DR-Z400 card
reading `1.4 qt` and stamped `verified` when the manual says **1.9 qt**. Two Suzuki dirt bikes, two
Homelites, three cars with different oil specs, all now sitting flat in one 113K context with no
disambiguation block. The lake got a pin after it hurt someone. The machine register has not had its
2,800 ft moment yet.

This is the strongest single reason to pilot tool-use **on the machines first** (§0.3, Stage 3a).

### 0.3 The staged design

Each stage names what it buys, what it costs, and **what would falsify it**. Stages 3+ are all gated on
Stage 1's baseline; if the baseline comes back clean, most of this plan should not be built.

---

**Stage 0 — correct the instrument (nothing to decide).**
The digest is **~106K**, the prefix **~113.6K**. `BACKLOG.md` says ~98.7K because `build-digest.py:204`
estimates `chars // 4`, which under-reads by ~13%. **The ~100K retrieval-degradation threshold the A6
audit row treats as a future boundary was crossed on 2026-07-28** with the vehicle restore — a change
Paul approved. Every "but that would cross 100K" argument in the backlog is arguing about a line
already behind us.
*Buys:* an honest baseline. *Costs:* one estimator fix. *Falsifier:* none — it's arithmetic.

---

**Stage 1 — THE TEST HARNESS. This is the first build, and it is also measurement hygiene.**

Paul's orienting principle for this run is that the input-surface cleanup goes first *because the
confusing input stack contaminates the instrument we steer by*. My lane has the identical disease one
layer down: **`/api/chat` cannot be probed because `/api/conversations` is an instrumented Mom-input
channel that cannot tell who arrived.** `CLAUDE.md:32` already concedes the point — *"a deviceId is a
browser bucket, not a person"* — and already ships a manual workaround for it (`--acknowledged-through
<ts>`, to clear Paul's own test taps by hand). A human clearing a measurement error by hand is the tell
that the instrument is missing a field.

So the harness and the hygiene are **the same build**, which is why it belongs at the front rather than
competing with the UX work.

**H1 — provenance at the write boundary, not a flag in the prompt.** `/api/chat` accepts an `origin`
(`app` | `harness` | `paul-test`), stamped **server-side** into the conversation record; the
`momlib`/`check-mom-ack` channel readers count only `origin == "app"`. Per the tool-boundary principle,
this must be enforced where the write happens, not remembered by whoever runs the harness — a
harness-origin turn should be *structurally incapable* of raising an ack. Add a leg to
`tools/test-feedback-cycle.py` asserting exactly that. Side benefit: Paul's own test taps stop
polluting her engagement numbers, permanently.
*This is the Tier-3 item. Question + capture path in the findings table (A-1).*

**H2 — the canon fact table.** A deterministic script extracts checkable atomic facts from the same
source JSONs `build-digest.py` reads: `property.elevation_ft = 2959`, `drz400.oil = "1.8 US qt with
filter"`, `crabgrass.observedZones = [fairway, fairway-fringe]`. Generated, never authored, so it cannot
drift from canon. This is the artifact that would have caught 2,800 ft.

**H3 — the question set, and this is the half that must not be built naively.** Two parts, both small:
- **The distractor set (~20–30 questions).** One per known near-duplicate pair, each phrased to sit
  *near* the confusion: *"How deep is the pond and how warm does it stay through summer?"* (property vs
  lake elevation) · *"How much oil does the DR200 take?"* (vs DR-Z400) · *"What zone is the stiltgrass
  in?"* (fairway vs fairway-fringe). Chroma's evidence says degradation lives at distractors, so the
  test lives there too.
- **The negative set (~10).** Closed-world questions whose right answer is *"Not one we tend"* — the
  depth filter, which is the wedge, and the thing tool-use is most likely to break.
- **Free corpus:** the **66 already-stored turns** replay as a regression set at zero marginal design
  cost. (See §4 — this is the local substitute for shadow traffic, and it is better here.)

**Scoring is deterministic assertion against the fact table** — does the reply contain `2,959` and not
`2,800`? **No LLM-as-judge in v1.** At 30 questions run a handful of times a year, a judge is a second
thing to debug.

*Buys:* the ability to change Guru **at all**. Every stage below is unmeasurable without it.
*Costs:* H1 is a Worker + `momlib` change and needs Paul's ratification. H2/H3 are one session. A full
harness run costs **~$2.00** at today's per-turn price — roughly 80% of Guru's entire lifetime spend
($2.47). That number is not a problem; it is a proof that cost was never the axis.
*Falsifier — and this one is real:* **if the baseline scores ≥95% on the distractor set, the case for
re-architecting collapses.** The entire architecture argument rests on one bug (n=1) plus literature,
and Chroma found Claude models the most likely to abstain rather than confabulate under distractors. If
the pin plus Haiku's abstention behaviour is already holding at 113K, the right answer is: keep
stuffing, keep pinning, spend the hours on Track A UX. **Say this out loud before building anything
else.**

---

**Stage 2 — pin the near-duplicates, systematically; and test the model tier.**

**2a. Make disambiguation derived, not noticed.** `a7d7725` worked, cost 12 lines, and is the right
instrument for confusability. Its weakness is that it took a live incident to write. Replace "somebody
noticed" with a **~50-line deterministic near-duplicate detector** over canon: same field, similar
values, different entities → emit a candidate pin list for a human to author. No AI, no new doctrine.
This is `Derive a gate's pending-count; don't list it` applied to disambiguation. First outputs will be
the fish/pond-species residual (scoping doc §2), fairway vs fairway-fringe, and the machine cluster.

**2b. Test the model tier — the cheapest instrument nobody has costed.** Guru runs on
`claude-haiku-4-5` — **the smallest model in the family, on the surface where trust is load-bearing,
chosen under a cost concern the measurement has since falsified** ($2.47 lifetime). Chroma's distractor
experiment found the larger Claude models abstain when uncertain where smaller/other models confidently
pick the wrong value. Moving the ask path to Sonnet is a **one-string change**, reversible in one
commit, and at 199 turns/yr costs roughly **$40/year** more. Against $9.29/yr of tool-use savings and a
multi-session migration, that is an absurdly good trade *if it moves the number*. It might not — and
the harness is exactly the thing that says. Voice is the real risk (the field-journal register was
tuned on Haiku), and that is Paul's ear, not a metric.
*Buys:* the highest evidence-per-hour in the batch; both are additive, neither changes the architecture.
*Costs:* 2a ~half a session; 2b one line plus a harness run.
*Falsifier:* if pins don't move the distractor score, stop writing them. If Sonnet doesn't either, the
problem is not retrieval degradation and this whole design is aimed at the wrong thing.

---

**Stage 3 — split the substrate. Two independent moves that must NOT ship together.**

**3a. Identity lookup for the MACHINE REGISTER only.** This is the recommendation I most want on the
record, because I don't think it has been proposed and it is strictly better than the all-or-nothing
migration the backlog frames:

- It is the **densest near-duplicate cluster** (§0.2) — the most to gain.
- It is **Paul-facing**. A tool-call miss costs Paul a wrong answer he can check against a manual. The
  same miss on Mom's plants costs trust, which is the thing the project cannot spend. **Pilot the
  risky primitive where the blast radius is right.**
- It is the biggest single non-plant block (13.4K, 12.6% of the digest).
- **The four fence flows that depend on digest-exact naming are mostly plant flows.** Migrating vehicles
  does not force that rewrite. The machine log-fence (`worker.js:641`) does depend on machine names —
  and is served by the same names index the tool needs.
- The always-loaded names index the closed-world negative requires can be piloted at **~16 entries,
  ~200 tokens** instead of building the full 103-entity index up front.

Hybrid is explicitly fine and is the point: keep stuffing plants and wildlife, tool-call the machines,
and instruct plainly — *"for machines you must call `get_machine`; you do not have their specs."*

**The failure mode to measure, not assume.** The 2025–26 tool-calling literature is consistent that
**invocation reliability is the scale-sensitive variable** — the "knowing-doing gap," where a model
recognises a tool is needed and answers from priors anyway; ToolFailBench's "parametric traps" are
literally this. The published magnitudes are from 3B local models and **do not transfer to Haiku 4.5** —
discount them (§4). But the *direction* is why the harness must report **tool-invocation rate as a
first-class metric**, not just answer accuracy. A Guru that answers Fernwood questions from general
gardening priors has silently destroyed the wedge, and it will look fine.

**3b. Retrieval for the prose library only.** `references.json` (~14.4K, ~85 curated resources) is the
one genuine RAG case: no ids, topical queries, and near-duplicates *don't matter* there — two good
sources on moss management both surfacing is a feature. It is also **not in the digest today**, so this
is purely additive capability, not a replacement. Gate it behind the corpus-curation row (A6) and
behind Stage 1. Do not vectorise the digest, ever.

*Buys:* 3a removes the highest-risk distractor cluster and produces the only honest data on whether
tool-use is safe here. 3b adds depth Guru has never had.
*Costs:* 3a is the real engineering — a tool loop, error paths, partial-failure behaviour, the machine
names index, and a harness run before and after. 3b needs curation first.
*Falsifier:* if 3a's invocation rate is below ~98% on machine questions, or the negative set regresses,
**stop — do not migrate plants.** Revert to stuffing and pinning; the substrate split has failed its
own test on the easiest domain.

---

**Stage 4 — full migration, with streaming, or not at all.**
Only if Stage 3a's numbers earn it. Streaming ships **with** it, not after: tool-use adds a second round
trip on rural LTE, and the latency literature is unambiguous that **time-to-first-token is what a person
feels** — a reply that starts in 400ms and streams for four seconds feels fast; one that starts at two
seconds feels slow at identical total time. Tool-use degrades exactly the metric the A6 streaming row
gates on (*"if turns feel laggy on LTE"*), so that gate should be considered pre-fired by any tool-use
ship.

---

### 0.4 Where the two tracks meet

The brief asks for a ranking of Track A vs Track B. My lens says **don't rank them here — sequence them
so B de-risks A.** The vehicle register is the safest place to learn whether tool-use works on this
model, on this prompt, at this scale. Track B is Track A's test bed for the one capability Track A
eventually needs. That is the only place in this backlog where the two products help each other, and it
is worth spending.

---

## 1 · Tiered findings

Tier 1 = nothing blocks it. Tier 2 = an answer already given. Tier 3 = a question not yet asked
(carries the exact words + the capture path).

| # | Tier | Claim | Touches | Effort |
|---|---|---|---|---|
| **A-1** | **3** | **The harness's prerequisite is a provenance field on conversations, not a test flag.** An agent cannot probe `/api/chat` without forging a Mom-ack signal, so Guru cannot be regression-tested at all. Fix at the write boundary: `origin` stamped server-side, channel readers count only `origin=="app"`, plus a `test-feedback-cycle.py` leg proving a harness turn raises no ack. Same fix retires the manual `--acknowledged-through` workaround for Paul's own test taps. | A6 "worked question" ②; `worker.js` `/api/chat`; `momlib.py:609`; `CLAUDE.md:32` | M |
| | | **Q (ask Paul):** *"May `/api/chat` carry an `origin` field — `app` / `harness` / `paul-test` — stamped by the Worker, so the ack loop counts only real app turns? It means an agent can finally test Guru without faking a signal from Mom, and it also stops your own test taps from inflating her engagement numbers."* **Capture:** Paul answers in session → ratified line lands in `CLAUDE.md` under "Mama's Perspective" channel definitions → enforced by a new `test-feedback-cycle.py` leg (not by memory). | | |
| **A-2** | **3** | **The Guru-turn factual audit: the containment is sufficient in shape, but only if you drop the model.** Assistant-turns-only is the right cut — that is the project's own output, not her words. Two gaps: (i) an assistant turn can *quote* Mom, so the audit's **artifact** must be the fact triple only (`claim / record says / match`) with a conversation-id citation, never turn text; (ii) v1 needs **no AI at all** — the fact table gives exact strings, so `2,800` in an assistant turn is a regex hit. Descoping the model shrinks the boundary change from "AI may analyze conversation content" to "a script may grep our own output," which Paul can approve in one line. | A6; `CLAUDE.md:69–74` (AI boundary + amendment) | M |
| | | **Q (ask Paul):** *"May a deterministic script read Garden Guru's own assistant turns — not yours, not Mom's — and report only whether each canon fact it stated matches the record: a list of `claim / record says / match-or-not`, with no conversation text ever leaving the Worker? It is a grep, not a model, and it would have caught the 2,800 ft answer."* **Capture:** in-session → new **EGRESS-AUDIT** clause on the 2026-07-26 amendment in `CLAUDE.md` → containment enforced by a test leg. *(A model seat on this is a separate, later ratification with evidence behind it — not bundled.)* |  | |
| **A-3** | **3** | **The AI boundary should gain a provenance rule, not be replaced by one.** The observation is right (18 stock photos + generic guides came from zero AI calls) but the proposed swap trades an *enforceable* rule for an *unenforceable* one — the model rule is mechanical ("did this path call the SDK?"), provenance is judgment. Keep both: model rule = the fence; provenance rule = the **content-admission** rule. Fernwood already has the vocabulary (`confidence`, `attribution.source: "Property record"`, the provenance chip, `_chatgptProvenanceWarning`) — the stock photos were a failure to *apply* an existing stamp, not a missing rule. The generalisable statement: **volume without provenance is the harm; a model is just the cheapest way to make volume.** | A6 "Doctrine amendments forced (proposed, unapplied)"; `CLAUDE.md:69–74` | S (doctrine) + S (gate) |
| | | **Q (ask Paul):** *"Two rules instead of one — keep 'AI never touches her surface or her words' as the mechanical fence, and add 'nothing enters canon or her surface without a provenance stamp naming its origin and verification state.' The stock photos break the second, not the first. Agreed?"* **Capture:** in-session → `CLAUDE.md` AI-boundary section gains the provenance clause → enforced by a new `tools/check-provenance.py` (fails on any canon photo without `attribution.source`, any guide without a source), joining the session-start check family. | | |
| **A-4** | **2** | **Add `turf.json` and `zones.json` to the digest — but pruned, and the "~5.1K, crosses 100K" objection is wrong twice over.** See §3 status corrections: (i) we crossed 100K on 7/28; (ii) **lean zones costs ~208 tokens, not ~3,700** — 94% of `zones.json` is `vertices` (polygon geometry) and `history` (an edit audit trail carrying `by: "device"` / `by: "agent-claude"`), neither of which Guru can ever verbally reference and both of which are pure numeric distractor mass next to a property with a contested elevation. Turf's useful half (`summary`+`intro`+`regimes`+`grassesIntro`) is ~920 tok; `_meta` + `sources` (318 tok of citations) strip out. **Real combined cost ~1.1K, not 5.1K.** Both close a live "Guru reads an id it cannot resolve" hole, which is strictly worse than absent data — an unresolvable reference invites confabulation. | A6 audit row ① and ②; `tools/build-digest.py:173–186` | S |
| **A-5** | **1** | **Ship a `fairway` / `fairway-fringe` pin in the same commit as A-4.** Adding zones introduces two near-duplicate entities by construction, on the exact path Mom uses (her map, her zone walks). Pin them the way the lake was pinned; do not wait for the incident. | `worker.js:449–456` HARD FACTS | S |
| **A-6** | **1** | **The near-duplicate detector.** ~50 lines of deterministic Python over canon: same field, similar values, different entities → a candidate-pin list. Turns disambiguation from "somebody noticed after it hurt Mom" into a derived report. First outputs: pond-vs-lake *species*, fairway-vs-fringe, DR200-vs-DR-Z400. | A6; new `tools/` script | S |
| **A-7** | **1** | **The machine register is the densest unpinned near-duplicate cluster in the corpus, and it arrived on 7/28.** 16 machines, ~5.1K tok of `maintenance` alone; B2's audit already caught a DR-Z400 oil capacity wrong by ½ qt *and falsely stamped verified*. Same failure shape as 2,800 ft, no pin, on a block Paul just restored. | A6 vision row; A6 audit row; B2 | S (pin) / L (3a) |
| **A-8** | **1** | **Tool-use is a distractor-elimination instrument, not a cost instrument — and the substrate split has a reason, not just a stipulation.** Retrieval selects by nearness (maximises distractors); identity lookup selects by id (minimises them). 93% of the digest is N-instances-of-one-schema, the shape where that divergence is largest. Rewrite A6's framing accordingly; the $9.29/yr number stops being the headline. | A6 "worked question" ①; `BACKLOG.md:267` | S (doc) |
| **A-9** | **1** | **Pilot tool-use on machines first, hybrid, Paul-facing.** Blast radius is right, the fence-flow rewrite is avoided, and the names index pilots at ~16 entries / ~200 tok instead of 103 / ~1,075. The harness must report **tool-invocation rate** as a first-class metric, because "answered from priors" is the failure that looks fine. | A6 "worked question" ③ ⑤ ⑥ | L (gated on Stage 1) |
| **A-10** | **1** | **Test the model tier before testing the architecture.** Guru is on the family's smallest model on the surface where trust is load-bearing, under a cost concern measured at $2.47 lifetime. Sonnet on the ask path ≈ **+$40/yr**, one string, reversible in one commit, and aimed directly at the documented failure mode. Run it through the harness before committing to a multi-session migration. | A6 "worked question"; `worker.js:1164` | S |
| **A-11** | **1** | **Streaming ships WITH tool-use, not after.** TTFT is what a person feels on LTE; tool-use adds a round trip. Treat the A6 streaming gate (*"if turns feel laggy"*) as pre-fired by any tool-use ship. | A6 "Streaming responses" | M |
| **A-12** | **1** | **The free-text triage seat moves from third to FOURTH — revised, not re-affirmed.** The original reasoning holds: it would not have caught the rainfall note faster (the watcher runs 09:00/19:00, she wrote at 09:20 — **cadence was the bottleneck, not comprehension**, and the fix is a write-triggered ping, not a model). **New reason to demote it further:** under this run's orienting principle, the input stack is currently too ambiguous to tell what a note *is* — an answer to the card above it, the composer, or the general-feedback tab. A triage model over that would be **classifying noise and laundering it as signal**. It now sits behind the UX input-stack cleanup, not just behind the harness. | A6; `.ai-advisor/2026-07-26-feedback-loop-ai-seats.md` | — |

---

## 2 · Kill list

| Kill | Why |
|---|---|
| **The 80K digest gate** (`tools/build-digest.py:212`) | A tripwire nobody acts on, computed by an estimator that under-reads 13%, proxying for a cost constraint measured at **$2.47 lifetime**. Paul already retired it in the 7/28 vision row; delete the mechanism so it stops generating false urgency. Replace with the near-duplicate detector (A-6) or with nothing. |
| **"Add zones + turf costs ~5.1K and crosses the 100K note"** | Wrong twice: 100K was crossed 2026-07-28, and the real pruned cost is **~1.1K**. Kill the row's framing, keep the row (A-4). |
| **The corpus row's stated rationale** (`BACKLOG.md` A6, *"stuffing more context makes that worse; retrieval makes it better"*) | That sentence is the **overturned claim still living in the row** — the 7/26 correction killed retrieval as the grounding fix. The corpus work survives on its own merits (the prose library genuinely is the RAG case, §0.3 Stage 3b), but its justification must stop citing the 2,800 ft bug. |
| **LLM-as-judge scoring in harness v1** | 30 questions, a few runs a year, deterministic assertions available. A judge is a second thing to debug. |
| **Anthropic's Tool Search Tool / `defer_loading` / programmatic tool calling** | Built for hundreds-to-thousands of tools; Fernwood would have ~6. Adds a round trip and a failure mode to solve a problem it doesn't have. |
| **A vector database / RAG framework for the 85-resource library** | At that scale a curated topic index plus full-text search beats an embedding pipeline. Anthropic removed vector search from Claude Code in May 2025 in favour of grep — that's the precedent, on a much larger corpus. |
| **Shadow traffic / canary deployment as the eval mechanism** | Correct diagnosis, wrong instrument here — there is no traffic to shadow at 0.54 turns/day. Take the idea, replace the mechanism with the 66 stored turns (§4). |
| **Vectorising the digest** | Standing. Not a backlog row — nothing to do — but keep it stated so it doesn't get re-proposed. |

---

## 3 · Status corrections

| Correction | Evidence |
|---|---|
| **The digest is ~106,016 tok and the cached prefix ~113,632 tok — not "~98.7K."** `BACKLOG.md`'s figure comes from `build-digest.py:204`'s `chars // 4`, which under-reads by ~13% against the measured 0.2693 tok/char. The A6 vision row's "Digest ~98.7K" was already ~105.3K at `a73afbd`. | `json.dumps(digest, separators, ensure_ascii=False)` at HEAD = 393,672 chars × 0.2693; `git show a73afbd:worker/digest.json` = 390,909 chars ≈ 105,272 tok |
| **The ~100K retrieval-degradation threshold was crossed on 2026-07-28, not "would be crossed."** Every "this is not a free add because it crosses ~100K" argument is about a line already behind us. | growth trace: `a73afbd` 105,272 → `0b4713e` 105,827 → `29a5db2` 106,016 (all 7/28–7/29) |
| **The digest grew ~750 tok in one day of Track-B fold work** (Bolores eyeball verdicts). Growth is no longer driven by Mom-facing additions. | same trace |
| **`zones.json` does not cost ~3.7K tok — the useful fields cost ~208.** 94% is `vertices` (polygon geometry, ~318 chars/zone) and `history` (edit audit trail, ~943 chars/zone, carrying `by: "device"` and `by: "agent-claude"`). | field profile of `zones.json`; lean projection `[id,name,type,status]` × 10 = 772 chars ≈ 208 tok |
| **`turf.json` is prose, not "8 entries."** Sections: `_meta` 125 · `summary` 18 · `intro` 115 · `regimes` 743 · `grassesIntro` 44 · `sourcesIntro` 19 · `sources` 318 tok. Useful half ≈ 920 tok. | field profile of `turf.json` |
| **SHIPPED, contradicting the scoping artifact §1.5(a):** the stale "seventeen" is gone. | `grep -c seventeen worker/worker.js` → **0** |
| **SHIPPED, contradicting the scoping artifact §1.5(b):** the machine register is no longer dead weight — vehicles are back in the digest (13,368 tok), so `worker.js:461`'s machine instruction is accurate again. | `worker/digest.json` keys include `vehicles`, n=16 |
| **Still true and still unfixed:** `worker.js:1153–1154` calls the digest *"the ~57K-token digest."* It is ~106K — off by 86%. | `worker/worker.js:1153–1154` |
| **Still true:** post-fix efficacy of `a7d7725` remains unproven at n=3 turns. Nothing has changed; only the harness settles it. | scoping artifact §2, unchanged |

---

## 4 · External research — and what each source changes

Cited where it moves a row. **Where general practice does not survive contact with a two-user,
0.54-turns-per-day hobby assistant, it is discounted below rather than quietly applied.**

**Applies — take it:**

| Source | What it establishes | Row it changes |
|---|---|---|
| [Chroma Research, *Context Rot* (Jul 2025)](https://www.trychroma.com/research/context-rot) — 18 frontier models, 10K–500K tok | Distractors compound with length; models do *worse* on coherent haystacks than shuffled ones; with a correct and a plausible-wrong value both present, models pick wrong at rising rates — though **Claude models hallucinate least and abstain most**. | **The whole design.** Reframes A6's "retrieval degradation" from a token-count problem to a **distractor-density** problem (§0.1) → drives the substrate rule (A-8), the harness's distractor set (Stage 1 H3), the pin-systematically row (A-6), and the model-tier test (A-10, on the abstention finding). Also supplies the **falsifier**: Claude's abstention behaviour is a live reason the baseline might come back clean. |
| [NoLiMa (ICML 2025)](https://arxiv.org/html/2502.05167v3) — 13 models claiming ≥128K | Effective context ≪ advertised context: 11 of 13 models drop below 50% of short-context baseline **at 32K**; degradation is worst when the question and the fact share no literal wording. | Kills "Haiku is 200K, we sit at 106K, therefore fine" as an argument anywhere it appears. Mom's questions are conversational (*"why is the pond green?"*), the canon fields are technical — that is precisely the low-lexical-overlap regime NoLiMa isolates. |
| [Anthropic, *Effective context engineering for AI agents* (Sep 2025)](https://www.anthropic.com/engineering) — "just-in-time context loading"; and the May 2025 removal of vector search from Claude Code in favour of grep | Keep lightweight identifiers in context, load content at runtime; on a structured corpus, direct lookup beat an embedding pipeline well enough to delete the pipeline. | Directly supports the **names index + identity lookup** shape (A-9) over retrieval for the digest, and supports **killing the vector-DB option** for the 85-resource library. Precedent is on a far larger corpus than Fernwood's. |
| ToolFailBench, *Model-Adaptive Tool Necessity / the knowing-doing gap*, and the tool-invocation-reliability diagnostics (2025–26) | The dominant tool-use failure is not a malformed call — it is **recognising a tool is needed and answering from priors anyway** ("parametric traps"); reliability is scale-sensitive. | Makes **tool-invocation rate a first-class harness metric** (A-9) and confirms A6's input ③. This is the failure that looks fine and quietly destroys the depth filter. |
| Latency/TTFT practice (2025–26): TTFT is what users feel; <600ms responsive, >2s noticed; mobile round trips dominate on weak networks | Streaming does not shorten a response, it moves the first words forward — which is the whole perceived-speed win. | **A-11**: streaming ships *with* tool-use, and the A6 streaming gate is pre-fired by any tool-use ship. |
| Contrastive / hard-negative entity disambiguation (e.g. [contrastive coreference for historical texts](https://arxiv.org/pdf/2406.15576); [adaptive entity linking, EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.231.pdf)) | The state of the art for near-duplicate entities is **explicit hard negatives** — naming the wrong candidate and why it is wrong — not more context. | Confirms `a7d7725`'s pinned block was the right instrument, not a stopgap, and that the *negative binding* ("2,800 ft is the LAKE, never the property") is the load-bearing part. Drives **A-5** and **A-6**. |
| [Shadow traffic / canary for LLM rollout (2026 practice)](https://futureagi.com/blog/llm-eval-shadow-traffic-canary-2026/) | Diagnosis: curated synthetic sets miss the messiness of real inputs; test against the real distribution before a user sees it. | **Diagnosis taken, mechanism discarded** — see below. The local substitute is replaying the **66 already-stored turns**, which *is* the real distribution here, in a file, for free. |

**Discounted — general advice that does not survive contact:**

1. **"The 2026 default is hybrid: retrieve 50–200K, then long-context reason."** Fernwood's *entire
   corpus* is 106K. There is nothing to retrieve down *to*; retrieval would be selecting 100K from 106K.
   Discard.
2. **Shadow traffic / canary deployment as the eval mechanism.** Premise inverts: the argument for
   shadow traffic is that production is richer than synthetic. Fernwood has **66 turns, ever**, already
   stored. Replay beats mirroring, costs nothing, and needs no new infrastructure.
3. **Vector databases / RAG frameworks.** Every listicle result is enterprise-scale. 85 prose documents
   is a curated index and full-text search, not an embedding pipeline.
4. **Tool Search Tool, `defer_loading`, programmatic tool calling.** For hundreds-to-thousands of tools.
   Fernwood needs ~6.
5. **RL-trained retrieval / agentic multi-hop search stacks.** Not at this scale.
6. **LLM-eval platforms (LangWatch, Future AGI, et al.).** 30 questions a few times a year is a Python
   script with assertions. Keep Hamel Husain's *posture* — look at your data, error-analysis before
   metrics — which is free; skip the platform.
7. **The small-model tool-calling failure magnitudes** (89% init failures on qwen2.5:3b; 31.6% invalid
   calls; capacity thresholds at 14B/32B). Those are 3B local models. **Haiku 4.5 is not that** and the
   numbers must not be quoted at Fernwood. Take the *direction* (invocation reliability is the
   scale-sensitive variable); discard the *magnitudes*; measure locally.

---

## 5 · Sequencing view

| # | Do | Tier | Effort | Gate |
|---|---|---|---|---|
| 1 | Land the status corrections (§3): digest ~106K / prefix ~113.6K; fix the `//4` estimator; record that 100K was crossed 7/28. | 1 | S | — |
| 2 | Add pruned `turf` + lean `zones` to the digest, **with** the fairway/fringe pin in the same commit. ~1.1K tok. | 2 (one-line Paul confirm — it reaches Mom) | S | — |
| 3 | Near-duplicate detector → candidate pin list; author the pond-vs-lake *species* pin and the machine-cluster pin. | 1 | S | — |
| 4 | **H1 — `origin` provenance on `/api/chat`**, enforced at the write boundary + a `test-feedback-cycle.py` leg. | **3 → A-1** | M | Paul ratifies |
| 5 | **H2 + H3 — fact table, distractor set, negative set, replay of the 66 stored turns.** | 1 | M | after 4 |
| 6 | **BASELINE RUN. The decision point for everything below.** | 1 | S | after 5 |
| 7 | Model-tier experiment: Sonnet on the ask path, measured, ~+$40/yr, one commit to revert. | 1 | S | after 6 |
| 8 | Guru-turn factual audit, deterministic v1, fact-triples only. | **3 → A-2** | M | Paul ratifies |
| 9 | Provenance clause + `check-provenance.py`. | **3 → A-3** | S+S | Paul ratifies |
| 10 | **Tool-use pilot: machine register only**, hybrid, + a 16-entry names index. Harness before/after, invocation rate reported. | 1 | L | after 6 |
| 11 | Streaming. | 1 | M | ships with 10 |
| 12 | Retrieval over the prose library (`references.json`). | 1 | L | after corpus curation + 6 |
| 13 | Full migration — plants, wildlife, the four fence flows, the promote-species drafter. | — | XL | **only if 10's numbers earn it** |
| 14 | Free-text triage seat. | — | M | after the UX input-stack cleanup, and after 6 |

**The one-sentence version:** correct the numbers, make the two cheap digest adds, build the harness
(which is also the measurement hygiene), *measure* — and let the measurement decide whether the
architecture changes at all.

---

## 6 · What I could not determine

| Open | What would settle it |
|---|---|
| **Whether `a7d7725`'s pin actually works.** n=3 post-fix turns. This is the single most load-bearing unknown in the design — if pinning holds at 113K, most of Stages 3–4 should not be built. | The harness distractor set (Stage 1). Not resolvable any other way; probing forges a Mom signal. |
| **Haiku 4.5's tool-invocation rate on *this* prompt, at this context size, with image/audio blocks in the turn.** Published numbers are from far smaller models and do not transfer. | The Stage 3a machine pilot, with invocation rate reported. Nothing in the literature substitutes. |
| **Whether Mom's Guru questions cluster in any domain** — which would say where distractor risk actually bites, and whether the plants block or the machines block is the real hazard. Metadata alone (24 conversations, 66 turns) cannot say; the content can. | Same ratification as **A-2**. The audit question and this question are one question. |
| **Whether the field-journal voice survives a model-tier change.** Not a metric — Paul's ear. | Paul reads five answers from a Sonnet run side by side with five from Haiku. |
| **The tool-use prefix estimate (~9,539 tok / ~$0.0199 per turn).** Still the only projected figure in this whole line of work; unchanged from the scoping artifact and still low-confidence. | One real tool-use call, logged. Available as a by-product of Stage 3a. |
| **How much of `plants` and `vehicles` is strippable.** Unlike `zones`, they profile as mostly substance (`care` 27.9K, `maintenance` 5.1K) — so I found no large hygiene win there, but I did not audit field-by-field for non-verbal content. | A field-level pass over `build-digest.py`'s strip list, using the `zones` finding as the template. Worth one session, low risk, before any migration. |

---

*No `BACKLOG.md`, `worker/worker.js`, `viewer.html`, `questions.json`, or digest file was modified in
this run. `/api/chat` was not probed. Nothing was built.*
