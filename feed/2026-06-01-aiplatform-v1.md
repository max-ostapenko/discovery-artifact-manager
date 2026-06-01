---
date: 2026-06-01
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Grounding", "Storage", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-01  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a new grounding tool for model responses and expands storage options with several Hyperdisk types.

## Details

Developers can now integrate Exa.ai search directly into model workflows via the new `GoogleCloudAiplatformV1Tool.exaAiSearch` field, which supports custom configurations and API key authentication. On the infrastructure side, `PersistentDiskSpec` has been updated to support high-performance Hyperdisk variants, including `hyperdisk-ml`, `hyperdisk-balanced`, and `hyperdisk-throughput`. Additionally, video generation experiments now include an `originalRequestJson` field to help developers reproduce specific requests, and new metadata has been added for `ServingProfile` operations.

**Tags:** `AI` `Generative AI` `Grounding` `Storage` `Vertex AI`
