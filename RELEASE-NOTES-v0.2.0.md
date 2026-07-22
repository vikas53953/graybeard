# Graybeard v0.2.0 — it runs the app, and it never forgets

Two new organs, both born from real pain:

## 🧪 Vibe-QA — outside-in testing for AI-built apps
The reason your app "passes tests but is still broken": the AI that wrote the
code also wrote the tests. Vibe-QA tests like a stranger instead — 9 gated
phases: smoke → click-everything sweep → **wire-up audit** (is that screen live
data, or a hard-coded fake?) → Playwright user journeys → garbage-input tests →
UI review → hygiene audit → regression → an honest **"X% functional"** verdict
with a ranked fix list on a visual evidence page.
Works standalone on ANY app — even ones built without Graybeard:
say **"QA my app like a stranger would."**

## 🧠 Context Guard — survives the AI's own memory wipes
When the AI's context fills up, your coding tool silently summarizes and wipes
it — that's why it "forgets" fixes and re-asks settled questions. Context Guard
checkpoints every decision to `HANDOFF.md` at every boundary, fires a tripwire
the instant before a wipe (forcing the summary to keep decisions *with
reasons*, and logging the wipe to `.graybeard/context-events.log`), and hands
every new session its memory back automatically. You never re-explain your
project again.

## Also
- Conductor Stage 7 (QA) now runs Vibe-QA as its engine; Gate 4 won't open
  without its report.
- Work Law's "prove it before done" now means Vibe-QA phases 1–3 minimum for
  anything app-level, plus an immediate checkpoint.
- Hooks are plugin-level: auto-install, auto-remove, no settings.json changes.
  They need Python 3; without it, everything runs in discipline-only mode.
- README: side-by-side demos, honest comparison table, adopters table.

**Upgrade:** `/plugin install graybeard@graybeard` then restart Claude Code.
