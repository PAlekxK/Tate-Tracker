# Handoff: fernwood — the STANDING BACKLOG SESSION

<!-- generated 2026-09-12 · source: Tate-Tracker@9da095fb · main · CLEAN TREE, no window committing
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Every file:line has a half-life measured in MINUTES when several lanes are live (measured under ten
        on 2026-09-11). Cite the SYMBOL, stamp the sha, and re-read the file you are citing immediately
        before the commit — not only before the edit.
     ⛔ Model-flagged ≠ cleared. §8 says which is which. -->

## 1. Mission — what this window IS

`[paul-stated 2026-09-10]`: *"I almost think it's worth having just a standing session that's going
through the backlog and helping me refine it, and also queuing up items for the next couple laps of
build. Our commit phase is the one time we pull from the backlog, so that's the only time it really
needs to be frozen. We can keep having that conversation going in real time in another session."*

**You are that session.** A live, continuing conversation with Paul over `BACKLOG.md`: refine rows, surface what
is stale, and keep a short **queue for the next two build laps** that a build session can pull from at its commit
phase. You are not a build lane and not the coordinator.

⭐ **You are ALSO the registrar** `[paul-ruled 2026-09-10: "fold it in"]` — the registrar seat was folded into this
session rather than stood up separately. **One writer to `BACKLOG.md`, two voices.** Nothing else may write it
while you are live.

## 2. The three windows — and which you are

| window | job | never |
|---|---|---|
| ⭐ **coordination** — `tate-tracker` main, **the window that opened you, and it stays live as the coordinator** | routes, sequences, holds the commit-phase freeze, merges, runs laps | writes a feature · writes `BACKLOG.md` while you are live |
| **this one — backlog** | refines the backlog with Paul in real time; queues the next two laps; **sole writer of `BACKLOG.md`** | commits code; pulls rows into a build |
| **build** (opened separately, per item) | pulls from the queue at its commit phase and builds | edits `BACKLOG.md` status prose |

⛔ **The freeze is on the PULL, not the document** `[feedback_commit_phase_is_the_only_freeze]`. When a build lane
declares a commit-phase pull, hold edits to the rows it names until it releases. Everything else keeps moving.

⚠️ **Route to coordination, do not absorb:** anything that is a lap decision, a window to open, or a ruling for
Paul goes back to the coordinating window. **It routes; it never absorbs your work, and you never absorb its.**

## 3. Read first (in this order — POINT, don't re-derive)

1. **`cycle/release/CYCLE-LOG.md` § `## Lap 8`** (`:4005`) — ⭐ **read the ✅ CLOSED block at the END of the
   section**, not the heading alone. Lap 8 closed **2026-09-11 15:47 EDT**: row T (the testing architecture) alone,
   24 of 24, **NOTHING DEPLOYED, no candidate moved**, 7 of 10 declared cells UNWALKED with the gate REFUSING **by
   design**. ⛔ **Lap state is the `## Lap` HEADINGS, never `cycle-state.json`.**
2. **`.plans/2026-09-11-lap9-READINESS.md`** — ⭐ **rewritten 2026-09-12 at `9da095fb`; read §0-PRIME and
   §0-PRIME-B FIRST.** Five of its claims were re-measured and moved. Do not cite the pre-rewrite version.
3. **`BACKLOG.md`** — `# ▶️ NEXT` (`:31`), `## ⏭ THE NEXT TWO LAPS` (`:95`), `## 👤 WAITING ON PAUL` (`:136`).
4. *(as needed)* `.plans/2026-09-11-lap8-build-PLAN.md` § **ROW A · the door**, A0–A15 — **an audited build plan
   that was never executed.** It is the strongest queue candidate in the repo.

## 4. State — measured 2026-09-12 at `9da095fb`

- **HEAD `9da095fb`, `main`, clean tree, nothing uncommitted, no other window committing.** *(Contrast the last
  backlog session, which saw HEAD move eight times under it.)*
- `check-backlog-drift.py` → **exit 0, rested**, last rationalization 2026-09-11 (1d). **No grooming owed.**
- `check-backlog-ready.py` → ⛔ **exit 1**, and **not because of anything in `BACKLOG.md`** — every complaint is a
  `.plans/` header (R4 document-vs-item, orphans, a missing `stage:`). ⚠️ **Capture the exit code directly**:
  `python3 tools/check-backlog-ready.py >/tmp/o.txt 2>&1; echo $?`. Piping to `tail` returns **tail's** exit code
  and reads **0** — measured today, in this repo.
- `-READINESS` is a suffix the checker **grades by nothing** and says so. Adding it to `DOC_SUFFIXES` belongs to
  that tool's owner, not to you.
- **qa serves `87c7aae` — 148 commits behind HEAD**, app surfaces changed. Not yours to deploy; know it before
  reading any qa-derived number.

## 5. ⛔ Guardrails

1. **`BACKLOG.md` only.** `git commit --only BACKLOG.md` every time. Never `-a`. Never another lane's staged work.
2. **⛔ Do not edit `.plans/2026-09-11-lap9-READINESS.md`.** The coordinating window rewrote it today and owns it.
   Disagreements go back through coordination.
3. **Derive the two-lap queue with `check-backlog-ready.py --ladder`; never retype it.** That is the section's own
   rule.
4. **Escape `|` inside code spans in table cells** (`a \|\| b`) — unescaped, it silently splits a row into extra
   cells and nothing in the repo checks table integrity.
5. **An unchecked box is not open work.** Probe the world before acting on a row's status prose — these documents
   go stale in the direction of **over-reporting** open work. Today's rewrite is four fresh instances of exactly
   that.
6. **You flag; Paul clears.** Never promote a model-read value to a row as fact.
7. **Mom's words stay in `.private/`.** Rows carry counts, ids and dates only.

## 6. First tasks (ordered)

1. ⭐⭐ **File the four N-findings from today's re-measurement as rows.** They are measured, none is filed, and
   three of them block other rows. Source: `.plans/2026-09-11-lap9-READINESS.md` § 0-PRIME-C — **read it, do not
   re-type from this brief.**
   - **N1** zone saving returns 503 at `home`, `qa`, `lab`, `paul` — `GITHUB_TOKEN`/`GITHUB_REPO` exist on
     `legacy` and nowhere else. ⚠️ *Code + config read, NOT a live confirmation; the row should say so and name
     the POST-at-`lab` that would confirm it.*
   - **N2** `qa` has `ANTHROPIC_API_KEY` and **no** `ANTHROPIC_WORKSPACE_ID` — the 2026-09-03 identity-linked-key
     shape. ⚠️ *Binding measured; the "that is why qa routes DARK" half is INFERRED. File it as a hypothesis with
     its verify-by-use.*
   - **N3** G6 has **never rendered at `home`** — 13 real sessions, 0 served orders. Row E's counter is at **1 of
     10** and is not moving. *A defect on the path, not a wait.*
   - **N4** the two "cheap" refutation checks need a grant token (401 without one); and
     `fernwood-home.pages.dev/api/zones` returns **HTTP 200 with the SPA shell** — a status check against the
     wrong host reads green for an endpoint that is not there.
2. **Strike or correct every backlog row that rests on a claim §0-PRIME-B moved.** Specifically: any row treating
   **Q8 as blocking** (its narrow fix shipped 2026-09-07 in `e5fbe509`), any row saying **`read-glance-order.py`
   does not exist** (it shipped 2026-09-10), and any row carrying **R-Z6(B) as a live leak at `home`** (it cannot
   fire there — the class is real, the instance is not). ⭐ *A correction must sweep the files quoting it.*
3. **Regenerate the two-lap queue** — ⛔ it was **correctly blocked** last session because lap 8's shape was
   unknown. **It is known now.** Derive from `--ladder`.
4. **Place § INVITE & JOIN's five-seat scoping.** It was ruled into lap 8 (9·4) and **did not run** — no artifact
   exists. It is the one item in neither lap. It needs a lap or a hold **with a release condition**; "indefinitely"
   is not one. **Route the placement to Paul via coordination; file the row yourself.**
5. **The nine Fernwood needles in shipping comments** — held at lap 8's close *"for Paul to place — this lap or the
   next."* Still unplaced. File it as a row so it stops living only in a close record.
6. **The prior session's standing owes**, still open — the distinct-`questionId` count (TIER 1 · 59, filed, needs
   *running*) · the zones window's four register edits to TIER 2 · 7 · the PRODUCTIZE census · the `#card-told`
   cut, routed to content · and §10.C's four unfiled findings (**UR-§7a**, **SIZ-0c**, **SIZ-T18**, **MP-0**).
   ⚠️ **TIER 2 · 22's correction: three of its four items were reported done and NOT verified. Probe before
   editing that row.**

## 7. Un-sealed judgment — what is NOT on disk anywhere

⭐ **One item, and it is a real read, not a fact:** the coordinating window's recommendation is that **lap 9 should
be THE DOOR** (row A0–A15), overruling the ruled 8·3/9·2 ordering that puts the weather card first — because the
door is what rows C, D and F are all waiting on, it already has an audited build plan, and lap 8's own close
nominates it. ⛔ **Paul has NOT ruled on this.** It is written into the rewritten readiness §8 as a ranking with its
alternative beside it, so it is not lost — but **do not queue lap 9 as the door until he says so.** If he rules it
in your window, that ruling belongs in the CYCLE-LOG via coordination, not only in a backlog row.

Nothing else. The reset is otherwise safe.

## 8. Trust status — per open item

| item | status |
|---|---|
| Lap 8 closed; row T delivered 24/24; nothing deployed | ✅ **human-cleared** — `[paul-ruled: "go ahead and close the lap"]`, recorded in the CYCLE-LOG close block |
| 7 of 10 declared cells UNWALKED, gate refuses by design | ✅ **human-cleared** — Paul declared the cell list (`cycle/release/cells/lap-8.json`, `declaredBy: paul`) |
| Q8's narrow fix shipped (`e5fbe509`) | 🔵 **model-verified in code, not human-cleared.** Read at `engine/viewer.template.html:20779–20830`. The *general* mechanism (W-9) remains **unruled** |
| The door (A0–A15) was never built | 🔵 **model-verified, four independent probes.** Strong, but nobody has signed it |
| N1 · zone saving dead on four environments | 🟡 **model-flagged, NOT confirmed live.** Code + config read; no POST was made |
| N2 · qa's missing workspace id explains the dark Guru | 🟠 **binding MEASURED; cause INFERRED.** Do not file the cause as fact |
| N3 · G6 never renders at `home` | 🔵 **model-verified** by the reader's own output. ⚠️ A deviceId is a browser bucket, not a person |
| R-Z6(B) cannot fire at `home` | 🔵 **model-verified** (gate + binding list). ⭐ The *class* stays on the register |
| "Lap 9 should be the door" | 🔴 **MODEL OPINION. Paul has not ruled.** See §7 |
| Mom's two undispositioned arrivals | ⛔ **still undispositioned.** TIER 1 · 67 parks *when*, and **does not clear the channel**. The checker will keep flagging both — that is it working |

## 9. Done when

Paul says the session is done — ⛔ **this is a STANDING session; it has no self-closing condition.**
`[paul-stated: "close all the windows out when they're done with their work… do that as work actually concludes,
don't force it"]`

**A good first sitting is done when:** §6's items 1–3 are filed or explicitly deferred with a reason,
`check-backlog-drift.py` still rests, and the two-lap queue is derived from `--ladder` rather than typed.
