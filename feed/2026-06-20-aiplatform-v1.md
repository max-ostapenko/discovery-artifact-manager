---
date: 2026-06-20
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and Structured Output Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and Structured Output Deprecations

**Date:** 2026-06-20  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces full operation management for Online Evaluators and adds Hyperdisk support, while deprecating several core GenerationConfig fields in favor of a unified response format.

## Details

The API adds a new `onlineEvaluators.operations` resource, enabling standard LRO management (get, list, cancel, delete) for evaluation tasks. Significant deprecations hit `GenerationConfig`: `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated in favor of the `response_format` field. Similarly, Google Maps grounding widgets are being phased out. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and documentation is beginning to reflect a shift in branding from 'Vertex AI' to 'Agent Platform' for specific resource types.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
