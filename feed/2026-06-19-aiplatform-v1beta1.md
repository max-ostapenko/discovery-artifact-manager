---
date: 2026-06-19
api: aiplatform.v1beta1
service: Vertex AI
title: "Breaking Changes to Agents and Interaction APIs"
impact: high
breaking: true
tags: ["AI", "Agents", "Breaking Change"]
interesting_score: 8
---

# Breaking Changes to Agents and Interaction APIs

**Date:** 2026-06-19  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A significant update to the v1beta1 surface introduces new governance resources while applying breaking changes to parameter naming, tool types, and method availability.

## Details

The Interactions API sees several breaking changes: the `delete` method has been removed, and parameters `include_input` and `last_event_id` have been renamed to camelCase (`includeInput`, `lastEventId`). In the Agents surface, `AgentTool` types have shifted from `mcp` to `mcp_server`, and `skillId` is now a required parameter for skill creation. New resources include the `SemanticGovernancePolicyEngine` (a singleton for policy management) and `AgentAnomalyDetectionScope` for monitoring agent behavior. Additionally, many internal schema references were namespaced (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`) and media delivery enums changed from `URL` to `URI`.

**Tags:** `AI` `Agents` `Breaking Change`
