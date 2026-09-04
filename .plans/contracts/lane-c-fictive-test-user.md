# LANE C — the fictive test user

Read `_PREAMBLE.md` first. It binds.

## OWNS (the only paths you may write)
- `~/Developer/Tate-Tracker/.user-research/2026-09-04-fictive-test-user.md` (new file)

## MUST NOT TOUCH
`persona-mom.md` · `persona-paul-co-steward.md` · any existing `.user-research/`
file · any research about a real person. **This lane creates one new document.**

⛔ **The hard line:** this persona is SYNTHETIC and must never be confused with,
merged into, or used to speak for Mom or Bob. Real-user research and a synthetic
test fixture are different classes of evidence. Say so in the document itself, at
the top, so a future reader cannot mistake one for the other.

## The task (Paul's 2026-09-04 memos, 1:46 and 1:47 PM ET)
Design a **fictive AI test user** that runs as a standing leg of QA and UX review:
- What does a typical first-time user expect to see, and how do they interact?
- ⭐ **Over time the persona builds its own instance of the app** — so the whole
  thing actually gets exercised end to end, not just inspected. This is the part
  that makes it more than another review lens, and it is the part to design
  carefully: what state does the instance hold, where does it live, and how does it
  not contaminate real estate data?
- It should be **durable and additive** — it runs *alongside* the blind fresh-eyes
  pass in `/ux-sweep`, not instead of it. Paul was explicit that this is *"one
  additional test,"* and the un-primed pass is the thing it must not displace.
- Extensible later to testing hypotheses about consumer segments (older users
  especially) — note the hook; don't build it now.

## Model to follow
Paul: *"we've made like a synthetic Scott Hillyer in the Hillyer case — something to
model after that."* ⚠️ **I could not locate that artifact** in `~/LocalProjects/hillyer-case`
on a quick grep. Find it and read it before designing, or report plainly that it
could not be found rather than inventing what it probably was.

## The second, separable ruling in the same memo
> *"we need to be sure that these reviews are done in desktop and mobile views, and
> that both views look really good."*

This is a **review-process rule**, not a persona feature. Propose where it wires so
it actually gets used — the `/ux-sweep` skill's contract is the obvious candidate.
Keep it a clearly separate section; do not bury it inside the persona.

## GATE (stop here and report)
The persona document plus the desktop/mobile wiring proposal. **Do not edit the
`/ux-sweep` skill** — propose the change, the hub and Paul decide.
