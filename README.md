# Recursive Invariant Discovery Model

RIDM is an evidence-bound architecture for adaptive reasoning and action. It
governs how a system interprets a task, finds the nearest sufficient invariant,
classifies material residuals, acts within authority, learns from observations,
and stops with a verifiable result.

The active specification is [RIDM 11.0](RIDM.MD).

## Primary Question

> What is the minimum grounded and authorized structure required for this user
> to believe, predict, decide, or act safely and correctly, and what observation
> will prove that the task is complete?

## Core Principles

- Establish the task contract before deep refinement.
- Ground every decisive material claim.
- Treat authority, safety, privacy, evidence, and irreversible harm as hard
  gates that soft benefits cannot offset.
- Select the nearest sufficient invariant instead of pursuing depth for its own
  sake.
- Prefer low-risk, reversible actions with observable outcomes.
- Recompute materiality when evidence, state, authority, or stakes change.
- Report completion only when success criteria are directly validated.
- Expose the material delta and suppress detail that cannot change the result.

## RIDM 11.0 Architecture

```text
Task request
  -> Task contract
  -> Authority envelope
  -> Evidence ledger
  -> Proof-carrying interpretations
  -> Nearest sufficient invariant
  -> Materiality graph
  -> Non-compensable gates
  -> Minimum sufficient decision
  -> Action admission
  -> Action and observation
  -> Materiality reclassification
  -> Output contract
  -> Completion certificate
  -> Feedback reopening
```

The complete definitions, control laws, evaluation criteria, and reference
procedure are in [RIDM.MD](RIDM.MD).

## What RIDM Is For

RIDM can guide:

- reasoning systems that must distinguish material from merely valid detail
- agents that inspect, modify, or communicate through tools
- decision support under uncertainty and changing evidence
- evaluation of grounding, authority compliance, stopping, and disclosure
- human review of reasoning and action policies

RIDM is a specification, not an executable library. It does not require private
chain-of-thought disclosure, grant authority, or replace domain-specific safety,
legal, or professional requirements.

## Repository Layout

| Path | Purpose |
| --- | --- |
| [RIDM.MD](RIDM.MD) | Active RIDM specification |
| [AGENTS.md](AGENTS.md) | Repository instructions for coding agents |
| [README.md](README.md) | Project overview and navigation |
| [LICENSE](LICENSE) | MIT license |

## Contributing

Keep changes focused and evidence-bound. Preserve the specification's heading
and section structure, update affected cross-references, and validate the exact
surface that changed. Repository-specific instructions are in
[AGENTS.md](AGENTS.md).

Before presenting a change:

1. Review the full diff.
2. Run `git diff --check`.
3. Verify headings, numbered sections, code fences, math delimiters, and links.
4. Confirm that files are UTF-8 without a byte-order mark and use LF endings.
5. Report any skipped check or unresolved material risk.

## License

RIDM is available under the [MIT License](LICENSE).
