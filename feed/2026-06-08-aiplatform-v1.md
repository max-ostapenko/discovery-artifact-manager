---
date: 2026-06-08
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Experiments and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo Video Experiments and Exa.ai Grounding

**Date:** 2026-06-08  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and professional codecs, alongside a new built-in tool for Exa.ai search grounding.

## Details

The API adds significant experimental capabilities for video generation via CloudAiLargeModelsVisionGenerateVideoExperiments, including support for the VIDEO_CODEC_DNXHR codec, temporal looping, and spatial tessellation (horizontal/vertical). A new GoogleCloudAiplatformV1ToolExaAiSearch tool has been added to the Tool schema, allowing models to ground responses using Exa.ai search results. Additionally, PersistentDiskSpec now supports several Hyperdisk types (ML, Balanced, Throughput), and reasoningEngines.memories.patch now explicitly defines scope and memory_type as immutable fields. Note the documentation shift in several schemas from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
