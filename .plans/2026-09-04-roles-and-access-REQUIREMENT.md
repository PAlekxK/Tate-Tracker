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

## ⭐ ANSWERED `[paul-stated 2026-09-04]` — and it collapses the design

> *"Read-only means the production one, understanding that will develop over time. The frozen
> Fernwood she already has access to — just call her **Angel**. We can give her access rights as we
> deem fit, and that's the administrative layer that no one else really needs to see. But this is the
> same journey: she has to log in, create an account, and then is presented with the options of
> viewing Fernwood, or adding a property or asset or anything like that."*

**IT IS ONE JOURNEY, NOT TWO.** Angel and Mom walk the identical flow; only what sits behind the door
differs. That retires the "option to add a property" as a yes/no step and replaces it with a
**chooser rendered from her grants**:

| | account layer | then the chooser offers |
|---|---|---|
| **Mom** | identical | *add a place* (she has no existing grant) |
| **Angel** | identical | *view Fernwood* · *add a place* |

**Consequences, all good:**
- The flow gets **built once**, and it generalises to every future person by construction — the
  chooser is a render of grant rows, not a branch per person.
- It matches §3e's invariant exactly: **a person's estates are exactly the grant rows minted for
  them.** The chooser IS that list. There is no second derivation to go wrong.
- ⭐ *"Add a place"* is offered to **everyone, always** — which answers the no-provocation tension
  from the other side. It is not a promoted affordance; it is one of the doors she is standing in
  front of, the same as any other. Nothing pushes her toward it.
- Access rights stay administrator-set and invisible: *"that's the administrative layer that no one
  else really needs to see."*

## Still open
- **Read-only is scoped to PRODUCTION Fernwood**, which does not exist yet — so this requirement
  cannot be satisfied before production is stood up. It is downstream of that, not parallel to it.
- ⚠️ **A third party reading a household's content is a consent question the current gate does not
  cover.** `administrator-reads` exists because someone outside the household reading its notes needs
  agreement — but Angel is **not** the administrator, so that entry does not describe her. On the
  FROZEN Fernwood this is moot: it is a public GitHub Pages URL, readable by anyone with the link.
  **On production it is live**, because production is where private content would accumulate. Whose
  agreement covers Angel reading Mom's notes and Guru turns, and is it a new consent scope?
- Does view-only mean everything a member sees, or a subset (notes · Guru turns · the vault)?


---

## ⛔⛔ THE CHOOSER CANNOT BE RENDERED AS RATIFIED `[practice-steward 2026-09-04; hub-verified]`

The chooser Paul ratified — *log in, then be offered what your grants allow* — **cannot be built for
a person who spans estates.** `worker.js` reads exactly ONE KV binding (`env.OBSERVATIONS`), and
`wrangler.toml` declares that same single binding once per environment. **No deployment can read
another deployment's silo.** Angel's grant at Fernwood lives in Fernwood's silo; her grant at her own
place lives in that place's silo; **nothing can see both.**

⛔ The obvious workaround is forbidden by Paul's own ruling four hours earlier: a person-level index
across silos would be *"a second derivation that could disagree with"* the grant rows.

### ⭐ IT DOES NOT BLOCK MOM
She holds **one** grant, in the `home` deployment's own silo, which that deployment reads. Her
chooser has exactly one entry and **her flow works today.** The limitation bites only when a person
spans estates — Angel, not Mom.

### Three requirements now converge on ONE engineering change
Removing the instance↔deployment weld is needed by: Angel's chooser · *"she cannot create an estate
if creating one means Paul deploying a Worker"* · practice-steward's `until`-not-`by-design` ruling,
which until tonight had no driver.

⚠️ **The cost is real.** Many estates per deployment means many estates per namespace — **the blast
radius widens from one place to all of them.** Once estates share a silo, *"reset the environment"*
stops being safe; only delete-by-prefix is. **Backup granularity must move to the prefix at the same
time as the weld comes out, never after.** ⚠️ Unverified: whether `wrangler kv` offers per-prefix
delete/restore as a primitive.

**A Paul decision, not a technicality:** is a widened blast radius an acceptable price for self-serve
estate creation?

---

## ⭐⭐ THE HIERARCHY IS RELATIVE TO THE VIEWER, AND THE THING GRANTED IS NOT ALWAYS A PLACE `[paul-stated 2026-09-05 ~3 AM ET]`

> *"It says 'what's the address of your condo' — realistically, if someone's going through the flow
> there's not going to be any indication or promise that it's a condo versus whatever. So we'll
> eventually have to think of a way to normalize around that, because in theory someone should be
> able to add a car there, or a property, or a condo — I'd like to build in the flexibility that they
> can add an individual appliance there, if possible.*
>
> *That boils back down to the theory we talked about, about different individuals having a login and
> then being presented with a menu of different options, which are at different hierarchies based on
> who logged in. So Mom may see, when she logs in, Fernwood with the vehicle nested under it — that's
> a level up. For someone else when they log in, they just see that vehicle, not nested under a
> property. That's just a generic example to demonstrate the logic."*

**Two claims, and the second is the structural one.**

### 1 · The thing a person adds is a NODE, not necessarily a place
Property · vehicle · appliance are all candidates. The onboarding surface must therefore presume no
type — the word *condo* has been removed from `onboarding/index.html` for exactly this reason (it was
a first-instance leak into an `engine` surface, the same defect class as the Fernwood green that page
already had to shed). ⚠️ **The type question belongs one step EARLIER than the address** — *what are
you adding?* — and that step does not exist. Note that an address is the right first question for a
place and the **wrong** first question for a car, so this is not cosmetic: the first-run sequence
branches on a type we currently never ask for.

### 2 · ⭐ EACH PERSON'S TREE IS ROOTED AT THEIR OWN GRANTS
The same vehicle is *nested under Fernwood* for Mom and *a top-level thing* for someone whose grant is
on the vehicle alone. **There is no single global hierarchy — there is one tree per viewer, and its
roots are exactly that person's grant rows.**

⭐ **This does not contradict the ratified model; it is that model, generalized.** §3e already says a
person's estates are exactly the grant rows minted for them, and the chooser is *"a render of grant
rows, not a branch per person… there is no second derivation to go wrong."* Paul's example replaces
**estate** with **node** in that same sentence and it still holds. The invariant survives intact:
**membership confers nothing, and containment confers nothing either** — holding Fernwood does not
imply holding the vehicle inside it, and holding the vehicle implies nothing about Fernwood.

⚠️ **What it DOES cost, stated plainly.** Three things in running code assume the granted thing is an
estate and that an estate is the addressing root:
- `grantFor()` refuses a row whose `estateId` differs from the deployment binding — one deploy, one
  estate (`worker.js`).
- Every KV key is `<estateId>:<kind>:<suffix>`. A grant on a vehicle *inside* an estate has no key
  shape today.
- `tools/grant-mint.py` mints against `--estate`, and its new G3 gate asserts the estate matches the
  environment's binding.

So this lands on **the same instance↔deployment weld** the three converging requirements above
already name. It is now a **fourth** driver, and the sharpest, because it changes what a grant POINTS
AT rather than only how many of them one deployment can see.

⛔ **NOT SCOPED. NOT STARTED.** Captured on Paul's own framing — *"something to consider as we build,
in that we want all this flexibility"* — and deliberately not designed at 3 AM. The immediate,
already-shipped consequence is only the removal of the presumed type from the onboarding copy.

⚠️ **One thing to settle before anyone builds it,** because it is cheap now and expensive later:
whether a node's *containment* is a property of the node (the vehicle knows it sits at Fernwood) or of
the grant (a person's grant says where their view is rooted). Those look identical at n=1 and diverge
the moment two people see the same vehicle at different depths — which is precisely the example above.
