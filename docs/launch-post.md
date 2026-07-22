# Launch posts — v0.2.0 (edit freely, these are drafts in your voice)

## X / Twitter (thread starter)

I manage 800+ firewalls at a bank. I cannot write code.

My AI told me "Fixed! ✅" for 25 days straight while the button stayed broken.

So I built the tool that makes AI prove its work — under its own rules, with
every receipt in the repo.

Graybeard v0.2 is out: [repo link]

🧵 what's new:

1/ Vibe-QA: your AI wrote the code AND the tests — so "47 tests pass" means
nothing. Vibe-QA tests like a stranger: clicks every button, proves screens
show live data (not fakes), walks real journeys with Playwright, ends with an
honest "X% functional." Works on ANY app, even ones built without Graybeard.

2/ Context Guard: ever notice your AI "forgets" a fix mid-session? Its memory
gets silently wiped when full. Context Guard checkpoints every decision to
disk, fires a tripwire the instant before a wipe, and hands new sessions
their memory back. You never re-explain your project again.

3/ The part nothing else has: point Graybeard at a session that made you
angry. It finds the underlying disease, writes ONE general rule, PROVES the
rule works with a before/after test, and installs it. Your AI gets better
from your worst days.

Built on ideas from @mattpocock's skills, @garrytan's gstack, and
@every's compound-engineering — for the rest of us who review outcomes,
not diffs.

MIT. Free. Receipts included: [repo link]

## Reddit (r/ClaudeAI) — title options

- "I can't write code, my AI lied to me for 25 days, so I built a plugin that
  makes it prove its work (v0.2: it now QAs the app like a stranger and
  survives context wipes)"
- "Why your vibe-coded app 'passes all tests' but is still broken — and the
  open-source fix"

## Reddit body (short)

Network engineer, zero coding ability. After my AI said "fixed!" for 25 days
on one button, I built Graybeard — a free Claude Code plugin that acts like a
senior engineer for non-coders: briefs before code, clickable mocks before
real code, hard approval gates, and it refuses to say "done" without running
the thing.

v0.2 adds the two things I couldn't find anywhere:

**Vibe-QA** — outside-in testing for AI-built apps. The AI that writes the
code also writes the tests, so green tests prove nothing. Vibe-QA clicks
everything, audits whether screens show live data or hard-coded fakes, runs
Playwright journeys, and gives an honest "X% functional" verdict. Runs
standalone on any app.

**Context Guard** — the AI's memory gets silently wiped when full (that's why
it "forgets" your fixes). This checkpoints decisions to disk, hooks the
moment before a wipe, and auto-resumes new sessions from files.

The repo contains its own birth certificate — every approval gate and QA run
from its own development, unedited. It was built under its own rules by
someone who can't read the code it produced. AMA about that experience.

[repo link]

## Posting notes (delete before publishing)
- Post the X thread and Reddit on different days; Reddit dislikes cross-spam.
- Reply to every single comment in the first 24h — that's the algorithm.
- The 90-second screen capture of Vibe-QA catching a fake-data screen is the
  single highest-leverage asset; pin it to the thread when ready.
- awesome-claude-code style lists: submit a PR adding Graybeard (check each
  list's contributing rules first).
