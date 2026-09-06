# DR-Z400S — steering-head connector repair

**2001 Suzuki DR-Z400S "Desert Storm" · `drz400s-2001` · opened 2026-09-06**

Status: **OPEN — connector is depinned, parts not yet ordered.** This file is the procedure
and the log. It exists because the same fault has now been "fixed" once and came back.

---

## Why this exists

Total power loss when turning the bars. Three readings of the same fault in three months,
each one confident, the first two wrong:

| Date | Read as | Fix applied | Held |
|---|---|---|---|
| 2026-06-13 | Broken/fatigued **conductor** in the steering-head flex bundle | none — diagnosis only | n/a |
| 2026-07-03 | **Dirty/loose contacts** | reseat pins, contact cleaner, patch joints, electrical tape | ~8 weeks |
| 2026-09-06 | **Degraded terminals** — plating breached, corrosion regrows | terminals + housings on order | tbd |

The 8-week interval is the tell. Cleaning a terminal whose plating is already breached
resets the clock; it does not stop the corrosion. Steering flex is the **trigger** that
opens a marginal contact, not the cause.

The July entry pre-registered a recurrence watch — *"if the fault ever returns when turning
the bars…"* — and the watch fired. That worked exactly as intended.

---

## ⚠️ The instrument was wrong, and that is why this took three passes

The June diagnosis measured **12.7 V at the green connector** and concluded *"power is good
right up to the steering head."*

**A static voltage reading cannot see a high-resistance joint.** A corroded connection reads
full battery voltage at no current, then collapses the moment the headlight draws. The meter
was telling the truth and the truth was uninformative.

**The right instrument is a voltage-drop test, under load:**

- Key on, headlight burning — current actually flowing.
- Meter **across** the connection, not to ground.
- Want **well under 0.2 V**.
- **Near 0.5 V is a bad joint** even if the circuit currently works.

This is also the **acceptance test** for the repair. Do not close this out on a static
12.7 V reading a second time.

---

## The part

🔬 **Hypothesis, not yet caliper-verified.** Sumitomo-pattern **.090" (2.3 mm)** series.
Bright green housings, Suzuki pattern — a 4-cavity and a 2-position at the steering head.
The circuit is the always-hot main feed (red) plus orange.

**Corroborated negatively 2026-09-06:** Home Depot's smallest crimp terminal is **.250"
(6.3 mm)** — nearly 3× too wide. This is a specialty Japanese motorcycle part; no hardware
store or auto-parts chain stocks it. That negative is real evidence for the 090 family.

⚠️ **Correction:** an earlier read this session guessed a **.250" lock type**. Wrong, on both
the photos and the Home Depot negative. Recorded so the wrong number doesn't resurface.

### Two 30-second checks that settle the order

1. **Calipers on the terminal blade.** ~2.3 mm → 090 confirmed.
   (2.3 = 090 · 2.8 = 110 · 4.8 = 187 · 6.3 = 250 — the **inch name is the anchor**; at least
   one vendor index lists the metric pairings inconsistently, so check against the product photo.)
2. **Sealed or unsealed?** Where the wire enters the back of the housing —
   **rubber grommet → sealed (MT)** · **bare plastic → unsealed (HM)**.

---

## Sourcing

| Vendor | What | Notes |
|---|---|---|
| [Cycle Terminal — .090](https://www.cycleterminal.com/090-connectors.html) | **Start here.** HM + MT 090, 2/3/4/6-pin | Loose terminals: male **$0.18**, female **$0.20**, wire seals **$0.17**. $5.00 order minimum. US. |
| [Eastern Beaver](https://www.easternbeaver.com/Main/Elec__Products/Connectors/connectors.html) | Backup — deepest Japanese-bike catalog | Ships from Japan, slower |
| [Corsa Technic](https://www.corsa-technic.com/category.php?manufacturer_id=44&category_id=110) | Second backup, US | |

**Buy past the ID uncertainty.** At twenty cents a terminal, order both series, both genders,
seals, and complete 2-pin and 4-pin housing sets — under $20 all in, with spares to practice
crimps on. Optimizing the order down to the exact part risks a week of shipping to save $6.

**Skip the Amazon assortment kits** for the repair itself — inconsistent plating on an unfused
always-hot feed. Fine as practice terminals.

### Tool

Standard crimpers **crush** a 2.3 mm open-barrel terminal. Needs an open-barrel crimper:
**Engineer PA-09** (the die Eastern Beaver calls for) or an IWISS equivalent. Order it with
the terminals.

---

## Procedure

### Depinning

1. **Battery negative off.** The red wire is unfused-hot to this connector.
2. **Photograph both faces before anything comes apart** — wire colour per cavity, lock-tab
   orientation. Colours are 25 years faded; a mis-pin is worse than the original fault.
3. **Find the access slot.** Two lock designs exist and the slot tells you which:
   - **Housing lance** (plastic finger in the cavity) — usually released from the **front**.
   - **Terminal lance** (springy metal tang on the terminal) — thin blade **alongside** the
     terminal from the front, flattening the tang.
4. **Check for a secondary lock** — a coloured wedge or hinged flap that comes off *first*.
   A terminal that won't budge is usually this, and forcing it breaks housings.
5. Pick in straight until it stops. **Do not lever it**, and keep pressure off the terminal
   itself — that binds it in the housing.
6. Hold the lock off and **pull the wire gently** from the back. It should slide with almost
   no force. If it doesn't, the pick isn't on the lock.

**Two specific to this bike:** corroded terminals can stay stuck with the lance fully lifted —
that's corrosion binding, not the lock, and forcing it tears the wire off the terminal. And a
bent tang lifts back up with a fine pick, but a **broken housing lance can't be fixed** — that
cavity won't retain and the housing gets replaced.

### Before reassembly — the check that decides whether this works

**Corrosion wicks up the copper strands under the insulation,** sometimes an inch or more,
while the jacket still looks perfect. This is the most likely reason a repair like the July
one comes back.

Strip a half-inch back on each wire pulled. **If the copper isn't bright** — green, dark grey,
dull black — a new terminal alone will not fix it. Cut back until you reach bright copper,
however far that takes, and splice in fresh wire if you run out of slack.

### The repair

- **Crimp the terminal. Do not solder it.** Solder wicks up the strands and creates a hard
  spot right where the wire leaves the terminal — a stress riser, at a flex point. That is how
  the next failure gets manufactured.
  ⚠️ This does **not** reverse the pre-registered solder-splice plan: a splice belongs
  **mid-wire, away from the bend**. The terminal itself gets crimped.
- Replace **every terminal in the connector, both halves.** They shared the same water.
- **Inspect the housing for heat damage** — discoloration, a softened cavity. High resistance
  on an unfused high-current feed makes heat, which accelerates corrosion, which raises
  resistance. A runaway worth catching.
- **Leave a service loop** so flex spreads over a length instead of one point — that is what
  killed it originally. Dielectric grease on the mating faces. Route clear of the steering-head
  stops.
- **Consider a sealed series** if the original is unsealed. A flex point with this bike's water
  history is the textbook case for it.

### While it's apart

Pull the **neighbouring steering-head connectors**. The speedometer entry already flagged them
for the same corrosion, and the speedo itself died of water in this same cluster. The speedo
rebuild is held until this closes — reinstalling it now would put two variables back in play,
which is the exact thing that entry was written to avoid.

---

## Open items

- [ ] Calipers on the terminal — confirm 2.3 mm / 090
- [ ] Sealed vs unsealed determination
- [ ] Order terminals + housings + seals + open-barrel crimper
- [ ] Strip-back check for wicked corrosion on every wire pulled
- [ ] Housing heat-damage inspection
- [ ] Neighbouring steering-head connectors pulled and inspected
- [ ] **Voltage-drop acceptance test under load** (< 0.2 V), then bars lock-to-lock, then horn
      and brake light on the same feed
- [ ] Speedometer rebuild released once the above is green

---

## Sources

- [Cycle Terminal — terminal extraction procedure](https://www.cycleterminal.com/terminal-extraction-procedure.html) — photos and cross-sections
- [Cycle Terminal — motorcycle connectors index](https://www.cycleterminal.com/motorcycle-connectors.html)
- [Cycle Terminal — .090 series](https://www.cycleterminal.com/090-connectors.html) · [HM 090](https://cycleterminal.com/hm-series-090.html) · [MT 090](https://cycleterminal.com/mt-series-090.html)
- [Eastern Beaver — connector catalog](https://www.easternbeaver.com/Main/Elec__Products/Connectors/connectors.html) — 1–1.5 mm jeweller's flat blade releases most of these pins
- [FindPigtails — de-pin / re-pin technique](https://findpigtails.com/automotive-connector-repair/de-pin-re-pin/)
- Video: [Sumitomo HM 090 — assembly & terminal removal](https://www.youtube.com/watch?v=e0T6qRGiHIM) · [Motorcycle Connectors 101](https://www.youtube.com/watch?v=gE-hRjrLuyQ)
- Factory service manual §7 (`manuals/text/drz400s-2001-service.txt`): *"when disconnecting a
  connector, be sure to hold the terminals; do not pull the lead wires"*; *"with a lock-type
  coupler, be sure to release the lock before disconnecting."*
- ThumperTalk DR-Z harness threads — ⛔ per the fleet-cycle rule, take a **question** from a
  forum, never a number.
