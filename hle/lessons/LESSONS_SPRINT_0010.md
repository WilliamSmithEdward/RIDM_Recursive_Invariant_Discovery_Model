# Framework Lessons - Sprint 0010 (Q000091 to Q000100)

Distilled, content-free lessons from the sprint's runs in [../runs/](../runs/). Each lesson
names the run that produced it, the RIDM surface it touches, and the change it suggests. One
lessons file exists per sprint of ten runs.

Section numbers cited in this file and in this sprint's run logs refer to RIDM 20, the
specification version under evaluation during the sprint.

Consolidation status: L74 through L79 are consolidated into RIDM 21, released 2026-09-01.
The next sprint's lessons start in `lessons/LESSONS_SPRINT_0011.md`.

The sprint's dominant signal: five of ten runs scored, and the misses cluster at the
instrument and model layer rather than the commitment layer the previous revision hardened.
Two runs kept working inside a frame or model after the run's own evidence had refuted it,
one by explaining away givens that were provably unrepresentable in the working model, one
by blending a refuted model's scores into an aggregate that a correct direct measurement
had already solved. One run committed a compound answer at a band its weakest slot's
margin-to-noise ratio could not support. One run never enumerated the mechanism class its
recall item asked about, and one applied a distribution-level contrast as a per-instance
classifier. The wins were carried by the same instrument disciplines the misses violated:
anchored enumeration and spectral computation, full-system reproduction with margin
checks, and designed-detail reading of layout and duplicated stimuli.

## L74. An unrepresentable given refutes the frame, not the figure (Q000091)

RIDM 20 surface: Sections 19, 23, and 24. The run proved exhaustively that the item's
initial values could not be represented by any state of the working model under any
labeling convention, then discharged that impossibility as a shared plotting artifact and
kept the model. The proof was a frame refutation, and the spec's menu-mismatch rule
already generalizes: a given that is impossible under the working model reopens model
identification, never the credibility of the given. Exact algebraic fingerprints in the
givens (simple half-integers, root-two forms) are model-identification evidence pointing
at the variant that represents them exactly. Two corollaries: a numerical coincidence
discovered inside a refuted frame carries no design weight, however many samples it spans;
and a rigor-class band cap, once the classification is made, is applied mechanically, not
re-argued from the strength of the derivation the cap exists to discount.

## L75. Compound bands price the weakest slot's margin against noise (Q000092, Q000095)

RIDM 20 surface: Sections 21 and 29. A nine-slot commitment was banded high although its
two weakest slots rested on an angle discrimination whose margin (about half the gap
between adjacent hypotheses) was comparable to the instrument's own per-measurement
spread. A measured value landing between adjacent hypotheses at noise scale is an
in-window ambiguity: the choices are instrument escalation (a stronger statistic, a
global template, more data) or a band cap, never nearest-neighbor selection under a
one-to-one constraint dressed as a measurement. The companion win applied the rule three
runs later: the same class of task, an explicit weakest-slot margin-to-noise check
(fourfold at worst), and two extraction defects caught by validating intermediate
products before trusting the output.

## L76. Enumerate the mechanism class before the value on cap items (Q000093)

RIDM 20 surface: Sections 19 and 23. A maximum-per-the-source recall item was answered
from a convergent-series mechanism, with a data-type bound as the only rival. The keyed
mechanism was a third class: an explicit clamp constant in the source. For any recall
item asking for a maximum, cap, or limit "per the source," the candidate set opens at
the mechanism level: convergent formula, data-type bound, explicit clamp. The clamp is
the modal authored referent because it is a quotable, intentional line. The stem phrase
"according to the source" fails the deletion test under the formula reading and is
consumed only by the clamp reading, which marks it before commitment.

## L77. Refutation taints all of a model's outputs (Q000096)

RIDM 20 surface: Sections 16, 20, and 29. A matching task was solved twice: by a
generative model of the underlying process, and by a direct measurement of the asked
relation (the long-horizon average provably embeds the short-horizon frames). The
generative model was refuted in-run: it demonstrably could not reproduce several items.
The direct measurement, solved as a global assignment, was fully correct; the committed
answer blended in the refuted model's scores, which flipped two slots, and a manual
single-cell override of the solved assignment flipped a third. Three rules follow. A
model refuted by any subset of the data drops all of its outputs to narrative-tier
everywhere; blending them into stronger evidence is scalar laundering of a failed
evidence gate. Before reverse-engineering a generator, check whether the asked relation
is directly measurable; the direct instrument was derivable from the stem and cheaper
than every generative attempt. And a jointly-optimal assignment is one object: a
single-cell edit justified by a single matrix entry silently reallocates the displaced
labels, so overrides re-solve the assignment or do not happen.

## L78. Distributional recall stays distributional (Q000100)

RIDM 20 surface: Sections 16 and 21. A cross-population contrast (a species is on
average denser in its invaded range) was used to classify one photograph per range.
One sample per side cannot measure a distributional difference, and the species
expresses the "invaded" phenotype inside its native range too. This is contrast
transplantation one level down: the recalled direction was sound, the inference
licensed from a single instance was not. On adversarially filtered pools the vividness
of such an association is magnet evidence: an association strong enough to feel like a
per-instance classifier is exactly what an item is built to invert, and slot confidence
must track the validity of the licensed inference, not the familiarity of the cue.

## L79. What worked: direct instruments, anchors, layout as construction (Q000094 to Q000099)

RIDM 20 surface: Sections 19, 23, 24, 39, and 40. Full-system reproduction turned two
matching tasks into derivations: a physics simulation from extracted geometry with
exhaustive assignment and margin checks, and a tight-binding computation whose
measuring instrument was validated on analytic ground truth before use. Anchored
enumeration (hand-derived small cases, start-condition invariance across equivalence
classes) carried a combinatorics item; anchored spectral numerics with a classical
known case carried an operator-index item, with the zero mode classified structurally
before it could be miscounted. Minimal-pair and layout reading carried two more: a
duplicated photograph and a mimic-causer column split were consumed as authored
construction, and an engineered one-phrase document difference selected the reranking
answer. Five of the sprint's five wins were instrument-led; so were three of the five
losses, on the occasions the instrument's own discipline was waived.
