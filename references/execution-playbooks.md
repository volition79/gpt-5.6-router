# Adaptive Execution Playbooks

## Stage Graph

Represent only meaningful stages and dependencies. Collapse tightly coupled stages into one agent. Split independent evidence lanes or disjoint write sets when parallelism has clear value.

## Handoff Contract

Each subagent receives the approved stage, explicit non-goals, allowed write surface, evidence packet, quality threshold, validation, output shape, and instruction not to spawn descendants. Do not send the full conversation when a compact contract is sufficient.

For design-bearing program work, the Sol design contract must state the intended experience, information hierarchy, visual system, interaction and motion principles, responsive behavior, outcome-based acceptance rubric, and a `creative latitude` section defining which choices Terra may refine. Prefer principles and ranges over premature pixel prescriptions. Terra returns screenshots, interaction evidence, objective checks, applied in-contract improvements, emergent ideas, and material deviation proposals to the Sol owner for subjective acceptance.

When the design is open-ended and comparison is worthwhile, the Sol handoff must record the distinct concepts considered, why the selected direction is strongest, and which unused ideas remain available. The final Sol pass must be willing to revise the initial contract when the working result demonstrates a stronger solution.

## Runtime Role Adapter

Prefer `sol_planner`, `sol_executor`, `sol_reviewer`, `sol_critical_reviewer`, `terra_explorer`, `terra_builder`, `terra_verifier`, `luna_extractor`, or `luna_worker` when the runtime exposes installed custom roles.

If it exposes only built-in roles, map read-only work to `explorer`, implementation to `worker`, and other bounded work to `default`; pin the approved `gpt-5.6-sol`, `gpt-5.6-terra`, or `gpt-5.6-luna` model and approved reasoning effort, then include the custom role contract in the task prompt. Do not change the model, permission, scope, or quality floor. If model pinning is unavailable, stop rather than pretending routing occurred.

## Common Routes

- Parent Sol -> Terra build/test -> parent integration: balanced implementation.
- Parent Sol design contract -> Terra implementation/objective UI checks -> parent Sol design acceptance: balanced program or product build.
- Parent Terra/unknown -> Sol design contract -> Terra implementation/objective UI checks -> same Sol owner design acceptance -> parent integration: design-bearing build when the parent is not reliably Sol.
- Parent Sol -> parallel Terra evidence lanes -> parent decision: independent research with reduced Sol reading.
- Parent Sol -> Luna batch -> Terra anomaly review -> parent acceptance: deterministic volume.
- Parent Terra -> Sol architecture or high-consequence contract -> parent/Terra implementation -> Sol review: high-consequence non-design work when parent is not Sol.
- Sol direct: small, context-heavy, or tightly coupled work.

These are examples, not mandatory patterns.

## Independent Review

Use a reviewer that did not implement the change when independence matters. Provide the approved contract, actual result, and test evidence. Do not add review solely to make the team look comprehensive.

Sol subjective design acceptance is required for meaningful design surfaces even when an independent reviewer is not. Acceptance evaluates clarity, coherence, usability, emotional fit, distinctiveness, and craft rather than literal conformity to the first draft. The original Sol design owner may perform that acceptance in BALANCED or TOKEN_SAVER; PERFORMANCE may add an independent Sol reviewer when the expected quality gain justifies it.

## Escalation

An agent reports ambiguity or failed validation instead of improvising outside its capability floor. The parent decides whether the escalation fits the approved envelope or requires reapproval.

## Completion

The parent compares the approved and actual routes, resolves contradictions, checks evidence, and reports observed metrics only when available. Never convert estimates into claimed measurements.
