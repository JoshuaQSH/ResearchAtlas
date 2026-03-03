# 2025 Compiler Papers

## [LLM Compiler: Foundation Language Models for Compiler Optimization]

- **Authors:** Chris Cummins, Volker Seeker, Dejan Grubisic, Baptiste Roziere, Jonas Gehring, Gabriel Synnaeve, Hugh Leather
- **Venue:** CC 2025
- **Year:** 2025
- **Tags:** Compiler Optimization, LLM Systems & Algorithms
- **Paper Link:** https://dblp.org/rec/conf/cc/CumminsSGRGSL25
- **Code Link:** N/A

### Short Summary
LLM Compiler studies whether foundation language models can act directly as compiler optimizers rather than only as assistants around compiler development. The paper is relevant because it shifts compiler optimization from a hand-designed heuristic space toward a model-driven one. It also brings the recent wave of LLM capability into a classical compiler-construction venue. The contribution is conceptually important even where traditional heuristics remain stronger on some workloads. It provides a clean CC entry with direct overlap between LLM algorithms and compiler optimization.

### Core Innovation
- Direct use of foundation models for compiler optimization decisions.
- Strong bridge between LLM reasoning and compiler-construction workflows.
- Extension of language-model capability into a traditional systems domain.

### Technical Approach
- The system represents compiler optimization problems in a form consumable by large language models.
- It evaluates whether model-driven choices can improve or guide compiler behavior.
- The work compares LLM-based optimization against conventional compiler strategies.

### Results
- Evaluated on compiler-optimization tasks and program benchmarks.
- The paper reports that foundation models can be useful for selected optimization decisions.
- Results motivate further study of LLMs as active components in compiler pipelines.

### Potential Drawbacks
- Reliability and generalization remain open problems compared with mature compiler heuristics.
- Model cost can be hard to justify for latency-sensitive optimization passes.
