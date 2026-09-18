# CodeFoundry

CodeFoundry is a **file-based multi-agent SDLC framework**. It is not a
program you run — it is a structured set of instruction files
(`SKILL.md`, `AGENT.md`, `CAPABILITY.md`, `workflow.md`, and shared
protocol documents) that any sufficiently capable LLM-driven coding
agent can read and act on, taking on the roles those files define
(Ideation interviewer, Pre-Planning debater, Design Council member,
Frontend/Backend/Mobile developer, QA verifier, and so on).

Nothing in this repo requires Claude specifically. If your agent can
read files in this repo and write files/commits to a project
repository, it can run CodeFoundry.

## Quickstart — using this as a skill, with any agent

1. Point your agent at this repository (clone it, or attach/mount it
   read-only alongside the project it will work on).
2. Tell your agent, in plain language: *"Read `SKILL.md` in this repo
   and follow it as your process for the following idea/project."*
   That file is the canonical entrypoint — it explains the project-name
   rule, how to tell a genuinely new idea from an already-started
   project, and the full pipeline below.
3. Everything CodeFoundry produces (idea docs, debate transcripts,
   design docs, code, handoffs, QA verdicts) is written to the actual
   project's own repository/folder — never into this repo. This repo
   is reference material only; it does not accumulate project output.

This works identically whether your agent is Claude Code, a different
vendor's coding agent, or a manually-driven chat session where you
paste in the relevant `.md` files yourself — the instructions are
plain text, not a proprietary format.

**Starting a real session?** See `SHARED/SESSION_STARTUP.md` for the
platform-specific mechanics (Claude Code CLI vs. Claude Code on the
web) and `SHARED/STARTUP_PROMPTS.md` for ready-to-paste opening
messages, covering a brand-new idea, an existing codebase, and
resuming an in-progress project.

## Pipeline

```text
Idea (or a structured explanation, or existing code)
  → AGENTS/Ideation/   or   AGENTS/Ingestion/   (same idea.md output)
  → COUNCILS/Pre-Planning/        (4-role debate: build it or not)
  → Epic Selection
  → COUNCILS/Design-Council/      (7-role debate + independent critic)
  → DEPARTMENTS/Developer_Organization/   (implementation — Frontend/
                                    Backend/Mobile developer workers)
  → DEPARTMENTS/QA_Organization/   (independent verification)
  → Verify
  → AGENTS/Git-Maintainer/
  → Release
```

Each arrow is a **frozen, written handoff** (`SHARED/HANDOFF_CONTRACT.md`),
not a live negotiation between agents — this is what makes the pipeline
usable by a single agent working stage-by-stage, or by several
different agents/sessions picking up successive stages.

## Task tracking

CodeFoundry does not build its own Kanban/Gantt UI — it uses
**GitHub Projects** (free, native, board/roadmap/table views included)
attached to each project's own repo, fed from the ticket/log state
CodeFoundry already maintains. See `SHARED/PROJECT_TRACKING.md`.

## Folder map

| Folder | What it is |
|---|---|
| `SKILL.md` | The entrypoint. Read this first, always. |
| `AGENTS/<Agent>/AGENT.md` | One single-agent stage (Ideation, Ingestion, Orchestrator, Git-Maintainer, Deployment-Engineer, Product-Manager, Product-Owner, and the Frontend/Backend/Mobile developer agents). |
| `COUNCILS/<Council>/` | A multi-role debate stage (Pre-Planning: 4 roles; Design-Council: 7 roles), each role in its own file under `roles/`. |
| `DEPARTMENTS/Developer_Organization/` | The implementation department — `CAPABILITIES/<Worker>/` holds the growable skill pool each developer worker draws on (see Capability Evolution, below). Independently shippable as its own repo later. |
| `DEPARTMENTS/QA_Organization/` | Independent verification department, run separately from Development by design (never the same agent/session verifying its own work). Independently shippable as its own repo later. |
| `SHARED/` | Cross-cutting protocol documents every stage depends on — handoff schema, document governance/versioning, process-scaling tiers, hard constraints, reuse/license rules, session continuity, sprint ceremonies, task tracking (`PROJECT_TRACKING.md`), and how to start a session against this skill (`SESSION_STARTUP.md`, `STARTUP_PROMPTS.md`). |
| `TESTING/` | The structural/evaluation contract used to test one unit (an agent, a council, a department) in isolation. |
| `MANIFEST.json` | Machine-readable index of every testable unit and department root — read this before writing tooling that walks the package. |

## Fixing or improving CodeFoundry itself

CodeFoundry is meant to keep getting better at the work it hands out,
not stay a static, one-time-built set of files. There are two
distinct, deliberately separate change loops — read
`SHARED/CAPABILITY_EVOLUTION.md` in full before changing anything here,
but in short:

- **Capability Evolution** — improving *what a worker knows how to do*
  (a better Frontend pattern, a Backend approach, a Mobile technique).
  Scoped to `DEPARTMENTS/Developer_Organization/CAPABILITIES/<Worker>/`
  files. Lower stakes. Follows a DISCOVER → ANALYZE → BENCHMARK →
  PROPOSE → HUMAN APPROVAL → ADOPT loop — a candidate that overlaps an
  existing capability must be benchmarked head-to-head against it
  (real output, real token cost, neutrally reported), never swapped in
  on a vibe.
- **Organization Evolution** — improving *how CodeFoundry itself runs*
  (the stage sequence, a council's debate protocol, a constitution-
  level rule, `AGENTS/Orchestrator/`, `COUNCILS/*/`). High stakes —
  changes what every future project depends on. Always requires
  explicit human approval; never bundled into a Capability Evolution
  change, even when the finding that prompted it came from the same
  source.

Both loops are reactive today (triggered by an actual finding, not a
standing background scan) and both preserve the previous version of
whatever file they update rather than overwriting it
(`SHARED/DOCUMENT_GOVERNANCE.md`). A change to this repo that skips
human approval, or that mixes a capability-level fix with an
organization-level one in the same change, is out of process — flag it
instead of pushing it through.

## Testability-first structure

CodeFoundry is organized into atomic test units plus shared
infrastructure, so any single stage can be evaluated on its own:

- `AGENTS/<Agent>/` = one agent test target.
- `COUNCILS/<Council>/` = one complete council test target, including
  its member roles.
- `DEPARTMENTS/<Department>/` = one independently packaged department
  test target (with `CAPABILITIES/<Worker>/` inside
  `Developer_Organization` as a finer-grained target), each shippable
  as its own repository afterward.
- `SHARED/` = dependencies, not normally a test target by itself.
- `TESTING/` = the common evaluation contract.

Examples: supply `AGENTS/Ideation/` alone to test Ideation; supply both
`COUNCILS/Pre-Planning/` and `COUNCILS/Design-Council/` to the same
evaluator to compare them. This preserves clean separation without
destroying the runtime/test boundary.

## What CodeFoundry is not (yet)

Every rule in this package is currently enforced by an agent choosing
to follow written instructions — `SHARED/SCRIPTS/*.py` and
`TESTING/resolve_targets.py` check structure (does a unit have the
files it's supposed to), not behavior (did an agent actually freeze a
contract before parallelizing, actually run a debate instead of
asserting a conclusion). Treat any status claim a CodeFoundry stage
makes ("tests pass," "council reached consensus," "verified") as
unverified until independently re-checked — this is the same
evidence-over-assertion discipline `DEPARTMENTS/QA_Organization`'s own
Constitution states explicitly, and it applies to CodeFoundry's own
claims about itself just as much as to any project it produces.
