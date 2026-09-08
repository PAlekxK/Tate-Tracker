# CLOUDFLARE ACCESS ON QA — keep it or drop it, in the context of the whole stack

- row: process · kind: decisions · class: engine · declared · objective: O5
- seats: practice-steward → `2026-09-07-review-gate-to-qa-DESIGN.md` (raised it) ·
         privacy seat → `.engineering/2026-09-03-c6-privacy-seat-review.md:539-547` (ruled on it once
         already, and was overridden the next day)
- depends-on: .plans/2026-09-07-review-gate-to-qa-DESIGN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ Nothing here executes. It is a recommendation with its condition attached.
- stage-note: 2026-09-07 — Paul asked for this *"in the context of our full stack"* while ruling that
  his review gate moves to QA and that **QA must be a mirror of production**. That ruling is what
  makes this decidable: Access is the single largest way QA is not one.

---

## 0 · ✅ RULED AND DONE — 2026-09-07

**Access was DROPPED from QA**, both applications (the apex and the `*.` wildcard covering preview
deploys). ⭐ **The order mattered:** the neutrality condition attached to this recommendation FAILED
first — QA served `<title>Fernwood</title>` — and chasing that found the real cause, `pages-deploy`'s
`HOUSEHOLD` set excluding `qa`. Fixing that also caught a leak I had shipped an hour earlier. Access
came off only once the condition read `rendered=0` against the live origin.

### ⭐ THE FOLLOW-ON RULING — Paul uses his REAL address in QA `[paul-ruled 2026-09-07]`

*"I need my real address in QA to be able to tell whether anything makes sense."* Correct: a fictional
address yields nonsense weather and a nonsense "what grows here", so the walk cannot answer the only
question it exists to answer.

**Measured before agreeing, because the question deserved a number rather than a reassurance:**

| | address in the public build | `whoami` with no grant |
|---|---|---|
| `fernwood-home` (production) | **0** | **404** |
| `fernwood-qa` | **0** | **404** |

⭐ **An address is not in the public bytes of either origin.** It lives in KV behind a grant token; the
other read routes are 401; every unauthenticated endpoint (`feedback`, `door`, `onboarding-metrics`)
is **write-only**. ⛔ **So Access was never what protected an address** — production has been public in
exactly this way the whole time, holding his real address, and nobody had noticed because nothing was
ever exposed.

**What removing Access DID change:** a stranger with the URL can reach QA's **signup form**. That is
an abuse surface — junk accounts on a synthetic estate, visible in `watch-accounts.py` — not a data
leak. Three shapes were put to Paul; he ruled **(3) leave it open**:

1. ⛔ put Access back — closes it, and restores the mirror defect that hid a live production bug from
   QA all evening;
2. ⛔ put Access on production too — they would match, but it changes what a real person meets at the
   front door of a product whose whole open defect cluster is that door;
3. ✅ **leave it** — the estate is synthetic, the build is verified neutral, and a junk signup costs
   nothing and is observable.

⚠️ **The residual, stated rather than glossed:** QA writes real rows, so his address now sits in QA's
KV as well as production's. `reset-production-estate.py --estate est-qa0001` clears it on his word.

---

## 1 · WHAT IS ACTUALLY GATED — measured, not assumed

| surface | status |
|---|---|
| `fernwood-qa.pages.dev` (the app) | 🔒 **302 → Access** |
| `fernwood-qa…workers.dev/health` | 🌐 **200, public** |
| `fernwood-qa…workers.dev/api/feedback` · `/api/door` · `/api/observations` | 🔒 **401** — the Worker's own auth |
| `fernwood-home.pages.dev` (production) | 🌐 **200, public** |
| `fernwood-lab.pages.dev` (dev) | 🌐 **200, public** |

⭐ **THE FIRST THING WORTH KNOWING: Access is on the STATIC SITE ONLY. The QA Worker is public**, and
its data is protected by *its own token auth*, not by Access. So Access is not what keeps QA's records
private — that was true before Access existed and stays true without it.

⭐ **What Access actually protects is the QA app shell** — `viewer.html` built from `instance/qa.json`,
whose identity is **"My Home"** on synthetic estate `est-qa0001`. `measured`: **0 `_qaFixture` markers
at HEAD.**

---

## 2 · ⭐ THE HOLD'S RELEASE CONDITION HAS ARRIVED — nobody wrote it down, so nobody noticed

Access went on **2026-09-04**, one day *after* the privacy seat reviewed this exact fork and marked
**"accept a public QA origin" as RECOMMENDED**, on the grounds that it is *"less machinery, it keeps
agent testing frictionless, and 'the QA fixture contains nothing real' is a rule that can be checked
by reading it, whereas an Access policy is a setting that can be silently changed."*

It was overridden for a **real but time-bounded** reason (`BACKLOG.md:130`): **keep QA away from Mom
while the parallel instance was being built.**

⛔ **THAT REASON HAS EXPIRED, and it is measurable.** Mom does not go to QA. She goes to a new
household — `home` / `est-e6696a` — and `[ruling 3b, 2026-09-07]` she has the link in hand. The thing
Access was protecting her from is no longer where she is pointed.

⚠️ **This is the failure `[[feedback_a_hold_names_the_work_not_the_mechanism]]` describes exactly**: a
hold with no written release condition does not lift when its condition is met. It just persists, and
then gets defended on grounds nobody re-derived.

---

## 3 · THE RECOMMENDATION

> ### ⭐ DROP ACCESS FROM QA. Keep production public. Make the two match.

**Five reasons, in the order they carry weight:**

1. ⭐ **Paul has ruled QA must be a mirror of production.** Access is the single biggest way it is
   not — measured, and it is the defect that made a live production bug invisible in its own mirror.
2. **The reason it went on has expired** (§2), and it was overridden guidance to begin with.
3. **It protects a neutral shell for a synthetic estate.** The records everyone actually cares about
   are behind the Worker's own auth, and stay there either way (`measured`: 401).
4. ⭐ **It removes the last observer outside Access.** All 140 QA walks already arrive
   pre-authorised — so today nothing checks what an unauthenticated arrival meets, at the exact moment
   Paul's review moves to QA and the front-door seam is the biggest open defect.
5. **A rule beats a setting.** *"The QA build contains nothing real"* is checkable by reading. An
   Access policy is a dashboard toggle with no history in this repo.

### ⛔ THE CONDITION, and it is not optional

**Run `check-estate-neutral.py` against the QA ORIGIN — not the export — and have it pass, before
Access comes off.**

⚠️ **Because this exact property has already failed in a way our checker could not see.** On
2026-09-07 Fernwood's own gauge record — *123 days, 30.83", "OUR GAUGE", "the gauge's sheltered spot
by the pond"* — rendered at households in Roswell, Dahlonega and Bangor, and `check-estate-neutral`
read **✅ 311 needles / rendered=0** against the very origin four seats had walked. **It tests for
NAMES. That leak was numbers and possessive pronouns.**

⭐ And CLAUDE.md already records that the bare invocation **does not scan `viewer.html` at all** — the
`--url <origin>` form is the one that does, and *"both are used; neither is optional."*

**So: neutrality is the thing Access is standing in for, and it must be proven by the check before
the backstop is removed.** If it cannot pass, that is the finding, and Access stays until it does.

### ⬜ What I am NOT recommending, and why

**Putting Access on production instead** — the other way to make them match. It is coherent and it is
wrong here: it changes what a real person meets at the front door, in a product whose entire open
defect cluster *is* the front door. Making the mirror match by degrading the thing being mirrored is
not a mirror.

---

## 4 · ⚠️ WHAT THIS RECOMMENDATION COULD GET WRONG

- **`check-estate-neutral` passing is necessary, not sufficient** — by its own recorded failure. A
  green there is evidence about **names**, and about nothing else.
- **CI has no Access token** (`[[reference_fernwood_qa_cloudflare_access]]`), so some CI behaviour
  today is shaped by a gate that would disappear. Nothing was measured about that here.
- **I did not test what an unauthenticated browser actually renders at QA**, because it is gated —
  which is itself the argument: nobody can currently see what a stranger meets there.
