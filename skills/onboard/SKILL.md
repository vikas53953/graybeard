---
name: onboard
description: Use when the user runs /onboard, says "set up Graybeard", "personalize my laws", "onboard me", or when Graybeard is freshly installed and no ~/.claude/graybeard/profile.md exists yet. Runs the short personalization interview and generates the user's profile, standing orders, and every-turn reminder (the plugin's rulebooks stay universal — they're not copied).
---

# /onboard — personalize Graybeard in one short interview

*Design target (not a promise to display): keep the whole thing under ~10 minutes
and ≤7 questions. Speed comes from one question at a time with a recommendation, so
the user can often just say "yes" — never from rushing or batching questions.*

Turns the de-personalized starter laws into **this user's** laws. Asks ≤7
questions (one at a time, each with a recommendation so they can just say
"yes"), plus one optional story question, then generates a small set of
user-owned files. Safe by construction: every existing file is backed up before
it is touched, and everything generated is recorded in a manifest so
`/graybeard-uninstall` can undo it exactly.

## Before you ask anything — orient (silent, ~20s)

1. Find HOME: `~` = `$HOME` (mac/linux) or `%USERPROFILE%` (Windows). All
   generated files live under it. Use forward slashes; the shell tools handle
   the OS.
2. Check for an existing profile at `~/.claude/graybeard/profile.md`.
   - **Exists →** this is a RE-RUN. Read it. Tell the user in one line: "You're
     already set up — I'll only re-ask what you want to change. Say 'keep' to any
     question to leave it as-is." Pre-fill every recommendation with their
     current answer. Re-running UPDATES; it never duplicates.
   - **Missing →** first run. One-line welcome, then Q1 in the SAME message.
3. Get a timestamp for backups: run `date +%Y%m%d-%H%M%S` (bash) or
   `Get-Date -Format yyyyMMdd-HHmmss` (PowerShell). Call it `<ts>`.
4. **Traffic-control scan (KTD6, silent):** look for other discipline plugins so
   the generated orders defer instead of fighting (blindspot B4). Check:
   `~/.claude/plugins/`, `~/.claude/skills/`, and the user's settings for names
   containing `superpowers`, `gstack`, `compound-engineering`, `idea-to-product`,
   `brief-first`, or `finding-unknowns`. Remember what you find for the profile's
   traffic note and for step "Generate" below.

## The interview — ONE question per message, recommendation attached

Never fire a wall of questions. Each message: the question, your recommended
answer in **bold**, one line of why, then wait. Highest-impact first. If an
answer doesn't change any generated file, don't ask it.

- **Q1 — What should I call you?**
  Rec: whatever name they use. → `USER_NAME`.
- **Q2 — What do you build, and how much code can you read?**
  Rec: **"I describe what I want in plain words; I don't read code."** (most
  users here). → `USER_BACKGROUND` + `CODE_COMFORT`.
- **Q3 — When I finish a piece of work, how do you want to review it?**
  Options: a visual HTML page you open in a browser · a short plain-text summary
  · just tell me it's done. Rec: **visual HTML page** (you catch problems you'd
  never spot in text). → `REVIEW_STYLE`.
- **Q4 — How plain should I keep my replies?**
  Rec: **"Short and jargon-free; teach me a term only when I need it."** →
  `PLAINNESS`.
- **Q5 — When something breaks twice in a row, keep trying quick fixes, or stop
  and dig for the root cause even if it's slower?**
  Rec: **stop and root-cause** (quick-fix loops are how AI projects rot). →
  `TWO_STRIKES`. (This confirms a core law; almost everyone keeps it.)
- **Q6 — Want me to offer a 3-question quiz after big changes, and teach you the
  landmines of an unfamiliar area before we build?**
  Rec: **yes** (keeps the code from becoming a black box you can't steer). →
  `QUIZ_PREF`.
- **Q7 — When I read your app's logs and spot a problem, what should I do?**
  Options: LEVEL 1 — tell you and ask before changing anything (propose-first) ·
  LEVEL 2 — fix safe things myself and report, ask before anything risky.
  Rec: **LEVEL 1** to start; move to LEVEL 2 once you trust me. → `AUTONOMY_LEVEL`
  (store as `LEVEL 1` or `LEVEL 2`).

- **Q8 (optional) — the story.** After Q7: "One more, optional — tell me about
  the last time an AI coding session made you angry. What happened? I'll turn
  your worst day into your first personal law." If they tell a story, distill it
  into a one-line law seed → `STORY_SEED`, and tell them the loop (`/learn-from-pain`)
  can test and install it fully whenever they want. If they skip, set
  `STORY_SEED` = "(none yet — run /learn-from-pain after your first painful
  session)".

Stop asking the moment further answers wouldn't change a generated file (iron
law: one question per message; don't pad to hit seven).

## Confirm before writing (show, don't surprise)

Before generating anything, show the user a compact recap of their answers and
say plainly what you're about to create and change:

```
I'll create:
  ~/.claude/graybeard/profile.md          (your settings — the source of truth)
  ~/.claude/graybeard/manifest.txt        (list of everything I add, for clean uninstall)
I'll safely add to (backup first):
  ~/.claude/CLAUDE.md                      (your standing orders — one marked block)
  ~/.claude/settings.json                  (the every-turn reminder — merged, not replaced)
The three rulebooks are already installed with the plugin — I don't copy them;
your name and preferences above make them act personally.
```

Wait for "go" (worklaw law #1). Then generate.

## Generate (KTD2 files, KTD5 safety) — order matters

**Backups protect the PRISTINE pre-Graybeard file — never a re-run.** For every
file that already exists and will be modified: FIRST check whether a
`<file>.graybeard-backup-*` ALREADY exists. If one does, it is the pristine
pre-install copy from an earlier run — **keep it, do NOT make another**, and
reuse its path in the manifest. Only if no graybeard backup exists yet do you
copy the file to `<file>.graybeard-backup-<ts>`. This is what makes re-running
`/onboard` any number of times still uninstall byte-clean: the backup is always
the original, never a copy that already contains Graybeard's edits. Never write
over a user file without a pristine backup on record.

**The manifest is an append-log, written AS YOU GO — not at the end.** Create
`~/.claude/graybeard/manifest.txt` FIRST (before step 1), then append one line
the moment each file is created or backed up. If onboard is interrupted
half-way, the manifest still records exactly what was done so far, so
`/graybeard-uninstall` can always undo a partial run. Files Graybeard creates
fresh are recorded as `CREATED`; pristine backups as `BACKUP`. Never leave a
created/modified file unrecorded.

Build a substitution map from the answers:
`{{USER_NAME}} {{USER_BACKGROUND}} {{CODE_COMFORT}} {{REVIEW_STYLE}} {{PLAINNESS}}
{{TWO_STRIKES}} {{QUIZ_PREF}} {{AUTONOMY_LEVEL}} {{STORY_SEED}} {{TRAFFIC_NOTE}}
{{GENERATED_DATE}} {{PLUGIN_VERSION}}`. `PLUGIN_VERSION` = the `version` in this
plugin's `.claude-plugin/plugin.json`. `GENERATED_DATE` = today.

Then, in this order:

1. **Profile (source of truth):** fill `templates/profile.md` → write
   `~/.claude/graybeard/profile.md`. Write this FIRST so everything else can be
   regenerated from it later.
2. **(No skill copies.)** The three rulebooks ship with the plugin and run
   as-is, written in universal language. Personalization does NOT clone them —
   it lives in the profile (this step 1), the standing orders (step 3), and the
   every-turn reminder (step 4), which the AI reads each session. This keeps one
   source of truth per personal fact and avoids two same-named rulebooks
   clashing. (Design decision A, approved by Vikas 2026-07-07.)
3. **Standing orders:** fill `templates/claude-md-section.md` and MERGE it into
   `~/.claude/CLAUDE.md`:
   - Back up `CLAUDE.md` first if it exists.
   - If a `GRAYBEARD:BEGIN…GRAYBEARD:END` block already exists (re-run), replace
     exactly that block. Otherwise append the filled block at the end. Never
     touch the user's own text outside the markers.
4. **Every-turn reminder:** merge `templates/hook.json` into
   `~/.claude/settings.json`:
   - Pristine-backup `settings.json` first (per the backup rule above); if it
     doesn't exist, create a minimal valid one (`{}`) and record it in the
     manifest as `CREATED` (not backed up — it didn't exist).
   - Merge **only** the array entry at `hooks.UserPromptSubmit[0]` from the
     template. The template's ROOT-level `_graybeard` key is documentation —
     never write it into the user's settings.json.
   - Parse the JSON. Ensure `hooks.UserPromptSubmit` is an array. If an entry
     already carries `"_graybeard": "graybeard-every-turn-reminder"` (re-run),
     REPLACE it; otherwise APPEND the filled entry. Preserve every other hook and
     key byte-for-byte. Write valid JSON back.
   - Fill `{{USER_NAME}} {{REVIEW_STYLE}} {{AUTONOMY_LEVEL}}` in the echo command.
     These are free-text answers: before substituting, strip or backslash-escape
     any `"` or `\` in them so the `command` string stays valid JSON and the
     shell `echo` doesn't break. (A name with a stray quote must not corrupt
     settings.json.)
5. **Traffic control (KTD6):** if the scan found another discipline plugin, add a
   line to the generated CLAUDE.md block naming one owner per stage and deferring
   (e.g. "superpowers detected — for planning defer to its brainstorming; for the
   idea→product loop use graybeard-conductor"), and record it in the profile's
   `TRAFFIC_NOTE`. If nothing was found, `TRAFFIC_NOTE` = "None detected — Graybeard
   owns every stage."
6. **Manifest (already growing — reconcile at the end):** you created the
   manifest first and appended to it as you went (see the append-log rule above).
   Now do a final pass: confirm every file you created has a `CREATED` line and
   every pristine backup has a `BACKUP <original>	<backup-path>` line, with no
   duplicates. This is the exact record `/graybeard-uninstall` replays.

## Verify before you claim done (worklaw law #8 — they confirm, never discover)

Do NOT tell the user it worked until you have checked, yourself:
- `~/.claude/graybeard/profile.md` exists and has no leftover `{{…}}` tokens.
- `~/.claude/CLAUDE.md` contains exactly ONE `GRAYBEARD:BEGIN` and one
  `GRAYBEARD:END`, and no leftover `{{…}}` tokens.
- `~/.claude/settings.json` still parses as valid JSON and contains exactly one
  `graybeard-every-turn-reminder` entry (not two — re-run must not duplicate).
- `~/.claude/graybeard/manifest.txt` lists every created file and every backup.

Grep for `{{` across the generated files; any hit is a bug — fix before
reporting.

## Report (plain, in their chosen review style)

Confirm what was created and changed, where their profile lives (and that it's
theirs to edit), that everything is local-only, and the one restart note:
**the every-turn reminder loads at Claude Code startup — restart Claude Code once
for it to take effect** (the rulebooks are already active from install). Then
give them the true first step: "Now just tell me what you want to build."

## Red flags — STOP if you catch yourself thinking:

| Thought | Reality |
|---|---|
| "I'll ask all seven at once to save time" | One per message with a recommendation. That IS the product. |
| "I'll overwrite settings.json with the new hook" | Merge. Back up first. Never clobber their other hooks. |
| "Re-run — I'll just append again" | Replace the marked block/hook. Duplicates are a bug. |
| "It should have worked" | Grep for `{{`, check the JSON parses, count the markers. Then report. |
| "The user can restart and see if it works" | You verify the files first. They confirm, they don't debug. |
