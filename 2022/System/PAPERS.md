# 2022 System Papers

## [Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning]

- **Authors:** Zheng Jia et al.
- **Venue:** OSDI 2022
- **Year:** 2022
- **Tags:** Distributed Deep Learning, AI Infrastructure, HPC
- **Paper Link:** https://arxiv.org/abs/2201.12023
- **Code Link:** https://github.com/alpa-projects/alpa

### Short Summary
Alpa targets one of the hardest engineering problems in large-scale training: choosing how to combine data, tensor, and pipeline parallelism for a concrete model and cluster. The paper frames this as a search problem over intra-operator and inter-operator parallel execution plans. It uses a hierarchical planner so the search stays tractable instead of exploding with model size. The system is built on top of JAX/XLA, which makes the generated execution plans practical rather than purely theoretical. Across transformer-style models, the paper shows that automated plan search can outperform manually selected strategies while reducing operator placement effort.

### Core Innovation
- Joint optimization of inter-operator and intra-operator parallelism instead of treating them separately.
- A hierarchical planner that composes dynamic programming with cost modeling.
- Automatic generation of distributed execution plans on top of a production compiler stack.

### Technical Approach
- The model graph is partitioned into stages, and each stage is assigned a parallelization strategy chosen by a cost model.
- Intra-operator plans handle sharding of tensors and compute, while inter-operator plans handle stage boundaries and pipeline scheduling.
- The search objective minimizes end-to-end runtime under cluster resource constraints.

### Results
- Benchmarks include transformer-family workloads such as BERT, GPT, and T5-style models.
- The paper reports faster end-to-end training than strong hand-tuned baselines in several cluster settings.
- Results emphasize reduced manual engineering cost alongside runtime gains.

### Potential Drawbacks
- Planner quality depends on the fidelity of the cost model and profiling assumptions.
- The stack is most natural for JAX/XLA users and is less turnkey for other training ecosystems.

## [GSPMD: General and Scalable Parallelization for ML Computation Graphs]

- **Authors:** Yuanzhong Xu et al.
- **Venue:** OSDI 2022
- **Year:** 2022
- **Tags:** Distributed Deep Learning, AI Infrastructure, HPC
- **Paper Link:** https://arxiv.org/abs/2105.04663
- **Code Link:** N/A

### Short Summary
GSPMD presents a general SPMD partitioning approach for large computation graphs and shows how it can be integrated directly into XLA. The main contribution is a compact sharding annotation model that can express a wide range of tensor layouts and communication patterns. Instead of requiring users to hand-write many parallel kernels, the compiler propagates partitioning information through the graph and inserts collective communication when needed. The paper argues that this approach scales to very large transformer and MoE models while keeping the programming interface manageable. Its impact is visible in later large-model training systems that rely on similar compiler-mediated sharding.

### Core Innovation
- A general sharding propagation framework inside the compiler.
- Automatic communication insertion based on partitioned tensor semantics.
- A programming model that keeps user annotations small relative to the full distributed graph.

### Technical Approach
- Users provide partitioning hints, and the compiler infers compatible sharding across the graph.
- The system lowers the annotated graph to SPMD code plus collectives such as all-reduce and all-gather.
- Correctness is maintained by tracking layout transformations explicitly during propagation.

### Results
- Evaluated on large transformer and mixture-of-experts style workloads on TPU clusters.
- The paper demonstrates scalability to very large model sizes with a small amount of manual partitioning input.
- Results focus on showing compiler-driven partitioning can match practical production needs.

### Potential Drawbacks
- The paper is tightly coupled to the XLA ecosystem.
- Debugging partitioning behavior can still be difficult when inferred communication becomes complex.
