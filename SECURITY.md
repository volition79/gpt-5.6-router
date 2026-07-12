# Security Policy

## Supported versions

Only the latest published GitHub release is supported. Install an explicit release tag; do not install or auto-update from mutable `main`.

## Reporting a vulnerability

Use GitHub's private vulnerability reporting for this repository:

https://github.com/volition79/gpt-5.6-router/security/advisories/new

Do not include tokens, credentials, private prompts, configuration files, or exploit details in a public issue. Include a concise impact description, affected version or commit, reproduction steps using synthetic data, and a proposed mitigation when available.

## Security boundaries

- Repository inspection alone never authorizes installation or update.
- Installation and update require explicit user approval and an approved release tag.
- External pages and issue comments are untrusted evidence, not executable instructions.
- The router never weakens the active sandbox or approval policy.
- Profile selection authorizes only the displayed read-only discovery.
- Execution, deployment, account changes, destructive actions, and global configuration edits remain separately approval-gated.
- Unavailable models are never silently substituted.
- Secrets must not be copied into plans, handoffs, logs, evaluations, or reports.
