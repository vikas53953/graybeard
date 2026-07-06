---
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
execution: code
product_contract_source: conductor (conversation-gathered, see implementation-notes.md)
created: 2026-07-06
plan_added: 2026-07-06 (Gate 2 approved: onboarding Style A + optional story Q)
---

# Graybeard (working name) — Product Contract

## Goal Capsule

An open-source **Claude Code plugin** that gives non-coders the discipline of a
senior engineering team: a starter rulebook of tested working laws, an
onboarding interview that personalizes them, and — the core — **the loop**: a
command that turns any painful session transcript into a new, tested,
machine-enforced law. Users don't need to know how programmers think; the
plugin thinks that way for them and gets smarter from their own failures.

## Actors

- **A1 — The builder (primary):** domain expert, non-coder, uses Claude Code to
  build real products. Can't read diffs; reviews visual pages; speaks plain
  language (often voice-to-text).
- **A2 — The model:** whatever Claude model is running; must be forced into
  disciplined behavior by files, not willpower.
- **A3 — The tinkerer (secondary):** technical user who customizes/extends the
  laws; contributor to the open-source repo.

## Requirements

- **R1 — Two-command install.** Fresh Claude Code → working plugin with:
  marketplace add + plugin install. Zero manual config edits. (Bar: ≤2 commands,
  ≤2 minutes.)
- **R2 — Onboarding interview.** A command (working name `/onboard`) that asks
  ≤7 questions, ONE at a time, each with a recommendation; generates the user's
  personal standing orders (CLAUDE.md section), the every-turn reminder hook
  (safely merged into settings.json), and personalized copies of the starter
  laws (their name, their review preferences). (Bar: ≤10 minutes end to end.)
- **R3 — Starter rulebook.** De-personalized versions of the proven laws as
  skills: work-law (brief before code, neighbors re-tested, evidence before
  done, he-confirms-never-discovers, feedback-said-once, class-not-case),
  unknowns-law (blindspot pass, one question, mock before wire), and the
  conductor pipeline (scoreboard, 4 hard gates as HTML pages, breadth on hard
  forks, bars are numbers, cost before spending).
- **R4 — The loop (core).** A command (working name `/learn-from-pain`): user
  points at a painful transcript or describes the pain → plugin mines it →
  proposes ONE general law (class, never case) → tests it with subagents
  (baseline fails, with-law passes) → installs it into the user's laws + ledger.
  (Bars: one sitting ≤1 hour; test evidence shown on a visual page; the law is
  general — a reviewer can't point at a case-specific "if asked about X" clause.)
- **R5 — Visual review everywhere.** Every artifact the user must approve
  (requirements, mocks, plans, QA results, ship dashboards, loop evidence) is a
  self-contained HTML page in plain language, jargon glossed. Never a text wall.
- **R6 — Safety & reversibility.** settings.json merged, never overwritten;
  clean uninstall removes everything it added; transcript mining is local-only
  (nothing leaves the machine); never conflicts with other installed plugins
  (one-owner-per-stage traffic control built in).
- **R7 — Non-coder docs.** README quickstart written for A1 (no jargon), a
  2-minute "first project" walkthrough, and a contributor guide for A3.
- **R8 — Open source.** Public repo, permissive license (rec: MIT), plugin
  marketplace manifest so others can install and fork.
- **R9 — System Design Principles stage (added at Gate 1 by Vikas, 2026-07-06).**
  Before any build, the pipeline produces a plain-language **System Design
  page** with two halves:
  (a) **The map** — every component the application needs (screens, brain/
  backend, memory/database, keys/login, home/hosting, watchtower/logs &
  monitoring, locks/security, pipes/APIs), one plain sentence each, what was
  chosen, what was skipped and why — no component silently chosen.
  (b) **The principles** — the senior-engineer design rules APPLIED to this
  design and named on the page: one job per file/module (no god-files), one
  source of truth per fact, simplest thing that works (complexity must earn its
  keep), clear one-direction data flow, security at the boundaries,
  observability built in (the app can explain its own failures), loose coupling
  (a change in one part can't silently break another), and design-for-deletion
  (features can be removed cleanly). Each principle shown with HOW this design
  honors it, in one sentence. Violations found later at code review are treated
  as bugs. (Bars: a non-coder can name their app's components and the top-3
  principles after one read; no file over ~500 lines ships in v1 output.)

## Flows

- **F1 — First contact:** install (R1) → `/onboard` (R2) → first project starts
  under the laws automatically.
- **F2 — Build something:** user pastes an idea → conductor pipeline runs
  (scoreboard, gates, visual pages) → shipped project.
- **F3 — The loop:** something went painfully wrong → `/learn-from-pain` →
  tested personal law installed → next session already obeys it.
- **F4 — Resume:** new session, any project → scoreboard + ledger read →
  "welcome back, we're at stage N."

## Acceptance Examples

- **AE1:** A fresh Claude Code user with zero plugins runs 2 commands and a
  10-minute interview; their next "build me X" message gets a brief, a
  scoreboard, and one question at a time — without them knowing any skill names.
- **AE2:** A user pastes a transcript where the AI claimed "fixed" five times
  while the app stayed broken; within the hour they have an evidence-before-done
  law installed, with a test page showing baseline-fail → with-law-pass.
- **AE3:** Uninstall leaves their settings.json byte-equivalent to pre-install
  (minus our additions), verified.

## Out of scope (v1)

Other AI tools (Cursor/Codex ports), any cloud service or telemetry, team/multi-
user features, a GUI beyond HTML artifact pages, non-English onboarding.

## Blindspots / open risks (from stage 1)

- **B1:** Testing laws needs subagent runs — costs the user tokens; the loop
  must state cost before spending (their law #7) and offer a cheaper "install
  untested, flagged" path.
- **B2:** Hook installation edits user settings.json — highest-risk touchpoint;
  needs merge + backup + verified uninstall (R6, AE3).
- **B3:** Transcripts contain private data — mining stays local; docs must say
  so loudly.
- **B4:** Users with gstack/superpowers/compound-engineering installed — traffic
  control must detect and defer, not fight.
- **B5:** Claude Code plugin/marketplace format may evolve — pin to documented
  manifest schema; keep the plugin thin.
- **B6:** Name/trademark check needed before publishing (taste gate item).

## Taste decisions (batched for Gate 1)

- Product name — recommendation: **Graybeard** ("the senior engineer watching
  over your shoulder"); alternates: Sensei, The Compact, Scar Tissue.
- Command names — recommendation: `/onboard`, `/learn-from-pain`.
- License — recommendation: MIT.

---

# Planning Contract (added at Stage 4)

## Key Technical Decisions (KTDs — mechanical, decided by principle)

- **KTD1 — The plugin is almost entirely markdown.** Skills, templates, and law
  files; the only "code" is what Claude executes at runtime via its own tools
  (Edit/Bash) following skill instructions. Simplest thing that works; nothing
  to compile; contributors edit text. (Principle: complexity must earn its keep.)
- **KTD2 — Templates in plugin, personalization in user space.** The plugin
  (read-only cache) ships templates; `/onboard` GENERATES user-owned files:
  `~/.claude/graybeard/profile.md` (single source of truth for the user's
  answers), a Graybeard section in `~/.claude/CLAUDE.md`, the every-turn hook in
  `~/.claude/settings.json` (merged, with timestamped backup), and personalized
  law skills in `~/.claude/skills/`. (Principles: one source of truth; loose
  coupling — plugin updates never clobber personal laws.)
- **KTD3 — Per-project state stays in the project.** PIPELINE.md scoreboard +
  implementation-notes.md ledger, exactly as proven this week. (One source of
  truth per fact; travels with the repo.)
- **KTD4 — The loop's tests run as Claude subagents** with a fixed
  baseline-vs-with-law recipe (3+3 runs, sonnet-tier); cost estimate shown
  before running; "install untested (flagged)" path costs nothing. (His law 7.)
- **KTD5 — Safety mechanics:** every write to user files is preceded by a
  `.graybeard-backup-<timestamp>` copy; `/graybeard-uninstall` restores backups
  and deletes generated files; a manifest of everything generated is kept in
  `~/.claude/graybeard/manifest.txt` so uninstall is exact (AE3).
- **KTD6 — Traffic control at onboard time:** `/onboard` greps installed
  plugins/skills; if gstack/superpowers/compound-engineering are present, the
  generated standing orders name one owner per stage and defer accordingly.

## System Design (Graybeard itself — map + principles)

Screens: HTML artifact/gate pages · Brain: the skills (rulebooks) · Memory:
profile.md + per-project PIPELINE.md/ledger · Keys: none (local, no accounts) ·
Home: GitHub repo + Claude plugin marketplace · Watchtower: loop test evidence
+ implementation-notes ledger · Locks: local-only mining, backups, exact
uninstall · Pipes: Claude Code plugin surface (skills, hooks, CLAUDE.md).
Principles applied: one job per skill file; one source of truth (profile);
simplest thing (markdown-first); one-direction flow (templates → generated
files → behavior); observability (every law change evidenced + ledgered);
loose coupling (each skill standalone); design-for-deletion (manifest-driven
uninstall).

## Implementation Units

### U1. Repo scaffold & manifest
Files: `.claude-plugin/plugin.json`, `LICENSE` (MIT), `.gitignore`, repo layout.
Approach: minimal valid plugin manifest (name graybeard, description = trigger-
style), directories: `skills/`, `templates/`, `docs/`.
Tests: plugin loads in a fresh Claude Code without errors.

### U2. Starter rulebook (3 skills, de-personalized)
Files: `skills/graybeard-worklaw/SKILL.md`, `skills/graybeard-unknowns/SKILL.md`,
`skills/graybeard-conductor/SKILL.md`.
Approach: port this week's brief-first / finding-unknowns / idea-to-product with
`{{USER_NAME}}`-style placeholders + review-preference slots; conductor includes
the System Design section (map + principles) at Gate 3 per R9.
Tests: simulated-scenario reps per skill (the proven baseline/green method),
2 reps each minimum, pass = law behavior appears.

### U3. /onboard skill
Files: `skills/onboard/SKILL.md`, `templates/profile.md`, `templates/hook.json`,
`templates/claude-md-section.md`.
Approach: Style A interview (7 questions, one at a time, recommendation each) +
optional story question #8 that seeds the first personal law; generates the
KTD2 file set with KTD5 safety; detects other plugins (KTD6).
Tests: dry-run in a sandbox HOME; verify all files generated, settings.json
merged not replaced, backup exists; re-running /onboard updates, not duplicates.

### U4. /learn-from-pain skill (THE CORE)
Files: `skills/learn-from-pain/SKILL.md`, `templates/evidence-page.html`,
`templates/law.md`.
Approach: input = transcript path or pasted text or plain description; mine →
classify the disease → propose ONE general law (explicit class-not-case check) →
cost line → subagent test recipe (baseline 3 / green 3) → evidence HTML page →
on approval install law + append to user ledger.
Tests: run against a sanitized Touch-the-Grass excerpt (the real fixture!);
verify: law is general (no case clause), evidence page rendered, install +
ledger correct, untested path flags properly.

### U5. Uninstall & safety
Files: `skills/graybeard-uninstall/SKILL.md`.
Approach: manifest-driven restore/delete per KTD5.
Tests: AE3 — snapshot user dirs, install+onboard, uninstall, diff = only
pre-existing files remain, settings.json restored.

### U6. Docs
Files: `README.md` (non-coder quickstart, 2-min first project, privacy promise),
`CONTRIBUTING.md`, `docs/how-it-works.md`.
Tests: readability pass — no unglossed jargon (grep against a jargon list).

## Verification Contract / Definition of Done
- All R1-R9 bars met with evidence (install ≤2 cmds; onboard ≤7 Q / ≤10 min in a
  timed dry run; loop ≤1 hr on the fixture; AE3 diff clean).
- Every skill passes its simulated-scenario tests (documented in docs/testing.md).
- Plan-vs-built audit at review; QA = fresh-machine walkthrough of F1-F4.

## R10 — The Watchtower Law (added at Gate 3 by Vikas, 2026-07-06)

Every application built under Graybeard gets logging from day one (R9's
watchtower is mandatory, machine-readable). The working law it powers:
**logs before guesses** — after every build, run, or reported failure, the AI
reads the app's own logs FIRST and diagnoses from that evidence; assuming
without reading logs is a law violation. Repeated or hard failures convene an
agent panel (breadth law) over the log evidence. Proactively — at session
start and after runs — the AI scans logs, surfaces what it found, and acts at
the user's chosen autonomy level, set during onboarding: LEVEL 1 propose-first
(default) or LEVEL 2 fix-quietly-and-report (safe fixes only; destructive or
scope-changing actions always gated regardless of level).
(Bars: zero "press X and tell me what happens" requests for information the
logs already contain; every diagnosis on an evidence page cites log lines.)

Unit impact: U2 worklaw gains the logs-before-guesses law; U3 interview gains
the autonomy-level question; U2 conductor's build stage requires the watchtower
component wired before Gate 4.
