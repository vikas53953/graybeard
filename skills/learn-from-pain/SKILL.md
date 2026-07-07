---
name: learn-from-pain
description: Use when the user runs /learn-from-pain, or says "that session was painful", "the AI kept doing X", "turn this into a rule", "learn from this", or points at a transcript of a frustrating Claude session. Mines the pain into ONE general, tested, machine-enforced law and installs it. This is Graybeard's core loop.
---

# /learn-from-pain — turn a bad session into a tested law

This is the loop that makes Graybeard get smarter from the user's own failures.
A painful session goes in; a **general** law (never a case-specific patch),
**proven** to help (baseline fails, with-law passes), comes out and installs
itself into the user's laws and ledger. The user never has to know how engineers
think — the loop encodes it for them.

Iron rules, non-negotiable: (1) the law is a **class fix, never a case fix**;
(2) **no cost is spent without saying the price first**; (3) the user sees the
test **evidence on a visual page** before anything installs; (4) the user
**confirms, never discovers** — you verify the install yourself.

## Step 1 — get the pain

Accept any of four inputs, in this priority:
- **The current conversation** — when the pain just happened in THIS session
  (e.g. the worklaw's two-strikes moment fired), the visible session IS the
  transcript. Don't ask the user to point at anything.
- **A transcript path** the user points at (a `.txt`/`.md`/`.jsonl` export, or a
  Claude Code session file). Read it locally. It never leaves the machine —
  say that out loud once.
- **Pasted text** of the session.
- **A plain description** ("it kept saying it fixed things that were still
  broken"). If this is all you have, that's fine — you'll reconstruct the disease
  from their words.

If you have nothing concrete, ask ONE question: "Point me at the transcript, or
just tell me in a sentence what it kept doing wrong."

## Step 2 — diagnose the disease (the class, not the case)

Read the pain and name the **underlying class of failure**, not the surface
incident. Ask yourself: "What is the ONE principle whose absence caused this, and
100 other bugs like it?" Examples of good class-level diseases:
- claimed "done/fixed" without ever running it → *no evidence before completion*
- fixed one thing and broke a neighbor → *changes made without re-testing
  neighbors*
- added a rule for each specific case → *case-patching instead of class fixes*
- guessed at causes without reading logs → *diagnosis without evidence*

Write the disease as a sentence that names the class. If you can only describe
the single incident, you haven't found the disease yet — keep going.

If the pain contains **more than one distinct disease**, don't silently pick:
ask ONE question ("I found two separate diseases here: X and Y — which hurt
more?"), run the loop for that one, and note the other in the law ledger as a
candidate for next time. One law per run.

## Step 3 — propose ONE general law + prove it's general

Draft one law that makes the whole class impossible. Then run the **generality
check on yourself** before showing the user:
- Does the law contain the words "if asked about X" or any single-case trigger?
  → REJECT it, generalize.
- Would this law have also prevented three *different* bugs in the same class?
  → if not, it's still a patch.
- Could a reviewer point at one specific scenario the law is clearly tailored to?
  → if yes, lift it up a level.

State, in one line, WHY the law is general (this becomes `GENERALITY_CHECK` on
the evidence page). A law that fails this check must not proceed to testing.
If your draft fails the generality check **twice**, stop — tell the user this
pain may not be a law-shaped problem (some pains are one hard bug, not a
behavior pattern) and end the run cleanly with nothing written.

While the disease is fresh, also draft two small pieces the law file needs:
`LAW_CHECK` — one observable signal that tells you the law is working (e.g. "every
completion claim cites a result that was actually run"), and one red-flag row
(`RED_FLAG_THOUGHT` = the rationalizing thought that leads back into this disease,
`RED_FLAG_REALITY` = the one-line correction). Derive both from the disease, not
from the single incident.

## Step 4 — say the cost, then offer the two paths (iron rule 2 above)

Testing runs real subagents and costs the user tokens. NEVER run them silently.
Say, in one line: roughly how many runs and the rough cost, e.g. *"Proving this
takes 6 helper runs (3 without the law, 3 with) — about $1–2 and ~2 minutes.
Want me to prove it, or install it untested and flagged for free?"* Then offer:

- **Path A — prove it (recommended).** Run the test recipe in Step 5.
- **Path B — install untested (free).** Skip testing; install the law but mark it
  `UNTESTED` in the law ledger and in the law file's header, so it's honest. Good
  when the user is sure or low on budget. Then jump to Step 7 — on Path B there
  is NO evidence page; the ledger entry says `UNTESTED` and the manifest gets a
  CREATED line for the law skill only.

Wait for their pick. Never assume Path A. If they decline **both** paths, end
the run cleanly: nothing written anywhere, and say so in one line ("Nothing was
installed or changed.").

## Step 5 — the test recipe (baseline vs with-law)

Pick a **task that would trigger the disease** — ideally the same kind of task
from their painful session (sanitized: strip any private specifics). The user's
current laws live at `~/.claude/skills/graybeard-law-*/SKILL.md` (plus their
standing-orders block in `~/.claude/CLAUDE.md`); subagents do NOT inherit them
automatically, so paste the relevant text into the subagent prompt. Then:

1. **Baseline runs — {{BASELINE_N}} (default 3):** spawn subagents (sonnet-tier)
   whose prompt contains the task + the user's current laws pasted in, WITHOUT
   the new law. Record whether each falls into the disease (fail) or not (pass).
   Expect mostly fails — that's what proves the pain is real.
2. **With-law runs — {{GREEN_N}} (default 3):** spawn subagents with the same
   prompt PLUS the new law's text pasted in. Record pass/fail against the same
   disease.
3. Each run is independent and blind to the others. Use a clear, identical
   pass/fail criterion tied to the disease ("did it run the thing before saying
   done? yes=pass").

The law is proven when baseline mostly fails and with-law mostly passes. If the
with-law runs still fail, the LAW is wrong, not the test — go back to Step 3 and
sharpen it. Two failed sharpen attempts = stop and tell the user this pain needs
a different kind of fix (worklaw two-strikes rule); don't install a law that
didn't work.

## Step 6 — the evidence page (visual, never a text wall) — Path A only

Fill `templates/evidence-page.html` and write it to the project (or a scratch
path) as `graybeard-evidence-<slug>.html`. Substitute every `{{…}}`:
`LAW_TITLE, LAW_SLUG, USER_NAME, LEARNED_DATE, DISEASE, LAW_BODY, GENERALITY_CHECK,
BASELINE_N, BASELINE_FAIL, GREEN_N, GREEN_PASS, COST_ACTUAL, COMPLETENESS, VERDICT`.
`COST_ACTUAL` = the estimate you quoted in Step 4, written AS an estimate
("≈ $1–2, quoted before running") — never invent a precise number you didn't
measure. `VERDICT` = `PROVEN` (baseline mostly failed AND with-law mostly
passed), `WEAK` (margin under 2 runs — say so), or `NOT PROVEN`.
`BASELINE_ROWS` / `GREEN_ROWS` = one `<div class="run pass|fail"><span class="tag">
PASS|FAIL</span>…one-line what happened…</div>` per run — set each row's
pass/fail class from that run's ACTUAL result, never decoratively. `COMPLETENESS` = /10 (10 =
tested both ways with a clear criterion; lower if you cut runs to save cost — say
so). Open it / hand the user the path. Then ask the one-line question: **install
or skip?** Grep the file for `{{` first — any leftover token is a bug.

## Step 7 — install (only on "install") + verify (they confirm, never discover)

On approval:
1. **The law skill:** fill `templates/law.md` → write
   `~/.claude/skills/graybeard-law-<slug>/SKILL.md`. Fill `LAW_SLUG, LAW_TRIGGER,
   LAW_TITLE, USER_NAME, LEARNED_DATE, BASELINE_FAIL, BASELINE_N, GREEN_PASS,
   GREEN_N, EVIDENCE_PATH, DISEASE, LAW_BODY, LAW_CHECK, RED_FLAG_THOUGHT,
   RED_FLAG_REALITY`. `LAW_TRIGGER` is the skill `description` — make it fire on
   exactly the situations in this disease's class. For Path B, replace the whole
   italic block (the lines from `*A personal law` through `{{EVIDENCE_PATH}}.*`)
   with: `*A personal law {{USER_NAME}} chose to install on {{LEARNED_DATE}}.
   UNTESTED — installed without proof, at the user's request.*` — still filling
   USER_NAME and LEARNED_DATE (both come from the profile at
   `~/.claude/graybeard/profile.md`; if no profile exists, ask the user their
   name once and use today's date).
2. **The law ledger:** append to `~/.claude/graybeard/ledger.md` (create with a
   header if missing) one entry: date, disease, law title, result
   (`baseline X/N fail → with-law Y/N pass`, or `UNTESTED` on Path B), and the
   evidence-page path (Path A only — Path B entries have no evidence page).
   This is the user's growing record of every law they earned. (Not to be
   confused with the project feedback tracker — PIPELINE.md /
   implementation-notes.md — which lives per-project.)
3. **The manifest — the record uninstall trusts.** If
   `~/.claude/graybeard/` or `manifest.txt` doesn't exist yet (the user ran
   `/learn-from-pain` before ever running `/onboard` — a valid entry point),
   CREATE the directory and manifest first. Then append a `CREATED<TAB><path>`
   line (fields separated by ONE TAB) for EACH thing this run wrote that isn't
   already listed: `~/.claude/skills/graybeard-law-<slug>/SKILL.md`, the evidence
   page `graybeard-evidence-<slug>.html` (Path A only), and the ledger if you
   just created it. Every
   file this loop writes must be in the manifest, or `/graybeard-uninstall` can't
   remove it (breaks the leave-no-trace promise). If the evidence page is written
   to a throwaway scratch path outside `~/.claude`, say so to the user instead of
   recording it — never leave an unrecorded file inside their config.
4. **Verify before claiming done:** confirm the law file exists with no `{{`
   tokens, the ledger entry is present, and a manifest `CREATED` line exists for
   the law skill — and, on Path A only, for the evidence page too. Only then
   report.

## Step 8 — report (plain, in their review style)

One short message: the law's name, one line on what it now prevents, that it's in
their ledger, and the restart note (**new skills load at Claude Code startup —
restart once for the law to take effect**). Offer: "Want to feel it work? I can
show a before/after on a fresh task." Never claim the law is active in this
session without the restart.

## Red flags — STOP if you catch yourself thinking:

| Thought | Reality |
|---|---|
| "I'll write 'when asked about X, do Y'" | That's a case patch. 100,000 cases exist. Find the class. |
| "I'll just run the tests, they're cheap" | Say the cost first. Always. Their money, their call (iron rule 2). |
| "The law's obviously right, skip the test" | Offer Path B honestly, but don't skip proof by yourself. Evidence, not opinion. |
| "With-law runs failed but close enough — install it" | A law that didn't pass isn't a law. Sharpen it or stop. Don't ship a dud. |
| "A summary of the test is fine" | The evidence is a visual page. That's the product. |
| "It's installed, tell them it's working" | Skills load at startup. Verify the file, then say 'restart to activate'. |
