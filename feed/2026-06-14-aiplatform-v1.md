---
date: 2026-06-14
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Agents"]
interesting_score: 8
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-14  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, Exa.ai search grounding, and enhanced safety features for computer-use agents.

## Details

The API adds significant capabilities to video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including seamless looping, spatial tessellation (horizontal/vertical), and the `VIDEO_CODEC_DNXHR` codec. A new `exaAiSearch` tool enables grounding model responses using Exa.ai. For agentic workflows, `ToolComputerUse` now supports `enablePromptInjectionDetection` and environment-specific flags for mobile and desktop. Infrastructure-wise, `PersistentDiskSpec` expands to support Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. Note that Google Maps widget context tokens in grounding metadata are now deprecated.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Agents`
