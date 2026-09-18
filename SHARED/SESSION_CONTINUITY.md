# Session Continuity — V1 (Completed)

## What this is, and how it's different from what already exists

Two other mechanisms already cover related ground — this fills the actual gap between them:

- `AGENTS/Ideation/AGENT.md`'s three-layer memory — scoped to one stage (Ideation), not the whole session.
- `projects/<name>/handoffs/` — scoped to one project's stage transitions (per `HANDOFF_CONTRACT.md`), not the whole session, and a session can touch multiple projects (this actual chat worked on both `baseflix` and `repo-analyzer`).

**This file defines the missing layer: one compressed record per session, spanning everything discussed, regardless of stage or project.**

## Where it lives

```text
<CodeFoundry root>/sessions/<date>-session.md
```

A sibling to `projects/`, not inside any single project — because a session isn't owned by one project.

## Append vs. new file — the actual rule

```text
Session begins
        ↓
Does a session file for TODAY already exist and is it still
the same continuous working session (not a genuinely new,
separate sitting)?
        ↓
YES → APPEND to the existing file — add what's new since the
       last write, don't regenerate the whole thing
        ↓
NO  → CREATE a new file for this session
```

In practice: within one continuous Claude Code session (however long it runs, however many separate exchanges), everything appends to the same file. Closing Claude Code and starting a genuinely new session later — even on the same day — starts a new file, unless the person explicitly says they're continuing the same thread.

## What triggers a write

- At the natural end of a session (Claude Code closing, or the person indicating they're done for now).
- Whenever the file would otherwise grow unboundedly — for a very long single session, write a compressed update periodically rather than waiting until the very end and trying to compress everything at once.

## Content — compressed, not a transcript

Reuses `HANDOFF_CONTRACT.md`'s fields, but session-scoped and deliberately compressed:

```text
SESSION: <date>
PROJECTS TOUCHED: <list>

WHAT HAPPENED (compressed, chronological)
  - key decisions made, in order, one line each

DECISIONS
  - durable decisions, with brief reasoning — not full debate transcripts

OPEN QUESTIONS CARRIED FORWARD
  - anything still unresolved when the session ended

FILES CREATED OR CHANGED
  - path list, not full diffs

NEXT SESSION SHOULD
  - the single most useful pointer for picking this back up cold
```

This is deliberately NOT a full transcript and NOT the three-layer Working Memory from Ideation — it's a compressed session-level checkpoint, closer in spirit to `SESSION_HANDOVER.md` from this actual chat than to any per-stage artifact.

## Who's responsible for it

`AGENTS/Orchestrator/AGENT.md` — this is a state/continuity responsibility, not a specialist reasoning task, which is exactly the Orchestrator's lane.
