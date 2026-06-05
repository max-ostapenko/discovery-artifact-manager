---
date: 2026-06-05
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Infrastructure", "Machine Learning"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-05  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with Exa.ai search integration and introduces high-performance Hyperdisk options for persistent storage.

## Details

Developers can now utilize the `exaAiSearch` tool within the `GoogleCloudAiplatformV1Tool` schema to ground model responses using Exa.ai, which includes support for custom configurations and requires an API key. On the infrastructure side, `PersistentDiskSpec` has been updated to support multiple Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-extreme`, catering to high-performance ML workloads. Additionally, a new `originalRequestJson` field in video generation experiments allows for better reproducibility by preserving the original REST request.

**Tags:** `AI` `Vertex AI` `Grounding` `Infrastructure` `Machine Learning`
