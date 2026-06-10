---
date: 2026-06-10
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video loops and Exa.ai search grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video loops and Exa.ai search grounding

**Date:** 2026-06-10  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai search tool for model grounding.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports 'seamless' parameters for temporal looping and spatial tessellation, plus an 'anchorLastFrame' option. Developers can now use 'exaAiSearch' as a Tool for grounding model responses using Exa.ai's search engine. Additionally, PersistentDiskSpec has been expanded to support various Hyperdisk types (ML, Throughput, Extreme), and Reasoning Engine memory patches now explicitly mark 'scope' and 'memory_type' as immutable. Note the documentation shift in several resource schemas from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `RAG` `Infrastructure`
