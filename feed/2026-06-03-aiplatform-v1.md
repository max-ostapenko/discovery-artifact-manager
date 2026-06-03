---
date: 2026-06-03
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Grounding and Hyperdisk Support"
impact: medium
breaking: false
tags: ["Vertex AI", "Machine Learning", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Grounding and Hyperdisk Support

**Date:** 2026-06-03  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI now supports Exa.ai for search-based grounding and introduces high-performance Hyperdisk options for persistent storage.

## Details

The addition of GoogleCloudAiplatformV1ToolExaAiSearch allows models to use Exa.ai for real-time information retrieval, featuring API key management and custom configuration passthrough. On the infrastructure side, PersistentDiskSpec has been expanded to support Hyperdisk types including hyperdisk-ml, hyperdisk-extreme, and hyperdisk-throughput. Additionally, video generation experiments now capture the originalRequestJson to aid in request reproduction, and new metadata has been added for ServingProfile creation operations.

**Tags:** `Vertex AI` `Machine Learning` `Grounding` `Infrastructure`
