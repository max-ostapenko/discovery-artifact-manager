---
date: 2026-06-16
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Advanced Video Controls"
impact: medium
breaking: true
tags: ["AI", "Generative AI", "Grounding", "Video Generation"]
interesting_score: 8
---

# Vertex AI adds Exa.ai Grounding and Advanced Video Controls

**Date:** 2026-06-16  
**API:** `aiplatform.v1`  
**Impact:** Medium  
**⚠️ Breaking change**  

## Summary

Vertex AI (increasingly referred to as 'Agent Platform' in documentation) introduces Exa.ai search grounding, advanced video generation parameters for Veo, and computer-use safety features.

## Details

This update introduces significant experimental features for video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including seamless looping, spatial tessellation, and support for the `VIDEO_CODEC_DNXHR` codec. A new `ExaAiSearch` tool has been added for grounding model responses using Exa.ai. For agentic workflows, `ToolComputerUse` now supports environment-specific flags (Mobile/Desktop) and a new `enablePromptInjectionDetection` toggle. Additionally, `PersistentDiskSpec` has been expanded to support several Hyperdisk types (ML, Throughput, Balanced). Developers should note that the Google Maps widget context token fields are now deprecated and slated for removal.

**Tags:** `AI` `Generative AI` `Grounding` `Video Generation`
