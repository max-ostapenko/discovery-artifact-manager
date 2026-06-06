---
date: 2026-06-06
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Refines Agent Platform"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 9
---

# Vertex AI adds Semantic Governance and Refines Agent Platform

**Date:** 2026-06-06  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance Policy Engine and makes several breaking changes to the Agent and Skill APIs, including required fields and enum renames.

## Details

Vertex AI is introducing a robust governance layer with the new `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing for structured AI policy management. The 'Agent' ecosystem is also being refined, with the API documentation pivoting toward 'Agent Platform' branding and the `AgentTool` type `mcp` being renamed to `mcp_server`. Additionally, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types (balanced, extreme, throughput, etc.).

Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required rather than optional. In `AudioResponseFormat` and `ImageResponseFormat`, the delivery enum value `URL` has been changed to `URI`. Furthermore, the `interactions.delete` method has been moved under the location-based resource hierarchy, and several long-running operation methods for the governance engine have been restructured.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
