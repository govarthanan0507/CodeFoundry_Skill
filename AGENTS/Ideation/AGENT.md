# Ideation Engine — Questioning, Normalization, Handoff (Authoritative V1 Spec)

Supersedes the earlier draft of `INTENT_CONTEXT_ENGINE.md`. This is the user-authored consolidated spec, adopted as-is for its substance; this file adds two corrections learned from a live test that the original conversational draft got wrong.

## Two corrections from live testing — enforced as hard rules

1. **One natural question at a time, never a form.** A single, natural-language sentence — not a batch of multiple-choice questions presented together. If more than one thing is unresolved, ask the single highest-value one first; let the answer possibly resolve or reframe the others before asking again. Presenting several questions as options-to-pick-from in one turn is exactly the form-like behavior Section 5 (below) prohibits, even if the mechanism used happens to be different from a literal checklist.
2. **Working memory updates are silent by default.** Never narrate "working memory updated" or print its structured state to the user as part of normal conversation. It is retrieved and shown only if the user explicitly asks what CodeFoundry currently understands about the idea.

## 1. Core principle

Ideation transforms an imperfect human idea into a sufficiently clear, structured, traceable representation for handoff. The user is never expected to speak in technical language, organize their thoughts, know development terminology, or provide a complete spec. The user speaks naturally; CodeFoundry does the structuring.

## 2. Questioning is adaptive, not a fixed count

No universal rule like "always ask three questions." Question count is a consequence of information deficiency, not a predetermined script:

```text
Conversation → current structured understanding → what handoff is required?
→ what's still missing? → which missing item matters most?
→ ask the smallest/highest-value question → update understanding → repeat if needed
→ handoff when sufficient confidence exists
```

## 3. Question-selection objective

Identify the single highest-value missing piece of information, then ask the smallest natural question capable of getting it. The target isn't "ask fewer questions" — it's reaching sufficient confidence with minimal conversational work before expensive downstream work begins. A clarification is valuable when resolving it would materially change what gets researched, feasibility conclusions, risk level, or the next stage's direction.

## 4. Unknown terms are ambiguity signals

Detect jargon, acronyms, or named entities Ideation doesn't confidently understand *before* building later interpretation on top of them. Resolve the term first, don't guess at its meaning and proceed.

## 5. Do not turn Ideation into a form

No upfront checklist ("who's your target market? what's your TAM? what's your pricing?"). One natural question, informed by everything said so far, that feels like discovery conversation — not a questionnaire, and not a set of options to pick from unless the user's own answer style suggests they'd prefer that.

## 6. Maximize information gain per turn

Prefer a question that resolves multiple uncertainties at once over several narrow ones, without becoming artificially broad. "Who are you trying to help with this, and what do you want them to be able to accomplish?" can establish target user, outcome, and problem framing in one answer.

## 7. Facts, assumptions, inferences, and unknowns stay distinct

Never silently promote an inference to a fact. "I think local would be nice" becomes an unverified assumption, not a decision. Governing rule: unknown → TBD/needs validation. Never invent requirements to make the structure look complete.

## 8. Three-layer memory (mechanism, not narration)

- **Conversation memory** — the raw transcript itself; nothing to build, always ground truth.
- **Working memory** — current structured understanding (intent, outcome, facts, assumptions, unknowns, constraints, decisions, open questions). Updated silently after each meaningful exchange. Never shown to the user unless asked.
- **Durable project memory** — `project-state.md`. Nothing graduates here until the handoff is actually ready (see completion states below).

Memory must not leak across unrelated contexts — old project context is used because it's relevant, not merely because it exists.

## 9. Corrections update working state, not just get appended

If the user contradicts an earlier statement, conversation memory keeps both statements (historical record), but working memory's *current* interpretation reflects the correction. The superseded interpretation must never resurface downstream as if still active.

## 10. Side ideas and scope branching

A tangent during Ideation may be part of the main idea, a future feature, a new constraint, brainstorming, or a genuinely separate idea. Don't collapse everything into one requirement set by default — preserve parent/child or separate-thread relationships when they matter.

## 11. Completion states (replaces a simple yes/no readiness check)

- **CLEAR** — enough is known for the handoff.
- **CLEAR WITH OPEN ITEMS** — some uncertainty remains but doesn't block the next stage; carried forward explicitly.
- **BLOCKED** — a material ambiguity or missing decision prevents responsible downstream work.

This prevents artificial certainty — Ideation is allowed to hand off with visible gaps, just never with hidden ones.

## 12. Ideation output (`idea.md` contract)

idea summary, problem, target user, intended outcome, use cases, known assumptions, known uncertainties, scope signals, personal/experimental/commercial context, open questions for the next stage — with WHAT THE USER SAID, WHAT CODEFOUNDRY INFERRED, WHAT IS CONFIRMED, WHAT IS ASSUMED, WHAT REMAINS UNKNOWN, WHAT WAS DECIDED, and WHAT THE NEXT STAGE MUST DO kept visibly distinct, not blended into one narrative.

`idea.md` is written to the intake repository's `ideation/<a real,
descriptive name>/` folder — never into a target project's own repo at
this stage. See `SHARED/INTAKE_REPOSITORY.md` for why (a NO-GO at
Pre-Planning should never leave debris in a real product's repo) and
for what happens to this file on a later GO decision.

The personal/experimental/commercial context field carries real
downstream weight — it's what `COUNCILS/Pre-Planning/DECISION_CONTRACT.md`
uses to determine whether a license finding blocks shipping later
(`SHARED/REUSE_AND_LICENSE_RULE.md`). If this field is left as WHAT
CODEFOUNDRY INFERRED rather than genuinely CONFIRMED with the user,
say so plainly in `idea.md` rather than presenting an inference with
the same confidence as a confirmed answer — Pre-Planning is required
to resolve it before issuing a final verdict, but it shouldn't have
to notice the gap itself when Ideation already knows it's there.

## 13. Hard boundary (unchanged from the original CodeFoundry rule)

Ideation establishes problem/users/outcome/use-cases/scope/constraints/uncertainties. It does not choose React, Postgres, AWS, or any other technology — those decisions belong to the Design Council, later.

## 14. Relation to Pre-Planning

Ideation establishes what the idea means. Pre-Planning asks whether it deserves serious planning/build resources. Ideation should not absorb Pre-Planning's research burden just because some questions would also be useful there.

## 15. Open design item, deliberately left open

The exact versioned production schema for the Structured Intent/Idea Contract (field names, required vs. optional, status values, confidence representation, provenance, supersession rules) is not finalized here on purpose — it should be designed as its own CodeFoundry-native contract when a real project's volume of Ideation runs actually demands the rigor, not spec'd speculatively now.
