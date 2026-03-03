# 2022 Compiler Papers

## [TensorIR: An Abstraction for Automatic Tensorized Program Optimization]

- **Authors:** Tianqi Chen et al.
- **Venue:** OSDI 2022
- **Year:** 2022
- **Tags:** Compiler Optimization, MLIR, GPU Optimization
- **Paper Link:** https://www.usenix.org/conference/osdi22/presentation/zheng-lianmin
- **Code Link:** https://github.com/apache/tvm

### Short Summary
TensorIR extends the TVM stack with an intermediate representation aimed at making tensorized schedule generation more explicit and programmable. The paper matters because it bridges the gap between high-level graph optimization and the low-level schedule details needed for modern accelerators. It supports transformation primitives that are expressive enough for tensor cores, memory hierarchy control, and auto-tuning workflows. By exposing schedule structure in the IR, it makes both manual optimization and automated search easier to reason about. The result is a compiler abstraction that fits modern ML operators better than earlier black-box schedule templates.

### Core Innovation
- IR design that explicitly represents tensor program structure and scheduling decisions.
- Better support for auto-tuning and accelerator-specific tensorization.
- A unified abstraction that connects manual scheduling and compiler automation.

### Technical Approach
- Tensor programs are represented with explicit loop, block, and memory constructs.
- Scheduling transformations rewrite the IR while preserving semantics.
- Auto-tuning searches over legal transformations to optimize generated kernels.

### Results
- Evaluated on common ML operators and end-to-end workloads on modern accelerators.
- The paper reports strong performance against prior compiler baselines and vendor libraries in several settings.
- Results show the value of exposing schedule structure directly in the IR.

### Potential Drawbacks
- Expert users still need deep hardware knowledge to get the best manual schedules.
- Compiler search spaces can become expensive without careful pruning.

## [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness]

- **Authors:** Tri Dao et al.
- **Venue:** NeurIPS 2022
- **Year:** 2022
- **Tags:** CUDA Kernels, GPU Optimization, LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2205.14135
- **Code Link:** https://github.com/Dao-AILab/flash-attention

### Short Summary
FlashAttention reframes exact attention as an IO problem instead of only a FLOP problem. The paper shows that standard attention implementations waste substantial time and memory traffic by materializing large intermediate matrices. Its tiled algorithm keeps data in on-chip memory longer and fuses the softmax computation into an exact attention pipeline. This makes the method valuable both as a kernel contribution and as a conceptual lesson in hardware-aware algorithm design. The work quickly became a default reference for efficient transformer training and inference.

### Core Innovation
- Exact attention algorithm designed around memory traffic minimization.
- Tiled kernel structure that avoids materializing the full attention matrix.
- Hardware-aware reformulation that preserves numerical correctness.

### Technical Approach
- Query, key, and value blocks are streamed through SRAM-friendly tiles.
- Softmax statistics are accumulated online so exact normalization is preserved.
- Kernel fusion reduces round trips to high-bandwidth memory.

### Results
- Benchmarks include BERT- and GPT-style transformer workloads.
- The paper reports significant speed and memory improvements over standard exact attention implementations.
- Results helped establish IO-aware kernel design as central to transformer systems work.

### Potential Drawbacks
- Benefits depend on GPU architecture, sequence length, and implementation maturity.
- Integrating the kernel into every framework and attention variant requires ongoing engineering.
