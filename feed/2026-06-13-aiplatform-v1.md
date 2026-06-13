---
date: 2026-06-13
api: aiplatform.v1
service: Vertex AI
title: "Exa.ai Grounding and Advanced Veo Video Generation"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Video", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Exa.ai Grounding and Advanced Veo Video Generation

**Date:** 2026-06-13  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai search grounding, seamless video looping for Veo, and expanded Hyperdisk support while deprecating Google Maps widgets.

## Details

Developers can now use the new `ExaAiSearch` tool for RAG workflows and access experimental Veo features like `seamless` (looping/tessellation) and `anchorLastFrame` for video generation. The `ToolComputerUse` schema adds prompt injection detection and specific environment flags for mobile and desktop. Infrastructure-wise, `PersistentDiskSpec` now supports Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. Note that the Google Maps widget context token is now deprecated and slated for removal. Additionally, documentation is shifting terminology from 'Vertex AI' to 'Agent Platform' across several resource schemas, signaling a broader strategic shift.

**Tags:** `AI` `Generative AI` `Video` `Grounding` `Infrastructure`
