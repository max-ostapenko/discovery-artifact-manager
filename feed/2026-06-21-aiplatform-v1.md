---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and Major GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "deprecations", "infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and Major GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI (now appearing as 'Agent Platform' in documentation) has introduced long-running operation management for Online Evaluators and deprecated several core fields in GenerationConfig in favor of a unified response format.

## Details

A new resource hierarchy under `onlineEvaluators.operations` has been added, supporting standard `get`, `list`, `cancel`, and `delete` methods for managing asynchronous evaluation tasks. Significant deprecations have hit `GenerationConfig`: `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated, signaling a move toward the `response_format` field for structured output and image generation. Additionally, the Google Maps contextual widget for grounding is being phased out. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Balanced, Extreme, Throughput), and `reasoningEngines.memories.patch` now explicitly flags `scope` and `memory_type` as immutable fields.

**Tags:** `generative-ai` `deprecations` `infrastructure`
