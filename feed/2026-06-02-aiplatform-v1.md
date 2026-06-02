---
date: 2026-06-02
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Storage", "Machine Learning", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-02  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with Exa.ai search integration and introduces high-performance Hyperdisk options for persistent storage.

## Details

Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using Exa.ai, featuring a dedicated `apiKey` field and `customConfigs` for passing search parameters. On the infrastructure side, `PersistentDiskSpec` has been updated to support several Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments allows for better reproducibility by preserving the exact REST request sent to the API.

**Tags:** `AI` `Grounding` `Storage` `Machine Learning` `Vertex AI`
