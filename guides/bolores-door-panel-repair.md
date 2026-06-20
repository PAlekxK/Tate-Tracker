# Bolores — Driver Door Panel Repair Guide

*1989 Ford Bronco Eddie Bauer · chestnut interior · driver-side door panel, cracked through with broken clip mounts*

The goal: structurally sound panel that mounts solidly (no rattle — this is what gates the audio build), with the visible face cleaned up and color-matched. Repair-in-place is the plan; sourcing a replacement panel is the fallback if the repair doesn't hold.

> **One teardown, three jobs.** Pulling this panel is also when you (1) diagnose the driver door **power lock** — meter the switch → actuator, prime suspect is the door-jamb boot wiring — and (2) prep for eventual **soundproofing + subs**. Do them as one session so you only open the door once.

---

## STEP 0 — The material check (do this FIRST, before buying any adhesive)

**Everything downstream depends on what the panel is actually made of.** The chemicals that bond ABS will *not* bond polypropylene, and vice-versa. Don't buy the adhesive system until you've confirmed the substrate.

**Find the recycling stamp** — a small triangle with letters, molded into the **back** of the panel:

| Stamp | Material | Bonds easily? |
|---|---|---|
| `>ABS<` | ABS | ✅ Yes — best case. Solvent-welds *and* epoxies. |
| `>PP<` | Polypropylene | ⚠️ No — needs special primer/adhesive (see PP column below). |
| `>PE<` / `>HDPE<` | Polyethylene | ⚠️ No — same problem as PP (low surface energy). |
| `>PVC<` | PVC | Bonds with PVC cement; epoxy OK. |
| No stamp | unknown | Run the two tests below. |

**If there's no stamp, two quick tests:**
1. **Float test** — drop a small shaving in water. **Floats = PP or PE** (the hard-to-bond ones). **Sinks = ABS** (or PVC). PP/PE are less dense than water; ABS is denser.
2. **Acetone test** — dab acetone on a hidden spot and wait ~30 sec. **Gets tacky / softens / dulls = ABS** (acetone attacks it — which is exactly why acetone welds it). **No effect = PP/PE.**

**→ Write the result here once you know it:** `Substrate = __________`

---

## STEP 1 — Materials & shopping list

### Buy now (needed regardless of substrate)
- [ ] **ABS sheet stock** — 1/16" (0.06") for contoured backing patches, plus a little 1/8" for rebuilding clip mounts. Black is fine (it's all hidden). *(Even if the panel turns out to be PP, ABS sheet is still the backing material — you just change the adhesive.)*
- [ ] **Heat gun** — to form the ABS backing to the panel's contour. *(You have one.)*
- [ ] **Plastic trim / door-panel removal tools** — the forked nylon pry tools, so you pull the panel without snapping *more* clips.
- [ ] **Door-panel retainer clip kit** — Bronco / F-series ('87–91) push-in panel clips. Cheap; replace them all while you're in there.
- [ ] **Degreaser** — isopropyl alcohol (90%+) and/or acetone, plus clean rags. *Non-negotiable: nothing bonds to years of skin oil + Armor-All.*
- [ ] **Sandpaper** — 80/120/220 grit (scuff for adhesion + knock down repairs) and 320/400 for finish.
- [ ] **Nitrile gloves, mixing sticks, plastic spreaders, painter's tape, clamps / spring clamps.**
- [ ] **Flexible filler for the show face** — automotive flexible plastic repair (e.g., 3M Flexible Parts Repair, or SEM Bumper/Flexible filler). *Not* rigid Bondo on a flexing panel.

### Buy AFTER the Step 0 material check (substrate-specific bonding)

| Application | If panel is **ABS** | If panel is **PP / PE** |
|---|---|---|
| **Back-side structural bond** (ABS sheet → panel) | **Acetone or MEK solvent weld** (chemically fuses ABS-to-ABS — strongest), *and/or* **JB Weld** (2-part epoxy) as reinforcement. Belt + suspenders: solvent-weld, then epoxy the edges. | **Plastic welding with PP rod** (melt PP-to-PP — the real fix), **or** a low-surface-energy adhesive **+ its primer**: e.g. **Loctite 401 + 770 Polyolefin Primer**, or a **3M adhesion promoter + flexible repair**, or a **methacrylate (MMA / Plexus)** adhesive rated for PP. Plain epoxy will *not* hold. |
| **Crack fill — hidden back** | JB Weld (rigid is fine where it doesn't flex) | PP-rated structural adhesive (same as above) |
| **Crack fill — visible front face** | **Flexible** plastic filler, then sand + color-match | **Flexible** plastic filler rated for PP (e.g. with adhesion promoter), then color-match |
| **Color match** | Chestnut interior dye / SEM Color Coat (vinyl & plastic adhesion paint), or a matched interior trim paint | same |

> **Why flexible on the front:** a door panel flexes every time you lean on it or close the door. Rigid epoxy at a crack edge telegraphs and re-cracks. Structure comes from the *back*; the front is cosmetic and wants to move a little.

---

## STEP 2 — The repair sequence

1. **Remove the panel.** Window crank / handle hardware off first, then work the perimeter clips with the nylon tools. Note which clips are broken vs. which pockets are broken — different fixes (Step 4).
2. **Fix the lock wiring while it's off.** (See the power-lock restoration item — meter switch → actuator, suspect the jamb-boot wiring.) Easiest with the panel out of the way.
3. **Degrease everything.** Both faces, every bond area. Isopropyl/acetone until the rag comes away clean. Let it flash off.
4. **Scuff the bond areas** with 80–120 grit so the adhesive has tooth. Wipe again.
5. **Back-reinforce the cracks.** Cut ABS sheet to span each crack with overlap. Warm it with the heat gun and press it to the panel's contour — *keep the gun moving* so it conforms without bubbling/scorching; hold until cool or it springs back. Bond per the Step-1 table for your substrate.
6. **Rebuild the clip mounts** (Step 4).
7. **Fill the front face** with flexible filler, sand 220 → 320 → 400, then **color-match** the chestnut.
8. **Reinstall** with the new clip kit. Confirm it sits tight with no rattle — that's the bar that unblocks soundproofing + subs.

---

## STEP 3 — (covered in sequence above)

## STEP 4 — The broken clip pockets / bosses

These are **not** the dash bezel's screw bosses — different geometry, different load — so we're not reusing that exact heat-shrink trick. A panel clip pocket is a flat slotted/"doghouse" mount that a push-in clip snaps *through*, and it sees a pull-out load when you tug the panel off. Approaches to try (decide hands-on once you see what's left of each pocket):

- **If only the clip is broken, not the panel pocket** → just use the new clip kit. Done.
- **If the pocket/tab is torn off the panel** → fabricate a replacement mount from the 1/8" ABS: cut a backing plate with a correctly-sized slot/hole for the clip, then bond it to the panel (substrate-appropriate adhesive from the Step-1 table) so the new plate carries the pull-out load across a wide glued area, not a single weak point. A fender washer behind the slot can spread the load further.
- **If a whole section of edge is gone** → back it with a heat-formed ABS strip first (Step 2.5), then build the new pocket onto *that*, so you're mounting to fresh material.

The principle: spread the load over a **large bonded area** of fresh ABS rather than trusting the original cracked plastic at a point.

---

## Cautions

- **Acetone is the ABS test *and* the ABS weld — but it also attacks the show-face finish.** Keep it to the back / hidden areas and the hidden bond lines.
- **Heat gun on ABS:** form, don't cook. Bubbling/shiny scorch = too hot.
- **Color match is the hard part** (you flagged this). Test the dye/paint on a hidden spot first; chestnut is easy to miss warm-vs-cool.
- **If the repair doesn't hold** → fallback is sourcing an '87–91 Bronco / F-series driver panel in chestnut. Long lead, so it's worth keeping an eye on listings even while you attempt the repair.

---

*Companion to the `bronco-1989` restoration list in `vehicles.json` → "Driver door panel."*
