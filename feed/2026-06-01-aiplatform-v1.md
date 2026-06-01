---
date: 2026-06-01
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Machine Learning"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-01  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool for Exa.ai search, expands storage options with Hyperdisk support, and improves video generation reproducibility.

## Details

Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using the Exa.ai search engine; this requires an API key and supports passing custom configurations directly to Exa. Storage specifications in `PersistentDiskSpec` have been expanded to support Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced-high-availability`, catering to high-performance ML workloads. Additionally, the video generation experimental schema now includes `originalRequestJson` to help users reproduce specific requests from output artifacts.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Machine Learning`
