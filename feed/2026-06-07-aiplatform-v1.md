---
date: 2026-06-07
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Experiments and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Veo Video Experiments and Exa.ai Grounding

**Date:** 2026-06-07  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for experimental models, a new Exa.ai search tool for model grounding, and expanded Hyperdisk storage support.

## Details

The API adds significant surface area for video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including support for seamless looping, spatial tessellation (horizontal/vertical), and the `VIDEO_CODEC_DNXHR` codec. A new `exaAiSearch` tool has been added to the `Tool` schema, allowing developers to ground model responses using Exa.ai. Additionally, `PersistentDiskSpec` now supports high-performance Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`. Note that documentation now frequently refers to the service as 'Agent Platform' in resource descriptions.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
