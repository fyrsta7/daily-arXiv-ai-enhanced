# 自动代码优化强相关论文精选

> 数据范围：2026-04-18 至 2026-07-22；生成时间：2026-07-22T17:30:31+00:00。
> 以 SemOpt 的“程序分析/策略知识 + LLM 自动改写 + 正确性与真实性能验证”为研究锚点，只保留强相关论文。

共筛选 **76** 篇（去重候选论文 7105 篇，模型评估 2247 篇）。

## 快速索引

1. [daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization](#1) — 0.98
2. [Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games](#2) — 0.98
3. [PassNet: Scaling Large Language Models for Graph Compiler Pass Generation](#3) — 0.98
4. [Optimas: An Intelligent Analytics-Informed Generative AI Framework for Performance Optimization](#4) — 0.98
5. [Beyond the Need for Speed: Energy-Aware Code Generation via Simulation-Guided Reinforcement Learning](#5) — 0.96
6. [Understanding Agent-Based Patching of Compiler Missed Optimizations](#6) — 0.96
7. [EGG: An Expert-Guided Agent Framework for Kernel Generation](#7) — 0.96
8. [AUTOGATE: Automated Clock Gating via Toggling-Aware LLM-based RTL Rewriting](#8) — 0.96
9. [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](#9) — 0.96
10. [Learning When to Optimize: Verified Optimization Skills from Expert GPU-Kernel Lineages](#10) — 0.96
11. [SIA: Self Improving AI with Harness & Weight Updates](#11) — 0.96
12. [Metal-Sci: A Scientific Compute Benchmark for Evolutionary LLM Kernel Search on Apple Silicon](#12) — 0.96
13. [CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement](#13) — 0.96
14. [MOA: A Profiling-Guided LLM Framework for Memory-Optimization Automation at Codebase Scale](#14) — 0.95
15. [AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning](#15) — 0.95
16. [AI-PROPELLER: Warehouse-Scale Interprocedural Code Layout Optimization with AlphaEvolve](#16) — 0.95
17. [AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents](#17) — 0.95
18. [SkillEvolver: Skill Learning as a Meta-Skill](#18) — 0.95
19. [ARIADNE: Agentic Reward-Informed Adaptive Decision Exploration via Blackboard-Driven MCTS for Competitive Program Generation](#19) — 0.95
20. [Agentic Architect: An Agentic AI Framework for Architecture Design Exploration and Optimization](#20) — 0.95
21. [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](#21) — 0.94
22. [An Ocean Model Ported by a Large Language Model: Experience and Lessons from FESOM2 (Fortran to C to C++/Kokkos)](#22) — 0.94
23. [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](#23) — 0.93
24. [PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization](#24) — 0.93
25. [Hawk: Harnessing Hardware-Aware Knowledge for High-Performance NPU Kernel Generation](#25) — 0.93
26. [Towards Autonomous Accelerator Design: FPGA Accelerator Generation with SECDA](#26) — 0.93
27. [GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization](#27) — 0.93
28. [FastKernels: Benchmarking GPU Kernel Generation in Production](#28) — 0.93
29. [Distribution-Aware Algorithm Design with LLM Agents](#29) — 0.93
30. [CppPerf: An Automated Pipeline and Dataset for Performance-Improving C++ Commits](#30) — 0.93
31. [AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance](#31) — 0.92
32. [Evaluating LLMs on Real-World Software Performance Optimization](#32) — 0.92
33. [LLM-Guided Test-Time Discovery of Quantum-Chemical Approximation Algorithms](#33) — 0.92
34. [PreAct: Computer-Using Agents that Get Faster on Repeated Tasks](#34) — 0.92
35. [Embedded Arena: Iterative Optimization via Hardware Feedback](#35) — 0.92
36. [Structuring agentic AI for HPC code modernization](#36) — 0.92
37. [AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference](#37) — 0.92
38. [The Time is Here for Just-in-Time Systems: Challenges and Opportunities](#38) — 0.92
39. [CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging](#39) — 0.92
40. [Heuristic Learning for Active Flow Control Using Coding Agents](#40) — 0.90
41. [Rethinking Code Performance Benchmarks for LLMs](#41) — 0.90
42. [Auto: The AGI Compiler](#42) — 0.90
43. [Copper: Unifying Correctness and Performance Specification in Code Generation](#43) — 0.90
44. [Can Coding Agents Implement Missed Compiler Optimizations? Evaluating LLM Agents on LLVM Peephole Optimizations](#44) — 0.90
45. [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](#45) — 0.90
46. [JETO-Bench: A Reproducible Benchmark for Execution Time Improvement Patches in Java](#46) — 0.90
47. [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](#47) — 0.90
48. [Chiseling Out Efficiency: Structured Skeleton Supervision for Efficient Code Generation](#48) — 0.90
49. [Systematic LLM Translation of Legacy Scientific Code to Differentiable Frameworks: Application to a Land Surface Model](#49) — 0.90
50. [CodegenBench: Can LLMs Write Efficient Code Across Architectures?](#50) — 0.90
51. [Step-TP: A Grounded, Step-Level Dataset with Chain-of-Thought Reasoning for LLM-Guided Tensor Program Optimization](#51) — 0.90
52. [CoRe-Code: Collaborative Reinforcement Learning for Code Generation](#52) — 0.90
53. [JEDI: Java Evaluation of Declarative and Imperative Queries](#53) — 0.90
54. [MileStone: A Multi-Objective Compiler Phase Ordering Framework for Graph-based IR-Level Optimization](#54) — 0.90
55. [Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization](#55) — 0.90
56. [optimize_anything: A Universal API for Optimizing any Text Parameter](#56) — 0.90
57. [SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution](#57) — 0.90
58. [A3D: Agentic AI flow for autonomous Accelerator Design](#58) — 0.90
59. [PerfCodeBench: Benchmarking LLMs for System-Level High-Performance Code Optimization](#59) — 0.90
60. [HLS-Seek: QoR-Aware Code Generation for High-Level Synthesis via Proxy Comparative Reward Reinforcement Learning](#60) — 0.90
61. [Kernel Foundry: A Diagnosis-driven Evolutionary Kernel Optimizer with Multi-Experts](#61) — 0.90
62. [Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs](#62) — 0.90
63. [MappingEvolve: LLM-Driven Code Evolution for Technology Mapping](#63) — 0.90
64. [LLM-Guided Strategy Synthesis for Scalable Equality Saturation](#64) — 0.90
65. [Portable models as a replacement for industrial heuristics in compiler optimizations](#65) — 0.88
66. [QuTuner: Feature- and Learning-Guided Optimization Pass Tuning for Quantum Compilers](#66) — 0.88
67. [SkelDPO: A Skeleton-Guided Direct Preference Optimization Framework for Efficient Code Generation](#67) — 0.88
68. [Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search](#68) — 0.88
69. [SeaEvo: Advancing Algorithm Discovery with Strategy Space Evolution](#69) — 0.88
70. [When to Use Which? Benchmarking Optimisers for Configurable Systems under Varying Budgets](#70) — 0.85
71. [What Do AI Agents Actually Change? An Empirical Taxonomy of Mutation Patterns in Performance-Improving Pull Requests](#71) — 0.85
72. [A Multi-Dimensional, Per-Pass Empirical Study of the LLVM Optimization Pipeline](#72) — 0.85
73. [SOLAR: AI-Powered Speed-of-Light Performance Analysis](#73) — 0.85
74. [Source-Free Detection and Impact Analysis of Compiler Optimization Problems in Mobile Applications](#74) — 0.85
75. [CodeGolf Bench: A Multi-Language Benchmark for Evaluating Concise Code Generation Capabilities of Large Language Models](#75) — 0.85
76. [Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization](#76) — 0.84

---

<a id="1"></a>
## 1. [daVinci-kernel: Co-Evolving Skill Selection, Summarization, and Utilization via RL for GPU Kernel Optimization](http://arxiv.org/abs/2606.16497v2)

- **相关度**：0.98
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化、Kernel/自动调优
- **收录日期**：2026-06-15
- **arXiv ID**：2606.16497
- **作者**：Dayuan Fu, Mohan Jiang, Tongyu Wang, Dian Yang, Jiarui Hu, Liming Liu, Jinlong Hou, Pengfei Liu
- **入选理由**：使用RL和共享LLM骨干进行GPU内核优化，含技能库、执行验证和speedup报告，与SemOpt高度一致

**TL;DR**：提出一个强化学习框架daVinci-kernel，通过技能发现和利用动态演化技能库，联合训练三个共享LLM骨干的智能体，在KernelBench上显著优于现有方法。

**中文摘要**：GPU内核优化代表了一种范式，其中功能正确性被假定，执行效率是目标。我们提出了daVinci-kernel，这是一个强化学习框架，通过动态演化的技能库将技能发现与技能利用相结合。daVinci-kernel联合训练三个共享一个LLM骨干的智能体：一个技能选择智能体，通过BM25和LLM重排序检索相关技术；一个策略智能体，根据所选技能生成多轮CUDA/Triton内核；以及一个技能总结智能体，将成功的轨迹提炼为可重复使用的技能。候选技能仅在执行验证证实可重复加速后才被添加。所有三个智能体共享单个LLM骨干，通过在多样性过滤数据上进行结构化SFT冷启动初始化，然后使用多轮REINFORCE和每个智能体的优势估计进行端到端联合优化。在KernelBench上，daVinci-kernel-14B在Fast_1阈值下，Level 1、Level 2和Level 3上分别达到37.2%、70.6%和32.2%，优于之前最强的RL训练模型Dr. Kernel-14B。

**方法**：构建由技能选择、策略生成和技能总结三个智能体组成的框架，共享一个LLM骨干。技能选择使用BM25和LLM重排序检索相关技术；策略生成条件于技能产生多轮内核；技能总结从成功轨迹中提取新技能。所有智能体通过SFT冷启动后，采用多轮REINFORCE和优势估计联合训练，技能需经执行验证后才加入库。

**结果**：在KernelBench上，daVinci-kernel-14B在Fast_1阈值下，Level 1、Level 2和Level 3分别达到37.2%、70.6%和32.2%，全面超越之前最强的RL模型Dr. Kernel-14B。

[返回索引](#快速索引)

---

<a id="2"></a>
## 2. [Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games](http://arxiv.org/abs/2606.10389v1)

- **相关度**：0.98
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-06-09
- **arXiv ID**：2606.10389
- **作者**：Haoran Li, Zengle Ge, Ziyang Zhang, Xiaomin Yuan, Yui Lo, Qianhui Liu, Bocheng An, Dongke Rong, Jiaqun Liu, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen
- **入选理由**：LLM驱动策略代码进化提升对抗游戏胜率，包含评估器协同进化，直接属于自动代码性能优化

**TL;DR**：提出FAMOU框架，通过评估器协同进化、分层深度评估和弱点压力三种机制，解决对抗多智能体游戏中因评估环境变化导致的进化停滞问题，在MCTF任务上取得最优性能，并生成全新战术结构。

**中文摘要**：近年来，基于大语言模型的代码进化技术通过迭代生成和改进程序，实现了自动化发现。然而，将这些方法应用于对抗性多智能体游戏时面临一个根本性挑战：随着策略的提升，评估环境也在变化，导致固定的评估器变得不可靠，进化陷入停滞。我们提出了三种机制来解决这一挑战：评估器协同进化，将发现的最优策略纳入对手池；分层深度评估，用统计可靠的评估替代噪声大的少量游戏得分；以及弱点压力，动态增加最困难对手的权重以突破平台期。我们在FAMOU框架中实现了这些机制，该框架建立在与OpenEvolve和ShinkaEvolve相同的基础模型代码进化范式之上。在MCTF 2026 3v3海上夺旗任务中，FAMOU在两种骨干大语言模型下均持续优于基线，取得了最高综合得分（0.526）和最佳泛化能力（对未见对手胜率61.7%），而消融实验证实了每种机制对性能的贡献。值得注意的是，大语言模型变异过程生成了种子策略中完全不存在的战术结构——包括前向搜索和自适应拦截——证明了代码级进化能在对抗环境中产生非平凡的算法创新。FAMOU进化出的策略还在AAMAS 2026 MCTF竞赛中获得了硬件循环赛第一名和模拟赛第三名，验证了其在现实世界中的可迁移性。通过我们的进化过程优化的实现和相应的评估代码可在以下网址获取：https://github.com/1xiangliu1/FAMOU-CoEvo

**方法**：提出三种机制：评估器协同进化（将最优策略加入对手池）、分层深度评估（统计可靠评估替代噪声得分）、弱点压力（动态增加困难对手权重），并在FAMOU框架中实现。

**结果**：在MCTF 2026任务中，FAMOU取得最高综合分0.526和61.7%的胜率，超越基线；消融实验证明各机制有效；生成前向搜索等新策略，并在实际竞赛中获得第一名/第三名。

[返回索引](#快速索引)

---

<a id="3"></a>
## 3. [PassNet: Scaling Large Language Models for Graph Compiler Pass Generation](http://arxiv.org/abs/2605.29357v1)

- **相关度**：0.98
- **方向标签**：LLM/Agent 代码优化、编译器优化、Benchmark/评测
- **收录日期**：2026-05-28
- **arXiv ID**：2605.29357
- **作者**：Yiqun Liu, Yingsheng Wu, Ruqi Yang, Enrong Zheng, Honglei Qiu, Sijun He, Tai Liang, Jingjing Wu, Yuhan Zhou, Yiwei Zhang, Dongyan Chen, Weihan Yi, Xinqi Li, Siqi Bao
- **入选理由**：使用LLM生成编译器pass优化程序性能，包含数据集、基准测试和性能验证，与SemOpt高度一致。

**TL;DR**：PassNet是一个基于LLM的编译器通证生成生态系统，通过数据集和基准测试展示了LLM在编译器优化中的潜力，并验证了微调小模型可接近前沿性能。

**中文摘要**：现代张量编译器（如TorchInductor）在主流模型上实现了显著的加速，但在长尾工作负载上面临系统性的性能瓶颈——我们的分析显示，43%的真实世界子图在默认编译下会出现端到端性能下降。虽然LLM为实现自动化优化提供了一条路径，但现有工作主要集中在独立的核生成上。我们认为，通证生成——即LLM编写可直接集成到编译器流水线中的结构化图变换——是更合适的抽象。为此，我们提出PassNet，这是首个用于基于LLM的编译器通证生成的大规模生态系统，包括：(1) PassNet-Dataset，包含来自10万个真实世界模型的超过1.8万个独特计算图；(2) PassBench，包含200个精心挑选的长尾可融合任务（共计2060个子图），在错误感知加速分数（ES_t）——一个统一了正确性、稳定性和性能的指标——下进行评估，并配备分层完整性防御以防止LLM的系统性滥用。实验表明，PassBench既具有高度的区分性，又真正未达到饱和：最佳前沿模型在聚合性能上落后TorchInductor 37%，但在单个子图上，LLM可实现对同一编译器的高达3倍加速——这表明瓶颈在于一致性，而非能力。在仅约4000个PassNet轨迹上微调一个小模型即可获得2.67倍的改进，接近前沿模型性能，证明了巨大的提升空间，并验证了PassNet作为推进LLM驱动编译器优化的实时训练基础设施的有效性。所有数据、基准和工具均已公开。

**方法**：提出PassNet，包含大规模计算图数据集PassNet-Dataset和基准测试PassBench，采用错误感知加速分数ES_t作为评估指标，并设计了分层完整性防御。

**结果**：最佳LLM在PassBench上聚合性能落后TorchInductor 37%，但单个子图上可高达3倍加速；微调小模型在约4000个轨迹上获得2.67倍改进，接近前沿模型。

[返回索引](#快速索引)

---

<a id="4"></a>
## 4. [Optimas: An Intelligent Analytics-Informed Generative AI Framework for Performance Optimization](http://arxiv.org/abs/2604.23892v1)

- **相关度**：0.98
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-04-26
- **arXiv ID**：2604.23892
- **作者**：Mohammad Zaeed, Tanzima Z. Islam, Vladimir Indic
- **入选理由**：Optimas利用LLM自动进行代码转换以优化性能，并在实验中验证了加速效果。

**TL;DR**：Optimas是一个基于多智能体工作流的全自动代码优化框架，利用LLM将性能诊断映射到代码转换，在实验中生成100%正确代码，98.82%实验提升性能，平均加速8%-79%。

**中文摘要**：大型语言模型（LLM）在自动化代码优化方面显示出潜力。然而，在没有性能上下文的情况下，它们难以产生正确且有效的代码转换。现有的性能工具可以识别瓶颈，但止步于生成可操作的代码更改。因此，性能优化仍然是耗时且需要手动进行的工作，通常只有具备详细架构理解的专业人员才能承担。为了弥合这一差距，我们引入了Optimas，这是一个基于多智能体工作流的模块化、全自动、端到端的生成式AI框架。Optimas利用LLM将来自多个报告的性能诊断映射到已建立的、有文献支持的代码转换，同时将洞察提取、代码生成、执行和验证统一到单个流水线中。在10个基准测试和两个HPC小型应用上的3,410次真实世界实验中，Optimas生成了100%正确的代码，并在超过98.82%的实验中提升了性能，在NVIDIA GPU上实现了平均8.02%-79.09%的加速。

**方法**：提出Optimas框架，采用多智能体工作流，利用LLM将多个性能报告中的诊断映射到有文献支持的代码转换，并统一洞察提取、代码生成、执行和验证。

**结果**：在3410次实验（10个基准和2个HPC应用）中，生成100%正确代码，98.82%实验性能提升，NVIDIA GPU上平均加速8.02%-79.09%。

[返回索引](#快速索引)

---

<a id="5"></a>
## 5. [Beyond the Need for Speed: Energy-Aware Code Generation via Simulation-Guided Reinforcement Learning](http://arxiv.org/abs/2607.04577v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-07-06
- **arXiv ID**：2607.04577
- **作者**：Saurabhsingh Rajput, Tushar Sharma
- **入选理由**：使用仿真反馈强化学习生成节能C++代码，直接优化性能（能耗），与SemOpt高度一致。

**TL;DR**：提出用确定性仿真代替硬件测量来训练节能代码模型，构建Green Tea数据集，通过监督微调和强化学习训练能量感知模型，并引入CARET指标评估，在保留问题上取得显著能效提升，同时揭示IPC作为能效代理的不可靠性。

**中文摘要**：代码模型严格优先考虑功能正确性，将软件能效视为未优化的副产品。训练模型生成节能代码需要可扩展的可重复反馈，而由于硬件测量的方差，物理硬件测量无法可靠提供。在本文中，我们用确定性架构模拟框架替代硬件性能分析，构建了Green Tea，一个包含来自1,474个C++问题的350万次评估的数据集。我们通过在能量对比对上进行监督微调，然后使用仿真在环反馈进行闭环强化学习（GRPO），训练了一个能量感知的代码模型。为了严格评估部署准备程度，我们引入了正确性调整后的能量总减少量（CARET），该指标明确惩罚牺牲功能以换取效率的代码。在143个保留问题上，我们的仿真在环流程实现了12.63%的CARET，几乎将单独微调的增益提高了三倍，并且在其有效输出中成功击败了人类专家参考的能效，占58.4%。此外，我们的分析揭示了IPC陷阱：像每周期指令数（IPC）这样的标准吞吐量代理在67.8%的问题上主动错误排序真实能效，证明了直接能量模拟的绝对必要性。通过发布我们的数据集和基础设施，我们绕过了重现所需的263,000 CPU小时，从根本上赋能社区部署固有节能的代码生成模型。

**方法**：使用确定性架构模拟构建Green Tea数据集（350万评估），通过能量对比对监督微调，再结合GRPO强化学习（仿真在环反馈）训练能量感知模型，并引入CARET指标惩罚牺牲功能换取效率的行为。

**结果**：在143个保留问题上取得12.63% CARET，比单独微调提升近三倍，58.4%有效输出超越人类专家能效；分析发现IPC在67.8%问题上错误排序能效。

[返回索引](#快速索引)

---

<a id="6"></a>
## 6. [Understanding Agent-Based Patching of Compiler Missed Optimizations](http://arxiv.org/abs/2607.02370v2)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、编译器优化、优化策略检索
- **收录日期**：2026-07-02
- **arXiv ID**：2607.02370
- **作者**：Batu Guan, Zirui Wang, Shaohua Li
- **入选理由**：研究LLM代理修补编译器错过优化，使用历史知识增强技术，与SemOpt的优化策略检索高度对齐。

**TL;DR**：本文系统研究了代理修补编译器错过优化的能力，发现代理生成的补丁在优化范围上与开发者补丁存在差异，并提出了历史知识增强技术以改善泛化。

**中文摘要**：编译器错过的优化是指编译器未能优化某些代码的情况。实现或修补这些错过的优化需要许多编译器开发人员的努力。在本文中，我们系统性地研究了代理(agent)修补编译器错过的优化的能力。我们识别了一个重大挑战：修补错过的优化不仅仅需要修复报告的具体案例，还需要泛化到类似案例。我们构建了一个真实世界LLVM错过优化问题的基准，并从优化范围的角度比较了代理生成的补丁与开发人员生成的补丁。我们的结果表明，编码代理经常优化给定的示例，但许多生成的补丁要么只覆盖了开发人员预期范围的一部分，要么与之部分重叠；在某些情况下，它们甚至进一步泛化到参考补丁之外。我们进一步引入了历史知识增强技术，通过检索和蒸馏利用先前的LLVM优化拉取请求，表明这些技术改善了与开发人员对齐的泛化，并在应用于真实世界IR时产生了实际效益。

**方法**：构建了真实世界LLVM错过优化问题的基准，比较代理与开发者补丁的优化范围，并引入基于检索和蒸馏的历史知识增强技术。

**结果**：代理常优化给定示例，但补丁多只部分覆盖开发者意图范围，甚至过度泛化；历史知识增强技术提升了与开发者对齐的泛化能力。

[返回索引](#快速索引)

---

<a id="7"></a>
## 7. [EGG: An Expert-Guided Agent Framework for Kernel Generation](http://arxiv.org/abs/2606.26758v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优
- **收录日期**：2026-06-25
- **arXiv ID**：2606.26758
- **作者**：Yaochen Han, Ke Fan, Hongxu Jiang, Wanqi Xu, Weiyu Xie, Runhua Zhang, Chenhui Zhu, Yixiang Zhang
- **入选理由**：专家引导LLM代理自动生成高性能GPU内核，两阶段分解，在KernelBench上大幅加速，与SemOpt高度同题

**TL;DR**：EGG是一个专家引导的代理框架，通过两阶段分解和阶段感知多代理协作，自动化生成高性能GPU内核，在KernelBench上实现2.13倍加速。

**中文摘要**：高性能GPU内核对于降低大型语言模型（LLMs）指数级增长的计算成本至关重要，但其开发严重依赖领域专家的手动调优。虽然近期基于LLM的方法在自动化内核生成方面展现出潜力，但仍难以同时实现正确性和高性能。这一限制主要源于缺乏领域特定的优化指导，阻碍了优化空间的有效探索。我们提出EGG，一个专家引导的代理框架用于内核生成，该框架融入专家优化原则来指导LLM的决策。受专家工作流程启发，我们将内核生成分解为两个层次阶段：1）算法结构设计，建立高质量的计算结构基础；2）硬件特定调优，通过并行映射、张量分块和内存优化进行针对性调整。这种分阶段分解定义了明确的优化目标，结构化设计空间以实现逐步细化。为此，设计了一种阶段感知的多代理协作机制，用于阶段间和阶段内的上下文管理，确保稳定的优化轨迹。在KernelBench和实际工作负载上的实验表明，EGG相比PyTorch实现了2.13倍的平均加速，优于现有的基于代理和基于RL的方法。

**方法**：EGG将内核生成分解为算法结构设计和硬件特定调优两个层次阶段，并设计阶段感知的多代理协作机制。

**结果**：在KernelBench和真实工作负载上，EGG相比PyTorch平均加速2.13倍，优于现有基于代理和基于RL的方法。

[返回索引](#快速索引)

---

<a id="8"></a>
## 8. [AUTOGATE: Automated Clock Gating via Toggling-Aware LLM-based RTL Rewriting](http://arxiv.org/abs/2606.17461v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-06-16
- **arXiv ID**：2606.17461
- **作者**：Yiting Wang, Chenhui Deng, Chia-Tung Ho, Yanqing Zhang, Zhuo Feng, Cunxi Yu, Ang Li, Gang Qu, Brucek Khailany
- **入选理由**：基于LLM agent的RTL时钟门控优化，减少动态功耗，有ML-LLM协同和真实性能验证。

**TL;DR**：提出AUTOGATE，首个基于ML-LLM协同的智能体框架，通过层次化多智能体架构和聚类算法实现工业级RTL时钟门控优化，显著降低动态功耗。

**中文摘要**：细粒度时钟门控（FGCG）是降低动态功耗最有效的技术之一，然而当前的FGCG优化流程仍然很大程度上依赖手动操作。近期基于LLM的RTL优化方法仍然存在两个主要缺点：(1)无法处理跨越数百万个周期的长波形轨迹，(2)难以在保持正确性的同时将优化扩展到大型层次化代码库。在这项工作中，我们提出了AUTOGATE，首个面向工业级RTL功耗优化的智能体框架，能够在大型层次化代码库中实现工作负载感知的时钟门控优化。AUTOGATE引入了一种机器学习（ML）-LLM协同设计，桥接了波形级分析和RTL重写。具体来说，我们设计了一种基于ML的聚类算法，将原始翻转轨迹提炼为紧凑、结构化的表示，指导基于LLM的RTL重写。这使得能够准确识别和应用时钟门控机会，而无需LLM直接处理原始波形数据。为增强可扩展性，AUTOGATE采用层次化多智能体架构，将大型设计分解为可独立优化的模块，从而在深层设计层次中实现协调优化。我们在从小型RTL设计到大型工业级代码库的多样化设计上评估了AUTOGATE。实验结果表明，AUTOGATE相对于基线持续降低动态功耗。在小型设计套件上，AUTOGATE平均降低动态功耗49.31%。在工业级设计上，AUTOGATE在NVDLA和BlackParrot上分别实现了19.34%和7.96%的动态功耗降低，在高度优化的专有生产设计上最高降低6.86%。

**方法**：ML-LLM协同设计：ML聚类算法将原始波形轨迹提炼为紧凑结构化表示引导LLM重写；层次化多智能体架构将大型设计分解为独立优化模块。

**结果**：小型设计平均动态功耗降低49.31%；工业级设计NVDLA降低19.34%，BlackParrot降低7.96%，专有生产设计最高降低6.86%。

[返回索引](#快速索引)

---

<a id="9"></a>
## 9. [AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?](http://arxiv.org/abs/2606.05080v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-06-03
- **arXiv ID**：2606.05080
- **作者**：Zhangchen Xu, Junda Chen, Yue Huang, Dongfu Jiang, Jiefeng Chen, Hang Hua, Zijian Wu, Zheyuan Liu, Zexue He, Lichi Li, Shizhe Diao, Jiaxin Pei, Jinsung Yoon, Hao Zhang, Mengdi Wang, Radha Poovendran, Misha Sra, Alex Pentland, Zichen Chen
- **入选理由**：AutoLab是一个面向超长时域闭环优化的基准，包含系统优化和CUDA kernel优化，要求LLM/agent通过反复基准测试和编辑来实现性能提升，与SemOpt高度一致。

**TL;DR**：提出了AutoLab基准，用于评估超长时域闭环优化，发现持续迭代能力比初始尝试质量更关键。

**中文摘要**：科学和工程进步本质上是一个长期迭代过程：提出变化、进行实验、测量结果，并不断改进产物。然而，现有的前沿模型基准主要评估单轮响应或短时间跨度的智能体轨迹，未能捕捉到在长时间范围内持续迭代改进的挑战。为了弥补这一空白，我们引入了AutoLab，这是一个用于超长时域闭环优化的新基准。AutoLab包含36个由专家策划的现实任务，涵盖四个不同领域：系统优化、谜题与挑战、模型开发和CUDA内核优化。每个任务从一个正确但故意次优的基线开始，挑战智能体在严格的墙钟时间预算内改进它。对17个最先进模型的评估显示，成功的主要预测因素不是智能体初始尝试的质量，而是它持续地进行基准测试、编辑和整合经验反馈的毅力。虽然claude-opus-4.6展示了强大的长时域优化能力，但大多数前沿模型，包括几个专有模型，要么过早终止，要么在预算耗尽时进展甚微。这些结果强调了自主智能体中时间意识和持续迭代的重要性。我们开源了完整的基准、评估工具和任务工件，以加速对真正有能力的长期智能体的研究。

**方法**：构建了包含36个专家策划任务的AutoLab基准，覆盖四个领域，并在严格时间预算下评估17个前沿模型。

**结果**：claude-opus-4.6表现最佳，多数模型过早终止或进展甚微。

[返回索引](#快速索引)

---

<a id="10"></a>
## 10. [Learning When to Optimize: Verified Optimization Skills from Expert GPU-Kernel Lineages](http://arxiv.org/abs/2605.28213v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优、优化策略检索
- **收录日期**：2026-05-27
- **arXiv ID**：2605.28213
- **作者**：Shuoming Zhang, Qiuchu Yu, Yangyu Zhang, Ruiyuan Xu, Xiyu Shi, Guangli Li, Xiaobing Feng, Huimin Cui, Jiacheng Zhao
- **入选理由**：从专家GPU内核反向推导优化技能，指导LLM生成高质量内核，验证正确性与性能，与SemOpt方法高度一致。

**TL;DR**：KLineage通过从专家内核反向推导优化技能，教会LLM何时应用优化，从而提升GPU内核生成质量和效率。

**中文摘要**：基于LLM的智能体越来越多地用于生成GPU内核，但它们通常知道尝试哪些优化，却不知道这些优化何时是合理的。我们引入了KLineage，它从专家内核中学习这种缺失的“何时”知识：KLineage不是依赖前向展开，而是通过验证门控的简化反向遍历专家实现，并将每个被接受的步骤逆转成一个可重用的优化技能。每个技能不仅记录了优化意图，还记录了它在代码中的应用位置、使其有效的条件、产生的影响以及其假设避免了哪些失败。下游的LLM在相同的编译/正确性/性能分析门控下将这些技能具体化到新的代码表面上。在两个NVIDIA架构上的五个专家工作负载中，这些从谱系中衍生出的技能作为有效的优化课程，在相同的固定预算下，在最终内核质量和优化效率方面均超过了最近基于记忆的LLM内核基线。我们还使用一个单独的22实例保留检查作为对源案例记忆化的健全性测试。

**方法**：通过验证门控的简化反向遍历专家实现，将每个被接受的步骤逆转成可重用的优化技能，记录意图、位置、条件、效果和避免的失败。

**结果**：在两个NVIDIA架构的五个专家工作负载上，KLineage在相同预算下，最终内核质量和优化效率超越基于记忆的LLM内核基线。

[返回索引](#快速索引)

---

<a id="11"></a>
## 11. [SIA: Self Improving AI with Harness & Weight Updates](http://arxiv.org/abs/2605.27276v2)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优
- **收录日期**：2026-05-26
- **arXiv ID**：2605.27276
- **作者**：Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran
- **入选理由**：提出SIA自我改进循环，通过LLM代理同时更新框架和权重来优化GPU kernel，实现12.4%速度提升，直接涉及自动代码/ kernel优化并验证真实性能。

**TL;DR**：提出SIA，一种同时更新任务智能体框架和权重的自我改进循环，在三个领域显著超越先前最优方法。

**中文摘要**：人类是构建和改进AI的瓶颈。模型及其包装的智能体都是由人编写、调整和纠正的。AI能够自行改进的长期目标仍未实现。两个大致独立的研究方向试图突破这一瓶颈。框架更新学派让元智能体重写任务特定智能体的脚手架（其工具、提示、重试逻辑和搜索过程），而模型权重保持不变。测试时训练学派则使用手工编写的强化学习流水线，基于任务反馈更新模型自身的权重，而框架保持不变。这两个领域各自孤立运作。我们提出SIA，一个自我改进循环，其中语言模型智能体（反馈智能体）同时更新任务特定智能体的框架和权重。我们在三个对比鲜明的领域进行评估：中文法律罪名分类、底层GPU内核优化和单细胞RNA去噪。结合两种杠杆在所有三个基准上都优于仅迭代脚手架。SIA-W+H在LawBench上比先前SOTA高25.1%，GPU内核比先前SOTA快12.4%（1017微秒对比1161微秒），去噪效果比先前SOTA高20.4%。框架更新使模型具有智能体性，塑造其搜索和行动方式，而权重更新建立了任何提示或脚手架都无法灌输的领域直觉。

**方法**：设计一个语言模型反馈智能体（Feedback-Agent），在每次任务执行后同时调整任务特定智能体的框架（工具、提示、搜索策略等）和模型权重，形成闭环自我改进。

**结果**：在中文法律分类、GPU内核优化和单细胞RNA去噪三个任务上，结合框架和权重更新（SIA-W+H）分别比先前最优方法提升25.1%、12.4%和20.4%。

[返回索引](#快速索引)

---

<a id="12"></a>
## 12. [Metal-Sci: A Scientific Compute Benchmark for Evolutionary LLM Kernel Search on Apple Silicon](http://arxiv.org/abs/2605.09708v2)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化、Kernel/自动调优、Benchmark/评测
- **收录日期**：2026-05-10
- **arXiv ID**：2605.09708
- **作者**：Víctor Gallego
- **入选理由**：专注于Apple Silicon Metal kernel的LLM进化搜索，自动生成并优化kernel性能，有speedup验证和roofline分析，与SemOpt高度一致。

**TL;DR**：提出了Metal-Sci基准测试和自动化内核搜索框架，通过保留的评分函数实现廉价机械监督，捕获了LLM生成内核的静默回归问题。

**中文摘要**：我们提出了Metal-Sci，一个包含10个任务的科学Apple Silicon Metal计算内核基准测试，涵盖六种优化场景（模板、n体问题中的全对、多场玻尔兹曼、邻居列表分子动力学、多核偏微分方程、FFT）。每个任务配备了一个CPU参考、一个基于roofline的适应度函数和一个保留的泛化规模。我们将该基准测试与一个轻量级自动化内核搜索工具配对，该工具对每个候选进行运行时编译，针对多个规模根据roofline进行评分，并将结构化的编译和每个规模的正确性诊断反馈给一个冻结的LLM，该LLM驱动一个(1+1)进化循环。我们报告了在M1 Pro上对Claude Opus 4.7、Gemini 3.1 Pro和GPT 5.5进行的单模型扫描结果：分布内自加速比在1.00倍到10.7倍之间。除了原始加速之外，我们的核心方法论主张是结构性的：保留的评分函数Φ_T（在运行结束时对代理在搜索过程中从未见过的配置评估一次）在此自动搜索循环中作为一个廉价的机械监督原语，能够捕获例如一个返回错误样本的Opus模板<uint D> HMC win在未见维度上的错误，以及一个GPT FFT3D最佳配置在分布内以2.95倍加速胜出，但在256^3的保留立方体上性能骤降至0.23倍，这是一个仅凭分布内分数无法看到的静默回归。代码见https://github.com/vicgalle/metal-sci-kernels。

**方法**：构建10任务基准测试，每个任务包含CPU参考、roofline适应度函数和保留规模；设计轻量级工具，使用冻结LLM驱动的(1+1)进化循环搜索内核，并通过保留评分函数Φ_T在搜索结束时进行一次性验证。

**结果**：在M1 Pro上对三个LLM进行单模型扫描，分布内加速比达1.00x-10.7x；保留评分函数有效捕获了Opus和GPT的回归案例。

[返回索引](#快速索引)

---

<a id="13"></a>
## 13. [CodeEvolve: LLM-Driven Evolutionary Optimization with Runtime-Enriched Target Selection for Multi-Language Code Enhancement](http://arxiv.org/abs/2605.04677v1)

- **相关度**：0.96
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-05-06
- **arXiv ID**：2605.04677
- **作者**：Ajay Krishna Borra, Wenzhuo Yang, Samarth Arora, Akhilesh Deepak Gotmare, Gokulakrishnan Gopalakrishnan, Tharun Gali, Madhav Rathi, Doyen Sahoo, Manpreet Singh, Mayuresh Verma, Laksh Venka, Shuchita Singh
- **入选理由**：直接使用LLM和进化搜索自动进行程序性能优化，通过运行时分析和MCTS生成并筛选候选，在Java和Apex上实现加速并保持正确性。

**TL;DR**：CodeEvolve是一个利用LLM和进化搜索自动提升程序性能的框架，通过运行时分析和MCTS生成并筛选优化候选，在Java和Apex任务上实现了显著加速，并保持了正确性。

**中文摘要**：我们提出了CodeEvolve，一个利用大型语言模型（LLM）改进程序性能和代码质量的进化框架。CodeEvolve扩展了OpenEvolve，加入了运行时引导的目标选择、蒙特卡洛树搜索（MCTS）、自动代码精炼以及针对Java和Salesforce Apex的特定语言评估流水线。该系统使用Java Flight Recorder（JFR）配置文件构建加权组件图，并选择占大多数执行成本的优化目标，减少了对人工瓶颈识别的依赖。对于每个目标，CodeEvolve生成候选编辑，通过构建验证、单元测试、性能检查、静态分析和基于LLM的评审进行评估，并只保留保持功能正确性的变体。在真实世界的优化任务中，CodeEvolve在保持正确性的同时提升了性能和代码指标。在一个大型企业Java代码库上，它在七个热点函数上实现了平均15.22倍的加速，并在其中五个函数上优于单次LLM优化。在Apex优化上的消融研究表明，完整的MCTS增强配置平均产生19.5个有效程序（满分20），表明搜索、过滤和精炼每一点都有助于更可靠的优化。

**方法**：扩展OpenEvolve，使用JFR配置文件构建加权组件图选择优化目标，通过MCTS生成候选编辑，经过构建验证、单元测试、性能检查、静态分析和LLM评审的多阶段流水线过滤，仅保留保持功能正确性的变体。

**结果**：在企业Java代码库上，七个热点函数平均加速15.22倍，其中五个优于单次LLM优化；在Apex优化消融实验中，完整MCTS配置平均产生19.5个有效程序（满分20）。

[返回索引](#快速索引)

---

<a id="14"></a>
## 14. [MOA: A Profiling-Guided LLM Framework for Memory-Optimization Automation at Codebase Scale](http://arxiv.org/abs/2606.31368v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、Profiling/程序分析、优化策略检索
- **收录日期**：2026-06-30
- **arXiv ID**：2606.31368
- **作者**：Jiaxi Liang, Yuanxiang Shi, Zezhou Yang, Chenxiong Qian
- **入选理由**：LLM驱动自动检测和修复内存低效，包含profiling分析、anti-pattern提取和补丁生成，与SemOpt高度相似。

**TL;DR**：MOA是一个LLM驱动的框架，自动检测和修复大规模代码库中的内存低效问题，在OpenHarmony上实现了显著的内存和二进制大小减少。

**中文摘要**：现代大型软件系统常常遭受普遍的内存低效问题（例如膨胀、抖动），导致过度的资源成本和性能下降。现有的优化工作流缺乏端到端的自动化，迫使开发者手动将复杂工具的输出综合为可操作且保留语义的修复方案，这阻碍了在大型代码库中的可扩展性。为了解决这个问题，本文提出了MOA，一个LLM驱动的框架，能够自动检测和修复生产规模代码库中反复出现的内存低效问题。具体来说，MOA通过三个代理运行：分析器从性能剖析数据中挖掘反模式，检查器生成器通过模板引导的细化合成静态分析器，以及修补器通过状态机驱动的工作流生成优化补丁。我们在OpenHarmony（一个拥有超过1亿行C/C++代码的开源操作系统）上的评估显示，MOA从3个剖析的服务中识别出13个反模式（其中9个是之前未知的），在更广泛的7个服务中检测到超过10,000个低效问题，并生成了769个补丁，专家接受率为92.5%，平均实现了42.2%的堆内存减少和10.6%的二进制大小减少。我们认为MOA是生产规模性能工程的一个有价值工具。

**方法**：MOA采用三个LLM驱动的代理：分析器挖掘反模式，检查器合成静态分析器，修补器生成优化补丁。

**结果**：在OpenHarmony上识别13个反模式，检测超1万个低效，生成769个补丁（92.5%接受率），平均堆减少42.2%，二进制大小减少10.6%。

[返回索引](#快速索引)

---

<a id="15"></a>
## 15. [AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning](http://arxiv.org/abs/2606.20373v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-18
- **arXiv ID**：2606.20373
- **作者**：Zepeng Li, Jie Ren, Zhanyong Tang, Jie Zheng, Zheng Wang
- **入选理由**：多智能体框架利用LLM查询编译器内部状态和运行时反馈迭代优化编译选项，实现真实加速，与LLM自动代码优化强相关。

**TL;DR**：AutoPass是一个多智能体框架，通过开放编译器内部信息给LLM并利用运行时反馈，实现了无需训练的编译器性能自动调优，在x86-64和ARM64上分别取得1.043x和1.117x的加速。

**中文摘要**：大型语言模型（LLM）在代码编译任务中展现出潜力，但由于复杂的微架构效应和嘈杂的运行时测量，将其应用于运行时性能调优十分困难。我们提出了AutoPass，一个用于编译器性能调优的多智能体框架，它利用编译器和运行时证据来指导LLM生成的优化决策。与先前的自动调优方案将编译器视为黑盒不同，AutoPass向LLM开放编译器，使其能够查询编译器内部的优化状态并分析中间表示，以编排编译器选项。搜索过程使用测量的运行时反馈迭代优化配置，以诊断性能回退并指导延迟改进的修改。AutoPass在仅推理、无需训练的设置下运行，不需要离线训练或任务特定的微调，使其能够直接应用于新的基准测试和平台。我们在LLVM编译器上实现了AutoPass，并在服务器级x86-64和嵌入式ARM64系统上进行了评估。AutoPass优于专家调整的启发式方法和经典自动调优方法，在x86-64和ARM64上相较于LLVM -O3分别实现了1.043倍和1.117倍的几何平均加速。

**方法**：提出AutoPass多智能体框架，允许LLM查询编译器内部优化状态和中间表示，基于运行时反馈迭代优化编译选项。

**结果**：在LLVM编译器上，AutoPass在x86-64和ARM64上相对于-O3分别实现1.043x和1.117x的几何平均加速，优于专家启发式和经典自动调优。

[返回索引](#快速索引)

---

<a id="16"></a>
## 16. [AI-PROPELLER: Warehouse-Scale Interprocedural Code Layout Optimization with AlphaEvolve](http://arxiv.org/abs/2606.00131v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化、编译器优化
- **收录日期**：2026-05-28
- **arXiv ID**：2606.00131
- **作者**：Chaitanya Mamatha Ananda, Rajiv Gupta, Mircea Trofin, Aiden Grossman, Sriraman Tallam, Xinliang David Li, Amir Yazdanbakhsh
- **入选理由**：使用Magellan代理工作流进化Propeller编译器启发式，实现过程间代码布局优化，在实际硬件上测量性能获得显著提升，属于LLM/agent自动进行程序性能优化并有真实反馈。

**TL;DR**：AI-PROPELLER通过代理工作流将Propeller扩展为细粒度过程间代码布局优化器，在实际硬件上测量性能，实现显著性能提升。

**中文摘要**：后链接优化器（PLO），如Propeller和BOLT，已经证明精确的、基于profile的代码布局可以从高度优化的二进制文件中提取显著的性能提升。然而，这些系统目前仅限于过程内技术，留下了过程间布局的全局潜力尚未被充分挖掘。由于组合爆炸的搜索空间和复杂的调用返回语义难以建模，过程间代码布局历来困难。因此，细粒度过程间布局的性能潜力在实践中尚未得到证明。AI-PROPELLER使用Magellan，一个代理工作流，它将Propeller中的编译器启发式演变为细粒度的过程间优化器，并微调生成的策略超参数。为了确保高保真度，我们放弃了近似的静态成本模型，代理工作流生成多个布局变体，并在实际硬件上执行以测量真实性能计数器，为进化循环提供精确的奖励信号。AI-PROPELLER在多个基准测试上进行了评估，包括大型仓库规模应用，实验显示在已经使用最先进的FDO和PLO优化的情况下，性能提升为0.23%到1.6%，这对于实际二进制文件是显著的。这是首次在工业环境中对大型仓库规模应用进行细粒度过程间代码布局优化。

**方法**：使用Magellan代理工作流，将编译器启发式演变为细粒度过程间优化器，并通过在实际硬件上执行布局变体测量性能计数器来提供精确奖励信号，进行进化调优。

**结果**：在多个基准测试（包括大型仓库规模应用）上，相比最先进的FDO和PLO，实现0.23%到1.6%的性能提升。

[返回索引](#快速索引)

---

<a id="17"></a>
## 17. [AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents](http://arxiv.org/abs/2605.16819v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、Benchmark/评测、Kernel/自动调优
- **收录日期**：2026-05-16
- **arXiv ID**：2605.16819
- **作者**：Sharareh Younesian, Wenwen Ouyang, Sina Rafati, Mehdi Rezagholizadeh, Sharon Zhou, Ji Liu, Yue Liu, Yuchen Yang, Hao Li, Ziqiong Liu, Dong Li, Vikram Appia, Zhenyu Gu, Emad Barsoum
- **入选理由**：提出AgentKernelArena，专门评估AI代理自动优化GPU内核性能的基准，与SemOpt的自动代码优化目标高度一致。

**TL;DR**：提出了AgentKernelArena，一个用于评估AI代理在GPU内核优化上的开源基准，包含196个任务，发现最强代理在PyTorch到HIP任务上平均加速6.89倍，但泛化测试显示PyTorch到HIP正确率显著下降。

**中文摘要**：GPU内核优化对于高效深度学习系统越来越关键，但编写高性能内核仍然需要大量的低级专业知识。最近的AI编码代理可以迭代读取代码、调用编译器和性能分析器并改进实现，然而现有的内核基准测试评估的是单个LLM调用而非完整的代理工作流，并且没有一个同时包含内核到内核优化和未见配置泛化测试。我们提出了AgentKernelArena，一个用于衡量AI编码代理在GPU内核优化上的开源基准测试。该基准测试包含196个任务，涵盖HIP到HIP优化、Triton到Triton优化以及PyTorch到HIP翻译，并在隔离工作区中使用门控编译、正确性和性能检查来评估完整的代理工作流，集中评分以及一个未见配置泛化协议，测试优化是否转移到代理从未观察到的输入配置。在包括Cursor Agent、Claude Code和Codex Agent在内的生产代理中，我们发现大多数任务类别具有近乎完美的编译和高正确率，最强配置在PyTorch到HIP任务上平均加速达6.89倍，HIP到HIP任务上6.69倍，Triton到Triton任务上2.13倍。我们的未见配置评估显示，HIP到HIP和Triton到Triton优化很大程度上转移到未见输入形状，而PyTorch到HIP表现出显著的正确率下降，表明从头生成内核的代理经常硬编码形状相关的假设。AgentKernelArena被设计为一个模块化、可扩展的框架，用于跨代理、任务和硬件目标进行严格的代理型GPU内核优化评估。

**方法**：构建包含196个任务的基准测试，涵盖HIP-to-HIP、Triton-to-Triton优化和PyTorch-to-HIP翻译，采用门控编译、正确性和性能检查，以及未见配置泛化协议。

**结果**：最强配置在PyTorch-to-HIP上平均加速6.89x，HIP-to-HIP上6.69x，Triton-to-Triton上2.13x；泛化测试中HIP-to-HIP和Triton-to-Triton转移良好，但PyTorch-to-HIP正确率大幅下降。

[返回索引](#快速索引)

---

<a id="18"></a>
## 18. [SkillEvolver: Skill Learning as a Meta-Skill](http://arxiv.org/abs/2605.10500v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-05-11
- **arXiv ID**：2605.10500
- **作者**：Genrui Zhang, Erle Zhu, Jinfeng Zhou, Caiyan Jia, Hongning Wang
- **入选理由**：SkillEvolver在GPU kernel优化任务上通过元技能迭代优化代码，显著提升speedup，符合LLM/agent自动代码优化并有速度验证。

**TL;DR**：SkillEvolver通过元技能迭代优化技能代码和描述，无需重新训练，在多样任务上显著超越静态技能和基线。

**中文摘要**：智能体技能如今是静态的人工制品：一次创建——通过人工策展或从参数化知识的一次性生成——然后保持不变地使用，没有从实际使用中改进的机制。我们提出了SkillEvolver，一种轻量级、即插即用的在线技能学习解决方案，其中单个元技能迭代地创作、部署和改进领域特定技能。SkillEvolver的学习目标是技能的描述和代码，而不是模型权重，因此生成的人工制品可以无需重新训练就放入任何智能体；而且元技能本身只是另一个技能，通过相同的接口被任何符合协议的CLI智能体加载。与轨迹蒸馏不同，元技能仅在部署所学技能之后进行改进，因此学习信号来自另一个智能体使用该技能时遇到的失败，而不仅仅是探索性轨迹。改进迭代由一个新鲜智能体过拟合审计控制，该审计捕获可能的泄漏以及部署技能特定的失败，包括静默绕过模式——其中技能在内容上看似有效，但在运行时从未被调用。在涵盖15+领域的83个SkillsBench任务上，SkillEvolver达到了56.8%的准确率，而人工策展技能为43.6%，无技能基线为29.9%；在来自KernelBench的3个GPU内核优化任务上，它还将平均加速比从1.16提高到1.51。

**方法**：提出SkillEvolver，使用单一元技能迭代地创作、部署和精炼领域技能，学习目标是技能代码和文本，通过失败信号进行在线优化，并采用新鲜智能体过拟合审计防止泄漏和静默绕过。

**结果**：在83个SkillsBench任务上准确率56.8%，高于人工技能43.6%和无技能29.9%；在3个GPU内核优化任务上平均加速从1.16提升至1.51。

[返回索引](#快速索引)

---

<a id="19"></a>
## 19. [ARIADNE: Agentic Reward-Informed Adaptive Decision Exploration via Blackboard-Driven MCTS for Competitive Program Generation](http://arxiv.org/abs/2605.02431v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-05-04
- **arXiv ID**：2605.02431
- **作者**：Minnan Wei, Xiang Chen, Xiaoshuai Niu, Siyu Chen
- **入选理由**：结合MCTS搜索与执行反馈自动生成竞赛程序，满足性能约束并验证正确性与速度。

**TL;DR**：提出黑板驱动的MCTS框架，通过顺序决策和共享黑板积累证据，显著提升LLM在竞赛程序生成中的Pass@1性能。

**中文摘要**：竞赛程序生成旨在自动生成满足严格时间和内存约束的编程竞赛问题的正确且高效的解决方案。现有的基于LLM的方法往往无法进行显式的算法规划，并且不能鲁棒地处理边缘情况，导致单次生成不可靠。此外，尽管执行反馈对于迭代调试和精炼至关重要，但在有限的计算预算内有效整合此类反馈仍然困难。为了克服这些限制，我们提出了{	ool}，一个黑板驱动的蒙特卡洛树搜索（MCTS）框架，将程序生成建模为顺序决策过程。{	ool}将生成工作流组织为五个协调阶段（即策略选择、代码生成、测试生成、质量评估和代码修复），同时维护一个共享黑板，累积结构化证据以指导后续决策。在四个基准测试（APPS、CodeContests、CodeContests+和LiveCodeBench）上的实验表明，{	ool}在多个LLM后端上一致地实现了最佳的Pass@1性能。使用GPT-4o，{	ool}获得了41.30、46.67、27.27和20.91的Pass@1分数，超过最强基线CodeSim最多26.06分，而使用DeepSeek-V3.2时观察到了进一步的改进。这些结果表明，通过MCTS进行全局搜索与在共享黑板上持续积累证据相结合，能够实现系统探索和有效反馈利用，显著增强LLM在竞赛程序生成中的能力。

**方法**：采用黑板驱动MCTS框架，将程序生成建模为顺序决策过程，包含策略选择、代码生成、测试生成、质量评估和代码修复五个阶段，并通过共享黑板累积结构化证据指导后续决策。

**结果**：在APPS、CodeContests、CodeContests+和LiveCodeBench上，使用GPT-4o取得Pass@1分别为41.30、46.67、27.27和20.91，超越基线CodeSim最多26.06分；使用DeepSeek-V3.2进一步改进。

[返回索引](#快速索引)

---

<a id="20"></a>
## 20. [Agentic Architect: An Agentic AI Framework for Architecture Design Exploration and Optimization](http://arxiv.org/abs/2604.25083v1)

- **相关度**：0.95
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-04-28
- **arXiv ID**：2604.25083
- **作者**：Alexander Blasberg, Vasilis Kypriotis, Dimitrios Skarlatos
- **入选理由**：LLM agent驱动代码演化进行微架构设计探索，通过周期精确模拟验证性能提升，直接对应自动代码优化

**TL;DR**：提出Agentic Architect，一个结合LLM代码演化和周期精确模拟的智能体AI框架，用于计算机体系结构设计探索与优化，在缓存替换、数据预取和分支预测任务上达到或超越当前最优水平。

**中文摘要**：大语言模型（LLMs）的快速进步通过实现高效探索广泛、复杂的设计空间创造了新的机遇。这在计算机体系结构中尤其有价值，因为性能取决于从庞大的组合空间中提取的微架构设计和策略。我们引入了Agentic Architect，一个用于计算机体系结构设计探索和优化的智能体AI框架，它将LLM驱动的代码演化与周期精确模拟相结合。人类架构师指定优化目标、种子设计、评分函数、模拟器接口和基准分割，而LLM在这些约束内探索实现。在缓存替换、数据预取和分支预测方面，Agentic Architect匹配或超越了最先进的设计。我们最优的演化缓存替换设计在LRU上实现了1.062x的几何平均IPC加速，比Mockingjay（1.056x）高0.6%。我们演化的分支预测器在Bimodal上实现了1.100x的几何平均IPC加速，比其哈希感知机种子（1.085x）高1.5%。最后，我们演化的预取器在无预取基础上实现了1.76x的几何平均IPC加速，比其VA/AMPM Lite种子（1.59x）高17%，比SMS（1.55x）高21%。我们的分析揭示了关于智能体AI驱动的微架构设计的若干发现。在演化的设计之间，组件通常对应于已知技术；新颖之处在于它们如何协调。架构师的角色正在转变，但人类仍然处于中心位置。种子质量限制了搜索所能达到的：演化可以改进和扩展现有机制，但不能弥补薄弱的基础。同样，目标、约束和提示指导影响可靠性和泛化能力。总体而言，Agentic Architect是首个用于智能体AI体系结构探索和优化的端到端开源框架。

**方法**：结合LLM驱动的代码演化与周期精确模拟，人类指定目标、种子设计、评分函数等，LLM在约束下自动生成和优化实现。

**结果**：缓存替换设计在LRU上实现1.062x IPC加速，分支预测在Bimodal上实现1.100x IPC加速，数据预取在无预取基础上实现1.76x IPC加速，均优于或接近当前最优方法。

[返回索引](#快速索引)

---

<a id="21"></a>
## 21. [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](http://arxiv.org/abs/2606.12563v1)

- **相关度**：0.94
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化、编译器优化、Kernel/自动调优
- **收录日期**：2026-06-10
- **arXiv ID**：2606.12563
- **作者**：Neha Prakriya, Chaojun Hou, Zheng Gong, Huasha Zhao, Xi Zhao, Mou Li, Zhenyu Gu, Emad Barsoum
- **入选理由**：多智能体树搜索自动优化LLM推理全栈，含kernel/编译配置，达193%帕累托改进

**TL;DR**：Arbor通过多智能体树搜索实现了LLM推理的全自动优化，达到193%帕累托改进且可泛化至多种硬件。

**中文摘要**：Arbor是一个多智能体框架，它将结构化树搜索作为自主智能体在大型、有状态动作空间中运行的认知层。先前的自主优化系统在孤立的目标上运行，且评估是无状态的。Arbor则维护一个显式的评分假设搜索树，作为智能体之间的共享工作记忆，随着每次测量而演化，将失败视为诊断信号，重塑后续探索，并随着先前成功改变瓶颈分布而扩展。我们在全栈LLM推理优化上验证了Arbor，这是一个历史上需要跨应用、框架、编译器、内核和硬件堆栈的工程团队协调努力才能达到峰值性能的领域。Arbor将一个编排器智能体（通过委托给推理堆栈中的领域专家来驱动优化）与一个评论家智能体（通过根因分析、内省和测量验证来维护稳定性）配对，形成一种制衡架构，其中任何一个智能体都不能单方面驱动系统。智能体能力被分解为硬技能（领域专业知识）和软技能（决定贡献如何组合的协调协议），从而实现了完全自主的多日优化活动。Arbor在吞吐量-延迟帕累托改进上相比供应商优化的基线达到了高达193%的提升，而一个没有该框架的单一智能体仅在吞吐量上提升了33%，并在几小时内不可恢复地崩溃。Arbor可以泛化到多代硬件平台，运行间方差在2个百分点以内，表明该方法与硬件无关且可重复。

**方法**：Arbor采用多智能体框架，包含编排器和评论家两个智能体，维护一个共享的假设搜索树作为工作记忆，利用硬技能和软技能分解，通过树搜索探索和利用失败信号进行优化。

**结果**：在LLM推理优化中，Arbor实现高达193%的吞吐量-延迟帕累托改进，单智能体仅提升33%并崩溃；方法硬件无关，运行间方差小于2个百分点。

[返回索引](#快速索引)

---

<a id="22"></a>
## 22. [An Ocean Model Ported by a Large Language Model: Experience and Lessons from FESOM2 (Fortran to C to C++/Kokkos)](http://arxiv.org/abs/2606.11356v1)

- **相关度**：0.94
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-09
- **arXiv ID**：2606.11356
- **作者**：Nikolay V. Koldunov, Suvarchal K. Cheedela, Sergey Danilov, Dmitry Sidorenko, Sebastian Beyer, Thomas Jung
- **入选理由**：LLM辅助将完整海洋模型从Fortran移植到C++/Kokkos，保持物理准确性并实现GPU性能提升，属于LLM自动修改源代码以优化性能

**TL;DR**：LLM成功将完整海洋模型FESOM2从Fortran移植到C和C++/Kokkos，保持物理准确性，GPU性能优于CPU。

**中文摘要**：大型语言模型（LLM）可以翻译和修改源代码，并且已被证明可以对不同复杂度的代码进行此类操作。但它们是否能够在不降低物理准确性的情况下，将一个完整的生产地球物理模型移植到不同的语言，这一点尚未得到证实。我们证明，LLM辅助的代码翻译可以在将完整生产海洋模型移植到现代性能可移植形式的同时，保持其物理特性。我们报告了使用一个由领域专家指导的代理式LLM编码助手，将FESOM2非结构化网格海洋-海冰模型（约74000行核心Fortran代码）首先移植到C，然后移植到C++/Kokkos以实现跨CPU和GPU的性能可移植性的经验。我们描述了被证明必要的实践、哪些方法有效、哪些无效，以及我们遇到的失败模式。有三个实践最为重要：分两阶段进行翻译，将重现数值计算（从Fortran到干净的C参考）与引入并行性（从C到Kokkos）分开；要求严格逐字翻译，不允许助手“改进”源代码；以及针对每个阶段使用适合该阶段的验收标准进行验证。C移植在五年长期模拟统计量水平上重现了原始Fortran。Kokkos移植在CPU上与C参考逐位相同，在GPU上多年运行统计接近。在涡旋丰富的网格上，最高740万个表面顶点，单个A100 GPU节点运行速度比CPU节点快1.6-3.7倍，达到了生产集成所需的每天1-2模拟年。结果不仅仅是单个GPU移植：通过遵循明确的验证程序，LLM在几周内将一个完整的Fortran海洋模型移植到了另一种语言和加速器上，同时保持了其物理特性。

**方法**：使用代理式LLM编码助手，分两阶段翻译：先Fortran到C（保留数值计算），再C到C++/Kokkos（引入并行）；要求严格字面翻译，每阶段用不同验收标准验证。

**结果**：C移植在五年统计量上匹配Fortran；Kokkos在CPU上逐位一致，GPU上统计接近；单个GPU比CPU快1.6-3.7倍，达到生产运行速度。

[返回索引](#快速索引)

---

<a id="23"></a>
## 23. [Are LLM-Generated GPU Kernels Production-Ready? A Trace-Driven Benchmark and Optimization Agent](https://arxiv.org/abs/2607.14541)

- **相关度**：0.93
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优、Benchmark/评测
- **收录日期**：2026-07-18, 2026-07-19, 2026-07-20
- **arXiv ID**：2607.14541
- **作者**：Lingyun Yang, Yuxiao Wang, Shenghao Liang, Linfeng Yang, Daocheng Ying, Chunbo You, Rui Zhang, Luping Wang, Yinghao Yu, Guodong Yang, Liping Zhang
- **入选理由**：提出Atrex-Bench基准和AKA代理，通过迭代测量-修订搜索优化GPU内核，直接面向LLM自动代码性能优化。

**TL;DR**：提出Atrex-Bench基准测试，从生产轨迹采样，并推出AKA代理优化内核，显著提升性能。

**中文摘要**：现有的GPU内核生成基准测试从合成或精选来源中提取问题，这些来源与部署的工作负载存在差异。我们提出了Atrex-Bench，这是一个基准测试，其30个算子和440种形状直接从全集群生产推理轨迹中采样，针对计算受限、内存丰富的GPU。每个问题都带有一个重要性权重，该权重源自其在观察到的GPU时间中的份额，按应用卡时加权，并根据其运行的推理阶段分别计算，同时每个问题还带有屋顶线上限，因此总体得分突出了消耗最多推理时间的内核。在Atrex-Bench上评估六种前沿编码代理显示，即使是最好的普通模型也只能达到生产算子上硬件屋顶线的大约10%；而仅靠正确性会高估能力，因为很大一部分表面通过率来自PyTorch回退而非模型编写的内核。为弥合这一差距，我们共同发布了Atrex-Kernel-Agent（AKA），这是一种基于性能分析的内核优化代理，结合了迭代测量-修订搜索、用于逃离停滞搜索上下文的优化丢弃，以及分层GPU优化知识库（298个参考内核文件和244个优化知识文档，外加用于API/ISA查找的外部上游参考项目）。在一个受控案例研究中，该代理将零FlyDSL回退转换为实际内核，这些内核达到或超过了手动调整的生产基线。

**方法**：从全集群生产推理轨迹中采样30个算子和440种形状，赋予重要性权重和屋顶线上限；提出AKA代理，结合迭代测量-修订搜索、优化丢弃和分层GPU优化知识库。

**结果**：最佳普通模型仅达~10%屋顶线；AKA代理将零FlyDSL回退转换为达到或超过手动调优基线的内核。

[返回索引](#快速索引)

---

<a id="24"></a>
## 24. [PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization](https://arxiv.org/abs/2607.07744)

- **相关度**：0.93
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-07-08, 2026-07-12
- **arXiv ID**：2607.07744
- **作者**：Yingyun Cui, Yi Xie, Piaohong Wang, Jiawei Ma, Bo Liu, Liangliang Cao
- **入选理由**：提出PERFOPT-Bench，专门评估代码智能体在性能优化任务上的能力，涉及profiling、诊断、代码编辑和正确性验证。

**TL;DR**：提出 PERFOPT-Bench 基准，评估代码智能体在性能优化任务上的能力，发现优化性能取决于工作负载，且原始速度提升可能不安全。

**中文摘要**：代码智能体基准测试在很大程度上衡量了智能体能否生成功能正确的补丁，但生产软件还要求在真实执行目标上实现可测量的速度提升。性能优化是一个独特的智能体任务：智能体必须分析性能剖析，诊断跨层瓶颈，在编辑代码时不破坏正确性，并验证增益是可复现的而非测量假象。我们引入了 PERFOPT-Bench，一个用于评估这一完整性能工程循环的基准。每个任务提供一个正确但故意次优的代码库，并要求智能体改进一个目标性能指标；评分需要隐藏的正确性测试、验证的速度提升测量以及轨迹级审计。我们评估了 7 个不同 LLM 和智能体框架的智能体栈在 7 个长时优化任务上的表现。结果显示，优化性能是工作负载相关的，而非仅由模型身份决定：没有单一栈占优，改变智能体框架会显著改变同一 LLM 在不同任务上的速度提升分布。我们进一步发现，原始速度提升作为基准分数是不安全的，因为一些大的增益来自于基准特定的捷径利用；一个探索性的中继试点表明，在初始会话停止后，从外部优化摘要重新开始可以恢复额外的改进空间。该基准及我们的评估可在 https://anonymous.4open.science/r/Dataset-D3CC 获取。

**方法**：构建 PERFOPT-Bench 基准，包含正确但次优的代码库，要求智能体改进性能指标；使用隐藏的正确性测试和验证的速度提升进行评分，并评估多种 LLM 和智能体框架。

**结果**：优化性能与工作负载相关，而非模型身份；无单一栈占优；原始速度提升可能因捷径利用而不安全；中继试点可恢复额外优化空间。

[返回索引](#快速索引)

---

<a id="25"></a>
## 25. [Hawk: Harnessing Hardware-Aware Knowledge for High-Performance NPU Kernel Generation](http://arxiv.org/abs/2607.01590v2)

- **相关度**：0.93
- **方向标签**：Kernel/自动调优、LLM/Agent 代码优化
- **收录日期**：2026-07-02
- **arXiv ID**：2607.01590
- **作者**：Junyi Wen, Ruiyan Zhuang, Yongjia Xu, Pengtu Li, Rui Zou, Hongyi Chen, Chingman Wan, Puxu Yang, Wuhui Chen, Yanlin Wang
- **入选理由**：Hawk利用LLM自动生成NPU高性能内核，通过硬件感知知识提升准确率和执行速度，并验证性能。

**TL;DR**：Hawk是一个无需训练的NPU内核生成框架，通过硬件感知知识表示和检索，将准确率从49.4%提升到80.0%，执行加速高达2.2倍。

**中文摘要**：为神经处理单元（NPU）开发高性能内核是一个关键的行业瓶颈，要求开发者手动处理隐式的硬件约束和严格的内存层次结构。虽然大语言模型提供了巨大的自动化潜力，但由于缺乏硬件特定的先验知识，它们在NPU上会彻底失败。天真地移植来自类似NPU内核的代码片段可能通过编译器，但会持续触发运行时崩溃和性能下降，因为盲目违反了潜在的硬件约束。为了克服这个问题，我们引入了Hawk，一个无需训练的框架，通过三个核心模块利用硬件感知知识：（1）运行时知识合成模块，采用三分可执行知识表示来将错误上下文与可执行语义固有地耦合；（2）瓶颈感知知识检索模块，实现2D检索范式将查询投影到正交的语法和硬件对齐的语义空间；（3）效果驱动知识蒸馏模块，利用LLM驱动的语义仲裁，通过基于经验执行反馈修剪错误和整合冗余来持续蒸馏知识。在真实NPU工作负载上的广泛评估表明，Hawk将生成准确率从49.4%提升到80.0%，并且相比最先进的基线实现了高达2.2倍的执行加速。

**方法**：提出Hawk框架，包含三个模块：运行时知识合成（三分可执行知识表示耦合错误上下文与语义）、瓶颈感知知识检索（2D检索范式投影查询到语法和硬件对齐空间）、效果驱动知识蒸馏（LLM仲裁根据执行反馈修剪冗余）。

**结果**：在真实NPU工作负载上，生成准确率从49.4%提升至80.0%，执行速度相比最先进基线最高提升2.2倍。

[返回索引](#快速索引)

---

<a id="26"></a>
## 26. [Towards Autonomous Accelerator Design: FPGA Accelerator Generation with SECDA](http://arxiv.org/abs/2606.11117v1)

- **相关度**：0.93
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优、编译器优化
- **收录日期**：2026-06-09
- **arXiv ID**：2606.11117
- **作者**：Vinamra Sharma, Xingjian Fu, Jude Haris, José Cano
- **入选理由**：使用LLM引导FPGA加速器设计空间探索，生成并实际执行加速器设计，属于LLM自动生成kernel/硬件代码以优化性能

**TL;DR**：本文扩展了SECDA-DSE框架的评估，通过生成三种FPGA加速器设计（逐元素向量乘法、二维卷积和矩阵转置）并实际执行，证明LLM引导的设计空间探索能有效减少探索时间和人类专业知识需求。

**中文摘要**：为现代人工智能工作负载设计基于FPGA的加速器需要探索一个庞大而复杂的硬件设计空间，涉及架构参数、数据流策略和存储层次，使得该过程非常耗时。虽然现有的方法（如SECDA）通过SystemC仿真和FPGA执行实现了快速的硬件-软件协同设计，但识别高效的加速器配置仍然主要是一个需要大量领域知识的手动过程。SECDA-DSE是一个将大型语言模型（LLM）集成到SECDA生态系统中的框架，用于指导基于FPGA的加速器的设计空间探索（DSE）。它结合了一个用于生成候选架构的结构化DSE探索器和一个LLM堆栈，该堆栈使用检索增强生成和思维链提示执行推理引导的探索，并与反馈循环相结合进行迭代强化改进。基于我们之前介绍SECDA-DSE的工作，本文通过生成三个加速器设计（包括逐元素向量乘法、二维卷积和矩阵转置）并在FPGA硬件上执行端到端执行来扩展其评估。结果表明，SECDA-DSE可以生成符合SECDA规范的加速器设计，这些设计成功地在FPGA硬件上合成和执行。此外，生成的设计捕获了内核特定的计算并行性和数据移动之间的权衡，突显了LLM引导的探索在不同工作负载中适应架构配置的潜力，同时减少了探索时间和大量人类专业知识的需求。

**方法**：提出SECDA-DSE框架，将LLM集成到SECDA生态中，结合结构化DSE探索器生成候选架构，以及LLM堆栈（使用检索增强生成和思维链提示）进行推理引导探索，并通过反馈循环迭代优化。

**结果**：生成了三个符合SECDA规范的加速器设计（逐元素向量乘法、2D卷积、矩阵转置），成功在FPGA上合成和执行，并捕获了计算并行性与数据移动之间的内核特定权衡。

[返回索引](#快速索引)

---

<a id="27"></a>
## 27. [GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization](http://arxiv.org/abs/2605.31464v1)

- **相关度**：0.93
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优
- **收录日期**：2026-05-29
- **arXiv ID**：2605.31464
- **作者**：Zaid Khan, Justin Chih-Yao Chen, Jaemin Cho, Elias Stengel-Eskin, Mohit Bansal
- **入选理由**：LLM作为GPU内核性能预测替代品，优化内核搜索，属于LLM辅助编译/内核优化。

**TL;DR**：研究LLM作为GPU内核性能预测的替代品，通过强化学习提高准确性，在有限评估预算下找到更快内核。

**中文摘要**：GPU内核是现代深度学习的主力，优化它们（通过进化搜索或编码代理）通常需要在目标硬件上重复测量。虽然这些测量提供了内核搜索所需的地面真实信号，但它们是昂贵的，因为每次评估一个内核都需要在GPU上编译和重复执行。随着LLM推理的进步降低了编写新颖内核的成本，并且LLM驱动的搜索扩展到较大的搜索预算，设备端评估成为了一个瓶颈。为了解决这个问题，我们研究LLM如何通过预测提议内核的性能来作为选择性的GPU替代品。一个有用的替代品应该是准确的，并且它应该是选择性的，即知道何时可能出错，并推迟到GPU。为了评估替代品，我们测量其预测是否准确、校准良好，并且在有限的GPU测量预算下对于恢复快速内核是否实用。接下来，我们研究强化学习是否能提高预测准确性和置信度校准。我们的实验表明，LLM可以准确预测相对内核性能，并且它们的实用性可以通过强化学习得到改进。在内核搜索中使用时，该替代品使得搜索在相同的GPU评估预算下可以考虑更多候选者，从而找到比同等预算基线更快的内核。这些结果表明，LLM可以在内核优化中发挥更广泛的作用，即作为GPU的虚拟模型，而不仅仅是内核生成的搜索器。

**方法**：使用LLM预测内核性能，结合选择性机制（不确定时推迟到GPU），并通过强化学习提高预测准确性和置信度校准。

**结果**：LLM能准确预测相对性能，强化学习进一步改进；在相同GPU评估预算下，替代品允许搜索更多候选者，找到更快内核。

[返回索引](#快速索引)

---

<a id="28"></a>
## 28. [FastKernels: Benchmarking GPU Kernel Generation in Production](http://arxiv.org/abs/2605.23215v1)

- **相关度**：0.93
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-05-22
- **arXiv ID**：2605.23215
- **作者**：Gabriele Oliaro, Yichao Fu, May Jiang, Owen Lu, Junli Wang, Zhihao Jia, Hao Zhang, Samyam Rajbhandari
- **入选理由**：GPU内核生成基准，评估LLM agent优化性能，与SemOpt直接相关

**TL;DR**：现有GPU内核基准与生产环境脱节，导致代理优化效果虚假；FastKernels通过46个代表性架构和集成推理框架解决此问题，揭示最强代理仅达0.94倍加速。

**中文摘要**：基于LLM的GPU内核生成代理正在快速发展，但其进展从根本上受到其优化所依赖的基准测试的制约。现有基准测试与生产推理框架严重脱节：它们在单个GPU上使用合成输入评估内核，忽略周围的编译栈，并且奖励的是复制已知优化而非发现新优化。由此产生的奖励信号具有误导性：代理学会生成在沙盒中得分高但在集成到实际系统时会引入接口不兼容、编译栈冲突和静默正确性降级的内核。我们提出FastKernels，这是一个基于跨越8个类别的46个代表性架构的最小集合构建的内核基准测试，其内核共同涵盖了96.2%（409/425）的HuggingFace Transformers架构。FastKernels同时作为一个最小化的、生产级推理框架，在主流的LLM服务上与vLLM和SGLang等成熟系统运行效率相当，并在服务不足的架构上显著超越上游参考；每个任务的接口反映了其架构系列中最先进库的对应模块，支持将优化后的内核直接部署到生产代码库中。在FastKernels上评估最先进的内核代理时，我们发现即使最强的代理也只能在生产基线上实现0.94倍的累计加速，较弱的代理仅为0.78倍和0.53倍——这证实了基准测试与生产之间的不一致是该领域的关键瓶颈。我们发布FastKernels，作为通往基准测试收益直接转化为生产吞吐量改进的内核代理的垫脚石。代码可在https://github.com/Snowflake-AI-Research/fastkernels获取。

**方法**：构建包含46个代表性架构（覆盖96.2% HuggingFace模型）的基准FastKernels，同时作为生产级推理框架，其接口与各架构类的最优库对齐，支持直接部署。

**结果**：最强代理仅实现0.94倍累计加速，弱代理为0.78倍和0.53倍，确认基准-生产不一致是瓶颈。

[返回索引](#快速索引)

---

<a id="29"></a>
## 29. [Distribution-Aware Algorithm Design with LLM Agents](http://arxiv.org/abs/2605.14141v2)

- **相关度**：0.93
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-05-13
- **arXiv ID**：2605.14141
- **作者**：Saharsh Koganti, Priyadarsi Mishra, Pierfrancesco Beneventano, Tomer Galanti
- **入选理由**：LLM代理从样本分布学习并编译出运行更快的求解器代码，直接优化代码性能

**TL;DR**：通过从样本实例中学习分布特定的求解器提示，LLM代理可以编译出更快的求解器代码，在多个优化问题上取得高效率和高质量。

**中文摘要**：许多优化问题反复出现，但分布固定且未知。即使最坏情况下的问题很难，这种分布也可能携带可重用的结构，例如重复的几何结构、分解或资源模式。我们研究如何从样本实例中推断这种结构，并将其编译成求解器代码，该代码在未来的实例上运行更快，同时保持解决方案质量。我们的核心抽象是一个“求解器提示”：从样本中推断出的特定于分布的结构，用于专门化求解器。我们证明了经验上最快的样本一致求解器在正确性和运行时间上都优于固定求解器库，并且可识别的提示可以从多项式数量的样本中恢复。我们使用LLM代码代理在7个问题类别的21个组合优化分布上实例化了该框架。合成的求解器达到了平均归一化质量0.971，同时运行速度比经典启发式算法、Gurobi和有限时间的精确后端快几个数量级，尽管它们并不在每个族上都优于每个基线。与LLM合成基线相比，它们比一次性Codex、一次性Claude Code和最佳5选1的开源模型变体更快；它们提高了Claude Code和最佳5选1的质量，同时几乎匹配了Codex的质量并运行速度更快。这隔离了迭代合成循环的贡献，并没有声称在所有LLM基线上均匀支配。在PACE 2025支配集私有实例上，合成的求解器在所有100个图上都有效，并且运行速度比已发布的竞赛求解器快约75倍到125倍，解决方案大小在几个百分点之内。这些结果表明，LLM代理可以发现特定于分布的计算捷径，并将其编译成高效的求解器代码。

**方法**：提出“求解器提示”抽象，从样本中推断分布特定结构并编译成求解器代码；使用LLM代码代理在21个分布上迭代合成求解器。

**结果**：合成的求解器平均归一化质量0.971，速度比经典启发式、Gurobi等快多个数量级；在PACE 2025支配集上比竞赛求解器快75-125倍，质量接近。

[返回索引](#快速索引)

---

<a id="30"></a>
## 30. [CppPerf: An Automated Pipeline and Dataset for Performance-Improving C++ Commits](http://arxiv.org/abs/2605.10890v1)

- **相关度**：0.93
- **方向标签**：Benchmark/评测、优化策略检索
- **收录日期**：2026-05-11
- **arXiv ID**：2605.10890
- **作者**：Tommy Ho, Khashayar Etemadi, Zhendong Su
- **入选理由**：提出CppPerf-Mine流水线从GitHub挖掘C++性能补丁并构建基准CppPerf-DB，用于评估自动性能修复工具，与SemOpt从历史优化中提取策略的方向高度一致。

**TL;DR**：提出CppPerf-Mine流水线从GitHub挖掘C++性能补丁，构建了包含347个手动验证补丁的CppPerf-DB基准测试，发现现有工具修复率仅13.5%。

**中文摘要**：自动修复性能错误的最新进展需要现实、可执行的基准测试。然而，现有的C++性能基准测试主要来自竞争性编程提交，而近期的现实世界基准测试主要针对Python和.NET。为填补这一空白，我们提出了CppPerf-Mine，一个可配置的流水线，它结合了结构性提交过滤、基于LLM的提交分类器以及容器化构建与测试阶段，从GitHub上的开源C++仓库中挖掘执行时间改进的补丁，并为每个补丁生成完全可重现的Docker镜像。利用CppPerf-Mine，我们构建了CppPerf-DB，一个包含来自42个成熟C++仓库的347个手动验证补丁的基准测试，其中39%为多文件补丁，从而支持仓库级别的修复工具评估。在我们初步研究中，OpenHands仅正确修复了CppPerf-DB中13.5%的补丁，证实了现实世界C++性能修复仍然是一个开放的挑战。CppPerf-Mine和CppPerf-DB是开源且公开可用的，网址为：https://doi.org/10.5281/zenodo.20097425。此外，演示视频可在https://www.youtube.com/watch?v=nixlupIgSdM获取。

**方法**：通过组合结构性提交过滤、基于LLM的提交分类器和容器化构建与测试阶段，从GitHub开源C++仓库中挖掘可重现的性能改进补丁。

**结果**：构建了包含347个来自42个成熟C++仓库的手动验证补丁的基准测试CppPerf-DB，其中39%为多文件；OpenHands仅正确修复13.5%。

[返回索引](#快速索引)

---

<a id="31"></a>
## 31. [AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance](http://arxiv.org/abs/2606.30949v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-29
- **arXiv ID**：2606.30949
- **作者**：Yang Zou, Zijian Ding, Yizhou Sun, Jason Cong
- **入选理由**：LLM多智能体工作流自动重构软件为HLS代码以提升性能，包含自进化记忆系统，直接相关。

**TL;DR**：AgRefactor是一个基于LLM的多智能体工作流，用于将软件重构为HLS兼容程序，通过自进化记忆系统和自动化工具集成，在多个基准测试上优于现有方法。

**中文摘要**：高层次综合（HLS）提供了从概念到硅片的快速路径，但由于受限的语言支持以及软件与硬件编程实践之间的差距，将现实世界的软件转换为可综合的HLS代码仍然具有挑战性。现有的自动化和基于LLM的重构方法部分解决了这个问题，但它们往往缺乏灵活性，难以扩展，并且计算成本高昂。我们引入了AgRefactor，一种基于LLM的多智能体工作流，用于将软件重构为HLS兼容程序。AgRefactor包含一个自进化记忆系统，该系统跨任务积累和检索事实性和策略性知识，提高了对未见程序的鲁棒性和效率。为了降低成本并增强可扩展性，它集成了自动化重构工具，使智能体能够平衡LLM驱动的重写与高效的基于工具的转换。在11个具有挑战性的现实世界基准测试中的9个上，这些基准测试比先前工作中研究的最复杂案例长5-10倍，AgRefactor优于或匹配了最先进的自动化重构工具和基于相同框架构建的强LLM基线。进一步的智能体性能优化在SoTA pragma调优工具上实现了6.51倍的几何平均加速，并且在额外资源少于20%的情况下，相比优化的开源设计实现了1.20倍的加速。AgRefactor是完全自动化的并且是开源的。

**方法**：提出AgRefactor，包含多智能体协作、自进化记忆系统（积累事实和策略知识）以及集成自动化重构工具，平衡LLM驱动和工具化转换。

**结果**：在11个基准测试中9个优于或匹配现有方法；性能优化带来6.51倍加速（vs SoTA pragma调优）和1.20倍加速（vs优化开源设计），资源开销<20%。

[返回索引](#快速索引)

---

<a id="32"></a>
## 32. [Evaluating LLMs on Real-World Software Performance Optimization](http://arxiv.org/abs/2606.25530v1)

- **相关度**：0.92
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-06-24
- **arXiv ID**：2606.25530
- **作者**：Ezgi Sarıkayak, Wenchao Gu, Hesham Ghonim, Chunyang Chen
- **入选理由**：SWE-Pro是专门针对代码性能优化的仓库级基准，包含专家优化和噪声感知测量，直接用于评估LLM自动优化能力。

**TL;DR**：SWE-Pro是一个仓库级性能优化基准测试，基于102个专家优化，评估LLM在运行时和内存上的表现，发现LLM远不如专家。

**中文摘要**：软件性能优化是一项众所周知的复杂且人工密集的任务。尽管大型语言模型（LLMs）在代码优化方面的应用日益增长，但我们仍然缺乏能够捕捉真实代码库中优化实际发生方式的基准测试。现有的框架通常通过关注孤立的函数或单一的性能指标来过度简化问题，忽略了执行时间和内存占用之间的关键权衡、测量环境的固有噪声以及不同输入数据和执行条件引入的变异性。我们通过引入SWE-Pro来解决这个问题，这是一个从开源项目中102个专家编写的优化中得出的仓库级基准测试。与之前的基准测试不同，SWE-Pro为每个任务配对了参数化测试，以评估运行时、峰值内存和时间加权内存使用（TWMU），在不同的输入数据和执行条件下，并在考虑噪声的测量条件下进行。我们的评估表明，当前的LLMs表现不佳：运行时间提升微乎其微，内存优化几乎不存在。这与专家实现形成鲜明对比，专家实现在基准测试任务上实现了15.5倍的总体加速和171.3倍的峰值内存减少。在91.2%的任务中观察到专家编写的运行时间改进，在65.7%的任务中观察到峰值内存改进。我们的发现暴露了当前LLM能力与专家级工程需求之间的巨大差距。

**方法**：从开源项目中收集102个专家编写的优化，构建仓库级基准SWE-Pro，每个任务包含参数化测试，在噪声感知条件下评估运行时、峰值内存和时间加权内存使用（TWMU）。

**结果**：当前LLM的运行时增益可忽略，内存优化几乎为零；而专家实现平均加速15.5倍，峰值内存减少171.3倍，91.2%任务有运行时改进，65.7%有内存改进。

[返回索引](#快速索引)

---

<a id="33"></a>
## 33. [LLM-Guided Test-Time Discovery of Quantum-Chemical Approximation Algorithms](http://arxiv.org/abs/2606.20729v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-06-17
- **arXiv ID**：2606.20729
- **作者**：Masaya Hagai, Yuta Suzuki, Tomoya Murata, Shuhei Kurita, Masaki Adachi
- **入选理由**：LLM自动发现并实现近似算法加速量子化学计算，提升运行速度并有验证。

**TL;DR**：LADeQ是一个LLM引导的工作流，能在测试时自动发现、实现和基准测试候选近似算法，加速量子化学计算并保持误差可控。

**中文摘要**：量子化学模拟支撑着现代材料发现，但其影响受到高昂计算成本和对固定近似方案的依赖的限制。基础模型，如机器学习原子间势，加速了工作流程的某些部分，但它们对大规模预训练的依赖限制了其在化学前沿的适应性，而那里方法论创新和数据稀疏是常态。自主AI系统可以自动化现有模拟流程，但它们仍然受到它们编排的预定义工具和算法的约束。为此，我们引入了LADeQ，一个由LLM引导的工作流程，能够在测试时在现有量子化学代码中发现、实现和基准测试候选近似算法。LADeQ不是从预定义库中选择，而是按需构建候选近似方案，借鉴来自空间统计、电路模拟和核方法等学科的技术，这些技术在电子结构理论中此前鲜有出现。由于它基于现成的语言模型，LADeQ无需任务特定的预训练或精心策划的数据，并且由此产生的实现是透明且可检查的，具有明确可追溯的近似误差，从而能够原则性地控制精度-效率权衡。我们展示了LADeQ加速了耦合簇单双激发（CCSD）和组态相互作用单双激发（CISD）计算，同时将相关能量误差保持在用户指定的容差内，展示了在现有电子结构求解器内自主、目标驱动的近似算法发现。

**方法**：LADeQ利用现成语言模型，在测试时按需构建候选近似方案，借鉴空间统计、电路模拟和核方法等跨学科技术，无需任务特定预训练。

**结果**：LADeQ加速了CCSD和CISD计算，同时将相关能量误差控制在用户指定容差内。

[返回索引](#快速索引)

---

<a id="34"></a>
## 34. [PreAct: Computer-Using Agents that Get Faster on Repeated Tasks](http://arxiv.org/abs/2606.17929v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-06-16
- **arXiv ID**：2606.17929
- **作者**：Bojie Li
- **入选理由**：PreAct编译成功执行为状态机并重放加速重复任务，直接提升性能并验证正确性。

**TL;DR**：PreAct通过将首次成功的运行编译成状态机程序并在后续直接重放，实现8.5-13倍加速，同时通过存储时验证确保重放正确性，并在多个基准测试中提升性能。

**中文摘要**：使用计算机的代理通过屏幕操作真实软件——点击和打字——但它们每个任务都从头开始解决：要求重复执行任务时，代理会重新读取屏幕、重新推理每一步操作，并再次付出全部代价。我们提出PreAct，让这样的代理在重复执行任务时变得更快。第一次成功时，PreAct将运行过程编译成一个小的状态机程序——检查屏幕的状态、执行动作的转换——并在后续运行中直接重放该程序，而不是调用代理，速度提升8.5-13倍，且无需每步调用语言模型。重放并非盲目：在每个步骤中，PreAct在操作前检查屏幕是否与程序预期匹配，一旦出现异常便将控制权交还给代理。PreAct在决定保留哪些程序时也应用同样的原则：新编译的程序只有在从干净状态重新运行时，独立的评估者确认它解决了任务后，才进入存储库——这能捕获那些重放到最后一步却未完成任务的问题程序。在移动、桌面和网络基准测试中，这种存储时检查将改进的重复运行与因故障程序累积而退化的重复运行区分开来，每个基准测试提升1.75-2.6个任务，三个基准测试方向一致；当没有合适程序时，从头探索的备用策略使PreAct与强大的记录-重放基线持平。我们还报告了哪些因素不重要：提示措辞、运行时护栏，以及选择重用什么程序的是语言模型还是普通嵌入检索器。

**方法**：PreAct在代理首次成功完成任务时，将运行过程编译为轻量级状态机程序（包含屏幕检查和动作转换），后续运行时直接重放该程序，仅在屏幕状态不匹配时回退到代理。同时，新程序在存储前需通过独立评估者的验证，确保其能正确完成任务。

**结果**：PreAct在移动、桌面和网络基准测试中实现8.5-13倍加速，无需每步调用语言模型；存储时检查使性能提升1.75-2.6个任务，且与强基线持平；提示措辞、运行时护栏和选择策略对性能无显著影响。

[返回索引](#快速索引)

---

<a id="35"></a>
## 35. [Embedded Arena: Iterative Optimization via Hardware Feedback](http://arxiv.org/abs/2606.16190v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、Kernel/自动调优
- **收录日期**：2026-06-15
- **arXiv ID**：2606.16190
- **作者**：Zhihan Zhang, Alexander Le Metzger, Jiuyang Lyu, Chun-Cheng Chang, Jiayi Shao, Yujia Liu, Emmanuel Azuh Mensah, Edward Wang, Kurtis Heimerl, Gregory D. Abowd, Shwetak Patel, Natasha Jaques, Vikram Iyer
- **入选理由**：LLM代理通过硬件反馈迭代优化嵌入式模型与固件，实现压缩和精度提升，属于自动代码/系统性能优化。

**TL;DR**：提出硬件在环的LLM代理框架，通过迭代优化自动实现嵌入式AI模型的高效部署，在压缩和精度上均超越人类专家。

**中文摘要**：嵌入式设备，从野生动物监测站到临床可穿戴设备，由于延迟、通信或隐私限制，需要本地AI推理。为异构微控制器（MCU）优化模型需要同时满足内存、功耗和温度的严格物理约束，同时保持准确性，这是一种多维优化，目前由专家手动执行。我们探讨LLM代理是否能在真实硬件反馈的引导下自主导航这个复杂、多轮的流程，并引入一个硬件在环代理竞技场，其中代理迭代优化模型和固件——编译、烧录并在真实硬件上测量——以实现闭环优化。前沿模型，包括Claude Opus 4.7和Gemini 3.1 Pro，在没有硬件反馈的情况下完全失败（0%部署成功率），而我们的硬件在环公式在三次迭代内实现了首次成功部署，并在七次内超越人类专家结果。这种代理协同优化实现了视觉模型250倍压缩，精度损失<3.3%，音频模型400倍压缩，特征错误率损失<6%，通过太阳能收集实现了在商业MCU上的无电池运行。我们在两个实际系统中展示了实际影响：一个麋鹿检测相机陷阱（96.7%准确率）和一个用于儿童发展研究的语音转录可穿戴设备（8.44% FER）。

**方法**：构建硬件在环代理竞技场，LLM代理通过编译、烧录、测量真实硬件反馈，闭环迭代优化模型和固件。

**结果**：在三次迭代内成功部署，七次内超越人类；视觉模型250倍压缩（损失<3.3%），音频400倍压缩（损失<6%）；实现无电池太阳能量收集运行；实际系统准确率96.7%（目标检测）和8.44% FER（语音转录）。

[返回索引](#快速索引)

---

<a id="36"></a>
## 36. [Structuring agentic AI for HPC code modernization](http://arxiv.org/abs/2606.08710v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-07
- **arXiv ID**：2606.08710
- **作者**：Anthony Marinov, Igor Sfiligoi
- **入选理由**：代理AI成功将Fortran代码并行化为C++，实现代码性能现代化

**TL;DR**：本文介绍了一种高度结构化的“手把手”代理AI方法，成功将6万行Fortran单线程MPI代码在几个月内转换为OpenMP并行C++ MPI代码，而单纯LLM工具不足。

**中文摘要**：传统科学代码的现代化通常是为了跟上计算资源生态系统中不断变化的更新。并行化和从支持不良的软件生态系统迁移是研究软件工程领域中最耗时的两项活动。本文介绍了我们在两阶段AI辅助下对NMAP-RKPM进行现代化改造的经验，NMAP-RKPM是一个基于再生核粒子方法（RKPM）的约6万行、3D显式固体力学物理引擎。我们在几个月内将这款基于Fortran的单线程MPI应用程序转换为OpenMP并行C++ MPI工具。虽然基于大语言模型（LLM）的工具本身被证明是不足的，但我们开发了一种高度结构化的“手把手”代理AI方法，比如提供手动创建的示例、确保持续可构建性以及限制会话范围，这种方法反而非常有效。本文提供了成功的AI辅助步骤以及我们必须克服的问题，同时阐述了所选路径背后的推理。

**方法**：开发了高度结构化的“手把手”代理AI方法，包括提供手动创建的示例、确保持续可构建性和限制会话范围。

**结果**：在几个月内成功将NMAP-RKPM（约6万行Fortran单线程MPI代码）转换为OpenMP并行C++ MPI工具。

[返回索引](#快速索引)

---

<a id="37"></a>
## 37. [AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference](http://arxiv.org/abs/2606.07665v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-04
- **arXiv ID**：2606.07665
- **作者**：Xuanzhe Li, Ziyan Weng, Zhiyu Zhu, Junhui Hou
- **入选理由**：LLM引导编译器生成CUDA实现，实现4-5倍推理加速，直接相关。

**TL;DR**：AgentCompile利用LLM提供搜索元数据，编译器通过模板生成、验证和选择CUDA实现，在多个Transformer模型上实现4-5倍推理加速。

**中文摘要**：Transformer推理越来越依赖专门的编译器和运行时支持，但实际模型图仍然需要语义决策，即哪些区域值得专门优化以及哪些CUDA实现系列是可行的。我们提出了AgentCompile，一个LLM引导的CUDA推理编译器，它仅将LLM输出作为咨询性搜索元数据。给定编译器派生的区域摘要和有界候选空间，LLM提出语义标签、候选优先级、参数提示和风险注释；编译器通过模板实例化CUDA候选，检查接口和硬件约束，经验验证候选，根据测量延迟选择实现，并在不支持或无利可图的专门化时回退。在端到端自回归生成中，AgentCompile在五个代表性工作负载上，相对于PyTorch eager，在Qwen3-1.7B、Qwen3-4B和Llama-3.2-1B-Instruct上分别实现了平均5.66倍、4.05倍和4.26倍的加速。我们将开源该项目。

**方法**：LLM基于编译器区域摘要提出语义标签和候选优先级等元数据；编译器通过模板实例化CUDA候选，检查接口和硬件约束，通过经验验证选择延迟最优的实现，并支持回退。

**结果**：在Qwen3-1.7B、Qwen3-4B和Llama-3.2-1B-Instruct上，端到端自回归生成平均加速比分别达到5.66x、4.05x和4.26x。

[返回索引](#快速索引)

---

<a id="38"></a>
## 38. [The Time is Here for Just-in-Time Systems: Challenges and Opportunities](http://arxiv.org/abs/2605.24096v1)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-05-22
- **arXiv ID**：2605.24096
- **作者**：Shu Liu, Alexander Krentsel, Shubham Agarwal, Mert Cemri, Ziming Mao, Soujanya Ponnapalli, Alexandros G. Dimakis, Sylvia Ratnasamy, Matei Zaharia, Aditya Parameswaran, Ion Stoica
- **入选理由**：提出Jitskit，利用LLM生成针对特定规格的高性能键值存储系统，在18个规格上超越现有系统，实现了自动代码性能优化。

**TL;DR**：提出基于LLM的即时系统合成方法Jitskit，能针对特定规格自动生成高性能键值存储系统，在18个规格上超越现有系统。

**中文摘要**：核心系统（如键值存储）历来需要多年时间才能构建，并且设计为通用型以在部署之间分摊成本，但付出了显著的性能代价。我们认为，基于LLM的编码代理如今使一种不同的方法变得可行：即时系统（Just-in-Time Systems），即整个系统从头合成，专门针对环境、工作负载和所需系统属性进行定制。我们提出了一个即时系统合成流水线Jitskit，并探索了其在从覆盖不同YCSB工作负载、部署约束（例如，计算资源）和系统属性（例如，一致性和持久性）的规格卡中合成键值存储的有效性。Jitskit迭代地改进系统实现，以匹配规格说明和不断演进的评估测试套件。最终合成的系统性能卓越，在尝试的18个规格中全部超越了可比的最新系统，在最优规格上比最佳现成基线高出4.6倍。直接运行Claude Code要么奖励作弊，要么性能比Jitskit差5.4倍。我们讨论了在构建Jitskit过程中克服的挑战及其关键启示。

**方法**：提出Jitskit流水线，通过迭代精炼系统实现并匹配规格，结合评估测试套件，利用LLM编码代理合成键值存储。

**结果**：在18个规格上全部超越最佳基线，性能提升最高4.6倍；相比之下，直接使用Claude Code表现差5.4倍。

[返回索引](#快速索引)

---

<a id="39"></a>
## 39. [CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging](http://arxiv.org/abs/2605.08455v2)

- **相关度**：0.92
- **方向标签**：LLM/Agent 代码优化、Benchmark/评测
- **收录日期**：2026-05-08
- **arXiv ID**：2605.08455
- **作者**：Shiyang Li, Haoyang Chen, Mattia Fazzini, Caiwen Ding
- **入选理由**：CUDABeaver是LLM自动CUDA调试基准，直接评估修复后的性能保留，属于自动代码优化与评估。

**TL;DR**：提出CUDABEAVER基准和pass@k(M,C,A)指标，通过协议感知评估揭示LLM修复CUDA代码时性能保留对成功率的显著影响。

**中文摘要**：调试CUDA程序长期以来一直很有挑战性，因为故障通常源于硬件行为、编译器决策、内存层次结构和异步执行之间微妙的交互。更重要的是，随着GPU在科学计算、机器学习、图形学和系统工作负载中的快速扩展，CUDA调试变得比以往任何时候都更具挑战性。当前基于LLM的CUDA编程评估在很大程度上忽略了这一情况：模型可以通过退化性修复（degeneration）通过正确性测试，即将CUDA代码简化为更安全但更慢的程序，从而放弃原有的优化结构。我们引入了CUDABEAVER，这是一个针对LLM生成的CUDA代码中实际失败工作空间的CUDA调试基准。每个任务提供了有问题的候选代码、本地构建/测试命令、原始错误证据以及一个可编辑的文件。CUDABEAVER评估修复者是否真正修复了失败的CUDA代码，还是仅仅找到了一个更慢但能通过测试的替代方案，并按失败类别、调试轨迹、停滞模式和性能保持情况报告结果。我们进一步提出了pass@k(M,C,A)，一种协议条件的CUDA调试指标，通过明确修复者M、语料库C和协议轴A。使用该指标在213个任务和七个前沿LLM上，我们展示了协议感知的评估能更真实地反映CUDA调试能力：当性能损失容忍度较高时，修复者看起来更强，但即使是对性能的轻微更严格要求也会显著降低测量成功度，使分数变化高达40个百分点。

**方法**：构建CUDABEAVER基准（含213个真实失败任务），提出pass@k(M,C,A)指标，明确区分修复者、语料库和评估协议，在七个LLM上进行实验。

**结果**：协议感知评估显示，性能损失容忍度从宽松到严格时，修复成功率变化高达40个百分点，说明现有评估高估了LLM的调试能力。

[返回索引](#快速索引)

---

<a id="40"></a>
## 40. [Heuristic Learning for Active Flow Control Using Coding Agents](http://arxiv.org/abs/2607.11565v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-07-13
- **arXiv ID**：2607.11565
- **作者**：Paul Garnier, Jonathan Viquerat, Elie Hachem
- **入选理由**：使用LLM agent迭代搜索、评估和修订显式反馈控制器代码，在13个主动流动控制基准上匹配或超越DRL，属于直接的LLM/agent自动代码性能优化。

**TL;DR**：使用编码代理直接搜索显式反馈律的启发式学习在主动流动控制中实现了与深度强化学习相当或更优的性能，同时保持控制器的紧凑性和可解释性。

**中文摘要**：主动流动控制涉及非线性动力学、部分观测和计算代价高昂的仿真，使得控制器设计极具挑战性。深度强化学习已成为解决此类问题的强大框架，但其成功通常依赖于大量的仿真交互，并且产生的神经网络策略的决策过程往往难以解释。在这项工作中，我们研究了一种不同的范式：不是优化神经网络参数，而是使用现代编码代理直接搜索显式可执行的反馈律。我们引入了一种约束启发式学习协议，其中代理通过仅与公共基准接口交互，迭代地提出、评估和修改控制器实现。该框架在涵盖一维、二维和三维问题的13个主动流动控制基准上进行了评估，并在相同的仿真预算下与最强的现有深度强化学习基线进行了比较。发现的启发式控制器在13个环境中的10个中匹配或优于最佳深度强化学习策略，同时保持紧凑、可解释和可直接检查。在整体性能之外，所得控制器揭示了具有物理意义的反馈机制，成功迁移到更具挑战性的配置中，并在不同的雷诺数和瑞利数、执行器数量和观测稀疏性下保持竞争力。这些结果表明，通过编码代理进行启发式学习构成了传统强化学习的一个可信且互补的替代方案，结合了竞争性能与物理可解释的控制器表示。提示和源代码可在https://github.com/DonsetPG/fluid-heuristic-learning获取。

**方法**：提出约束启发式学习协议，通过编码代理迭代提出、评估和修改控制器实现，仅通过公共基准接口交互，直接搜索显式可执行的反馈律。

**结果**：在13个基准中，启发式控制器在10个上匹配或超越深度强化学习，控制器紧凑可解释，揭示物理反馈机制，并成功迁移到更复杂配置。

[返回索引](#快速索引)

---

<a id="41"></a>
## 41. [Rethinking Code Performance Benchmarks for LLMs](http://arxiv.org/abs/2607.07619v1)

- **相关度**：0.90
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-07-08
- **arXiv ID**：2607.07619
- **作者**：Nhat Minh Le, Yisen Xu, Zhijie Wang, Tse-Hsun, Chen
- **入选理由**：重新思考LLM代码性能基准，提出多智能体框架生成性能测试，暴露代码优化差异。

**TL;DR**：当前函数级性能基准测试因测试充分性不足而无法有效暴露LLM生成代码的性能差异，本文提出多智能体框架生成的性能测试能显著提升检测效果。

**中文摘要**：许多函数级性能基准测试已被提出，用于评估大型语言模型（LLM）是否能生成高效的程序。然而，这些基准测试的结果通常表明，LLM生成的实现与规范解决方案在执行时间上几乎没有差异。在本文中，我们重新审视了四个流行的基准测试：EffiBench、Enamel、EvalPerf和Mercury。我们通过将每个任务运行30次并利用统计检验评估规范解决方案与基准测试提供的高性能实现之间的运行时间差异，在更严格的设置下评估了1,538个任务。使用基准测试提供的测试套件，只有6.11%的高性能实现显著快于规范解决方案。在对308个非显著任务的手动分析中，99个高性能实现不包含有意义的性能变化，而209个包含潜在的性能改进，但这些改进未被原始测试暴露出来。这些结果表明，主要限制不仅在于评估方法，还在于基准测试提供的性能测试的充分性有限。为了解决这一限制，我们提出了一种基于LLM的多智能体框架，用于生成比原始测试更有效地暴露运行时差异的性能导向测试。该框架使用三个独立的智能体来生成、诊断和修复确定性测试，这些测试在保留功能正确性的同时更好地暴露性能差异。在原始测试未发现显著性能差异的1,345个基准任务中，使用DeepSeek-v3.1和GPT-4o的框架生成的测试分别揭示了24.01%和25.43%的任务存在统计显著的改进，优于当前最先进的基于LLM的性能测试生成方法。

**方法**：提出基于LLM的多智能体框架，包含生成、诊断和修复三个智能体，用于创建确定性性能测试，更有效地暴露运行时差异。

**结果**：在1,345个任务中，使用DeepSeek-v3.1和GPT-4o的框架分别使24.01%和25.43%的任务显示出统计显著的性能改进，优于现有方法。

[返回索引](#快速索引)

---

<a id="42"></a>
## 42. [Auto: The AGI Compiler](http://arxiv.org/abs/2607.04542v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-07-05
- **arXiv ID**：2607.04542
- **作者**：Jaber Jaber, Osama Jaber
- **入选理由**：将LLM agent行为编译为高效WebAssembly程序，降低延迟与成本，符合LLM驱动的代码自动优化。

**TL;DR**：Auto通过记录LLM智能体行为、提取确定性部分为已验证程序并生成WebAssembly认知二进制，利用分层运行时和守卫机制实现低成本推理。在AUTO-BENCH上87.1%的跨度是确定性的，成本降低6.4倍，准确率96.9%，但校准和参考保真度是关键。

**中文摘要**：每一轮LLM智能体的运行都会在前沿模型上逐个令牌地重新推导其行为：聪明、昂贵、缓慢且无边界。我们提出Auto，一个编译器，它记录实时智能体行为，测量哪些部分实际上是确定性的，将其提取为经过验证的程序或蒸馏后的专家，并生成认知二进制：WebAssembly工件，其清单携带测量保证，其声明的能力由沙箱物理强制执行。分层运行时在符合校准的守卫后面执行编译后的行为；守卫触发则回退到参考智能体，捕获的轨迹重新编译下来，因此没有东西被重复计算。我们使用“AGI编译器”在一个狭窄、可测试的意义上：一个系统，它能自主地将新经验转化为永久的、经过验证的、近乎免费的技能，同时衡量它不知道的东西。在AUTO-BENCH（我们引入并预注册的基准测试）上，560个记录的边缘智能体跨度中有87.1%是经见证确定性的（四个被普查的任务族中有三个达到100.0%）。在包含300个项目和三次预定分布转移的流上，闭环编译了三代工件，并将每项边际成本从59微美元降至2微美元（端到端6.4倍），在见证输入上达到96.9%的等价性，且零错误。同一流还量化了失败模式：一个松散的守卫错误地标记了48.9%的编译答案，一个不忠实的回退参考导致验证门拒绝重新编译。校准和参考保真度，而不是模型能力，决定了低成本是否保持正确。代码：https://github.com/RightNow-AI/auto

**方法**：记录实时智能体行为，测量确定性部分，将其提取为经过验证的程序或蒸馏专家，生成WebAssembly认知二进制；采用分层运行时，通过校准守卫执行编译行为，守卫触发时回退到参考智能体并重编译。

**结果**：在AUTO-BENCH上560个跨度中87.1%为确定性；300项流测试中边际成本从59降至2微美元（6.4倍），准确率96.9%且零错误；松散守卫导致48.9%错误标记，不忠实参考导致重编译拒绝。

[返回索引](#快速索引)

---

<a id="43"></a>
## 43. [Copper: Unifying Correctness and Performance Specification in Code Generation](http://arxiv.org/abs/2607.03130v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化
- **收录日期**：2026-07-03
- **arXiv ID**：2607.03130
- **作者**：André Lizardo, Raul Barbosa
- **入选理由**：结合形式化验证与性能感知规范自动生成高效代码，含自动性能剖析循环。

**TL;DR**：Copper框架通过结合形式化验证与性能感知规范，生成了可证明正确且高效的代码，在多样任务上显著优于基线AI生成代码。

**中文摘要**：生成式人工智能在生成功能正确的代码方面取得了显著进展，但确保同时具备正确性和性能仍然是一个开放挑战。我们提出了Copper，一个结合了形式化验证与性能感知规范的框架，用于生成可证明正确且高效执行的代码。我们的方法将AI驱动的代码合成与形式化验证工具以及自动化性能分析循环相结合。在多种算法和实际编程任务上的评估表明，与基线AI生成的代码相比，Copper生成的解决方案在满足严格正确性保证的同时，在运行时和内存效率方面实现了显著改进。这项工作表明，在AI辅助编程中弥合可信性与性能之间的鸿沟是可行的，为可靠、高性能代码生成提供了一条实用路径。

**方法**：将AI驱动的代码合成与形式化验证工具及自动化性能分析循环相结合，构建Copper框架。

**结果**：在多种算法和实际编程任务上，Copper生成的代码在运行时和内存效率上显著优于基线AI代码，同时满足严格正确性保证。

[返回索引](#快速索引)

---

<a id="44"></a>
## 44. [Can Coding Agents Implement Missed Compiler Optimizations? Evaluating LLM Agents on LLVM Peephole Optimizations](http://arxiv.org/abs/2607.02684v1)

- **相关度**：0.90
- **方向标签**：编译器优化、LLM/Agent 代码优化、Benchmark/评测
- **收录日期**：2026-07-02
- **arXiv ID**：2607.02684
- **作者**：Hongxu Xu, Chunhao Liao, Xintong Zhou, Chengnian Sun
- **入选理由**：评估编码代理修复LLVM编译器窥孔优化，涉及自动代码优化与性能验证

**TL;DR**：PeepholeBench是一个评估编码智能体修复LLVM编译器遗漏窥孔优化的基准，发现当前智能体在正确性和收益性上均无法匹敌人类开发者，主要失败模式为转换过窄和LLVM机制误用。

**中文摘要**：基于大型语言模型的编码智能体现在能够修补可观的真实世界代码库，但它们能否开发编译器优化仍然是一个开放问题。为了研究这一问题，我们引入了PeepholeBench，这是一个评估框架，其任务来源于针对LLVM的InstCombine pass报告的真实世界遗漏窥孔优化。由于遗漏的窥孔优化通常通过小而局部的补丁修复，它们为编码智能体提供了一个范围明确但要求严格的测试平台：正确的修复需要对程序语义进行严谨推理，并熟悉优化器特定的约定。PeepholeBench的任务源自21个已解决的LLVM问题和19个合并的拉取请求（PR），仅向智能体提供每个修复之前存在的issue上下文，并评估生成的补丁的正确性和收益性。通过PeepholeBench，我们评估了最先进的编码智能体修复LLVM InstCombine pass中遗漏窥孔优化的能力，并将其补丁与对应的人工编写的修复进行比较。我们观察到正确性与收益性之间存在张力，没有智能体能在两个维度上同时匹敌人类开发者。主要的失败模式是过于狭窄的转换以及对LLVM特定机制的误用，这些错误现有的测试套件很少能暴露。这些结果共同确立了PeepholeBench作为编码智能体的一个真实且具有挑战性的基准，并为构建能够更可靠地协助编译器优化开发的智能体指明了未来方向。

**方法**：构建PeepholeBench任务：从21个已解决LLVM问题和19个合并PR中提取真实窥孔优化案例，仅提供修复前的issue上下文，评估智能体生成的补丁的正确性和收益性，并与人类修复对比。

**结果**：无智能体能在正确性和收益性上同时匹敌人类；主要失败模式包括过于狭窄的转换和LLVM特定机制误用（如模式匹配错误），这些错误难以被现有测试套件捕获。

[返回索引](#快速索引)

---

<a id="45"></a>
## 45. [Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?](http://arxiv.org/abs/2607.01211v2)

- **相关度**：0.90
- **方向标签**：Benchmark/评测
- **收录日期**：2026-07-01
- **arXiv ID**：2607.01211
- **作者**：Zhi Chen, Zhensu Sun, Yuling Shi, David Lo, Lingxiao Jiang
- **入选理由**：审计性能优化基准（GSO, SWE-Perf等），直接评估代码优化代理。

**TL;DR**：对GSO、SWE-Perf和SWE-fficiency三个仓库级性能优化基准的审计表明，大多数参考补丁存在跨机器可重复性问题，评分规则导致排名不一致，且大量任务已被公开提交解决，揭示了排行榜分数的局限性。

**中文摘要**：仓库级性能优化基准测试（如GSO、SWE-Perf和SWE-fficiency）通过将补丁应用于真实仓库并对比运行时间与未优化基线和官方参考补丁来评估编码代理。其排行榜分数越来越多地被用作编码代理进展的证据，但这些分数可能混淆运行时不稳定、基准特定评分规则以及有多少任务已被至少一个公开提交解决。我们对这三个基准的这些问题进行了审计。首先，我们在四种常见的Google Cloud机器类型上重放了740个代码优化任务的官方参考补丁。大多数基准任务可以重放，但它们的参考补丁在所有跨机器重放中满足原始基准有效性规则的只有39/102的GSO任务、11/140的SWE-Perf任务和411/498的SWE-fficiency任务；SWE-Perf尤其脆弱，因为许多参考补丁产生的运行时变化几乎为零。其次，我们显示公开提交排名在很大程度上取决于基准评分规则。在GSO和SWE-fficiency共享的八个公开提交中，官方排名在28对提交比较中有9对不一致，而SWE-fficiency的排行榜评分规则将最差的十个任务的分数权重分配过高，达到58.5%-82.8%。第三，观察每个任务的10个公开提交，我们发现至少有1个提交在85.3%（384/450）的可重放GSO和SWE-fficiency任务中达到或超过了参考补丁，在99.8%（449/450）的任务中击败了未优化的基础代码。我们的研究通过识别具有更可靠性能信号的任务、量化每个任务的分数贡献以及揭示被聚合排名隐藏的剩余性能差距，补充了排行榜分数。

**方法**：重放740个任务的官方参考补丁于四种Google Cloud机器上验证有效性；对比八个公开提交的评分规则一致性；分析每个任务多个提交的表现。

**结果**：仅少数参考补丁跨机器有效（GSO 38%，SWE-Perf 8%，SWE-fficiency 83%）；评分规则导致排名分歧；大部分任务已有至少一个提交达到或超过参考补丁（85.3%）。

[返回索引](#快速索引)

---

<a id="46"></a>
## 46. [JETO-Bench: A Reproducible Benchmark for Execution Time Improvement Patches in Java](http://arxiv.org/abs/2606.31767v1)

- **相关度**：0.90
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-06-30
- **arXiv ID**：2606.31767
- **作者**：Khashayar Etemadi, Zhendong Su
- **入选理由**：提出可配置的Java执行时间改进补丁基准，支持自动化与可重复评估，直接服务于LLM自动代码性能优化评估

**TL;DR**：本文提出JETO-Mine，一个可配置可重用的工具，用于自动创建Java执行时间改进补丁的可重现基准，并基于此构建了JETO-Bench（660个ETIP，91个可执行），评估发现OpenHands修复率为14.3%，同时揭示了开源Java项目缺乏性能测试的问题。

**中文摘要**：自动修复性能问题正受到越来越多的关注。然而，现有的执行时间改进补丁基准是固定的数据集，针对Python、C++或.NET，并且无法根据用户定义的配置扩展到新补丁。在本文中，我们提出了JETO-Mine，这是第一个可配置且可重用的工具，用于自动创建真实世界Java项目中执行时间改进补丁（ETIP）的可重现基准。JETO-Mine采用三阶段流水线：静态分析阶段，爬取GitHub仓库并使用用户定义的过滤器和基于LLM的问题分类器识别ETIP；动态分析阶段，将识别出的ETIP封装在Docker镜像中以实现完全可重现的执行，并进行统计测试以寻找执行时间改进的客观证据；以及评估工具，能够对生成的补丁和生成的测试进行定量评估。与现有基准不同，JETO-Mine被设计为一个可重用的工具，允许研究人员持续收集符合自身所需过滤器和统计严谨级别的新基准。我们使用JETO-Mine构建了JETO-Bench，这是一个包含660个已识别ETIP和91个手动验证的可执行ETIP的基准，这些ETIP来自174个开源Java仓库。为了构建JETO-Bench，JETO-Mine扫描了11年的开源开发历史和近180万次提交。我们在JETO-Bench中的91个手动验证的可执行ETIP上运行了OpenHands（一个领先的开源编码智能体），发现它正确修复了14.3%（13/91）的问题，这与类似研究在其他编程语言上报告的结果一致。我们的结果还揭示了开源Java项目在很大程度上缺乏展示执行时间改进的测试，这为未来在测试生成方面的研究提供了机会。

**方法**：JETO-Mine采用三阶段流水线：1) 静态分析：爬取GitHub仓库，使用用户定义过滤器和LLM问题分类器识别ETIP；2) 动态分析：将ETIP封装在Docker镜像中实现可重现执行，并进行统计测试验证执行时间改进；3) 评估工具：对生成的补丁和测试进行定量评估。

**结果**：使用JETO-Mine构建了JETO-Bench，包含660个ETIP（其中91个手动验证可执行），来自174个开源Java仓库，扫描了11年历史和近180万次提交。在91个可执行ETIP上运行OpenHands，正确修复14.3%（13/91），与类似研究结果一致。此外，发现开源Java项目普遍缺乏展示执行时间改进的测试。

[返回索引](#快速索引)

---

<a id="47"></a>
## 47. [On the Shoulders of Giants: Empowering Automated Smart Contract Auditing via the GiAnt Corpus](http://arxiv.org/abs/2606.07363v1)

- **相关度**：0.90
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-06-05
- **arXiv ID**：2606.07363
- **作者**：Xiaoting Zhang, Zhipeng Gao, Yiran Lv, Xing Hu, Feifei Niu, Xin Xia
- **入选理由**：提供智能合约自动gas优化的评测基准和数据集，直接服务于自动代码性能优化。

**TL;DR**：提出GiANT框架，从真实审计报告中自动构建高质量智能合约漏洞数据集，生成包含7,711个漏洞的GiAnt语料库，经人工评估质量极高，并基准测试了4个LLM以验证实用性。

**中文摘要**：高质量的智能合约审计数据集对于评估安全工具和推进智能合约安全研究至关重要。现有数据集的两个主要局限是人工导致的扩展瓶颈以及数据粒度和多样性的不足。为解决这些局限，我们提出了GiANT，一个自动化框架，旨在通过从现实世界的审计报告中提炼漏洞洞察来整理智能合约审计数据集。GiANT采用分治策略结合思维链技术，从Code4rena报告中提取结构化漏洞信息，随后通过LLM作为评判机制进行严格的质量保证。为评估GiANT的有效性，我们将其应用于388份真实审计报告，生成了包含五个严重级别共7,711个漏洞发现的GiAnt语料库。对数据集的人工评估展示了信息提取的卓越可靠性，平均质量得分为4.76±0.37（满分5分），评估者间一致性κ为0.88。我们进一步通过基准测试4个最先进的LLM在漏洞检测、代码摘要、缓解建议和自动Gas优化任务上的表现，验证了该数据集的实用性，建立了性能基线，从而为未来自动智能合约审计研究提供了宝贵的数据基础。

**方法**：采用分治策略和思维链技术从Code4rena报告提取结构化漏洞信息，并通过LLM作为评判机制进行质量保证。

**结果**：在388份报告上生成7,711个漏洞发现，人工评估质量得分4.76±0.37，评估者间一致性κ=0.88；基准测试4个LLM建立性能基线。

[返回索引](#快速索引)

---

<a id="48"></a>
## 48. [Chiseling Out Efficiency: Structured Skeleton Supervision for Efficient Code Generation](http://arxiv.org/abs/2606.06821v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、优化策略检索
- **收录日期**：2026-06-05
- **arXiv ID**：2606.06821
- **作者**：Yu Yu, Zhihong Sun, Jia Li, Yao Wan, Chuanyi Li, Hongyu Zhang, Ruyun Wang, Tao Huang, Zhi Jin, Ge Li, Chen Lyu
- **入选理由**：提取效率骨架提升LLM生成代码效率，语义保持并获得真实加速

**TL;DR**：提出EffiSkel框架，通过显式提取和学习效率骨架（抽象结构模式），在多任务学习中联合优化代码生成和骨架预测，显著提升LLM生成代码的效率和功能正确性。

**中文摘要**：大型语言模型（LLM）能够生成语法正确且功能完整的程序，极大地简化了软件开发。然而，近期研究表明，这些程序通常比人类优化的对应版本运行得慢得多。现有弥补这一效率差距的方法通常涉及在生成后迭代优化代码或在高效代码语料库上微调模型。然而，这些方法仅通过模仿完整的优化解决方案将效率信号暴露给模型，而没有明确编码实现高运行时性能所必需的结构性代码模式。解决这一差距存在两个核心挑战：（1）提取和表示嵌入在复杂语法和控制流中的潜在效率导向的结构模式，（2）在不破坏LLM语义训练稳定性的情况下有效学习这些模式。为应对这些挑战，我们提出EffiSkel，一种效率骨架引导框架，通过利用三种互补策略明确提取和学习效率骨架——支撑高效代码的抽象、可重用的结构模式。这些骨架被集成到一个多任务学习框架中，该框架联合优化代码生成和骨架预测。跨多种编程语言和基准的实验表明，EffiSkel显著增强了功能正确性和效率，在Mercury上使用DeepSeek-Coder（7B）时，效率比（ER）相比EffiCoder提高了+11.11%，相比CodeDPO提高了+3.71%，平均加速比（AS）相比EffiCoder提高了+0.36，相比CodeDPO提高了+0.22。这些结果凸显了显式建模效率骨架在提高LLM生成代码运行时性能方面的有效性。

**方法**：提出EffiSkel，利用三种互补策略提取效率骨架，并集成到多任务学习框架中联合优化代码生成和骨架预测。

**结果**：在Mercury上，使用DeepSeek-Coder (7B)时，ER比EffiCoder高11.11%，比CodeDPO高3.71%；AS分别高0.36和0.22。

[返回索引](#快速索引)

---

<a id="49"></a>
## 49. [Systematic LLM Translation of Legacy Scientific Code to Differentiable Frameworks: Application to a Land Surface Model](http://arxiv.org/abs/2606.07681v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-06-04
- **arXiv ID**：2606.07681
- **作者**：Aya Lahlou, Linnia Hawkins, Pierre Gentine
- **入选理由**：LLM自动翻译遗留Fortran到JAX，提升性能24倍并验证正确性

**TL;DR**：提出一个基于LLM的五阶段管道，将遗留Fortran代码自动翻译为JAX，实现可微编程，并在19,000行陆面模型上验证，取得了显著性能提升。

**中文摘要**：可微编程为科学建模提供了变革性能力，使得基于梯度的参数估计、灵敏度分析和数据同化成为可能。然而，将遗留代码库迁移到可微框架仍然是一个挑战。我们提出了一个基于LLM的五阶段代理管道，将遗留Fortran代码翻译为JAX：静态依赖分析从完整调用图确定模块翻译顺序；迭代编译-修复循环自主纠正错误；Fortran参考验证器在模块级别强制执行数值一致性，然后进行集成和梯度验证。我们在CLM-ml-v2（一个19,000行的Fortran陆面模型）上实例化并评估该管道，分析了73个模块翻译任务中的代理行为。得到的可微模型在单个反向传播中计算完整的雅可比矩阵，在八倍少于无梯度优化的步数内恢复物理参数，并且在集成规模N=2,048时比顺序Fortran实现了24倍的加速比。翻译后的模型和管道基础设施均作为可重用框架发布，用于微分其他地球系统模型组件。

**方法**：开发了一个五阶段LLM-based代理管道，包括静态依赖分析、迭代编译-修复循环以及Fortran参考验证器，实现从Fortran到JAX的自动化翻译。

**结果**：在19,000行CLM-ml-v2模型上成功翻译，得到完整可微模型，计算雅可比矩阵，参数恢复优化步数减少8倍，并行加速比达24倍。

[返回索引](#快速索引)

---

<a id="50"></a>
## 50. [CodegenBench: Can LLMs Write Efficient Code Across Architectures?](http://arxiv.org/abs/2606.04023v1)

- **相关度**：0.90
- **方向标签**：Benchmark/评测
- **收录日期**：2026-06-01
- **arXiv ID**：2606.04023
- **作者**：Jie Li, Wenzhao Wu, Junqi Hu, Qinrui Zheng, Bowen Wu, Juepeng Zheng, Yutong Lu, Haohuan Fu
- **入选理由**：专门评测LLM在多种CPU架构上生成高效并行代码能力的基准，直接服务于自动代码性能优化评估。

**TL;DR**：提出CodegenBench基准测试，评估LLMs在三种CPU架构上的并行代码生成能力，发现其在跨平台泛化上存在局限，对中等难度问题效果较好。

**中文摘要**：尽管大型语言模型（LLMs）在通用编程和GPU加速环境（如PyTorch、CUDA）的代码生成任务上已被广泛评估，但它们在面向CPU的高性能计算（HPC）中跨多种架构的能力仍未得到充分探索。为填补这一空白，我们引入了CodegenBench，一个全面的基准测试套件，旨在评估跨三个不同硬件平台（x86_64、申威和鲲鹏）的高效并行代码生成。我们的基准测试包含106个标准基本线性代数子程序（BLAS）例程作为基本基线，以及20个针对每种独特超级计算架构（LeetSunway和LeetKunpeng）适配的专业计算核心。我们的广泛评估表明，尽管最先进的LLMs能够为像x86_64这样普遍存在的架构生成优化代码，但在公共文档和训练数据有限的特定领域架构上，它们表现出显著的性能下降，凸显了跨平台泛化的关键局限性。此外，我们对影响代码质量的因素（如实现长度和任务复杂度）的分析表明，当前LLMs在需要简洁代码片段的中等难度问题上最为有效。我们开源了我们的数据集和自动评估基础设施，以促进LLM驱动的高性能代码生成的未来研究。资源可在https://anonymous.4open.science/r/CodegenBench-EDE1/ 和 https://anonymous.4open.science/r/CodegenBenchDataset-2551 获取。

**方法**：构建CodegenBench基准测试，包含106个标准BLAS例程和20个针对申威与鲲鹏架构的专业计算核心，在x86_64、申威和鲲鹏三个平台上评估LLMs的并行代码生成性能。

**结果**：LLMs在x86_64上能生成优化代码，但在申威和鲲鹏等特定领域架构上性能显著下降；且对实现长度短、复杂度中等的任务最有效。

[返回索引](#快速索引)

---

<a id="51"></a>
## 51. [Step-TP: A Grounded, Step-Level Dataset with Chain-of-Thought Reasoning for LLM-Guided Tensor Program Optimization](http://arxiv.org/abs/2605.25954v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、编译器优化、Kernel/自动调优
- **收录日期**：2026-05-25
- **arXiv ID**：2605.25954
- **作者**：Mengfan Liu, Da Zheng, Junwei Su, Chuan Wu
- **入选理由**：提供LLM引导的张量程序优化数据集，含步骤级监督和链式推理，直接服务于自动代码优化。

**TL;DR**：提出了Step-TP数据集，通过原子步骤监督和结构化CoT实现张量程序的多步优化。

**中文摘要**：尽管大语言模型（LLMs）具有强大的推理能力，但由于需要精确、可组合的变换决策，优化张量程序的执行效率仍然具有挑战性。最近的LLM引导方法将张量程序优化视为一个迭代决策过程，但现有数据集仅提供使用令牌效率低下的表示的端到端优化程序对，缺乏可验证的步骤级监督和可解释性。因此，LLM难以在大型组合优化空间中做出可靠的单步决策。我们提出了Step-TP，一个用于张量程序优化的后训练数据集，它提供基于事实的、原子级的步骤级监督，并带有结构化思维链（CoT）推理。Step-TP在中间程序状态上形成一个封闭的推理循环，实现可靠的多步优化，而不是结果模仿。其设计遵循四个原则：（i）令牌高效、可验证的中间表示（IR），可确定性地降低到TVM TIR；（ii）原子且可组合的优化策略，将复杂轨迹分解为可解释的单步决策；（iii）结构化CoT监督与显式的IR到IR状态转换相结合；（iv）策略筛选以平衡覆盖率同时防止捷径利用。数据集和实现可在GitHub链接https://github.com/LIUMENGFAN-gif/StepTP获取。

**方法**：设计了一个后训练数据集Step-TP，包含令牌高效可验证的IR、原子可组合优化策略、结构化CoT监督和策略筛选。

**结果**：发布了Step-TP数据集和实现，可在GitHub上获取。

[返回索引](#快速索引)

---

<a id="52"></a>
## 52. [CoRe-Code: Collaborative Reinforcement Learning for Code Generation](http://arxiv.org/abs/2605.24812v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、搜索与进化优化
- **收录日期**：2026-05-24
- **arXiv ID**：2605.24812
- **作者**：Zhihao Dou, Qinjian Zhao, Zhongwei Wan, Xiaoyu Xia, Sumon Biswas
- **入选理由**：多智能体协作强化学习生成代码，优化执行时间和内存效率，符合LLM自动代码优化。

**TL;DR**：CoRe-Code通过Planner-Coder范式和基于GRPO的协作感知强化学习，增强了多智能体代码生成中的角色专业化和协调，显著提升了代码准确性和效率。

**中文摘要**：大型语言模型（LLM）在代码生成方面取得了强劲的性能，但大多数方法依赖自回归解码而缺乏全局规划，常常导致局部连贯但全局次优的解决方案（例如，失败的测试用例或低效的复杂度）。虽然最近的方法如思维链（CoT）和多智能体系统（MAS）引入了规划，但其有限的角色专业化和协调阻碍了在复杂任务上的表现。为了解决多智能体代码生成中的协调和专业化挑战，我们提出了协作强化代码（CoRe-Code），一个角色专业化的LLM智能体框架，它增强了智能体间的协调以生成更准确和高效的代码。CoRe-Code采用简单的规划器-编码器范式，其中规划器生成高级计划，编码器执行计划以生成代码。我们进一步引入了一个基于组相对策略优化（GRPO）的协作感知强化学习阶段，以增强角色专业化和对齐。实验表明，CoRe-Code优于广泛的现有基于强化学习和多智能体的方法。此外，我们证明了CoRe-Code可以泛化到其他多智能体框架（例如，检索和调试智能体），凸显了其灵活性和可扩展性。我们在多个难度不同的基准上使用三个基础模型评估了CoRe-Code。与现有基线相比，结果显示在准确性上的一致改进，同时在执行时间和内存使用方面也实现了更高的效率，证明了CoRe-Code的有效性和实用性。

**方法**：提出CoRe-Code框架，采用Planner-Coder范式，Planner生成高级计划，Coder执行代码生成；并引入基于GRPO的协作感知强化学习增强角色专业化和智能体间对齐。

**结果**：在多个基准测试上，CoRe-Code超越多种RL和多智能体方法，在准确性和效率（执行时间、内存使用）上均取得一致提升，且能泛化到其他多智能体框架。

[返回索引](#快速索引)

---

<a id="53"></a>
## 53. [JEDI: Java Evaluation of Declarative and Imperative Queries](http://arxiv.org/abs/2605.23543v1)

- **相关度**：0.90
- **方向标签**：Benchmark/评测
- **收录日期**：2026-05-22
- **arXiv ID**：2605.23543
- **作者**：Filippo Schiavio, Walter Binder
- **入选理由**：Java Stream API基准套件，专门用于性能分析及优化指导

**TL;DR**：提出了JEDI基准测试套件，自动从SQL转换生成Java流和命令式实现，用于分析Stream API性能并指导优化。

**中文摘要**：Java Stream API旨在通过易于阅读的声明式语法表达计算来提高开发人员生产力。它还简化了并行计算，在常见并行化方面提供了高层抽象。不幸的是，缺乏专门针对基于流的应用程序的基准测试。这种基准测试的缺乏使得Java类库的研究人员和开发人员难以优化Stream API。此外，在没有专门基准测试的情况下，难以分析流的性能以向开发人员建议如何使用API编写高效代码。在这项工作中，我们提出了JEDI，一个针对Stream API的基准测试套件。JEDI是通过将SQL基准测试转换为Java基准测试自动生成的。我们的代码生成器支持为同一查询生成不同实现（包括基于流的和命令式的）。我们基准测试套件的最终目标——以及这项工作的主要贡献——是分析不同实现的性能，以发现低效的代码结构和更好的替代方案，向Java开发人员建议最佳实践。在我们生成的多种实现中，我们关注不同的并行化策略，并根据处理数据的特征解释最有效的并行化策略。最后，生成命令式代码的代码生成定义了一个基线，可以指导研究人员和Java实现者优化Stream API。

**方法**：通过自动转换SQL基准测试生成Java基准测试，支持多种实现（流式和命令式），分析不同并行化策略的性能。

**结果**：生成了JEDI套件，能够识别低效代码结构，解释高效的并行化策略，并提供命令式基线。

[返回索引](#快速索引)

---

<a id="54"></a>
## 54. [MileStone: A Multi-Objective Compiler Phase Ordering Framework for Graph-based IR-Level Optimization](http://arxiv.org/abs/2605.23435v1)

- **相关度**：0.90
- **方向标签**：编译器优化、搜索与进化优化
- **收录日期**：2026-05-22
- **arXiv ID**：2605.23435
- **作者**：Amirhosein Sadr, Mehran Alidoost Nia
- **入选理由**：多目标编译器阶段排序框架，使用GNN和RL，方法可迁移

**TL;DR**：MileStone是一个模块化框架，通过图神经网络和强化学习将编译器阶段排序建模为多目标优化问题，实现帕累托最优解，在相同能量预算下减少执行时间高达45%。

**中文摘要**：编译器的阶段排序对程序性能有强烈影响。找到有效的优化序列仍然是一项困难的任务，因为搜索空间很大，而执行时间、代码大小和能耗通常相互冲突。现有方法通常依赖于固定的优化级别或有限的启发式方法，并且很少同时处理多个目标。本文提出了MileStone，一个模块化框架，将编译器阶段排序建模为多目标优化问题。MileStone将程序表示为图，使用图神经网络预测性能指标，并通过遵循用户约束的强化学习代理探索优化序列。该框架还构建了一个自进化数据库，收集编译器转换并提高预测质量。在标准基准测试上的实验表明，MileStone找到了强大的帕累托最优解，比LLVM优化级别和其他相关技术更准确地满足能量限制。在相同能量预算下，MileStone使用多目标方法将执行时间减少了高达45%。结果表明，MileStone为多目标编译器阶段排序提供了一种有效且可扩展的解决方案。

**方法**：提出MileStone框架，用图神经网络预测性能，用强化学习探索优化序列，并构建自进化数据库收集转换以改善预测。

**结果**：在标准基准上，MileStone找到强帕累托最优解，比LLVM优化级别更准确满足能量限制，相同能量下执行时间减少45%。

[返回索引](#快速索引)

---

<a id="55"></a>
## 55. [Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization](http://arxiv.org/abs/2605.19782v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-05-19
- **arXiv ID**：2605.19782
- **作者**：Dmitry Redko, Albert Fazlyev, Konstantin Sozykin, Maria Ivanova, Evgeny Burnaev, Egor Shvetsov
- **入选理由**：直接研究LLM在硬件感知代码优化中的行为，包括zero-shot kernel生成和反馈循环优化，探讨预训练先验与反馈的作用，与SemOpt高度相关。

**TL;DR**：LLM在代码优化中主要依赖预训练先验，而非反馈或代理结构，实验显示其在不同场景下表现各异。

**中文摘要**：LLM发现与优化系统越来越多地应用于各个领域，它们实现了一种常见的提议-评估-修改循环。这种优化或发现过程通过对来自环境的反馈进行上下文条件化来推进。然而，随着现代LLM代理在结构上越来越复杂，评估哪些组件贡献最大，以及这种探索何时以及如何可能失败变得困难。我们通过三个受控实验来回答这些问题。我们的发现：（1）在纯黑盒优化中，LLM表现为贪婪优化器。（2）在零样本内核生成中，提供明确的输入大小信息没有可测量的效果，模型会收敛到相同的内核参数，无论大小或温度如何，就好像大小指令不可见一样。此外，当任务是为不常见的内核大小执行内核优化时，无论使用哪种语言，性能都会急剧下降。（3）在反馈循环内核优化中，CUDA在迭代反馈下单调改进，而TVM IR则主动退化，这表明当模型使用低密度语言时，内核优化会退化。我们的结果得出结论，在代码优化任务中，LLM高度依赖于预训练的先验知识，而不是提供的反馈或代理结构。

**方法**：通过三个受控实验：纯黑盒优化、零样本内核生成和反馈循环内核优化，分析LLM的行为。

**结果**：LLM在纯黑盒优化中是贪婪的；零样本内核生成对输入大小不敏感且性能随罕见大小下降；反馈循环中CUDA提升而TVM IR下降。

[返回索引](#快速索引)

---

<a id="56"></a>
## 56. [optimize_anything: A Universal API for Optimizing any Text Parameter](http://arxiv.org/abs/2605.19633v1)

- **相关度**：0.90
- **方向标签**：Kernel/自动调优
- **收录日期**：2026-05-19
- **arXiv ID**：2605.19633
- **作者**：Lakshya A Agrawal, Donghyun Lee, Shangyin Tan, Wenjie Ma, Karim Elmaaroufi, Rohit Sandadi, Sanjit A. Seshia, Koushik Sen, Dan Klein, Ion Stoica, Joseph E. Gonzalez, Omar Khattab, Alexandros G. Dimakis, Matei Zaharia
- **入选理由**：基于LLM搜索的通用文本优化，包含CUDA kernel生成与性能验证，符合自动代码优化

**TL;DR**：本文展示了一个单一的基于LLM的文本优化系统在六个不同任务上均达到最先进性能，证明其作为通用问题解决范式的有效性。

**中文摘要**：一个基于LLM的优化系统能否在根本不同的领域中匹配专业工具？我们证明，当优化问题表述为改进由评分函数评估的文本工件时，一个支持单任务搜索、跨问题迁移的多任务搜索以及泛化到未见输入的单一AI优化系统，在六个不同任务上实现了最先进的结果。我们的系统发现了使Gemini Flash的ARC-AGI准确率几乎翻三倍（从32.5%到89.5%）的智能体架构，找到了将云成本降低40%的调度算法，生成了87%匹配或超越PyTorch的CUDA内核，并超越了AlphaEvolve报告的圆填充解决方案（n=26）。跨三个领域的消融实验表明，与仅反馈分数的方案相比，附带可操作侧面信息能实现更快的收敛和更高的最终分数；在给定等效每问题预算下，多任务搜索通过跨任务迁移优于独立优化，且其收益随相关任务数量的增加而扩大。综合来看，我们首次证明基于LLM搜索的文本优化是一种通用问题解决范式，将传统上需要特定领域算法的任务统一在一个单一框架下。我们将optimize_anything开源，支持多个后端，作为GEPA项目的一部分，地址为https://github.com/gepa-ai/gepa。

**方法**：将优化问题形式化为改进由评分函数评估的文本工件，采用LLM-based搜索支持单任务、多任务（含跨问题迁移）和对未见输入的泛化；通过消融实验研究侧面信息反馈和多任务迁移的效果。

**结果**：在六个任务上取得SOTA：ARC-AGI准确率从32.5%提升至89.5%，云成本降低40%，CUDA内核87%匹配或超越PyTorch，圆填充超越AlphaEvolve；消融实验表明附带侧面信息优于仅分数反馈，多任务搜索优于独立优化且收益随相关任务数增加。

[返回索引](#快速索引)

---

<a id="57"></a>
## 57. [SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution](http://arxiv.org/abs/2605.15308v1)

- **相关度**：0.90
- **方向标签**：搜索与进化优化
- **收录日期**：2026-05-14
- **arXiv ID**：2605.15308
- **作者**：Jiachen Jiang, Huminhao Zhu, Zhihui Zhu
- **入选理由**：使用顺序蒙特卡洛和LLM驱动程序进化，提升算法效率，直接涉及程序性能优化，且方法可迁移。

**TL;DR**：SMCEvolve通过顺序蒙特卡洛将程序搜索转化为采样问题，利用三个原则性组件和复杂度分析，在多个基准上以更少LLM调用超越最先进系统。

**中文摘要**：LLM驱动的程序演化已成为自动化科学发现的强大工具，然而现有框架在设计其各个组件时缺乏原则性指导，且无法保证搜索收敛。我们提出了SMCEvolve，它将程序搜索重新定义为从奖励倾斜的目标分布中采样，并使用顺序蒙特卡洛（SMC）采样器来近似。从这个视角出发，三个核心机制作为有原则的组件出现：自适应父代重采样、混合变异与接受、自动收敛控制。我们进一步提供了有限样本复杂度分析，限定了达到目标近似误差所需的LLM调用预算。在数学、算法效率、符号回归和端到端机器学习研究基准测试中，SMCEvolve在自我决定的终止条件下使用更少的LLM调用超越了最先进的进化系统。代码可在https://github.com/kongwanbianjinyu/SMCEvolve获取。

**方法**：将程序搜索建模为从奖励倾斜分布采样，用顺序蒙特卡洛（SMC）近似，包含自适应父代重采样、混合变异与接受、自动收敛控制，并提供有限样本复杂度分析。

**结果**：在数学、算法效率、符号回归和端到端机器学习研究基准上，SMCEvolve以更少LLM调用超越最先进的进化系统。

[返回索引](#快速索引)

---

<a id="58"></a>
## 58. [A3D: Agentic AI flow for autonomous Accelerator Design](http://arxiv.org/abs/2605.15237v1)

- **相关度**：0.90
- **方向标签**：LLM/Agent 代码优化、编译器优化
- **收录日期**：2026-05-14
- **arXiv ID**：2605.15237
- **作者**：Abinand Nallathambi, Christopher Knight, Shantanu Ganguly, Wilfried Haensch, Anand Raghunathan
- **入选理由**：A3D使用智能体AI自动生成硬件加速器HLS代码，优化性能和能效

**TL;DR**：A3D是一个利用智能体AI自动完成硬件加速器设计的流程，从工作负载分析到微架构生成，无需人工干预，并在LAMMPS和QMCPACK上验证了有效性。

**中文摘要**：通过设计硬件加速器来加速应用程序可以显著提升系统性能和能效。尽管高级综合（HLS）等技术取得了进展，但为复杂应用程序设计加速器仍然高度劳动密集，需要深厚的专业知识，包括理解待加速的工作负载、硬件设计、微架构和EDA工具使用，这对应用领域专家构成了挑战。因此，大多数加速器解决方案局限于具有规则可预测数据流的应用程序。人工智能的进步使得智能体能够执行自主规划、推理、执行和反思，从而通过智能体AI实现前所未有的自动化潜力。我们提出了A3D，一种用于硬件加速器设计端到端自动化的智能体AI流程。A3D自动化了工作负载分析、性能瓶颈识别、针对HLS兼容性的代码重构以及微架构生成。A3D还通过自动探索速度-面积权衡空间来生成多样化的加速器设计。近期工作探索了将AI用于特定任务（如HLS中的设计空间探索），但仍有多个任务需要手动完成。A3D通过以下方式解决了将现代LLM应用于加速器设计中的挑战：在专家智能体之间明智地划分任务，使用专家和验证智能体编排流程循环，利用预先存在的和自定义工具，以及采用智能体RAG进行代码库和专有EDA工具文档探索。我们使用Claude Sonnet 4.5和Catapult HLS工具等商业组件实现的A3D，通过从LAMMPS（分子动力学模拟）和QMCPACK（量子化学）等复杂科学应用中无需人工干预生成加速器设计，展示了其有效性。

**方法**：A3D采用智能体AI架构，通过专家智能体分工、流程循环编排、预定义和自定义工具利用以及智能体RAG，自动化工作负载分析、性能瓶颈识别、代码重构和微架构生成，并探索速度-面积权衡。

**结果**：使用Claude Sonnet 4.5和Catapult HLS工具，A3D成功从LAMMPS和QMCPACK等复杂科学应用自动生成加速器设计，无需任何人工干预。

[返回索引](#快速索引)

---

<a id="59"></a>
## 59. [PerfCodeBench: Benchmarking LLMs for System-Level High-Performance Code Optimization](http://arxiv.org/abs/2605.15222v2)

- **相关度**：0.90
- **方向标签**：Benchmark/评测、LLM/Agent 代码优化
- **收录日期**：2026-05-13
- **arXiv ID**：2605.15222
- **作者**：Huihao Jing, Wenbin Hu, Shaojin Chen, Haochen Shi, Hanyu Yang, Sirui Zhang, Haoran Li, Yangqiu Song
- **入选理由**：提出PerfCodeBench基准，专门评测LLMs进行系统级高性能代码优化的能力，包含正确性和运行时效率指标。

**TL;DR**：提出了PerfCodeBench基准，评估LLMs在高性能代码优化方面的不足，发现与专家优化代码存在显著差距。

**中文摘要**：大型语言模型（LLMs）通常能够生成功能正确的代码，但它们在为性能关键的系统任务生成高效实现方面的能力仍然有限。现有的代码基准主要强调正确性或算法问题解决，而现实中的系统级优化仍未得到充分探索。为了填补这一空白，我们提出了PerfCodeBench，这是一个可执行的基准测试，用于评估LLMs在高性能代码优化方面的表现。这些任务需要系统级的实现选择、硬件感知优化以及对性能瓶颈的谨慎处理。每个任务都包含可执行正确性检查、基线实现和参考优化方案。这使我们能够评估正确性和面向运行时的效率。我们对一系列最先进的LLMs进行的评估显示，模型生成的代码与专家优化的实现之间存在明显差距。这种差距在涉及并行性和GPU操作的任务中尤为显著。当前的模型在跨语言鲁棒性和持续达到专家级效率方面也显示出弱点。这些结果表明，仍然需要进行性能感知评估。LLMs应该超越生成仅仅正确的代码，转向生成高效的系统软件。我们将基准数据、评估基础设施以及所有LLMs生成代码的完整日志提交到https://anonymous.4open.science/r/perfcodebench-7CDE。

**方法**：构建PerfCodeBench可执行基准，每个任务包含正确性检查、基线实现和参考优化方案，从正确性和运行时效率两方面评估LLMs生成的代码。

**结果**：在多个最先进LLMs上的评估显示，模型生成的代码与专家优化代码存在明显差距，尤其在并行和GPU任务上；同时模型在跨语言鲁棒性和达到专家级效率方面表现不佳。

[返回索引](#快速索引)

---

<a id="60"></a>
## 60. [HLS-Seek: QoR-Aware Code Generation for High-Level Synthesis via Proxy Comparative Reward Reinforcement Learning](http://arxiv.org/abs/2605.13536v1)

- **相关度**：0.90
- **方向标签**：编译器优化、Kernel/自动调优
- **收录日期**：2026-05-13
- **arXiv ID**：2605.13536
- **作者**：Qingyun Zou, Feng Yu, Hongshi Tan, Yao Chen, Bingsheng He, WengFai Wong
- **入选理由**：HLS-Seek使用强化学习优化HLS代码生成的QoR（延迟和资源），并验证性能提升。

**TL;DR**：HLS-Seek是一个QoR感知的NL-to-HLS框架，通过比较代理奖励模型和不确定性感知的MC dropout切换，在保持语法正确性的同时显著提升QoR，训练速度比传统方法快8.5倍。

**中文摘要**：高级综合（HLS）将算法性的C/C++描述编译为硬件，其结果质量（QoR）——延迟和资源利用率——关键地由pragma配置和代码结构决定。现有的基于LLM的HLS方法训练以实现功能正确性，但完全忽略QoR。我们观察到，用于HLS的强化学习（RL）不需要绝对综合结果——只需要候选之间的相对比较。基于这一见解，我们提出	extbf{HLS-Seek}，一个QoR感知的自然语言到HLS框架，用比较代理奖励模型取代昂贵的综合在环强化学习，实现了99.53%的帕累托支配准确率。为了防止奖励破解，我们引入了	extit{不确定性感知的蒙特卡洛（MC）dropout切换}，该切换对低置信度候选选择性调用真实的Vitis HLS综合并在线更新代理，形成一个自我改进的奖励系统。HLS-Seek在HLS-eval上以仅7B参数实现了81.5%的语法正确率pass@1和81.4%的Func@5，超越了GPT-5.1和其他前沿模型，同时训练速度比真实奖励RL快8.5倍。在QoR评估上，HLS-Seek在16/30个核上实现了最低延迟，并在9个核上帕累托支配了HLS特定基线。

**方法**：使用比较代理奖励模型替代昂贵的综合在环RL，并引入不确定性感知的MC dropout切换来选择性调用真实综合以更新代理，形成自改进的奖励系统。

**结果**：在HLS-eval上达到81.5%语法正确率pass@1和81.4% Func@5，训练速度比真实奖励RL快8.5倍；QoR上在16/30个核上取得最低延迟，并在9个核上帕累托支配HLS基线。

[返回索引](#快速索引)

---

<a id="61"></a>
## 61. [Kernel Foundry: A Diagnosis-driven Evolutionary Kernel Optimizer with Multi-Experts](http://arxiv.org/abs/2605.30359v1)

- **相关度**：0.90
- **方向标签**：Kernel/自动调优、编译器优化
- **收录日期**：2026-05-08
- **arXiv ID**：2605.30359
- **作者**：Zixuan Huang, Da Chen, Kecheng Huang, Lihao Yin, Xing Li, Huiling Zhen, Mingxuan Yuan, Zili Shao
- **入选理由**：诊断驱动的进化框架自动优化GPU内核，结合LLM生成与结构化反馈，验证正确性与性能提升。

**TL;DR**：Kernel Foundry是一个诊断驱动的进化框架，通过专家引导初始化、多岛进化搜索和结构化诊断反馈，自动优化GPU内核，在KernelBench上显著提升正确性和性能。

**中文摘要**：生成高性能GPU内核仍然具有挑战性，因为需要兼顾正确性和硬件感知优化。虽然大语言模型（LLM）在代码生成方面显示出潜力，但它们通常无法生成既正确又高效的内核。我们提出Kernel Foundry，一种诊断驱动的进化框架，用于自动GPU内核优化。我们的方法结合了专家引导、检索增强初始化与多岛进化搜索，其中候选内核通过结构化诊断反馈进行迭代细化。一个集中的经验库积累可重用的优化知识以指导后续进化，同时显式机制防止作弊行为绕过内核级计算。在KernelBench上的实验表明，我们的方法在正确性和性能上均持续优于强基线，在Level 2上实现了高达100%的正确性。

**方法**：结合专家引导检索增强初始化、多岛进化搜索、结构化诊断反馈迭代优化，并利用集中经验库积累知识，同时防止作弊行为。

**结果**：在KernelBench上，方法持续优于强基线，Level 2上正确率达到100%。

[返回索引](#快速索引)

---

<a id="62"></a>
## 62. [Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs](http://arxiv.org/abs/2605.03208v2)

- **相关度**：0.90
- **方向标签**：Kernel/自动调优、Profiling/程序分析
- **收录日期**：2026-05-04
- **arXiv ID**：2605.03208
- **作者**：Cole Ramos, Keith Lowery
- **入选理由**：自动GPU内核提取与隔离，支持快速迭代调优，可作为LLM驱动的内核优化基板。

**TL;DR**：Kerncap是一种自动化GPU内核提取工具，通过HSA运行时拦截和地址空间闭包，为HIP和Triton生成自包含的可重现项目，实现快速的编辑-重新编译-验证循环。

**中文摘要**：迭代式GPU内核调优受到托管内核的应用程序规模的瓶颈。快速迭代需要隔离内核以便在不重建完整应用程序的情况下进行编辑、重新编译和验证——但手动隔离需要手动重构构建标志、调度配置和运行时输入，因此开发者通常只能接受缓慢的原位编辑。我们提出了Kerncap，一种自动化内核提取工具，它在HSA运行时拦截HIP和Triton的调度，通过轻量级的Python编译钩子垫片将Triton仅JIT的元数据桥接到HSA级别的捕获中。Kerncap对所有设备内存执行地址空间闭包——一种虚拟地址保真的快照，无需DWARF元数据或指针追踪即可保留嵌入的设备指针——定位内核源代码，并生成自包含的可重现项目。HIP可重现项目使用Clang VFS覆盖来实现源代码级重新编译，而无需修改原始构建系统；Triton可重现项目则进行调优固定，将捕获的自动调优器配置绑定到工件中，以保留JIT内核的数值合同。在跨越传统HPC和ML领域的六个真实世界HIP和Triton工作负载上，针对三种AMD GPU架构（CDNA2、CDNA3、RDNA3），Kerncap从152 MB到30 GB的快照中提取并验证内核——包括通过指针间接寻址达到的vLLM的混合专家权重池的VA保真捕获。在我们的llama-cpp案例研究中，Kerncap的编辑-重新编译-验证循环相比传统工作流程实现了13.6倍的速度提升，将内核隔离从数小时的过程减少为单个命令。生成的可重现项目还作为自动调优代理和需要快速、隔离评估候选内核的LLM驱动内核生成器的基板。

**方法**：Kerncap在HSA运行时拦截HIP和Triton的调度，使用Python编译钩子垫片桥接Triton的JIT元数据，执行设备内存的地址空间闭包生成虚拟地址保真快照，定位内核源代码并生成自包含的可重现项目（HIP使用Clang VFS覆盖，Triton绑定调优配置）。

**结果**：在六种真实工作负载和三种AMD GPU架构上，Kerncap成功提取并验证了从152 MB到30 GB的快照，包括vLLM的MoE权重池；在llama-cpp案例中实现了13.6倍的加速，将内核隔离从数小时缩短为一条命令。

[返回索引](#快速索引)

---

<a id="63"></a>
## 63. [MappingEvolve: LLM-Driven Code Evolution for Technology Mapping](http://arxiv.org/abs/2604.26591v1)

- **相关度**：0.90
- **方向标签**：编译器优化
- **收录日期**：2026-04-29
- **arXiv ID**：2604.26591
- **作者**：Rongliang Fu, Yi Liu, Qiang Xu, Tsung-Yi Ho
- **入选理由**：使用LLM和分层智能体架构直接演化技术映射代码，显著提升面积缩减与整体性能，属于直接的编译器/自动化代码优化。

**TL;DR**：提出MappingEvolve框架，利用LLM和分层智能体架构直接演化技术映射代码，在面积缩减和整体性能上显著超越现有方法。

**中文摘要**：技术映射是逻辑综合中一个关键但具有挑战性的阶段。虽然大语言模型（LLMs）已被用于生成优化脚本，但其在核心算法增强方面的潜力尚未被挖掘。我们提出了MappingEvolve，一个开创性的开源框架，利用LLMs直接演化技术映射代码。我们的方法将映射过程抽象为不同的优化算子，并采用分层智能体架构，包括规划者、进化者和评估者，以指导进化搜索。这种结构化方法使得代码修改更具战略性和有效性。实验表明，我们的方法显著优于直接演化和强基线，与ABC相比实现了10.04%的面积缩减，与mockturtle相比实现了7.93%的面积缩减，在EPFL基准测试上S_overall改进达46.6%–96.0%，同时明确地权衡了面积与延迟。我们的代码和数据可在https://github.com/Flians/MappingEvolve获取。

**方法**：将技术映射过程抽象为多个优化算子，采用由规划者、进化者和评估者组成的分层智能体架构，使用LLM驱动代码的定向进化搜索。

**结果**：在EPFL基准测试上，与ABC相比面积减少10.04%，与mockturtle相比减少7.93%，S_overall改进46.6%–96.0%，并有效平衡面积与延迟。

[返回索引](#快速索引)

---

<a id="64"></a>
## 64. [LLM-Guided Strategy Synthesis for Scalable Equality Saturation](http://arxiv.org/abs/2604.17364v1)

- **相关度**：0.90
- **方向标签**：编译器优化
- **收录日期**：2026-04-19
- **arXiv ID**：2604.17364
- **作者**：Chenyun Yin, Youwei Xiao, Yuze Luo, Yuyang Zou, Yun Liang
- **入选理由**：LLM引导的等式饱和策略合成，优化编译器（e-graph）降低成本和内存使用，直接涉及自动代码/编译器优化。

**TL;DR**：EggMind是一个LLM引导的框架，通过引入领域特定语言EqSatL和智能体工作流，自动合成可重用的等式饱和策略，显著降低了成本与内存使用。

**中文摘要**：等式饱和（EqSat）是一种强大的优化范式，它通过e-graph紧凑地表示许多等价程序，并延迟提交直到提取选择最低成本的程序。因此，使EqSat有效不仅需要特定领域的重写规则，还需要特定领域的策略。如今，大部分策略设计仍然是手动的，这成为自动化基于e-graph的编译器的主要障碍。最近的规则合成框架可以从语义规范中自动推断出大量的重写词汇，但它们也扩大了重写空间并进一步加剧了e-graph爆炸。尽管大语言模型（LLM）使得自动化策略合成成为可能，但直接演化后端代码在实践中仍然无效。这种搜索缺乏可重用的策略抽象和可操作的反馈，并且很容易触发e-graph爆炸或收敛到糟糕的设计。我们提出了EggMind，一个LLM引导的、端到端的框架，用于合成可重用的EqSat策略。其核心是，EggMind引入了一种领域特定语言EqSatL，将EqSat策略表示为显式且可检查的工件。然后，它提出了一种LLM引导的智能体工作流，配备了新颖的技术，包括从证明派生的重写模式缓存和可处理性引导，以高效搜索高质量策略，同时在e-graph增长下保持合成稳定。评估表明，EggMind在向量化基准测试上显著改善了资源-质量权衡，相对于完整的EqSat，最终成本降低了45.1%，峰值RAM降低了69.1%。我们进一步展示了相同的方法论有效迁移到了基于XLA的张量编译器，并在一项具有增强重写空间的逻辑综合案例研究中展示了其实用潜力。

**方法**：提出EggMind框架，包含领域特定语言EqSatL表示策略，以及LLM引导的智能体工作流，利用证明派生的重写模式缓存和可处理性引导进行高效搜索。

**结果**：在向量化基准测试上，最终成本降低45.1%，峰值RAM降低69.1%；方法有效迁移到XLA张量编译器，并在逻辑综合案例中展示潜力。

[返回索引](#快速索引)

---

<a id="65"></a>
## 65. [Portable models as a replacement for industrial heuristics in compiler optimizations](https://arxiv.org/abs/2607.17389)

- **相关度**：0.88
- **方向标签**：编译器优化
- **收录日期**：2026-07-22
- **arXiv ID**：2607.17389
- **作者**：Fot Nikolai, Vinarsky Alexander
- **入选理由**：用可移植模型预测编译器内联决策，编译器优化且可迁移到LLM自动优化。

**TL;DR**：提出一个可移植的内联预测框架，利用生产编译器诊断作为监督，通过特征提取和模型训练，在轻量级系统中预测函数内联决策。在十五个开源C项目的评估中，CatBoost模型达到ROC-AUC 0.928和PR-AUC 0.713。

**中文摘要**：本文研究了在无法重用GCC或LLVM优化基础设施的紧凑编译器、源到源工具和解释器中预测函数内联决策的可能性。这项工作的相关性取决于需要将成熟的内联启发式方法转移到具有有限编译器基础设施、受限运行时依赖性和减少对目标特定分析访问的系统。现有的生产编译器已经包含强大的内联器，但它们的决策依赖于内部中间表示（IR）、遍序、目标模型和分析栈，这些在轻量级系统中难以复现。为了克服这些限制，我们提出了一个可移植的内联预测框架。生产编译器诊断作为监督；一个单独提取器重建调用者-被调用者调用点，准备无菌源代码片段，将它们规范化为通用AST，可选地降级为轻量级结构IR，并导出标量特征用于模型训练。因此，训练好的预测器可以作为普通C代码发出，无需编译器运行时依赖。为了评估所提出的框架，我们构建了一个数据集，包含来自十五个开源C项目的336,938个调用点，包括79,287个编译器报告的内联事件。使用项目感知验证对几个表格模型进行了比较。在留一项目验证下，CatBoost达到了ROC-AUC 0.928和PR-AUC 0.713；阈值调整后，F1从0.670提高到0.729，假阳性率从0.192下降到0.084。特征分析表明，大多数信号集中在源代码位置、显式内联意图、被调用者大小、副作用、分支和调用结构、签名形状以及调用点参数形状上。

**方法**：提出可移植的内联预测框架：使用生产编译器诊断作为监督，通过提取器重建调用点，准备无菌代码片段，规范化为通用AST，可选降级为轻量级结构IR，导出标量特征用于训练，并将预测器作为C代码输出。

**结果**：在十五个C项目的336,938个调用点数据集上，CatBoost在留一项目验证下达到ROC-AUC 0.928和PR-AUC 0.713；阈值调整后F1从0.670提升至0.729，假阳性率从0.192降至0.084。

[返回索引](#快速索引)

---

<a id="66"></a>
## 66. [QuTuner: Feature- and Learning-Guided Optimization Pass Tuning for Quantum Compilers](http://arxiv.org/abs/2607.04586v1)

- **相关度**：0.88
- **方向标签**：编译器优化
- **收录日期**：2026-07-06
- **arXiv ID**：2607.04586
- **作者**：Ming Zhong, Xiangyu Ren, Jinglei Cheng, Shaohua Li, Zhiding Liang
- **入选理由**：特征引导量子编译器优化序列调优，自动优化编译器配置，方法可迁移。

**TL;DR**：QuTuner通过结合静态电路特征和优化感知嵌入来引导量子编译器优化序列调优，显著提升指标降幅并减少调优时间。

**中文摘要**：量子编译器在将量子电路转换为更低代价、更高执行保真度的实现中起着关键作用。这一过程通常由电路级指标（如门计数和电路深度）引导。尽管编译器优化序列调优在经典编译器中已被广泛研究，但直接将这些技术迁移到量子编译器面临挑战，因为量子程序以电路形式表达，并展现出受量子特定结构塑造的优化行为。先前的量子编译器调优方法已开始使用电路特征来指导优化序列选择，但仍存在两个局限：它们仅搜索优化序列空间的一小部分，并且主要依赖静态特征，这些特征并未明确反映电路对编译器优化的响应。我们提出QuTuner，一种特征引导的量子编译器优化序列调优框架，可跨编译器和调优目标泛化。QuTuner首先构建一个大型优化数据集。然后从两个互补视角表征每个电路：描述电路结构的静态电路特征，以及总结电路对各优化序列响应的优化感知优化序列嵌入。利用这些表示，QuTuner训练两个离线模型来对未见电路检索和排序候选优化序列，随后进行轻量级优化。我们在Qiskit和PyTKET上使用两个基准套件评估QuTuner。在Qiskit上，QuTuner比最强基线最多提升84.85%的评估指标降幅，同时减少73.59%的调优时间。在PyTKET上，它最多提升18.68%的指标降幅，并减少64.49%的调优时间。这些结果表明QuTuner为量子编译器提供了一种有效的自适应优化序列调优方法。

**方法**：构建大型优化数据集，从静态电路特征和优化感知嵌入两个视角表征电路，训练离线模型检索和排序候选优化序列，再轻量级微调。

**结果**：在Qiskit上指标降幅提升84.85%，调优时间减少73.59%；在PyTKET上指标降幅提升18.68%，调优时间减少64.49%。

[返回索引](#快速索引)

---

<a id="67"></a>
## 67. [SkelDPO: A Skeleton-Guided Direct Preference Optimization Framework for Efficient Code Generation](http://arxiv.org/abs/2606.06826v1)

- **相关度**：0.88
- **方向标签**：LLM/Agent 代码优化、优化策略检索
- **收录日期**：2026-06-05
- **arXiv ID**：2606.06826
- **作者**：Yu Yu, Chen Lyu
- **入选理由**：骨架引导偏好优化提升代码生成效率，联合优化语义和效率

**TL;DR**：提出SkelDPO框架，通过骨架引导的偏好优化提升代码生成效率，在多项指标上超越现有方法。

**中文摘要**：随着代码大型语言模型（Code LLMs）在语义正确性方面取得显著进展，执行效率已成为评估其实用性的越来越重要的维度。然而，现有方法通常将完整程序作为训练期间的单一优化目标，而没有显式建模影响效率的结构因素。因此，尽管这些模型能够生成语义正确的代码，但它们无法在细粒度层面上学习导致高效实现的底层骨架特征。为了解决这一局限性，我们提出了SkelDPO（骨架引导的直接偏好优化），一种骨架引导的偏好优化框架，系统地提升代码生成的效率。SkelDPO首先从代码数据集中识别高效和低效的实现，并通过比较分析定位它们的效率倾向点和低效倾向点，形成高效骨架与低效骨架之间的对齐信号。在训练过程中，引入了联合代码和骨架偏好损失，使模型在学习语义正确性的同时，强化其对代码中效率关键组件的理解。结果表明，SkelDPO持续超越现有方法：与仅依赖高效和低效代码偏好优化的SOTA方法相比，它在Pass@1、Beyond@1和Effi@1上分别提升了3-6%、3-7%和2-5%，在复杂任务上提升更为显著。总体而言，SkelDPO为骨架级效率对齐提供了新视角，突破了传统偏好优化仅依赖正确性或效率对的限制。所有数据集和源代码已在https://github.com/icpcSkelDPO/SkelDPO公开提供。

**方法**：SkelDPO：从数据集中识别高效/低效实现，通过比较定位效率关键点；引入联合代码和骨架偏好损失进行训练，同时学习语义正确性和效率结构。

**结果**：在Pass@1、Beyond@1、Effi@1上分别比SOTA提升3-6%、3-7%、2-5%，复杂任务提升更显著。

[返回索引](#快速索引)

---

<a id="68"></a>
## 68. [Lean Refactor: Multi-Objective Controllable Proof Optimization via Agentic Strategy Search](http://arxiv.org/abs/2605.20244v1)

- **相关度**：0.88
- **方向标签**：LLM/Agent 代码优化、优化策略检索、编译器优化
- **收录日期**：2026-05-18
- **arXiv ID**：2605.20244
- **作者**：Jialin Lu, Soonho Kong, Rodrigo Stehling, Kaiyu Yang, Zhangyang Wang, Weiran Sun, Wuyang Chen
- **入选理由**：使用检索增强agent自动重构Lean证明以压缩长度和减少编译时间，属于LLM自动修改代码提升性能。

**TL;DR**：Lean Refactor是一个检索增强的智能体框架，通过检索多目标重构策略实现对Lean证明的高效压缩和版本鲁棒重构。

**中文摘要**：我们提出了Lean Refactor，一个即插即用的检索增强智能体框架，用于Lean证明的多目标、可控、版本鲁棒的重构。LLM生成的证明以其正确但冗长且跨库版本脆弱而闻名，然而现有的重构工作忽略了三个实际挑战：1）Lean重构本质上是多目标（证明长度、编译成本和版本兼容性常常相互冲突）；2）Lean仓库具有脆弱的兼容性，而LLM发布对Lean/Mathlib版本一无所知；3）基于训练的流水线需要随着每个新LLM的发布而反复微调，既无法随模型更迭扩展，也无法适应Lean的发布周期。Lean Refactor通过从精心策划的多目标重构策略数据库中检索来引导一个冻结的智能体LLM，每个策略都密集地注释有元数据，如支持的Lean/Mathlib版本和预期的编译成本降低。实验显示，在竞赛基准上实现了超过70%的token级压缩，在研究仓库上超过20%，编译时间减少高达60%，优于先前的工作和Claude Code。版本过滤检索进一步改善了目标Lean版本上的压缩，并且重构后的miniF2F证明在向未来Lean版本的零样本迁移中表现出比未重构版本更强的性能。

**方法**：提出Lean Refactor，使用冻结的智能体LLM，从精心策划的多目标重构策略数据库中检索，每个策略带有版本和编译成本等元数据，指导重构。

**结果**：在竞赛基准上token压缩超70%，研究仓库超20%，编译时间减少高达60%；版本过滤检索进一步提升目标版本压缩；重构后的证明在未来版本上零样本迁移更强。

[返回索引](#快速索引)

---

<a id="69"></a>
## 69. [SeaEvo: Advancing Algorithm Discovery with Strategy Space Evolution](http://arxiv.org/abs/2604.24372v2)

- **相关度**：0.88
- **方向标签**：搜索与进化优化、LLM/Agent 代码优化
- **收录日期**：2026-04-27
- **arXiv ID**：2604.24372
- **作者**：Sichun Luo, Yi Huang, Haochen Luo, Fengyuan Liu, Guanzhi Deng, Lei Li, Qinghua Yao, Zefa Hu, Junlan Feng, Qi Liu
- **入选理由**：利用自然语言策略改进LLM引导进化搜索，应用于系统优化并可直接迁移至自动代码性能优化

**TL;DR**：通过引入持久化自然语言策略作为种群级状态，提高了LLM引导进化搜索的效果，在多个基准上取得平均20.6%的相对改进。

**中文摘要**：大型语言模型（LLM）引导的进化搜索越来越多地被用于自动化算法发现，然而大多数当前方法主要通过可执行程序和标量适应度来跟踪搜索进度。即使通过启发式描述或反思使用自然语言推理，它通常仍然是短暂的变异上下文或非结构化记忆，而不是作为持久化的种群级状态组织成战略方向。因此，进化搜索可能难以区分同一想法的语法不同实现，保留低适应度但具有战略前景的方向，或检测整个策略家族何时已经饱和。我们引入了\model，一个模块化的策略空间层，它将语言级战略推理转化为LLM驱动程序搜索中的一级种群级进化状态。\model为每个候选程序表示一个明确的自然语言策略，通过策略语义对档案进行聚类，检索行为上互补的灵感，并定期导航策略景观以避免饱和方向。在不修改底层进化算法的情况下，\model在大多数设置中改进了算法发现、系统优化和智能体框架设计任务中的现有进化骨架。在四个系统基准测试中，\model实现了20.6%的平均相对改进，Prism上的最佳单次运行得分高出3倍。这些结果表明，持久策略表示为提高LLM引导进化搜索的有效性和成本效益提供了一种实用机制，指向复合AI系统，其搜索能力受益于算法策略的结构化积累和重用。

**方法**：提出\model，一个模块化策略空间层，将每个候选程序关联一个自然语言策略，按策略语义聚类，检索互补灵感，并定期导航策略景观以避免饱和方向。

**结果**：在算法发现、系统优化和智能体框架设计任务中，在大多数设置下改进了现有进化骨架；四个系统基准平均相对改进20.6%，Prism最佳单次运行得分高3倍。

[返回索引](#快速索引)

---

<a id="70"></a>
## 70. [When to Use Which? Benchmarking Optimisers for Configurable Systems under Varying Budgets](https://arxiv.org/abs/2607.16476)

- **相关度**：0.85
- **方向标签**：Kernel/自动调优
- **收录日期**：2026-07-22
- **arXiv ID**：2607.16476
- **作者**：Chao Jiang, Yulong Ye, Tao Chen, Miqing Li
- **入选理由**：系统配置调优优化器比较，自动优化程序性能，方法可迁移

**TL;DR**：比较了不同预算下多种优化器的性能，发现FLASH优化器在各种预算下表现稳定。

**中文摘要**：软件配置调优对于优化系统性能至关重要，过去十年中出现了各种优化器。然而，调优过程中所需的时间可能因系统而异。在某些系统（例如PostgreSQL）中，测量一个配置可能需要几分钟，而在其他系统（例如MariaDB）中，可能需要几个小时。此外，即使在同一系统中，用户可能有不同的预算和偏好设置。这自然引出了一个问题——在给定的预算水平下，哪个优化器是软件工程从业者的最佳选择？这很重要，因为优化器通常有自己的“舒适区”，并且在不同的预算下表现可能非常不同。在本文中，我们旨在回答这个问题。我们系统地评估了八种成熟的优化器在22个可配置系统上不同预算水平下的表现。我们发现，不出所料，基于模型的优化器（例如SMAC）在预算紧张时表现良好，而无需模型的优化器（例如遗传算法）在预算充足时表现更优。然而，有趣的是，有一种优化器FLASH在大多数系统上无论预算多少都表现一致良好。最后，我们研究了这种现象的原因，发现许多系统拥有良好的局部最优（具有大的吸引域），使得贪婪优化器（例如FLASH）能够实现强性能。本工作的源代码、数据和补充材料可在https://anonymous.4open.science/r/Config-W2W-98B2获取。

**方法**：系统评估8种优化器在22个系统上不同预算水平的表现。

**结果**：基于模型的优化器在紧预算下好，无模型在宽松预算下好，但FLASH始终表现好。

[返回索引](#快速索引)

---

<a id="71"></a>
## 71. [What Do AI Agents Actually Change? An Empirical Taxonomy of Mutation Patterns in Performance-Improving Pull Requests](http://arxiv.org/abs/2607.05666v1)

- **相关度**：0.85
- **方向标签**：优化策略检索、Benchmark/评测
- **收录日期**：2026-07-06
- **arXiv ID**：2607.05666
- **作者**：Illia Dovhoshliubnyi, Nima Soroush, Ashkan Sami, Alexander Brownlee
- **入选理由**：分析AI代理性能优化PR的突变模式，揭示优化策略分布，与优化策略挖掘与检索密切相关

**TL;DR**：本文分析AI编码代理的性能优化PR，发现其突变操作符分布与传统遗传改进语料库显著不同，且代理身份和目标策略可缩小SBSE算子空间。

**中文摘要**：AI编码代理是黑盒：我们无法检查它们如何生成代码，但可以检查它们更改了什么。这一区别对于基于搜索的软件工程（SBSE）非常重要，其中诸如遗传改进（在我们研究的性能优化应用中）等技术依赖于反映代码实际转换方式的突变算子。在AIDev-pop中，33,596个代理PR中不到1%针对性能，使得每个案例成为进入原本不透明的代理行为的罕见窗口。我们使用双LLM交集管道，将来自216个这些PR的1,254个与性能相关的差异块（跨越五个代理系统）与Even-Mendoza等人（2025）的18类语法突变分类法进行分类。三个类别占主导地位：名称修改（37.0%）、对象创建（26.4%）和类型更改（22.7%），这一分布与之前的遗传改进语料库显著不同，后者中无变化占84%。每个代理部署的系统承诺一种独特的突变词汇，每个性能策略激活一个大多不相交的类别子集。因此，代理身份和目标策略是有信息量的先验，缩小了有效的SBSE算子空间。复制包：https://github.com/5uper6rain/ssbse-challenge-2026

**方法**：从AIDev-pop数据集中的33,596个PR中筛选出216个性能相关PR，提取1,254个差异块，使用Even-Mendoza等人（2025）的18类语法突变分类法，通过双LLM交集管道进行分类。

**结果**：三个类别占主导：名称修改（37.0%）、对象创建（26.4%）、类型更改（22.7%），与之前GI语料库（无变化占84%）显著不同；每个代理有独特突变词汇，性能策略激活几乎不相交的类别子集。

[返回索引](#快速索引)

---

<a id="72"></a>
## 72. [A Multi-Dimensional, Per-Pass Empirical Study of the LLVM Optimization Pipeline](http://arxiv.org/abs/2606.31238v1)

- **相关度**：0.85
- **方向标签**：编译器优化、Benchmark/评测
- **收录日期**：2026-06-30
- **arXiv ID**：2606.31238
- **作者**：Federico Bruzzone, Walter Cazzola
- **入选理由**：对LLVM优化流水线的实证分析，提供编译器优化行为洞察，可服务于自动优化决策。

**TL;DR**：本文通过对LLVM -O3流水线的大规模测量，揭示了其非单调性和后加载特性，发现少数pass主导性能提升，并指出IR指令数不可靠等关键发现，为编译器优化提供了指导。

**中文摘要**：量化单个优化pass的边际影响是阶段排序、pass选择、优化设计以及pass/硬件交互分析的基础。在LLVM（通过MLIR作为C/C++、Rust和ML栈的标准后端）中，优化pass之间的交互、测量噪声和流水线规模使得这一任务变得困难。我们提出了对LLVM -O3优化流水线的系统性实证研究。我们将流水线分解为累积的逐pass前缀。然后，我们在84,750次测量中测量了执行时间、编译时间、二进制大小、硬件计数器和RAPL能量，这些测量覆盖了在30个PolyBench/C内核上评估的-O3流水线的113个累积前缀，并严格进行了噪声抑制。在这些计算密集型的仿射内核上，流水线是非单调的（6.6-9.7%的转变出现回归），并且严重后加载（中位数非回归内核需要84.8%的流水线才能获得80%的加速）。大多数收益是由一个小的Pareto主导的pass核心驱动的，而最终的-O3配置在（大小，加速）上对于30个内核中的29个是Pareto被支配的。我们进一步表明，IR指令数不是运行时的可靠预测指标，运行时导向的pass实际上也是能量导向的（节省30-60%），并且由于阶段干扰导致的损失的无搜索理想可加性上限是46.35%。这些发现使得更明智的pass剪枝、成本模型校准和自动调优成为可能。

**方法**：将LLVM -O3流水线分解为累积前缀，在30个PolyBench/C内核上测量执行时间、编译时间、二进制大小、硬件计数器和RAPL能量，共84,750次测量，并严格抑制噪声。

**结果**：流水线非单调（6.6-9.7%过渡出现回归），中位数内核需要84.8%的流水线才能获得80%的加速；少数Pareto主导pass贡献大部分收益，最终-O3配置在29/30内核上Pareto被支配；IR指令数不可预测运行时，运行时pass实际节能30-60%，阶段干扰损失上限46.35%。

[返回索引](#快速索引)

---

<a id="73"></a>
## 73. [SOLAR: AI-Powered Speed-of-Light Performance Analysis](http://arxiv.org/abs/2606.26383v1)

- **相关度**：0.85
- **方向标签**：Profiling/程序分析
- **收录日期**：2026-06-24
- **arXiv ID**：2606.26383
- **作者**：Qijing Huang, Sana Damani, Zhifan Ye, Athinagoras Skiadopoulos, Siva Kumar Sastry Hari, Jason Clemons, Sahil Modi, Jingquan Wang, Aditya Kane, Edward C Lin, Humphrey Shi, Christos Kozyrakis
- **入选理由**：自动从PyTorch/JAX代码推导和验证speed-of-light性能界限，为LLM驱动的代码优化提供关键性能分析和优化机会识别。

**TL;DR**：提出SOLAR框架，自动从PyTorch/JAX代码推导经过验证的Speed-of-Light界限，支持多保真度分析和优化洞察。

**中文摘要**：深度学习模型在目标硬件上能跑多快？当前的实现距离该极限还有多远？这些问题对软件、硬件和算法优化至关重要。光速（Speed-of-Light, SOL）分析通过计算工作负载在给定架构上的理论最小执行时间来回答它们。然而，推导SOL界限仍然是手动的、易出错的，并且与快速的模型开发脱节。为了填补这一空白，我们引入了SOLAR，这是一个从PyTorch和JAX源代码自动推导出经过验证的SOL界限的框架。SOLAR在其流程中利用了生成式和确定性组件：一个LLM前端将任何源程序转换为可执行的仿射循环IR（Affine Loop IR），并通过输出比较进行验证；一个确定性流程将IR提升为einsum图；以及一个分析后端计算未融合、融合和缓存感知的SOL界限。SOLAR提供了全面的算子和语言覆盖，产生了零观察到SOL违规的验证界限，并提供了多保真度分析，以收紧界限并揭示优化见解。我们在KernelBench、JAX/Flax模型和机器人工作负载上评估了SOLAR。这些实验展示了四个用例：多保真度级别的余量分析、识别优化机会、跨平台探索以及反向屋顶线硬件配置。

**方法**：使用LLM前端将源码转为仿射循环IR，经确定性流程提升为einsum图，再由分析后端计算未融合、融合和缓存感知的SOL界限。

**结果**：零SOL违规的验证界限，多保真度分析，在KernelBench、JAX/Flax模型和机器人工作负载上展示四个用例。

[返回索引](#快速索引)

---

<a id="74"></a>
## 74. [Source-Free Detection and Impact Analysis of Compiler Optimization Problems in Mobile Applications](http://arxiv.org/abs/2606.23512v1)

- **相关度**：0.85
- **方向标签**：Profiling/程序分析
- **收录日期**：2026-06-22
- **arXiv ID**：2606.23512
- **作者**：Han Hu, Xiaoheng Xie, Bo Sun, Jian Gu, Gang Fan, Li Li
- **入选理由**：从二进制检测编译优化问题的静态分析框架，可直接服务于自动优化的热点定位。

**TL;DR**：提出OptDetect框架，通过分析二进制文件检测低优化级别编译的原生库，发现30.5%的库存在该问题，修复后可显著提升性能。

**中文摘要**：移动应用程序经常遭受性能问题，例如帧率下降、过热和过高的功耗。虽然开发者优化算法和调试代码，但一个关键的瓶颈往往被忽视：以低优化级别（O0/O1而非O2/O3）编译的原生库。由于这些库在功能上无错误地执行，由此产生的性能下降在生产应用程序中仍然隐藏，影响数百万用户。我们提出	extsc{OptDetect}，一个无源码框架，可直接从应用程序二进制文件检测编译器优化问题，无需源代码或构建元数据。	extsc{OptDetect}通过二进制反汇编、块级分类和加权得分聚合的流水线处理单个二进制文件中的混合优化级别，在受控数据集上达到93.0%的准确率，在真实数据集上达到81.9%的准确率。将	extsc{OptDetect}应用于来自830个顶级Google Play应用的21,972个原生库，我们发现30.5%的库使用低优化级别，影响91.7%的应用。通过对12个生产应用（6个商业，6个开源）的案例研究，我们证明修复检测到的问题可将商业应用的CPU指令减少10-63%（中位数：20.5%），开源应用减少15-58%（中位数：32%），性能投诉中位数减少42%，评分中位数增加0.14分。进一步调查揭示了一个先前被忽视的根本原因：广泛使用的第三方库本身以低优化级别分发，在一个主要仓库的1,073个库中有49.7%存在此问题。这些发现凸显了自动化检测工具和行业级优化标准的必要性。

**方法**：提出OptDetect框架，通过二进制反汇编、块级分类和加权得分聚合，无需源码即可检测二进制文件中的编译器优化级别问题。

**结果**：在受控和真实数据集上分别达到93.0%和81.9%准确率；对21972个库检测发现30.5%使用低优化；修复后CPU指令减少10-63%，性能投诉减少42%，评分提升0.14。

[返回索引](#快速索引)

---

<a id="75"></a>
## 75. [CodeGolf Bench: A Multi-Language Benchmark for Evaluating Concise Code Generation Capabilities of Large Language Models](http://arxiv.org/abs/2605.30394v1)

- **相关度**：0.85
- **方向标签**：Benchmark/评测
- **收录日期**：2026-05-28
- **arXiv ID**：2605.30394
- **作者**：Vedant Padwal
- **入选理由**：提出CodeGolf Bench基准，评估LLM在60种编程语言中生成简洁代码的能力，简洁代码对应于代码尺寸优化，属于自动代码优化领域的基准测试。

**TL;DR**：提出了CodeGolf Bench基准，用于评估LLM在60种语言中的简洁代码生成能力，发现推理模型显著优于非推理模型。

**中文摘要**：本文介绍了CodeBench，一个能够评估大型语言模型在60种编程语言中生成简洁代码能力的基准测试。基于代码高尔夫（一种追求最短字符或字节解决方案的娱乐编程竞赛），该基准测试为衡量LLM生成高效、简洁代码的能力提供了独特的度量标准。与受限于固定问题集和语言覆盖范围的现有基准不同，CodeGolf Bench利用code.golf平台提供新问题以及实时的人类表现基线。对9个LLM在Python和C++任务上的评估表明，推理模型显著优于非推理模型，最佳平均百分位达到70.97%。这一性能差距在C++中尤为显著，凸显了推理对于语法要求严格的语言的重要性。非推理模型在两种语言上的效率优化方面表现更差，其最佳百分位远低于推理模型。CodeGolf Bench提供了一个动态框架，用于根据代码高尔夫中不断进化的人类表现来评估LLM的代码生成能力。

**方法**：基于code.golf平台构建基准，包含60种编程语言的代码高尔夫问题，并提供实时人类表现基线；对9个LLM在Python和C++任务上评估推理与非推理模型。

**结果**：推理模型最佳平均百分位达70.97%，非推理模型远低于此；差距在C++中更明显。

[返回索引](#快速索引)

---

<a id="76"></a>
## 76. [Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization](http://arxiv.org/abs/2607.13184v1)

- **相关度**：0.84
- **方向标签**：Profiling/程序分析
- **收录日期**：2026-07-14
- **arXiv ID**：2607.13184
- **作者**：Saber Ganjisaffar, Chengyu Song, Nael Abu-Ghazaleh
- **入选理由**：提出Microflow微架构因果可观测性框架，能够自动归因性能瓶颈，直接服务于自动代码优化的热点定位与性能分析。

**TL;DR**：Microflow是一个可观察性框架，通过中间表示MFIR捕获微架构事件因果关系，实现精确停顿归因和关键路径分解，揭示了SPEC CPU 2017中的隐藏瓶颈。

**中文摘要**：现有的架构模拟器暴露聚合指标或原始跟踪，但未能揭示微架构事件之间的复杂交互及其与程序执行的关系。因此，架构师观察到性能症状，但无法系统地将其归因于跨抽象层的根本原因。本文介绍了Microflow，一个将因果关系提升为一级分析对象的可观察性框架。Microflow将执行跟踪转换为Microflow中间表示（MFIR），明确捕获软件语义、指令、微架构事件和硬件资源之间的依赖关系。通过统一这些元素，MFIR能够直接从观察到的停顿遍历到其根本原因，为自动根本原因分析铺平了道路。Microflow精确地归因停顿，揭示不可观察的现象，并通过反事实分析实现精确的关键路径分解。这些能力允许对现有工具不透明的复杂硬件-软件交互进行系统推理。通过使因果关系可查询，Microflow为性能分析和硬件-软件协同设计提供了坚实基础。我们在两个SPEC CPU 2017基准测试上演示了它，揭示了从聚合症状中不可见的瓶颈：leela中隐藏的误预测成本和mcf中的跨循环迭代争用。

**方法**：Microflow将执行跟踪转换为MFIR，明确捕获软件语义、指令、微架构事件和硬件资源之间的依赖关系，通过反事实分析实现停顿归因和关键路径分解。

**结果**：在SPEC CPU 2017基准测试中，Microflow发现了隐藏的误预测成本（leela）和跨循环迭代争用（mcf）等不可见瓶颈。

[返回索引](#快速索引)

---
