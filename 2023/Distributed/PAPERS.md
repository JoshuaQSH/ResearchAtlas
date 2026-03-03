# 2023 Distributed Papers

## [MegaBlocks: Efficient Sparse Training with Mixture-of-Experts]

- **Authors:** Samyam Rajbhandari et al.
- **Venue:** MLSys 2023 Workshop / arXiv 2023
- **Year:** 2023
- **Tags:** Distributed Deep Learning, Sparse Matrix & Kernels, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2211.15841
- **Code Link:** https://github.com/databricks/megablocks

### Short Summary
MegaBlocks revisits sparse MoE training from the kernel and systems side rather than only the routing side. The key idea is to avoid wasting computation on padded expert batches by using block-sparse structure that fits GPU execution well. This matters because expert imbalance is one of the major reasons sparse models can underdeliver on hardware. The paper shows that block-sparse kernels can preserve sparsity gains while avoiding the worst utilization collapse. It is representative of the broader shift toward system-aware sparse modeling.

### Core Innovation
- Block-sparse reformulation of MoE execution to reduce padding waste.
- GPU-efficient sparse kernels tailored to expert workloads.
- A bridge between routing sparsity and practical accelerator utilization.

### Technical Approach
- Tokens are bucketed for experts and mapped into block-sparse compute structures.
- Kernels operate on regularized sparse blocks instead of heavily padded dense tensors.
- The runtime is designed to keep expert execution more balanced on GPU hardware.

### Results
- Evaluated on large-scale mixture-of-experts training settings.
- The paper reports better hardware efficiency and training throughput than dense-padding approaches.
- Results support sparse training as a practical route to larger effective model capacity.

### Potential Drawbacks
- Benefits depend on expert routing statistics and chosen block granularity.
- Sparse-kernel engineering is more specialized than dense-kernel deployment.

## [Ring Attention with Blockwise Transformers for Near-Infinite Context]

- **Authors:** Hao Liu et al.
- **Venue:** arXiv 2023
- **Year:** 2023
- **Tags:** Distributed Deep Learning, LLM Systems & Algorithms, HPC
- **Paper Link:** https://arxiv.org/abs/2310.01889
- **Code Link:** https://github.com/Selimonder/ring-attention

### Short Summary
Ring Attention studies how to scale context length by combining blockwise attention with distributed communication across devices. The paper is interesting because it treats long context as both an algorithmic and a communication problem. Instead of assuming a single device can store all sequence state, it organizes computation around a ring-style exchange pattern. This lets attention span much longer effective contexts while controlling device memory pressure. The work is part of the long-context systems wave that followed the first generation of efficient attention kernels.

### Core Innovation
- Distributed long-context attention built around ring communication.
- Blockwise transformer execution that keeps memory growth manageable.
- Joint treatment of context extension and inter-device communication.

### Technical Approach
- Sequence blocks are distributed across devices and processed incrementally.
- Devices exchange the information needed for attention using ring-style communication.
- The method composes blockwise execution with exact or near-exact attention calculations.

### Results
- Evaluated on long-context transformer tasks and synthetic scaling studies.
- The paper reports the ability to handle sequence lengths that exceed standard single-device memory limits.
- Results highlight communication-aware design as essential for long-context inference and training.

### Potential Drawbacks
- Communication overhead can dominate when interconnect performance is weak.
- Integrating the method into full serving stacks requires careful scheduler support.
