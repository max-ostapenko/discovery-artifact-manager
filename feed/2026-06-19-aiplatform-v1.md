---
date: 2026-06-19
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluators and Hyperdisk support arrive in Vertex AI"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "LLM", "Infrastructure"]
interesting_score: 7
---

# Online Evaluators and Hyperdisk support arrive in Vertex AI

**Date:** 2026-06-19  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds management for online evaluation operations and introduces Hyperdisk support for compute resources. Several core generation configuration fields are now deprecated in favor of a unified response_format.

## Details

Developers can now manage long-running evaluation tasks via the new onlineEvaluators.operations resource, including list, get, cancel, and delete methods. In GenerationConfig, the fields responseMimeType, responseSchema, and responseJsonSchema are officially deprecated; developers should migrate to the response_format field for structured outputs. Additionally, PersistentDiskSpec now supports high-performance Hyperdisk types (e.g., hyperdisk-ml, hyperdisk-balanced), and ReasoningEngines memories now explicitly flag scope and memory_type as immutable during patch operations.

**Tags:** `AI` `Vertex AI` `LLM` `Infrastructure`
