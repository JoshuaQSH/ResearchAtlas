# 2026 AI Papers

## [MoEless: Efficient MoE LLM Serving via Serverless Computing]

- **Authors:** Hanfei Yu, Bei Ouyang, Shwai He, Ang Li, Hao Wang
- **Venue:** arXiv 2026
- **Year:** 2026
- **Tags:** AI Infrastructure, Distributed Deep Learning, LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2603.06350
- **Code Link:** N/A

### Short Summary
MoEless focuses on inference-time load imbalance in expert-parallel MoE serving, where a small subset of experts can become persistent stragglers. The paper argues static serverful deployments are a poor fit because expert demand changes quickly and unevenly over time. It introduces a serverless MoE serving framework that scales experts elastically and places them to improve locality. The system uses lightweight predictors to estimate incoming expert load and proactively detect bottleneck experts. This combines systems scheduling and serving elasticity to reduce latency and cost in practical MoE inference. In the 2026 update, MoEless is a relevant AI-infrastructure paper connecting MoE algorithms to production serving behavior.

### Core Innovation
- First serverless-oriented framework targeting MoE expert-load imbalance during LLM serving.
- Layer-aware expert-load prediction used to preemptively identify and mitigate stragglers.
- Placement and scaling policies designed to balance expert demand while preserving locality.

### Technical Approach
- The runtime predicts per-expert request pressure before bottlenecks fully materialize.
- It scales and places serverless experts using policies that trade off locality, utilization, and load balance.
- The framework is implemented on top of Megatron-LM and evaluated under realistic open-source MoE workloads.
- Serving control is coordinated across experts and GPUs to limit queueing collapse around hot experts.

### Results
- On the reported testbed and workloads, MoEless reports 43% lower inference latency.
- The paper reports 84% lower inference cost compared with its chosen state-of-the-art baselines.
- Results indicate that elasticity-aware expert placement can materially improve MoE serving efficiency.

### Potential Drawbacks
- Serverless cold-start and orchestration overhead can offset gains in some deployment environments.
- Predictor error may reduce effectiveness under rapidly shifting traffic patterns.
- Operational complexity may increase relative to stable, serverful deployments.
