# 🧙 Graybeard

**A senior engineer, watching over your shoulder — for people who don't write code.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](PIPELINE.md)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-orange.svg)](https://claude.com/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

You have ideas. AI can write the code. And yet your projects keep collapsing —
the AI says *"fixed!"* while the app stays broken, every fix breaks the thing
next to it, and the code becomes a black box you can't question.

**That's not your fault. Nobody gave the AI rules.**

Graybeard is a free plugin for [Claude Code](https://claude.com/claude-code)
that gives your AI the discipline of a seasoned engineering team — written in
plain language, personalized to you in a 10-minute interview, and (the part
nothing else has) **able to learn new rules from your own painful sessions,
with proof they work.**

---

## Before / after

**Without Graybeard:**

> **You:** the button still doesn't work
> **AI:** Fixed! The issue was in the event handler. ✅
> **You:** it's still broken
> **AI:** You're right, I apologize! Fixed now. ✅
> **You:** IT'S STILL BROKEN
> *…repeat for 25 days.*

**With Graybeard:**

> **You:** the button still doesn't work
> **AI:** Checking my notes — you reported this yesterday, so I won't ask you to
> re-explain. *[reads the app's own logs]* The log shows the click event fires
> but the save call returns an error on line 3 of the log. Here's my brief:
> what's broken, the root cause with evidence, what I'll change, and what I'll
> re-test so the fix doesn't break the page next to it. Say "go".
> **AI (later):** Done — and here are 2 steps so you can confirm it yourself.
> I already ran them; you're confirming, not discovering.

---

## What it does — three things

| | |
|---|---|
| 📜 **Proven working laws** | Habits like *brief me before you code*, *never say "done" without running it*, *fix the class of the bug, not just today's case*, *read the logs before guessing*. Shipped tested — each law was verified to actually change AI behavior before it got in. |
| 🪪 **Made yours in 10 minutes** | A short interview (7 questions, one at a time, each with a suggested answer) writes your personal standing orders and a gentle every-turn reminder. Your name lives in exactly one file you own. |
| 🔁 **The loop — it learns from your pain** | Point it at a session that made you angry. It finds the *underlying* disease, writes **one general rule** (never a case-patch), **proves the rule works** with a before/after test, shows you the evidence, and installs it. Your AI literally gets better from your own worst days. |

You never need to know how programmers think. Graybeard thinks that way for you.

---

## Install (2 commands)

Inside Claude Code, type:

```
/plugin marketplace add vikas53953/graybeard
/plugin install graybeard@graybeard
```

Then restart Claude Code once so the plugin loads.

> **On Windows, or if `/plugin marketplace add` shows nothing?** That command can
> silently no-op (a known Claude Code quirk). Confirm with `/plugin list` — if
> graybeard isn't listed, restart Claude Code fully, or see
> [`docs/how-it-works.md`](docs/how-it-works.md) for the settings-file method.

## Set it up

```
set up Graybeard
```

Plain English always works (the typed form is `/graybeard:onboard`). Seven short
questions, one at a time, each with a suggested answer — often you just say
"yes." The optional last question asks about *the last time an AI session made
you angry*, and turns that story into your very first personal rule.

Everything it writes is a file **you own and can read**: your profile, your
standing orders, and an every-turn reminder that keeps the AI from drifting.
Nothing is sent anywhere — no account, no server, no telemetry.

## Your first project

```
build me a simple page that tracks my daily water intake
```

Watch what changes:

- 📋 a short **brief** before any code — and it waits for your "go"
- 🖼️ approvals arrive as **visual pages** you open in a browser, never walls of text
- ❓ **one question at a time** when it's unsure, always with a recommendation
- 🗺️ for bigger ideas, a full **idea → product pipeline**: requirements you
  approve, clickable mock-ups before real code, a system-design page that shows
  every component *and the engineering principles applied*, and a scoreboard
  (`PIPELINE.md`) so a brand-new session resumes exactly where the last one stopped
- ✅ it refuses to say "done" until it has **run the thing and can prove it** —
  you confirm its evidence; you never discover its bugs

## The loop — turn a bad session into a permanent rule

```
learn from this painful session
```

(Typed form: `/graybeard:learn-from-pain`.) Point it at a saved transcript or
just describe what kept going wrong. Graybeard:

1. finds the **class-level disease** (not the surface symptom),
2. drafts **one general rule** — if the rule mentions your specific feature, it
   failed its own standard,
3. **tells you the small testing cost first** (you can decline and install
   untested, clearly flagged),
4. proves it: baseline runs *without* the rule fail, runs *with* it pass,
5. shows you the evidence on a visual page, and installs the rule.

And it's already becoming proactive: when a fix fails twice in a row (the
"two-strikes" moment), Graybeard offers the loop right there — pain is freshest
at the moment it happens.

## Remove it anytime — leaves no trace

```
remove Graybeard
```

(Typed form: `/graybeard:graybeard-uninstall`.) Every file it added is removed;
every file it touched is restored from the backup it took first. It keeps a
manifest of everything it changed, so removal is exact — this is tested to the
byte.

---

## 🔍 The receipts — this repo contains its own birth certificate

Graybeard was built by a network engineer who cannot write code, using Claude —
**under Graybeard's own rules.** Every gate of its development is in this repo,
unedited:

| Stage | Evidence |
|---|---|
| Requirements the owner approved | [`docs/gates/gate1-requirements.html`](docs/gates/gate1-requirements.html) |
| Clickable mocks before any code | [`docs/gates/gate2-mocks.html`](docs/gates/gate2-mocks.html) |
| System design & build plan | [`docs/gates/gate3-plan.html`](docs/gates/gate3-plan.html) |
| Code review: 10 issues found, honestly logged | [`docs/gates/stage6-review.html`](docs/gates/stage6-review.html) |
| QA: 18/18 paths run, not read | [`docs/gates/stage7-qa.html`](docs/gates/stage7-qa.html) |
| The ship decision itself | [`docs/gates/gate4-ship.html`](docs/gates/gate4-ship.html) |
| Every deviation from the plan | [`implementation-notes.md`](implementation-notes.md) |

We think every AI-built project should ship its receipts. This one starts.

## Honest positioning — is Graybeard for you?

If you **read code fluently**, you may be happier with
[compound-engineering](https://github.com/EveryInc/compound-engineering-plugin),
[gstack](https://github.com/garrytan/gstack), or
[mattpocock/skills](https://github.com/mattpocock/skills) — mature,
engineer-first systems we admire (and credit below). Graybeard is for the rest
of us: domain experts, founders, and builders who review *outcomes*, not diffs.
One idea here is worth stealing at any skill level, though: **the loop.** No
other tool turns your failures into tested rules automatically.

## What's inside (plain-words map)

| Piece | What it is | Say (or type) |
|---|---|---|
| 🛠️ Work Law | day-to-day habits for fixes and small builds | *automatic* |
| 🔦 Unknowns Law | clears up fuzzy requests before building | *automatic* |
| 🎼 Conductor | the idea → product pipeline with checkpoints | *automatic* |
| 🪪 Setup interview | makes the laws yours | "set up Graybeard" · `/graybeard:onboard` |
| 🔁 The loop | turns bad sessions into tested rules | "learn from this session" · `/graybeard:learn-from-pain` |
| 🧹 Clean removal | puts your machine back exactly | "remove Graybeard" · `/graybeard:graybeard-uninstall` |

The first three trigger themselves when they fit what you're doing — you never
call them by name. Full story: [`docs/how-it-works.md`](docs/how-it-works.md).

## Roadmap

- **v0.2 — the automatic loop:** learn-from-pain fires itself at the pain moment
  (with guardrails: checks your existing rules first, caps active laws to
  prevent rule-sprawl, and never installs without your nod).
- **Community laws:** export/import rules *with their test evidence attached*.
- Have an idea born from your own painful session? That's exactly the point —
  [open an issue](../../issues).

## Credits

Graybeard stands on ideas from people we admire:
[Thariq Shihipar](https://x.com/trq212)'s *Field Guide to Fable* (finding your
unknowns), [Garry Tan's gstack](https://github.com/garrytan/gstack)
(plain-English decision briefs, click-everything QA),
[Matt Pocock's skills](https://github.com/mattpocock/skills) (one-question
grilling, checkable completion), and
[Every's compound-engineering](https://github.com/EveryInc/compound-engineering-plugin)
(the one-plan-file pipeline). The synthesis, the plain-language layer, and the
loop are ours; the shoulders are theirs.

## License

[MIT](LICENSE) — free to use, change, and share.
