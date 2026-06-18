---
date: 2026-06-18
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and GenerationConfig Consolidation"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Gemini", "Deprecation"]
interesting_score: 7
---

# Online Evaluator Ops and GenerationConfig Consolidation

**Date:** 2026-06-18  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds lifecycle management for online evaluation operations and deprecates several structured output fields in GenerationConfig in favor of a unified response_format.

## Details

This update introduces a new resource path `onlineEvaluators.operations` for managing long-running operations (Get, List, Cancel, Delete) specifically for online evaluation tasks. Significant deprecations are hitting `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated, with the API moving toward a unified `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and documentation now frequently refers to the service as 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Gemini` `Deprecation`
