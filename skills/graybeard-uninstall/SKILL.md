---
name: graybeard-uninstall
description: Use when the user runs /graybeard-uninstall, says "remove Graybeard", "undo the onboarding", "take Graybeard off my machine", or "put my settings back". Removes everything Graybeard generated and restores every backup exactly, using the manifest — leaves the machine as if Graybeard was never installed.
---

# /graybeard-uninstall — leave no trace

Graybeard's promise (R6, acceptance example AE3): uninstall restores the user's
`settings.json` to byte-equivalent-minus-our-additions and removes every file it
generated. This works because `/onboard` and `/learn-from-pain` recorded every
change in a manifest. Uninstall just replays it in reverse. Never guess what to
remove — the manifest is the source of truth.

## Step 1 — read the manifest (the exact record)

Read `~/.claude/graybeard/manifest.txt`. Each line is tab-separated:
- `CREATED <path>` — a file Graybeard made (didn't exist before). Delete it.
- `BACKUP <original>	<backup-path>` — a file Graybeard modified after backing it
  up. Restore the original from the backup.

If the manifest is missing, do NOT start deleting by guesswork. Tell the user the
manifest is gone and offer the careful fallback in Step 5.

## Step 2 — show the plan, get "go" (they confirm, never discover)

Before touching anything, show a plain list: which files will be deleted, which
will be restored-from-backup, and which of the user's own files are untouched.
Call out that their personal laws earned via `/learn-from-pain` will be removed
too (they're in the manifest). Wait for "go". This is a destructive action —
never run it unasked.

## Step 3 — restore backups, then delete created files (order matters)

1. **Restore first.** For each `BACKUP <original>	<backup>` line: copy the backup
   back over the original. This returns `~/.claude/CLAUDE.md` and
   `~/.claude/settings.json` to their pre-Graybeard contents in one move — which
   is cleaner and safer than trying to surgically un-merge the hook or the
   CLAUDE.md block.
   - Edge case: if the ORIGINAL never existed (Graybeard created `settings.json`
     from scratch), there's a `CREATED` line for it instead of a `BACKUP` — it
     gets deleted in the next step, correctly.
2. **Delete created files.** For each `CREATED <path>` line: delete it. This
   covers `profile.md`, the ledger, and every `graybeard-law-*` skill the user
   earned via `/learn-from-pain`. (The three built-in rulebooks live in the
   plugin, not the user's space — onboarding never copied them, so there's
   nothing of theirs to delete there.)
3. **Remove the backups and the Graybeard folder.** Once originals are restored,
   glob-delete **every** `*.graybeard-backup-*` file under `~/.claude/` — not
   only the ones named in the manifest. (A user who re-ran `/onboard` may have
   older orphaned backups from earlier runs; sweep them all so nothing is left
   behind.) Then remove the now-empty `~/.claude/graybeard/` directory and any
   emptied `~/.claude/skills/graybeard-*` directories, deleting the manifest
   itself last.

## Step 4 — verify the clean diff (AE3) before claiming done

Do not tell the user it's clean until you've checked:
- `~/.claude/settings.json` parses as valid JSON and contains NO
  `graybeard-every-turn-reminder` entry and no `_graybeard` markers.
- `~/.claude/CLAUDE.md` contains NO `GRAYBEARD:BEGIN` / `GRAYBEARD:END` markers.
- No `~/.claude/skills/graybeard-*` directories remain.
- `~/.claude/graybeard/` is gone.
- No stray `*.graybeard-backup-*` files remain.
Grep for `graybeard` (case-insensitive) under `~/.claude/settings.json` and
`~/.claude/CLAUDE.md`; any hit that isn't the user's own text is a leftover —
fix it before reporting.

## Step 5 — fallback if the manifest is missing

Only with the user's explicit go-ahead, remove by known markers instead of by
manifest: strip the `GRAYBEARD:BEGIN…END` block from `CLAUDE.md`, remove the
`settings.json` hook entry carrying `_graybeard`, and delete
`~/.claude/skills/graybeard-*` and `~/.claude/graybeard/`. Back up each file
before editing it (a `*.graybeard-uninstall-backup` copy) so a mistake is
recoverable. Show the diff and let the user confirm each file.

## Step 6 — report (plain)

Confirm what was restored and removed, and the restart note: **the every-turn
reminder and laws are unloaded at the next Claude Code startup — restart once to
fully clear them.** Thank them; leave the door open to reinstall with `/onboard`.

## Red flags — STOP if you catch yourself thinking:

| Thought | Reality |
|---|---|
| "No manifest — I'll just delete the graybeard stuff I can find" | Guessing risks the user's own files. Use the manifest, or the marker-based fallback with per-file confirm. |
| "I'll un-merge the hook by hand" | Restoring the backup is exact and safe. Prefer it over surgery. |
| "Deleted — it's clean" | Grep settings.json and CLAUDE.md for `graybeard`; count the markers at zero. Then say clean. |
| "The user asked, I'll wipe it all now" | Show the plan and get 'go' — this is destructive and includes their earned laws. |
