<!-- GRAYBEARD:BEGIN (managed by Graybeard /onboard — edit above/below this block, not inside; /graybeard-uninstall removes exactly this block) -->

# Standing orders ({{USER_NAME}} — installed by Graybeard)

These are your personal working laws. Claude reads this file at the start of
every project. Edit `~/.claude/graybeard/profile.md` and re-run `/onboard` to
change them.

- **New idea, new feature, or anything bigger than a small fix** (including
  one-liners like "build X"): run the `graybeard-conductor` skill. If the
  project has a `PIPELINE.md`, read it and resume — never redo approved stages.
- **Any small build / fix / debug / refactor:** follow `graybeard-worklaw`.
  Brief before code (BROKEN / CAUSE / CHANGE / NEIGHBORS / BLINDSPOTS), wait for
  "go", re-test neighbors before saying done, done report ends with TEST IT
  steps and a quiz offer.
- **Any vague or unfamiliar request:** run `graybeard-unknowns` — blindspot
  pass, one question at a time, mock before wiring.
- **Review medium:** {{USER_NAME}} reviews finished work as {{REVIEW_STYLE}}.
  Anything to approve (specs, plans, status, comparisons, QA results, done
  reports for big changes) is shown that way — never a wall of text. Machine
  files stay markdown; {{USER_NAME}}'s view is always {{REVIEW_STYLE}}.
- **Always:** {{PLAINNESS}}; name every assumption out loud; one goal at
  a time; plain-words role for every file named.
  <!-- template rule: placeholders are always complete phrases that stand alone
       between punctuation — never spliced into the middle of a sentence. -->
- **Logs before guesses (Watchtower):** after every build, run, or reported
  failure, read the app's own logs first and diagnose from that evidence.
  Autonomy level {{AUTONOMY_LEVEL}}.

<!-- GRAYBEARD:END -->
