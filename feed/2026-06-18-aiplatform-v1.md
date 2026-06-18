---
date: 2026-06-18
api: aiplatform.v1
service: Vertex AI
title: "Structured Output Deprecations and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Gemini", "Storage", "Deprecation"]
interesting_score: 8
---

# Structured Output Deprecations and Hyperdisk Support

**Date:** 2026-06-18  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI is streamlining structured output configuration by deprecating several GenerationConfig fields in favor of a unified response_format. The update also introduces high-performance Hyperdisk storage options and new management operations for online evaluators.

## Details

A significant shift is occurring in how developers handle structured LLM outputs: `response_mime_type`, `response_schema`, and `response_json_schema` in `GenerationConfig` are now deprecated; developers should migrate to the `response_format` field. On the infrastructure side, `PersistentDiskSpec` now supports Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-throughput`), offering better performance for training and prediction workloads. Additionally, a new `onlineEvaluators.operations` resource has been added, providing standard LRO (Long Running Operation) methods like `cancel`, `delete`, and `list` for evaluation tasks. Note the documentation shift where 'Vertex AI' is being replaced by 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Gemini` `Storage` `Deprecation`
