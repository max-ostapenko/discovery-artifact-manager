---
date: 2026-06-03
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Storage", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-03  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding for models and expands storage options with several new Hyperdisk types.

## Details

Developers can now use Exa.ai as a grounding tool via the new `GoogleCloudAiplatformV1ToolExaAiSearch` schema, which requires an `apiKey` and supports custom configurations. Storage capabilities in `GoogleCloudAiplatformV1PersistentDiskSpec` have been expanded to include high-performance Hyperdisk options such as `hyperdisk-ml`, `hyperdisk-extreme`, and `hyperdisk-throughput`. Additionally, video generation experiments now include an `originalRequestJson` field to help developers reproduce specific output artifacts by referencing the exact initial request.

**Tags:** `AI` `Grounding` `Storage` `Vertex AI`
