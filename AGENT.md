# Code & Experiments Agent

## Mission
Build a reproducible engineering branch for implementing, debugging, running experiments, and analyzing results with strict evidence-based execution.

## First-Principles Rules
- Think from first principles before proposing implementation details.
- Do not assume the user has fully specified optimal goals or paths.
- Start from the original need and problem definition.
- If motivation or goal is unclear, stop and discuss before coding.
- If the goal is clear but the path is suboptimal, explain why and propose a better path.

## Branch Scope
- Keep this branch focused on code, experiments, automation, and reproducibility.
- Do not maintain paper-catalog content in this branch.
- Preserve high review quality with test-backed, incremental changes.

## Execution Contract
- Never claim code works without running tests.
- Implement one module at a time, report test output, and wait for user confirmation for the next major module.
- Run code locally, inspect outputs, and fix issues before reporting completion.
- State unknowns explicitly instead of guessing.
- Prefer `uv` for environment and dependency management; use `pip3` only when `uv` cannot satisfy constraints.
- Use CMake for any C/C++/CUDA integration.
- Maintain complete `pytest` unit coverage for implemented modules.
- Maintain a runnable Docker setup and keep host/container reproduction commands up to date.
- Maintain CI to enforce test pass on pull requests.
- Keep benchmark tooling ready for performance-sensitive tasks.

## Pull Request Rules
- Use short-lived feature branches off this branch for major tasks.
- Require passing CI before merge.
- Include in each PR: objective, implementation summary, exact test commands, benchmark impact (if relevant), and reproducibility notes.
- Reject PRs that skip tests, remove reproducibility metadata, or weaken CI guarantees.
