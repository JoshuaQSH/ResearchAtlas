# 2024 Distributed Papers

## [HeteGen: Heterogeneous Distributed Transformer Serving and Generation]

- **Authors:** Hailong Yang et al.
- **Venue:** arXiv 2024
- **Year:** 2024
- **Tags:** Distributed Deep Learning, AI Infrastructure, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2405.21064
- **Code Link:** N/A

### Short Summary
HeteGen studies an increasingly practical serving scenario: the available accelerator pool is heterogeneous, but the model still needs to deliver predictable generation performance. The paper argues that uniform placement assumptions are too limiting for real clusters. It develops scheduling and partitioning ideas that account for device heterogeneity during distributed inference. This is relevant because production inference fleets often mix generations of GPUs or vary in memory size. The work broadens distributed LLM serving beyond homogeneous-cluster assumptions.

### Core Innovation
- Distributed generation design that explicitly models heterogeneous devices.
- Scheduling and partitioning choices adapted to unequal memory and compute budgets.
- Practical framing of inference on mixed accelerator fleets.

### Technical Approach
- Model shards and request workloads are assigned based on device capabilities.
- The runtime coordinates execution so slower devices do not dominate end-to-end latency unnecessarily.
- Placement and batching strategies trade off throughput against imbalance.

### Results
- Evaluated on heterogeneous-cluster serving scenarios.
- The paper reports better performance than naive uniform placement strategies.
- Results emphasize heterogeneity as a first-class design constraint for real inference infrastructure.

### Potential Drawbacks
- Accurate device characterization is required for robust scheduling decisions.
- Mixed-fleet optimization increases operational complexity and testing burden.
