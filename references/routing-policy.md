# Adaptive Routing Policy

## Capability Floors

Choose the lowest-cost model that meets the stage's required capability and consequence level.

| Stage characteristic | Default floor | Escalate when |
|---|---|---|
| Deterministic extraction or bulk transformation | Luna | ambiguity, anomalies, or non-deterministic acceptance |
| Read-heavy exploration or ordinary implementation | Terra | architecture, conflicting evidence, or high consequence |
| Test construction and behavioral verification | Terra | adversarial or release-critical judgment is required |
| Product, UX/UI, visual, interaction, motion, art direction, or subjective design acceptance | Sol | remain on Sol |
| Architecture, ambiguous planning, security, destructive policy, final high-risk acceptance | Sol | remain on Sol |

These are defaults, not keyword rules. Consider ambiguity, consequence, breadth, context size, independence, repetition, evidence quality, and verification burden together.

## Parent-Model Awareness

The parent always owns orchestration and final integration.

- Parent Sol: use the parent for planning and final judgment. Do not spawn `sol_planner` merely to repeat that work. Use Terra or Luna for justified execution stages; add a Sol reviewer only for valuable independence.
- Parent Terra: use the parent for ordinary exploration, implementation, and integration. Add Sol for every meaningful design stage and its subjective acceptance, plus high-consequence review; use Luna for deterministic volume.
- Parent Luna: keep the parent to coordination of explicit contracts. Delegate every meaningful design stage and its subjective acceptance to Sol; delegate other non-deterministic analysis and final judgment to Terra or Sol.
- Parent unknown: do not claim duplicate-role savings. Use the smallest conservative route and state the uncertainty.

## Design Ownership Invariant

For programs, products, apps, games, websites, and user-facing tools, explicitly detect the design surface before routing implementation.

- Sol owns product/experience direction, information architecture, UX/UI, visual language, interaction and motion behavior, art direction, design systems, and subjective design acceptance.
- Terra may translate an approved Sol design contract into code and perform objective checks such as viewport, contrast, overlap, state, and screenshot capture.
- Material design deviations discovered during implementation return to Sol. Terra must not silently resolve them as design decisions.
- If the parent is Sol, count the parent as the design owner instead of spawning a duplicate Sol planner. If the parent is not reliably Sol, include a Sol design role.
- The invariant applies to every profile. TOKEN_SAVER may narrow the Sol context packet and omit duplicate Sol review when the same Sol owner can judge the final evidence, but it may not substitute Terra or Luna for design.

## Creative Freedom Floor

Sol ownership is a quality floor, not a requirement to freeze a solution before implementation.

- Specify design contracts through intent, audience, principles, constraints, creative range, and outcome-based acceptance. Avoid exact visual prescriptions unless fidelity, regulation, or the user requires them.
- On open-ended design surfaces, compare at least two structurally distinct concepts before choosing a direction when the comparison repays its cost. TOKEN_SAVER may keep the comparison terse, but it must not turn a creative task into the first generic answer.
- Give Terra an explicit `creative latitude` field covering which composition, interaction, motion, responsive, and implementation-level choices it may refine.
- Treat in-contract, reversible improvements as implementation tactics. Terra may apply and report them without reapproval.
- Treat material direction changes as proposals for Sol. Preserve the idea and evidence; do not silently reject or adopt it.
- Let Sol update its initial judgment after seeing working implementation evidence. Final acceptance measures outcome quality and originality, not obedience to the first draft.

## Profiles

### PERFORMANCE

Prioritize correctness, depth, creative breadth, and independent evidence. Use parallel agents only for independent lanes. Preserve Sol design ownership, compare meaningfully different concepts for open-ended work, and add an independent Sol design review when visual or experiential quality materially benefits from independence. Add an independent Sol review for high-consequence work when it materially improves confidence. More tokens or time are acceptable only when disclosed and justified.

### BALANCED

Default profile. Use the Sol parent or one Sol role for meaningful design, one Terra for most ordinary execution, and Luna only when deterministic volume repays setup and validation. Preserve bounded Terra creative latitude and return final subjective design evidence plus emergent ideas to the Sol owner without adding a duplicate reviewer unless independence has clear value. Escalate selectively. Avoid overlapping agents and full-context duplication.

### TOKEN_SAVER

Minimize calls, duplicated context, and non-required Sol work. Prefer one Terra end-to-end only when the task has no meaningful design surface and meets the quality floor. For design-bearing work, use the narrowest sufficient outcome-based Sol design contract, retain meaningful creative latitude, and return concise implementation evidence and emergent ideas to the same Sol owner for acceptance. Use Luna for sufficiently large deterministic batches. Never reduce required design, creative freedom, safety, or acceptance criteria.

## Sol-Direct Guard

Sol direct is always a valid fallback. Recommend it when work is small, tightly coupled, context-heavy, or difficult to partition; when delegation would repeat the parent's work; or when the selected profile has no credible advantage without an unacceptable regression.

This guard prevents knowingly poor routing but cannot guarantee runtime, token, or quality superiority.

## Escalation

Escalate Luna -> Terra -> Sol when evidence conflicts, assumptions fail, validators reject output, consequence rises, or scope changes. Material escalation pauses execution for reapproval; ordinary tactical handling inside the approved envelope does not.
