---
date: 2026-06-11
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Controls"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation Controls

**Date:** 2026-06-11  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding for models and significant new parameters for experimental video generation, including seamless looping and Hyperdisk support.

## Details

Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using Exa.ai search results. The video generation suite (`CloudAiLargeModelsVisionGenerateVideoExperiments`) has been expanded with a `seamless` object for creating loopable or tessellated videos, an `anchorLastFrame` option, and support for the `VIDEO_CODEC_DNXHR` codec. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (Balanced, Extreme, ML, Throughput), and documentation across several resources has been updated to reflect a shift toward the 'Agent Platform' terminology.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
