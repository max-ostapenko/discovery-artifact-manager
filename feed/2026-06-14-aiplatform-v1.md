---
date: 2026-06-14
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Veo Video Looping"
impact: medium
breaking: false
tags: ["generative-ai", "video-gen", "grounding", "infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Veo Video Looping

**Date:** 2026-06-14  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding, advanced video generation controls for Veo, and expanded storage options with Hyperdisk support.

## Details

This update brings significant additions to the generative AI suite. A new `ExaAiSearch` tool enables grounding model responses using Exa.ai's search engine. For video generation (Veo), the `GenerateVideoExperiments` schema now includes `seamless` parameters for temporal looping and spatial tessellation, as well as `anchorLastFrame` for custom border masks. Additionally, `ToolComputerUse` now supports prompt injection detection and specific mobile/desktop environment targeting. On the infrastructure side, `PersistentDiskSpec` has been expanded to support high-performance Hyperdisk types (ML, Throughput, and Extreme). Note that the Google Maps contextual widget functionality is now deprecated and marked for removal.

**Tags:** `generative-ai` `video-gen` `grounding` `infrastructure`
