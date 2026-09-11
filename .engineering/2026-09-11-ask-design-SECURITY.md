# ASK DESIGN — security-steward read · mode ① ROSTER (with one ③ LEGIBILITY constraint list)

<!-- filed verbatim by the ask-design window (tate-tracker-52) from the seat's return, 2026-09-11 — the seat holds no
     write tool. Commissioned by `.plans/2026-09-11-ask-design-PLAN.md` §4a. Nothing edited; the seat's own
     denominator and falsifiers stand as written. -->

Repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`. **Symbols cited; line numbers are as read in the working tree this session, uncommitted changes present in `worker/worker.js`.** I have no `Bash` and could not stamp a sha — trust the symbol, not the number.

---

## DENOMINATOR FIRST

**Read and verified by me:** `worker/worker.js` symbols `PERSON_UNKNOWN`, `declarePerson`, `attributeToPerson`, `attributeTo`, `stampVia`, `writeEstatePlace`, `handleEstateFound`, `personFor`, `ACCOUNT_SURFACES` + its comment block, `feedbackDestination`, `accountFeedbackKey`, `handleFeedback` (POST and GET), **both router call sites for `/api/feedback`** (`:4209` above the gate with `fbGrant`, `:4847` below it with no grant), `ADMIN_ONLY`/`MEMBER_OK` + the unclassified-route fail-closed, `handleRecoveryRead`, and a census of every `keyFor(scope*, …)` estate-level singleton · `VOCABULARY.md` §2, §3b, §3e, **§3e·R**, §3f, §3i, §4 · `.plans/2026-09-03-privacy-scrub-PROPOSAL.md` §1 (the charter, whole) · `.engineering/2026-09-10-recovery-route-SECURITY.md` (my own, whole) · `tools/elicitation-lens.py` `CONTRACT` + `contract_of` + the first-run noise block · `handoff/handoff-ask-design.md` §4 item 4 (the ask-ledger spec) · `CLAUDE.md` § AI boundary, § EVERY ITEM SHIPS WITH AN ASK, § check-canon-scope, § watch-activity.

**NOT checked, each of which could change a ruling:**
- ⛔ **`.plans/2026-09-02-data-model-design.md` §7 DOES NOT EXIST at the path I was given** — it is in the private sibling (`../fernwood-private/`), outside this repo. **I ruled the administrator-consent clause from `CLAUDE.md`'s restatement and `VOCABULARY.md` §3f, which are second-hand.** The load-bearing prerequisite in ruling ③ rests on a paraphrase. Someone must read §7 itself before that gate is built.
- I did not read `questions.json`, `MomQueue`/`buildCard` in `viewer.html`, `onboarding/index.html`, or any card-intro surface — **so I have not seen the ask.** Everything below rules on the record, not the screen.
- I did not read `.plans/2026-09-11-lap8-build-PLAN.md` or the lap-8/9 scope. If the ledger is already specified there, mine is the second voice.
- **No probe, no live KV, no deployed-Worker comparison, no route-table enumeration** — the third consecutive run with that hole, twice previously stated and still unclosed.

---

# ① ROSTER — per tier (`estate × person × credential class`)

Credential classes in play: **none** · **member grant** · **owner grant (`capability: administrator`)** · **master token (application administrator)**.

### 1 · The preference declaration on the estate record

**Value class: PREFERENCE (an interest). Not a value** — UV/AQI/pollen derive from the address already on the estate record. ✅ That is the correct shape and it is `elicitation-lens`'s own thesis: **one asked field, many derived facts.**

**✅ SUBJECT: the ESTATE. ⛔ NOT the grant.** A grant is authorization class; an interest is content about how the place is read. And `tools/grant-mint.py`'s `PLACE_FACTS` mirrors the grant's field list under a **selftest clause that binds them**, so widening the grant writes preferences into `fernwood-private/grants.json`, the register. ⛔ Refused — this is RR-1's boundary in the same direction.

**✅ SHAPE: copy `writeEstatePlace()` field-for-field.** It is the ruled model of a declaration on an estate record: `declaredBy` · `declaredAt` · `placeSource` (`self · attested · fixture`). A preference row gets `declaredBy: personId` · `declaredAt` · `declaredVia: "card-intro"`.

**✅ WHO MAY WRITE: any member.** This is the **first member-authored estate-record write in the product** — measured: every estate-level singleton today is either founding (`place`) or `ADMIN_ONLY` (`zones`). It is therefore a genuinely new tier and exactly what the roster exists for. ⛔ **Owner-only would be the ruling that costs input**: Mom is a member at a house she does not own, and a rule that stops her shaping the card she actually opens defeats the ask.

> ### ⛔⛔ THE ONE THING THAT MUST NOT BE BUILT: A SINGLE-WINNER PREFERENCE
> `writeEstatePlace`'s own comment records the defect in Paul's system already: *"electing from member rows put Paul's real home address into a test estate's Guru prompt, and it looked entirely reasonable because every estate had exactly one placed member."* That is `publish-digest.household_property()`'s rank-election, and **a preference is a SET across people, so it invites the identical bug.** The estate row must hold the **union**, each element carrying its own `declaredBy` — never a winner picked by rank, recency, or iteration order. ⭐ It is free to get right today because nobody has written one; it is a migration the day two people have.

**⚠️ WHAT IT REVEALS ABOUT A PERSON, and it is the real finding here.** `declaredBy` on a member-readable estate row means **member B can read that member A asked for pollen and air quality.** Those are health-adjacent inferences (allergy, asthma, cardiac/respiratory sensitivity) about a named person, sitting in a tier any member grant reaches.

⛔ **The remedy is NOT to strip `declaredBy`** — that destroys the ribbon's attribution, which is the only trust credit this ask generates, and it is the control that costs input. **The failure is not visibility; it is undisclosed visibility.** Ruling: ✅ `declaredBy` may exist, **conditional on the ask itself disclosing who sees the answer** — `elicitation-lens.CONTRACT["who-sees"]` is not decoration, it is the clause that makes this row legal. A preference a housemate can see is fine if the person was told before the tap. ⛔ Not told = out of tier.

- `settled_by`: code read (`writeEstatePlace`, the `keyFor` singleton census, `MEMBER_OK`). `authority_checked: **true**` for the tier; **`false`** for "a health inference is the right class for a weather interest" — that is a judgement I made, not a measurement.
- **Falsifier:** `grep -n 'keyFor(scopeOfRoute\|keyFor(scopeOf' worker/worker.js` — if any estate-level singleton is already member-writable, the "first of its kind" claim is void. And `python3 tools/grant-mint.py --selftest` must still pass **without** `PLACE_FACTS` widening.

### 2 · The feedback record that captures the tap

⛔ **`context` IS NOT A TRUSTED FIELD, and the Worker says so in its own comment** (above `ACCOUNT_SURFACES`, measured 2026-09-10 *"against a claim that it was bounded"*): free-form client JSON, capped at 2048 bytes, **no server-side surface roster anywhere.**

> **Consequence the spec must absorb: the client chooses the record's namespace.** `feedbackDestination(grant, context)` sends the tap to `account:<personId>:feedback:<date>` if `context.surface` ∈ {`onboarding`,`homes`,`account`}, and to the estate stream otherwise. Both are legal destinations the server pre-approved — but which one a card-interest tap lands in is decided by the page.

| field | ruling |
|---|---|
| `context:{type:"card-interest", card:"weather", askId}` | ✅ — **and `surface` must be OMITTED**: a preference about the place belongs in the estate stream, with the estate declaration it mirrors |
| `personId` / `estateId` | ✅ **only via `attributeTo(record, grant)` from the resolved grant.** The POST path at `:4209` resolves `fbGrant` when `X-Grant` is presented — that is the one legal writer. Never from the body |
| `sentiment` | ✅ — required in practice: `handleFeedback` **rejects** a record with neither sentiment nor note (`need-sentiment-or-note`). A bare interest-tap with no note must map its tap to the sentiment enum or it 400s |
| `deviceId` | ⛔ **FORBIDDEN ON AN ATTRIBUTED RECORD.** ⚠️ **This is live in running code, not a spec risk:** `handleFeedback` copies `deviceId` from the body unconditionally, then `stampVia` attributes the person — so an attributed row **can carry both today**. A deviceId beside a personId is the browser-bucket→person join that `watch-activity.py`'s own rule refuses to assert. The ask makes it routine. *(Fix is engineering-partner's; my ruling is only the tier.)* |
| `sessionId` | ⛔ **FORBIDDEN** — a join key into `/api/metrics` batches. Same ruling as the recovery route |
| the derived value (a UV index, an AQI number) | ⛔ **FORBIDDEN at rest beside the person.** The derivation runs one way, address → reading. A stored reading beside a personId is a location trace wearing a weather label |

**Forbidden joins, named:** `personId × deviceId` · `personId × sessionId` · `personId × door records` (door carries `personId:null` by construction — ⛔ do not "repair" that) · `preference × coordinates`.

### 3 · The free-text answer

✅ **Verbatim, bounded (the 2000-char slice already exists), AI-free on the capture path.** That is settled doctrine and this ask changes nothing about it.

⚠️ **Tier: the estate stream, `MEMBER_OK` `[paul-ruled 2026-09-10]` with the consequence stated to him.** At `est-e6696a` the other member reads it.

> ### ⛔ A FREE-TEXT FIELD'S TIER IS SET BY THE WORST THING THE PROMPT INVITES, NOT BY WHAT IT EXPECTS
> *"Anything else about the weather here?"* is an open door onto health ("my wife's asthma"), absence ("nobody's there Nov–March"), and neighbours — none of which the estate-stream tier or the forward rule can hold. ✅ **Build the box** — `read-onboarding.py`'s own framing is that this is *the only line where someone can name a need we never anticipated*, and removing it is the control that costs the most input. ⛔ **Bound the PROMPT to the card** ("what else about the weather at this place should the card show?"). An unbounded *"anything else"* is out of tier by construction.

⛔ **Never in a tracked file.** CLAUDE.md § QUARANTINE + the forward rule + `watch-feedback.py`'s *"her words stay in `.private/`"*. The ledger (④) reads counts and must be structurally unable to read a note.

⛔ **THE ADMINISTRATOR-AT-A-NON-FAMILY-ESTATE GATE FIRES HERE, AND THIS ASK IS ITS TRIGGER.** VOCABULARY §3f: *"that agreement is owed to Bob before his daughters write anything, and it is Paul's to get."* A free-text weather box **is** first contributor input.

> **ROSTER ROW (proposed) RR-8:** *A free-text ask may be enabled at an estate only where the administrator holds a relationship there, OR an `administrator-reads` consent entry exists on the grant (VOCABULARY §3e's gated row).* ⚠️ That consent list ships with C6 3a and **does not exist today**, so the honest state is: ✅ enabled where the administrator is a member (`legacy`, `home`, `paul`, `qa`, `lab`); ⛔ **refused at Bob's, and at every estate founded by a stranger.** ⚠️ Rests on a second-hand read of §7 — see the denominator.

### 4 · The ledger's "counts, never people"

> ### ⛔ THE CASE WHERE A COUNT **IS** A PERSON IS NOT AN EDGE CASE — IT IS EVERY PRODUCTION NUMBER TODAY
> `legacy` holds **Mom, alone**. `home` holds **one account**. `paul` holds **Paul**. So a per-estate row reading `weather-interests · served 1 · answered 1 · folded into: UV` is **a full disclosure of what Mom asked for, with a number in front of it.**

⚠️ **And k=2 is not anonymity either:** at a two-member estate with one answer, the other member knows it was not them. A per-estate ask count is a claim about an individual until an estate has ≥3 people who could have answered — and **the ledger cannot establish that number from its own inputs.**

**RULING — and it is the simple one, deliberately:**
- ✅ **The ledger reports per-ASK, per-ENV totals. It does not report per-estate, at any size.** Per-estate reading belongs to the administrator's own read of their own household, not to a portfolio instrument. This costs nothing real: the question the ledger exists for (*which asks land*) is answered at the ask level.
- ✅ `lab`/`qa` are fixtures — counts free, and they are where the ledger earns its keep.
- ⛔ `production` and `legacy` — where n is 1, print **`n=1 — not reported`**, a state distinct from `0` and from `unread`. ⚠️ *That string itself leaks that someone answered.* If even that is too much, the honest form is to omit the env, and say the env was omitted and why.
- ⛔ **Structurally unable to read a note.** Its inputs are the ask register, `questions.json`, card intros, and count queries. A tool that can read a note will one day print one.

**Exit 3 UNREADABLE — what it must refuse to read, never green by absence:**
1. an env whose KV it cannot reach;
2. **an estate whose answerer count it cannot establish** — ⛔ never assume ≥3;
3. a range where `served` is derivable and `answered` is not — **a ratio with an unknown denominator is the exact false-green this corpus is built against**;
4. **a legacy unprefixed key era** — `watch-activity.py`'s measured trap: 94 unprefixed `metrics:` keys and zero under the prefix, so *absence under a prefix is a fact about the prefix, not about the world*;
5. an ask present in `questions.json` with no row in the register (the four-field contract's own failure mode: an ask with no reader).

### 5 · The attribution ribbon in a shared household — ③ LEGIBILITY

⛔ **It may NOT name which member's answer changed the card, and it may not say "you."** In a shared house one surface is read by several people: *"your answer changed this"* is **false for every reader but one**, and it is simultaneously a **disclosure** — it tells member B that member A asked for pollen, on a surface B never consented to read.

✅ **Permitted posture: attribute to the ACT and the PLACE, not to the reader.** The declaration row already carries `declaredBy` and `declaredAt`; the ribbon renders that something was asked for *here*, and when.

**Constraints for content-steward — the list, not the sentence:**
1. ⛔ No second-person possessive on a shared surface. "You/your" is an unverifiable claim about who is holding the phone.
2. ✅ It may name the ACT and the DATE (both on the row). It may name the PERSON **only where the estate holds exactly one grant**, and that condition is **computed at render**, never assumed — the single-member assumption is the one that put a real address in another estate's prompt.
3. ⛔ It may not imply the preference is private to the person who set it. It is on the estate record; every member sees the card change.
4. ⭐ **The who-sees clause belongs to the ASK, not the ribbon.** Disclosure after the tap is not disclosure. `elicitation-lens.CONTRACT` grades presence; this is the one clause whose absence makes the record itself out of tier (ruling ①).
5. ✅ "Everything is changeable" applies — **and it must be true**: if the interest can be turned back off, the copy says where.
6. ⛔ No sentence may claim the interest is not used elsewhere. If enabling pollen adds a **third-party request**, the day-one roster row (*no third-party request from a household surface, ever* — measured true today, enforced nowhere) fires, and the copy must not pre-empt a ruling nobody has made.

---

## ⚠️ TWO THINGS I FOUND THAT ARE NOT IN THE BRIEF

1. **`GET /api/feedback` reads `dateKey(scopeOf(env), …)` — the DEPLOYMENT's scope, not the caller's.** `scopeFor(request, env, grant)` exists and is used for canon routes; the feedback read does not use it. Harmless while a deployment holds one household. ⛔ **The lap-8 single-origin production (VOCABULARY §3i step 3) makes every member's feedback read a cross-household read, silently, on the day the deployments collapse.** The same shape holds for `zones`. This ask puts preference declarations and free text into exactly that stream. *(`settled_by`: code read. `authority_checked: true` for the call sites; `false` for what lap 8 will do — I did not read its plan.)*
2. **The recovery-channel precedent is already the right answer to R-B and it is in the tree:** `/api/recovery` is `ADMIN_ONLY` with its own key. **If Paul wants the free-text answers out of the member-readable tier, the mechanism exists and has shipped once.** Cost: it leaves the mom-cycle sweep, which is where her words are meant to arrive. Not mine to choose.

---

## THE CLOSE

**✅ MAY BE BUILT AS DESCRIBED**
- The preference declaration on the **estate** record, `writeEstatePlace`'s shape (`declaredBy`/`declaredAt`/`declaredVia`), **any member may write**, union-not-election.
- The tap as a feedback record with `context.type:"card-interest"` and `surface` omitted, attributed via `attributeTo` from the resolved grant at `:4209`.
- The free-text box — **bounded prompt**, verbatim, AI-free, `.private/` only.
- A derived ask ledger — **per-ask, per-env**, exit 3 on all five refusal conditions.
- The ribbon attributing the **act and the place**.

**⚠️ MUST CHANGE IN SPEC**
1. **The ask must disclose who sees the answer, before the tap.** Without it, `declaredBy` on a member-readable row is out of tier. This is a build-blocking dependency on content, not a polish item.
2. **Union, never election**, on the preference set — with the `household_property()` defect cited in the spec so the next writer knows why.
3. **`deviceId` must be null on any record carrying a personId** — live defect, not a new risk.
4. **`sessionId` forbidden**; `context` must not be trusted for any access or routing decision the server cares about.
5. **The ledger does not report per-estate.** Production and legacy are n=1 today; "counts, never people" is false there by arithmetic.
6. **Free text is gated per estate** on the administrator's relationship or an `administrator-reads` consent entry (RR-8) — and **someone must read `../fernwood-private/.plans/2026-09-02-data-model-design.md` §7 directly**, because I could not.

**⛔ MUST NOT**
- The preference on the **grant** row (authorization class; drags it into the register via `PLACE_FACTS`).
- A single-winner elected preference.
- The derived value (UV/AQI reading) stored beside a person.
- `"your answer changed this"` on any surface an estate with >1 grant can render.
- An unbounded *"anything else"* prompt at the estate tier.
- A per-estate answered-count at production or legacy.

**⛔ WHERE A CONTROL WOULD COST INPUT — stated because the seat's purpose is earning it.** Owner-only writes would lock Mom out of shaping her own card. Stripping `declaredBy` would kill the ribbon's attribution, which is the only trust credit this ask generates — **prefer disclosure over suppression.** Deleting the free-text box would close the only line where someone names a need nobody anticipated. A blanket consent gate would block nothing at four of five estates and cost a screen. In each case the cheaper control is **telling the person**, and in each case it is also the honest one.

**⛔ THE HONEST SHAPE OF THIS RUN.** **I have not seen the ask.** I read no card, no `questions.json`, no onboarding screen — so every ruling above is about the record and none of it is evidence that the screen asks well. I ran no probe and read no live KV, so the n=1 claim in ④ rests on `wrangler.toml`-derived prose in `CLAUDE.md`/`VOCABULARY.md`, not on a member count I measured. **I could not open the consent clause that ruling ③ turns on.** And for the third consecutive run I did not enumerate the route table — if a real failure in this surface is found by someone else, it will be in a route I have never read, or in the deployed Worker, which I have still never compared to the tree. Per the falsifier: if that happens, **this denominator did not name it.**
