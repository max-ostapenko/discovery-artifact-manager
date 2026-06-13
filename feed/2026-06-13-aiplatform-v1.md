---
date: 2026-06-13
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-13  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai search tool for model grounding.

## Details

The video generation suite (Veo) receives significant experimental updates via `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for seamless temporal looping, spatial tessellation (horizontal/vertical), and a new `VIDEO_CODEC_DNXHR` codec. For RAG and grounding workflows, a new `exaAiSearch` tool has been added to the `Tool` schema, allowing models to query Exa.ai directly. Additionally, infrastructure specs now support high-performance Hyperdisk types (ML, Throughput, and Extreme) in `PersistentDiskSpec`, and several documentation strings have been updated to refer to the 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
