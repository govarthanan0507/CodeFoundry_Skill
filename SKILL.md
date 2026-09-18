---
name: codefoundry
description: Turns an idea into a built product through structured stages - Ideation, a 4-agent Pre-Planning debate on whether to build it, a 7-role Design Council with tested debate outcomes, Development (Frontend/Backend/Mobile/Git Maintainer workers), and Release - with real gates, versioned documents, and a permanent handoff record. Use this skill whenever the person wants to build a product or feature from an idea, run it through structured planning and design review, or pick up an in-progress CodeFoundry project.
---

# CodeFoundry

Read this file first when this skill is invoked. Before anything else
— before Ideation, before any question about the idea itself — this
skill requires a project name. This is a hard rule, not a formality:

```text
Does `projects/<name>/` already exist for a name the person gave or
that's obvious from context (resuming work)?
    ├── YES → resume: read the project's current state, latest
    │         handoff, and latest signed-off documents. Do not ask the
    │         person to re-explain context already captured there.
    └── NO  → ask for the project name before proceeding to Ideation
              or anything else. `projects/<name>/` is created fresh
              per `SHARED/PROJECT_FOLDER_STRUCTURE.md` — this skill
              does not begin working inside an unnamed or shared
              space, and does not infer a name on its own when the
              person hasn't given one.
```

Once the project folder exists, check what's actually been handed
over before defaulting to Ideation's conversation:

```text
Genuinely open-ended, unformed idea → AGENTS/Ideation/ (as below)
A structured explanation, or an existing codebase already handed over
  → AGENTS/Ingestion/ instead — same idea.md output, fewer redundant
    questions on thinking (or code) that already exists
```

See `SHARED/PROJECT_FOLDER_STRUCTURE.md` for the full folder shape
this creates — the shared documents folder, and, once work reaches
that stage, the separate `dev_<name>/` and `test_<name>/` workspaces
that Developer_Organization and QA_Organization each own and never
cross into.

## Lifecycle

```text
Idea (or a structured explanation, or existing code)
  → AGENTS/Ideation/  or  AGENTS/Ingestion/  (same idea.md output)
  → COUNCILS/Pre-Planning/        (4-role debate + decision)
  → [IF Ingestion produced CODE_DIGEST.md: SHARED/EXISTING_CODE_AUDIT_GATE.md
     — mandatory, blocks the next step until signed off]
  → Epic Selection (AGENTS/Product-Manager/ decomposes into epics,
     scored per SHARED/EPIC_SELECTION_CRITERIA.md)
  → COUNCILS/Design-Council/      (7-role debate + independent critic)
  → AGENTS/Product-Owner/         (writes user stories into
                                    requirements.md, one ticket each,
                                    per SHARED/AGILE_WORKFLOW.md)
  → DEPARTMENTS/Developer_Organization/  (implementation — the major
                                    Frontend/Backend/Mobile block)
  → DEPARTMENTS/QA_Organization/   (independent verification —
                                    pulled in as a block for testing;
                                    see MANIFEST.json)
  → Verify
  → AGENTS/Git-Maintainer/
  → Release
```

## Testable-unit architecture

CodeFoundry separates **organization** from the **test boundary**.

- `AGENTS/<name>/` is one independently testable agent.
- `COUNCILS/<name>/` is one independently testable council **as a complete bundle**. Its member roles live inside it and are implementation members, not separate council targets by default.
- `DEPARTMENTS/<name>/` is one independently testable, independently packaged department — currently `Developer_Organization` (Frontend/Backend/Mobile capabilities, Kanban workflow) and `QA_Organization` (independent verification, its own constitution/engine). Each is self-contained on purpose: it should not require the rest of this skill to be read or run on its own, since the eventual plan is to ship each as its own separate repository — they are co-located here only for integrated testing during this phase.
- `SHARED/` contains common contracts, governance, state, memory, process rules, and scripts.
- `TESTING/` defines the generic evaluation contract and machine-readable target format.

This means an evaluator can receive: one agent folder, one council folder, one department folder, or multiple folders for a matched comparison. In particular, Pre-Planning and Design Council remain separate atomic council targets and can be tested side-by-side.

## Core rules

- `COUNCILS/Design-Council/HARD_CONSTRAINTS.md` routes hard-constraint decisions to the human.
- `SHARED/PROCESS_SCALING.md` determines how much process a task warrants.
- `SHARED/PARALLELIZATION_GUARDRAIL.md` governs safe concurrency.
- `SHARED/HANDOFF_CONTRACT.md` defines stage transitions.
- `SHARED/STAGE_EXIT_CONTRACT.md` defines universal stage exit criteria, gate outcomes, and stopping rules.
- `SHARED/SHARED_STATE_MODEL.md` governs evidence, working state, and approved artifacts.
- `SHARED/DOCUMENT_GOVERNANCE.md` governs versioning and sign-off.
- `SHARED/EXECUTION_LEVELS.md` requires deterministic automation before model calls where applicable.
- `SHARED/SESSION_CONTINUITY.md` and `SHARED/MEMORY_MODEL.md` govern continuity and memory.

## Linear execution

If subagents are unavailable, run roles sequentially. The same debate protocol and evidence rules still apply.

## Unit testing

Read `TESTING/AGENT_EVALUATION_CONTRACT.md` before evaluating a unit. Each unit has a `UNIT.json`. A council's member roles must be evaluated as part of the council's end-to-end behavior, not merely as isolated prompt quality.

## Package map

```text
SKILL.md                  — root entrypoint
AGENTS/                   — individual agents
COUNCILS/                 — atomic debate councils + their internal roles
DEPARTMENTS/              — independently packaged departments
  Developer_Organization/ —   Frontend/Backend/Mobile capabilities + Kanban
  QA_Organization/        —   independent verification, its own repo-shaped package
SHARED/                   — common infrastructure and governance
TESTING/                  — generic evaluation contract
UI/                      — local helper pages
```

Known source gaps are documented in `MANIFEST.json`; they are not silently fabricated.
