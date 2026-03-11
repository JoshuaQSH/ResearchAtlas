#!/usr/bin/env bash
set -euo pipefail

uv run research-atlas run --name smoke-demo -- python -c "print('demo-ok')"
uv run research-atlas summarize
