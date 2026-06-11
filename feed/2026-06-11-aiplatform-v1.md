---
date: 2026-06-11
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-11  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and professional codecs, alongside a new Exa.ai grounding tool and Hyperdisk storage support.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) gains significant experimental features: 'seamless' parameters for temporal looping and spatial tessellation, an 'anchorLastFrame' option, and support for the VIDEO_CODEC_DNXHR codec. For RAG and agentic workflows, a new 'exaAiSearch' tool allows models to ground responses using Exa.ai search results. Infrastructure-wise, PersistentDiskSpec now supports Hyperdisk types (ML, Throughput, Balanced), and Reasoning Engine memories have clarified immutability for 'scope' and 'memory_type' during patch operations.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Storage`
