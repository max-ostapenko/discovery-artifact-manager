---
date: 2026-05-29
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Search grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["Vertex AI", "Generative AI", "RAG", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Search grounding and Hyperdisk support

**Date:** 2026-05-29  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool for Exa.ai search and expands infrastructure options with Hyperdisk support for persistent disks.

## Details

Developers can now use Exa.ai as a grounding source via the new `GoogleCloudAiplatformV1Tool.exaAiSearch` field, which requires an API key and supports custom configurations. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced`. Additionally, video generation experiments now include an `originalRequestJson` field to help developers reproduce specific outputs by saving the exact request parameters alongside artifacts.

**Tags:** `Vertex AI` `Generative AI` `RAG` `Infrastructure`
