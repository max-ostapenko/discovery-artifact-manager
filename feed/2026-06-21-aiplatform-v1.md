---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: GenerationConfig Deprecations and Hyperdisk Support"
impact: medium
breaking: false
tags: ["generative-ai", "deprecations", "storage", "lro"]
interesting_score: 7
---

# Vertex AI: GenerationConfig Deprecations and Hyperdisk Support

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI v1 introduces lifecycle management for online evaluation operations and adds support for high-performance Hyperdisk types. Significant deprecations were added to GenerationConfig and Google Maps grounding, signaling a shift in how structured outputs and grounding widgets are handled.

## Details

The API now includes a full suite of operation management methods (get, list, cancel, delete) for the `onlineEvaluators` resource. For compute configurations, `PersistentDiskSpec` has been expanded to support Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`. Most importantly, several fields in `GenerationConfig` used for structured output—`responseMimeType`, `responseSchema`, and `responseJsonSchema`—are now deprecated in favor of the unified `response_format` field. Similarly, Google Maps grounding widget tokens are being phased out. Developers using Reasoning Engines should also note that `scope` and `memory_type` are now explicitly marked as immutable during patch operations.

**Tags:** `generative-ai` `deprecations` `storage` `lro`
