---
date: 2026-06-18
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and Interactions"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes to Agents and Interactions

**Date:** 2026-06-18  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection while applying several breaking changes to the Agents and Interactions APIs, including parameter renames and field requirement updates.

## Details

Several breaking changes have been introduced in this revision. The `interactions.delete` method has been removed entirely. In the `interactions.getPoll` and `getStream` methods, parameters have been renamed from snake_case to camelCase (e.g., `include_input` to `includeInput` and `last_event_id` to `lastEventId`). Additionally, `skillId` is now a required parameter for `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. On the feature side, new resources for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` have been added to support better agent oversight. Many internal schema references were also namespaced from `Genai*` to `GenaiVertexV1beta1*`.

**Tags:** `AI` `Vertex AI` `Agents` `Breaking Change`
