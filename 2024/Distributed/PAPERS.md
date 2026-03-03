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

## [QUART: Throughput Optimization for Parallel Graph Neural Network Training]

- **Authors:** Yanying Lin, Yanbo Li, Shijie Peng, Yingfei Tang, Shutian Luo, Haiying Shen, Cheng-Zhong Xu, Kejiang Ye
- **Venue:** ICDCS 2024
- **Year:** 2024
- **Tags:** Distributed Deep Learning, Graph Neural Networks, AI Infrastructure
- **Paper Link:** https://dblp.org/rec/conf/icdcs/LinLPTLSXY24
- **Code Link:** N/A

### Short Summary
QUART addresses throughput bottlenecks in parallel GNN training, where neighborhood sampling and irregular communication make distributed execution difficult. The paper is useful because GNN systems often fall between the assumptions of dense tensor training and graph-processing frameworks. It focuses on throughput as the primary optimization target rather than only single-iteration speed. The work provides a concrete distributed-systems treatment of GNN training. It is a strong ICDCS entry with direct overlap with atlas topics.

### Core Innovation
- Throughput-oriented system design for distributed GNN training.
- Explicit treatment of irregular graph-training bottlenecks.
- Clear optimization target around end-to-end training efficiency.

### Technical Approach
- The system reorganizes sampling, communication, and execution to improve parallel efficiency.
- It targets the imbalance and overheads created by irregular graph neighborhoods.
- Optimization decisions are made around sustained throughput instead of isolated kernel behavior.

### Results
- Evaluated on distributed graph neural network training workloads.
- The paper reports higher throughput than strong distributed GNN baselines.
- Results show GNN training needs specialized distributed execution strategies.

### Potential Drawbacks
- Gains depend on graph structure and partition quality.
- Distributed GNN systems remain sensitive to sampling and communication overhead.

## [PckGNN: Optimizing Aggregation Operators with Packing Strategies in Graph Neural Networks]

- **Authors:** Zhengding Hu, Jingwei Sun, Zhongyang Li, Guangzhong Sun
- **Venue:** IPDPS 2024
- **Year:** 2024
- **Tags:** Graph Neural Networks, Sparse Matrix & Kernels, GPU Optimization
- **Paper Link:** https://dblp.org/rec/conf/ipps/Hu0LS24
- **Code Link:** N/A

### Short Summary
PckGNN studies one of the core performance bottlenecks in graph neural networks: aggregation operators on irregular sparse structures. The paper proposes packing strategies that improve how these operators map onto parallel hardware. That matters because GNN performance is often decided by aggregation efficiency rather than only by dense linear algebra. The work makes the graph-systems angle more concrete by focusing on a critical kernel family. It serves as a good IPDPS representative for graph and parallel optimization.

### Core Innovation
- Packing strategies tailored to GNN aggregation operators.
- Focus on sparse, irregular graph kernels rather than dense tensor cores alone.
- Practical optimization of a major GNN systems bottleneck.

### Technical Approach
- The method reorganizes aggregation work into more hardware-friendly packed layouts.
- Execution is tuned to reduce irregular access overheads and improve parallel efficiency.
- The design targets the sparse operator structure common in GNN workloads.

### Results
- Evaluated on graph neural network aggregation workloads.
- The paper reports better operator efficiency than less specialized baselines.
- Results show data layout and packing decisions matter heavily for practical GNN acceleration.

### Potential Drawbacks
- Benefits may vary with graph sparsity pattern and model architecture.
- Integration into full training stacks requires compatibility with broader GNN frameworks.

## [GraNNDis: Decoupling Graph Neural Network Training via Placing Computation Near the Data in Distributed Environments]

- **Authors:** Jaeyong Song, Hongsun Jang, Hunseong Lim, Jaewon Jung, Youngsok Kim, Jinho Lee
- **Venue:** PACT 2024
- **Year:** 2024
- **Tags:** Distributed Deep Learning, Graph Neural Networks, AI Infrastructure
- **Paper Link:** https://dblp.org/rec/conf/IEEEpact/SongJL0KL24
- **Code Link:** N/A

### Short Summary
GraNNDis rethinks distributed GNN training by moving more computation toward the data rather than assuming a conventional centralized training pipeline. This matters because graph workloads can be communication-dominated when features and structure are partitioned poorly. The paper decouples parts of training to reduce data movement and improve scalability. It is directly relevant to the atlas because it combines graph learning with distributed systems design. The work also provides a clear PACT coverage paper with ML-systems relevance.

### Core Innovation
- Data-near-computation design for distributed GNN training.
- Decoupling strategy that reduces communication overhead.
- Strong systems framing of graph-training scalability.

### Technical Approach
- Training computation is reorganized so more work can happen close to the graph partitions that own the data.
- The system reduces repeated remote access patterns that dominate distributed GNN workloads.
- The design targets scalability under distributed environments with partitioned graph structure.

### Results
- Evaluated on distributed graph neural network training tasks.
- The paper reports improved scalability and reduced communication overhead over baseline designs.
- Results support moving graph computation closer to partitioned data.

### Potential Drawbacks
- Benefits depend on partition quality and workload structure.
- The design may be harder to integrate with standard dense-model training infrastructure.
