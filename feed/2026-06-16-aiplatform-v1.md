---
date: 2026-06-16
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Veo video features and Exa.ai grounding"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Veo video features and Exa.ai grounding

**Date:** 2026-06-16  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduced advanced video generation controls for Veo, integrated Exa.ai for search grounding, and expanded infrastructure options with Hyperdisk support.

## Details

The video generation suite (Veo) receives significant experimental updates in CloudAiLargeModelsVisionGenerateVideoExperiments, including support for seamless looping, spatial tessellation (horizontal/vertical), and the professional VIDEO_CODEC_DNXHR codec. Developers can now use Exa.ai as a grounding tool via the new exaAiSearch field in the Tool schema. Additionally, ToolComputerUse now includes a toggle for prompt injection detection and environment-specific flags for mobile and desktop. On the infrastructure side, PersistentDiskSpec has been expanded to support high-performance Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
