---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and New Governance"
impact: high
breaking: true
tags: ["agents", "genai", "breaking-change"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes to Agents and New Governance

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for Agents while implementing several breaking changes, including parameter renames and making skillId required.

## Details

Vertex AI has introduced the `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` resources for better control over agentic workflows. However, several breaking changes were introduced: the `interactions.delete` method was removed, and parameters for `getPoll` and `getStream` were renamed from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Additionally, `skillId` is now a required parameter in `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Developers should also note that `AudioResponseFormat` and `ImageResponseFormat` now use `URI` instead of `URL` in their delivery enums.

**Tags:** `agents` `genai` `breaking-change`
