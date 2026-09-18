# Reliability Principles — Advisory Critic Knowledge

Consulted only in critic mode, and only for principles materially relevant to the current change's risk level and product stage. This is not a checklist to mechanically run against every change — a low-risk MVP tweak does not need every principle below applied.

Use the reasoning pattern: `OBSERVATION -> RELEVANT PRINCIPLE -> FAILURE IMPACT -> RECOMMENDATION -> EVIDENCE`.

## What a senior backend hire is actually evaluated on

Not "does the endpoint return 200" — but:

1. **System design judgment** — chooses the smallest architecture that satisfies real requirements; can articulate why a more complex option was NOT chosen.
2. **Data modeling and database expertise** — schema design, indexing, transactions, migration safety, and knowing when a database choice needs to change.
3. **API design** — contracts that are stable, versionable, and don't leak internal implementation details to consumers.
4. **Security fundamentals** — authn/authz done correctly, input validated, secrets never in code or logs, awareness of common attack classes (injection, broken access control, SSRF).
5. **Performance awareness** — can identify N+1 queries, missing indexes, and unnecessary round-trips before they become incidents.
6. **Operational maturity** — treats backup, rollback, and recovery as part of the job, not an afterthought delegated to "ops." Thinks about what happens when this fails unattended.
7. **Testing discipline** — tests that would actually catch a regression, not tests written to make coverage numbers look good.
8. **Communicates tradeoffs** — states the reasoning behind a choice (database, architecture, scope) so a non-specialist stakeholder can make an informed call, rather than presenting a decision as the only option.

## Failure-mode questions worth asking (select relevant ones only)

- What happens if this operation is interrupted halfway through (partial write, network failure)?
- What happens if this endpoint receives 10x the expected traffic in a burst?
- Who/what is notified if this background job silently stops running?
- If this migration goes wrong in production, how long does recovery actually take, and has that been tested or only assumed?
- Does this change assume the database is always reachable, always fast, always consistent — and what happens on the day it isn't?
- If this data is deleted by mistake tomorrow, is there an actual tested path to get it back, or only a belief that backups exist?

## Anti-patterns to flag

- A migration with no rollback, justified as "we'll just fix it forward."
- A backup strategy that has never been restore-tested.
- Business logic directly calling a platform-specific SDK deep inside otherwise-portable code.
- Choosing a database for the traffic you might have in three years instead of the traffic you have now.
- Treating a passing test suite as equivalent to production readiness.
- Security checks planned as a "later" pass rather than part of the implementation itself.
