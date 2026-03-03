# 2023 AI Papers

## [Llama 2: Open Foundation and Fine-Tuned Chat Models]

- **Authors:** Hugo Touvron et al.
- **Venue:** arXiv / Meta AI
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2307.09288
- **Code Link:** https://github.com/meta-llama/llama

### Short Summary
Llama 2 is one of the most consequential open-weight model releases because it provided a strong common baseline for research and deployment. The paper details model sizes, training choices, and a safety-tuned chat variant that rapidly became standard in downstream experiments. Its importance to this atlas is partly indirect: open models dramatically accelerated work on serving, quantization, and compilation because researchers could benchmark realistic systems without closed APIs. The report also made instruction-tuned open models more credible for production-like evaluation. In practice, much of the 2023 and 2024 systems literature is easier to interpret because Llama 2 existed.

### Core Innovation
- High-quality open-weight foundation model family with aligned chat variants.
- Standardized open benchmark target for systems and compression research.
- Strong evidence that open models can be competitive enough to drive tooling ecosystems.

### Technical Approach
- Decoder-only transformers are pretrained on large corpora and then instruction tuned for chat use.
- Model families are released at multiple scales to support both research and deployment.
- Safety-tuning and evaluation are integrated into the release process.

### Results
- Benchmarks span language understanding, reasoning, and dialogue-oriented evaluations.
- The paper reports strong open-model performance for its generation.
- Results made Llama 2 a default target for low-bit inference and serving papers.

### Potential Drawbacks
- The report is less detailed than a full systems paper on some training pipeline choices.
- Open weights accelerate research, but they also require careful downstream safety handling.

## [Mistral 7B]

- **Authors:** Albert Q. Jiang et al.
- **Venue:** arXiv / Mistral AI
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2310.06825
- **Code Link:** https://github.com/mistralai/mistral-inference

### Short Summary
Mistral 7B demonstrated that model quality and serving efficiency can improve together when architecture choices are tuned carefully. The paper combines grouped-query attention and sliding-window attention to improve practical inference behavior for a compact model. That made it especially relevant for real deployments where memory and latency matter more than leaderboard scale alone. The model became a popular target for quantization and edge-serving experiments because it was both strong and relatively accessible. It is a useful example of algorithmic choices being made with systems consequences in mind.

### Core Innovation
- Compact but strong open-weight LLM with architecture choices favorable to inference.
- Use of grouped-query attention and sliding-window attention in a practical release.
- Strong quality-per-parameter profile that influenced later small-model design.

### Technical Approach
- A decoder-only transformer is trained with architecture modifications that reduce inference cost.
- Sliding-window attention limits effective context operations while preserving long-range behavior through recurrence across layers.
- Grouped-query attention reduces KV-cache footprint compared with full multi-head attention.

### Results
- Benchmarked on common language understanding and reasoning tasks.
- The paper reports strong performance relative to larger open models at the time.
- Results made Mistral 7B a common baseline for fast serving and low-bit deployment work.

### Potential Drawbacks
- Context handling is still constrained compared with later dedicated long-context methods.
- Smaller open models remain sensitive to data quality and evaluation protocol choices.

## [QLoRA: Efficient Finetuning of Quantized LLMs]

- **Authors:** Tim Dettmers et al.
- **Venue:** NeurIPS 2023
- **Year:** 2023
- **Tags:** Model Compression, Model Quantization, LLM Systems & Algorithms
- **Paper Link:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html
- **Code Link:** https://github.com/artidoro/qlora

### Short Summary
QLoRA made low-cost adaptation of large language models broadly accessible by combining 4-bit quantization with LoRA fine-tuning. The method matters because it turned compression into an enabler for training workflows, not just inference. By keeping the base model quantized and training only low-rank adapters, the paper dramatically reduced the hardware barrier for instruction tuning. The work was quickly adopted in both research and production experimentation. It also reinforced the idea that quantization-aware system design should span the full model lifecycle.

### Core Innovation
- Finetuning pipeline that keeps the frozen backbone in 4-bit form.
- Combination of quantization and low-rank adaptation for practical resource reduction.
- Strong enabling effect for wider participation in LLM adaptation work.

### Technical Approach
- The base model is quantized with a 4-bit representation while LoRA adapters remain trainable.
- Optimizer state and gradient flow are designed to keep memory use manageable.
- The method is evaluated on instruction-following fine-tuning tasks.

### Results
- Benchmarks include chat-style and instruction-tuning evaluations across several model families.
- The paper reports strong quality retention despite the compressed training setup.
- Results turned QLoRA into a default baseline for parameter-efficient tuning.

### Potential Drawbacks
- Performance depends on careful hyperparameter choices and quantization implementation details.
- The method targets adaptation efficiency rather than maximal training throughput.

## [Towards Fine-Grained Explainability for Heterogeneous Graph Neural Network]

- **Authors:** Tong Li, Jiale Deng, Yanyan Shen, Luyu Qiu, Yongxiang Huang, Caleb Chen Cao
- **Venue:** AAAI 2023
- **Year:** 2023
- **Tags:** Explainable AI, Graph Neural Networks
- **Paper Link:** https://dblp.org/rec/conf/aaai/LiDSQHC23
- **Code Link:** N/A

### Short Summary
This paper targets explainability for heterogeneous graph neural networks, where node and edge types make attribution harder than in homogeneous graphs. The core idea is to explain predictions at a finer granularity than earlier graph-explanation methods. That matters because many practical graph tasks depend on typed relations and diverse neighborhoods that collapse poorly into coarse explanations. The paper contributes a more structure-aware explanation formulation for heterogeneous settings. It is useful in this atlas because it closes the explainability gap with a graph-oriented method from a top AI venue.

### Core Innovation
- Fine-grained explanation method specialized for heterogeneous GNNs.
- Better alignment between explanation outputs and typed graph structure.
- Clear extension of graph explainability beyond homogeneous assumptions.

### Technical Approach
- The method scores relation- and structure-level components that influence a prediction.
- It uses the heterogeneous graph schema to constrain what an explanation can highlight.
- Explanations are optimized to remain faithful while preserving interpretability.

### Results
- Evaluated on heterogeneous graph benchmarks with node-classification style tasks.
- The paper reports more faithful and informative explanations than generic baselines.
- Results show explanation quality improves when graph heterogeneity is modeled explicitly.

### Potential Drawbacks
- Explanation metrics remain imperfect proxies for human usefulness.
- Computational overhead can rise when many relation types are present.

## [Scaling Up Dynamic Graph Representation Learning via Spiking Neural Networks]

- **Authors:** Jintang Li et al.
- **Venue:** AAAI 2023
- **Year:** 2023
- **Tags:** Graph Neural Networks, AI Infrastructure
- **Paper Link:** https://dblp.org/rec/conf/aaai/LiYZC0ZTWM23
- **Code Link:** N/A

### Short Summary
This paper explores dynamic graph representation learning through a spiking-neural-network formulation. The work is interesting because temporal graph updates and event-driven computation have a natural conceptual match. By using spiking dynamics, the model aims to scale dynamic-graph learning while preserving temporal sensitivity. The paper is also relevant to the atlas because it broadens graph-system design beyond standard transformer or message-passing recipes. It gives the graph-neural-network bucket more coverage from a mainstream AI venue.

### Core Innovation
- Event-driven dynamic graph learning with spiking neural networks.
- Alternative scalability path for temporal graph representation learning.
- Stronger fit between event streams and computational model.

### Technical Approach
- Dynamic graph interactions are encoded as temporally evolving signals.
- A spiking architecture aggregates and propagates information over these graph events.
- The design targets efficient updates rather than repeated full-graph recomputation.

### Results
- Evaluated on dynamic-graph representation benchmarks.
- The paper reports competitive or improved predictive performance with scalable temporal handling.
- Results suggest event-driven architectures can be practical for dynamic graph workloads.

### Potential Drawbacks
- Spiking architectures are less standardized than mainstream GNN baselines.
- Adoption may be limited by framework maturity and implementation complexity.
