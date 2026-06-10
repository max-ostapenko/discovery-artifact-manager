---
date: 2026-06-10
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video controls and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video controls and Exa.ai grounding

**Date:** 2026-06-10  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation parameters for Veo, a new Exa.ai search tool for grounding, and expanded Hyperdisk storage support.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now includes controls for seamless looping, spatial tessellation (horizontal/vertical), and 'anchorLastFrame' for consistent video borders. A new tool, 'exaAiSearch', has been added to the Tool resource, allowing developers to use Exa.ai for model grounding via an API key. Additionally, PersistentDiskSpec now supports Hyperdisk types (balanced, extreme, ML, throughput), and Reasoning Engine memory patches now explicitly flag 'scope' and 'memory_type' as immutable fields.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
