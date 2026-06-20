---
date: 2026-06-20
api: aiplatform.v1beta1
service: Vertex AI
title: "Breaking Changes to Agents, Skills, and Interactions"
impact: high
breaking: true
tags: ["vertex-ai", "agents", "breaking-change"]
interesting_score: 9
---

# Breaking Changes to Agents, Skills, and Interactions

**Date:** 2026-06-20  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the Vertex AI Beta API introduces several breaking changes, including parameter renames, required field updates, and the removal of the interaction delete method.

## Details

This update contains significant breaking changes for developers using the AI Agents and Interactions surface. The `interactions.delete` method has been removed entirely. In `interactions.getPoll` and `getStream`, the parameters `include_input` and `last_event_id` have been renamed to camelCase (`includeInput` and `lastEventId`). Furthermore, `skillId` is now a **required** parameter in `skills.create` (previously optional), and the `AgentTool` type `mcp` has been renamed to `mcp_server`. 

On the feature side, a new `SemanticGovernancePolicyEngine` singleton resource has been added for policy management, alongside `AgentAnomalyDetectionScope` for monitoring agent behavior. Many internal schemas have also been namespaced (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`), and `URL` enums in audio/image formats have been changed to `URI`.

**Tags:** `vertex-ai` `agents` `breaking-change`
