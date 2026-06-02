---
date: 2026-06-02
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["AI", "Grounding", "Infrastructure", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-02  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces native Exa.ai search integration for model grounding and expands infrastructure options with high-performance Hyperdisk support.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, enabling developers to ground model responses using the Exa.ai search engine by providing an API key and optional custom configurations. On the infrastructure side, `PersistentDiskSpec` has been updated to support various Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-throughput`, and `hyperdisk-balanced-high-availability`. Additionally, a new `originalRequestJson` field in video generation experiments allows for better reproducibility by preserving the exact REST request sent to the API.

**Tags:** `AI` `Grounding` `Infrastructure` `Generative AI`
