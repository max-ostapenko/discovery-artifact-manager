---
date: 2026-05-29
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Storage", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-05-29  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a grounding tool for LLMs and expands storage options with several new Hyperdisk types.

## Details

Developers can now use Exa.ai for search-based grounding by adding the `exaAiSearch` tool to their model requests, which includes support for custom configurations and API key management. On the infrastructure side, `PersistentDiskSpec` has been expanded to support various Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments helps with reproducibility by preserving the exact REST request sent to the API.

**Tags:** `AI` `Grounding` `Storage` `Generative AI`
