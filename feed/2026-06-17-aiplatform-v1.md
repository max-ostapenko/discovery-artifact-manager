---
date: 2026-06-17
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: high
breaking: true
tags: ["AI", "Generative AI", "Video Generation", "Grounding", "Security"]
interesting_score: 8
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-17  
**API:** `aiplatform.v1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces advanced video generation controls for Veo, Exa.ai search grounding, and enhanced 'Computer Use' security, while deprecating Google Maps widget tokens.

## Details

The API adds significant experimental features for video generation (Veo) via the CloudAiLargeModelsVisionGenerateVideoExperiments schema, including seamless looping, spatial tessellation, and the VIDEO_CODEC_DNXHR codec. A new grounding tool, exaAiSearch, allows developers to use Exa.ai for search-based model grounding. Additionally, ToolComputerUse now includes a prompt injection detection toggle and environment flags for mobile/desktop contexts. On the infrastructure side, PersistentDiskSpec now supports Hyperdisk ML and throughput-optimized disk types. Note that the Google Maps contextual widget behavior is officially deprecated and slated for removal.

**Tags:** `AI` `Generative AI` `Video Generation` `Grounding` `Security`
