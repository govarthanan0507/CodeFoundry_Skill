# Backend Developer — Workflow

## Lifecycle

```text
UNDERSTAND
  Read requirements, acceptance criteria, existing schema/API, stage/budget context.
  If anything required is missing -> BLOCKED / WAITING_FOR_HUMAN.

DESIGN
  Produce or update the data model and API contract (see API_CONTRACT.md).
  State the database/infra choice and its stage-based reasoning explicitly.

VALIDATE CONTRACT
  Lint the API spec. Where tooling supports it, verify against a mock server
  before real implementation begins. Catch contract problems before they're
  built into working code.

PLAN
  Write the migration plan: forward migration, paired rollback, backup
  strategy. For anything destructive or production-bound, plan the backup
  and restore-test BEFORE planning the change itself.

BUILD
  Implement against the validated contract. Follow the ten implementation
  rules in AGENTS/Backend/AGENT.md.

RUN
  Start the service against a real (not stubbed) data layer where feasible.

VERIFY
  Run the QA_CONTRACT.md checklist scaled to this change's risk level:
  primary flows, migration + rollback, backup + restore test, load behavior,
  auth/input validation.

CRITIQUE
  Switch to critic mode. Apply relevant items from RELIABILITY_PRINCIPLES.md.
  Look specifically for what happens when this fails unattended.

FIX
  Resolve actionable findings within scope. Escalate what isn't.

RE-VERIFY
  Repeat VERIFY for anything changed during FIX.

HANDOFF
  Use the structured handoff format. Do not mark SUCCEEDED without the
  required evidence.
```

## When a design problem surfaces mid-build

```text
BUILD
  ↓
Conflict / impossibility / missing decision
  ↓
Report as a change request, not a silent redesign
  ↓
Escalate to orchestrator / architecture role
  ↓
Approved change
  ↓
Resume BUILD
```

The worker does not silently override an approved architecture or contract decision because implementation revealed friction. Friction is evidence to report upstream, not license to improvise.

## Risk-scaled verification

Not every change needs the full checklist. Scale verification to risk:

- **Low risk** (internal tooling, no user data, easily reversible): primary flow + basic auth check is sufficient.
- **Medium risk** (user-facing feature, schema change, no destructive operation): add migration + rollback test.
- **High risk** (production data, destructive operation, auth/security surface, anything affecting money or compliance): full checklist — backup + verified restore, load test, security review — is mandatory, not optional.

State which risk tier was applied and why in the handoff.
