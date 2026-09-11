# Handoff: fernwood — BUG LANE · "I can't sign in to my own place from my phone"

<!-- generated 2026-09-10 ~7:20 PM ET · source: Tate-Tracker@8e93f88 on LOCAL main
     RECEIVER: verify the sha against HEAD. Cite the symbol, stamp the sha. -->

## 1. The report — Paul's words, verbatim, 2026-09-10 evening

> *"I went to this link on my phone and tried to sign in and it didn't accept any of my credentials. I used my
> pkirsch production credentials. I actually also just tried logging in on the laptop here and I'm not able to
> get in."* — `https://fernwood-home.pages.dev/onboarding`
>
> *"Using that link I'm auto-logged in on my computer. On my phone, it just takes me to the generic empty My Home
> green page with all the empty cards."* — `https://fernwood-home.pages.dev/estate/`
>
> *"This is an important issue… maybe this does tie into ensuring that devices are synced automatically with the
> accounts and being able to access from different devices, but this is a big usability issue for me right now.
> For example I can't just pick up my phone and take pictures of stuff in my condo to share with you, or with the
> Guru."*

**Mission:** find out exactly what happened on each of the four attempts (phone/onboarding · laptop/onboarding ·
laptop/estate · phone/estate), name the defect(s) by symbol, and put to Paul a ruling-shaped answer to the
product question underneath: *one person, one sign-in, every device, every place they belong to.* You are a
**dedicated lane** with expert seats. You may build a fix only after Paul rules; you may measure anything.

## 2. What the coordinator measured before opening this lane — start here, verify it

1. **`fernwood-home.pages.dev` is Mom's household** (`home`, est-e6696a). **Paul's condo is `myhome-paul.pages.dev`**
   (`paul`, est-d93508). Accounts live **per deployment namespace** — each household has its own KV namespace
   (`worker/wrangler.toml`), and `route:<sha256(token)>`, `username:` and `account:` rows are written into the
   namespace of the deployment that created them. The `home` store held **one** account at tonight's sweep
   (`marguerite`, Mom's); the `paul` store held `pkirsch` (3 grants, all routed); `qa` also held `pkirsch`.
   **So `pkirsch` at `fernwood-home` cannot resolve: the username index is not in that namespace.** That is the
   design as built, not a code fault — and it is exactly the usability wall he hit.
2. **The laptop "auto-login" at `/estate/`** is almost certainly a **stored credential in that origin's
   localStorage** from an earlier session (the migration/onboarding work of 09-04 → 09-08 signed Paul in at
   `fernwood-home` as Mom's stand-in, and the sunset-banner path). Read `estate/index.html`'s whoami consumer and
   the storage-key roster (`check-storage-keys.py`) to say which key, and **which person/estate that credential
   resolves to** — if it is a grant on est-e6696a, he was auto-signed-in *as a member of Mom's household*, which
   is a finding of its own (row 33: est-e6696a now holds Mom's Fernwood record and Paul's Grant Park records).
3. **The phone's "empty green My Home page with empty cards"** at `/estate/` with no stored credential is the
   **bare door (J5)** rendering: the estate page paints its shell before/without a resolved grant. Whether it
   should instead route to the door with a sentence is a design question the seats answer, not a guess.
4. **"Didn't accept any of my credentials" is the wrong sentence for what happened** and the product produced
   it: the page cannot tell *wrong password* from *this account is not at this house*. Find the copy at
   `onboarding/index.html` (`/api/session` failure branch) and the Worker's response codes for
   *unknown username* vs *bad word* (`POST /api/session` handler, `worker.js`).
5. **What just shipped there:** both `home` and `paul` serve `318416a` (pages) with Workers byte-identical to it,
   deployed ~6:35–6:45 PM ET tonight. If his attempts were after that, they were against the founding build.
   `grantFor()`'s legacy fallback is load-bearing for pre-existing credentials — **do not touch it.**

## 3. Seats to run (each writes its own trail; you synthesise)

- **engineering-partner (path-evaluation):** the per-namespace account model vs. "one person, any device, any
  place" — what a person-level index would look like (a deployment-independent `person:` namespace, or a
  cross-namespace username directory), what breaks (grantFor's route rows are per-namespace by construction),
  and the smallest honest change that lets `pkirsch` sign in at any origin he belongs to. Cite
  `handoff/handoff-fernwood-credential-path.md` and `.plans/2026-09-10-multi-tenancy-PLAN.md`.
- **security-steward (roster + legibility):** may a credential minted at one household be presented at another
  household's origin? What does the person need to be able to *tell* when a sign-in fails? (⛔ it may never
  report "no vulnerabilities found".)
- **ux-expert (review):** the four screens he met — what each should have said; the empty-cards page; the
  sign-in failure copy; the cross-device "pick up my phone and take a photo" job.
- **user-researcher (research):** the JTBD behind the report — capture from the phone at the condo, share with
  Paul-the-admin and with the Guru — tagged assumption | inferred | validated.

## 4. Deliverables

1. `.plans/2026-09-10-cross-device-signin-FINDINGS.md` — the four attempts explained by symbol; the defects
   named; the seat trails linked; **the ruling-shaped question for Paul** (question · recommendation ·
   alternatives) on the account model; rows proposed for the register (send them to `tate-tracker-0d`, the one
   door — you do not edit `BACKLOG.md`). Stamp the sha.
2. A **readback first**, per the launcher, before any of the above.

## 5. Guardrails — Paul's

Never push `origin/main`. **Never deploy anywhere** in this lane. Never delete or rewrite a credential, route
row or account — read only in KV. Never mint an invite. Coordination window is `paulkirschenbauer-96`; the
backlog session is `tate-tracker-0d`; the design window `tate-tracker-8d` is designing account lifecycle and
must cite your findings, not re-derive them. Two hook-generated files are dirty (`worker/digest.json`,
`cycle/release/cycle-state.json`) — never commit them.

## 6. What NOT to trust here

That the laptop credential is on est-e6696a (inferred, unread). That his attempts post-dated the deploy. Every
`file:line`. The word "production" — it names two things; use the deployment name.
