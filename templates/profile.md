# Graybeard profile — {{USER_NAME}}

This file is the **single source of truth** for how Graybeard works with you.
It was written by `/onboard` and it is yours to edit anytime. Change a line
here, then run `/onboard` again to regenerate your standing orders and the
every-turn reminder from it. (Telling Claude "reread my Graybeard profile"
applies your changes for the current session only — the regenerated files need
the re-run.) Nothing here leaves your machine.

Generated: {{GENERATED_DATE}}   ·   Graybeard version: {{PLUGIN_VERSION}}

## Who you are
- **Name:** {{USER_NAME}}
- **Background:** {{USER_BACKGROUND}}
- **How much code you read:** {{CODE_COMFORT}}

## How you want to work
- **Review style (how finished work is shown to you):** {{REVIEW_STYLE}}
- **Plain-language level:** {{PLAINNESS}}
- **Two-strikes rule (stop-and-root-cause after 2 failed tries):** {{TWO_STRIKES}}
- **Quiz & teach-me offers:** {{QUIZ_PREF}}

## Watchtower autonomy
- **Level:** {{AUTONOMY_LEVEL}}
  - LEVEL 1 = propose-first: Claude reads the logs, tells you what it found, and
    asks before changing anything.
  - LEVEL 2 = fix-quietly-and-report: Claude may apply *safe* fixes on its own
    and report them; anything destructive or scope-changing is still asked first.

## Your first law seed (from the story question, optional)
{{STORY_SEED}}

## Other tools detected on your machine (traffic control)
{{TRAFFIC_NOTE}}

---
*Edit freely. This profile is the source of truth — your CLAUDE.md standing
orders and the every-turn reminder are regenerated from it on each `/onboard`
run. Run `/graybeard-uninstall` to remove everything Graybeard added — exactly
and only Graybeard's additions.*
