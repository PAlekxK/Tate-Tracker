# product-steward — QUESTIONS IT COULD NOT CITE

- row: process — no BACKLOG row, same posture as every process document in `.plans/`
- objective: O5
- kind: queue
- class: engine · declared
- seats: product-steward (this file is its only write destination outside a BACKLOG row)
- depends-on: .plans/2026-09-07-product-steward-CHARTER.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ NOTHING HERE EXECUTES. A question is an OPEN question; it is not a finding, a
  recommendation, or a decision. ⛔ **This seat may not CLOSE a question** — that verb is not in its
  table. Paul closes, or a later citation does.
- stage-note: 2026-09-07 — **created to close process-audit G3.** Beat 8's exit condition is *"each
  finding reaches a row it can CITE, or opens a question where it cannot"*, and the charter's verb
  table promises *"one queue file of questions it could not cite"* (`:105`) — **without ever naming
  the file.** `measured`: no such file existed. The three `*-queue.md` files already in `.plans/`
  (`field-capture`, `grooming`, `independent`) belong to other threads and are not this.
  ⭐ **The failure mode that made this worth fixing before beat 8 runs**, not after: with no named
  destination the choice gets made per-finding, at speed, by whoever is writing — which is how the
  same class of item ends up in three places and the register stops being one register.

---

## ⭐ THE TWO DESTINATIONS, NAMED — this is the whole point of the file

| beat 8 outcome | destination |
|---|---|
| the finding **can be cited** to an existing row | ⭐ **`BACKLOG.md`** — the row's own fields (stage · pointer · stage-note · seat citation), with a `[paul-ruled <date>] <file:line>` provenance line. **No new row is created** — `CREATE` is not in the seat's verb table |
| the finding **cannot be cited** | ⭐ **THIS FILE**, one entry, with what it could not find |

⛔ **There is no third destination**, and a finding that reaches neither has not been carried.

---

## Open questions

*(none yet — beat 8 has not run. Its input is beat 7's read, which is in flight.)*

⚠️ **The inbox beat 8 will work from**, `measured` by `python3 tools/product-steward.py` at HEAD
`cfd41fb`: **20 ruling lines that nothing in the register carries**, plus **8 more UNCHECKABLE by
that predicate** (no quotable verbatim on the line — *absent*, not *clean*), **3 uncited seat trails**,
and **1 plan whose newest stage-note predates its own last commit**.

⛔ **Those 20 are NOT questions yet and must not be bulk-copied here.** The point of the beat is that
each is *looked at* and either cited to a row or written down as a question with its own reason. A
bulk paste would reproduce exactly the batch-clear failure this repo already records
`[[feedback_gated_is_ruling_or_hunt]]` — a list captioned *needs Paul* where a third of the rows
carried no judgement at all.

---

## Entry format

```
### Q<n> · <the question, in one line>
- raised-by: <beat 8 run date> · from <chronicle file:line, or the seat trail>
- the finding: <what was carried>
- why it could not be cited: <the specific row that should exist and does not, or the ambiguity>
- what would close it: <a citation, or Paul's word — say which>
```

⭐ **`why it could not be cited` is the load-bearing field.** *"No row exists"* and *"two rows both
half-cover it and I cannot tell which"* are different problems with different fixes, and a question
that does not distinguish them is a shrug with a heading.
