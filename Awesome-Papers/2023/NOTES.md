# Notes 2023

### Trend: Serving And Compression Converge
- Inference systems and quantization papers started to co-evolve instead of living in separate communities.
- Open-weight models accelerated systems benchmarking because reproducible baselines became easy to share.
- Sparse and low-bit methods became production-facing rather than purely academic compression topics.

### Note: Explanation and Testing Spill Into LLM Infrastructure
- `Explainable AI` entries in 2023 are no longer limited to classic attribution papers; graph explainability and code-model analysis start to overlap with deployment trust.
- LLM-assisted testing papers use the model as a search policy or structured-input generator, which is architecturally closer to an agent loop than to static code completion.
- For fuzzing-style workflows, the effective kernel is often the feedback loop `generate -> execute -> score -> refine`, not the language model in isolation.
