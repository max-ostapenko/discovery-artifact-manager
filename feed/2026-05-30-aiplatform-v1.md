---
date: 2026-05-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Machine Learning", "Grounding", "Storage", "Vertex AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-05-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new grounding tool for Exa.ai search and expands storage options to include several Hyperdisk types.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, enabling models to be grounded on Exa.ai search results via a required `apiKey` and optional `customConfigs`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-extreme`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in `CloudAiLargeModelsVisionGenerateVideoExperiments` allows developers to capture and reproduce the exact REST request used for video generation artifacts.

**Tags:** `AI` `Machine Learning` `Grounding` `Storage` `Vertex AI`
