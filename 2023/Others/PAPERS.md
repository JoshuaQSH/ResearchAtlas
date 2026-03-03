# 2023 Other Papers

## [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models]

- **Authors:** Guangxuan Xiao et al.
- **Venue:** ICML 2023
- **Year:** 2023
- **Tags:** Model Quantization, Model Compression, GPU Optimization
- **Paper Link:** https://proceedings.mlr.press/v202/xiao23c.html
- **Code Link:** https://github.com/mit-han-lab/smoothquant

### Short Summary
SmoothQuant tackles the practical problem that activation quantization is often the blocker for very low-cost LLM inference. The paper introduces a simple weight-activation rescaling trick that shifts quantization difficulty from activations into weights, where it is easier to manage. This makes post-training W8A8 deployment substantially more realistic for large models. The paper was quickly adopted because the method is easy to implement and composes well with existing inference kernels. It became one of the anchor references for modern LLM PTQ.

### Core Innovation
- Activation smoothing that redistributes quantization difficulty into weights.
- Simple post-training method with strong practical deployment value.
- A calibration-friendly design that fits production inference workflows.

### Technical Approach
- Per-channel scaling factors are chosen to rebalance activation and weight ranges.
- The transformed model is then quantized into a lower-precision inference format.
- The method is designed to preserve model function while improving low-bit robustness.

### Results
- Evaluated on OPT, BLOOM, and other large language model families.
- The paper reports strong accuracy retention with efficient low-bit inference settings.
- Results helped make W8A8 a practical default in LLM serving stacks.

### Potential Drawbacks
- Calibration quality still matters, especially on harder downstream tasks.
- The method does not by itself solve extreme low-bit settings such as aggressive 4-bit activation quantization.

## [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration]

- **Authors:** Ji Lin et al.
- **Venue:** MLSys 2024 / arXiv 2023
- **Year:** 2023
- **Tags:** Model Quantization, Model Compression, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2306.00978
- **Code Link:** https://github.com/mit-han-lab/llm-awq

### Short Summary
AWQ is a highly practical low-bit quantization method that focuses on preserving the most important weights using activation information. The paper is influential because it combines simple selection logic with deployment-friendly low-bit inference targets. In the LLM serving ecosystem, AWQ became one of the default 4-bit baselines used in open-source toolchains and vendor stacks. Its appeal comes from strong quality retention without requiring heavy retraining. The work helped make 4-bit LLM inference feel routine instead of experimental.

### Core Innovation
- Activation-aware criterion for protecting important weights during quantization.
- Strong 4-bit deployment performance without full retraining.
- Direct fit with real serving systems and open-source inference stacks.

### Technical Approach
- Calibration activations identify weight groups that are more sensitive to quantization error.
- The quantizer preserves those weights more carefully while compressing the rest aggressively.
- Runtime support targets efficient low-bit matrix multiplication.

### Results
- Evaluated on common open LLM families and downstream language benchmarks.
- The paper reports strong quality retention in 4-bit settings with practical inference speedups.
- Results drove broad adoption across open-source serving frameworks.

### Potential Drawbacks
- Sensitivity can depend on the calibration set and chosen grouping strategy.
- Hardware support for optimal 4-bit execution still varies across GPU generations.

## [SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot]

- **Authors:** Elias Frantar and Dan Alistarh
- **Venue:** ICML 2023
- **Year:** 2023
- **Tags:** Model Compression, Sparse Matrix & Kernels, Model Quantization
- **Paper Link:** https://proceedings.mlr.press/v202/frantar23a.html
- **Code Link:** https://github.com/IST-DASLab/sparsegpt

### Short Summary
SparseGPT shows that large language models can be pruned effectively with a one-shot, post-training procedure. This is important because it avoids the expensive retraining loops that make many pruning methods impractical at LLM scale. The method uses local second-order information to decide which parameters can be removed with limited quality loss. It became a key reference for the return of pruning in the LLM era. The paper also motivated later work on combined sparsity and quantization pipelines.

### Core Innovation
- One-shot pruning method that avoids full retraining at LLM scale.
- Practical use of second-order approximations for structured parameter removal.
- Strong evidence that post-training sparsification is viable for large transformers.

### Technical Approach
- Weight blocks are pruned using local Hessian-informed approximations.
- The procedure iterates layer by layer while approximately correcting for induced error.
- The method is designed to keep the workflow feasible on large pretrained models.

### Results
- Evaluated across several large language model families and sparsity targets.
- The paper reports strong retention of model quality relative to naive pruning baselines.
- Results made pruning newly relevant for efficient LLM deployment discussions.

### Potential Drawbacks
- Kernel support for unstructured or semi-structured sparsity remains uneven in production systems.
- Quality can degrade sharply at very high sparsity ratios.

## [The Devil is in the Tails: How Long-Tailed Code Distributions Impact Large Language Models]

- **Authors:** Xin Zhou, Kisub Kim, Bowen Xu, Jiakun Liu, DongGyun Han, David Lo
- **Venue:** ASE 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/ase-2023/ase-2023-papers/66/The-Devil-is-in-the-Tails-How-Long-Tailed-Code-Distributions-Impact-Large-Language-M
- **Code Link:** N/A

### Short Summary
This ASE paper studies a practical weakness of code LLMs: software corpora are long-tailed, and rare patterns can dominate failure cases. The paper examines how distribution imbalance affects model behavior instead of only headline average accuracy. That perspective is valuable because software-engineering use cases often care about precisely the rare cases that general-purpose code models miss. The work therefore complements mainstream LLM papers by focusing on deployment-relevant data skew. It is tagged `Hodgepodge` because the venue is software engineering, but the paper is clearly AI-related.

### Core Innovation
- Long-tail analysis of code LLM performance.
- Shift from average-case evaluation to rare-pattern robustness.
- Software-engineering framing of model-data mismatch.

### Technical Approach
- The study partitions code distributions into frequent and rare patterns.
- It evaluates how language models degrade across these tails.
- The analysis connects empirical behavior to data imbalance in code corpora.

### Results
- Benchmarks include code-modeling and code-understanding tasks.
- The paper reports significant performance sensitivity to long-tail distribution effects.
- Results argue for more careful training and evaluation on rare code patterns.

### Potential Drawbacks
- The work is primarily diagnostic rather than a full algorithmic fix.
- Findings can depend on the exact code corpora used for analysis.

## [An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair]

- **Authors:** Kai Huang, Xiangxin Meng, Jian Zhang, Yang Liu, Wenjie Wang, Shuhao Li, Yuqing Zhang
- **Venue:** ASE 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, Model Compression, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/ase-2023/ase-2023-papers/98/An-Empirical-Study-on-Fine-tuning-Large-Language-Models-of-Code-for-Automated-Program
- **Code Link:** N/A

### Short Summary
This paper evaluates whether code-focused LLMs can be fine-tuned effectively for automated program repair. Rather than introducing a new base model, it studies adaptation behavior, repair quality, and limitations in a software-engineering setting. That makes it useful for the atlas because it shows how LLM adaptation techniques transfer into a high-value engineering workflow. The findings are mostly empirical, but they reveal where generic code LLMs are brittle when moved into repair pipelines. It is another explicit venue-coverage entry with a clear AI connection.

### Core Innovation
- Empirical evaluation of code-LLM fine-tuning for automated repair.
- Detailed focus on an applied software-engineering use case.
- Clear comparison between generic code generation and repair-specific adaptation.

### Technical Approach
- Code LLMs are fine-tuned or adapted on repair-oriented datasets.
- Evaluation measures patch plausibility and task-specific success rates.
- The paper analyzes both improvements and common failure modes.

### Results
- Benchmarks involve automated program repair tasks on bug datasets.
- The paper reports measurable gains from repair-oriented fine-tuning over untuned baselines.
- Results also show remaining generalization and correctness limitations.

### Potential Drawbacks
- Repair success can still depend heavily on dataset construction and validation protocol.
- The connection to the atlas core is weaker than systems or compiler papers.

## [Multilingual Code Co-evolution using Large Language Models]

- **Authors:** Jiyang Zhang, Pengyu Nie, Junyi Jessy Li, Milos Gligoric
- **Venue:** FSE 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, Hodgepodge
- **Paper Link:** https://2023.esec-fse.org/details/fse-2023-research-papers/109/Multilingual-Code-Co-Evolution-Using-Large-Language-Models
- **Code Link:** N/A

### Short Summary
This FSE paper studies how large language models can support co-evolution across multilingual codebases. That problem matters in real software systems because logic often spans multiple languages and synchronized changes are hard to maintain. The paper treats LLMs as assistants for coordinated evolution rather than only for single-file completion. It is relevant to the atlas because it reflects one of the main 2023 themes: LLMs moving into concrete developer workflows. The fit is software-engineering-heavy, so it is tagged `Hodgepodge`.

### Core Innovation
- LLM framing of multilingual co-evolution in software maintenance.
- Focus on consistency across multiple programming languages.
- Practical engineering task beyond standalone code completion.

### Technical Approach
- The system or study analyzes related changes across multilingual components.
- Language models are used to propose, align, or evaluate coordinated edits.
- The evaluation focuses on whether cross-language consistency can be improved.

### Results
- Evaluated on multilingual software-evolution scenarios.
- The paper reports that LLM support can improve consistency or reduce manual effort in selected settings.
- Results emphasize the promise and fragility of LLM assistance in maintenance tasks.

### Potential Drawbacks
- Correctness remains hard to guarantee across multiple languages and toolchains.
- The paper is more software-maintenance-oriented than core AI systems work.

## [Baldur: Whole-Proof Generation and Repair with Large Language Models]

- **Authors:** Emily First, Markus N. Rabe, Talia Ringer, Yuriy Brun
- **Venue:** FSE 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, Compiler Optimization, Hodgepodge
- **Paper Link:** https://2023.esec-fse.org/details/fse-2023-research-papers/2/Baldur-Whole-Proof-Generation-and-Repair-with-Large-Language-Models
- **Code Link:** N/A

### Short Summary
Baldur applies large language models to proof generation and proof repair, connecting code-oriented LLM work with formal methods. This is not a central atlas topic, but it is a useful boundary case because it studies structured reasoning over formal artifacts. The paper explores whether language models can help generate whole proofs instead of only local edits. That places it near the broader reasoning-systems discussion even though the venue is software engineering. It is tagged `Hodgepodge` to make that boundary explicit.

### Core Innovation
- Whole-proof generation and repair with language models.
- Application of LLMs to formal artifacts rather than natural-language-only tasks.
- Bridge between software engineering and structured reasoning.

### Technical Approach
- The system represents proof states and repair objectives in a promptable form.
- The language model proposes proof steps or repaired proofs.
- The outputs are checked against the formal environment for validity.

### Results
- Evaluated on proof-generation and proof-repair tasks.
- The paper reports promising gains relative to simpler heuristic or baseline approaches.
- Results show both the potential and brittleness of LLMs in formal reasoning settings.

### Potential Drawbacks
- Formal validity remains a hard constraint that language models frequently violate.
- The connection to the atlas core topics is indirect.

## [Large Language Models Are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models]

- **Authors:** Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, Lingming Zhang
- **Venue:** ISSTA 2023
- **Year:** 2023
- **Tags:** LLM Systems & Algorithms, Hodgepodge, AI Infrastructure
- **Paper Link:** https://2023.issta.org/details/issta-2023-technical-papers/27/Large-Language-Models-Are-Zero-Shot-Fuzzers-Fuzzing-Deep-Learning-Libraries-via-Larg
- **Code Link:** N/A

### Short Summary
This paper asks whether large language models can generate useful fuzzing inputs for deep-learning libraries with little or no task-specific tuning. That makes it unusually relevant to this atlas because the target systems are AI libraries rather than generic software alone. The work combines software testing methodology with a practical AI-infrastructure target. It is an example of how LLMs started to alter evaluation and bug-finding workflows around ML systems. The venue is outside the atlas core, but the technical target is close enough to include.

### Core Innovation
- Zero-shot fuzzing strategy driven by language models.
- Direct application to deep-learning libraries rather than generic code only.
- Practical link between LLM prompting and AI-system robustness testing.

### Technical Approach
- The model is prompted to generate inputs or programs likely to trigger unusual behaviors.
- Generated artifacts are fed into fuzzing-style workflows for DL libraries.
- The system measures whether model-generated cases expose crashes, inconsistencies, or edge cases.

### Results
- Benchmarks target testing of deep-learning libraries.
- The paper reports that LLM-guided fuzzing can discover useful edge cases without heavy task-specific engineering.
- Results support LLMs as flexible generators in testing pipelines.

### Potential Drawbacks
- Coverage and reliability depend strongly on prompt design.
- The method is more a testing workflow than a core model or systems contribution.

## [TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings]

- **Authors:** Norman P. Jouppi et al.
- **Venue:** ISCA 2023
- **Year:** 2023
- **Tags:** AI Infrastructure, HPC
- **Paper Link:** https://dblp.org/rec/conf/isca/JouppiK0MNNPSST23
- **Code Link:** N/A

### Short Summary
The TPU v4 paper describes a supercomputer-scale ML system with architectural support tuned for modern recommendation and embedding-heavy workloads. It is important because it shows how cluster design, optical reconfiguration, and hardware support for irregular model components fit together in production-scale ML. The paper goes beyond a single accelerator chip and focuses on the full system. That makes it a strong atlas entry for infrastructure-aware machine learning. It also fills ISCA coverage with a clearly AI-centered architecture paper.

### Core Innovation
- Supercomputer-scale ML architecture with optical reconfiguration.
- Hardware support for embedding-heavy workloads.
- Full-system treatment of accelerator, network, and cluster design for ML.

### Technical Approach
- The design combines specialized ML hardware with a reconfigurable interconnect.
- System features are tuned for large-scale distributed training and serving workloads.
- The architecture pays special attention to embeddings and communication-heavy ML tasks.

### Results
- Evaluated on large machine-learning workloads inside production-style infrastructure.
- The paper reports strong scalability and efficiency for ML-relevant tasks.
- Results show system-level co-design is essential once accelerator clusters reach supercomputer scale.

### Potential Drawbacks
- The platform is highly specialized and difficult to reproduce outside large organizations.
- Benefits depend on workloads that can exploit the custom interconnect and accelerator stack.

## [ViTCoD: Vision Transformer Acceleration via Dedicated Algorithm and Accelerator Co-Design]

- **Authors:** Haoran You et al.
- **Venue:** HPCA 2023
- **Year:** 2023
- **Tags:** AI Infrastructure, GPU Optimization
- **Paper Link:** https://dblp.org/rec/conf/hpca/YouSSYZZLLL23
- **Code Link:** N/A

### Short Summary
ViTCoD targets the performance gap between generic accelerators and the particular structure of vision transformers. The paper co-designs algorithmic structure and accelerator behavior rather than treating the model as a fixed workload. That is valuable because transformers outside NLP bring different attention and tensor-shape constraints that hardware must handle efficiently. The work therefore sits at the intersection of model design and architecture design. It provides a clean HPCA entry with direct AI-system relevance.

### Core Innovation
- Co-design of vision-transformer algorithms and accelerator architecture.
- Hardware-aware treatment of transformer-specific bottlenecks.
- Strong emphasis on specialization rather than generic acceleration alone.

### Technical Approach
- The design analyzes attention and feed-forward components in vision transformers.
- Accelerator dataflow and execution strategies are tuned to those workloads.
- The paper studies how algorithm-level restructuring can improve hardware efficiency.

### Results
- Evaluated on representative vision-transformer workloads.
- The paper reports improved efficiency relative to less specialized accelerator baselines.
- Results support model-architecture co-design for transformer acceleration.

### Potential Drawbacks
- Specialization can limit portability to rapidly changing model designs.
- Benefits may shrink for workloads that diverge from the target transformer patterns.
