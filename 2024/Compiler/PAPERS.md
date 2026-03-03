# 2024 Compiler Papers

## [Marlin: Mixed-Auto-Regressive Linear Kernels for Efficient LLM Inference]

- **Authors:** Elias Frantar et al.
- **Venue:** arXiv 2024
- **Year:** 2024
- **Tags:** CUDA Kernels, GPU Optimization, Compiler Optimization
- **Paper Link:** https://arxiv.org/abs/2408.11743
- **Code Link:** https://github.com/IST-DASLab/marlin

### Short Summary
Marlin focuses on the kernel layer of quantized inference, where theoretical compression gains often disappear if kernels are not tuned carefully. The paper designs mixed low-bit matrix multiplication kernels specialized for autoregressive decoding workloads. That is an important niche because decoding stresses memory movement and small-batch efficiency differently from large training batches. Marlin became notable in practice because it delivered strong real-world speed on common open-weight LLM deployments. It is a representative example of kernel work becoming inseparable from quantization research.

### Core Innovation
- Low-bit kernels specialized for autoregressive inference rather than generic GEMM alone.
- Practical focus on real serving shapes where batch sizes and cache behavior matter.
- Tight integration of quantization format and kernel mapping.

### Technical Approach
- Matrix multiplication kernels are tuned for low-bit weights and decoding-oriented access patterns.
- Work partitioning is chosen to balance tensor-core use, memory movement, and small-batch latency.
- Implementation targets common LLM layer shapes seen in open serving stacks.

### Results
- Evaluated on quantized LLM decoding workloads on modern GPUs.
- The paper reports strong throughput relative to less specialized low-bit kernels.
- Results show that kernel design remains a major determinant of realized quantization gains.

### Potential Drawbacks
- Specialized kernels can be brittle across model shapes and hardware generations.
- Integration into broader serving frameworks requires ongoing maintenance.

## [A Tensor Compiler with Automatic Data Packing for Simple and Efficient Fully Homomorphic Encryption]

- **Authors:** Aleksandar Krastev, Nikola Samardzic, Simon Langowski, Srinivas Devadas, Daniel Sánchez
- **Venue:** PLDI 2024
- **Year:** 2024
- **Tags:** Compiler Optimization, Sparse Matrix & Kernels, Hodgepodge
- **Paper Link:** https://dblp.org/rec/journals/pacmpl/KrastevSLDS24
- **Code Link:** N/A

### Short Summary
This PLDI paper presents a tensor compiler that automates data packing for fully homomorphic encryption workloads. It is not a mainstream ML-systems paper, but the compiler techniques are still relevant to tensor-program optimization and numeric kernel generation. The work shows how compiler abstractions can simplify an otherwise complex performance problem. That makes it a reasonable atlas entry under `Hodgepodge` while still strengthening compiler coverage. It also provides PLDI representation with a tensor-centric compiler paper.

### Core Innovation
- Automatic data-packing compiler for tensor-style encrypted computation.
- Abstraction of a difficult low-level optimization problem into compiler machinery.
- Useful overlap between tensor compilation and specialized numeric execution.

### Technical Approach
- The compiler analyzes tensor computations and inserts efficient data-packing transformations.
- It aims to reduce manual optimization effort while preserving performance.
- The design targets the constraints imposed by fully homomorphic encryption kernels.

### Results
- Evaluated on encrypted tensor workloads.
- The paper reports simpler programming and competitive efficiency compared with manual approaches.
- Results show compiler automation can make specialized numeric domains more tractable.

### Potential Drawbacks
- The direct connection to mainstream AI systems is limited.
- Performance gains depend on the target encrypted workload and backend characteristics.

## [FastFold: Optimizing AlphaFold Training and Inference on GPU Clusters]

- **Authors:** Seongyeon Park, Junguk Hong, Jaeyong Song, Hajin Kim, Youngsok Kim, Jinho Lee
- **Venue:** PPoPP 2024
- **Year:** 2024
- **Tags:** AI Infrastructure, GPU Optimization, HPC
- **Paper Link:** https://dblp.org/rec/conf/ppopp/ParkHSKKL24
- **Code Link:** N/A

### Short Summary
FastFold targets one of the most expensive scientific AI workloads in practice: AlphaFold training and inference on GPU clusters. The paper is relevant because protein-structure modeling combines large model execution with demanding systems constraints. It optimizes the workload across GPU kernels, communication, and cluster-level execution. That makes it an especially good fit for the atlas’s AI infrastructure and HPC themes. It also gives PPoPP direct coverage with a high-value systems paper.

### Core Innovation
- Cluster-scale optimization of AlphaFold training and inference.
- Joint treatment of kernels, communication, and system execution.
- Practical systems work for scientific AI workloads rather than generic NLP alone.

### Technical Approach
- The system identifies AlphaFold bottlenecks across GPU computation and distributed execution.
- It introduces optimizations that improve efficiency on GPU clusters.
- The design aims to preserve model fidelity while reducing overall runtime.

### Results
- Evaluated on AlphaFold training and inference workloads.
- The paper reports substantial efficiency improvements on GPU clusters.
- Results show scientific AI workloads benefit from dedicated systems optimization rather than generic frameworks alone.

### Potential Drawbacks
- The optimizations are tied closely to AlphaFold-like workloads.
- Maintaining performance across rapidly changing model implementations can be difficult.
