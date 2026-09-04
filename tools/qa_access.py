"""qa_access.py — the Cloudflare Access service token for the QA origin (fernwood-qa.pages.dev is behind Access since
2026-09-04). Every tool that fetches the QA PAGE (not the Worker — the Worker has its own token gate) sends these two
headers, read from `.private/cf-access-service-token.json` (mode 600, gitignored) or from the env (CI: CF_ACCESS_CLIENT_ID
/ CF_ACCESS_CLIENT_SECRET as repository secrets — Paul's to set). No token → headers() is {} and the tool will meet the
login redirect, which qa-walk reports as "the wrong document" (exit 2), never as clean."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
FILE = os.path.join(ROOT, ".private", "cf-access-service-token.json")
QA_HOSTS = ("fernwood-qa.pages.dev",)

def token():
    i, s = os.environ.get("CF_ACCESS_CLIENT_ID"), os.environ.get("CF_ACCESS_CLIENT_SECRET")
    if i and s: return i, s
    try:
        d = json.load(open(FILE, encoding="utf-8")); return d.get("CF_ACCESS_CLIENT_ID"), d.get("CF_ACCESS_CLIENT_SECRET")
    except (OSError, ValueError): return None, None

def headers(url=""):
    """{} unless the url is a QA-page host and a token is present."""
    if url and not any(h in url for h in QA_HOSTS): return {}
    i, s = token()
    return {"CF-Access-Client-Id": i, "CF-Access-Client-Secret": s} if i and s else {}
