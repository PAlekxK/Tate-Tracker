# Blue Thunder — starting-fault diagnosis

**2017 Suzuki DR200S · `dr200s-2017` · opened 2026-08-30**

Status: **OPEN — no test results recorded yet.** This file is the protocol and the log.
Nothing below is a diagnosis until a row in the Results table says so.

---

## Why this exists

"The bike won't start" has already resolved to **three unrelated root causes** in 16 months,
all of them on this same bike, all of them presenting the same way to whoever was standing there:

| Date | Presented as | Actual cause |
|---|---|---|
| 2025-05-09 | won't start | **fuel** — battery was fully charged; degraded gas, drained tank + carb, flushed |
| 2026-07-21 | intermittent no-start | **electrical contacts** — cleaned and reset; "starts immediately" after |
| undated | won't start | **kill switch engaged** |

So the symptom carries no information. The point of this protocol is to make each incident
declare which axis it is on **before** anyone starts turning wrenches.

## ⚠️ CORRECTION 2026-08-30 — THE MANUAL ON DISK IS FOR A DIFFERENT MODEL

**`paul-stated`, standing at the machine: there is NO KICKSTARTER on the DR200S or the DR-Z400S.
Both are electric start only.** An earlier version of this guide built its no-tools discriminator
around kicking her over. That test does not exist. It is replaced below by the jump pack.

**Where it came from, because the cause matters more than the fact.**
`manuals/text/dr200s-2017-service.txt` **is not a DR200S manual.** Its own line 3 reads *"This manual
contains an introductory description on SUZUKI **DR200SE**"* — a different, earlier model that
genuinely does have electric **and** kick. The filename says `dr200s`, and `manuals/INDEX.md` even
names it *"Suzuki **DR200SE** Service Manual"* behind a 🟡 marker. **Nothing was hidden. It was read
past.** The INDEX's own note — *"DR200S unchanged across years"* — answers a question about YEARS
and was read as covering a question about MODELS.

Three specs disagree between that manual and this vehicle's own card, which is what a
different-model document looks like:

| | card (DR200S) | manual (DR200SE) |
|---|---|---|
| stroke | 58.0 mm | 58.2 mm |
| compression | 9.5 : 1 | 9.4 : 1 |
| starter | **electric only** *(Paul-verified at the machine)* | electric **and kick** |

⚠️ **SO EVERY NUMBER IN THIS FILE SOURCED TO THAT MANUAL IS PROVENANCE-DOWNGRADED** — the battery
type, the 13.0–16.0 V charging band, the 150 W generator output, the carburetor I.D. numbers, the
float height, the reserve capacity. They are *probably* right (the two models share the 199 cc engine
and the BST31SS carb) but **none is verified against a DR200S source**, and at least three sibling
specs demonstrably differ. Treat them as `inferred`, not `verified`.

**What survives unharmed, and why it does:** the tests themselves. **13.0–16.0 V at ~5 000 r/min is
generic to any 12 V lead-acid charging system** — a bike reading 12.3 V and sagging is not charging,
whatever the model — and the T1/T2/T4 thresholds are properties of a lead-acid battery, not of this
motorcycle. The carb rule was already written as *read the I.D. stamped on the carb body*, which is
now load-bearing rather than belt-and-braces.

**The rule this produced:** *the filename is the container; the manual's own foreword is the payload.*
Compare `drz400s-2001-service.txt`, which we hold correctly — its foreword names the DR-Z400S and its
spec table reads **"Starter system … Electric"**, agreeing with Paul. The method works when the
document actually is the right one.

## The confound we are actually trying to break

`paul-stated 2026-08-30`: the repeated presentation is **slow, labored crank → then nothing or a
single click**. That sequence is what a 6 Ah battery does under repeated cranking *regardless of
why the engine didn't fire*. It is downstream of both stories:

- **Story A** — she walked up to a battery that was already low (charging system, parasitic
  drain, or a battery at end of life), and the labored crank is the cause of the no-start.
- **Story B** — she walked up to a healthy battery, the engine wouldn't fire for a **fuel**
  reason (low tank, petcock position, flooded from seepage), and the labored crank is the
  *consequence* of her attempts.

By the third attempt the evidence is destroyed — the battery is now low either way. Only two
observations separate the stories, and both must be taken **before the battery is run down**.

---

# PART 1 — SHOP CARD (print this, tape it in the shop)

## If Blue Thunder won't start

**Before you press the button — 20 seconds:**

1. **Kill switch** on RUN (red switch, right handlebar)
2. **Petcock** on **ON** — not RES. Save RES for when ON starves.
3. **Look in the tank.** She has no fuel gauge. Reserve is only 0.7 gal.
4. **Cold?** Choke fully ON, throttle closed.
5. **Read the voltmeter** if one is fitted — write the number down.

**Then: THREE TRIES, FIVE SECONDS EACH. THEN STOP.**

> Suzuki's own limit is 5 seconds of starter at a time — longer overheats the starter motor and
> the harness. Wait 10–15 seconds between tries. A bike that is going to start usually starts on
> the first or second. **Every try past the third flattens the battery and erases the evidence.**

**On the FIRST labored crank — before it gets worse — PUT THE JUMP PACK ON IT.**
The AVAPOW jump starter lives in the kit. Clip it to the battery and try again.

- **Fires on the jump pack** → engine, fuel and spark are all fine. It was purely a charge problem.
- **Still won't fire on the jump pack** → not the battery's cranking power. Fuel or spark.

*(Do this at the first labored crank, not after she's cranked down to a click.)*

**Write down which one it was:**

- ☐ **1** — nothing at all, or a single click
- ☐ **2** — starter spins slowly and labors
- ☐ **3** — starter spins briskly but it never fires
- ☐ **4** — fires and dies

Then stop and call Paul. **Do not keep cranking.**

---

# PART 2 — BENCH TESTS (Paul, with a multimeter)

Every threshold below is from the factory service manual on disk —
`manuals/text/dr200s-2017-service.txt` — not from memory.

**Reference values** — ⚠️ from the **DR200SE** manual (see the correction above), so `inferred` for this bike, not `verified`. The battery/charging thresholds are generic to 12 V lead-acid and stand regardless:

| Item | Spec | Manual |
|---|---|---|
| Battery | **YTX7L-BS**, 12 V 21.6 kC (**6 Ah**)/10 HR | ELECTRICAL spec table |
| Regulated voltage | **13.0 – 16.0 V at 5 000 r/min** | ELECTRICAL spec table |
| Generator max output | 150 W at 5 000 r/min | ELECTRICAL spec table |
| Generator no-load | >60 V AC at 5 000 r/min *(a second table in the same manual says >70 V — tables disagree; treat as ">60 V, confirm before condemning")* | ELECTRICAL spec table ×2 |
| Generator coil resistance | 0.1 – 1.5 Ω | ELECTRICAL spec table |
| Starter relay resistance | 2 – 6 Ω | ELECTRICAL spec table |
| Main fuse | 20 A | ELECTRICAL spec table |
| Spark plug | NGK DR8EA, gap 0.6 – 0.7 mm (0.024 – 0.028 in) | already `verified` in the record |
| Fuel tank / reserve | 12.5 L (3.3 gal) total, **reserve 2.5 L (0.7 gal)** | CAPACITIES |

### T1 — Resting voltage
Charger off at least an hour; overnight is better (sheds surface charge). Meter across the posts.

≥12.6 V full · 12.4 ≈ 75% · 12.2 ≈ 50% · ≤12.0 flat.
Repeated trips below 12.0 permanently sulfate an AGM.

### T2 — Cranking voltage
Meter still on the posts, starter for ~3 s. Should hold above **~10.5 V**.
A *fully charged* battery that collapses below **~9.5 V** cannot deliver current any more —
it is finished, whatever it reads at rest.

### T2b — The crank-down ladder · **the capacity test, using the starter as the load**

**T2 catches a dead battery. T2b catches a DYING one** — and dying is what this bike is behaving
like. `paul-asked 2026-08-30`: *"So does that mean I should be able to turn the bike on, turn it off,
and then turn it back on? How can we kinda test this?"* Yes, and here is the test.

**Why the starter is the right load.** A commercial load test pulls ~3× the amp-hour rating — about
**18 A** here. The starter pulls **60–100 A**. It is a harsher load than a load tester and it is the
one the bike actually sees, so no equipment beats it.

**Setup:** fully charged, charger **off the bike**, rested ≥1 hour. Meter on the posts. Two people —
Mom presses, Paul reads. *(If the meter has **MIN/MAX hold**, use it and one person can do it.)*

**Three cranks, 60 seconds apart. Record the LOWEST voltage each time.**

| | lowest volts during the crank |
|---|---|
| crank 1 | ______ V |
| crank 2 (+60 s) | ______ V |
| crank 3 (+60 s) | ______ V |

**Read the SHAPE, not any single number** — the same rule as T3:

| what you see | what it means |
|---|---|
| all three **≥10.5 V**, within ~0.3 V of each other | battery is fine. The fault is elsewhere. |
| **first one already below ~9.5 V** | it cannot deliver current. **Done — replace it**, no further testing needed. |
| **a descending ladder**, each low meaningfully worse | ⭐ **capacity is gone.** This is the failure the 8/30 three-start hour looked like, made visible in three cranks instead of three weeks. |

The last two are **different failures** — one battery is weak, the other empties fast — which is
exactly why the ladder beats a single reading.

⭐ **IT WORKS EVEN IF SHE FIRES IMMEDIATELY.** The deepest sag happens in the **first half-second**,
on inrush, before the engine has really turned over — so a one-second crank gives almost the same
minimum as a five-second one. Start her, shut her off, wait 60 s, repeat.

⛔ **Do NOT pull the plug cap to stop her firing.** Cranking with an ungrounded cap can take out the
coil or CDI, and there is nothing to gain — see above.

⭐ **THE NO-METER VERSION IS MOM'S, and it is the same test by ear.** Start, shut off, wait a minute,
start, shut off, wait a minute, start. **"Did the third sound the same as the first, or slower?"**
Same → the battery is fine and it is fuel or spark. Slower → the battery, full stop, and stop
cranking. That one sentence is the most useful thing she can give over the phone.

⚠️ **Warm restarts are the EASIEST thing you can ask of a battery** — no choke, warm oil, less
friction. So a bike that degrades across three warm restarts is failing the gentlest version of this
test, which is what makes the 8/30 hour damning rather than ambiguous.

### T3 — Charging voltage · **RUN THIS FIRST** · **TAKE THREE READINGS, NOT ONE**
Meter across the battery. Read it **stopped**, then at **idle**, then holding **~5 000 r/min**.
**Pass = 13.0 – 16.0 V at 5 000 r/min.**

⭐ **Three readings, because one is ambiguous** — from FIELD sweep 1 (a 1998 DR200 owner, quarantined
in `cycle/fleet/FIELD-NOTES.md`): a dead charging system reads *"12.9 volts not running, 12.9–13.0
running."* A single running figure of 12.9 V could be a flat battery mid-charge. **The same figure
stopped AND at 5 000 r/min cannot be anything but a dead charging system.** What you are reading is
whether it *climbs*, not what it says.

⚠️ **Do not read T3 at idle and stop there.** Output rises steeply with rpm; the 150 W figure is at
5 000 r/min and idle is a small fraction of it. A low reading at idle is normal and proves nothing.

- 13.5 – 14.5 → charging system fine; the battery is being replenished. Look elsewhere.
- Sits ~12.3 and sags → **she is not charging at all.** Every ride runs the 6 Ah battery down
  instead of topping it up, and a new battery would die exactly the same way. This single result
  would explain the whole pattern — rode fine yesterday, dead this morning — and it makes the
  "was it low gas or low battery" argument moot.
- Above 16 V → regulator/rectifier failing, and it is *cooking* the battery.

### T4 — Overnight hold
After T3: park level, **petcock OFF**, record the voltage. Next morning, before touching
anything, record it again.
Within ~0.1 V = normal. A drop of 0.3 V or more = parasitic drain or a battery that no longer
holds. T1/T2 say which.

### T5 — Parasitic draw *(only if T4 drops)* — **run it as an A/B now that a charger is in the picture**
Key off, kill switch off. Pull the **negative** cable. Meter **in series** between the
negative post and the cable — never across the two posts, that is a dead short.

⛔ **INSTRUMENT CAVEAT, added 2026-09-01 — THIS TEST CANNOT BE RUN ON THE 10 A RANGE OF THE METER PAUL OWNS.** The meter is an **All-Sun EM830** `[photo-MODEL-READ 2026-09-01]`. Its **10 A** range resolves in ~10 mA steps, and the threshold below is *5–10 mA* — so it would read `0.00`/`0.01` and **look like a valid measurement while being unable to see the answer.** Its 10 A jack is also rated **10 s max every 15 min**, and a draw test needs a sustained read. **Use the `VΩmA` jack on `200m` (0.1 mA) or `20m` (0.01 mA).** *Match the payload, not the container — the same defect class as the manual, and as beat 0's resolver this same day.*

Once on a range that can resolve it: A carbureted bike with no clock should sit at a few **milliamps**.
Take the reading **twice**: (A) charger clips still attached but unpowered, (B) charger clips removed
entirely. **A − B is the charger's contribution, measured rather than argued**; B alone is the bike's
own draw. More than ~5–10 mA on **B** = something is live on the bike. Pull the 20 A main fuse to confirm the side, then
disconnect the **regulator/rectifier** — one shorted diode there is the single most common cause
of a bike battery that keeps going flat overnight.

### T6 — Fuel / spark, on the next failed start (no tools)
- Look under the carb **before** cranking: a drip at the overflow tube = float needle passing.
- Pull the plug: **wet and smelling of gas = flooded** (too much fuel, not too little).
  **Dry = starvation or no spark.**
- Ground the plug against the head, crank, look for a fat blue spark.

---

## How many cranks does she actually have? `[paul-asked 2026-08-30]`

**The arithmetic, then why it lies.** A YTX7L-BS is **6 Ah at the 10-hour rate** — 0.6 A for ten
hours. A 199 cc starter pulls roughly **60–100 A** *(estimate — no manual figure, and our manual is
the wrong model; treat as `inferred`)*. That is ~150× the rate the capacity was measured at, and
capacity collapses under that load (Peukert). Worked out: **~1.7–2.8 Ah usable → 70–110 seconds of
continuous cranking → 25–35 three-second cranks to truly flat.**

**You will never see that number, because the limit is VOLTAGE, not charge.** The starter must spin
the engine fast enough to fire, and that threshold arrives around 50–70% depth of discharge — far
earlier on an old battery whose internal resistance has climbed.

| | 3-second cranks from a full charge |
|---|---|
| **healthy** YTX7L-BS | **~10–20**, with rests, degrading gradually |
| **tired / end-of-life** | **~3–6**, falling off a cliff |

- **Rests genuinely buy cranks.** 10–15 s between attempts lets the chemistry recover. Suzuki's
  5-on/10-off is partly starter heat and partly this.
- **Cranking with no fuel is the expensive case** — the engine never catches, so the starter carries
  full load for the whole three seconds. When she fires after one second, you spent one second.

⭐ **WHY THIS MAKES THE 8/30 THREE-START HOUR MORE DAMNING, NOT LESS.** All three attempts *fired*,
so each cost perhaps 1–2 seconds — **about five seconds of cranking across the whole hour. A healthy
battery would not notice five seconds.** So that episode is not a battery being used up by cranking.
It is either a battery with almost no usable capacity, or one that was **already low when he walked
up** — which is exactly what the unpowered-charger hypothesis predicts. T1 and T2 separate them.

## Should the idle be turned up to help it charge? `[paul-asked 2026-08-30]`

**No, and it would barely help.** Output climbs steeply with rpm — the 150 W figure is at 5 000
r/min, and idle is a small fraction of it while the headlight draws the whole time. Moving 1 500 →
1 800 r/min takes you from *slightly negative* to *slightly less negative*, and costs correct idle
behaviour (gear engagement, creeping, slow return to idle) for nothing.

**Set it to spec for its own sake: 1 500 ± 100 r/min** *(⚠️ DR200SE manual — `inferred`)*.

⭐ **And a stubbornly low idle is a data point for the CARB job, not a thing to dial around.** On a
carbureted bike an idle that keeps wanting to sit low points at the pilot circuit — a partly blocked
pilot jet or a mis-set fuel screw. The DR200's pilot screw is factory **PRE-SET and usually capped**,
and a rebuild kit is already queued for the fall put-away.

**The actual recharge is rpm and time: ride her 20 minutes at 3 000+ r/min.** Nothing done at idle
substitutes for that.

## Two free checks, from FIELD sweep 1 — no meter, no charge spent

Both come from a 2003 DR200 thread (quarantined in `cycle/fleet/FIELD-NOTES.md`).
⚠️ **DR200SE-generation, not this 2017 bike — confirm at the machine.**

1. ~~**Look at what the key can be turned to.**~~ 🔴 **DONE AND FALSIFIED 2026-08-30** — Paul, at the
   machine: *"There's no park mode that I can see. Just on, off, and lock."* No key position on this
   bike can hold a circuit live. ⚠️ **This removes one drain candidate, it does not clear a drain:**
   the always-live side (battery → starter relay → regulator/rectifier) is live whatever the key
   does, and a shorted rectifier diode is the classic bike-battery drain. **Check 2 got more
   valuable, not less.**
2. **The spark test.** Pull the negative cable and **tap it against the post.** A spark with
   everything off means something is live — T5's question answered without a meter. Isolate by
   unplugging one connector at a time and re-tapping.

## Make the invisible variable visible

Nobody fetches a multimeter at the moment of failure, which is why the pre-crank number never
gets taken. Fix it with hardware:

- a **handlebar voltmeter** wired to the ignition circuit (~$10–15), or
- a **Battery Tender pigtail** with a voltmeter plug — worth fitting regardless, because a 150 W
  generator at 5 000 r/min puts very little back during a slow lap of the property, and she is
  ridden in short hops.

Then "I think the battery was low" becomes "it says 12.1" — a number that exists *before* the
first crank, and one Mom can read out over the phone.

## The fact the record is missing

**Battery age.** The record carries no purchase or install date for the YTX7L-BS. There is a date
stamp on the case — go read it. If it is the 2017 original it is ~9 years old against a 3–5 year
AGM life, and it has been deep-cycled repeatedly (June 2026 recommission, the July contact
episode, this week).

⚠️ **Do not replace it before T3.** If the charging system is dead, a new battery just becomes
the next dead battery.

---

# PART 3 — RESULTS LOG

Append a row per incident or test. **An empty row is not a passing test.**

| Date | What | Reading / observation | Symptom # | Verdict |
|---|---|---|---|---|
| 2026-08-30 | Left sitting with a **trickle charger attached but UNPOWERED** | Lost charge. Days elapsed not recorded. ✅ **CHARGER NOW IDENTIFIED 2026-09-01** — **NEXPEAK NC201 PRO**, 12 V/24 V, "7-stage intelligent pulse repair charger", modes STD / AGM-GEL / WET / REPAIR. ⚠️ `[photo-MODEL-READ 2026-09-01, unverified]` — read off Paul's photograph of the unit, not from a purchase record. | — | **Hypothesis, not a verdict.** A charger with no blocking diode back-feeds through its own output stage when unpowered. 20 mA for 3 days = 1.4 Ah of a 6 Ah battery. A smart maintainer draws microamps; a dumb trickle charger often does not. **Read the label.** |
| 2026-08-30 | **Three starts in ~1 hour**, each shut off quickly (t=0, +30 min, +60 min) | Start 1 fine · start 2 fine · start 3 **clearly struggling, barely caught** | 2 | ⭐ **The most informative run so far, because it held FUEL CONSTANT.** The engine fired all three times — fuel, spark and carb are all exonerated for this episode. The only thing that degraded was cranking power, monotonically. **This episode is on the electrical axis.** ⚠️ Partly self-inflicted: see the standing rule below — a short idle run on this bike is a net WITHDRAWAL, so three of them is a discharge test. Still: three starts should not take a healthy 6 Ah battery from fine to barely-turning. |
| 2026-09-01 | ⭐ **CHARGED FULLY, LEFT OVERNIGHT, WOULD NOT START** — Paul, verbal, at fleet lap 2 beat 0 | *"charging the 200 for a good amount and then left it overnight… the battery kind of dimmed and it sounded like I was trying to turn over… it just wound up clicking"*. No meter reading taken before the attempts. | 2 | ⭐ **THIS BREAKS THE RECORD'S OWN PATTERN.** Every prior episode had *charging restores starting*, which is why the record read this as charge STATE. A full charge that does not survive one night is a different claim: the battery is not HOLDING, or something drained it. **This is an uninstrumented T4 failure.** ⚠️ Paul: *"I don't think the bike was plugged into the charger"* — hedged, so the 8/30 back-feed hypothesis is weakened, NOT excluded; T5's A/B settles it by measurement. ⚠️ The clean T4 for this night is GONE — it was cranked repeatedly before any reading. |
| 2026-09-04 | ⭐ **CHARGE CYCLE ON THE NEXPEAK — "empty" → "full" in ~15 MINUTES — then open-circuit decay with the charger ATTACHED BUT UNPOWERED** — Paul, verbal, same day | Charger clipped on; it reported the battery **empty**. Mains on. **~15 minutes later it reported essentially full.** Mains unplugged, **charger left clipped to the battery**; **13.1 V**. Over the next **~1 hour** the reading fell **below 13.0 V** and the charger's own gauge dropped below full. ⚠️ Every value here is **charger-display-reported** unless Paul confirms the 13.1 came off the All-Sun EM830 — a charger's SoC bar is not a state-of-charge measurement. ⚠️ Clock times not recorded. | — *(no start attempted)* | ⭐ **THE 15 MINUTES IS THE FINDING. THE FIRST-HOUR DECAY IS NOT.** ① **A 6 Ah battery cannot go from empty to full in 15 minutes** — that is on the order of 1 Ah delivered at any rate this charger can push. So one of three things is true, and **two of them are the same failure**: the "empty" was a depressed-voltage read on a battery that was never empty; or there is so little usable capacity left that it fills in minutes; or the charger terminated on *terminal voltage*, which a battery with high internal resistance reaches almost instantly. The last two are **capacity / internal resistance** — the T2b *"capacity is gone"* branch, seen for the first time **without cranking the bike**. ② ⛔ **The decay 13.1 → just under 13.0 in an hour is NORMAL surface-charge dissipation and is not evidence of a fault.** A freshly-charged lead-acid/AGM sits at 13.0–13.2 and falls toward its true resting OCV (12.6–12.8 when healthy) over 1–4 hours. **What matters is where it SETTLES, not that it fell.** And the charger "now showing less than full" is *the same observation read off a second display* — not independent corroboration. ③ ⛔ **CONFOUNDED TWICE, AND BOTH ARE INSTRUMENT PROBLEMS, NOT BATTERY ONES.** ⚠️ **`paul-stated 2026-09-04`: every number in this row came off the NEXPEAK's own display, NOT the EM830.** So the protocol's named instrument was never used — *match the payload, not the container*, the same defect class as the manual and as beat 0's resolver. A charger's voltage readout is uncalibrated, typically ±0.1–0.2 V, and its SoC bar is a derived guess sitting on top of that. **AND THE SECOND CONFOUND IS VISIBLE IN THE FIRST:** with mains unplugged, that display was **still lit and still reporting** — which means the charger was **awake and running off the battery it was measuring.** That is not the back-feed hypothesis argued, it is the attached-and-dead draw *observed*, and it is exactly what the standing habit forbids — *"a charger is either POWERED or fully DISCONNECTED — never attached and dead."* ⭐ **BUT DO NOT LET IT EXPLAIN THE AFTERNOON.** Run the arithmetic before assigning blame: even a generous 20–30 mA over 1.5 hours is **~0.04 Ah of a 6 Ah pack, under 1%** — it cannot move the terminal voltage half a volt. **The afternoon's decay is surface charge, essentially all of it.** The draw matters over *nights and days*, not hours: ~0.24 Ah overnight, **~1.4 Ah over three days** — which is the 8/30 episode exactly. **So the charger must come off before T4, and its presence this afternoon is a provenance problem rather than a discharge one.** ④ What it does narrow: **the engine never ran today.** If she is charged, the charger is taken fully off, and she still slides overnight, the fault is the battery or a parasitic drain and the charging system is not the explanation for *that*. ⚠️ **T3 still has to be run before anything is replaced** — a dead charging system would kill a new battery the same way. |

### Incident record so far (from conversation, not yet instrumented)

| Date | What happened | Recorded by |
|---|---|---|
| ~2026-08-28 | Wouldn't start on the charger-fed attempt; fuel found low at the filter, tank filled | Paul, verbal |
| 2026-08-29 | Ran fine, rode it around the property; **left the petcock on RES** | Paul, verbal |
| 2026-08-30 AM | Wouldn't start | Paul, verbal |
| 2026-08-30 | Charged the battery — starts | Paul, verbal |
| prior | Battery pulled and the contacts tightened down | Paul, verbal |

⚠️ These are recalled, not measured. They are here so the pattern is legible, **not** as evidence.

---

## 🧨 TWO WEEKS OF REPAIR MODE HAVE ALREADY BEEN RUN — `paul-stated 2026-09-04`

*"I've put it on repair mode multiple times over the past two weeks, and it's done the pulse
treatment and the sulfurization and all that. I've switched modes up and tried to recharge it. So I
don't think just switching modes will fix the option because I've tried that."*

**He is right, and this retires the fix proposed one section above before it was ever tried.** The
"chronic partial charging on the wrong profile" candidate assumed the AGM profile was *untried*. It
was not. **Mode is not the untested variable.** Struck.

### What this DOES and DOES NOT establish — the two are easy to run together and they are not the same

✅ **The rescue routes are spent.** Repeated desulfation, mode changes and recharges across two weeks
have not changed the behaviour. Whatever is wrong is **not going to be charged out of it.** As a
practical matter that is settled, and it is the part that governs what to do next.

⛔ **But it is NOT proof the battery is unrecoverable, and the reason matters:** *pulse desulfation
is of contested efficacy.* A treatment that may do nothing, doing nothing, is **not a valid negative
test** — it fails to distinguish *"the battery cannot be recovered"* from *"the treatment was inert."*
**Do not let a failed rescue be promoted into a diagnosis.** It removes an option; it does not supply
a finding. *(Same discipline as the manual and the charger display: the container ran, the payload
was never verified.)*

### ⚠️ AND A NEW RISK, POINTING AT THE TREATMENT ITSELF

**Desulfation modes work by applying elevated-voltage pulses** — commonly well above the 13.0–16.0 V
band this file already flags as the point where a regulator is *"cooking the battery."* **A sealed
AGM cannot replace electrolyte it gasses off.** So **two weeks of repeated REPAIR cycles on a sealed
AGM is a candidate CONTRIBUTOR to its decline, not only a failed rescue of it.**

⛔ **Recommendation: stop running REPAIR mode on this battery.** It has had its chances, the upside is
unproven, and the downside is a mechanism this file already names elsewhere. ⚠️ Hypothesis, not a
verdict — nothing here is measured, and the pulse voltage of this unit is unknown.

### ⭐⭐ THE QUESTION IS NOT WHICH MODE. IT IS **HOW LONG.**

Every charge in this record terminates fast — *"pretty much full after 15 minutes."* **If it declares
full in fifteen minutes in EVERY mode, then mode was never the variable, and the fast termination is
a PROPERTY OF THE BATTERY rather than a setting on the charger.** A pack whose terminal voltage jumps
to the cutoff almost immediately is describing **high internal resistance** — which is the same thing
the settled 12.60 hints at, arrived at from a second direction.

👤 **The one open question worth Paul's memory:** *across all those attempts, did any single charge
ever run for HOURS rather than minutes?* Not which mode — **how long.** If the honest answer is that
none of them ever ran long, **this battery has never once been full in this record's memory**, and
that is a finding rather than an oversight.

## 🔁 THE CHARGER WAS IN **STD** MODE — `paul-stated 2026-09-04` — and it reframes the day

**It was never on AGM/GEL.** A 6 Ah sealed AGM was charged on the STANDARD (car) profile. Three
consequences, and the first is a **retraction of this file's own reasoning from earlier today.**

### ⚠️ RETRACTION — "it cannot be a real charge in 15 minutes" was overstated

That claim was written assuming a maintainer-rate current. **On a car profile it does not hold.**
If STD pushes several amps, 15 minutes is on the order of **1–2 Ah**, which into a 6 Ah battery
sitting part-full is a substantial and entirely legitimate slug of charge.

**What survives, and it is narrower:** *no* lead-acid battery reaches genuine **full** in 15 minutes
at any current, because the absorption phase is **chemistry-limited, not current-limited** — it takes
hours whatever you feed it. So the charger did not lie about *charging*; it lied about **"full."** It
terminated at the end of **bulk**, which lands a lead-acid battery around **80%**.

⭐⭐ **AND THAT RECONCILES THE WHOLE DAY WITHOUT A DYING BATTERY.** Bulk termination ≈ 80%, settling
to a resting **12.60 ≈ 75%**, is a *coherent and innocent* story. **The 15-minute charge stops being
evidence of lost capacity and becomes evidence of an interrupted charge.** ⛔ **It does not clear the
battery either** — it removes a witness, it does not supply an alibi. **We now have no clean reading
of what this battery can hold, because it has not been properly filled.**

### The risk running the other way — STD on an AGM is not neutral

- **Rate.** The rule of thumb is 10–30% of capacity: **0.6–1.8 A for a 6 Ah battery.** A car-mode
  current well above that heats a small AGM and costs it life. ⚠️ **The NC201 Pro's per-mode current
  is NOT known to this record — read it off the unit or its manual.** It decides the arithmetic above.
- **Profile.** A flooded/STD stage set can run absorption higher than an AGM wants, and a
  flooded **equalisation** stage is genuinely damaging to a sealed battery, which cannot replace
  gassed-off electrolyte. *(Whether STD on this unit equalises is unknown — same question, same place.)*

### ⭐ SO THE ROOT-CAUSE LIST GAINS A FOURTH CANDIDATE, AND IT IS THE ONLY ONE THAT EXPLAINS EVERYTHING

The record's three prior causes were **fuel**, **contacts**, **kill switch** — each explained one
incident and none explained the pattern. This one explains the pattern:

> **CHRONIC PARTIAL CHARGING.** Every charge terminates at ~80% on the wrong profile → the battery
> is never actually filled → progressive **sulfation** → capacity falls → *charging restores starting*
> (a partial charge is plenty for a day or two) → **and then it fades again.** Self-reinforcing, and it
> matches every episode in this file including the 9/01 overnight failure.

**Its falsifier is cheap and is the next test:** give her one *genuine* full charge on the right
profile and see where she settles. **12.8–12.9 V rested = the battery was never the problem, it was
the charging of it.** Still ~12.6 after a proper full charge = the capacity really is gone, and now we
know it rather than suspect it. *(The NC201 Pro's REPAIR/desulfation mode exists for exactly this
failure — worth a look **after** the honest baseline, never before it, or it corrupts the reading.)*

### 🔎 The NAPA question is ASKED AND UNANSWERED — do not re-ask it

`paul-stated 2026-09-04: "I don't know about number two."` The 2025-10-10 NAPA battery core stays
**unassigned**, now with three candidates instead of two (F-150, GTI, **and this bike**). Recorded so
a later pass does not spend Paul's attention on a question he has already declined to answer from
memory. **A receipt or an order number is the only thing that closes it now** — not another ask.

### ✅ WHAT THE OPEN-WINDOW LIST BELOW STILL GETS RIGHT, AND THE ONE PLACE IT IS NOW WRONG

Steps 1–3 are **done**: charger off, and a settled **12.60 V** on the EM830 at 18:09:36. Step 2's
label read is **with Paul** *(`paul-stated`: "I'll get number one")*.

⛔ **But the list says T2b next, and that is now the wrong order.** T2b's own written precondition is
*"fully charged, charger off the bike, rested ≥1 hour"* — **and we have just established she is at
about 75%, not fully charged.** A crank ladder run at 75% cannot separate *"capacity is gone"* from
*"it simply was not full,"* which is the exact confusion this whole file exists to break. Running it
now would burn the charge and produce an uninterpretable result.

⚠️ **This reverses the "do not recharge" instruction given earlier today, and the reversal is the
point, not a contradiction.** That instruction was correct while the voltage was still falling — the
settled number was the thing at risk, and it was taken. **We have it. The question has moved.**

**THE ORDER NOW — ⚠️ SUPERSEDED THE SAME DAY, see the box below. Kept because the reasoning still
holds and only the priority changed.**

1. ~~**Recharge on `AGM/GEL`**~~ — **STRUCK: already tried** (`paul-stated`, see the REPAIR MODE
   section above). Mode is not the untested variable.
2. **Let it run for HOURS, and do not believe an early "full."** ⭐ **This half SURVIVES and is now
   the open question** — bulk ends ~80%, absorption is what actually fills it and cannot be hurried.
   Note the time on and the time off.
3. **Charger fully OFF, rest ≥1 hour — overnight better.** EM830 on the posts. ≥12.8 V = the battery
   was never the problem; still ~12.6 = the capacity is gone, measured rather than suspected.
4. **T4 comes free** if it rests overnight — read it again before touching anything.
5. **THEN T2b**, from a genuinely full battery, where its ladder finally means something.
6. **T3** while she is running.

---

# 🎯 STOP TREATING THE BATTERY. RUN T3. — the standing next action as of 2026-09-04 evening

**T3 has been called "the decisive test" and "the next test to run" since 2026-08-30, and across five
days and three sessions it still has not been run.** Everything else has been.

⭐⭐ **T3 IS THE ONLY TEST IN THIS FILE WHOSE VALIDITY DOES NOT DEPEND ON THE BATTERY'S CONDITION.**
T1, T2b and T4 all ask *"how good is this battery?"* and every one of them has been confounded today
by not knowing how full it was. **T3 asks a different question — is the bike putting charge back? —
and a 75%-charged battery answers it exactly as well as a new one would.** That is why it keeps
coming out on top however the battery evidence moves, and it is why it should have been first.

**And it is the only test whose result changes what you BUY.**

| T3 result | what it means | what to do |
|---|---|---|
| **13.0–16.0 V at ~5 000 r/min** | charging system is fine | the battery is the fault. **Replace it** — the evidence is already sufficient and the rescue routes are spent. |
| **~12.3 V, no climb from stopped → 5 000** | **she is not charging at all** | ⛔ **do not buy a battery yet** — a new one dies exactly the same way. Fix the charging system first. This single result explains the entire record. |
| **above 16 V** | regulator/rectifier failing | it has been **cooking** the battery — which would also explain why an AGM aged out early. Fix before replacing. |

**⏱ RUN IT NOW, WHILE SHE STILL HAS THE CHARGE TO START.** She is at ~75%, which started her three
times on 8/30. Every day spent treating the battery spends that margin — and if she gets too flat to
start, T3 becomes hard to run at all.

**How, in one pass:**
1. Meter on the posts, **20 V DC**, and leave it clipped there.
2. ⭐ **Set MIN/MAX hold if the EM830 has it** — then you can rev with both hands and read the peak
   afterwards, instead of needing a second person.
3. Read **stopped** → write it down. Start her, read at **idle** → write it down. Hold **~5 000 r/min**
   for a few seconds → write it down. **Three numbers. What you are reading is whether it CLIMBS.**
4. Then **ride her 20 minutes at 3 000+ r/min** — the only thing that actually puts charge back, and
   it doubles as the recharge the next test wants.


---

# 🔎 THE BATTERY CAME OUT AND WAS PHOTOGRAPHED — 2026-09-05 10:10–10:11 ET

**Five photographs, EXIF-stamped, taken deliberately to settle the identification.** In-situ label
shot at 10:10:29, battery out and in hand 10:11:21 → 10:11:30.

## ✅ IDENTIFICATION CLOSED — and the record's part number was never this battery's

**The label, read off a legible high-resolution photograph of the battery in Paul's hand:**

> **XTREME** · AGM TECHNOLOGY · **`XTAX7L-BS` · 12V · 6AH** · POWER SPORT BATTERY
> *Distributed by / Distribuido cerca* **Ascent Battery Supply, LLC**, 1325 Walnut Ridge Drive,
> Hartland, Wisconsin 53029 · 1-888-9 ASCENT · **© 2019 Batteries Plus, LLC**

⭐ **This corroborates the 2026-09-04 `[photo-MODEL-READ, UNVERIFIED]` from a SECOND, independent
photograph** — a different day, a different angle, the battery out of the bike and held to the
camera on purpose. Two legible reads agreeing is materially stronger than one. **Paul's one-word
yes promotes it to `paul-verified`; until then it stands as a corroborated photo read.**

**What it settles:** the record says `YTX7L-BS` on the vehicle card, in this guide and in the open
item. **`YTX7L-BS` is the SIZE SPEC — the JIS group — not this battery's part number.** Nothing in
the record was wrong about the *fitment*; it was wrong to read a group designation as an identity.
*(The same container/payload confusion as the manual and as beat 0's resolver. Third instance.)*

## ⛔ AND IT FALSIFIES A FORUM CLAIM THE SAME DAY IT WAS RAISED

Research this morning surfaced a forum post asserting **Xtreme is made by East Penn/Deka** — a
tier-C note, and it was carried as a question rather than a fact, per the FIELD-beat rule.

**The back panel says `Made in Vietnam · Hecho en Vietnam`.** East Penn is Pennsylvania. **The
claim is dead, killed by direct observation of the object in under three hours.** ⭐ This is the
quarantine rule working exactly as designed: *a forum may send you to look; it may never tell you
what you will find.*

## ⭐⭐ AND THE BACK PANEL CONFIRMS IT IS A DRY-CHARGE BATTERY, IN ITS OWN WORDS

The retailer listing said *"Dry Charge AGM."* That was a third-party page. **The battery itself
now says the same thing:**

> *"See owner's manual for proper disposal of **acid container**… Follow **preparation
> instructions** carefully. Do not tip. **Keep vent caps tight and level.**"*

**That is activation language.** It shipped dry and was filled with acid at a counter.

⭐ **WHY THIS MATTERS MORE THAN THE BRAND TIER.** A dry-charge battery requires an **initial
charge after filling** — typically hours at low current — or it never reaches full capacity and
sulfates from the start. Counters routinely fill and hand over. **If that is what happened here,
this battery was capacity-limited on day one**, and it explains the whole file without needing a
second fault: the 15-minute charge termination, the settle at ~12.60, the monotonic crank
degradation, and this guide's own line that *the battery has never had a genuine full charge in
this record's memory.*

⚠️ **Hypothesis, and it is falsifiable by a question, not a measurement:** does Paul remember it
being filled at the counter, or did it come sealed in a box?

## ⭐ THE MOLDED CASE CODE — `LE010824-V`

Molded into the case side, read at 4× on a contrast-stretched crop, unambiguous.

**Reading, offered as a hypothesis:** `LE01` plant/mold code · **`0824` = August 2024** ·
`V` = Vietnam, matching the back panel.

⛔ **IT IS A CASE DATE, NOT AN ACTIVATION DATE**, and the difference matters. What it gives is a
**FLOOR, and the floor is the useful part: the battery cannot be older than its case.** If the
reading is right, **this battery is at most ~13 months old.**

⭐⭐ **THAT RETIRES THE LAST OF THE AGE ARGUMENT, AND IT MAKES THE FAILURE WORSE, NOT BETTER.** The
open item's original reasoning — *"if it is the 2017 original it is ~9 years old against a 3–5
year AGM life"* — was already reasoning from a false premise once the replacement was spotted on
09-04. It is now dead twice over. **An AGM that is roughly one year old and behaving like this has
no age explanation at all**, which pushes the weight onto activation, charging profile, or the
charging system.

## 🎯 THE ACTION THIS CREATES, AND IT COMES BEFORE BUYING ANYTHING

**`© Batteries Plus` + `Ascent Battery Supply` means the purchase happened at a Batteries Plus**,
and the nearest is **store #969, 3640 Marietta Hwy Ste 200, Canton GA 30114 · (770) 609-3111**
(the other is Woodstock #859, 9820 Hwy 92).

**Batteries Plus keeps purchase history against a phone number.** One call answers two things this
record has been unable to answer by any other means:

1. 📅 **The exact purchase/activation date** — *"The fact the record is missing"* section above has
   been open since 08-30 and asks for exactly this. A receipt closes it outright, and it is the
   only thing that ever could: **an order number, not another ask.**
2. 💵 **Whether the 12-month free-replacement warranty is still live.** ⚠️ The 12-month term is
   from a third-party listing and is **unverified for this SKU** — but if the case date is right
   and it was activated in late 2024 or later, **this may be a free replacement.**

⚠️ **AND IF IT IS UNDER WARRANTY, THE STORE TEST SHOULD HAPPEN THERE**, not at an auto-parts
counter — a warranty claim wants their own tester's verdict on their own paperwork.

⛔ **NONE OF THIS UNBLOCKS T3.** Whatever battery goes in, free or bought, the charging system is
still unmeasured and still the only thing that decides whether the new one survives.

---

# ✅ RULING — REPLACE IT. `paul-decided 2026-09-05`, and the record supports him.

**Paul: *"I think at this point I want to just replace it… look at the full battery diagnosis
history and tell me whether that doesn't make sense."*** It makes sense. This section is the
audit he asked for, including the one hole that remains and the cheap way to close it.

## FIVE INDEPENDENT LINES, AND THEY ALL LAND ON THE SAME MECHANISM

| # | evidence | date | what it indicts |
|---|---|---|---|
| 1 | **Three warm restarts, monotonic degradation** — fine · fine · barely caught | 08-30 | cranking power, and it held fuel constant |
| 2 | **"Empty" → "full" in ~15 minutes** on the bench charger | 09-04 | terminal voltage reached almost instantly = **high internal resistance** |
| 3 | **Settles at ~12.60 after every "full"** | 09-04 | never actually filled, or cannot hold a fill |
| 4 | **12.55 rested → 9.41 under crank, then clicking** | 09-05 | cannot deliver current |
| 5 | ⭐ **T4 PASSES (−0.09 V/12 h) AND SHE STILL WON'T START** | 09-05 | **holds voltage, cannot supply current** |

⭐⭐ **LINE 5 IS THE ONE THAT CLOSES IT, AND IT ONLY EXISTS AS OF TODAY.** Every earlier reading
was ambiguous between *charge state* and *capacity*. A battery that **holds its voltage overnight
within 0.09 V** and then **collapses to 9.41 V under load** has separated those two for the first
time: **the charge is there and the current is not.** That is the textbook signature of high
internal resistance, and it is the same mechanism lines 2 and 3 arrived at from the bench.

⭐ **IT ALSO RESOLVES THE 09-01 CONTRADICTION.** That row reads *"charged fully, left overnight,
would not start"* and was recorded as **the record breaking its own pattern** — a battery that
does not hold. **Today's measured overnight hold contradicts that reading.** The battery held on
09-01 too; it simply could not start the bike. *"It didn't hold"* was an inference from a failed
start, taken with no meter. **The measurement wins, and the mechanism is one thing, not two.**

## ⭐ AND TWO OF THE FIVE ARE ALTERNATOR-INDEPENDENT — WHICH IS WHY THE T3 GATE NO LONGER BLOCKS

**Lines 2 and 4 were both taken with the engine off.** The 15-minute charge termination happened
on a **mains charger**; the 9.41 collapse was a load test from a **known resting voltage**. The
state of the charging system cannot explain either one. **So the battery is condemned on evidence
that does not depend on T3, and running T3 first would not change the verdict on the battery.**

## ⛔ BUT THE GATE'S REAL ARGUMENT SURVIVES — IT IS JUST NOT AN ARGUMENT FOR WAITING

The gate never said *"the battery might be fine."* It said: **a dead charging system would kill a
new battery the same way**, and that is still true. The 09-04 **CHRONIC PARTIAL CHARGING**
candidate — the only one that explains the whole pattern — is untested and remains untested.

⭐⭐ **WHAT CHANGED IS THE DIRECTION OF THE BLOCK, AND THIS IS THE WHOLE RULING.** The gate was
written on 09-04 when *she could still start* and buying was speculative. **Both halves inverted
overnight:**

- **Then:** T3 was free (she started), a battery was a guess → *test first, then buy.*
- **Now:** she will not start, so T3 needs a jump pack and a careful unclip → **the battery is the
  cheapest way to un-block T3.** A new battery makes the decisive test trivial to run.

**So the ORDER reverses and the GATE does not disappear:**

> ### 🎯 BUY THE BATTERY. RUN T3 ON THE FIRST RIDE, NOT "SOON."
>
> The exposure from being wrong is **weeks of slow drain, not one ride** — and T3 takes five
> minutes with an engine that runs. Running it the same day the new battery goes in costs nothing
> and closes the last candidate. **A new battery that is never followed by T3 is the failure this
> gate was written to prevent, and it is now the only way to reach it.**

## ⚠️ THE ONE HONEST HOLE, AND IT CLOSES FOR FREE ON THE WAY TO THE STORE

**This battery has never had a genuine full charge in this record's memory.** Every charge
terminated at the end of bulk (~80%), so *"the capacity is gone"* has never been measured from a
truly full state. That hole is real and it is the only thing that could still surprise us.

⭐ **TAKE THE OLD BATTERY WITH YOU.** Every major parts counter runs a free conductance test and a
free charge. It costs one trip you are already making, and it buys three things this record
cannot otherwise get:

1. **A measured CCA against the rating** — a *number*, not five converging inferences. Tell them
   12 V 6 Ah AGM powersports, ~100 CCA.
2. **A free charge on a proper charger**, which closes the never-actually-full hole — and if they
   hand it back reading **12.8–12.9 V rested**, that is the 09-04 falsifier firing and the only
   result that should stop the purchase.
3. 👁 **The label read.** `XTAX7L-BS` vs the record's `YTX7L-BS` is still `[photo-MODEL-READ,
   UNVERIFIED]`. The battery will be in your hands — settle it in ten seconds.

⚠️ **This does NOT overturn this file's own line that the starter is a harsher load than a
commercial tester.** It is still 18 A against 60–100 A. **A conductance tester is not being used
as a better load test — it is being used as an INSTRUMENT**, reporting internal resistance
directly, which is the exact quantity all five lines above infer. Different question, and the one
that has never been measured. ⛔ **A "GOOD" verdict from it does not clear the battery** against
five converging lines and a 9.41 V collapse; it would mean *stop and think*, not *stand down*.

## WHAT TO BUY, AND THE TWO HABITS THAT COME WITH IT

- **Size:** `YTX7L-BS` / `XTAX7L-BS` — 12 V, 6 Ah, sealed AGM. Mainstream, shelf stock. **Read the
  spec off the old case, do not order off this file.**
- ⛔ **Charge it on the AGM/GEL profile, never STD.** The 09-04 finding stands: a 6 Ah sealed AGM
  was being charged on the car profile. Rate wants **0.6–1.8 A**, not car-mode current.
- ⛔ **Never run REPAIR/desulfation mode on the new one.** Two weeks of elevated-voltage pulses on
  a sealed AGM is a *candidate contributor* to the old one's decline, not just a failed rescue.
- ⛔ **A charger is POWERED or FULLY DISCONNECTED — never attached and dead.** That is the measured
  ~20 mA path: 0.24 Ah overnight, **1.4 Ah over three days**, which is the 08-30 episode exactly.
- ⭐ **Fit the Battery Tender pigtail with a voltmeter plug** while the battery is out. It makes
  the pre-crank number exist for the first time, and it is a number Mom can read over the phone.

## ⛔ AND THE FALSIFIER, PRE-REGISTERED BEFORE THE PART IS FITTED

**If she still will not start on a brand-new, properly-charged battery, the fault was never the
battery** — and the axis moves to the starter, the relay, the main fuse or the wiring. Writing
that down now is what stops a new battery from being read as a diagnosis. **A part that fixes it
is evidence; a part that does not must be allowed to say so.**

---

# 📉 THE WINDOW CLOSED, AND IT CLOSED ON A MEASUREMENT — 2026-09-05, fleet lap 3

**Three meter photographs, timestamps read deterministically from EXIF (`DateTimeOriginal`,
offset −04:00), so the SEQUENCE is not a model read even where the digits are.**

| # | ET timestamp | reading | provenance | what it is |
|---|---|---|---|---|
| 1 | **2026-09-04 21:07:13** | **12.64 V** | `[photo-MODEL-READ, UNVERIFIED]` | rested, charger off — 3h after the 18:09:36 settled 12.60 |
| 2 | **2026-09-05 09:46:19** | **12.55 V** | `[photo-MODEL-READ, UNVERIFIED]` | rested, next morning, before the first crank |
| 3 | **2026-09-05 09:46:32** | **9.41 V** | ⭐ **`paul-stated`** — he gave the figure in words | **13 seconds later**, on/just after a start attempt: *"it seemed to not have enough energy and then start clicking"* |

## ✅ T4 — RUN, UNPLANNED, AND IT PASSES

**12.64 → 12.55 over 12 h 39 m = −0.09 V.** T4's own band is *"within ~0.1 V = normal; a drop of
0.3 V or more = parasitic drain or a battery that no longer holds."*

⭐ **So the battery HOLDS ITS CHARGE OVERNIGHT, and there is no parasitic drain.** That is the first
clean, in-band result this file has ever recorded, and it **retires T5** unless something else
resurfaces it. It also kills a candidate: *"something is live on the bike draining it"* is now
measured false, not merely unlikely.

⚠️ **Two limits, stated rather than smoothed over.** (a) T4's written precondition is *"after T3,
park level, petcock OFF"* — T3 was never run and the petcock state that night is not recorded, so
this is a valid overnight-hold measurement taken outside the protocol's frame, not a protocol-clean
T4. (b) Both endpoints are digits read off a photograph. **The DELTA is what carries the finding,
and a consistent misread of the same display would preserve it** — but Paul confirming the two
numbers is a ten-second job that would promote this from inferred to verified.

## ⛔ AND THE SAME MORNING, THE OTHER HALF: SHE COLLAPSED TO 9.41 V AND CLICKED

**T2's threshold, quoted from this file:** *"Should hold above ~10.5 V. A fully charged battery that
collapses below ~9.5 V cannot deliver current any more — it is finished, whatever it reads at rest."*

**T2b's ladder table, first row:** *"first one already below ~9.5 V → it cannot deliver current.
Done — replace it, no further testing needed."*

**9.41 is below both.** And the clicking is the corroborating symptom, not a second opinion: a
starter relay that chatters instead of pulling in is the signature of a supply that cannot hold up
under inrush.

### ⚠️ THE ONE THING THAT STOPS THIS BEING A VERDICT, and it is the protocol's own caveat

**Both thresholds are written for a FULLY CHARGED battery, and she was at ~12.55 V ≈ 78%.** This is
the exact confusion the whole file exists to break — *"capacity is gone"* vs *"it simply was not
full."* Lap 2's own reasoning struck a T2b run for precisely this reason.

**But the asymmetry has flipped, and that is the new thing.** At 75% you cannot conclude the battery
is fine from a good number — a partial charge flatters nothing. **A 78%-charged battery collapsing
to 9.41 V is not flattered by anything.** It is a floor, not a ceiling: a fuller battery would have
done better, so the true capacity is *at least* this bad. The reading is weak evidence FOR the
battery and strong evidence AGAINST it, and it points the same way as the settled-12.60 /
fast-termination / high-internal-resistance reasoning from 9/04 — a third independent direction
arriving at the same place.

### 👤 THE QUESTION THAT DECIDES HOW HARD THIS LANDS — one sentence from Paul

**Was the 9.41 V read WITH THE STARTER BUTTON HELD DOWN, or AFTER releasing it?** The photographs
are 13 seconds apart and both readings answer different questions:

- **Under load (button held)** → this is a textbook **T2 crank reading**, below the 9.5 V floor.
  Bad, expected, and interpretable.
- **After release, still sitting at 9.41** → **far worse.** A battery that does not spring back
  toward its resting voltage within seconds of the load coming off has essentially no charge
  acceptance left, and the ~12.55 that preceded it was surface charge sitting on a pack that cannot
  deliver. That reading would end the investigation on the battery axis by itself.

⛔ **Not guessed. Recorded as open.**

## 🎯 WHAT THIS CHANGES — T3 IS STILL THE TEST, AND IT IS STILL RUNNABLE TODAY

**The 9/04 warning came true:** *"RUN IT NOW, WHILE SHE STILL HAS THE CHARGE TO START… if she gets
too flat to start, T3 becomes hard to run at all."* She is now too flat to start. **The open window
is closed.**

⭐ **But T3 is NOT lost, because the AVAPOW jump starter is in the kit** (this file's own no-tools
discriminator is built on it). T3 asks *"is the bike putting charge back?"* — a question about the
**alternator**, not the battery — so how the engine got running is irrelevant to the answer.

**The procedure, with the one step that would otherwise ruin the reading:**

1. Clip the AVAPOW on. Start her.
2. ⛔ **TAKE THE JUMP PACK OFF before reading anything.** With it clipped on, the meter across the
   battery reads the jump pack's output, not the bike's charging system — **a plausible number that
   answers the wrong question.** *(Match the payload, not the container.)*
3. Meter on the posts, 20 V DC. Read **stopped** (she is already running, so take this as the
   pre-start 12.55) → **idle** → **~5 000 r/min held a few seconds**. Three numbers.
4. **What you are reading is whether it CLIMBS.**
5. Then ride her 20 minutes at 3 000+ r/min — the only thing that actually puts charge back.

⚠️ **AND THE JUMP-PACK START IS ITSELF A FREE TEST**, per this file's line 102: **fires on the jump
pack → engine, fuel and spark are all fine, it was purely a charge problem.** Still won't fire →
the fault was never the battery's cranking power. Either way the answer is worth having before
anything is bought.

## 💵 THE PURCHASE GATE IS UNCHANGED AND IT IS THE WHOLE POINT

**T3's result table decides what to buy, and nothing measured today moves it:**

| T3 at ~5 000 r/min | verdict | buy |
|---|---|---|
| **13.0–16.0 V** | charging system fine → the battery is the fault, and the rescue routes are spent | ✅ **buy the battery** |
| **~12.3 V, no climb** | she is not charging at all | ⛔ **DO NOT buy a battery** — a new one dies exactly the same way |
| **above 16 V** | regulator/rectifier cooking the battery | ⛔ **fix first** — it would also explain an AGM aging out early |

⛔ **So: do not buy a battery on today's trip on the strength of the 9.41 alone.** Today's readings
make the battery look bad — they do **not** establish that the battery is the *cause*, and the
middle row of that table is the one where buying now wastes the money twice.

---

## ⏱ OPEN WINDOW — 2026-09-04, and it closes when the charge does

**The battery is charged and off mains RIGHT NOW.** That is the precondition every bench test in
this file has been waiting on for five days, and it is the cleanest one this record has ever had:
nothing has been cranked, so no evidence has been destroyed yet. **T3 has never been measured and
this guide calls it decisive.** The order below is deliberate — each step preserves the next.

1. **Unmate the charger completely** (SAE connector apart, or clips off). Do not leave it attached
   and dead — that is the confound, and it is also the standing habit. *(30 seconds. Do this first
   even if you do nothing else — every reading after it is clean, and every reading before it isn't.)*
2. ⭐⭐ **THE BATTERY IS NOT THE ONE THE RECORD THINKS IT IS — and that kills the open item's premise.**
   `[photo-MODEL-READ 2026-09-04, UNVERIFIED]` The label in photo `51AB05F2…` reads **XTREME · 12V ·
   AGM TECHNOLOGY · XTAX7L-BS · 12V 6AH**. The record says **YTX7L-BS** everywhere — on the vehicle
   card, in this guide, in the open item. An **XTAX7L-BS is an aftermarket Xtreme AGM**, the
   size-and-rating equivalent of a YTX7L-BS, **not** what Suzuki would have shipped in 2017 (that
   would be a Yuasa).

   **So this battery is a REPLACEMENT, and the open item's whole argument — *"if it is the 2017
   original it is ~9 years old against a 3–5 year AGM life"* — is reasoning from a false premise.**
   It is newer than 2017. How much newer is still unknown, and it matters more now, not less: an
   aftermarket AGM that is only a year or two old and already behaving like this is a *worse* sign
   than a nine-year-old original, because age stops being the explanation.

   ⚠️ **This is a model read off a photograph and is a hypothesis until Paul confirms it** — the same
   gate the NEXPEAK identification went through on 9/01. **Two ways to close it, and the second is
   better than the case stamp:**
   - 👁 **Look at the label** and read the part number back. Ten seconds, and it settles the identity.
   - 🔎 **Find the purchase.** A replacement battery was *bought*, so a dated receipt exists somewhere.
     **SEARCHED 2026-09-04, and the local registers do not have it:** zero matches for *Xtreme* /
     *XTAX7L* in `.private/service-records/`, nothing in `AMAZON-PARTS.md`, nothing battery-shaped in
     `EMAIL-RECEIPTS.md`, and `dr200s-2017/EXTRACTED.md` has no battery row at all. ⚠️ **That absence
     is not evidence** — those registers are known wrong in both directions and clear an order only
     with an order number. **Unswept, not empty.** The next place to look is Gmail/Amazon directly.

   ⭐⭐ **AND THERE IS ONE LIVE LEAD, SITTING IN ANOTHER VEHICLE'S FILE.**
   `.private/service-records/bronco-1989/EYEBALL-VERDICTS.md` #01 closed a split receipt — **NAPA
   Canton, 2025-10-10** — where Paul ruled *"I got the windshield wipers at Napa for the bronco.
   **Battery not for bronco.**"* It left an explicit, unresolved residual: *"the battery core belongs
   to something… the other 1989-era candidates that day are the F-150 or the GTI. Left unassigned
   rather than guessed."*

   **THE DR200S WAS NEVER ON THAT CANDIDATE LIST** — the residual only ever considered cars. A
   motorcycle battery bought in **October 2025** would also sit correctly against this bike's own
   note that she was *"recommissioned ~June 2026 after sitting… the battery stored off the bike."*

   ⛔ **THIS IS A QUESTION, NOT AN ANSWER — and it is filed as one on purpose** (the loop's own rule:
   *never take a number, take a question*). Nothing here says the NAPA core was Blue Thunder's. What
   it does is add a **third candidate to a two-candidate residual**, and hand Paul one question that
   could close a dangling thread in the Bronco file and date this battery in the same breath:
   **"the battery core you traded at NAPA on 2025-10-10 — was that the 200's?"**
   - Still worth doing while you are in there: **look for a date stamp** on the case anyway.
3. **T1, on the meter, not the charger.** EM830, red lead in `VΩmA`, dial to **20 V DC (`—`)**, probes
   on the posts. Write the number **and the time**. Then again in ~2 hours. ≥12.6 full · 12.4 ≈ 75% ·
   12.2 ≈ 50% · ≤12.0 flat. **Where it settles is the answer; the fall on the way there is not.**

   | time (ET) | reading | instrument | note |
   |---|---|---|---|
   | ~15:1x | **13.1 V** | 🟡 NEXPEAK display | mains just unplugged, charger still clipped on and awake |
   | ~16:2x | **12.6 V** | 🟡 NEXPEAK display | Paul, verbal — *"it's down to 12.6"* |
   | **18:08:16** | **12.6 V** | 🟡 NEXPEAK display | last reading before unplugging · photo `664E1ED4-92E1-4476-831C-ED831C5828AB` |
   | **18:09:36** | **12.60 V** | ✅ **All-Sun EM830** | **charger disconnected** · photo `51AB05F2-C34A-4A52-9106-6C1D07E9244C` |

   *(Times are EXIF `DateTimeOriginal`, offset −04:00, read off the two photographs — deterministic,
   not recalled. 80 seconds apart, charger first.)*

   ⭐⭐ **TWO RESULTS, AND THE FIRST ONE RETIRES A WARNING THIS FILE HAS BEEN CARRYING.**

   **① THE NEXPEAK'S VOLTMETER IS GOOD.** Charger display **12.6**, meter **12.60**, eighty seconds
   apart on the same battery. So the 🔴 provenance downgrade written into the 9/04 row is **too harsh
   for the voltage figure** and is corrected to 🟡: the 13.1 V may be read as a real measurement.
   ⚠️ **This clears the voltmeter ONLY.** Its **state-of-charge bar is a separate instrument** and is
   still ungraded — a derived guess, not a measurement, and the *"full in 15 minutes"* claim came from
   *that*, not from the voltage.

   **② IT HAS SETTLED, AND IT SETTLED LOW.** 12.6 at ~16:2x and **still 12.6 at 18:08** — about
   **1¾ hours flat.** The decay is over; 13.1 → 12.6 was surface charge shedding exactly as predicted,
   and this is now a **settled open-circuit voltage** rather than a number in motion.
   ⚠️ *Flat to the display's resolution* — the NEXPEAK shows one decimal, so it cannot see movement
   below ~0.05 V. The EM830's two decimals can, and 12.60 is the first reading that could.
   ⭐ **A settled 12.60 on an AGM is roughly 75%, not full.** So a battery the charger called *full*
   three hours ago has come to rest at about three-quarters — **it never actually reached full**,
   which is precisely what a 15-minute termination predicts. **This is a soft fail, not a hard one:**
   12.60 is a serviceable resting voltage and would start most bikes. It does not condemn the battery
   and it does not clear it. **Voltage still is not capacity — T2b is still the test.**

   ⭐ **12.6 IS A CEILING, NOT AN ANSWER — it was still falling when it was read.** A settled OCV is
   the number that *stops moving* (1–4 h, longer to be strict), so the true resting figure is **at or
   below** this. ⚠️ **And the T1 ladder above is the generic flooded scale.** A **YTX7L-BS is AGM**,
   and AGM rests **higher** — full is ~**12.8–12.9 V**, and **12.6 on an AGM is roughly 75%**, not
   100%. So a freshly-charged AGM that lands on 12.6 *and is still sliding* is a soft pass at best.
   ⛔ **AND VOLTAGE IS NOT CAPACITY.** A battery with high internal resistance can show a perfectly
   respectable resting voltage and still collapse the instant the starter loads it — which is
   precisely what the 15-minute "full" charge predicts, and precisely what T1 cannot see. **A good
   T1 does not clear this battery. Only T2b does.**

4. **T2b — three cranks, 60 s apart, lowest volts each.** Start / shut off / wait / repeat. Use MIN/MAX
   hold if the meter has it. All three ≥10.5 and within ~0.3 V = the battery is fine, look elsewhere.
   A descending ladder = **capacity is gone**, which is what the 15-minute charge already hints at.
   *(No meter, no helper? The by-ear version is the same test: "did the third sound like the first?")*
5. **T3, straight off the third crank while she is running — THE decisive one.** Meter still on the
   posts. Read **stopped**, then **idle**, then holding **~5 000 r/min**. Pass = **13.0–16.0 V at
   5 000**. Same figure stopped *and* at 5 000 = the charging system is dead, and that single result
   explains the entire pattern and moots the battery argument.
6. **Then ride her 20 minutes at 3 000+ r/min** — not an idle, which is a net withdrawal.
7. **T4 tonight.** Park level, **petcock OFF**, charger fully off the battery, record volts + time.
   Read again in the morning **before touching anything**. ≤0.1 V = normal · ≥0.3 V = drain or a
   battery that no longer holds. **This is the reading 9/01 lost** by being cranked before anyone read it.

⚠️ **Do not buy a battery on today's evidence.** The 15-minute charge is a strong hint and it is
still a charger's own display talking. T3 first — a dead charging system kills the replacement the
same way it killed this one.

## What would close this

- **T3 out of spec** → charging-system fault. Everything else is downstream. Closes it.
- **T3 in spec + T4 drops + T5 shows draw** → parasitic drain; isolate to a circuit.
- **T3 in spec + T4 drops + T5 clean** → battery is end-of-life. Replace the YTX7L-BS.
- **T1 ≥12.4 at the moment of a real no-start** → it was never the battery. Go to T6.

## Standing habits, regardless of outcome

- **Petcock OFF whenever she is parked.** Her own recorded technique is that she weeps fuel at a
  lean. If the float needle is passing, ON *or* RES feeds that overnight and you get a flooded
  cylinder in the morning — which looks identical to a battery problem once someone has cranked
  it flat trying. Petcock off removes that whole branch from the experiment.
- **Petcock ON, not RES,** when riding. RES is 0.7 gal with no gauge behind it.
- Three attempts, five seconds each, then stop. ⭐ **AND THIS RULE NEVER PROTECTED THE BATTERY**
  `[paul-derived 2026-08-30]` — three 5-second cranks is 15 seconds, about **20% depth of discharge**
  on a healthy YTX7L-BS, which shrugs it off without the cranking speed audibly drooping. The
  **5 seconds** protects the *starter motor* (Suzuki's thermal limit) and the **three** protects the
  *evidence*. So the rule doubles as a test: **if she cannot do three five-second attempts without
  visibly weakening, that IS the diagnosis** — see T2b.
- ⭐ **DO NOT SHORT-CYCLE HER — a brief idle run is a net WITHDRAWAL** (added 2026-08-30, from the
  three-start hour above). The headlight is on whenever the engine runs, and the generator makes its
  150 W at **5 000 r/min** — far less at idle. Starting, idling a minute and shutting off spends a
  large slug of amp-hours on the starter and returns almost none, so starting her "just to check on
  her" flattens the battery *and* corrupts the next measurement. If you want to run her, **ride her at
  3 000+ r/min for 20 minutes** — that is the only thing that puts charge back.
- **A charger is either POWERED or fully DISCONNECTED — never attached and dead.** To leave the
  pigtail on the bike, keep the ring terminals bolted to the battery and **unmate the SAE
  connector**: bare wire with nothing plugged into it cannot draw anything.

## Related

- Carburetor refurbish at the next decommission — see `restoration` on `dr200s-2017` in
  `vehicles.json`. A rebuild kit replaces the float needle and seat, which would close the
  seepage/flooding branch of T6 outright.
- Technique already on file: *"She weeps fuel when parked at a steep lean — park her level"*
  (`provenAt` 2026-07-27). Its falsifier stands: **weeping on level ground, or at only a mild
  lean, means the bowl level is riding high** — check float height (13.0 ± 1.0 mm) and the float
  needle seat.
