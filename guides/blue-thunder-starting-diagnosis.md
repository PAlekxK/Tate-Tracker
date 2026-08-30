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
Key off, kill switch off. Pull the **negative** cable. Meter on **10 A DC** in series between the
negative post and the cable. A carbureted bike with no clock should sit at a few **milliamps**.
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

1. **Look at what the key can be turned to.** A park / accessory detent that holds the tail light
   live is a parasitic drain that flattens a 6 Ah battery over days. If this bike has one and it has
   been left there, that alone explains *"left it sitting and it lost charge."*
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
| 2026-08-30 | Left sitting with a **trickle charger attached but UNPOWERED** | Lost charge. Days elapsed and charger make/model not yet recorded | — | **Hypothesis, not a verdict.** A charger with no blocking diode back-feeds through its own output stage when unpowered. 20 mA for 3 days = 1.4 Ah of a 6 Ah battery. A smart maintainer draws microamps; a dumb trickle charger often does not. **Read the label.** |
| 2026-08-30 | **Three starts in ~1 hour**, each shut off quickly (t=0, +30 min, +60 min) | Start 1 fine · start 2 fine · start 3 **clearly struggling, barely caught** | 2 | ⭐ **The most informative run so far, because it held FUEL CONSTANT.** The engine fired all three times — fuel, spark and carb are all exonerated for this episode. The only thing that degraded was cranking power, monotonically. **This episode is on the electrical axis.** ⚠️ Partly self-inflicted: see the standing rule below — a short idle run on this bike is a net WITHDRAWAL, so three of them is a discharge test. Still: three starts should not take a healthy 6 Ah battery from fine to barely-turning. |

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
- Three attempts, five seconds each, then stop.
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
