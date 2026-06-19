---
date: 2026-06-19
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Semantic Governance and Breaking Agent Changes"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 9
---

# Vertex AI Beta: Semantic Governance and Breaking Agent Changes

**Date:** 2026-06-19  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 API introduces Semantic Governance and Anomaly Detection while enforcing significant breaking changes to Agent schemas and interaction parameters.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI governance policies, and `AgentAnomalyDetectionScopes` for monitoring agentic workflows. Developers should be wary of several breaking changes: the `interactions.delete` method has been removed, and interaction parameters have shifted from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and response formats for audio/image now use the `URI` enum value instead of `URL`. Many internal schema references were also renamed from `Genai*` to `GenaiVertexV1beta1*` to improve namespacing.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Breaking Change`
