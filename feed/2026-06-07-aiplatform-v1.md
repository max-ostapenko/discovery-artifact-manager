---
date: 2026-06-07
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video controls and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video controls and Exa.ai grounding

**Date:** 2026-06-07  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation parameters for Veo, including seamless looping and tessellation, alongside a new Exa.ai grounding tool and Hyperdisk support.

## Details

This update brings significant enhancements to video generation via the `CloudAiLargeModelsVisionGenerateVideoExperiments` schema, adding support for the `VIDEO_CODEC_DNXHR` codec, custom experimental parameters, and 'seamless' generation features like temporal looping and spatial tessellation. A new `ExaAiSearch` tool has been added to the `Tool` schema, allowing models to ground responses using Exa.ai search results. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-throughput`), and the documentation reflects a branding shift from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
