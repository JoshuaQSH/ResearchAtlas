# Reproducibility Playbook

## Environment
- Prefer `uv` for dependency and virtual environment management.
- Fallback to `pip3` only if `uv` cannot satisfy dependency constraints.

## Core commands
```bash
uv sync --dev
uv run pytest
uv run ruff check .
uv run research-atlas run --name smoke -- python -c "print('ok')"
uv run research-atlas summarize
```

## Docker commands
```bash
docker build -t researchatlas-code-lab .
docker run --rm researchatlas-code-lab
```

## Benchmark command
```bash
uv run python benchmarks/benchmark_runner_overhead.py
```

## C/C++/CUDA policy
- Always require a top-level or module-level `CMakeLists.txt` for C/C++/CUDA additions.
- Include build and test commands in README and PR notes.
