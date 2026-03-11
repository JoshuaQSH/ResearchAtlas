# 2026 Distributed Papers

## [Scalable Training of Mixture-of-Experts Models with Megatron Core]

- **Authors:** Zijie Yan, Hongxiao Bai, Xin Yao, Dennis Liu, Tong Liu, Hongbin Liu, Pingtian Li, Evan Wu, Shiqing Fan, Li Tao, Robin Zhang, Yuzhong Wang, et al.
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** Distributed Deep Learning, AI Infrastructure, HPC
- **Paper Link:** https://arxiv.org/abs/2603.07685
- **Code Link:** https://github.com/NVIDIA/Megatron-LM

### Short Summary
This report studies system-level scaling of Mixture-of-Experts training, where sparse activation shifts bottlenecks across memory, communication, and compute. The core argument is that isolated optimization of one dimension often creates pressure in another, so end-to-end co-design is required. Megatron Core integrates optimizations spanning fine-grained recomputation/offloading, optimized dispatch/overlap, and compute-kernel improvements such as grouped GEMM and fusions. The paper also covers parallel-folding strategies and low-precision modes such as FP8 and NVFP4 for large-scale MoE workloads. It targets production-scale training, including long-context configurations and large GPU clusters. For atlas coverage, this is a strong 2026 distributed systems reference for MoE training infrastructure.

### Core Innovation
- End-to-end co-design of memory, communication, and compute optimizations for MoE training.
- Parallel Folding framework for flexible multi-dimensional parallel strategy composition.
- Production-focused support for low-precision and long-context MoE scaling.

### Technical Approach
- Memory pressure is reduced through mechanisms such as fine-grained recomputation and offloading.
- Communication paths use optimized expert dispatch and overlap to reduce distributed synchronization cost.
- Compute throughput is improved using grouped GEMM, fused kernels, and CUDA Graph execution.
- The framework composes these components for large-cluster MoE runs with multiple parallel dimensions.

### Results
- On NVIDIA GB300/GB200, reported performance includes 1,233/1,048 TFLOPS per GPU for DeepSeek-V3-685B.
- For Qwen3-235B, the paper reports 974/919 TFLOPS per GPU on GB300/GB200.
- The report states successful use from billion- to trillion-parameter MoE training across up to thousands of GPUs.

### Potential Drawbacks
- Reported performance depends on highly optimized NVIDIA hardware/software environments.
- Engineering complexity is substantial when composing multiple parallel and precision modes.
- Portability to non-NVIDIA stacks is not established in this report.
