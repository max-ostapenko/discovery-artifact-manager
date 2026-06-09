---
date: 2026-06-09
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video controls and Exa.ai grounding"
impact: medium
breaking: false
tags: ["Generative AI", "Video", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI adds Veo video controls and Exa.ai grounding

**Date:** 2026-06-09  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduced advanced video generation parameters for Veo, integrated Exa.ai as a grounding tool, and expanded storage options with Hyperdisk support.

## Details

The update introduces 'CloudAiLargeModelsVisionGenerateVideoExperiments' for Veo, adding support for seamless temporal looping, spatial tessellation, and the DNXHR codec. A new 'ExaAiSearch' tool allows models to ground responses using Exa.ai search results via a required API key. Additionally, 'PersistentDiskSpec' now supports various Hyperdisk types (ML, Balanced, Throughput), and 'reasoningEngines.memories.patch' documentation now explicitly flags 'scope' and 'memory_type' as immutable fields. Notably, many resource descriptions have been updated to refer to the 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `Generative AI` `Video` `Grounding` `Storage`
