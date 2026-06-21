---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: New Evaluator Ops and Structured Output Migration"
impact: medium
breaking: false
tags: ["AI/ML", "Deprecation", "Infrastructure"]
interesting_score: 7
---

# Vertex AI: New Evaluator Ops and Structured Output Migration

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds standard operation management for Online Evaluators and expands disk support to Hyperdisk. Crucially, several structured output fields in GenerationConfig are now deprecated in favor of a unified response_format.

## Details

The API introduces a new `onlineEvaluators.operations` resource, enabling developers to list, get, cancel, and delete long-running evaluation tasks. In the `GenerationConfig` schema, `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated; developers should migrate to the new `response_format` field for structured LLM outputs. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-balanced`), and the documentation reflects a branding shift from 'Vertex AI' to 'Agent Platform' in several resource descriptions.

**Tags:** `AI/ML` `Deprecation` `Infrastructure`
