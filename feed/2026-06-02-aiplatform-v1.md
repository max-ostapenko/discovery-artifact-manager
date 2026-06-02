---
date: 2026-06-02
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["Vertex AI", "Grounding", "Infrastructure", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk support

**Date:** 2026-06-02  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its grounding capabilities with Exa.ai search integration and introduces support for high-performance Hyperdisk types in persistent disk specifications.

## Details

Developers can now use Exa.ai as a grounding tool via the new `exaAiSearch` property in `GoogleCloudAiplatformV1Tool`, which requires an API key and supports custom configurations. On the infrastructure side, `GoogleCloudAiplatformV1PersistentDiskSpec` has been updated to support several Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`, specifically designed for high-performance ML workloads. Additionally, experimental video generation now captures `originalRequestJson` for better reproducibility, and sandbox environments gain explicit resource request/limit controls.

**Tags:** `Vertex AI` `Grounding` `Infrastructure` `Generative AI`
