# Notes 2024

### Trend: Long Context And Low-Bit Serving
- Long-context inference triggered renewed work on attention sparsity and runtime scheduling.
- Quantization papers moved from standalone calibration tricks toward full serving-stack co-design.
- Structured program execution became a practical systems topic rather than an orchestration afterthought.

### Note: Infrastructure Validation As A First-Class AI Systems Problem
- Papers such as `SuperBench` and `ServiceLab` make a useful distinction between outright failures and tiny hidden regressions.
- In large GPU fleets, reliability is partly a statistical testing problem: small per-node slowdowns compound into large cluster-level waste.
- This shifts some systems math from operator-level cost models toward variance estimation and controlled performance experimentation.
