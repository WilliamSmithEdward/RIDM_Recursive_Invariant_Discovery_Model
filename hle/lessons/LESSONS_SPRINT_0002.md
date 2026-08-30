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
