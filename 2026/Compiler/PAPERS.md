# 2026 Compiler Papers

## [PolyBlocks: A Compiler Infrastructure for AI Chips and Programming Frameworks]

- **Authors:** Uday Bondhugula, Akshay Baviskar, Navdeep Katel, Vimal Patel, Anoop JS, Arnab Dutta
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** Compiler Optimization, MLIR, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2603.06731
- **Code Link:** N/A

### Short Summary
PolyBlocks presents a modular MLIR-based compiler infrastructure intended to be reusable across multiple AI frameworks and target chips. The work centers on pass pipelines that compose loop/SSA transformations with lightweight affine analysis and analytical cost models. It includes multi-level tiling, fusion, scratchpad usage, matrix-unit mapping, and attention-layer fusion among its key optimizations. The design goal is to minimize per-chip compiler reimplementation by reusing common infrastructure and specializing pipelines where needed. The paper evaluates PyTorch and JAX JIT scenarios on NVIDIA GPUs to compare with mainstream compiler stacks. For this atlas, PolyBlocks is a 2026 compiler contribution with direct relevance to MLIR-centered AI code generation.

### Core Innovation
- Reusable MLIR pass-pipeline architecture for both AI frameworks and heterogeneous AI chips.
- Analytical-model-guided transformation selection over loop-nest and SSA representations.
- Emphasis on reusable infrastructure rather than one-off backend-specific optimization logic.

### Technical Approach
- High-level framework graphs are lowered into MLIR IR where transformation pipelines are applied.
- Pipelines combine tiling, fusion, locality optimization, and hardware mapping passes.
- Cost models and heuristics coordinate pass ordering and parameterization for target hardware.
- The stack supports generation down to low-level target-specific intrinsics.

### Results
- The paper reports matching or outperforming Torch Inductor and XLA in several evaluated cases.
- For operators such as matmul and convolution, generated kernels are reported as competitive with vendor-tuned libraries or hand-written kernels.
- Results indicate the architecture can retain performance while improving portability and reuse.

### Potential Drawbacks
- Tuning and heuristic robustness can vary across unseen hardware targets.
- Competitive results in selected cases do not guarantee uniform wins across all workloads.
- The operational complexity of maintaining broad pass pipelines remains non-trivial.

## [Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)]

- **Authors:** Mohammed Javed Absar, Muthu Baskaran, Abhikrant Sharma, Abhilash Bhandari, Ankit Aggarwal, Arun Rangasamy, Dibyendu Das, Fateme Hosseini, Franck Slama, Iulian Brumar, Jyotsna Verma, Krishnaprasad Bindumadhavan, et al.
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** Compiler Optimization, MLIR, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2602.19762
- **Code Link:** https://github.com/qualcomm/hexagon-mlir

### Short Summary
Hexagon-MLIR introduces an open-source MLIR-based stack targeting Qualcomm Hexagon NPUs with support for lowering both Triton kernels and PyTorch model subgraphs. The paper emphasizes a structured pass sequence that exploits NPU architectural features for AI acceleration. A notable design point is generation of mega-kernels that improve data locality in tightly coupled memory and reduce bandwidth bottlenecks. The work is positioned as complementary to commercial toolchains, giving developers a flexible open path for compiler innovation. It is explicitly presented as an ongoing effort, with additional optimization work planned. Within ResearchAtlas, Hexagon-MLIR is a practical 2026 compiler-systems entry bridging MLIR, Triton, and NPU deployment.

### Core Innovation
- Unified MLIR-based lowering path for Triton kernels and PyTorch workloads onto Hexagon NPUs.
- Mega-kernel generation strategy to increase locality in NPU tightly coupled memory.
- Open-source compiler path that complements proprietary deployment stacks.

### Technical Approach
- The compiler applies a sequence of MLIR passes tuned to Hexagon NPU capabilities.
- Triton kernels and selected framework subgraphs are lowered into target binaries through automated pipelines.
- Locality-oriented transformations attempt to reduce bandwidth pressure by maximizing on-chip reuse.
- The system emphasizes kernel-to-binary automation for faster deployment iteration.

### Results
- The paper reports functional end-to-end compilation and deployment support for targeted workloads.
- It reports improved locality and reduced bandwidth bottlenecks through mega-kernel generation relative to library-style approaches.
- As a work in progress, results are presented as early but promising for open NPU compilation.

### Potential Drawbacks
- The stack is explicitly work-in-progress, so feature completeness is evolving.
- NPU-specific optimizations may limit portability across other accelerator families.
- Performance characterization remains less exhaustive than long-mature GPU compiler stacks.
