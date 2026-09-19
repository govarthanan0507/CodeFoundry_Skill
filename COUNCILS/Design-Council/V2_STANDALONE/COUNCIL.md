# Design Council V2

## Mission
Turn the approved product into coherent product structure and design while preserving upstream meaning and feasibility conditions.

## Sequence
Validate inputs/authorization → enumerate capabilities and domain concepts → PM proposes Capability→Epic→Version → specialists debate capability-by-capability → resolve tradeoffs → Independent Critic → produce PRD/FRD/TRD → final traceability gate → handoff.

## Final artifacts
PRD.md — PM: what product/version is built and why.
FRD.md — Council: observable functional behavior, flows, states, interaction rules, design risks.
TRD.md — Council: architecture, technical decisions, API shape, data model, security/reliability, integrations, hosting/deployment, tradeoffs and rejected alternatives.

## Final gate
Fail on capability omission, domain concept loss, upstream commitment loss, technical-layer-only epic, incoherent V1, non-reconstructable PRD, missing PRD→FRD→TRD traceability, or silent conversion of unresolved product meaning into design.

Downstream Planning consumes the complete inherited context plus PRD/FRD/TRD; it must not rediscover product structure.
