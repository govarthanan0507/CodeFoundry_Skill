# Design Decisions

Per `CONSTITUTION.md` principle 9 (Succession), this exists so a future
maintainer understands why this organization looks the way it does,
without access to the conversation that produced it.

## Why this is extracted from CodeFoundry, not built fresh

CodeFoundry's Frontend/Backend/Mobile Developer workers, its Kanban
workflow, delivery-timeline tracking, and QA-handoff loop were already
built and hardened in the same working session that produced this
package. Rebuilding them here would have repeated work that already
exists and is already correct — the same "don't reinvent what's
already proven" motto CodeFoundry itself is built around, applied to
this organization's own construction. This package's job was
organizing that material into something independently shippable, not
producing new capability content.

## Why this is a separate package from CodeFoundry and from QA_Organization

Established directly, before this package was built: CodeFoundry is
the umbrella "company," and its departments (Ideation, Pre-Planning,
Design Council, this one, QA, eventually Release) are each meant to be
independently packaged and shippable — not only usable bundled
together. `QA_Organization` already proved this model works as a real,
standalone repo. This package is the same model, applied to the build
side, deliberately kept separate from the QA repository per an
explicit instruction earlier in this project's history: the two are
not to be merged or nested inside each other.

## Why the periodic-logging rule is Constitutional, not procedural

This was stated as the one non-negotiable rule for this organization,
directly, rather than left as an implementation detail buried in a
workflow file. The reasoning connects to the `Base_Memory_OS` case
study examined earlier in this project's history: a prior AI-driven
build produced good code and heavy documentation, and still let a
false "100% complete, verified" claim through, because nothing forced
a check at the moment of the claim. Constitution principle 2
(verification before claiming) is the direct fix for that failure.
Principle 1 (periodic logging) is the complementary fix for a related
but distinct risk: even an honest developer can lose track of what
they've actually learned mid-task if it isn't captured as it happens,
and a reconstructed-afterward log is exactly the kind of artifact this
project's own QA_Organization already learned not to trust (evidence
recorded after the fact is weaker than evidence recorded at the time).

## Why Development doesn't get its own QA capability

Considered and rejected: CodeFoundry's `WORKER_SCOPE_REGISTRY.md`
lists "QA Worker" as scoped-but-unbuilt. Building it inside this
package, or inside CodeFoundry, would create two QA systems — a
weaker one here and the real one in `QA_Organization` — with no clear
reason for either to defer to the other. `SHARED/HANDOFF_TO_QA.md`
routes to the real one instead, reusing its actual schema
(`FINDING.schema.json`) and cycle model (`LIFECYCLE.md`'s
fix-verification re-entry) rather than approximating them.

## Open question, deliberately left open

Whether this package should eventually get its own `ENGINE/`-style
staged state machine (mirroring `QA_Organization`'s fifteen-stage
engine) or stay contract-plus-Kanban-shaped, as it is now. The working
assumption carried into this package is the same one recorded in
`QA_Organization`'s own history: build it lighter than QA, because
mature development tooling already exists for the mechanical parts,
and the missing piece was handoff/logging discipline, not process
depth. This has not been tested against real, sustained use yet — the
same "prove it before hardening it further" discipline this whole
project keeps applying to itself.
