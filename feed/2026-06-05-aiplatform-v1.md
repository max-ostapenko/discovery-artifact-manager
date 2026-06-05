---
date: 2026-06-05
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Infrastructure", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-05  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI now supports Exa.ai as a grounding tool for model responses and expands storage options with several Hyperdisk types for high-performance ML workloads.

## Details

The API introduces a new grounding tool, `GoogleCloudAiplatformV1ToolExaAiSearch`, allowing developers to integrate Exa.ai search results directly into model response generation via an API key. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-balanced`, and `hyperdisk-extreme`. Additionally, a new `originalRequestJson` field in video generation experiments helps developers track and reproduce specific requests, while new metadata schemas suggest upcoming 'Serving Profile' management features.

**Tags:** `AI` `Grounding` `Infrastructure` `Vertex AI`
