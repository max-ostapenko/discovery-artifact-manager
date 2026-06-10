---
date: 2026-06-10
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks"
impact: medium
breaking: false
tags: ["Generative AI", "Video Generation", "Grounding", "Storage"]
interesting_score: 7
---

# Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks

**Date:** 2026-06-10  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, including seamless looping and tessellation, alongside a new Exa.ai grounding tool and expanded Hyperdisk storage support.

## Details

The video generation schema (Veo) has been significantly expanded with `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for seamless temporal looping, spatial tessellation (horizontal/vertical), and a new DNxHR codec. Developers can now use `exaAiSearch` as a built-in tool for grounding model responses with Exa.ai. On the infrastructure side, `PersistentDiskSpec` now supports multiple Hyperdisk types (ML, Balanced, Throughput, etc.), and sandbox environments now allow explicit resource requests and limits. Note that `reasoningEngines.memories.patch` now explicitly marks `scope` and `memory_type` as immutable fields.

**Tags:** `Generative AI` `Video Generation` `Grounding` `Storage`
