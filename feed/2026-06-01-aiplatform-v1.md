---
date: 2026-06-01
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Infrastructure", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-01  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with Exa.ai integration and introduces high-performance Hyperdisk options for persistent storage.

## Details

Developers can now use Exa.ai as a grounding tool via the new `exaAiSearch` field in `GoogleCloudAiplatformV1Tool`, requiring an API key and supporting custom configurations. On the infrastructure side, `PersistentDiskSpec` now supports several Hyperdisk variants, including `hyperdisk-ml` and `hyperdisk-extreme`, for more demanding ML workloads. Additionally, a new `originalRequestJson` field in video generation experiments enables better reproducibility by preserving the initial REST request.

**Tags:** `AI` `Grounding` `Infrastructure` `Vertex AI`
