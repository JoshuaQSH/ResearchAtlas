# 2022 AI Papers

## [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]

- **Authors:** Jason Wei et al.
- **Venue:** NeurIPS 2022
- **Year:** 2022
- **Tags:** LLM Systems & Algorithms, AI Infrastructure
- **Paper Link:** https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html
- **Code Link:** N/A

### Short Summary
Chain-of-thought prompting showed that large language models can solve many reasoning tasks more effectively when they are prompted to expose intermediate steps. The paper is conceptually simple, but its impact was large because it changed the default way the community evaluated reasoning in LLMs. It also highlighted that model capability can depend strongly on inference-time prompting format, not just pretraining. The work became a foundation for later reasoning, tool-use, and test-time scaling papers. In practice, it shifted attention from pure next-token modeling toward controllable inference procedures.

### Core Innovation
- Demonstration that intermediate reasoning traces can unlock latent model capability.
- A simple prompting intervention with wide transfer across task families.
- A strong empirical case for separating training-time capacity from inference-time elicitation.

### Technical Approach
- Few-shot prompts include worked reasoning examples before the answer.
- The model is then evaluated on multi-step arithmetic, commonsense, and symbolic reasoning tasks.
- Performance is compared against standard answer-only prompting.

### Results
- Benchmarks include GSM8K, arithmetic reasoning, symbolic reasoning, and commonsense tasks.
- The paper reports clear gains over direct prompting on sufficiently large models.
- Results helped establish reasoning prompting as a standard evaluation axis for LLMs.

### Potential Drawbacks
- Gains are size-dependent and are much weaker for smaller models.
- Generated reasoning traces are not guaranteed to be faithful explanations of internal computation.

## [Recipe for a General, Powerful, Scalable Graph Transformer]

- **Authors:** Ladislav Rampasek et al.
- **Venue:** NeurIPS 2022
- **Year:** 2022
- **Tags:** Graph Neural Networks, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2205.12454
- **Code Link:** https://github.com/rampasek/GraphGPS

### Short Summary
GraphGPS proposes a practical recipe for graph transformers that mixes message passing with global attention and positional encodings. The paper is important because it avoids treating graph transformers as a one-size-fits-all replacement for GNNs. Instead, it shows how local structure bias and global receptive field can be combined in a scalable architecture. The work became a useful reference for later graph foundation-model discussions because it is modular and implementation-oriented. It also helped stabilize empirical practice on long-range graph benchmarks.

### Core Innovation
- Hybrid architecture combining local message passing with global transformer blocks.
- Practical integration of positional and structural encodings for graph data.
- A scalable recipe rather than a narrowly specialized graph transformer.

### Technical Approach
- Local MPNN layers capture neighborhood structure, while attention layers supply global communication.
- Structural encodings are injected to preserve graph identity and relative position information.
- The architecture is evaluated as a configurable recipe across multiple graph benchmarks.

### Results
- Benchmarks include ZINC, PCQM4Mv2, and long-range graph tasks.
- The paper reports strong accuracy and good scalability relative to prior graph transformer baselines.
- Results support the claim that hybridization is more robust than pure global attention on graphs.

### Potential Drawbacks
- Performance depends on careful choice of structural encodings and local backbone.
- Scaling to very large graphs can still be memory-intensive because of attention layers.
