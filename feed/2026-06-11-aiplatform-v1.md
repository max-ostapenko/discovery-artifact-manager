---
date: 2026-06-11
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-11  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduced advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai grounding tool and Hyperdisk storage support.

## Details

The API adds significant experimental features for video generation via CloudAiLargeModelsVisionGenerateVideoExperiments, including 'anchorLastFrame' for custom border masks and a 'seamless' configuration for temporal looping and spatial tessellation. A new Tool type, 'exaAiSearch', enables model grounding using the Exa.ai search engine. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types (ML, Balanced, Throughput), and Reasoning Engine memories have clarified immutability for 'scope' and 'memory_type' during patch operations. Notably, several resource descriptions have been updated to refer to the 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
