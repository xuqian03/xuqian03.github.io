---
title: "Light Field Referring Segmentation: A Benchmark and an LLM-Based Approach"
collection: publications
category: manuscripts
permalink: /publication/2026-03-01-light-field-referring-segmentation
excerpt: 'We introduce the first light-field referring segmentation benchmark and LFLLM, an LLM-based framework for multimodal light-field referring segmentation.'
date: 2026-03-01
venue: 'IEEE Transactions on Broadcasting'
paperurl: 'https://doi.org/10.1109/TBC.2026.3659013'
citation: 'Tian, S., Xu, Q., Gui, H., Su, T., Li, Y., &amp; Wang, Q. (2026). &quot;Light Field Referring Segmentation: A Benchmark and an LLM-Based Approach.&quot; <i>IEEE Transactions on Broadcasting</i>, 72(1), 361–372.'
---

Referring image segmentation (RIS) requires models to segment objects from natural language descriptions. Existing RIS models have limited leverage of geometric information, which often leads to a mismatch between language and vision.

This paper presents the first light-field referring segmentation dataset with rich occlusions and depth-referring descriptions, benchmarks 2D RIS methods on the dataset, and proposes LFLLM. LFLLM includes a Center Angular Aggregation Module that warps adjacent views to the central view and a Depth Convergence Module that injects a depth token into large language models.

Paper: [IEEE TBC](https://doi.org/10.1109/TBC.2026.3659013)  
Code: [LFLLM-TBC2026](https://github.com/ShishunTian/LFLLM-TBC2026)
