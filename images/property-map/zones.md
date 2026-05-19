# Fernwood — gardening zones

A growing list of the areas on the property where plants live. Each zone is the **gardening area** around a feature — not just the feature itself. So "eastern patio" means the patio AND the bed plantings that wrap it; "pond area" means the pond AND the plantings around it.

These will eventually become `zoneId` values on plants in `plants.json`, and SVG overlay shapes on the property map view.

**Canonical base image**: `gep-2015-03-leafoff.png` (Google Earth Pro, Mar 6 2015, leaf-off — the layout is most legible here).

**Framing note (Paul, 2026-05-19):** Treat every zone as a gardening zone — the area around the feature, not the feature itself. Plants are what we're locating; structures are just useful anchors for naming.

---

## Zone types

Three flavors are showing up:

- **`planted`** — gardening beds with specific plants. The plants in `plants.json` will eventually carry a `zoneId` pointing to one of these.
- **`turf`** — actively-managed grass / lawn. Watering on a schedule, seeding bare spots, mowing regularly. Tracked at the area level, not the plant level.
- **`meadow`** — low-management mixed-grass / open ground. Occasional mowing, no active watering or reseeding. Distinct from `turf` because the care pattern is much lighter.

(Future zones might add `restoration` for chestnut/hemlock work, `wildland` for unmanaged forest interior, etc. Add types as they come up.)

---

## Zones (growing list)

### Started 2026-05-19

| ID | Name | Type | Anchor | Description (so far) |
|---|---|---|---|---|
| `eastern-patio` | Eastern patio area | `planted` | East side of the house | Garden area around the eastern patio — east-facing aspect, morning sun, afternoon shade |
| `western-patio` | Western patio area | `planted` | West side of the house | Garden area around the western patio — afternoon sun and heat, driveway-side approach |
| `pond-area` | Pond area | `planted` | South of the house, between house and fairway | Garden area around the pond and the tree that covers it — moist, partially shaded |
| `fairway-edge-west` | Western fairway edge | `planted` | Where the fairway clearing meets the forest on the west / "greener" side | The most active fairway-edge planting band — plants set along the edge between cleared turf and forest |
| `front-lawn` | Front lawn | `turf` | Directly south of the house — the active-care portion of the fairway | True managed turf — watering on a schedule, reseeding bare spots, regular mowing. The part of the fairway right in front of the house that gets active care. |
| `fairway-meadow` | Fairway meadow | `meadow` | The rest of the south-facing clearing beyond the front lawn | Low-management meadow — occasional mowing, no active watering or reseeding. The bulk of the fairway extending out from the front lawn. |
| `forest-interior` | Forest interior (placeholder) | `planted` | Wraps the property on west, north, east | Scattered plantings throughout — Paul will build this out with specific data points later; left as a placeholder for now so plants can be tagged here without a richer schema |

---

## To capture later (when Paul has more)

- **East-side fairway edge** — Paul emphasized the western edge as the "greener" / most active planting area. Whether the east edge is its own zone or just absorbs into `fairway-edge-west` semantically is TBD.
- **House-perimeter beds** — north side, front entry, anything off the patio garden zones
- **Driveway approach** — any plantings along the gravel road as it comes up from the southwest
- **Forest interior — specific data points** — when Paul tags specific spots (a stand of mountain laurel, a planted chestnut, etc.), those can break out from the placeholder `forest-interior` into named sub-zones
- **Cardinal precision** for the patios — are they true E/W of each other, or offset N/S? Affects sun exposure modeling
- **Sun exposure tag per zone** (full sun / part sun / shade)
- **Soil notes per zone** if they differ from the property baseline (Hayesville/Cecil/Pacolet)
- **Care notes for turf zones** (watering frequency, seeding schedule, mow cadence)

## How this connects to other files later

- `plants.json` will get an optional `zoneId` field per plant
- The map view will render each zone as a colored SVG polygon over the base image
- The conversational assistant (Phase E) will treat zones as a first-class lookup key — "what's planted near the pond" becomes a real query
