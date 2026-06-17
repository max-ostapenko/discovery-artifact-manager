---
date: 2026-06-17
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks"
impact: medium
breaking: false
tags: ["AI", "Generative AI", "Grounding", "Infrastructure"]
interesting_score: 8
---

# Vertex AI: Veo Video Looping, Exa.ai Grounding, and Hyperdisks

**Date:** 2026-06-17  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI (increasingly branded as 'Agent Platform' in docs) adds advanced video generation controls, Exa.ai search grounding, and high-performance Hyperdisk support.

## Details

The video generation suite (Veo) receives significant updates with the new `CloudAiLargeModelsVisionSeamless` schema, enabling temporal looping and spatial tessellation (horizontal/vertical). Developers can now also use the `ExaAiSearch` tool for grounding model responses via Exa.ai. For agentic workflows, `ToolComputerUse` now includes a `enablePromptInjectionDetection` toggle and specific environment enums for mobile and desktop. On the infrastructure side, `PersistentDiskSpec` has been expanded to support several Hyperdisk variants, including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Generative AI` `Grounding` `Infrastructure`
