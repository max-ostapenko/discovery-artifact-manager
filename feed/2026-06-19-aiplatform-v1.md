---
date: 2026-06-19
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Operations and GenerationConfig Deprecations"
impact: medium
breaking: false
tags: ["generative-ai", "storage", "deprecation"]
interesting_score: 7
---

# Online Evaluator Operations and GenerationConfig Deprecations

**Date:** 2026-06-19  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces management for online evaluation operations and expands storage options with Hyperdisk support, while deprecating several core fields in GenerationConfig and Google Maps grounding.

## Details

A new resource `onlineEvaluators.operations` has been added, providing standard LRO methods (get, list, cancel, delete) for tracking evaluation tasks. In a significant schema shift, `GenerationConfig` has deprecated `responseMimeType`, `responseSchema`, and `responseJsonSchema` in favor of a unified `response_format` field. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and the Google Maps grounding widget context tokens are being phased out. Interestingly, documentation strings are being updated to refer to 'Agent Platform' in place of 'Vertex AI' for resource management descriptions.

**Tags:** `generative-ai` `storage` `deprecation`
