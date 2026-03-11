from __future__ import annotations

from pathlib import Path

from research_atlas_agent.profiling import (
    KERNEL_PLOTTING_PALETTES,
    available_palettes,
    load_kernel_profile_csv,
    plot_kernel_profile,
)


def test_available_palettes() -> None:
    assert set(available_palettes()) == {"blue", "slate", "violet"}
    assert KERNEL_PLOTTING_PALETTES["violet"][0] == "#ECDFFF"


def test_load_profile_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "profile.csv"
    csv_path.write_text(
        "kernel_name,duration_ms\nflash_fwd,2.1\nlayernorm,1.0\n",
        encoding="utf-8",
    )
    rows = load_kernel_profile_csv(csv_path)
    assert len(rows) == 2
    assert rows[0]["kernel_name"] == "flash_fwd"
    assert rows[0]["duration_ms"] == 2.1


def test_plot_kernel_profile(tmp_path: Path) -> None:
    rows = [
        {"kernel_name": "kernel_a", "duration_ms": 2.4},
        {"kernel_name": "kernel_b", "duration_ms": 1.2},
        {"kernel_name": "kernel_c", "duration_ms": 3.7},
    ]
    output_path = tmp_path / "plot.png"
    result = plot_kernel_profile(rows=rows, output_path=output_path, palette="blue", top_k=2)
    assert result == output_path
    assert output_path.exists()
    assert output_path.stat().st_size > 0
