# Startup Prompts — copy-paste opening messages

Pick the scenario that matches, then the platform you're on. See
`SHARED/SESSION_STARTUP.md` for why each of these is shaped the way it
is. Replace anything in `<angle brackets>`.

---

## Scenario 1 — Brand-new idea, no project repo yet

### Claude Code CLI (skill already installed globally)

```
I have a new idea I want to run through CodeFoundry: <describe the idea>.
There is no project repo yet. Start with Ideation.
```

### Claude Code CLI (skill not yet installed globally)

```
Read SKILL.md from https://github.com/govarthanan0507/CodeFoundry_Skill
and follow it as your process for this session.

I have a new idea: <describe the idea>. There is no project repo yet.
Start with Ideation, then Pre-Planning.
```

### Claude Code on the web

```
Read SKILL.md from https://github.com/govarthanan0507/CodeFoundry_Skill
and follow it as your process. Attach that repo read-only — do not
request or use push access to it.

I have a new idea: <describe the idea>. There is no project repo yet.
Start with Ideation, then Pre-Planning. Do not create a project repo
until Pre-Planning clears.
```

---

## Scenario 2 — An existing codebase already built

### Claude Code CLI (skill already installed globally)

```
This project (the repo I'm running you in) already has an existing
codebase. Per CodeFoundry's routing rule, use Ingestion instead of
Ideation — read the existing code/docs here and produce the same
idea.md output Ideation would. Continue into Pre-Planning from there.
```

### Claude Code CLI (skill not yet installed globally)

```
Read SKILL.md from https://github.com/govarthanan0507/CodeFoundry_Skill
and follow it as your process for this session.

This project (the repo I'm running you in) already has an existing
codebase. Use AGENTS/Ingestion/ instead of Ideation, per SKILL.md's
routing rule. Continue into Pre-Planning from there.
```

### Claude Code on the web

```
Read SKILL.md from https://github.com/govarthanan0507/CodeFoundry_Skill
and follow it as your process. Attach that repo read-only — do not
request or use push access to it.

This project already has an existing codebase (this repo). Use
AGENTS/Ingestion/ instead of Ideation, per SKILL.md's routing rule —
read what's here and produce the same idea.md output, without
re-asking me things the codebase already answers. Continue into
Pre-Planning from there. All real changes happen in this repo, never
in CodeFoundry_Skill.
```

---

## Scenario 3 — Resuming an in-progress CodeFoundry project

### Claude Code CLI (skill already installed globally)

```
Resume the CodeFoundry project <project-name>. Read its current state,
latest handoff, and latest signed-off documents before doing anything
else — don't re-ask me for context that's already captured there.
```

### Claude Code on the web

```
Read SKILL.md from https://github.com/govarthanan0507/CodeFoundry_Skill
and follow it as your process. Attach that repo read-only.

Resume the CodeFoundry project <project-name> (this repo /
<path/repo where its project folder lives>). Read its current state,
latest handoff, and latest signed-off documents before doing anything
else.
```

---

## A note on real-world validation runs (e.g. a QA fix-verification cycle)

If you're using CodeFoundry to actually fix something QA flagged (a
`V{n}-FIX-{m}` cycle per `DEPARTMENTS/QA_Organization/LIFECYCLE.md`),
say so explicitly and name the exact findings — this routes the agent
into `DEPARTMENTS/Developer_Organization`'s fix workflow rather than a
fresh Ideation/Ingestion pass:

```
Act as a CodeFoundry Developer. Here is the QA handoff to fix: <paste
or link the handoff>. This is a fix-verification cycle
(V<n>-FIX-<m>), re-entering at the Developer/QA stages only — not a
full re-plan.
```
