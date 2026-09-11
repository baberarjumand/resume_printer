#!/usr/bin/env python3
"""Aggregate grading.json files into benchmark.json for an eval iteration.

Usage:
  python3 scripts/eval_aggregate.py --iteration /path/to/evals-workspace/iteration-1

Scans */with_skill/grading.json and */without_skill/grading.json (or old_skill/).
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path


def collect(iteration: Path, label: str) -> list[dict]:
    reports = []
    for path in iteration.glob(f"*/{label}/grading.json"):
        reports.append(json.loads(path.read_text(encoding="utf-8")))
    return reports


def summarize(reports: list[dict]) -> dict:
    if not reports:
        return {
            "pass_rate": {"mean": 0.0, "stddev": 0.0, "n": 0},
            "evals": 0,
        }
    rates = [r["summary"]["pass_rate"] for r in reports]
    return {
        "pass_rate": {
            "mean": statistics.mean(rates),
            "stddev": statistics.pstdev(rates) if len(rates) > 1 else 0.0,
            "n": len(rates),
        },
        "evals": len(rates),
        "raw": [
            {
                "slug": r.get("slug"),
                "pass_rate": r["summary"]["pass_rate"],
                "passed": r["summary"]["passed"],
                "failed": r["summary"]["failed"],
            }
            for r in reports
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate eval grading into benchmark.json")
    parser.add_argument("--iteration", type=Path, required=True)
    args = parser.parse_args()
    iteration = args.iteration.resolve()
    if not iteration.is_dir():
        print(f"Error: iteration dir not found: {iteration}", file=sys.stderr)
        sys.exit(1)

    with_skill = summarize(collect(iteration, "with_skill"))
    without = summarize(collect(iteration, "without_skill"))
    if without["evals"] == 0:
        without = summarize(collect(iteration, "old_skill"))

    delta = {
        "pass_rate": with_skill["pass_rate"]["mean"] - without["pass_rate"]["mean"],
    }
    benchmark = {
        "run_summary": {
            "with_skill": with_skill,
            "without_skill": without,
            "delta": delta,
        }
    }
    out = iteration / "benchmark.json"
    out.write_text(json.dumps(benchmark, indent=2), encoding="utf-8")
    print(json.dumps(benchmark, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
