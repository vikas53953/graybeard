# Implementation notes — deviations & decisions

- 2026-07-06: Stage 1 (unknowns) not re-run as a fresh finding-unknowns
  interview — the shaping happened across the 2026-07-04→06 conversation
  (who it's for, loop-vs-rulebook, option A). Re-interviewing would violate
  "feedback is said once." Remaining unknowns recorded as blindspots in the PRD.
- 2026-07-06: Requirements artifact written directly from the gathered
  conversation instead of re-running the ce-brainstorm interview (same reason).
  Artifact conforms to the ce requirements-only contract so ce-plan/ce-work can
  consume it at stages 4-5.
- 2026-07-06: Working folder named "graybeard" (mechanical); the NAME itself is
  a taste decision batched at Gate 1 — folder rename is trivial if he picks
  another.
- 2026-07-06: Stage 4 authored directly in ce-plan artifact format (implementation-ready, U-IDs) instead of re-running the ce-plan interview — same feedback-said-once rationale as stage 2; all product decisions were already gathered at Gates 1-2.
- 2026-07-06: U2 tested with 1 smoke rep per skill at build time (3 subagents, ~$1); the full 2+ rep matrix runs at stage 6 review per the Verification Contract. Conservative sequencing to keep build momentum.
