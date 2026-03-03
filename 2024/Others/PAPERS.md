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
