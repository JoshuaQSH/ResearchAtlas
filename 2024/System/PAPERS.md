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

## [SuperBench: Improving Cloud AI Infrastructure Reliability with Proactive Validation]

- **Authors:** Yifan Xiong et al.
- **Venue:** USENIX ATC 2024
- **Year:** 2024
- **Tags:** AI Infrastructure, GPU Optimization, HPC
- **Paper Link:** https://www.usenix.org/conference/atc24/presentation/xiong
- **Code Link:** N/A

### Short Summary
SuperBench studies gray failures in cloud AI infrastructure, where redundant systems continue to function but silently degrade ML performance. The paper argues that standard reliability mechanisms are not enough because performance regressions can remain hidden for long periods. It presents a proactive validation framework with a broad benchmark suite tailored to AI hardware and workloads. This is directly relevant to the atlas because cloud ML performance now depends as much on infrastructure validation as on model kernels. The work provides a concrete reliability perspective that complements pure throughput optimization papers.

### Core Innovation
- Proactive validation system for cloud AI infrastructure.
- Focus on hidden degradation instead of only outright failures.
- Broad benchmark suite tied to real AI workload behavior.

### Technical Approach
- The system runs targeted validation jobs across hardware components and configurations.
- It compares signals across devices to detect silent performance degradation.
- Benchmarks are chosen to approximate important AI training and inference behaviors.

### Results
- Evaluated in Microsoft cloud infrastructure settings.
- The paper reports improved detection of hidden degradation and better root-cause localization.
- Results show validation can prevent costly AI-performance regressions from lingering.

### Potential Drawbacks
- Coverage depends on the representativeness of the validation suite.
- Operational deployment requires continuous maintenance as hardware fleets evolve.

## [ServiceLab: Preventing Tiny Performance Regressions at Hyperscale through Pre-Production Testing]

- **Authors:** Mike Chow et al.
- **Venue:** OSDI 2024
- **Year:** 2024
- **Tags:** AI Infrastructure, HPC, Hodgepodge
- **Paper Link:** https://www.usenix.org/conference/osdi24/presentation/chow
- **Code Link:** N/A

### Short Summary
ServiceLab is a large-scale performance testing platform built to detect very small regressions before production rollout. The paper is not exclusively about AI, but it explicitly includes ML models among the workloads it validates at fleet scale. Its main contribution is operational: tiny regressions matter when they affect enormous deployments, so pre-production testing must be both statistically disciplined and operationally scalable. This perspective is increasingly relevant for AI services that consume massive infrastructure budgets. The paper is tagged `Hodgepodge` because it is more broadly systems-operational than AI-specific.

### Core Innovation
- Hyperscale pre-production platform for detecting extremely small regressions.
- Statistical treatment of noisy infrastructure effects at fleet scale.
- Operational systems contribution with direct ML-service relevance.

### Technical Approach
- The platform runs controlled performance experiments before broad deployment.
- It models variance from machine, kernel, and datacenter factors to improve sensitivity.
- The design emphasizes repeated large-scale measurement rather than isolated benchmarking.

### Results
- Evaluated on Meta services and ML workloads at very large scale.
- The paper reports detection of tiny regressions that would otherwise waste significant fleet capacity.
- Results show production-scale testing can materially reduce performance drift.

### Potential Drawbacks
- The platform relies on large internal infrastructure and may be hard to replicate externally.
- Its relevance to core AI algorithms is indirect.

## [VeriSMo: A Verified Security Module for Confidential VMs]

- **Authors:** Ziqiao Zhou et al.
- **Venue:** OSDI 2024
- **Year:** 2024
- **Tags:** AI Infrastructure, Hodgepodge
- **Paper Link:** https://www.usenix.org/conference/osdi24/presentation/zhou
- **Code Link:** N/A

### Short Summary
VeriSMo is a verified security module for confidential virtual machines running on AMD SEV-SNP. It is included because confidential-computing support is increasingly relevant to secure AI infrastructure, even though the paper is fundamentally a systems-security contribution. The work goes beyond memory-safe implementation claims by verifying critical properties of the module. That is valuable for infrastructure that may host sensitive training or inference workloads. The paper broadens the atlas toward infrastructure trust and isolation, with an explicit `Hodgepodge` tag because the AI link is indirect.

### Core Innovation
- Verified security module for confidential VMs.
- Stronger assurance than implementation in Rust alone.
- Relevant infrastructure primitive for sensitive compute workloads.

### Technical Approach
- The module is specified and verified against key security properties.
- It targets AMD SEV-SNP and supports integrity and secret-management features.
- Unsafe implementation details are controlled through a verified design pipeline.

### Results
- Evaluated as a functional confidential-VM security module.
- The paper reports that strong assurance is achievable without abandoning practical deployment goals.
- Results strengthen the case for formally justified infrastructure components.

### Potential Drawbacks
- Verification cost and engineering complexity are substantial.
- The paper is less central to the atlas than model-serving or compiler work.

## [Rethinking Machine Learning Inference Serving from User Perspectives]

- **Authors:** Daniel Mendoza, Francisco Romero, Caroline Trippel
- **Venue:** EuroSys 2024
- **Year:** 2024
- **Tags:** AI Infrastructure, GPU Optimization
- **Paper Link:** https://dblp.org/rec/conf/eurosys/MendozaRT24
- **Code Link:** N/A

### Short Summary
This EuroSys paper argues that machine-learning inference serving should be evaluated and optimized from user-facing objectives rather than only provider-centric throughput metrics. That framing matters because latency-critical workloads often care about tail behavior, quality of service, and model selection tradeoffs more than raw utilization. The paper therefore expands the design space for inference systems beyond conventional throughput-maximization. It is directly relevant to the atlas as a serving-systems contribution with operational focus. It also fills EuroSys coverage with a strong ML-serving paper.

### Core Innovation
- User-centric reframing of inference serving objectives.
- Focus on latency-critical and service-level outcomes.
- Practical systems perspective on ML inference beyond pure throughput.

### Technical Approach
- The work studies model selection and serving behavior under user-facing constraints.
- It evaluates tradeoffs between latency, service quality, and infrastructure efficiency.
- The system perspective emphasizes what users experience rather than only provider utilization.

### Results
- Evaluated on latency-critical ML inference serving scenarios.
- The paper reports that user-centric choices can alter which serving strategies are preferred.
- Results show that throughput-only evaluation can miss important operational tradeoffs.

### Potential Drawbacks
- User-centric optimization may complicate capacity planning and scheduling.
- Findings depend on the exact workload and service-level objectives considered.
