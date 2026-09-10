# Nothing on the open web — the requirement, and where we actually stand

`[paul-ruled 2026-09-10]` — *"ideally everything is private, right? None of this should be available
online. You should have to log in, so that users have confidence their information is not posted on
the web or anything like that. That's a clear requirement."*

**Measured the same hour, against the live origins.** Not asserted.

## ✅ WHAT IS ALREADY TRUE — a household's information is NOT on the web

**Every data route refuses an unauthenticated caller** (`fernwood-home`, no credential):

| route | answer |
|---|---|
| `/api/observations` · `/api/feedback` · `/api/zones` · `/api/conversations` | **401 unauthorized** |
| `/api/grant/whoami` | **404** — an unknown credential is not told it guessed wrong |

**And the household's built app carries no household record.** `fernwood-home.pages.dev/viewer`
inlines `PLANTS_DATA`, `ZONES_DATA`, `VEHICLES_DATA`, `BIRDS_DATA` as
`{"_meta":{"declaredAbsent":true}, …: []}` and `PROPERTY_DATA` as the neutral shape. **A household's
records live in KV behind its grant and are not in the page.** That separation works today.

⭐ So the core of the requirement — *their information is not posted on the web* — **holds for
household data right now.**

## 🔴 WHERE IT DOES NOT HOLD, four gaps, in order of seriousness

### 1. Fernwood's entire record is public, with no login
`https://palekxk.github.io/Tate-Tracker/viewer.html` — **HTTP 200, 2,062,839 bytes, titled
"Fernwood."** The legacy GitHub Pages build, served from `origin/main`. It carries the address, the
plants, the zones, the vehicles, the property file.

⚠️ **This is Paul's own record and he published it deliberately, long before the requirement
existed.** It is a decision to revisit, not a bug to fix quietly. But it is the largest single thing
standing against *"none of this should be available online."*

### 2. Fernwood's data is inside every OTHER household's page
Needles found in the **public `fernwood-home` build**: `2,873` · `Jasper` · `34.5496` · `OUR GAUGE`
· `Fernwood`.

⛔ **This is the 2026-09-07 finding, still live.** CLAUDE.md already records why the guard misses it:
`check-estate-neutral` *"TESTS FOR NAMES"*, and that leak was *"NUMBERS AND POSSESSIVE PRONOUNS."*
These are engine literals, the same class as the 60 in the model prompts — **one household's facts
shipped in another household's app.**

### 3. The app SHELL is publicly loadable
Every origin answers **200 to anyone**: `fernwood-home` · `myhome-bob` · `fernwood-qa`. No Cloudflare
Access, no login wall. The *data* behind it is gated; the *page* is not.

⚠️ **And the URL itself discloses.** `myhome-bob.pages.dev` existing tells a stranger that a
household exists for someone called Bob. ⭐ **The one-production-environment move dissolves this** —
one origin for everyone names nobody.

### 4. The repo is public
`PAlekxK/Tate-Tracker` is public with `instance/` tracked. Fernwood's canon is in it by choice.
⛔ **Nobody else's may ever be** — enforced in code as of today: `derive-property.py` runs
`git ls-files` on its target and **refuses to write a filled property record anywhere git tracks.**

## WHAT FOLLOWS

| | | owner |
|---|---|---|
| **P1** | strip the Fernwood literals out of the engine — gap 2, and the same work as the 60 prompt literals | agent |
| **P2** | decide what happens to the public legacy Fernwood build — gap 1 | ⛔ **Paul** |
| **P3** | put the app behind login, or accept a public shell over gated data — gap 3 | ⛔ **Paul** |
| **P4** | keep every household's record off tracked disk — gap 4 | ✅ **enforced in code today** |

⭐ **P3 is a real product question, not a defect.** A public shell over gated data is how most web
apps work, and the *"you have to log in"* experience is already true — a stranger loading the page
gets an app with nothing in it. Whether the page itself must also be walled is Paul's call, and it
has a cost: Cloudflare Access on a household origin means Mom meets a second login before the app's.
