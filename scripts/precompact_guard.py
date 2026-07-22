#!/usr/bin/env python3
"""Context Guard - PreCompact tripwire.

Fires the instant before Claude Code compacts (summarizes + wipes) the
session. Whatever this script prints to stdout is handed to the
summary-writer as extra instructions. We use that to force the summary to
keep the things whose loss causes the classic "AI forgot everything" loop.

Also appends one line to .graybeard/context-events.log so the user (or the
learn-from-pain loop) can later see exactly WHEN memory wipes happened --
useful evidence when diagnosing a session that went bad.

This script must never crash the session: every failure path degrades to
doing nothing, silently.
"""

import datetime
import json
import sys
from pathlib import Path

PRESERVE_INSTRUCTIONS = """CRITICAL preservation rules for this summary (Context Guard):
1. Keep EVERY decision that was made, verbatim, WITH its reason
   ("chose X over Y because Z"). Losing the reason causes the decision
   to be silently reversed later.
2. Keep the full list of files created or modified, each with its
   plain-words role in parentheses.
3. Keep exact test status: what was RUN and CONFIRMED working, and what
   is known broken or unverified. Never collapse these into "mostly works".
4. Keep the current task and the single NEXT STEP, specific enough to
   execute with no other memory.
5. Keep any rule, constraint, or preference the user stated
   ("never do X", "always use Y").
6. If a HANDOFF.md or PIPELINE.md exists in the project, state that they
   are the source of truth and must be re-read before continuing.
Prefer dropping old file contents and tool output over dropping ANY of
the above."""


def log_event(trigger: str) -> None:
    """Best-effort breadcrumb: when did a memory wipe happen?"""
    try:
        log_dir = Path.cwd() / ".graybeard"
        log_dir.mkdir(exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{stamp} | compaction ({trigger}) | memory wiped, summary injected with preservation rules\n"
        with open(log_dir / "context-events.log", "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass  # a logging failure must never break the session


def main() -> None:
    trigger = "auto"
    try:
        payload = json.load(sys.stdin)
        trigger = payload.get("trigger", "auto")
    except Exception:
        pass  # no/bad stdin: proceed with defaults

    log_event(trigger)

    # stdout -> custom instructions for the compaction summarizer
    try:
        print(PRESERVE_INSTRUCTIONS)
        sys.stdout.flush()
    except Exception:
        pass  # even a closed stdout must not produce an error


if __name__ == "__main__":
    main()
