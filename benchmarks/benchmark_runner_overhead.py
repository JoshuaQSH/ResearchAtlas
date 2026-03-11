from __future__ import annotations

import statistics
import sys
import tempfile
import time
from pathlib import Path

from research_atlas_agent.experiments import ExperimentSpec, run_experiment


def run_benchmark(rounds: int = 5) -> dict[str, float]:
    durations: list[float] = []
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_root = Path(tmp_dir)
        for _ in range(rounds):
            start = time.perf_counter()
            result = run_experiment(
                ExperimentSpec(name="bench", command=[sys.executable, "-c", "pass"]),
                output_root=output_root,
            )
            if result.return_code != 0:
                raise RuntimeError("Benchmark command failed")
            durations.append(time.perf_counter() - start)

    return {
        "rounds": float(rounds),
        "mean_seconds": statistics.mean(durations),
        "median_seconds": statistics.median(durations),
        "min_seconds": min(durations),
        "max_seconds": max(durations),
    }


def main() -> None:
    stats = run_benchmark()
    print("benchmark_runner_overhead")
    for key, value in stats.items():
        print(f"{key}: {value:.6f}")


if __name__ == "__main__":
    main()
