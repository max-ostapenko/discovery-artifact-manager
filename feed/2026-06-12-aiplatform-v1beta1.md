---
date: 2026-06-12
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance Engine and Agent Tool Refactors"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance Engine and Agent Tool Refactors

**Date:** 2026-06-12  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance framework and applies several breaking changes to Agent tools, response formats, and resource paths.

## Details

A new singleton resource, `SemanticGovernancePolicyEngine`, has been added with `get` and `update` (upsert) methods, alongside a `SemanticGovernancePolicies` resource for managing AI guardrails. Developers using the Agent Platform should note several breaking changes: the `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `skillId` parameter is now required when creating skills. Additionally, `AudioResponseFormat` and `ImageResponseFormat` have changed their delivery enum values from `URL` to `URI`. The `interactions.delete` method has also been moved from the top-level to a location-scoped path.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Breaking Change`
