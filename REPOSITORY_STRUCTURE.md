# Repository Structure

## Top-level directories and files
- `AGENT.md`: Operational charter for first-principles coding and experiment execution.
- `README.md`: Branch overview, setup, workflows, and reproducibility commands.
- `pyproject.toml`: Python package metadata, dependency definitions, and tool config.
- `Dockerfile`: Containerized reproducible environment for tests and workflows.
- `.github/workflows/ci.yml`: Pull-request CI pipeline running lint and tests.
- `src/research_atlas_agent/`: Core implementation package.
- `tests/`: Unit tests using `pytest`.
- `benchmarks/`: Benchmark scripts and benchmark instructions.
- `demos/`: Small demo scripts for end-to-end smoke validation.
- `skills/code-experiments-agent/`: Skill configuration for branch-focused autonomous coding workflows.

## Core implementation map
- Experiment execution engine: `src/research_atlas_agent/experiments.py`
- Run metadata loading and summaries: `src/research_atlas_agent/analysis.py`
- Command line interface: `src/research_atlas_agent/cli.py`

## Test coverage map
- Experiment execution tests: `tests/test_experiments.py`
- Metadata and summary tests: `tests/test_analysis.py`
- CLI behavior tests: `tests/test_cli.py`

## Benchmark map
- Runner overhead benchmark: `benchmarks/benchmark_runner_overhead.py`
