# 2024 Other Papers

## [AQLM: Accurate Quantization for Language Models]

- **Authors:** Yury Egorov et al.
- **Venue:** arXiv 2024
- **Year:** 2024
- **Tags:** Model Quantization, Model Compression, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2401.06118
- **Code Link:** https://github.com/Vahe1994/AQLM

### Short Summary
AQLM studies how to push quantization quality further for language models without giving up practical deployment value. The paper focuses on accuracy-preserving representation design and calibration choices for low-bit weights. This is useful because many serving systems rely on quantization methods whose tradeoffs are not uniform across model families. AQLM provides another strong point in the design space between aggressive compression and stable accuracy. It is representative of the rapid refinement phase of LLM PTQ in 2024.

### Core Innovation
- Quantization scheme tuned for stronger accuracy retention on LLMs.
- Emphasis on practical low-bit deployment rather than purely theoretical compression.
- Useful refinement of the post-training quantization design space.

### Technical Approach
- The method selects quantization parameters and representations to reduce language-model sensitivity.
- Calibration and layer-wise handling are designed for transformer stability.
- The resulting model is intended to map into efficient low-bit inference kernels.

### Results
- Evaluated on open LLM families and downstream language benchmarks.
- The paper reports favorable quality-efficiency tradeoffs against strong PTQ baselines.
- Results contributed to a crowded but fast-improving quantization landscape.

### Potential Drawbacks
- Improvements can be model-family dependent.
- Serving gains still depend on whether the target runtime supports the chosen low-bit format well.

## [QQQ: Quality Control for Quantization of Large Language Models]

- **Authors:** Jiaming Tang et al.
- **Venue:** arXiv 2024
- **Year:** 2024
- **Tags:** Model Quantization, Model Compression
- **Paper Link:** https://arxiv.org/abs/2406.09904
- **Code Link:** https://github.com/HandH1998/QQQ

### Short Summary
QQQ focuses on preserving model quality under aggressive quantization by explicitly controlling error-sensitive components. The paper belongs to the mature phase of LLM PTQ, where the core question is no longer whether quantization works but how robustly it works across models and tasks. It contributes practical guidance on maintaining accuracy while still targeting efficient inference formats. This is relevant for real deployments because regressions on a small set of sensitive layers can erase much of the compression benefit. The work fits well with the broader trend toward more reliable PTQ pipelines.

### Core Innovation
- Quality-oriented quantization strategy that targets the most error-sensitive model parts.
- Practical emphasis on robustness across downstream tasks.
- Another step away from one-size-fits-all quantization heuristics.

### Technical Approach
- Quantization decisions are adjusted based on observed sensitivity during calibration.
- Layer- or group-specific treatment is used where uniform quantization would be too destructive.
- The pipeline is meant to remain practical for large pretrained models.

### Results
- Evaluated on multiple LLM families and task suites.
- The paper reports better accuracy preservation than simpler low-bit baselines in challenging settings.
- Results support more selective and quality-aware PTQ workflows.

### Potential Drawbacks
- Additional control logic increases pipeline complexity.
- More selective schemes can reduce the simplicity that makes some PTQ methods easy to deploy.

## [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs]

- **Authors:** Markus Ashboos et al.
- **Venue:** NeurIPS 2024
- **Year:** 2024
- **Tags:** Model Quantization, CUDA Kernels, GPU Optimization
- **Paper Link:** https://arxiv.org/abs/2404.00456
- **Code Link:** https://github.com/spcl/QuaRot

### Short Summary
QuaRot proposes rotating the representation space of LLMs so that quantization outliers are easier to manage. The paper is notable because it targets one of the recurrent failure modes in low-bit inference: a small number of problematic channels dominate error. By reshaping the representation, the method enables more uniform low-bit quantization behavior. That gives it both algorithmic interest and systems relevance, since more uniform formats are easier to implement efficiently. It is part of the broader 2024 effort to make 4-bit inference less brittle.

### Core Innovation
- Rotation-based handling of quantization outliers in LLMs.
- Better compatibility between accuracy preservation and efficient low-bit execution.
- A clean conceptual approach to a recurring PTQ failure mode.

### Technical Approach
- Model representations are transformed so that extreme outlier behavior is reduced.
- The rotated form is then quantized into a low-bit inference format.
- The method aims to preserve function while improving compression robustness.

### Results
- Evaluated on open LLMs under 4-bit inference settings.
- The paper reports improved quality relative to outlier-sensitive quantization baselines.
- Results suggest representation shaping is a useful tool in the PTQ toolbox.

### Potential Drawbacks
- Rotation steps add implementation complexity and compatibility considerations.
- End-to-end serving gains still depend on efficient kernel support for the resulting format.

## [Large Language Models for Test-Free Fault Localization]

- **Authors:** Aidan Z. H. Yang, Claire Le Goues, Ruben Martins, Vincent J. Hellendoorn
- **Venue:** ICSE 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/icse-2024/icse-2024-research-track/60/Large-Language-Models-for-Test-Free-Fault-Localization
- **Code Link:** N/A

### Short Summary
This ICSE paper explores whether large language models can localize software faults without relying on executable tests. That is important in settings where failing tests are incomplete, unavailable, or expensive to construct. The work is AI-related but software-engineering-heavy, so it is included as a `Hodgepodge` venue-coverage paper. Its main value for the atlas is showing how reasoning-style LLM behavior gets repurposed for program understanding workflows. It also illustrates the rapid migration of LLMs into diagnostic engineering tasks in 2024.

### Core Innovation
- Fault localization driven by language models rather than tests alone.
- Applied use of LLM reasoning in program diagnosis.
- A practical software-engineering workflow for LLMs.

### Technical Approach
- The system prompts or conditions the model on code and bug context.
- The model ranks or proposes suspicious locations in the program.
- Evaluation compares localization quality against traditional or heuristic baselines.

### Results
- Benchmarks involve software-fault localization tasks.
- The paper reports that LLM-based localization can be competitive in selected scenarios.
- Results indicate that language models can contribute useful priors without dynamic execution.

### Potential Drawbacks
- Localization quality can be brittle and difficult to calibrate.
- The paper is only loosely aligned with the atlas core topics.

## [Traces of Memorisation in Large Language Models for Code]

- **Authors:** Ali Al-Kaswan, Maliheh Izadi, Arie van Deursen
- **Venue:** ICSE 2024
- **Year:** 2024
- **Tags:** Explainable AI, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/icse-2024/icse-2024-research-track/133/Traces-of-Memorisation-in-Large-Language-Models-for-Code
- **Code Link:** N/A

### Short Summary
This paper studies memorization in code LLMs, a topic that matters for both privacy and model interpretability. It does not present a serving or compiler contribution, but it is useful for the atlas because understanding memorization is a key part of making code models explainable and trustworthy. The paper investigates how often outputs appear memorized rather than generalized. That makes it a practical interpretability study for generative models on software artifacts. It is tagged `Hodgepodge` because the venue focus is software engineering.

### Core Innovation
- Empirical analysis of memorization behavior in code LLMs.
- Link between trust, privacy, and model interpretability.
- Practical study of a failure mode in code generation systems.

### Technical Approach
- The paper probes model outputs for signs of training-data memorization.
- It compares memorized behavior against more generalizable code synthesis behavior.
- The analysis focuses on realistic code-generation settings rather than only synthetic prompts.

### Results
- Evaluated on code-generation scenarios involving code LLMs.
- The paper reports measurable memorization effects that matter for deployment and trust.
- Results argue for more rigorous memorization-aware evaluation of code models.

### Potential Drawbacks
- Memorization is hard to define perfectly and can be confounded with common-pattern recall.
- The contribution is empirical rather than a direct mitigation method.

## [LLMParser: An Exploratory Study on Using Large Language Models for Log Parsing]

- **Authors:** Zeyang Ma, An Ran Chen, Dong Jae Kim, Tse-Hsun Chen, Shaowei Wang
- **Venue:** ICSE 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, AI Infrastructure, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/icse-2024/icse-2024-research-track/150/LLMParser-An-Exploratory-Study-on-Using-Large-Language-Models-for-Log-Parsing
- **Code Link:** N/A

### Short Summary
LLMParser examines whether language models can replace or augment traditional log-parsing heuristics. This is relevant to AI infrastructure because modern training and serving systems generate large, messy operational logs that are expensive to parse manually. The paper treats parsing as an exploratory LLM-assisted task rather than a fixed rule-engine problem. That makes it an interesting operations-facing complement to mainstream model-serving work. It is included with `Hodgepodge` because its home venue is software engineering.

### Core Innovation
- LLM-assisted log parsing for operational software systems.
- Shift from rule-heavy parsers to general language reasoning.
- Clear connection between LLMs and observability workflows.

### Technical Approach
- The system prompts or adapts an LLM to identify templates and structure in logs.
- Parsed outputs are evaluated against traditional parsers and annotated datasets.
- The study focuses on robustness across heterogeneous log formats.

### Results
- Benchmarks target real-world log parsing tasks.
- The paper reports that LLM-based parsing can be competitive and more flexible on heterogeneous inputs.
- Results show language models can reduce manual parser engineering in some settings.

### Potential Drawbacks
- Cost and latency can be problematic for large-scale online parsing.
- Operational reliability may still favor simpler specialized parsers in production.

## [Fuzz4All: Universal Fuzzing with Large Language Models]

- **Authors:** Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian, Michael Pradel, Lingming Zhang
- **Venue:** ICSE 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, Hodgepodge, AI Infrastructure
- **Paper Link:** https://conf.researchr.org/details/icse-2024/icse-2024-research-track/119/Fuzz4All-Universal-Fuzzing-with-Large-Language-Models
- **Code Link:** N/A

### Short Summary
Fuzz4All uses large language models to generalize fuzzing across multiple domains instead of building domain-specific generators each time. That is a meaningful AI-systems-adjacent idea because fuzzing ML libraries, DSLs, and compilers often suffers from brittle input-generation logic. The paper frames the LLM as a universal input generator guided by task structure. It therefore sits between software testing and LLM reasoning. The venue fit is software engineering, so the entry uses `Hodgepodge`.

### Core Innovation
- Universal fuzzing workflow built around LLM input generation.
- Reduced dependence on domain-specific handcrafted generators.
- Flexible testing application to AI-related libraries and languages.

### Technical Approach
- Prompts and feedback loops guide the model to generate structured test inputs.
- The system then executes those inputs in standard fuzzing or bug-finding pipelines.
- Coverage and discovered failures are used to assess effectiveness.

### Results
- Evaluated across multiple domains rather than a single narrow fuzzing target.
- The paper reports that LLM-guided fuzzing can find useful bugs with relatively low manual setup.
- Results suggest language models are viable general-purpose input generators for testing.

### Potential Drawbacks
- Generated inputs can be redundant or semantically shallow without strong feedback signals.
- The paper is not a core systems-runtime contribution.

## [Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions]

- **Authors:** Zhe Liu et al.
- **Venue:** ICSE 2024
- **Year:** 2024
- **Tags:** LLM Systems & Algorithms, Hodgepodge
- **Paper Link:** https://conf.researchr.org/details/icse-2024/icse-2024-research-track/180/Make-LLM-a-Testing-Expert-Bringing-Human-like-Interaction-to-Mobile-GUI-Testing-via-
- **Code Link:** N/A

### Short Summary
This paper applies LLMs to mobile GUI testing by modeling interaction decisions in a more human-like way. It belongs to the growing family of papers where language models act as adaptive controllers rather than pure text generators. That perspective is relevant to the atlas because it shows how LLM reasoning can be embedded into search and exploration loops. The concrete domain is software testing, so the paper is tagged `Hodgepodge`. It still adds useful evidence for LLMs as general decision-making components in engineering workflows.

### Core Innovation
- Functionality-aware GUI testing driven by an LLM.
- More human-like interaction strategy than fixed exploration heuristics.
- Use of language reasoning in sequential software-testing control.

### Technical Approach
- The system observes mobile-GUI context and chooses actions with an LLM-guided policy.
- Decisions are shaped by functionality cues rather than only surface-level navigation.
- The evaluation compares exploration and bug-finding behavior against existing testing tools.

### Results
- Benchmarks target Android or mobile GUI testing scenarios.
- The paper reports stronger task-directed exploration in selected cases.
- Results support the view that LLMs can act as flexible control policies in testing loops.

### Potential Drawbacks
- Reproducibility and stability can depend heavily on prompt and model choice.
- The fit to the atlas core topics is weak.

## [DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation]

- **Authors:** Mingke Yang, Yuqi Chen, Yi Liu, Ling Shi
- **Venue:** ISSTA 2024
- **Year:** 2024
- **Tags:** Explainable AI, LLM Systems & Algorithms, Hodgepodge
- **Paper Link:** https://2024.issta.org/details/issta-2024-papers/47/DistillSeq-A-Framework-for-Safety-Alignment-Testing-in-Large-Language-Models-using-K
- **Code Link:** N/A

### Short Summary
DistillSeq targets safety-alignment testing for large language models and uses knowledge distillation to improve the testing process. This paper is useful for the atlas because it touches model behavior analysis rather than only deployment efficiency. Testing safety alignment is increasingly important as LLMs are integrated into engineering systems with broader action spaces. The work sits close to explainability and evaluation, though it comes from a testing venue. It is included as `Hodgepodge` because the software-testing framing dominates.

### Core Innovation
- Safety-alignment testing framework for LLMs.
- Use of distillation to support scalable or structured testing.
- Evaluation-focused contribution on model behavioral reliability.

### Technical Approach
- The framework builds a distilled representation to help probe safety-relevant behaviors.
- Test cases are generated or organized around alignment-sensitive scenarios.
- The system measures whether the model remains aligned across those probes.

### Results
- Evaluated on LLM safety-alignment testing scenarios.
- The paper reports improved efficiency or coverage over less structured testing approaches.
- Results support more systematic testing for aligned model behavior.

### Potential Drawbacks
- Safety testing remains only a partial proxy for real-world harmful behavior.
- The systems contribution is limited relative to core runtime papers.
