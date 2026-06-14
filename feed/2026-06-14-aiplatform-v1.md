---
date: 2026-06-14
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Veo Video Controls, Exa.ai Grounding, and Hyperdisk"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Infrastructure", "Video", "Grounding"]
interesting_score: 7
---

# Vertex AI: Veo Video Controls, Exa.ai Grounding, and Hyperdisk

**Date:** 2026-06-14  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its generative capabilities with advanced video looping/tessellation, Exa.ai search grounding, and high-performance Hyperdisk support.

## Details

This update introduces significant experimental features for video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including seamless looping, spatial tessellation (horizontal/vertical), and support for the `VIDEO_CODEC_DNXHR` codec. For grounding, a new `exaAiSearch` tool has been added to `GoogleCloudAiplatformV1Tool`, allowing models to query Exa.ai. Infrastructure-wise, `PersistentDiskSpec` now supports Hyperdisk types (ML, Throughput, Balanced). Additionally, `ToolComputerUse` now includes a `enablePromptInjectionDetection` flag and specific environment targets for mobile and desktop. Note that the Google Maps contextual widget fields are now deprecated and slated for removal.

**Tags:** `AI` `Generative AI` `Infrastructure` `Video` `Grounding`
