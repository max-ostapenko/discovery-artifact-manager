---
date: 2026-05-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["Vertex AI", "Machine Learning", "Grounding", "Storage", "Exa.ai"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-05-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI now supports Exa.ai as a search tool for model grounding and introduces high-performance Hyperdisk options for persistent storage.

## Details

This update introduces the `GoogleCloudAiplatformV1ToolExaAiSearch` schema, allowing developers to integrate Exa.ai as a grounding tool for model responses, complete with API key management and custom configuration passing. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`, which are critical for high-performance ML workloads. Additionally, video generation experiments now include an `originalRequestJson` field to facilitate request reproduction, and the `reasoningEngines.memories.patch` method has been updated to clarify that `scope` and `memory_type` are immutable fields.

**Tags:** `Vertex AI` `Machine Learning` `Grounding` `Storage` `Exa.ai`
