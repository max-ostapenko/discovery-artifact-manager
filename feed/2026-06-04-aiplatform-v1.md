---
date: 2026-06-04
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Machine Learning", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-04  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces third-party grounding via Exa.ai and expands infrastructure options with support for high-performance Hyperdisk types.

## Details

Developers can now use the `exaAiSearch` tool within `GoogleCloudAiplatformV1Tool` to ground model responses using Exa.ai's search engine, which includes support for custom configurations and requires an API key. On the infrastructure side, `PersistentDiskSpec` has been updated to support several Hyperdisk variants, including `hyperdisk-ml` and `hyperdisk-extreme`, catering to high-performance storage needs. Additionally, a new `originalRequestJson` field in video generation experiments allows for better reproducibility by preserving the exact REST API request sent by the user.

**Tags:** `AI` `Machine Learning` `Grounding` `Storage`
