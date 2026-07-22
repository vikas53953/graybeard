---
name: context-guard
description: The AI's memory insurance. Use this skill in EVERY coding session, automatically — whenever building, fixing, or continuing work on any project. It prevents the three memory diseases of long AI sessions: forgetting decisions after auto-compaction, getting dumber as the session grows, and new sessions starting blind. Trigger especially when a session has been running a long time, when the AI repeats itself or contradicts earlier work, when resuming a project, or right before/after any compaction. The user never needs to invoke this by name.
---

# Context Guard — the memory insurance

**The problem in plain words:** the AI's working memory (the "context window")
is a whiteboard of fixed size. As the session grows, the whiteboard fills up.
When it's full, the tool secretly photographs the whiteboard, wipes it, and
writes a short summary back. Anything not in that summary is **gone** — and
that's when the AI "forgets" a fix, re-breaks something, or asks you to
re-explain what you settled an hour ago.

The cure is old-school ops discipline: **anything worth remembering goes on
disk, not on the whiteboard.** Files survive; chat memory doesn't.

---

## The Four Laws

### Law 1 — Checkpoint at every boundary
The moment any of these happens, update `HANDOFF.md` in the project root
(use the template in the plugin's `templates/HANDOFF-template.md`) **before doing anything
else**:

- a fix is confirmed working
- a pipeline stage or gate completes
- the user approves anything
- a decision is made ("we'll use X, not Y" — and **why**)
- you are about to try a second attempt at a failed fix (two-strikes moment)

The test, every time: **"If this session died right now, could a brand-new
session pick up from the files alone?"** If no — you are not done writing.

### Law 2 — Resume from disk, never from memory
At the start of any session (or after any compaction), before touching code:
read `HANDOFF.md` and `PIPELINE.md` if they exist. Trust the files over your
own recollection — your recollection may be a lossy summary. Never ask the
user to re-explain something the files already answer. Tell the user in one
line what you resumed from: *"Picking up from HANDOFF.md — last confirmed
state: X. Next step: Y."*

### Law 3 — Notice your own degradation
If you catch yourself doing any of these, STOP — checkpoint to `HANDOFF.md`
immediately, then tell the user plainly:

- repeating a question the user already answered
- re-reading files you already read this session
- contradicting or undoing an earlier confirmed fix
- losing track of which fix attempt you're on

Say: *"My working memory is getting unreliable — I've saved the full state to
HANDOFF.md. I recommend a fresh session; it will resume exactly from the file.
Say 'continue anyway' to keep going here."* A fresh session with a good
handoff file **always** outperforms a bloated session.

### Law 4 — One task, one session (prefer it)
When the user starts a clearly new task in an old session, offer once:
*"This is a new task — a fresh session would give you sharper results. Your
current state is safe in HANDOFF.md. Want to continue here anyway?"* Respect
their answer; never nag twice.

---

## What HANDOFF.md must contain (and must NOT)

MUST (see the template):
- **DECISIONS** — every settled choice, one line each, with the *why*
- **FILES TOUCHED** — each file + its plain-words role in parentheses
- **CONFIRMED WORKING** — what was actually run and proven (not "should work")
- **NOT WORKING / OPEN** — known-broken things and unanswered questions
- **NEXT STEP** — the single next action, specific enough to execute cold

MUST NOT:
- code snippets (they belong in the code files)
- anything already in `PIPELINE.md` — HANDOFF.md is the *session* state,
  PIPELINE.md is the *project* stage. Link, don't duplicate.
- walls of text. The whole file under ~60 lines. A handoff nobody reads
  protects nobody.

---

## How the automatic part works (the hooks)

Two tripwires are installed automatically with the plugin via `hooks/hooks.json` (plain words:
"hooks" = small scripts the coding tool fires automatically on events —
like an SNMP trap triggering a config backup):

1. **PreCompact** — fires the instant before the tool wipes the whiteboard.
   It injects strict instructions into the summary-writer: *preserve every
   decision, file role, test result, and the next step — verbatim.* So even
   the automatic summary keeps what matters.
2. **SessionStart** — fires when a session starts or resumes. It reads
   `HANDOFF.md` and `PIPELINE.md` off disk and puts them straight into the
   new session's memory. Resume is automatic, not a favor you ask for.

The hooks are the seatbelt. The Laws are the driving. Both together mean the
user never loses work to a memory wipe — and never has to know the word
"compaction" at all.

## If the hooks aren't installed

The Laws still apply in full. The skill works in behavior-only mode on any
tool (Cursor, Codex, etc.) — you just checkpoint by discipline instead of by
tripwire. Never skip Law 1 because "the hook will catch it": the hook
preserves a summary; only YOU can write a proper handoff.
