---
date: 2026-05-31
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai Search Tool and Hyperdisk Support"
impact: medium
breaking: false
tags: ["Vertex AI", "Generative AI", "Grounding", "Infrastructure"]
interesting_score: 7
---

# Vertex AI adds Exa.ai Search Tool and Hyperdisk Support

**Date:** 2026-05-31  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces Exa.ai as a grounding tool for model responses and expands infrastructure options with Hyperdisk support for persistent storage.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, enabling models to perform searches via Exa.ai for grounded response generation; this requires an API key and supports custom configurations. Infrastructure-wise, `PersistentDiskSpec` now supports several Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-extreme`, offering higher performance for AI workloads. Additionally, video generation experiments now include an `originalRequestJson` field to facilitate request reproduction, and new metadata has been added for `CreateServingProfile` operations.

**Tags:** `Vertex AI` `Generative AI` `Grounding` `Infrastructure`
