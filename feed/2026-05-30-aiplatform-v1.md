---
date: 2026-05-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-05-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a new grounding tool for LLMs and expands storage options with support for multiple Hyperdisk types.

## Details

Developers can now integrate Exa.ai search into their model workflows via the new `GoogleCloudAiplatformV1ToolExaAiSearch` schema, which requires an API key and allows for custom search configurations. On the infrastructure side, `PersistentDiskSpec` has been updated to support high-performance Hyperdisk options, including `hyperdisk-ml` and `hyperdisk-extreme`. Additionally, the video generation experiments schema now includes an `originalRequestJson` field to help users reproduce specific requests by saving the exact REST payload alongside output artifacts.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Generative AI`
