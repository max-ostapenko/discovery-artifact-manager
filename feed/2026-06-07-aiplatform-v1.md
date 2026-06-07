---
date: 2026-06-07
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-07  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduced advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new grounding tool via Exa.ai and expanded Hyperdisk storage options.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports 'seamless' parameters for temporal looping and spatial tessellation, an 'anchorLastFrame' option, and the DNxHR codec. A new 'exaAiSearch' tool has been added to the Tool resource, enabling RAG workflows grounded in Exa.ai search results (requires an API key). On the infrastructure side, PersistentDiskSpec now supports several Hyperdisk variants including 'hyperdisk-ml' and 'hyperdisk-throughput'. Notably, documentation strings are shifting terminology from 'Vertex AI' to 'Agent Platform' across several resource types.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
