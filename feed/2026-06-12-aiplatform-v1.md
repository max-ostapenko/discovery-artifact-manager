---
date: 2026-06-12
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video looping and Exa.ai grounding"
impact: high
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 8
---

# Vertex AI adds Veo video looping and Exa.ai grounding

**Date:** 2026-06-12  
**API:** `aiplatform.v1`  
**Impact:** High  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new grounding tool via Exa.ai and expanded Hyperdisk storage options.

## Details

The video generation suite (Veo) receives significant experimental updates in `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding `seamless` parameters for temporal looping and spatial tessellation, plus an `anchorLastFrame` option. For RAG and grounding workflows, a new `exaAiSearch` tool has been added to `GoogleCloudAiplatformV1Tool`, requiring an API key to leverage Exa.ai for model responses. Infrastructure-wise, `PersistentDiskSpec` now supports multiple Hyperdisk types (Balanced, Extreme, ML, Throughput), and `reasoningEngines.memories.patch` now explicitly flags `scope` and `memory_type` as immutable fields.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Storage`
