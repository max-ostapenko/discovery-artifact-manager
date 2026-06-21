---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds standard operation management for Online Evaluators and expands disk support to Hyperdisk, while deprecating several core generation config fields in favor of a unified response format.

## Details

A new `onlineEvaluators.operations` resource has been added, providing standard `get`, `list`, `cancel`, and `delete` methods for managing long-running evaluation tasks. In `GenerationConfig`, the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated; developers should migrate to the `response_format` field. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Throughput, Balanced, Extreme), and documentation reflects a shift in terminology from 'Vertex AI' to 'Agent Platform' for certain resource descriptions.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
