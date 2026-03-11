from __future__ import annotations

import json
import os
import subprocess
from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_OUTPUT_ROOT = Path("experiments/runs")


@dataclass(slots=True)
class ExperimentSpec:
    """A single experiment execution plan."""

    name: str
    command: Sequence[str]
    workdir: str = "."
    env: Mapping[str, str] = field(default_factory=dict)
    seed: int | None = None


@dataclass(slots=True)
class ExperimentResult:
    """Execution result and artifact locations for an experiment run."""

    run_id: str
    name: str
    command: list[str]
    return_code: int
    status: str
    started_at: str
    ended_at: str
    duration_seconds: float
    run_dir: str
    stdout_path: str
    stderr_path: str
    metadata_path: str


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _sanitize_name(name: str) -> str:
    sanitized = "".join(ch.lower() if ch.isalnum() else "-" for ch in name.strip())
    sanitized = "-".join(part for part in sanitized.split("-") if part)
    return sanitized or "experiment"


def _create_run_dir(output_root: Path, name: str) -> tuple[str, Path]:
    output_root.mkdir(parents=True, exist_ok=True)
    base_id = f"{_utc_now().strftime('%Y%m%dT%H%M%SZ')}_{_sanitize_name(name)}"
    run_id = base_id
    run_dir = output_root / run_id
    suffix = 1
    while run_dir.exists():
        run_id = f"{base_id}_{suffix}"
        run_dir = output_root / run_id
        suffix += 1
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_id, run_dir


def run_experiment(
    spec: ExperimentSpec,
    output_root: Path | str = DEFAULT_OUTPUT_ROOT,
) -> ExperimentResult:
    """Run one experiment command and persist reproducibility artifacts."""

    command = list(spec.command)
    if not command:
        raise ValueError("Experiment command cannot be empty")

    root = Path(output_root)
    run_id, run_dir = _create_run_dir(root, spec.name)

    started = _utc_now()
    stdout_path = run_dir / "stdout.log"
    stderr_path = run_dir / "stderr.log"

    child_env = os.environ.copy()
    child_env.update({str(k): str(v) for k, v in spec.env.items()})
    if spec.seed is not None:
        child_env.setdefault("PYTHONHASHSEED", str(spec.seed))
        child_env.setdefault("SEED", str(spec.seed))

    with stdout_path.open("w", encoding="utf-8") as stdout_file, stderr_path.open(
        "w", encoding="utf-8"
    ) as stderr_file:
        completed = subprocess.run(
            command,
            cwd=spec.workdir,
            env=child_env,
            check=False,
            stdout=stdout_file,
            stderr=stderr_file,
            text=True,
        )

    ended = _utc_now()
    duration = (ended - started).total_seconds()
    status = "success" if completed.returncode == 0 else "failed"

    result = ExperimentResult(
        run_id=run_id,
        name=spec.name,
        command=command,
        return_code=completed.returncode,
        status=status,
        started_at=started.isoformat(),
        ended_at=ended.isoformat(),
        duration_seconds=round(duration, 6),
        run_dir=str(run_dir),
        stdout_path=str(stdout_path),
        stderr_path=str(stderr_path),
        metadata_path=str(run_dir / "metadata.json"),
    )

    metadata = {
        "spec": asdict(spec),
        "result": asdict(result),
    }
    Path(result.metadata_path).write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    return result
