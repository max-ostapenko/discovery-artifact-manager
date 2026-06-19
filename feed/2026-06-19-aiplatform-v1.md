---
date: 2026-06-19
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "deprecations", "ops"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-19  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces operation management for Online Evaluators and deprecates several structured output fields in GenerationConfig in favor of a new unified format.

## Details

A new resource path `onlineEvaluators.operations` has been added, supporting standard LRO methods (get, list, cancel, delete) for managing evaluation tasks. Significant deprecations have hit `GenerationConfig`: `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated, with developers directed to use the new `response_format` field. Additionally, `PersistentDiskSpec` now supports Hyperdisk variants (balanced, extreme, ML, throughput), and the Google Maps grounding widget context is being phased out.

**Tags:** `generative-ai` `deprecations` `ops`
