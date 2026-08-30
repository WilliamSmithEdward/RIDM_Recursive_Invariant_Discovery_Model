# Run Tools

Persistent tooling for the one-at-a-time HLE runs, kept in the repository so it survives
evaluation sessions. Code only: the tools contain no benchmark content, and they keep all
mutable state outside the repository tree so no gated question data or dataset id can enter
version control.

## hle_fetch.py

Fetches one question at a time from the locally cached, gated `cais/hle` dataset and grades
it after the answer has been committed in writing.

```bash
python hle_fetch.py --random [--text-only] [--category NAME]
python hle_fetch.py --id QUESTION_ID
python hle_fetch.py --reveal QUESTION_ID
python hle_fetch.py --stats
```

- Fetch commands print the question id, category, subject, answer type, and question text,
  and decode any question image to a local file. They never print the answer, rationale, or
  canary field.
- `--reveal` prints the official answer and rationale for strict self-grading, and is run
  only after the attempt's answer is committed.
- Every fetched or revealed id is appended to a seen-id log, so `--random` never repeats a
  question whose text has already been exposed.

## State and privacy

State lives in `~/.ridm_hle` (override with the `RIDM_HLE_DIR` environment variable):
`seen_ids.txt` holds one dataset id per line, and `images/` holds decoded question images.
That directory is deliberately outside the repository. Dataset access requires the operator's
own Hugging Face authentication and an accepted dataset gate; the tools never handle tokens.
