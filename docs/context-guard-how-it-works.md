# Context Guard — how it works, in plain words

## The disease

Your AI has a whiteboard, not a notebook. Everything you discuss lives on
one whiteboard of fixed size. When it fills up, the coding tool quietly
photographs it, wipes it clean, and writes a short summary back in the
corner. The tool calls this "compaction." You never see it happen.

Everything not in that summary is gone. That's the real reason behind:

- "We fixed this yesterday, why is it broken again?"
- The AI asking you to re-explain the project mid-session
- Fixes that reverse decisions you already settled ("wait, why is it
  using Y again? We chose X!")
- Sessions that start smart and get dumber by the hour

It's not the AI being lazy. It's amnesia by design — and nobody told you.

## The cure — two parts

**Part 1: The Laws (discipline).** The AI must write anything worth
remembering to a file on disk — `HANDOFF.md` — at every natural boundary:
a fix confirmed, a stage done, a decision made. Files survive the wipe;
the whiteboard doesn't. The standing test: *"if this session died right
now, could a new one continue from the files alone?"*

**Part 2: The tripwires (automation).** Two tiny scripts hook into the
coding tool's own events:

| Tripwire | Fires when | What it does |
|---|---|---|
| PreCompact | the instant before a wipe | forces the auto-summary to keep every decision (with reasons), file roles, real test status, and the next step — and logs the wipe to `.graybeard/context-events.log` so you have evidence it happened |
| SessionStart | a session starts or resumes | reads `HANDOFF.md` + `PIPELINE.md` off disk and hands them to the new session — it opens already knowing where you stopped |

The Laws are the driving; the tripwires are the seatbelt. With both, a
memory wipe becomes a non-event: state was already on disk, and the next
session picks it up automatically.

## For network people (the honest analogy)

The context window is device RAM — running-config. Compaction is an
unplanned reboot with a partial config backup. Context Guard is what any
network engineer already does about that: **scheduled config backups to a
TFTP server at every change window** (Law 1), **restore-from-backup on
boot** (SessionStart), and a **syslog line every time a reboot happens**
(the events log). You'd never run 800 firewalls trusting running-config
alone. Don't run your AI that way either.

## What it does NOT do

- It does not raise the memory limit — nothing can.
- It does not make marathon sessions a good idea. Fresh session per task,
  resumed from files, still beats one long session every time. The guard
  makes fresh sessions *cheap*, which is the point.
- The hooks are Claude Code-only today (Cursor/Codex have no PreCompact
  event). On those tools the Laws still work in behavior-only mode.
