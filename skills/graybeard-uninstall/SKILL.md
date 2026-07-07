---
name: graybeard-uninstall
description: Use when the user runs /graybeard-uninstall, says "remove Graybeard", "undo the onboarding", "take Graybeard off my machine", or "put my settings back". Surgically removes everything Graybeard added, using the manifest and Graybeard's own markers — and never touches the user's own content.
---

# /graybeard-uninstall — leave no trace, keep everything theirs

Graybeard's promise: removal is **exact** — everything Graybeard added
disappears; everything the user (or Claude Code itself) wrote stays, including
changes made AFTER Graybeard was installed. That is why removal is **surgical
by default**: every Graybeard addition carries a marker put there for exactly
this moment. Blind backup-restore is the LAST resort, because a backup is a
photo of the past — restoring it erases every edit made since.

Where things live (shared vocabulary, used by all Graybeard skills):
- **The manifest** — `~/.claude/graybeard/manifest.txt`: one line per change,
  fields separated by ONE TAB. `CREATED<TAB><path>` or
  `BACKUP<TAB><original><TAB><backup-path>`.
- **Earned laws** — `~/.claude/skills/graybeard-law-*/` (from /learn-from-pain).
- **The law ledger** — `~/.claude/graybeard/ledger.md`.

## Step 1 — read the manifest

Read the manifest. If it's missing, do NOT guess — say so and use Step 5's
marker-only path with per-file confirmation.

## Step 2 — show the plan, get "go" (they confirm, never discover)

Plain list before touching anything: what will be removed from which file
(by marker), which whole files will be deleted (CREATED lines: profile, law
ledger, earned `graybeard-law-*` skills — call these out; they're the user's
earned laws), and what stays untouched. Wait for "go". Destructive — never run
unasked.

## Step 3 — surgical removal (the default)

Work file by file. **Do not delete any backups yet.**

1. **`~/.claude/CLAUDE.md`:** delete exactly the lines from
   `<!-- GRAYBEARD:BEGIN` through `GRAYBEARD:END -->` inclusive. Touch nothing
   outside the markers.
2. **`~/.claude/settings.json`:** parse the JSON. Remove ONLY the
   `hooks.UserPromptSubmit` entry carrying the `_graybeard` marker. Leave every
   other key and hook untouched. If removal leaves `UserPromptSubmit` as an
   empty array, remove just that empty array. Re-serialize and confirm it still
   parses. If the file was CREATED by Graybeard and now contains nothing but
   `{}`, you may delete it; if it contains anything else (Claude Code writes
   its own settings over time), leave the file in place.
   - If settings.json does NOT parse before you start: STOP. Tell the user;
     change nothing in that file.
3. **Delete CREATED files** listed in the manifest (skip the settings.json
   special case above). The three built-in rulebooks live in the plugin, not
   user space — nothing to delete there.

## Step 4 — VERIFY, then (and only then) sweep

Verify first, while every backup still exists:
- settings.json parses as valid JSON; zero `_graybeard` markers; the user's
  other hooks/keys still present.
- CLAUDE.md has zero `GRAYBEARD:BEGIN/END` markers; the user's own content
  above and below the old block is intact.
- No `~/.claude/skills/graybeard-law-*` directories remain. (A `graybeard-law-*`
  folder containing a file NOT in the manifest = the user put something there:
  do not force-delete; list it and ask.)
- Case-insensitive grep for `graybeard` in settings.json and CLAUDE.md: any hit
  that isn't the user's own text is a leftover — fix before proceeding.

Only after every check passes: delete the backup files **listed in the
manifest**, then `~/.claude/graybeard/` (manifest last). If you find
`*.graybeard-backup-*` files NOT in the manifest, list them to the user and ask
— an unmanifested backup may be the only pre-Graybeard copy of something, and
silently deleting it violates the never-guess rule.

If any check FAILS: stop, report exactly what's wrong, and leave all backups in
place — they are the recovery path.

## Step 5 — fallbacks (in order of preference)

1. **Markers without manifest** (manifest missing): same surgery as Step 3 by
   markers alone, with a fresh `*.graybeard-uninstall-backup` copy of each file
   before editing, and per-file confirmation from the user.
2. **Backup-restore** (only if surgery is impossible — e.g. markers were
   hand-mangled): warn the user FIRST, in plain words: *"restoring the backup
   returns this file to the day Graybeard was installed — any changes you or
   Claude Code made to it since then will be lost."* Get explicit approval per
   file. Never present this as the clean path; it isn't.

## Step 6 — report (plain)

What was removed and from where, what was verified, and the restart note:
**restart Claude Code once to fully unload the reminder and laws.** Also say
plainly: the plugin itself (the three built-in rulebooks) is still installed —
to remove it too, use `/plugin` → uninstall graybeard. Leave the door open to
reinstall with `/onboard`.

## Red flags — STOP if you catch yourself thinking:

| Thought | Reality |
|---|---|
| "Restoring the backup is simpler than surgery" | The backup erases everything written since install day. Surgery by markers is the exact path; backups are the emergency exit, with a warning. |
| "No manifest — I'll just delete the graybeard stuff I can find" | Marker-based fallback with per-file confirm. Never guess. |
| "Sweep the backups, then verify" | Verify FIRST. Backups are the recovery copies — they die last. |
| "This stray backup file isn't in the manifest, delete it too" | Unmanifested backup = possibly the only pre-Graybeard copy of something. List and ask. |
| "Deleted — it's clean" | Grep both files, count markers at zero, confirm user content intact. Then say clean. |
