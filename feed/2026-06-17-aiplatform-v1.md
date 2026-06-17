---
date: 2026-06-17
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video looping and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video looping and Exa.ai grounding

**Date:** 2026-06-17  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces advanced video generation controls for Veo, third-party search grounding via Exa.ai, and enhanced security for 'Computer Use' tools.

## Details

The video generation schema (CloudAiLargeModelsVisionGenerateVideoExperiments) now supports seamless looping, spatial tessellation, and the DNxHR codec. A new ExaAiSearch tool has been added to the Tool resource, allowing models to ground responses using Exa.ai search results. Additionally, the 'Computer Use' tool now includes a prompt injection detection toggle and environment-specific enums for mobile and desktop. Infrastructure-wise, PersistentDiskSpec has been expanded to support several Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
