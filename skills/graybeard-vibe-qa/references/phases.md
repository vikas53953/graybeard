# Vibe-QA Phases — Detailed Tests & Acceptance Criteria

Read this fully before starting a QA run. Execute in order. Stop and report after each phase.

## §0 Journey Checklist (pre-testing)

Write 10–15 user journeys in plain English **from the spec, not the code**. Format:

```
J1: [Persona] opens app → [action] → [action] → EXPECTS: [visible outcome + persistence]
```

Example set for a music app:
- J1: New user opens app → sees populated home → EXPECTS: real content, no placeholders
- J2: User searches "Arijit" → results appear → EXPECTS: relevant results; absurd query shows empty state
- J3: User plays a track → EXPECTS: button toggles, progress bar moves, time counts up
- J4: User pauses/skips/seeks/volume → EXPECTS: each control visibly works
- J5: User creates playlist → adds 3 songs → reloads page → EXPECTS: playlist + songs persist
- J6: User deletes a song from playlist → reloads → EXPECTS: still gone
- J7: User signs up with bad email → EXPECTS: clear error; with valid data → EXPECTS: success + logged in
- J8: User logs out and back in → EXPECTS: their data is still theirs

**Gate:** every spec feature covered by ≥1 journey; user confirmed the list.

## §1 Smoke Test (~5 min)

Tests: app loads; open DevTools console — note every error; visit every route in the nav; check for blank sections, broken images, missing icons; confirm dev server + backend + DB all actually running.

**Gate:** zero uncaught console errors on load; all nav routes reachable; nothing fully dead. If anything is fully dead, STOP and report before deeper testing.

## §2 Link & Button Sweep

Tests: on every page, enumerate every `<a>`, `<button>`, clickable icon, menu item. Click each. Log a table: `Page | Element | Claims to do | Actually did`. Flag: `href="#"` / empty href; links that reload the same page; buttons with zero visible effect; icons styled clickable but inert; nav items that don't navigate.

**Gate:** 100% of clickables logged; every no-op either fixed-listed as a Blocker or explained (e.g., intentionally disabled state with visual indication).

## §3 Wire-Up Audit

### §3A Code-level (when code is accessible — builder/CLI context)

AUDIT ONLY — no fixes. Grep/inspect for:
1. Dead links: `href="#"`, `href=""`, routes not in the router
2. Unwired handlers: missing/empty onClick/onSubmit/onChange; console.log stubs; TODO handlers
3. Mock/static data: hardcoded arrays, placeholder JSON, fake API responses, lorem ipsum rendered in production paths
4. Unwired backend: frontend calls to endpoints that don't exist; backend endpoints nothing calls
5. Silent failures: fetch/axios without error handling; forms with no success/failure feedback
6. TODO / FIXME / HACK / "coming soon"
7. Spec features with no implementation at all

Output table: `# | File:Line | Element | Problem | Severity (Blocker/Major/Minor) | Fix needed` + counts per category + top-10 blockers + honest wired-vs-demo-ware %.

### §3B Behavioral (browser-only context, e.g., Claude in Chrome)

For each data-driven area:
- Search an absurd string ("zzzzqqqq123"): identical results = static; proper empty state = wired
- Search something real: results relevant?
- Create something → RELOAD → persisted? No = not wired
- Edit/delete → reload → same check
- Same items, same order every visit regardless of actions = likely hardcoded
- Displayed counts ("1,204 songs") — do they ever change with any action?

**Gate:** every data view proven live or listed in the audit table; report delivered and approved BEFORE any fixing.

## §4 E2E Journey Tests (Playwright)

Setup: `npm init playwright@latest` (Chromium is enough). Config: `baseURL` → local dev server; `webServer` block so Playwright auto-starts it; `screenshot: 'only-on-failure'`; `video: 'retain-on-failure'`; `trace: 'on-first-retry'`. Verify with one trivial test and RUN it — show real output before writing more.

Tests:
- `tests/crawl.spec.ts`: visit every router route; assert no 404, no console errors, visible content; click all internal links; assert none dead
- One spec file per §0 journey; assert on VISIBLE outcomes (text, state, URL, persistence-after-reload), never just element existence

**Gate:** every journey has a spec; full suite green with pasted terminal output; every test can fail (verify by breaking one assertion once).

## §5 Negative & Edge Testing

Tests: every form submitted empty, with garbage, very long input, and special characters (`<script>alert(1)</script>`, quotes, emoji); rapid/double-clicks on submit; browser Back/Forward mid-flow; same item open in two views, act in one, check the other; kill network mid-action (offline mode) — graceful error or crash?

**Gate:** every invalid input produces a clear user-visible error; no crashes; no double-submits creating duplicates.

## §6 UI / UX / Design Review

Tests: font/spacing/color/button consistency across pages; alignment, overlap, overflow, cut-off text; loading states (spinner/skeleton vs jump/flash); post-action feedback (toast/state change — never silent); resize to mobile width — layout survives; empty states designed (not broken-looking); Tab-key reaches all interactive elements; icons/images meaningful without color alone.

**Gate:** no Blocker-level visual breakage; every action gives feedback; app usable at 375px width; keyboard navigation possible.

## §7 AI-Code Hygiene Audit (vibe-coded apps need this extra pass)

1. **Phantom feature audit** — diff spec vs what actually functions; AI builds UI (settings toggles, menu items) wired to nothing
2. **Dependency verification** — every package.json entry real AND used; run `npm audit`; AI hallucinates packages and picks stale versions
3. **Secrets & security defaults** — grep for API keys/tokens in frontend and git history; check CORS, rate limiting, input sanitization. MANDATORY before anything is public.
4. **Consistency/drift review** — find duplicated components/logic and inconsistent patterns across sessions (root cause of whack-a-mole)
5. **Silent-failure sweep** — every `catch` block must surface something to the user, not just console.log
6. **Persistence reality check** — where does data actually live? localStorage/in-memory posing as a database = Major

**Gate:** no secrets anywhere; deps clean or triaged; phantom features listed; persistence location matches spec.

## §8 Regression Re-Run

Re-run the FULL Playwright suite after every fix session — no exceptions. AI changes more surface area per fix than a human; blast radius is bigger.

**Gate:** suite green after every fix session, output pasted.

## §9 Final Report Template

```
## <App> QA Report
### Verdict: [X]% functional — [one honest sentence]
### Blockers (user cannot proceed)
| # | Page | Element/Feature | Expected | Actual | Repro steps |
### Majors (works wrong / static / unwired)
(same table)
### Minors (cosmetic / polish)
(same table)
### Suspected static data / unwired backend (evidence from §3)
### Hygiene findings (§7)
### What actually works well
### Top 5 fixes in priority order (by user impact)
```

**Gate:** report complete; fixes then proceed ONE at a time with §8 after each.
