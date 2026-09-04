#!/usr/bin/env python3
"""guru-probe.py — asks the Guru the derived facts (guru-facts.py) on the QA WORKER ONLY (Guru plan 3a/3c).

Resolver (3a): FERNWOOD_QA_TOKEN or .private/fernwood-qa-token, and FERNWOOD_QA_WORKER_URL — NO fallback
to momlib.resolve_token() (that is the prod token). Before any row it reads /health and REFUSES unless
env=="qa" && kv_canary=="qa" (the qa-write-probe shape): a probe that could point at prod would spend
Paul's budget and write conversations Mom's readers count.

The live leg (3c) is Paul's to cap (Q1): it runs only with --live and --max-turns N (a convenience, NOT
load-bearing — the Worker-side ceiling on QA is, 3b). Grading is inverted: a row is red when the answer
carries a must-NOT (the stale self, the confusable sibling) even if the right number is also there.

    python3 tools/guru-probe.py --selftest
    python3 tools/guru-probe.py --live --max-turns 3        # QA only, origin "test"
"""
import argparse, json, os, re, sys, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
QA_URL = os.environ.get("FERNWOOD_QA_WORKER_URL", "https://fernwood-qa.paul-kirschenbauer.workers.dev").rstrip("/")
QA_TOKEN_FILE = os.path.join(ROOT, ".private", "fernwood-token-qa")


def resolve_qa_token():
    tok = os.environ.get("FERNWOOD_QA_TOKEN", "").strip()
    if tok:
        return tok
    try:
        with open(QA_TOKEN_FILE, encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
    except FileNotFoundError:
        pass
    return ""


def health(base):
    with urllib.request.urlopen(urllib.request.Request(base + "/health", headers={"User-Agent": "guru-probe"}), timeout=30) as r:
        return json.load(r)


def gate(h):
    """(ok, why) — refuse anything that is not the QA Worker bound to the QA namespace."""
    if not isinstance(h, dict) or h.get("env") != "qa":
        return False, "env=%r is not \"qa\"" % (h.get("env") if isinstance(h, dict) else None)
    if h.get("kv_canary") != "qa":
        return False, "kv_canary=%r — the QA Worker is bound to the wrong namespace" % h.get("kv_canary")
    return True, "env=qa kv_canary=qa"


def grade(row, text):
    """inverted: any must-NOT hit is red regardless of must-contain; then every must-contain must hit."""
    hits_not = [n for n in row["must_not_contain"] if n.get("rx") and re.search(n["rx"], text)]
    if hits_not:
        return "RED", "carries a must-NOT: " + ", ".join("%s (%s)" % (n["class"], n["from"]) for n in hits_not)
    missing = [rx for rx in row["must_contain"] if not re.search(rx, text)]
    if missing:
        return "RED", "missing must-contain %s" % missing
    return "GREEN", "ok"


def ask(base, token, row, substrate="digest"):
    body = {"origin": "test", "conversation_id": "guru-probe-" + row["id"] + ("-core" if substrate == "core" else ""), "turns": [{"role": "user", "content": row["ask"], "ts": "2026-01-01T00:00:00Z"}], "live_state": {}}
    if substrate == "core":
        body["substrate"] = "core"   # Guru 4b — the flag the real client never sends
    req = urllib.request.Request(base + "/api/chat", data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "X-Tate-Token": token, "User-Agent": "guru-probe"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.load(e)
        except Exception:  # noqa: BLE001
            return e.code, {"error": "http %d" % e.code}


def live(max_turns, substrate="digest"):
    import importlib.util
    spec = importlib.util.spec_from_file_location("gf", os.path.join(HERE, "guru-facts.py")); gf = importlib.util.module_from_spec(spec); spec.loader.exec_module(gf)
    tok = resolve_qa_token()
    if not tok:
        print("⛔ no QA token — set FERNWOOD_QA_TOKEN or write .private/fernwood-qa-token"); return 2
    try:
        h = health(QA_URL)
    except Exception as e:  # noqa: BLE001
        print("⛔ cannot read %s/health: %s" % (QA_URL, e)); return 2
    ok, why = gate(h)
    print("  %s GATE   %s" % ("✅" if ok else "⛔", why))
    if not ok:
        print("⛔ REFUSED — no turn spent."); return 2
    if h.get("chat_budget"):
        b = h["chat_budget"]; print("  · QA chat budget today: $%.3f of $%.2f · %s turn(s)" % (b.get("used_usd", 0), b.get("ceiling_usd", 0), b.get("turns", 0)))
    fix_dir = os.path.join(ROOT, ".private", "guru-fixtures"); os.makedirs(fix_dir, exist_ok=True)
    rows = [r for r in gf.rows() if not r["requires_tool"]][:max_turns]
    rc = 0
    subs = ("digest", "core") if substrate == "both" else (substrate,)
    seen_prefix = {}
    for sub in subs:
      if len(subs) > 1: print("  ── substrate: %s ──" % sub)
      for row in rows:
        st, resp = ask(QA_URL, tok, row, sub)
        if st == 429 and isinstance(resp, dict) and resp.get("error") == "chat-budget-exceeded":
            print("  💰 BUDGET  %s — the Worker refused ($%s used / $%s ceiling); stopping, not erroring" % (row["id"], resp.get("used_usd"), resp.get("ceiling_usd"))); return 3
        if st != 200:
            print("  ⛔ ERROR   %s — HTTP %s %s" % (row["id"], st, json.dumps(resp)[:120])); rc = 1; continue
        text = resp.get("reply", "")
        verdict, why = grade(row, text)
        dbg = resp.get("debug") or {}
        u = dbg.get("usage") or {}
        seen_prefix.setdefault(sub, set()).add(dbg.get("prefix_sha"))
        print("  %s %-24s %s · %sms · prefix %s · cache read %s / new %s" % ("✅" if verdict == "GREEN" else "🔴", row["id"], why, dbg.get("latency_ms", "?"), str(dbg.get("prefix_sha", "?"))[:8], u.get("cache_read", "?"), u.get("cache_creation", "?")))
        if verdict != "GREEN":
            rc = 1; print("      reply: %s" % text[:220].replace("\n", " "))
        # Guru 2b — a FIXTURE per row: the harness's own ask, never a conversation of hers; prefix_sha beside it
        import datetime as _dt
        json.dump({"row_id": row["id"], "substrate": sub, "request": {"ask": row["ask"], "origin": "test"}, "response": text, "usage": resp.get("usage") or u, "model": resp.get("model"),
                   "prefix_sha": dbg.get("prefix_sha"), "latency_ms": dbg.get("latency_ms"), "verdict": verdict, "recorded_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")},
                  open(os.path.join(fix_dir, row["id"] + ("" if sub == "digest" else "." + sub) + ".json"), "w"), indent=1, ensure_ascii=False)
    if len(subs) > 1:
        a, b = seen_prefix.get("digest", set()), seen_prefix.get("core", set())
        print("  %s the two substrates render DIFFERENT prefixes" % ("✅" if a and b and not (a & b) else "🔴"))
    return rc


def selftest():
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond); print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("guru-probe selftest\n")
    check("REFUSES a prod-shaped /health", not gate({"env": "production", "kv_canary": "production"})[0])
    check("REFUSES env qa on the wrong namespace", not gate({"env": "qa", "kv_canary": "production"})[0])
    check("REFUSES a /health with no env", not gate({"ok": True})[0])
    check("ALLOWS qa/qa", gate({"env": "qa", "kv_canary": "qa"})[0])
    row = {"must_contain": [r"2,?8\s?73"], "must_not_contain": [{"rx": r"2,?9\s?59", "class": "stale-self", "from": "x"}, {"rx": r"2,?8\s?00", "class": "confusable-sibling", "from": "y"}]}
    check("inverted grading: right number + the stale one → RED", grade(row, "It is 2,873 ft (formerly 2,959).")[0] == "RED")
    check("inverted grading: right number + the lake's → RED", grade(row, "2,873 ft, like the lake at 2,800")[0] == "RED")
    check("right number alone → GREEN", grade(row, "The house sits at 2,873 feet.")[0] == "GREEN")
    check("missing → RED", grade(row, "quite high up")[0] == "RED")
    saved = os.environ.pop("FERNWOOD_QA_TOKEN", None); import shutil, tempfile
    global QA_TOKEN_FILE; real = QA_TOKEN_FILE; QA_TOKEN_FILE = os.path.join(tempfile.gettempdir(), "no-such-token")
    check("no QA token → empty (the live leg exits non-zero naming the variable)", resolve_qa_token() == "")
    QA_TOKEN_FILE = real
    if saved is not None: os.environ["FERNWOOD_QA_TOKEN"] = saved
    try:
        h = health("https://fernwood.paul-kirschenbauer.workers.dev")
        check("LIVE: pointed at prod's /health it refuses", not gate(h)[0], h.get("env"))
        check("LIVE: prod /health carries NO chat_budget key (the ceiling is QA-only)", "chat_budget" not in h)
        tok = resolve_qa_token()
        if tok:
            code = None
            try:
                urllib.request.urlopen(urllib.request.Request("https://fernwood.paul-kirschenbauer.workers.dev/api/conversations?start=2026-09-01&end=2026-09-02", headers={"X-Tate-Token": tok, "User-Agent": "guru-probe"}), timeout=30)
            except urllib.error.HTTPError as e:
                code = e.code
            check("LIVE: the QA token against prod → 401 (a different value, made structural)", code == 401, code)
    except Exception as e:  # noqa: BLE001
        print("  · live checks skipped: %s" % e)
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest", action="store_true"); ap.add_argument("--live", action="store_true"); ap.add_argument("--max-turns", type=int, default=1)
    ap.add_argument("--substrate", choices=("digest", "core", "both"), default="digest", help="Guru 4b: which prompt substrate the Worker assembles (core = the flag the client never sends)")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (live(a.max_turns, a.substrate) if a.live else (print(__doc__) or 0)))
