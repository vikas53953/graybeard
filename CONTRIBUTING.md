# Contributing to Graybeard

Thanks for wanting to make Graybeard better. It's built to be easy to change:
it's almost entirely plain text, with no build step and nothing to compile.

## What Graybeard is made of

- **Skills** (`skills/*/SKILL.md`) — Markdown files that tell the AI how to
  behave. Each starts with a small `---` header giving the skill a `name` and a
  `description` (the `description` is what makes the AI reach for that skill at
  the right moment — write it as a list of trigger situations).
- **Templates** (`templates/`) — fill-in-the-blank files that `/onboard` and the
  loop copy into the user's space, replacing `{{PLACEHOLDER}}` tokens with real
  answers.
- **Docs** (`README.md`, `docs/`) — written for non-coders. No unglossed jargon.

That's it. No JavaScript, no dependencies, no compile step.

## Ground rules for laws

Graybeard's whole value is discipline, so its own laws must hold to a high bar:

1. **Class, not case.** A law must prevent a whole *class* of failure, never one
   specific scenario. If you find yourself writing "if the user asks about X…",
   stop and generalize. A reviewer who can point at the single case a law was
   built for will reject it.
2. **Plain language.** Laws and docs are read by people who don't code. Gloss
   every technical term the first time it appears. Short sentences.
3. **Visual review, never walls of text.** Anything a user must approve is a
   self-contained HTML page (no internet dependencies — everything inline), not a
   block of prose.
4. **Evidence before "done."** If your change claims to fix or improve something,
   show how you verified it — ideally the same baseline-vs-with-law test the loop
   uses.
5. **Safety and reversibility.** Any change that writes to a user's files must
   back them up first and record them in the manifest, so uninstall stays exact.
6. **One job per file.** Keep each skill focused; don't grow "god files." Nothing
   in the shipped output should exceed roughly 500 lines.

## How to propose a change

1. Fork the repo and make your change in a branch.
2. If you changed or added a law, include evidence it helps — the simplest is a
   short before/after showing the AI behaving badly without your law and well
   with it.
3. Keep placeholders consistent: if you add a new `{{TOKEN}}` to a template, make
   sure `/onboard` (or the relevant skill) fills it, and that nothing ships with a
   raw `{{` left in it.
4. Open a pull request describing, in plain words, the pain your change prevents.

## Testing your change locally

Because skills are just instructions, the honest test is behavioral: run Claude
Code with your changed skill and check it actually behaves the way the law
intends. For the personalization and loop skills, do a dry run in a throwaway home
folder and confirm:

- all expected files are generated, with no leftover `{{` tokens;
- `settings.json` is still valid and merged (not overwritten);
- backups exist for every file that was modified;
- `/graybeard-uninstall` puts everything back cleanly.

## Style

- Match the voice of the existing skills: short, direct, a "Red flags — STOP if
  you catch yourself thinking" table where it helps.
- Prefer the simplest thing that works. Complexity has to earn its keep.

By contributing you agree your work is released under the project's
[MIT license](LICENSE).
