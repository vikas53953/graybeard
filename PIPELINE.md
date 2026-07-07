# PIPELINE — Graybeard (working name)            updated: 2026-07-07

Open-source Claude Code plugin: the senior-engineer discipline loop for
non-coders. Direction approved by Vikas 2026-07-06: Claude Code only (option A);
the product core is THE LOOP (pain → tested law), shipped with a starter
rulebook and an onboarding interview.

| # | Stage             | Status                              | Artifact |
|---|-------------------|-------------------------------------|----------|
| 0 | Intake            | done                                | this file |
| 1 | Unknowns          | done (shaped in chat 2026-07-04→06) | blindspots recorded in PRD |
| 2 | Requirements      | APPROVED by Vikas 2026-07-06 (+R9 system-design stage; name=Graybeard, MIT, commands accepted) | docs/plans/2026-07-06-001-product-graybeard-plan.md + docs/gates/gate1-requirements.html |
| 3 | UX mocks          | APPROVED by Vikas 2026-07-06 (Style A + optional story Q; tabs 2&3 as shown) | docs/gates/gate2-mocks.html |
| 4 | Architecture+plan | GREEN LIT by Vikas 2026-07-06 (+R10 Watchtower Law amendment) | plan file (implementation-ready) + docs/gates/gate3-plan.html |
| 5 | Build             | DONE — U1-U6 all built | skills/, templates/, docs/, README |
| 6 | Code review       | DONE 2026-07-07 — 10/10 tests green (loop, onboard 13/13, uninstall AE3 incl. re-run, 6/6 rulebook reps); 9/10 issues resolved (1 cosmetic deferred); decision #7→A applied & retested | docs/gates/stage6-review.html |
| 7 | QA                | MECHANICS DONE 2026-07-07 — 18/18 test paths pass (install manifests, onboard×4, loop×3, uninstall×4, rulebooks 6/6); marketplace.json built; 5 live-machine confirmations left to Vikas (install/timing) | docs/gates/stage7-qa.html |
| 8 | Ship (open source)| GATE 4 IN PROGRESS 2026-07-07 — ✅ install+load CONFIRMED live; ✅ ONBOARDING run live on Vikas's machine + verified 11/11; ✅ worklaw v0.1 auto-offer seed added + smoke-tested (Fable 5 opinion, Option A). Ready to publish (gh authed as vikas53953, repo scope); awaiting Vikas confirm of public repo name. Not-yet-live-tested: build-brief, loop, uninstall (sandbox-proven) | docs/gates/gate4-ship.html |
| 9 | Learn             | not started                         | — |

Open questions (batched at Gate 1, taste): product name (rec: Graybeard),
command names (rec: /onboard, /learn-from-pain), license (rec: MIT).

BACKLOG (v0.2, raised by Vikas 2026-07-07): **auto-trigger the loop.** /learn-from-pain
should not be only manual. The worklaw 2-strikes moment IS the pain signal — the
conductor/worklaw should auto-DETECT a learnable failure after N failed attempts
and, at the user's autonomy level (LEVEL 1 auto-offer / LEVEL 2 auto-draft, paid
test still gated by cost-before-spending law #7), fire the loop behind the scenes.
Manual /learn-from-pain stays as an explicit option. Touches worklaw + conductor +
learn-from-pain; needs its own design + test pass. Vikas's words: "learn from pain
should be automatic, not manually enforced." v0.1 ships a minimal seed: worklaw
law #5 now OFFERS /learn-from-pain at the 2-strikes moment (auto-offer, no new
machinery, cost still gated). Fable 5's v0.2 guardrails: (1) detector checks the
LEDGER for a repeating class before offering (don't nag on a one-off); (2)
law-hygiene — check existing laws first + CAP active laws to prevent law inflation;
(3) even at LEVEL 2, auto-DRAFT but NEVER auto-install (install is always the
user's call).

Deviations: see implementation-notes.md
