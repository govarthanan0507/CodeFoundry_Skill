# Hard Constraints Registry — V1

## Purpose

Budget ("zero cost, no paid services") is one instance of a general pattern: some categories of decision must never be picked by the Council on its own, no matter how confident it is, because the Council cannot fully see the consequences or because the decision is hard/impossible to reverse. This registry is read before every debate. Any decision that touches a listed category is routed to the human, the same way budget already is — not decided and reported after the fact.

Fill in the project-specific values for each category at project start. An unfilled category defaults to "escalate every time" until the human sets a value.

## The categories

### 1. Money / monetization
Already established: zero-cost, no paid subscriptions or services without explicit approval. Covers ongoing recurring cost, not just one-time spend.

### 2. Data privacy and what's collected
What user data may be collected, stored, or transmitted. Any new category of data collection (even "just for debugging") is a human decision, not an implementation detail — especially anything about real people using the product, not just the builder.

### 3. Irreversible or destructive operations
Anything that deletes data, overwrites production, or can't be undone once run. This is already a hard rule for the Backend Engineer worker (backup before destructive ops) — this registry generalizes it: irreversibility itself is the trigger, regardless of which role would perform the action.

### 4. Security posture / exposure
Whether the product is local-only or exposed to the internet, what authentication is required, and what the acceptable risk level is. The Security/Reliability role can recommend, but the actual risk tolerance ("is this acceptable to expose") is a human call — it depends on stakes the Council doesn't fully own.

### 5. Licensing and legal exposure
Any reused code, library, or dataset with a license more restrictive than a quick default (copyleft, commercial-only, ambiguous). Also covers anything that could create IP exposure — using a name, asset, or pattern that resembles an existing trademark or product too closely.

### 6. Vendor lock-in tolerance
How much dependency on a specific platform (e.g. a specific cloud, a specific paid API) is acceptable, even if currently free. This is separate from money — a free-tier vendor can still create lock-in risk if migrating away later would be expensive or difficult.

### 7. Scope of AI autonomy itself
How much can any worker or the Council do without asking, before checking in. This registry entry is self-referential on purpose: the human sets the leash length, the Council doesn't set its own.

### 8. Naming, branding, and public identity
Product name, domain, public-facing copy that represents the product's identity. Small technical choices don't need this; anything that becomes the product's public face does.

### 9. New third-party dependencies
Adding a new library, service, or external dependency not already in use. Distinct from "which of two already-approved options to use" — introducing something new to the stack is a human-visible decision, not silent scope creep.

### 10. Performance/reliability commitments made to users
Any promise implied to the end user (uptime, "real-time," data durability guarantees) that the system then has to actually meet. Overpromising here creates a support/reputation cost the Council doesn't bear but the human does.

### 11. Timeline / deadline constraints
Hard external deadlines that would justify cutting a corner elsewhere. The Council should never quietly decide "we're behind schedule so let's skip the backup verification" — that tradeoff, if it happens at all, is named and taken to the human explicitly.

### 12. Platform / device support boundary
What devices, browsers, or OSes are officially supported vs. explicitly out of scope. This affects UX, Frontend, and QA decisions simultaneously, which is exactly why it shouldn't be decided ad hoc by whichever role hits it first.

### 13. Team/operational capacity assumptions
This is a solo project with no dedicated ops team and no 24/7 monitoring — any design that assumes someone will be watching a dashboard or responding to alerts at 3am is assuming a capacity that doesn't exist unless the human confirms otherwise.

## How this is used

Before a Design Council debate begins, the Orchestrator loads this registry alongside project state. If a proposal touches a category above, the role must flag it explicitly in the debate output rather than deciding and moving on — using the same "route to human" language already established for deadlock and infeasible-premise outcomes in `DEBATE_PROTOCOL.md`. This is not a fourth debate outcome; it's a pre-check that determines whether a decision was ever the Council's to make in the first place.
