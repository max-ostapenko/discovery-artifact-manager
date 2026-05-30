---
date: 2026-05-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["Vertex AI", "Generative AI", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk support

**Date:** 2026-05-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new Exa.ai search tool for model grounding and expands infrastructure options with several Hyperdisk types.

## Details

The most significant update is the addition of `GoogleCloudAiplatformV1ToolExaAiSearch`, allowing developers to use Exa.ai as a grounding source for model responses by providing an `apiKey`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support Hyperdisk types including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments helps with reproducibility by preserving the exact REST request sent to the API.

**Tags:** `Vertex AI` `Generative AI` `Grounding` `Infrastructure`
