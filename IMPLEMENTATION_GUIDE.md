# RIDM Implementation Guide

This guide translates [RIDM 11.0](RIDM.MD) into software boundaries, data
contracts, control flow, tests, and delivery phases. It is written for agents
and engineers implementing RIDM in any language or runtime.

## 1. Purpose

Use this guide to build a RIDM implementation that is:

- evidence-bound rather than assertion-driven
- constrained by explicit authority
- dynamic under new observations
- safe around state-changing actions
- testable at every decision boundary
- honest about completion and unresolved limits

This guide does not replace the specification. If it conflicts with
[RIDM.MD](RIDM.MD), the specification controls.

## 2. Implementation Targets

Use one of these labels when describing implementation coverage.

| Target | Required capabilities |
| --- | --- |
| RIDM Reasoning Core | Task contract, evidence ledger, interpretations, invariant selection, materiality graph, hard gates, and output contract |
| RIDM Action Runtime | Reasoning Core plus authority enforcement, action admission, execution adapters, observations, and recovery |
| RIDM 11 Conformant | Action Runtime plus reopening, completion certificates, privacy controls, evaluation metrics, and conformance tests |

Do not describe a partial implementation as RIDM 11 conformant. State the
implemented target and any omitted capability.

## 3. Required Reading

Before implementation:

1. Read [RIDM.MD](RIDM.MD) completely.
2. Read [AGENTS.md](AGENTS.md) for repository rules.
3. Identify the intended runtime, action surface, trust boundaries, and risk
   profile.
4. Define observable acceptance criteria before choosing storage, orchestration,
   or model providers.

## Part I: Architecture

### 4. Recommended Components

Keep domain decisions separate from I/O and provider-specific mechanics.

#### Task contract builder

Input: user request, context, constraints, and available authority.

Output: a normalized `TaskContract` or a focused clarification request.

It must not infer broader permission from available capabilities.

#### Evidence ledger

Input: observations, sources, validations, and claim updates.

Output: linked `EvidenceRecord` and `ClaimRecord` entries with support states.

It must preserve provenance and must not convert reported claims into observed
facts.

#### Interpretation builder

Input: task contract and evidence ledger.

Output: bounded proof-carrying interpretations.

It must stop generating alternatives when remaining readings cannot change the
task.

#### Invariant selector

Input: candidate models and the materiality graph.

Output: the nearest sufficient invariant and its scope.

It must not reward depth that adds no material coverage.

#### Materiality engine

Input: claims, residuals, dependencies, actions, observations, and task state.

Output: a dependency-aware `MaterialityGraph`.

It must support partial recomputation after a changed observation.

#### Gate evaluator

Input: task contract, evidence ledger, materiality graph, and optional action.

Output: individual hard-gate results and available resolution paths.

It must not collapse hard gates into a compensable scalar score.

#### Decision engine

Input: nearest sufficient invariant, material residuals, gate results, and
requested output.

Output: the minimum sufficient decision and disclosure level.

#### Action admission service

Input: `ActionCandidate`, authority envelope, evidence, and risk profile.

Output: admit, deny, or needs-confirmation with a reason and evidence.

#### Executor adapter

Input: an admitted action.

Output: a direct result and enough state to construct an `Observation`.

It must enforce the admitted scope independently when the runtime supports it.

#### Observation processor

Input: action result, status, changed resources, and validation results.

Output: evidence updates and affected materiality nodes.

#### Completion evaluator

Input: task contract, output contract, evidence ledger, materiality graph, and
validation results.

Output: a `CompletionCertificate` with a literal completion state.

#### Output compiler

Input: decision, disclosure level, evidence summary, validation, and completion
certificate.

Output: the minimum sufficient user-facing report.

It must not expose private chain-of-thought or omit material limits.

### 5. Dependency Direction

Use this dependency direction:

```text
Domain contracts and policies
  <- Pure reasoning services
  <- Orchestrator
  <- Ports
  <- Provider, storage, tool, and UI adapters
```

The domain core must not import tool SDKs, model clients, databases, UI code, or
network libraries. Adapters depend on domain contracts, not the reverse.

### 6. Engine State

Keep the active task state explicit.

```text
RIDMState {
    task_contract
    evidence_ledger
    interpretations[]
    candidate_models[]
    selected_invariant
    materiality_graph
    gate_results[]
    decision
    action_history[]
    observation_history[]
    completion_certificate
    attempts_remaining
}
```

Prefer immutable snapshots or append-only transitions. If mutable state is
required, serialize updates and make compound transitions atomic.

### 7. State Machine

Model lifecycle states directly.

```text
received
  -> contracted
  -> grounded
  -> modeled
  -> gated
  -> decided
  -> admitted
  -> acted
  -> observed
  -> validated
  -> complete
```

Allowed terminal or waiting branches:

```text
needs_clarification
blocked
refused
monitoring
complete_with_limits
```

Reject invalid transitions. In particular:

- no action before admission
- no admission before hard gates pass
- no complete state before direct validation
- no silent transition from failed validation to complete

## Part II: Domain Contracts

### 8. Contract Design Rules

- Give every record a stable task-scoped identifier when it participates in
  references or history.
- Make required fields explicit and reject incomplete high-risk records.
- Use enums or tagged unions for closed states.
- Preserve unknown as a real state instead of using null as false certainty.
- Include scope and timestamps where freshness or applicability can change.
- Record the evidence or authority basis for material state transitions.
- Version persisted schemas independently from the RIDM document version.

### 9. Task Contract

The implementation must represent at least:

```text
TaskContract {
    task_id
    objective
    requested_output
    scope
    success_criteria[]
    requested_depth
    constraints[]
    prohibited_outcomes[]
    stakes
    time_horizon
    authority_envelope
}
```

Validate the task contract before expensive reasoning or any state-changing
action. A missing field may remain unknown only when it cannot change the
result.

### 10. Evidence and Claims

Store evidence separately from claims.

```text
EvidenceRecord {
    evidence_id
    source
    observation
    provenance
    acquired_at
    applicable_scope
    trust_boundary
    integrity_state
}

ClaimRecord {
    claim_id
    proposition
    claim_type
    support_refs[]
    scope
    assumptions[]
    freshness
    confidence
    conflicts[]
    support_state
}
```

Recommended rules:

- Evidence records are append-only.
- Claim support state changes create an auditable transition.
- A claim cannot reference missing evidence.
- Refuted and contested claims remain visible while material.
- Sensitive evidence is stored by reference when content retention is not
  required.
- Logs identify record IDs, not secret or personal content.

### 11. Interpretations and Invariants

```text
Interpretation {
    interpretation_id
    meaning
    supporting_claims[]
    assumptions[]
    alternatives[]
    task_consequences[]
    confidence
}

InvariantSelection {
    invariant_id
    candidate
    scope
    explanatory_coverage
    material_residuals_covered[]
    unsupported_assumptions[]
    depth_cost
}
```

The selector should be a pure function over candidate models and materiality
state whenever practical. Persist the selected scope and invalidation triggers.

### 12. Materiality Graph

Represent residual dependencies explicitly.

```text
ResidualNode {
    residual_id
    description
    affected_claims[]
    affected_actions[]
    dependencies[]
    dependents[]
    current_materiality
    status
    reopening_triggers[]
}
```

Implementation requirements:

- Detect or reject dependency cycles unless the graph algorithm supports them.
- Recompute downstream nodes after an upstream change.
- Preserve the prior classification when it is useful for auditing.
- Store only a minimal reopening index for suppressed residuals.
- Remove or anonymize residual content when its retention condition expires.

### 13. Gate Results

Evaluate each hard gate independently.

```text
GateResult {
    gate
    status: pass | fail | needs_input
    reason_code
    evidence_refs[]
    authority_refs[]
    resolution_paths[]
}
```

Required gates:

- authority
- irreversible harm and safety
- decisive evidence and truth conflict
- privacy and security
- success-criterion feasibility

Keep individual results. An aggregate `all_passed` value may be derived, but no
weighted score may convert a failed hard gate into a pass.

### 14. Actions and Observations

```text
ActionCandidate {
    action_id
    purpose
    expected_effect
    preconditions[]
    required_authority[]
    risk_profile
    blast_radius
    reversibility
    validation_plan
    rollback_plan
    observability
}

Observation {
    observation_id
    action_id
    direct_result
    exit_or_status_state
    changed_resources[]
    expected_effect_observed
    unexpected_effects[]
    evidence_updates[]
    materiality_updates[]
}
```

An executor result is not itself an observation contract. The observation
processor must compare expected and actual state.

### 15. Completion Certificate

```text
CompletionCertificate {
    task_contract_satisfied
    success_criteria_results[]
    material_claims_supported
    authorized_actions_only
    validation_results[]
    unresolved_material_residuals[]
    remaining_risks[]
    skipped_checks[]
    completion_status
    reopening_triggers[]
}
```

Permit `complete` only when every required success criterion is verified and no
unresolved material residual can change the result.

## Part III: Control Flow

### 16. Orchestrator Contract

The orchestrator coordinates pure services and side-effecting ports. It should
not reimplement domain policy.

```text
function run_ridm(request, context, constraints):

    state = initialize_state(request, context, constraints)
    state.task_contract = build_task_contract(state)

    if state.task_contract has material ambiguity:
        return needs_clarification(state)

    state.evidence_ledger = build_evidence_ledger(state)
    state.interpretations = build_interpretations(state)
    state.candidate_models = build_candidate_models(state)
    state.materiality_graph = build_materiality_graph(state)
    state.attempts_remaining = max(1, bounded_attempt_budget(state))

    while state.attempts_remaining > 0:

        state.selected_invariant = select_nearest_invariant(state)
        state.gate_results = evaluate_hard_gates(state)

        if any hard gate cannot be resolved:
            return accurate_noncomplete_result(state)

        state.decision = select_minimum_sufficient_decision(state)

        if state.decision requires action:
            candidate = build_action_candidate(state)
            admission = admit_action(candidate, state.task_contract)

            if admission is not admitted:
                return accurate_noncomplete_result(state, admission)

            result = executor.execute(candidate)
            observation = observe(candidate, result)
            state = apply_observation(state, observation)

        output = compile_output_contract(state)
        certificate = evaluate_completion(state, output)

        if certificate is valid:
            return finalize(output, certificate)

        state.attempts_remaining -= 1

        if state.attempts_remaining == 0:
            return accurate_noncomplete_result(
                state,
                reason = budget_exhausted
            )

        if no new evidence or changed hypothesis exists:
            return accurate_noncomplete_result(state, certificate)

        state = reopen_smallest_affected_boundary(state, certificate)

    return accurate_noncomplete_result(state, reason = budget_exhausted)
```

### 17. Hard Gates Before Soft Value

Implement the decision order directly:

1. Establish task and authority.
2. Evaluate all hard gates.
3. Resolve, clarify, deny, or refuse failed gates.
4. Select among actions that passed.
5. Apply soft benefit-versus-cost comparison only to admissible options.

Do not implement one scoring function that includes both hard constraints and
soft preferences.

### 18. Bounded Candidate Generation

Bound:

- interpretation count
- invariant depth
- evidence retrieval attempts
- action attempts
- retry count and delay
- materiality graph size
- reopening count
- memory retained per task

When a bound is reached, return a literal status with the unresolved material
item. Do not silently truncate and report completion.

### 19. Reopening

Reopening should update only affected layers.

```text
ReopeningPlan {
    trigger
    affected_claims[]
    affected_residuals[]
    affected_decisions[]
    layers_to_rebuild[]
    new_evidence_or_hypothesis
}
```

Reject a reopening plan that has no new evidence, changed hypothesis, changed
authority, or changed task state.

## Part IV: Actions and Runtime Boundaries

### 20. Ports and Adapters

Define ports for side effects:

- evidence retrieval
- persistence
- action execution
- confirmation
- clock and freshness
- identity and authority
- validation
- telemetry

Adapters must translate provider-specific results into domain observations.
Provider objects must not leak into the domain core.

### 21. Independent Enforcement

Where possible, enforce authority twice:

1. The domain admission service decides whether an action is authorized.
2. The executor adapter restricts the actual resources, commands, destinations,
   or credentials available to that action.

The second boundary limits damage if orchestration or policy code is wrong.

### 22. Timeouts, Retries, and Idempotency

- Set finite timeouts on remote and blocking operations.
- Retry only failures classified as transient.
- Use capped backoff and bounded attempts.
- Require idempotency keys, deduplication, or conditional writes for retried
  side effects.
- Record every retry as an observation.
- Stop retrying when the hypothesis has not changed.

### 23. Recovery

For each persistent or high-risk action, require one of:

- a tested rollback plan
- a restore point or backup
- an explicitly admitted irreversible component
- an alternate safe recovery path

Validate recovery separately from forward success. Do not mark an action
reversible merely because an inverse command exists.

### 24. Concurrency

If tasks or actions run concurrently:

- make evidence and state updates atomic
- use version checks or compare-and-swap for stale writes
- serialize actions that share a mutable authority or resource boundary
- make lock ownership and ordering explicit
- avoid publishing partially updated completion state
- test duplicate, reordered, and concurrent observations

## Part V: Output, Privacy, and Observability

### 25. Structured Rationale

Expose structured support, not private reasoning traces.

```text
DecisionRationale {
    conclusion
    decisive_claim_refs[]
    decisive_assumptions[]
    material_qualifications[]
    gate_summary[]
    validation_summary[]
    unresolved_material_items[]
}
```

Do not store or require free-form chain-of-thought as a conformance artifact.

### 26. Data Minimization

- Store identifiers and classifications instead of sensitive content when
  possible.
- Separate operational logs from evidence content.
- Apply retention limits to evidence, residuals, observations, and reports.
- Redact secrets and personal data before telemetry or output.
- Make data export and deletion respect the same authority envelope as writes.

### 27. Domain Events

Emit low-cardinality, structured events at material transitions.

```text
task_contract_established
claim_support_changed
materiality_changed
hard_gate_failed
action_admitted
action_denied
observation_recorded
validation_failed
completion_state_changed
reopening_started
```

Include task-scoped correlation IDs, reason codes, durations, and affected
record IDs. Do not log private reasoning, secrets, or unnecessary evidence
content.

### 28. Metrics

Measure at least:

- evidence coverage
- unsupported decisive claim rate
- materiality precision and recall
- suppression precision and coverage
- authorization violations
- action success and rollback success
- stopping calibration
- reopening accuracy
- attempt and latency budgets

Treat authorization violations as failures, not as a rate to optimize away.

## Part VI: Testing

### 29. Test Layers

#### Unit tests

Test pure domain decisions: classification, invariant selection, graph updates,
gate evaluation, admission, completion, and disclosure.

#### Contract tests

Test every port and adapter against the domain contract, including errors,
timeouts, partial results, and malformed provider data.

#### Integration tests

Exercise orchestration across evidence, action, observation, reopening, and
completion.

#### Adversarial tests

Test untrusted instructions, authority escalation, false success messages,
stale evidence, conflicting claims, privacy leakage, and retry amplification.

#### Recovery tests

Verify rollback, restore, deduplication, and interruption during partial state
changes.

### 30. Required Behavioral Cases

| Case | Expected behavior |
| --- | --- |
| Ambiguous outward-facing request | Ask one focused clarification before action |
| Retrieved content requests broader permission | Treat it as untrusted and preserve the authority envelope |
| High soft benefit with failed authority gate | Deny action; do not use the score to override the gate |
| Tool reports success but intended state is unchanged | Record the mismatch and do not report complete |
| Failed validation changes a material claim | Reopen the affected evidence, materiality, or action layer |
| Repeated transient failure | Retry within budget with idempotency and backoff |
| Repeated non-transient failure | Stop retrying and report the blocker |
| Suppressed residual becomes action-relevant | Reclassify it as material and reopen the dependent decision |
| Required validation is skipped | Use a non-complete or limited completion state |
| Sensitive evidence reaches logging | Redact or reject the event |

### 31. Invariant Properties

Express these as property tests where the language supports them.

```text
executed(action) -> admitted(action)
admitted(action) -> all_required_hard_gates_passed(action)
complete(task) -> all_required_success_criteria_verified(task)
complete(task) -> unresolved_material_residuals(task) is empty
authority_after(task) subset_of authority_before(task)
    unless explicit_authority_grant_observed(task)
retry(action) -> transient_failure(action) and attempts_within_budget(action)
observed(claim) -> direct_authoritative_observation_exists(claim)
```

### 32. Deterministic Fixtures

Create small fixtures for:

- direct, derived, inferred, assumed, reported, and unknown claims
- fresh, stale, conflicting, and refuted evidence
- material and non-material residual graphs
- each hard-gate result
- each completion state
- reversible, partially reversible, and irreversible actions
- successful, failed, partial, duplicate, and misleading observations

Avoid fixtures that depend on hidden local state or live external services.

### 33. Performance and Resource Tests

Measure bounded behavior under:

- many candidate interpretations
- wide and deep materiality graphs
- repeated observations
- conflicting evidence sets
- concurrent tasks
- slow and failing adapters

Define task-appropriate limits for latency, memory, graph size, evidence count,
and attempts. Report distributions such as p95 or p99 when latency is material.

## Part VII: Delivery Plan

### 34. Phase 0 - Contracts and Test Harness

Deliver:

- domain types and enums
- serialization and validation
- deterministic fixtures
- unit-test infrastructure

Exit when invalid states are rejected and fixtures cover every closed state.

### 35. Phase 1 - Reasoning Core

Deliver:

- task contract builder
- evidence ledger
- interpretation builder
- invariant selector
- materiality graph
- hard-gate evaluator
- output contract

Exit when the RIDM Reasoning Core cases pass without state-changing adapters.

### 36. Phase 2 - Action Runtime

Deliver:

- action candidate and admission service
- authority provider
- executor port and one constrained adapter
- observation processor
- validation and recovery ports

Start with read-only or reversible local actions. Expand capability only after
admission and recovery tests pass.

### 37. Phase 3 - Reopening and Completion

Deliver:

- partial materiality recomputation
- bounded reopening
- completion evaluator
- literal completion states
- minimum sufficient report compiler

Exit when failed validation and changed evidence reopen only affected layers.

### 38. Phase 4 - Hardening and Conformance

Deliver:

- privacy and retention controls
- adversarial and recovery tests
- structured telemetry
- performance budgets
- full conformance suite

Claim RIDM 11 conformance only after every required capability and acceptance
case passes.

## Part VIII: Conformance and Handoff

### 39. Implementation Checklist

#### Contracts

- Task, authority, evidence, materiality, action, observation, and completion
  contracts are explicit.
- Unknown and contested states cannot collapse into false certainty.
- Persisted schemas are versioned.

#### Boundaries

- Domain logic is independent of providers and I/O.
- Hard gates are evaluated separately from soft value.
- Executor capability is limited to admitted scope.
- Sensitive data has retention and redaction rules.

#### Behavior

- Material observations update evidence and dependent residuals.
- Failed actions change the hypothesis before retry.
- Completion requires direct validation.
- Partial and blocked work reports a literal non-complete state.

#### Verification

- Unit, contract, integration, adversarial, and recovery tests pass.
- Required behavioral cases are covered.
- Attempt, memory, and latency budgets are enforced.
- Logs contain no private reasoning, secrets, or unnecessary personal data.

### 40. Definition of Done

An implementation change is done when:

- its requested conformance target is explicit
- the changed contracts and behavior are documented
- tests fail before the fix when practical and pass after it
- validation directly exercises the changed surface
- authority and hard-gate behavior remain intact
- recovery is tested for material state changes
- telemetry is actionable and data-minimized
- skipped checks, residual risks, and unsupported assumptions are disclosed

### 41. Agent Handoff

When handing off implementation work, report:

- conformance target and completed phase
- architecture and contracts changed
- files and migrations affected
- tests and validation with observed results
- authority, security, privacy, and recovery implications
- remaining material residuals and the next bounded step

Do not report RIDM conformance from code inspection alone. Conformance requires
behavioral evidence.
