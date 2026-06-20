---
date: 2026-06-20
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Online Evaluator LROs and Generation Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "vertex-ai", "deprecations", "storage"]
interesting_score: 7
---

# Vertex AI: Online Evaluator LROs and Generation Deprecations

**Date:** 2026-06-20  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds management for online evaluation operations and introduces significant deprecations in GenerationConfig and Google Maps grounding.

## Details

This update introduces a new `onlineEvaluators.operations` resource, providing standard methods (get, list, delete, cancel) for managing long-running evaluation tasks. Developers using Gemini models should note that several fields in `GenerationConfig` — including `responseMimeType`, `responseSchema`, and `responseJsonSchema` — are now deprecated in favor of the unified `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types (ML, Balanced, Extreme, Throughput), and the Google Maps contextual widget behavior in grounding is being phased out. Interestingly, documentation descriptions are shifting terminology from 'Vertex AI' to 'Agent Platform' for certain resource configurations.

**Tags:** `generative-ai` `vertex-ai` `deprecations` `storage`
