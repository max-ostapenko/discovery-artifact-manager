---
date: 2026-06-11
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video experiments and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video experiments and Exa.ai grounding

**Date:** 2026-06-11  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces experimental video generation features for Veo, a new Exa.ai grounding tool, and expanded Hyperdisk support for infrastructure specs.

## Details

The API adds significant experimental capabilities to video generation via `CloudAiLargeModelsVisionGenerateVideoExperiments`, including seamless looping, spatial tessellation (horizontal/vertical), and support for the `VIDEO_CODEC_DNXHR` codec. A new grounding tool, `exaAiSearch`, is now available in `GoogleCloudAiplatformV1Tool`, requiring an API key to integrate Exa.ai search results into model responses. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`. Notably, documentation strings across several resources have begun transitioning terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
