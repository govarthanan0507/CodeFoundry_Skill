# Testing CodeFoundry Units

The package is intentionally organized around **testable units**, not merely neat folders.

### Test one agent
Give the evaluator: `AGENTS/Ideation/` (or any other agent folder).

### Test one council
Give the evaluator: `COUNCILS/Pre-Planning/` or `COUNCILS/Design-Council/`. The supplied council folder contains its member roles, protocol, constraints, and output contract.

### Compare the two councils
Give the evaluator both folders as two matched targets. The harness resolves each `UNIT.json`, runs the same test scenarios, and produces a side-by-side benchmark.

### Test a department
Give the evaluator one `DEPARTMENTS/<name>/` folder — e.g.
`DEPARTMENTS/Developer_Organization/CAPABILITIES/<Worker>/` for one
capability, or the whole `Developer_Organization/`/`QA_Organization/`
folder for an end-to-end department test.

This means separation is organizational only; the **unit boundary is explicit and machine-readable**.
