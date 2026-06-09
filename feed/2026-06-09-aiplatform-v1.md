---
date: 2026-06-09
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Features"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation Features

**Date:** 2026-06-09  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds Exa.ai as a grounding tool and significantly expands experimental video generation capabilities, including seamless looping and spatial tessellation.

## Details

Developers can now integrate Exa.ai search for model grounding via the new `exaAiSearch` tool, which supports custom configurations and requires an API key. The video generation experimental schema (`CloudAiLargeModelsVisionGenerateVideoExperiments`) has been heavily updated with a `seamless` object for temporal looping and spatial tessellation (horizontal/vertical), a new `VIDEO_CODEC_DNXHR` enum, and an `anchorLastFrame` option. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (ML, Throughput, Balanced), and the Reasoning Engine memory patch method now explicitly marks `scope` and `memory_type` as immutable.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
