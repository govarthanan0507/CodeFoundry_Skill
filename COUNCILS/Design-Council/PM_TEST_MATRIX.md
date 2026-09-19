# Product Manager Adversarial Test Matrix

## Purpose

This is the dedicated adversarial test boundary for the Design Council Product Manager.

The objective is not to test whether the PM can produce a polished epic list. The objective is to detect whether decomposition silently changes, compresses, fragments, or loses the product.

The matrix is intentionally broader than conventional SaaS examples because the known failure mode is conceptual compression: a novel product is rewritten as generic infrastructure and the resulting epics look reasonable.

## Hard invariants

A PM run fails if any of these occur:

1. A current-scope capability has no disposition.
2. A material upstream commitment disappears without an explicit disposition.
3. A domain-defining concept disappears or becomes only an implementation detail.
4. A technical layer is presented as a product outcome without an enabling relationship.
5. A meaningful product outcome is split into unusable fragments.
6. Independent product outcomes are artificially collapsed merely to reduce epic count.
7. A cross-cutting capability is silently assigned to one epic or duplicated without an ownership rule.
8. A deliberate non-goal is silently converted into scope.
9. Version 1 is technically buildable but not a coherent product increment.
10. The PRD cannot reconstruct the product without the original conversation.
11. The PM silently changes upstream intent instead of escalating/re-entering.
12. PRD → FRD → TRD traceability cannot be established.
13. The PM invents precision through arbitrary scoring or an arbitrary target epic count.
14. The PM uses architecture as the substitute for product structure.
15. The PM marks a product as complete when unresolved product meaning remains.

## Concept families

| ID | Concept family | Adversarial case |
|---|---|---|
| PM-01 | Novel semantic domain | Product's value depends on an unusual ontology or semantic model |
| PM-02 | Workflow | Value emerges only from several connected steps |
| PM-03 | Platform | Most work is enabling infrastructure |
| PM-04 | API product | Product boundary is an API rather than a UI |
| PM-05 | Data product | Value depends on data lifecycle and analysis |
| PM-06 | AI/ML | Model/embedding/retrieval components tempt implementation-first decomposition |
| PM-07 | Search/retrieval | Index/retriever can be mistaken for the product |
| PM-08 | Recommendation | Ranking mechanism can overshadow user outcome |
| PM-09 | Content/media | Content types/screens can replace the actual experience |
| PM-10 | Creative tool | Tools/screens can replace creative workflow and artifact lifecycle |
| PM-11 | Automation/agentic | Agents/tools/tasks can replace the user's goal |
| PM-12 | Marketplace | Multiple participant outcomes must coexist |
| PM-13 | Multi-sided B2B | Buyer, operator, end user, admin and provider can differ |
| PM-14 | Collaboration/realtime | Synchronization can overshadow collaboration outcome |
| PM-15 | Physical + software | Hardware/software layers can fragment one product |
| PM-16 | Migration | Migration mechanics can overshadow destination outcome |
| PM-17 | Existing-code extension | Legacy architecture can distort approved product meaning |
| PM-18 | Personal/hobby | Commercial ROI is inappropriate as the primary value criterion |
| PM-19 | Regulated/high consequence | Compliance can swallow product purpose |
| PM-20 | Security/privacy | Security mechanisms can replace protected product behavior |
| PM-21 | Compound capability | One capability contains several independent outcomes |
| PM-22 | Tiny product | Over-decomposition creates meaningless epics |
| PM-23 | Large product | Under-decomposition hides distinct domains |
| PM-24 | Cross-cutting capability | Capability legitimately affects several epics |
| PM-25 | Shared enabling capability | Foundation supports multiple product outcomes |
| PM-26 | Negative scope | Non-goals are important product boundaries |
| PM-27 | State/lifecycle-heavy | States/transitions/invariants are part of product meaning |
| PM-28 | Uncertain concept | Product intent itself is unresolved; false precision is dangerous |
| PM-29 | Cost-constrained product | Feasibility constraints tempt architecture-first epics |
| PM-30 | Scale/concurrency-sensitive | Operational conditions materially change product boundaries |
| PM-31 | International/multi-locale | Locale, language, regulatory and content variation interact |
| PM-32 | Role/permission-heavy | Multiple actors and permissions define behavior |
| PM-33 | Event-driven | Events and timing are product behavior, not just infrastructure |
| PM-34 | Offline/local-first | Sync, local state and conflict behavior matter to the product |
| PM-35 | Integration ecosystem | External systems are dependencies, not automatically product epics |
| PM-36 | Monetization-dependent | Payment/billing may be a capability, constraint, or enabling mechanism depending on product meaning |

## Required test procedure

For every test case:

1. Supply the PM with only the inherited artifacts that CodeFoundry says it should receive.
2. Do not tell the PM the expected epic count.
3. Do not provide a suggested decomposition.
4. Require capability enumeration before epic selection.
5. Require domain-defining concept extraction.
6. Require explicit current scope and non-goals.
7. Require capability → epic traceability.
8. Require product-value justification for every epic.
9. Require dependency and version reasoning.
10. Require the PRD reconstruction test.
11. Require the PM self-audit against the applicable concept families.
12. Run the independent Design Council progression gate against the result.

## Mutation tests

Take a passing product definition and mutate exactly one property:

- rename a domain concept to a generic technical term;
- add a hidden enabling commitment in Feasibility;
- add a non-goal that conflicts with an apparent feature;
- merge two independent capabilities;
- split one compound capability into technical layers;
- add a cross-cutting capability;
- add a new actor with a required outcome;
- change a feasibility constraint;
- introduce an unresolved product decision;
- remove a capability from the upstream document.

Expected behavior: the PM must either preserve the changed meaning, expose the change, or fail/escalate. It must never silently produce the same-looking epic structure.

## Scoring rule

This matrix is a contract test, not a subjective quality score.

- Any hard-invariant failure = FAIL.
- A polished PRD with one silent omission = FAIL.
- A correct escalation because product meaning is genuinely unresolved = PASS.
- A smaller epic count is not better.
- A larger epic count is not better.
- The only valid optimization is preservation of product meaning with coherent delivery boundaries.

## Minimum qualification set

Before a PM version is treated as hardened, it must pass at least:

- all 36 concept families above;
- all mutation tests;
- a dedicated reproduction of the historical base_memory_os failure;
- a technical-layer compression case;
- a semantic/domain-model preservation case;
- a cross-cutting capability case;
- a compound-capability case;
- a negative-scope case;
- an enabling-foundation case;
- an unresolved-intent case.

The test result must identify the exact invariant checked, not merely report "PM output looks good."
