# 2025 AI Papers

## [DeepSeek-R1]

- **Authors:** DeepSeek-AI et al.
- **Venue:** arXiv / DeepSeek
- **Year:** 2025
- **Tags:** LLM Systems & Algorithms, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2501.12948
- **Code Link:** https://github.com/deepseek-ai/DeepSeek-R1

### Short Summary
DeepSeek-R1 is one of the most visible reasoning-model releases of 2025 and rapidly became a reference point for open reasoning systems. The paper emphasizes training and post-training techniques that improve deliberate reasoning behavior while keeping the model deployable. Its importance extends beyond raw benchmark performance because it changed what open-weight reasoning models were expected to do. The release also stimulated new systems work on long reasoning traces, sampling strategies, and serving cost. It is a core 2025 reference for the reasoning-model wave.

### Core Innovation
- Open reasoning-focused model release with strong practical impact.
- A concrete demonstration that open models can compete in reasoning-heavy evaluations.
- Strong influence on downstream inference and evaluation practice.

### Technical Approach
- The model combines large-scale pretraining with additional reasoning-oriented training or post-training stages.
- Evaluation focuses on difficult reasoning tasks and open benchmarks.
- The release is structured to support broad downstream experimentation.

### Results
- Benchmarks include math, code, and reasoning-oriented tasks.
- The paper reports strong reasoning performance for an open model in its generation.
- Results triggered follow-on work on efficient reasoning-time inference.

### Potential Drawbacks
- Reasoning-focused models can be expensive to serve because they generate long traces.
- Training details are less open than a fully reproducible academic system paper.

## [Qwen3 Technical Report]

- **Authors:** Qwen Team
- **Venue:** arXiv / Alibaba
- **Year:** 2025
- **Tags:** LLM Systems & Algorithms, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2505.09388
- **Code Link:** https://github.com/QwenLM/Qwen3

### Short Summary
Qwen3 extends the strong-open-model trend with a broad model family aimed at practical deployment and downstream customization. The report is valuable because it couples model quality with an ecosystem-friendly release strategy. That makes it relevant to systems and compression research, which rely on stable open baselines. The model family quickly entered serving, quantization, and tool-use evaluations across the community. It is a useful 2025 reference for open LLM infrastructure rather than only model capability.

### Core Innovation
- Broad open model family designed for immediate downstream use.
- Practical release pattern that supports serving and compression ecosystems.
- Strong continuation of the high-quality open-weight model trend.

### Technical Approach
- Multiple decoder-only models are trained and released with deployment-oriented variants.
- The report covers general capability and usability rather than only a single flagship size.
- Open release supports rapid adoption in external systems experiments.

### Results
- Benchmarks span general language, instruction following, and reasoning tasks.
- The paper reports strong open-model performance for the 2025 generation.
- Results helped make Qwen3 a common baseline in later efficiency papers.

### Potential Drawbacks
- Technical reporting is less focused than a narrow systems paper on runtime details.
- Real deployment quality still depends on surrounding alignment and serving choices.

## [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition]

- **Authors:** DeepSeek-AI et al.
- **Venue:** arXiv / DeepSeek
- **Year:** 2025
- **Tags:** LLM Systems & Algorithms
- **Paper Link:** https://arxiv.org/abs/2508.03680
- **Code Link:** N/A

### Short Summary
DeepSeek-Prover-V2 is more specialized than the general-purpose reasoning models, but it is relevant to this atlas because it pushes test-time reasoning and decomposition methods in a concrete domain. The paper studies how reinforcement learning and subgoal decomposition can improve formal mathematical reasoning. That makes it a useful example of 2025's broader move from generic next-token capability toward structured reasoning procedures. While the domain is narrow, the methodological ideas are widely relevant to LLM algorithms. It also highlights the serving implications of deeper search-like inference loops.

### Core Innovation
- Reinforcement-learning-based improvement of structured formal reasoning.
- Explicit subgoal decomposition in theorem-proving style tasks.
- A domain-specific but methodologically relevant reasoning-system paper.

### Technical Approach
- The model is trained or refined to propose and solve intermediate subgoals.
- Reinforcement learning shapes the search process toward successful proofs.
- The system is evaluated in formal mathematics settings where correctness is explicit.

### Results
- Benchmarks focus on formal mathematical reasoning and theorem-proving tasks.
- The paper reports stronger proof construction behavior than simpler baseline strategies.
- Results illustrate the growing importance of structured reasoning procedures in LLM work.

### Potential Drawbacks
- Domain specialization limits direct transfer to general text-generation workloads.
- Structured reasoning methods can be expensive at inference time.
