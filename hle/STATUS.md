# HLE Run Status

Tabular summary of every attempted run. Content-free: categories, formats, outcomes, and
confidence bands only. Updated after each run. All grading is strict: a run scores correct
only on a match with the official key. Key-quality notes, where material, live in the
individual run logs. Two calibration aggregates sit in Totals: misses committed at the
high band, the overconfidence count, and candidate coverage, the rate at which the keyed
answer entered the pre-commitment candidate set, tracked from sprint 0013 onward.

## Totals

| Measure | Value |
| --- | --- |
| Runs completed | 170 |
| Correct | 98 |
| Percent correct | 58% |
| Incorrect, strict | 72 |
| Incorrect against defective or under-determined keys | 2 of 72 |
| High band record | 64 of 82 |
| Medium band record, recall-backed | 7 of 17 |
| Medium band record, derivation-backed | 13 of 20 |
| Medium band record, inference-backed | 9 of 29 |
| Low and very-low band record | 5 of 22 |
| Misses committed at the high band | 18 of 72 |
| Candidate coverage, tracked from sprint 0013 | 43 of 50 runs |

## By RIDM Model

Success and failure by the specification version governing the attempt. Strict scoring:
runs against defective or under-determined keys count as failures. Samples are small and
category mix varies by sprint; treat rates as indicative, not conclusive.

| RIDM model | Runs | Success | Fail | Success rate |
| --- | --- | --- | --- | --- |
| RIDM 30 | 10 | 6 | 4 | 60% |
| RIDM 29 | 10 | 8 | 2 | 80% |
| RIDM 27 | 10 | 4 | 6 | 40% |
| RIDM 26 | 10 | 4 | 6 | 40% |
| RIDM 23 | 10 | 7 | 3 | 70% |
| RIDM 22 | 10 | 7 | 3 | 70% |
| RIDM 21 | 10 | 6 | 4 | 60% |
| RIDM 20 | 10 | 5 | 5 | 50% |
| RIDM 19 | 10 | 8 | 2 | 80% |
| RIDM 18 | 10 | 6 | 4 | 60% |
| RIDM 17 | 10 | 9 | 1 | 90% |
| RIDM 16 | 10 | 3 | 7 | 30% |
| RIDM 15 | 10 | 4 | 6 | 40% |
| RIDM 14 | 10 | 6 | 4 | 60% |
| RIDM 13 | 10 | 5 | 5 | 50% |
| RIDM 12 | 10 | 6 | 4 | 60% |
| RIDM 11 | 10 | 4 | 6 | 40% |


## Sprints

| Sprint | Runs | Specification under test | Outcome |
| --- | --- | --- | --- |
| 0017 | Q000161 to Q000170 | RIDM 30 | 5 lessons (L114 to L118), consolidated into RIDM 31 (released) |
| 0016 | Q000151 to Q000160 | RIDM 29 | 4 lessons (L110 to L113), consolidated into RIDM 30 (released) |
| 0015 | Q000141 to Q000150 | RIDM 27 | 6 lessons (L104 to L109), consolidated into RIDM 28 (released) |
| 0014 | Q000131 to Q000140 | RIDM 26 | 6 lessons (L98 to L103), consolidated into RIDM 27 (released) |
| 0013 | Q000121 to Q000130 | RIDM 23 | 6 lessons (L92 to L97), consolidated into RIDM 24 (released) |
| 0012 | Q000111 to Q000120 | RIDM 22 | 6 lessons (L86 to L91), consolidated into RIDM 23 (released) |
| 0011 | Q000101 to Q000110 | RIDM 21 | 6 lessons (L80 to L85), consolidated into RIDM 22 (released) |
| 0010 | Q000091 to Q000100 | RIDM 20 | 6 lessons (L74 to L79), consolidated into RIDM 21 (released) |
| 0009 | Q000081 to Q000090 | RIDM 19 | 5 lessons (L69 to L73), consolidated into RIDM 20 (released) |
| 0008 | Q000071 to Q000080 | RIDM 18 | 7 lessons (L62 to L68), consolidated into RIDM 19 (released) |
| 0007 | Q000061 to Q000070 | RIDM 17 | 5 lessons (L57 to L61), consolidated into RIDM 18 (released) |
| 0006 | Q000051 to Q000060 | RIDM 16 | 8 lessons (L49 to L56), consolidated into RIDM 17 (released) |
| 0005 | Q000041 to Q000050 | RIDM 15 | 8 lessons (L41 to L48), consolidated into RIDM 16 (released) |
| 0004 | Q000031 to Q000040 | RIDM 14 | 8 lessons (L33 to L40), consolidated into RIDM 15 (released) |
| 0003 | Q000021 to Q000030 | RIDM 13 | 8 lessons (L25 to L32), consolidated into RIDM 14 (released) |
| 0002 | Q000011 to Q000020 | RIDM 12 | 7 lessons (L18 to L24), consolidated into RIDM 13 (released) |
| 0001 | Q000001 to Q000010 | RIDM 11 | 17 lessons, consolidated into RIDM 12 (released) |


## HLE Qs

| Run | Sprint | Category | Format | Image | Result | Confidence band |
| --- | --- | --- | --- | --- | --- | --- |
| [Q000170](runs/Q000170.md) | 0017 | Math, mean-convex surface topology | multiple choice | no | correct | high |
| [Q000169](runs/Q000169.md) | 0017 | Chemistry as labeled, weak-localization estimate | exact match | no | correct | medium |
| [Q000168](runs/Q000168.md) | 0017 | Math, moduli of curves | exact match | no | correct | high |
| [Q000167](runs/Q000167.md) | 0017 | History, search-interest chart identification | exact match | yes | correct | high |
| [Q000166](runs/Q000166.md) | 0017 | History, Second World War naval losses | exact match | no | incorrect | medium |
| [Q000165](runs/Q000165.md) | 0017 | Math, rotation-group optimization | exact match | no | correct | high |
| [Q000164](runs/Q000164.md) | 0017 | Engineering, industrial power network harmonics | multiple choice | yes | incorrect | low |
| [Q000163](runs/Q000163.md) | 0017 | Psychology, sentence processing and metonymy | exact match | no | incorrect | medium |
| [Q000162](runs/Q000162.md) | 0017 | CS, substitution cipher decipherment | exact match | no | correct | high |
| [Q000161](runs/Q000161.md) | 0017 | Math, digit-probability series convergence | exact match | no | incorrect | medium |
| [Q000160](runs/Q000160.md) | 0016 | Chemistry, cycloaddition selectivity | exact match | no | correct | medium |
| [Q000159](runs/Q000159.md) | 0016 | Math, long-ray compactifications | exact match | no | correct | medium |
| [Q000158](runs/Q000158.md) | 0016 | Math, polyhedral geodesics | exact match | no | incorrect | high |
| [Q000157](runs/Q000157.md) | 0016 | Math, ordinal arithmetic | exact match | no | correct | high |
| [Q000156](runs/Q000156.md) | 0016 | Math, coadjoint orbits and equivariant cohomology | exact match | no | incorrect | medium |
| [Q000155](runs/Q000155.md) | 0016 | CS, chess forced-mate distance | exact match | no | correct | medium |
| [Q000154](runs/Q000154.md) | 0016 | Math, contour residues | exact match | yes | correct | high |
| [Q000153](runs/Q000153.md) | 0016 | CS, exterior visibility guarding | exact match | no | correct | medium |
| [Q000152](runs/Q000152.md) | 0016 | Physics, time-varying electrodynamics | exact match | no | correct | high |
| [Q000151](runs/Q000151.md) | 0016 | Physics, sky-chart geolocation | exact match | yes | correct | high |
| [Q000150](runs/Q000150.md) | 0015 | CS/AI, recommender puzzle chain | exact match | no | incorrect | medium |
| [Q000149](runs/Q000149.md) | 0015 | Math, semistable reduction | exact match | no | incorrect | medium |
| [Q000148](runs/Q000148.md) | 0015 | CS, LSM-tree sizing | exact match | no | incorrect | low |
| [Q000147](runs/Q000147.md) | 0015 | Linguistics, lexical complexity features | multiple choice | no | incorrect | medium |
| [Q000146](runs/Q000146.md) | 0015 | Biology, image authenticity | multiple choice | yes | correct | high |
| [Q000145](runs/Q000145.md) | 0015 | Art history, museum provenance | exact match | no | correct | medium |
| [Q000144](runs/Q000144.md) | 0015 | Math, grid extremal combinatorics | exact match | no | correct | high |
| [Q000143](runs/Q000143.md) | 0015 | Math, cardinality multi-select | exact match | no | incorrect | medium |
| [Q000142](runs/Q000142.md) | 0015 | Math, extremal enclosure geometry | exact match | no | correct | high |
| [Q000141](runs/Q000141.md) | 0015 | Chemistry, hybrid perovskite materials | multiple choice | no | incorrect | medium |
| [Q000140](runs/Q000140.md) | 0014 | Engineering, remote sensing fusion | multiple choice | no | correct | low |
| [Q000139](runs/Q000139.md) | 0014 | Medicine, epidemiology threshold | exact match | no | incorrect | medium |
| [Q000138](runs/Q000138.md) | 0014 | CS, security attack graphs | exact match | no | incorrect | medium |
| [Q000137](runs/Q000137.md) | 0014 | Other, multidomain trivia chain | exact match | no | incorrect | low |
| [Q000136](runs/Q000136.md) | 0014 | CS/AI, prototype learning | exact match | no | incorrect | low |
| [Q000135](runs/Q000135.md) | 0014 | Math, topological signal processing | multiple choice | no | correct | medium |
| [Q000134](runs/Q000134.md) | 0014 | Math, algebraic geometry zero-cycles | exact match | no | correct | high |
| [Q000133](runs/Q000133.md) | 0014 | Chemistry, structure determination | exact match | no | incorrect | high |
| [Q000132](runs/Q000132.md) | 0014 | Engineering, power-system optimization | multiple choice | yes | incorrect | low |
| [Q000131](runs/Q000131.md) | 0014 | CS/AI, boolean expression enumeration | exact match | no | correct | high |
| [Q000130](runs/Q000130.md) | 0013 | Chemistry, retrosynthesis | exact match | no | correct | high |
| [Q000129](runs/Q000129.md) | 0013 | Art history, symbol identification | exact match | no | incorrect | medium |
| [Q000128](runs/Q000128.md) | 0013 | Medicine, genetic disorders and metabolism | multiple choice | no | correct | medium |
| [Q000127](runs/Q000127.md) | 0013 | Math, Rademacher sum asymptotics | exact match | no | correct | high |
| [Q000126](runs/Q000126.md) | 0013 | Chemistry, sulfonation NMR prediction | exact match | yes | correct | low |
| [Q000125](runs/Q000125.md) | 0013 | CS, graph algorithms | multiple choice | no | correct | high |
| [Q000124](runs/Q000124.md) | 0013 | Engineering, conservation lighting | exact match | no | incorrect | low |
| [Q000123](runs/Q000123.md) | 0013 | Math, ODE boundary-value problem | exact match | no | correct | high |
| [Q000122](runs/Q000122.md) | 0013 | CS, information encoding | exact match | no | correct | medium |
| [Q000121](runs/Q000121.md) | 0013 | Epistemology, probabilistic reasoning | multiple choice | no | incorrect | medium |
| [Q000120](runs/Q000120.md) | 0012 | Ecology, path-analysis signs | multiple choice | no | correct | medium |
| [Q000119](runs/Q000119.md) | 0012 | Chemistry, cation cyclization | exact match | yes | incorrect | high |
| [Q000118](runs/Q000118.md) | 0012 | Chemistry, route identification | exact match | yes | correct | high |
| [Q000117](runs/Q000117.md) | 0012 | Physics, optical activity | multiple choice | no | correct | medium |
| [Q000116](runs/Q000116.md) | 0012 | Medicine, vector identification | exact match | yes | correct | high |
| [Q000115](runs/Q000115.md) | 0012 | Physics, relativity foundations | exact match | no | incorrect | high |
| [Q000114](runs/Q000114.md) | 0012 | Physics, photoproduction threshold | exact match | no | incorrect | medium |
| [Q000113](runs/Q000113.md) | 0012 | CS, logic-program granularity | multiple choice | no | correct | medium |
| [Q000112](runs/Q000112.md) | 0012 | Math, PDE long-time decay | exact match | no | correct | high |
| [Q000111](runs/Q000111.md) | 0012 | Medicine, biliary infection imaging | multiple choice | yes | correct | medium |
| [Q000110](runs/Q000110.md) | 0011 | Puzzle, multi-peg disk transfer | exact match | no | correct | high |
| [Q000109](runs/Q000109.md) | 0011 | Math, metric geometry | exact match | no | correct | medium |
| [Q000108](runs/Q000108.md) | 0011 | Linguistics, source-passage recall | exact match | no | correct | high |
| [Q000107](runs/Q000107.md) | 0011 | CS/AI, machine simulation | exact match | no | correct | high |
| [Q000106](runs/Q000106.md) | 0011 | Cultural studies, dress hierarchy | multiple choice | no | correct | medium |
| [Q000105](runs/Q000105.md) | 0011 | Art history, Roman architecture | multiple choice | no | incorrect | medium |
| [Q000104](runs/Q000104.md) | 0011 | Engineering, ground-effect aerodynamics | exact match | no | correct | high |
| [Q000103](runs/Q000103.md) | 0011 | Chemistry, complexity metric | exact match | no | incorrect | low |
| [Q000102](runs/Q000102.md) | 0011 | Chemistry, intercalation staging | exact match | yes | incorrect | medium |
| [Q000101](runs/Q000101.md) | 0011 | Physics, Feynman graph counting | exact match | no | incorrect | medium |
| [Q000100](runs/Q000100.md) | 0010 | Biology, invasion ecology | exact match | yes | incorrect | low |
| [Q000099](runs/Q000099.md) | 0010 | Math, lattice combinatorics | exact match | no | correct | high |
| [Q000098](runs/Q000098.md) | 0010 | Biology, mimicry ecology | exact match | yes | correct | high |
| [Q000097](runs/Q000097.md) | 0010 | Math, minimal surface stability | exact match | no | correct | high |
| [Q000096](runs/Q000096.md) | 0010 | Math, cellular automata | exact match | yes | incorrect | low |
| [Q000095](runs/Q000095.md) | 0010 | Engineering, roller kinematics | exact match | yes | correct | high |
| [Q000094](runs/Q000094.md) | 0010 | CS/AI, retrieval reranking | multiple choice | no | correct | high |
| [Q000093](runs/Q000093.md) | 0010 | Other, source-code trivia | exact match | no | incorrect | low |
| [Q000092](runs/Q000092.md) | 0010 | Physics, nanotube optics | exact match | yes | incorrect | high |
| [Q000091](runs/Q000091.md) | 0010 | Physics, open quantum dynamics | exact match | yes | incorrect | high |
| [Q000090](runs/Q000090.md) | 0009 | Physics, electron-phonon path integral | exact match | no | correct | high |
| [Q000089](runs/Q000089.md) | 0009 | Linguistics, loanword phonology | exact match | no | correct | low |
| [Q000088](runs/Q000088.md) | 0009 | Chemistry, MS modification mapping | multiple choice | no | incorrect | high |
| [Q000087](runs/Q000087.md) | 0009 | Engineering, cable capacitance | exact match | no | correct | high |
| [Q000086](runs/Q000086.md) | 0009 | CS/AI, network width bound | exact match | no | correct | high |
| [Q000085](runs/Q000085.md) | 0009 | CS/AI, Weisfeiler-Leman theory | multiple choice | no | correct | high |
| [Q000084](runs/Q000084.md) | 0009 | Math, bootstrap percolation | exact match | no | correct | high |
| [Q000083](runs/Q000083.md) | 0009 | Math, ODE system integral | exact match | no | correct | high |
| [Q000082](runs/Q000082.md) | 0009 | Other, instrument identification | multiple choice | yes | correct | high |
| [Q000081](runs/Q000081.md) | 0009 | Math, coverage cost optimization | exact match | no | incorrect | medium |
| [Q000080](runs/Q000080.md) | 0008 | CS, decimal-architecture program design | exact match | no | incorrect | low |
| [Q000079](runs/Q000079.md) | 0008 | Math, incidence geometry | exact match | no | correct | high |
| [Q000078](runs/Q000078.md) | 0008 | Math, matrix-dressed integral | multiple choice | no | correct | high |
| [Q000077](runs/Q000077.md) | 0008 | Math, high-precision evaluation | exact match | no | correct | high |
| [Q000076](runs/Q000076.md) | 0008 | Bioinformatics, sequence identification | multiple choice | no | correct | high |
| [Q000075](runs/Q000075.md) | 0008 | Math, constrained estimation puzzle | exact match | no | incorrect | low |
| [Q000074](runs/Q000074.md) | 0008 | Engineering, ECU cycle budgeting | exact match | no | correct | medium |
| [Q000073](runs/Q000073.md) | 0008 | Math, policy gradient | exact match | yes | incorrect | high |
| [Q000072](runs/Q000072.md) | 0008 | Education, automation bias | multiple choice | no | incorrect | high |
| [Q000071](runs/Q000071.md) | 0008 | CS, memory-constrained programming | exact match | no | correct | medium |
| [Q000070](runs/Q000070.md) | 0007 | Math, packing optimization | multiple choice | no | incorrect | medium |
| [Q000069](runs/Q000069.md) | 0007 | Math, bounded cohomology | exact match | no | correct | medium |
| [Q000068](runs/Q000068.md) | 0007 | CS/AI, linear separability | multiple choice | no | correct | high |
| [Q000067](runs/Q000067.md) | 0007 | Math, inverse limits | exact match | no | correct | high |
| [Q000066](runs/Q000066.md) | 0007 | Math, spectral combinatorics | exact match | no | correct | high |
| [Q000065](runs/Q000065.md) | 0007 | Statistics, model selection | exact match | no | correct | high |
| [Q000064](runs/Q000064.md) | 0007 | Medicine, pharmacy counseling | exact match | no | correct | medium |
| [Q000063](runs/Q000063.md) | 0007 | Archaeology, site identification | exact match | yes | correct | low |
| [Q000062](runs/Q000062.md) | 0007 | Engineering, textile permeability | exact match | no | correct | medium |
| [Q000061](runs/Q000061.md) | 0007 | Math, geometric reconstruction | exact match | yes | correct | high |
| [Q000060](runs/Q000060.md) | 0006 | Chemistry, phase-transfer catalysis | exact match | yes | correct | high |
| [Q000059](runs/Q000059.md) | 0006 | Game theory, mancala | multiple choice | no | incorrect | high |
| [Q000058](runs/Q000058.md) | 0006 | Games, Connect 4 tactics | exact match | no | incorrect | medium |
| [Q000057](runs/Q000057.md) | 0006 | Molecular biology, translation | exact match | no | correct | high |
| [Q000056](runs/Q000056.md) | 0006 | Physics, jammed packings | exact match | no | incorrect | medium |
| [Q000055](runs/Q000055.md) | 0006 | Math, Markov chains | exact match | no | incorrect | high |
| [Q000054](runs/Q000054.md) | 0006 | Math, combinatorial game theory | exact match | no | incorrect | high |
| [Q000053](runs/Q000053.md) | 0006 | Art history, attribution | exact match | yes | incorrect | very low |
| [Q000052](runs/Q000052.md) | 0006 | CS, combinatory logic | exact match | no | correct | high |
| [Q000051](runs/Q000051.md) | 0006 | CS, computational complexity | exact match | no | incorrect | high |
| [Q000050](runs/Q000050.md) | 0005 | Math, algebraic geometry | exact match | no | incorrect | high |
| [Q000049](runs/Q000049.md) | 0005 | Math, algebraic cocycles | exact match | no | correct | high |
| [Q000048](runs/Q000048.md) | 0005 | Math, analytic number theory | exact match | no | correct | high |
| [Q000047](runs/Q000047.md) | 0005 | Poetry, symbol interpretation | multiple choice | no | incorrect | medium |
| [Q000046](runs/Q000046.md) | 0005 | Oceanography, interfacial flow | multiple choice | no | incorrect | medium |
| [Q000045](runs/Q000045.md) | 0005 | CS, algorithm complexity | exact match | no | correct | medium |
| [Q000044](runs/Q000044.md) | 0005 | Engineering, pavement design | exact match | no | incorrect | high |
| [Q000043](runs/Q000043.md) | 0005 | Genetics, population model logic | multiple choice | no | incorrect | medium |
| [Q000042](runs/Q000042.md) | 0005 | Medicine, pain pharmacotherapy | multiple choice | no | incorrect | medium |
| [Q000041](runs/Q000041.md) | 0005 | Math, geometric measure theory | exact match | no | correct | high |
| [Q000040](runs/Q000040.md) | 0004 | Physics, variable-mass mechanics | exact match | no | correct | high |
| [Q000039](runs/Q000039.md) | 0004 | Chemistry, organic mechanism | exact match | yes | correct | medium |
| [Q000038](runs/Q000038.md) | 0004 | Ecology, settlement experiment | multiple choice | no | correct | medium |
| [Q000037](runs/Q000037.md) | 0004 | Logic, propositional | exact match | no | incorrect | medium |
| [Q000036](runs/Q000036.md) | 0004 | AI, deep learning theory | multiple choice | no | correct | medium |
| [Q000035](runs/Q000035.md) | 0004 | Law, securities regulation | multiple choice | no | correct | medium |
| [Q000034](runs/Q000034.md) | 0004 | Medicine, clinical vignette | multiple choice | no | incorrect | medium |
| [Q000033](runs/Q000033.md) | 0004 | Puzzle, cipher | exact match | no | correct | high |
| [Q000032](runs/Q000032.md) | 0004 | Neuroscience, comorbidity imaging | multiple choice | no | incorrect | medium |
| [Q000031](runs/Q000031.md) | 0004 | Math, mathematical physics PDE | exact match | no | incorrect | medium |
| [Q000030](runs/Q000030.md) | 0003 | Neuroscience, MEA recording | exact match | yes | incorrect | medium |
| [Q000029](runs/Q000029.md) | 0003 | Physics, gauge symmetry | multiple choice | no | incorrect | high |
| [Q000028](runs/Q000028.md) | 0003 | Veterinary medicine, ECG | exact match | yes | correct | high |
| [Q000027](runs/Q000027.md) | 0003 | Math, combinatorial geometry | exact match | no | incorrect | high |
| [Q000026](runs/Q000026.md) | 0003 | Math, algorithm engineering | exact match | no | correct | medium |
| [Q000025](runs/Q000025.md) | 0003 | Bioinformatics, network science | exact match | yes | incorrect | high |
| [Q000024](runs/Q000024.md) | 0003 | Biology, comparative genomics | multiple choice | yes | incorrect | medium |
| [Q000023](runs/Q000023.md) | 0003 | Engineering, semiconductor devices | exact match | yes | correct | high |
| [Q000022](runs/Q000022.md) | 0003 | Math, arithmetic groups | exact match | no | correct | high |
| [Q000021](runs/Q000021.md) | 0003 | Classics, paleography | exact match | yes | correct | medium |
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
| [Q000010](runs/Q000010.md) | 0001 | Engineering, simulation | exact match | no | incorrect | low |
| [Q000009](runs/Q000009.md) | 0001 | CS, model-based diagnosis | exact match | yes | correct | high |
| [Q000008](runs/Q000008.md) | 0001 | Film studies | multiple choice | no | incorrect | medium |
| [Q000007](runs/Q000007.md) | 0001 | Math, dynamical systems | multiple choice | no | correct | high |
| [Q000006](runs/Q000006.md) | 0001 | Art history | exact match | no | incorrect | low |
| [Q000005](runs/Q000005.md) | 0001 | CS, numeric formats | exact match | no | incorrect | medium |
| [Q000004](runs/Q000004.md) | 0001 | Biology/Medicine | exact match | no | incorrect | medium |
| [Q000003](runs/Q000003.md) | 0001 | Math, algorithms | multiple choice | no | incorrect | medium |
| [Q000002](runs/Q000002.md) | 0001 | Math | exact match | no | correct | high |
| [Q000001](runs/Q000001.md) | 0001 | Physics | exact match | no | correct | high |