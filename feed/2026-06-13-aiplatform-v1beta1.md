---
date: 2026-06-13
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agent tools"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agent tools

**Date:** 2026-06-13  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and makes several breaking changes to Agent tool definitions and response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, allowing for structured policy management within the AI platform. Several breaking changes are included: the `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `AudioResponseFormat` and `ImageResponseFormat` enums have changed the value `URL` to `URI`. Additionally, `skillId` is now a required parameter for the `skills.create` method. The API also shows a terminology shift in documentation from 'Vertex AI' to 'Agent Platform' for certain resource descriptions.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
