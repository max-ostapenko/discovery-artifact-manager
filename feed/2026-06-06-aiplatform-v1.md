---
date: 2026-06-06
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Experiments and Exa.ai Grounding"
impact: high
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Veo Video Experiments and Exa.ai Grounding

**Date:** 2026-06-06  
**API:** `aiplatform.v1`  
**Impact:** High  

## Summary

Vertex AI introduces advanced video generation controls including seamless looping and tessellation, alongside a new Exa.ai search tool for model grounding.

## Details

The API adds significant experimental capabilities for video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including `seamless` video (looping and spatial tessellation), `anchorLastFrame` for custom border masks, and support for the `VIDEO_CODEC_DNXHR` codec. For RAG and grounding workflows, a new `exaAiSearch` tool is available in the `Tool` schema, allowing models to query Exa.ai directly. Infrastructure-wise, `PersistentDiskSpec` now supports Hyperdisk types (Balanced, Extreme, ML, Throughput), and `reasoningEngines.memories.patch` clarifies that `scope` and `memory_type` are immutable fields.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
