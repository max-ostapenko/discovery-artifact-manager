---
date: 2026-05-31
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Machine Learning"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-05-31  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool via Exa.ai search and expands storage options with Hyperdisk support for ML workloads.

## Details

The most significant update is the addition of `GoogleCloudAiplatformV1Tool.exaAiSearch`, allowing models to be grounded on Exa.ai search results using a provided `apiKey` and optional `customConfigs`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support several Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-extreme`, and `hyperdisk-throughput`. Developers working with video generation will also find a new `originalRequestJson` field in `CloudAiLargeModelsVisionGenerateVideoExperiments` to help with request reproducibility, while `reasoningEngines.memories.patch` now explicitly flags `scope` and `memory_type` as immutable fields.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Machine Learning`
