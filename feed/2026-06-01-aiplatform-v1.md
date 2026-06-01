---
date: 2026-06-01
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Machine Learning"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-01  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool via Exa.ai search and expands storage options with several Hyperdisk types for high-performance ML workloads.

## Details

Developers can now use Exa.ai as a grounding tool within `GoogleCloudAiplatformV1Tool`, enabling models to search the web via Exa's API (requires an `apiKey`). On the infrastructure side, `PersistentDiskSpec` has been expanded to support Hyperdisk types including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments helps track and reproduce specific requests, and resource limits can now be defined for sandbox environment templates.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Machine Learning`
