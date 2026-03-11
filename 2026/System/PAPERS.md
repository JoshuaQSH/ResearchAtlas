# 2026 System Papers

## [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling]

- **Authors:** Ted Zadouri, Markus Hoehnerbach, Jay Shah, Timmy Liu, Vijay Thakkar, Tri Dao
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** CUDA Kernels, GPU Optimization, LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2603.05451
- **Code Link:** https://github.com/Dao-AILab/flash-attention

### Short Summary
FlashAttention-4 targets the new bottlenecks that appear on Blackwell GPUs, where tensor-core throughput scales faster than other units. The paper argues that optimizations tuned for Hopper are no longer sufficient for the B200 and GB200 generation. It co-designs algorithmic updates and kernel pipelines to keep attention throughput high under this asymmetric scaling profile. The implementation emphasizes asynchronous matrix operations, larger tiling strategies, and reduction of non-matmul overheads in softmax-related work. The authors also implement the stack in CuTe-DSL embedded in Python to improve iteration speed for kernel development. For ResearchAtlas, this is a high-signal 2026 kernel-systems paper because it links hardware shifts directly to attention-runtime redesign.

### Core Innovation
- Co-design of attention algorithm and kernel pipeline for Blackwell-era asymmetric hardware scaling.
- Reduction of non-matmul bottlenecks through software-emulated exponential and conditional softmax rescaling.
- CuTe-DSL implementation that substantially reduces compile-time overhead while preserving kernel expressivity.

### Technical Approach
- The method redesigns the forward/backward pipelines around fully asynchronous MMA operations and larger tiles.
- It uses software-level reformulation for expensive softmax-path operations so tensor cores stay better utilized.
- It leverages tensor memory plus 2-CTA MMA mode to reduce shared-memory traffic and backward-pass atomic pressure.
- The implementation is built in Python-hosted CuTe-DSL rather than traditional template-heavy C++ kernels.

### Results
- The paper reports up to 1.3x speedup versus cuDNN 9.13 and up to 2.7x versus Triton on B200 with BF16.
- Peak reported performance reaches 1613 TFLOPs/s (71% utilization).
- The DSL-based implementation reports approximately 20-30x faster compile times than comparable C++ template workflows.

### Potential Drawbacks
- Gains are tied to Blackwell-specific hardware characteristics and may not transfer uniformly to older GPUs.
- Kernel complexity and specialized pipelining increase maintenance cost.
- Production integration still depends on ecosystem alignment around CuTe-DSL deployment practices.

## [PackInfer: Compute- and I/O-Efficient Attention for Batched LLM Inference]

- **Authors:** Rui Ning, Wei Zhang, Fan Lai
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** AI Infrastructure, GPU Optimization, LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2602.06072
- **Code Link:** N/A

### Short Summary
PackInfer addresses a practical serving gap: most attention optimizations focus on single-request kernels, while production inference batches heterogeneous request lengths. The paper shows this mismatch causes compute and I/O imbalance, request stragglers, and low GPU utilization in real serving pipelines. It introduces a kernel-level framework that explicitly packs and groups requests for load-balanced batched execution. The system also reorganizes KV-cache layouts to improve locality and reduce redundant movement as generation progresses. This makes the contribution relevant to deployment settings where throughput and tail latency both matter. In the 2026 atlas, PackInfer is a representative systems paper on batched attention efficiency rather than isolated kernel microbenchmarks.

### Core Innovation
- Compute- and I/O-aware batched attention execution for heterogeneous request sets.
- Request packing strategy that improves kernel occupancy under mixed sequence lengths.
- KV-cache grouping and layout reorganization for lower memory overhead during generation.

### Technical Approach
- Requests are grouped into load-balanced execution packs to reduce straggler effects.
- Attention kernels are built over packed query-key regions to eliminate redundant computation.
- I/O-aware grouping colocates shared-prefix requests and reorganizes KV-cache storage into group-contiguous layouts.
- The runtime adapts grouping as sequence lengths evolve during autoregressive decoding.

### Results
- On real-world workloads, the paper reports 13.0-20.1% lower inference latency.
- It reports around 20% throughput improvement over a FlashAttention-based state-of-the-art baseline.
- Reported gains come from combined compute balancing and cache-I/O optimization.

### Potential Drawbacks
- Real gains depend on workload heterogeneity and batching policy quality.
- Additional packing logic adds scheduler complexity in serving stacks.
- Integration may require invasive KV-cache layout changes in existing runtimes.
