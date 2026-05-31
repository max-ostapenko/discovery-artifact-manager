---
date: 2026-05-31
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "RAG", "Storage", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-05-31  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool for Exa.ai search and expands storage options with several Hyperdisk variants for high-performance workloads.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, enabling developers to ground model responses using the Exa.ai search engine by providing an `apiKey` and optional `customConfigs`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-balanced`, and `hyperdisk-extreme`. Additionally, experimental video generation now includes an `originalRequestJson` field to help developers reproduce specific output artifacts by preserving the exact parameters used in the request.

**Tags:** `AI` `RAG` `Storage` `Vertex AI`
