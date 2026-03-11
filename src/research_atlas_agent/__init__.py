"""Utilities for reproducible experiment execution and reporting."""

from .analysis import RunSummary, collect_run_metadata, format_summary, summarize_runs
from .experiments import ExperimentResult, ExperimentSpec, run_experiment
from .profiling import (
    KERNEL_PLOTTING_PALETTES,
    available_palettes,
    load_kernel_profile_csv,
    plot_kernel_profile,
)

__all__ = [
    "ExperimentResult",
    "ExperimentSpec",
    "RunSummary",
    "collect_run_metadata",
    "format_summary",
    "KERNEL_PLOTTING_PALETTES",
    "available_palettes",
    "load_kernel_profile_csv",
    "plot_kernel_profile",
    "run_experiment",
    "summarize_runs",
]
