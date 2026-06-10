---
date: 2026-06-10
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Veo Video Looping and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 8
---

# Vertex AI: Veo Video Looping and Exa.ai Grounding

**Date:** 2026-06-10  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds advanced video generation controls for Veo, including looping and tessellation, alongside a new Exa.ai search tool for grounding.

## Details

The vision API now supports 'seamless' video generation via CloudAiLargeModelsVisionSeamless, enabling temporal looping and spatial tessellation (horizontal/vertical). A new tool, GoogleCloudAiplatformV1ToolExaAiSearch, allows developers to integrate Exa.ai search for model grounding by providing an API key. On the infrastructure side, PersistentDiskSpec has been expanded to support Hyperdisk types including hyperdisk-ml and hyperdisk-throughput, while reasoningEngines.memories.patch now explicitly marks 'scope' and 'memory_type' as immutable fields.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
