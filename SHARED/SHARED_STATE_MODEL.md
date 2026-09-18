# Shared State Model — V1 (Completed)

## Why this matters

Without an explicit split, nothing stops multiple roles from treating `project-state.md` as one undifferentiated blob — and once that happens, a role can overwrite something another role depended on, or treat a draft note as if it were a settled decision. Three categories, each with different rules for who can change them and how.

## The three categories

### 1. Immutable evidence

Research findings, captured sources, recorded observations, test results, approved decision records. **Once written, these are never edited to say something different — they're superseded, not overwritten.** A corrected finding gets a new entry that references and supersedes the old one; the old one stays visible for traceability, the same way `AGENTS/Ideation/AGENT.md`'s correction rule keeps the original statement in conversation memory while updating current interpretation.

Where it lives in `project-state.md`: the `artifacts.completed` list and any evidence embedded in a handoff's `EVIDENCE` field, once that handoff has closed.

### 2. Mutable working state

Current plans, drafts, open questions, pending tasks, temporary findings — the equivalent of Ideation's Working Memory, generalized to every stage, not just Ideation. **This is allowed to change freely, be wrong, and be revised** — it's a scratchpad, not a record.

Where it lives: `project-state.md`'s `assumptions.active`, `risks.open`, `questions.open`, and `decisions.pending` sections — all explicitly named as mutable in the existing schema, which turns out to already match this model without having been labeled that way.

### 3. Approved artifacts

The authoritative documents downstream stages rely on — requirements.md once gated, an approved design package, an accepted architecture decision. **These require a gate to create or change.** No role edits an approved artifact unilaterally because implementation revealed friction — that's exactly the failure `COUNCIL.md`'s post-handoff accountability mechanism and `PARALLELIZATION_GUARDRAIL.md` both exist to prevent, generalized here to the state model itself.

Where it lives: `project-state.md`'s `artifacts.completed` list once a decision has moved from `decisions.pending` to `decisions.approved`, and any file explicitly marked as gate-approved (e.g. a `requirements.md` that's passed its human gate).

## The rule that ties it together

```text
Mutable working state
        ↓
  (a decision gets made, evidence supports it)
        ↓
Immutable evidence
        ↓
  (a human gate approves it)
        ↓
Approved artifact
```

Nothing skips a step. A role cannot promote its own draft directly to "approved artifact" status — that's the same overreach as a role deciding its own Hard Constraint is fine to proceed on without asking. And nothing moves backward silently — an approved artifact that needs to change re-enters through a gate, not a quiet edit, which is precisely what the Orchestrator's re-entry logic in `AGENTS/Orchestrator/AGENT.md` is for.

## Why this prevents "10 agents rewriting the same artifact"

Each category has exactly one path to being written and one path to being changed. A role touching `project-state.md` should always be able to say which of the three categories it's writing to and why — if it can't, that's a sign the write shouldn't be happening yet, or should be going through a gate first.
