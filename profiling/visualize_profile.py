from __future__ import annotations

import argparse
from pathlib import Path

from research_atlas_agent.profiling import (
    available_palettes,
    load_kernel_profile_csv,
    plot_kernel_profile,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Visualize kernel profiling CSV files")
    parser.add_argument("--input-csv", required=True, help="Path to profiling CSV")
    parser.add_argument("--output-png", required=True, help="Output figure path")
    parser.add_argument("--top-k", type=int, default=15, help="Number of kernels to plot")
    parser.add_argument(
        "--palette",
        default="violet",
        choices=available_palettes(),
        help="Color palette for bars",
    )
    parser.add_argument(
        "--title",
        default="Kernel Duration Profile",
        help="Plot title",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    rows = load_kernel_profile_csv(Path(args.input_csv))
    output = plot_kernel_profile(
        rows=rows,
        output_path=Path(args.output_png),
        palette=args.palette,
        top_k=args.top_k,
        title=args.title,
    )
    print(f"Wrote: {output}")


if __name__ == "__main__":
    main()
