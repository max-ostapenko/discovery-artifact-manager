---
date: 2026-06-18
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI: Online Evaluator Ops and Major Deprecations"
impact: medium
breaking: false
tags: ["AI", "Gemini", "Deprecation", "Storage"]
interesting_score: 7
---

# Vertex AI: Online Evaluator Ops and Major Deprecations

**Date:** 2026-06-18  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces lifecycle management for Online Evaluator operations and marks several core GenerationConfig fields as deprecated in favor of a unified response_format.

## Details

This update adds a full suite of operation management methods (get, list, cancel, delete) under the `onlineEvaluators` resource, allowing better control over long-running evaluation tasks. Significant deprecations have been applied to `GenerationConfig`: the fields `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated, with developers directed to use the new `response_format` field instead. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and Google Maps grounding widget tokens are being phased out. Notably, documentation strings are shifting terminology from 'Vertex AI' to 'Agent Platform' in several resource descriptions.

**Tags:** `AI` `Gemini` `Deprecation` `Storage`
