---
date: 2026-06-10
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Looping and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["generative-ai", "video", "grounding", "infrastructure"]
interesting_score: 8
---

# Vertex AI adds Veo Video Looping and Exa.ai Grounding

**Date:** 2026-06-10  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai search tool for model grounding.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports 'seamless' parameters for temporal looping and spatial tessellation, a new DNXHR codec, and an 'anchorLastFrame' option. Developers can now use the 'exaAiSearch' tool within the Tool schema to ground model responses using Exa.ai. Infrastructure updates include support for several Hyperdisk types (ML, Throughput, Extreme) in PersistentDiskSpec. Additionally, the Reasoning Engines memory patch method now explicitly flags 'scope' and 'memory_type' as immutable fields.

**Tags:** `generative-ai` `video` `grounding` `infrastructure`
