from __future__ import annotations

import sys
from pathlib import Path

from research_atlas_agent.analysis import collect_run_metadata, summarize_runs
from research_atlas_agent.experiments import ExperimentSpec, run_experiment


def test_collect_and_summarize(tmp_path: Path) -> None:
    run_experiment(
        ExperimentSpec(name="ok", command=[sys.executable, "-c", "print('ok')"]),
        output_root=tmp_path,
    )
    run_experiment(
        ExperimentSpec(name="fail", command=[sys.executable, "-c", "import sys; sys.exit(2)"]),
        output_root=tmp_path,
    )

    records = collect_run_metadata(tmp_path)
    summary = summarize_runs(records)

    assert len(records) == 2
    assert summary.total_runs == 2
    assert summary.success_runs == 1
    assert summary.failed_runs == 1
    assert summary.fastest_run_id is not None
