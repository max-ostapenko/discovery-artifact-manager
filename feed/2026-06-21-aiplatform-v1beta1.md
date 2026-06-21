---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Governance and Breaking Parameter Renames"
impact: high
breaking: true
tags: ["AI", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Agent Governance and Breaking Parameter Renames

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Significant updates to the Vertex AI v1beta1 API include new governance tools for agents and several breaking changes to parameter naming and resource methods.

## Details

This update introduces several breaking changes: the `interactions.delete` method has been removed, and parameters in `interactions.getPoll` and `getStream` have shifted from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and delivery enums for audio/image formats changed from `URL` to `URI`. On the feature side, new resources for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` have been added to support better oversight of agentic workflows. Many internal schema references were also namespaced (e.g., `GenaiStruct` is now `GenaiVertexV1beta1Struct`).

**Tags:** `AI` `Agents` `Breaking Change`
