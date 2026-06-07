---
date: 2026-06-07
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-07  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls including seamless looping, DNxHR codec support, and a new Exa.ai search tool for model grounding.

## Details

The video generation suite (Veo) receives significant experimental updates via CloudAiLargeModelsVisionGenerateVideoExperiments, adding support for the DNxHR codec, 'anchorLastFrame' controls, and a new 'seamless' configuration for temporal looping and spatial tessellation. For LLM grounding, the API now includes a native ExaAiSearch tool, allowing models to query Exa.ai directly. Infrastructure-wise, PersistentDiskSpec has been expanded to support Hyperdisk types (ML, Throughput, and Balanced), and several resource descriptions have been updated to reflect a shift in terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
