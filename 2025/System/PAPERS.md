# 2025 System Papers

## [FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving]

- **Authors:** FlashInfer Team et al.
- **Venue:** arXiv 2025
- **Year:** 2025
- **Tags:** LLM Systems & Algorithms, CUDA Kernels, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2501.01005
- **Code Link:** https://github.com/flashinfer-ai/flashinfer

### Short Summary
FlashInfer is a serving-oriented attention engine that focuses on the practical diversity of inference workloads rather than a single idealized kernel shape. The paper is significant because modern serving stacks need to support multiple attention variants, cache layouts, and batching regimes without constant rewrites. It presents an engine-style approach with customizable operators and efficient implementations tuned for LLM inference. This is important in 2025 because inference stacks were becoming modular platforms rather than monolithic runtimes. The work reflects the maturation of low-level LLM serving infrastructure.

### Core Innovation
- Engine-style attention runtime for inference-serving use cases.
- Customizable support for multiple attention and cache-management patterns.
- Practical emphasis on integration into full serving systems.

### Technical Approach
- The system provides optimized attention primitives that can be composed by serving runtimes.
- Kernel implementations are tuned for decoding-oriented access patterns and heterogeneous workloads.
- The design emphasizes flexibility without giving up low-level efficiency.

### Results
- Benchmarks target real LLM serving scenarios with varying attention and batching configurations.
- The paper reports strong performance while preserving flexibility across runtime designs.
- Results suggest inference infrastructure is shifting toward reusable kernel engines.

### Potential Drawbacks
- Generality can make tuning and API design more complex than single-purpose kernels.
- Real benefits depend on integration quality inside the surrounding serving stack.

## [vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention]

- **Authors:** Yao Fu et al.
- **Venue:** ASPLOS 2025
- **Year:** 2025
- **Tags:** AI Infrastructure, GPU Optimization, LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2405.04437
- **Code Link:** https://github.com/microsoft/vattention

### Short Summary
vAttention revisits the memory-management problem in LLM serving and argues that PagedAttention is not the only workable design point. The paper designs a different dynamic allocation strategy that aims to preserve throughput without the same style of paging abstraction. This is valuable because vLLM had become the de facto baseline, and the field needed principled alternatives. The work shows that memory-manager design choices materially shape end-to-end inference performance. It represents a healthy second wave in LLM serving systems research where the baseline itself is being challenged.

### Core Innovation
- Alternative dynamic memory manager for LLM serving without relying on PagedAttention.
- A direct systems comparison against the dominant cache-virtualization approach.
- Strong focus on serving-runtime memory behavior as a core research problem.

### Technical Approach
- KV-cache allocation and reclamation are managed using a different runtime abstraction from paging.
- Scheduler and memory manager are co-designed to reduce fragmentation and overhead.
- The implementation targets continuous-batching style serving workloads.

### Results
- Evaluated on realistic multi-request LLM serving workloads.
- The paper reports competitive or improved performance relative to strong PagedAttention baselines in selected settings.
- Results show the serving-memory design space remains open rather than settled.

### Potential Drawbacks
- Comparisons depend heavily on workload mix and implementation maturity.
- Alternative memory managers can be harder to reason about operationally than widely adopted baselines.
