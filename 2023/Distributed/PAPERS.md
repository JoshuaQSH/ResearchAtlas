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

## [CausalSim: A Causal Framework for Unbiased Trace-Driven Simulation]

- **Authors:** Abdullah Alomar, Pouya Hamadanian, Arash Nasr-Esfahany, Anish Agarwal, Mohammad Alizadeh, Devavrat Shah
- **Venue:** NSDI 2023
- **Year:** 2023
- **Tags:** AI Infrastructure, Distributed Deep Learning, HPC
- **Paper Link:** https://www.usenix.org/conference/nsdi23/presentation/alomar
- **Code Link:** N/A

### Short Summary
CausalSim studies a practical weakness in trace-driven systems evaluation: the collected traces are often biased by the policy that produced them. The paper reframes unbiased simulator construction as a causal inference problem instead of a pure replay problem. This matters for adaptive video, networking, and learned systems where naive replay can rank algorithms incorrectly. The system learns latent factors and uses randomized-control data to adjust the simulation so counterfactual interventions are more credible. It is a strong NSDI paper because it turns a methodological problem into a deployable evaluation framework.

### Core Innovation
- Causal reformulation of trace-driven simulation.
- Use of randomized data and invariance structure to remove policy bias.
- A practical framework for more reliable counterfactual systems evaluation.

### Technical Approach
- The method models observed traces together with latent variables that capture environment state.
- It uses randomized control trial data to estimate a causal structure that supports unbiased simulation under new policies.
- The core computation is cast as a tensor-completion style problem with strong structural assumptions.

### Results
- Evaluated on real and synthetic adaptive bitrate streaming data.
- The paper reports lower simulation error than expert-designed and supervised baselines.
- Results show that unbiased simulation can materially change the conclusions about competing algorithms.

### Potential Drawbacks
- The method depends on access to suitable randomized data.
- Causal assumptions can still break under heavy distribution shift.

## [High Throughput Training of Deep Surrogates from Large Ensemble Runs]

- **Authors:** Lucas Thibaut Meyer, Marc Schouler, Robert Alexander Caulk, Alejandro Ribés, Bruno Raffin
- **Venue:** SC 2023
- **Year:** 2023
- **Tags:** Distributed Deep Learning, HPC, AI Infrastructure
- **Paper Link:** https://dblp.org/rec/conf/sc/MeyerSCRR23
- **Code Link:** N/A

### Short Summary
This SC paper studies how to train deep surrogate models efficiently from very large scientific ensembles. The work is relevant because surrogate modeling has become a key AI workload in scientific computing, but its data movement and throughput demands differ from mainstream web-scale training. The paper focuses on end-to-end throughput rather than only model quality. It shows how HPC-aware pipeline design can make surrogate training practical at scale. That makes it a good bridge between HPC and modern AI infrastructure.

### Core Innovation
- Throughput-oriented training design for surrogate models on large ensembles.
- Clear integration of scientific-computing requirements with AI training workflows.
- Practical demonstration that HPC pipelines can accelerate AI surrogate construction.

### Technical Approach
- The system organizes large simulation ensembles into efficient training streams.
- Data loading, preprocessing, and distributed training are tuned for HPC environments.
- The study focuses on pipeline bottlenecks that dominate end-to-end wall-clock time.

### Results
- Evaluated on large ensemble scientific workloads.
- The paper reports higher training throughput and better system utilization than simpler baselines.
- Results show surrogate-model training can be made operationally viable at HPC scale.

### Potential Drawbacks
- Benefits depend on access to large HPC infrastructure and ensemble-style datasets.
- The paper is narrower than general-purpose deep learning systems work.

## [DIPPM: Data Intensive Parallelism Performance Model]

- **Authors:** Karthick Panner Selvam, Mats Brorsson
- **Venue:** Euro-Par 2023
- **Year:** 2023
- **Tags:** HPC, Hodgepodge
- **Paper Link:** https://dblp.org/rec/conf/europar/SelvamB23
- **Code Link:** N/A

### Short Summary
DIPPM is a performance-modeling paper for data-intensive parallel workloads. It is not centered on AI models directly, but it is relevant to the atlas because AI pipelines increasingly depend on predictable parallel data processing behavior. The paper contributes a modeling view of how compute, memory, and communication interact in data-intensive execution. That is useful for reasoning about ML data pipelines and distributed preprocessing systems. It is tagged `Hodgepodge` because the AI connection is indirect.

### Core Innovation
- Performance model for data-intensive parallel execution.
- Explicit treatment of interactions between compute and data movement.
- Useful abstraction for reasoning about distributed pipeline efficiency.

### Technical Approach
- The paper builds an analytical or semi-empirical model for parallel execution behavior.
- It captures bottlenecks from data access, communication, and resource contention.
- The model is used to explain or predict throughput across parallel configurations.

### Results
- Evaluated on parallel data-intensive workloads.
- The paper reports that the model tracks important performance trends across configurations.
- Results support more principled reasoning about parallel workload tuning.

### Potential Drawbacks
- The link to core AI algorithms is weak.
- Predictive models can break when workloads or hardware depart from the fitted regime.
