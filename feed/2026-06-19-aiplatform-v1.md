---
date: 2026-06-19
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Generative AI", "Deprecation"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-19  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds lifecycle management for Online Evaluator operations and deprecates several structured output fields in GenerationConfig in favor of a unified response_format.

## Details

This update introduces a new resource path `onlineEvaluators.operations` with standard methods (get, list, cancel, delete) for managing long-running evaluation tasks. Significant deprecations have been applied to `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated, with the API steering developers toward the `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced`. Developers should also note a documentation shift where 'Vertex AI' is being rebranded as 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Vertex AI` `Generative AI` `Deprecation`
