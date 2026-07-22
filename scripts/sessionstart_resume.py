#!/usr/bin/env python3
"""Context Guard - SessionStart resume.

Fires when a session starts, resumes, or continues after a compaction.
Whatever this script prints to stdout is placed into the new session's
context. We use it to hand the fresh session its own memory back:
HANDOFF.md (session state) and PIPELINE.md (project stage), read straight
off disk.

Result: the user never re-explains a project. The new session opens
already knowing where the last one stopped.

Must never crash the session: every failure path degrades to printing
nothing.
"""

import sys
from pathlib import Path

MAX_CHARS_PER_FILE = 8000  # keep the injection small; these files should be short anyway

HEADER = """[Context Guard] State files found on disk. These are the source of
truth for this project -- trust them over any summarized memory. Read them
now, then tell the user in ONE line what you resumed from and what the next
step is. Do not ask the user to re-explain anything these files answer.
"""


def read_capped(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    if len(text) > MAX_CHARS_PER_FILE:
        text = text[:MAX_CHARS_PER_FILE] + "\n[... truncated by Context Guard -- open the file for the rest ...]"
    return text.strip()


def main() -> None:
    try:
        cwd = Path.cwd()
    except Exception:
        return

    sections = []
    for name in ("HANDOFF.md", "PIPELINE.md"):
        p = cwd / name
        if p.is_file():
            content = read_capped(p)
            if content:
                sections.append(f"===== {name} =====\n{content}")

    if sections:
        print(HEADER)
        print("\n\n".join(sections))
    # No state files -> print nothing; session starts normally.


if __name__ == "__main__":
    main()
    sys.exit(0)
