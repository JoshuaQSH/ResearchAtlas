# 2024 System Papers

## [SGLang: Efficient Execution of Structured Language Model Programs]

- **Authors:** Lianmin Zheng et al.
- **Venue:** NeurIPS 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, AI Infrastructure, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2312.07104
- **Code Link:** https://github.com/sgl-project/sglang

### Short Summary
SGLang treats LLM applications as structured programs instead of opaque prompt strings and designs a runtime around that assumption. The paper is significant because structured decoding, tool use, and control flow are hard to serve efficiently with standard text-only runtimes. It combines a programming abstraction with runtime techniques such as prefix reuse and efficient scheduling. That makes it relevant both to application builders and to systems researchers thinking about execution models for agentic workloads. The work helped broaden the scope of LLM systems research beyond plain next-token serving.

### Core Innovation
- Programming abstraction for structured LLM execution rather than raw prompt concatenation.
- Runtime optimizations that exploit shared prefixes and control-flow structure.
- Joint language-and-systems view of LLM application execution.

### Technical Approach
- Developers write structured programs that interleave prompts, generation, and program logic.
- The runtime compiles or interprets these programs into optimized execution schedules.
- Cache reuse and scheduling policies exploit common substructures across requests.

### Results
- Evaluated on realistic structured-generation workloads and serving benchmarks.
- The paper reports higher throughput and lower overhead than unstructured baseline execution paths.
- Results suggest structured execution is a worthwhile systems abstraction for LLM applications.

### Potential Drawbacks
- Benefits depend on application structure and the amount of reusable prompt prefix.
- Runtime complexity is higher than a minimal text-generation server.

## [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention]

- **Authors:** Zirui Liu et al.
- **Venue:** NeurIPS 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, Sparse Matrix & Kernels, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2407.02490
- **Code Link:** https://github.com/microsoft/MInference

### Short Summary
MInference targets the prefill phase, which became a major bottleneck as long-context models grew in popularity. The paper argues that many long-context workloads do not need uniformly dense attention during prefill and can exploit dynamic sparsity instead. It designs a sparse attention pattern and runtime to accelerate this stage without requiring a completely new model family. This is important because prefill cost often dominates real prompt-heavy applications. The work represents the 2024 push toward long-context optimization as a systems problem rather than only a modeling problem.

### Core Innovation
- Dynamic sparse attention specialized for prefill acceleration.
- Focus on the prompt-processing phase rather than only autoregressive decoding.
- Practical long-context speedups without retraining a brand-new architecture.

### Technical Approach
- The method predicts or selects sparse attention structure during prompt ingestion.
- Kernels exploit this structure to reduce memory traffic and compute cost.
- The runtime integrates sparse prefill with standard dense decoding paths.

### Results
- Benchmarks target long-context prompt processing for large language models.
- The paper reports faster prefill and lower memory pressure than dense baselines on long inputs.
- Results make prefill optimization a primary topic in inference stack design.

### Potential Drawbacks
- Sparse patterns may not generalize equally well across all prompts or model families.
- Dynamic sparsity introduces additional scheduling and kernel-selection complexity.

## [QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving]

- **Authors:** Qinghao Hu et al.
- **Venue:** arXiv 2024
- **Year:** 2024
- **Tags:** Model Quantization, AI Infrastructure, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2405.04532
- **Code Link:** https://github.com/mit-han-lab/qserve

### Short Summary
QServe is a representative paper from the wave of work that stopped treating quantization and runtime engineering as separate concerns. The paper co-designs low-bit model formats with the scheduler, kernels, and memory system used during serving. That is important because low-bit models often fail to deliver their theoretical gains when the rest of the stack stays optimized for high precision. QServe demonstrates that carefully chosen W4A8KV4 formats can be made practical in real LLM serving stacks. The paper is useful as a reference for system-level quantized inference design.

### Core Innovation
- Joint design of low-bit formats and serving runtime behavior.
- Focus on weight, activation, and KV-cache precision together.
- Practical system path from compression method to deployable inference engine.

### Technical Approach
- Model state is quantized into asymmetric low-bit formats suited to GPU execution.
- The serving stack uses custom kernels and memory layouts tuned for the chosen representation.
- Scheduler behavior is adjusted to preserve throughput under low-bit execution.

### Results
- Benchmarks target real LLM serving throughput and latency under low-bit settings.
- The paper reports strong efficiency gains versus higher-precision baselines.
- Results show co-design is necessary to realize the promise of extreme low-bit inference.

### Potential Drawbacks
- The design is hardware-aware and may require retuning on new accelerators.
- Aggressive low-bit settings still involve quality-risk tradeoffs on some tasks.
