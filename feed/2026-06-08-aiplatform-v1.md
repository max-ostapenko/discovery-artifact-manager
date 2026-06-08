---
date: 2026-06-08
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Storage", "Grounding"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-08  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

This update introduces advanced video generation controls for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk storage options.

## Details

The API adds significant experimental parameters for video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including `anchorLastFrame`, DNxHR codec support, and a `seamless` object for temporal looping and spatial tessellation. A new `exaAiSearch` tool has been added to `GoogleCloudAiplatformV1Tool`, allowing models to ground responses using Exa.ai search results. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and documentation across several resources has begun rebranding 'Vertex AI' as 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Storage` `Grounding`
