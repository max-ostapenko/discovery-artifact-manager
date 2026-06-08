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

Vertex AI introduces advanced video generation parameters for looping and tessellation, alongside a new Exa.ai search tool for model grounding and expanded Hyperdisk support.

## Details

The `CloudAiLargeModelsVisionGenerateVideoExperiments` schema now supports `seamless` video generation (enabling temporal looping and spatial tessellation) and an `anchorLastFrame` option for custom border masking. A new `exaAiSearch` tool has been added to the `Tool` resource, allowing developers to ground model responses using the Exa.ai search engine. Additionally, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`, while several resource descriptions have been updated to reflect a shift toward 'Agent Platform' branding.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
