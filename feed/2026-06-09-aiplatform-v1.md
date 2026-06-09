---
date: 2026-06-09
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Video Generation Features"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Grounding", "Video Generation", "Infrastructure"]
interesting_score: 7
---

# Exa.ai Grounding and Advanced Video Generation Features

**Date:** 2026-06-09  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search as a grounding tool, expands video generation capabilities with looping and tessellation, and adds Hyperdisk support.

## Details

This update introduces the `exaAiSearch` tool, allowing models to be grounded using Exa.ai search results via a required `apiKey`. The video generation experimental schema (`CloudAiLargeModelsVisionGenerateVideoExperiments`) sees significant expansion, adding `seamless` parameters for temporal looping and spatial tessellation, an `anchorLastFrame` option, and support for the `VIDEO_CODEC_DNXHR` codec. Additionally, `PersistentDiskSpec` now supports multiple Hyperdisk types (ML, Throughput, Extreme), and documentation across several resources has been updated to reflect a shift in terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Generative AI` `Grounding` `Video Generation` `Infrastructure`
