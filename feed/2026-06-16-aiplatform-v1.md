---
date: 2026-06-16
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Looping, Exa.ai Grounding, and Hyperdisks"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Grounding", "Infrastructure", "Video"]
interesting_score: 7
---

# Vertex AI adds Veo Video Looping, Exa.ai Grounding, and Hyperdisks

**Date:** 2026-06-16  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, third-party grounding via Exa.ai, and support for high-performance Hyperdisks.

## Details

The video generation suite (Veo) receives significant experimental updates, including a new `seamless` property for temporal looping and spatial tessellation, plus support for the `VIDEO_CODEC_DNXHR` codec. Grounding capabilities are expanded with the `ExaAiSearch` tool, allowing models to query Exa.ai directly. Infrastructure-wise, `PersistentDiskSpec` now supports several Hyperdisk variants (ML, Balanced, Throughput, etc.). Developers using 'Computer Use' tools can now toggle `enablePromptInjectionDetection` and specify `ENVIRONMENT_MOBILE` or `ENVIRONMENT_DESKTOP` targets. Notably, many documentation strings have been updated to refer to 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `AI` `Generative AI` `Grounding` `Infrastructure` `Video`
