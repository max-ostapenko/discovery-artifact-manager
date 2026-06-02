---
date: 2026-06-02
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["Vertex AI", "LLM", "Grounding", "Storage", "Machine Learning"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-02  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces native Exa.ai search integration for model grounding and expands storage options with high-performance Hyperdisk types.

## Details

The API now includes a native tool for Exa.ai search (`GoogleCloudAiplatformV1Tool.exaAiSearch`), enabling models to retrieve and ground responses using Exa's search engine. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk variants, including `hyperdisk-balanced`, `hyperdisk-extreme`, and `hyperdisk-ml`, providing more performance tiers for ML workloads. Additionally, video generation experiments now include an `originalRequestJson` field to aid in request reproduction, and sandbox environments gain more granular resource request/limit controls.

**Tags:** `Vertex AI` `LLM` `Grounding` `Storage` `Machine Learning`
