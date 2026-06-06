---
date: 2026-06-06
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and advanced video generation"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and advanced video generation

**Date:** 2026-06-06  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a grounding tool, expands experimental video generation with looping and tessellation, and adds Hyperdisk support for high-performance storage.

## Details

A new `GoogleCloudAiplatformV1ToolExaAiSearch` tool has been added, allowing developers to ground model responses using Exa.ai search results via an API key. The video generation suite (`CloudAiLargeModelsVisionGenerateVideoExperiments`) sees significant updates including a `seamless` object for temporal looping and spatial tessellation, support for the `VIDEO_CODEC_DNXHR` codec, and an `anchorLastFrame` option. Infrastructure-wise, `PersistentDiskSpec` now supports various Hyperdisk types (Balanced, Extreme, ML, Throughput), and `reasoningEngines.memories.patch` now explicitly marks `scope` and `memory_type` as immutable fields.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Storage`
