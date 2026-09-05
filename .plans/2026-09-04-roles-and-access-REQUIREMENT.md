# Roles and responsibilities — a VIEW-ONLY role, and self-serve estates `[paul-stated 2026-09-04]`

> *"I wanna add to our requirements the concept of roles and responsibilities. There should be a
> view-only role. For example, I have a user that I want to invite with read-only on Fernwood, but
> the ability to create her own estates if she ever wants to or explores it, with no provocation."*

⛔ **CAPTURE ONLY. Nothing scoped, nothing decided, no build started.**

## What the ratified model already gives us (`VOCABULARY.md` §3e, `paul-ratified 2026-09-03`)

- Grants are keyed `(personId, estateId)` — so **one person can hold different standing at different
  estates by construction.** Read-only at Fernwood and owner at her own place is not a special case.
- Two axes exist: `relationship` (owner · contributor · member) and `capability` (administrator ·
  member), plus `entry` / `vault` — *what the credential opens*.
- ⭐ **THE INVARIANT: membership confers nothing.** A person's estates are exactly the grant rows
  minted for them, never derived from family. The family→estates map stays deliberately unbuilt.
- ⭐ **The founding-owner bootstrap already anticipates self-serve:** a founding grant is legitimate
  *"under the bootstrap repair — the prospective owner's own **request** is the entire warrant."*

## The two gaps this requirement opens

### 1 · There is no access axis today, and `relationship` must not become one
§3e is explicit: **`relationship` is NOT an access axis** — it exists for the consent gate and the
activation rule, and *"anything that reads `relationship` to decide reachability is the defect this
line names."* So **view-only cannot be `relationship: member`.** It needs either a real verb axis
(read vs write) or an extension of `entry`/`vault` — and `entry`/`vault` describe **doors**, not
**verbs**, so they are the wrong shape as they stand. ⚠️ This is the trap to avoid: `member` reads
like it already means view-only, and it does not.

### 2 · ⭐⭐ "With no provocation" forces BOTH deferred engine questions from *eventually* to *now*
For her to create her own estate spontaneously:
- **The estate must be creatable without a deployment.** Today `ESTATE_ID` is a per-environment
  binding — one deploy, one estate. She cannot create an estate if creating one means Paul deploying
  a Worker. ⚠️ practice-steward ruled 2026-09-04 that this must be recorded as **`until`, never
  `by-design`** — the key scheme is *already* multi-estate (the prefix exists so estates can share a
  namespace, and QA's namespace holds three estates' keys today); `grantFor()` merely *compares* the
  grant's estateId to the binding rather than *resolving* from it, and `worker.js:376` says C6 later
  passes the grant-resolved id through the same signature. **This requirement is the driver for that
  work.**
- **The founding grant must be authorable by her.** §3e already supplies the *rule* — her own request
  is the warrant. What is missing is a **surface for her to make the request through**. The rule is
  ready; the door is not.

## The design tension worth naming before anyone builds it
*"No provocation"* means the affordance exists and is never pushed. That runs directly into
[[feedback_defer_affordances_pending_signal]] — a standing "create an estate" button is the
affordance-without-signal trap, and Fernwood's own measured evidence is that every affordance which
**asks** got zero taps while the one that **moves** got 100%. So the question is not *where does the
button go*; it is **what does she have to already be doing for creating a place to be the obvious
next move.** That is a research question, not a UI one.

## Open, for Paul
- Who is this person, and does read-only at Fernwood mean the **frozen** instance or the production one?
- Does view-only see everything a member sees, or a subset (Mom's notes? Guru turns? the vault)?
  ⚠️ The administrator-reads consent gate exists because someone outside a household reading its
  notes is a consent question — a view-only role inherits that question, it does not escape it.
