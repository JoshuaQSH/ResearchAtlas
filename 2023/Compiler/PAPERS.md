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

## [Mosaic: An Interoperable Compiler for Tensor Algebra]

- **Authors:** Manya Bansal, Olivia Hsu, Kunle Olukotun, Fredrik Kjolstad
- **Venue:** OOPSLA 2023
- **Year:** 2023
- **Tags:** Compiler Optimization, Sparse Matrix & Kernels
- **Paper Link:** https://dblp.org/rec/journals/pacmpl/BansalHOK23
- **Code Link:** N/A

### Short Summary
Mosaic addresses a common compiler fragmentation problem in tensor algebra systems: different IRs and execution backends are difficult to compose cleanly. The paper presents an interoperable compiler design aimed at making tensor algebra compilation more modular. That matters because AI and scientific-computing workloads increasingly rely on specialized sparse and dense tensor operations that span multiple compiler ecosystems. The work is relevant to the atlas as a language-and-compiler contribution sitting close to ML operator generation. It also broadens conference coverage into OOPSLA without abandoning the tensor-program focus.

### Core Innovation
- Interoperable compiler design for tensor algebra workloads.
- Better composition across tensor abstractions and backends.
- Language-and-systems approach to compiler modularity for numeric programs.

### Technical Approach
- Tensor algebra programs are lowered through a compiler interface designed for interoperability.
- The system focuses on preserving algebraic structure while enabling backend-specific optimization.
- Compilation stages are organized so different tools can share tensor representations more effectively.

### Results
- Evaluated on tensor-algebra and sparse/dense numeric kernels.
- The paper reports improved interoperability with competitive performance.
- Results suggest compiler modularity does not have to come at the expense of optimization quality.

### Potential Drawbacks
- Interoperability layers can still introduce engineering complexity.
- The work is more compiler-architecture-oriented than end-to-end ML system benchmarking.
