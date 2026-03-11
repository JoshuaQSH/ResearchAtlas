from __future__ import annotations

import csv
from collections.abc import Iterable, Sequence
from pathlib import Path

KERNEL_PLOTTING_PALETTES: dict[str, list[str]] = {
    "violet": [
        "#ECDFFF",
        "#D4C4EE",
        "#BDAADE",
        "#A690CF",
        "#8E78BF",
        "#8C75BC",
        "#6A579C",
    ],
    "blue": [
        "#aed0ee",
        "#88abda",
        "#6f94cd",
        "#5976ba",
        "#2e59a7",
        "#145ca0",
    ],
    "slate": [
        "#3658a1",
        "#7393c6",
        "#8ba8d6",
        "#a4b8db",
        "#d3e1ef",
        "#d2dee5",
        "#bdcbd7",
        "#b7d3dd",
        "#99b4cc",
        "#82a4ca",
    ],
}


def available_palettes() -> list[str]:
    """Return supported plotting palette names."""

    return sorted(KERNEL_PLOTTING_PALETTES)


def load_kernel_profile_csv(
    csv_path: Path | str,
    kernel_field: str = "kernel_name",
    duration_field: str = "duration_ms",
) -> list[dict[str, object]]:
    """Load kernel profiling rows from a CSV file."""

    rows: list[dict[str, object]] = []
    path = Path(csv_path)
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            kernel_name = row.get(kernel_field)
            duration_text = row.get(duration_field)
            if kernel_name is None or duration_text is None:
                raise ValueError(
                    f"Missing required fields: '{kernel_field}' and "
                    f"'{duration_field}' in {csv_path}"
                )
            rows.append(
                {
                    "kernel_name": str(kernel_name),
                    "duration_ms": float(duration_text),
                }
            )
    return rows


def _normalize_rows(rows: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    normalized: list[dict[str, object]] = []
    for row in rows:
        kernel_name = row.get("kernel_name")
        duration_value = row.get("duration_ms")
        if kernel_name is None or duration_value is None:
            raise ValueError("Each row must include 'kernel_name' and 'duration_ms'")
        normalized.append(
            {
                "kernel_name": str(kernel_name),
                "duration_ms": float(duration_value),
            }
        )
    return normalized


def plot_kernel_profile(
    rows: Sequence[dict[str, object]],
    output_path: Path | str,
    palette: str = "violet",
    top_k: int = 15,
    title: str = "Kernel Duration Profile",
) -> Path:
    """Plot the top-k kernels by duration and save a PNG figure."""

    if palette not in KERNEL_PLOTTING_PALETTES:
        options = ", ".join(available_palettes())
        raise ValueError(f"Unknown palette '{palette}'. Use one of: {options}")

    normalized = _normalize_rows(rows)
    if not normalized:
        raise ValueError("No profiling rows provided")

    selected = sorted(normalized, key=lambda item: float(item["duration_ms"]), reverse=True)[:top_k]
    labels = [str(item["kernel_name"]) for item in reversed(selected)]
    values = [float(item["duration_ms"]) for item in reversed(selected)]

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    colors = KERNEL_PLOTTING_PALETTES[palette]
    bar_colors = [colors[idx % len(colors)] for idx in range(len(values))]

    figure_height = max(4.0, 0.45 * len(values))
    fig, axis = plt.subplots(figsize=(12, figure_height))
    axis.barh(labels, values, color=bar_colors)
    axis.set_xlabel("Duration (ms)")
    axis.set_ylabel("Kernel")
    axis.set_title(title)
    axis.grid(axis="x", linestyle="--", alpha=0.3)

    for idx, value in enumerate(values):
        axis.text(value, idx, f" {value:.3f}", va="center", ha="left", fontsize=9)

    fig.tight_layout()
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=160)
    plt.close(fig)
    return destination
