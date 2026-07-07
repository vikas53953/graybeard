# Graybeard — full state summary (for a fresh model's opinion)

**Written 2026-07-07 for Fable 5 to read cold and weigh in on the next step.**
Everything below is honest: what's proven is marked proven; what's unproven says so.

---

## TL;DR — the decision we want an opinion on

Graybeard (an open-source Claude Code plugin) is **built, tested, and confirmed
installing + loading on a real machine.** It is NOT yet published.

Mid-way through the final ship gate, the owner (Vikas) raised a feature idea that
is arguably the product's soul (see §7). The open question:

- **Option A (current recommendation):** ship the tested v0.1 now, then build the
  new idea as the first v0.2 feature with its own design + test pass.
- **Option B:** stop the ship, build the new idea into v0.1 now (re-opens the
  tested build, delays launch).

We want Fable 5's opinion on A vs B, and on the design of the v0.2 idea itself.

---

## 1. What Graybeard is

An open-source **Claude Code plugin** that gives non-coders the discipline of a
senior engineering team. Three parts:
1. **A starter rulebook** — three "law" skills that change how the AI works:
   - `graybeard-worklaw` — brief-before-code, re-test neighbors, evidence before
     "done", fix the class not the case, two-strikes→root-cause, logs-before-guesses.
   - `graybeard-unknowns` — blindspot pass, one question at a time, mock before build.
   - `graybeard-conductor` — the idea→product pipeline (scoreboard + 4 HTML gates).
2. **Onboarding** (`onboard` skill) — a ≤7-question interview that personalizes the
   laws to the user (writes their profile + standing orders + an every-turn reminder).
3. **The loop** (`learn-from-pain` skill) — the core: point it at a painful AI
   session, it mines the underlying failure, proposes ONE *general* law (never a
   case-patch), tests it with subagents (baseline-fails vs with-law-passes), shows
   a visual evidence page, and installs it. This is how the plugin "gets smarter."

Plus `graybeard-uninstall` — manifest-driven, restores everything byte-clean.

Audience: non-coders who build with Claude Code, can't read diffs, review visual
pages, speak plain language. Everything is local-only (no cloud, no telemetry).

## 2. How it was built (pipeline)

Ran a full idea→product pipeline. Stages 0-4 (intake, unknowns, requirements, UX
mocks, architecture+plan) were **approved by Vikas** via HTML gate pages (Gates
1-3). Requirements = R1-R10, in `docs/plans/2026-07-06-001-product-graybeard-plan.md`.
Build (stage 5) produced 6 skills + 5 templates + docs + plugin/marketplace manifests.

## 3. Key design decisions

- **Markdown-first:** the plugin is almost entirely Markdown skill files; the only
  "code" is what Claude executes at runtime following the instructions. Nothing to compile.
- **Design decision A (approved 2026-07-07):** the 3 rulebooks stay **universal**
  (no per-user copies). Personalization lives in ONE place — the user's profile,
  which feeds their `~/.claude/CLAUDE.md` standing-orders block + an every-turn
  reminder hook. Reason: one source of truth per fact; no same-named-skill clashes;
  plugin updates never touch personal settings; clean uninstall.
- **Safety (KTD5):** every write to a user file is backed up first; a manifest
  records everything created/backed-up so uninstall is exact (acceptance test AE3).
- **Watchtower law (R10):** logs-before-guesses + a per-user autonomy level
  (LEVEL 1 propose-first / LEVEL 2 fix-safe-and-report) set at onboarding.

## 4. What's been TESTED (with evidence)

All run for real, not asserted:
- **Loop quality (the core):** fed a real-style angry transcript (an AI claimed
  "fixed!" 5×, never running it). The loop named the class-level disease
  ("claiming done without proof") and produced a law with zero case detail —
  PASS. A separate judge confirmed generality.
- **Onboarding:** dry-run in a sandbox HOME — 13/13 structural checks (files
  generated, settings merged-not-overwritten, backup taken, re-run doesn't duplicate).
- **Uninstall (AE3):** clean-path restore = byte-identical to pre-install.
  Also tested: re-run→uninstall (byte-clean after a bug fix), and the
  missing-manifest fallback. Zero residue in all cases.
- **Rulebooks change behavior:** 6/6 independent subagent reps (worklaw briefs
  under time pressure + lists neighbors; unknowns asks one Q + offers a mock;
  conductor builds a scoreboard + resumes without re-asking).
- **QA stranger test:** 18/18 paths (manifests valid, onboard ×4 edge cases,
  loop ×3, uninstall ×4, rulebooks 6/6).
- **Code review:** 10 issues found, 8 mechanical bugs fixed (biggest: a re-run
  backup-clobber that would have broken clean uninstall silently), 1 design
  decision (→ decision A), 1 cosmetic deferred.

Evidence pages: `docs/gates/stage6-review.html`, `stage7-qa.html`, `gate4-ship.html`.

## 5. Live install — CONFIRMED on the real machine (2026-07-07)

This was the one thing that couldn't be faked, and it's now proven:
`/plugin list` on Vikas's machine shows `graybeard@graybeard (v0.1.0) ✔ enabled`,
7 plugins total, all 6 skills registered (graybeard:onboard, :learn-from-pain, etc.).

The install was painful and produced a **real bug fix worth knowing:**
- `marketplace.json` plugin `source` must start with `./` — ours was `"."`, which
  Claude Code silently rejects. Fixed to `"./"`. (Would have hit every user.)
- `/plugin marketplace add "<path>"` silently no-ops on Windows paths with spaces
  (known Claude Code bug). Worked around by writing the on-disk registries directly
  (`~/.claude/plugins/known_marketplaces.json` + `installed_plugins.json`) + copying
  the plugin into the managed marketplace/cache dirs, mirroring how the working
  plugins are stored. NOTE: on his machine the plugin loads from that **cache copy**
  — editing a skill in the repo needs a re-copy + `/reload-plugins` to take effect.

## 6. Current in-flight state (paused cleanly)

We were running onboarding live as the real test. Vikas answered all 7 questions
(Vikas · product owner, plain words, no code · visual HTML reviews · short/jargon-free
· stop-and-root-cause · quizzes on · LEVEL 1 autonomy · superpowers +
compound-engineering detected → defer). **Nothing has been written to his `~/.claude/`
yet** — paused at the "say go to write" step. Zero cleanup needed to pivot.

## 7. The v0.2 idea that triggered this summary (Vikas's, verbatim intent)

"Learn from pain should be **automatic**, not manually enforced. There should be a
manual option too, but the conductor should automatically fire learn-from-pain
after failed attempts (e.g. after the 2-strikes rule)."

Analysis: the worklaw's **2-strikes moment already IS the pain signal.** The clean
design reuses the autonomy level the user just set:
- **Auto-detect + auto-offer (LEVEL 1):** at 2 strikes, the AI proposes "turn this
  into a permanent law?" — no spend without a nod.
- **Auto-draft (LEVEL 2):** mine + draft the law automatically; only the paid
  subagent test step asks first (honoring law #7, cost-before-spending).
So: automatic *detection*, never silent *spending*. Touches worklaw + conductor +
learn-from-pain; deserves its own design + test pass. Logged in PIPELINE.md backlog.

## 8. Not done / honest gaps

- **Not published.** Local git repo, branch `master`, no remote. Publishing is
  outward-facing/irreversible — gated on Vikas's explicit go. README has
  `<owner>/<repo>` placeholders to swap at publish.
- **Timing bars unmeasured** (≤2min install, ≤10min onboard, ≤1hr loop). We
  de-numbered all shipped copy rather than ship a marketing number; these get real
  numbers only after a timed human run.
- **Real end-to-end user run not yet completed** — install+load is proven; the
  full first-run (onboard→build→loop→uninstall on the real machine) is mid-flight.

## 9. Where to look

- Scoreboard: `PIPELINE.md` · Deviation ledger: `implementation-notes.md`
- Plan/requirements: `docs/plans/2026-07-06-001-product-graybeard-plan.md`
- Skills: `skills/*/SKILL.md` · Templates: `templates/` · Docs: `README.md`, `docs/how-it-works.md`
- Gate/evidence pages: `docs/gates/*.html`

**The ask for Fable 5:** given all this, is the next step A (ship v0.1, then build
the auto-trigger as v0.2) or B (build auto-trigger into v0.1 first)? And how would
you design the auto-trigger so it stays honest about cost?
