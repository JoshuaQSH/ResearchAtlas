from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class RunSummary:
    total_runs: int
    success_runs: int
    failed_runs: int
    success_rate: float
    fastest_run_id: str | None
    fastest_duration_seconds: float | None


def collect_run_metadata(output_root: Path | str = "experiments/runs") -> list[dict]:
    """Load metadata.json from every run directory."""

    root = Path(output_root)
    if not root.exists():
        return []

    records: list[dict] = []
    for metadata_file in sorted(root.glob("*/metadata.json")):
        records.append(json.loads(metadata_file.read_text(encoding="utf-8")))
    return records


def summarize_runs(records: list[dict]) -> RunSummary:
    """Build a high-level summary over recorded experiment runs."""

    total = len(records)
    if total == 0:
        return RunSummary(0, 0, 0, 0.0, None, None)

    successes = [r for r in records if r["result"]["status"] == "success"]
    failures = total - len(successes)
    success_rate = len(successes) / total

    fastest_run_id: str | None = None
    fastest_duration: float | None = None
    for record in records:
        duration = float(record["result"]["duration_seconds"])
        if fastest_duration is None or duration < fastest_duration:
            fastest_duration = duration
            fastest_run_id = record["result"]["run_id"]

    return RunSummary(
        total,
        len(successes),
        failures,
        success_rate,
        fastest_run_id,
        fastest_duration,
    )


def format_summary(summary: RunSummary) -> str:
    """Render summary text for CLI output."""

    lines = [
        f"total_runs: {summary.total_runs}",
        f"success_runs: {summary.success_runs}",
        f"failed_runs: {summary.failed_runs}",
        f"success_rate: {summary.success_rate:.2%}",
    ]
    if summary.fastest_run_id is not None and summary.fastest_duration_seconds is not None:
        lines.append(
            f"fastest_run: {summary.fastest_run_id} ({summary.fastest_duration_seconds:.6f}s)"
        )
    return "\n".join(lines)
