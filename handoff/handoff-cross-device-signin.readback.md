# Readback: cross-device-signin — "I can't sign in to my own place from my phone"

<!-- written 2026-09-10 ~9:05 PM ET by the incoming lane · brief stamped Tate-Tracker@8e93f88 · HEAD is 5ffe811
     Everything marked VERIFIED below was read from the repo at 5ffe811 in this session. Everything marked
     UNREAD is carried from the brief and has not been checked against KV, a browser, or Paul. -->

## 0. Stamp

The brief says `8e93f88`. HEAD is `5ffe811`. The only difference is the commit that added the brief itself
(`handoff/handoff-cross-device-signin.md`, 85 lines, nothing else). So the stamp is effectively current and I
trust the brief's view of the code.

⚠️ **The working tree does not match the brief's §5 dirty-file roster, in both directions.** The brief says the
two hook-generated dirty files are `worker/digest.json` and `cycle/release/cycle-state.json`. Actual `git status`:

| file | state | brief says |
|---|---|---|
| `worker/digest.json` | modified | named — matches |
| `cycle/release/cycle-state.json` | **clean** | named as dirty — it is not |
| `tools/check-backlog-ready.py` | **modified, +148/−9** | not named — and this is not hook noise, it is somebody's real work-in-progress |
| `handoff/patches/` (2 `.patch` files, 5:47 PM ET, "row-three-states") | **untracked** | not named |

The `check-backlog-ready.py` edit and the two patches look like the backlog lane's (`tate-tracker-0d`) work sitting
in the shared tree. Under the concurrent-session guard I will not commit, revert, or touch any of them, and I
will not `git add -A` anything in this lane. If the outgoing session knows whose they are, say so in the grade.

## 1. What I understand the thread to be

A **bug lane** opened from Paul's report tonight. He tried to sign in from his phone at
`fernwood-home.pages.dev/onboarding` with the `pkirsch` credentials and was refused. Same on the laptop at the
same origin. At `fernwood-home.pages.dev/estate/` the laptop was "auto-logged in" and the phone got an empty
green "My Home" shell. His underlying complaint is not any single screen: he cannot pick up his phone at the
condo and capture photos for the record or the Guru, because sign-in does not carry across devices.

The lane's job is three things, in order:

1. Explain **each of the four attempts** (phone/onboarding · laptop/onboarding · laptop/estate · phone/estate)
   by symbol, from the record and the code, not by inference.
2. Name the defect or defects.
3. Put a **ruling-shaped question** to Paul on the model underneath: *one person, one sign-in, every device,
   every place they belong to.* Recommendation plus alternatives. Rows go to the backlog session
   `tate-tracker-0d`; I do not edit `BACKLOG.md`.

Four expert seats run and write their own trails (engineering-partner path-eval, security-steward roster +
legibility, ux-expert review, user-researcher JTBD). I synthesise into
`.plans/2026-09-10-cross-device-signin-FINDINGS.md`. No build until Paul rules. Never push, never deploy, never
write to KV, never mint an invite.

## 2. Current state — what is established vs. what is inferred

### VERIFIED from the repo this session

- **Each deployment has its own KV namespace, and the account rows are deployment-scoped.** `worker/wrangler.toml`
  binds a distinct `OBSERVATIONS` namespace id per env (`fernwood` top-level, `qa`, `lab`, `home`, `bob`, `paul`).
  `home` is `ESTATE_ID = est-e6696a`, `FAMILY_HOSTS = fernwood-home.pages.dev`. `paul` is `est-d93508`,
  `myhome-paul.pages.dev`. In `worker.js`, `ACCOUNT_PREFIX = "account:"`, `USERNAME_PREFIX = "username:"` and
  `ROUTE_PREFIX = "route:"` are all **bare, deployment-scoped** keys by the code's own comments (~`:591-600`,
  ~`:1513-1519`). So the brief's core claim holds: a `username:pkirsch` index written at `paul` does not exist at
  `home`, and `POST /api/session` at `fernwood-home` cannot find him. This is the design as built.
- **The sign-in failure copy is deliberately non-specific, and that is a security choice, not an accident.**
  `handleSession` (`worker.js:870`) answers unknown-username and wrong-password with one byte-identical
  `404 {error:"not-found"}` (`deny()` at `:877`), and `onboarding/index.html` (~`:1177`) mirrors it on purpose:
  *"That username and password don't go together. Have another look — or ask Paul for a fresh link."* The comment
  says a distinguishable pair is a username oracle. ⭐ This changes the shape of finding 4 in the brief: the page
  *cannot* tell him "this account is not at this house" without a ruling that trades the oracle defence for
  legibility. That is precisely the security-steward's question, and I would not let ux-expert "fix the copy"
  ahead of it.
- **The laptop "auto-login" mechanism is the `fw-grant` localStorage key.** `estate/index.html:232` declares
  `K_GRANT = "fw-grant"`, reads it at `:261`, and calls `/api/grant/whoami` with it at `:509`. So on the laptop,
  at the `fernwood-home.pages.dev` origin, there is a stored grant token from an earlier session. **Which
  person and which estate it resolves to is UNREAD** (see §4).
- **The empty shell has TWO possible causes, and the brief names only one.** Without any `fw-grant`, the estate
  page paints its shell before a resolved grant — the brief's "bare door (J5)". But `worker.js:4455-4461` also
  returns `{hasAccount:true, estateId:null, estates:[]}` from whoami for a credential that names a person **with
  no grant at this deployment** — the "empty shelf" that the founding work made a normal state. On the phone the
  first is far more likely (his sign-in had just failed, so nothing stored the token), but a stale `fw-grant`
  from a past phone session is not excluded. The record can distinguish them; I should not guess.
- **A grant presented at the wrong deployment fails twice.** `grantFor` looks up under the deployment's own
  scope and then rejects `row.estateId !== env.ESTATE_ID`; a host mismatch also 404s (`hostAgrees`). Every one of
  those failures writes a server-side `door_failed` record with `reason: unknown-or-other-estate` or
  `host-mismatch` (`worker.js:4463-4470`). ⭐ **That means the `/estate/` attempts should be in the `door:` record
  at `home` with timestamps** — which is how I would settle "did his attempts post-date the 6:35–6:45 PM deploy"
  deterministically rather than by asking.
- **`check-storage-keys.py` reads 🔴** on `fw-journal-name` (used in three surfaces, never declared by
  onboarding). Not this lane's defect, but it is on the same key roster the brief tells me to read, so I am
  noting it rather than letting it vanish.

### UNREAD — carried from the brief, not yet checked

- That `home`'s KV held exactly one account (`marguerite`) and `paul` and `qa` each held `pkirsch`. Plausible,
  read-only to confirm, not yet confirmed by me.
- That the laptop's stored grant is on est-e6696a (the brief itself flags this as inferred).
- That `home` and `paul` serve `318416a` with byte-identical Workers, deployed 6:35–6:45 PM ET.
- "Row 33: est-e6696a now holds Mom's Fernwood record and Paul's Grant Park records." **I do not know which
  document "row 33" is a row of.** If it is true it is the most important fact in the brief, because it means
  Paul is a *grant-holder* at Mom's household without a *username index* there — which would explain all four
  attempts at once (grant works at `/estate/`, username fails at `/onboarding`). Please name the source.

## 3. The open decision

**The account model.** Today a person is a per-deployment row. Paul wants one person, one sign-in, every device,
every place he belongs to. The ruling-shaped question I expect to put to him is roughly: *do we (a) add a
deployment-independent person directory that any origin can resolve a username against, (b) add a
cross-namespace username lookup that keeps rows where they are, or (c) keep per-namespace accounts and make the
door say which house it is so he signs up once per house?* — with the engineering seat's read on what each
breaks (route rows are per-namespace by construction; `grantFor`'s legacy fallback must not move) and the
security seat's read on whether a credential minted at one household may ever be presented at another.

I will not pre-decide. But I note that **(c) is the only one that is not a build**, and the brief's own
description of the failure ("that is the design as built, not a code fault") leans toward it being at least the
honest baseline the other two are measured against.

⚠️ **A window collision I cannot resolve from here.** The brief says `tate-tracker-8d` is *designing account
lifecycle* right now and must cite my findings. My findings will not exist for hours. Either that window is
already deciding the same model without them, or it is waiting on me and nobody told it the ETA. Whoever grades
this: which is it?

## 4. What has NOT been tested or verified

1. **Which person the laptop's `fw-grant` at `fernwood-home` names, and on which estate.** Needs a read-only KV
   look at `home`'s `route:` and `est-e6696a:grant:` rows, or a `whoami` from Paul's laptop. I cannot read his
   browser's localStorage; the KV side I can.
2. **The timeline of his attempts relative to the deploy.** Readable from `door:` at `home` (server-side
   `door_failed` rows) for the `/estate/` attempts. ⚠️ For the `/onboarding` sign-in attempts I have **not**
   confirmed that `handleSession`'s `deny()` writes any door record at all — if it does not, those two attempts
   left no trace and only Paul can time them.
3. **Which deployment Paul's "pkirsch production credentials" were minted at.** The brief warns "production"
   names two things. The coordinator's sweep found `pkirsch` at `paul` and `qa`; it does not mention the
   top-level `fernwood` env (`est-3c9f1a`, the legacy Fernwood Mom actually uses). If Paul's mental "production"
   is that one, the picture has a third namespace in it.
4. **Whether the phone had a prior `fw-grant`** (empty-shelf vs. bare-door, §2).
5. **The brief's §2 KV counts** (one account at `home`, three grants at `paul`).
6. **Nothing in the brief's §2 has been walked in a browser.** All four attempts are explained by reading code.
   Once the seats have the facts, one measured walk of the two failing screens on a clean profile would turn
   inference into a record.

## 5. What looks thin in the brief

- **The sign-in copy finding is framed as a defect and the code frames it as a defence.** The brief says the
  product "produced the wrong sentence." The code says the sentence is deliberately uninformative to avoid a
  username oracle. Both are true. The brief should have said the seats are being asked to rule on a *trade*,
  not to fix a bug.
- **"Row 33" has no source.** See §2.
- **The dirty-file roster is wrong** (§0), and it omits a real WIP edit in a shared tree.
- **No mention of the `door:` record as the timing instrument**, even though `watch-door.py` exists for exactly
  "who reached the door and who got through." The brief's §6 says not to trust the timing; it does not say the
  timing is readable.
- **No mention of `check-storage-keys.py` currently reading 🔴**, while telling me to use it to name the key.
- **`.plans/2026-09-10-multi-tenancy-PLAN.md` and `handoff/handoff-fernwood-credential-path.md` exist** (checked);
  I have not read them yet, so I cannot say whether the per-namespace model was a *ruled* choice or a *default*.
  That distinction decides whether option (c) above is "the design" or "the accident."

## 6. What I would do next, in order, once Paul says go

1. **Read the record before anything else.** `watch-door.py` and `watch-accounts.py` at `home` and `paul`
   (read-only), plus a direct read-only KV listing of `route:` / `username:` / `account:` at `home`. Establish:
   who the laptop grant is, whether `pkirsch` exists at `home` in any shape, and the timestamps of tonight's
   `door_failed` rows. Check whether `handleSession` writes a door record.
2. **One question to Paul, batched:** which origin he originally set `pkirsch` up on, and whether the phone had
   ever been signed into `fernwood-home` before tonight. Two facts, no browser needed.
3. **Read the two cited plans** to learn whether per-namespace accounts were ruled or defaulted.
4. **Spawn the four seats in parallel** with the verified facts from 1–3 as their shared ground, each told
   explicitly that the sign-in copy is an oracle defence and not a typo.
5. **Write the FINDINGS**, sha-stamped, with the ruling-shaped question, and send the proposed rows to
   `tate-tracker-0d`. Tell `tate-tracker-8d` where they are.
6. Nothing is built, deployed, or written to KV in this lane before Paul rules.
