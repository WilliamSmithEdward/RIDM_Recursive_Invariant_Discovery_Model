# Framework Lessons - Sprint 0002 (Q000011 to Q000020)

Distilled, content-free lessons from the sprint's runs in [../runs/](../runs/). Each lesson
names the run that produced it, the RIDM surface it touches, and the change it suggests. One
lessons file exists per sprint of ten runs.

Section numbers cited in this file and in this sprint's run logs refer to RIDM 12, the
specification version under evaluation during the sprint.

## L18. Task provenance is evidence (Q000011)

RIDM 12 surface: Section 23, candidate coverage. The tradition a task comes from encodes how
its clues work: a question translated from another language's quiz culture carries hints
whose semantics live in that culture's school ontology. Identify provenance and genre before
interpreting clues; treat them as evidence alongside the task text. In Q000011 this made the
decisive clue interpretable and the answer reconstructible without verbatim recall.

## L19. Decouple compound-answer slots (Q000012, incorrect answer)

RIDM 12 surface: Section 23, candidate coverage. A multi-part answer's elements are often
drawn from different categories by design, especially when an ensemble signals breadth.
Generate and rank candidates for each slot independently instead of drawing every slot from
the pool that fit the first. In Q000012 the slot the clue selected directly was right; the slot
inherited from the first slot's category was wrong.

## L20. Scope-match recalled constants; derive when feasible (Q000013, incorrect answer)

RIDM 12 surface: Sections 16, 19, 29, and 40. A remembered numeric result silently carries
its source's parameter binding; hard tasks alter parameters precisely to defeat copying.
Before reuse, verify the binding matches the task. When the derivation to the constant is
feasible at comparable cost, compute it and demote the recalled value to an anchor check;
a derivation route dominates numeric recall the way a derived claim dominates a reported
one. In Q000013 the mechanism and closed form were already derived, the computation was
cheap, and a constant recalled from a different parameterization was committed instead.
Corollary for calibration: unverified numeric recall is low band by rule.

## L21. Carry derived precision; do not snap to remembered round values (Q000014, incorrect)

RIDM 12 surface: Sections 16 and 40. Rounding a self-derived intermediate constant to match
a rounder remembered figure silently replaces a derived claim with a reported one in the
middle of a chain. In Q000014 the attempt derived the decisive constant correctly, then
snapped it to a remembered textbook value forty percent lower; keeping its own derivation
would have landed within one unit of the official answer. Remembered values are anchor
checks for derived ones, never replacements.
