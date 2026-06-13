---
date: 2026-06-13
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Features"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation Features

**Date:** 2026-06-13  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding for models and significant enhancements to experimental video generation, including seamless looping and Hyperdisk support.

## Details

The API now includes a `GoogleCloudAiplatformV1ToolExaAiSearch` tool, enabling model grounding via the Exa.ai search engine with a required `apiKey`. Video generation capabilities (Veo) have been expanded via `CloudAiLargeModelsVisionGenerateVideoExperiments`, adding support for the `VIDEO_CODEC_DNXHR` codec and a new `seamless` configuration for temporal looping and spatial tessellation. Additionally, `PersistentDiskSpec` now supports multiple Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and documentation across several resources has been updated to reflect a shift from 'Vertex AI' to 'Agent Platform' management.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
