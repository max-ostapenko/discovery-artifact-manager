---
date: 2026-06-08
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video controls and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video controls and Exa.ai grounding

**Date:** 2026-06-08  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation parameters for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk storage options.

## Details

The video generation schema (Veo) now includes `CloudAiLargeModelsVisionSeamless` for temporal looping and spatial tessellation, along with support for the `VIDEO_CODEC_DNXHR` codec. A new `exaAiSearch` tool has been added to the `Tool` resource, allowing models to ground responses using Exa.ai search results. Additionally, `PersistentDiskSpec` has been expanded to support high-performance Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`. Notably, several resource descriptions have been updated to refer to the service as 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
