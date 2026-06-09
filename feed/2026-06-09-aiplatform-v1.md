---
date: 2026-06-09
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Controls"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Vertex AI", "Video", "Storage"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation Controls

**Date:** 2026-06-09  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding, advanced video generation features like seamless looping, and expanded Hyperdisk storage options.

## Details

A new `exaAiSearch` tool allows grounding model responses using Exa.ai via the `GoogleCloudAiplatformV1Tool` schema. The video generation suite (`CloudAiLargeModelsVisionGenerateVideoExperiments`) now supports `anchorLastFrame`, `VIDEO_CODEC_DNXHR`, and a `seamless` object for temporal looping and spatial tessellation. Storage specs in `PersistentDiskSpec` have been expanded to include Hyperdisk variants such as `hyperdisk-ml` and `hyperdisk-throughput`. Additionally, documentation across several resources has been updated to reflect a shift in terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Vertex AI` `Video` `Storage`
