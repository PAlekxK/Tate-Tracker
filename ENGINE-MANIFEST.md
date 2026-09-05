# ENGINE MANIFEST — which class every tracked file belongs to

**What this is.** The one declaration of *engine · config · instance · mixed · private-pointer* for
every tracked path in this repo — C4 step 5a, C5 step 5 (`.plans/2026-09-03-c4-environments-PLAN.md`,
`.plans/2026-09-03-c5-record-prep-PLAN.md`), designed in `.plans/2026-09-03-c5-manifest-check-PROPOSAL.md`.
`tools/check-engine-manifest.py` reads the JSON block below and **fails when a tracked file has no
class** (P1) or an exception row has rotted (P2). It classifies; it never moves a file.

**The axis** (`BACKLOG.md` § second axis, `[paul-ratified 2026-09-02]`): ⚙️ **engine** — shared
machinery that serves every estate; a divergence here is a defect · 🎛 **config** — a per-estate
declaration as data · 🏡 **instance** — Fernwood's own record and content · **mixed** — a file that is
demonstrably both, carrying a declared shrink target · **private-pointer** — a filename kept in the
public repo only so a reference resolves, its content living in `fernwood-private`.

**Class is DERIVED from layout** (the dir→class table), never hand-rostered per file — 694 files would
rot in a week. Root files derive from the three rosters that already exist and are **read, not
restated**: `momlib.DOMAINS` (domain canon → instance), `check-domains.py`'s `NON_DOMAINS` (each
carries its own reason), `check-data-inline.py`'s `SOURCES` (the re-inlined consts). The exception
table below carries only what none of those place.

⭐ **"Invert ownership, not the directory"** `[paul-ruled 2026-09-03, C4]`: `tools/` and `worker/`
are **engine and do not move**. `ROOT = parent of tools/` stays true for all 51 tool sites. The
engine's eventual home is `engine/` *inside* each instance repo (C4 5b/5d) — this table is what says
which files go there.

⚠️ **Divergence tiers are Paul's assignments, not derived** (`PRODUCT-ENGINE.md` § the divergence
contract: *"the ASSIGNMENTS are Paul's"*). The tiers below are **proposed** by the agent that wrote
this file and are marked so. The checker verifies a tier is *stated*, never that it is right.

⚠️ **What the checker cannot see, stated so this does not read as coverage:** whether a class is the
*right* class; whether an engine file has actually diverged from an engine source of truth (P3 —
`skipped` until an engine remote exists at 5d, never `pass`); a config value copied into engine code
(P4 — counted, and its detector is C5 step 4's lint, not built yet); whether a `mixed` file's share
is moving in the right direction (reported as a count, never graded).

```json manifest
{
  "version": 1,
  "declared": "2026-09-03",
  "engine_remote": null,
  "classes": ["engine", "config", "instance", "mixed", "private-pointer"],

  "dirs": {
    "engine/":           {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "the engine's own home — viewer.template.html (C4 5b); byte-identity to the built viewer is the check"},
    "instance/":         {"class": "config",   "note": "per-estate declarations as data (C4 5b) — what canon does not say, never a restated fact"},
    "onboarding/":       {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-05; Paul assigns", "note": "the first run — recognised · one question · the wait. Serves EVERY estate and names none: it is the door a person walks through before an instance exists, so it carries no canon and no place name. Deployed alone to an estate's Pages origin; the viewer is deliberately NOT in that deploy (see the fernwood-home hazard note in engine/viewer.template.html)"},
    "tools/":            {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "explicit row — invert ownership, not the directory"},
    "worker/":           {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "explicit row — the Worker is the engine's server half; two files inside are mixed, see below"},
    ".github/":          {"class": "engine",   "tier": "DECLARED",         "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "workflows are engine shape; the weather recorder's schedule is a declared per-instance exception (C4 process Q4)"},
    "images/":           {"class": "instance", "note": "the place's photographs, basemap, plant references"},
    "sounds/":           {"class": "instance", "note": "the place's bird/insect/amphibian recordings"},
    "manuals/":          {"class": "instance", "note": "this fleet's manuals"},
    "guides/":           {"class": "instance", "note": "authored guides for this fleet and place"},
    "research/":         {"class": "instance", "note": "research about this place"},
    "data/":             {"class": "instance", "note": "instance data files"},
    "cycle/":            {"class": "instance", "note": "this instance's loop chronicles, state and inbound door"},
    "handoff/":          {"class": "instance", "note": "this instance's session baton-passes"},
    "review/":           {"class": "instance", "note": "dated trail — process record of this instance; history, never rewritten"},
    ".engineering/":     {"class": "instance", "note": "dated trail"},
    ".ux-reviews/":      {"class": "instance", "note": "dated trail"},
    ".user-research/":   {"class": "instance", "note": "dated trail"},
    ".plans/":           {"class": "instance", "note": "dated trail — plans and proposals for this instance and the engine work done from it"},
    ".decisions/":       {"class": "instance", "note": "decision cards (operating-layer intake)"},
    ".design-options/":  {"class": "instance", "note": "dated trail"},
    ".ai-advisor/":      {"class": "instance", "note": "dated trail"},
    ".content-reviews/": {"class": "instance", "note": "dated trail"},
    ".audit/":           {"class": "instance", "note": "dated trail"},
    ".content/":         {"class": "instance", "note": "dated trail"},
    ".design-research/": {"class": "instance", "note": "dated trail"},
    ".ai-reviews/":      {"class": "instance", "note": "dated trail"},
    ".history/":         {"class": "instance", "note": "archived history; never rewritten"}
  },

  "root_rules": {
    "domains_from_momlib":            {"class": "instance", "note": "every momlib.DOMAINS file — the record of this place"},
    "non_domains_from_check_domains": {"class": "instance", "note": "every NON_DOMAINS file — each already carries its reason in check-domains.py"},
    "markdown_default":               {"class": "instance", "note": "root *.md is this instance's documentation unless listed in root_files"}
  },

  "root_files": {
    "viewer.html":        {"class": "mixed",    "shrink_to": "engine/viewer.template.html + instance/fernwood.json via tools/build-viewer.py (C4 5b)", "note": "53% instance by data-model §3 measurement; 22 *_DATA consts + the identity block are the instance half"},
    "index.html":         {"class": "engine",   "tier": "DECLARED", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "the entry redirect"},
    "CLAUDE.md":          {"class": "mixed",    "shrink_to": "engine guidance → PRODUCT-ENGINE.md; the file stays Fernwood's (its own § Product engine says so)", "note": "instance doc that still carries engine rules"},
    "PRODUCT-ENGINE.md":  {"class": "engine",   "tier": "FREE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "the engine's own capture doc"},
    "VOCABULARY.md":      {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "schema words are shared by construction"},
    "ENGINE-MANIFEST.md": {"class": "engine",   "tier": "MUST-NOT-DIVERGE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "this file"},
    "INSTANCE-RECIPE.md": {"class": "engine",   "tier": "FREE", "tier_by": "agent-proposed 2026-09-03; Paul assigns", "note": "GENERATED by tools/instance-recipe.py (--check); the refinement log inside it is hand-kept"},
    ".gitignore":         {"class": "engine",   "tier": "DECLARED", "tier_by": "agent-proposed 2026-09-03; Paul assigns"},
    ".gitattributes":     {"class": "engine",   "tier": "DECLARED", "tier_by": "agent-proposed 2026-09-03; Paul assigns"},
    "COMMS-CHANNELS.json":       {"class": "instance", "note": "exception — not a domain and not in NON_DOMAINS: this instance's declared inbound channels for the comms board"},
    "arrival-dispositions.json": {"class": "instance", "note": "exception — not a domain and not in NON_DOMAINS: per-arrival dispositions (check-arrival-dispositions.py)"},
    "phase-f-session2-unified-input-2026-05-21.png": {"class": "instance", "note": "a dated screenshot"}
  },

  "mixed_in_dirs": {
    "worker/worker.js":   {"shrink_to": "prompts and hard facts derive from instance config (C5 7b); the estate id from the credential (C6)", "note": "engine server code carrying typed instance literals (2,873 ft ×5 blocks, the station MAC default)"},
    "worker/digest.json": {"shrink_to": "already built from canon by build-digest.py; stays mixed by nature — an engine artifact whose content is instance", "note": "generated"}
  },

  "private_pointers": {}
}
```

**How to add a file.** Put it in a directory the table already classifies and nothing changes. A new
top-level directory, or a root file no roster places, fails P1 at the next session start — add a row
here with its class and a reason. A row is a claim; the reason is what lets the next reader audit it.

**Pre-registered** (proposal §7, discharged in C5's `## Retro`): *did P4 or P5 reach its arming
condition by the time C5 closed, and if not, what was the count on the closing run?*
