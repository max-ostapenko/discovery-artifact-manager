---
date: 2026-06-06
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Features"
impact: high
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 8
---

# Exa.ai Grounding and Advanced Video Generation Features

**Date:** 2026-06-06  
**API:** `aiplatform.v1`  
**Impact:** High  

## Summary

Vertex AI introduces Exa.ai search integration for model grounding and a suite of experimental video generation features including seamless looping and DNxHR support.

## Details

This update brings significant new capabilities to the Vertex AI platform. Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using Exa.ai. The video generation suite (`CloudAiLargeModelsVisionGenerateVideoExperiments`) has been expanded with `seamless` parameters for temporal looping and spatial tessellation, support for the `VIDEO_CODEC_DNXHR` codec, and an `anchorLastFrame` option. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Throughput, Balanced HA), and documentation across several resources now refers to the 'Agent Platform' alongside Vertex AI.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Storage`
