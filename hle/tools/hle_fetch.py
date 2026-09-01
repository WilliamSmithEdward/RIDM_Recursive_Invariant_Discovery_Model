"""Fetch and grade Humanity's Last Exam questions one at a time for RIDM runs.

Code only: this file contains no benchmark content. Question data comes from the locally
cached, gated Hugging Face dataset `cais/hle` and stays on the local machine. All mutable
state (the seen-id log and decoded images) lives in a data directory outside the repository
tree, so no gated content or dataset id can enter version control.

Fetch commands print the question id, safe metadata, and question text, and decode any
question image to a file. They never print the answer, rationale, or canary. Grading happens
only through --reveal, and --reveal is interlocked: it refuses to run until the answer has
been recorded with --commit, so a premature reveal is structurally impossible rather than
merely prohibited (RIDM oracle-sequencing law).

Usage:
  python hle_fetch.py --random [--text-only] [--category NAME]
  python hle_fetch.py --id QUESTION_ID
  python hle_fetch.py --commit QUESTION_ID "committed answer"
  python hle_fetch.py --reveal QUESTION_ID
  python hle_fetch.py --stats

State:
  Data directory: RIDM_HLE_DIR environment variable if set, otherwise ~/.ridm_hle
  Seen log:       <data dir>/seen_ids.txt (one id per line, # comments allowed)
  Commit log:     <data dir>/commits.txt (tab-separated: id, UTC time, committed answer)
  Images:         <data dir>/images/<id>[_rationale].<ext>

Any fetched or revealed id is appended to the seen log, so --random never repeats a
question whose text has already been exposed. The commit log lives outside the repository
with the rest of the state, so committed answers never enter version control.
"""

import argparse
import base64
import random
import re
import sys
from collections import Counter
from pathlib import Path

SAFE_META = ("category", "raw_subject", "answer_type")

DATA_URI_RE = re.compile(
    r"^data:image/(?P<ext>[a-zA-Z0-9.+-]+);base64,(?P<b64>.*)$", re.DOTALL
)


def data_dir():
    import os

    root = Path(os.environ.get("RIDM_HLE_DIR", "") or Path.home() / ".ridm_hle")
    (root / "images").mkdir(parents=True, exist_ok=True)
    return root


def load_seen(root):
    path = root / "seen_ids.txt"
    if not path.exists():
        return set()
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            seen.add(line.split()[0])
    return seen


def mark_seen(root, qid):
    if qid in load_seen(root):
        return
    with (root / "seen_ids.txt").open("a", encoding="utf-8") as f:
        f.write(qid + "\n")


def load_dataset_rows():
    from datasets import load_dataset

    return load_dataset("cais/hle", split="test")


def row_by_id(ds, qid):
    try:
        index = ds["id"].index(qid)
    except ValueError:
        sys.exit(f"id not found in dataset: {qid}")
    return ds[index]


def save_image(value, dest_stem, root):
    """Write an image field (data-URI string or PIL image) to the images dir; return path."""
    if value is None:
        return None
    images = root / "images"
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        match = DATA_URI_RE.match(text)
        if not match:
            return None
        ext = match.group("ext").lower()
        ext = {"jpeg": "jpg", "svg+xml": "svg"}.get(ext, ext)
        path = images / f"{dest_stem}.{ext}"
        path.write_bytes(base64.b64decode(match.group("b64")))
        return path
    if hasattr(value, "save"):
        path = images / f"{dest_stem}.png"
        value.save(path)
        return path
    return None


def print_question(row, root):
    qid = row["id"]
    print("=" * 78)
    print(f"id: {qid}")
    for key in SAFE_META:
        if key in row:
            print(f"{key}: {row[key]}")
    image_path = save_image(row.get("image"), qid, root)
    print(f"image: {image_path if image_path else 'none'}")
    print("-" * 78)
    print(row["question"])
    print("=" * 78)
    mark_seen(root, qid)


def cmd_random(args):
    root = data_dir()
    seen = load_seen(root)
    ds = load_dataset_rows()
    ids = ds["id"]
    pool = [i for i, qid in enumerate(ids) if qid not in seen]
    if args.category:
        categories = ds["category"]
        want = args.category.lower()
        pool = [i for i in pool if want in categories[i].lower()]
    if not pool:
        sys.exit("no unseen questions match the filters")
    rng = random.SystemRandom()
    rng.shuffle(pool)
    for index in pool:
        row = ds[index]
        if args.text_only and isinstance(row.get("image"), str) and row["image"].strip():
            continue
        print_question(row, root)
        return
    sys.exit("no unseen questions match the filters")


def cmd_id(qid):
    root = data_dir()
    print_question(row_by_id(load_dataset_rows(), qid), root)


def load_commits(root):
    path = root / "commits.txt"
    if not path.exists():
        return set()
    committed = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            committed.add(line.split("\t")[0])
    return committed


def cmd_commit(qid, answer):
    from datetime import datetime, timezone

    root = data_dir()
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with (root / "commits.txt").open("a", encoding="utf-8") as f:
        f.write(f"{qid}\t{stamp}\t{answer}\n")
    print(f"committed answer recorded for {qid} at {stamp}")
    print("reveal is now unlocked for this id")


def cmd_reveal(qid):
    root = data_dir()
    if qid not in load_commits(root):
        sys.exit(
            "reveal refused: no committed answer recorded for this id.\n"
            "Record the commitment first:\n"
            f'  python hle_fetch.py --commit {qid} "your committed answer"\n'
            "A reveal before commitment spends the item and voids the run."
        )
    row = row_by_id(load_dataset_rows(), qid)
    print("=" * 78)
    print(f"id: {row['id']}")
    print(f"answer_type: {row.get('answer_type')}")
    print("-" * 78)
    print("ANSWER:")
    print(row["answer"])
    print("-" * 78)
    print("RATIONALE:")
    print(row.get("rationale") or "(none)")
    rationale_image = save_image(row.get("rationale_image"), f"{qid}_rationale", root)
    if rationale_image:
        print(f"rationale image: {rationale_image}")
    print("=" * 78)
    mark_seen(root, qid)


def cmd_stats():
    root = data_dir()
    seen = load_seen(root)
    ds = load_dataset_rows()
    ids = ds["id"]
    unseen = sum(1 for qid in ids if qid not in seen)
    print(f"total questions: {len(ids)}")
    print(f"seen ids logged: {len(seen)}")
    print(f"unseen remaining: {unseen}")
    for name, count in Counter(ds["category"]).most_common():
        print(f"  {name}: {count}")
    print(f"data dir: {root}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(
        description="Fetch and grade HLE questions one at a time for RIDM runs."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--random", action="store_true", help="print one unseen question")
    group.add_argument("--id", metavar="QUESTION_ID", help="print one specific question")
    group.add_argument(
        "--commit",
        nargs=2,
        metavar=("QUESTION_ID", "ANSWER"),
        help="record the committed answer; required before --reveal for that id",
    )
    group.add_argument(
        "--reveal",
        metavar="QUESTION_ID",
        help="print the answer and rationale for grading (requires a prior --commit)",
    )
    group.add_argument("--stats", action="store_true", help="dataset and seen-log summary")
    parser.add_argument(
        "--text-only", action="store_true", help="with --random, skip questions with images"
    )
    parser.add_argument(
        "--category", metavar="NAME", help="with --random, filter by category substring"
    )
    args = parser.parse_args()
    if args.random:
        cmd_random(args)
    elif args.id:
        cmd_id(args.id)
    elif args.commit:
        cmd_commit(args.commit[0], args.commit[1])
    elif args.reveal:
        cmd_reveal(args.reveal)
    else:
        cmd_stats()


if __name__ == "__main__":
    main()
