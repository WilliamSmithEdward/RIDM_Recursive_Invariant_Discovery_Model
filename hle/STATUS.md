# HLE Run Status

Tabular summary of every attempted run. Content-free: categories, formats, outcomes, and
confidence bands only. Updated after each run. An asterisk marks a run scored against an
official key documented as defective or under-determined in that run's log.

| Run | Sprint | Category | Format | Image | Result | Confidence band |
| --- | --- | --- | --- | --- | --- | --- |
| [Q000001](runs/Q000001.md) | 0001 | Physics | exact match | no | correct | high |
| [Q000002](runs/Q000002.md) | 0001 | Math | exact match | no | correct | high |
| [Q000003](runs/Q000003.md) | 0001 | Math, algorithms | multiple choice | no | incorrect | medium |
| [Q000004](runs/Q000004.md) | 0001 | Biology/Medicine | exact match | no | incorrect | medium |
| [Q000005](runs/Q000005.md) | 0001 | CS, numeric formats | exact match | no | incorrect* | medium |
| [Q000006](runs/Q000006.md) | 0001 | Art history | exact match | no | incorrect | low |
| [Q000007](runs/Q000007.md) | 0001 | Math, dynamical systems | multiple choice | no | correct | high |
| [Q000008](runs/Q000008.md) | 0001 | Film studies | multiple choice | no | incorrect | medium |
| [Q000009](runs/Q000009.md) | 0001 | CS, model-based diagnosis | exact match | yes | correct | high |
| [Q000010](runs/Q000010.md) | 0001 | Engineering, simulation | exact match | no | incorrect* | low |
| [Q000011](runs/Q000011.md) | 0002 | Humanities, literature | exact match | no | correct | low |
| [Q000012](runs/Q000012.md) | 0002 | Trivia | exact match | no | incorrect | very low |
| [Q000013](runs/Q000013.md) | 0002 | CS, runtime analysis | exact match | no | incorrect | medium |
| [Q000014](runs/Q000014.md) | 0002 | Physics, photometry | exact match | no | incorrect | low |
| [Q000015](runs/Q000015.md) | 0002 | Engineering, mechanics | exact match | no | correct | high |

## Totals

| Measure | Value |
| --- | --- |
| Runs completed | 15 |
| Correct | 6 |
| Incorrect, strict | 9 |
| Incorrect against defective or under-determined keys | 2 of 9 |
| High band record | 5 of 5 |
| Medium band record | 0 of 5 |
| Low and very-low band record | 1 of 5 |

## By RIDM Model

Success and failure by the specification version governing the attempt. Strict scoring:
runs against defective or under-determined keys count as failures. Samples are small and
category mix varies by sprint; treat rates as indicative, not conclusive.

| RIDM model | Runs | Success | Fail | Success rate |
| --- | --- | --- | --- | --- |
| RIDM 11.0 | 10 | 4 | 6 | 40% |
| RIDM 12 (sprint in progress) | 5 | 2 | 3 | 40% |

## Sprints

| Sprint | Runs | Specification under test | Outcome |
| --- | --- | --- | --- |
| 0001 | Q000001 to Q000010 | RIDM 11.0 | 17 lessons, consolidated into RIDM 12 (released) |
| 0002 | Q000011 to Q000020 | RIDM 12 | in progress |
