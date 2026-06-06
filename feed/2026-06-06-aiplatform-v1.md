---
date: 2026-06-06
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Experiments and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Storage", "Grounding"]
interesting_score: 8
---

# Vertex AI adds Veo Video Experiments and Exa.ai Grounding

**Date:** 2026-06-06  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk storage options.

## Details

The update brings significant enhancements to video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for seamless looping, spatial tessellation (horizontal/vertical), and the `VIDEO_CODEC_DNXHR` codec. A new `exaAiSearch` tool has been added to the `Tool` schema, enabling models to perform grounded searches using Exa.ai. Additionally, `PersistentDiskSpec` now supports multiple Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-throughput`), and the Nearest Neighbor Search API now explicitly flags `DUPLICATE_ID` errors. Note that several resource descriptions have been updated to refer to the 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `AI` `Generative AI` `Video` `Storage` `Grounding`
