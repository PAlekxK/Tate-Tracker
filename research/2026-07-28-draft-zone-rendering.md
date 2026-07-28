# Draft zones now render as draft — a traced boundary no longer reads as a surveyed one

Mission `t1`, 2026-07-28. Repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`, branch `main`,
base commit `258ba3c`. Changed file: `viewer.html` only (28 insertions, 1 deletion —
`git diff --stat`). `zones.json` is byte-identical to HEAD (`git diff --quiet -- zones.json` → clean).

---

## Where zones are drawn (file:line)

The property map is one function. Everything about how a zone looks lives in two places:

| What | Where | Note |
|---|---|---|
| Zone polygon emitted into the SVG overlay | `viewer.html:8336-8337` (was `viewer.html:8310` at HEAD) | one `<polygon class="pmap-zone">` per zone, inside `renderPropertyMap()` |
| `renderPropertyMap()` entry | `viewer.html:8310` | called from `renderProperty()` at `viewer.html:10906` — the map opens the Property card |
| Zone label, second pass | `viewer.html:8345` | drawn after all polygons so text sits above fills |
| Polygon style (the confirmed baseline) | `viewer.html:552-559` | `.pmap-zone` — sage fill `rgba(122,149,104,0.18)`, stroke `#2a4a1a`, `stroke-width: 2` |
| **Draft style (new)** | `viewer.html:574-579` | `.pmap-zone.is-draft` |
| Vertex→pixel projection | `viewer.html:8250-8285` (`ZoneGeo`) | WGS84 `[lon, lat]` → base-image pixels |
| Tap handler binding | `viewer.html:8720` | `document.querySelectorAll(".pmap-zone")` — an *additive* class cannot break it, and a click test confirms it (below) |
| Status shown as a WORD, on tap only | `viewer.html:8897-8900` | `"· draft"` / `"· confirmed"` / `"· flagged for review"` in the zone panel |

That last row is the shape of the bug precisely: the app already knew the word "draft" and already
said it — but only *inside a panel Mom has to open*. On the map itself, at HEAD, every polygon was
literally the same DOM node with the same single class (`viewer.html:8310` at HEAD emitted
`class="pmap-zone"` unconditionally, with no reference to `z.status`). Measured on the rendered
HEAD page: all 10 polygons came back `cls: "pmap-zone"`, `fill: rgba(122,149,104,0.18)`,
`sw: 2px`, `dash: none` — indistinguishable (baseline run against
`git show HEAD:viewer.html`, output below).

The data source is inlined: `const ZONES_DATA` at `viewer.html:5897`, kept in sync with `zones.json`
by `tools/reinline.py` and guarded by `tools/check-data-inline.py:78`.

## Current draft/confirmed counts

**10 draft. 0 confirmed. 0 flagged.** Every zone on Mom's map is a draft.

```
$ python3 -c "import json,collections; z=json.load(open('zones.json'))['zones']; print(collections.Counter(x['status'] for x in z))"
Counter({'draft': 10})
```

Per zone (`zones.json`, id | status | vertex count):

| id | status | verts | provenance |
|---|---|---|---|
| fairway | draft | 11 | agent-claude, "v2 re-trace … off NAIP basemap" |
| parking-bank | draft | 6 | agent-claude, "v2 re-trace of driveway/parking loop" |
| pond-area | draft | 5 | device-drawn 2026-07-17 |
| stable-grounds | draft | 7 | device-drawn 2026-07-17 |
| eastern-patio | draft | 8 | device-drawn 2026-07-17 |
| western-garden | draft | 9 | device-drawn 2026-07-17 |
| fairway-fringe | draft | 8 | device-drawn 2026-07-17 |
| lower-40 | draft | 8 | device-drawn 2026-07-17 |
| upper-uber-wall-area | draft | 10 | device-drawn 2026-07-17 |
| house | draft | 6 | agent-claude 2026-07-22, `"provenance": "agent-proposed hypothesis traced off base-naip-2022-01-leafoff; Paul corrects"` (`zones.json:78`, house `history[0].details`) |

**The mission's premise is one zone too narrow, and this is the most load-bearing correction in
this report.** The brief describes the house zone as the draft one among confirmed peers. It is
not the exception — it is one of ten. `grep -c '"status"' zones.json` → 10; `grep -n 'confirmed'
zones.json` returns exactly one hit, `zones.json:102`, and that is a *history action*
(`fairway`, `{"by": "device", "action": "confirmed"}`, 2026-05-28), not a status. Fairway's
status went back to `draft` when its v1 vertices were cleared in the v1→v2 schema migration
(`zones.json`, fairway `history`, `{"by": "paul", "action": "vertices-cleared"}`, 2026-07-17):
the old confirmation was of geometry that no longer exists.

`zones.json:_meta.accuracyHonesty` says the same thing about all of them: *"Vertices traced off
this basemap are HYPOTHESES, not measurements… ±6 m @ 95%… the real budget ~15-30 ft."* So the
honest rendering of this file today is a map on which **nothing** is drawn as settled. That is
what now ships, and it is a bigger visible change than "the house zone looks different" — see the
card at the bottom, which is about what that means for Mom, not about whether it is correct.

## The treatment and why it satisfies the accessibility rule

```css
/* viewer.html:574-579 */
.pmap-zone.is-draft {
  fill: rgba(122, 149, 104, 0.08);   /* confirmed is 0.18 — less than half the density */
  stroke-width: 2.5;                 /* confirmed is 2 */
  stroke-dasharray: 10 7;
  stroke-linecap: butt;
}
```

```js
// viewer.html:8335 — inside renderPropertyMap()
const draftClass = z.status === "confirmed" ? "" : " is-draft";
```

Against the icon + size + colour + position rule, and what each carrier does:

- **Texture / shape — the primary carrier.** A broken outline. A line with gaps in it is
  *unfinished* pre-verbally; it is the same convention a pencil line has against an inked one, and
  it is the convention the app *already uses for exactly this meaning* — `.pmap-draw-edge`
  (`viewer.html:791-798`) dashes the polygon Paul is mid-way through tracing, `stroke-dasharray: 8 6`.
  A draft zone is now drawn the way a zone being drawn is drawn. This carrier is entirely geometric:
  it survives greyscale, any colour-vision deficiency, and a monochrome screenshot.
- **Weight / size.** Fill drops `0.18 → 0.08`, so a draft zone sits back off the photograph
  instead of sitting on it. Stroke goes `2 → 2.5` in the same move — and that direction is
  deliberate. Dashes remove roughly 40% of the outline's ink (`10 on / 7 off`), and the CSS
  comment at `viewer.html:507-509` sets a hard floor: *"Mom-no-glasses floor: polygon stroke must
  read at default zoom."* A draft zone must be **quieter, never fainter**; thinning the stroke
  would have traded honesty for legibility, which on this map is not a trade that is allowed.
- **Colour — deliberately NOT a carrier.** Measured on the rendered page, draft and confirmed
  share the identical stroke colour, `rgb(42, 74, 26)`, and the identical fill hue,
  `rgb(122, 149, 104)`. Only the fill's alpha differs, and alpha is doing weight, not hue. So the
  distinction cannot fail on a colour-blind read, and there is no new colour to learn.
- **Position — untouched, on purpose.** A zone's position *is its content*; nudging or insetting a
  draft polygon to mark it would corrupt the one thing the polygon asserts. Position is left alone.
- **No legend.** Nothing was added to consult: no key, no chip, no control, no copy. The word
  "draft" already exists on tap at `viewer.html:8899` and was not touched.

What was considered and rejected: a hatch/crosshatch fill pattern (needs an SVG `<pattern>` def
and reads as *hazard* on an aerial — the brief forbids alert language, and hatching is the visual
grammar of a warning); a colour shift to amber/grey (colour-alone, violates the rule outright);
a `?` or `~` glyph on the label (that is copy, and copy on Mom's map is Paul's call — it is
the card at the bottom).

## Rendered-page verification evidence

Served from the repo (`python3 -m http.server 8899`, `curl -o /dev/null -w "%{http_code}"
http://localhost:8899/viewer.html` → `200`) and driven with **playwright-core** against the Chrome
for Testing binary already cached at
`~/Library/Caches/ms-playwright/chromium-1234/chrome-mac-arm64/`, iPhone-sized viewport
430×932 @2x. (The Playwright MCP tool was not permission-granted in this unattended run; the
harness is `playwright-core` driven from `node`, which is the same browser.) Scripts:
`/tmp/tt-verify/verify.mjs`, `/tmp/tt-verify/baseline.mjs`, `/tmp/tt-verify/tap.mjs`.

**1. Measured computed styles, on the live page — all 10 polygons.** Not the stylesheet, the
resolved values off `getComputedStyle` after `expandCard('card-property')`:

```
{'id': 'house', 'statusAttr': 'draft', 'cls': 'pmap-zone is-draft',
 'fill': 'rgba(122, 149, 104, 0.08)', 'stroke': 'rgb(42, 74, 26)',
 'strokeWidth': '2.5px', 'strokeDasharray': '10px, 7px', 'strokeLinecap': 'butt'}
```
Identical shape for `fairway`, `parking-bank`, `pond-area`, `stable-grounds`, `eastern-patio`,
`western-garden`, `fairway-fringe`, `lower-40`, `upper-uber-wall-area` — 10/10 carry `is-draft`
and the dashed 2.5px / 0.08-fill treatment.

**2. Before/after against HEAD, same harness, same browser.** `git show HEAD:viewer.html >
viewer-head-baseline.html`, served alongside, then removed via `trash`:

| | HEAD (before) | working tree (after) |
|---|---|---|
| class | `pmap-zone` | `pmap-zone is-draft` |
| fill | `rgba(122, 149, 104, 0.18)` | `rgba(122, 149, 104, 0.08)` |
| stroke-width | `2px` | `2.5px` |
| stroke-dasharray | `none` | `10px, 7px` |

**3. Rendered class checked against the record, fetched independently.** The verify script does
*not* trust the inlined const — it `fetch`es `/zones.json` in the page and compares each
polygon's class to the file's own status:

```
{'id': 'fairway',              'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'parking-bank',         'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'pond-area',            'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'stable-grounds',       'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'eastern-patio',        'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'western-garden',       'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'fairway-fringe',       'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'lower-40',             'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'upper-uber-wall-area', 'recordStatus': 'draft', 'dashed': True, 'correct': True}
{'id': 'house',                'recordStatus': 'draft', 'dashed': True, 'correct': True}
```
10/10 `correct: True` — rule asserted as `(status === 'confirmed') ? !dashed : dashed`.

**4. Synthetic confirmed control — proving the two states actually diverge.** Because the record
contains no confirmed zone, "it renders draft correctly" is unfalsifiable on its own. So the
script strips `is-draft` from a live polygon and re-measures the same node:

```
{'id': 'fairway',
 'draft':               {'dash': '10px, 7px', 'w': '2.5px', 'fill': 'rgba(122, 149, 104, 0.08)'},
 'confirmedSynthetic':  {'dash': 'none',      'w': '2px',   'fill': 'rgba(122, 149, 104, 0.18)'}}
```
The confirmed branch resolves to exactly the HEAD baseline, i.e. a zone Paul confirms tomorrow
renders precisely as every zone rendered yesterday. No regression is possible for confirmed zones.

**5. Screenshots — A/B of the same map, same session, same pixels except the class.**
- `research/evidence/2026-07-28-draft-zones.png` — as it ships (all 10 dashed, quiet fill)
- `research/evidence/2026-07-28-draft-zones-control-confirmed.png` — same map, `is-draft` stripped
  from every polygon (the old rendering)

Read side by side, the dashed outlines are unmistakably distinct from the solid ones at default
zoom with no panning, which is the `viewer.html:507-509` floor.

**6. Tap behaviour intact.** The class is additive, and `viewer.html:8720` binds on `.pmap-zone`;
clicking the house polygon on the live page:
```
{"panel": {"name": "House", "status": "· draft"}, "pageErrors": []}
```
Panel opens, correct zone, correct status word, zero page errors.

**7. Console.** Identical profile before and after — this change introduces nothing:

| message | HEAD | after |
|---|---|---|
| `warning: Almanac — load failed: ReferenceError: Cannot access 'FN_STORAGE_KEY' before initialization` | 16 | 16 |
| `verbose: [DOM] Password field is not contained in a form` | 1 | 1 |
| `error: Failed to load resource: 404` | 1 | 1 |

Zero `pageerror`. **Not "0 console errors" — 1, and it is pre-existing.** The 404 is
`/favicon.ico` (`grep '404' /tmp/tt-server.log` → `4  GET /favicon.ico HTTP/1.1" 404`), browser-issued,
present identically at HEAD. The 16 `FN_STORAGE_KEY` warnings originate at `viewer.html:15381`
in `fnLoadAll` via `renderVehicleItem` (`viewer.html:11556`) — the vehicles card, untouched by this
work, and present in identical count at HEAD. A later run also showed two `429`s from
`archive-api.open-meteo.com`; that is the external weather API rate-limiting repeated local loads,
not a page fault. **Two pre-existing defects are visible in this evidence and neither is in scope
here** — flagged, not fixed, not counted as mine.

**8. Repo's own data-drift guard.** `python3 tools/check-data-inline.py` →
`OK ZONES_DATA: 10 entries, content in sync.` … `All data consts in sync with source JSONs.`

## What I did NOT change

- **`zones.json` — not one byte.** `git diff --quiet -- zones.json` exits clean. No status
  promoted or demoted, no zone added or removed, no vertex moved. The freeze holds; `git status
  --short` shows only `M viewer.html` plus the untracked `research/` artifacts.
- **The confirmed rendering.** `.pmap-zone` (`viewer.html:552-559`) is untouched — measured
  proof in evidence #4.
- **No new UI.** No legend, no key, no chip, no toggle, no filter, no tooltip, no copy anywhere.
  The zone panel's status word (`viewer.html:8897-8900`) is exactly as it was.
- **No label change.** `.pmap-zone-label` (`viewer.html:560-571`, emitted at `viewer.html:8345`)
  is byte-identical. Adding a word or glyph to a zone name is Mom-facing copy — the card below.
- **Two pre-existing defects, observed and left alone:** (a) the `FN_STORAGE_KEY` TDZ error on
  the vehicles card, `viewer.html:15381`, 16× per load; (b) at default zoom the zone labels
  overlap into an unreadable cluster — visible in both screenshots, "Upper-Uber Wall Area" and
  "House" and "Eastern Patio" collide. Both predate this change and are outside a
  correctness-only brief.
- **`tools/draw-zones.py`** — the offline Python zone renderer was not touched; the brief scoped
  the viewer, and that script produces no Mom-facing surface.

---

## CARD FOR DECISION

**With 0 of 10 zones confirmed, a dashed outline has nothing on screen to contrast against.
Should a draft zone say so in a word — and is an all-dashed map what you want Mom to open?**

The fix above is correct and it ships either way: status now drives rendering, and the day you
confirm a zone it goes solid with no further work. But two things follow from the count that the
brief did not anticipate, and both are yours:

1. **Legibility of the distinction, today.** "Dashed = not yet confirmed" is a convention. A
   convention with no counter-example visible on the same screen is, functionally, a legend — and
   the brief forbids a legend. Mom will see ten dashed shapes and no solid one. She may read
   *"drawn, not settled"* from the pencil-line quality alone, which is the bet I shipped; or she
   may read nothing at all and the honesty stays invisible until the first zone is confirmed. The
   only carrier that works with zero contrast is a **word** — e.g. the label rendering
   `House` → `House · not yet confirmed`, or a small `~` before draft names. That is Mom-facing
   copy on Mom's map, which this project does not let an agent decide. **I did not add it.**
2. **The blast radius is the whole map, not the house.** The brief framed this as one provisional
   zone among confirmed ones. It is all ten, because the v1→v2 migration cleared fairway's
   confirmed geometry and nothing has been confirmed since. So this change alters how Mom's entire
   property map looks, not one polygon. That is the honest state of the record — but "honest" and
   "what you want her to open on" are your call, not mine.

The cheapest thing that dissolves both: **walk one zone and confirm it.** A single `confirmed`
status turns the dashed/solid pairing into a self-teaching contrast on the screen, with no copy
added and no design decision needed. Fairway is the obvious candidate — it was confirmed once
already, on 2026-05-28.

---

## SOURCES / CONFIDENCE LEDGER

| Claim | Source | Confidence |
|---|---|---|
| Zone polygons are emitted at one site inside `renderPropertyMap()` | `viewer.html:8336-8337` (HEAD: `viewer.html:8310`) | high |
| At HEAD every polygon rendered identically, no reference to `z.status` | HEAD source + measured on rendered HEAD page (`baseline.mjs`): 10/10 `cls: "pmap-zone"`, `dash: none`, `sw: 2px` | high |
| Confirmed-zone baseline style is fill 0.18 / stroke `#2a4a1a` / width 2 | `viewer.html:552-559`; computed style on rendered page | high |
| 10 zones, all `status: "draft"`; 0 confirmed, 0 flagged | `python3 -c "…collections.Counter…"` over `zones.json` → `Counter({'draft': 10})`; `grep -c '"status"' zones.json` → 10 | high |
| The single `confirmed` string in `zones.json` is a history action on `fairway`, not a status | `zones.json:102`; fairway `history[1]` = `{"by":"device","action":"confirmed"}` 2026-05-28 | high |
| Fairway's confirmation was voided by the v1→v2 vertex clearing | `zones.json` fairway `history[2]`, `{"by":"paul","action":"vertices-cleared"}` 2026-07-17 | high |
| House zone is an agent-traced hypothesis | `zones.json` house `history[0].details.provenance`: "agent-proposed hypothesis traced off base-naip-2022-01-leafoff; Paul corrects" | high |
| All v2 vertices are hypotheses, ±6 m @ 95%, real budget 15-30 ft | `zones.json:_meta.accuracyHonesty` | high |
| The app already says "draft" as a word, but only in the tap-panel | `viewer.html:8897-8900`; live tap → `{"status": "· draft"}` | high |
| Draft now renders dashed 10/7, stroke 2.5px, fill alpha 0.08 — on the live page, 10/10 | `getComputedStyle` via `verify.mjs`, viewport 430×932@2x | high |
| Rendered class matches `zones.json` status for every zone | in-page `fetch('/zones.json')` cross-check, 10/10 `correct: True` | high |
| Confirmed branch resolves to exactly the HEAD baseline (no regression possible) | synthetic control in `verify.mjs`: `is-draft` stripped → `dash: none`, `w: 2px`, fill `0.18` | high |
| Draft and confirmed share identical stroke colour and fill hue — colour is not the carrier | measured: both `rgb(42, 74, 26)` stroke, both `rgb(122, 149, 104)` fill | high |
| The dashed idiom already means "being drawn" in this app | `.pmap-draw-edge`, `viewer.html:791-798`, `stroke-dasharray: 8 6` | high |
| Stroke must read at default zoom (why 2 → 2.5, not thinner) | `viewer.html:507-509` CSS comment, "Mom-no-glasses floor" | high |
| Dashes remove ~40% of outline ink (10 on / 7 off) | arithmetic on the declared dasharray, `viewer.html:577` | high |
| Tap handlers unaffected by the additive class | `viewer.html:8720` binds `.pmap-zone`; live click → panel "House" / "· draft", 0 page errors | high |
| Console profile identical before/after; the 1 error is a pre-existing `/favicon.ico` 404 | `baseline.mjs` on both builds; `grep '404' /tmp/tt-server.log` → `4  GET /favicon.ico … 404` | high |
| 16 `FN_STORAGE_KEY` warnings are pre-existing, from the vehicles card | `viewer.html:15381` via `renderVehicleItem` `viewer.html:11556`; count 16 at HEAD and after | high |
| The two `429`s are external API rate-limiting, not a page fault | `failedRequests` → `archive-api.open-meteo.com`, appeared only on a repeat run | med |
| Inlined `ZONES_DATA` still in sync with the source JSON | `python3 tools/check-data-inline.py` → "All data consts in sync" | high |
| `zones.json` unmodified | `git diff --quiet -- zones.json` exits 0; `git status --short` → only `M viewer.html` | high |
| Screenshots show the distinction at default zoom without panning | `research/evidence/2026-07-28-draft-zones.png` + `-control-confirmed.png`, both viewed | high |
| Label overlap at default zoom is a pre-existing defect | visible in BOTH screenshots incl. the control (which is the HEAD rendering) | med |
| Mom will read a dashed outline as "not settled" without a word | none — this is the design bet, not a finding | **low** — the card |
