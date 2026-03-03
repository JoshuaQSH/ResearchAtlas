# 2023 System Papers

## [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention]

- **Authors:** Woosuk Kwon et al.
- **Venue:** SOSP 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, AI Infrastructure, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2309.06180
- **Code Link:** https://github.com/vllm-project/vllm

### Short Summary
vLLM addresses a central serving bottleneck for large language models: the KV cache wastes memory when requests have different lengths and decoding states. The paper introduces PagedAttention, which virtualizes KV-cache allocation using a paged memory abstraction. That choice lets the serving runtime pack many more active requests onto the same GPU memory budget. The system is influential because it changed the baseline assumptions for modern LLM serving engines. Many later runtimes either adopt its ideas directly or define themselves against the PagedAttention design point.

### Core Innovation
- KV-cache virtualization via a paged memory abstraction.
- Decoupling logical sequence state from physically contiguous memory allocation.
- A serving runtime designed around high-throughput continuous batching.

### Technical Approach
- Sequence KV state is stored in fixed-size blocks rather than monolithic contiguous tensors.
- The runtime schedules decoding requests continuously as blocks are allocated and reclaimed.
- Attention kernels are adapted to gather logical sequence state efficiently from paged storage.

### Results
- Evaluated on LLM serving workloads with realistic request-length variability.
- The paper reports higher throughput and better memory utilization than prior serving baselines.
- Results show that cache management is a first-order systems problem for LLM inference.

### Potential Drawbacks
- Non-contiguous cache access complicates kernel design and can create gather overheads.
- The memory manager adds runtime complexity that must be carefully maintained under new model architectures.

## [Punica: Multi-Tenant LoRA Serving]

- **Authors:** Yuhui Zhou et al.
- **Venue:** arXiv 2023
- **Year:** 2023
- **Tags:** AI Infrastructure, LLM Systems & Algorithms, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2310.18547
- **Code Link:** https://github.com/punica-ai/punica

### Short Summary
Punica focuses on a problem that became urgent with the spread of LoRA adapters: how to serve many customized models without duplicating the full base model in memory. The paper treats adapters as first-class runtime objects and designs batching and kernel strategies around that assumption. This is important because multi-tenant LLM serving is a systems problem, not just a storage problem. The runtime shows that many user-specific adapters can share a backbone model while preserving throughput. It helped turn LoRA-based personalization into a practical serving pattern.

### Core Innovation
- Multi-tenant serving architecture specialized for LoRA adapters.
- Batching and kernel strategies that keep shared-base execution efficient.
- Systems framing for adapter-based customization at scale.

### Technical Approach
- A single base model is shared while lightweight LoRA deltas are applied per request.
- The runtime groups requests to maximize backbone reuse and minimize adapter overhead.
- Kernel support is tailored to mixed batches with distinct low-rank updates.

### Results
- Benchmarks target concurrent serving of many adapter-specialized tasks.
- The paper reports strong throughput relative to naive per-adapter model replication.
- Results show that adapter personalization can scale without linearly scaling memory cost.

### Potential Drawbacks
- Benefits shrink when request mixes are highly fragmented or adapters differ significantly in shape.
- The design is specialized for LoRA-style updates rather than arbitrary fine-tuning methods.

## [zpoline: A System Call Hook Mechanism Based on Binary Rewriting]

- **Authors:** Kenichi Yasukata, Hajime Tazaki, Pierre-Louis Aublin, Kenta Ishiguro
- **Venue:** USENIX ATC 2023
- **Year:** 2023
- **Tags:** AI Infrastructure, Hodgepodge
- **Paper Link:** https://www.usenix.org/conference/atc23/presentation/yasukata
- **Code Link:** N/A

### Short Summary
zpoline is not an AI paper, but it is a high-impact systems paper that fits the venue-coverage requirement and remains relevant to instrumentation-heavy ML infrastructure. The paper presents a user-space system-call hook mechanism that relies on binary rewriting rather than kernel changes. That lets the mechanism intercept calls broadly while preserving portability and low overhead. In practice, this kind of capability is useful for sandboxing, observability, and compatibility layers that can show up in large infrastructure stacks. It is included here as an explicit `Hodgepodge` entry because the fit to the atlas core is indirect.

### Core Innovation
- Binary-rewriting-based system-call hooking without kernel modification.
- Broad coverage of system calls with low runtime overhead.
- Practical design for instrumentation and compatibility tooling.

### Technical Approach
- Short system-call instructions are rewritten into jumps toward hook logic.
- The mechanism avoids source-code requirements and specialized libc modifications.
- The runtime preserves execution correctness while redirecting control to user-level hooks.

### Results
- Evaluated on x86-64 workloads involving interception and emulation tasks.
- The paper reports low overhead while preserving exhaustive coverage.
- Results demonstrate a clean systems design point compared with heavier kernel-level approaches.

### Potential Drawbacks
- The method is architecture-specific in its low-level implementation details.
- It is only loosely related to AI systems compared with the atlas core material.
