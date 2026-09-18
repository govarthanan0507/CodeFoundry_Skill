# CodeFoundry Frontend Developer Worker

This package turns the CodeFoundry frontend specialist into an explicit worker with its own skill, workflow, design contract, and QA contract.

## Package

- `CAPABILITY.md` — agent-facing operating instructions (renamed from SKILL.md so only the package root keeps that reserved name)
- `workflow.md` — execution lifecycle
- `DESIGN_CONTRACT.md` — persistent `DESIGN.md` rules
- `QA_CONTRACT.md` — verification and evidence rules
- `UX_PRINCIPLES.md` — advisory behavioral-design knowledge for critic mode
- `../../AGENTS/Frontend/AGENT.md` — CodeFoundry specialist identity and handoff contract

## Reference capabilities

The worker is designed around three complementary ideas:

1. **Taste-style design intelligence** — infer visual direction and avoid generic AI-generated interfaces.
2. **Persistent DESIGN.md** — keep visual language as a durable project artifact.
3. **Playwright browser verification** — validate the actual running application rather than trusting source code or build output alone.

These are reference capabilities, not copied third-party implementations. CodeFoundry retains authority over lifecycle gates, approvals, evidence, and worker completion state.

## V1 completion principle

```text
Code written
   !=
Frontend complete

Frontend complete
   =
Implementation + verification + evidence
```

**Test boundary:** this worker package is directly testable as one unit; its linked specialist identity is a dependency, not a second worker.
