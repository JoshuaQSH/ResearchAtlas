# ResearchAtlas Code & Experiments Branch

This branch is a code-first, experiment-first workspace for reproducible AI systems research engineering.
It replaces the paper-catalog workflow from `master` with an implementation/debug/benchmark workflow.

## Scope
- Implement and debug modules with strict test-backed claims.
- Run experiments with persisted logs and metadata.
- Analyze run outcomes with reproducible summaries.
- Maintain Docker and CI so collaborators can reproduce results quickly.

## Quick Start (Host)
```bash
uv sync --dev
uv run pytest
uv run research-atlas run --name smoke -- python -c "print('ok')"
uv run research-atlas summarize
```

## Quick Start (Docker)
```bash
docker build -t researchatlas-code-lab .
docker run --rm researchatlas-code-lab
```

## Reproducibility Workflow
1. Implement one module.
2. Write and run unit tests immediately.
3. Run a smoke experiment and persist logs under `experiments/runs/`.
4. Summarize results with `research-atlas summarize`.
5. Include exact commands and outputs in PR descriptions.

## Benchmarking
```bash
uv run python benchmarks/benchmark_runner_overhead.py
```

## Profiling
```bash
uv run python profiling/visualize_profile.py \
  --input-csv profiling/samples/kernel_profile_example.csv \
  --output-png profiling/samples/kernel_profile_example.png \
  --palette violet
```

## Optional Tracking (`wandb`)
```bash
uv sync --dev --extra tracking
```

## PR Rules
- Every PR must pass `.github/workflows/ci.yml`.
- Every behavior claim must include test evidence.
- Every experiment claim must include reproducible run commands.
- Benchmark-impacting changes should include benchmark deltas.

## Related branch policy
See `AGENT.md` for first-principles operating rules and execution constraints.
