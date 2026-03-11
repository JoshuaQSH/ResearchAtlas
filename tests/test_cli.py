from __future__ import annotations

import json
import sys
from pathlib import Path

from research_atlas_agent.cli import main


def test_cli_run_and_summarize(tmp_path: Path, capsys) -> None:
    rc = main(
        [
            "run",
            "--name",
            "cli-smoke",
            "--output-root",
            str(tmp_path),
            "--",
            sys.executable,
            "-c",
            "print('cli')",
        ]
    )
    assert rc == 0

    run_output = capsys.readouterr().out
    payload = json.loads(run_output)
    assert payload["status"] == "success"

    rc = main(["summarize", "--output-root", str(tmp_path)])
    assert rc == 0
    summary_output = capsys.readouterr().out
    assert "total_runs: 1" in summary_output
