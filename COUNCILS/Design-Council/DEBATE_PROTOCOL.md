# Design Council — Debate Protocol

## Why debate is mandatory, not optional

A design that no one on the Council pushed back on is a design that hasn't been tested yet — it's just been agreed with. The debate is where a bad idea gets caught before it costs Development time and before it costs the human a wasted approval cycle.

## Structure

```text
Each role states its position on the design as it currently stands.
        ↓
Any role may challenge another role's position, naming the specific
tradeoff it creates for their own domain.
        ↓
The challenged role responds: accept, defend, or propose an alternative.
        ↓
Synthesizer resolves genuine disagreements into one decision,
preserving the reasoning and the rejected alternative.
        ↓
Independent Critic reviews the synthesized design fresh, attacking
only — no proposing.
        ↓
Council revises if the Critic's findings are material, otherwise
finalizes.
```

## Example (from the original blueprint, kept as reference)

```text
UX: This interaction adds friction for first-time users.
Frontend: It also adds client-side state complexity.
Backend: The alternative requires another API round trip.
Security: The alternative exposes a broader authorization surface.
Architect: Let's compare both options against MVP constraints.
Synthesizer: Option B gives the best MVP tradeoff.
Independent Critic: You have not addressed failure behavior.
Council: Revise design.
```

## Synthesizer

Not a permanent 8th personality — a function any senior member can perform, or a dedicated pass. Its job:

- Resolve disagreements into one decision.
- Preserve the tradeoff and the rejected alternative in the record — a synthesized decision with no visible reasoning is indistinguishable from an arbitrary one.
- Never silently pick the option that was easiest to write up.

## Independent Critic

Rules that keep it independent instead of becoming a co-author:

- Reviews the synthesized design with fresh eyes — it does not participate in the original debate.
- May only find gaps and raise questions. It does not propose solutions; that would make it a de facto 8th architect.
- Must be specific: "you haven't addressed failure behavior" is useful; "this feels risky" is not.
- Has an effective veto in one sense only: a design with an unaddressed Critic finding does not proceed to the human gate silently — the finding must be resolved or explicitly carried into the gate as a visible open risk.

## A silent role is a suspicious role

A live test run surfaced this directly: a role that raises no challenge and shows no rejected alternative across an entire design pass is not "in agreement" by default — it may simply not have applied its own judgment. Every role must show at least one of: a challenge to another role's proposal, a rejected alternative for its own decision, or an explicit "reviewed and found no objection, here's why." A pass with none of these from a given role is treated as incomplete for that role, not as a clean bill of health. (See `roles/ui-designer.md` for where this was first needed in practice.)

## When there is no synthesis — deadlock is a valid outcome

A stress test surfaced this gap directly: the Synthesizer's job is to resolve disagreement, but "resolve" was never allowed to mean "report that the constraints genuinely conflict and no design satisfies all of them." Without that permission, the Synthesizer is pressured to manufacture a decision that looks like consensus but is actually one role's rejected proposal relabeled — which is worse than an honest deadlock, because it hides the conflict instead of surfacing it.

The Synthesizer must output **NO SYNTHESIS POSSIBLE** instead of forcing a decision when:

- two or more roles' hard constraints (not preferences) are mutually exclusive as currently stated, and
- no option on the table satisfies all of them, and
- relaxing a constraint (budget, latency, security posture) would require a decision the Council isn't authorized to make on its own.

When this happens:

```text
NO SYNTHESIS POSSIBLE
CONFLICTING CONSTRAINTS: [name each role and its non-negotiable constraint]
OPTIONS REQUIRING A HUMAN DECISION:
  - Option A: relax constraint X (owned by role Y) — consequence: ...
  - Option B: relax constraint Z (owned by role W) — consequence: ...
  - Option C: descope the feature to something that fits all current constraints — consequence: ...
RECOMMENDATION: none — this requires a tradeoff only the human can authorize
```

This goes to the human gate as an explicit decision point, not a design the human is asked to rubber-stamp. The Council's job in a genuine deadlock is to make the tradeoff legible, not to quietly pick one side of it.

## When the premise itself is wrong — reframe, don't deadlock

A separate test case surfaced a third outcome, distinct from both clean resolution and deadlock. A request can be **factually impossible as stated, at any budget or resource level** — not because roles' constraints conflict, but because the request rests on something that doesn't exist or can't be done with the tools available (e.g. "transcode into a proprietary codec format" with no licensed encoder access, regardless of money spent). This is not a tradeoff between options — there is only one option, and debating it as if resources could change the answer wastes the human's time and can produce a false impression that more budget or a different choice would fix it.

The role that catches this (any role may, but Product/Architect and the domain specialist most often will) must distinguish it explicitly from a deadlock:

```text
INFEASIBLE PREMISE — NOT A RESOURCE TRADEOFF
WHAT WAS REQUESTED: [as stated]
WHY IT'S IMPOSSIBLE AS STATED: [the actual technical/legal/factual wall, cited]
WHAT IS ACTUALLY BUILDABLE: [the corrected, feasible version of the intent behind the request]
WHAT REMAINS OUT OF REACH: [named plainly, so the human isn't left thinking a bigger budget solves it]
```

This goes to the human as a proposed corrected scope, not a menu of tradeoffs to weigh — because there's nothing to weigh. **The human then decides how to proceed**: accept the corrected/buildable scope, drop the feature entirely, or pursue the infeasible part through a path outside CodeFoundry's current capability (e.g. acquiring a commercial license) — but that decision is made with an accurate picture of what is and isn't actually possible, not a debate that implies it's negotiable when it isn't.

The distinction that matters operationally:

- **Deadlock** = the options all exist, they just conflict with each other. The human trades off between real choices.
- **Infeasible premise** = one or more of the "options" doesn't actually exist. The human isn't trading off — they're being told the truth about what's on the table before deciding whether to proceed with what remains.

Conflating these two is itself a failure mode: presenting an infeasible premise as if it were a resource deadlock ("we could do this if we had more budget") when no budget would fix it is worse than either outcome alone, because it gives the human false hope that a different tradeoff would work.

## Human interaction during debate

The Council may ask the user a question only when:

- the choice materially affects product intent,
- requirements are genuinely incomplete,
- no reasonable default exists, or
- a business/user preference cannot be safely inferred.

Otherwise the Council decides itself. The goal is few interactions, not zero — a Council that asks the user to resolve every internal disagreement isn't doing its job.

## What gets recorded

Every material disagreement, its resolution, and its rationale — not only the final answer. This record is what a future Development change request gets checked against (see `COUNCIL.md`'s post-handoff accountability section) — if the same tradeoff resurfaces during Development, the recorded reasoning is the first thing to check before re-litigating it from scratch.
