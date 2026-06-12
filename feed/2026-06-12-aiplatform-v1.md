---
date: 2026-06-12
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Infrastructure"]
interesting_score: 7
---

# Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks

**Date:** 2026-06-12  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai grounding tool and Hyperdisk support.

## Details

The update adds significant capabilities to video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including `seamless` parameters for temporal looping and spatial tessellation, and an `anchorLastFrame` option. Developers can now use `exaAiSearch` as a grounding tool within `GoogleCloudAiplatformV1Tool`, requiring an API key. Infrastructure-wise, `PersistentDiskSpec` now supports multiple Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and `reasoningEngines` memories have clarified immutable fields during patch operations. There is also a notable terminology shift in documentation from 'Vertex AI' to 'Agent Platform' for resource management.

**Tags:** `AI` `Generative AI` `Video` `Infrastructure`
