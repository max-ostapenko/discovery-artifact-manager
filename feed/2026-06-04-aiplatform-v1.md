---
date: 2026-06-04
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Infrastructure", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-04  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new Exa.ai search tool for model grounding and expands persistent disk options to include high-performance Hyperdisk types.

## Details

Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using Exa.ai, requiring an `apiKey` and supporting `customConfigs`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk variants including `hyperdisk-ml` and `hyperdisk-extreme`. Additionally, a new `originalRequestJson` field in video generation experiments enables better reproducibility by preserving the exact REST API request sent by the user.

**Tags:** `AI` `Vertex AI` `Grounding` `Infrastructure` `Generative AI`
