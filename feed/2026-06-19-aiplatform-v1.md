---
date: 2026-06-19
api: aiplatform.v1
service: Vertex AI
title: "Structured Output Refactor and Online Evaluator Operations"
impact: medium
breaking: false
tags: ["generative-ai", "vertex-ai", "deprecations", "infrastructure"]
interesting_score: 7
---

# Structured Output Refactor and Online Evaluator Operations

**Date:** 2026-06-19  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI is consolidating structured output settings into a single field while adding standard operation management for Online Evaluators and support for Hyperdisk storage.

## Details

A significant cleanup is happening in GenerationConfig: responseMimeType, responseSchema, and responseJsonSchema are now deprecated in favor of a unified response_format field. Developers using Gemini for structured JSON output should plan to migrate. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types (including hyperdisk-ml and hyperdisk-balanced), and Online Evaluators have gained a full suite of LRO management methods (get, list, cancel, delete) for tracking evaluation tasks. Note that Google Maps grounding widgets are also being deprecated.

**Tags:** `generative-ai` `vertex-ai` `deprecations` `infrastructure`
