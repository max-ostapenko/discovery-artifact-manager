---
date: 2026-06-11
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agent APIs"
impact: high
breaking: true
tags: ["AI", "Agents", "Governance", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agent APIs

**Date:** 2026-06-11  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework and includes several breaking changes to Agent tools, skill creation, and response formats.

## Details

Vertex AI has introduced the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing for structured policy management within specific locations. Significant changes were made to the Agent Platform surface: the `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `skillId` parameter in `skills.create` is now required rather than optional. Additionally, the API is transitioning terminology from 'Vertex AI' to 'Agent Platform' in several resource descriptions.

Breaking changes include the renaming of enum values in `AudioResponseFormat` and `ImageResponseFormat` from `URL` to `URI`. The `interactions.delete` method has also been moved under the project/location hierarchy, and several long-running operation methods for the governance engine were refactored.

**Tags:** `AI` `Agents` `Governance` `Breaking Change`
