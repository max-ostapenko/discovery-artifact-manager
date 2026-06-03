---
date: 2026-06-03
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "LLM", "Grounding", "Infrastructure", "Storage"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-03  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a native grounding tool and expands storage options with several new Hyperdisk types for persistent workloads.

## Details

The most notable addition is the `exaAiSearch` tool within the `Tool` schema, allowing models to ground responses using Exa.ai search results via a user-provided API key. Infrastructure-wise, `PersistentDiskSpec` now supports a wide range of Hyperdisk options, including `hyperdisk-ml`, `hyperdisk-balanced-high-availability`, and `hyperdisk-throughput`. For those working with generative video, a new `originalRequestJson` field in `CloudAiLargeModelsVisionGenerateVideoExperiments` captures the raw request for better experiment reproducibility.

**Tags:** `AI` `LLM` `Grounding` `Infrastructure` `Storage`
