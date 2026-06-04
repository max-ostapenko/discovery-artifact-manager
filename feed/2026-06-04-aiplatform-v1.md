---
date: 2026-06-04
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Storage", "Grounding"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-04  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new Exa.ai search tool for model grounding and expands storage options with several Hyperdisk types for high-performance workloads.

## Details

The API now supports Exa.ai as a grounding tool via GoogleCloudAiplatformV1ToolExaAiSearch, requiring an apiKey and allowing for custom configurations. On the infrastructure side, PersistentDiskSpec has been updated to support multiple Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput. Additionally, video generation experiments now include an originalRequestJson field to help developers reproduce requests, and new metadata has been added for ServingProfile creation operations.

**Tags:** `AI` `Generative AI` `Storage` `Grounding`
