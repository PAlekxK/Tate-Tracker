# Zone mapping — what data exists now, and what ever will (2026-07-16)

Companion to `.engineering/2026-07-16-path-zone-coordinate-model.md`. Commissioned by Paul:
*"the most effective way to set these zones that's going to endure and be able to be refined in
the future based on what data we expect to be accessible now and in the future."*

Target: Fernwood, Jasper GA · 34.5496, -84.3674 · 2,959 ft · Pickens County.
Where noted **[verified at point]**, the live service was queried against the property's exact
coordinate rather than repeating documentation.

---

## ⭐ The finding that decides it

**Every free remote source is stuck in a 15–30 ft accuracy band, and none of them is going to
improve for rural Pickens County.**

- **Esri World Imagery over this property has been frozen at a 2022-02-12 capture for four
  straight years** [verified at point]. Prior refreshes: 2017-01 → 2018-01 → 2019-04 → 2022-02.
  Rural north Georgia is low priority.
- **Georgia is a 60 cm NAIP state.** The 30 cm option exists; no evidence GA has been upgraded.
- **FY26 3DEP funded zero Georgia lidar projects.** The 2018/2019 collect is the lidar, indefinitely.

**So "wait for better imagery" is not a strategy — that band will not move on its own.** What moves
it is entirely Paul-side: one afternoon with a sub-250 g drone + a free OPUS control point takes the
property from **±25 ft to ±2 in**, permanently, on imagery he owns, in a season he chooses.

**Corollary for the schema:** the zones must be **re-registerable, not re-drawable**. That is only
possible if we write down *what each vertex was drawn against*.

---

## 1. Imagery

### USDA NAIP — the right basemap for a public repo [verified at point]

Full history at this quarter-quad (`m_3408430_sw`), via Planetary Computer STAC + USGS catalog:

| Date | GSD | Season | Item ID |
|---|---|---|---|
| 2010-08-31 | 1.0 m | leaf-on | `ga_m_3408430_sw_16_1_20100831` |
| 2013-10-25 | 1.0 m | late fall | `ga_m_3408430_sw_16_1_20131025_20131126` |
| 2015-09-15 | 1.0 m | leaf-on | `ga_m_3408430_sw_16_1_20150915_20151221` |
| 2017-10-20 | 1.0 m | late fall | `ga_m_3408430_sw_16_1_20171020_20171207` |
| 2019-10-04 | 0.6 m | early fall | `ga_m_3408430_sw_16_060_20191004_20200103` |
| **2022-01-10** | **0.6 m** | **leaf-OFF** ⭐ | `ga_m_3408430_sw_16_060_20220110` |
| 2023-10-07 | 0.6 m | early fall (current) | `ga_m_3408430_sw_16_060_20231007_20240103` |

- **Public domain. Redistributable on a public GitHub repo.** This is the deciding property.
- Accuracy: **±6 m @ 95%** (~20 ft) — NAIP contract spec since 2009.
- Cadence: "no more than 3-year cycle"; observed GA: 2019 → 2022 → 2023. **No 2025 GA item exists**
  in Planetary Computer or the USGS catalog today — next capture genuinely unknown.
- Leaf-on is **not** guaranteed: this quad's 2022 capture is dead-of-winter.
- Access: Planetary Computer STAC `POST /api/stac/v1/search` (cleanest way to pull a *specific
  date*) · USGS NAIP ImageServer `https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer`
  (no key, no zoom cap, queryable catalog with `acquisition_date`) · EarthExplorer per-tile.
- **Verdict: design for this.** Store the STAC item ID + capture date with anything digitized off it.

### Esri World Imagery — use live, never bake in [verified at point]

Queried Esri Wayback metadata layers at the property across 2018→2026:

| Wayback release | Actual capture here | Src res | Declared accuracy |
|---|---|---|---|
| 2018-12-14 | 2017-01-10 | 0.50 m | 10.16 m |
| 2019-12-12 | 2018-01-04 | 0.31 m | 4.00 m |
| 2020/2021 | 2019-04-16 | 0.50 m | 5.00 m |
| 2022 → 2025 | **2022-02-12** | 0.31 m | 5.00 m |
| **2026-06-30 (current)** | **2022-02-12** | 0.31 m | **8.47 m (27.8 ft)** |

- Source is **WorldView-3 satellite**, Maxar "Vivid" (Maxar now brands as **Vantor**) — not aerial.
- **Every Esri capture here is leaf-off or early spring.** There has never been a leaf-on one.
- **The declared accuracy got *worse* in the 2026.R02 release: 5.00 m → 8.47 m.** Same image,
  re-declared.
- 🚨 **Licensing: the tiles may NOT be redistributed.** Free use requires an ArcGIS account,
  non-revenue use, and attribution to Esri *and* all data providers; you may display them live,
  not commit them to a repo. **This disqualifies Esri as a committed basemap for a public repo.**
- Query the vintage yourself (no key): `waybackconfig.json` → the release's `metadataLayerUrl`
  layer 4/5 → fields `SRC_DATE2` (real capture; `SRC_DATE` is epoch-zero/null), `SRC_RES`, `SRC_ACC`.
- **Verdict: live visual reference only. Do not anchor geometry to it; do not host it.**

### Others

- **Google Earth** — no programmatic access for this use; Geo Guidelines permit "a handful of static
  images" with attribution, which a tiled basemap is not. **Manual eyeball only** (useful for
  spotting leaf-on years). Ignore as a layer.
- **Georgia GIO State Imagery** — statewide, leaf-on *and* leaf-off, free — **but only to Georgia
  governmental entities**, and it's purchased from Google, so it'd carry Google's terms anyway. Ignore.
- **Pickens County parcels** — no public/open service found (qPublic/Schneider viewer only; probes of
  plausible county ArcGIS hosts + an AGOL search returned nothing). Resellers exist, implying no free
  feed. **The recorded plat is the better anchor** — county parcel layers are tax cartography,
  routinely 10–50 ft off and disclaimed as non-survey.
- **`basemap.nationalmap.gov/USGSImageryOnly` z18/z19 404** — **not retired; capped by design.**
  `maxScale: 9027.977411` = LOD 16; the cache is only built to z16 though `lods` declares 24 levels.
  z16 returns 200, z17+ 404. **Replacement: `imagery.nationalmap.gov` NAIP ImageServers** (dynamic,
  no zoom ceiling, 0.3 m pixel size).

---

## 2. ⭐ 3DEP lidar — the most underrated asset [verified at point]

**Project `GA_Statewide_2018_B18_DRRA`, block B3** — flown **2019-03-23 → 2019-04-24, leaf-off**.

- **1 m DEM:** `USGS_1M_16_x74y383_GA_Statewide_2018_B18_DRRA.tif`
  (`prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/GA_Statewide_2018_B18_DRRA/TIFF/`)
- **Point cloud:** 2 LAZ tiles cover the property — `e1056n1340` (20 MB) + `e1056n1341` (26 MB), at
  `rockyweb.usgs.gov/vdelivery/Datasets/Staged/Elevation/LPC/Projects/GA_Statewide_2018_B18_DRRA/GA_Statewide_B3_2018/LAZ/`
- Density ~3.92 pts/m² project-wide (**4.95 pts/m²** for block B3 per OpenTopography).
- **Vertical accuracy: 7.2 cm RMSE open / 18.69 cm vegetated (95th pct).**
- QL2 is **inferred** (ANPS 0.71 m + LBS v1.3 + 1 m DEM), never stated in the metadata read.
- Free, public domain, unrestricted download, **redistributable**.
- Bonus baseline: **2012 GADNR lidar covering Pickens** (1.0 pt/m², 0.0381 m RMSE, leaf-off) via NOAA
  Digital Coast — a 7-year comparison if the pond/drainage ever needs a then-vs-now.

**Why it matters more than any image:** at 1 m leaf-off it gives the **bare-earth surface *under*
the canopy** — which *no* imagery source on this list can do. Slope breaks (parking bank, fairway
edge, terrace lips), the **spring drainage thalweg**, and the **pond rim** all read cleanly on a
hillshade + slope raster. Recipe: pull the DEM, `gdaldem hillshade` + `gdaldem slope`, render as a
semi-transparent underlay beneath NAIP. **And it does not expire** — terrain isn't moving and no
reflight is scheduled.

---

## 3. Owner-collected positioning — the refinement path

### Phone GNSS
- Dual-frequency **L1+L5 starts at iPhone 14 Pro**; 15/16 Pro/17 carry it. (Non-Pro 16: unconfirmed.)
- Realistic under a north-GA hardwood canopy, from the forestry literature:
  **~4–6 m (13–20 ft) leaf-on**, ~3–4 m leaf-off, ~2–3 m in the open fairway. Dual-frequency buys
  about a **one-third** error reduction (multipath rejection) — it does *not* get you sub-metre in woods.
  (Forests 13(10):1591 — Mi 8: 6.13 m leaf-on → 4.10 m leaf-off → 2.23 m open. Sensors 22(3):1289 —
  Mi 10 DRMS 4.56 m under canopy.)
- ⚠️ **iOS `horizontalAccuracy` is a fused estimate and is optimistic under canopy** — it will report
  5 m when you are 15 m off.
- **Good enough to place a *zone*; not to place a *plant*.**

### RTK — and the corrections answer
- Hardware (2026): SparkFun RTK Facet **$739.95** (backordered) · Emlid Reach RX **$1,599** ·
  Emlid Reach RS3 **$2,999** (7 mm + 1 ppm H, tilt comp). Avoid L-Band delivery — **u-blox
  PointPerfect L-Band sunsets 2025-12-31**.
- Georgia RTN is **not free**: eGPS **$1,650–2,475/yr**; RTKdata from **$40/mo**. RTK2go is a free
  community caster — *whether a base sits within the ~35–50 km baseline of Jasper is unverified*.
- ⭐ **The free answer is NOAA OPUS**: occupy a point, log raw GNSS **4+ hours**, submit, get
  coordinates **within ~2 cm** in NSRS. $0, no subscription.
- **Play:** one receiver → set it in the **open fairway** (the one spot with sky) → 4 h log → OPUS →
  a free 2 cm control point → use it as your own base and RTK off it. Caveat: **under dense hardwood
  the rover needs sky too — expect fixes in the fairway/gardens/pond/parking bank, float or no-fix
  deep in timber.**

### ⭐ Drone ortho — the endgame
- DJI Mini class (sub-250 g): **~0.74 cm/px at 40 m AGL**, ~1.9 cm/px at 100 m — **~30× sharper than
  NAIP, ~16× sharper than Esri**, on a date and in a season you choose.
- **WebODM / OpenDroneMap** (free, open source) → georeferenced ortho + DSM + DTM + point cloud;
  supports GCPs.
- FAA: fly under the **Exception for Limited Recreational Operations** (personal enjoyment only —
  *monetizing the dashboard would push this to Part 107*); **TRUST** is mandatory, free, carry proof;
  **sub-250 g recreational needs no registration** (over 250 g: $5/3 yr); **VLOS at all times**;
  verify airspace over Jasper. Owning land ≠ owning airspace, but 10 rural acres with VLOS is
  squarely inside the exception.
- ⚠️ **Without GCPs the ortho is internally centimetre-perfect but globally shifted several metres**
  (the drone's GNSS is single-frequency, non-RTK). *No peer-reviewed absolute-error figure for
  Mini+WebODM-without-GCPs was found — the mechanism is described rather than a number invented.*
- **The fix is cheap:** 3–5 GCPs occupied with the OPUS-derived control (paint an X on the driveway,
  the pond dam, two fairway corners) → WebODM's GCP interface → **the ortho snaps to ~cm**.

### EXIF geotags
Same GNSS chain, but worse in practice (shutter-time fix, no dwell/averaging, sometimes stale or
Wi-Fi-derived). **No** for plotting individual plants — a 15 ft error puts the pitcher plants in the
pond. **Yes** as a coarse **zone tag**: EXIF → point-in-polygon → zone label is mechanical and sits
cleanly inside the capture-path-stays-deterministic doctrine.

---

## 4. Error budget — how far off is the basemap?

| Source | Declared horizontal accuracy | Feet |
|---|---|---|
| **Esri @ this point, 2026.R02** | `SRC_ACC = 8.47 m` | **27.8 ft** |
| Esri @ this point, 2019–2025 | 5.00 m | 16.4 ft |
| **NAIP contract spec** | ±6 m @ 95% | **±19.7 ft** |
| Maxar WV-3 pointing (raw) | CE90 < 5 m | < 16.4 ft |

Esri does not document whether `SRC_ACC` is CE90 or RMSE — treat as "roughly one-sigma-ish, metres."

**Mountains make it worse.** Orthorectification projects the image through a DEM; Maxar's global
Vivid product does **not** use the 1 m 3DEP lidar — it uses a coarse global DEM. Error grows with
off-nadir angle and DEM error, and steep terrain adds stretch/smear where the sensor couldn't see the
back of a slope. **A 2,959 ft mountain is the bad case.** Realistic budget: **15–30 ft**.

🚨 **Two consequences for the design:**
1. **NAIP and Esri will not agree with each other** — two sources, each ~±20 ft, independently wrong.
   Trace the pond off one and the fairway off the other and the zones are **internally inconsistent by
   up to ~40 ft** with no way to tell why. **Trace everything against ONE source per session.**
2. **A vertex traced off a basemap is a HYPOTHESIS; a vertex from OPUS/RTK is a MEASUREMENT.**
   They must not look identical in the JSON. This is [[feedback_verify_scanned_image_inferences]] —
   model-read values are hypotheses until a deterministic source confirms them — applied to geometry.

---

## 5. The accuracy ceiling, next ~5 years

| Method | Realistic horizontal accuracy | Cost |
|---|---|---|
| Trace off Esri | ~15–30 ft | free, today |
| Trace off NAIP | ~20 ft | free, today |
| Walk with dual-frequency iPhone | ~13–20 ft leaf-on · ~7–10 ft in fairway | free, today |
| Drone ortho, **no** GCPs | relative cm, **absolute several m** | ~$300–800 |
| **Drone ortho + OPUS GCPs** | **~1–4 in** | ~$300 drone + receiver, one weekend |
| RTK rover, open areas | ~1 in | $0 corrections via OPUS + own base |
| RTK rover, dense canopy | **unreliable — float, not fix** | — |

---

## Flagged uncertainties — do NOT treat as fact

- Whether Georgia has **any** 2025/2026 NAIP flight scheduled or flown. Next capture date unknown.
- Whether Pickens is in the **"Georgia 9 County" 2025 lidar** block (described as *western* GA; TNM
  returns no newer DEM here, which argues no).
- **QL2** for `GA_Statewide_2018_B18_DRRA` — inferred, never stated.
- Whether Esri's **`SRC_ACC`** is CE90, RMSE, or other. Units documented; confidence standard not.
- **Measured** absolute error for DJI Mini + WebODM without GCPs. No peer-reviewed figure found.
- Whether an **RTK2go base** falls within 35–50 km of Jasper.
- Whether the **non-Pro iPhone 16** has L1+L5.
- Georgia GIO imagery resolution/cadence (unpublished; moot — government-only).

## Key sources

[NAIP accuracy spec (FSA)](https://www.fsa.usda.gov/Internet/FSA_File/pm2011_aaroneckert_accuracy.pdf) ·
[Planetary Computer STAC](https://planetarycomputer.microsoft.com/api/stac/v1/search) ·
[USGS NAIP ImageServer](https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer) ·
[Esri Wayback config](https://s3-us-west-2.amazonaws.com/config.maptiles.arcgis.com/waybackconfig.json) ·
[Esri wayback-core](https://github.com/Esri/wayback-core) ·
[Esri World Imagery — Uses Permitted](https://www.arcgis.com/home/item.html?id=8e90a00a0a6845a49262e0b756f57a10) ·
[BAS — spatial accuracy & ortho-correction](https://guides.geospatial.bas.ac.uk/10-things-to-know-about-vhr-satellite-data/4.-spatial-accuracy-and-ortho-correction) ·
[GA Statewide 2018 lidar (InPort)](https://www.fisheries.noaa.gov/inport/item/67264) ·
[OpenTopography GA_Statewide_B3_2018](https://portal.opentopography.org/usgsDataset?dsid=GA_Statewide_B3_2018) ·
[2012 GADNR lidar: Pickens](https://www.fisheries.noaa.gov/inport/item/49605) ·
[FY26 3DEP selected projects](https://www.usgs.gov/3d-national-topography-model/fy26-3dep-data-collaboration-announcement-dca-selected-projects) ·
[Forests 13(10):1591](https://doi.org/10.3390/f13101591) ·
[Sensors 22(3):1289](https://www.mdpi.com/1424-8220/22/3/1289) ·
[NOAA OPUS](https://geodesy.noaa.gov/OPUS/about.jsp) ·
[Emlid Reach RS3](https://store.emlid.com/products/reach-rs3) ·
[WebODM](https://webodm.org/) ·
[Skyebrowse — GSD tables](https://www.skyebrowse.com/news/posts/ground-sample-distance) ·
[FAA Recreational Flyers](https://www.faa.gov/uas/recreational_flyers) ·
[Georgia GIO State Imagery](https://gio.ga.gov/state-imagery-program/)
