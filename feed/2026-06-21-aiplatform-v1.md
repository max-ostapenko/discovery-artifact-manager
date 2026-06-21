---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator LROs and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "storage", "operations"]
interesting_score: 7
---

# Online Evaluator LROs and GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI is introducing lifecycle management for Online Evaluator operations and signaling a major shift in how structured LLM outputs are configured.

## Details

A new resource `onlineEvaluators.operations` has been added, providing standard methods (get, list, cancel, delete) for managing long-running evaluation tasks. Significant deprecations have hit `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, and `responseJsonSchema` are being phased out in favor of a unified `response_format` field. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-throughput`), and the Google Maps grounding widget context is being deprecated. Note the documentation terminology shift from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `generative-ai` `storage` `operations`
