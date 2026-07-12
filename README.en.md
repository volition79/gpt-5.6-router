# GPT-5.6 Model Router

[한국어](README.md)

A Codex skill that assigns work stages to GPT-5.6 Sol, Terra, and Luna according to their strengths. The user selects `PERFORMANCE`, `BALANCED`, or `TOKEN_SAVER`; the skill separates read-only discovery from execution approval and then proposes an adaptive model route.

This skill activates **only when explicitly invoked**.

## Highlights

- Two approval gates: profile selection and execution approval are separate
- Parent-model-aware routing that avoids duplicate work
- Sol: architecture, difficult judgment, product design, UX/UI, visual design, interaction, motion, and art direction
- Terra: exploration, general implementation, testing, and evidence synthesis
- Luna: deterministic repetition, extraction, and transformation
- Sol owns design direction and final subjective design acceptance
- A Sol design draft is not treated as an immutable specification
- Terra can improve composition, motion, responsive behavior, and microinteractions within the approved intent
- Runtime troubleshooting for missing role or model overrides

## Requirements

- A Codex environment that can discover skills
- A multi-agent runtime that can pin GPT-5.6 Sol, Terra, and Luna
- `git` for installation
- Python 3 and PyYAML for optional skill validation

If model pinning is unavailable, the skill stops instead of silently substituting another model.

## Installation

### Install globally for a Codex user

Run:

```bash
git clone https://github.com/volition79/gpt-5.6-router.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/gpt56-model-router"
```

If it is already installed, inspect local changes before updating:

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/gpt56-model-router" status --short
git -C "${CODEX_HOME:-$HOME/.codex}/skills/gpt56-model-router" pull --ff-only
```

Start a new Codex conversation or session after installation. The skill should appear as `gpt56-model-router`.

### Self-installation instructions for an AI agent

An AI inspecting this repository should:

1. Inspect `SKILL.md` and `agents/openai.yaml` at the repository root.
2. Use `$CODEX_HOME/skills/gpt56-model-router` when `CODEX_HOME` exists; otherwise use `~/.codex/skills/gpt56-model-router`.
3. Clone the repository directly to that path when the target does not exist.
4. When the target exists, inspect local changes first and never overwrite user files. Use `git pull --ff-only` only when safe.
5. Verify that `SKILL.md`, `agents/`, `references/`, and `assets/` exist.
6. Run the validation command below when the validator is available.
7. Tell the user to start a new session and invoke the skill explicitly.

Example instruction for an AI:

> Inspect this repository and install it as the user-global Codex skill `gpt56-model-router`. If an installation already exists, inspect its changes first and do not overwrite user files. Never print credentials or write them to the repository.

## Validation

When the Codex `skill-creator` validator is available, run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" \
  "${CODEX_HOME:-$HOME/.codex}/skills/gpt56-model-router"
```

If this reports `ModuleNotFoundError: No module named 'yaml'`, rerun it in a Python environment with PyYAML installed.

## Usage

The skill does not run implicitly. Invoke it in the prompt:

```text
Use $gpt56-model-router to build a polished analytics dashboard.
```

### Workflow

1. The skill presents three profiles with task-specific tradeoffs.
2. The user selects a profile. `BALANCED` is recommended by default.
3. The skill performs only the approved minimum read-only discovery.
4. It proposes an execution route with models, roles, order, permissions, deliverables, and validation.
5. The user explicitly approves the route.
6. Only the approved models and roles execute.
7. The parent agent integrates the results and validation evidence.

Selecting a profile authorizes read-only discovery only. File edits, deployment, and external actions begin only after the separate execution approval.

## Profiles

| Profile | Priority |
|---|---|
| `PERFORMANCE` | Maximize quality, depth, and independent validation |
| `BALANCED` | Preserve required quality while reducing duplicated calls and context |
| `TOKEN_SAVER` | Minimize calls and context without lowering mandatory quality floors |

All profiles preserve the Sol design floor for design-bearing program work. `TOKEN_SAVER` does not substitute Terra or Luna for design.

## Design and creative freedom

A typical route for design-bearing work is:

```text
Sol design exploration and direction
  → Terra implementation and objective UI validation
  → Sol outcome-based design acceptance
  → Parent integration
```

Sol defines intent, audience, emotional target, experience principles, constraints, and quality outcomes without freezing the solution too early. For open-ended work, it compares structurally distinct directions when the comparison is worth the cost.

Terra can refine implementation and expression within the approved design intent. Promising emergent ideas are preserved as applied in-contract improvements or material direction-change proposals for Sol.

Final design acceptance evaluates clarity, coherence, usability, emotional fit, distinctiveness, and craft rather than literal conformity to the first draft.

## Repository layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── routing-plan-template.md
└── references/
    ├── approval-protocol.md
    ├── evaluation.md
    ├── execution-playbooks.md
    ├── routing-policy.md
    └── runtime-troubleshooting.md
```

See [SKILL.md](SKILL.md) for the core workflow, [routing-policy.md](references/routing-policy.md) for capability floors, and [execution-playbooks.md](references/execution-playbooks.md) for handoffs.

## Security principles

- Routing approval never bypasses normal permission or deployment approval.
- Never silently substitute an unavailable model.
- Never weaken the active sandbox or approval policy.
- Never write secrets into plans, handoffs, logs, or the repository.
- External and destructive actions remain separately approval-gated.
