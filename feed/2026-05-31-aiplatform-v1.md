---
date: 2026-05-31
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "RAG", "Storage", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-05-31  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with a new Exa.ai search tool and adds support for high-performance Hyperdisk storage types.

## Details

Developers can now use Exa.ai as a grounding source via the new `exaAiSearch` field in `GoogleCloudAiplatformV1Tool`, which supports custom configurations and API key management. On the infrastructure side, `PersistentDiskSpec` has been expanded to support Hyperdisk variants including `hyperdisk-ml`, `hyperdisk-extreme`, and `hyperdisk-throughput`. Additionally, video generation experiments now include an `originalRequestJson` field to help developers reproduce specific outputs by saving the exact request parameters alongside artifacts.

**Tags:** `AI` `Vertex AI` `RAG` `Storage` `Generative AI`
