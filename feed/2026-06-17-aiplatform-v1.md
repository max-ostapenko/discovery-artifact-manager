---
date: 2026-06-17
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: New Online Evaluators and Generation Deprecations"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Vertex AI: New Online Evaluators and Generation Deprecations

**Date:** 2026-06-17  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds lifecycle management for online evaluation operations and marks several structured output fields in GenerationConfig as deprecated in favor of a unified response_format.

## Details

The API introduces the `onlineEvaluators.operations` resource, providing standard methods (get, list, cancel, delete) to manage long-running evaluation tasks. Significant deprecations hit `GenerationConfig`, where `response_schema`, `response_mime_type`, and `image_config` are being phased out for the new `response_format` field. Additionally, the infrastructure layer sees an upgrade with `PersistentDiskSpec` now supporting various Hyperdisk types (ML, Balanced, Extreme, Throughput), and Google Maps grounding widgets are officially deprecated. Note that documentation strings are shifting terminology from 'Vertex AI' to 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Generative AI` `Deprecation` `Infrastructure`
