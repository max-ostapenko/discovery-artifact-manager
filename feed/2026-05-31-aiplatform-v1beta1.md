---
date: 2026-05-31
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives alongside multiple breaking changes"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance arrives alongside multiple breaking changes

**Date:** 2026-05-31  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine for AI oversight while implementing several breaking changes to Skills, Agent tools, and response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing for structured governance over AI assets. However, developers should note several breaking changes: `skills.create` now requires a `skillId`, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `delivery` enum in `AudioResponseFormat` and `ImageResponseFormat` has changed from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced-high-availability`.

**Tags:** `AI` `Governance` `Breaking Change`
