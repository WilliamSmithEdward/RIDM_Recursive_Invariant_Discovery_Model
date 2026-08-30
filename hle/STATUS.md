# HLE Run Status

Tabular summary of every attempted run. Content-free: categories, formats, outcomes, and
confidence bands only. Updated after each run. An asterisk marks a run scored against an
official key documented as defective or under-determined in that run's log.

## Totals

| Measure | Value |
| --- | --- |
| Runs completed | 20 |
| Correct | 10 |
| Percent correct | 50% |
| Incorrect, strict | 10 |
| Incorrect against defective or under-determined keys | 2 of 10 |
| High band record | 7 of 7 |
| Medium band record, recall-backed | 0 of 5 |
| Medium band record, derivation-backed | 2 of 3 |
| Low and very-low band record | 1 of 5 |

## By RIDM Model

Success and failure by the specification version governing the attempt. Strict scoring:
runs against defective or under-determined keys count as failures. Samples are small and
category mix varies by sprint; treat rates as indicative, not conclusive.

| RIDM model | Runs | Success | Fail | Success rate |
| --- | --- | --- | --- | --- |
| RIDM 12 | 10 | 6 | 4 | 60% |
| RIDM 11 | 10 | 4 | 6 | 40% |


## Sprints

| Sprint | Runs | Specification under test | Outcome |
| --- | --- | --- | --- |
| 0002 | Q000011 to Q000020 | RIDM 12 | 7 lessons (L18 to L24), consolidated into RIDM 13 (released) |
| 0001 | Q000001 to Q000010 | RIDM 11 | 17 lessons, consolidated into RIDM 12 (released) |


## HLE Qs

| Run | Sprint | Category | Format | Image | Result | Confidence band |
| --- | --- | --- | --- | --- | --- | --- |
| [Q000020](runs/Q000020.md) | 0002 | CS, Bayesian agent theory | exact match | no | incorrect | medium |
| [Q000019](runs/Q000019.md) | 0002 | Physics, topological matter | exact match | no | correct | high |
| [Q000018](runs/Q000018.md) | 0002 | Math, asymptotics | exact match | no | correct | high |
| [Q000017](runs/Q000017.md) | 0002 | Math, linear algebra | exact match | no | correct | medium |
| [Q000016](runs/Q000016.md) | 0002 | Neuroscience, plasticity model | exact match | no | correct | medium |
| [Q000015](runs/Q000015.md) | 0002 | Engineering, mechanics | exact match | no | correct | high |
| [Q000014](runs/Q000014.md) | 0002 | Physics, photometry | exact match | no | incorrect | low |
| [Q000013](runs/Q000013.md) | 0002 | CS, runtime analysis | exact match | no | incorrect | medium |
| [Q000012](runs/Q000012.md) | 0002 | Trivia | exact match | no | incorrect | very low |
| [Q000011](runs/Q000011.md) | 0002 | Humanities, literature | exact match | no | correct | low |
| [Q000010](runs/Q000010.md) | 0001 | Engineering, simulation | exact match | no | incorrect* | low |
| [Q000009](runs/Q000009.md) | 0001 | CS, model-based diagnosis | exact match | yes | correct | high |
| [Q000008](runs/Q000008.md) | 0001 | Film studies | multiple choice | no | incorrect | medium |
| [Q000007](runs/Q000007.md) | 0001 | Math, dynamical systems | multiple choice | no | correct | high |
| [Q000006](runs/Q000006.md) | 0001 | Art history | exact match | no | incorrect | low |
| [Q000005](runs/Q000005.md) | 0001 | CS, numeric formats | exact match | no | incorrect* | medium |
| [Q000004](runs/Q000004.md) | 0001 | Biology/Medicine | exact match | no | incorrect | medium |
| [Q000003](runs/Q000003.md) | 0001 | Math, algorithms | multiple choice | no | incorrect | medium |
| [Q000002](runs/Q000002.md) | 0001 | Math | exact match | no | correct | high |
| [Q000001](runs/Q000001.md) | 0001 | Physics | exact match | no | correct | high |