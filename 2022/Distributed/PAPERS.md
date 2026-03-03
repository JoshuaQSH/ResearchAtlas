# 2022 Distributed Papers

## [PaLM: Scaling Language Modeling with Pathways]

- **Authors:** Aakanksha Chowdhery et al.
- **Venue:** arXiv / Google Research
- **Year:** 2022
- **Tags:** LLM Systems & Algorithms, AI Infrastructure, Distributed Deep Learning
- **Paper Link:** https://arxiv.org/abs/2204.02311
- **Code Link:** N/A

### Short Summary
PaLM is a large-scale language model report that combines scaling-law thinking with a production training stack capable of handling very large dense models. The paper is important not only for model quality but also for the engineering story around data, compute, and distributed optimization. It shows that a sufficiently large dense model can produce strong few-shot and chain-of-thought performance across many tasks. The report also makes clear that system design and model design are inseparable at this scale. Later open and closed foundation-model projects routinely cite PaLM as a reference point for large dense training.

### Core Innovation
- End-to-end demonstration of large dense LLM pretraining at Pathways scale.
- Strong evidence that scale plus careful training yields broad reasoning improvements.
- A widely cited reference for integrating model design with cluster-scale infrastructure.

### Technical Approach
- The model is trained as a large autoregressive transformer using distributed data and model parallel execution.
- Training design emphasizes large batch optimization, large corpora, and stable scaling to very high parameter counts.
- Evaluation includes standard language modeling, multilingual, commonsense, and reasoning benchmarks.

### Results
- Benchmarks include BIG-bench, MMLU-style academic tasks, and multilingual evaluations.
- The paper reports strong few-shot performance and notable improvements on reasoning tasks.
- Results helped reset expectations for dense-model capability before the open-weight wave of 2023.

### Potential Drawbacks
- The report provides limited reproducibility for most researchers because the full training setup is inaccessible.
- Environmental and cost implications are substantial for this scale of dense pretraining.

## [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale]

- **Authors:** Shaden Smith et al.
- **Venue:** ICML 2022
- **Year:** 2022
- **Tags:** Distributed Deep Learning, AI Infrastructure, Sparse Matrix & Kernels
- **Paper Link:** https://proceedings.mlr.press/v162/rajbhandari22a.html
- **Code Link:** https://github.com/microsoft/DeepSpeed

### Short Summary
DeepSpeed-MoE studies how to make mixture-of-experts models usable at training and inference time rather than just interesting on paper. The paper focuses on communication, memory placement, and expert parallel execution, which are the real bottlenecks in sparse expert models. It also shows how system-level optimizations can preserve the algorithmic benefits of sparse activation instead of giving them back in overhead. The work is influential because many later MoE training stacks inherit its decomposition of data, model, and expert parallelism. It marked a transition from MoE papers as modeling ideas to MoE papers as full systems artifacts.

### Core Innovation
- A practical expert-parallel training and inference stack integrated into DeepSpeed.
- System techniques that reduce communication and memory overhead in sparse MoE workloads.
- A full-stack view that connects routing sparsity with distributed systems constraints.

### Technical Approach
- Experts are partitioned across devices while tokens are dynamically routed to active experts.
- The runtime coordinates all-to-all style communication with memory-aware scheduling.
- Optimizations target both training throughput and inference latency for sparse transformer layers.

### Results
- Evaluated on large-scale MoE language model settings.
- The paper reports substantial efficiency improvements relative to less optimized sparse baselines.
- Results show sparse expert models can achieve competitive quality without dense-model compute cost.

### Potential Drawbacks
- Expert routing still introduces irregular communication that can be hard to optimize on commodity clusters.
- Benefits depend heavily on balanced routing and sufficient batch size.

## [ZeroQuant: Efficient and Affordable Post-Training Quantization for Large-Scale Transformers]

- **Authors:** Qinghao Hu et al.
- **Venue:** NeurIPS 2022 Workshop / arXiv 2022
- **Year:** 2022
- **Tags:** Model Quantization, Model Compression, AI Infrastructure
- **Paper Link:** https://arxiv.org/abs/2206.01861
- **Code Link:** https://github.com/microsoft/DeepSpeedExamples/tree/master/inference/huggingface/zero_inference

### Short Summary
ZeroQuant addresses the deployment problem that large transformer models are too expensive to serve at full precision in many real systems. The paper combines post-training quantization with quantization-friendly runtime support so the method is not just a calibration trick. It emphasizes accuracy preservation for large language models while reducing inference cost. The work also helped normalize weight-and-activation quantization as a practical path for large-model serving. It is a useful bridge between classic compression literature and the modern LLM deployment stack.

### Core Innovation
- Post-training quantization tailored to large transformers rather than smaller vision models.
- Co-design between quantized model representation and the serving runtime.
- Practical focus on preserving downstream accuracy without expensive retraining.

### Technical Approach
- The method calibrates low-bit weights and activations using a small data pass.
- Quantization is paired with efficient inference kernels and memory layout choices.
- Layer-wise handling is designed to keep difficult transformer blocks stable after quantization.

### Results
- Evaluated on BERT- and GPT-style transformer deployments.
- The paper reports improved speed and reduced memory footprint while retaining strong task accuracy.
- Results highlight quantization as a cost-control mechanism for production inference.

### Potential Drawbacks
- Sensitivity can vary substantially across architectures and layers.
- The strongest gains depend on an inference stack that is aware of the quantized format.
