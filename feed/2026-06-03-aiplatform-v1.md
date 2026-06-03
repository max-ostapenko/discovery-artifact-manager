---
date: 2026-06-03
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Exa.ai grounding and Hyperdisk support"
impact: medium
breaking: false
tags: ["Vertex AI", "Machine Learning", "Grounding", "Infrastructure", "Generative AI"]
interesting_score: 7
---

# Vertex AI adds Exa.ai grounding and Hyperdisk support

**Date:** 2026-06-03  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI expands its toolset with Exa.ai search grounding and introduces support for high-performance Hyperdisk types in persistent disk specs.

## Details

The `GoogleCloudAiplatformV1Tool` schema now includes `exaAiSearch`, allowing models to use Exa.ai for grounded responses by providing an API key and optional custom configurations. On the infrastructure side, `PersistentDiskSpec` has been updated to support several Hyperdisk variants, including `hyperdisk-ml` and `hyperdisk-extreme`, which are critical for I/O-intensive machine learning workloads. Additionally, video generation experiments now include an `originalRequestJson` field to facilitate request reproduction, and sandbox environments gained more granular resource request/limit controls.

**Tags:** `Vertex AI` `Machine Learning` `Grounding` `Infrastructure` `Generative AI`
