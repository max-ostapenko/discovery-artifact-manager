---
date: 2026-06-18
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and Generation Config Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Online Evaluator Ops and Generation Config Deprecations

**Date:** 2026-06-18  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds management for online evaluation operations and deprecates several core GenerationConfig fields in favor of a unified response_format.

## Details

A new resource, `onlineEvaluators.operations`, has been introduced, providing standard methods (get, list, cancel, delete) to manage long-running evaluation tasks. Significant deprecations have hit `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated and should be replaced with the new `response_format` field. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and Google Maps grounding widgets are being phased out. Note the documentation shift where 'Vertex AI' is being replaced by 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
