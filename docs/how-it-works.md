# How Graybeard works

A plain-language tour. No prior coding knowledge assumed; the few technical words
are glossed the first time they appear.

## The one idea

AI coding assistants are powerful but undisciplined. Left alone they claim things
are "done" when they aren't, fix one thing while breaking another, bury you in
walls of text, and guess instead of checking. A senior engineer doesn't do those
things — not because they're smarter in the moment, but because they follow
**habits earned from past pain.**

Graybeard is those habits, written down as files the AI must read, plus a way to
**grow new habits from your own bad sessions.** You get the discipline without
having lived the twenty years.

## The three parts

### 1. The starter rulebook (the laws)

Three **skills** ship with Graybeard. (A "skill" is just a Markdown file — plain
text — that tells the AI how to behave in a certain situation.)

- **The Work Law** (`graybeard-worklaw`) — for everyday fixes and small builds.
  Brief you before coding; never claim "done" without running it; re-test the
  things next to what it changed; fix the *class* of problem, not the one case;
  read the app's own logs before guessing.
- **The Unknowns Law** (`graybeard-unknowns`) — for fuzzy requests. Surface what
  you don't know you don't know; ask one sharp question at a time; show you a
  fake mock-up before building the real thing.
- **The Conductor** (`graybeard-conductor`) — for anything bigger. Runs a full
  pipeline from idea to finished product, with a scoreboard and four checkpoints
  where you approve a **visual page** before it moves on.

### 2. The onboarding interview ("set up Graybeard")

You start it by just telling Claude "set up Graybeard" (or the typed form
`/graybeard:onboard`). The starter laws are written for "the user" in general;
this interview makes them
**yours**: it asks seven short questions (one at a time), then writes:

- **`~/.claude/graybeard/profile.md`** — your answers in plain English. This is
  the *single source of truth*: change a line here, re-run `/graybeard:onboard`, and
  everything updates. (`~` means your home folder; `.claude` is where Claude Code
  keeps its settings.)
- **A block in `~/.claude/CLAUDE.md`** — your standing orders. Claude Code reads
  this file at the start of every project, so your rules are always in force.
- **An entry in `~/.claude/settings.json`** — a small automatic reminder that
  re-states your top rules on every message, so the AI never drifts. (A
  "settings file" is where Claude Code keeps its configuration; Graybeard
  *merges* into it — adds one line without disturbing the rest — and backs it up
  first.)
The three rulebooks themselves aren't copied or edited — they ship with the
plugin and speak in general terms. What makes them act *personally* is the
standing orders and the every-turn reminder above: the AI reads both each
session, so it always knows your name, that you want visual reviews, and your
autonomy level. Keeping your details in one place (the profile, which feeds the
other two) means there's never two copies of a preference disagreeing.

Every file Graybeard creates is recorded in a **manifest** (a simple list of
everything added), which is what makes clean uninstall possible.

### 3. The loop ("learn from this session") — the heart of Graybeard

This is what makes Graybeard different from a static rulebook. When a session
goes badly:

1. **You hand it the pain** — a saved transcript, pasted text, or just a
   sentence describing what kept going wrong.
2. **It names the disease** — not the single incident, but the *class* of mistake
   behind it. ("It kept saying it fixed things" → *the real disease is claiming
   done without proof.*)
3. **It proposes one general rule** — and checks itself that the rule is general,
   not a patch for one specific case. A rule that says "if asked about X, do Y" is
   rejected; there are always a hundred thousand X's.
4. **It proves the rule works** — it tells you the small cost first (a couple of
   dollars of AI time, and you can say no), then runs the same task several times
   *without* the rule and several times *with* it, using separate helper AIs. If
   the rule helps, the "without" runs mostly fail and the "with" runs mostly pass.
5. **It shows you the evidence** — a visual page (open it in your browser) with
   the before/after results side by side and a plain verdict.
6. **On your OK, it installs the rule** — as a new law in your space, and records
   it in your **ledger** (`~/.claude/graybeard/ledger.md`), your growing history
   of every rule you've earned.

Next session, the AI already obeys it. Your assistant gets smarter from your
worst days — and you never had to know how engineers think.

## Why it's built this way (for the curious)

- **Almost all plain text.** The laws are Markdown files; there's nothing to
  compile or run. The only "program" is the AI following the instructions. This
  keeps it simple and easy to fork.
- **Your files, not ours.** The add-on itself is read-only; everything personal
  to you is written into *your* space, so updates to Graybeard never overwrite
  your rules.
- **One source of truth.** Your profile drives everything else, so there's never
  two copies of a setting disagreeing.
- **Safe to remove.** Because every change is backed up and listed in the
  manifest, uninstall puts your machine back exactly as it was.
- **Built-in honesty.** Nothing is called "done" without evidence; nothing is
  spent without telling you the cost; nothing you must approve is shown as a wall
  of text.

## The files at a glance

```
Graybeard (the add-on, read-only):
  skills/graybeard-worklaw/       the everyday habits
  skills/graybeard-unknowns/      clearing up fuzzy requests
  skills/graybeard-conductor/     the idea → product pipeline
  skills/onboard/                 the setup interview
  skills/learn-from-pain/         the loop
  skills/graybeard-uninstall/     clean removal
  templates/                      the fill-in-the-blank files /onboard and the loop use

Yours (created on your machine by /onboard and the loop):
  ~/.claude/graybeard/profile.md      your settings (source of truth)
  ~/.claude/graybeard/ledger.md       every rule you've earned
  ~/.claude/graybeard/manifest.txt    the exact list of what was added (for uninstall)
  ~/.claude/CLAUDE.md                  your standing orders (one marked block)
  ~/.claude/settings.json             the every-turn reminder (one merged entry)
  ~/.claude/skills/graybeard-law-*/    laws YOU earned via /learn-from-pain (one folder each)
```

---

## Install fallback — when `/plugin marketplace add` silently does nothing

On some machines (seen on Windows, especially with spaces in folder paths) the
`/plugin marketplace add` menu accepts your input and then… nothing appears in
`/plugin list`. It's a known Claude Code quirk, not something you did wrong.

**The easy fix — just ask Claude.** In Claude Code, say:

```
The /plugin marketplace add command silently failed. Please install the
graybeard plugin from github vikas53953/graybeard by editing the plugin
registry files directly (the same files the menu writes), then reload plugins
and show me /plugin list to prove it's there.
```

Claude Code can edit its own registry files (`~/.claude/plugins/`
`known_marketplaces.json` and `installed_plugins.json` — the files the menu
writes for working plugins) and mirror a working entry for Graybeard. Make it
show you the plugin listed and enabled before you continue — you confirm, you
never discover.
