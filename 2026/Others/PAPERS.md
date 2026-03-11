# 2026 Other Papers

## [TiledAttention: a CUDA Tile SDPA Kernel for PyTorch]

- **Authors:** Taimur Khan
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** CUDA Kernels, GPU Optimization, Sparse Matrix & Kernels
- **Paper Link:** https://arxiv.org/abs/2603.01960
- **Code Link:** https://github.com/thisistaimur/TiledAttention

### Short Summary
TiledAttention provides a PyTorch-callable SDPA forward operator implemented in cuTile Python (TileIR), targeting rapid kernel research workflows on NVIDIA GPUs. The paper focuses on making kernel schedule changes easy from Python while preserving realistic behavior via online softmax and tiled streaming of keys and values. This directly addresses a tooling gap between very fast but hard-to-edit production kernels and easy-to-edit but slow research prototypes. The reported implementation enables reproducible benchmarking across sequence lengths, head dimensions, and FP16/BF16 settings. While it is not positioned as a universal production replacement, it demonstrates strong practical speedups over eager attention paths. In the atlas, this paper fits as a kernel-research enabler that can accelerate experimentation velocity.

### Core Innovation
- Editable, Python-level SDPA kernel research stack with realistic tiled execution behavior.
- Integration path that keeps kernels directly callable from PyTorch workflows.
- Balance between performance and modifiability for rapid attention-kernel iteration.

### Technical Approach
- SDPA forward is implemented with tiled key/value streaming and online softmax.
- Schedules (tile size, staging, shared-memory layout) are exposed for direct Python-level modification.
- A reproducible benchmark harness evaluates behavior against PyTorch SDPA auto-dispatch and unfused baselines.
- The approach emphasizes fast experimentation over exhaustive production specialization.

### Results
- The paper reports large speedups over standard eager attention execution paths.
- It shows practical competitiveness for research workflows while noting that highly fused production kernels remain stronger overall.
- Results support the claim that schedule-level editability can coexist with meaningful kernel performance.

### Potential Drawbacks
- The strongest production fused kernels still outperform it in many settings.
- The contribution is currently centered on forward SDPA and research experimentation use cases.
- Performance portability beyond the tested GPU/software stack is not yet established.
