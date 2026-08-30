# HLE Run Log

This directory records the application of RIDM to questions from Humanity's Last Exam (HLE),
one question at a time. The runs stress the specification against closed-book problems at the
edge of answerability, and the lessons feed the next RIDM version.

## Privacy Policy

Out of respect for the HLE project's terms, no benchmark content appears here: no question
text, no answers, no rationale content, no dataset identifiers, and no images. Logs are
process-level only. Each run is identified by a sequential run number, its subject category,
its answer format, and the outcome.

## Method

- Each attempt is closed book: no web search, no external tools beyond reading the question.
- RIDM governs the attempt: task contract, claim typing, materiality, hard gates, and an
  honest confidence statement.
- The answer is committed in writing before the official answer is revealed.
- Grading is strict. A near miss counts as incorrect and is noted as such.
- After grading, the run log records where RIDM helped, where it misled, and where it was
  silent. Distilled lessons accumulate in [LESSONS.md](LESSONS.md).

## Layout

| Path | Purpose |
| --- | --- |
| `runs/Q001.md`, `runs/Q002.md`, ... | One log per attempted question |
| [LESSONS.md](LESSONS.md) | Accumulated framework lessons driving the next version |
