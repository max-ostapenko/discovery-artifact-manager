---
date: 2026-06-11
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-11  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI (increasingly referred to as 'Agent Platform' in documentation) introduced advanced video generation controls, including seamless looping and tessellation, alongside a new grounding tool via Exa.ai.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports 'seamless' parameters for temporal looping and spatial tessellation (horizontal/vertical), plus a new DNxHR codec option. Developers can now use the 'exaAiSearch' tool for model grounding, which integrates directly with Exa.ai via an API key. On the infrastructure side, PersistentDiskSpec has been expanded to support high-performance Hyperdisk types including 'hyperdisk-ml' and 'hyperdisk-throughput'. Additionally, the Reasoning Engines API now explicitly marks 'scope' and 'memory_type' as immutable during memory patch operations.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
