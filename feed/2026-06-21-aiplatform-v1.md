---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and Structured Output Deprecations"
impact: medium
breaking: false
tags: ["AI", "Gemini", "VertexAI", "Deprecation"]
interesting_score: 7
---

# Online Evaluator Ops and Structured Output Deprecations

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI adds LRO support for Online Evaluators and deprecates several GenerationConfig fields in favor of the new response_format.

## Details

Developers using Gemini for structured output should note that response_mime_type, response_schema, and response_json_schema in GenerationConfig are now deprecated; you should migrate to the new response_format field. The API also introduces a full suite of operation management methods (get, list, cancel, delete) for onlineEvaluators. Additionally, PersistentDiskSpec has been expanded to support Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput, and reasoningEngines.memories.patch now explicitly flags scope and memory_type as immutable fields.

**Tags:** `AI` `Gemini` `VertexAI` `Deprecation`
