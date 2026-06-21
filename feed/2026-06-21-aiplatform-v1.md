---
date: 2026-06-21
api: aiplatform.v1
service: Vertex AI
title: "Online Evaluator Ops and Hyperdisk Support"
impact: medium
breaking: false
tags: ["generative-ai", "infrastructure", "deprecations"]
interesting_score: 7
---

# Online Evaluator Ops and Hyperdisk Support

**Date:** 2026-06-21  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces operation management for online evaluators and adds Hyperdisk support for ML workloads, while deprecating several generative configuration fields.

## Details

The API now includes a full suite of standard operation methods (get, list, cancel, delete) under the `onlineEvaluators` resource, allowing better management of long-running evaluation tasks. In `GenerationConfig`, several fields including `responseMimeType`, `responseSchema`, and `responseJsonSchema` are now deprecated in favor of the unified `response_format` field. Additionally, `PersistentDiskSpec` has been expanded to support various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), offering higher performance for compute-intensive AI tasks. Note that documentation descriptions are shifting terminology from 'Vertex AI' to 'Agent Platform' in several resource schemas.

**Tags:** `generative-ai` `infrastructure` `deprecations`
