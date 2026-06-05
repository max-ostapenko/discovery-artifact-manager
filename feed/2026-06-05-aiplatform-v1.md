---
date: 2026-06-05
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video looping and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Storage", "RAG"]
interesting_score: 8
---

# Vertex AI adds Veo video looping and Exa.ai grounding

**Date:** 2026-06-05  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk storage options.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports seamless looping and spatial tessellation (horizontal/vertical), along with a high-quality DNxHR codec and frame anchoring. A new tool, GoogleCloudAiplatformV1ToolExaAiSearch, allows developers to integrate Exa.ai for model grounding using an API key. Additionally, PersistentDiskSpec has been expanded to support various Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput, catering to high-performance AI workloads. Notably, several resource descriptions have been updated to refer to the 'Agent Platform' instead of 'Vertex AI', signaling a shift in platform branding or architecture.

**Tags:** `AI` `Generative AI` `Video` `Storage` `RAG`
