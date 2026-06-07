---
date: 2026-06-07
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Veo Video Enhancements"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Veo Video Enhancements

**Date:** 2026-06-07  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a grounding tool and significantly expands experimental video generation capabilities with looping, tessellation, and professional codecs.

## Details

A new tool, `GoogleCloudAiplatformV1ToolExaAiSearch`, allows developers to ground model responses using Exa.ai search results. The video generation suite (Veo) receives experimental updates including `seamless` parameters for temporal looping and spatial tessellation, an `anchorLastFrame` option, and support for the `VIDEO_CODEC_DNXHR` codec. Additionally, `PersistentDiskSpec` now supports several Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-extreme`), and the `reasoningEngines` memory patch method now explicitly flags `scope` and `memory_type` as immutable.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
