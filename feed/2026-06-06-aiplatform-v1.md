---
date: 2026-06-06
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Advanced Video Generation"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Exa.ai Grounding and Advanced Video Generation

**Date:** 2026-06-06  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its generative capabilities with Exa.ai search grounding and advanced video generation features like seamless looping, while also adding Hyperdisk support for high-performance ML infrastructure.

## Details

This update introduces the `GoogleCloudAiplatformV1ToolExaAiSearch` tool, allowing developers to ground model responses using Exa.ai search results. The video generation suite (`CloudAiLargeModelsVisionGenerateVideoExperiments`) receives significant experimental upgrades, including `seamless` parameters for temporal looping and spatial tessellation, an `anchorLastFrame` option, and support for the `VIDEO_CODEC_DNXHR` codec. Infrastructure-wise, `PersistentDiskSpec` now supports various Hyperdisk types (Balanced, Extreme, ML, Throughput), and `reasoningEngines.memories.patch` now explicitly flags `scope` and `memory_type` as immutable. Notably, documentation strings are shifting terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
