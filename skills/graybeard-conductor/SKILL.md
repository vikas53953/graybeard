---
name: graybeard-conductor
description: Use when the user brings a new product/app idea, a new feature, or any request bigger than a small fix — especially raw one-liners ("build X", "i want an app that..."). Also use when a project contains PIPELINE.md (resume it). NOT for small bug fixes — graybeard-worklaw handles those directly.
---

# The Conductor — idea to product

Forces the full path a real product team runs, so nothing ships half-broken and
the user is never buried in text. The conductor ROUTES each stage; it never
rebuilds what an installed skill already does.

## Rule zero — sort the request
- Small fix/tweak → skip the pipeline; `graybeard-worklaw` alone.
- `PIPELINE.md` exists → read it, 2-sentence "welcome back — stage N, waiting
  on X", resume. Never redo approved stages; never re-ask what's recorded.
- Feature or product → run the stages. No UI change → stage 3 may be skipped
  (say so on the scoreboard).

## The scoreboard — PIPELINE.md
Create at intake; update at EVERY stage transition: stage table (status +
artifact per stage), open questions, deviations pointer.

## The stages
0 **Intake** + scoreboard (silent) · 1 **Unknowns** (`graybeard-unknowns`:
blindspot pass, ONE question per message with recommendation) · 2
**Requirements** — plain-language PRD with measurable bars → **HARD GATE 1** ·
3 **Mocks** — 2–4 structurally different clickable HTML directions, fake data →
**HARD GATE 2** · 4 **System Design & plan** → **HARD GATE 3 (green light)** ·
5 **Build** (under worklaw; deviations ledgered; scoreboard ticks per unit;
watchtower/logging wired FIRST) · 6 **Review** — plan-vs-built audit: every
item DONE / PARTIAL / NOT DONE / CHANGED / UNVERIFIABLE (in doubt →
UNVERIFIABLE) · 7 **QA — the stranger test**: every page, every button, every
form (empty/wrong/edge), empty/loading/error states, console, mobile width;
plus a log sweep (Watchtower) · 8 **Ship** → **HARD GATE 4**: dashboard, QA
evidence, TEST IT steps, quiz · 9 **Learn** — capture lessons for next time.

## Stage 4 must always produce the System Design section
(a) **The map** — every component the app needs: screens, brain/backend,
memory/database, keys/login, home/hosting, watchtower/logs, locks/security,
pipes/APIs — one plain sentence each, chosen or SKIPPED with the reason and
when to revisit. No component silently chosen. The watchtower is never
skippable (R10).
(b) **The principles applied, named**: one job per file/module (no god-files),
one source of truth per fact, simplest thing that works, one-direction data
flow, security at boundaries, observability built in, loose coupling,
design-for-deletion — each with one sentence on how this design honors it.
Principle violations found at review are bugs.

## Hard gates
A hard gate = a self-contained HTML review page (plain words, jargon glossed)
+ a one-line ask in chat. Never a markdown wall. Shows: what was decided,
options side by side where choices exist, the recommendation and what's at
stake if wrong, and a completeness score /10. Approval recorded on the
scoreboard with date.

## Iron laws
1. **User sovereignty.** Models recommend; the user decides. Never act to
   change their stated direction — present the case and ask.
2. **No skipping.** No code before Gate 3's green light.
3. **One question per message**, recommendation attached; the first real
   question ships in the same message as the intake plan.
4. **Degraded session → hand off.** Update scoreboard, write a short handoff,
   fresh session. Never push on degraded.
5. **Hard forks get breadth, never A/B.** Expensive-to-get-wrong decisions —
   including ones discovered mid-build: pause, note on scoreboard, generate
   genuinely different options (agent panel when useful), decision page,
   user picks.
6. **Bars are numbers.** "Fast" isn't a requirement until it's "≤1.5s" and on
   the scoreboard. A bar missed after two fix attempts = a hard fork, never a
   third patch.
7. **Say the cost before spending.** Agent fan-outs and model escalations get
   a one-line price + reason first.
8. **Logs before guesses.** After every build/run/failure, read the app's logs
   first; diagnose from evidence; act at the user's autonomy level (set in their
   standing orders; default propose-first).

## Red flags — STOP:
| Thought | Reality |
|---|---|
| "The idea is clear, I'll start coding" | Nothing is clear until Gate 1 approval. |
| "I'll ask these 5 questions together" | One per message, with a recommendation. |
| "A markdown summary is fine for this gate" | Users review HTML pages, not text walls. |
| "QA mostly passed" | Every button, every state, or NOT DONE. |
| "It's either option A or option B" | Hard fork → 4+ genuinely different options, panel-tested. |
| "Logging can come later" | The watchtower is a day-one component. Later = never. |
