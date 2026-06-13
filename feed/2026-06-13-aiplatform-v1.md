---
date: 2026-06-13
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Looping and Exa.ai Search Tool"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo Video Looping and Exa.ai Search Tool

**Date:** 2026-06-13  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI (increasingly branded as Agent Platform) introduced advanced video generation controls for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk support for high-performance ML workloads.

## Details

Developers working with video generation can now use the `CloudAiLargeModelsVisionSeamless` schema to create looping or tessellated videos and utilize the `VIDEO_CODEC_DNXHR` codec. A significant addition is the `exaAiSearch` tool within the `Tool` schema, enabling models to ground responses using Exa.ai via a required API key. On the infrastructure side, `PersistentDiskSpec` now supports several Hyperdisk variants including `hyperdisk-ml` and `hyperdisk-throughput`. Note that for `reasoningEngines.memories.patch`, the `scope` and `memory_type` fields are now explicitly documented as immutable.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
