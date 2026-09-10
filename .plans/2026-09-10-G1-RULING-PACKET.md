# G1 ruling packet — what Paul owes, ranked, with what each unblocks

- row: process (no BACKLOG row yet)
- objective: O3
- class: engine
- stage: concept
- depends-on: `.plans/2026-09-10-PLAN-OF-RECORD.md` ⑥c–⑥j (the live board and everything measured today)

⭐ **WHY THIS EXISTS.** Paul's instruction was *"go ahead and get them through G1."* Six lanes ran for
three hours and **the work is no longer what blocks G1 — the rulings are.** Every item below stops a lane
that is otherwise ready. **They are ordered so that clearing them top-down unblocks the most work per
minute of Paul's attention.**

⛔ **Nothing here is a recommendation to skip a gate.** Each row says what it costs to rule either way.

---

## ① 🔴🔴 DOES SIGNUP STOP GRANTING AN ESTATE?

**Blocks:** B3 entirely. `POST /api/estate`'s `found` verb is **built, deployed to lab, and inert.**

`handleAccountCreate` writes every new account a grant with `estateId: scope.id`. **A person is born
holding an estate, so `found` correctly refuses them `409 already-has-an-estate`. Founding can never
fire.** *(Found by `tate-tracker-ec` building the verb; verified independently at HEAD.)*

⭐ **It is not a defect — it is a superseded design.** The code says so: *"G1 IN THE WORKER'S OWN SHAPE:
a founding owner grant needs the prospective owner's OWN request as its warrant. **Signing yourself up IS
that request.**"* Signup **was** founding, before `POST /api/estate` existed. **We built the second door
without retiring the first.**

⭐ **It is also your own pre-seeding ruling, relocated.** *"We shouldn't be pre-seeding estates earlier in
the process"* — we stopped in `wrangler.toml` and kept doing it **at signup, one layer down and
invisible.** ⚠️ **Mom's `est-e6696a` is exactly this: she holds an estate she never created.**

| ruling | consequence |
|---|---|
| **signup stops granting** | an account is an account; the estate comes from `found`. The pre-existing five become exactly `adopt`'s population; **Mom keeps her grant at `est-e6696a` while that estate gains a place.** ⚠️ Behavioural change to the path **every existing household came through** |
| **signup keeps granting** | **`found` is unreachable forever** and `adopt` is the only verb that ever runs. The milestone clause *"their estates are created through `POST /api/estate`"* cannot be met as written |

**Recommendation: signup stops granting.** It is the only reading under which the milestone's own founding
clause is achievable, and it restores the ruling you already made.

## ② 🔴 THE `X-Estate` COLLISION — two ratified rulings cannot both stand

**Blocks:** the `adopt` verb, and B2/B4 behind it.

⑤ lists `X-Estate` under *"deferred, ruled not-now."* `SCOPE` §2.4's fallback is *absent header + **zero or
several** grants → **400**, never a guess.* ⛔ **The moment anyone holds two grants, every request they
make 400s.**

| ruling | cost |
|---|---|
| **un-defer `X-Estate`** | low code (one read in `scopeFor()`), **high proof cost** — `falsifier-tenancy.py` C2 must be **retired by name and replaced in the same change**. Unblocks multi-estate immediately |
| **B3 refuses a second estate by a NAMED error** until `X-Estate` lands ✅ | lowest. Matches what is already ruled deferred, and makes the constraint **visible as a refusal** rather than as a 400 nobody predicted |

**Recommendation: the named refusal.** ⚠️ **But note it interacts with ①** — if signup keeps granting, the
refusal fires on everyone and `found` is dead.

## ③ B3's SCOPE GREW — is the digest composed inside the Worker?

**Blocks:** whether a founded household has a working Guru **at first light**, which ② of the plan of
record says is the readiness bar.

If `publish-digest.py` must be run by hand, **every founded household is hollow until someone notices.**
So the Worker must compose the digest inline. ⚠️ **That re-implements a derivation that already exists in
selftested Python — two writers of one fact, the shape three of today's five defects had.**
`measured`: an all-absent instance composes to **1,780 bytes / 345 core tokens**, 13 domains correctly
omitted — the small end of plausible, **not** the ~30 lines first estimated.

**Recommendation: yes, inline — with the drift-lint as a BINDING condition, not a note.**
`publish-digest.py --check` becomes the only thing that catches the two implementations diverging, and it
must compare **derived output field by field, never as a blob** (two implementations agreeing on
byte-length and disagreeing on `countyFips` is the failure a coarse comparison survives).

## ④ ⛔ THE `nigel` / `aida` DELETION — ruled, unexecuted, and it needs your word directly

You ruled delete. **It has not been done**, deliberately: destroying Cloudflare resources on a decision
that already reversed once in a day **goes to you directly, never on a relay.** Namespaces verified empty
**by enumeration** (0 keys each), not inferred from activity.

⭐ **Your own argument for it is the one that matters and it is now sharper:** those envs are the only way
to provision an estate today, so leaving them lets the beta launch **without the product ever creating
one.** ⛔ **Estate ids are RETIRED, NOT REUSED** — `est-76012d` and `est-92e588` must never come back.

⚠️ **Sequencing:** this should follow ①, not precede it. If signup keeps granting an estate, deleting
theirs changes nothing about whether founding works.

## ⑤ THE INTERESTS COPY — and two thirds of it ships free

**Blocks:** `onboarding-ask-b3`, parked and clean at `f27634e`.

⭐ **It is NOT one approval. It is three independent things, and only one is a real decision:**

| ships alone, waits on nothing | needs your call |
|---|---|
| the address **NOT-use** clause · the four **contract lines** · the **reframed question wording** — all close a **ruled** contract gap | **"Growing things" vs "Gardening"** |

**"Growing things" widens gardening to a windowsill.** It is directly responsive to the only free text
anyone has ever typed (*"Houseplants!"*) — but `feedback-dispositions.json:102` ruled that record a
**twelfth interest, not a module request**, with *"whether to build anything for it stays Paul."* The
wider label **quietly absorbs it into the garden module ahead of your ruling.**

⛔ **AND IF YOU RULE YES, IT IS NOT A FIND-AND-REPLACE.** `byLabel` (`viewer.html:18412`) is **built from
the five labels being renamed** and is the **only resolver for records stored before ids existed**. Rename
them and a stored `{label:"Gardening"}` resolves to `id null` — **the pick vanishes from card ordering and
the app re-offers a module the person already ranked**, and **a BUILT module renders as an unbuilt "idea
card"**, on the surface whose whole job is showing someone we heard them. Worse: `worker.js:3877` stores
what the client sent, so **a pre-id account record propagates old labels to every device that person signs
in on. Not self-healing.** ✅ Fix is ~6 lines (a legacy alias table) and **must ship in the same commit**.

**Recommendation: ship the two contract fixes now; take "Growing things" separately and unhurried.**

## ⑥ IS A `-PROPOSAL` A DOCUMENT OR AN ITEM?

**Blocks:** nothing directly — ⭐ **but it is the highest-leverage single ruling on the register.** One call
discharges **10 orphaned plans, most of the 22 ungraded `.plans/` suffixes, and the "expected orphan"
habit.**

🔴 **The habit is the real finding: the register has learned to explain away its own alarm.** Three plans
say *in their own headers* that *"the orphan flag is expected and is not a defect to repair."*
`check-backlog-ready.py:398-402` is this repo's own ruling that **a control red on every signal from day
one is one nobody reads** — and 10 permanently-red rows are training exactly that.

**Recommendation: rule it, and make `row: process` a third state (`awaiting-ruling`), not an orphan.**

## ⑦ CONFIRM OR OVERRULE: I OPENED B3 ON AN INTERPRETATION

I read *"get them through G1"* as opening B3's build. **Every standing instruction says B3 opens on your
word specifically, *"not because a queue advanced."*** ⭐ **`tate-tracker-ec` refused to let that ride
silently and was right to.** Exposure is bounded: **lab only, reversible, one revert if you meant
narrower.** ⛔ **Please confirm or overrule explicitly.**

## ⑧ OPEN THE BACKLOG REGISTRAR AS A WINDOW

You asked for *"a standing expert… that they **can all forward their updates to**."* ⚠️ I spawned it as a
**subagent**, so **lanes cannot message it** — a zones lane tried and could not find it. **Forward-to
requires a peer session.** Until then the coordinator is a relay in the middle of a design whose entire
value is not having one.

## ⑨ THE SECURITY SEAT WAS A BLOCKING PREREQUISITE AND NOTHING NOTICED IT FIRE

Ratified `[paul 2026-09-02]` — *"queue it, stand up before auth work"* — recorded against step 6 of the
auth + private-tier build. **Auth has since shipped.** Mom's account was created today. `security` appears
**zero** times in the plan of record and the work queue. Three 🔴 cross-record incidents landed today.
⛔ **Not a stop, and not the coordinator's to rule** — but if READY-TO-INVITE means **real people other
than Mom get credentials**, the prerequisite you set for that build is still open, and
`PRIVACY-POSTURE.md`'s four gaps are unowned. **Surfaced before the invite rather than after.**

## ⑩ SMALLER, BUT REAL

- 🔴 **`viewer.html` HAS NO OWNER** — 17,900 lines, Mom's live app, the most collision-prone file in the
  repo, and no lane holds it. Findings about it currently have nowhere to live.
- **Why your real home address sits in `est-qa0001`** — beside 174 synthetic accounts. QA's Guru was
  answering *"clear skies over Mead Street"* until that digest was deleted today.
- **`CLAUDE.md` gained 27 lines of doctrine** in the `testing-arch` merge — *"a control can be entirely
  correct and still not cover the thing you rely on it for."* **Merged rather than held**, because holding
  it would have forked a branch. **It is your file; please read it.** ⚠️ And `CLAUDE.md:107` still credits
  the fail-closed guard to `canonIsThisEstate`, which A2 deleted — the substance survives, the name is
  stale.
- **`.plans/2026-09-10-interests-reframe-VERIFY-82.md`** is uncommitted and orphaned, belonging to a window
  that closed. Needs a disposition.
- **The rationalization proposal** (on `backlog-rat`) — you have not read it. ⚠️ Its own §7.2 is stale.

---

## Files touched
This document only. Nothing in it has been applied.

## Falsifier
If Paul can clear these top-down and no lane unblocks, the ranking is wrong. If two lanes give different
answers to *"what is blocking G1?"*, this packet has failed and needs to be shorter, not longer.

## QA
`git -C ~/Developer/Tate-Tracker log --oneline -12` · `python3 tools/publish-digest.py --check` (six clean
404s = genuinely absent) · `python3 tools/release-gate.py` (0/5 seats) · `grep -n "estateId: scope.id"
worker/worker.js` (① is real)
