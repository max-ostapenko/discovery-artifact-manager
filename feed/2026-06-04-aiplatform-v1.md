---
date: 2026-06-04
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Infrastructure", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-04  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with Exa.ai search integration and introduces high-performance Hyperdisk options for persistent storage.

## Details

Developers can now use Exa.ai as a tool for model grounding via the new `exaAiSearch` property in `GoogleCloudAiplatformV1Tool`, which supports custom configurations and API key authentication. On the infrastructure side, `PersistentDiskSpec` has been updated to support several Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments helps with reproducibility by preserving the exact REST request sent to the API.

**Tags:** `AI` `Grounding` `Infrastructure` `Vertex AI`
