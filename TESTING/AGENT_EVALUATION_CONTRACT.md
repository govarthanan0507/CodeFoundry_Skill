# CodeFoundry — Generic Unit Evaluation Contract

The evaluator must accept **one unit folder as the target**. The unit may be an agent, council, or worker. A council folder is the complete council test boundary; its member folders are not required as separate inputs.

## Modes
- **Single-unit:** `evaluate(target_folder)`
- **Matched comparison:** `evaluate([target_a, target_b, ...])` using the same scenario set and scoring rubric
- **Agent vs direct LLM baseline:** compare the unit-mediated workflow with a matched direct-underlying-LLM workflow
- **Council vs council:** supply both council folders; evaluate end-to-end decision quality, evidence use, robustness, cost/tokens, latency, and human interventions

## Core rule
Measure the outcome produced by the whole unit, not merely its internal response quality. For a council, the outcome is the council decision package and gate behavior.

## Required metrics
Functional correctness, role/instruction adherence, ambiguity handling, evidence quality, unsupported assumptions, adversarial robustness, output quality, downstream utility, input/output/total tokens, model calls, latency, cost, human interventions, clarification turns, corrections/rework, success/failure, and reproducibility.

## Baseline
Where possible, use the same underlying model, tools, knowledge, context, objective, and scenario. Never weaken the baseline.

## Key question
**If I removed this unit and replaced it with the direct underlying LLM workflow, what would I lose?**

For comparisons, report raw measurements and the net difference. Never hide negative savings.
