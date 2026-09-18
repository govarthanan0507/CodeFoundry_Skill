# Session Startup — how to point a fresh agent at CodeFoundry

## The one rule everything else follows

CodeFoundry (this repo) is a **skill — reference material an agent
reads**, never a place work happens. The project being built or fixed
is a *separate* repo/folder, attached with real write access. An agent
that mixes the two — writing project output into this repo, or
treating this repo as something it may edit — is set up wrong,
regardless of which platform it's running on.

See `SHARED/STARTUP_PROMPTS.md` for the exact text to paste; this file
explains the mechanics behind each platform and scenario.

## Two platforms, two different mechanics for staying read-only

### Claude Code CLI (your own machine)

Once installed at `~/.claude/skills/CodeFoundry/` (see this repo's
root `README.md` Quickstart), every session picks it up automatically
— no per-session instruction needed, and there's no local checkout of
this repo for the agent to accidentally write to.

Before that global install (e.g. while still testing), reference it
explicitly instead: point the agent at this repo's raw GitHub URL and
tell it to read `SKILL.md` from there. There's still no local clone in
that case, so nothing to write to.

### Claude Code on the web

This repo gets attached to the session as an additional repository,
separate from the project repo. The two are given different access
levels:

- `CodeFoundry_Skill` → **read-only** (`access:"read"`) — fetch/clone
  only.
- The actual project repo → **push** (`access:"push"`) — real
  write/commit access, after a genuine GitHub permission check.

This isn't just an instruction the agent is trusted to follow — a
write to a repo only attached read-only is refused unless it's
separately re-attached with `access:"push"`, which itself requires the
repo owner to have authorized the Claude GitHub App for that specific
repo. So as long as the opening instruction never asks the agent to
modify `CodeFoundry_Skill`, there's a real permission gate behind the
read-only boundary, not just politeness.

## The three starting scenarios

### 1. Brand-new idea — no project repo exists yet

CodeFoundry's own `AGENTS/Ideation/` stage exists specifically because
a project repo isn't created until *after* Pre-Planning clears
(`SHARED/PROJECT_FOLDER_STRUCTURE.md`). Don't create or attach a
project repo up front — start the session against a scratch/placeholder
workspace (or `CodeFoundry_Skill` itself, read-only, since nothing gets
written during Ideation/Pre-Planning), and let the idea/build decision
happen first. A real repo only gets created once there's something
worth building.

### 2. An existing codebase already built

Use `AGENTS/Ingestion/` instead of Ideation — same `idea.md` output,
without re-asking questions the existing code/docs already answer.
Here the project repo *is* attached from the start (with push access),
since the codebase itself is the input CodeFoundry reads.

### 3. Resuming an in-progress CodeFoundry project

Per `SKILL.md`'s own resume rule: if `projects/<name>/` already exists
for the project, the agent should read its current state, latest
handoff, and latest signed-off documents — not re-ask for context
that's already captured there. State which project you're resuming in
the opening message so it doesn't default to treating it as new.

## Why this is documented separately from the README

The root `README.md` covers what CodeFoundry is and how to install it
once. This file is the thing to re-read every time you're about to
*start* a session against it — the part that's easy to get wrong by
skipping the read-only setup, not the part you read once at install
time.
