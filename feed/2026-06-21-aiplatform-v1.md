---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Storage"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduced management for online evaluation operations and deprecated several core fields in GenerationConfig in favor of a unified response_format.

## Details

A new resource `onlineEvaluators.operations` has been added, providing standard methods (get, list, cancel, delete) for managing long-running evaluation tasks. Significant deprecations have hit `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are being phased out in favor of the new `response_format` structure. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-throughput`), and documentation across the API is shifting terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Deprecation` `Storage`
