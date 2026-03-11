# Profiling Workspace

This directory stores model and kernel profiling utilities and artifacts.

## Layout
- `visualize_profile.py`: CLI helper that converts kernel profiling CSV files into plots.
- `samples/kernel_profile_example.csv`: Example kernel profile input file.

## Expected CSV format
- `kernel_name`: Kernel identifier.
- `duration_ms`: Kernel duration in milliseconds.

## Generate a plot
```bash
uv run python profiling/visualize_profile.py \
  --input-csv profiling/samples/kernel_profile_example.csv \
  --output-png profiling/samples/kernel_profile_example.png \
  --palette violet \
  --top-k 10
```

## Palette sets
- `violet`, `blue`, and `slate`
