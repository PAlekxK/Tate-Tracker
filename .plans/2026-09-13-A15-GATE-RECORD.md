# A15 — THE GATE BEFORE ROW B · ✅ **PASSED** at `9b7e4ba5`, 2026-09-13

<!-- The record of one RUN, not a standing claim. Re-run `tools/falsifier-tenancy.py` at any later
     candidate sha; this file is evidence about the sha it names and about no other. -->

## 1 · The verdict

**`python3 tools/falsifier-tenancy.py` — exit 0, 10 of 10 clauses ✅, no clause UNPROVEN.**

Run against the **deployed** Worker at dev (`/health` → `build_sha 9b7e4ba5` = HEAD, clean, `env=dev`,
`est-lab0001`), not against a working tree.

```
✅ P1  estate A's credential resolves to A — 200 est-lab0001
✅ P2  estate B's credential resolves to B — 200 est-lab0002
✅ C1  a route with no grant behind it → 404 with no estate named
✅ C2  A cannot NAME B — 4 surface(s) probed, none answered as B
✅ C2b a two-house credential naming B is answered as B — 200
✅ C2c the SAME credential naming no house → 200 and it named no estate
✅ C2d naming an estate it does not hold → 200 and it named no estate
✅ C3  B's credential is B's own row, not A's
✅ C4  a FOREIGN administrator invite confers NOTHING — 201, estates=[], conferred=None
✅ C5  the foreign invite SURVIVES unspent at its own estate — 200 est-lab0002
```

**The claim it falsifies, in the plan's own words, is not restated here** — read it at the top of
`tools/falsifier-tenancy.py`. A second copy of a security clause is a second clause.

⭐ **P1/P2 ARE PRECONDITIONS AND THEY ARE GREEN, WHICH IS WHY THE REST MEANS ANYTHING.** The trap the
tool was built against is that estate B reads nothing of estate A's *because estate B cannot read
anything* — green by absence, and it would have certified isolation the code did not implement.
Estate B resolves to **itself** (200, `est-lab0002`) before any isolation clause is read.

## 2 · ⛔ WHAT THIS DOES NOT CLEAR — read this before citing the pass

- **A15 IS NOT A14.** A14 has two clauses and **its second is RED**: `check-scope-sites.py` reports
  **20 unclassified** sites. They do not substitute for each other — ① is behaviour at a live
  deployment, ② is source — and the plan says so in those words. See §3.
- **It is MECHANISM, never EXPERIENCE.** Every credential here is a fixture driven by curl. Nobody
  has signed in at a browser and seen two houses on a shelf.
- **It is dev, and dev binds one estate id.** The second estate exists only because the fixture
  minted it. Nothing here is a statement about qa, home, production or legacy.
- **The fixture is torn down.** This record is not re-derivable from dev's KV after the fact — it is
  re-derivable by running `--setup` again, which is the point of keeping the run scripted.
- It says nothing about whether a **converted** site resolves the RIGHT grant in code that this run
  did not exercise. Three converted B-CACHE sites exist; **one** (`/api/drought`) was exercised
  end-to-end. `/api/airnow` and `/api/today-line` answer 503 at dev before building a key.

## 3 · ⛔⛔ THE GATE IS NOT FULLY OPEN, AND THE BLOCKER IS THE PLAN, NOT THE BUILD

`8·2` rules that **row B comes after A15 passes**. A15 has passed. **A14 has not**, and A14 is the
step that stands immediately before it.

`check-scope-sites.py` at `9b7e4ba5`: **28 converted · 10 declared · 20 UNCLASSIFIED.**

| where | sites | why it is not a declaration anyone may write today |
|---|---|---|
| `fetch(dispatcher)` | 13 | mixed class in one "function". Four of them (`:5116 :5118 :5153 :5178`) are **sequenced later by the code itself** — `worker.js:5110` says read-only handlers convert FIRST and **writers LAST**, because `assertScope` catches a forgotten conversion and never a wrong one, and those four "stay on the binding until the writers' slice." The rest are the account/session layer |
| `handleZoneAudio` | 4 | pre-auth capture |
| `handleFeedback` | 2 | pre-auth capture |
| `handleEstateFound` | 1 | pre-auth capture |

⭐ **ROW A CONTAINS NO WRITERS' SLICE.** So A14's second clause is **unreachable within row A as
written** — not through anyone's omission, but because the work it demands is in a slice the row does
not contain. Either the gate's condition or the row's scope is mis-specified. **That is Paul's call.**

⛔ **AND THE ONE THING THAT MUST NOT HAPPEN TO IT.** The clause can be turned green in ten minutes by
declaring the twenty sites in `worker/scope-sites.json`. That would make `check-scope-sites.py`
certify the **opposite of the truth** on the one gate standing in front of a real household's record
— and the register's own `_declared_note` forbids it by name: *"a site awaiting a later slice must
stay UNCLASSIFIED — declaring it would launder PENDING into BY DESIGN, the instrument would read
green, and the pass that owed the work would skip it because the tool said it was handled."*
**A gate that cannot pass honestly today is information, not an obstacle.**

## 4 · How to reproduce, and what it costs

```bash
python3 tools/falsifier-tenancy.py --setup      # 14 rows at dev, every one stamped _falsifier:true
python3 tools/falsifier-tenancy.py              # A15 — the gate
python3 tools/migration-rehearsal.py            # A14 — both clauses, reported separately
python3 tools/falsifier-tenancy.py --teardown   # removes exactly those 14, by the fixture's own record
```

⚠️ `--setup` refuses any environment but dev and proves the destination before writing. `--teardown`
deletes **by the fixture file's record, never by pattern** — including the A6 person-keyed edges,
which a hash-keyed sweep would leave behind as a fixture person holding a house forever.

⚠️ Running the clauses emits `door_failed` records at dev with reason `unknown-or-other-estate`. That
is the Worker **correctly refusing a foreign grant** and is expected noise, not a finding.
