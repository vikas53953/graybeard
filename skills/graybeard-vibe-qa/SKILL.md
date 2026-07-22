---
name: graybeard-vibe-qa
description: The click-everything QA engine for AI-built apps. Use whenever the user asks to test, QA, audit, or verify an app; says something is broken, unwired, or fake; says an app "passes tests but is still broken"; before declaring ANY app done; at Conductor Stage 7 (QA); and whenever fixes keep breaking neighbors (whack-a-mole). Works on apps built with OR without Graybeard — this skill can be run standalone on any project.
---

# Vibe-QA — others review the code; this runs the app

**The disease, in plain words:** AI-built apps fail in a special way. The AI
says "47 tests passed!" — and the app is still broken for a real person. Dead
links. Buttons wired to nothing. A screen showing fake sample data dressed up
as a real backend. Forms that fail silently. Why? **The same AI that wrote the
code also wrote the tests** — so the tests check what the code *does*, not
what you *wanted*. Both share the same blind spot.

The cure is testing from the *outside in*: click everything, walk every real
user journey, feed it garbage, and demand proof — exactly like a stranger
using the app for the first time.

## Non-Negotiable Rules (every phase)

1. **Hard gates.** Phases run in order. Stop after each phase, report, wait
   for the user's "go." Never skip ahead.
2. **Real output only.** Paste actual terminal output / describe actually
   observed browser behavior. A result you didn't see is not a result.
3. **No self-grading.** A test that cannot fail is itself a failure. Assert
   on things a user can see (text, state changes, URL, data surviving a
   reload) — never just "the element exists."
4. **Audit before fixing.** During audits, report only. Fix ONE item at a
   time after approval, re-testing after each.
5. **Honest verdicts.** Every report ends with "X% functional" and one honest
   sentence. "UNVERIFIED" is an acceptable answer; guessing is not.

## Phase 0 — Journey Checklist (before any testing)

Write 10–15 core user journeys in plain English **from what the user asked
for** (the spec / PIPELINE.md / requirements gate) — never from the code.
These become the acceptance tests for everything downstream. Get the user's
confirmation of the list. Template: `references/phases.md` §0.

## The Pipeline

| # | Phase | Question it answers |
|---|-------|--------------------|
| 1 | Smoke test | Does it even load? |
| 2 | Link & button sweep | Does every clickable do something real? |
| 3 | Wire-up audit | Is the screen truly connected to a real backend — or showing fake data? |
| 4 | E2E journey tests | Do complete user flows work start to finish? (Playwright) |
| 5 | Negative & edge testing | What happens with garbage input and weird usage? |
| 6 | UI / UX review | Consistent, mobile-safe, gives feedback, keyboard-navigable? |
| 7 | AI-code hygiene audit | Phantom features, leaked secrets, silent failures? |
| 8 | Regression re-run | Did the fixes break anything old? |
| 9 | Final report | Honest verdict + prioritized fix list, as a visual evidence page |

Detailed per-phase steps and acceptance criteria: **read
`references/phases.md` fully before starting a run.** Copy-paste handover
prompts (wire-up audit, Playwright suite, Claude-in-Chrome master prompt):
`references/prompts.md`. Full testing-type catalog: `references/testing-types.md`.

## Acceptance gates (short form)

- **P1:** loads, zero console errors, every page reachable, no blanks.
- **P2:** 100% of clickables logged expected→actual; zero unexplained no-ops.
- **P3:** every data view proven live (search changes results; created data
  survives reload; deletes persist). Zero mock arrays on production paths.
- **P4:** one Playwright spec per Phase-0 journey, all green with pasted
  output, each asserting a visible outcome.
- **P5:** every form tested empty + garbage + oversized + special characters;
  every failure shows a user-visible error; no crashes from back/forward or
  double-click.
- **P6:** consistent styling, survives mobile width, loading/empty states
  exist, every action gives feedback, Tab-key navigation works.
- **P7:** no secrets in frontend or git history; dependencies real and
  audited; no phantom UI; errors surface to the user; data lives where the
  spec says.
- **P8:** full suite green after EVERY fix session — no exceptions.
- **P9:** report on the Graybeard evidence page (`templates/evidence-page.html`),
  Blockers/Majors/Minors with repro steps, top-5 fixes ranked by user impact.

## How this connects to the rest of Graybeard

- **Conductor Stage 7 (QA)** — this skill IS that stage's engine. Gate 4
  (Ship) must not open until this pipeline's report exists as evidence.
- **Work Law's "prove it before done"** — for anything bigger than a one-line
  fix, "proof" means at minimum Phases 1–3 here, not a single happy-path run.
- **Fix loop** — hand the Blockers table to the building session: *"Fix these
  ONE at a time. After each fix, re-run the suite and the repro steps. Paste
  real output."* Two failed fixes on one item = Work Law two-strikes = offer
  /learn-from-pain.
- **Context Guard** — after each phase's report, checkpoint status to
  HANDOFF.md so a QA run survives a session wipe.

## Environment

Assume Windows + PowerShell unless told otherwise (`npx playwright test`,
`npm init playwright@latest`). If the dev server won't start or a dependency
fails, say so plainly — never silently switch approach. Browser-only testing
(no code access): run behavioral wire-up detection (§3B in
`references/phases.md`) and mark code-level items "NEEDS CODE-LEVEL CHECK."
