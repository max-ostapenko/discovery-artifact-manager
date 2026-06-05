---
date: 2026-06-05
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-05  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, a new Exa.ai grounding tool, and expanded high-performance storage options with Hyperdisk support.

## Details

The video generation surface (Veo) sees significant experimental additions in `CloudAiLargeModelsVisionGenerateVideoExperiments`, including `seamless` looping, spatial tessellation, and support for the `VIDEO_CODEC_DNXHR` codec. For RAG workflows, a new `exaAiSearch` tool has been added to `GoogleCloudAiplatformV1Tool`, allowing developers to ground model responses using Exa.ai. Infrastructure-wise, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Throughput, Extreme), and `ReasoningEngines` memories now explicitly mark `scope` and `memory_type` as immutable during patch operations.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
