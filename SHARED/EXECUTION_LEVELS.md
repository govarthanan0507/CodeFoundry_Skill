# Execution Levels — V1 (Completed)

## The question this answers, and why it comes before model selection

Every task so far has assumed "which model handles this" is the first question. It isn't — the first question is **"does this need a model at all?"** Routine, fully-specified, mechanical work should run as plain code, zero tokens, zero variability. A model gets invoked only when something genuinely requires judgment, synthesis, or handling ambiguity.

## The three levels

```text
Level 0 — Deterministic code, no AI
  Filesystem checks, validation against a known schema, folder
  structure verification, report generation from existing files,
  version/status scanning. If the logic can be written as an
  if/else against known rules, it belongs here.

Level 1 — Lightweight model (cheap tier)
  Classification, simple extraction, routing decisions,
  normalization — genuinely needs a model, but not deep reasoning.

Level 2 — Deep reasoning model
  Architecture decisions, adversarial debate, ambiguous
  interpretation, anything already assigned Opus/Sonnet in the
  per-role `model:` frontmatter across this system.
```

## The rule

Before any Orchestrator-routed task reaches a model at all, check whether a Level 0 script already covers it. If yes, run the script — don't spend a model call on it. `AGENTS/Orchestrator/AGENT.md` owns this check, same lane as its existing model-selection responsibility, just one step earlier.

## Real scripts, not just the rule

Two actually work, included in `scripts/` and run against this project's real folders to confirm they function, not just described:

- `scripts/validate_structure.py` — checks every project folder against `PROJECT_FOLDER_STRUCTURE.md`'s convention (has `documents/`, `handoffs/`, `state/`; document filenames match the `-vN` versioning pattern). Pure validation, no AI needed, ever.
- `scripts/document_status_report.py` — scans every project's `documents/` folder and reports DRAFT vs. SIGNED OFF status per `DOCUMENT_GOVERNANCE.md`'s header format, across every project at once. Pure text parsing, no AI needed.

Both are genuinely Level 0 — a model would get the same answer, slower and at real token cost, for zero benefit over a script that runs instantly and identically every time.
