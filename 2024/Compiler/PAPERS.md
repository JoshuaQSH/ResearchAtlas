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
