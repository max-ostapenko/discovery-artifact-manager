---
date: 2026-06-20
api: aiplatform.v1
service: Vertex AI
title: "GenerationConfig Deprecations and Online Evaluator LROs"
impact: medium
breaking: false
tags: ["generative-ai", "gemini", "deprecations", "infrastructure"]
interesting_score: 7
---

# GenerationConfig Deprecations and Online Evaluator LROs

**Date:** 2026-06-20  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI is consolidating its generative configuration under a new response format while introducing long-running operation support for online evaluators.

## Details

A significant cleanup of `GenerationConfig` is underway: `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated in favor of the unified `response_format` field. Developers using Gemini for structured output or image generation should plan to migrate. Additionally, the API now supports standard Long-Running Operations (LROs) for `onlineEvaluators`, including `get`, `list`, `cancel`, and `delete` methods. Infrastructure-wise, `PersistentDiskSpec` has been expanded to support Hyperdisk types (ML, Balanced, Extreme, etc.), and several resource descriptions have been updated to reflect a shift toward 'Agent Platform' branding.

**Tags:** `generative-ai` `gemini` `deprecations` `infrastructure`
