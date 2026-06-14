---
date: 2026-06-14
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation for Veo"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation for Veo

**Date:** 2026-06-14  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI (transitioning to 'Agent Platform' in docs) adds Exa.ai as a grounding tool and significantly expands experimental video generation capabilities including looping and tessellation.

## Details

Developers can now use the `exaAiSearch` tool for grounding model responses via Exa.ai. The video generation suite (Veo) receives a major update with `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for `seamless` looping, horizontal/vertical tessellation, and a `VIDEO_CODEC_DNXHR` option. Additionally, `ToolComputerUse` now includes a `enablePromptInjectionDetection` flag and specific environment enums for mobile and desktop. On the infrastructure side, `PersistentDiskSpec` has been expanded to support various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
