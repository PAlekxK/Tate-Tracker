# Guru retrieval architecture — the worked question

**Seat:** `ai-advisor` · **Mode:** CONSULT · 2026-09-03 · **Ends at Paul's gate; nothing is ruled.**
**Item:** `BACKLOG.md` § A6, *"How to evolve Guru's capability — the worked question"* (Paul, 2026-07-28).
**Nothing was built, deployed, or spent** — no `/api/chat` call was made. Every number came from running
something against this working tree. **Citations are by file + section/role, never by line** (§ C4).

---

## §0 · Six corrections, measured today — they reorder the whole item

**① The test-conversation exclusion ALREADY EXISTS. It shipped 2026-07-29 — one day after the scope
doc named its absence as the reason to park this.** `worker/worker.js` § *Origins a conversation can
have* defines `CONVERSATION_ORIGINS = ["app","probe","test"]` and `REAL_CONVERSATION`; the origin is
sticky and one-way; `/api/conversations` excludes non-`app` by default and reports `excludedNonApp`;
`/api/chat` accepts `origin` and `device_id` at its boundary; and `tools/momlib.py` (`_drop_harness` +
`harness_device_ids`) filters the `guru` channel by the harness device in `tools/people.json`
(`d-telemetrytest-harness-v1`). Its header names the exact failure it was built for: probing Guru made
`check-mom-ack.py` report Paul as owing Mom a reply.
⇒ **The prerequisite is not the safety mechanism. It is the assertions.** Days of work, not a design
problem; § A6's *"nothing else can be changed safely without it"* is 36 days stale.
⚠️ Caveat that becomes a harness requirement: a mistyped origin **fails open** to `app`, by design.

**② The elevation pin is now the stale value, and it is instructed to outrank canon.**
`property.json` § `location.elevation` = **2,873 ft**, `confidence: measured`, USGS 1 m lidar
2026-08-31, carrying an explicit `supersededValue` of 2,959 and its lesson. Measured today:
`worker/digest.json` **58** × `2,873 ft`; `viewer.html` **94** × `2,873 ft` vs 4; **`worker/worker.js`
14 × `2,959` and ZERO × `2,873`**, across five prompt blocks (Guru, today-line, classify, sound-ID,
schema-drafter). And `GARDEN_GURU_SYSTEM` § HARD FACTS opens *"these override anything you infer from
the digest below."*
⇒ **The instrument built to fix the 2,800 ft error is now injecting an 86 ft error and is told to
win.** Live on Mom's surface. Strongest argument for the harness, and the cheapest fix in the item.

**③ The breaker directory exists.** `vehicles.json` holds **30** `circuits` rows on the
household-systems entry, **61** `serviceHistory` rows across 8 machines, **13** `rhythms` — all
dropped by `digest_vehicles()` (`PRODUCT-ENGINE.md` § dropped-fields table). The brief's *"does not
yet exist"* is wrong: written and unreachable, which is worse, and is exactly Paul's falsifier.

**④ Haiku 4.5 has no announced retirement.** The `claude-api` skill's `shared/models.md` lists
`claude-haiku-4-5` under **Current Models · Active**, no retire date; the only Haiku in the deprecation
table is Haiku 3. My own 09-02 seat asserted a *"retirement floor 2026-10-15"* — **not supported; drop
that leg of the rung-1 case.**

**⑤ The prefix, measured 2026-09-03:** `GARDEN_GURU_SYSTEM` 29,881 chars ≈ **8,047 tok** + digest
503,319 compact chars ≈ **135,544 tok** (calibrated 0.2693 tok/char) ⇒ **~143.6K per turn**, vs 139,771
on 09-02. Still growing. Plants **44%** (59,820); vehicles **14%** (19,471).

**⑥ Latency has never been measured.** `logChatCost` records four token fields and **zero timing** — the
standing streaming gate (*"if turns feel laggy on LTE"*) watches a metric nothing records. And the site
premise is **no cell service, Wi-Fi from the house** (`PRODUCT-ENGINE.md` § condo), so the LTE framing
is wrong too: the risk is a second sequential model call, not bandwidth.

---

## §1 · The substrate split

**Recommendation: a ~15K always-loaded core, everything structured behind lookups, prose behind
retrieval last.** Measured, against today's digest:

| Layer | Contents | Measured tok |
|---|---|---|
| **CORE** — always loaded, cached | voice/rules block (prune the dead weight first) **8,047 → target ~6K** · **names index 1,848** (171 entities, id+name, 10 domains) · `property` **4,621** (estate identity, hard facts, hardiness, frost, microclimate) · `zones` **489** (23 ids — Mom's map vocabulary, referenced by weeds' `observedZones` and plants' `zones`) · `turf` **1,195** (coin flip, §7) · tool schemas **~500–900** | **~15K — 9.6× smaller than today's 143.6K** |
| **LOOKUPS** — structured canon | `get_plant` · `list_plants(zone\|season)` · `list_weeds` · `get_species(domain,id)` · `get_zone` · `service_history(vehicle)` · `circuit_for(room\|label)` · `rhythms(scope)` · `turf_regime()` · `fishing_species` | schemas only |
| **RETRIEVAL** — prose, LAST | `references.json` (~13K), `research-resources.md` (131 KB), `manuals/`, eventually the 254 receipt scans | rung 4 |

**The core has a FLOOR, not just a ceiling.** The `claude-api` skill's `shared/prompt-caching.md`:
the prompt-cache minimum is **4,096 tokens on Haiku 4.5** (512 on the newest models), and below it
caching **silently** does not happen. 15K is safe — but a core pruned toward ~4K, **or a module-aware
core on a plantless estate**, can cross that floor and push cost *up* while every check stays green.
Assert the floor in the build.

**What the core is for — three jobs, only these.** (a) The **closed-world negative**: *"not one we
tend"* is a claim over all of canon and no per-record lookup can ground it; the names index can.
(b) The **estate identity** — the hard facts errors actually happen on (§0②). (c) **Routing**: telling
*"this names something we have, look it up"* from *"this names nothing we have"* without guessing an id.

**Honesty markers ride in the record and must not be summarized away.** Measured: **91** inline markers
in the digest — 73 × `[UNCONFIRMED — verify before relying on this]`, 18 × `[SOIL SERIES UNCONFIRMED …]`.
They sit inside per-record prose, so a lookup carries them **for free**; a names index or summary layer
must never carry a marked field's content without its marker. Harness assertion, not a prompt line.

**What C5's module-set declaration does to it.** The core is **assembled from the declaration**: a
plantless estate ships no `plants` in the index, no `get_plant` in the schema list, and no plant clause
in the depth filter — which means the depth-filter clause becomes a **per-module fragment**, where
today it is a sentence in the voice block (`GARDEN_GURU_SYSTEM` § THE DEPTH FILTER names plants, weeds
and species inline). Real work. **Falsifier:** if a plantless estate's assembled core still contains the
word *"plant"*, the modularization is not done — knowable before she is shipped anything (§ C7).

---

## §2 · The test harness — first, and now cheap

**Shape:** `tools/guru_probe.py`, modeled on `tools/test-feedback-cycle.py` — a walk with an assert on
every leg, written after a real failure — with `--selftest` (13 tools already carry the convention).

**What it asserts: a fact table whose expected values are DERIVED FROM CANON at run time, never typed
into the test.** Seed rows, each with a must-contain, a must-not-contain, and a canon source:

| row | must contain | must NOT contain | source | today |
|---|---|---|---|---|
| elevation | `2,873` | `2,8\s?00` · `2,959` | `property.json` § location.elevation | **FAILS** |
| the negative | *"not one we tend"* / *"not a species the journal tracks yet"* | any substitute species name | names index | ? |
| the negative's false positive (a weed that IS canon) | named as one we know | any disowning phrase | `weeds.json` | ? |
| service history | a `service_history` **tool call** | any date stated without one | `vehicles.json` serviceHistory | **FAILS** (dropped) |
| breaker | a `circuit_for` **tool call** | a breaker number without one | `vehicles.json` circuits | **FAILS** (dropped) |
| honesty marker | the hedge | a bare claim from a marked field | the 91 markers | ? |
| each of the 4 fence flows | a fence whose name **resolves against canon** | an unresolvable name | the flows' own contracts | ? |

**The fail mode tool-use ADDS — and the assertion that catches it.** Today's failure shape is *a wrong
number inside a correctly-grounded answer*. Tool-use adds *the model didn't call the tool and answered
from nothing* — harder to see, on a surface where trust is the load-bearing emotion. Three layers, and
the third is the one that matters:

1. **Forced tool use** on the first turn naming a canon entity: `tool_choice: {type:"any"}` +
   `strict: true`. Available — the skill's `shared/tool-use-concepts.md` records that only
   Fable/Mythos 400 on forced tool use; **Haiku 4.5 accepts it.**
2. **The names index**, so "look it up" vs "we don't have it" is a lookup, not a guess.
3. ⭐ **The harness reads `response.content` for `tool_use` blocks and asserts tool-called on every row
   whose answer is only obtainable by lookup. A row that returns the RIGHT answer with no tool call is
   a FAIL.** That inverts the usual grading and it is the point: a right answer with no lookup means
   the model reconstructed it, and the 2,800 ft error is what reconstruction looks like when it misses.

**Where it runs. Recommendation: the § C4 QA Worker, Q3 = YES, under a hard budget cap.** QA has its
**own `OBSERVATIONS` namespace** and bindings are non-inheritable, so a QA `/api/chat` cannot reach
Mom's channel **structurally** — strictly stronger than prod's origin predicate, which fails open on a
typo (`origin:"prob"` → `app` → an obligation to Mom manufactured by a typo). Priced: ~15 rows cold at
today's 143.6K prefix and $1.25/MTok 5-min write ≈ **$2.69/run**; at a 15K core ≈ **$0.28/run**. The
probe refuses to run above a declared per-run budget read back from `/api/cost-log`.

**Recorded-response replay is the other half, not the alternative.** Cache every
`(request, response, usage)` to `.private/guru-fixtures/`; replay asserts the parsers, the four fences,
tool dispatch and the names-index negative at **zero spend, in CI, on every commit**; the live leg is
pre-deploy. The deterministic half of this harness must have a **non-AI door** — a fence-parsing
regression must be catchable without an API key. **Falsifier:** if a replay ever passes while a live
run on the same table fails, the fixtures have drifted and the replay leg is theatre — so stamp each
fixture with model id + a hash of the assembled prefix, and **expire the set on any prompt change**.

---

## §3 · The private tier through the box

**READ — yes, to fields:** service history, service contacts, circuit labels, manual references,
rhythms, receipt **metadata** (that it exists, date, vendor, amount, which machine); bodies later, rung 4.
**NEVER read:** anything derived from a person's words about themselves — the QUARANTINE clause
(`CLAUDE.md` § The AI boundary) keeps her account of her own uncertainty in `.private/`, never
reflected back to her. That covers the voice transcripts and the disposition logs.
**WRITE — never. Zero write tools, permanently.** The write path stays the fence: a routing marker the
client resolves and a human approves (*the fence is the bridge*). A tool that writes is how the ask
path quietly becomes the capture path.

**How a lookup enforces the grant.** The tool receives `estateId` + the grant's capability set from the
**verified credential**, resolved server-side — never from the prompt, never from the request body.
⛔ **There is no seat for that yet, and it is structural, not a preference:** `authOk` checks a single
`SHARED_TOKEN` for the whole Worker (`/api/chat` is gated by the catch-all, not its own check), and per
`.plans/2026-09-02-data-model-design.md` § 3 **zero of the 11 KV namespaces carry a property
coordinate**. ⇒ **hard gate on C6.**
The shape once C6 exists: `handleChat` resolves `{estateId, capabilities}` before assembling tools, and
**the tool list is derived from the grant** — a person with no vault grant gets a schema with no
`get_receipt` in it. Nothing to refuse, nothing to leak: the playbook's *schema-as-boundary* move
applied to authorization, **give the wrong answer nowhere to land**. One boundary, one place (§ 6).
**Falsifier:** if `estateId` appears anywhere in the accepted request body, the boundary is misplaced.

**The third path, and why a lookup is not it.** `PRODUCT-ENGINE.md` § condo names it: a model doing
**editorial selection** — *"positive local news"*, choosing what she **sees** rather than drafting
something Paul approves. Neither ask-path, nor capture-path, nor authored-content-behind-a-gate; it
needs its own ruling before it is built. A lookup is not that: invoked **inside a turn she initiated**,
returning a **deterministic** subset over a **closed input set**, **selecting nothing** — it retrieves
what she named. The model chooses *which tool*, never what is true and never what she sees.
⚠️ **The route by which a lookup could become selection, stated so it is checkable: if a tool's result
set is ever ranked or filtered by the model's judgment of relevance, it has crossed.** So lookups
return the record complete, deterministically sorted, or **raise** — never `[]`, never a model-chosen
top-k. And **rung 4 retrieval is the case that does edge toward selection**, since nearest-neighbour
ranking *is* a relevance judgment: a second, independent reason it goes last and stays scoped to prose
the user explicitly asked about.

---

## §4 · Latency and shape on her surface

**Do this first, with rung 0: instrument it.** `logChatCost` gains `latencyMs` and `toolRoundTrips` —
two lines, zero risk, and the only way the streaming gate can ever fire. *Altimeter, not autopilot*: a
gate watching an unrecorded metric is not a gate.

**Streaming ships WITH tool-use, not after.** One round trip = one latency unit and tolerable dead air;
two roughly doubles it on a surface with no progress signal, and streaming is the only mitigation that
doesn't cut capability. Architecture requirement, mine: **tool round trips complete before the stream
opens** — never stream a partial answer a pending tool call is about to contradict. The *shape* of the
waiting state is `ux-expert`'s.

**600-token reply cap — KEEP the number; move where truncation happens.** 600 tokens is ~two short
paragraphs, which the voice rules already demand. But lookups change the content: *"when did we last do
the Bronco's brakes"* is now a 22-row answer, and 600 tokens is where a list truncates mid-row.
**Required either way:** truncate in the **tool** — at most N rows, deterministically most-recent-first,
stating *"22 rows, showing 5"*. A truncated reply looks exactly like a complete one
([[reference_match_payload_not_container]]); a counted one cannot.

**6-turn cap — KEEP, but it now measures the wrong thing, and the migration breaks it silently.** The
client caps **user** turns; the Worker's defence-in-depth ceiling caps **message-array length at 20**.
With tool-use one user turn becomes 2–3 array entries (`tool_use` + `tool_result`), so a legal 6-turn
conversation starts hitting a ceiling set when a turn was one call. **Bound user turns, not array length.**
**Falsifier:** if measured p50 for a tool-use turn on house Wi-Fi lands under ~1.5× today's p50,
streaming can ship after the core and §6's sequence changes.

---

## §5 · Model and cost

**Source of truth: the `claude-api` skill's bundled reference.** ⚠️ It is **not on disk** — no
`claude-api` directory exists under `~/.claude/skills` or the plugin marketplaces; it is embedded in
the CLI binary (`~/.local/share/claude/versions/2.1.259`) as zstd blobs. I extracted and read
`shared/models.md`, the skill root's pricing table, `shared/prompt-caching.md`, `shared/tool-use-concepts.md`.
**Haiku 4.5** = `claude-haiku-4-5` (full `claude-haiku-4-5-20251001`), 200K ctx, **$1.00 in / $5.00 out**
per MTok. **Sonnet 5** = `claude-sonnet-5`, 1M, **$2.00 / $10.00**. Ids exactly, no date suffixes. Cache
reads ~0.1× base; writes **1.25×** (5-min) / **2×** (1-hour). **Prompt-cache minimum on Haiku 4.5 =
4,096 tokens, failing silently below.** Haiku 4.5 Active (§0④).

**Recommendation: stay on Haiku 4.5 for this migration; re-open Sonnet 5 as a separate, Mom-gated
change after the core lands.** This reverses the *emphasis* of my own 09-02 rung-1 call. Rung 1's case
was 5× headroom against a 143.6K prefix growing ~950 tok/day toward a 200K wall. **A 15K core retires
that pressure outright** — 7.5% of 200K is better retrieval territory than 14% of 1M — *and* it is the
only one of the two that fixes **reachability** (61 service rows, 30 breakers), which no window buys
back. They substitute for the headroom problem, not the reachability problem. Two more reasons: Sonnet
5 is a **different voice on Mom's surface** and owes the mom-proxy walk — don't stack two voice risks in
one release; and the retirement-floor leg doesn't survive §0④.
**Falsifier:** if the harness shows Haiku 4.5 missing the *tool-called* assertion at a rate prompting
can't fix (say >1 in 10 on forced rows), the model is the constraint and Sonnet 5 goes first.

**Cost at measured volume** (0.54 turns/day ≈ 197/yr; ~30% warm cache): today ≈ **$0.088/turn ≈
$11.80/yr** (from the cost-log's measured $2.91/90d). At a 15K core with 2 round trips ≈ **$0.026/turn
≈ $5/yr**; **3 estates ≈ $15/yr**, since the cache amortizes **within** a 5-minute window and never
across estates (N estates ≈ N cold cores). ⛔ **Cost is not the argument and must not be presented as
one** — this halves an already-negligible bill, and the July `$9.29/year` figure is what happens when
it is. What scales badly with estates is not dollars but **the number of cores to keep fresh** — C5's
module-set declaration doing real work.

**Caching the core:** unchanged three-layer geometry (Layers 1–2 cached, Layer 3 per-call; already
spread on its own to `SCHEMA_DRAFTER_SYSTEM`). Two additions: **tool schemas belong in Layer 1–2** and
must be assembled in a **declared order** or a reordering silently breaks the cache; and **assert the
core is ≥ 4,096 tokens** at build time.

---

## §6 · Sequence — and what ships independently

| # | Ships | Independent? | Deterministic check (existing tool first) |
|---|---|---|---|
| **0** | **Rung 0 + latency**: the digest gate reads the **billed** prefix back from `/api/cost-log` and hard-fails above a declared budget; `logChatCost` gains `latencyMs` | yes | `check-digest-fresh.py` exit 0; **drive the gate** — feed it a budget below the measured prefix and require a nonzero exit |
| **1** | **The elevation pin**: 2,959 → 2,873 in all five prompt blocks, sourced from canon. Mom-facing ⇒ Paul confirms the wording | yes | new `tools/check-prompt-facts.py` — every hard-coded number in `worker.js` prompts matches its canon source; `check-data-inline.py` + `check-digest-fresh.py` exit 0 |
| **2** | **The harness**: fixtures + zero-spend replay, then the live QA leg | yes | `--selftest`; **mutation test** — doctor a fixture back to 2,959 and it must FAIL; origin controls per `test-feedback-cycle.py`'s hygiene pattern (`/api/conversations` default excludes it and `excludedNonApp` increments; `check-mom-ack.py` exit 0; `read-mom-feedback.py --pickup` silent) |
| **3** | **Core + lookups behind a flag** — the flag is a request field the client doesn't send, so prod stays byte-identical until flipped | after 2 | harness green on **both** paths over the same fact table; core ≥4,096 and ≤ budget asserted in the build; all four fences resolve against canon |
| **4** | **Retrieval for prose** — references, research library, manuals; complete and unranked-by-model | after 3 | harness rows that must cite a source, plus a *"no relevant source"* row that must refuse rather than paraphrase |
| **5** | **The private tier** — credential → grant → tool list | **gated on C6** | negative-control grant with no vault capability receives a schema **without** the private tools (assert on the request, not the answer); a cross-estate probe 403s at the credential, not at the tool |
| **6** | **Streaming** — with 3 if step 0's measurement says the doubled wait is real | after 3 | measured p50 first-token vs today's p50 full reply |

Steps 0 and 1 are independent of everything and of each other; **1 goes first in practice because it
is live and wrong.**

---

## §7 · What I did NOT decide — Paul's

- **Q3, the QA Anthropic key.** I recommend **yes, with a hard per-run budget cap**; it is his spend. A
  "no" costs the live leg and leaves replay only.
- **Whether 600 and 6 are product decisions.** The **numbers** are his; the **mechanisms** are mine and
  required either way — truncate in the tool with a count, bound *user* turns not array length.
- **When the private tier joins** — after C6 by sequence, but whether *"everything in that estate's
  database"* includes it at all is still the open crux in `PRODUCT-ENGINE.md` § ③.
- **Whether the elevation fix ships as its own release** or inside the harness item.
- **Whether `turf` sits in the core** or behind `turf_regime()`. Coin flip; I lean core — it's cheap and
  the weeds' advice is incoherent without it.
- **The module on/off UNIT** (domain vs named bundle, C5's open call): it sets the core's assembly
  granularity, so §1's module-awareness can't be finished without it.

## §8 · Open questions

1. Is 2,873 the figure that reaches Mom, or does the pin need **both** numbers with the same
   explicit-negative disambiguation that made the 2,800 ft pin work?
2. Does the fact table live in the repo as canon (reviewable, diffable) or in `.private/`?
3. Is the names index built by `build-digest.py` — one artifact, one freshness check — or by a new tool?
4. What is the declared per-run budget for a live harness leg, and who is told when it's exceeded?
5. Does the fact table become a gate on the deploy script, or a beat in the mom-cycle?
6. For a record with a standing COVERAGE warning (the parts record, wrong in both directions), does
   every lookup return *"not in the record"*, or does each tool declare its own honesty string?
7. Is there a second estate's canon shape to design the tool namespace against yet, or does
   one-estate-at-a-time hold through the migration?
8. Do the five prompt blocks that each restate the property's facts collapse into one shared hard-facts
   fragment, or does each keep its own copy and its own way of going stale?
