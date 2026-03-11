---
name: code-experiments-agent
description: Build, debug, and maintain reproducible code-and-experiment workflows for AI research projects. Use when tasks require implementation, test-backed validation, experiment execution, benchmark analysis, Docker/CI setup, or reproducibility hardening.
---

# Code Experiments Agent

## Workflow
1. Clarify the user need from first principles before implementation.
2. If the motivation or goal is unclear, pause and discuss with the user.
3. If the path is valid but not shortest, explain and propose a better route.
4. Implement one module at a time.
5. After each module, write and run tests immediately.
6. Report what was built, provide test evidence, and wait for confirmation before major next modules.

## Non-Negotiable Rules
1. Never claim anything works without running tests.
2. Iterate and fix errors proactively by running the code and inspecting outputs.
3. State unknowns explicitly; never guess.
4. Prefer `uv` for environment and dependency management.
5. Use `pip3` only when `uv` is unavailable or cannot satisfy package constraints.
6. Keep a clear and reproducible `pyproject.toml`.
7. Use CMake for all C/C++/CUDA code (`CMakeLists.txt` required).
8. Maintain complete `pytest` unit tests for each implemented module.
9. Provide a small demo to validate end-to-end behavior.
10. Keep Docker reproducibility ready and verify containerized tests before claiming success.
11. Keep GitHub Actions CI ready so PRs must pass tests.
12. Keep a `benchmarks/` directory ready and run benchmarks when performance is relevant.
13. Maintain a repository-structure markdown file that maps implementations to concrete file paths.
14. Keep a `profiling/` directory ready for model and kernel profiling workflows.
15. Maintain at least one reusable visualization helper for profiling-result plots.
16. Use `wandb` to track model training when experiment tracking is needed.
17. Prefer these plotting palettes:
    - Violet set: `#ECDFFF`, `#D4C4EE`, `#BDAADE`, `#A690CF`, `#8E78BF`, `#8C75BC`, `#6A579C`
    - Blue set: `#aed0ee`, `#88abda`, `#6f94cd`, `#5976ba`, `#2e59a7`, `#145ca0`
    - Slate-blue set: `#3658a1`, `#7393c6`, `#8ba8d6`, `#a4b8db`, `#d3e1ef`, `#d2dee5`, `#bdcbd7`, `#b7d3dd`, `#99b4cc`, `#82a4ca`

## Branch Policy
- This branch is code and experiments only.
- Do not add paper-catalog content from the atlas workflow here.
- Keep PR quality strict: objective, implementation summary, commands executed, test results, and benchmark notes.

## References
- Use `references/repro-playbook.md` for canonical host, Docker, benchmark, and lint/test command sets.
