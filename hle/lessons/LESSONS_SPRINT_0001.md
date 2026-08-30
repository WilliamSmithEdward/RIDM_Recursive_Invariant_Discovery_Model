# Framework Lessons - Sprint 01 (Q001 to Q010)

Distilled, content-free lessons from the sprint's runs in [runs/](runs/). Each lesson names
the run that produced it, the RIDM surface it touches, and the change it suggests. One
lessons file exists per sprint of ten runs; this file is closed.

Consolidation status: L1 through L17 are consolidated into RIDM 12, released 2026-08-30.
The next sprint's lessons start in `lessons/LESSONS_SPRINT_0002.md`.

Section numbers cited in this file and in this sprint's run logs refer to RIDM 11.0, the
specification version under evaluation during the sprint.

## L1. Closed-world validation rung (Q001)

RIDM surface: Section 34, validation as evidence. In closed-book tasks none of the ladder's
rungs exist. The strongest available checks are convergent independent derivation routes and
anchor cases with known outcomes. The ladder needs a rung for verification-starved settings.

## L2. Recall is evidence with a default type (Q001)

RIDM surface: Sections 12 to 15, evidence and claims. Parametric recall functions as a
reported claim from an unreliable internal source. It should carry that type by default, with
named upgrade paths: derivation, anchor agreement, or external observation. In Q001 the only
partly wrong claim after reveal was an untyped-feeling recalled attribution; typing had
correctly kept it off the critical path.

## L3. Anchor tests deserve standing (Q001)

RIDM surface: Section 34. Calibrating a method against a special case with an independently
known outcome, before applying it to the unknown case, was decisive in both the warm-up run
and Q001. The specification never names this device.

## L4. Internal route conflicts need the external conflict rules (Q002)

RIDM surface: Section 17, conflicting evidence. Two of the agent's own reasoning routes can
disagree exactly as two external sources do. The same discipline applies: do not average,
prefer the more direct and rigorous route, and record what would resolve the disagreement.
The specification currently frames conflict as an external-source phenomenon only.

## L5. Adversarial calibration of the task itself (Q002)

RIDM surface: Sections 19 to 21, interpretations and invariant selection. Hard tasks are
often calibrated so that the most available invariant is almost right but not right. An
explicit pass asking which constraint is load-bearing, and whether the obvious bound is
designed to be non-tight, belongs in invariant selection for high-difficulty tasks. This is
the reasoning analogue of Section 52's untrusted-content stance: the task statement is honest,
but its difficulty is engineered around the solver's defaults.

## L6. Literal contract precedence in forced choice (Q003, incorrect answer)

RIDM surface: Sections 8 to 9 and 19 to 20, task contract and interpretations. When
clarification is unavailable, the task text and its option set are the contract. Modeling the
requester's unstated intent may break ties between readings the text supports equally; it
must not override a result derived from the stated criterion. In Q003 an inferred
author-intent claim overrode a derived dominance result and produced the wrong commitment.

## L7. Trap-depth iteration (Q003, incorrect answer)

RIDM surface: invariant selection. Discovering one designed reversal in a hard task creates
false confidence that the trap has been found. Continue until no admissible option dominates
the current choice under the literal criterion. One-layer trap detection is a stopping
failure.

## L8. Claim-type precedence must bind at final selection (Q003, incorrect answer)

RIDM surface: Sections 13 to 15 and 24. Typing claims during analysis is not enough; the
moment of commitment needs its own gate. Before finalizing, check that the selected
conclusion is not dominated, under the stated success criterion, by an alternative resting on
stronger-typed support. In Q003 the inversion (inferred over derived) happened exactly and
only at the decision step.

## L9. Coherence gate on interpretations (Q004, incorrect answer)

RIDM surface: Sections 19 to 20. If the leading interpretation makes the stimulus internally
incoherent, that is evidence against the interpretation, not evidence that the source is
sloppy. The failure signature is noticing a contradiction and overriding it by downgrading
the author's coherence. Prefer the reading under which the scenario makes sense.

## L10. State changes propagate in pure reasoning too (Q004, incorrect answer)

RIDM surface: Section 39. A stated mid-scenario state change is a reopening trigger exactly
like a post-action observation: recompute every dependent claim, including signs and
directions of needs and effects. Carrying a stale sign forward after an inversion is the
reasoning-side twin of the static-materiality failure mode.

## L11. Availability is the weakest support tier (Q004, incorrect answer)

RIDM surface: Sections 13 to 15. Famous associations that pattern-match the surface, and
thematic echoes planted earlier in a text, are narrative-tier support. They may generate
hypotheses; they may never resolve conflicts or survive a failed coherence check.

## L12. Verify the verifier (Q005, defective official answer)

RIDM surface: Sections 33, 41, and the tool-result literalism failure mode. Answer keys,
graders, tests, and correction signals are reported evidence, not automatic truth. Before a
contradiction from validation infrastructure reopens the model, check the signal's internal
consistency. A verdict that contradicts itself loses authority regardless of its source. In
Q005 the official rationale contained several checkable arithmetic impossibilities;
capitulating to it would have corrupted the model.

## L13. Surprise decomposition before self-revision (Q005)

RIDM surface: Sections 39 to 42, reopening. When an observed error falls entirely outside
the stated residual, first ask whether the observation was generated by something other than
the modeled task: a defective oracle, a changed environment, an unmodeled regime. Reopening
the reasoning layer is only correct when the contradicting evidence is itself well-formed.

## L14. Candidate-set coverage before ranking (Q006, incorrect answer)

RIDM surface: Section 20, generation boundaries. In recall regimes the binding constraint is
whether the true answer is in the candidate set, not how well the set is ranked. Widen the
set with one retrieval probe per discriminative clue, asking what each clue uniquely
selects, independently of the candidates already listed. Consistency-scoring against an
availability-shaped set silently excludes the answer.

## L15. Per-band confidence calibration (Q006 and cumulative)

RIDM surface: Sections 18 and 55. Qualitative confidence bands drift: across eight runs the
high band scored 3 of 3, the low band 0 of 1 (as expected), and the medium band 0 of 4. The
specification prescribes typed uncertainty but has no mechanism for auditing band accuracy
against outcomes over time. Calibration tracking should be a named discipline, with drifted
bands recalibrated; in weak-recall regimes, medium confidence should be capped near the
structural prior (for example, the option-count prior in forced choice).

## L16. The task text is an evidence source (Q008, incorrect answer)

RIDM surface: Sections 12 and 19 to 20. Emphasized qualifiers, oddly specific descriptions,
and asymmetries of detail inside the task statement are micro-evidence about the answer. Run
the unique-selection probe over the task text first, before consulting domain memory;
narrative-plausibility abduction must not outrank question-internal textual evidence.

## L17. Criterion-information mismatch (Q010, incorrect per under-determined key)

RIDM surface: Sections 8 to 9 and 18. Sometimes the stated success criterion demands more
precision than the task statement determines: stochastic outcomes with unstated seeds,
unstated software versions, or unstated counting conventions. Recognize the regime
explicitly. Report the central estimate with its band, flag the mismatch, and cap
confidence at what the answer distribution's concentration supports; convention uncertainty
usually dominates sampling noise. In agentic settings this regime is a clarification
trigger distinct from ambiguity of meaning.
