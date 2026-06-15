---
date: 2026-06-15
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Veo video looping"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Vertex AI", "Storage"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Veo video looping

**Date:** 2026-06-15  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its generative capabilities with new experimental video generation features (looping, tessellation) and a new Exa.ai search tool for grounding.

## Details

The API introduces significant updates to video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for seamless looping, spatial tessellation (horizontal/vertical), and the high-quality `VIDEO_CODEC_DNXHR` codec. A new `ExaAiSearch` tool has been added to `GoogleCloudAiplatformV1Tool`, allowing developers to ground model responses using Exa.ai's search engine. Additionally, the `ComputerUse` tool now includes prompt injection detection and environment selection (Mobile/Desktop). On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Generative AI` `Vertex AI` `Storage`
