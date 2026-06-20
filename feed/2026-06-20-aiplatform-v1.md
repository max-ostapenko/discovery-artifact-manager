---
date: 2026-06-20
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and GenerationConfig Deprecations

**Date:** 2026-06-20  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds lifecycle management for Online Evaluator operations and introduces significant deprecations in GenerationConfig to favor a unified response format.

## Details

The API now includes a full suite of Long Running Operation (LRO) methods for `onlineEvaluators`, allowing developers to get, list, cancel, and delete evaluation tasks. Significant changes were made to `GenerationConfig`: `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated in favor of the `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types (ML, Balanced, Extreme, etc.), and the Google Maps grounding widget context tokens are being phased out. Note that `reasoningEngines.memories.patch` now explicitly marks `scope` and `memory_type` as immutable.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
