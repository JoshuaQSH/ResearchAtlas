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
