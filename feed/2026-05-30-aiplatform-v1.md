---
date: 2026-05-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Storage", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-05-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a native Exa.ai search tool for model grounding and expands storage options with several Hyperdisk types.

## Details

The most notable addition is the `exaAiSearch` tool within the `GoogleCloudAiplatformV1Tool` schema, allowing developers to ground model responses using Exa.ai search results. This tool requires an `apiKey` and supports `customConfigs` for passing passthrough parameters to the Exa API. On the infrastructure side, `GoogleCloudAiplatformV1PersistentDiskSpec` now supports multiple Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced-high-availability`, catering to high-performance ML workloads. Additionally, video generation experiments now capture `originalRequestJson` to aid in request reproducibility, and new metadata has been added for `CreateServingProfile` operations.

**Tags:** `AI` `Grounding` `Storage` `Vertex AI`
