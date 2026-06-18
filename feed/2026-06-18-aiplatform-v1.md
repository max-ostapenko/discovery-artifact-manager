---
date: 2026-06-18
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-18  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds lifecycle management for online evaluation operations and signals a major shift in how structured outputs are configured in GenerationConfig.

## Details

A new resource `onlineEvaluators.operations` has been introduced, providing standard methods (get, list, cancel, delete) to manage long-running evaluation tasks. Significant deprecations have hit `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated in favor of a unified `response_format`. Similarly, Google Maps grounding widgets are being phased out. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Throughput, Balanced, Extreme), and documentation terminology is shifting from 'Vertex AI' to 'Agent Platform' for several resource types.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
