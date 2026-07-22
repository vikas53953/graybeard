# Vibe-QA Handover Prompts

Three ready-to-paste prompts. Adapt app-specific journey lists (Phase 3/§0) per project.

## Prompt A — Wire-Up Audit (for Claude Code; run FIRST)

```
Act as a hostile QA auditor. Do NOT fix anything yet — audit only.

Scan this entire codebase and produce a WIRE-UP AUDIT REPORT of every UI element that is not fully connected to real functionality.

Search for and list:
1. Dead links: href="#", href="", empty <a> tags, links to routes that don't exist in the router
2. Unwired handlers: buttons/inputs with no onClick/onSubmit/onChange, or handlers that are empty functions, console.log stubs, or TODO
3. Mock/static data: hardcoded arrays, placeholder JSON, fake API responses, lorem ipsum, sample data rendered instead of real backend calls
4. Unwired backend: frontend calls to API endpoints that don't exist in the backend, and backend endpoints no frontend code ever calls
5. Silent failures: fetch/axios calls with no error handling, forms that submit with no success/failure feedback
6. TODO / FIXME / HACK / "coming soon" comments
7. Features in the spec that have no corresponding implementation at all

Output format — markdown table:
| # | File:Line | Element/Feature | Problem | Severity (Blocker/Major/Minor) | Fix needed |

At the end give me: total count per category; top 10 blockers ranked by user impact; a one-line honest verdict — what % of the app is actually wired vs. demo-ware.

Rules: verify by reading actual code, not assumption; mark uncertain items "UNVERIFIED" — do not guess; write no fix code until I approve the report.
```

## Prompt B — Playwright E2E Suite (for Claude Code)

```
Set up a real Playwright end-to-end test suite for this app. Not the MCP — actual test scripts I can run with npx playwright test.

Phase 1 — Setup (confirm with me before proceeding):
1. npm init playwright@latest (Chromium only is fine)
2. playwright.config.ts: baseURL → my local dev server; webServer option so Playwright auto-starts the dev server; screenshot: 'only-on-failure'; video: 'retain-on-failure'; trace: 'on-first-retry'
3. Verify with one trivial test (homepage loads, title correct) and RUN it. Show real terminal output. Do not proceed until it passes.

Phase 2 — Route & link crawler (tests/crawl.spec.ts):
- Visit every route in the app router
- Assert: no 404, no console errors, visible content (not blank)
- Collect every <a> and button per page; click internal links; assert none lead to 404, blank pages, or href="#"
- Output a summary of every broken link/route

Phase 3 — User journey tests (one spec per journey):
[PASTE YOUR §0 JOURNEY LIST HERE]
Each test must assert on VISIBLE user-facing outcomes (text, state change, URL, persistence after reload) — never just "element exists".

Phase 4 — Run and report:
- npx playwright test; paste the REAL terminal output — never summarize without showing it
- Per failure: screenshot path, what the user would experience, root cause (frontend bug vs backend not wired vs missing feature)
- Do NOT fix yet. Failure report first; wait for my approval on which to fix.

Rules: one phase at a time, stop and wait for my "go"; a test that can't fail counts as a failure; if the dev server or a dependency fails on Windows/PowerShell, tell me instead of silently switching approach.
```

## Prompt C — Claude in Chrome Master QA Prompt (browser-only)

Note: browser-only testing can't read code or run Playwright — it does behavioral detection instead.

```
You are a hostile senior QA engineer performing a full user-acceptance test of this web app. Assume nothing works until you personally verify it in the browser. It was built with AI assistance, so the likeliest bugs are: dead links, buttons that do nothing, features that look real but are static mock data, and forms that submit nowhere.

TEST ONE PHASE AT A TIME; mini-summary after each before continuing.

PHASE 1 — SMOKE: loads without errors? blank sections, broken images? every page reachable from nav? Report immediately if anything is fully dead.

PHASE 2 — LINK & BUTTON SWEEP: click EVERY link and button on EVERY page. Record: claims to do → actually happened. Flag links going nowhere, zero-effect buttons, inert clickable-looking icons.

PHASE 3 — STATIC DATA / WIRE-UP DETECTION: per data area — search an absurd string ("zzzzqqqq123"): identical results = static; search something real: relevant? Create something → RELOAD → persisted? Edit/delete → reload → same check. Same items same order regardless of actions = hardcoded. Do displayed counts ever change?

PHASE 4 — USER JOURNEYS (assert visible outcomes):
[PASTE YOUR §0 JOURNEY LIST HERE]

PHASE 5 — NEGATIVE & EDGE: every form empty / garbage / very long / special chars (<script>, quotes, emoji); rapid double-clicks; Back/Forward mid-flow; act on an item in one view, check the other.

PHASE 6 — UI/UX: consistency (fonts, spacing, colors, buttons); alignment/overflow; loading states; feedback after every action; narrow-width resize; empty states; Tab-key navigation.

PHASE 7 — FINAL REPORT in this format:
## QA Report
### Verdict: [X]% functional — [one honest sentence]
### Blockers | Majors | Minors — tables: # | Page | Element | Expected | Actual | Repro steps
### Suspected static data / unwired backend (Phase 3 evidence)
### What works well
### Top 5 fixes in priority order

RULES: never mark "working" without seeing the visible result; if undeterminable from the browser, mark "NEEDS CODE-LEVEL CHECK" — don't guess.
```

## Prompt D — Fix Loop (for the builder session, after any report)

```
Here is the Blockers table from QA: [PASTE TABLE]
Fix these ONE at a time. After each fix: re-run the full Playwright suite AND the specific repro steps for that item. Paste real terminal output. Do not proceed to the next item until I confirm. If a fix touches shared components, list every other page that uses them so I can retest those too.
```
