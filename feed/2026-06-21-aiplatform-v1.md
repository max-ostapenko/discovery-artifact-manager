---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "vertex-ai", "deprecations", "storage"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces lifecycle management for online evaluation tasks and marks several core GenerationConfig fields as deprecated in favor of a unified response format.

## Details

A new resource `onlineEvaluators.operations` has been added, providing standard GET, LIST, CANCEL, and DELETE methods for managing long-running evaluation tasks. Significant deprecations have hit `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, `responseJsonSchema`, and `imageConfig` are now deprecated, with the API moving toward a unified `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support high-performance Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-throughput`), and the Google Maps grounding widget context is being phased out. Note that in Reasoning Engine memories, `scope` and `memory_type` are now explicitly documented as immutable during patch operations.

**Tags:** `generative-ai` `vertex-ai` `deprecations` `storage`
