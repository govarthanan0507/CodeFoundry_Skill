# User Ideation Preferences — Cross-Project

## Why this is a separate file, not part of the three-layer model

`INTENT_CONTEXT_ENGINE.md`'s three layers are all scoped **per project** — working memory and durable project memory both live under `projects/<name>/state/`. This file is different on purpose: it's scoped **per user, across every project**, because how you like to be interviewed doesn't reset just because you started a new idea. Putting it inside a per-project file would mean CodeFoundry relearns your interview style from zero on every new project, which defeats the point.

Location: `state/user-ideation-preferences.md` (project root level, not under `projects/<name>/`).

## What this file tracks

- Whether this user tends to give detailed technical context upfront (skip basic clarifying questions) or a rough sketch (ask more).
- Whether they respond better to open-ended questions or being shown concrete options to react to.
- Recurring shorthand or terminology they use that shouldn't need re-explaining each time.
- Question types that have historically produced a fast, useful answer vs. ones that stalled the conversation or got an annoyed response.
- How many clarifying questions they tolerate before wanting to just proceed with a stated assumption instead.

## How it's updated

After each Ideation pass, append what was actually observed — not a personality profile, just interview-tactics that worked or didn't. This is deliberately narrow: it's about *how to ask*, not *who the user is* or *what they've decided* — that second kind of information belongs in the project's own durable state or the human's own memory files, not here.

## How it's used

Product reads this file at the start of a new Ideation pass, before asking the first clarifying question — not mid-conversation. It adjusts question style and density, not content; it never lets a preference like "tolerates few questions" cause Ideation to skip the completion contract from `INTENT_CONTEXT_ENGINE.md` — a user who prefers fewer questions still needs the structured idea to actually converge, they just get there with fewer round-trips, more assumptions stated upfront for them to confirm or correct in one pass.

## Template

```markdown
# User Ideation Preferences

## Observed interview style
- 

## Question types that worked
- 

## Question types that stalled or annoyed
- 

## Tolerance for clarifying questions before wanting to proceed on assumptions
- 

## Recurring shorthand/terminology
- 
```
