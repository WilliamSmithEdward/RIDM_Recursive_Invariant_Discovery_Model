# Recursive Invariant Discovery Model

RIDM is an evidence-bound architecture for adaptive reasoning and action. It
governs how a system interprets a task, finds the nearest sufficient invariant,
classifies material residuals, acts within authority, learns from observations,
and stops with a verifiable result.

## Primary Question

> What is the minimum grounded and authorized structure required for this user
> to believe, predict, decide, or act safely and correctly, and what observation
> will prove that the task is complete?

## Core Principles

- Establish the task contract before deep refinement, and ground every decisive material
  claim.
- Treat authority, safety, privacy, evidence, and irreversible harm as hard gates that
  soft benefits cannot offset; prefer low-risk, reversible actions with observable
  outcomes.
- Cover the space before ranking: candidates, frames, mechanisms, extent rungs, the null,
  what the state holds, what the task grants, and the reasoner's own recall variants and
  near-neighbors. A perfect ranking of an incomplete set is a miss, and nothing the
  first pass generated is dropped unprobed.
- Observe what the task points at, down to its introduced symbols and counted givens,
  and keep the givens exact, complete, and inviolate.
- Treat memory as a fallible witness: recall carries its parameterization, contrast, and
  level; conflicting variants rank by anchor authority; famous-neighbor agreement is
  contamination, not corroboration.
- Treat selection as evidence: condition on the process that produced what you see, from
  filtered pools to harvested option clusters.
- Model every artifact's author: rigor from structure, canon from provenance, options
  from idiolect, and the criterion as the author's implementation, defects included.
- Derive first and keep what derivation wins; engineered details select among completed
  routes.
- Let the canonical reading lead and resolve every selection layer blind; coincidence,
  elegance, and a choice's effect on the ranking never select, and every rule that fires
  has its verdict reconciled before commitment.
- Treat the frame as a candidate, refuted by givens it cannot represent.
- Move nothing without typed evidence at matching scope, and discharge or bind every
  noticed alarm.
- Price confidence at the audited weakest decisive link, against instrument noise and
  the referent's predictable defects.
- Commit before consulting any oracle, enforce the order in the mechanism, and check a
  verdict for consistency and for membership in the answer's value class before updating;
  commit one answer under scoped representations that name one object.
- Recompute materiality when evidence, state, authority, or stakes change; report
  completion only when success criteria are directly validated; expose the material
  delta and suppress detail that cannot change the result.

## RIDM 30 Architecture

```text
Task request
  -> Task contract and authority envelope
  -> Provenance, rigor, author, and canon
  -> Selection-process consumption: pool filters, harvested clusters, menu architecture
  -> Frame selection with representability audit and load-bearingness
  -> Census: standing structures, granted capabilities, flagged observables
  -> Direct measurement where the asked relation permits, instruments anchored first
  -> Rigorous routes, refuted-model quarantine, referent basis by designed detail
  -> Predictable referent variants and the answer's value class computed pre-reveal
  -> Evidence ledger with recall-layer coverage
  -> Candidate coverage with constructed keying readings
  -> Typed ranking under canonical precedence
  -> Nearest sufficient invariant and materiality graph
  -> Non-compensable gates
  -> Verdict ledger: every fired rule reconciled
  -> Trigger-indexed commitment gate
  -> Scoped representation forks in the output
  -> Action admission and interlocked oracle sequencing
  -> Observation, oracle discipline, materiality reclassification
  -> Output contract and completion certificate
  -> Feedback reopening
```

The complete definitions, control laws, evaluation criteria, and reference
procedure are in [RIDM.MD](RIDM.MD). Guidance for building the framework is in
[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md).

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
| [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) | Software implementation and conformance guide |
| [hle/](hle/) | Evaluation run logs and per-sprint lessons, content-free |
| [AGENTS.md](AGENTS.md) | Repository instructions for coding agents |
| [README.md](README.md) | Project overview and navigation |
| [LICENSE](LICENSE) | MIT license |

## Contributing

Keep changes focused and evidence-bound. Preserve the specification's heading
and section structure, update affected cross-references, and validate the exact
surface that changed. Repository-specific instructions are in
[AGENTS.md](AGENTS.md). Implementation work should also follow
[IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md).

Before presenting a change:

1. Review the full diff.
2. Run `git diff --check`.
3. Verify headings, numbered sections, code fences, math delimiters, and links.
4. Confirm that files are UTF-8 without a byte-order mark and use LF endings.
5. Report any skipped check or unresolved material risk.

## License

RIDM is available under the [MIT License](LICENSE).
