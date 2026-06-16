---
date: 2026-06-16
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Veo video looping"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video Generation", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Veo video looping

**Date:** 2026-06-16  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding, advanced video generation controls for Veo, and Hyperdisk support for persistent storage.

## Details

The API adds `exaAiSearch` to the `Tool` resource, allowing models to ground responses using Exa.ai. Video generation experiments (Veo) receive significant updates, including a `seamless` object for temporal looping and spatial tessellation, plus support for the `VIDEO_CODEC_DNXHR` codec. The 'Computer Use' toolset now includes `enablePromptInjectionDetection` and specific environment targets for mobile and desktop. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`). Note that the Google Maps contextual widget fields are now deprecated and slated for removal.

**Tags:** `AI` `Generative AI` `Video Generation` `Grounding` `Infrastructure`
