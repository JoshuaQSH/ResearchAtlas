from __future__ import annotations

import json
import sys
from pathlib import Path

from research_atlas_agent.experiments import ExperimentSpec, run_experiment


def test_run_experiment_success(tmp_path: Path) -> None:
    spec = ExperimentSpec(
        name="smoke success",
        command=[sys.executable, "-c", "print('ready')"],
    )

    result = run_experiment(spec, output_root=tmp_path)

    assert result.return_code == 0
    assert result.status == "success"
    assert Path(result.stdout_path).read_text(encoding="utf-8").strip() == "ready"

    metadata = json.loads(Path(result.metadata_path).read_text(encoding="utf-8"))
    assert metadata["spec"]["name"] == "smoke success"
    assert metadata["result"]["status"] == "success"


def test_run_experiment_failure(tmp_path: Path) -> None:
    spec = ExperimentSpec(
        name="smoke failure",
        command=[sys.executable, "-c", "import sys; print('bad'); sys.exit(3)"],
    )

    result = run_experiment(spec, output_root=tmp_path)

    assert result.return_code == 3
    assert result.status == "failed"
