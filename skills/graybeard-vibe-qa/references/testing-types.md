# Testing Types Catalog (Classic + AI-Specific)

Use for planning coverage and answering "what testing exists / what applies here."

## Core (every app, every time)

| Type | Question | Best tool |
|---|---|---|
| Smoke | Does it even load? | Browser, 5 min |
| Sanity | After a fix, does that area still work? | Browser |
| Functional | Does each feature match the spec? | Playwright |
| E2E / journey | Do complete flows work start-to-finish? | Playwright + browser agent |
| Wire-up / integration | Is frontend really connected to backend? | Code audit + behavioral tests |
| Regression | Did the new fix break something old? | Re-run Playwright suite |
| Negative | What happens with wrong/garbage input? | Forms + edge phase |
| UAT | Would a real user accept this? | The human, manually |
| Usability / UX | Pleasant and obvious to use? | Browser review + human eyes |
| UI / visual | Looks right, consistent, aligned? | Screenshot review |
| Responsive | Works at mobile/tablet widths? | DevTools device mode |
| Persistence | Data survives reload/re-login? | Reload trick |

## Situational (at scale / on launch)

| Type | Question | When it matters |
|---|---|---|
| Cross-browser | Chrome vs Firefox vs Safari? | Public launch (Playwright runs all three) |
| Load / stress | Survives 100 / 10,000 users? | Public launch |
| Soak | Degrades after hours of running (memory leaks)? | Long-session apps (music players!) |
| API / contract | Endpoints honor agreed request/response shapes? | Frontend & backend evolving separately |
| Performance | Fast? Lags with lots of data? | Lighthouse in DevTools |
| Accessibility | Keyboard, screen reader, contrast? | Lighthouse + Tab-walk |
| Security | Injection, exposed data, auth bypass? | Before public, always |
| Compatibility / install | Different OS/devices/versions? | Mobile apps |
| Recovery | Crash, lost network, killed session? | Worth 10 min always (offline mid-action) |
| Localization | Other languages, RTL, date formats? | Multi-language only |
| Exploratory | Unscripted human "try to break it" | Always |

## AI/Vibe-Coded Extras (mandatory for AI-built apps)

| Type | Failure mode it catches |
|---|---|
| Phantom feature audit | UI built for features never implemented (settings toggles wired to nothing) |
| Dependency verification | Hallucinated/unused packages; stale vulnerable versions (`npm audit`) |
| Secrets & security defaults scan | Hardcoded API keys, open CORS, no rate limiting, secrets in git |
| Consistency / drift review | Duplicated logic + inconsistent patterns across sessions → whack-a-mole |
| Silent-failure sweep | `catch (e) { console.log(e) }` — errors the user never sees |
| Persistence reality check | localStorage/in-memory posing as a real database |
| Regression-as-habit | AI's per-fix blast radius is larger; suite re-run after EVERY fix |

## Fastest bug-catching order

Smoke → Link/Button sweep → Wire-up → Journeys → Negative → UI/UX → Hygiene → Regression (after every fix).
