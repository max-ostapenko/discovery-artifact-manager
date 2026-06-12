---
date: 2026-06-12
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and advanced video generation"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and advanced video generation

**Date:** 2026-06-12  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search as a grounding tool and expands experimental video generation capabilities with looping and tessellation. New Hyperdisk options also provide more storage flexibility for high-performance workloads.

## Details

The API now includes a GoogleCloudAiplatformV1ToolExaAiSearch schema, allowing models to use Exa.ai for real-time information retrieval via an API key. For video generation (Veo), the CloudAiLargeModelsVisionGenerateVideoExperiments schema adds support for 'seamless' video generation (looping and spatial tessellation), an 'anchorLastFrame' option for custom border masks, and the VIDEO_CODEC_DNXHR codec. Additionally, PersistentDiskSpec has been expanded to support various Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput, for more specialized storage requirements.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Storage`
