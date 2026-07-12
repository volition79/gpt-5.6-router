# Two-Gate Approval Protocol

## States

- `NO_SELECTION`: router is active but no optimization profile is selected.
- `DISCOVERY_APPROVED`: the user selected a profile and approved the displayed read-only discovery.
- `DISCOVERING`: only approved read-only evidence gathering is running.
- `AWAITING_EXECUTION_APPROVAL`: the adaptive route is visible and no implementation agent or write action has started.
- `EXECUTING`: the explicitly approved route is running.
- `REAPPROVAL_REQUIRED`: a material route change is necessary and work is paused at a safe boundary.
- `COMPLETED`: approved execution and validation are integrated.
- `CANCELLED`: the user rejected or cancelled the flow.

Profile selection authorizes only the displayed read-only discovery. It never authorizes implementation or external actions.

## Gate 1 Requirements

Show all three profiles, recommend `BALANCED`, provide a task-specific directional tradeoff, and state the exact read-only evidence surfaces to inspect. Use structured user input only when the tool is explicitly available and the active mode permits it. In Default mode, use numbered text choices without attempting the tool.

## Gate 2 Requirements

Show the recommended adaptive route, parent-model assumption, stage assignments, permissions, validation, Sol-direct comparison, directional quality/time/token effects, confidence, and separate approvals. Only explicit approval of this route starts execution.

## Reapproval Triggers

Pause before adding or substituting a model or role, widening scope, accessing a new sensitive surface, changing read-only work to writes, changing order in a risk-significant way, accepting materially higher cost or latency, or performing external/destructive/account/deployment actions.

Do not require reapproval for hypotheses, file choices, implementation tactics, or validation refinements inside the approved scope, permissions, risk, and cost envelope.

On model unavailability, do not silently downgrade. Show the substitute and changed tradeoff, then wait.
