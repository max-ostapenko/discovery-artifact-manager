---
date: 2026-06-08
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-08  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls like looping and tessellation, alongside a new Exa.ai search tool for model grounding and Hyperdisk support.

## Details

The API now includes significant updates for experimental video generation (Veo) via the `CloudAiLargeModelsVisionGenerateVideoExperiments` schema, adding support for `seamless` looping, horizontal/vertical tessellation, and `anchorLastFrame` for custom border masks. For RAG and grounding workflows, a new `GoogleCloudAiplatformV1ToolExaAiSearch` tool allows models to query Exa.ai directly. Infrastructure-wise, `PersistentDiskSpec` has been expanded to support Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-throughput`), and `ReasoningEngine` memory patches now explicitly treat `scope` and `memory_type` as immutable.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
