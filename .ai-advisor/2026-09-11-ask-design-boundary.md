# The AI boundary for ASKS — ai-advisor's return to the ask-design window

- date: 2026-09-11 · seat: ai-advisor (CONSULT) · window: ASK DESIGN (`handoff/handoff-ask-design.md`)
- status: **agent-proposed. Paul rules.** Nothing here moves the human gate in either direction.
- read: CLAUDE.md § The AI boundary (7/14 rule · the 09-02 role amendment · INGRESS · QUARANTINE · modes 1–8 ·
  the "third category" clause · the >10 threshold · the 15–20 log-summarizer seat) · § Design-time default ·
  `~/.claude/ai-playbook/cross-cutting/ask-capture-boundary.md` + `definable-loops.md` + `fernwood.md` ·
  `.decisions/fernwood-11 · -12 · -17` · BACKLOG § CONTENT·CARDS · `.plans/2026-09-11-legacy-toolchain-INVENTORY.md` §4

---

## 1 · Does ">10 answered across reseed cycles" govern a card-intro ask?

**No — and not because the bar is low. Because it measures the wrong thing.**

Read the clause in context: *"phrasing was never the bottleneck; revisit AI-draft-behind-the-gate only if the
loop proves durable."* It is a **cost-benefit gate on the CONFIRM loop**, not a safety gate. It asks: does
`harvest-questions.py` mint enough near-identical cards that per-card phrasing labour recurs? A card-intro ask
is not in that loop: no canon target, no verdict on our guess, not mechanically harvestable from a marker, and
authored **once per card**, not once per record.

**THE COUNT TODAY, since a threshold cited without its number is the failure this repo pays for.**
`questions.json` = 22 cards; `momlib.question_state()` reads **draft 11 · unprobeable 5 · resolved 5 · open 1**.
Answers actually settled and folded: **5** — `q-almanac-name` · `q-crocosmia-lucifer` · `q-white-mophead-annabelle`
· `q-panicle-hydrangea-bloom` (Paul 99%-attributed) · `q-top-categories`. With `momqueue_tapped` 3-in-60-days
(08-12) and lap 8's 0-of-10 offers, **the confirm-card gate is not met after fourteen months and nothing in this
window opens it.** Say so out loud so no reader infers otherwise from the rest of this document.

**RECOMMENDATION — the card-intro ask gets its own gate, and it counts CARDS, not answers.**
Hand-author until the same ask has been written for **three cards** (weather + two) and the third is visibly the
same shape as the first. Rationale: for a confirm card the bottleneck was phrasing; for an intro ask the
bottleneck is **knowing what the card can actually vary** — a fact about the code, learned by building cards,
not by collecting answers. Before three, a model has no form to draft against and will produce plausible
questionnaire prose, which is exactly what `fernwood-17`'s elicitation ruling forbids (*not "ask more questions"*).

**FALSIFIER, both directions.** If card 3's ask is *not* structurally the same as cards 1–2, there is no template,
the gate does **not** open and hand-authoring continues. And the likelier outcome, stated as a prediction so it
can be checked: if cards 1–3 are so alike that a **deterministic** template bank produces them — *"Which of these
would you like <card> to show?"* over a list derived from the card's own sub-components — then **the model's seat
never opens at all**, and that is a success, not a shortfall.

## 2 · The definable loop, if a model may draft

**Trigger, not cadence:** a card is being built, or gains a sub-component. Loops rest.

| # | step | who | AI? |
|---|---|---|---|
| 1 | **derive what the card can vary** — sub-components read from the code/manifest | tool | ⛔ no — this is the non-AI door |
| 2 | **derive what must NOT be asked** — anything the address or the ranking already gives (UV·AQI·climate·frost·elevation are address-derived; the card's presence is ranking-derived) | tool | ⛔ no — the elicitation rule as a **pre-gate** |
| 3 | **DRAFT one ask** over (1) minus (2) | model | ✅ **the only seat** |
| 4 | **post-check** — every option ∈ (1); none ∈ (2); fold target exists on the household record; ONE affirmative grammar; exactly one question | tool | ⛔ reject, never auto-repair |
| 5 | **⭐ the administrator confirms the words** — a stamp only a human writes, as `rationalize-bench.py --approve` already is | human | ⛔ **not negotiable** |
| 6 | land, with `_source: drafted \| authored` so the ledger can read which | tool | ⛔ |
| 7 | serve — template bank / MomQueue, cap and ordering already ruled | tool | ⛔ **no model at serve time, ever** |
| 8 | capture — verbatim | tool | ⛔ |
| 9 | read — `tools/ask-ledger.py` | tool | ⛔ |
| 10 | **self-improve, pre-registered** — see below | both | |

**Step 3's containment is structural, not instructional:** forced tool-use with a typed schema whose `options[]`
are an **enum of step-1 identifiers** and whose `foldTarget` is an enum of household-record keys. No free-text
option field. An ask for a thing the card cannot render has nowhere to land. (`fernwood.md` § forced tool-use;
`cross-cutting` § the fence is the bridge.)

**Checks that have been SEEN to fail** (the definable-loop requirement — not decoration):
- ⛔ **the watermark.** CLAUDE.md: an `unprobeable` card is *the one state that cannot clear itself* and holds the
  ceiling until a human retires it. The inventory §4 measures the consequence: **a family of intro asks shipped as
  `_kind: reflective` would pin the watermark by design.** An intro ask must have its own fold target — a
  *declaration* on the household record — before the first one ships. This is the loop's blocking prerequisite.
- ⛔ **entity resolution degrading silently** (`ENTITY_SOURCES`; the weed card served six days rendering nothing).
  An intro ask has no entity; the post-check asserts that absence is **declared**, never inferred.
- ⛔ **a completion claim with no mechanism** (`fernwood-12`, the refrigerator). An ask must not imply the card
  will change if nothing is wired to read the answer.

**Pre-registered self-improvement, two numbers, registered BEFORE the first lap:** (a) step-4 rejection rate,
(b) **the administrator's EDIT rate at step 5** — did the human ship the model's words unchanged? Falsifiers, both
written now: **>50% rewritten → the model is not saving work, the seat closes.** Zero rejections *and* zero edits
across three cards → the draft was deterministic; **demote it to a template and delete the model call.**

**Awareness surface:** one line in the pickup block — asks served · answered · drafted-vs-authored · edit rate.
Glanceable; never a stream to parse.

### What the model may READ — the rule is one line
**The model reads the PRODUCT, never the person.**

| input | verdict | creep mode at risk |
|---|---|---|
| the card's sub-components, its copy, the ask grammar, prior authored **asks** | ✅ yes | — |
| the module/interest taxonomy as published in `onboarding/index.html` (a **shape**) | ✅ yes | — |
| **this household's ordered ranking** | ⛔ **no** | 4 (re-interpreting her taps) · 8 (a behavioural record into an artifact). Falsifier: if drafts are measurably worse without it *and* every administrator edit is about ordering, revisit |
| address-derived facts | ⛔ **no**, and not for privacy — step 2 *subtracts* them deterministically; handing the model a set it is forbidden to use is strictly worse. `check-canon-scope.py` also stands: a drafting prompt reading the address is a sixth model route inheriting that leak | — |
| **prior ANSWERS, any household** | ⛔ **no. The clause most under pressure and the one to rule explicitly.** *"The model would write better asks if it saw what people answered"* is true and is still no | 1 (classifying her note) · 4 · 8. If answers should shape the next ask, that reading is the **administrator's**, off the ledger |
| `.private/`, zone audio, transcripts, Guru turns | ⛔ no | QUARANTINE, unchanged — cited, not restated |

## 3 · The ledger on the way out

The ledger is deterministic and **stays the door** (*deterministic things need a non-AI door*: if the only way to
learn how many asks were answered is to ask Claude, it is broken).

**May a model summarize it? Yes in principle — it is analysis of the record on the way out, inside the existing
egress clause and needing no new permission. Not yet in practice, and the gate is not n.** At 22 asks and 5
settled answers a summary is a **reformatted table**. The gate is *"the table stopped fitting on a screen"* —
concretely **≥40 asks across ≥3 estates**, where a cross-estate pattern is a reading a table does not give.

⛔ **This is NOT the 15–20 seat, and the distinction matters.** That seat (CLAUDE.md, 7/14) summarizes *her
answers*; it sits at 5 and stays shut. The ledger's rows are **product facts** — served, answered-count, fold
target, row link. Nobody should read *"the ledger may be summarized"* as *"her notes may be summarized."*

**Four things the summary may never do:**
1. **Place a seed** — suggest, never write (the 7/14 clause's own words; `seed-not-thesis`).
2. **Phrase an ask** — a summary that arrives pre-worded has bypassed gate 5 in one sentence. It observes gaps in
   the **indicative** (*"no household has been asked what the weather card should highlight"*), never the
   imperative (`mood is the fence`).
3. **Name or characterize a person** — counts only; a deviceId is a browser bucket (`watch-door.py`'s own rule).
4. **Become the ledger** — a second reader, never the door; and per the 09-10 rule it states on its own face what
   it does **not** cover.

**Its falsifier:** if the first three summaries say nothing the deterministic table did not, delete it — the
`post-deploy.py` self-falsifier model.

## 4 · fernwood-11's third option, and fernwood-12

**They are usually spoken of as one direction. In boundary terms they are opposite, and that is the thing to make
visible before Paul rules.**

> **The cost, in one paragraph.** Making the Guru the primary **capture** surface puts a model between a person's
> words and the record. Today capture is deterministic and verbatim — what she typed or tapped is what is stored,
> and the model is never in that path. Guru-as-capture means the model *hears* the fact and something downstream
> writes it, so the model's understanding, not her words, is what lands: that is forbidden mode 1 (AI cleaning or
> classifying at capture) and mode 4 (AI re-interpreting) **by construction**, not by accident, and every existing
> capture guarantee becomes conditional on a model behaving. It is also structurally fragile at this site — the
> physical premise is no cell reception away from the house, so a capture path needing a model round-trip fails
> exactly where she is standing when she has something to say, and a capture path that can lose her words while
> appearing to succeed is the failure `fernwood-12` already caught once (*"It's in the record now"*, nothing
> written). Ruling option 3 would not be *more AI*; it would make four of the eight creep modes unenforceable and
> require the boundary to be **rewritten rather than amended**. **The fence is the way to get the behaviour
> without the change:** the Guru *proposes* a structured capture, the person's own words are written, a human
> confirms — which is why `fernwood-12` is not a smaller `fernwood-11` option 3 but its replacement.

**Recommendation:** rule `fernwood-11` = **keep-asking-and-instrument-her-doors** (I concur with the card), and
`fernwood-12` = **extend-the-fence**, scoped to `household-system` and `vehicle`/`equipment` first.

⭐ **And the point specific to THIS window, which neither card states.** The Guru is already on the ask path, so a
card-intro ask *delivered conversationally* is **not an ask/capture violation at all** — the model would merely be
asking. But it **is a gate violation**: every ask today is human-confirmed *before* it reaches a person, and a
conversational ask is composed at runtime and cannot be pre-confirmed. **So the card-intro ask is served
deterministically from the card, not by the Guru.** If a Guru-delivered ask is ever wanted, it must be a fixed
pre-approved string the model delivers verbatim — which is a template bank with extra steps, and says the
deterministic path was right.

## 5 · For the playbook — THE RULE, in the boundary's own form

> **THE RULE FOR AI IN ASKS.** An ask is **authored content** — the boundary's third category — so the model's
> seat is *drafting*, never authoring and never asking. **On the way in:** a model may draft an ask's words from
> the **PRODUCT** — the card's own sub-components and the ask grammar — and never from the **PERSON**: not their
> ranking, not their address-derived facts, not a prior answer, not a word they have said (INGRESS and QUARANTINE
> unchanged; modes 1, 4 and 8 are the ones this clause holds shut). The draft is bounded by a typed schema whose
> options enumerate what the card can actually render, so an ask for a thing that does not exist has nowhere to
> land. **The administrator between:** the words are confirmed by a human before they reach anyone, by a stamp
> only a human writes — the gate `rationalize-bench.py --approve` already is; an agent may run every other step.
> **On the way out:** the ask ledger is deterministic and stays the door; a model may analyse it, in the
> indicative, never phrasing an ask, never placing a seed, never naming a person — and **not yet**. **Serving and
> capture are untouched:** the ask is served deterministically and the answer captured verbatim — *the model is
> never in the room when a person answers.*

⚠️ **Proposed for `~/.claude/ai-playbook/fernwood.md` as a new pattern — NOT written. Paul confirms first.**
