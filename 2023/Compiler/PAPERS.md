# 2023 Compiler Papers

## [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning]

- **Authors:** Tri Dao
- **Venue:** arXiv 2023 / ICLR 2024
- **Year:** 2023
- **Tags:** CUDA Kernels, GPU Optimization, Compiler Optimization
- **Paper Link:** https://arxiv.org/abs/2307.08691
- **Code Link:** https://github.com/Dao-AILab/flash-attention

### Short Summary
FlashAttention-2 extends the original IO-aware attention idea with improved work partitioning and better GPU utilization. The paper focuses on how to map attention computation more effectively across thread blocks and warps, which is where much of the remaining performance headroom lived. It is an important follow-on because it turns a strong algorithmic idea into a more mature production kernel family. The work also demonstrates that efficient attention remains a moving target as model shapes and GPU generations evolve. It became the default attention baseline for many later inference and training systems papers.

### Core Innovation
- Better parallel decomposition of attention work on modern GPUs.
- Kernel redesign that improves occupancy and reduces serial bottlenecks.
- A second-generation attention implementation that preserves exactness while raising throughput.

### Technical Approach
- The algorithm rebalances work across query blocks and GPU thread groups.
- Kernel structure is tuned to improve tensor-core use and memory behavior.
- Implementation details are adapted to common head dimensions and transformer layouts.

### Results
- Benchmarks cover training and inference settings for transformer models.
- The paper reports faster execution than the first FlashAttention implementation in many workloads.
- Results show that kernel-level parallelism choices still matter after major algorithmic optimization.

### Potential Drawbacks
- Gains depend on GPU generation and attention shape.
- Real integration still requires framework support and careful kernel dispatch choices.
