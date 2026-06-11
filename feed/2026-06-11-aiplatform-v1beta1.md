---
date: 2026-06-11
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives alongside breaking Agent changes"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 9
---

# Semantic Governance arrives alongside breaking Agent changes

**Date:** 2026-06-11  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance framework for policy management while implementing several breaking changes to Agents, Skills, and media response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies`, enabling structured governance over AI interactions. However, developers should note several breaking changes: the `skillId` parameter in `Skills.create` is now required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the `AudioResponseFormat` and `ImageResponseFormat` schemas have changed their delivery enum values from `URL` to `URI`. The `Agents.list` method also sees a significant default behavior change, with the default `pageSize` dropping from 100 to 10.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
