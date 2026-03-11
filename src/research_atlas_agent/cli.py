from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .analysis import collect_run_metadata, format_summary, summarize_runs
from .experiments import ExperimentSpec, run_experiment


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="research-atlas",
        description="Run and summarize reproducible experiment executions.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one experiment command")
    run_parser.add_argument("--name", required=True, help="Experiment name")
    run_parser.add_argument(
        "--output-root",
        default="experiments/runs",
        help="Directory where run artifacts are written",
    )
    run_parser.add_argument("--workdir", default=".", help="Working directory for the command")
    run_parser.add_argument("--seed", type=int, default=None, help="Optional deterministic seed")
    run_parser.add_argument(
        "command_parts",
        nargs=argparse.REMAINDER,
        help="Command to run, prefixed by --, e.g. -- python -m pytest",
    )

    summarize_parser = subparsers.add_parser("summarize", help="Summarize previous runs")
    summarize_parser.add_argument(
        "--output-root",
        default="experiments/runs",
        help="Directory containing run artifacts",
    )
    return parser


def _normalize_command(command_parts: list[str]) -> list[str]:
    while command_parts and command_parts[0] == "--":
        command_parts = command_parts[1:]
    if not command_parts:
        raise ValueError("No experiment command provided. Use -- before the command.")
    return command_parts


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        command = _normalize_command(args.command_parts)
        spec = ExperimentSpec(
            name=args.name,
            command=command,
            workdir=args.workdir,
            seed=args.seed,
        )
        result = run_experiment(spec=spec, output_root=Path(args.output_root))
        print(json.dumps(asdict(result), indent=2))
        return 0 if result.return_code == 0 else result.return_code

    if args.command == "summarize":
        records = collect_run_metadata(Path(args.output_root))
        summary = summarize_runs(records)
        print(format_summary(summary))
        return 0

    parser.print_help()
    return 2


def entrypoint() -> None:
    raise SystemExit(main())


if __name__ == "__main__":
    entrypoint()
