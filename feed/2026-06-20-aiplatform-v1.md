---
date: 2026-06-20
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluators and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Deprecation", "LRO"]
interesting_score: 7
---

# Online Evaluators and GenerationConfig Deprecations

**Date:** 2026-06-20  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new onlineEvaluators resource for managing long-running evaluation operations and deprecates several GenerationConfig fields in favor of a unified response_format.

## Details

A new resource path `onlineEvaluators.operations` has been added, providing standard LRO management (get, list, cancel, delete) for evaluation tasks. Significant deprecations hit `GenerationConfig`, where `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated; developers should migrate to the `response_format` field. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and Google Maps grounding widgets are being phased out. Note the terminology shift in documentation from 'Vertex AI' to 'Agent Platform' for resource management descriptions.

**Tags:** `AI` `Vertex AI` `Deprecation` `LRO`
