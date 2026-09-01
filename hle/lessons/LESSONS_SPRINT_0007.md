# Framework Lessons - Sprint 0007 (Q000061 to Q000070)

Distilled, content-free lessons from the sprint's runs in [../runs/](../runs/). Each lesson
names the run that produced it, the RIDM surface it touches, and the change it suggests. One
lessons file exists per sprint of ten runs.

Section numbers cited in this file and in this sprint's run logs refer to RIDM 17, the
specification version under evaluation during the sprint.

Consolidation status: L57 through L61 are consolidated into RIDM 18, released 2026-09-01.
The next sprint's lessons start in `lessons/LESSONS_SPRINT_0008.md`.

The sprint's dominant signal: RIDM 17's disciplines held. Nine of ten runs scored, the best
sprint to date, with hits across instrumented image measurement, closed-form optimization,
site identification, clinical vignette partition, model-selection tournaments, spectral
combinatorics, degenerate-candidate coverage, separability analysis, and research-level
recall split into derived and recalled halves. The single genuine miss was not at the frame
or ranking layer that dominated earlier sprints; it was at the solution-assembly layer of an
optimization item: a rival packing was found, costed without the mechanism that makes it
win, and pruned, while a stem-granted capability sat unused under the committed reading and
a menu option inside the solver's own feasibility window went unprobed. One additional item
was spoiled by a protocol error, the grading oracle consulted before the answer was
committed; it was excluded without consuming a run number.

## L57. A granted capability is construction (Q000070)

RIDM 17 surface: Sections 23 and 24. The frame discipline prices a constructed position,
dataset, or parameter set as load-bearing; the same status belongs to a capability the stem
grants, an operation, a product form, a move type, a permitted composite. A committed
solution under which a granted capability is never used is an undischarged alarm: the rival
solution that uses the capability must be constructed and computed to parity before
ranking. The welded-option decoy reading is real but must be earned by that comparison, not
assumed from per-unit values.

## L58. Dominance compares whole solutions (Q000070)

RIDM 17 surface: Sections 20 and 23. A per-unit or per-cell dominance claim, this option is
worth less than that one from the same material, does not extend to solutions: the dominated
option can be globally optimal when it extracts value from regions the dominant option
cannot reach. Before a dominance argument prunes a candidate, restate it at the
whole-solution level and check that the pruned candidate cannot buy access to otherwise
unreachable value.

## L59. An option inside the feasibility window is a flagged observable (Q000070)

RIDM 17 surface: Sections 23, 24, and 29. When the solver's own bounds place a menu option
strictly between the committed value and the derived ceiling, that option is evidence that
a better construction exists. It enters the commitment gate as an alarm: reproduce the
construction that would achieve it or refute it. Menu presence was used to select a reading
in the same run; the discipline is symmetric, and an unexplained in-window option above the
commitment binds exactly as an off-menu derivation does.

## L60. The oracle reveal is an irreversible action gated on commitment (process)

RIDM 17 surface: Sections 35, 43, and 48. Consulting the grading oracle is an irreversible
information action: once seen, the key cannot be unseen, and the item is spent. Its
admission precondition is a recorded commitment. One item this sprint was spoiled by
running the reveal before the answer was committed; the correct handling, applied, is to
void the item without scoring it, record the error, and re-establish the sequencing check
before the next reveal. The framework's action-admission gates apply to the evaluation
harness itself, not only to the task under evaluation.

## L61. What worked: instrumentation, tournaments, split recall (Q000061 to Q000069)

RIDM 17 surface: Sections 16, 21, 23, 39, and 40. Instrumenting an image measurement
dissolved a spurious eyeball reading and upgraded the claim to observed. Computing every
plausible model in a fitted tournament converted a parsimony adjective into a derived
comparison. Deriving jurisdiction from coordinates before recall eliminated a
name-collision trap. Treating a character's self-diagnosis as a planted rival reading, not
evidence, let the given-role partition select the answer. Testing a recalled theorem's
hypothesis scope against the task's class opened the degenerate candidate that was the
key. Splitting a research-level claim into a derived lower bound plus a minimal recalled
remainder set the band honestly at the recalled link. These are the intended uses of the
existing disciplines; no rule change follows, and the record is kept to weigh against
future revisions that would trade them away.
