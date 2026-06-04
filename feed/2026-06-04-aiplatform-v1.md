---
date: 2026-06-04
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Grounding", "Storage", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-04  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new Exa.ai search tool for model grounding and expands storage options with several Hyperdisk types.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, enabling models to use Exa.ai for real-time information retrieval and grounding. On the infrastructure side, `PersistentDiskSpec` has been expanded to support Hyperdisk types including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments helps developers reproduce specific outputs by preserving the original REST request, and sandbox environments now support explicit resource requests and limits.

**Tags:** `AI` `Vertex AI` `Grounding` `Storage` `Generative AI`
