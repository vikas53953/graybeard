# Graybeard

**A senior engineer, watching over your shoulder — for people who don't write code.**

Graybeard is a free add-on for [Claude Code](https://claude.com/claude-code)
(the AI coding assistant you run in your terminal). It gives the AI the
discipline of a seasoned engineering team, so your projects don't quietly fall
apart the way AI-built projects usually do.

It does three things:

1. **Ships proven working laws** — habits like *brief me before you code*,
   *never say "done" without proving it ran*, and *don't break the thing next to
   the thing you just fixed*.
2. **Personalizes them to you** in a short interview — your name, how you
   like to review work, how much it should explain.
3. **Gets smarter from your worst days** — point it at a session that made you
   angry and it turns that pain into a new, *tested* rule so it never happens
   again.

You never need to know how programmers think. Graybeard thinks that way for you.

---

## Install (2 commands)

Inside Claude Code, type these two lines. (A "marketplace" here just means the
public list of add-ons; "plugin" is the add-on itself.)

```
/plugin marketplace add vikas53953/graybeard
/plugin install graybeard@graybeard
```

Then restart Claude Code once (close it and open it again) so the add-on loads.

> **On Windows, or if `/plugin marketplace add` shows nothing?** That command can
> silently no-op (a known Claude Code quirk). Confirm with `/plugin list` — if
> graybeard isn't there, restart Claude Code fully, or see
> [`docs/how-it-works.md`](docs/how-it-works.md) for the settings-file method.

## Set it up (a short interview)

Just tell Claude, in plain words:

```
set up Graybeard
```

(If you prefer a typed command, it's `/graybeard:onboard` — but you never have to
remember that; plain English works.)

Graybeard asks you **seven short questions, one at a time** — each with a
suggested answer, so you can often just say "yes." At the end (optional) it asks
about *the last time an AI session made you angry* and turns that story into your
very first personal rule.

When it's done, it has quietly written a few files that are **yours** (you can
read and edit any of them):

- your settings, in plain English, in one file you own;
- your standing orders, that the AI reads at the start of every project;
- a gentle every-turn reminder so the AI never drifts off your rules.

Nothing is sent anywhere. It all stays on your computer.

## Your first project

Just tell Claude what you want, in plain words:

```
build me a simple page that tracks my daily water intake
```

Watch what changes. Instead of dumping code on you, Graybeard will:

- give you a short **brief** — what it's about to do — and wait for your "go";
- show you things to approve as **visual pages you open in a browser**, not walls
  of text;
- ask you **one question at a time** when it's unsure, always with a recommendation;
- refuse to say "done" until it has actually run the thing and can prove it works.

That's the whole point: you stay in the driver's seat, and nothing ships broken.

## The loop — learn from a painful session

When an AI session goes badly, don't just sigh. Feed it to Graybeard — just say:

```
learn from this painful session
```

(Typed form: `/graybeard:learn-from-pain`.)

Point it at the transcript (a saved copy of the chat) or just describe what kept
going wrong. Graybeard finds the *underlying* mistake, writes one general rule to
prevent it, **proves the rule works** with a quick before/after test (it tells
you the small cost first, and you can decline), shows you the result on a visual
page, and installs it. Your AI literally gets better from your own bad days.

## Remove it anytime (leaves no trace)

Just say:

```
remove Graybeard
```

(Typed form: `/graybeard:graybeard-uninstall`.)

Every file Graybeard added is removed and every file it touched is put back
exactly as it was. It keeps a precise record of everything it changed, so this is
clean and complete.

---

## Your privacy — the short version

- **Everything stays local.** Graybeard reads your files and transcripts on your
  own machine. It never uploads anything, has no account, no server, no tracking.
- **Nothing is overwritten blindly.** Before it changes any file of yours, it
  saves a backup copy first.
- **It plays nice with others.** If you already run other discipline add-ons,
  Graybeard notices and steps aside where they overlap, instead of fighting them.

## What's inside (plain-words map)

You mostly just talk to Claude in plain words — it picks the right piece for you.
Here's what's under the hood:

| Piece | What it is | Say (or type) |
|---|---|---|
| Work Law | the day-to-day habits for small fixes and builds | *automatic* |
| Unknowns Law | how it clears up fuzzy requests before building | *automatic* |
| Conductor | runs a full "idea → finished product" pipeline with checkpoints | *automatic* |
| Setup interview | makes the laws yours | "set up Graybeard" · `/graybeard:onboard` |
| The loop | turns bad sessions into tested rules | "learn from this session" · `/graybeard:learn-from-pain` |
| Clean removal | puts your machine back exactly | "remove Graybeard" · `/graybeard:graybeard-uninstall` |

The first three trigger themselves when they fit what you're doing — you don't
call them by name.

Want the full story of how it works? See [`docs/how-it-works.md`](docs/how-it-works.md).

## For tinkerers & contributors

Graybeard is almost entirely plain text (Markdown) — no build step, nothing to
compile. If you want to improve a law or add one, see
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE) — free to use, change, and share.
