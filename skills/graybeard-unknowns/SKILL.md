---
name: graybeard-unknowns
description: Use when starting a new project or feature, when a request is vague or one line ("build it"), when the domain is unfamiliar to the user or to Claude, when the user can't say what "good" looks like, before writing an implementation plan for non-trivial work, or when scope keeps shifting mid-build.
---

# The Unknowns Law — clear them while they're cheap

**The map is not the territory.** The request is a map; the codebase and real
world are the territory. The gap is the *unknowns*, and every unknown left
unfound gets filled by a silent assumption — which becomes the next bug or the
next wasted build. Run these proactively; don't wait to be asked.

| Quadrant | What it is | Main tools |
|---|---|---|
| Known knowns | What's in the request | (confirm it back) |
| Known unknowns | Gaps we can name | Interview, named assumptions |
| Unknown knowns | "I'll know it when I see it" | Mocks, design directions, references |
| Unknown unknowns | Nobody sees it yet | Blindspot pass, teach-me, quiz |

## The techniques (pick 1–3 by situation, never all ceremonially)

**Before building:**
1. **Blindspot pass** — unfamiliar area? Surface the landmines, historical
   context, missing concepts, and unwritten conventions — ordered by severity —
   and teach the user what they had no way of knowing.
2. **Teach the vocabulary** — when the user lacks the words (auth, color
   grading, whatever): teach the 3–5 terms they need so they can say what they
   actually want.
3. **Design directions** — visual taste is an unknown known: show 2–4 wildly
   different directions in one HTML page and let them react.
4. **Mock before you wire** — ANY output the user will look at (a summary, a
   screen, a report): fake it with sample data first. Reacting to a fake costs
   minutes; reacting to a built one costs a rebuild.
5. **Brainstorm the intervention** — vague problem, many possible solutions:
   ~10 candidates from cheapest to most ambitious; the user picks.
6. **The interview** — remaining ambiguity: ONE question per message, each with
   a recommended answer, highest blast-radius first. Stop when answers stop
   changing the design. Never a wall of questions.
7. **Point at a reference** — when words run out: get a reference (code, site,
   component) and read how it's built, not just how it looks.

**While building:**
8. **Implementation notes** — edge case forces a deviation? Conservative
   option, one line in `implementation-notes.md`, keep going, tell the user.

**After building:**
9. **Quiz before sign-off** — 3 short questions the user must pass. "Ok"
   without understanding is how code becomes a black box.

## Common mistakes

| Mistake | Instead |
|---|---|
| Firing 3–4 questions in one message | One at a time, blast-radius order, recommendation attached |
| Building the real thing to "see how it looks" | Mock with fake data first |
| Explaining a hard tradeoff in prose | Decision page: options side by side, downsides visible, user picks |
| Asking questions whose answer changes nothing | Only ask what would change the approach |
