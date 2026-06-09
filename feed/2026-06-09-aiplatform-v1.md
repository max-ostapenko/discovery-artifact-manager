---
date: 2026-06-09
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo Video Experiments and Exa.ai Grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo Video Experiments and Exa.ai Grounding

**Date:** 2026-06-09  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for experimental models and a new Exa.ai search tool for grounding, alongside expanded Hyperdisk support for infrastructure.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) has been significantly expanded with support for seamless looping, spatial tessellation (horizontal and vertical), and a new DNxHR codec option. For RAG and grounding workflows, a new ExaAiSearch tool has been added to the Tool resource, allowing models to query Exa.ai directly using a provided API key. Additionally, the PersistentDiskSpec now supports various Hyperdisk types including hyperdisk-ml and hyperdisk-throughput, providing more performant storage options for AI workloads. Note that several resource descriptions have been updated to refer to the 'Agent Platform' instead of 'Vertex AI'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
