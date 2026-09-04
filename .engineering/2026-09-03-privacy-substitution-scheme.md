# Privacy substitution scheme · the register, the token, and the check that has to notice

- item: the privacy seat's standing scrub-and-substitute duty (Paul commissioned it 2026-09-03)
- objective: O5
- class: engine
- mode: path-evaluation · seat: privacy/security
- date: 2026-09-03 (ET)
- scope: **mine** — what is scrubbable, the substitution scheme, the register's shape, the detection
  method, what breaks. ⛔ **not mine** — the seat's role, the gate, reachability and the decision-history
  siting: `practice-steward` writes `.plans/2026-09-03-privacy-scrub-PROPOSAL.md`. Overlaps are cited, never ruled.
- measured against: HEAD `5d7760f`, **718 tracked files**, **1,730 commits** reachable from HEAD
  (1,731 across all refs). ⚠️ HEAD and the working tree **moved twice during this review** — the parallel
  session shipped I2's needle row into `tools/check-public-build.py` mid-read. Every count below is
  re-stated against the tree as of 22:45 ET.
- read first: `.engineering/2026-09-03-c6-privacy-seat-review.md` (the standard and the calibration) ·
  `.engineering/2026-09-03-setup-journey.md` §I2 · `tools/check-public-build.py` · `CLAUDE.md` § The AI boundary

**Calibration, carried from C6 so nothing below is read at the wrong altitude.** A family app, one
vulnerable user, ~2 people, no adversary with a motive; the worst realistic actor is a bored scanner.
Two things raise the floor: the private tier is real (receipts, contractor phone numbers, the breaker
directory), and a third household is one item away. Nothing here is scored as a production multi-tenant
system, and no recommendation below asks for one.

**Evidence marks.** `[verified]` = I executed something and read the result tonight. `[unverified]` =
inference, or a claim I am taking from a document. ⭐ **The seat's own recorded lesson applies to the
seat:** *a tool that reads OUR files reports on the RECORD, not the world.* Where a document and the
world disagreed below, I went and looked — and **twice tonight my own scan reported clean because it
had failed, not because the repo was clean.** Both are written up in §4, because they are the exact
failure mode this scheme exists to prevent, and I produced them by hand inside two hours.

---

## THE ANSWER, up front

**Three things, in the order they bind.**

> ### 1 · The literal ask cannot be built, and the reason is measurable, not philosophical.
> *"Scrub every release of anything, even potentially PII"* — measured, that is **6,234 occurrences of
> Paul's given name across 318 of 442 tracked text files**, **3,110 of "Mom"**, and — the part no scrub
> can reach — **1,162 commits whose author field is Paul's full legal name**, five carrying his personal
> email, all permanently public on GitHub. `[verified]` A rule that says *no personal identifier is in
> this repo* is **already false 1,162 times before any file is edited**, and it would delete *Mama's
> Perspective*, which is a product surface name Mom reads.
>
> **The rule that survives contact, and it is stronger, not weaker:**
> **the administrator's own identity is published by git and stays. Nobody else's enters.**
> That is enforceable, it is already 95% true, it is exactly what Paul ruled at `165f787`, and it
> generalises to estate 2 without a rewrite. Q1 asks him to ratify it.

> ### 2 · The scrub has no "on the way out," and I tested the one seam that looked like it.
> `[verified]` `tools/build-viewer.py --check` is green: `viewer.html` **is** byte-identical to
> `engine/viewer.template.html` + `instance/fernwood.json`. So the repo *does* now have a build seam —
> but the **built artifact is itself tracked and pushed**, so a scrub placed at build time scrubs
> nothing. `[verified]` `curl` of `raw.githubusercontent.com/PAlekxK/Tate-Tracker/main/...` as an
> anonymous client returned **HTTP 200**, and the GitHub API reports `private: false`. **The repo is the
> release.** Constraint 3 is confirmed by execution, not accepted on the record.
>
> **Therefore the only two legal scrub positions are `never-enters` and `at-source`**, never `at-build`.
> §2b names which class takes which.

> ### 3 · The detection that exists is the right shape and is green over a live leak.
> `[verified]` A **full 17-character VIN** sits in `cycle/requests.jsonl`, tracked, pushed to
> `origin/main`, and I fetched it anonymously over HTTPS tonight — while `check-public-build.py`'s
> `full-vins` row, which is `enforce: True`, prints ✅. Two independent reasons: the row's scope is six
> `SERVED` artifacts and that file is not one of them, and its regex requires a `"vin": "…"` JSON key
> while the value sits in prose. Same shape: **4 distinct real-shaped device ids in 10 tracked files**
> while the `device-ids` row reports *"GONE from the public build."*
>
> I2's needle row got the scope right (`git ls-files`) and the class rows did not. **The fix is to give
> the class rows I2's scope**, not to add a scheme beside them.

---

## 1 · WHAT IS ACTUALLY SCRUBBABLE — measured, with the predicate for every count

⛔ **No value below is quoted.** Class, location and count only — a trail that names the value *is* the
leak, and this seat has already made that mistake once tonight (see F-self-2).

### 1a · The classes that exist, ranked by what they would cost if read by a stranger

| # | class | predicate (exact) | measured |
|---|---|---|---|
| A | **full 17-char VIN** | `\b[A-HJ-NPR-Z0-9]{17}\b` over `git ls-files`, then hand-classified | **1 real** in `cycle/requests.jsonl` — WMI `3VV` (VW NA), timestamped fleet-cycle document read, **its 11-char prefix does not match any recorded prefix**, so it is either the true VIN or a near-miss of it. `[verified]` **pushed; HTTP 200 anonymously.** 3 other hits are a selftest fixture, a ScienceDirect `…/article/pii/…` URL, and Ford boilerplate — all false positives |
| B | **real-shaped device ids** (`d-8-8-8`) | `\bd-[a-z0-9]{8}-[a-z0-9]{8}-[a-z0-9]{8}\b` over `git ls-files` | **4 distinct, 22 occurrences, 10 tracked files** — `.engineering/`, `research/`, `.ux-reviews/`, **`.user-research/persona-mom.md`**, `MOM-CYCLE-LOG.md`, `.audit/`. Ruled private 2026-09-03; moved out of `tools/people.json` only |
| C | **the weather-station MAC** | `\b(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\b` | **1 distinct, 4 occurrences, 3 files**: `worker/wrangler.toml` ×2, `tools/check-config-derivation.py` ×1, **and `.engineering/2026-09-03-c6-privacy-seat-review.md` ×1 — this seat's own trail file.** C6 F3 is still live and I widened it |
| D | **third-party personal email addresses** | `[A-Za-z0-9._%+-]+@(gmail\|windstream\|uga\.edu)` , minus Paul's own | **3 distinct, not Paul's.** 2 are inlined into **`viewer.html` and `engine/viewer.template.html`** — a small nursery's proprietor address on a card Mom can read |
| E | **phone numbers** | `\b1?[-. ]?\(?[2-9]\d{2}\)?[-. ]\d{3}[-. ]\d{4}\b`, normalised to 10 digits, `manuals/` excluded | **31 distinct**; **25 reach a served artifact**; 8 are toll-free vendor lines → **23 geographic numbers.** Institutional (UGA Extension, Poison Center, dealers) except a handful of one-person nurseries where the "business" line is plausibly a mobile |
| F | **image EXIF** | `exiftool -n` over all 232 tracked images | **4 carry GPS *and* a capture timestamp**, all 21–31 m from the recorded property centroid, all shot on the same phone model. **9 carry camera Make/Model.** 0 OwnerName, 0 camera serial. ⚠️ **The coordinates locate the place (already published). The timestamp + device model locates a *person* at the property at a minute** — and **no text scan will ever see this**, because it is binary |
| G | **household naming, at scale** | `\bMom(?:'s)?\b` etc. over `git ls-files` | Paul **6,234 / 318 files**; Mom **3,110 / 265**; Mama **226 / 72**; Bob (first name only) **96 / 18**. `viewer.html` alone: Paul ×459, Mom ×115 |
| H | **`attribution` objects** | recursive walk of every tracked JSON for key `attribution` | **125 objects, 81 distinct authors.** 115 `source: "Wikimedia Commons"` (79 authors — **licence-required, published by them, not scrubbable and must not be**), 7 `source: "Property record"` (1 author — a household member as photo credit), 2 `Phase F submission`, 1 blank |
| I | **`serviceHistory` / `serviceContacts`** | recursive walk of `vehicles.json` | **61 history entries, 32 distinct `shop` values, 6 contact rows** carrying `name·phone·address·url·role·hours·notes`. **31 of 32 shops carry a business token; 1 is person-shaped** (15 chars, 1×) and is most likely a founder-named dealership — **a human must rule, a regex cannot** |
| J | **`feedback-log.json` dispositions** | parsed; quote-mark and first-person probes on all 5 rows | **5 rows, 44–230 chars, hand-typed.** ✅ **`_meta`'s claim *"Never her words"* is TRUE** — the only quote marks present are **possessive apostrophes**, not quoted spans. `[verified by execution, not by reading the _meta]` 3 of 5 name a household member by role |
| K | **street addresses** | `\d{1,5}\s+…\s+(Road\|Rd\|…)` | 26 distinct / 34 files. The top value is the **property's own** (34× across 15 files) — published in `CLAUDE.md` by design. The rest are businesses, plus **2 in `images/insects/_attribution.json`** (iNaturalist observation localities — a third party's, but published by them) |
| L | **coordinates** | `-?\d{2}\.\d{5,}\s*,\s*-?\d{2,3}\.\d{5,}` | **1,060 distinct pairs / 5 files** (`zones.json`, `viewer.html`, the traced-with-Mom plan). **These locate the place, not a person. Not scrubbable — they are O2's substance** |
| M | **commit messages** | regex sweep of 1.44 MB of `%s`+`%b` across all refs | **2 MACs, 2 real-shaped device ids.** ✅ **0 phone numbers, 0 personal emails, and 0 occurrences of the surname removed at `165f787`** |

### 1b · What is NOT there — stated, because a negative you measured is worth more than one you assumed

- `[verified]` **0 SSN-shaped strings.** 3 credit-card-shaped hits, all false positives (long digit runs in scanned manuals and one research doc).
- `[verified]` **0 human-voice audio is tracked.** All 44 tracked `.m4a/.mp3/.wav` are wildlife recordings under `sounds/`. Mom's zone audio stayed in `.private/`. ✅ The QUARANTINE clause is holding on its hardest surface.
- `[verified]` **Paul's `165f787` ruling was executed, not merely recorded.** The removed surname appears in **0 tracked files** and **0 commit messages**; 4 commits still carry it in their blobs, by his knowing ruling.
- `[verified]` **`fernwood-private` has no remote.** It is in `guard-secret-push.py`'s `NEVER_PUBLIC`. Constraint 1's siting is sound.

### 1c · What I could not check, and why

1. **Person names in prose — the largest class, and not mechanically enumerable.** *"Is this capitalised bigram a person?"* is a model read, and a model read is a hypothesis, not a check (Paul's standing rule). I measured the *proxies* (row G, row H, row I) and stopped. **This is the gap the needle register exists to close, and it closes it only forward.**
2. **Whether the 3 third-party emails and the 23 geographic phone numbers belong to a natural person or to a business.** For a one-proprietor nursery those are the same number. **No predicate can separate them; a human must.** → Q4.
3. **Whether the full VIN in `cycle/requests.jsonl` is the true VIN or a misread.** It arrived as a document read — a model-read value, so unverified by Paul's own rule. **The exposure is identical either way**, so I did not chase it.
4. **The 79 Wikimedia photographers' identities.** Out of scope by licence: naming them is the *condition* of using the images.
5. **Binary content beyond EXIF.** I read EXIF/XMP via `exiftool`; I did not examine pixel content for faces, screenshots of documents, or legible text in the 232 tracked images. `.design-options/**/shots/` and `.ux-reviews/` screenshots are the realistic risk surface. **Unmeasured.**
6. **History blob content beyond the pickaxe on one surname.** I did not sweep 1,730 commits × every class. Row M covers messages only.

---

## 2 · THE SUBSTITUTION SCHEME

### 2a · The one principle, stated so it covers both halves

> ### ⭐ **The substitute is either obviously NOT a value, or obviously LESS THAN the value. Never a same-shaped different value.**

**Why this is the whole scheme.** A plausible fake gets believed, propagates into a card, into a digest,
into an agent's context, and **corrupts the record about the place — which is O2 itself.** It is also
Paul's stated fear from the other direction: a developer meeting a plausible value **will "correct" it
back**, because a plausible value looks like a typo, and the substitution is silently undone by someone
being helpful. A value that announces itself cannot be helpfully corrected. **Both failure modes have the
same root and the same fix**, which is why this is one principle and not two rules.

### 2b · Where the human/machine line falls — and it is not where the constraint assumed

The constraint says *anything Mom reads cannot carry a raw token*. Correct. But the resolution is **not**
"tokens for machines, plausible values for humans" — that reintroduces the fake on the exact surface
where a fake does the most damage. **Paul's own ratified precedent shows the third form.** At `165f787`
he did not tokenize and he did not invent: he **truncated** — the full name became `Bob`, still a true
statement, carrying strictly less. `[verified: 96 first-name occurrences remain across 18 tracked files;
the surname is gone from all of them]`

| surface | form | example shape | why |
|---|---|---|---|
| **machine-facing** — canon JSON, `worker/digest.json`, tool output, `.plans/`, `.engineering/`, `BACKLOG.md`, commit messages | **token** `[[redacted:contact-04]]` | `[[redacted:<class>-<nn>]]` | self-announcing (`[[…]]` is already this corpus's link convention), greppable, sorts, and **cannot be mistaken for data by a developer or a model** |
| **human-facing** — anything rendered to Mom or a contributor | **generalise or truncate** — the role noun (*"the plumber"*, *"a neighbour"*) or the first name | `Bob` · `the well contractor` | still **true**, carries less, reads as written English. ⛔ **Never a token, never an invented name** |
| **absent-by-design** — the true value | **nothing.** The field is not present on the public side at all | — | the strongest form; §2c |

⚠️ **The truncation form's one weakness, and its mitigation.** A token is self-documenting; a truncation
is not — *"Bob"* looks like a complete value and nobody will know a rule applied. **So a truncation is
only legal when the register carries the row.** The register is what makes the human-facing half auditable;
without it, truncation and sloppiness are indistinguishable six months later. That is the answer to Paul's
documentation ask: **the developer never needs the value — they need the rule, and the rule is public.**

### 2c · Where the scrub sits — three positions, one rejected outright

| | position | mechanics | verdict |
|---|---|---|---|
| **P1** | **at-source** | edit the canon JSON / prose to the substitute, then rebuild through the normal path | ✅ **for values with no reader** (the stray VIN, EXIF, a device id in a trail file). `check-data-inline.py` and `build-viewer.py --check` stay green **by construction** — see §5 |
| **P2** | **at-build** | template holds a token; `instance/*.json` supplies the real value | ⛔ **Reject.** It breaks `--check`'s byte-identity by design, **and the instance file is tracked anyway** — the value is published regardless. It buys nothing and costs the check |
| **P3** | **never-enters** | the true value lives only in the sibling or in KV; the public side holds the token; the viewer fetches it from the Worker behind the grant | ✅ **for values with a reader** (contractor phones, the breaker directory). This is **C6 step 5, the vault** — already planned, already gated, already scoped |

**Recommendation: P3 where a human needs the value, P1 where nobody does, never P2.** The mapping is
already implicit in `check-public-build.py`'s roster notes (*"Mechanics when released: `serviceContacts` →
the sibling; the card renders a name without a number until login"*) — this names it as the general rule
rather than a per-row aside.

### 2d · Token mechanics

- **Form:** `[[redacted:<class>-<nn>]]`. Classes from the roster ids already in `check-public-build.py`
  (`contact`, `device`, `vin`, `name`, `phone`) — **reuse them; do not mint a class vocabulary.**
- **Stability:** the token is **permanent and never reused.** `contact-04` means one entity for the life
  of the project. A recycled token silently merges two people's histories, which is worse than either leak.
- **Collisions:** the register assigns; nothing else may. Sequence per class, monotonic, never renumbered.
  Two spellings of one entity get **one token and two register aliases** — otherwise the needle scan misses
  the spelling that was not registered.
- **Reversible by register only.** No hash, no encoding, no derivation from the value. ⛔ **Never a hash of
  the value** — a 10-digit phone number has 10^10 candidates, and an unsalted digest of it is reversible in
  seconds on a laptop. A token that *encodes* the value is not a scrub, it is an obfuscation with a
  certificate. An opaque counter has zero information content, which is the entire point.

### 2e · ⛔ Git history — the honest posture, stated plainly

**Substitution forward does not scrub what is already pushed, and this repo has 1,730 commits.**
`[verified]` Paul has already ruled on exactly this question once (`165f787`: *"remove forward, keep
history"*), knowingly accepting that the 09-01 commit stays reachable on GitHub. **I am not proposing a
history rewrite and I do not think one is warranted at these stakes.**

The reasoning, so the posture is a decision and not an omission:

1. **A rewrite is the highest-risk operation available here** and this is a family app. C4's three
   `filter-repo` passes were justified by ten third-party trails; one VIN and four device ids are not that.
2. **It cannot succeed anyway.** `[verified]` 1,162 commits carry Paul's full legal name in the author
   field and 5 carry his personal email. Rewriting those rewrites **every sha in the repo**, breaking every
   `[verified]` citation in `.engineering/`, `.plans/` and `BACKLOG.md` — of which this corpus has hundreds —
   and GitHub keeps the old objects reachable by sha regardless.
3. **The clean-up that IS warranted is forward and small.** The VIN, the 22 device-id occurrences and the
   MAC stop being *added to*; the current values are already out and cannot be recalled.

⚠️ **One thing the forward rule must state out loud, because `165f787` did not have to:** **a value that
has been pushed is public permanently.** Row A's VIN and row C's MAC were fetched anonymously tonight.
Nothing in this scheme un-publishes them, and **no artifact may record them as "fixed."** The correct
record for a pushed value is *"stopped publishing on <date>; the pre-existing exposure stands."*

---

## 3 · THE REGISTER

### 3a · Reuse, do not mint — the file already exists as of tonight

`[verified]` The parallel session created `fernwood-private/supplied-names.json` at **22:40 ET**, with
`_meta.purpose / rule / shape / declared / today` and `names: []`. **This corpus's measured defect is
minting a second convention when one exists.** So:

> **Extend `supplied-names.json` into the register. Do not create a second file.**
> `names` becomes a list of **objects** instead of strings, and `scan_needles()` reads `row["value"]`
> instead of the bare string — a one-line change to a scanner that is 20 minutes old and has an
> **empty** list, so the migration cost is literally zero today and rises every day it waits.
> ⚠️ This is the **only** part of this document with a closing window. → Q2.

⛔ **And do not store a derived needle list beside the register.** Derive the needles in memory at scan
time. A stored projection is a generated view, and `reference_generated_views_check` says a generated
view needs a byte-identity check and a roster row — which is real cost for a list you can rebuild in a
microsecond. **Not generating it is cheaper than checking it.**

### 3b · The row, and where each field lives

| field | example | lives | why there |
|---|---|---|---|
| `token` | `[[redacted:contact-04]]` | **both** — sibling *and* the public `.decisions/` card | it is the join key and it is meant to be seen |
| `value` | *the true value* | **sibling only** | the whole point |
| `aliases` | *other spellings* | **sibling only** | a needle scan finds only what it knows |
| `class` | `contact` | both | roster id, reused |
| `surfaceForm` | `the well contractor` | both | what a human-facing surface may say instead |
| `scrubbedOn` | `2026-09-14` | both | |
| `ruledBy` | `paul-stated 2026-09-14` / `agent-proposed` | both | the C6 roster's own convention — **preserve the distinction between what Paul ruled and what an agent proposed** |
| `why` | one sentence | both | Paul's *"understand rationale, don't repeat mistakes"* |
| `positions` | `never-enters` / `at-source` | both | §2c, so the next reader does not re-derive it |
| `historyPosture` | `forward-only; pre-existing exposure stands` | both | §2e — **so nothing records it as fixed** |
| `supersedes` | prior token, if a ruling was reversed | both | the decision *history*, not just the decision |

⭐ **The split is the answer to Paul's confusion risk.** Every field except `value` and `aliases` is
**public**, in a tracked `.decisions/fernwood-N.md` card — the convention that already exists for exactly
this (`- key: value` header + prose reasoning). **A developer meeting `[[redacted:contact-04]]` can read
the class, the rule, the date, who ruled it and why — in the public repo, without the value and without
the sibling.** They cannot "correct" it back, because there is nothing to correct it to and a card telling
them not to. *(Siting the card is `practice-steward`'s call, not mine — I only note that the split makes
the public half safe to site anywhere.)*

⛔ **What the register must never contain:** any value from the QUARANTINE clause (Mom's account of
herself — that is `.private/`, not the sibling, and not even here); a credential, token or key of any
kind (C6's *"an agent may not persist a credential value anywhere"* covers this file too); or any hash
**of** a registered value (§2d).

### 3c · ⚠️ The register is a re-identification key, and it is more dangerous than the repo it protects

**State this plainly rather than treating it as solved.** Before the scheme, an attacker who wanted a
contractor's phone number had to find it among 718 files. After, **one file hands over every scrubbed
value, its token, every alias, and a map to where each one appears** — pre-correlated, machine-readable,
and complete. The register does not reduce total exposure; **it concentrates it and moves it behind a
different control.** That is a good trade *only* because the control is real: no remote, `NEVER_PUBLIC`,
encrypted off-site bundle. It stops being a good trade the moment any of those three lapses.

**Consequences that follow, all cheap:**

1. **The register is never printed by any tool, ever** — not in a summary, not in a `--verbose`, not in
   an error message. A check reports `3 needle(s) registered, 0 hits`, never which. `[verified]` I2's
   scanner already does exactly this in the clean case; ⚠️ **its failure path prints the matched name**
   (`hits: {rel: [name, …]}`). That output goes to a terminal whose contents are routinely pasted into
   `MOM-CYCLE-LOG.md` — **169 KB, tracked, public.** The check that finds the leak becomes the leak.
   **Print the token and the file, never the value.** → §4, gap 5.
2. **Grep hygiene.** A `grep -r <value>` at a shell leaves it in `~/.zsh_history` and in the transcript.
   The register's own tooling must take the value from the file, never from `argv`.
3. **Loss of the register is loss of the ability to un-scrub, but not a breach.** That is the correct
   asymmetry: the failure mode of losing it is *the record gets less useful*, never *someone is exposed*.

### 3d · Surviving disk loss — measured, and it does not currently hold

`[verified], and this is the most concrete finding in §3:`

| fact | measured |
|---|---|
| encrypted bundle exists | ✅ `…/CloudDocs/Backups/private-repos/fernwood-private-2026-09-03.bundle.gpg`, **15:27 ET** |
| `never-public-backup-check.py` verdict | **19 registered · 19 covered · 0 MISSING · 0 stale** |
| `grants.json` written | **17:01** — *after* the bundle |
| `people-devices.json` written | **19:09** — *after* the bundle |
| `supplied-names.json` created | **22:40** — *after* the bundle |
| sibling HEAD | **22:42** — *after* the bundle |

**The coverage check is green and three of the four private artifacts postdate the only backup.** It is
not wrong — `STALE_DAYS = 30`, which is a sound window for a slow repo and **the wrong instrument for a
register that gains a row every time a name is captured.** *A tool that reads OUR files reports on the
record, not the world* — the register said covered; the clock said otherwise.

**Recommendation, one line and no new machinery: the register's write is what triggers the backup, not a
calendar.** Whatever act appends a row also re-bundles the sibling. → Q5. ⚠️ **And `never-public-backup-check.py`
already says the honest thing about its own limit** — *"'covered' means an artifact exists, never that it
works"* — so a restore has still never been proven. That is Paul's (the passphrase is his) and is not new
tonight; it is simply now load-bearing for a re-identification key rather than for a receipts manifest.

---

## 4 · DETECTION — the part that has to actually work

### 4a · Verdict on I2's shape: **adopt it, and extend it. Do not replace it.**

I2 gets the three hard things right, and I want them named so a later edit does not undo them:

1. ✅ **A needle, not a heuristic.** *"Is this a person's name"* is a model read; a literal needle held
   privately is deterministic and **provable by mutation before any real name exists** — which is a window
   that closes the day the first name is captured.
2. ✅ **`git ls-files` scope, not the six `SERVED` artifacts.** Correct, and §4b shows it is the *only*
   row that gets this right.
3. ✅ **UNCHECKABLE (exit 3) when the sibling is absent.** `[verified]` in the code tonight: `EXIT_UNCHECKABLE = 3`,
   a distinct status, never folded into green. This is the single most important line in the file.

### 4b · Five gaps, all measured tonight, in severity order

**Gap 1 — ⛔ `critical` at this deployment level: nothing runs the check before a push.**
`[verified]` `.git/hooks/` contains **zero non-sample hooks**. `[verified]` CI runs
`check-public-build.py --skip-needles`, which prints *"NOT CHECKED … the row is checked locally, before a
push."* `[verified]` `guard-secret-push.py` is a **`PreToolUse|Bash` hook** — it fires on an *agent's*
tool call and **cannot see Paul typing `git push` in his own terminal**, and his standing doctrine
deliberately leaves git ungated.
**So: CI never checks names; the local check is a ritual; and the only historical control is a person
looking — which is precisely what 2026-07-26 proved is not enough.**
> **The fix, and it is the smallest thing that changes the outcome: a repo-local `.git/hooks/pre-push`
> that runs `check-public-build.py` and refuses on non-zero.** It fires for Paul *and* for an agent,
> it is local-only (never committed, never inherited by a clone), and ⚠️ **it is bypassable with
> `--no-verify`, which is correct** — Paul's git-is-not-gated doctrine survives, because the hook makes
> the check *default* rather than *mandatory*. **A check nothing calls is a document.**

**Gap 2 — ⚠️ `important`: the class rows are scoped to six artifacts and are green over live values.**
`[verified]` `SERVED` is 6 files; `full-vins` and `device-ids` additionally carry `only_in`.
Measured consequence: **a full VIN in `cycle/requests.jsonl` (pushed, HTTP 200) with `full-vins` at
`enforce: True` printing ✅**, and **4 device ids in 10 tracked files with `device-ids` printing "GONE."**
The selftest even asserts the second one as a *pass*.
> **Fix: give every `enforce`-able class row I2's `git ls-files` scope.** Keep `SERVED` as a *reporting
> lens* — "is it in what Pages renders?" is a genuinely different and useful question from "is it in what
> GitHub publishes?" — but **the enforcement predicate must be the repo.** The repo is the release.
> ⚠️ Widening will surface hits the current rows hide; expect the first run to be loud. That is the check
> starting to work, not the check breaking.

**Gap 3 — ⚠️ `important`: an empty register prints ✅ and exits 0.**
`[verified]` tonight's live run: `✅ supplied-names  ruled-private  0 needle(s) registered, none in any
tracked file — EMPTY register: the row can find nothing yet`. The **prose is honest and the mark and the
exit code are not**, and a reader scanning marks sees a green column.
> **A zero-needle register is a vacuous pass at a different layer than an absent file.** I2 caught the
> absent-file case and not the empty-file case — the same failure wearing a different hat.
> **Fix: `0 needles` is its own status (⚠️, and `--strict` non-zero), never ✅.** Cheap, and it is the
> difference between *"we looked and found nothing"* and *"we had nothing to look for."*

**Gap 4 — ⚠️ `important`: the binary blind spot.** Row F: 4 tracked images carry GPS + timestamp + device
model. **Every check in this repo is a text scan.** No needle, no regex and no roster row will ever see
them.
> **Fix, and prevention beats detection here:** an `exiftool`-backed roster row (`image-metadata`,
> `enforce: True`, scope = tracked images) **and** a strip at intake in whichever `wire-*-photos` tool
> writes property photos. ⚠️ **Stripping EXIF is lossy and irreversible** — `takenOn` is real record data
> that O2 wants — so **read the date into the record first, then strip.** Marked irreversible in §6.

**Gap 5 — ⚠️ `important`: the check prints what it finds.** §3c.1. `hits: {rel: [name, …]}` puts the
matched value on stdout, and this project's terminal output is routinely pasted into a tracked 169 KB log.
> **Fix: print the token and the file path. Never the value.** One line.

### 4c — ⚠️ And the pattern-level defect: a detector must not carry its own needle

`[verified]` `check-public-build.py`'s `extension-office-phone` row hard-codes a real phone number as
its regex, in a tracked public file. **Here it is harmless** — a public office's published number, ruled
public. **As a pattern it is fatal**, and it is the exact thing this scheme scales up: the moment a row
detects something private by literal, the tracked detector publishes it.
> **Rule: a detector's needle never lives in the artifact it protects.** I2 already got this right by
> sourcing from the sibling; make it the standing rule so no future row reaches for a literal.
> `SUPPLIED_NAMES_FILE` env override — already in the code — is the correct escape for CI and fixtures.

### 4d — ⚠️ F-self: two false negatives I produced by hand tonight, reported because they are the point

1. **`grep` on this machine is `ugrep`, and it rejected my phone-number alternation** (`(\(|\b)` →
   *"empty (sub)expression"*). Piped into `cut`, the error vanished and the run printed **nothing** — which
   I initially read as *"zero phone numbers in the repo."* There are **31.** *The check reported clean
   because it had failed.*
2. **My first `attribution` walk counted string values only, and `attribution` is an object.** It reported
   **0**. There are **125.**

Neither was a bad regex so much as **a scan with no positive control.** Both would have been caught in one
second by a fixture the scan is *known* to hit.
> **This is the argument for I2's mutation proof, generalised: every roster row carries a fixture it must
> find. A scan that has never been seen to fire is not evidence of absence.** `check-public-build.py`'s
> selftest already does this for four rows — **make it the requirement for all of them**, including the
> widened ones. And it is the argument for §4b gap 3: my scan and an empty register failed in exactly the
> same way, and only one of them printed a warning.

---

## 5 · WHAT BREAKS

Named, because **a scheme that fights the repo every run will be turned off.**

| # | what it collides with | effect | mitigation |
|---|---|---|---|
| 1 | **`check-data-inline.py`** — deep-compares canon JSON against the `*_DATA` consts in `viewer.html` | ✅ **No collision, if P1 is done correctly.** A scrub is an **edit to the source followed by a normal rebuild**, not an interception between them. Both sides carry the token; the deep compare agrees. **It only goes red if someone edits `viewer.html` by hand** — which it already exists to catch | none needed. **Constraint 4 dissolves once the scrub is at-source rather than in-transit** |
| 2 | **`build-viewer.py --check`** — byte-identity vs. template + instance | ✅ **No collision under P1.** ⛔ **P2 breaks it by design** — which is the strongest reason to reject P2 | reject P2 |
| 3 | **`.github/workflows/build-viewer.yml`** runs the audit with `--skip-needles` | ⚠️ **CI can never check names** — the sibling is not there and must not be | correct as built. **Gap 1's pre-push hook is what covers it.** Do **not** put the register in CI |
| 4 | **`tools/momlib.py::_people()`** already merges `fernwood-private/people-devices.json` and reports `UNMAPPED` when absent | ✅ **This is the precedent to copy, not a collision.** Same sibling, same absent-is-loud posture | reuse the pattern; do not invent a second loader |
| 5 | **Widening the class rows (gap 2)** | ⚠️ First run goes loud — 22 device-id occurrences, 1 VIN, the MAC | expected. Land the widening and the scrub **in the same change**, or the check is red-on-arrival and someone turns it off |
| 6 | **`tools/check-config-derivation.py:68`** declares `wrangler.toml` *"the ONE place the station lives"* | ⚠️ Moving the MAC to a secret makes the check that **blesses** the leak fail | C6 F3 already specifies it: flip the roster row to expect it **absent** |
| 7 | **Every pickup/report tool that prints** (`read-mom-feedback.py --pickup`, `read-mom-funnel.py`, `analyze-fernwood.py`, `read-mom-engagement.py`) | ⚠️ I2's own finding: *"no automated writer leaks a name — prose does."* Add the check's failure output (gap 5) to that list | one rule, both places: **a registered value is never printed by any tool** |
| 8 | **`MOM-CYCLE-LOG.md`** — 169 KB, tracked, fed by pasted terminal output | ⚠️ The transport for gap 5 and #7 | already carries **2 real device ids**; it is the measured proof this path is live, not theoretical |
| 9 | **The deploy path** — `build-viewer.yml`, `deploy-worker.yml`, `deploy-worker-qa.yml`, `record-weather.yml` | ✅ No collision. The scrub touches source content; the Pages deploy serves whatever is committed | ⚠️ **`record-weather.yml` commits on a schedule** (435 bot commits) — an unattended writer, so **it must never be given a path that could carry a registered value** |
| 10 | **`.decisions/` cards + the sibling** | ⚠️ Two homes for one row invites drift | **derive, never duplicate**: the sibling is the source, the card carries the public subset. If a tool ever writes the card, it needs `generated_views.py`; if a human writes it, it does not |

---

## 6 · COST, REVERSIBILITY, AND THE IRREVERSIBLE STEPS

| step | cost | reversible? |
|---|---|---|
| Extend `supplied-names.json` rows to objects; `scan_needles` reads `row["value"]` | **~20 min. Today.** The list is empty | ✅ fully |
| Give the class rows `git ls-files` scope; keep `SERVED` as a reporting lens | ~1 h incl. fixtures | ✅ fully |
| `0 needles` → its own status; failure prints token not value | ~20 min | ✅ fully |
| `.git/hooks/pre-push` calling the audit | ~15 min | ✅ fully — delete the file |
| A `.decisions/` card documenting the scheme for developers | ~1 h, hand-written | ✅ fully |
| Register-write triggers the sibling re-bundle | ~30 min | ✅ fully |
| Scrub the VIN + 22 device-id occurrences at source | ~1 h | ✅ **forward.** ⛔ the **pushed values are already public and stay so** (§2e) |
| `exiftool` roster row | ~1 h | ✅ fully |
| **Strip EXIF from the 4 GPS-bearing images** | ~30 min | ⛔ **IRREVERSIBLE — lossy.** Read `takenOn` into the record *first* |
| **`wrangler secret put AMBIENT_MAC`** (C6 F3) | ~15 min | ⚠️ reversible as config; ⛔ **the published MAC cannot be recalled and a MAC cannot be rotated** |
| **Any git-history rewrite** | days, high risk | ⛔ **IRREVERSIBLE. Not recommended — see §2e.** If ever undertaken: a verified `--all` bundle first, per the `165f787` precedent |

**Total for everything except the two irreversible rows: roughly one working day.** The single highest
value-per-minute item is **gap 1's pre-push hook (~15 min)** — without it every other item is a document.

---


## ✅ RULED — Q1, the PII rule `[paul-stated 2026-09-03]`

> *"B is fine, and we can always revisit that."*

**Q1 → (b): the administrator's own identity is published by git and stays. NOBODY ELSE'S ENTERS.**

This is the enforceable rule, it is what Paul already ruled in practice at `165f787` (a third party's
full name removed forward), it measures ~95% true today, and it generalises to a second estate
unchanged. ✅ **Unblocks §2 (the human-facing substitution form) and §3 (the register's scope), both of
which descend from it.**

⛔ **Option (a) was rejected because it was unbuildable, not because it was undesirable.** *"No personal
identifier in the repo"* is already false **1,162 times** — the count of commits authored under Paul's
own legal name, which no forward rule can reach and which a history rewrite would only trade for
breaking every sha citation in the corpus. It would also delete *"Mama's Perspective."* **An overstated
boundary is worse than an unstated one: it reads as a promise.**

**What the ruling accepts, stated plainly rather than left implied:** Paul's name and Mom's stay in the
public repo permanently. *That is already the world; this ruling only stops it being an accident.*

⚠️ **"We can always revisit that" — the revisit is REAL in one direction and NOT in the other.**
Tightening later (deciding Mom's name should not have been public) **cannot be executed** — 1,730
commits, a public remote, and GitHub retains objects after a rewrite. Loosening later is free.
**So (b) is a floor, not a setting.** The live consequence: the rule binds hardest on material that has
not been written yet, which is why the forward rule and the name needle are the load-bearing halves and
the existing occurrences are not.

## 7 · QUESTIONS FOR PAUL

```
Q1 · framing · The literal ask — "scrub anything even potentially PII" — measures as 6,234
     occurrences of your own given name, 3,110 of "Mom", and 1,162 commits authored under your
     full legal name that no forward rule can reach. Which rule do you actually want?
   options: a) no personal identifier in the repo (unbuildable — already false 1,162 times, and it
                deletes "Mama's Perspective")
          | b) the administrator's own identity is published by git and stays; NOBODY ELSE'S ENTERS
          | c) case-by-case, no standing rule
   recommend: b — it is enforceable, it is what you already ruled at 165f787, it is ~95% true today,
              and it generalises to estate 2 unchanged. (a) promises a coverage git itself forecloses,
              and an overstated boundary reads as a promise.
   caveat: (b) means your name and Mom's stay in the public repo forever. That is already the world;
           it just stops being an accident.
   blocks: every other step — §2's human-facing form and §3's register scope both descend from this.
           Until you rule, the seat applies (b) as the working rule and marks it agent-proposed.

Q2 · assent · fernwood-private/supplied-names.json shipped tonight at 22:40 with `names: []`.
     Extending its rows from strings to objects (adding token/class/why/ruledBy) costs nothing
     TODAY and rises with every row added. Extend it, or keep it needles-only and put the
     register in a second file?
   options: a) extend supplied-names.json into the register (one file)
          | b) a second file for the register, keep supplied-names.json as needles
   recommend: a — this corpus's measured defect is minting a second convention when one exists, and
              the scanner change is one line against an EMPTY list. In a week it is a migration.
   caveat: none — but this is the only item here with a closing window.
   blocks: §3 entirely. Nothing else waits on it.

Q3 · assent · Gap 1: nothing runs the name check before a push. CI uses --skip-needles by design,
     guard-secret-push.py only fires on an AGENT's Bash call, and .git/hooks is empty. Install a
     repo-local pre-push hook that runs check-public-build.py and refuses on non-zero?
   options: a) pre-push hook (local, uncommitted, bypassable with --no-verify)
          | b) leave it as a documented ritual before a push
          | c) block the push hard, no bypass
   recommend: a — it makes the check the DEFAULT without making it mandatory, so your standing
              "git is not gated" doctrine survives intact. (b) is what failed on 2026-07-26, when a
              person looking was the only control. (c) fights the doctrine and will get uninstalled.
   caveat: a local hook is never inherited by a clone, so it protects THIS working copy only —
           which is the only one that exists.
   blocks: nothing technically. But until it exists, every other item in §4 is a document rather
           than a control.

Q4 · framing · 3 third-party personal email addresses (2 inlined into viewer.html, on a card Mom
     reads) and 23 geographic phone numbers. For a one-proprietor nursery, "business contact" and
     "a person's mobile" are the same number, and no predicate can separate them.
   options: a) published business contact = public; only a contact given to you privately is scrubbed
          | b) any natural person's contact detail is scrubbed regardless of publication
          | c) scrub the small-operator ones, keep institutional (UGA Extension, Poison Center, dealers)
   recommend: a — it has a bright line an agent can apply without judgment ("did they publish it
              themselves?"), and it keeps sources.json useful, which is O2's substance. But this
              is genuinely a values call about other people's data, not an engineering one.
   caveat: (a) leaves a proprietor's personal gmail rendered inside Mom's viewer. Correct under the
           rule; may still not be what you want to ship.
   blocks: the sources.json / serviceContacts half of the first scrub pass. The VIN, device ids,
           MAC and EXIF do not wait on this — they are unambiguous and can proceed.

Q5 · assent · The encrypted sibling bundle is from 15:27 today. grants.json (17:01),
     people-devices.json (19:09) and supplied-names.json (22:40) all postdate it, and
     never-public-backup-check.py reports "0 stale" because its window is 30 days. Should a
     register write trigger the re-bundle?
   options: a) the write triggers the backup | b) tighten STALE_DAYS for this repo only
          | c) leave it — 30 days is fine
   recommend: a — the register is the ONLY copy of a re-identification key, and a calendar is the
              wrong instrument for a file that changes on an event. (b) narrows the window without
              closing it; (c) is what produced tonight's 7-hour gap.
   caveat: "covered" still means an artifact exists, never that it restores — the check says so
           itself. Proving a restore needs your passphrase and is not automatable.
   blocks: nothing today (the sibling is on disk and healthy). It blocks calling constraint 1
           satisfied, which no artifact should claim until this holds.

Q6 · framing · §2e: substitution forward does not scrub 1,730 commits of history, and a rewrite
     would break every sha citation in this corpus while GitHub keeps the old objects anyway.
     Confirm the 165f787 posture — forward-only, history kept — as the STANDING rule?
   options: a) forward-only, standing, and no artifact may record a pushed value as "fixed"
          | b) forward-only now, revisit if something worse than a VIN appears
          | c) rewrite history for the current findings
   recommend: a — you already ruled exactly this once, knowingly. Making it standing means the next
              agent does not re-litigate it at 11pm, and the "never record it as fixed" clause is
              what stops a trail from claiming a coverage it does not have.
   caveat: (a) requires accepting that the VIN and the MAC fetched anonymously tonight stay public.
           Neither is rotatable. That is the honest cost.
   blocks: nothing. The forward rule already stands as YOUR ruling; this only asks whether to
           generalise it. Until you say otherwise the seat applies it as written at 165f787.
```

---

## Overlaps with `practice-steward` — cited, not ruled

- **Where the public half of the register lives** (a `.decisions/` card vs. elsewhere) is siting, and
  siting is theirs. I only establish that §3b's split makes the public half **safe to site anywhere**,
  because it carries no value.
- **Who may write a register row** is role, and role is theirs. §3c constrains only the *content*
  (never a QUARANTINE value, never a credential, never a hash of a registered value).
- **When the seat runs relative to a push** is the gate, and the gate is theirs. Q3 supplies the
  measured input — CI cannot check names, and nothing currently runs before a push.
- **Decision history** is theirs to shape; §3b's `ruledBy` / `why` / `supersedes` fields are offered as
  the register's contribution to it, not as a competing home.

---

## VERDICT

**The scheme is buildable, it is about a day of work, and the hard part is not the substitution.** The
token form is easy and Paul has already set the precedent for the human-facing half by hand. The register
has a home that shipped tonight and should be extended before it has rows. The scrub position is forced:
the repo is the release — measured by anonymous HTTP 200 — so it is *never-enters* or *at-source*, and
`check-data-inline.py` and `build-viewer.py --check` do not collide with either, because a scrub is an
edit to a source and not an interception in transit. **Constraint 4 dissolves once that is stated.**

**What actually decides whether this works is §4.** Detection exists, I2 gave it the right shape, and it
is currently green over a full VIN that I fetched anonymously from `raw.githubusercontent.com` tonight —
because the enforced rows look at six files and the repo publishes 718. **Nothing runs any of it before a
push**: CI skips the name row by design, the push guard only sees an agent's tool call, and `.git/hooks`
is empty. So the honest statement of today's posture is the one from 2026-07-26, unchanged: **the only
control that has ever caught this is a person looking.** A fifteen-minute pre-push hook is the difference
between this document and a control.

**And one sentence to carry into whatever is built:** *the register is a re-identification key that is
more dangerous than the repo it protects, held on one disk whose last encrypted copy is seven hours
behind it.* Every convenience that would print it, copy it, cache it or defer its backup should be read
against that sentence first.
