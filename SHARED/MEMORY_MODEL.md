# Memory Model — Generalized (V1, Completed)

## What changed from the Ideation-scoped version

`AGENTS/Ideation/AGENT.md`'s three layers were explicitly scoped to one stage. This generalizes the same three layers to every stage and every project — the mechanism doesn't change, only its reach.

## Layer A — Conversation Memory (CodeFoundry's own copy, not borrowed from any one tool)

**Correction from the first version of this file:** pointing to Claude Code's own transcript log was wrong — that log lives inside Claude Code's own storage, which means the record disappears the moment a different tool is used instead. That breaks the core principle already established elsewhere in this system: CodeFoundry owns the memory, the underlying model/tool is an implementation detail, not the other way around.

The full raw record is instead CodeFoundry's own file, independent of whatever tool produced it:

```text
sessions/<date>-full-record.md
```

Written by whichever tool is actually running the session (Claude Code today, potentially something else later) — the format is CodeFoundry's own, not a vendor-specific export. This sits alongside, not instead of, the compressed `sessions/<date>-session.md` from `SESSION_CONTINUITY.md`: one file is the full record, the other is the compressed checkpoint derived from it. Portability was the actual point of building this system-wide in the first place — a memory model that only works inside one tool isn't really CodeFoundry's memory, it's that tool's.

## Layer B — Working Memory (per active stage/project, not just Ideation)

Generalized: any active stage (Ideation, Pre-Planning, Design Council, Development) maintains its own working understanding while active — intent, current decisions, open questions — exactly the Ideation pattern, just no longer exclusive to that one stage. Lives in each project's `state/` folder alongside `project-state.md`.

## Layer C — Durable memory, now two kinds

1. **Project-level durable memory** — `project-state.md`, unchanged.
2. **Cross-project user-pattern memory (new)** — `state/user-profile.md` at the CodeFoundry root, generalizing what `state/user-ideation-preferences.md` already started (interview style) into the broader pattern-recognition you're asking for: recurring preferences, working style, how much detail you give upfront, terminology you use — built from patterns observed across sessions, not a raw copy of them.

## What this enables later, honestly scoped

Preference analysis, semantic analysis, and understanding you better over time all become possible *because* Layer A is preserved and Layer C's pattern file exists to hold what's actually derived from it. Nothing here claims those analyses run automatically yet — this is the foundation they'd need, not the analysis itself.

## The privacy discipline — deliberate, not an afterthought

Full-record retention makes this worth being careful about, the same way it would be careful in any real system:

- `state/user-profile.md` holds **patterns**, not a raw transcript dump — derived observations ("tends to give detailed technical context upfront"), not verbatim quotes lifted wholesale.
- **Other people who appear in conversations** (family, friends, colleagues mentioned in passing) are not profiled — this system's pattern memory is about you, the person using CodeFoundry, not everyone you've ever mentioned to it.
- Sensitive categories (health, financial specifics, anything that wouldn't belong in a settings page you'd be comfortable with anyone seeing) don't get promoted into the durable pattern file even if they appear in the raw conversation log — Layer A can hold what was actually said (it's a record), but Layer C's pattern file is deliberately narrower than what it's drawn from.
- This mirrors, in spirit, the same discipline any well-built memory system should apply — not because a rule requires it, but because a full-record system without any filter on what gets promoted to a standing profile is a real risk, not just a nice-to-have.

## Where this lives going forward

`AGENTS/Orchestrator/AGENT.md` — Layer B/C maintenance joins its existing state-management responsibilities. `AGENTS/Product-Manager/AGENT.md` remains the primary consumer of `state/user-profile.md` at the start of any Ideation pass, same relationship as before, just fed by a richer, more general source than interview-style alone.
