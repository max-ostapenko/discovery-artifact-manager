---
date: 2026-06-05
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "RAG"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-05  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with a new Exa.ai search tool and adds support for high-performance Hyperdisk types in persistent disk specs.

## Details

Developers can now integrate Exa.ai as a grounding tool via the new `GoogleCloudAiplatformV1ToolExaAiSearch` schema, which supports custom configurations and API key authentication. The `PersistentDiskSpec` has been updated to include several Hyperdisk variants, such as `hyperdisk-ml` and `hyperdisk-balanced`, providing more performant storage options for AI workloads. Additionally, a new `originalRequestJson` field in video generation experiments enables better reproducibility by capturing the exact REST request sent by the user.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `RAG`
