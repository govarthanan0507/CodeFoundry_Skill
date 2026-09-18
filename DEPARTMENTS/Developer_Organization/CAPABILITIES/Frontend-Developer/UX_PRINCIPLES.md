# UX Principles — Advisory Critic Knowledge

This file gives the Frontend Developer Worker a compact set of human-computer interaction principles to consider during critique.

These are **advisory heuristics, not hard acceptance gates**. A principle may be intentionally violated when the product context, accessibility needs, platform convention, or task requirements justify it.

## Critic behavior

During `CRITIQUE`:

1. Identify which principles are materially relevant to the current screen, workflow, and user task.
2. Do not mechanically evaluate every principle on every task.
3. Look for observable design consequences rather than merely naming a law.
4. Prefer concrete recommendations tied to the user's task.
5. Use browser evidence when the issue can be observed or tested.
6. Do not invent universal numeric thresholds unless the project or platform provides one.
7. Treat an intentional trade-off as acceptable when there is a defensible product reason.
8. Prioritize findings by user impact: `BLOCKER`, `MAJOR`, `MINOR`, or `ADVISORY`.
9. Do not block completion solely because an advisory UX principle is imperfect.
10. Surface only the most useful findings; avoid critique noise.

## Principle groups

### Decision load

**Hick's Law — choice complexity**
- Check whether the number and prominence of choices unnecessarily slow the primary task.
- Look for competing primary actions, excessive navigation choices, and unclear prioritization.
- Prefer reducing or grouping choices when that improves the task.

**Miller's Law — manageable information chunks**
- Check whether information is grouped into understandable chunks.
- Avoid treating a fixed number such as seven items as a universal limit.
- Consider scanning, grouping, progressive disclosure, and task context.

**Pareto Principle — focus on the high-value path**
- Check whether the interface gives disproportionate attention to the small set of actions that matter most.
- Secondary features should not visually overwhelm the core workflow.

### Interaction ergonomics

**Fitts's Law — target acquisition**
- Check whether important interactive targets are easy to acquire and appropriately sized.
- Consider target size, spacing, proximity to related controls, and device/input method.
- Pay special attention to touch interfaces and destructive actions.

**Minimize target distance**
- Check whether frequently paired actions or controls are unnecessarily far apart.
- Consider cursor travel, thumb reach, and task flow.
- Do not optimize distance at the expense of hierarchy or accessibility.

### Familiarity and consistency

**Jakob's Law — familiarity**
- Check whether common interface patterns behave in ways users are likely to recognize.
- Avoid novelty that makes basic navigation or controls harder to understand without a product reason.

**Law of Proximity — grouping by spatial closeness**
- Check whether related labels, controls, values, and content are visually grouped.
- Check whether unrelated elements have enough separation.

**Law of Similarity — similar things look related**
- Check whether controls with the same purpose share visual treatment and behavior.
- Avoid visually identical treatment for meaningfully different actions.

**Uniform Connectedness — explicit visual relationship**
- Check whether elements that form one conceptual group are visibly connected through containers, shared backgrounds, borders, lines, or other appropriate treatment.
- Do not add decoration merely to create grouping where proximity already communicates it clearly.

### Hierarchy and attention

**Von Restorff Effect — distinctive important elements**
- Check whether the most important action or information is sufficiently distinguishable.
- Avoid making everything visually prominent.

**Serial Position Effect — order matters**
- Check whether important items appear where users are most likely to notice and remember them.
- Consider first/last placement, task sequence, and whether critical actions are buried in the middle of long lists.

**Law of Prägnanz — perceptual simplicity**
- Check whether the interface can be understood with the simplest coherent visual structure.
- Remove unnecessary visual complexity without removing necessary information.

### Feedback and task completion

**Doherty Threshold — responsiveness and perceived waiting**
- Check whether the interface provides timely feedback for actions and visible progress for operations that take time.
- Prefer measured project-specific performance evidence when available.
- Do not invent a universal latency requirement; feedback quality matters when precise timing data is unavailable.

**Peak-End Rule — memorable moments and endings**
- Check important moments and especially task completion.
- Successful workflows should end with clear confirmation, useful next steps, or an understandable result rather than an abrupt state change.

**Zeigarnik Effect — unfinished tasks remain salient**
- For multi-step or interruptible workflows, check whether progress, incomplete work, and recovery paths are clear.
- Consider preserving context so users can understand what remains and resume confidently.
- Do not force progress indicators onto simple tasks where they add noise.

### Complexity and trade-offs

**Tesler's Law — complexity cannot always disappear**
- Check where unavoidable complexity has been placed.
- Prefer absorbing complexity into the product when that meaningfully reduces user burden, but do not hide necessary decisions or safety-critical complexity.

**Occam's Razor — simplest adequate solution**
- Check whether the UI introduces unnecessary concepts, controls, steps, or visual machinery.
- Prefer the simplest solution that satisfies the actual requirement.

**Parkinson's Law — unnecessary expansion**
- Check whether workflows, screens, forms, or content have grown beyond what the task needs.
- Look for excessive configuration, whitespace used without purpose, feature bloat, and unnecessary steps.

### Input and output behavior

**Postel's Law — tolerant input, clear output**
- Where appropriate, accept reasonable variations in user input instead of making users conform to unnecessary formatting rules.
- At the same time, be strict about safety, validity, and domain constraints.
- Return clear, predictable, actionable validation and system feedback.

## Applying the principles

The worker should reason in this form:

```text
OBSERVATION
→ RELEVANT PRINCIPLE
→ USER IMPACT
→ RECOMMENDATION
→ EVIDENCE
```

Example:

```text
OBSERVATION
Three equally prominent buttons compete at the end of a checkout flow.

PRINCIPLE
Hick's Law + Von Restorff Effect

USER IMPACT
The user may hesitate over which action completes checkout.

RECOMMENDATION
Establish one dominant completion action and visually subordinate secondary actions.

EVIDENCE
Browser screenshot + DOM snapshot of checkout footer.
```

## Reporting

Only report materially useful principles. A critique may contain:

```text
UX PRINCIPLES
- Hick — ADVISORY: three equally prominent next actions compete for attention.
- Fitts — PASS: primary controls are appropriately sized for the target input device.
- Peak-End — MAJOR: successful submission ends without clear confirmation.
- Zeigarnik — N/A: single-step task with no unfinished workflow state.
```

`PASS`, `ADVISORY`, `MAJOR`, `BLOCKER`, and `N/A` are critique outcomes, not automatic product gates. The overall CodeFoundry completion contract remains authoritative.
