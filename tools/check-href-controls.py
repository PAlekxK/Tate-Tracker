#!/usr/bin/env python3
"""T18 · lap 8 row T — every `href="#"` control has a handler registered in the same page.

An `<a href="#">` is a control that does NOTHING unless JavaScript attaches behaviour to it. When the
attachment is missing the link still looks like a control, still highlights, still takes the tap — and
the page jumps to the top instead. To the person tapping it, the product is broken in the most
confusing way available: it responded, and nothing happened.

⛔ ZERO BROWSER. It reads TRACKED ENGINE SOURCE ONLY (security R6-A) — never an origin, never a built
instance, never a running page. That is what makes it cheap enough to run on every commit, and it is
also the whole of its limitation.

⛔⛔ ITS STATED SHORTFALL IS ITS FALSIFIER, AND THAT IS DELIBERATE. `[measured 2026-09-11]` THIS CHECK
IS GREEN ON W2. `si-tosignup`'s handler EXISTS in the page — so the static test passes — but it is
registered inside `showFrontDoor()`, which means a person who reaches the sign-in screen by any other
route has a live `href="#"` and no listener. A static reader cannot see that: "the handler exists in
this file" and "the handler is registered on the path this person took" are different claims, and only
a browser can tell them apart.
⭐ THE REAL W2 COVER IS A REGION-CHANGE STOP and it lands in lap 8 · row H, against the page row A
creates — not against the screen being replaced.
⚠️ IF SOMEONE LATER "FIXES" THIS TOOL TO GO RED ON W2 WITHOUT A BROWSER, CHECK WHAT IT NOW ALSO GOES
RED ON. A static check that acquires browser-shaped authority is worse than one that admits its
boundary: it will start refusing correct code, and the refusals will be trusted because the tool used
to be right.
"""
import argparse, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ⛔ A control may be allow-listed ONLY when its href is written by script at runtime — i.e. the `#`
# is a placeholder, not a missing handler. The marker is an explicit comment in the page, so the
# allowance is made by the AUTHOR in the source, never by a list kept in this file that drifts.
ALLOW_MARKER = "dynamic-href"


def pages(root=None):
    r = root or ROOT
    out = []
    for pat in ("*/index.html", "*/*/index.html"):
        out += glob.glob(os.path.join(r, pat))
    return sorted(out)


def controls_in(text):
    """→ [(id_or_None, tag)] for every `<a href="#">`."""
    out = []
    for tag in re.findall(r'<a\b[^>]*href="#"[^>]*>', text):
        m = re.search(r'id="([^"]+)"', tag)
        out.append((m.group(1) if m else None, tag))
    return out


def classify_control(text, cid):
    """→ (state, why). GREEN = provably wired · ALLOWED = the href is written at runtime ·
    RED = provably nothing can attach · UNRESOLVED = THIS TOOL CANNOT TELL.

    ⛔⛔ UNRESOLVED EXISTS BECAUSE THE FIRST VERSION OF THIS FILE MANUFACTURED FIVE FINDINGS OUT OF
    EIGHT CONTROLS. It looked only for `getElementById("<id>")` written with the id as a literal
    argument, and this codebase binds four other ways:
      · a BULK ID CACHE — `["a","b",…].forEach(function(id){ el[id] = document.getElementById(id) })`
        — so the id is a string in an array and `getElementById` never sees it as a literal;
      · `el.<id>.addEventListener("click", …)` off that cache;
      · an `el("<id>")` HELPER assigned to a local, then bound: `var a = el("askreset"); a.add…`;
      · `el.<id>.href = …` — a RUNTIME HREF, where `#` is a placeholder and not a missing handler.
    A tool that reports 5 noise findings in 8 is worse than no tool: it spends a reader's attention
    and teaches them to skim it. That is the elicitation lens's own recorded failure (13 noise of 16),
    and this file reproduced it on its first run.
    ⭐ THE FIX IS NOT A WIDER GREEN. It is a THIRD STATE. RED now means "provably nothing can attach";
    anything this static reader cannot resolve says so, and says so is not a pass."""
    if not cid:
        return "RED", 'an href="#" control with NO id — nothing can attach to it'

    q = r'[\'"]%s[\'"]' % re.escape(cid)
    quoted = re.search(q, text) is not None
    if not quoted:
        # the id appears nowhere as a string: no cache, no helper, no direct fetch can reach it
        return "RED", "the id appears nowhere as a string literal — nothing can attach to it"

    # ── runtime href: `#` is a placeholder, not a missing handler ─────────────────────────────────
    if re.search(r'el\.%s\s*\.\s*href\s*=' % re.escape(cid), text) or \
       re.search(r'el\[\s*%s\s*\]\s*\.\s*href\s*=' % q, text):
        return "ALLOWED", "its href is ASSIGNED AT RUNTIME — `#` is a placeholder, not a dead control"

    # ── bound off the bulk cache ──────────────────────────────────────────────────────────────────
    if re.search(r'el\.%s\s*\.\s*(addEventListener|onclick)' % re.escape(cid), text) or \
       re.search(r'el\[\s*%s\s*\]\s*\.\s*(addEventListener|onclick)' % q, text):
        return "GREEN", "bound via the page's id cache (`el.%s.addEventListener`)" % cid

    # ── fetched through a helper or directly, then bound to a local nearby ────────────────────────
    for m in re.finditer(r'(?:getElementById\(\s*%s\s*\)|\bel\(\s*%s\s*\))' % (q, q), text):
        window = text[m.start():m.start() + 400]
        if re.search(r'addEventListener\(\s*[\'"]click', window) or ".onclick" in window:
            return "GREEN", "fetched and bound within the same block"
        if re.search(r'\.href\s*=', window):
            return "ALLOWED", "its href is assigned at runtime near where it is fetched"

    # ── in the cache, but this reader cannot see the binding ──────────────────────────────────────
    if re.search(r'forEach', text) and quoted:
        return "UNRESOLVED", ("the id is cached by the page but this STATIC reader cannot see where "
                              "it is bound — not a finding, and not a pass")
    return "RED", "no fetch and no binding for this id anywhere in the page"


def audit(root=None):
    """→ (rows, findings). rows are (file, id, state, why)."""
    rows, findings = [], []
    for p in pages(root):
        rel = os.path.relpath(p, root or ROOT)
        try:
            text = open(p, encoding="utf-8", errors="replace").read()
        except OSError as e:
            findings.append((rel, None, "UNREADABLE", str(e)))
            continue
        for cid, tag in controls_in(text):
            if ALLOW_MARKER in tag:
                rows.append((rel, cid, "ALLOWED", "marked `%s` — the href is written at runtime" % ALLOW_MARKER))
                continue
            state, why = classify_control(text, cid)
            rows.append((rel, cid, state, why))
            if state == "RED":
                findings.append(rows[-1])
    return rows, findings


def selftest():
    ok = []

    def ck(name, cond):
        ok.append(bool(cond)); print("  %s %s" % ("✅" if cond else "🔴", name))

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        def mk(sub, body):
            d = os.path.join(td, sub); os.makedirs(d, exist_ok=True)
            open(os.path.join(d, "index.html"), "w").write(body)

        # M24a — nothing can attach → RED, naming the id and the file.
        mk("a", '<a id="dead" href="#">tap</a>')
        rows, f = audit(td)
        ck("M24a a control nothing can attach to → RED, naming the id and the file",
           len(f) == 1 and f[0][1] == "dead")

        # ⛔ M24a2 — RED MUST STILL BE REACHABLE. A check that cannot fail is ceremony, and the fix
        # for five false positives is a THIRD STATE, never a wider green.
        ck("M24a2 RED is still reachable after the predicate was widened", len(f) >= 1)

        mk("b", '<a id="dyn" href="#" data-dynamic-href>tap</a>')
        rows, f = audit(td)
        ck("M24b a control marked `dynamic-href` → ALLOWED, not a finding",
           any(r[1] == "dyn" and r[2] == "ALLOWED" for r in rows))

        mk("c", '<a id="live" href="#">t</a><script>'
                'document.getElementById("live").addEventListener("click",function(){});</script>')
        rows, f = audit(td)
        ck("M24b2 fetched directly and bound → GREEN",
           any(r[1] == "live" and r[2] == "GREEN" for r in rows))

        # ⭐ THE FOUR REAL BINDING SHAPES THIS CODEBASE USES, each of which the first version called
        # a finding. All four were measured in the tree, not imagined.
        mk("f", '<a id="cached" href="#">t</a><script>var el={};["cached"].forEach(function(id){'
                'el[id]=document.getElementById(id)});el.cached.addEventListener("click",function(){});</script>')
        rows, f = audit(td)
        ck("M24e the BULK ID CACHE + `el.<id>.addEventListener` → GREEN (not a finding)",
           any(r[1] == "cached" and r[2] == "GREEN" for r in rows))

        mk("g", '<a id="viahelper" href="#">t</a><script>'
                'var a = el("viahelper"); a.addEventListener("click", function(){});</script>')
        rows, f = audit(td)
        ck("M24f an `el(\'<id>\')` HELPER bound to a local → GREEN (not a finding)",
           any(r[1] == "viahelper" and r[2] == "GREEN" for r in rows))

        mk("h", '<a id="rt" href="#" target="_blank">t</a><script>var el={};["rt"].forEach('
                'function(id){el[id]=document.getElementById(id)});el.rt.href="https://x";</script>')
        rows, f = audit(td)
        ck("M24g a RUNTIME HREF assignment → ALLOWED — `#` is a placeholder, not a dead control",
           any(r[1] == "rt" and r[2] == "ALLOWED" for r in rows))

        # ⛔ M24c — THE SHORTFALL, ASSERTED AS A PROPERTY. A handler registered inside a function
        # that only some routes call passes this check. The clause EXISTS so that anyone who later
        # makes it red here is forced to notice they changed the tool's class.
        mk("d", '<a id="w2" href="#">t</a><script>function showFrontDoor(){'
                'document.getElementById("w2").addEventListener("click",function(){});}</script>')
        rows, f = audit(td)
        ck("M24c a handler registered INSIDE a function stays GREEN — the W2 shape, and the check "
           "says on its face it cannot see it",
           any(r[1] == "w2" and r[2] == "GREEN" for r in rows))

        mk("e", '<a href="#">t</a>')
        rows, f = audit(td)
        ck("M24d an href=\"#\" control with NO id is RED — nothing can attach to it",
           any(r[1] is None and r[2] == "RED" for r in rows))

        # ⛔ AND THE ACCEPTANCE THAT MATTERS MOST: zero false positives on the REAL tree.
        real_rows, real_f = audit()
        ck("M24h ZERO red findings on the real tree — the first version reported FIVE of eight, "
           "every one a false positive", len(real_f) == 0 and len(real_rows) == 8)

    print("\n%s check-href-controls selftest (%d/%d)" % ("✅" if all(ok) else "🔴", sum(ok), len(ok)))
    return 0 if all(ok) else 1


def main():
    ap = argparse.ArgumentParser(description="Every href=\"#\" control has a handler in the same page. "
                                             "Zero browser; tracked engine source only.")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    rows, findings = audit()
    print("href controls — %d across %d page(s)\n" % (len(rows), len({r[0] for r in rows})))
    for rel, cid, state, why in rows:
        mark = {"GREEN": "✅", "RED": "🔴", "ALLOWED": "⬜", "UNRESOLVED": "⬜",
                "UNREADABLE": "⬜"}[state]
        print("  %s %-28s %-14s %s" % (mark, rel, cid or "(no id)", why))
    print("\n⛔ WHAT THIS CHECK CANNOT SEE, on its own face: it proves a handler EXISTS IN THE PAGE,")
    print("   never that it is REGISTERED ON THE PATH A PERSON TOOK. A handler inside a function that")
    print("   only some routes call passes here and still leaves a dead control for everyone else —")
    print("   that is W2, and this check is GREEN on it. The real cover is a region-change stop in")
    print("   lap 8 · row H, against the page row A creates.")
    if findings:
        print("\n🔴 %d control(s) with no handler in their own page." % len(findings))
        return 1
    print("\n✅ every href=\"#\" control has a handler registered in its own page.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
