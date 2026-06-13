---
date: 2026-06-13
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-13  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, grounding via Exa.ai, and expanded infrastructure options including Hyperdisk support.

## Details

This update brings significant experimental features to video generation (Veo), including seamless looping, spatial tessellation (horizontal/vertical), and support for the `VIDEO_CODEC_DNXHR` codec. Developers can now use the `exaAiSearch` tool for grounding model responses via Exa.ai. Additionally, the `ComputerUse` tool has been hardened with a new `enablePromptInjectionDetection` flag and specific environment enums for mobile and desktop. On the infrastructure side, `PersistentDiskSpec` now supports several Hyperdisk variants (ML, Throughput, Balanced), and there is a notable documentation shift referring to the service as 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
