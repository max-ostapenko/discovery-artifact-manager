---
date: 2026-06-03
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Hyperdisk"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-03  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding for LLMs and expands storage options with Google Cloud Hyperdisk support.

## Details

Developers can now use `exaAiSearch` within `GoogleCloudAiplatformV1Tool` to ground model responses using the Exa.ai search engine, requiring an `apiKey` and supporting `customConfigs`. On the infrastructure side, `PersistentDiskSpec` has been updated to support several Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-extreme`, which are critical for high-performance ML workloads. Additionally, a new `originalRequestJson` field in video generation experiments allows for better reproducibility by preserving the exact REST request sent to the API.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Hyperdisk`
