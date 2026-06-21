---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["AI", "Gemini", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces operation management for online evaluators and deprecates several structured output fields in GenerationConfig in favor of a unified response_format.

## Details

This update adds a full suite of standard operation methods (get, list, cancel, delete) to the `onlineEvaluators` resource, allowing better lifecycle management of evaluation tasks. Significant deprecations hit `GenerationConfig`: `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated, with developers directed to use the new `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. Note the terminology shift in documentation from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `AI` `Gemini` `Deprecation` `Infrastructure`
